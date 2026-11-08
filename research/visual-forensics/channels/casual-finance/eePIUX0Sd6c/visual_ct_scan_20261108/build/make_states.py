# build/make_states.py  (cwd = workspace): notes.txt + tables -> build/states_data.py + tables/zoom_measure.csv
import csv, json, sys, statistics as S, numpy as np, cv2
SRC = sys.argv[1]; MEASURE = len(sys.argv) > 2 and sys.argv[2] == 'measure'
fm = list(csv.DictReader(open('tables/frame_metrics.csv'))); N = len(fm); px = [int(r['fullres_changed_px_thr25']) for r in fm]
eps = [(int(e['start_frame']), int(e['end_frame'])) for e in csv.DictReader(open('tables/episodes.csv'))]
L = [l.rstrip('\n').split('|') for l in open('build/notes.txt') if l.strip()]
starts = [int(l[0]) for l in L]; ends = [s - 1 for s in starts[1:]] + [N - 1]
motion_not = {'HOLD', 'START', 'CUT', 'POP_IN', 'POSE'}
shot = 0; D = []
for l, a, b in zip(L, starts, ends):
    if l[1].startswith(('START', 'CUT')): shot += 1
    D.append([a, f'SH{shot:03d}', l[1], l[3], l[4], l[5], l[6], l[2], b])
# episodes needing in-state motion cover
need = {}
for a, b in eps:
    if any(abs(a - s) <= 1 for s in starts): continue
    k = max(i for i, s in enumerate(starts) if s <= a); need.setdefault(k, []).append(a)
# zoom measurement
zm = {}
if MEASURE:
    jobs = {}
    for k, d in enumerate(D):
        a, b = d[0], d[8]
        if b - a + 1 < 25: continue
        fa, fb = a + 4, b - 3
        if fb - fa < 15: continue
        inner = [px[i] for i in range(a + 3, b + 1)]
        if not inner or max(inner) < 150: continue
        jobs[k] = (fa, fb)
    need_f = sorted({x for v in jobs.values() for x in v}); fr = {}
    cap = cv2.VideoCapture(SRC); i = 0
    while i <= need_f[-1]:
        ok, f = cap.read()
        if not ok: break
        if i in need_f: fr[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        i += 1
    orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    for k, (fa, fb) in jobs.items():
        ka, da = orb.detectAndCompute(fr[fa], None); kb, db = orb.detectAndCompute(fr[fb], None)
        if da is None or db is None or len(ka) < 40 or len(kb) < 40: zm[k] = (fa, fb, None, None, None, 0, 0); continue
        m = bf.match(da, db)
        if len(m) < 30: zm[k] = (fa, fb, None, None, None, len(m), 0); continue
        pa = np.float32([ka[x.queryIdx].pt for x in m]); pb = np.float32([kb[x.trainIdx].pt for x in m])
        M, inl = cv2.estimateAffinePartial2D(pa, pb, method=cv2.RANSAC, ransacReprojThreshold=1.5)
        if M is None: zm[k] = (fa, fb, None, None, None, len(m), 0); continue
        zm[k] = (fa, fb, float(np.hypot(M[0, 0], M[1, 0])), float(M[0, 2]), float(M[1, 2]), len(m), int(inl.sum()))
    with open('tables/zoom_measure.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['state_start', 'state_end', 'frame_a', 'frame_b', 'scale_b_over_a', 'tx', 'ty', 'matches', 'inliers'])
        for k, v in zm.items(): w.writerow([D[k][0], D[k][8], v[0], v[1], v[2] if v[2] is None else round(v[2], 5), v[3] if v[3] is None else round(v[3], 2), v[4] if v[4] is None else round(v[4], 2), v[5], v[6]])
else:
    try:
        for r in csv.DictReader(open('tables/zoom_measure.csv')):
            k = next(i for i, d in enumerate(D) if d[0] == int(r['state_start']))
            zm[k] = (int(r['frame_a']), int(r['frame_b']), None if r['scale_b_over_a'] == '' else float(r['scale_b_over_a']), None, None, int(r['matches']), int(r['inliers']))
    except FileNotFoundError: pass
out = []
for k, d in enumerate(D):
    a, b = d[0], d[8]; cls = d[2]; suf = ''; pre = '+' in cls
    inner = [px[i] for i in range(a + 3, b + 1) if px[i] >= 300]
    z = zm.get(k)
    zoomed = bool(z and z[2] and z[6] >= 150 and abs(z[2] - 1) >= 0.004)
    if k in need or zoomed:
        if zoomed: suf = '+ZOOM_IN' if z[2] > 1 else '+ZOOM_OUT'
        elif inner and S.median(inner) >= 15000: suf = '+ANIM'
        else: suf = '+MICRO'
    if (cls in motion_not or k in need or zoomed) and not pre:
        cls2 = cls + suf
    else: cls2 = cls
    zdesc = f"; MEASURED scale f{z[0]}->f{z[1]} = {z[2]:.4f} ({z[6]} inlier matches)" if zoomed else ''
    ndesc = f"; {len(need[k])} in-state activity episodes" if k in need else ''
    out.append((a, d[1], cls2, d[3], d[4], d[5], d[6] + zdesc + ndesc, d[7]))
open('build/states_data.py', 'w').write('D = ' + repr(out) + f'\nLAST = {N-1}\n')
print('states', len(out), 'need-cover states', len(need), 'zoom measured', len(zm), 'zoomed', sum(1 for k in zm if zm[k][2] and zm[k][6] >= 150 and abs(zm[k][2] - 1) >= 0.004))
from collections import Counter; print(Counter(x[2] for x in out))
