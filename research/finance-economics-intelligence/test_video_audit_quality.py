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
        for video_id in ('RgaTGzeFcPQ','RmJKnJkUgxA','S0xwBH_fAn0'):
            with self.subTest(video_id=video_id):
                text = self.con.execute('select transcript_text from transcripts where youtube_video_id=?',(video_id,)).fetchone()[0]
                self.assertEqual([], strict_receipt_errors(self.rows[video_id], text, self.master))

    def test_ranges_must_cover_every_character_once(self):
        self.assertEqual([], contiguous_range_errors([[0,4],[4,9]],9))
        self.assertTrue(contiguous_range_errors([[0,4],[5,9]],9))
        self.assertTrue(contiguous_range_errors([[0,4]],9))


if __name__ == '__main__':
    unittest.main()
