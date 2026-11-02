"""Structural check for a content plan's framework use (never certifies semantic quality).
Plan JSON: {plan_id, framework_version, retrieved: [section_id...], applications: [{stage, rule_id, implementation | exception}], unavailable_inputs: [..]}
Usage: python content_plan_check.py <db> <plan.json>"""
import json, sqlite3, sys
STAGES = ['TOPIC', 'TITLE_THUMBNAIL', 'HOOK_SCRIPT', 'STORYBOARD_EDIT', 'PAYOFF_CTA', 'SOURCE_ACCURACY', 'POST_PUBLICATION']
def check(db, plan):
    con = sqlite3.connect(f'file:{db}?mode=ro', uri=True); e = []
    if plan.get('framework_version') != 'v1': e.append('framework_version')
    if not plan.get('retrieved'): e.append('RETRIEVAL_EMPTY: no framework sections retrieved; do not claim framework use')
    for sid in plan.get('retrieved', []):
        if not con.execute('select 1 from ref_section where section_id=?', (sid,)).fetchone(): e.append('unknown section ' + sid)
    seen = set()
    for a in plan.get('applications', []):
        seen.add(a.get('stage'))
        if a.get('stage') not in STAGES: e.append('bad stage ' + str(a.get('stage')))
        r = con.execute('select rule_class from ref_rule where rule_id=? and framework_version=?', (a.get('rule_id'), 'v1')).fetchone()
        if not r: e.append('unknown rule ' + str(a.get('rule_id')))
        elif r[0] == 'NOT_APPLICABLE': e.append('rule not applicable ' + a['rule_id'])
        if not (a.get('implementation') or a.get('exception')): e.append(f"no implementation or exception for {a.get('rule_id')}")
    e += ['stage missing ' + s for s in STAGES if s not in seen]
    return e
if __name__ == '__main__':
    e = check(sys.argv[1], json.load(open(sys.argv[2]))); print('OK (structural only)' if not e else e); sys.exit(bool(e))
