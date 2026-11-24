import csv, sys, itertools
sys.path.insert(0, '.')
from pathlib import Path
import ledger_lib as L
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos')
def campaign(v):
    fps = 24.0
    sh = [int(r['start_frame']) for r in csv.DictReader(open(C / v / 'shot_ledger.csv'))][1:]
    ev = [int(r['start_frame']) for r in csv.DictReader(open(C / v / 'visual_event_ledger.csv'))]
    return sh, sorted(set(ev))
def match(a, b, tol):
    used, hit = set(), 0
    for x in a:
        c = [j for j, y in enumerate(b) if abs(x - y) <= tol and j not in used]
        if c: j = min(c, key=lambda j: abs(x - b[j])); used.add(j); hit += 1
    return hit
if __name__ == '__main__':
    V = sys.argv[1].split(',')
    cache = {v: L.probe(L.media(v)) and v for v in V}
    for ACT, TP in itertools.product([0.0004, 0.0008, 0.0016], [24, 32, 48]):
        tot = dict(sh_c=0, sh_m=0, sh_hit=0, ev_c=0, ev_m=0, ev_hit=0)
        for v in V:
            m = L.measure(L.media(v), ACT_FRAC=ACT, T_PIX=TP); cuts, ev = L.segments(m)
            csh, cev = campaign(v); es = [e['start_frame'] for e in ev]
            tot['sh_c'] += len(csh); tot['sh_m'] += len(cuts); tot['sh_hit'] += match(csh, cuts, 2)
            tot['ev_c'] += len(cev); tot['ev_m'] += len(es); tot['ev_hit'] += match(cev, es, 3)
        p = tot['ev_hit'] / max(tot['ev_m'], 1); r = tot['ev_hit'] / max(tot['ev_c'], 1)
        print(f"ACT={ACT} T_PIX={TP} | shots camp {tot['sh_c']} meas {tot['sh_m']} hit {tot['sh_hit']} | events camp {tot['ev_c']} meas {tot['ev_m']} hit {tot['ev_hit']} P={p:.2f} R={r:.2f}", flush=True)
