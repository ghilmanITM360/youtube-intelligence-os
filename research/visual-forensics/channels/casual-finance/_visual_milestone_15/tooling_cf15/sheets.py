# usage: sheets.py SRC WS overview|episodes [tile_w]  -> WS/frames/*.jpg  (bounded JPEG evidence sheets; labels frame index + PTS)
import cv2, csv, sys, json, numpy as np, os
src, ws, mode = sys.argv[1:4]; TW = int(sys.argv[4]) if len(sys.argv) > 4 else 270
pts = json.load(open(f'{ws}/tables/pts.json')); os.makedirs(f'{ws}/frames', exist_ok=True)
cap = cv2.VideoCapture(src); fps = round(1 / (pts[1] - pts[0]))
def grab(idx):
    out = {}; need = sorted(set(idx)); i = 0
    while i <= need[-1]:
        ok, f = cap.read()
        if not ok: break
        if i in need: out[i] = f
        i += 1
    return out
def tile(f, label, tw):
    h, w = f.shape[:2]; th = int(tw * h / w); t = cv2.resize(f, (tw, th), interpolation=cv2.INTER_AREA)
    cv2.rectangle(t, (0, 0), (tw, 16), (255, 255, 255), -1); cv2.putText(t, label, (3, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 0, 255), 1); return t
def pack(tiles, cols, name):
    th, tw = tiles[0].shape[:2]; rows = []
    for k in range(0, len(tiles), cols):
        r = tiles[k:k+cols]
        while len(r) < cols: r.append(np.full((th, tw, 3), 128, np.uint8))
        rows.append(np.hstack(r))
    cv2.imwrite(f'{ws}/frames/{name}', np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 82])
if mode == 'overview':
    idx = list(range(0, len(pts), fps)) + [len(pts) - 1]; fr = grab(idx); tl = [tile(fr[i], f'f{i} t{pts[i]:.2f}', TW) for i in idx]
    per = 18
    for k in range(0, len(tl), per): pack(tl[k:k+per], 6, f'overview_{k//per+1:02d}.jpg')
    print(len(idx), 'overview tiles')
else:
    efile = sys.argv[6] if len(sys.argv) > 6 else 'episodes.csv'; pref = sys.argv[7] if len(sys.argv) > 7 else 'episodes'; ep = [dict(e, ep=e.get('ep') or e.get('id')) for e in csv.DictReader(open(f'{ws}/tables/{efile}'))]; spec = []
    for e in ep:
        a, b = int(e['start_frame']), int(e['end_frame']); mid = (a + b) // 2
        fl = sorted({max(a - 1, 0), a, mid, b, min(b + 1, len(pts) - 1)}); spec.append((e['ep'], fl))
    need = [i for _, fl in spec for i in fl]; fr = grab(need)
    rows = []
    for eid, fl in spec:
        t = [tile(fr[i], f'{eid} f{i}', TW) for i in fl]
        while len(t) < 5: t.append(np.full_like(t[0], 128))
        rows.append(np.hstack(t[:5]))
    per = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    for k in range(0, len(rows), per): cv2.imwrite(f'{ws}/frames/{pref}_{k//per+1:02d}.jpg', np.vstack(rows[k:k+per]), [cv2.IMWRITE_JPEG_QUALITY, 80])
    print(len(rows), 'episode strips ->', (len(rows) + per - 1) // per, 'sheets')
