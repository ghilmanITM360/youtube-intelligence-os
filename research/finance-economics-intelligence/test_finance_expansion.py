import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "expansion-12-channel-2026-10-20"


class ExpansionContract(unittest.TestCase):
    def test_validation_contract(self):
        v = json.loads((ROOT / "EXPANSION_VALIDATION.json").read_text())
        self.assertEqual(v["status"], "PASS")
        self.assertEqual(v["captured_rows"], 445)
        self.assertEqual(v["frozen_baseline_unique_ids"], 966)
        self.assertTrue(all(v["checks"].values()))

    def test_master_and_crosswalk_reconcile(self):
        with (ROOT / "FINANCE_INCLUSION_CROSSWALK.csv").open(newline="", encoding="utf-8") as f:
            crosswalk = list(csv.DictReader(f))
        with (ROOT / "FINANCE_EXPANSION_MASTER.csv").open(newline="", encoding="utf-8") as f:
            master = list(csv.DictReader(f))
        expected = {r["video_id"] for r in crosswalk if r["expansion_disposition"] == "INCLUDE_UNIQUE_EXPANSION"}
        actual = {r["video_id"] for r in master}
        self.assertEqual(len(crosswalk), 445)
        self.assertEqual(expected, actual)
        self.assertEqual(len(actual), len(master))


if __name__ == "__main__":
    unittest.main()
