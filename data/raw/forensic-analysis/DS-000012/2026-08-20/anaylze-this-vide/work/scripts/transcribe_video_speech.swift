import Foundation
import Speech

let args = CommandLine.arguments
guard args.count >= 2 else {
    fputs("Usage: swift transcribe_video_speech.swift <media-file>\n", stderr)
    exit(2)
}

let mediaURL = URL(fileURLWithPath: args[1])
let locale = Locale(identifier: args.count >= 3 ? args[2] : "en_US")

let authSemaphore = DispatchSemaphore(value: 0)
var authStatus: SFSpeechRecognizerAuthorizationStatus = .notDetermined
SFSpeechRecognizer.requestAuthorization { status in
    authStatus = status
    authSemaphore.signal()
}
_ = authSemaphore.wait(timeout: .now() + 30)

guard authStatus == .authorized else {
    fputs("speech_authorization=\(authStatus.rawValue)\n", stderr)
    exit(3)
}

guard let recognizer = SFSpeechRecognizer(locale: locale) else {
    fputs("speech_recognizer_unavailable\n", stderr)
    exit(4)
}

let request = SFSpeechURLRecognitionRequest(url: mediaURL)
request.shouldReportPartialResults = false
if #available(macOS 10.15, *) {
    request.requiresOnDeviceRecognition = true
}

let done = DispatchSemaphore(value: 0)
var finalText = ""
var finalSegments: [SFTranscriptionSegment] = []
var finalError: Error?

let task = recognizer.recognitionTask(with: request) { result, error in
    if let result {
        finalText = result.bestTranscription.formattedString
        finalSegments = result.bestTranscription.segments
        if result.isFinal {
            done.signal()
        }
    }
    if let error {
        finalError = error
        done.signal()
    }
}

let waitResult = done.wait(timeout: .now() + 180)
task.cancel()

if waitResult == .timedOut {
    fputs("speech_timeout\n", stderr)
    exit(5)
}

if let finalError, finalText.isEmpty {
    fputs("speech_error=\(finalError.localizedDescription)\n", stderr)
    exit(6)
}

print("transcript=\(finalText)")
for segment in finalSegments {
    let start = String(format: "%.2f", segment.timestamp)
    let duration = String(format: "%.2f", segment.duration)
    print("segment\t\(start)\t\(duration)\t\(segment.substring)")
}

if let finalError {
    fputs("speech_warning=\(finalError.localizedDescription)\n", stderr)
}
