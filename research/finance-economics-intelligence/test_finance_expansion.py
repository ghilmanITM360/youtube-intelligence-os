import csv
import hashlib
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

    def test_audit_ledger_is_isolated_and_honest_about_missing_sources(self):
        with (ROOT / "FINANCE_EXPANSION_MASTER.csv").open(newline="", encoding="utf-8") as f:
            master = list(csv.DictReader(f))
        ledger = [json.loads(line) for line in (ROOT / "EXPANSION_AUDIT_LEDGER.jsonl").read_text().splitlines()]
        with (ROOT.parent / "audit-baseline" / "VIDEO_IDS.csv").open(newline="", encoding="utf-8") as f:
            baseline_ids = {row["Video_ID"] for row in csv.DictReader(f)}
        self.assertEqual({row["video_id"] for row in master}, {row["video_id"] for row in ledger})
        self.assertEqual(len(ledger), 197)
        self.assertFalse({row["video_id"] for row in ledger} & baseline_ids)
        target = next(row for row in ledger if row["video_id"] == "HjlVexL2Lxk")
        self.assertEqual(target["statuses"]["SCRIPT_REVIEW"], "BLOCKED_MISSING_SOURCE")
        self.assertEqual(target["statuses"]["TOPIC_REVIEW"], "BLOCKED_MISSING_SOURCE")
        self.assertEqual(target["deep_audit_completion"], "BLOCKED_PARTIAL_EVIDENCE")
        validation = json.loads((ROOT / "EXPANSION_AUDIT_VALIDATION.json").read_text())
        self.assertEqual(validation["registered_expansion_ids"], 197)
        self.assertEqual(validation["deep_audited"], 0)
        self.assertEqual(validation["blocked_partial_evidence"], 1)
        self.assertEqual(validation["metadata_only_not_started"], 196)
        self.assertTrue(all(validation["checks"].values()))

    def test_audit_checksums_cover_ledger_batch_receipt_and_image(self):
        checksums = json.loads((ROOT / "EXPANSION_AUDIT_CHECKSUMS_SHA256.json").read_text())
        required = {
            "EXPANSION_AUDIT_LEDGER.jsonl",
            "EXPANSION_AUDIT_VALIDATION.json",
            "audit-batches/EXPANSION_001.json",
            "audit-batches/EXPANSION_001_READ_RECEIPTS.json",
            "audit-evidence/HjlVexL2Lxk.jpg",
        }
        self.assertTrue(required <= set(checksums))
        for relative in required:
            self.assertEqual(checksums[relative], hashlib.sha256((ROOT / relative).read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
