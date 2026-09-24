import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count == 3 else {
    fputs("usage: ocr_selected <frames_dir> <output.tsv>\n", stderr)
    exit(2)
}

let framesDir = URL(fileURLWithPath: CommandLine.arguments[1], isDirectory: true)
let output = URL(fileURLWithPath: CommandLine.arguments[2])
let files = try FileManager.default.contentsOfDirectory(at: framesDir, includingPropertiesForKeys: nil)
    .filter { $0.pathExtension.lowercased() == "jpg" }
    .sorted { $0.lastPathComponent < $1.lastPathComponent }
let regex = try NSRegularExpression(pattern: #"(V\d+)_(\d+)ms"#)
var lines = ["visual\ttime\tconfidence\tx\ty\twidth\theight\ttext"]

for file in files {
    autoreleasepool {
        guard let image = NSImage(contentsOf: file),
              let tiff = image.tiffRepresentation,
              let bitmap = NSBitmapImageRep(data: tiff),
              let cgImage = bitmap.cgImage else { return }
        let name = file.lastPathComponent as NSString
        let match = regex.firstMatch(in: name as String, range: NSRange(location: 0, length: name.length))
        let visual = match.map { name.substring(with: $0.range(at: 1)) } ?? "V00"
        let milliseconds = match.map { name.substring(with: $0.range(at: 2)) } ?? "0"
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["en-US"]
        do {
            try VNImageRequestHandler(cgImage: cgImage, options: [:]).perform([request])
            for observation in request.results ?? [] {
                guard let candidate = observation.topCandidates(1).first else { continue }
                let text = candidate.string.replacingOccurrences(of: "\t", with: " ").replacingOccurrences(of: "\n", with: " ")
                let box = observation.boundingBox
                lines.append(String(format: "%@\t%.3f\t%.3f\t%.4f\t%.4f\t%.4f\t%.4f\t%@", visual, (Double(milliseconds) ?? 0) / 1000.0, candidate.confidence, box.origin.x, box.origin.y, box.width, box.height, text))
            }
        } catch {
            fputs("OCR failed for \(file.lastPathComponent): \(error)\n", stderr)
        }
    }
}

try (lines.joined(separator: "\n") + "\n").write(to: output, atomically: true, encoding: .utf8)
print("ocr_lines\t\(lines.count - 1)")
