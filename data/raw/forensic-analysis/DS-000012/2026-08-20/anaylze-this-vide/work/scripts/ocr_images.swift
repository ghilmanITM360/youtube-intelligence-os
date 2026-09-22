import Foundation
import Vision
import AppKit
import ImageIO

let args = CommandLine.arguments.dropFirst()
guard !args.isEmpty else {
    fputs("Usage: swift ocr_images.swift <image> [<image> ...]\n", stderr)
    exit(2)
}

func recognizeText(in url: URL) throws -> [String] {
    guard let source = CGImageSourceCreateWithURL(url as CFURL, nil),
          let cgImage = CGImageSourceCreateImageAtIndex(source, 0, nil) else {
        throw NSError(domain: "ocr_images", code: 1, userInfo: [NSLocalizedDescriptionKey: "Could not load image"])
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["en-US"]
    request.minimumTextHeight = 0.01

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    try handler.perform([request])

    guard let observations = request.results else {
        return []
    }

    return observations.compactMap { observation in
        observation.topCandidates(1).first?.string
    }
}

for arg in args {
    let url = URL(fileURLWithPath: arg)
    do {
        let lines = try recognizeText(in: url)
        print("FILE\t\(url.path)")
        if lines.isEmpty {
            print("TEXT\t")
        } else {
            for line in lines {
                print("TEXT\t\(line)")
            }
        }
    } catch {
        print("FILE\t\(url.path)")
        print("ERROR\t\(error.localizedDescription)")
    }
}
