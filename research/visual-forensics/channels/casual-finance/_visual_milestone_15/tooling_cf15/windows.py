# usage: windows.py SRC WS NAME "a-b,c-d,..." [tile_w] -> WS/frames/NAME_NN.jpg ; one row per window of consecutive decoded frames (no interpolation)
import cv2, sys, json, numpy as np
src, ws, name, spec = sys.argv[1:5]; TW = int(sys.argv[5]) if len(sys.argv) > 5 else 170
W = [tuple(map(int, s.split('-'))) for s in spec.split(',')]; need = sorted({i for a, b in W for i in range(a, b + 1)})
cap = cv2.VideoCapture(src); fr = {}; i = 0
while i <= need[-1]:
    ok, f = cap.read()
    if not ok: break
    if i in need: fr[i] = f
    i += 1
def t(f, lab):
    h, w = f.shape[:2]; th = int(TW * h / w); x = cv2.resize(f, (TW, th), interpolation=cv2.INTER_AREA)
    cv2.rectangle(x, (0, 0), (TW, 14), (255, 255, 255), -1); cv2.putText(x, lab, (2, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1); return x
rows = []
for a, b in W:
    tl = [t(fr[k], f'f{k}') for k in range(a, b + 1)]; rows.append(np.hstack(tl))
mw = max(r.shape[1] for r in rows); rows = [np.hstack([r, np.full((r.shape[0], mw - r.shape[1], 3), 128, np.uint8)]) if r.shape[1] < mw else r for r in rows]
per = 4
for k in range(0, len(rows), per): cv2.imwrite(f'{ws}/frames/{name}_{k//per+1:02d}.jpg', np.vstack(rows[k:k+per]), [cv2.IMWRITE_JPEG_QUALITY, 82])
print(len(rows), 'windows')
