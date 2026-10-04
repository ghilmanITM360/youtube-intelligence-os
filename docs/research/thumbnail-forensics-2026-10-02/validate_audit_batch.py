"""Mechanical validation of an audit batch JSON (schema, enums, score arithmetic, source hashes, template-repetition screen).

Usage: validate_audit_batch.py audit-batch-B002-01.json [expected_count]
This checks form and repetition only; visual correctness is checked by the adversarial re-opening QA.
"""
import csv, hashlib, itertools, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SCORES = dict(story_score=15, psychological_hook_score=15, title_partnership_score=15, hierarchy_score=10, mobile_readability_score=10,
              composition_score=10, emotion_subject_alignment_score=10, credibility_score=10, distinctiveness_score=5)
NARR = ['text', 'scene', 'composition', 'typography', 'colors', 'psychology', 'partnership', 'scan', 'art', 'strength', 'weakness', 'bottleneck', 'action']
ENUM = dict(
    mechanism_primary={'curiosity', 'warning', 'specificity', 'hidden_answer', 'comparison', 'contradiction', 'consequence', 'authority', 'mistake',
                       'challenge', 'demonstration', 'transformation', 'recognition', 'other'},
    face_scale={'NONE', 'SMALL', 'MEDIUM', 'LARGE'}, text_density={'NONE', 'LOW', 'MEDIUM', 'HIGH'},
    mobile_readability_160={'PASS', 'PARTIAL', 'FAIL'}, background_complexity={'LOW', 'MEDIUM', 'HIGH'},
    title_relation={'DUPLICATES', 'COMPLEMENTS', 'ESCALATES', 'CONTRADICTS', 'UNRELATED', 'NO_TITLE'},
    reveal_too_much_risk={'LOW', 'MEDIUM', 'HIGH'}, confidence={'HIGH', 'MEDIUM', 'LOW'},
    art_style={'PHOTO', 'ILLUSTRATED_CARTOON', 'STICK_FIGURE', 'THREE_D_RENDER', 'AI_STYLE_ILLUSTRATION', 'SCREENSHOT_OR_DOCUMENT', 'MIXED', 'OTHER'},
    medical_label={'NOT_HEALTH', 'MEDICAL_PACKAGING_SAFE', 'NEEDS_CONTEXT', 'MISLEADING_RISK', 'CONTRADICTED_BY_CONTENT', 'UNRESOLVED'})
YN = ['arrow_present', 'before_after', 'numbers_in_text', 'age_marker', 'warning_color_used', 'face_visible', 'hierarchy_clear']
ALLOWED_TOP = set(NARR) | set(SCORES) | set(ENUM) | set(YN) | {'Thumbnail_ID', 'mechanism', 'mechanism_secondary', 'word_count', 'people_count_visible', 'expression_label',
    'hero_object', 'counterexample', 'score_100', 'evidence_labels', 'content_promise_verified', 'medical_flags', 'medical_notes', 'batch_id', 'seq', 'qa_status'}


def sents(t): return {re.sub(r'\W+', ' ', s).strip().lower() for s in re.split(r'(?<=[.;!?])\s+', t) if len(s) > 25}


def validate(rows, inputs=None):
    errs, warns = [], []
    if inputs is not None:
        want = [i['Thumbnail_ID'] for i in inputs]
        if [r.get('Thumbnail_ID') for r in rows] != want: errs.append('ROW_SET_OR_ORDER_MISMATCH')
        for i in inputs:
            p = ROOT / i['Source_Path']
            if hashlib.sha256(p.read_bytes()).hexdigest() != i['Thumbnail_ID'][4:]: errs.append(f"HASH_MISMATCH {i['Thumbnail_ID'][:12]}")
    for r in rows:
        t = r.get('Thumbnail_ID', '?')[:16]
        miss = [k for k in list(NARR) + list(SCORES) + list(ENUM) + YN + ['mechanism', 'score_100', 'word_count', 'hero_object', 'counterexample', 'medical_flags'] if k not in r]
        if miss: errs.append(f'{t} MISSING {miss}'); continue
        for k, v in ENUM.items():
            if r[k] not in v: errs.append(f'{t} BAD_ENUM {k}={r[k]!r}')
        for k in YN:
            if r[k] not in ('Y', 'N'): errs.append(f'{t} BAD_YN {k}')
        tot = 0
        for k, mx in SCORES.items():
            if not isinstance(r[k], int) or not 0 <= r[k] <= mx: errs.append(f'{t} SCORE_RANGE {k}={r[k]}')
            else: tot += r[k]
        if r['score_100'] != tot: errs.append(f"{t} SCORE_SUM {r['score_100']}!={tot}")
        for k in NARR:
            if not isinstance(r[k], str) or len(r[k].strip()) < (12 if k in ('strength', 'weakness', 'bottleneck') else 2 if k == 'text' else 25): errs.append(f'{t} TOO_SHORT {k}')
        if not isinstance(r['word_count'], int) or r['word_count'] < 0: errs.append(f'{t} BAD_WORD_COUNT')
        tx = re.sub(r'\[[^\]]*\]', '', r['text'])
        if (r['numbers_in_text'] == 'Y') != bool(re.search(r'\d', tx)) and not re.search(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|zero)\b', tx, re.I): errs.append(f'{t} NUMBERS_TAG_VS_TEXT')
        if (r['face_visible'] == 'N') != (r['face_scale'] == 'NONE'): errs.append(f'{t} FACE_TAG_MISMATCH')
        negated = re.search(r'\bno (separate |visible |literal )?arrows?\b|without (an )?arrows?|not an arrow', (r['scene'] + ' ' + r['composition']).lower())
        if r['arrow_present'] == 'N' and re.search(r'\barrow', (r['scene'] + ' ' + r['composition']).lower()) and not negated: warns.append(f'{t} ARROW_TAG_VS_NARRATIVE')
        if r['warning_color_used'] == 'N' and not re.search(r'no warning|not a warning|no red', r['colors'].lower()) and re.search(r'red[^.]*(warning|urgen|alarm|danger)|(warning|urgen|alarm|danger)[^.]*red', r['colors'].lower()): warns.append(f'{t} WARNING_COLOR_TAG_VS_COLORS')
        n_words = len(re.findall(r"[A-Za-z0-9$%#'’]+", tx))
        if r['word_count'] and abs(n_words - r['word_count']) > max(3, 0.35 * r['word_count']): warns.append(f"{t} WORD_COUNT {r['word_count']} vs {n_words}")
        extra = set(r) - ALLOWED_TOP
        if extra: errs.append(f'{t} UNKNOWN_FIELDS {sorted(extra)}')
    # template-repetition screen
    rep = []
    for k in ('strength', 'weakness', 'bottleneck', 'action', 'scan', 'psychology', 'partnership'):
        c = Counter(s for r in rows for s in sents(r.get(k, '')))
        rep += [(k, s[:70], n) for s, n in c.items() if n >= 3]
        for a, b in itertools.combinations(rows, 2):
            x, y = set(re.findall(r'\w+', a.get(k, '').lower())), set(re.findall(r'\w+', b.get(k, '').lower()))
            if x and y and len(x & y) / len(x | y) > 0.8 and len(x) > 6: rep.append((k, f"{a['Thumbnail_ID'][:12]}~{b['Thumbnail_ID'][:12]}", round(len(x & y) / len(x | y), 2)))
    sc = Counter(r.get('score_100') for r in rows)
    flags = dict(consistency_warnings=warns, repeated_sentences_or_near_duplicates=rep, most_common_total_score=sc.most_common(1), distinct_total_scores=len(sc),
                 mean_score=round(sum(r.get('score_100', 0) for r in rows) / max(1, len(rows)), 1))
    return errs, flags


if __name__ == '__main__':
    p = Path(sys.argv[1]); p = p if p.is_absolute() else HERE / p
    rows = json.loads(p.read_text())
    bid = re.search(r'(B\d+-\d+)', p.name).group(1)
    inp = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/audit') / bid / 'input.json'
    errs, flags = validate(rows, json.loads(inp.read_text()) if inp.exists() else None)
    print(json.dumps(dict(rows=len(rows), errors=errs[:40], n_errors=len(errs), **flags), indent=1)[:4000])
    sys.exit(1 if errs else 0)
