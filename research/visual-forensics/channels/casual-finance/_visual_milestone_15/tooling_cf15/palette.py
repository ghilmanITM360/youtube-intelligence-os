import cv2, csv, json, sys, numpy as np
src, ws = sys.argv[1:3]
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); need = sorted({int(s['rep_frame']) for s in st})
cap = cv2.VideoCapture(src); px = []; i = 0
while i <= need[-1]:
    ok, f = cap.read()
    if not ok: break
    if i in need: px.append(cv2.resize(f, (160, 90), interpolation=cv2.INTER_AREA).reshape(-1, 3))
    i += 1
X = np.concatenate(px).astype(np.float32)
crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1.0)
_, lab, cen = cv2.kmeans(X, 8, None, crit, 3, cv2.KMEANS_PP_CENTERS)
cnt = np.bincount(lab.ravel(), minlength=8) / len(lab)
out = sorted([{'hex': '#%02X%02X%02X' % (int(c[2]), int(c[1]), int(c[0])), 'share_pct': round(float(p) * 100, 1)} for c, p in zip(cen, cnt)], key=lambda d: -d['share_pct'])
json.dump({'method': 'k-means k=8 over one 160x90 representative frame per state (%d states), OpenCV decode' % len(px), 'colors': out}, open(f'{ws}/tables/palette.json', 'w'), indent=1)
print(out)
