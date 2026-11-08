# usage: measure_band.py SRC WS Y_SPLIT  -> WS/tables/band_metrics.csv, caption_events.csv, content_episodes.csv
# For videos with a burned-in caption band: rows >= Y_SPLIT are CAPTION track, rows < Y_SPLIT are CONTENT track (full-res diff >25 counts).
import cv2, csv, sys, numpy as np, json
src, ws, ysplit = sys.argv[1], sys.argv[2], int(sys.argv[3]); pts = json.load(open(f'{ws}/tables/pts.json')); cap = cv2.VideoCapture(src); prev = None; rows = []; i = 0
while True:
    ok, f = cap.read()
    if not ok: break
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    if prev is None: rows.append([0, pts[0], 0, 0, 0.0])
    else:
        d = cv2.absdiff(g, prev) > 25; c = int(d[:ysplit].sum()); k = int(d[ysplit:].sum())
        sm = cv2.resize(g[:ysplit], (160, 120), interpolation=cv2.INTER_AREA).astype(np.int16); rows.append([i, pts[i], c, k, 0.0]); rows[-1][4] = float((np.abs(sm - psm) > 10).mean())
    psm = cv2.resize(g[:ysplit], (160, 120), interpolation=cv2.INTER_AREA).astype(np.int16); prev = g; i += 1
with open(f'{ws}/tables/band_metrics.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['frame', 'pts_time', 'content_px_thr25', 'caption_px_thr25', 'content_frac160']); w.writerows(rows)
def clusters(vals, gap):
    act = [r[0] for r in rows if vals(r)]; out = []; cur = None
    for a in act:
        if cur and a - cur[1] <= gap: cur[1] = a
        else:
            if cur: out.append(cur)
            cur = [a, a]
    if cur: out.append(cur)
    return out
cap_ev = clusters(lambda r: r[3] >= 150, 1); con_ev = clusters(lambda r: r[2] >= 150 or r[4] >= 0.0008, 3)
for name, ev, col in (('caption_events', cap_ev, 3), ('content_episodes', con_ev, 2)):
    with open(f'{ws}/tables/{name}.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['id', 'start_frame', 'end_frame', 'start_pts', 'end_pts', 'n', 'peak_px']); 
        for k, (a, b) in enumerate(ev): w.writerow([f"{'CAP' if col == 3 else 'CON'}{k+1:04d}", a, b, pts[a], pts[b], b - a + 1, max(r[col] for r in rows[a:b+1])])
print('caption events', len(cap_ev), 'content episodes', len(con_ev))
