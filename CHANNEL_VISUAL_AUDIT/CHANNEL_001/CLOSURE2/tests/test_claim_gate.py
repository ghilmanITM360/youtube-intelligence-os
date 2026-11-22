import sys, os, copy, unittest, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from claim_gate import authorize

CHK = {k: {'result': 'ok'} for k in ['definition', 'population', 'geography', 'denominator', 'units', 'time_period', 'publication_date', 'dataset_vintage', 'causal_vs_correlational', 'comparable_measures']}
SRC = {'id': 'S1', 'url': 'https://example.gov/page', 'publisher': 'Example Agency', 'retrieved': '2026-11-22', 'published': '2023-10-19', 'sha256': 'ab' * 32}
EXC = 'Net interest margin is net interest income divided by average earning assets. The agency said "rates will stay flat". The hypothetical example used $1,000.'
def claim(**kw):
    c = {'id': 'C1', 'status': 'VERIFIED', 'approved_wording': 'Net interest margin is net interest income divided by average earning assets.',
         'evidence': [{'source_id': 'S1', 'locator': 'para 1', 'excerpt': EXC}], 'checks': copy.deepcopy(CHK),
         'definition': {'must_include': ['net interest income', 'average earning assets']}, 'numbers': []}
    c.update(kw); return c
def scene(**kw):
    s = {'id': 'SC1', 'factual': True, 'claim_ids': ['C1'], 'narration': 'Net interest margin is a ratio.', 'on_screen_text': ['Net interest margin']}
    s.update(kw); return s
def run(c, s):
    return authorize({'sources': [SRC], 'claims': c if isinstance(c, list) else [c]}, {'scenes': [s]})
def hyp(**kw):
    c = {'id': 'C1', 'status': 'HYPOTHETICAL', 'approved_wording': 'Hypothetical: $1,000 at 5% for 2 years.',
         'hypothetical': {'label': 'Hypothetical example', 'inputs': [{'value': 1000, 'unit': 'USD'}, {'value': 5, 'unit': 'percent'}],
                          'arithmetic': [{'expr': '1000*1.05**2', 'expected': 1102.5, 'unit': 'USD'}]}}
    c.update(kw); return c

class Gate(unittest.TestCase):
    def test_positive_control_authorizes(self): self.assertTrue(run(claim(), scene()).ok)
    def test_banking_definition_error_blocked(self):   # earlier transfer test: NIM described as a two-rate spread
        r = run(claim(approved_wording='Net interest margin is the gap between the loan rate and the deposit rate.'), scene())
        self.assertFalse(r.ok); self.assertIn('defining element', str(r))
    def test_dollar_vs_percentage_conflation_blocked(self):   # C-12: $17.50 shown as 17.5%
        c = claim(numbers=[{'value': 17.5, 'unit': 'USD', 'as_in_source': '$1,000'}])
        r = run(c, scene(on_screen_text=['17.5%']))
        self.assertFalse(r.ok)
    def test_unsupported_number_blocked(self):
        r = run(claim(), scene(on_screen_text=['Banks keep $2,400']))
        self.assertFalse(r.ok); self.assertIn('no cited claim supports', str(r))
    def test_number_not_in_excerpt_blocked(self):
        r = run(claim(numbers=[{'value': 7, 'unit': 'percent', 'as_in_source': '7.1%'}]), scene(on_screen_text=['7%']))
        self.assertFalse(r.ok); self.assertIn('does not appear in the cited excerpt', str(r))
    def test_misleading_comparison_blocked(self):
        self.assertFalse(run(claim(comparison={'a': 'avg deposit rate', 'b': 'one bank APR', 'compatible': False}), scene()).ok)
        self.assertFalse(run(claim(status='MISLEADING'), scene()).ok)
    def test_hypothetical_shown_as_actual_blocked(self):
        r = run(hyp(), scene(on_screen_text=['$1,102.50 after 2 years']))
        self.assertFalse(r.ok); self.assertIn('label is not on screen', str(r))
    def test_hypothetical_labelled_and_correct_passes(self):
        self.assertTrue(run(hyp(), scene(on_screen_text=['Hypothetical example: $1,000 at 5% grows to $1,102.50'], ignore_numbers=[2])).ok)
    def test_hypothetical_wrong_arithmetic_blocked(self):
        c = hyp(); c['hypothetical']['arithmetic'][0]['expected'] = 1105.0
        self.assertFalse(run(c, scene(on_screen_text=['Hypothetical example'])).ok)
    def test_fabricated_quotation_blocked(self):
        r = run(claim(quote={'text': 'rates will triple', 'speaker': 'Example Agency'}), scene())
        self.assertFalse(r.ok); self.assertIn('quotation does not appear', str(r))
    def test_real_quotation_passes(self):
        self.assertTrue(run(claim(quote={'text': 'rates will stay flat', 'speaker': 'agency'}), scene()).ok)
    def test_missing_qualification_blocked(self):
        c = claim(status='VERIFIED WITH QUALIFICATION', required_qualification='calculated once a year')
        self.assertFalse(run(c, scene()).ok)
        self.assertTrue(run(c, scene(narration='Net interest margin, calculated once a year.')).ok)
    def test_unverified_and_rejected_block(self):
        for st in ('UNVERIFIED', 'REJECTED'): self.assertFalse(run(claim(status=st), scene()).ok)
    def test_source_tag_without_excerpt_blocked(self):
        c = claim(); c['evidence'][0]['excerpt'] = ''
        r = run(c, scene()); self.assertFalse(r.ok)
    def test_unreviewed_check_blocked(self):
        c = claim(); c['checks']['denominator']['result'] = 'unreviewed'; self.assertFalse(run(c, scene()).ok)
        c = claim(); c['checks']['time_period'] = {'result': 'fail'}; self.assertFalse(run(c, scene()).ok)
        c = claim(); c['checks']['geography'] = {'result': 'na'}; self.assertFalse(run(c, scene()).ok)  # na needs a note
    def test_disputed_needs_flag_and_two_sources(self):
        self.assertFalse(run(claim(status='DISPUTED'), scene()).ok)
    def test_factual_scene_without_claim_blocked(self): self.assertFalse(run(claim(), scene(claim_ids=[])).ok)
    def test_unknown_claim_id_blocked(self): self.assertFalse(run(claim(), scene(claim_ids=['C9'])).ok)
    def test_nonfactual_scene_not_gated(self): self.assertTrue(run(claim(), scene(factual=False, claim_ids=[], on_screen_text=['$999'])).ok)

if __name__ == '__main__': unittest.main()
