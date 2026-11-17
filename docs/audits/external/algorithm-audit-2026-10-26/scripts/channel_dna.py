"""Per-channel descriptive DNA from derived/per_video_features.csv + source titles/dates.
Usage: python3 -I channel_dna.py <audit_root>"""
import csv, json, statistics as S, sys, collections as C

ROOT = sys.argv[1]
rows = list(csv.DictReader(open(f'{ROOT}/derived/per_video_features.csv', newline='')))
FEATS = ['H01_money_amount', 'H02_curiosity_gap', 'H03a_threat_fear', 'H03b_opportunity', 'H05_explicit_audience', 'H07_list_count', 'H10_timely_marker', 'H11a_open_question', 'H11d_open_number']
out = {}
for ch in sorted({r['ch'] for r in rows}):
    rs = [r for r in rows if r['ch'] == ch]
    rated = sorted((r for r in rs if r['ratio']), key=lambda r: float(r['ratio']))
    if len(rs) < 10:
        continue
    lf = [r for r in rs if r['fmt'] == 'LONG_FORM']
    d = {'set': C.Counter(r['set'] for r in rs).most_common(1)[0][0], 'videos': len(rs), 'long_form': len(lf),
         'shorts': sum(r['fmt'] == 'SHORTS' for r in rs), 'with_ratio': len(rated),
         'deep_complete': sum(r['deep'] == 'True' for r in rs),
         'median_duration_min': round(S.median(float(r['dur']) for r in lf if r['dur']) / 60, 1) if lf else None,
         'median_ratio': round(S.median(float(r['ratio']) for r in rated), 3) if rated else None,
         'strong_share': round(sum(float(r['ratio']) >= 2 for r in rated) / len(rated), 3) if rated else None,
         'weak_share': round(sum(float(r['ratio']) < .5 for r in rated) / len(rated), 3) if rated else None,
         'feature_prevalence': {f: round(sum(r[f] == 'True' for r in rs) / len(rs), 3) for f in FEATS if any(r[f] in ('True', 'False') for r in rs)},
         'top3': [(r['id'], round(float(r['ratio']), 2)) for r in rated[-3:][::-1]],
         'bottom3': [(r['id'], round(float(r['ratio']), 2)) for r in rated[:3]]}
    ages = sorted(float(r['age']) for r in rs if r['age'])
    gaps = [b - a for a, b in zip(ages, ages[1:])]
    d['median_days_between_uploads'] = round(S.median(gaps), 2) if gaps else None
    out[ch] = d
json.dump(out, open(f'{ROOT}/derived/channel_dna.json', 'w'), indent=1)
for k, v in out.items():
    print(k, json.dumps(v)[:700])
