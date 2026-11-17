"""Chronological review sheets from segments_v1.csv: every HOLD -> 1 tile (its last frame = settled state),
every ACTIVITY -> k tiles (frame before, samples across the run, frame after). Tiles carry seg id, frame index, PTS.
Writes frames/sheets/SHEET_nn.jpg and tables/sheet_index.csv (tile -> seg, frame). Usage: python -I xk_sheets.py <video_dir>"""
import csv, sys, pathlib, cv2, numpy as np

V = pathlib.Path(sys.argv[1]); segs = list(csv.DictReader(open(V / "tables/segments_v1.csv")))
src = (V / "evidence/source_path.txt").read_text().strip()
pts = {int(r["frame"]): float(r["pts_time"]) for r in csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv")) if r["pts_time"]}
N = len(pts)
tiles = []
for s in segs:
    a, b = int(s["start_frame"]), int(s["end_frame"])
    if s["kind"] == "HOLD":
        fr = [b]
    else:
        n = b - a + 1; k = min(6, max(1, n // 3 + 1))  # neighbours shown by adjacent HOLD tiles
        fr = sorted({int(round(a + (n - 1) * q / max(1, k - 1))) for q in range(k)})
    for f in fr: tiles.append((s["seg"], s["kind"][0], f))
need = sorted({t[2] for t in tiles})
cap = cv2.VideoCapture(src); W0 = int(cap.get(3)); H0 = int(cap.get(4))
portrait = H0 > W0
tw, th = (270, 480) if portrait else (480, 270); cols, rows_ = (5, 2) if portrait else (3, 4)
got = {}; k = 0; ni = 0
while ni < len(need):
    ok, im = cap.read()
    if not ok: break
    if k == need[ni]: got[k] = cv2.resize(im, (tw, th), interpolation=cv2.INTER_AREA); ni += 1
    k += 1
out = V / "frames/sheets"; out.mkdir(parents=True, exist_ok=True)
for old in out.glob("SHEET_*.jpg"): old.unlink()
idx = []; per = cols * rows_
for sn in range(0, len(tiles), per):
    canvas = np.full((rows_ * (th + 4), cols * (tw + 4), 3), 90, np.uint8)
    for j, (seg, kind, f) in enumerate(tiles[sn:sn + per]):
        r, c = divmod(j, cols); y, x = r * (th + 4), c * (tw + 4)
        t = got[f].copy(); col = (0, 0, 200) if kind == "A" else (0, 120, 0)
        cv2.rectangle(t, (0, 0), (tw - 1, th - 1), col, 3)
        cv2.rectangle(t, (0, th - 22), (tw, th), (0, 0, 0), -1)
        cv2.putText(t, f"{seg} {kind} f{f} {pts.get(f, 0):.3f}s", (4, th - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        canvas[y:y + th, x:x + tw] = t
        idx.append(dict(sheet=f"SHEET_{sn // per + 1:02d}.jpg", slot=j + 1, seg=seg, kind=kind, frame=f, pts=pts.get(f)))
    cv2.imwrite(str(out / f"SHEET_{sn // per + 1:02d}.jpg"), canvas, [cv2.IMWRITE_JPEG_QUALITY, 88])
with open(V / "tables/sheet_index.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(idx[0])); w.writeheader(); w.writerows(idx)
print("tiles", len(tiles), "sheets", (len(tiles) + per - 1) // per, "segments", len(segs))
