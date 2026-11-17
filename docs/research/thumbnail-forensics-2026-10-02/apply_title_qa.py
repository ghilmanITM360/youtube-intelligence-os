"""Apply the title-QA findings. Stage A (sample): build title-qa-corrections-log.csv from the six reviewer files and apply concrete ANALYST fixes.
PROGRAMMATIC findings are never hand-edited: they are fixed by rule changes in build_title_forensics.py (taxonomy v2) and marked
RESOLVED_BY_RULE_FIX when the rebuilt value equals the reviewer's proposal. Stage B (systematic): mechanical clean of analyst `unnecessary_words`
across all 2,303 rows (negations/non-title words). Every change is logged; nothing is edited silently. Usage: apply_title_qa.py
"""
import csv, glob, json, re, subprocess
from collections import Counter
from pathlib import Path
import validate_title_audit as V

HERE = Path(__file__).resolve().parent
OUTP = {'overpromise_risk', 'medical_title_flag', 'orientation', 'tells_too_much', 'tells_too_little'}
FREE = {'overpromise_note'}
LIM = dict(improvement=18, exact_promise=16, intended_viewer=8, core_topic=8, unanswered_question=14)
NEG = re.compile(r"^(?:never|not|no|don'?t|don’t|stop|only|nobody|can'?t|won'?t|without)$", re.I)
norm = lambda v: re.sub(r'\s+', ' ', str(v or '')).strip().upper()


BASE = '8711eed'  # last commit before any title-QA edit; the script always starts from it so reruns are idempotent


def load_chunks():
    ch = {}
    for f in sorted(glob.glob(str(HERE / 'title-analyst-audit-T-*.json'))):
        rel = Path(f).relative_to(HERE.parents[2])
        ch[f] = json.loads(subprocess.run(['git', 'show', f'{BASE}:{rel}'], cwd=HERE.parents[2], capture_output=True, text=True, check=True).stdout)
    idx = {r['Video_ID']: r for rows in ch.values() for r in rows}
    return ch, idx


def apply_value(r, field, prop):
    if field in OUTP:
        if prop in V.ENUM[field]: r[field] = prop; return True
        return False
    if field == 'mechanism_reliance':
        v = [x.strip() for x in re.split(r'[;,]', str(prop))]
        if v and set(v) <= V.REL: r[field] = v; return True
        return False
    if field in FREE:
        p = str(prop or '').strip()
        if p and not p.startswith('('): r[field] = p; return True
        return False
    if field in LIM:
        p = str(prop or '').strip()
        if not p or p.startswith('(') or re.match(r'(?:a |an )?(?:different|better) wording|coherent|none', p, re.I) or len(p.split()) > LIM[field] + 2: return False
        r[field] = p; return True
    if field in V.MAX and str(prop).strip().isdigit() and 0 <= int(prop) <= V.MAX[field]:
        r[field] = int(prop); r['score_100'] = sum(r[k] for k in V.MAX); return True
    return False


MANUAL = {  # (Video_ID, field): (new value, note) for reviewer findings whose proposal was descriptive rather than a value
    ('95kkamSxHr8', 'improvement'): ('Hedge it: "Nail Changes After 60 Worth Mentioning to Your Neurologist"', 'reviewer asked for wording distinct from the sibling title; coordinator wrote it'),
    ('ZqyV6kzdsO8', 'improvement'): (None, 'NO_CHANGE: existing rewrite already matches the literal reading adopted in the exact_promise correction'),
}
MATERIAL_SCORE = {'6LVsfOAdubA': dict(clarity_score=14, promise_strength_score=8, curiosity_score=10, audience_fit_score=6)}  # reviewer proposed total 64; components as listed sum to 65 (coordinator keeps specificity/credibility/concision)


def stage_b(idx, sel_log):
    """Systematic: strip negations (cutting them reverses meaning) and words that are not in the title from analyst unnecessary_words, project-wide."""
    out = []
    for vid, r in idx.items():
        t = r.get('_title', '')
        keep, drop = [], []
        for u in r.get('unnecessary_words', []):
            core = u.strip().strip(' ?.!,:').lower().replace('’', "'")
            if NEG.match(core) or core not in t: drop.append(u)
            else: keep.append(u)
        if drop:
            r['unnecessary_words'] = keep
            out.append(dict(Video_ID=vid, Field='unnecessary_words', Current_Value=';'.join(keep + drop), Proposed_Value=';'.join(keep), Reason=('negation word: removing it reverses the title meaning' if any(NEG.match(d.strip(' ?.!,:')) for d in drop) else 'item does not occur in the title text')))
    return out


def main():
    chunks, idx = load_chunks()
    tf0 = {r['Video_ID']: r['Exact_Title'] for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
    for vid, r in idx.items(): r['_title'] = tf0[vid].lower().replace('’', "'")
    v2 = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
    sel = json.load((HERE / 'title-qa-selection.json').open())['video_ids']
    log, n = [], 0
    for k in range(1, 7):
        for it in json.load((HERE / f'title-qa-review-{k}.json').open()):
            vid = it['Video_ID']
            for i in it['issues']:
                n += 1; cur, prop, fld = i.get('current'), i.get('proposed'), i['field']
                status, applied = 'LOGGED_NOT_APPLIED', ''
                if i['layer'] == 'PROGRAMMATIC':
                    new = v2[vid].get(fld)
                    status = 'RESOLVED_BY_RULE_FIX' if new is not None and norm(new) == norm(prop) else 'REMAINS_RULE_LIMITATION'
                    applied = new if new is not None else ''
                elif i['class'] in ('SUBJECTIVE', 'STYLE_ONLY'): status = 'NOT_APPLIED_' + i['class']
                elif (vid, fld) in MANUAL:
                    val, note = MANUAL[(vid, fld)]
                    if val is not None: idx[vid][fld] = val
                    status, applied = ('APPLIED_MANUAL' if val is not None else 'NO_CHANGE_NEEDED'), (val or note)
                elif fld == 'unnecessary_words':
                    keepw = [u for u in idx[vid].get('unnecessary_words', []) if str(prop or '').lower().find(u.strip(' ?.').lower()) >= 0 and not NEG.match(u.strip(' ?.!,:'))]
                    idx[vid]['unnecessary_words'] = keepw; status, applied = 'APPLIED', ';'.join(keepw)
                elif fld == 'ANALYST_TITLE_DIAGNOSTIC_SCORE':
                    for kk, vv in MATERIAL_SCORE[vid].items(): idx[vid][kk] = vv
                    idx[vid]['score_100'] = sum(idx[vid][kk] for kk in V.MAX); status, applied = 'APPLIED_MANUAL', idx[vid]['score_100']
                else:
                    before = idx[vid].get(fld)
                    if apply_value(idx[vid], fld, prop):
                        status, applied = 'APPLIED', idx[vid][fld]
                        if fld == 'overpromise_risk' and prop in ('MEDIUM', 'HIGH') and not idx[vid].get('overpromise_note'): idx[vid]['overpromise_note'] = i['reason'][:160]  # validator requires a note
                    else: status = 'MANUAL_REVIEW_NEEDED'
                log.append(dict(Correction_ID=f'TQA-{n:03d}', Source=f'SAMPLE_REVIEWER_{k}', Video_ID=vid, Layer=i['layer'], Field=fld, Error_Class=i['class'], Current_Value=cur, Proposed_Value=prop,
                                Reason=i['reason'], Status=status, Applied_Value=applied))
    for e in stage_b(idx, None):
        n += 1; log.append(dict(Correction_ID=f'TQA-{n:03d}', Source='SYSTEMATIC_MECHANICAL_ALL_ROWS', Video_ID=e['Video_ID'], Layer='ANALYST', Field=e['Field'], Error_Class='MINOR_FACTUAL', Current_Value=e['Current_Value'],
                                Proposed_Value=e['Proposed_Value'], Reason=e['Reason'], Status='APPLIED', Applied_Value=e['Proposed_Value']))
    for rows in chunks.values():
        for r in rows: r.pop('_title', None)
        for r in rows: r['qa_status'] = 'QA_SAMPLED' if r['Video_ID'] in set(sel) else 'NOT_SAMPLED'
    for f, rows in chunks.items(): json.dump(rows, open(f, 'w'), indent=1, ensure_ascii=False)
    with (HERE / 'title-qa-corrections-log.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(log[0])); w.writeheader(); w.writerows(log)
    print(Counter(l['Status'] for l in log))
    return log


if __name__ == '__main__': main()
