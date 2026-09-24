import Foundation
import AVFoundation

guard CommandLine.arguments.count == 3 else {
    fputs("usage: extract_audio <video> <output.m4a>\n", stderr)
    exit(2)
}

let source = URL(fileURLWithPath: CommandLine.arguments[1])
let output = URL(fileURLWithPath: CommandLine.arguments[2])
try? FileManager.default.removeItem(at: output)
let asset = AVURLAsset(url: source)
guard let session = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetAppleM4A) else {
    fputs("could not create export session\n", stderr)
    exit(1)
}

let semaphore = DispatchSemaphore(value: 0)
Task {
    do {
        try await session.export(to: output, as: .m4a)
        print("status\tcompleted")
        let attrs = try FileManager.default.attributesOfItem(atPath: output.path)
        print("bytes\t\(attrs[.size] ?? 0)")
    } catch {
        fputs("export error: \(error)\n", stderr)
        exit(1)
    }
    semaphore.signal()
}
semaphore.wait()
