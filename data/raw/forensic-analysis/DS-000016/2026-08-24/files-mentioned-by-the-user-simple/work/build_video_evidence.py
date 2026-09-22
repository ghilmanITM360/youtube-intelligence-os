import csv
import json
import math
import re
import sys
from pathlib import Path

import av
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def timestamp(seconds: float) -> str:
    millis = round(seconds * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def safe_filename_time(seconds: float) -> str:
    return timestamp(seconds).replace(":", "-").replace(".", "-")


def mean_abs_difference(a: Image.Image, b: Image.Image) -> float:
    aa = np.asarray(a.convert("L").resize((160, 90)), dtype=np.float32)
    bb = np.asarray(b.convert("L").resize((160, 90)), dtype=np.float32)
    return float(np.mean(np.abs(aa - bb)))


if len(sys.argv) != 5:
    raise SystemExit("Usage: build_video_evidence.py VIDEO SCENE_METADATA OUTPUT_DIR DURATION")

video_path = Path(sys.argv[1])
scene_path = Path(sys.argv[2])
output_dir = Path(sys.argv[3])
duration = float(sys.argv[4])
frames_dir = output_dir / "shot_triplets"
montage_dir = output_dir / "shot_montages"
frames_dir.mkdir(parents=True, exist_ok=True)
montage_dir.mkdir(parents=True, exist_ok=True)

scene_text = scene_path.read_text(encoding="utf-8")
cut_times = [float(x) for x in re.findall(r"pts_time:([0-9.]+)", scene_text)]
scene_scores = [float(x) for x in re.findall(r"lavfi\.scene_score=([0-9.]+)", scene_text)]
boundaries = [0.0] + cut_times + [duration]

shots = []
targets = []
for index, (start, end) in enumerate(zip(boundaries[:-1], boundaries[1:]), 1):
    shot_duration = end - start
    inset = min(0.12, shot_duration * 0.12)
    start_sample = start + inset
    end_sample = max(start_sample, end - inset)
    mid_sample = (start + end) / 2
    samples = {"start": start_sample, "mid": mid_sample, "end": end_sample}
    shot = {
        "shot_id": f"S{index:03d}",
        "visual_id": f"V{index:03d}",
        "in_seconds": start,
        "out_seconds": end,
        "duration_seconds": shot_duration,
        "in_timestamp": timestamp(start),
        "out_timestamp": timestamp(end),
        "scene_score_in": None if index == 1 else scene_scores[index - 2],
        "samples": samples,
        "sample_files": {},
    }
    shots.append(shot)
    for label, target in samples.items():
        targets.append((target, index - 1, label))

targets.sort(key=lambda item: item[0])
target_cursor = 0
container = av.open(str(video_path))
stream = container.streams.video[0]
stream.thread_type = "AUTO"

for frame in container.decode(stream):
    if frame.time is None:
        continue
    frame_time = float(frame.time)
    while target_cursor < len(targets) and frame_time >= targets[target_cursor][0]:
        target, shot_index, label = targets[target_cursor]
        image = frame.to_image().resize((640, 360), Image.Resampling.LANCZOS)
        shot = shots[shot_index]
        filename = f"{shot['shot_id']}_{label}_{safe_filename_time(target)}.jpg"
        image.save(frames_dir / filename, quality=92, optimize=True)
        shot["sample_files"][label] = filename
        shot.setdefault("actual_sample_times", {})[label] = frame_time
        target_cursor += 1
    if target_cursor >= len(targets):
        break

container.close()

for shot in shots:
    images = {
        label: Image.open(frames_dir / filename).convert("RGB")
        for label, filename in shot["sample_files"].items()
    }
    if all(label in images for label in ("start", "mid", "end")):
        d_start_mid = mean_abs_difference(images["start"], images["mid"])
        d_mid_end = mean_abs_difference(images["mid"], images["end"])
        d_start_end = mean_abs_difference(images["start"], images["end"])
        shot["motion_metrics"] = {
            "mean_abs_start_mid": round(d_start_mid, 3),
            "mean_abs_mid_end": round(d_mid_end, 3),
            "mean_abs_start_end": round(d_start_end, 3),
        }
        peak = max(d_start_mid, d_mid_end, d_start_end)
        shot["measured_change_class"] = (
            "very_low" if peak < 1.0 else
            "low" if peak < 2.5 else
            "moderate" if peak < 6.0 else
            "high"
        )

font = ImageFont.load_default(size=18)
small_font = ImageFont.load_default(size=15)
for page_index in range(math.ceil(len(shots) / 16)):
    subset = shots[page_index * 16 : (page_index + 1) * 16]
    canvas = Image.new("RGB", (1280, 1024), "white")
    draw = ImageDraw.Draw(canvas)
    for cell_index, shot in enumerate(subset):
        row, col = divmod(cell_index, 4)
        x, y = col * 320, row * 256
        image = Image.open(frames_dir / shot["sample_files"]["mid"]).convert("RGB").resize((320, 180))
        canvas.paste(image, (x, y))
        draw.rectangle((x, y + 180, x + 320, y + 256), fill="white")
        draw.text((x + 6, y + 185), f"{shot['shot_id']} / {shot['visual_id']}", fill="black", font=font)
        draw.text((x + 6, y + 210), f"{shot['in_timestamp']} – {shot['out_timestamp']}", fill="black", font=small_font)
        change = shot.get("measured_change_class", "unknown")
        draw.text((x + 6, y + 232), f"within-shot change: {change}", fill="black", font=small_font)
    page_path = montage_dir / f"shot_montage_{page_index + 1:02d}.jpg"
    canvas.save(page_path, quality=90, optimize=True)

for page_index in range(math.ceil(len(shots) / 8)):
    subset = shots[page_index * 8 : (page_index + 1) * 8]
    canvas = Image.new("RGB", (960, 1680), "white")
    draw = ImageDraw.Draw(canvas)
    for row, shot in enumerate(subset):
        y = row * 210
        for col, label in enumerate(("start", "mid", "end")):
            x = col * 320
            image = Image.open(frames_dir / shot["sample_files"][label]).convert("RGB").resize((320, 180))
            canvas.paste(image, (x, y))
            draw.rectangle((x, y, x + 62, y + 22), fill=(0, 0, 0))
            draw.text((x + 5, y + 3), label.upper(), fill="white", font=small_font)
        draw.rectangle((0, y + 180, 960, y + 210), fill="white")
        metric = shot.get("motion_metrics", {}).get("mean_abs_start_end", "n/a")
        draw.text(
            (6, y + 185),
            f"{shot['shot_id']} {shot['in_timestamp']}–{shot['out_timestamp']} | start→end MAD {metric}",
            fill="black",
            font=small_font,
        )
    page_path = montage_dir / f"motion_triplets_{page_index + 1:02d}.jpg"
    canvas.save(page_path, quality=90, optimize=True)

(output_dir / "shot_manifest.json").write_text(json.dumps(shots, indent=2), encoding="utf-8")
with (output_dir / "shot_manifest.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(
        handle,
        fieldnames=[
            "shot_id", "visual_id", "in_timestamp", "out_timestamp", "duration_seconds",
            "scene_score_in", "measured_change_class", "mean_abs_start_end",
        ],
    )
    writer.writeheader()
    for shot in shots:
        writer.writerow(
            {
                "shot_id": shot["shot_id"],
                "visual_id": shot["visual_id"],
                "in_timestamp": shot["in_timestamp"],
                "out_timestamp": shot["out_timestamp"],
                "duration_seconds": round(shot["duration_seconds"], 6),
                "scene_score_in": shot["scene_score_in"],
                "measured_change_class": shot.get("measured_change_class"),
                "mean_abs_start_end": shot.get("motion_metrics", {}).get("mean_abs_start_end"),
            }
        )

print(f"Built evidence for {len(shots)} shots; wrote {target_cursor} sampled frames")
