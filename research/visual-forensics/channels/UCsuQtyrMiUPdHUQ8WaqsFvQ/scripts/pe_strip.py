"""Dense strips for undersampled ACTIVITY segments (n_frames > 18, i.e. sheet sampled <1 tile per 3 frames).
Every frame (stride 2 if >96 frames, stride 4 if >192) at small scale, labelled with frame, PTS and changed_frac.
Writes frames/strips/<seg>.jpg + tables/strip_index.csv. Usage: python3 -I xk_strip.py <video_dir> [seg ...]"""
import csv, sys, pathlib, cv2, numpy as np

V = pathlib.Path(sys.argv[1]); only = set(sys.argv[2:])
segs = [s for s in csv.DictReader(open(V / "tables/segments_v1.csv"))
        if s["kind"] == "ACTIVITY" and (s["seg"] in only if only else int(s["frames"]) > 12)]
meas = {int(r["frame"]): r for r in csv.DictReader(open(V / "tables/FULL_FRAME_MEASUREMENTS.csv"))}
cfk = next(k for k in next(iter(meas.values())) if k.startswith("changed_frac"))
plan = []
for s in segs:
    a, b = int(s["start_frame"]), int(s["end_frame"]); n = b - a + 1
    st = 1 if n <= 96 else 2 if n <= 192 else 4
    plan.append((s["seg"], list(range(a, b + 1, st)) + ([b] if (b - a) % st else [])))
need = sorted({f for _, fr in plan for f in fr})
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip())
W0, H0 = int(cap.get(3)), int(cap.get(4)); tw, th = (108, 192) if H0 > W0 else (240, 135); cols = 12 if H0 > W0 else 8
got, k, ni = {}, 0, 0
while ni < len(need):
    ok, im = cap.read()
    if not ok: break
    if k == need[ni]: got[k] = cv2.resize(im, (tw, th), interpolation=cv2.INTER_AREA); ni += 1
    k += 1
out = V / "frames/strips"; out.mkdir(parents=True, exist_ok=True); idx = []
for seg, fr in plan:
    rows = -(-len(fr) // cols); lab = 14
    canvas = np.full((rows * (th + lab + 2), cols * (tw + 2), 3), 60, np.uint8)
    for j, f in enumerate(fr):
        r, c = divmod(j, cols); y, x = r * (th + lab + 2), c * (tw + 2)
        canvas[y:y + th, x:x + tw] = got[f]
        cf = float(meas[f][cfk] or 0)
        cv2.putText(canvas, f"f{f} {cf:.3f}", (x + 2, y + th + 11), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0, 255, 255) if cf > 0.05 else (255, 255, 255), 1)
    p = out / f"{seg}.jpg"; cv2.imwrite(str(p), canvas, [cv2.IMWRITE_JPEG_QUALITY, 80])
    idx.append(dict(seg=seg, strip=p.name, first=fr[0], last=fr[-1], tiles=len(fr), stride=fr[1] - fr[0] if len(fr) > 1 else 1,
                    max_cf_frame=max(fr, key=lambda f: float(meas[f][cfk] or 0))))
with open(V / "tables/strip_frames.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["seg", "frame"]); w.writerows((seg, f) for seg, fr in plan for f in fr)
with open(V / "tables/strip_index.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(idx[0]) if idx else ["seg"]); w.writeheader(); w.writerows(idx)
print(V.name, len(idx), "strips")
