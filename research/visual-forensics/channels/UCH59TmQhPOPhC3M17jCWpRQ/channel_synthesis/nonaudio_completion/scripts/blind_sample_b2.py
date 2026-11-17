# Blind batch 2: every unsampled tile-only row labelled STATIC_HOLD whose dense measurement is LOC/BOTH/CAM (label contradicts
# measurement). Same sheet builder and frozen brief as batch 1.
# Builds UNLABELLED sheets (interval id + frame numbers only). Camera rows use full frames; others use residual-bbox crop.
import csv, random, cv2, numpy as np, json, hashlib
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'
OUT = N / 'r13_blind/batch2'; VIDS = ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']; rng = random.Random(20261105)
sample = []
B1 = {r['interval_id'] for r in csv.DictReader(open(N / 'r13_blind/BLIND_SAMPLE_INDEX.csv'))}
for vid in VIDS:
    for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}.csv')):
        if r['event_class'] == 'STATIC_HOLD' and r['measured_class'] in ('LOC', 'BOTH', 'CAM') and r['review_status'] == 'VISUALLY_NAMED_TILES' and r['interval_id'] not in B1:
            sample.append((vid, r, 'STATIC_LABEL_VS_MEASURED_CHANGE'))
dm = {}
for vid in VIDS: dm[vid] = {int(r['frame']): r['residual_bbox'] for r in csv.DictReader(open(N / f'dense/DENSE_MOTION_{vid}.csv'))}
idx = []; TW, TH, PER = 460, 520, 3
for vid in VIDS:
    plan = {}
    for v, r, why in sample:
        if v != vid: continue
        a, b = int(r['start_frame']), int(r['end_frame'])
        fr = list(range(a - 1, b + 2))[:8] if b - a < 6 else sorted(set(np.linspace(a - 1, b + 1, 8).astype(int)))
        bb = [list(map(int, dm[vid][f].replace('x', '-').split('-'))) for f in range(a, b + 1) if dm[vid].get(f)]
        full = why == 'CAMERA_UNCERTAIN' or not bb
        box = (0, 1919, 0, 1079) if full else (max(0, min(x[0] for x in bb) - 40), min(1919, max(x[1] for x in bb) + 40), max(0, min(x[2] for x in bb) - 40), min(1079, max(x[3] for x in bb) + 40))
        plan[r['interval_id']] = (fr, box, why)
    want = {f for fr, _, _ in plan.values() for f in fr}; F = {}
    cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); i = 0
    while True:
        ok, im = cap.read()
        if not ok: break
        if i in want: F[i] = im
        i += 1
    ids = list(plan); (OUT / 'sheets_local_only').mkdir(parents=True, exist_ok=True)
    for s in range(0, len(ids), PER):
        sheet = np.full((PER * (TH + 40), 4 * TW, 3), 255, np.uint8); name = f'{vid}_D{s // PER + 1:03d}.jpg'
        for k, iid in enumerate(ids[s:s + PER]):
            fr, (x0, x1, y0, y1), why = plan[iid]; y = k * (TH + 40)
            cv2.putText(sheet, f'{iid}  crop x{x0}-{x1} y{y0}-{y1}', (4, y + 14), 0, 0.5, (0, 0, 0), 1)
            for j, f in enumerate(fr):
                if f not in F: continue
                c = F[f][y0:y1 + 1, x0:x1 + 1]; sc = min((TW - 8) / c.shape[1], (TH // 2 - 14) / c.shape[0])
                c = cv2.resize(c, (max(1, int(c.shape[1] * sc)), max(1, int(c.shape[0] * sc))), interpolation=cv2.INTER_AREA if sc < 1 else cv2.INTER_NEAREST)
                gx, gy = (j % 4) * TW, y + 20 + (j // 4) * (TH // 2 + 10)
                sheet[gy + 12:gy + 12 + c.shape[0], gx:gx + c.shape[1]] = c
                cv2.putText(sheet, f'f{f}', (gx + 2, gy + 10), 0, 0.42, (200, 0, 0), 1)
            idx.append(dict(video=vid, sheet=name, interval_id=iid, frames=' '.join(map(str, fr)), crop=f'{x0}-{x1}x{y0}-{y1}', sample_reason=why))
        cv2.imwrite(str(OUT / 'sheets_local_only' / name), sheet, [cv2.IMWRITE_JPEG_QUALITY, 88])
with open(OUT / 'BLIND_SAMPLE_INDEX.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(idx[0])); w.writeheader(); w.writerows(idx)
# reviewer-visible index has no sample_reason
with open(OUT / 'BLIND_SHEET_INDEX_FOR_REVIEWER.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['video', 'sheet', 'interval_id', 'frames', 'crop']); w.writeheader(); w.writerows([{k: r[k] for k in ['video', 'sheet', 'interval_id', 'frames', 'crop']} for r in idx])
from collections import Counter; print(len(idx), Counter(r['sample_reason'] for r in idx), Counter(r['video'] for r in idx))
