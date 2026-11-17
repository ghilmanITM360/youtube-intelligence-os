import json
import sqlite3
import unittest

from validate_audit_966 import BASE, ROOT, contiguous_range_errors, strict_receipt_errors


class CurrentDeepAuditQualityContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = {r['Video_ID']: r for r in map(json.loads, (BASE/'VIDEO_AUDIT_966.jsonl').read_text().splitlines())}
        cls.master = {r['Video_ID']: r for r in __import__('build_audit_966').read('VIDEO_MASTER.csv')}
        cls.con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)

    @classmethod
    def tearDownClass(cls):
        cls.con.close()

    def test_recent_receipts_reconcile_to_canonical_evidence(self):
        for video_id in ('RgaTGzeFcPQ','RmJKnJkUgxA','S0xwBH_fAn0','SsHQ-TtXhRQ'):
            with self.subTest(video_id=video_id):
                text = self.con.execute('select transcript_text from transcripts where youtube_video_id=?',(video_id,)).fetchone()[0]
                self.assertEqual([], strict_receipt_errors(self.rows[video_id], text, self.master))

    def test_ranges_must_cover_every_character_once(self):
        self.assertEqual([], contiguous_range_errors([[0,4],[4,9]],9))
        self.assertTrue(contiguous_range_errors([[0,4],[5,9]],9))
        self.assertTrue(contiguous_range_errors([[0,4]],9))

    def test_nick_162_census_household_income_bin_contract(self):
        receipts = json.loads((BASE / 'audit-batches/NICK_162_READ_RECEIPTS.json').read_text())
        census = next(r for r in receipts['primary_source_receipts']
                      if r['claim'] == 'Household income distribution')
        self.assertEqual('ACSST1Y2024.S1901', census['dataset'])
        self.assertEqual('2024_ACS_1_YEAR', census['source_date'])
        self.assertEqual('United States (010XX00US)', census['geography'])
        self.assertEqual('Households estimate', census['estimate_column'])
        self.assertEqual('United States households', census['population_denominator'])
        self.assertEqual(132737146, census['total_households'])
        self.assertEqual(
            {'label': '$50,000 to $74,999', 'estimate_percent': 15.6},
            census['variables']['S1901_C01_007E'],
        )
        self.assertEqual(
            {'label': '$200,000 or more', 'estimate_percent': 13.7},
            census['variables']['S1901_C01_011E'],
        )
        claim = next(c for c in self.rows['S_8SLGjLrBM']['script']['claim_audit']
                     if c['claim'].startswith('Only 12%-13%'))
        self.assertIn('13.7%', claim['assessment'])
        self.assertIn('$50,000-$74,999', claim['assessment'])
        self.assertNotIn('15.6% of households at $200,000 or more', claim['assessment'])


if __name__ == '__main__':
    unittest.main()
