"""Automated wave checks over ALL rows of the listed batches: wave_checks.py B002-04 B002-05 B002-06 [--out qa-wave-checks-X.json]
Checks: schema/enums/arithmetic/hash (validate_audit_batch), cross-batch duplicate Thumbnail_ID (also vs all earlier B002 batches), missing IDs,
cross-batch near-identical prose and repeated action/diagnosis sentences, score distribution."""
import glob, itertools, json, re, sys
from collections import Counter
from validate_audit_batch import validate, HERE, ROOT
from qa_select import SCR

bids = [a for a in sys.argv[1:] if a.startswith('B')]
rows, inputs = [], []
for b in bids:
    rows += json.loads((HERE / f'audit-batch-{b}.json').read_text()); inputs += json.loads((SCR / b / 'input.json').read_text())
errs, flags = validate(rows, inputs)
prior = Counter(r['Thumbnail_ID'] for f in glob.glob(str(HERE / 'audit-batch-B002-*.json')) for r in json.loads(open(f).read()))
dups = [t for t, n in prior.items() if n > 1]
sc = Counter(r['score_100'] for r in rows)
bands = Counter(min(r['score_100'] // 10 * 10, 90) for r in rows)
act = Counter(re.sub(r'\W+', ' ', r['action'].lower())[:60] for r in rows)
rep_act = [(k, n) for k, n in act.items() if n > 1]
comps = {k: Counter(r[k] for r in rows).most_common(1)[0] for k in ('story_score', 'psychological_hook_score', 'credibility_score')}
res = dict(batches=bids, rows=len(rows), validator_errors=errs, consistency_warnings=flags['consistency_warnings'], repeated_prose=flags['repeated_sentences_or_near_duplicates'],
           duplicate_thumbnail_ids_across_b002=dups, distinct_scores=len(sc), mean_score=flags['mean_score'], score_bands=dict(sorted(bands.items())),
           most_common_score=sc.most_common(2), repeated_actions=rep_act, most_common_component_values=comps,
           mechanism_mix=dict(Counter(r['mechanism_primary'] for r in rows)), medical=dict(Counter(r['medical_label'] for r in rows)),
           confidence=dict(Counter(r['confidence'] for r in rows)), mobile=dict(Counter(r['mobile_readability_160'] for r in rows)))
out = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--out=')), None)
if out: (HERE / out).write_text(json.dumps(res, indent=1))
print(json.dumps(res, indent=1)[:3500])
