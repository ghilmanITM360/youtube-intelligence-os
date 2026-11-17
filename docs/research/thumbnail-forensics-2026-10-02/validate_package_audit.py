"""Validate package-audit-<BATCH>.json against its input: ids/order, enums, score ranges and sums, text lengths, duplicate improvements.
Usage: validate_package_audit.py PK-01 [PK-02 ...]   (inputs live in the scratchpad packages dir)"""
import json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/packages')
MAX = dict(title_clarity=10, title_curiosity_specificity=10, thumbnail_visual_proposition=10, thumbnail_hierarchy=10, title_thumbnail_complementarity=15,
           one_second_comprehension_score=10, curiosity_gap=10, credibility=10, mobile_viability=5, distinctiveness=5, promise_alignment=5)
REL = {'COMPLEMENTARY', 'REINFORCING', 'REDUNDANT', 'CURIOSITY_GAP', 'THUMBNAIL_EXTENDS_TITLE', 'TITLE_EXPLAINS_THUMBNAIL', 'CONTRADICTORY', 'THUMBNAIL_OVERPROMISE', 'TITLE_OVERPROMISE', 'DISCONNECTED', 'UNCLEAR'}
YN = ['thumbnail_repeats_title', 'thumbnail_adds_curiosity', 'title_explains_what_thumbnail_cannot', 'image_reveals_answer_too_early', 'unnecessary_duplication', 'contradiction',
      'thumbnail_escalates_beyond_title', 'title_escalates_beyond_thumbnail', 'content_verification_queue']
YPN = ['one_second_comprehension', 'credible', 'fits_target_audience']
ENUM = dict(misleading_risk={'LOW', 'MEDIUM', 'HIGH'}, confidence={'HIGH', 'MEDIUM', 'LOW'},
            medical_package_label={'NOT_HEALTH', 'MEDICAL_PACKAGING_SAFE', 'NEEDS_CONTEXT', 'MISLEADING_RISK', 'UNRESOLVED'},
            medical_escalation={'NONE', 'TITLE_MODERATE_THUMBNAIL_EXTREME', 'TITLE_EXTREME_THUMBNAIL_NEUTRAL', 'BOTH_EXTREME', 'BOTH_MODERATE'})
WORDS = dict(title_says=20, thumbnail_says=20, shared_information=20, title_only_information=20, thumbnail_only_information=20, unanswered_question=16, package_promise=20,
             viewer_expectation=20, strongest_element=20, weakest_element=20, improvement=24)
KEYS = set(MAX) | set(YN) | set(YPN) | set(ENUM) | set(WORDS) | {'Package_ID', 'Video_ID', 'Thumbnail_ID', 'seq', 'batch_id', 'relationships', 'primary_relationship', 'score_100', 'content_promise_verified', 'evidence_labels', 'qa_status'}


def validate(rows, inp):
    errs = []
    if [r.get('Video_ID') for r in rows] != [i['Video_ID'] for i in inp]: errs.append('ID_SET_OR_ORDER_MISMATCH')
    for r, i in zip(rows, inp):
        t = str(r.get('Video_ID'))[:11]
        if r.get('Thumbnail_ID') != i['Thumbnail_ID'] or r.get('Package_ID') != i['Package_ID']: errs.append(f'{t} ID_MISMATCH')
        miss = [k for k in KEYS if k not in r]
        if miss: errs.append(f'{t} MISSING {miss}'); continue
        if set(r) - KEYS: errs.append(f'{t} UNKNOWN_FIELDS {sorted(set(r) - KEYS)}')
        for k, mx in MAX.items():
            if not isinstance(r[k], int) or not 0 <= r[k] <= mx: errs.append(f'{t} RANGE {k}={r[k]}')
        if r['score_100'] != sum(r[k] for k in MAX if isinstance(r[k], int)): errs.append(f"{t} SUM {r['score_100']}")
        for k in YN:
            if r[k] not in ('Y', 'N'): errs.append(f'{t} YN {k}={r[k]!r}')
        for k in YPN:
            if r[k] not in ('YES', 'PARTIAL', 'NO'): errs.append(f'{t} YPN {k}={r[k]!r}')
        for k, v in ENUM.items():
            if r[k] not in v: errs.append(f'{t} ENUM {k}={r[k]!r}')
        if not isinstance(r['relationships'], list) or not r['relationships'] or not set(r['relationships']) <= REL: errs.append(f"{t} RELATIONSHIPS {r['relationships']}")
        elif r['primary_relationship'] not in r['relationships']: errs.append(f"{t} PRIMARY_NOT_IN_RELATIONSHIPS {r['primary_relationship']}")
        for k, mx in WORDS.items():
            v = r[k]
            if not isinstance(v, str) or len(v.strip()) < 2: errs.append(f'{t} TEXT {k}')
            elif len(v.split()) > mx + 4: errs.append(f'{t} TOO_LONG {k} {len(v.split())}>{mx}')
        if r['content_promise_verified'] != 'NOT_CHECKED': errs.append(f'{t} CONTENT_VERIFIED_CLAIM')
        if r['medical_package_label'] == 'NOT_HEALTH' and (r['medical_escalation'] != 'NONE' or r['content_verification_queue'] != 'N'): errs.append(f'{t} NON_HEALTH_ESCALATION')
        if 'CONTRADICTORY' in r['relationships'] and r['contradiction'] != 'Y': errs.append(f'{t} CONTRADICTORY_VS_FLAG')
    imp = Counter(r.get('improvement') for r in rows)
    sc = Counter(r.get('score_100') for r in rows)
    return errs, dict(rows=len(rows), duplicate_improvements=[k[:50] for k, n in imp.items() if n > 1], distinct_scores=len(sc), mean=round(sum(r.get('score_100', 0) for r in rows) / max(1, len(rows)), 1),
                      primary_relationships=dict(Counter(r.get('primary_relationship') for r in rows)))


if __name__ == '__main__':
    bad = 0
    for b in sys.argv[1:]:
        rows = json.loads((HERE / f'package-audit-{b}.json').read_text()); inp = json.loads((S / f'{b}.json').read_text())
        e, f = validate(rows, inp); bad += len(e)
        print(b, json.dumps(f), 'ERRORS', len(e), e[:12])
    sys.exit(1 if bad else 0)
