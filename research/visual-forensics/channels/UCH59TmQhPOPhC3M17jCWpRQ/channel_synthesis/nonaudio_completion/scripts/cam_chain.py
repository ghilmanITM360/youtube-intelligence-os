# Third method (orchestrator, after visual look): chain ORB+RANSAC similarity over 10-frame steps inside the interval and
# compose. Same frozen thresholds as cam_endpoint.py, applied to the composed transform; every link needs >=40 inliers.
import csv, cv2, numpy as np
from pathlib import Path
SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; N = Path(__file__).resolve().parents[1]
cap = cv2.VideoCapture(str(next(SRC.glob('*mNLNb-Z4T0M*.mp4')))); orb = cv2.ORB_create(4000); out = []
def g(i):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, im = cap.read(); return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
for iid, a, b in [('mNLN-U0029', 1256, 1354), ('mNLN-U0081', 3946, 4060), ('mNLN-U0228', 12273, 12355), ('mNLN-U0258', 14467, 14551)]:
    fs = list(range(a, b, 10)) + [b]; T = np.eye(3); mn = 10**9
    for x, y in zip(fs, fs[1:]):
        A, B = g(x), g(y); ka, da = orb.detectAndCompute(A, None); kb, db = orb.detectAndCompute(B, None)
        m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(da, db)
        M, inl = cv2.estimateAffinePartial2D(np.float32([ka[k.queryIdx].pt for k in m]), np.float32([kb[k.trainIdx].pt for k in m]), method=cv2.RANSAC, ransacReprojThreshold=2.0)
        mn = min(mn, int(inl.sum()) if inl is not None else 0); T = np.vstack([M, [0, 0, 1]]) @ T if M is not None else T
    s = float(np.hypot(T[0, 0], T[1, 0])); t = float(np.hypot(*((T @ [960, 540, 1])[:2] - [960, 540])))
    v = 'CAMERA_VERIFIED' if mn >= 40 and (abs(s - 1) >= 0.005 or t >= 3) else 'CAMERA_REJECTED' if mn >= 40 and abs(s - 1) < 0.002 and t < 1.5 else 'UNRESOLVED'
    out.append(dict(interval_id=iid, frame_a=a, frame_b=b, links=len(fs) - 1, min_link_inliers=mn, scale=round(s, 5), centre_shift_px=round(t, 2), verdict=v)); print(out[-1])
with open(N / 'r13_blind/CAMERA_CHAIN_CHECK.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
