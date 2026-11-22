"""The REAL proof register must authorize; each tampering must be refused (so the normal verified-production path cannot silently proceed)."""
import sys, os, json, copy, unittest
from pathlib import Path
P = str(Path(__file__).resolve().parents[4] / 'productions/doc-animation-proof-01') + '/'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from claim_gate import authorize
C = json.load(open(P + 'claims.json')); S = json.load(open(P + 'scenes.json'))
def claim(d, i): return next(c for c in d['claims'] if c['id'] == i)
class Proof(unittest.TestCase):
    def test_authorizes(self): self.assertTrue(authorize(C, S).ok)
    def test_unverified_blocks_doc_scene(self):
        d = copy.deepcopy(C); claim(d, 'C3')['status'] = 'UNVERIFIED'; self.assertFalse(authorize(d, S).ok)
    def test_altered_excerpt_breaks_number(self):
        d = copy.deepcopy(C); claim(d, 'C4')['evidence'][0]['excerpt'] = claim(d, 'C4')['evidence'][0]['excerpt'].replace('$52.50', '$52.00'); self.assertFalse(authorize(d, S).ok)
    def test_wrong_diagram_number_blocks(self):
        s = copy.deepcopy(S); s['scenes'][3]['on_screen_text'][-1] = 'Balance after year 3: $1,175.63'; self.assertFalse(authorize(C, s).ok)
    def test_dropping_hypothetical_label_blocks(self):
        s = copy.deepcopy(S); s['scenes'][4]['on_screen_text'][0] = 'Interest picture'; self.assertFalse(authorize(C, s).ok)
    def test_dropping_once_a_year_blocks(self):
        s = copy.deepcopy(S); sc = s['scenes'][1]; sc['narration'] = sc['narration'].replace('once a year', 'each period'); self.assertTrue(authorize(C, s).ok)   # still on screen as 'Once a year'
        sc['on_screen_text'] = [t.replace('Once a year', 'Yearly') for t in sc['on_screen_text']]; self.assertFalse(authorize(C, s).ok)   # gone from both
    def test_wrong_hypothetical_arithmetic_blocks(self):
        d = copy.deepcopy(C); claim(d, 'H2')['hypothetical']['arithmetic'][2]['expected'] = 7.36; self.assertFalse(authorize(d, S).ok)
if __name__ == '__main__': unittest.main()
