#!/usr/bin/env python3
"""Claim-blocking gate: research claim -> evidence -> approved wording -> scene -> on-screen graphics -> render authorization.

  python3 claim_gate.py check <claims.json> <scenes.json>     # exit 0 = AUTHORIZED, 1 = BLOCKED, 2 = bad input
  from claim_gate import authorize; authorize(claims, scenes)  # returns Report; Report.ok / Report.problems

WHAT THIS DOES: mechanically refuses scene specs that break the production contract (missing claim ids, blocked statuses,
absent evidence/quote locators, unlabelled hypotheticals, wrong arithmetic, quotes not present in the source text,
missing qualifications, unit mismatches, numbers on screen no claim supports, incompatible comparisons, any of the ten
semantic checks left unreviewed or marked fail).
WHAT IT CANNOT DO: establish truth. A reviewer must still read the cited source and set the ten checks honestly;
this gate only guarantees that an unreviewed/failed/missing check, or a number/quote/definition that is not in the cited
excerpt, cannot reach render. A source tag is never accepted as entailment: the evidence must carry a verbatim excerpt
and the claim's numbers, quote and defining terms must be present in it."""
import hashlib, json, re, sys, decimal
from decimal import Decimal, ROUND_HALF_UP

STATUSES = {'VERIFIED', 'VERIFIED WITH QUALIFICATION', 'HYPOTHETICAL', 'DISPUTED', 'UNVERIFIED', 'MISLEADING', 'REJECTED'}
BLOCKING = {'UNVERIFIED', 'MISLEADING', 'REJECTED'}
CHECKS = ['definition', 'population', 'geography', 'denominator', 'units', 'time_period', 'publication_date',
          'dataset_vintage', 'causal_vs_correlational', 'comparable_measures']
NUM = re.compile(r'(\$)?\s?(\d[\d,]*(?:\.\d+)?)\s?(%|percent)?')


class Report:
    def __init__(s): s.problems = []; s.notes = []
    @property
    def ok(s): return not s.problems
    def fail(s, where, msg): s.problems.append(f'{where}: {msg}')
    def __str__(s): return ('AUTHORIZED' if s.ok else 'BLOCKED') + ''.join('\n  - ' + p for p in s.problems)


def norm(t): return re.sub(r'\s+', ' ', (t or '').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()


def num_tokens(text):
    """(value Decimal, unit) for each number in text; unit USD, percent or none."""
    out = []
    for m in NUM.finditer(text or ''):
        v = Decimal(m.group(2).replace(',', ''))
        out.append((v, 'USD' if m.group(1) else ('percent' if m.group(3) else 'none'), m.group(0).strip()))
    return out


def safe_eval(expr):
    """Decimal arithmetic only: numbers, + - * / ** and parentheses."""
    if not re.fullmatch(r'[0-9.+\-*/() ]+', expr): raise ValueError('illegal characters in arithmetic expression')
    tokens = re.sub(r'(\d+\.?\d*)', r'Decimal("\1")', expr)
    return eval(tokens, {'__builtins__': {}, 'Decimal': Decimal})


def check_claim(c, sources, rep):
    cid = c.get('id', '?'); st = c.get('status')
    if st not in STATUSES: rep.fail(cid, f'unknown status {st!r}'); return
    if not c.get('approved_wording'): rep.fail(cid, 'no approved wording')
    if st in BLOCKING: return  # blocked at scene level; nothing further to prove
    ev = c.get('evidence') or []
    if st != 'HYPOTHETICAL' and not ev: rep.fail(cid, 'factual claim has no evidence (a source tag is not entailment)')
    texts = []
    for e in ev:
        s = sources.get(e.get('source_id'))
        if not s: rep.fail(cid, f"evidence cites unknown source {e.get('source_id')!r}"); continue
        for k in ('url', 'publisher', 'retrieved', 'sha256'):
            if not s.get(k): rep.fail(cid, f"source {s.get('id')} missing {k}")
        if 'published' not in s: rep.fail(cid, f"source {s.get('id')} missing published (write 'undated' explicitly if none)")
        if not e.get('locator') or not e.get('excerpt'): rep.fail(cid, 'evidence needs a locator and a verbatim excerpt')
        texts.append(norm(e.get('excerpt')))
    blob = ' '.join(texts)
    if st != 'HYPOTHETICAL':
        chk = c.get('checks') or {}
        for k in CHECKS:
            v = (chk.get(k) or {}).get('result')
            if v not in ('ok', 'na'): rep.fail(cid, f"semantic check '{k}' is {v!r} (must be reviewed as ok or na)")
            elif v == 'na' and not (chk[k].get('note') or '').strip(): rep.fail(cid, f"check '{k}' is na without a note")
        for n in c.get('numbers', []):
            shown = norm(n.get('as_in_source', ''))
            if not shown or shown not in blob: rep.fail(cid, f"number {n.get('as_in_source')!r} does not appear in the cited excerpt")
        for term in (c.get('definition') or {}).get('must_include', []):
            if norm(term) not in blob: rep.fail(cid, f"definition does not match the source: excerpt lacks {term!r}")
            if norm(term) not in norm(c.get('approved_wording')): rep.fail(cid, f"approved wording drops a defining element of the source definition: {term!r}")
        q = c.get('quote')
        if q:
            if norm(q.get('text')) not in blob: rep.fail(cid, 'quotation does not appear in the cited source excerpt')
            if not q.get('speaker') or norm(q['speaker']) not in blob + ' ' + norm(' '.join(str(sources.get(e.get('source_id'), {}).get('author', '')) for e in ev)):
                rep.fail(cid, 'quotation speaker is not attributed by the cited source')
        cmp_ = c.get('comparison')
        if cmp_ and not cmp_.get('compatible'): rep.fail(cid, 'comparison uses incompatible measures (definition, population, period or basis differ)')
    if st == 'VERIFIED WITH QUALIFICATION' and not (c.get('required_qualification') or '').strip(): rep.fail(cid, 'qualified claim lacks required_qualification')
    if st == 'DISPUTED' and len({e.get('source_id') for e in ev}) < 2: rep.fail(cid, 'disputed claim needs evidence from at least two sources')
    if st == 'HYPOTHETICAL':
        h = c.get('hypothetical') or {}
        if not h.get('label'): rep.fail(cid, 'hypothetical needs the exact on-screen label')
        if not h.get('arithmetic'): rep.fail(cid, 'hypothetical needs its arithmetic listed (expr, expected)')
        for a in h.get('arithmetic', []):
            try:
                got = safe_eval(a['expr']).quantize(Decimal(1).scaleb(-a.get('places', 2)), rounding=ROUND_HALF_UP)
                if got != Decimal(str(a['expected'])): rep.fail(cid, f"arithmetic wrong: {a['expr']} = {got}, claimed {a['expected']}")
            except Exception as ex: rep.fail(cid, f"arithmetic not evaluable ({ex})")


def claim_amounts(c):
    """(value, unit) pairs this claim licenses on screen."""
    out = set()
    for n in c.get('numbers', []): out.add((Decimal(str(n['value'])), n['unit']))
    for a in (c.get('hypothetical') or {}).get('arithmetic', []): out.add((Decimal(str(a['expected'])), a.get('unit', 'USD')))
    for n in (c.get('hypothetical') or {}).get('inputs', []): out.add((Decimal(str(n['value'])), n['unit']))
    return out


def check_scene(sc, claims, rep):
    sid = sc.get('id', '?'); onscreen = ' '.join(sc.get('on_screen_text', [])); nar = sc.get('narration', '')
    ids = sc.get('claim_ids') or []
    if not sc.get('factual', True): return
    if not ids: rep.fail(sid, 'factual scene references no claim id'); return
    allowed = set(); allowed_nar = norm(nar + ' ' + onscreen)
    for i in ids:
        c = claims.get(i)
        if not c: rep.fail(sid, f'unknown claim id {i}'); continue
        st = c.get('status')
        if st in BLOCKING: rep.fail(sid, f'claim {i} is {st}: affected factual scene may not be produced'); continue
        if st == 'DISPUTED' and not sc.get('represents_as_disputed'): rep.fail(sid, f'claim {i} is DISPUTED; scene must present it as disputed with both sources')
        if st == 'VERIFIED WITH QUALIFICATION':
            qual = norm(c.get('required_qualification'))
            if qual and qual not in allowed_nar: rep.fail(sid, f"claim {i} qualification {c.get('required_qualification')!r} missing from narration/on-screen text")
        if st == 'HYPOTHETICAL':
            label = norm((c.get('hypothetical') or {}).get('label'))
            if not label or label not in norm(onscreen): rep.fail(sid, f"claim {i} is HYPOTHETICAL but its label is not on screen")
        allowed |= claim_amounts(c)
    ign = {Decimal(str(x)) for x in sc.get('ignore_numbers', [])}
    for text, where in ((onscreen, 'on-screen'), (nar, 'narration')):
        for v, unit, raw in num_tokens(text):
            if v in ign and unit == 'none': continue
            if (v, unit) not in allowed:
                near = [u for (x, u) in allowed if x == v]
                why = f"unit mismatch (claim licenses {sorted(set(near))})" if near else 'no cited claim supports it'
                rep.fail(sid, f"{where} number {raw!r}: {why}")


def authorize(claims_doc, scenes_doc):
    rep = Report()
    sources = {s['id']: s for s in claims_doc.get('sources', [])}
    claims = {c['id']: c for c in claims_doc.get('claims', [])}
    used = {i for sc in scenes_doc.get('scenes', []) for i in sc.get('claim_ids', [])}
    for i in used:
        if i in claims: check_claim(claims[i], sources, rep)
    for sc in scenes_doc.get('scenes', []): check_scene(sc, claims, rep)
    return rep



# The render contract seals real backend arguments, including numeric geometry.
RENDER_OPS = {'txt', 'source', 'document', 'host', 'rect', 'stroke_item', 'arrow'}


def payload_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def payload_digest(value):
    return hashlib.sha256(payload_bytes(value)).hexdigest()


def authorize_render(register, storyboard, plan, spec, capture):
    """Authorize resolved inputs against separate, reviewer-maintained field bindings."""
    report = authorize(register, storyboard)
    approval = register.get('render_approval', {})
    claims = {c['id']: c for c in register['claims']}
    sources = {s['id']: s for s in register['sources']}
    story = {scene['id']: scene for scene in storyboard['scenes']}
    used = set()
    for name, rows, indexed in (
        ('claims', register['claims'], claims),
        ('sources', register['sources'], sources),
        ('storyboard.scenes', storyboard['scenes'], story),
    ):
        if len(rows) != len(indexed):
            report.fail(name, 'duplicate ID')

    def require_ids(path, ids, scene_ids=None):
        for claim_id in ids:
            used.add(claim_id)
            claim = claims.get(claim_id)
            if not claim:
                report.fail(path, f'unknown claim {claim_id}')
            elif claim['status'] in BLOCKING:
                report.fail(path, f'claim {claim_id} is {claim["status"]}')
            elif scene_ids is not None and claim_id not in scene_ids:
                report.fail(path, f'claim {claim_id} absent from scene approval')

    def exact(path, actual, expected):
        if payload_digest(actual) != expected:
            report.fail(path, 'differs from the approved render binding')

    source = spec['source']
    source_id = approval.get('document_source_id')
    approved_source = sources.get(source_id)
    if not approved_source:
        report.fail('document.source', f'unknown approved source {source_id}')
    else:
        if hashlib.sha256(capture).hexdigest() != approved_source['sha256']:
            report.fail('document.source.file', f'capture hash does not match {source_id}')
        for field in ('sha256', 'url', 'publisher', 'title'):
            if source[field] != approved_source[field]:
                report.fail(f'document.source.{field}', f'does not match {source_id}')
        exact(f'sources.{source_id}', approved_source, approval.get('source_digest'))

    require_ids('document.source.claim_ids', source['claim_ids'])
    mark_bindings = approval.get('annotations', {})
    for mark in spec['annotations']:
        path = f'document.annotations.{mark["id"]}'
        claim_id = mark['claim_id']
        require_ids(path, [claim_id], source['claim_ids'])
        binding = mark_bindings.get(mark['id'], {})
        evidence = [
            e for e in claims.get(claim_id, {}).get('evidence', [])
            if e['source_id'] == source_id and e['locator'] == binding.get('locator')
        ]
        if not norm(mark['passage']) or not any(norm(mark['passage']) in norm(e['excerpt']) for e in evidence):
            report.fail(path + '.passage', f'claim {claim_id} does not match the approved source excerpt')
        exact(f'{path} (claim {claim_id})', mark, binding.get('digest'))
    if set(mark_bindings) != {mark['id'] for mark in spec['annotations']}:
        report.fail('document.annotations', 'missing or unexpected annotation')
    exact('document (capture, crop, context and annotation order)', spec, approval.get('document_digest'))

    approved_scenes = approval.get('scenes', [])
    if [sc['id'] for sc in plan['scenes']] != [sc['id'] for sc in approved_scenes]:
        report.fail('render.scenes', 'missing, extra or reordered scene')
    for scene, approved in zip(plan['scenes'], approved_scenes):
        path = f'render.scenes.{scene["id"]}'
        scene_ids = story.get(scene['id'], {}).get('claim_ids', [])
        exact(path + '.header', {k: v for k, v in scene.items() if k != 'items'}, approved['header'])
        items = scene['items']
        if len(items) != len(approved['items']):
            report.fail(path + '.items', 'missing or extra rendering operation')
        for index, item in enumerate(items):
            item_path = f'{path}.items[{index}]'
            ids = item['claim_ids']
            require_ids(item_path, ids, scene_ids)
            if item['op'] not in RENDER_OPS:
                report.fail(item_path, f'unknown render operation {item["op"]}')
            if item['op'] == 'document' and ids != source['claim_ids']:
                report.fail(item_path, 'document claims differ from source claims')
            digest = approved['items'][index] if index < len(approved['items']) else None
            exact(f'{item_path} (claims {ids})', item, digest)
        for claim_id in {i for item in items for i in item['claim_ids']}:
            claim = claims.get(claim_id, {})
            if claim.get('status') == 'HYPOTHETICAL':
                label = claim['hypothetical']['label']
                if not any(
                    it['op'] == 'txt' and it['args'][0] == label and it['args'][5] == scene['start']
                    and claim_id in it['claim_ids'] for it in items
                ):
                    report.fail(path, f'claim {claim_id} needs its on-screen label from scene entry')
    for claim_id in sorted(used & claims.keys()):
        claim = claims[claim_id]
        if claim['status'] == 'VERIFIED WITH QUALIFICATION':
            qualification = norm(claim.get('required_qualification'))
            mark_id = approval.get('qualification_marks', {}).get(claim_id)
            has_mark = any(
                mark['claim_id'] == claim_id and mark['id'] == mark_id
                and qualification in norm(mark['passage'])
                for mark in spec['annotations']
            )
            if not qualification or not has_mark:
                report.fail(f'claims.{claim_id}.required_qualification',
                            f'approved rendered document mark {mark_id!r} is missing the qualification')
        exact(f'claims.{claim_id}', claims[claim_id], approval.get('claim_digests', {}).get(claim_id))
    exact('render.planned_clauses', plan['planned_clauses'], approval.get('planned_clauses'))
    exact('render.plan', plan, approval.get('plan_digest'))
    return report

if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] != 'check': print(__doc__); sys.exit(2)
    try: r = authorize(json.load(open(sys.argv[2])), json.load(open(sys.argv[3])))
    except Exception as e: print('bad input:', e); sys.exit(2)
    print(r); sys.exit(0 if r.ok else 1)
