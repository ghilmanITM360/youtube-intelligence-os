import sys, itertools, numpy as np
sys.path.insert(0, '.')
import ledger_lib as L
from ledger_tune import campaign, match
V = sys.argv[1].split(',')
M = {v: L.measure(L.media(v), ACT_FRAC=0.0004, T_PIX=24) for v in V}
for CF, BW, BH in itertools.product([0.02, 0.04, 0.08, 0.15], [0.0, 0.5, 0.8], [0.0, 0.5]):
    tot = dict(c=0, m=0, hit=0)
    for v in V:
        m = M[v]; cuts = []
        for k, f in enumerate(m['frac']):
            b = m['bbox'][k]
            if f >= CF and b and (b[2] - b[0]) >= BW and (b[3] - b[1]) >= BH: cuts.append(k + 1)
        cuts = [c for j, c in enumerate(cuts) if j == 0 or c - cuts[j - 1] > 2]
        csh, _ = campaign(v); tot['c'] += len(csh); tot['m'] += len(cuts); tot['hit'] += match(csh, cuts, 2)
    print(f"CF={CF} BW={BW} BH={BH} | camp {tot['c']} meas {tot['m']} hit {tot['hit']} P={tot['hit']/max(tot['m'],1):.2f} R={tot['hit']/tot['c']:.2f}")
