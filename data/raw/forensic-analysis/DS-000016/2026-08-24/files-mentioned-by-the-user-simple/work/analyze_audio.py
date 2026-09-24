import csv
import json
import math
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def dbfs(value: float) -> float:
    return 20.0 * math.log10(max(value, 1e-9))


def stamp(seconds: float) -> str:
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes):02d}:{secs:05.2f}"


if len(sys.argv) != 5:
    raise SystemExit("Usage: analyze_audio.py WAV TRANSCRIPT_JSON OUTPUT_DIR WINDOW_SECONDS")

wav_path = Path(sys.argv[1])
transcript_path = Path(sys.argv[2])
output_dir = Path(sys.argv[3])
window_seconds = float(sys.argv[4])
output_dir.mkdir(parents=True, exist_ok=True)

with wave.open(str(wav_path), "rb") as handle:
    sample_rate = handle.getframerate()
    channels = handle.getnchannels()
    width = handle.getsampwidth()
    frames = handle.getnframes()
    raw = handle.readframes(frames)

if width != 2:
    raise RuntimeError(f"Expected 16-bit PCM, found sample width {width}")
samples = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
if channels > 1:
    samples = samples.reshape(-1, channels).mean(axis=1)

transcript = json.loads(transcript_path.read_text(encoding="utf-8"))
speech_intervals = [(item["start"], item["end"]) for item in transcript["segments"]]
window_size = round(sample_rate * window_seconds)
rows = []
for index, start_sample in enumerate(range(0, len(samples), window_size)):
    block = samples[start_sample : start_sample + window_size]
    if len(block) == 0:
        continue
    start = start_sample / sample_rate
    end = min(len(samples), start_sample + window_size) / sample_rate
    rms = float(np.sqrt(np.mean(block * block)))
    peak = float(np.max(np.abs(block)))
    overlap = 0.0
    for speech_start, speech_end in speech_intervals:
        overlap += max(0.0, min(end, speech_end) - max(start, speech_start))
    speech_fraction = min(1.0, overlap / max(end - start, 1e-9))
    spectrum = np.abs(np.fft.rfft(block * np.hanning(len(block))))
    freqs = np.fft.rfftfreq(len(block), d=1.0 / sample_rate)
    centroid = float(np.sum(spectrum * freqs) / max(np.sum(spectrum), 1e-9))
    rows.append(
        {
            "start_seconds": start,
            "end_seconds": end,
            "rms_dbfs": dbfs(rms),
            "peak_dbfs": dbfs(peak),
            "spectral_centroid_hz": centroid,
            "speech_fraction": speech_fraction,
        }
    )

speech_rows = [row for row in rows if row["speech_fraction"] >= 0.5]
nonspeech_rows = [row for row in rows if row["speech_fraction"] < 0.1]
silence_threshold = -45.0
silence_runs = []
run_start = None
for row in rows:
    if row["rms_dbfs"] < silence_threshold:
        if run_start is None:
            run_start = row["start_seconds"]
    elif run_start is not None:
        if row["start_seconds"] - run_start >= 0.3:
            silence_runs.append([run_start, row["start_seconds"]])
        run_start = None
if run_start is not None:
    silence_runs.append([run_start, rows[-1]["end_seconds"]])

top_peaks = sorted(rows, key=lambda row: row["peak_dbfs"], reverse=True)[:20]
summary = {
    "sample_rate": sample_rate,
    "channels": channels,
    "duration_seconds": len(samples) / sample_rate,
    "window_seconds": window_seconds,
    "rms_dbfs_median_all": float(np.median([row["rms_dbfs"] for row in rows])),
    "rms_dbfs_p10_all": float(np.percentile([row["rms_dbfs"] for row in rows], 10)),
    "rms_dbfs_p90_all": float(np.percentile([row["rms_dbfs"] for row in rows], 90)),
    "rms_dbfs_median_speech": float(np.median([row["rms_dbfs"] for row in speech_rows])),
    "rms_dbfs_median_nonspeech": float(np.median([row["rms_dbfs"] for row in nonspeech_rows])) if nonspeech_rows else None,
    "nonspeech_window_count": len(nonspeech_rows),
    "silence_threshold_dbfs": silence_threshold,
    "silence_runs": silence_runs,
    "top_peak_windows": [
        {
            "time": row["start_seconds"],
            "timestamp": stamp(row["start_seconds"]),
            "peak_dbfs": row["peak_dbfs"],
            "rms_dbfs": row["rms_dbfs"],
            "speech_fraction": row["speech_fraction"],
        }
        for row in top_peaks
    ],
}
(output_dir / "audio_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

with (output_dir / "audio_envelope.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

width_px, height_px = 1800, 720
margin_left, margin_right, margin_top, margin_bottom = 90, 30, 40, 80
plot_w = width_px - margin_left - margin_right
plot_h = height_px - margin_top - margin_bottom
canvas = Image.new("RGB", (width_px, height_px), "white")
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default(size=18)
small_font = ImageFont.load_default(size=15)
draw.rectangle((margin_left, margin_top, margin_left + plot_w, margin_top + plot_h), outline="#777777", width=1)
for db in range(-60, 1, 10):
    y = margin_top + (0 - db) / 60 * plot_h
    draw.line((margin_left, y, margin_left + plot_w, y), fill="#dddddd", width=1)
    draw.text((12, y - 9), f"{db} dBFS", fill="#333333", font=small_font)
duration = rows[-1]["end_seconds"]
for minute in range(0, math.ceil(duration / 60) + 1):
    x = margin_left + (minute * 60 / duration) * plot_w
    draw.line((x, margin_top, x, margin_top + plot_h), fill="#eeeeee", width=1)
    draw.text((x - 20, margin_top + plot_h + 12), f"{minute}:00", fill="#333333", font=small_font)

points = []
for row in rows:
    x = margin_left + (row["start_seconds"] / duration) * plot_w
    clipped_db = min(0.0, max(-60.0, row["rms_dbfs"]))
    y = margin_top + (0 - clipped_db) / 60 * plot_h
    points.append((x, y))
if len(points) > 1:
    draw.line(points, fill="#1756a9", width=2)
draw.text((margin_left, 8), "Audio RMS envelope (0.25 s windows)", fill="#111111", font=font)
draw.text((margin_left + 430, 10), "Blue = measured full-mix RMS; transcript timing used only to classify speech vs gaps", fill="#555555", font=small_font)
canvas.save(output_dir / "audio_envelope.png")

print(json.dumps(summary, indent=2))
