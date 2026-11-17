"""EARLY, NON-FINAL scan: within-channel difference in age-matched performance percentile for programmatic title features.
Per channel x format cohort (>=5 videos with and >=5 without the feature) take mean(percentile | feature) - mean(percentile | no feature); report the
median difference across cohorts, the share of cohorts where it is positive, and the number of cohorts. Observational (evidence tier D); no causal claim."""
import csv, json, statistics as st
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
tf = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
mp = {r['Video_ID']: r for r in csv.DictReader((HERE / 'master-packages.csv').open())}
ta = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-analyst-audit.csv').open())}
FEAT = {'Number_Present': lambda t, a: t['Number_Present'] == '1', 'Question_Form': lambda t, a: t['Question_Form'] == '1', 'List_Form': lambda t, a: t['List_Form'] == '1',
        'Warning_Frame': lambda t, a: t['Warning_Frame'] == '1', 'Fear_Frame': lambda t, a: t['Fear_Frame'] == '1', 'Authority_Cue_present': lambda t, a: t['Authority_Cue'] != 'NONE',
        'Age_Number_Present': lambda t, a: t['Age_Number_Present'] == '1', 'Mistake_Frame': lambda t, a: t['Mistake_Frame'] == '1', 'Secret_Frame': lambda t, a: t['Secret_Frame'] == '1',
        'Second_person_YOU/YOUR': lambda t, a: any(x in t['Person_Address'].split('|') for x in ('YOU', 'YOUR')), 'Short_title_(<=45 chars)': lambda t, a: int(t['Character_Count']) <= 45,
        'Long_title_(>=75 chars)': lambda t, a: int(t['Character_Count']) >= 75, 'Curiosity_frame': lambda t, a: t['Curiosity_Frame'] == '1', 'Hope_frame': lambda t, a: t['Hope_Frame'] == '1',
        'Analyst_orientation_BROWSE': lambda t, a: a['orientation'] == 'BROWSE', 'Analyst_score_>=70': lambda t, a: int(a['ANALYST_TITLE_DIAGNOSTIC_SCORE']) >= 70}
coh = defaultdict(list)
for v, m in mp.items():
    if m['Perf_Percentile_Age_Matched'] != '': coh[(m['Channel_ID'], m['Format'])].append((float(m['Perf_Percentile_Age_Matched']), v))
out = []
for k, f in FEAT.items():
    d = []
    pos = []
    for c, g in coh.items():
        a = [p for p, v in g if f(tf[v], ta[v])]; b = [p for p, v in g if not f(tf[v], ta[v])]
        if len(a) >= 5 and len(b) >= 5: d.append(st.mean(a) - st.mean(b))
    n_with = sum(1 for g in coh.values() for p, v in g if f(tf[v], ta[v]))
    out.append(dict(feature=k, videos_with_feature=n_with, cohorts_compared=len(d), median_within_cohort_percentile_diff=round(st.median(d), 3) if d else None,
                    share_cohorts_positive=round(sum(x > 0 for x in d) / len(d), 2) if d else None))
V1_REF = {'Number_Present': 0.045, 'List_Form': 0.044, 'Second_person_YOU/YOUR': 0.043, 'Fear_Frame': -0.076, 'Authority_Cue_present': -0.126, 'Mistake_Frame': -0.128}  # first scan, taxonomy v1 flags
for o in out: o['evidence_label'] = 'EXPLORATORY_ASSOCIATION'; o['v1_flag_median_diff'] = V1_REF.get(o['feature'])
json.dump(dict(evidence_label='EXPLORATORY_ASSOCIATION', evidence_tier='D_AGE_ADJUSTED_PUBLIC (within channel x format cohort percentile)', taxonomy_version='v2-2026-10-04',
               caveats=['observational, no causal claim', 'multiple features tested, no correction', 'coarse percentile outcome (1/13 granularity)', 'channel and topic heterogeneity not controlled', 'few cohorts per feature for rare features',
                        'feature flags are rule-based and were revised after title QA: Fear/Authority/Mistake effects moved between flag versions, which is itself evidence of instability', 'promotion requires counterexamples, larger samples and within-channel support'],
               features=out), open(HERE / 'early-title-feature-scan.json', 'w'), indent=1)
for o in out: print(o)
