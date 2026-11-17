# Per-frame camera trajectory: similarity transform of every frame vs the window's first frame (ORB + RANSAC partial affine).
# usage: cam_traj.py SRC f_start f_end OUT.json  -> scale, tx, ty, rot per frame; progress = normalised cumulative scale change
import cv2, json, sys, numpy as np
src, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
cap = cv2.VideoCapture(src); cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, a - 60)); i = int(cap.get(cv2.CAP_PROP_POS_FRAMES)); F = {}
while i <= b:
    ok, im = cap.read()
    if not ok: break
    if i >= a: F[i] = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    i += 1
orb = cv2.ORB_create(4000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
k0, d0 = orb.detectAndCompute(F[a], None); rows = []
for f in range(a, b + 1):
    k1, d1 = orb.detectAndCompute(F[f], None); m = sorted(bf.match(d0, d1), key=lambda x: x.distance)[:1500]
    M, inl = cv2.estimateAffinePartial2D(np.float32([k0[x.queryIdx].pt for x in m]), np.float32([k1[x.trainIdx].pt for x in m]), method=cv2.RANSAC, ransacReprojThreshold=2)
    s = float(np.hypot(M[0, 0], M[1, 0])); rows.append(dict(frame=f, scale=round(s, 5), tx=round(float(M[0, 2]), 2), ty=round(float(M[1, 2]), 2),
                                                            rot_deg=round(float(np.degrees(np.arctan2(M[1, 0], M[0, 0]))), 3), inliers=int(inl.sum())))
s = np.array([r['scale'] for r in rows]); ds = np.diff(s, prepend=s[0]); tot = s[-1] - s[0]
for r, v, dv in zip(rows, s, ds): r['progress'] = round(float((v - s[0]) / tot), 4) if abs(tot) > 1e-4 else None; r['dscale'] = round(float(dv), 5)
json.dump(dict(src=src, window=[a, b], total_scale_change=round(float(tot), 4), rows=rows), open(out, 'w'), indent=1)
for r in rows: print(r['frame'], r['scale'], r['tx'], r['ty'], r['progress'], r['dscale'], r['inliers'])
