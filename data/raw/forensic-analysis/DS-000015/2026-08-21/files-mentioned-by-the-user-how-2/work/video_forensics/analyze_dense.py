from __future__ import annotations

import csv
import math
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "dense_frames"
OUT = ROOT / "analysis"


def get_time(path: Path) -> float:
    return int(re.search(r"_(\d+)ms", path.name).group(1)) / 1000


paths = sorted(FRAMES.glob("frame_*ms.jpg"))
times = np.array([get_time(p) for p in paths])
arrays = []
hists = []
for path in paths:
    im = Image.open(path).convert("RGB").resize((45, 80), Image.Resampling.BILINEAR)
    arr = np.asarray(im, dtype=np.float32) / 255.0
    arrays.append(arr)
    hp = []
    for c in range(3):
        h, _ = np.histogram(arr[..., c], bins=24, range=(0, 1))
        hp.append(h / h.sum())
    hists.append(np.concatenate(hp))

rgb = np.zeros(len(paths))
hist = np.zeros(len(paths))
for i in range(1, len(paths)):
    rgb[i] = np.abs(arrays[i] - arrays[i - 1]).mean()
    hist[i] = np.abs(hists[i] - hists[i - 1]).mean()
hybrid = rgb + 2.5 * hist

with (OUT / "dense_metrics.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "file", "rgb_mad", "hist_l1", "hybrid_diff"])
    for i, path in enumerate(paths):
        writer.writerow([f"{times[i]:.3f}", path.name, f"{rgb[i]:.8f}", f"{hist[i]:.8f}", f"{hybrid[i]:.8f}"])

peaks = [i for i in range(1, len(paths) - 1) if hybrid[i] >= hybrid[i - 1] and hybrid[i] >= hybrid[i + 1]]
peaks = sorted(peaks, key=lambda i: hybrid[i], reverse=True)
kept = []
for i in peaks:
    if all(abs(times[i] - times[j]) >= 0.20 for j in kept):
        kept.append(i)
    if len(kept) >= 100:
        break

with (OUT / "dense_change_peaks.tsv").open("w") as f:
    f.write("rank\ttime\thybrid_diff\trgb_mad\thist_l1\tfile\n")
    for rank, i in enumerate(kept, 1):
        f.write(f"{rank}\t{times[i]:.3f}\t{hybrid[i]:.8f}\t{rgb[i]:.8f}\t{hist[i]:.8f}\t{paths[i].name}\n")

provisional = [6.0, 12.0, 14.0, 15.75, 16.5, 17.75, 21.25, 25.5, 31.5, 43.0, 50.0, 53.5, 68.5, 74.5, 95.75, 104.5, 111.5, 113.5]
refined = []
for target in provisional:
    window = np.where((times >= target - 0.35) & (times <= target + 0.35))[0]
    i = int(window[np.argmax(hybrid[window])])
    refined.append(i)

with (OUT / "refined_boundaries.tsv").open("w") as f:
    f.write("target\trefined_time\thybrid_diff\trgb_mad\tprevious_file\tcurrent_file\n")
    for target, i in zip(provisional, refined):
        f.write(f"{target:.3f}\t{times[i]:.3f}\t{hybrid[i]:.8f}\t{rgb[i]:.8f}\t{paths[i-1].name}\t{paths[i].name}\n")


# Motion energy in quarter-second bins, useful for identifying static holds.
motion_rows = []
for start in np.arange(0, times[-1] + 0.25, 0.25):
    idx = np.where((times >= start) & (times < start + 0.25))[0]
    if len(idx):
        motion_rows.append((start, float(np.mean(rgb[idx])), float(np.max(rgb[idx]))))
with (OUT / "motion_energy_250ms.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["start", "mean_rgb_mad", "max_rgb_mad"])
    writer.writerows((f"{a:.3f}", f"{b:.8f}", f"{c:.8f}") for a, b, c in motion_rows)


def contact_sheet(indices: list[int], output: Path):
    columns, cell_w, cell_h = 6, 180, 350
    rows = math.ceil(len(indices) / columns)
    canvas = Image.new("RGB", (columns * cell_w, rows * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=17)
    for j, i in enumerate(indices):
        im = Image.open(paths[i]).convert("RGB")
        im = ImageOps.contain(im, (cell_w - 8, cell_h - 38), Image.Resampling.NEAREST)
        x = j % columns * cell_w + (cell_w - im.width) // 2
        y = j // columns * cell_h + 28
        canvas.paste(im, (x, y))
        draw.text((j % columns * cell_w + 6, j // columns * cell_h + 5), f"{times[i]:.3f}", fill="white", font=font)
    canvas.save(output, quality=92)


boundary_frames = []
for i in refined:
    boundary_frames.extend([max(0, i - 2), max(0, i - 1), i, min(len(paths) - 1, i + 1), min(len(paths) - 1, i + 2)])
for page, start in enumerate(range(0, len(boundary_frames), 30), 1):
    contact_sheet(boundary_frames[start : start + 30], OUT / f"refined_boundaries_{page:02d}.jpg")

print(f"dense_frames={len(paths)}")
print(f"max_hybrid={hybrid.max():.8f}")
print(f"median_hybrid={np.median(hybrid[1:]):.8f}")
print((OUT / "refined_boundaries.tsv").read_text())
