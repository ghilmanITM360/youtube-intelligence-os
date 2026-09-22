from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile
from scipy.signal import stft


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "analysis"
OUT.mkdir(parents=True, exist_ok=True)
sample_rate, original = wavfile.read(ROOT / "audio.wav")
source_dtype = original.dtype
data = original.astype(np.float32)
if np.issubdtype(source_dtype, np.integer):
    data /= max(abs(np.iinfo(source_dtype).min), np.iinfo(source_dtype).max)

if data.ndim == 2:
    mid = data.mean(axis=1)
    side = (data[:, 0] - data[:, 1]) / 2
else:
    mid = data
    side = np.zeros_like(mid)

duration = len(mid) / sample_rate
bin_seconds = 0.05
bin_size = int(sample_rate * bin_seconds)
metrics = []
for index in range(math.ceil(len(mid) / bin_size)):
    chunk = mid[index * bin_size : min(len(mid), (index + 1) * bin_size)]
    rms = float(np.sqrt(np.mean(chunk**2))) if len(chunk) else 0.0
    peak = float(np.max(np.abs(chunk))) if len(chunk) else 0.0
    metrics.append((index * bin_seconds, rms, 20 * math.log10(max(rms, 1e-9)), peak))

with (OUT / "audio_envelope.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["time", "rms", "rms_dbfs", "peak"])
    writer.writerows((f"{time:.3f}", f"{rms:.8f}", f"{db:.3f}", f"{peak:.8f}") for time, rms, db, peak in metrics)

db_values = np.array([row[2] for row in metrics])
silence_mask = db_values < -42.0
silences = []
start = None
for index, quiet in enumerate(silence_mask):
    if quiet and start is None:
        start = index
    if start is not None and ((not quiet) or index == len(silence_mask) - 1):
        end = index if not quiet else index + 1
        if (end - start) * bin_seconds >= 0.15:
            silences.append((start * bin_seconds, min(duration, end * bin_seconds)))
        start = None

transcript = json.loads((ROOT / "transcript.json").read_text())
speech_mask = np.zeros(len(mid), dtype=bool)
for segment in transcript["segments"]:
    start_sample = max(0, int(float(segment["start"]) * sample_rate))
    end_sample = min(len(mid), int(float(segment["end"]) * sample_rate))
    speech_mask[start_sample:end_sample] = True

def rms_db(values: np.ndarray) -> float:
    return 20 * math.log10(max(float(np.sqrt(np.mean(values**2))), 1e-9)) if len(values) else -180.0

summary = [
    f"sample_rate={sample_rate}",
    f"channels={1 if data.ndim == 1 else data.shape[1]}",
    f"duration_seconds={duration:.6f}",
    f"absolute_peak={float(np.max(np.abs(data))):.6f}",
    f"overall_rms_dbfs={rms_db(mid):.2f}",
    f"mid_rms_dbfs={rms_db(mid):.2f}",
    f"side_rms_dbfs={rms_db(side):.2f}",
    f"speech_region_rms_dbfs={rms_db(mid[speech_mask]):.2f}",
    f"outside_transcript_rms_dbfs={rms_db(mid[~speech_mask]):.2f}",
    f"rms_dbfs_p10={float(np.quantile(db_values, 0.10)):.2f}",
    f"rms_dbfs_median={float(np.median(db_values)):.2f}",
    f"rms_dbfs_p90={float(np.quantile(db_values, 0.90)):.2f}",
    f"measured_silence_intervals={len(silences)}",
    "silences=" + ", ".join(f"{start:.2f}-{end:.2f}" for start, end in silences),
    f"transcript_segments={len(transcript['segments'])}",
]
(OUT / "audio_summary.txt").write_text("\n".join(summary) + "\n")

# Waveform envelope image.
width, height = 1800, 520
canvas = Image.new("RGB", (width, height), "#10131a")
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default(size=18)
left, right, top, bottom = 80, width - 30, 40, height - 70
for second in range(0, math.ceil(duration) + 1, 10):
    x = left + (right - left) * second / duration
    draw.line((x, top, x, bottom), fill="#333a48", width=1)
    draw.text((x - 18, bottom + 12), f"{second}s", fill="#cbd3df", font=font)
for level in (-60, -50, -40, -30, -20, -10, 0):
    y = bottom - (bottom - top) * (level + 60) / 60
    draw.line((left, y, right, y), fill="#252b35", width=1)
    draw.text((12, y - 8), f"{level} dB", fill="#9aa6b5", font=font)
points = []
for time, _, db, _ in metrics:
    x = left + (right - left) * time / duration
    clipped = min(0.0, max(-60.0, db))
    y = bottom - (bottom - top) * (clipped + 60) / 60
    points.append((x, y))
draw.line(points, fill="#73d2de", width=2)
draw.text((left, 8), "50 ms RMS envelope", fill="white", font=font)
canvas.save(OUT / "audio_envelope.png")

# Spectrogram up to 12 kHz.
frequencies, _, spectrum = stft(mid, fs=sample_rate, nperseg=2048, noverlap=1536)
mask = frequencies <= 12_000
power = 20 * np.log10(np.maximum(np.abs(spectrum[mask]), 1e-7))
power = np.clip((power + 90) / 75, 0, 1)
image = Image.fromarray(np.uint8(np.flipud(power) * 255), mode="L").resize((1800, 620), Image.Resampling.BILINEAR)
image.save(OUT / "spectrogram.png")
print((OUT / "audio_summary.txt").read_text(), end="")
