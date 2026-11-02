import json, pathlib, unittest, copy, tempfile
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
if __name__ == '__main__': unittest.main()


class KnowledgeBaseTests(unittest.TestCase):
    def test_rebuild_retrieval_plan_gate_and_population(self):
        import hashlib, json, tempfile, build_reference_kb as kb, content_plan_check as cp
        db = tempfile.mktemp(suffix='.db'); con = kb.build(db, fresh=True)
        self.assertEqual(con.execute('select count(*) from ref_source_member').fetchone()[0], 20)
        self.assertEqual(con.execute('select count(*) from ref_constituent_video').fetchone()[0], 62)
        self.assertEqual(con.execute('pragma foreign_key_check').fetchall(), [])
        hits = kb.search(con, 'open loop', 3); self.assertTrue(hits)
        good = {'plan_id': 'T', 'framework_version': 'v1', 'retrieved': [hits[0][0]], 'applications': [{'stage': s, 'rule_id': 'FR-SCR-03', 'implementation': 'x'} for s in cp.STAGES]}
        self.assertEqual(cp.check(db, good), [])
        self.assertTrue(any('RETRIEVAL_EMPTY' in m for m in cp.check(db, {**good, 'retrieved': []})))
        self.assertTrue(any('no implementation' in m for m in cp.check(db, {**good, 'applications': [{'stage': 'TOPIC', 'rule_id': 'FR-SCR-03'}]})))
        fz = json.load(open(H.parent / 'reanalysis/REANALYSIS_POPULATION_v1.json'))
        self.assertEqual(len(fz['video_ids']), len(set(fz['video_ids'])))
        self.assertEqual(hashlib.sha256('\n'.join(sorted(fz['video_ids'])).encode()).hexdigest(), fz['population_sha256'])
        self.assertEqual(rc.check_coverage(), [])
