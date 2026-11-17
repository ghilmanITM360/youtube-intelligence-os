#!/usr/bin/env python3
"""Deep-VF B3 viewing aid: one tile per reviewed ACTIVITY event in [t0,t1) from the existing asset-library state JPGs
(no new decode), captioned with event PTS, subtype and the ASR segment text active at that moment (ASR_UNCERTIFIED).
usage: <venv python> -I beat_sheet.py <video_id> <t0> <t1>  -> deep_vf/script_beats/beats_<vid>_<t0>-<t1>.jpg (+ .csv)"""
import csv, glob, json, os, sys, textwrap
from PIL import Image, ImageDraw
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); v, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
OUT = f"{H}/asset_library/_channel/deep_vf/script_beats"
S = [s for s in json.load(open(f"{H}/videos/{v}/asr/asr_small_en.json"))["segments"] if s["text"].strip()]
ev = [r for r in csv.DictReader(open(f"{H}/videos/{v}/tables/state_ledger.csv")) if r["kind"] == "ACTIVITY" and t0 <= float(r["start_pts"]) < t1]
img = {os.path.basename(p).split("_")[0]: p for p in glob.glob(f"{H}/asset_library/{v}/states/*.jpg")}
rows = []
for r in ev:
    t = float(r["start_pts"]); s = max((x for x in S if x["start"] <= t), key=lambda x: x["start"], default={"text": "", "start": 0})
    rows.append(dict(seg=r["seg"], pts=f"{t:.3f}", frames=r["frames"], subtype=r["subtype"], asr_start=f"{s['start']:.2f}", asr_text=s["text"].strip(), img=img.get(r["seg"], "")))
with open(f"{OUT}/beats_{v}_{int(t0)}-{int(t1)}.csv", "w", newline="") as fo: w = csv.DictWriter(fo, list(rows[0])); w.writeheader(); w.writerows(rows)
port = Image.open(rows[0]["img"]).height > Image.open(rows[0]["img"]).width
tw, th = (200, 356) if port else (400, 225); cols = 8 if port else 5; cap = 64
sheet = Image.new("RGB", (cols * tw, ((len(rows) + cols - 1) // cols) * (th + cap)), (35, 35, 35)); d = ImageDraw.Draw(sheet)
for i, r in enumerate(rows):
    X, Y = (i % cols) * tw, (i // cols) * (th + cap)
    if r["img"]: t = Image.open(r["img"]).convert("RGB"); t.thumbnail((tw, th)); sheet.paste(t, (X, Y + cap))
    d.text((X + 2, Y + 1), f"{r['pts']}s {r['subtype'][:18]} {r['frames']}f", fill=(255, 220, 0))
    for k, line in enumerate(textwrap.wrap(r["asr_text"], 30 if port else 62)[:4]): d.text((X + 2, Y + 13 + 12 * k), line, fill=(200, 230, 255))
sheet.save(f"{OUT}/beats_{v}_{int(t0)}-{int(t1)}.jpg", quality=85); print(len(rows), "events")
