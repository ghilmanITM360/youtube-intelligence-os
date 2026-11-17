"""Apply reviewer corrections from qa2-review-<BATCH>-*.json to audit-batch-<BATCH>.json and log every change.

Usage: apply_qa_corrections.py B002-03 [round_tag]
Every error with a corrected_value is applied (field edits only; Thumbnail_ID is never touched); score_100 is recomputed.
The log qa-corrections-log.csv keeps original_value, corrected_value, error_class, reviewer, reason and evidence (append-only).
Rows reviewed with no errors get qa_status QA2_REVIEWED_PASS; rows corrected get QA2_REVIEWED_CORRECTED.
"""
import csv, glob, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SC = ['story_score', 'psychological_hook_score', 'title_partnership_score', 'hierarchy_score', 'mobile_readability_score', 'composition_score', 'emotion_subject_alignment_score', 'credibility_score', 'distinctiveness_score']
INT = set(SC) | {'word_count', 'people_count_visible'}
FIELDS = ['batch', 'seq', 'thumbnail_id', 'field', 'error_class', 'original_value', 'corrected_value', 'reviewer', 'reason', 'evidence']

bid = sys.argv[1]; tag = sys.argv[2] if len(sys.argv) > 2 else 'QA2'
p = HERE / f'audit-batch-{bid}.json'; rows = json.loads(p.read_text()); by = {r['seq']: r for r in rows}
log = HERE / 'qa-corrections-log.csv'; new = not log.exists()
n = 0
with log.open('a', newline='') as lf:
    w = csv.DictWriter(lf, FIELDS)
    if new: w.writeheader()
    for f in sorted(glob.glob(str(HERE / f'qa2-review-{bid}-*.json'))):
        d = json.loads(Path(f).read_text())
        for rv in d['rows']:
            r = by[rv['seq']]; assert r['Thumbnail_ID'] == rv['thumbnail_id'], ('ID mismatch', bid, rv['seq'])
            for e in rv['errors']:
                fld, cv = e['field'], e['corrected_value']
                if fld not in r: continue
                if fld in INT: cv = int(re.match(r'\s*(\d+)', str(cv)).group(1))
                if r[fld] == cv: continue
                w.writerow(dict(batch=bid, seq=rv['seq'], thumbnail_id=r['Thumbnail_ID'], field=fld, error_class=e['error_class'], original_value=r[fld], corrected_value=cv,
                                reviewer=d['reviewer'], reason=e['reason'], evidence=e['evidence'])); r[fld] = cv; n += 1
            r['score_100'] = sum(r[k] for k in SC)
            r['qa_status'] = f'{tag}_REVIEWED_CORRECTED' if rv['errors'] else f'{tag}_REVIEWED_PASS'
p.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(bid, 'field corrections applied:', n)
