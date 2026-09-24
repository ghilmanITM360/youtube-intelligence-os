import Foundation
import AVFoundation
import CoreMedia

func fourCC(_ value: FourCharCode) -> String {
    let n = UInt32(value)
    let chars: [UInt8] = [
        UInt8((n >> 24) & 0xff),
        UInt8((n >> 16) & 0xff),
        UInt8((n >> 8) & 0xff),
        UInt8(n & 0xff)
    ]
    return String(bytes: chars, encoding: .ascii) ?? String(value)
}

guard CommandLine.arguments.count >= 2 else {
    fputs("Usage: analyze_video.swift VIDEO\n", stderr)
    exit(2)
}

let url = URL(fileURLWithPath: CommandLine.arguments[1])
let asset = AVURLAsset(url: url)
let duration = CMTimeGetSeconds(asset.duration)
let videoTracks = asset.tracks(withMediaType: .video)
let audioTracks = asset.tracks(withMediaType: .audio)

var output: [String: Any] = [
    "duration_seconds": duration,
    "video_track_count": videoTracks.count,
    "audio_track_count": audioTracks.count,
    "file_size_bytes": (try? FileManager.default.attributesOfItem(atPath: url.path)[.size]) ?? 0
]

if let track = videoTracks.first {
    let transformed = track.naturalSize.applying(track.preferredTransform)
    output["display_width"] = abs(transformed.width)
    output["display_height"] = abs(transformed.height)
    output["natural_width"] = track.naturalSize.width
    output["natural_height"] = track.naturalSize.height
    output["nominal_fps"] = track.nominalFrameRate
    output["estimated_data_rate"] = track.estimatedDataRate
    output["preferred_transform"] = [
        track.preferredTransform.a,
        track.preferredTransform.b,
        track.preferredTransform.c,
        track.preferredTransform.d,
        track.preferredTransform.tx,
        track.preferredTransform.ty
    ]
    if let anyDesc = track.formatDescriptions.first {
        let desc = anyDesc as! CMFormatDescription
        output["video_codec"] = fourCC(CMFormatDescriptionGetMediaSubType(desc))
    }
}

if let track = audioTracks.first {
    output["audio_estimated_data_rate"] = track.estimatedDataRate
    if let anyDesc = track.formatDescriptions.first {
        let desc = anyDesc as! CMAudioFormatDescription
        output["audio_codec"] = fourCC(CMFormatDescriptionGetMediaSubType(desc))
        if let asbd = CMAudioFormatDescriptionGetStreamBasicDescription(desc)?.pointee {
            output["audio_sample_rate"] = asbd.mSampleRate
            output["audio_channels"] = asbd.mChannelsPerFrame
        }
    }
}

let data = try JSONSerialization.data(withJSONObject: output, options: [.prettyPrinted, .sortedKeys])
print(String(decoding: data, as: UTF8.self))
