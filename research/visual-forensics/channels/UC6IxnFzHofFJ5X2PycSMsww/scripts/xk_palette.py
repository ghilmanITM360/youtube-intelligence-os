"""Measured palette per video from settled HOLD frames (native resolution). Quantises to 8-level/channel bins,
reports background mode, ink share, accent hues and canvas ink coverage per hold. Usage: python -I xk_palette.py <video_dir>"""
import csv, json, sys, pathlib, cv2, numpy as np
V = pathlib.Path(sys.argv[1]).resolve()
segs = [s for s in csv.DictReader(open(V / "tables/segments_v1.csv")) if s["kind"] == "HOLD"]
need = {int(s["end_frame"]): s["seg"] for s in segs}
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip())
hist = {}; per = []; k = 0; last = max(need)
while k <= last:
    ok, im = cap.read()
    if not ok: break
    if k in need:
        q = (im // 32).reshape(-1, 3); keys, cnt = np.unique(q, axis=0, return_counts=True)
        for kk, c in zip(map(tuple, keys), cnt): hist[kk] = hist.get(kk, 0) + int(c)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV); g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ink = float((g < 128).mean()); fill = float(((g >= 128) & (g < 225)).mean())
        red = float((((hsv[..., 0] < 10) | (hsv[..., 0] > 170)) & (hsv[..., 1] > 90) & (hsv[..., 2] > 60)).mean())
        sat = float((hsv[..., 1] > 60).mean())
        per.append(dict(seg=need[k], frame=k, dark_ink_frac=round(ink, 4), mid_grey_frac=round(fill, 4), red_accent_frac=round(red, 5), saturated_frac=round(sat, 5)))
    k += 1
tot = sum(hist.values()); top = sorted(hist.items(), key=lambda x: -x[1])[:10]
def hexbin(b): bgr = [int(x) * 32 + 16 for x in b]; return "#%02X%02X%02X" % (bgr[2], bgr[1], bgr[0])
# exact background value: mode of full-res pixels in brightest bin of first hold frame
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); ok, im0 = cap.read()
vals, cnt = np.unique(im0.reshape(-1, 3), axis=0, return_counts=True); bg = vals[cnt.argmax()]
out = dict(method="8-level/channel quantised histogram over settled HOLD frames (native res); bin centres reported; background = exact modal RGB of frame 0",
           background_exact_rgb="#%02X%02X%02X" % (bg[2], bg[1], bg[0]),
           top_bins=[dict(hex_bin_centre=hexbin(b), share=round(c / tot, 4)) for b, c in top],
           holds=len(per), mean_dark_ink_frac=round(float(np.mean([p["dark_ink_frac"] for p in per])), 4),
           max_dark_ink_frac=max(p["dark_ink_frac"] for p in per), holds_with_red_accent=sum(p["red_accent_frac"] > 0.0005 for p in per),
           holds_with_any_saturation=sum(p["saturated_frac"] > 0.001 for p in per), per_hold=per)
(V / "tables/palette_measured.json").write_text(json.dumps(out, indent=1))
print({k: v for k, v in out.items() if k not in ("per_hold",)})
