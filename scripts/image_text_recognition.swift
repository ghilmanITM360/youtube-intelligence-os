#!/usr/bin/env swift
// Apple Vision OCR helper (Phase 1C). On-device only; never uploads the
// image anywhere. Prints one JSON object to stdout. Read-only: never
// modifies the source image. Run as: swift scripts/image_text_recognition.swift <path>

import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count == 2 else {
    FileHandle.standardError.write("usage: image_text_recognition.swift <path>\n".data(using: .utf8)!)
    exit(2)
}
let path = CommandLine.arguments[1]
let url = URL(fileURLWithPath: path)

guard let nsImage = NSImage(contentsOf: url),
      let cgImage = nsImage.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    let err = ["error": "could not load image"]
    let data = try! JSONSerialization.data(withJSONObject: err)
    FileHandle.standardOutput.write(data)
    exit(1)
}

struct Line: Codable {
    let text: String
    let confidence: Float
    let boundingBox: [String: Double]
}

var lines: [Line] = []
var errorMessage: String? = nil

let request = VNRecognizeTextRequest { (req, error) in
    if let error = error {
        errorMessage = error.localizedDescription
        return
    }
    guard let observations = req.results as? [VNRecognizedTextObservation] else { return }
    for obs in observations {
        guard let candidate = obs.topCandidates(1).first else { continue }
        let box = obs.boundingBox
        lines.append(Line(
            text: candidate.string,
            confidence: candidate.confidence,
            boundingBox: [
                "x": Double(box.origin.x),
                "y": Double(box.origin.y),
                "width": Double(box.size.width),
                "height": Double(box.size.height),
            ]
        ))
    }
}
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["en-US"]

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
do {
    try handler.perform([request])
} catch {
    errorMessage = error.localizedDescription
}

if let errorMessage = errorMessage {
    let err = ["error": errorMessage]
    let data = try! JSONSerialization.data(withJSONObject: err)
    FileHandle.standardOutput.write(data)
    exit(1)
}

// Reading order: top-to-bottom (Vision's y is bottom-up, so descending y first), then left-to-right.
lines.sort { a, b in
    let ay = a.boundingBox["y"] ?? 0
    let by = b.boundingBox["y"] ?? 0
    if abs(ay - by) > 0.01 { return ay > by }
    return (a.boundingBox["x"] ?? 0) < (b.boundingBox["x"] ?? 0)
}

let fullText = lines.map { $0.text }.joined(separator: "\n")
let meanConfidence = lines.isEmpty ? 0.0 : lines.map { Double($0.confidence) }.reduce(0, +) / Double(lines.count)

struct Output: Codable {
    let fullText: String
    let meanConfidence: Double
    let lineCount: Int
    let lines: [Line]
}

let output = Output(fullText: fullText, meanConfidence: meanConfidence, lineCount: lines.count, lines: lines)
let encoder = JSONEncoder()
let outData = try! encoder.encode(output)
FileHandle.standardOutput.write(outData)
