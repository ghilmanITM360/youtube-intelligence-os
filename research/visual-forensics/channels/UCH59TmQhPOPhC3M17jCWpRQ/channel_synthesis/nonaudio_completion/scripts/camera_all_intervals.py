# Measured camera component for EVERY dense-ledger interval (streaming decode). Same frozen rule as
# blind_adjudicate_measure.py v2: chained ORB+RANSAC similarity over <=10-frame steps start..end; CAMERA_VERIFIED needs
# every link >=40 inliers spanning >=50% of width and height and |scale-1|>=0.005 or centre shift>=3 px;
# CAMERA_REJECTED: >=40 inliers, |scale-1|<0.002, shift<1.5; NO_FRAMEWIDE_SUPPORT: verified-size move but
# inliers do not span the frame; else UNRESOLVED. Single-frame intervals: NOT_APPLICABLE.
import csv, sys, cv2, numpy as np
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; vid = sys.argv[1]
rows = list(csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}.csv')))
pts = {}
for r in rows:
    a, b = int(r['start_frame']), int(r['end_frame'])
    for f in sorted(set(list(range(a, b, 10)) + [b])): pts.setdefault(f, []).append(r['interval_id'])
orb = cv2.ORB_create(4000); st = {r['interval_id']: dict(prev=None, T=np.eye(3), mn=10**9, sp=1.0, links=0) for r in rows}
cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); i = 0; last = max(pts)
while i <= last:
    ok, im = cap.read()
    if not ok: break
    if i in pts:
        k, d = orb.detectAndCompute(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), None)
        for iid in pts[i]:
            s = st[iid]
            if s['prev'] is not None:
                ka, da = s['prev']; m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(da, d) if da is not None and d is not None else []
                M, inl = cv2.estimateAffinePartial2D(np.float32([ka[x.queryIdx].pt for x in m]), np.float32([k[x.trainIdx].pt for x in m]), method=cv2.RANSAC, ransacReprojThreshold=2.0) if len(m) >= 8 else (None, None)
                n = int(inl.sum()) if inl is not None else 0; s['mn'] = min(s['mn'], n); s['links'] += 1
                if n:
                    P = np.float32([ka[x.queryIdx].pt for x in m])[inl.ravel() == 1]; s['sp'] = min(s['sp'], (P[:, 0].max() - P[:, 0].min()) / 1920, (P[:, 1].max() - P[:, 1].min()) / 1080)
                else: s['sp'] = 0
                if M is not None: s['T'] = np.vstack([M, [0, 0, 1]]) @ s['T']
            s['prev'] = (k, d)
    i += 1
out = []
for r in rows:
    s = st[r['interval_id']]; T = s['T']; sc = float(np.hypot(T[0, 0], T[1, 0])); t = float(np.hypot(*((T @ [960, 540, 1])[:2] - [960, 540])))
    if s['links'] == 0: v = 'NOT_APPLICABLE'
    elif s['mn'] >= 40 and (abs(sc - 1) >= 0.005 or t >= 3): v = 'CAMERA_VERIFIED' if s['sp'] >= 0.5 else 'NO_FRAMEWIDE_SUPPORT'
    elif s['mn'] >= 40 and abs(sc - 1) < 0.002 and t < 1.5: v = 'CAMERA_REJECTED'
    else: v = 'UNRESOLVED'
    out.append(dict(video=vid, interval_id=r['interval_id'], start_frame=r['start_frame'], end_frame=r['end_frame'], links=s['links'], min_link_inliers=s['mn'] if s['links'] else 0, inlier_spread=round(s['sp'], 3) if s['links'] else 0, scale=round(sc, 5), centre_shift_px=round(t, 2), camera_measured=v, ledger_event_class=r['event_class']))
with open(N / f'dense/CAMERA_CHAIN_ALL_{vid}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
import collections; print(vid, collections.Counter(o['camera_measured'] for o in out))
