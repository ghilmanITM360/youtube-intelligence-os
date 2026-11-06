"""Reference-comparison annex helpers + structural validator (v1). Semantic quality is judged separately by the analyst.
TRANSCRIPT_RANGE and TITLE witnesses are checked against the registry. THUMBNAIL_OBSERVATION text is an analyst's unverified observation: passing proves nothing about the image.
Usage: python reference_comparison.py validate comparisons/NICK_281_REFERENCE_COMPARISON.json [...]"""
import csv, json, pathlib, re, sqlite3, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
JUDGMENTS = {'MET', 'PARTLY_MET', 'NOT_MET', 'NOT_EVALUABLE', 'NOT_APPLICABLE'}
HEDGED = {'FR-SCR-02', 'FR-INTRO-02', 'FR-16C-06'}          # retention-flavoured rules: must say inferred / not evaluable
REQUIRED_ANY = [{'FR-HOOK-01', 'FR-INTRO-01'}, {'FR-TITLE-02', 'FR-TITLE-03', 'FR-TITLE-04'}, {'FR-SCR-03', 'FR-16C-04'}, {'FR-SCR-02', 'FR-16C-07', 'FR-SCR-06'}, {'FR-BT-01', 'FR-16C-03', 'FR-SCR-04'}]
MEASURED = re.compile(r'\b(viewers? (dropped|left|clicked)|drop-?off (occurred|at)|ctr (was|of)|retention (was|dropped))\b', re.I)

MODES = {'PROSPECTIVE_AUDIT', 'HISTORICAL_REANALYSIS_CONTENT_FIRST', 'REASSESSMENT_ANNEX_NOT_AUDIT_RECEIPT'}

def rules():
    return {r['Rule_ID']: r for r in csv.DictReader(open(HERE / 'REFERENCE_RULE_INDEX_v1.csv'))}

def transcript(vid):
    con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    return con.execute('select transcript_text from transcripts where youtube_video_id=?', (vid,)).fetchone()[0]

def canonical_video(vid):
    """(title, transcript text) from the registry, or None for an unknown video."""
    con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    return con.execute('select v.title, t.transcript_text from videos v left join transcripts t using (youtube_video_id) where v.youtube_video_id=?', (vid,)).fetchone()

def witness(text, phrase):
    """Locate a whitespace-flexible phrase; must be unique. Returns a witness dict with raw offsets."""
    m = list(re.finditer(r'\s+'.join(map(re.escape, phrase.split())), text))
    assert len(m) == 1, f'{len(m)} matches for {phrase[:40]!r}'
    return {'kind': 'TRANSCRIPT_RANGE', 'start_char': m[0].start(), 'end_char': m[0].end(), 'text': m[0].group(0)}

def load(path):
    """Parsed comparison object, or None if the file is missing, not JSON, or not an object."""
    try: d = json.load(open(path))
    except (OSError, ValueError): return None
    return d if isinstance(d, dict) else None

def validate(path):
    d = load(path)
    if d is None: return ['unreadable or malformed comparison file']
    if not d.get('comparisons') or not isinstance(d['comparisons'], list): return ['no comparisons']
    video = canonical_video(d.get('video_id')) if isinstance(d.get('video_id'), str) else None
    if not video: return [f"unknown video {d.get('video_id')}"]
    title, t = video[0] or '', video[1] or ''
    R = rules(); e = []; seen = set()
    if d.get('assessment_mode') not in MODES: e.append('bad assessment_mode')
    for i, c in enumerate(d['comparisons']):
        if not isinstance(c, dict): e.append(f'malformed comparison #{i}'); continue
        k = f"{c.get('rule_id')}#{i}"; r = R.get(str(c.get('rule_id')))
        if not r: e.append('unknown rule ' + k); continue
        seen.add(c['rule_id'])
        if c.get('source_locator') != r['Locator'] or c.get('source_member') != r['Source_Member']: e.append('locator mismatch ' + k)
        if c.get('judgment') not in JUDGMENTS: e.append('bad judgment ' + k)
        w = c.get('witness') or {}
        if not isinstance(w, dict): e.append('malformed witness ' + k); continue
        if c.get('judgment') not in ('NOT_APPLICABLE', 'NOT_EVALUABLE') or w:
            text = w.get('text') if isinstance(w.get('text'), str) else ''
            if w.get('kind') == 'TRANSCRIPT_RANGE':
                a, b = w.get('start_char'), w.get('end_char')
                if not (isinstance(a, int) and isinstance(b, int) and text and t[a:b] == text): e.append('witness offset mismatch ' + k)
            elif w.get('kind') == 'TITLE':
                if not text.strip() or text not in title: e.append('witness not in canonical title ' + k)
            elif w.get('kind') == 'THUMBNAIL_OBSERVATION':
                if not text.strip(): e.append('empty witness ' + k)
            else: e.append('missing witness ' + k)
        rationale, uncertainty = str(c.get('rationale') or ''), str(c.get('uncertainty') or '')
        if len(rationale) < 40: e.append('thin rationale ' + k)
        if MEASURED.search(rationale + uncertainty): e.append('measured-behaviour claim ' + k)
        u = uncertainty.lower()
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

def check_coverage():
    """Gate: every accepted batch NICK_281+ must have a validating comparison; every ledger reanalysis file must validate."""
    import glob
    e = []; R = HERE.parent
    for f in glob.glob(str(R / 'audit-batches/NICK_*.json')):
        n = pathlib.Path(f).name
        if n.endswith(('_VALIDATION.json', '_RECEIPTS.json')): continue
        num = int(n.split('_')[1].split('.')[0]) if n.split('_')[1].split('.')[0].isdigit() else 0
        if num < 281: continue
        p = HERE / 'comparisons' / f'NICK_{num}_REFERENCE_COMPARISON.json'
        if not p.exists(): e.append(f'missing comparison NICK_{num}'); continue
        x = validate(str(p)); d = load(p) or {}; batch = load(f) or {}
        ids = {v.get('Video_ID') for v in batch.get('reviews', [])}
        if d.get('batch_id') != f'NICK_{num}': x.append('wrong batch_id')
        if d.get('video_id') not in ids: x.append('video not in batch')
        if d.get('assessment_mode') != 'PROSPECTIVE_AUDIT': x.append('accepted batch comparison must be PROSPECTIVE_AUDIT')
        e += [f'NICK_{num}: {m}' for m in x]
    for r in csv.DictReader(open(R / 'reanalysis/REANALYSIS_CAMPAIGN_LEDGER.csv')):
        if r['reanalysis_file']:
            x = validate(str(R / r['reanalysis_file']))
            if (load(R / r['reanalysis_file']) or {}).get('video_id') != r['video_id']: x.append('file is for another video')
            e += [f"{r['video_id']}: {m}" for m in x]
    return e
if __name__ == '__main__' and sys.argv[1:2] == ['check-all']:
    e = check_coverage(); print('OK' if not e else e); sys.exit(bool(e))
