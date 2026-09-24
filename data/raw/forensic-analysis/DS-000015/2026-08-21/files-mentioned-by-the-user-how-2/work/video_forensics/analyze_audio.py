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
WAV = ROOT / "audio.wav"
TRANSCRIPT = ROOT / "transcript.json"
OUT = ROOT / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

rate, original = wavfile.read(WAV)
original_dtype = original.dtype
data = original.astype(np.float32)
if np.issubdtype(original_dtype, np.integer):
    data /= float(max(abs(np.iinfo(original_dtype).min), np.iinfo(original_dtype).max))
peak_abs = max(float(np.max(np.abs(data))), 1e-9)

if data.ndim == 2:
    mono = data.mean(axis=1)
    mid = mono
    side = (data[:, 0] - data[:, 1]) / 2
else:
    mono = data
    mid = mono
    side = np.zeros_like(mono)

duration = len(mono) / rate
bin_seconds = 0.05
bin_size = int(rate * bin_seconds)
count = math.ceil(len(mono) / bin_size)
metrics = []
for i in range(count):
    chunk = mono[i * bin_size : min(len(mono), (i + 1) * bin_size)]
    rms = float(np.sqrt(np.mean(np.square(chunk)))) if len(chunk) else 0.0
    peak = float(np.max(np.abs(chunk))) if len(chunk) else 0.0
    zcr = float(np.mean(np.signbit(chunk[1:]) != np.signbit(chunk[:-1]))) if len(chunk) > 1 else 0.0
    metrics.append(
        {
            "time": i * bin_seconds,
            "rms": rms,
            "rms_dbfs": 20 * math.log10(max(rms, 1e-9)),
            "peak": peak,
            "peak_dbfs": 20 * math.log10(max(peak, 1e-9)),
            "zcr": zcr,
        }
    )

with (OUT / "audio_envelope.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(metrics[0].keys()))
    writer.writeheader()
    writer.writerows(metrics)

db = np.array([m["rms_dbfs"] for m in metrics])
delta = np.diff(db, prepend=db[0])
candidate_indices = [
    i
    for i in range(1, len(db) - 1)
    if delta[i] >= np.quantile(delta, 0.985) and delta[i] >= delta[i - 1] and delta[i] >= delta[i + 1]
]
candidate_indices = sorted(candidate_indices, key=lambda i: delta[i], reverse=True)
kept = []
for i in candidate_indices:
    if all(abs(i - j) * bin_seconds >= 0.35 for j in kept):
        kept.append(i)
    if len(kept) == 20:
        break
kept.sort()

silence_mask = db < -42.0
silences = []
start = None
for i, is_silent in enumerate(silence_mask):
    if is_silent and start is None:
        start = i
    if (not is_silent or i == len(silence_mask) - 1) and start is not None:
        end = i if not is_silent else i + 1
        if (end - start) * bin_seconds >= 0.15:
            silences.append((start * bin_seconds, min(duration, end * bin_seconds)))
        start = None

transcript = json.loads(TRANSCRIPT.read_text())
speech_ranges = [(float(s["start"]), float(s["end"])) for s in transcript["segments"]]

summary_lines = [
    f"sample_rate={rate}",
    f"channels={1 if data.ndim == 1 else data.shape[1]}",
    f"duration_seconds={duration:.6f}",
    f"absolute_peak={peak_abs:.6f}",
    f"overall_rms_dbfs={20 * math.log10(max(float(np.sqrt(np.mean(mono**2))), 1e-9)):.2f}",
    f"mid_rms_dbfs={20 * math.log10(max(float(np.sqrt(np.mean(mid**2))), 1e-9)):.2f}",
    f"side_rms_dbfs={20 * math.log10(max(float(np.sqrt(np.mean(side**2))), 1e-9)):.2f}",
    f"rms_dbfs_p10={np.quantile(db, 0.10):.2f}",
    f"rms_dbfs_median={np.median(db):.2f}",
    f"rms_dbfs_p90={np.quantile(db, 0.90):.2f}",
    f"measured_silence_intervals={len(silences)}",
    "silences=" + ", ".join(f"{a:.2f}-{b:.2f}" for a, b in silences),
    "energy_rise_candidates=" + ", ".join(f"{metrics[i]['time']:.2f}(+{delta[i]:.1f}dB)" for i in kept),
    "last_5s_bins=" + ", ".join(f"{m['time']:.2f}:{m['rms_dbfs']:.1f}" for m in metrics if m["time"] >= duration - 5 and round(m["time"] * 4) % 4 == 0),
    "speech_ranges=" + ", ".join(f"{a:.2f}-{b:.2f}" for a, b in speech_ranges),
]
(OUT / "audio_summary.txt").write_text("\n".join(summary_lines) + "\n")


# Render a compact waveform/envelope with measured hard-cut guides.
width, height = 1800, 520
canvas = Image.new("RGB", (width, height), "#10131a")
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default(size=18)
plot_left, plot_right, plot_top, plot_bottom = 80, width - 30, 40, height - 70
for sec in range(0, math.ceil(duration) + 1, 10):
    x = plot_left + (plot_right - plot_left) * sec / duration
    draw.line((x, plot_top, x, plot_bottom), fill="#333a48", width=1)
    draw.text((x - 18, plot_bottom + 12), f"{sec}s", fill="#cbd3df", font=font)
for level in (-50, -40, -30, -20, -10, 0):
    y = plot_bottom - (plot_bottom - plot_top) * (level + 60) / 60
    draw.line((plot_left, y, plot_right, y), fill="#252b35", width=1)
    draw.text((12, y - 8), f"{level} dB", fill="#9aa6b5", font=font)

points = []
for m in metrics:
    x = plot_left + (plot_right - plot_left) * m["time"] / duration
    clipped = min(0.0, max(-60.0, m["rms_dbfs"]))
    y = plot_bottom - (plot_bottom - plot_top) * (clipped + 60) / 60
    points.append((x, y))
draw.line(points, fill="#73d2de", width=2)

shot_boundaries = [6.0, 12.0, 14.0, 15.75, 16.5, 17.75, 21.25, 25.5, 31.5, 43.0, 50.0, 53.5, 68.5, 74.5, 95.75, 104.5, 111.5, 113.5]
for boundary in shot_boundaries:
    x = plot_left + (plot_right - plot_left) * boundary / duration
    draw.line((x, plot_top, x, plot_bottom), fill="#ff6b6b", width=1)
draw.text((plot_left, 8), "50 ms RMS envelope (cyan); provisional shot boundaries (red)", fill="white", font=font)
canvas.save(OUT / "audio_envelope.png")


# Render a log-magnitude spectrogram.
_, t, z = stft(mono, fs=rate, nperseg=2048, noverlap=1536)
freqs = np.fft.rfftfreq(2048, d=1 / rate)
mask = freqs <= 12_000
power = 20 * np.log10(np.maximum(np.abs(z[mask]), 1e-7))
power = np.clip((power + 90) / 75, 0, 1)
power = np.flipud(power)
spec = Image.fromarray(np.uint8(power * 255), mode="L").resize((1800, 620), Image.Resampling.BILINEAR)
spec.save(OUT / "spectrogram.png")

print((OUT / "audio_summary.txt").read_text())
