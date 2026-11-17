#!/usr/bin/env python3
"""Contact sheet of library frames for the viewing pass (local only). Adapted copy of the CF tool: label_mode
'portrait' makes 9:16 tiles for Shorts; anything else = 16:9 tiles.
usage: <venv python> -I make_sheet.py <asset_library_root> <out.jpg> <cols> <thumb_w> <landscape|portrait> <rel_path|cluster_id> ...
Each tile is labelled with a running number + short id; <out>.members.csv maps tile -> item -> path."""
import csv, os, sys
from PIL import Image, ImageDraw, ImageFont
root, out, cols, tw, mode, *items = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], *sys.argv[6:]
root = os.path.abspath(root)
idx = {r["cluster_id"]: r for r in csv.DictReader(open(f"{root}/_channel/unique_frames_index.csv"))}
tiles = []
for n, it in enumerate(items):
    if it in idx: p = f"{root}/{idx[it]['rep_file']}"; lab = f"{n+1} {idx[it]['rep_video'][:6]}/{idx[it]['rep_state']}"
    else: p = f"{root}/{it}"; b = os.path.basename(it).split('_f')[0]; lab = f"{n+1} {it.split('/')[0][:6]}/{b}"
    tiles.append((p, lab))
th = int(tw * 16 / 9) if mode == "portrait" else int(tw * 9 / 16); pad = 14
rows = (len(tiles) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + pad)), (40, 40, 40)); d = ImageDraw.Draw(sheet)
try: f = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 11)
except Exception: f = ImageFont.load_default()
for i, (p, lab) in enumerate(tiles):
    im = Image.open(p); im.draft("RGB", (tw * 2, th * 2)); im = im.convert("RGB"); im.thumbnail((tw, th), Image.LANCZOS)
    x, y = (i % cols) * tw, (i // cols) * (th + pad)
    sheet.paste(im, (x + (tw - im.size[0]) // 2, y + pad)); d.text((x + 2, y + 1), lab, fill=(255, 255, 0), font=f)
sheet.save(out, quality=85); print(out, sheet.size, len(tiles))
with open(out + ".members.csv", "w", newline="") as mf:
    w = csv.writer(mf); w.writerow(["tile", "item", "path"]); [w.writerow([n + 1, it, p]) for n, (it, (p, _)) in enumerate(zip(items, tiles))]
