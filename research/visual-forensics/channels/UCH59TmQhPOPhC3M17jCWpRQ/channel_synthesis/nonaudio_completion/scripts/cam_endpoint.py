# Resolve camera claims the per-frame tracker could not corroborate: robust ORB+RANSAC similarity between interval
# endpoints (f_start-1 vs f_end+1), full frames. Frozen rule (set before running): CAMERA_VERIFIED if inliers>=40 and
# (|scale-1|>=0.005 or |t|>=3 px); CAMERA_REJECTED if inliers>=40 and |scale-1|<0.002 and |t|<1.5; else UNRESOLVED.
import csv, cv2, numpy as np, json
from pathlib import Path
N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; out = []
for vid in ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']:
    rows = [r for r in csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}.csv')) if 'UNCERTAIN' in r['camera_claim_crosscheck']]
    cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4'))))
    def frame(i):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, im = cap.read(); return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(4000)
    for r in rows:
        a, b = int(r['start_frame']) - 1, int(r['end_frame']) + 1
        A, B = frame(a), frame(b); ka, da = orb.detectAndCompute(A, None); kb, db = orb.detectAndCompute(B, None)
        m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(da, db) if da is not None and db is not None else []
        M, inl = (None, None)
        if len(m) >= 8:
            M, inl = cv2.estimateAffinePartial2D(np.float32([ka[x.queryIdx].pt for x in m]), np.float32([kb[x.trainIdx].pt for x in m]), method=cv2.RANSAC, ransacReprojThreshold=2.0)
        n = int(inl.sum()) if inl is not None else 0
        s = float(np.hypot(M[0, 0], M[1, 0])) if M is not None else float('nan'); t = float(np.hypot(M[0, 2] + (s - 1) * 0, M[1, 2])) if M is not None else float('nan')
        # translation of the frame centre under M (separates zoom about centre from pan)
        if M is not None:
            c = np.array([960, 540, 1.0]); tc = M @ c - c[:2]; t = float(np.hypot(*tc))
        v = 'CAMERA_VERIFIED' if n >= 40 and (abs(s - 1) >= 0.005 or t >= 3) else 'CAMERA_REJECTED' if n >= 40 and abs(s - 1) < 0.002 and t < 1.5 else 'UNRESOLVED'
        out.append(dict(video=vid, interval_id=r['interval_id'], frame_a=a, frame_b=b, matches=len(m), inliers=n, scale=round(s, 5), centre_shift_px=round(t, 2), verdict=v, ledger_event_class=r['event_class'], ledger_what=r['what_changes'][:120]))
with open(N / 'r13_blind/CAMERA_ENDPOINT_CHECK.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for o in out: print(o['interval_id'], o['inliers'], o['scale'], o['centre_shift_px'], o['verdict'], '|', o['ledger_what'][:70])
