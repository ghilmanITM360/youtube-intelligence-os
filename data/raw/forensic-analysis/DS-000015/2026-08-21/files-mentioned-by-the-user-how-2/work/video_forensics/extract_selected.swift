import Foundation
import AVFoundation
import AppKit

guard CommandLine.arguments.count == 4 else {
    fputs("usage: extract_selected <video> <times.tsv> <outdir>\n", stderr)
    exit(2)
}

let source = URL(fileURLWithPath: CommandLine.arguments[1])
let list = URL(fileURLWithPath: CommandLine.arguments[2])
let outdir = URL(fileURLWithPath: CommandLine.arguments[3], isDirectory: true)
try FileManager.default.createDirectory(at: outdir, withIntermediateDirectories: true)

let asset = AVURLAsset(url: source)
let generator = AVAssetImageGenerator(asset: asset)
generator.appliesPreferredTrackTransform = true
generator.requestedTimeToleranceBefore = .zero
generator.requestedTimeToleranceAfter = .zero
generator.maximumSize = CGSize(width: 720, height: 1280)

let rows = try String(contentsOf: list, encoding: .utf8).split(separator: "\n").dropFirst()
for row in rows {
    let fields = row.split(separator: "\t")
    guard fields.count == 2, let seconds = Double(fields[1]) else { continue }
    let id = String(fields[0])
    autoreleasepool {
        do {
            var actual = CMTime.zero
            let cg = try generator.copyCGImage(at: CMTime(seconds: seconds, preferredTimescale: 60000), actualTime: &actual)
            let image = NSImage(cgImage: cg, size: NSSize(width: cg.width, height: cg.height))
            guard let tiff = image.tiffRepresentation,
                  let bitmap = NSBitmapImageRep(data: tiff),
                  let jpg = bitmap.representation(using: .jpeg, properties: [.compressionFactor: 0.92]) else { return }
            let filename = String(format: "%@_%07dms.jpg", id, Int((CMTimeGetSeconds(actual) * 1000).rounded()))
            try jpg.write(to: outdir.appendingPathComponent(filename))
            print(String(format: "%@\t%.6f\t%@", id, CMTimeGetSeconds(actual), filename))
        } catch {
            fputs("failed \(id): \(error)\n", stderr)
        }
    }
}
