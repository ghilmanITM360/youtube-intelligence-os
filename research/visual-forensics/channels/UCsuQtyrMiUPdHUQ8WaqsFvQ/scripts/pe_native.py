"""Native-resolution art evidence for primary review: frames picked deterministically (longest HOLD, plus largest-ink HOLD, plus most-coloured HOLD), written at source resolution, scaled copy of nothing. Writes frames/native/NATIVE_<frame>.png-quality JPEG and tables/native_frames.csv. Usage: python -I pe_native.py <video_dir> [n]"""
import csv, json, sys, pathlib, cv2
V = pathlib.Path(sys.argv[1]).resolve(); n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
H = [s for s in csv.DictReader(open(V / "tables/segments_v1.csv")) if s["kind"] == "HOLD"]
pal = {p["seg"]: p for p in json.load(open(V / "tables/palette_measured.json"))["per_hold"]}
pick = []
for key in (lambda s: int(s["frames"]), lambda s: pal[s["seg"]]["dark_ink_frac"], lambda s: pal[s["seg"]]["saturated_frac"]):
    for s in sorted(H, key=key, reverse=True):
        if s["seg"] not in [p["seg"] for p in pick]: pick.append(s); break
pick = pick[:n]
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); out = V / "frames/native"; out.mkdir(parents=True, exist_ok=True)
rows = []
for s in pick:
    f = int(s["end_frame"]); cap.set(cv2.CAP_PROP_POS_FRAMES, f); ok, im = cap.read(); assert ok
    # crop to the ink bounding box so native pixels are shown without the empty canvas
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); ys, xs = (g < 200).nonzero()
    x0, x1, y0, y1 = (int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())) if len(xs) else (0, im.shape[1] - 1, 0, im.shape[0] - 1)
    p = out / f"NATIVE_{f:06d}.jpg"; cv2.imwrite(str(p), im[y0:y1 + 1, x0:x1 + 1], [cv2.IMWRITE_JPEG_QUALITY, 92])
    rows.append(dict(seg=s["seg"], frame=f, pts=s["end_pts"], file=p.name, crop=f"{x0},{y0},{x1},{y1}", crop_w=x1 - x0 + 1, crop_h=y1 - y0 + 1, scale="1:1 native pixels"))
with open(V / "tables/native_frames.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(rows)
