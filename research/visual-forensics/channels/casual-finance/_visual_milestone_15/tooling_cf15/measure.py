# usage: measure.py SRC WS  -> WS/tables/frame_metrics.csv (one decode pass; per-frame reduced-res + fullres change + 4x4 grid)
import cv2, csv, sys, numpy as np, json
src, ws = sys.argv[1:3]
pts = json.load(open(f'{ws}/tables/pts.json'))
cap = cv2.VideoCapture(src); prev = prevf = None; rows = []; i = 0
while True:
    ok, fr = cap.read()
    if not ok: break
    h, w = fr.shape[:2]; s = 320 / max(h, w); sm = cv2.resize(fr, (int(w*s), int(h*s)), interpolation=cv2.INTER_AREA)
    g = cv2.cvtColor(sm, cv2.COLOR_BGR2GRAY).astype(np.int16); gf = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    if prev is None: frac = mad = 0.0; ff = 0; grid = [0.0]*16
    else:
        d = np.abs(g - prev); frac = float((d > 10).mean()); mad = float(d.mean()); ff = int((cv2.absdiff(gf, prevf) > 25).sum())
        gh, gw = d.shape; grid = [float((d[r*gh//4:(r+1)*gh//4, c*gw//4:(c+1)*gw//4] > 10).mean()) for r in range(4) for c in range(4)]
    rows.append([i, pts[i] if i < len(pts) else '', round(float(g.mean()), 2), round(frac, 5), round(mad, 4), ff] + [round(x, 4) for x in grid])
    prev, prevf = g, gf; i += 1
with open(f'{ws}/tables/frame_metrics.csv', 'w', newline='') as f:
    wr = csv.writer(f); wr.writerow(['frame','pts_time','mean_luma','changed_frac_thr10','mean_abs_diff','fullres_changed_px_thr25'] + [f'g{r}{c}' for r in range(4) for c in range(4)]); wr.writerows(rows)
print(i, 'frames measured; size', w, 'x', h)
