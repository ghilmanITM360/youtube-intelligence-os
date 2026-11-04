"""Measured stroke width of black ink in native frames (distance-transform ridge, px at source resolution). Adds to tables/stroke_measured.json. Usage: python -I pe_stroke.py <video_dir>"""
import csv, json, sys, pathlib, cv2, numpy as np
V = pathlib.Path(sys.argv[1]).resolve(); cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); out = []
for r in csv.DictReader(open(V / "tables/native_frames.csv")):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(r["frame"])); ok, im = cap.read(); g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); m = (g < 90).astype(np.uint8)
    d = cv2.distanceTransform(m, cv2.DIST_L2, 5); ridge = (d == cv2.dilate(d, np.ones((3, 3), np.uint8))) & (d >= 1)
    w = 2 * d[ridge]; out.append(dict(frame=int(r["frame"]), seg=r["seg"], ridge_px=int(ridge.sum()), p25=round(float(np.percentile(w, 25)), 1), median=round(float(np.median(w)), 1), p75=round(float(np.percentile(w, 75)), 1)))
(V / "tables/stroke_measured.json").write_text(json.dumps(dict(method="2*distance transform on g<90, local maxima; includes solid fills so upper tail is not stroke", per_frame=out), indent=1)); print(out)
