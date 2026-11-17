# Deterministic support for reconciling BLIND_REVIEW.csv: for every sampled interval, chained ORB+RANSAC similarity over
# <=10-frame steps from start to end frame (same frozen thresholds as cam_endpoint.py), plus the largest single-frame
# full-frame mean-abs-diff jump inside [start-1, end+1] with its frame (cut candidate) and whether it is the boundary.
import csv, cv2, numpy as np, sys
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'
D = N / (sys.argv[1] if len(sys.argv) > 1 else 'r13_blind'); RV = sys.argv[2] if len(sys.argv) > 2 else 'BLIND_REVIEW.csv'
S = list(csv.DictReader(open(D / 'BLIND_SAMPLE_INDEX.csv'))); L = {}
for v in ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']:
    for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{v}.csv')): L[r['interval_id']] = r
orb = cv2.ORB_create(4000); out = []
# v2 rule (added after first run, before adjudication): a similarity fit is a CAMERA move only if the RANSAC inliers of
# every link span >=50% of frame width AND height (background-wide support); otherwise NO_FRAMEWIDE_SUPPORT
# (the dominant matched feature set moved but does not span the frame, e.g. a character on a blank background: camera not established).
for vid in ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']:
    rows = [s for s in S if s['video'] == vid]; need = set()
    for s in rows:
        a, b = int(L[s['interval_id']]['start_frame']), int(L[s['interval_id']]['end_frame']); need |= set(range(a - 1, b + 2))
    F = {}; cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); i = 0; lo, hi = min(need), max(need)
    cap.set(cv2.CAP_PROP_POS_FRAMES, lo); i = lo
    while i <= hi:
        ok, im = cap.read()
        if not ok: break
        if i in need: F[i] = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        i += 1
    for s in rows:
        a, b = int(L[s['interval_id']]['start_frame']), int(L[s['interval_id']]['end_frame'])
        fs = sorted(set(list(range(a, b, 10)) + [b])); T = np.eye(3); mn = 10**9; sp = 1.0
        for x, y in zip(fs, fs[1:]):
            ka, da = orb.detectAndCompute(F[x], None); kb, db = orb.detectAndCompute(F[y], None)
            m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(da, db) if da is not None and db is not None else []
            M, inl = cv2.estimateAffinePartial2D(np.float32([ka[k.queryIdx].pt for k in m]), np.float32([kb[k.trainIdx].pt for k in m]), method=cv2.RANSAC, ransacReprojThreshold=2.0) if len(m) >= 8 else (None, None)
            mn = min(mn, int(inl.sum()) if inl is not None else 0)
            if inl is not None and inl.sum() > 0:
                P = np.float32([ka[k.queryIdx].pt for k in m])[inl.ravel() == 1]; sp = min(sp, (P[:, 0].max() - P[:, 0].min()) / 1920, (P[:, 1].max() - P[:, 1].min()) / 1080)
            else: sp = 0
            T = np.vstack([M, [0, 0, 1]]) @ T if M is not None else T
        if len(fs) < 2: mn = 0
        sc = float(np.hypot(T[0, 0], T[1, 0])); t = float(np.hypot(*((T @ [960, 540, 1])[:2] - [960, 540])))
        v = 'CAMERA_VERIFIED' if mn >= 40 and (abs(sc - 1) >= 0.005 or t >= 3) else 'CAMERA_REJECTED' if mn >= 40 and abs(sc - 1) < 0.002 and t < 1.5 else 'UNRESOLVED'
        if v == 'CAMERA_VERIFIED' and sp < 0.5: v = 'NO_FRAMEWIDE_SUPPORT'
        d = [(float(np.mean(cv2.absdiff(F[f], F[f - 1]))), f) for f in range(a, b + 2) if f in F and f - 1 in F]
        jm, jf = max(d) if d else (0, None)
        out.append(dict(video=vid, interval_id=s['interval_id'], start=a, end=b, links=len(fs) - 1, min_link_inliers=mn if len(fs) > 1 else 0, scale=round(sc, 5), centre_shift_px=round(t, 2), camera_measured=v, inlier_spread=round(float(sp), 3) if len(fs) > 1 else 0,
                        max_jump_mad=round(jm, 2), max_jump_frame=jf, jump_at=('NEXT_STATE_BOUNDARY' if jf == b + 1 else 'INTERVAL_START' if jf == a else 'INSIDE') if jf else ''))
with open(D / 'BLIND_ADJUDICATION_MEASURE.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
import collections; print(collections.Counter(o['camera_measured'] for o in out))
B = {r['interval_id']: r for r in csv.DictReader(open(D / RV))}
for o in out:
    b = B[o['interval_id']]
    if b['event_class'] == 'SHOT_CUT' or b['camera_move'] not in ('NONE', 'UNSURE') or o['max_jump_mad'] > 20:
        print(o['interval_id'], b['event_class'], b['camera_move'], '| meas', o['camera_measured'], o['scale'], o['centre_shift_px'], o['min_link_inliers'], '| jump', o['max_jump_mad'], o['max_jump_frame'], o['jump_at'], o['start'], o['end'])
