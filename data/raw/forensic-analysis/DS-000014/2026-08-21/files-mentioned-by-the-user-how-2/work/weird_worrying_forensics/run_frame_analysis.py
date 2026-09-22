from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

from forensic_analysis import parse_frame_time, select_peaks


ROOT = Path(__file__).resolve().parent
PROXY = ROOT / "proxy_frames"
DENSE = ROOT / "dense_frames"
OUT = ROOT / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

proxy_paths = sorted(PROXY.glob("frame_*ms.jpg"))
dense_paths = sorted(DENSE.glob("frame_*ms.jpg"))
if len(proxy_paths) != 191 or len(dense_paths) != 1141:
    raise SystemExit(f"unexpected evidence counts: proxy={len(proxy_paths)} dense={len(dense_paths)}")

font = ImageFont.load_default(size=18)

# One-second overview sequence, 16 frames per page.
overview_paths = proxy_paths[::4]
for page, start in enumerate(range(0, len(overview_paths), 16), 1):
    batch = overview_paths[start : start + 16]
    columns, cell_w, cell_h = 4, 240, 450
    rows = math.ceil(len(batch) / columns)
    canvas = Image.new("RGB", (columns * cell_w, rows * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for index, path in enumerate(batch):
        image = Image.open(path).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 12, cell_h - 44), Image.Resampling.LANCZOS)
        left = index % columns * cell_w
        top = index // columns * cell_h
        x = left + (cell_w - image.width) // 2
        canvas.paste(image, (x, top + 34))
        draw.text((left + 8, top + 7), f"{parse_frame_time(path.name):06.3f}s", fill="white", font=font)
    canvas.save(OUT / f"overview_{page:02d}.jpg", quality=92)

# Frame-distance metrics at source cadence.
times = [parse_frame_time(path.name) for path in dense_paths]
previous_array = None
previous_hist = None
rows = []
for path, timestamp in zip(dense_paths, times, strict=True):
    array = np.asarray(
        Image.open(path).convert("RGB").resize((45, 80), Image.Resampling.BILINEAR),
        dtype=np.float32,
    ) / 255.0
    hist = np.concatenate(
        [
            np.histogram(array[..., channel], bins=24, range=(0.0, 1.0))[0].astype(np.float32) / array[..., channel].size
            for channel in range(3)
        ]
    )
    rgb_mad = 0.0 if previous_array is None else float(np.abs(array - previous_array).mean())
    hist_l1 = 0.0 if previous_hist is None else float(np.abs(hist - previous_hist).mean())
    hybrid = rgb_mad + 2.5 * hist_l1
    rows.append((timestamp, path.name, rgb_mad, hist_l1, hybrid))
    previous_array = array
    previous_hist = hist

with (OUT / "dense_metrics.tsv").open("w", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(["time", "file", "rgb_mad", "hist_l1", "hybrid_diff"])
    for row in rows:
        writer.writerow([f"{row[0]:.3f}", row[1], f"{row[2]:.8f}", f"{row[3]:.8f}", f"{row[4]:.8f}"])

local_maxima = [
    row
    for index, row in enumerate(rows[1:-1], 1)
    if row[4] >= rows[index - 1][4] and row[4] >= rows[index + 1][4]
]
threshold = float(np.quantile([row[4] for row in local_maxima], 0.70))
selected_pairs = select_peaks(
    [(row[0], row[4]) for row in local_maxima],
    threshold=threshold,
    minimum_distance=0.18,
)
selected_times = {time for time, _ in sorted(selected_pairs, key=lambda pair: pair[1], reverse=True)[:120]}
selected_rows = [row for row in local_maxima if row[0] in selected_times]
selected_rows.sort(key=lambda row: row[4], reverse=True)

with (OUT / "dense_change_peaks.tsv").open("w") as handle:
    handle.write("rank\ttime\thybrid_diff\trgb_mad\thist_l1\tcurrent_file\n")
    for rank, row in enumerate(selected_rows, 1):
        handle.write(f"{rank}\t{row[0]:.3f}\t{row[4]:.8f}\t{row[2]:.8f}\t{row[3]:.8f}\t{row[1]}\n")

# Show before/current/after for the 72 strongest non-adjacent visual changes.
time_to_index = {row[0]: index for index, row in enumerate(rows)}
review_indices = []
for row in selected_rows[:72]:
    index = time_to_index[row[0]]
    review_indices.extend([max(0, index - 2), index, min(len(rows) - 1, index + 2)])
for page, start in enumerate(range(0, len(review_indices), 27), 1):
    batch = review_indices[start : start + 27]
    columns, cell_w, cell_h = 9, 120, 235
    canvas = Image.new("RGB", (columns * cell_w, math.ceil(len(batch) / columns) * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for cell, index in enumerate(batch):
        image = Image.open(dense_paths[index]).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 8, cell_h - 36), Image.Resampling.NEAREST)
        left = cell % columns * cell_w
        top = cell // columns * cell_h
        canvas.paste(image, (left + (cell_w - image.width) // 2, top + 28))
        draw.text((left + 4, top + 4), f"{times[index]:06.3f}s", fill="white", font=font)
    canvas.save(OUT / f"change_triplets_{page:02d}.jpg", quality=92)

# Quarter-second motion energy for hold/movement assessment.
with (OUT / "motion_energy_250ms.tsv").open("w") as handle:
    handle.write("start\tmean_rgb_mad\tmax_rgb_mad\n")
    start = 0.0
    while start <= times[-1]:
        values = [row[2] for row in rows if start <= row[0] < start + 0.25]
        if values:
            handle.write(f"{start:.3f}\t{float(np.mean(values)):.8f}\t{float(np.max(values)):.8f}\n")
        start += 0.25

hybrid_values = np.array([row[4] for row in rows[1:]])
summary = [
    f"proxy_frames={len(proxy_paths)}",
    f"dense_frames={len(dense_paths)}",
    f"overview_pages={math.ceil(len(overview_paths) / 16)}",
    f"change_review_pages={math.ceil(len(review_indices) / 27)}",
    f"median_hybrid={float(np.median(hybrid_values)):.8f}",
    f"p95_hybrid={float(np.quantile(hybrid_values, 0.95)):.8f}",
    f"p99_hybrid={float(np.quantile(hybrid_values, 0.99)):.8f}",
    f"max_hybrid={float(np.max(hybrid_values)):.8f}",
]
(OUT / "metric_summary.txt").write_text("\n".join(summary) + "\n")
print((OUT / "metric_summary.txt").read_text(), end="")
