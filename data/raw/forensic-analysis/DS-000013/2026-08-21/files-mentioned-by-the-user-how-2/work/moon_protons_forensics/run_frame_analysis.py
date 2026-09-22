from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

from forensic_metrics import frame_time_from_name, select_separated_peaks


ROOT = Path(__file__).resolve().parent
PROXY = ROOT / "proxy_frames"
DENSE = ROOT / "dense_frames"
OUT = ROOT / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

proxy_paths = sorted(PROXY.glob("frame_*ms.jpg"))
dense_paths = sorted(DENSE.glob("frame_*ms.jpg"))
if not proxy_paths or not dense_paths:
    raise SystemExit("decoded proxy and dense frames are required")

font = ImageFont.load_default(size=18)

# Overview pages: one frame every 0.75 seconds, 20 frames/page.
overview_paths = proxy_paths[::3]
for page, start in enumerate(range(0, len(overview_paths), 20), 1):
    batch = overview_paths[start : start + 20]
    columns, cell_w, cell_h = 5, 220, 430
    canvas = Image.new("RGB", (columns * cell_w, math.ceil(len(batch) / columns) * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for index, path in enumerate(batch):
        image = Image.open(path).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 12, cell_h - 46), Image.Resampling.LANCZOS)
        x = index % columns * cell_w + (cell_w - image.width) // 2
        y = index // columns * cell_h + 34
        canvas.paste(image, (x, y))
        draw.text((index % columns * cell_w + 8, index // columns * cell_h + 7), f"{frame_time_from_name(path.name):06.3f}s", fill="white", font=font)
    canvas.save(OUT / f"overview_{page:02d}.jpg", quality=91)

# Dense inter-frame difference metrics at source cadence.
times = [frame_time_from_name(path.name) for path in dense_paths]
arrays: list[np.ndarray] = []
hists: list[np.ndarray] = []
for path in dense_paths:
    arr = np.asarray(Image.open(path).convert("RGB").resize((45, 80), Image.Resampling.BILINEAR), dtype=np.float32) / 255.0
    arrays.append(arr)
    channel_hists = []
    for channel in range(3):
        hist, _ = np.histogram(arr[..., channel], bins=24, range=(0.0, 1.0))
        channel_hists.append(hist.astype(np.float32) / max(float(hist.sum()), 1.0))
    hists.append(np.concatenate(channel_hists))

rgb = np.zeros(len(dense_paths), dtype=np.float64)
hist = np.zeros(len(dense_paths), dtype=np.float64)
for index in range(1, len(dense_paths)):
    rgb[index] = float(np.abs(arrays[index] - arrays[index - 1]).mean())
    hist[index] = float(np.abs(hists[index] - hists[index - 1]).mean())
hybrid = rgb + 2.5 * hist

with (OUT / "dense_metrics.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["time", "file", "rgb_mad", "hist_l1", "hybrid_diff"])
    for index, path in enumerate(dense_paths):
        writer.writerow([f"{times[index]:.3f}", path.name, f"{rgb[index]:.8f}", f"{hist[index]:.8f}", f"{hybrid[index]:.8f}"])

local_maxima = [
    index
    for index in range(1, len(dense_paths) - 1)
    if hybrid[index] >= hybrid[index - 1] and hybrid[index] >= hybrid[index + 1]
]
selected_relative = select_separated_peaks(
    [times[index] for index in local_maxima],
    [float(hybrid[index]) for index in local_maxima],
    min_gap=0.18,
    limit=min(160, len(local_maxima)),
)
selected = [local_maxima[index] for index in selected_relative]
ranked_selected = sorted(selected, key=lambda index: hybrid[index], reverse=True)

with (OUT / "dense_change_peaks.tsv").open("w") as handle:
    handle.write("rank\ttime\thybrid_diff\trgb_mad\thist_l1\tprevious_file\tcurrent_file\n")
    for rank, index in enumerate(ranked_selected, 1):
        handle.write(
            f"{rank}\t{times[index]:.3f}\t{hybrid[index]:.8f}\t{rgb[index]:.8f}\t{hist[index]:.8f}\t{dense_paths[index-1].name}\t{dense_paths[index].name}\n"
        )

# Review pages for the 90 strongest events, each shown as before/current/after.
review_indices: list[int] = []
for index in ranked_selected[:90]:
    review_indices.extend([max(0, index - 2), index, min(len(dense_paths) - 1, index + 2)])
for page, start in enumerate(range(0, len(review_indices), 30), 1):
    batch = review_indices[start : start + 30]
    columns, cell_w, cell_h = 6, 180, 350
    canvas = Image.new("RGB", (columns * cell_w, math.ceil(len(batch) / columns) * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for cell, index in enumerate(batch):
        image = Image.open(dense_paths[index]).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 10, cell_h - 42), Image.Resampling.NEAREST)
        x = cell % columns * cell_w + (cell_w - image.width) // 2
        y = cell // columns * cell_h + 32
        canvas.paste(image, (x, y))
        draw.text((cell % columns * cell_w + 6, cell // columns * cell_h + 5), f"{times[index]:06.3f}s", fill="white", font=font)
    canvas.save(OUT / f"change_triplets_{page:02d}.jpg", quality=92)

# Motion energy in 250 ms bins for hold/movement assessment.
with (OUT / "motion_energy_250ms.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["start", "mean_rgb_mad", "max_rgb_mad"])
    start = 0.0
    while start <= times[-1]:
        indices = [index for index, value in enumerate(times) if start <= value < start + 0.25]
        if indices:
            writer.writerow([f"{start:.3f}", f"{float(np.mean(rgb[indices])):.8f}", f"{float(np.max(rgb[indices])):.8f}"])
        start += 0.25

summary = [
    f"proxy_frames={len(proxy_paths)}",
    f"dense_frames={len(dense_paths)}",
    f"overview_pages={math.ceil(len(overview_paths) / 20)}",
    f"review_pages={math.ceil(min(90, len(ranked_selected)) * 3 / 30)}",
    f"median_hybrid={float(np.median(hybrid[1:])):.8f}",
    f"p95_hybrid={float(np.quantile(hybrid[1:], 0.95)):.8f}",
    f"p99_hybrid={float(np.quantile(hybrid[1:], 0.99)):.8f}",
    f"max_hybrid={float(np.max(hybrid)):.8f}",
]
(OUT / "metric_summary.txt").write_text("\n".join(summary) + "\n")
print((OUT / "metric_summary.txt").read_text(), end="")
