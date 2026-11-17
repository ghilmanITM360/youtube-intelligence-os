"""Merge package-audit-PK-NN.json into package-forensics.csv/json (one row per package-audited video, exact Package_ID join).
Keeps TITLE_SCORE, THUMBNAIL_SCORE, PACKAGE_SCORE (EXPERT_PACKAGING_DIAGNOSTIC_SCORE) and PERFORMANCE_CLASS as separate columns. Re-run after audits or QA corrections."""
import csv, glob, json
from pathlib import Path
from build_package_inputs import thumb_rows
from packaging_audit_records import verified_records

HERE = Path(__file__).resolve().parent
rd = lambda f, k='Video_ID': {r[k]: r for r in csv.DictReader((HERE / f).open())}
mp, ta, tf = rd('master-packages.csv', 'Package_ID'), rd('title-analyst-audit.csv'), rd('title-forensics.csv')
tr = thumb_rows()
out = []
for records in [verified_records(HERE)[1].values()]:
    for r in records:
        m = mp[r['Package_ID']]; v = m['Video_ID']; b, th = tr[m['Thumbnail_ID']]
        o = dict(Package_ID=r['Package_ID'], Channel_ID=m['Channel_ID'], Channel_Name=m['Channel_Name'], Niche=m['Niche'], Format=m['Format'], Video_ID=v, Title=m['Title_Current'], Thumbnail_ID=m['Thumbnail_ID'],
                 Creative_Temporal_Alignment=m['Creative_Temporal_Alignment'], Package_Batch=r['batch_id'], Thumbnail_Batch=b,
                 TITLE_SCORE=ta[v]['ANALYST_TITLE_DIAGNOSTIC_SCORE'], THUMBNAIL_SCORE=th.get('score_100'), PACKAGE_SCORE=r['score_100'],
                 Title_Archetype=tf[v]['Title_Archetype'], Title_Archetypes_All=tf[v]['Title_Archetypes_All'], Title_Orientation=ta[v]['orientation'],
                 Thumb_Mechanism=th.get('mechanism_primary'), Thumb_Art_Style=th.get('art_style'), Thumb_Face_Scale=th.get('face_scale'), Thumb_Text_Density=th.get('text_density'), Thumb_Mobile_160=th.get('mobile_readability_160'),
                 PERFORMANCE_CLASS=m['Relative_Performance_Class'], Performance_Band=m['Performance_Band'], Perf_Percentile_Age_Matched=m['Perf_Percentile_Age_Matched'], Cohort_Size=m['Cohort_Size'],
                 Outlier_Multiple_Age_Adjusted=m['Outlier_Multiple_Age_Adjusted'], Evidence_Tier=m['Evidence_Tier'], Age_Days=m['Age_Days'], Metric_Date_Confidence=m['Metric_Date_Confidence'])
        for k, val in r.items():
            if k in ('Package_ID', 'Video_ID', 'Thumbnail_ID', 'seq', 'batch_id', 'score_100'): continue
            o[k] = ';'.join(val) if isinstance(val, list) else val
        out.append(o)
if out:
    with (HERE / 'package-forensics.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(dict.fromkeys(key for row in out for key in row)), lineterminator="\n"); w.writeheader(); w.writerows(out)
    (HERE / 'package-forensics.json').write_text(json.dumps(dict(method='ANALYST_PACKAGE_AUDIT_BLIND_TO_PERFORMANCE; PACKAGE_SCORE = EXPERT_PACKAGING_DIAGNOSTIC_SCORE is a diagnostic, not a CTR/views/virality prediction; PERFORMANCE_CLASS is public age-adjusted and separate', rows=out), ensure_ascii=False))
print(len(out), 'package audits merged')
