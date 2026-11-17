"""Validate title-analyst-audit-T-NN.json files against their inputs: ids/order, enums, score ranges and sums, repeated text.
Usage: validate_title_audit.py T-01 [T-02 ...]   (inputs live in the scratchpad titles dir)
"""
import json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/titles')
MAX = dict(clarity_score=20, specificity_score=15, curiosity_score=20, promise_strength_score=15, credibility_score=15, audience_fit_score=10, concision_score=5)
TXT = ['core_topic', 'exact_promise', 'intended_viewer', 'unanswered_question', 'improvement']
ENUM = dict(orientation={'SEARCH', 'BROWSE', 'MIXED'}, overpromise_risk={'LOW', 'MEDIUM', 'HIGH'}, confidence={'HIGH', 'MEDIUM', 'LOW'}, tells_too_much={'Y', 'N'}, tells_too_little={'Y', 'N'},
            medical_title_flag={'NOT_HEALTH', 'MEDICAL_PACKAGING_SAFE', 'NEEDS_CONTEXT', 'MISLEADING_RISK', 'UNRESOLVED'})
REL = {'FEAR', 'AUTHORITY', 'CURIOSITY', 'URGENCY', 'HOPE', 'SPECIFICITY', 'SOCIAL_PROOF', 'NOVELTY', 'NONE'}


def validate(rows, inp):
    errs = []
    if [r.get('Video_ID') for r in rows] != [i['Video_ID'] for i in inp]: errs.append('ID_SET_OR_ORDER_MISMATCH')
    for r in rows:
        t = str(r.get('Video_ID'))[:11]
        for k, mx in MAX.items():
            if not isinstance(r.get(k), int) or not 0 <= r[k] <= mx: errs.append(f'{t} RANGE {k}={r.get(k)}')
        if r.get('score_100') != sum(r[k] for k in MAX if isinstance(r.get(k), int)): errs.append(f"{t} SUM {r.get('score_100')}")
        for k, v in ENUM.items():
            if r.get(k) not in v: errs.append(f'{t} ENUM {k}={r.get(k)!r}')
        if not isinstance(r.get('mechanism_reliance'), list) or not r['mechanism_reliance'] or not set(r['mechanism_reliance']) <= REL: errs.append(f'{t} RELIANCE')
        if not isinstance(r.get('unnecessary_words'), list): errs.append(f'{t} UNNECESSARY_WORDS_TYPE')
        for k in TXT:
            if not isinstance(r.get(k), str) or len(r[k].strip()) < 3: errs.append(f'{t} TEXT {k}')
        if r.get('overpromise_risk') in ('MEDIUM', 'HIGH') and not r.get('overpromise_note'): errs.append(f'{t} OVERPROMISE_NOTE_MISSING')
    imp = Counter(r.get('improvement') for r in rows)
    dup = [k[:50] for k, n in imp.items() if n > 1]
    sc = Counter(r.get('score_100') for r in rows)
    return errs, dict(rows=len(rows), duplicate_improvements=dup, distinct_scores=len(sc), mean=round(sum(r.get('score_100', 0) for r in rows) / max(1, len(rows)), 1))


if __name__ == '__main__':
    bad = 0
    for b in sys.argv[1:]:
        rows = json.loads((HERE / f'title-analyst-audit-{b}.json').read_text()); inp = json.loads((S / f'{b}.json').read_text())
        e, f = validate(rows, inp); bad += len(e)
        print(b, json.dumps(f), 'ERRORS', len(e), e[:10])
    sys.exit(1 if bad else 0)
