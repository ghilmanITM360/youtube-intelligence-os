import Foundation
import AVFoundation
import AppKit

struct StreamInfo {
    let durationSeconds: Double
    let naturalSize: CGSize
    let nominalFrameRate: Float
    let hasAudio: Bool
}

func savePNG(_ image: CGImage, to url: URL) throws {
    let rep = NSBitmapImageRep(cgImage: image)
    guard let data = rep.representation(using: .png, properties: [:]) else {
        throw NSError(domain: "extract_video_frames", code: 1, userInfo: [NSLocalizedDescriptionKey: "Could not encode PNG"])
    }
    try data.write(to: url)
}

let args = CommandLine.arguments
guard args.count >= 4 else {
    fputs("Usage: swift extract_video_frames.swift <video> <output-dir> <frame-count>\n", stderr)
    exit(2)
}

let videoURL = URL(fileURLWithPath: args[1])
let outputURL = URL(fileURLWithPath: args[2], isDirectory: true)
let frameCount = max(1, Int(args[3]) ?? 12)

let asset = AVURLAsset(url: videoURL)
let duration = CMTimeGetSeconds(asset.duration)
let videoTrack = asset.tracks(withMediaType: .video).first
let audioTrack = asset.tracks(withMediaType: .audio).first
let size = videoTrack?.naturalSize ?? .zero
let fps = videoTrack?.nominalFrameRate ?? 0

print("duration_seconds=\(String(format: "%.3f", duration))")
print("video_size=\(Int(abs(size.width)))x\(Int(abs(size.height)))")
print("nominal_fps=\(String(format: "%.3f", fps))")
print("has_audio=\(audioTrack != nil)")

let generator = AVAssetImageGenerator(asset: asset)
generator.appliesPreferredTrackTransform = true
generator.maximumSize = CGSize(width: 1280, height: 1280)
generator.requestedTimeToleranceBefore = CMTime(seconds: 0.15, preferredTimescale: 600)
generator.requestedTimeToleranceAfter = CMTime(seconds: 0.15, preferredTimescale: 600)

try FileManager.default.createDirectory(at: outputURL, withIntermediateDirectories: true)

let usableDuration = duration.isFinite && duration > 0 ? duration : 0
let times: [Double]
if frameCount == 1 {
    times = [min(0.5, usableDuration)]
} else {
    times = (0..<frameCount).map { i in
        let fraction = Double(i) / Double(frameCount - 1)
        return min(max(usableDuration * fraction, 0.0), max(usableDuration - 0.05, 0.0))
    }
}

for (index, second) in times.enumerated() {
    let requested = CMTime(seconds: second, preferredTimescale: 600)
    do {
        var actual = CMTime.zero
        let image = try generator.copyCGImage(at: requested, actualTime: &actual)
        let actualSeconds = CMTimeGetSeconds(actual)
        let name = String(format: "frame_%02d_%07.2fs.png", index + 1, actualSeconds)
        let fileURL = outputURL.appendingPathComponent(name)
        try savePNG(image, to: fileURL)
        print("frame=\(fileURL.path)\ttime_seconds=\(String(format: "%.3f", actualSeconds))")
    } catch {
        fputs("frame_error time=\(second): \(error.localizedDescription)\n", stderr)
    }
}
