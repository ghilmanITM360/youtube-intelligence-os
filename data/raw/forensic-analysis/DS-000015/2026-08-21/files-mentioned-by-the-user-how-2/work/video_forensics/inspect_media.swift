import Foundation
import AVFoundation
import CoreMedia

func fourCC(_ value: FourCharCode) -> String {
    let chars: [UInt8] = [
        UInt8((value >> 24) & 0xff),
        UInt8((value >> 16) & 0xff),
        UInt8((value >> 8) & 0xff),
        UInt8(value & 0xff)
    ]
    return String(bytes: chars, encoding: .ascii) ?? String(value)
}

guard CommandLine.arguments.count == 2 else {
    fputs("usage: inspect_media <video>\n", stderr)
    exit(2)
}

let url = URL(fileURLWithPath: CommandLine.arguments[1])
let asset = AVURLAsset(url: url)
let semaphore = DispatchSemaphore(value: 0)

Task {
    do {
        let duration = try await asset.load(.duration)
        let tracks = try await asset.load(.tracks)
        let format = try await asset.load(.availableMetadataFormats)
        print("path\t\(url.path)")
        print(String(format: "duration_seconds\t%.6f", CMTimeGetSeconds(duration)))
        print("metadata_formats\t\(format.map { $0.rawValue }.joined(separator: ","))")
        print("track_count\t\(tracks.count)")

        for (index, track) in tracks.enumerated() {
            let mediaType = track.mediaType.rawValue
            let timeRange = try await track.load(.timeRange)
            let nominalFrameRate = try await track.load(.nominalFrameRate)
            let estimatedDataRate = try await track.load(.estimatedDataRate)
            let naturalSize = try await track.load(.naturalSize)
            let transform = try await track.load(.preferredTransform)
            let descriptions = try await track.load(.formatDescriptions)
            print("track_\(index)_type\t\(mediaType)")
            print(String(format: "track_%d_duration_seconds\t%.6f", index, CMTimeGetSeconds(timeRange.duration)))
            print(String(format: "track_%d_nominal_fps\t%.6f", index, nominalFrameRate))
            print(String(format: "track_%d_estimated_bitrate\t%.0f", index, estimatedDataRate))
            print(String(format: "track_%d_natural_size\t%.0fx%.0f", index, naturalSize.width, naturalSize.height))
            print(String(format: "track_%d_transform\t[%.3f %.3f %.3f %.3f %.3f %.3f]", index, transform.a, transform.b, transform.c, transform.d, transform.tx, transform.ty))
            for (j, description) in descriptions.enumerated() {
                let basic = CMFormatDescriptionGetMediaSubType(description)
                print("track_\(index)_format_\(j)_codec\t\(fourCC(basic))")
                if let ext = CMFormatDescriptionGetExtensions(description) as? [String: Any] {
                    let clean = ext.map { key, value in "\(key)=\(value)" }.sorted().joined(separator: " | ")
                    print("track_\(index)_format_\(j)_extensions\t\(clean)")
                }
                if mediaType == AVMediaType.audio.rawValue,
                   let audio = CMAudioFormatDescriptionGetStreamBasicDescription(description)?.pointee {
                    print(String(format: "track_%d_audio_sample_rate\t%.0f", index, audio.mSampleRate))
                    print("track_\(index)_audio_channels\t\(audio.mChannelsPerFrame)")
                }
            }
        }
    } catch {
        fputs("error: \(error)\n", stderr)
        exit(1)
    }
    semaphore.signal()
}

semaphore.wait()
