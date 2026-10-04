"""Four-quadrant packaging matrix over package-audited videos + per-channel best/worst lists.

STRONG_PACKAGE = PACKAGE_SCORE in the top third of the audited sample; WEAK_PACKAGE = bottom third (cut points recomputed from the data; MIDDLE_PACKAGE excluded from quadrants).
Performance = age-matched public class (HIGH/LOW; MIDDLE and INSUFFICIENT_COHORT excluded). Q1 STRONG+HIGH, Q2 WEAK+LOW, Q3 STRONG+LOW (counterexample), Q4 WEAK+HIGH (counterexample).
Quadrants are descriptive, not causal. Alternative-explanation columns use ONLY evidence in the repository (age, cohort, channel scale, orientation, format, metric-date confidence);
factors with no data (traffic source, timing, competition, search demand) are listed as NOT_TESTABLE."""
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader((HERE / 'package-forensics.csv').open()))
mp = {r['Video_ID']: r for r in csv.DictReader((HERE / 'master-packages.csv').open())}
chan_views = defaultdict(list)
for m in mp.values():
    if m['Views'] != '': chan_views[(m['Channel_ID'], m['Format'])].append(float(m['Views']))
sc = np.array([int(r['PACKAGE_SCORE']) for r in rows]); lo, hi = float(np.percentile(sc, 33.3)), float(np.percentile(sc, 66.7))
NT = 'search_demand;publication_timing;competition;traffic_source;external_promotion;audience_size_at_publish'
out = []
for r in rows:
    s = int(r['PACKAGE_SCORE']); pk = 'STRONG_PACKAGE' if s >= hi else 'WEAK_PACKAGE' if s <= lo else 'MIDDLE_PACKAGE'
    pc = r['PERFORMANCE_CLASS']
    q = {('STRONG_PACKAGE', 'HIGH'): 'Q1_STRONG_HIGH', ('WEAK_PACKAGE', 'LOW'): 'Q2_WEAK_LOW', ('STRONG_PACKAGE', 'LOW'): 'Q3_STRONG_LOW_COUNTEREXAMPLE', ('WEAK_PACKAGE', 'HIGH'): 'Q4_WEAK_HIGH_COUNTEREXAMPLE'}.get((pk, pc), 'NOT_IN_QUADRANT')
    v = chan_views[(r['Channel_ID'], r['Format'])]; med = float(np.median(v)) if v else 0
    ev = [f"channel_format_videos={len(v)}", f"channel_format_median_views={int(med)}", f"age_days={r['Age_Days']}", f"cohort_size={r['Cohort_Size']}", f"title_orientation={r['Title_Orientation']}", f"metric_date={r['Metric_Date_Confidence']}", f"thumbnail_alignment={r['Creative_Temporal_Alignment']}"]
    if q.startswith('Q3'):
        if float(r['Age_Days'] or 0) < 60: ev.append('YOUNG_VIDEO_MAY_STILL_ACCUMULATE')
        if len(v) < 20: ev.append('SMALL_CHANNEL_FORMAT_SAMPLE')
        if med < 20000: ev.append('LOW_CHANNEL_SCALE')
        if r['Title_Orientation'] == 'BROWSE': ev.append('BROWSE_TITLE_DEPENDS_ON_DISTRIBUTION')
    if q.startswith('Q4'):
        if r['Title_Orientation'] in ('SEARCH', 'MIXED'): ev.append('SEARCH_ORIENTED_TITLE_POSSIBLE_DEMAND_DRIVEN')
        if med >= 200000: ev.append('LARGE_CHANNEL_AUDIENCE')
        if r['Outlier_Multiple_Age_Adjusted'] and float(r['Outlier_Multiple_Age_Adjusted']) >= 10: ev.append('EXTREME_OUTLIER_LIKELY_EXTERNAL_OR_SEARCH_FACTORS')
    out.append(dict(Package_ID=r['Package_ID'], Channel_Name=r['Channel_Name'], Format=r['Format'], Title=r['Title'], TITLE_SCORE=r['TITLE_SCORE'], THUMBNAIL_SCORE=r['THUMBNAIL_SCORE'], PACKAGE_SCORE=s, Package_Strength=pk,
                    PERFORMANCE_CLASS=pc, Performance_Band=r['Performance_Band'], Perf_Percentile_Age_Matched=r['Perf_Percentile_Age_Matched'], Outlier_Multiple_Age_Adjusted=r['Outlier_Multiple_Age_Adjusted'], Quadrant=q,
                    Primary_Relationship=r['primary_relationship'], Available_Alternative_Evidence='|'.join(ev) if q.startswith(('Q3', 'Q4')) else '', Not_Testable_Factors=NT if q.startswith(('Q3', 'Q4')) else '', Evidence_Tier=r['Evidence_Tier']))
with (HERE / 'packaging-quadrants.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, list(out[0])); w.writeheader(); w.writerows(out)
qc = Counter(o['Quadrant'] for o in out)
json.dump(dict(packages=len(out), strong_cut=round(hi, 1), weak_cut=round(lo, 1), counts=dict(qc), definition='STRONG = top third of PACKAGE_SCORE in the audited sample; WEAK = bottom third; HIGH/LOW = age-matched public class; descriptive only, no causal claim',
               performance_by_package_strength={k: dict(Counter(o['PERFORMANCE_CLASS'] for o in out if o['Package_Strength'] == k)) for k in ('STRONG_PACKAGE', 'MIDDLE_PACKAGE', 'WEAK_PACKAGE')}), open(HERE / 'packaging-quadrants-summary.json', 'w'), indent=1)
print(len(out), dict(qc), 'cuts', round(lo, 1), round(hi, 1))
