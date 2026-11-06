import json, os, pathlib, sqlite3, unittest, copy, tempfile
from unittest import mock
import reference_comparison as rc
H = pathlib.Path(__file__).resolve().parent
class T(unittest.TestCase):
    def test_all_annexes_valid(self):
        for p in sorted((H / 'comparisons').glob('*.json')): self.assertEqual([], rc.validate(p), p.name)
    def test_rule_index_unique_and_sourced(self):
        R = rc.rules(); self.assertGreaterEqual(len(R), 30)
        for r in R.values():
            if r['Rule_Kind'] != 'NOT_APPLICABLE': self.assertEqual(64, len(r['Source_SHA256']), r['Rule_ID'])
    def test_validator_rejects_forged_witness_and_locator(self):
        p = next(iter(sorted((H / 'comparisons').glob('*.json')))); d = json.load(open(p))
        a = copy.deepcopy(d); a['comparisons'][0]['witness']['text'] = 'invented words'
        b = copy.deepcopy(d); b['comparisons'][0]['source_locator'] = 'p.99'
        for x in (a, b):
            with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f: json.dump(x, f)
            self.assertTrue(rc.validate(f.name))


class KnowledgeBaseTests(unittest.TestCase):
    def test_rebuild_retrieval_plan_gate_and_population(self):
        import hashlib, json, tempfile, build_reference_kb as kb, content_plan_check as cp
        db = tempfile.mktemp(suffix='.db'); con = kb.build(db, fresh=True)
        self.assertEqual(con.execute('select count(*) from ref_source_member').fetchone()[0], 20)
        self.assertEqual(con.execute('select count(*) from ref_constituent_video').fetchone()[0], 63)
        self.assertEqual(con.execute('pragma foreign_key_check').fetchall(), [])
        hits = kb.search(con, 'open loop', 3); self.assertTrue(hits)
        good = plan()
        self.assertEqual(cp.check(db, good), [])
        self.assertTrue(any('RETRIEVAL_EMPTY' in m for m in cp.check(db, {**good, 'retrieved': []})))
        self.assertTrue(any('no implementation' in m for m in cp.check(db, {**good, 'applications': [{'stage': 'TOPIC', 'rule_id': 'FR-SCR-03'}]})))
        fz = json.load(open(H.parent / 'reanalysis/REANALYSIS_POPULATION_v1.json'))
        self.assertEqual(len(fz['video_ids']), len(set(fz['video_ids'])))
        self.assertEqual(hashlib.sha256('\n'.join(sorted(fz['video_ids'])).encode()).hexdigest(), fz['population_sha256'])
        self.assertEqual(rc.check_coverage(), [])


class EntryPointTests(unittest.TestCase):
    """Real entry point: scripts/run_youtube_intelligence.py --framework-plan, backed by the tracked knowledge DB."""
    def test_orchestrator_framework_gate(self):
        import sys, json, tempfile
        root = H.parents[2]; sys.path.insert(0, str(root / 'scripts'))
        import run_youtube_intelligence as orch
        def run(plan):
            with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f: json.dump(plan, f)
            return orch.main(['--channel', 'CH-X', '--opportunity', 'OP-X', '--framework-plan', f.name])
        good = plan()
        self.assertEqual(orch.framework_plan_errors(self._write(good)), [])
        for bad in (dict(good, retrieved=[]), dict(good, applications=[dict(good['applications'][0], rule_id='FR-NOPE')] + good['applications'][1:]),
                    dict(good, applications=[{'stage': 'TOPIC', 'rule_id': 'FR-VC-01'}] + good['applications'][1:])):
            self.assertEqual(run(bad), 2)
        exc = dict(good, applications=[{'stage': 'TITLE_THUMBNAIL', 'rule_id': 'FR-TITLE-02', 'exception': 'not applicable to a Short: no title stage'} if a['stage'] == 'TITLE_THUMBNAIL' else a for a in good['applications']])
        self.assertEqual(orch.framework_plan_errors(self._write(exc)), [])
    @staticmethod
    def _write(p):
        import json, tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f: json.dump(p, f)
        return f.name


def _dump(obj):
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
        f.write(obj if isinstance(obj, str) else json.dumps(obj))
    return f.name


class AuditRegressionTests(unittest.TestCase):
    """Defects proved by the 2026-11-06 Machine A audit (C4-C7)."""

    def real(self):
        return json.load(open(H / 'comparisons/NICK_281_REFERENCE_COMPARISON.json'))

    def test_validate_rejects_empty_and_malformed_without_crashing(self):
        good = self.real()
        bad = {
            'empty object': {},
            'list': [],
            'not json': '{nope',
            'no comparisons': {**good, 'comparisons': []},
            'unknown video': {**good, 'video_id': 'NOT_A_VIDEO'},
            'non-dict row': {**good, 'comparisons': ['x']},
            'row missing judgment': {**good, 'comparisons': [{k: v for k, v in good['comparisons'][0].items() if k != 'judgment'}]},
            'non-dict witness': {**good, 'comparisons': [{**good['comparisons'][0], 'witness': 'x'}]},
            'non-int offsets': {**good, 'comparisons': [{**good['comparisons'][0], 'witness': {'kind': 'TRANSCRIPT_RANGE', 'start_char': 'a', 'end_char': None, 'text': 't'}}]},
            'no mode': {k: v for k, v in good.items() if k != 'assessment_mode'},
        }
        for name, doc in bad.items():
            with self.subTest(name):
                self.assertTrue(rc.validate(_dump(doc)))
        self.assertTrue(rc.validate('/nonexistent/comparison.json'))

    def test_title_witness_must_come_from_canonical_title(self):
        d = self.real(); i = next(n for n, c in enumerate(d['comparisons']) if (c.get('witness') or {}).get('kind') == 'TITLE')
        self.assertEqual([], rc.validate(_dump(d)))
        for fake in ('FABRICATED TEXT THAT IS NOT THE TITLE', '   '):
            d['comparisons'][i]['witness']['text'] = fake
            self.assertTrue(any('title' in m or 'empty' in m for m in rc.validate(_dump(d))), fake)

    def test_every_tracked_title_witness_still_matches(self):
        import glob
        files = glob.glob(str(H / 'comparisons/*.json')) + glob.glob(str(H.parent / 'reanalysis/videos/*.json'))
        n = sum((c.get('witness') or {}).get('kind') == 'TITLE' for f in files for c in json.load(open(f))['comparisons'])
        self.assertGreaterEqual(n, 57)
        for f in files: self.assertEqual([], rc.validate(f), f)

    def _coverage(self, doc, batch_id='NICK_281'):
        """check_coverage() against an isolated tree holding one batch and one comparison."""
        import shutil
        root = pathlib.Path(tempfile.mkdtemp()); rf = root / 'reference-framework'
        (rf / 'comparisons').mkdir(parents=True); (root / 'audit-batches').mkdir(); (root / 'reanalysis').mkdir()
        shutil.copy(H / 'REFERENCE_RULE_INDEX_v1.csv', rf)
        shutil.copy(H.parent / 'audit-batches' / f'{batch_id}.json', root / 'audit-batches')
        (root / 'reanalysis/REANALYSIS_CAMPAIGN_LEDGER.csv').write_text('video_id,reanalysis_file\n')
        (rf / 'comparisons' / f'{batch_id}_REFERENCE_COMPARISON.json').write_text(doc if isinstance(doc, str) else json.dumps(doc))
        with mock.patch.object(rc, 'HERE', rf):
            return rc.check_coverage()

    def test_coverage_gate_runs_validation(self):
        good = self.real()
        self.assertEqual([], self._coverage(good))
        wrong_rule = {**good, 'comparisons': [{**good['comparisons'][0], 'rule_id': 'FR-NOPE'}]}
        for name, doc in {'empty': {}, 'malformed': '{nope', 'invalid': wrong_rule,
                          'other batch': {**good, 'batch_id': 'NICK_282'},
                          'other video': {**good, 'video_id': json.load(open(H / 'comparisons/NICK_282_REFERENCE_COMPARISON.json'))['video_id']},
                          'not prospective': {**good, 'assessment_mode': 'REASSESSMENT_ANNEX_NOT_AUDIT_RECEIPT'}}.items():
            with self.subTest(name):
                self.assertTrue(self._coverage(doc))

    def test_real_coverage_passes(self):
        self.assertEqual([], rc.check_coverage())


DB = H.parents[2] / 'data/knowledge/reference_knowledge.db'


def plan(**over):
    """A plan the v1 rule set can honestly satisfy: stages without a v1 rule carry a reasoned exception."""
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    sid = lambda member, page: con.execute('select section_id from ref_section where member_id=? and locator=?', (member, page)).fetchone()[0]
    apps = [
        {'stage': 'TOPIC', 'rule_id': 'FR-VC-01', 'implementation': 'Topic is framed around a named audience pain point.'},
        {'stage': 'TITLE_THUMBNAIL', 'rule_id': 'FR-TITLE-02', 'implementation': 'Title candidates are checked against the retrieved title guidance.'},
        {'stage': 'HOOK_SCRIPT', 'rule_id': 'FR-HOOK-01', 'implementation': 'Opening uses context lean, then a contrarian snapback beat.'},
        {'stage': 'PAYOFF_CTA', 'rule_id': 'FR-16C-16', 'implementation': 'The ending loops back to the question asked in the opening.'},
        {'stage': 'STORYBOARD_EDIT', 'exception': 'Framework v1 has no storyboard rule; visual guidance is excluded as FR-NA.'},
        {'stage': 'SOURCE_ACCURACY', 'exception': 'Framework v1 has no source accuracy rule; handled by editorial fact checks.'},
        {'stage': 'POST_PUBLICATION', 'exception': 'Framework v1 has no post publication rule; no analytics exist before release.'},
    ]
    rules = {a['rule_id'] for a in apps if 'rule_id' in a}
    retrieved = sorted({sid(m, 'p.' + p) for m, loc in con.execute(f"select member_id, locator from ref_rule where rule_id in ({','.join('?' * len(rules))})", sorted(rules)) for p in __import__('re').findall(r'p\.(\d+)', loc)})
    return {'plan_id': 'T', 'framework_version': 'v1', 'retrieved': retrieved, 'applications': apps, **over}


class PlanGateTests(unittest.TestCase):
    def errs(self, p):
        import content_plan_check as cp
        return cp.check(str(DB), p)

    def swap(self, stage, **fields):
        p = plan(); p['applications'] = [{'stage': stage, **fields} if a['stage'] == stage else a for a in p['applications']]
        return p

    def test_honest_plan_passes(self):
        self.assertEqual([], self.errs(plan()))

    def test_trivial_text_rejected(self):
        for text in ('x', '.', 'TODO', 'n/a', 'tbd tbd tbd tbd tbd tbd tbd', 'x x x x x x x x x x x x x x'):
            with self.subTest(text):
                self.assertTrue(any('trivial' in m for m in self.errs(self.swap('TOPIC', rule_id='FR-VC-01', implementation=text))))
                self.assertTrue(any('trivial' in m for m in self.errs(self.swap('STORYBOARD_EDIT', exception=text))))

    def test_rule_dimension_must_fit_stage(self):
        impl = 'A concrete sentence describing how this plan applies it.'
        self.assertTrue(any('dimension' in m for m in self.errs(self.swap('TITLE_THUMBNAIL', rule_id='FR-HOOK-01', implementation=impl))))
        self.assertTrue(any('dimension' in m for m in self.errs(self.swap('STORYBOARD_EDIT', rule_id='FR-HOOK-01', implementation=impl))))

    def test_rule_must_come_from_retrieved_sections(self):
        p = plan(); con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
        other = con.execute("select section_id from ref_section where member_id='RM-63c5338e6a9e' limit 1").fetchone()[0]
        self.assertTrue(any('not retrieved' in m for m in self.errs({**p, 'retrieved': [other]})))

    def test_exception_cannot_replace_all_implementation(self):
        p = plan(); reason = 'Deliberately skipped because this format has no such stage.'
        p['applications'] = [{'stage': a['stage'], 'exception': reason} for a in p['applications']]
        self.assertTrue(any('no rule' in m.lower() for m in self.errs(p)))

    def test_ambiguous_and_malformed_rejected(self):
        both = self.swap('TOPIC', rule_id='FR-VC-01', implementation='A concrete sentence about the plan.', exception='A concrete sentence about the exception.')
        self.assertTrue(self.errs(both))
        for bad in ([], 'x', {**plan(), 'applications': 'x'}, {**plan(), 'applications': ['x']}, {**plan(), 'retrieved': [[]]}):
            with self.subTest(str(bad)[:30]):
                self.assertTrue(self.errs(bad))

    def test_every_rule_locator_resolves_to_a_section(self):
        import re
        con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
        for rid, member, loc in con.execute('select rule_id, member_id, locator from ref_rule where member_id is not null'):
            pages = re.findall(r'p\.(\d+)', loc)
            self.assertTrue(pages, rid)
            self.assertTrue([1 for x in pages if con.execute('select 1 from ref_section where member_id=? and locator=?', (member, 'p.' + x)).fetchone()], rid)


class FrameworkClaimTests(unittest.TestCase):
    def orch(self):
        import sys
        sys.path.insert(0, str(H.parents[2] / 'scripts'))
        import run_youtube_intelligence
        return run_youtube_intelligence

    def test_claim_without_plan_is_refused_before_any_output(self):
        o = self.orch(); out = tempfile.mkdtemp()
        with mock.patch.object(o, 'build_plan') as build, self.assertRaises(SystemExit) as stop:
            o.main(['--channel', 'CH-X', '--opportunity', 'OP-X', '--output-dir', out, '--framework-guided'])
        self.assertEqual(stop.exception.code, 2); build.assert_not_called(); self.assertEqual(os.listdir(out), [])

    def test_generic_run_does_not_need_framework(self):
        o = self.orch()
        with mock.patch.object(o, 'build_plan', return_value={}) as build, mock.patch.object(o, 'write_outputs', return_value=('j', 'm')):
            self.assertEqual(o.main(['--channel', 'CH-X', '--opportunity', 'OP-X']), 0)
        build.assert_called_once()

    def test_unreadable_plan_is_a_gate_failure(self):
        o = self.orch()
        for path in (_dump('{nope'), '/nonexistent/plan.json', _dump([])):
            self.assertEqual(o.main(['--channel', 'CH-X', '--opportunity', 'OP-X', '--framework-plan', path]), 2)

    def test_valid_plan_is_labelled_structural_only(self):
        o = self.orch()
        with mock.patch.object(o, 'build_plan', return_value={}), mock.patch.object(o, 'write_outputs', return_value=('j', 'm')) as w:
            self.assertEqual(o.main(['--channel', 'CH-X', '--opportunity', 'OP-X', '--framework-guided', '--framework-plan', _dump(plan())]), 0)
        self.assertEqual(w.call_args[0][0]['reference_framework']['status'], 'STRUCTURALLY_VALID_NOT_SEMANTICALLY_REVIEWED')


if __name__ == '__main__': unittest.main()
