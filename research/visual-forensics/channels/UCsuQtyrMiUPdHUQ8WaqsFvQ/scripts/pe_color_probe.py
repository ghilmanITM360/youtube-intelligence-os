"""Probe: per encoder-absorbed frame and per HOLD first-vs-last, measure change in colour (max channel diff) not luma. Usage: python -I pe_color_probe.py <video_dir> [montage_seg ...]"""
import csv, json, sys, pathlib, cv2, numpy as np
V = pathlib.Path(sys.argv[1]).resolve(); only = sys.argv[2:]
segs = list(csv.DictReader(open(V / "tables/segments_v1.csv"))); cal = json.load(open(V / "tables/detector_calibration.json")); E = set(cal["encoder_artifact_frames"])
holds = [s for s in segs if s["kind"] == "HOLD"]
need = set(E) | {f - 1 for f in E} | {int(s[k]) for s in holds for k in ("start_frame", "end_frame")}
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); F = {}; i = 0; last = max(need)
while i <= last:
    ok, im = cap.read()
    if not ok: break
    if i in need: F[i] = cv2.resize(im, (480, int(480 * im.shape[0] / im.shape[1])), interpolation=cv2.INTER_AREA)
    i += 1
def cd(a, b): d = cv2.absdiff(a, b).max(axis=2); return int((d >= 40).sum()), int(d.max())
er = [(f, *cd(F[f - 1], F[f])) for f in sorted(E) if f > 0]
hr = [(s["seg"], int(s["start_frame"]), int(s["end_frame"]), *cd(F[int(s["start_frame"])], F[int(s["end_frame"])])) for s in holds]
print("enc frames with colour change px40>200:", [x for x in er if x[1] > 200][:30])
print("holds first-vs-last colour px40>200:", [x for x in hr if x[3] > 200])
for seg in only:
    s = next(x for x in segs if x["seg"] == seg); a, b = int(s["start_frame"]), int(s["end_frame"]); fr = [a] + [f for f in sorted(E) if a <= f <= b] + [b]
    fr = sorted(set(fr))[:12]; cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); tiles = []
    for f in fr:
        cap.set(cv2.CAP_PROP_POS_FRAMES, f); ok, im = cap.read(); t = cv2.resize(im, (320, int(320 * im.shape[0] / im.shape[1]))); cv2.putText(t, f"{seg} f{f}", (4, 16), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1); tiles.append(t)
    while len(tiles) % 4: tiles.append(np.full_like(tiles[0], 90))
    cv2.imwrite(str(V.parents[1] / f"campaign/calib/{V.name}_{seg}.jpg"), np.vstack([np.hstack(tiles[k:k + 4]) for k in range(0, len(tiles), 4)]), [cv2.IMWRITE_JPEG_QUALITY, 85])
