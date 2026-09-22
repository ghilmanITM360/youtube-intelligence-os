import Foundation
import Speech

guard CommandLine.arguments.count >= 3 else {
    fputs("usage: transcribe_speech <audio> <output.tsv> [locale]\n", stderr)
    exit(2)
}

let audioURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2])
let locale = Locale(identifier: CommandLine.arguments.count > 3 ? CommandLine.arguments[3] : "en-US")
let authSemaphore = DispatchSemaphore(value: 0)
var authStatus = SFSpeechRecognizerAuthorizationStatus.notDetermined
SFSpeechRecognizer.requestAuthorization { status in
    authStatus = status
    authSemaphore.signal()
}

if authSemaphore.wait(timeout: .now() + 30) == .timedOut {
    fputs("authorization timed out\n", stderr)
    exit(1)
}
guard authStatus == .authorized else {
    fputs("speech authorization status: \(authStatus.rawValue)\n", stderr)
    exit(1)
}
guard let recognizer = SFSpeechRecognizer(locale: locale) else {
    fputs("recognizer unavailable for \(locale.identifier)\n", stderr)
    exit(1)
}

let request = SFSpeechURLRecognitionRequest(url: audioURL)
request.shouldReportPartialResults = false
request.taskHint = .dictation
if recognizer.supportsOnDeviceRecognition {
    request.requiresOnDeviceRecognition = true
}

let done = DispatchSemaphore(value: 0)
var finalResult: SFSpeechRecognitionResult?
var finalError: Error?
let task = recognizer.recognitionTask(with: request) { result, error in
    if let result = result {
        finalResult = result
        if result.isFinal { done.signal() }
    }
    if let error = error {
        finalError = error
        done.signal()
    }
}

if done.wait(timeout: .now() + 300) == .timedOut {
    task.cancel()
    fputs("recognition timed out\n", stderr)
    exit(1)
}
if let error = finalError, finalResult == nil {
    fputs("recognition error: \(error)\n", stderr)
    exit(1)
}
guard let transcription = finalResult?.bestTranscription else {
    fputs("no transcription result\n", stderr)
    exit(1)
}

var lines = ["start\tduration\tconfidence\ttext"]
for segment in transcription.segments {
    let token = segment.substring.replacingOccurrences(of: "\t", with: " ").replacingOccurrences(of: "\n", with: " ")
    lines.append(String(format: "%.3f\t%.3f\t%.3f\t%@", segment.timestamp, segment.duration, segment.confidence, token))
}
try (lines.joined(separator: "\n") + "\n").write(to: outputURL, atomically: true, encoding: .utf8)
print("segments\t\(transcription.segments.count)")
print("text\t\(transcription.formattedString)")
