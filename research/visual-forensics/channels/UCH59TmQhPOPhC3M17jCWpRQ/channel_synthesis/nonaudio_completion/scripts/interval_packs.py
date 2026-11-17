# Build bounded visual evidence packs for every uninspected interval: per interval up to 6 tiles
# (pre, start, 1/3, 2/3, end, post), 10 intervals per sheet. Local-only JPGs + index CSV (published).
import csv, sys, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'
vid = sys.argv[1]; mp4 = next(SRC.glob(f'*{vid}*.mp4'))
rows = [r for r in csv.DictReader(open(N / 'dense/DENSE_INTERVAL_CLASSIFICATION_v1.csv')) if r['video'] == vid]
TW, TH, ROWS = 220, 124, 10
def picks(a, b):
    if b - a < 2: s = [a - 1, a, b, b + 1]
    else: s = [a - 1, a, a + (b - a) // 3, a + 2 * (b - a) // 3, b, b + 1]
    return list(dict.fromkeys(max(0, x) for x in s))
need = {}
for r in rows: need[r['interval_id']] = picks(int(r['start_frame']), int(r['end_frame']))
want = set(f for v in need.values() for f in v); frames = {}
cap = cv2.VideoCapture(str(mp4)); i = 0
while True:
    ok, im = cap.read()
    if not ok: break
    if i in want: frames[i] = cv2.resize(im, (TW, TH), interpolation=cv2.INTER_AREA)
    i += 1
out = N / 'dense_review/packs_local_only' / vid; out.mkdir(parents=True, exist_ok=True); idx = []
for s in range(0, len(rows), ROWS):
    chunk = rows[s:s + ROWS]; name = f'{vid}_P{s // ROWS + 1:03d}.jpg'
    sheet = np.full((len(chunk) * (TH + 18), 170 + 6 * TW, 3), 255, np.uint8)
    for k, r in enumerate(chunk):
        y = k * (TH + 18)
        for j, t in enumerate(f'{r["interval_id"]}|{r["state"]}|{r["start_frame"]}-{r["end_frame"]}|n{r["n_frames"]}|{r["dominant"]}'.split('|')):
            cv2.putText(sheet, t, (4, y + 18 + j * 22), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        for j, f in enumerate(need[r['interval_id']]):
            if f in frames:
                x = 170 + j * TW; sheet[y + 16:y + 16 + TH, x:x + TW] = frames[f]
                lab = ('pre ' if f < int(r['start_frame']) else 'post ' if f > int(r['end_frame']) else '') + str(f)
                cv2.putText(sheet, lab, (x + 3, y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (200, 0, 0), 1)
        idx.append(dict(video=vid, sheet=name, interval_id=r['interval_id'], tiles=' '.join(map(str, need[r['interval_id']]))))
    cv2.imwrite(str(out / name), sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])
with open(N / f'dense_review/PACK_INDEX_{vid}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(idx[0])); w.writeheader(); w.writerows(idx)
print(vid, len(rows), 'intervals', len(set(x['sheet'] for x in idx)), 'sheets', i, 'frames decoded')
