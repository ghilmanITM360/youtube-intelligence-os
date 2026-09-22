from __future__ import annotations

import csv
import math
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / "proxy_frames"
OUT = ROOT / "analysis"
OUT.mkdir(parents=True, exist_ok=True)


def ts_label(seconds: float) -> str:
    minutes = int(seconds // 60)
    remain = seconds - 60 * minutes
    return f"{minutes:02d}:{remain:05.2f}"


def frame_time(path: Path) -> float:
    match = re.search(r"_(\d+)ms", path.name)
    if not match:
        raise ValueError(path)
    return int(match.group(1)) / 1000.0


paths = sorted(FRAMES.glob("frame_*ms.jpg"))
if not paths:
    raise SystemExit("No proxy frames found")

rows: list[dict[str, float | str]] = []
arrays: list[np.ndarray] = []
hists: list[np.ndarray] = []

for path in paths:
    image = Image.open(path).convert("RGB")
    small = image.resize((64, 114), Image.Resampling.BILINEAR)
    arr = np.asarray(small, dtype=np.float32) / 255.0
    arrays.append(arr)
    gray = arr @ np.array([0.2126, 0.7152, 0.0722], dtype=np.float32)
    gx = np.abs(np.diff(gray, axis=1)).mean()
    gy = np.abs(np.diff(gray, axis=0)).mean()
    hist_parts = []
    for channel in range(3):
        h, _ = np.histogram(arr[..., channel], bins=32, range=(0.0, 1.0), density=False)
        hist_parts.append(h.astype(np.float32) / h.sum())
    h = np.concatenate(hist_parts)
    hists.append(h)
    rows.append(
        {
            "time": frame_time(path),
            "file": path.name,
            "mean_luma": float(gray.mean()),
            "std_luma": float(gray.std()),
            "edge_energy": float(gx + gy),
            "rgb_mad": 0.0,
            "hist_l1": 0.0,
            "hybrid_diff": 0.0,
        }
    )

for i in range(1, len(rows)):
    rgb_mad = float(np.abs(arrays[i] - arrays[i - 1]).mean())
    hist_l1 = float(np.abs(hists[i] - hists[i - 1]).mean())
    hybrid = rgb_mad + 2.5 * hist_l1
    rows[i]["rgb_mad"] = rgb_mad
    rows[i]["hist_l1"] = hist_l1
    rows[i]["hybrid_diff"] = hybrid

with (OUT / "frame_metrics.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

diffs = np.array([float(r["hybrid_diff"]) for r in rows])
rgb_diffs = np.array([float(r["rgb_mad"]) for r in rows])
quantiles = {q: float(np.quantile(diffs[1:], q)) for q in (0.50, 0.75, 0.90, 0.95, 0.975, 0.99)}

candidates = []
threshold = quantiles[0.90]
for i in range(1, len(rows) - 1):
    if diffs[i] >= threshold and diffs[i] >= diffs[i - 1] and diffs[i] >= diffs[i + 1]:
        candidates.append(rows[i])

with (OUT / "cut_candidates.tsv").open("w") as f:
    f.write("time\thybrid_diff\trgb_mad\thist_l1\tfile\n")
    for r in sorted(candidates, key=lambda x: float(x["hybrid_diff"]), reverse=True):
        f.write(f"{float(r['time']):.3f}\t{float(r['hybrid_diff']):.6f}\t{float(r['rgb_mad']):.6f}\t{float(r['hist_l1']):.6f}\t{r['file']}\n")

(OUT / "metric_summary.txt").write_text(
    "\n".join([f"frames={len(rows)}", f"interval=0.25", *(f"q{int(q*1000):03d}={v:.6f}" for q, v in quantiles.items()), f"max={diffs.max():.6f}"])
    + "\n"
)


def make_contact_sheet(selected: list[Path], output: Path, columns: int = 5, cell_w: int = 216, cell_h: int = 410):
    rows_count = math.ceil(len(selected) / columns)
    canvas = Image.new("RGB", (columns * cell_w, rows_count * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=18)
    for idx, path in enumerate(selected):
        image = Image.open(path).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 12, cell_h - 42), Image.Resampling.LANCZOS)
        x = (idx % columns) * cell_w + (cell_w - image.width) // 2
        y = (idx // columns) * cell_h + 30
        canvas.paste(image, (x, y))
        draw.text(((idx % columns) * cell_w + 8, (idx // columns) * cell_h + 7), ts_label(frame_time(path)), fill="white", font=font)
    canvas.save(output, quality=90)


overview = [p for p in paths if int(round(frame_time(p) * 4)) % 4 == 0]
for page, start in enumerate(range(0, len(overview), 25), start=1):
    make_contact_sheet(overview[start : start + 25], OUT / f"overview_{page:02d}.jpg")

# Candidate sheets are time-ordered, with one frame before and after each local maximum.
candidate_indices = sorted({paths.index(FRAMES / str(r["file"])) for r in candidates})
triplets: list[Path] = []
for i in candidate_indices:
    triplets.extend(paths[max(0, i - 1) : min(len(paths), i + 2)])
for page, start in enumerate(range(0, len(triplets), 30), start=1):
    make_contact_sheet(triplets[start : start + 30], OUT / f"cut_triplets_{page:02d}.jpg", columns=6, cell_w=190, cell_h=360)

print((OUT / "metric_summary.txt").read_text(), end="")
print(f"candidate_local_maxima={len(candidates)}")
print(f"overview_sheets={math.ceil(len(overview)/25)}")
