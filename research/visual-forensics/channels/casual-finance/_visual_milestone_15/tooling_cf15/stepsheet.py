# usage: stepsheet.py SRC WS NAME "a-b:step,..." [tile_w]  -> one row per range, every step-th decoded frame (sampling, NOT all-frame)
import cv2, sys, numpy as np
src, ws, name, spec = sys.argv[1:5]; TW = int(sys.argv[5]) if len(sys.argv) > 5 else 140
R = []
for s in spec.split(','):
    r, st = s.split(':'); a, b = map(int, r.split('-')); R.append(list(range(a, b + 1, int(st))))
need = sorted({i for r in R for i in r}); cap = cv2.VideoCapture(src); fr = {}; i = 0
while i <= need[-1]:
    ok, f = cap.read()
    if not ok: break
    if i in need: fr[i] = f
    i += 1
def t(f, lab):
    h, w = f.shape[:2]; th = int(TW * h / w); x = cv2.resize(f, (TW, th), interpolation=cv2.INTER_AREA)
    cv2.rectangle(x, (0, 0), (TW, 13), (255, 255, 255), -1); cv2.putText(x, lab, (2, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 0, 255), 1); return x
rows = [np.hstack([t(fr[k], f'f{k}') for k in r]) for r in R]; mw = max(r.shape[1] for r in rows)
rows = [np.hstack([r, np.full((r.shape[0], mw - r.shape[1], 3), 128, np.uint8)]) for r in rows]
cv2.imwrite(f'{ws}/frames/{name}.jpg', np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 82]); print([len(r) for r in R])
