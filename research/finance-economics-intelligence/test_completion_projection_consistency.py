"""Current Finance completion must agree across live projections; the 2026-10-21
universe CSV is a frozen snapshot and must stay labelled as such."""
import csv
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "reconciliation-all-repository-2026-10-21"
COMPLETE = {"COMPLETE_EVIDENCE_BACKED", "COMPLETE_LIMITED_EVIDENCE"}


class CompletionProjectionConsistency(unittest.TestCase):
    def test_live_projections_agree_with_audit_ledger(self):
        ledger = [json.loads(line) for line in (ROOT / "VIDEO_AUDIT_966.jsonl").read_text().splitlines()]
        live = sum(all(s in COMPLETE for s in r["statuses"].values()) for r in ledger)
        with (ROOT / "VIDEO_COMPLETION_MATRIX.csv").open(newline="") as f:
            matrix = sum(all(v in COMPLETE for k, v in r.items() if k.endswith("_REVIEW")) for r in csv.DictReader(f))
        checkpoint = json.loads((ROOT / "FINANCE_PROGRESS_CHECKPOINT.json").read_text())["population"]
        built = json.loads(subprocess.check_output([sys.executable, str(ROOT / "build_combined_workbook_data.py")], text=True))["summary"]
        self.assertEqual(live, matrix)
        self.assertEqual(live, checkpoint["completed"])
        self.assertEqual(live, built["deep_audited"])
        self.assertEqual(1612 - live, checkpoint["remaining"])

    def test_universe_csv_is_a_checksummed_frozen_snapshot(self):
        sums = json.loads((SNAPSHOT / "FILE_CHECKSUMS_SHA256.json").read_text())
        digest = hashlib.sha256((SNAPSHOT / "FINANCE_UNIVERSE.csv").read_bytes()).hexdigest()
        self.assertEqual(sums["FINANCE_UNIVERSE.csv"], digest)
        readme = (SNAPSHOT / "SNAPSHOT_NOTICE.md").read_text()
        self.assertIn("FROZEN SNAPSHOT", readme)
        self.assertEqual(430, json.loads((SNAPSHOT / "VALIDATION.json").read_text())["deep_complete_original"])


if __name__ == "__main__":
    unittest.main()
