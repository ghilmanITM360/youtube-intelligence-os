# Sensitivity of M0/M1/M2/M3 on all intervals, M3 vs native adjudication on sampled rows, and blind held-out sheet builder.
# Held-out labels are hidden in method_v3/HELDOUT_KEY_local.csv until the orchestrator's labels are frozen.
import csv, json, random, collections, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; M = N / 'method_v3'; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; VIDS = ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']
R = []
for v in VIDS: R += list(csv.DictReader(open(M / f'CAMERA_M3_{v}.csv')))
m1 = lambda r: 'CAMERA_VERIFIED' if r['camera_m2'] in ('CAMERA_VERIFIED', 'NO_FRAMEWIDE_SUPPORT') else r['camera_m2']
S = dict(rows=len(R), M0_endpoint_reapplied=collections.Counter(r['m0_endpoint_all'] for r in R), M1_chain=collections.Counter(m1(r) for r in R), M2_chain_spread=collections.Counter(r['camera_m2'] for r in R), M3=collections.Counter(r['camera_m3'] for r in R), M2_to_M3=collections.Counter(f"{r['camera_m2']}->{r['camera_m3']}" for r in R))
json.dump(S, open(M / 'METHOD_SENSITIVITY.json', 'w'), indent=1); print(json.dumps(S))
A = {r['interval_id']: r for r in csv.DictReader(open(M / 'NATIVE_ADJUDICATION_ORCH.csv'))}; by = {r['interval_id']: r for r in R}
for i, a in A.items():
    r = by[i]; print(i, a['final_class'], a['camera_attribution'], '| m3', r['camera_m3'], 'm2', r['camera_m2'], 'shr', r['moved_share'], 'sp', r['inlier_spread'], 's', r['scale'], 't', r['centre_shift_px'], 'loc', r['local_change_after_comp'], 'ent', r['entry_link_used'])
used = set(A) | {r['interval_id'] for r in csv.DictReader(open(N / 'r13_blind/BLIND_SAMPLE_INDEX.csv'))} | {r['interval_id'] for r in csv.DictReader(open(N / 'r13_blind/batch2/BLIND_SAMPLE_INDEX.csv'))}
rng = random.Random(20261106); groups = {'CAMERA_FRAMEWIDE': 6, 'WHOLE_CONTENT_MOVE': 6, 'OBJECT_MOVE': 6, 'NO_CAMERA': 6}; pick = []
for g, n in groups.items():
    pool = [r for r in R if r['camera_m3'] == g and r['interval_id'] not in used and int(r['end_frame']) > int(r['start_frame'])]; rng.shuffle(pool); pick += pool[:n]
rng.shuffle(pick); key = []
for k, r in enumerate(pick): key.append(dict(hid=f'H{k+1:02d}', interval_id=r['interval_id'], video=r['video'], start_frame=r['start_frame'], end_frame=r['end_frame'], camera_m3=r['camera_m3']))
with open(M / 'HELDOUT_KEY_local.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(key[0])); w.writeheader(); w.writerows(key)
(M / 'heldout_local_only').mkdir(exist_ok=True); caps = {v: cv2.VideoCapture(str(next(SRC.glob(f'*{v}*.mp4')))) for v in VIDS}
def fr(v, i): caps[v].set(cv2.CAP_PROP_POS_FRAMES, i); return caps[v].read()[1]
rows = []
for k in key:
    v, a, b = k['video'], int(k['start_frame']), int(k['end_frame']); A_, B_ = fr(v, a), fr(v, b); d = np.clip(cv2.absdiff(A_, B_).astype(int) * 3, 0, 255).astype(np.uint8)
    tiles = []
    for lab, im in [(f"{k['hid']} first", A_), ('last', B_), ('|first-last|x3', d)]:
        t = cv2.resize(im, (520, 292), interpolation=cv2.INTER_AREA); cv2.putText(t, lab, (4, 18), 0, 0.55, (0, 0, 220), 2); tiles.append(t)
    rows.append(np.hstack(tiles))
for s in range(0, len(rows), 4): cv2.imwrite(str(M / f'heldout_local_only/S{s//4+1}.jpg'), np.vstack(rows[s:s + 4]), [cv2.IMWRITE_JPEG_QUALITY, 85])
print('heldout', len(key), 'by group count only', {g: sum(1 for k in key if k['camera_m3'] == g) for g in groups})
