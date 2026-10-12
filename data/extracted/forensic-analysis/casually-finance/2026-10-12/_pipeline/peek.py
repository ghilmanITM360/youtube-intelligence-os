"""Full-resolution frame peek for detail review (read-only on the source video).
Usage: python3 -B peek.py <VIDEO_ID> <WORK_ROOT> <OUT_IMG> <STATE_ID> [<STATE_ID> ...] [--w 640]
Pulls each state's representative frame (rep_t from visual_auto.json) straight from the source MP4 with ffmpeg and tiles them with labels.
"""
import json, subprocess, sys, tempfile, os
from pathlib import Path
from PIL import Image, ImageDraw

vid, work, outimg, *rest = sys.argv[1:]
w_tile = 640
if "--w" in rest:
    i = rest.index("--w"); w_tile = int(rest[i + 1]); rest = rest[:i] + rest[i + 2:]
va = json.load(open(Path(work) / vid / "visual_auto.json"))
src = json.load(open(Path(os.environ.get("OUT_DIR", "/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research")) / "00_MANIFEST/PROGRESS.json"))["videos"][vid]["source_path"]
by = {s["state_id"]: s for s in va["states"]}
tiles = []
for sid in rest:
    s = by[sid]; t = s["rep_t"]
    tmp = tempfile.mktemp(suffix=".png")
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB"); os.remove(tmp)
    h = int(im.height * w_tile / im.width); im = im.resize((w_tile, h))
    ImageDraw.Draw(im).rectangle([0, 0, 190, 22], fill=(200, 0, 0)); ImageDraw.Draw(im).text((4, 4), f"{sid} @{t:.2f}s", fill=(255, 255, 255))
    tiles.append(im)
W = sum(t.width for t in tiles); H = max(t.height for t in tiles)
sheet = Image.new("RGB", (W, H), (60, 60, 60)); x = 0
for t in tiles: sheet.paste(t, (x, 0)); x += t.width
sheet.save(outimg, quality=88)
print(outimg, sheet.size)
