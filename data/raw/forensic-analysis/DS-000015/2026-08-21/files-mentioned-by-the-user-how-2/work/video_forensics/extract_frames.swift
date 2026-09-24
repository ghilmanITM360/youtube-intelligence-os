import Foundation
import AVFoundation
import AppKit

guard CommandLine.arguments.count >= 6 else {
    fputs("usage: extract_frames <video> <outdir> <interval_seconds> <max_width> <max_height>\n", stderr)
    exit(2)
}

let source = URL(fileURLWithPath: CommandLine.arguments[1])
let outdir = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
let interval = Double(CommandLine.arguments[3]) ?? 1.0
let maxWidth = Double(CommandLine.arguments[4]) ?? 180.0
let maxHeight = Double(CommandLine.arguments[5]) ?? 320.0

try FileManager.default.createDirectory(at: outdir, withIntermediateDirectories: true)
let asset = AVURLAsset(url: source)
let duration = CMTimeGetSeconds(asset.duration)
let generator = AVAssetImageGenerator(asset: asset)
generator.appliesPreferredTrackTransform = true
generator.requestedTimeToleranceBefore = .zero
generator.requestedTimeToleranceAfter = .zero
generator.maximumSize = CGSize(width: maxWidth, height: maxHeight)

let manifest = outdir.appendingPathComponent("manifest.tsv")
FileManager.default.createFile(atPath: manifest.path, contents: nil)
let handle = try FileHandle(forWritingTo: manifest)
defer { try? handle.close() }
try handle.write(contentsOf: Data("requested_seconds\tactual_seconds\tfilename\n".utf8))

var t = 0.0
var count = 0
while t < duration {
    autoreleasepool {
        do {
            let request = CMTime(seconds: t, preferredTimescale: 60000)
            var actual = CMTime.zero
            let cg = try generator.copyCGImage(at: request, actualTime: &actual)
            let image = NSImage(cgImage: cg, size: NSSize(width: cg.width, height: cg.height))
            guard let tiff = image.tiffRepresentation,
                  let bitmap = NSBitmapImageRep(data: tiff),
                  let jpg = bitmap.representation(using: .jpeg, properties: [.compressionFactor: 0.84]) else {
                throw NSError(domain: "extract_frames", code: 1)
            }
            let ms = Int((t * 1000.0).rounded())
            let name = String(format: "frame_%07dms.jpg", ms)
            try jpg.write(to: outdir.appendingPathComponent(name))
            let line = String(format: "%.6f\t%.6f\t%@\n", t, CMTimeGetSeconds(actual), name)
            try handle.write(contentsOf: Data(line.utf8))
            count += 1
            if count % 50 == 0 { fputs("extracted \(count) frames\n", stderr) }
        } catch {
            fputs(String(format: "failed at %.3f: %@\n", t, String(describing: error)), stderr)
        }
    }
    t += interval
}
print("frames\t\(count)")
print(String(format: "duration_seconds\t%.6f", duration))
