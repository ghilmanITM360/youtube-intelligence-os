# Native-frame evidence for reconciliation: for each interval, frames start-1, start, end, end+1 at native resolution
# (crop = bbox of pixels changing >25 across those frames, padded 60 px, or full frame scaled) plus absdiff(start-1,start)
# and absdiff(start,end). Local only: derived frames are never published. Usage: b2_native_evidence.py OUTDIR id [id...]
import csv, cv2, sys, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True); ids = sys.argv[2:]
V = {'uPQc': 'uPQcyookL0Y', 'mNLN': 'mNLNb-Z4T0M', 'GNaB': 'GNaBxt_zIRA'}; idx = []
for pre, vid in V.items():
    L = {r['interval_id']: r for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}.csv'))}
    want = [i for i in ids if i.startswith(pre)]
    if not want: continue
    cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4'))))
    def fr(i): cap.set(cv2.CAP_PROP_POS_FRAMES, i); return cap.read()[1]
    for iid in want:
        a, b = int(L[iid]['start_frame']), int(L[iid]['end_frame']); F = [(f, fr(f)) for f in sorted({a - 1, a, b, b + 1})]
        # bbox ignores the end+1 frame, which may be a cut
        g = [cv2.cvtColor(x, cv2.COLOR_BGR2GRAY) for f, x in F if f <= b]; d = np.zeros_like(g[0], bool)
        for x, y in zip(g, g[1:]): d |= cv2.absdiff(x, y) > 25
        ys, xs = np.nonzero(d); box = (0, 1919, 0, 1079) if len(xs) == 0 else (max(0, xs.min() - 60), min(1919, xs.max() + 60), max(0, ys.min() - 60), min(1079, ys.max() + 60))
        x0, x1, y0, y1 = map(int, box); tiles = [(f'f{f}', x[y0:y1 + 1, x0:x1 + 1]) for f, x in F]
        fa, fb = dict(F)[a], dict(F)[b]
        dif = lambda p, q: cv2.cvtColor(np.clip(cv2.absdiff(p, q)[y0:y1 + 1, x0:x1 + 1].astype(int) * 3, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB)
        tiles += [(f'|f{a-1}-f{a}|x3', dif(dict(F)[a - 1], fa)), (f'|f{a}-f{b}|x3', dif(fa, fb))]
        h, w = tiles[0][1].shape[:2]; sc = min(1.0, 760 / w, 480 / h); sh = (int(h * sc), int(w * sc)); rows = []
        for j in range(0, len(tiles), 2):
            r = []
            for lab, im in tiles[j:j + 2]:
                im = cv2.resize(im, (sh[1], sh[0]), interpolation=cv2.INTER_AREA if sc < 1 else cv2.INTER_NEAREST); im = cv2.copyMakeBorder(im, 22, 4, 4, 4, cv2.BORDER_CONSTANT, value=(255, 255, 255)); cv2.putText(im, lab, (4, 16), 0, 0.5, (200, 0, 0), 1); r.append(im)
            if len(r) == 1: r.append(np.full_like(r[0], 255))
            rows.append(np.hstack(r))
        cv2.imwrite(str(OUT / f'{iid}.jpg'), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 90])
        idx.append(dict(interval_id=iid, start=a, end=b, crop=f'{x0}-{x1}x{y0}-{y1}', scale=round(sc, 3)))
with open(OUT / 'INDEX.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(idx[0])); w.writeheader(); w.writerows(idx)
print(len(idx))
