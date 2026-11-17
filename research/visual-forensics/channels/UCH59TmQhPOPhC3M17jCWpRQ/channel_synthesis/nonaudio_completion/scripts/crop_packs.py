# Native-resolution crop packs for intervals a dense reviewer flagged needs_native_crop=YES.
# Per interval: up to 8 frames (all if short), cropped to the union residual bbox (dense CSV) +40px, native pixels, tile max 460x260.
import csv, sys, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; vid = sys.argv[1]
rev = [r for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_{vid}_v1.csv')) if r['needs_native_crop'] == 'YES']
iv = {r['interval_id']: r for r in csv.DictReader(open(N / 'dense/DENSE_INTERVAL_CLASSIFICATION_v1.csv')) if r['video'] == vid}
dm = {int(r['frame']): r['residual_bbox'] for r in csv.DictReader(open(N / f'dense/DENSE_MOTION_{vid}.csv'))}
plan = {}
for r in rev:
    a, b = int(iv[r['interval_id']]['start_frame']), int(iv[r['interval_id']]['end_frame'])
    fr = list(range(a - 1, b + 2)) if b - a < 6 else sorted(set(np.linspace(a - 1, b + 1, 8).astype(int)))
    bb = [list(map(int, dm[f].replace('x', '-').split('-'))) for f in range(a, b + 1) if dm.get(f)]
    x0, x1, y0, y1 = (min(x[0] for x in bb), max(x[1] for x in bb), min(x[2] for x in bb), max(x[3] for x in bb)) if bb else (0, 1919, 0, 1079)
    plan[r['interval_id']] = (fr[:8], (max(0, x0 - 40), min(1919, x1 + 40), max(0, y0 - 40), min(1079, y1 + 40)))
want = {f for fr, _ in plan.values() for f in fr}; F = {}; cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); i = 0
while True:
    ok, im = cap.read()
    if not ok: break
    if i in want: F[i] = im
    i += 1
TW, TH, PER = 460, 520, 3; out = N / 'dense_review/crops_local_only' / vid; out.mkdir(parents=True, exist_ok=True); idx = []
ids = list(plan)
for s in range(0, len(ids), PER):
    sheet = np.full((PER * (TH + 40), 4 * TW, 3), 255, np.uint8); name = f'{vid}_C{s // PER + 1:03d}.jpg'
    for k, iid in enumerate(ids[s:s + PER]):
        fr, (x0, x1, y0, y1) = plan[iid]; y = k * (TH + 40)
        cv2.putText(sheet, f'{iid}  crop x{x0}-{x1} y{y0}-{y1}  (8 tiles: 2 rows x 4)', (4, y + 14), 0, 0.5, (0, 0, 0), 1)
        for j, f in enumerate(fr):
            if f not in F: continue
            c = F[f][y0:y1 + 1, x0:x1 + 1]; sc = min((TW - 8) / c.shape[1], (TH // 2 - 14) / c.shape[0]); c = cv2.resize(c, (max(1, int(c.shape[1] * sc)), max(1, int(c.shape[0] * sc))), interpolation=cv2.INTER_AREA if sc < 1 else cv2.INTER_NEAREST)
            gx, gy = (j % 4) * TW // 1 // 1, y + 20 + (j // 4) * (TH // 2 + 10)
            gx = (j % 4) * TW; sheet[gy + 12:gy + 12 + c.shape[0], gx:gx + c.shape[1]] = c
            cv2.putText(sheet, f'f{f}', (gx + 2, gy + 10), 0, 0.42, (200, 0, 0), 1)
        idx.append(dict(video=vid, sheet=name, interval_id=iid, frames=' '.join(map(str, fr)), crop=f'{x0}-{x1}x{y0}-{y1}'))
    cv2.imwrite(str(out / name), sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])
with open(N / f'dense_review/CROP_INDEX_{vid}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(idx[0])); w.writeheader(); w.writerows(idx)
print(vid, len(ids), 'intervals', -(-len(ids) // PER), 'sheets')
