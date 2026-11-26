"""How many frame transitions change at all? thresholds 2/8/24 grey levels, count of changed pixels, on the pilot video."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import ledger_lib as L
v = sys.argv[1]; p = L.media(v); w, h, fps, _ = L.probe(p); F, sw, sh = L.frames(p, w, h); F = F.astype(np.int16)
D = np.abs(F[1:] - F[:-1]); n = len(D)
for t in (0, 2, 8, 24):
    c = (D > t).reshape(n, -1).sum(1)
    print(f'thr>{t:2d}: transitions with 0 px {int((c==0).sum())}, 1-14 px {int(((c>0)&(c<15)).sum())}, >=15 px {int((c>=15).sum())}, of {n}')
c = (D > 8).reshape(n, -1).sum(1); a = np.where((c > 0) & (c < 15))[0]
print('frames with 1-14 px changed (thr 8), first 20:', a[:20].tolist())
import collections
c2 = (D > 2).reshape(n, -1).sum(1); idx = np.where(c2 >= 15)[0]
g = np.diff(idx); print('gaps between changing transitions (thr>2, >=15px):', sorted(collections.Counter(g.tolist()).items())[:12])
# runs of consecutive changing frames spaced by <=6: cadence
runs = []; cur = [idx[0]]
for i in idx[1:]:
    if i - cur[-1] <= 6: cur.append(i)
    else: runs.append(cur); cur = [i]
runs.append(cur); long_ = [r for r in runs if len(r) >= 4]
cad = collections.Counter(); 
for r in long_:
    cad[int(np.median(np.diff(r)))] += 1
print('runs>=4 changing transitions:', len(long_), 'median step (frames) counts:', dict(cad), '| example runs:', [(int(r[0]), len(r), int(np.median(np.diff(r)))) for r in long_[:8]])
