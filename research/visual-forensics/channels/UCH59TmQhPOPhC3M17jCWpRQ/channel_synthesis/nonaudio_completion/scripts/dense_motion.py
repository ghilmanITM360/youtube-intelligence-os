# Every-frame motion pass: frame-to-previous similarity transform (ORB+RANSAC at 640x360) = camera component;
# residual after motion compensation = local (object/character/graphic) change. Sequential decode of the whole MP4.
# usage: dense_motion.py SRC OUT.csv
import cv2, csv, sys, numpy as np
src, out = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src); orb = cv2.ORB_create(1500); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
W = csv.writer(open(out, 'w', newline='')); W.writerow(['frame', 'dx', 'dy', 'dscale', 'drot_deg', 'inliers', 'global_mad', 'residual_frac12', 'residual_bbox'])
prev = pk = pd = None; i = 0
while True:
    ok, im = cap.read()
    if not ok: break
    g = cv2.cvtColor(cv2.resize(im, (640, 360), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY); k, d = orb.detectAndCompute(g, None)
    row = [i, 0, 0, 0, 0, 0, 0, 0, '']
    if prev is not None:
        mad = float(np.abs(g.astype(int) - prev.astype(int)).mean()); M = None; n = 0
        if d is not None and pd is not None and len(k) > 8 and len(pk) > 8:
            m = bf.match(pd, d)
            if len(m) >= 8:
                M, inl = cv2.estimateAffinePartial2D(np.float32([pk[x.queryIdx].pt for x in m]), np.float32([k[x.trainIdx].pt for x in m]), method=cv2.RANSAC, ransacReprojThreshold=1.5)
                n = int(inl.sum()) if inl is not None else 0
        if M is None or n < 12: M = np.float32([[1, 0, 0], [0, 1, 0]])
        wp = cv2.warpAffine(prev, M, (640, 360), borderMode=cv2.BORDER_REPLICATE); r = np.abs(g.astype(int) - wp.astype(int)) > 12
        ys, xs = np.nonzero(r); bb = f'{xs.min()*3}-{xs.max()*3}x{ys.min()*3}-{ys.max()*3}' if len(xs) else ''
        s = float(np.hypot(M[0, 0], M[1, 0]))
        row = [i, round(float(M[0, 2]) * 3, 2), round(float(M[1, 2]) * 3, 2), round(s - 1, 5), round(float(np.degrees(np.arctan2(M[1, 0], M[0, 0]))), 3), n, round(mad, 3), round(float(r.mean()), 5), bb]
    W.writerow(row); prev, pk, pd = g, k, d; i += 1
print(out, i)
