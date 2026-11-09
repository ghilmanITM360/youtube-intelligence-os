# usage: repsheets.py SRC WS  -> WS/frames/state_rep_NN.jpg (one decoded representative frame per state, 18 per sheet)
import cv2, csv, sys, numpy as np
src, ws = sys.argv[1:3]; TW = 190
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); need = {int(s['rep_frame']) for s in st}; cap = cv2.VideoCapture(src); fr = {}; i = 0
while i <= max(need):
    ok, f = cap.read()
    if not ok: break
    if i in need: fr[i] = f
    i += 1
tl = []
for s in st:
    f = fr[int(s['rep_frame'])]; h, w = f.shape[:2]; x = cv2.resize(f, (TW, int(TW*h/w)), interpolation=cv2.INTER_AREA)
    cv2.rectangle(x, (0, 0), (TW, 13), (255, 255, 255), -1); cv2.putText(x, f"{s['visual_state_id']} f{s['rep_frame']}", (2, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1); tl.append(x)
per = 18
for k in range(0, len(tl), per):
    r = tl[k:k+per]
    while len(r) < per: r.append(np.full_like(tl[0], 128))
    cv2.imwrite(f'{ws}/frames/state_rep_{k//per+1:02d}.jpg', np.vstack([np.hstack(r[j:j+6]) for j in range(0, per, 6)]), [cv2.IMWRITE_JPEG_QUALITY, 82])
print(len(tl), 'states ->', (len(tl)+per-1)//per, 'sheets')
