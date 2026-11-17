import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reconciliation-all-repository-2026-10-21"


class RepositoryUniverseContract(unittest.TestCase):
    def test_counts_and_disjointness(self):
        result = json.loads((OUT / "VALIDATION.json").read_text())
        self.assertEqual("PASS", result["status"])
        self.assertEqual((966, 197, 63, 180, 206, 1612), tuple(result[k] for k in
            ("original", "expansion_12_channel", "expansion_monkey", "landscape_additions", "casually_finance_additions", "combined_total")))
        self.assertEqual(0, result["pairwise_overlap"])
        self.assertEqual(430, result["deep_complete_original"])
        self.assertEqual(1182, result["remaining_deep_audit"])

    def test_unique_and_metadata_only_additions(self):
        with (OUT / "FINANCE_UNIVERSE.csv").open() as f: rows = list(csv.DictReader(f))
        with (OUT / "NEW_ELIGIBLE_ADDITIONS.csv").open() as f: additions = list(csv.DictReader(f))
        self.assertEqual(len(rows), len({r["video_id"] for r in rows}))
        self.assertEqual(386, len(additions))
        self.assertEqual({"METADATA_ONLY_NOT_DEEP_AUDITED"}, {r["audit_status"] for r in additions})

    def test_medium_monkey_review_is_bounded(self):
        with (OUT / "MONKEY_MEDIUM_CONFIDENCE_REVIEW.csv").open() as f: rows = list(csv.DictReader(f))
        self.assertEqual(10, len(rows))
        self.assertEqual({"MEDIUM"}, {r["review_confidence"] for r in rows})
        self.assertEqual({"NOT_REGISTERED"}, {r["transcript_status"] for r in rows})


if __name__ == "__main__":
    unittest.main()
