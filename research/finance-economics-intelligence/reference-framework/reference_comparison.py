"""Reference-comparison annex helpers + structural validator (v1). Semantic quality is judged separately by the analyst.
Usage: python reference_comparison.py validate comparisons/NICK_281_REFERENCE_COMPARISON.json [...]"""
import csv, json, pathlib, re, sqlite3, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
JUDGMENTS = {'MET', 'PARTLY_MET', 'NOT_MET', 'NOT_EVALUABLE', 'NOT_APPLICABLE'}
HEDGED = {'FR-SCR-02', 'FR-INTRO-02', 'FR-16C-06'}          # retention-flavoured rules: must say inferred / not evaluable
REQUIRED_ANY = [{'FR-HOOK-01', 'FR-INTRO-01'}, {'FR-TITLE-02', 'FR-TITLE-03', 'FR-TITLE-04'}, {'FR-SCR-03', 'FR-16C-04'}, {'FR-SCR-02', 'FR-16C-07', 'FR-SCR-06'}, {'FR-BT-01', 'FR-16C-03', 'FR-SCR-04'}]
MEASURED = re.compile(r'\b(viewers? (dropped|left|clicked)|drop-?off (occurred|at)|ctr (was|of)|retention (was|dropped))\b', re.I)

def rules():
    return {r['Rule_ID']: r for r in csv.DictReader(open(HERE / 'REFERENCE_RULE_INDEX_v1.csv'))}

def transcript(vid):
    con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    return con.execute('select transcript_text from transcripts where youtube_video_id=?', (vid,)).fetchone()[0]

def witness(text, phrase):
    """Locate a whitespace-flexible phrase; must be unique. Returns a witness dict with raw offsets."""
    m = list(re.finditer(r'\s+'.join(map(re.escape, phrase.split())), text))
    assert len(m) == 1, f'{len(m)} matches for {phrase[:40]!r}'
    return {'kind': 'TRANSCRIPT_RANGE', 'start_char': m[0].start(), 'end_char': m[0].end(), 'text': m[0].group(0)}

def validate(path):
    d = json.load(open(path)); R = rules(); e = []
    t = transcript(d['video_id']); seen = set()
    for i, c in enumerate(d.get('comparisons', [])):
        k = f"{c.get('rule_id')}#{i}"; r = R.get(c.get('rule_id'))
        if not r: e.append('unknown rule ' + k); continue
        seen.add(c['rule_id'])
        if c.get('source_locator') != r['Locator'] or c.get('source_member') != r['Source_Member']: e.append('locator mismatch ' + k)
        if c.get('judgment') not in JUDGMENTS: e.append('bad judgment ' + k)
        w = c.get('witness') or {}
        if c['judgment'] not in ('NOT_APPLICABLE', 'NOT_EVALUABLE') or w:
            if w.get('kind') == 'TRANSCRIPT_RANGE':
                if t[w.get('start_char', -1):w.get('end_char', -1)] != w.get('text') or not w.get('text'): e.append('witness offset mismatch ' + k)
            elif w.get('kind') in ('TITLE', 'THUMBNAIL_OBSERVATION'):
                if not w.get('text'): e.append('empty witness ' + k)
            else: e.append('missing witness ' + k)
        if len(c.get('rationale', '')) < 40: e.append('thin rationale ' + k)
        if MEASURED.search(c.get('rationale', '') + c.get('uncertainty', '')): e.append('measured-behaviour claim ' + k)
        u = c.get('uncertainty', '').lower()
        if c['rule_id'] in HEDGED and not ('inferred' in u or 'not evaluable' in u): e.append('unhedged retention rule ' + k)
        if not u: e.append('no uncertainty ' + k)
    if d.get('assessment_mode') == 'PROSPECTIVE_AUDIT':
        for grp in REQUIRED_ANY:
            if not (grp & seen): e.append('coverage gap ' + '/'.join(sorted(grp)))
    if d.get('rule_index_version') != 'v1': e.append('rule index version')
    return e

if __name__ == '__main__' and sys.argv[1:2] == ['validate']:
    bad = 0
    for p in sys.argv[2:]:
        e = validate(p); print(p, 'OK' if not e else e); bad += bool(e)
    sys.exit(1 if bad else 0)

def row(rule_id, wit, judgment, rationale, uncertainty):
    r = rules()[rule_id]
    return {'rule_id': rule_id, 'source_member': r['Source_Member'], 'source_locator': r['Locator'], 'witness': wit,
            'judgment': judgment, 'rationale': rationale, 'uncertainty': uncertainty}
