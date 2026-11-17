# C3b background-static camera check: ORB similarity of every frame vs frame 0, keypoints restricted to the persistent
# background mask (pixels within L1<=36 of f0 in >=80% of frames). Too few background keypoints => cannot certify => FAIL.
# usage: bg_static_check.py MP4 [synthetic_pan_px]   -> prints JSON
import cv2, json, sys, numpy as np
mp4 = sys.argv[1]; pan = float(sys.argv[2]) if len(sys.argv) > 2 else 0
cap = cv2.VideoCapture(mp4); F = []
while True:
    ok, im = cap.read()
    if not ok: break
    F.append(im)
if pan:  # negative control: progressive horizontal pan of frame 0 across the clip
    F = [cv2.warpAffine(F[0], np.float32([[1, 0, pan * i / (len(F) - 1)], [0, 1, 0]]), (F[0].shape[1], F[0].shape[0]), borderMode=cv2.BORDER_REPLICATE) for i in range(len(F))]
f0 = F[0].astype(int); stay = np.zeros(f0.shape[:2], np.int32)
for im in F[1:]: stay += (np.abs(im.astype(int) - f0).sum(2) <= 36)
mask = ((stay >= 0.8 * (len(F) - 1)) * 255).astype(np.uint8); mask = cv2.erode(mask, np.ones((9, 9), np.uint8))
orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
g0 = cv2.cvtColor(F[0], cv2.COLOR_BGR2GRAY); k0, d0 = orb.detectAndCompute(g0, mask); worst = dict(scale=0, tx=0, ty=0); bad = []
if d0 is None or len(k0) < 200: res = dict(ok=False, reason='insufficient background keypoints', keypoints=0 if d0 is None else len(k0), mask_frac=round(float((mask > 0).mean()), 3))
else:
    for i, im in enumerate(F[1:], 1):
        k1, d1 = orb.detectAndCompute(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), None); m = bf.match(d0, d1)
        M, inl = cv2.estimateAffinePartial2D(np.float32([k0[x.queryIdx].pt for x in m]), np.float32([k1[x.trainIdx].pt for x in m]), method=cv2.RANSAC, ransacReprojThreshold=2)
        s = float(np.hypot(M[0, 0], M[1, 0])) - 1; tx, ty = float(M[0, 2]), float(M[1, 2])
        worst = dict(scale=max(worst['scale'], abs(s)), tx=max(worst['tx'], abs(tx)), ty=max(worst['ty'], abs(ty)))
        if abs(s) >= .003 or abs(tx) >= 2 or abs(ty) >= 2: bad.append(i)
    res = dict(ok=not bad, keypoints=len(k0), mask_frac=round(float((mask > 0).mean()), 3), moving_frames=bad[:20], n_moving=len(bad), worst={k: round(v, 4) for k, v in worst.items()})
print(json.dumps(res))
