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
