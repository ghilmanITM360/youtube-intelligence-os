# usage: epcrops.py SRC WS [efile] [rows_per_sheet] -> WS/frames/epc_NN.jpg and WS/tables/episode_bbox.csv
# Per episode row: [context frame at start with changed-pixel bbox (red)] [crop of bbox at start-1] [crop of bbox at start (first changed frame)].
# Evidence for what changed, including tiny local changes; bbox from full-res |diff|>25 between f-1 and f.
import cv2, csv, sys, json, numpy as np
src, ws = sys.argv[1:3]; efile = sys.argv[3] if len(sys.argv) > 3 else 'episodes.csv'; R = int(sys.argv[4]) if len(sys.argv) > 4 else 8
eps = [dict(e, ep=e.get('ep') or e.get('id')) for e in csv.DictReader(open(f'{ws}/tables/{efile}'))]
need = set()
for e in eps: a = int(e['start_frame']); need |= {a - 1, a}
need = sorted(x for x in need if x >= 0); cap = cv2.VideoCapture(src); fr = {}; i = 0
while i <= need[-1]:
    ok, f = cap.read()
    if not ok: break
    if i in need: fr[i] = f
    i += 1
W, H = 300, 169
def fit(img):
    h, w = img.shape[:2]; s = min(W / w, H / h); r = cv2.resize(img, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_CUBIC if s > 1 else cv2.INTER_AREA)
    c = np.full((H, W, 3), 128, np.uint8); c[:r.shape[0], :r.shape[1]] = r; return c
rows = []; bb = []
for e in eps:
    a = int(e['start_frame']); p, c = fr[max(a - 1, 0)], fr[a]
    d = (cv2.absdiff(p, c).max(axis=2) > 25); ys, xs = np.where(d)
    if len(ys) == 0: x0, y0, x1, y1 = 0, 0, c.shape[1], c.shape[0]
    else: x0, x1, y0, y1 = int(xs.min()), int(xs.max()) + 1, int(ys.min()), int(ys.max()) + 1
    bb.append(dict(ep=e['ep'], start_frame=a, changed_px=int(d.sum()), x0=x0, y0=y0, x1=x1, y1=y1))
    pad = 12; X0, Y0, X1, Y1 = max(x0 - pad, 0), max(y0 - pad, 0), min(x1 + pad, c.shape[1]), min(y1 + pad, c.shape[0])
    ctx = c.copy(); cv2.rectangle(ctx, (x0, y0), (x1, y1), (0, 0, 255), 4)
    t = [fit(ctx), fit(p[Y0:Y1, X0:X1]), fit(c[Y0:Y1, X0:X1])]
    row = np.hstack(t); lab = f"{e['ep']} f{a}-{e['end_frame']} px{int(d.sum())} bbox({x0},{y0})-({x1},{y1})  [context | f{a-1} crop | f{a} crop]"
    cv2.rectangle(row, (0, 0), (row.shape[1], 14), (255, 255, 255), -1); cv2.putText(row, lab, (3, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 0, 255), 1); rows.append(row)
for k in range(0, len(rows), R):
    cv2.imwrite(f'{ws}/frames/epc_{k // R + 1:02d}.jpg', np.vstack(rows[k:k + R]), [cv2.IMWRITE_JPEG_QUALITY, 85])
with open(f'{ws}/tables/episode_bbox.csv', 'w', newline='') as f:
    q = csv.DictWriter(f, fieldnames=list(bb[0])); q.writeheader(); q.writerows(bb)
print(len(rows), 'rows,', (len(rows) + R - 1) // R, 'sheets')
