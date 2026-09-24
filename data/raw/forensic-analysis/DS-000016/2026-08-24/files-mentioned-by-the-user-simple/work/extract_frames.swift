import Foundation
import AVFoundation
import ImageIO
import UniformTypeIdentifiers

guard CommandLine.arguments.count >= 4 else {
    fputs("Usage: extract_frames.swift VIDEO OUTPUT_DIR TIMES_FILE\n", stderr)
    exit(2)
}

let videoURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
let timeSpec = CommandLine.arguments[3]
try FileManager.default.createDirectory(at: outputURL, withIntermediateDirectories: true)

let asset = AVURLAsset(url: videoURL)
let times: [Double]
if timeSpec.hasPrefix("interval:") {
    let intervalText = String(timeSpec.dropFirst("interval:".count))
    guard let interval = Double(intervalText), interval > 0 else {
        fputs("Invalid interval specification\n", stderr)
        exit(2)
    }
    let duration = CMTimeGetSeconds(asset.duration)
    times = stride(from: 0.0, through: max(0.0, duration - 0.001), by: interval).map { $0 }
} else {
    let text = try String(contentsOfFile: timeSpec, encoding: .utf8)
    times = text.split(whereSeparator: { $0.isWhitespace }).compactMap { Double($0) }
}

let generator = AVAssetImageGenerator(asset: asset)
generator.appliesPreferredTrackTransform = true
generator.requestedTimeToleranceBefore = .zero
generator.requestedTimeToleranceAfter = .zero
generator.maximumSize = CGSize(width: 1280, height: 720)

var manifest: [[String: Any]] = []
for seconds in times {
    let requested = CMTime(seconds: seconds, preferredTimescale: 60000)
    var actual = CMTime.zero
    do {
        let image = try generator.copyCGImage(at: requested, actualTime: &actual)
        let actualSeconds = CMTimeGetSeconds(actual)
        let millis = Int((seconds * 1000).rounded())
        let filename = String(format: "frame_%09d.jpg", millis)
        let destinationURL = outputURL.appendingPathComponent(filename)
        guard let destination = CGImageDestinationCreateWithURL(destinationURL as CFURL, UTType.jpeg.identifier as CFString, 1, nil) else {
            throw NSError(domain: "FrameWriter", code: 1, userInfo: [NSLocalizedDescriptionKey: "Could not create image destination"])
        }
        let options = [kCGImageDestinationLossyCompressionQuality: 0.92] as CFDictionary
        CGImageDestinationAddImage(destination, image, options)
        guard CGImageDestinationFinalize(destination) else {
            throw NSError(domain: "FrameWriter", code: 2, userInfo: [NSLocalizedDescriptionKey: "Could not finalize image"])
        }
        manifest.append([
            "requested_seconds": seconds,
            "actual_seconds": actualSeconds,
            "file": filename,
            "width": image.width,
            "height": image.height
        ])
    } catch {
        manifest.append([
            "requested_seconds": seconds,
            "error": String(describing: error)
        ])
    }
}

let manifestData = try JSONSerialization.data(withJSONObject: manifest, options: [.prettyPrinted, .sortedKeys])
try manifestData.write(to: outputURL.appendingPathComponent("manifest.json"))
let extractedCount = manifest.filter { $0["file"] != nil }.count
print("Extracted \(extractedCount) / \(times.count) frames to \(outputURL.path)")
