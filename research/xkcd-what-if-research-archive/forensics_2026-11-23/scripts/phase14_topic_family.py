"""Phase 14: execute the preregistered topic-family stability check (14_TOPIC_FAMILY_PREREGISTRATION.md). usage: python3 -I scripts/phase14_topic_family.py"""
import csv, re, statistics as st, collections, os, hashlib, json
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
RULES = [('HUMAN_BODY', r'human|dna|eat |eating|cannibal|survive|swim|nuclear (storage|fuel)'), ('SPACE', r'moon|\bsun\b|sun.s|space|hubble|tatooine|sunset|mars|planet|wise men|black hole|visible light'),
         ('EARTH_WATER', r'earth|ocean|water|quake|magnitude|rotat|land mass|mariana|dig|niagara|lightning|trench|sky|world|country|climate|circumference|antimatter')]
def fam(t):
    for n, rx in RULES:
        if re.search(rx, t, re.I): return n
    return 'MACHINE_OTHER'
F = {}
for v, r in inv.items():
    f = r['format'].upper()
    if f.startswith('UNCLA'): continue
    F[v] = ('LONG' if f.startswith('LONG') else 'SHORT', fam(r['title']))
sm = {r['video_id']: r for r in csv.DictReader(open(A + '/05_SCRIPT_METRICS.csv'))}
hp = {r['video_id']: float(r['hold_pct']) for r in csv.DictReader(open(A + '/ct_scan_batch/BATCH_SUMMARY.csv'))}
fams = ['HUMAN_BODY', 'SPACE', 'EARTH_WATER', 'MACHINE_OTHER']
out = []; fails = []
def med(x): return st.median(x) if x else float('nan')
for fmt in ('LONG', 'SHORT'):
    for fa in fams:
        mine = [v for v, (f, g) in F.items() if f == fmt and g == fa]; rest = [v for v, (f, g) in F.items() if f == fmt and g != fa]
        row = dict(format=fmt, family=fa, n_videos=len(mine))
        for name, d, key in (('wps', sm, 'wps'),):
            a = [float(d[v][key]) for v in mine if v in d]; b = [float(d[v][key]) for v in rest if v in d]
            row['wps_n'] = len(a); row['wps_med'] = round(med(a), 2); row['wps_rest'] = round(med(b), 2)
            if len(a) >= 5: ok = abs(med(a) / med(b) - 1) <= 0.15; row['P1'] = 'PASS' if ok else 'FAIL'; (None if ok else fails.append((fmt, fa, 'P1', row['wps_med'], row['wps_rest'])))
            else: row['P1'] = 'NOT_JUDGED_n<5'
        a = [hp[v] for v in mine if v in hp]; b = [hp[v] for v in rest if v in hp]
        row['hold_n'] = len(a); row['hold_med'] = round(med(a), 1); row['hold_rest'] = round(med(b), 1)
        if len(a) >= 5: ok = abs(med(a) - med(b)) <= 5; row['P3'] = 'PASS' if ok else 'FAIL'; (None if ok else fails.append((fmt, fa, 'P3', row['hold_med'], row['hold_rest'])))
        else: row['P3'] = 'NOT_JUDGED_n<5'
        if fmt == 'LONG':
            o = [int(sm[v]['opens_attributed']) for v in mine if v in sm]; row['opens_n'] = len(o); row['opens_share'] = round(sum(o) / len(o), 2) if o else ''
            row['P2'] = ('PASS' if o and sum(o) / len(o) >= .8 else 'FAIL') if len(o) >= 5 else 'NOT_JUDGED_n<5'
            if row['P2'] == 'FAIL': fails.append((fmt, fa, 'P2', row['opens_share'], 0.8))
        out.append(row)
keys = ['format', 'family', 'n_videos', 'wps_n', 'wps_med', 'wps_rest', 'P1', 'opens_n', 'opens_share', 'P2', 'hold_n', 'hold_med', 'hold_rest', 'P3']
w = csv.DictWriter(open(A + '/14_TOPIC_FAMILY_RESULTS.csv', 'w', newline=''), fieldnames=keys, extrasaction='ignore', restval=''); w.writeheader(); w.writerows(out)
print(hashlib.sha256(open(A + '/14_TOPIC_FAMILY_PREREGISTRATION.md', 'rb').read()).hexdigest())
for r in out: print({k: r.get(k, '') for k in keys})
print('FAILS', fails)
