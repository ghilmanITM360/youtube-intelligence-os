"""Consolidate title-analyst-audit-T-NN.json into title-analyst-audit.csv/json (one row per canonical video, exact Video_ID join).
Analyst fields stay in their own file; programmatic fields stay in title-forensics.csv. Re-run after chunks change."""
import csv, glob, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = {}
for f in sorted(glob.glob(str(HERE / 'title-analyst-audit-T-*.json'))):
    for r in json.load(open(f)): rows[r['Video_ID']] = r
tf = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
out = []
for vid, t in tf.items():
    r = rows.get(vid)
    if not r: continue
    o = dict(Video_ID=vid, Channel_ID=t['Channel_ID'], Exact_Title=t['Exact_Title'], **{k: (';'.join(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ('Video_ID', 'seq')})
    o['ANALYST_TITLE_DIAGNOSTIC_SCORE'] = o.pop('score_100')
    out.append(o)
if out:
    with (HERE / 'title-analyst-audit.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(out[0])); w.writeheader(); w.writerows(out)
    (HERE / 'title-analyst-audit.json').write_text(json.dumps(dict(method='ANALYST_BLIND_TITLE_AUDIT (no performance data seen); score is a diagnostic, not a CTR/view prediction', rows=out), ensure_ascii=False))
print(len(out), 'of', len(tf), 'titles audited;', 'missing', len(tf) - len(out))
