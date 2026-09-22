import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count == 3 else {
    fputs("usage: ocr_frames <frames_dir> <output.tsv>\n", stderr)
    exit(2)
}

let framesDir = URL(fileURLWithPath: CommandLine.arguments[1], isDirectory: true)
let output = URL(fileURLWithPath: CommandLine.arguments[2])
let files = try FileManager.default.contentsOfDirectory(at: framesDir, includingPropertiesForKeys: nil)
    .filter { $0.pathExtension.lowercased() == "jpg" }
    .sorted { $0.lastPathComponent < $1.lastPathComponent }

let regex = try NSRegularExpression(pattern: #"frame_(\d+)ms"#)
var lines = ["time\tconfidence\tx\ty\twidth\theight\ttext"]

for (index, file) in files.enumerated() where index % 4 == 0 {
    autoreleasepool {
        guard let image = NSImage(contentsOf: file),
              let tiff = image.tiffRepresentation,
              let bitmap = NSBitmapImageRep(data: tiff),
              let cg = bitmap.cgImage else { return }
        let name = file.lastPathComponent as NSString
        let match = regex.firstMatch(in: name as String, range: NSRange(location: 0, length: name.length))
        let ms = match.map { name.substring(with: $0.range(at: 1)) } ?? "0"
        let time = (Double(ms) ?? 0) / 1000.0
        let request = VNRecognizeTextRequest()
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        request.recognitionLanguages = ["en-US"]
        do {
            try VNImageRequestHandler(cgImage: cg, options: [:]).perform([request])
            for observation in request.results ?? [] {
                guard let candidate = observation.topCandidates(1).first else { continue }
                let text = candidate.string.replacingOccurrences(of: "\t", with: " ").replacingOccurrences(of: "\n", with: " ")
                let b = observation.boundingBox
                lines.append(String(format: "%.3f\t%.3f\t%.4f\t%.4f\t%.4f\t%.4f\t%@", time, candidate.confidence, b.origin.x, b.origin.y, b.width, b.height, text))
            }
        } catch {
            fputs("OCR failed for \(file.lastPathComponent): \(error)\n", stderr)
        }
    }
}

try (lines.joined(separator: "\n") + "\n").write(to: output, atomically: true, encoding: .utf8)
print("ocr_lines\t\(lines.count - 1)")
