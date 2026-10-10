"""Per-channel packaging profile for all registry channels (one row each), rebuilt from current audits. No fabricated analysis: channels without package audits get INSUFFICIENT_PACKAGING_EVIDENCE.

BEST/WORST_PERFORMING_PACKAGE use age-matched public percentile (then age-adjusted outlier multiple) among that channel's package-audited videos, NOT lifetime views.
STRONGEST/WEAKEST_ANALYST_RATED_PACKAGE use PACKAGE_SCORE. The two pairs are deliberately independent. Coverage confidence by verified package count: >=20 HIGH, 10-19 MEDIUM, 5-9 LOW, 1-4 VERY_LOW, 0 INSUFFICIENT.
"""
import csv, json
from collections import Counter
from pathlib import Path
from build_package_inputs import thumb_rows

HERE = Path(__file__).resolve().parent
rd = lambda f: list(csv.DictReader((HERE / f).open()))
cov, mp, tf, pf, qd = rd('channel-coverage.csv'), rd('master-packages.csv'), {r['Video_ID']: r for r in rd('title-forensics.csv')}, rd('package-forensics.csv'), {r['Package_ID']: r for r in rd('packaging-quadrants.csv')}
tr = thumb_rows()
mode = lambda xs, n=3: '|'.join(f'{k}:{c}' for k, c in Counter(x for x in xs if x).most_common(n)) or ''
perf_key = lambda r: (float(r['Perf_Percentile_Age_Matched'] or -1), float(r['Outlier_Multiple_Age_Adjusted'] or 0))
lab = lambda r: f"{r['Video_ID']} | {r['Title'][:70]} | pkg={r.get('PACKAGE_SCORE', '')} class={r.get('PERFORMANCE_CLASS', '')}"
out = []
for c in cov:
    cid = c['Channel_ID']; vids = [m for m in mp if m['Channel_ID'] == cid]; pk = [p for p in pf if p['Channel_ID'] == cid]
    th = [tr[m['Thumbnail_ID']][1] for m in vids if m['Thumbnail_ID'] in tr]
    arch = [a for m in vids for a in tf[m['Video_ID']]['Title_Archetypes_All'].split('|') if a] if vids else []
    cls = [p for p in pk if p['PERFORMANCE_CLASS'] in ('HIGH', 'MIDDLE', 'LOW')]
    n = len(pk)
    conf = 'INSUFFICIENT_PACKAGING_EVIDENCE' if n == 0 else 'HIGH' if n >= 20 else 'MEDIUM' if n >= 10 else 'LOW' if n >= 5 else 'VERY_LOW'
    row = dict(Channel_ID=cid, Channel_Name=c['Channel_Name'], Own_Competitor_Reference=c['Own_Competitor_Reference'], Niche=c['Niche'], Coverage_Status=c['Coverage_Status'], Canonical_Videos=len(vids),
               Title_Coverage=f"{c['Videos_With_Title']}/{len(vids)}", Thumbnail_Coverage=f"{c['Videos_With_Thumbnail']}/{len(vids)}", Thumbnail_Audits_Complete=len(th), Verified_Package_Coverage=f'{n}/{len(vids)}',
               Dominant_Title_Archetypes=mode(arch) if vids else 'NO_VIDEO_DATA', Thumbnail_Style_Sample=len(th),
               Dominant_Thumbnail_Style=(mode([t.get('art_style') for t in th], 2) + ' | face:' + mode([t.get('face_scale') for t in th], 2) + ' | text:' + mode([t.get('text_density') for t in th], 2)) if th else ('NOT_AUDITED' if vids else 'NO_VIDEO_DATA'),
               Dominant_Title_Thumbnail_Relationship=mode([r for p in pk for r in p['relationships'].split(';')], 3) if pk else 'NOT_PACKAGE_AUDITED', Packages_With_Performance_Class=len(cls))
    if cls and n >= 2:
        row['BEST_PERFORMING_PACKAGE'] = lab(max(cls, key=perf_key)); row['WORST_PERFORMING_PACKAGE'] = lab(min(cls, key=perf_key))
    else: row['BEST_PERFORMING_PACKAGE'] = row['WORST_PERFORMING_PACKAGE'] = 'INSUFFICIENT_PACKAGING_EVIDENCE'
    if n >= 2:
        row['STRONGEST_ANALYST_RATED_PACKAGE'] = lab(max(pk, key=lambda r: int(r['PACKAGE_SCORE']))); row['WEAKEST_ANALYST_RATED_PACKAGE'] = lab(min(pk, key=lambda r: int(r['PACKAGE_SCORE'])))
        row['Mean_Package_Score'] = round(sum(int(p['PACKAGE_SCORE']) for p in pk) / n, 1)
    else: row['STRONGEST_ANALYST_RATED_PACKAGE'] = row['WEAKEST_ANALYST_RATED_PACKAGE'] = 'INSUFFICIENT_PACKAGING_EVIDENCE'; row['Mean_Package_Score'] = ''
    row['Counterexample_Count_Q3_Q4'] = sum(1 for p in pk if qd.get(p['Package_ID'], {}).get('Quadrant', '').startswith(('Q3', 'Q4')))
    row['Coverage_Confidence'] = conf
    best_title = max((m for m in vids if m['Outlier_Multiple_Age_Adjusted']), key=lambda m: float(m['Outlier_Multiple_Age_Adjusted']), default=None)
    row['Top_Video_By_Age_Adjusted_Outlier_ANY_AUDIT_STATE'] = f"{best_title['Video_ID']} | {best_title['Title_Current'][:70]} | x{best_title['Outlier_Multiple_Age_Adjusted']}" if best_title else 'NONE'
    out.append(row)
with (HERE / 'channel-packaging-profiles.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, list(out[0]), lineterminator="\n"); w.writeheader(); w.writerows(out)
(HERE / 'channel-packaging-profiles.json').write_text(json.dumps(dict(method='see build_channel_profiles.py docstring', rows=out), ensure_ascii=False))
print(len(out), Counter(r['Coverage_Confidence'] for r in out), 'channels with >=1 verified package', sum(1 for r in out if r['Coverage_Confidence'] != 'INSUFFICIENT_PACKAGING_EVIDENCE'))
