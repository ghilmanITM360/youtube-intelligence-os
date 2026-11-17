#!/usr/bin/env python3
"""P4: measure ONE bounded motion window (<=30 frames) from a SHA-verified xkcd source (local only, read-only source).
usage: <venv python> -I motion_window.py <video_id> <seg> <class_label>
Extracts frames [start-3, end+6] (capped at 30) as JPEG q2 into
<lib>/_channel/motion_windows/<class>_<video>_<seg>/, then per frame (MEASURED, 480-px-wide greyscale):
 diff_prev  = mean |f_t - f_t-1| (0-255)
 progress   = projection of (f_t - A) on (B - A), A = first frame, B = last frame (0..1; exact for a cross-dissolve,
              a proxy "how far toward the end state" for other classes)
 ink_frac   = share of pixels darker than 110
 ecc_tx/ty/scale = affine ECC alignment of f_t to A (camera-like moves; blank if ECC fails)
Writes window.csv, window.json (summary + source SHA) and strip.jpg (every frame, numbered) for viewing."""
import csv, hashlib, json, os, re, subprocess, sys, tempfile
import numpy as np, cv2
from PIL import Image, ImageDraw
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); vid, seg, label = sys.argv[1:4]
mp = f"{H}/videos/{vid}/source_manifest.json"
if os.path.exists(mp): man = json.load(open(mp))["source"]
else:  # ingested-only video: path + sha from the ingest evidence files
    man = dict(file_path=open(f"{H}/videos/{vid}/evidence/source_path.txt").read().strip(), sha256=open(f"{H}/videos/{vid}/evidence/source_sha256.txt").read().split()[0])
h = hashlib.sha256(); f = open(man["file_path"], "rb")
for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
assert h.hexdigest() == man["sha256"], "SOURCE SHA MISMATCH"
led = f"{H}/videos/{vid}/tables/state_ledger.csv"
row = next(r for r in csv.DictReader(open(led if os.path.exists(led) else f"{H}/videos/{vid}/tables/segments_v1.csv")) if r["seg"] == seg)
row.setdefault("subtype", "AUTO_SEGMENT_UNREVIEWED"); row.setdefault("description", "")
s, e = int(row["start_frame"]), int(row["end_frame"]); a, b = max(0, s - 3), min(e + 6, s - 3 + 29)
out = f"{sys.argv[4] if len(sys.argv) > 4 else H + '/asset_library/_channel/motion_windows'}/{label}_{vid}_{seg}"; os.makedirs(out, exist_ok=True)
fs = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False); fs.write(f"select='between(n\\,{a}\\,{b})',showinfo"); fs.close()
p = subprocess.run(["ffmpeg", "-v", "info", "-nostdin", "-i", man["file_path"], "-an", "-/filter:v", fs.name, "-fps_mode", "passthrough", "-q:v", "2", "-y", f"{out}/f_%03d.jpg"], capture_output=True, text=True)
os.remove(fs.name)
pts = [float(m[1]) for l in p.stderr.splitlines() if "Parsed_showinfo" in l for m in [re.search(r" pts_time:([\d.]+)", l)] if m]
files = sorted(x for x in os.listdir(out) if x.startswith("f_"))
assert len(files) == b - a + 1 == len(pts), f"count mismatch {len(files)} {len(pts)} {b-a+1}"
fps = 24.0; ok = all(abs(t - (a + i) / fps) < 0.5 / fps for i, t in enumerate(pts))
G = []
for x in files:
    im = cv2.imread(f"{out}/{x}", cv2.IMREAD_GRAYSCALE); r_ = 480 / im.shape[1]; G.append(cv2.resize(im, None, fx=r_, fy=r_, interpolation=cv2.INTER_AREA).astype(np.float32))
A, B = G[0], G[-1]; d = (B - A).ravel(); dd = float(d @ d) or 1.0
rows = []
for i, g in enumerate(G):
    tx = ty = sc = ""
    try:
        W = np.eye(2, 3, dtype=np.float32); _, W = cv2.findTransformECC(A, g, W, cv2.MOTION_AFFINE, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 60, 1e-4), None, 5)
        tx, ty, sc = f"{W[0,2]/r_:.1f}", f"{W[1,2]/r_:.1f}", f"{np.sqrt(abs(np.linalg.det(W[:, :2]))):.4f}"
    except cv2.error: pass
    rows.append(dict(frame=a + i, pts_s=f"{pts[i]:.4f}", in_ledger_activity=s <= a + i <= e, diff_prev=f"{np.abs(g - G[i-1]).mean():.2f}" if i else "0",
                     progress=f"{float((g - A).ravel() @ d) / dd:.3f}", ink_frac=f"{(g < 110).mean():.4f}", ecc_tx_px=tx, ecc_ty_px=ty, ecc_scale=sc, file=files[i]))
with open(f"{out}/window.csv", "w", newline="") as fo: w = csv.DictWriter(fo, list(rows[0])); w.writeheader(); w.writerows(rows)
act = [i for i, r in enumerate(rows) if float(r["diff_prev"]) > 0.3]
pr = [float(r["progress"]) for r in rows]
summ = dict(video_id=vid, seg=seg, label=label, ledger_subtype=row["subtype"], ledger_frames=[s, e], window_frames=[a, b], source_sha256=man["sha256"],
            pts_check="OK" if ok else "MISMATCH", changing_frames=[a + i for i in act], measured_duration_frames=(act[-1] - act[0] + 1) if act else 0,
            progress_max=max(pr), overshoot=max(pr) > 1.03, description=row["description"][:300])
json.dump(summ, open(f"{out}/window.json", "w"), indent=1)
cols = 6; tw = 320; th = int(tw * G[0].shape[0] / G[0].shape[1]) if G[0].shape[1] > G[0].shape[0] else int(tw * 16 / 9)
sheet = Image.new("RGB", (cols * tw, ((len(files) + cols - 1) // cols) * (th + 14)), (40, 40, 40)); dr = ImageDraw.Draw(sheet)
for i, x in enumerate(files):
    t = Image.open(f"{out}/{x}").convert("RGB"); t.thumbnail((tw, th)); X, Y = (i % cols) * tw, (i // cols) * (th + 14)
    sheet.paste(t, (X, Y + 14)); dr.text((X + 2, Y), f"f{a+i} d={rows[i]['diff_prev']} p={rows[i]['progress']}" + (" *" if rows[i]["in_ledger_activity"] else ""), fill=(255, 255, 0))
sheet.save(f"{out}/strip.jpg", quality=85)
print(json.dumps(summ)); print("progress:", [r["progress"] for r in rows]); print("ecc tx/ty/scale:", [(r["ecc_tx_px"], r["ecc_ty_px"], r["ecc_scale"]) for r in rows])
