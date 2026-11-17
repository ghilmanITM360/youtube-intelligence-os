"""Structural check for a content plan's framework use (never certifies semantic quality).
Plan JSON: {plan_id, framework_version, retrieved: [section_id...], applications: [{stage, rule_id, implementation | exception}], unavailable_inputs: [..]}
An exception may omit rule_id when a stage has no rule to apply. Passing proves shape and provenance only: a reviewer still has to read the text.
Usage: python content_plan_check.py <db> <plan.json>"""
import json, re, sqlite3, sys
STAGES = ['TOPIC', 'TITLE_THUMBNAIL', 'HOOK_SCRIPT', 'STORYBOARD_EDIT', 'PAYOFF_CTA', 'SOURCE_ACCURACY', 'POST_PUBLICATION']
# v1 rule audit_dimension values that a stage can implement. Empty: v1 has no such rule, so the stage needs a reasoned exception.
STAGE_DIMENSIONS = {'TOPIC': {'TOPIC', 'VIRALITY'}, 'TITLE_THUMBNAIL': {'TITLE'}, 'HOOK_SCRIPT': {'SCRIPT'}, 'PAYOFF_CTA': {'SCRIPT'},
                    'STORYBOARD_EDIT': set(), 'SOURCE_ACCURACY': set(), 'POST_PUBLICATION': set()}
def trivial(text):
    """Shape only: rejects placeholders such as 'x' or 'TODO'. ponytail: a long meaningless sentence still passes; that is the reviewer's job."""
    return not isinstance(text, str) or len(text.strip()) < 20 or len(set(re.findall(r'[^\W\d_]{2,}', text.lower()))) < 3
def check(db, plan):
    try: return _check(db, plan)
    except sqlite3.Error as exc: return [f'knowledge database unreadable: {exc}']
def _check(db, plan):
    if not isinstance(plan, dict): return ['plan is not a JSON object']
    apps, retrieved = plan.get('applications', []), plan.get('retrieved')
    if not isinstance(apps, list) or not all(isinstance(a, dict) for a in apps): return ['applications must be a list of objects']
    if retrieved is not None and (not isinstance(retrieved, list) or not all(isinstance(s, str) for s in retrieved)): return ['retrieved must be a list of section ids']
    con = sqlite3.connect(f'file:{db}?mode=ro', uri=True); e = []
    if plan.get('framework_version') != 'v1': e.append('framework_version')
    if not retrieved: e.append('RETRIEVAL_EMPTY: no framework sections retrieved; do not claim framework use')
    sections = set()
    for sid in retrieved or []:
        row = con.execute('select member_id, locator from ref_section where section_id=?', (sid,)).fetchone()
        if row: sections.add(row)
        else: e.append('unknown section ' + sid)
    seen = set(); implemented = 0
    for a in apps:
        stage, rid, impl, exc = a.get('stage'), a.get('rule_id'), a.get('implementation'), a.get('exception')
        seen.add(stage if isinstance(stage, str) else None)
        if stage not in STAGES: e.append('bad stage ' + str(stage))
        if impl and exc: e.append(f'both implementation and exception for {rid}')
        if not (impl or exc): e.append(f'no implementation or exception for {rid}')
        for label, text in (('implementation', impl), ('exception', exc)):
            if text and trivial(text): e.append(f'trivial {label} for {stage}/{rid}')
        if rid is None and exc: continue
        r = con.execute('select rule_class, audit_dimension, member_id, locator from ref_rule where rule_id=? and framework_version=?', (rid, 'v1')).fetchone() if isinstance(rid, str) else None
        if not r: e.append('unknown rule ' + str(rid)); continue
        if r[0] == 'NOT_APPLICABLE': e.append('rule not applicable ' + rid)
        if impl and r[0] == 'DUPLICATED_OR_SUPERSEDED': e.append('superseded rule cannot be implemented ' + rid)
        if impl and stage in STAGES and r[1] not in STAGE_DIMENSIONS[stage]: e.append(f'rule dimension {r[1]} of {rid} does not fit stage {stage}')
        if not any((r[2], 'p.' + page) in sections for page in re.findall(r'p\.(\d+)', r[3])): e.append(f'rule {rid} source section not retrieved')
        implemented += bool(impl)
    if apps and not implemented: e.append('no rule implemented: every stage is an exception; do not claim framework use')
    e += ['stage missing ' + s for s in STAGES if s not in seen]
    return e
if __name__ == '__main__':
    e = check(sys.argv[1], json.load(open(sys.argv[2]))); print('OK (structural only)' if not e else e); sys.exit(bool(e))
