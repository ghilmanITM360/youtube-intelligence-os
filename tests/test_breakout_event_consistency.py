"""Regression guard for the 2026-09-25 breakout-count drift bugs.

History: the small-channel breakout inventory was first miscounted as
"29 events (23 internal + 6 external)" (NC-05, corrected to 28 = 23+5), then
grew to 37 (32 internal + 5 external) the same day after Better Health While
Aging was acquired and added as Case 13 — and the workbook's 00_READ_ME
addendum cell was left stating the now-superseded "28" until this pass.

Rather than hardcoding "37" (which will go stale again the next time a case
is added), this test checks that the three places that state a breakout
count agree with each other: the canonical JSON, the workbook's per-event
sheet, and the workbook's prose addendum.
"""
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
V3_DIR = REPO_ROOT / "docs/research/senior-health-2026-09-25/forensic-v3"
CANONICAL_TABLE = V3_DIR / "cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json"
WORKBOOK = V3_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"


@unittest.skipUnless(CANONICAL_TABLE.exists() and WORKBOOK.exists(), "V3 breakout artifacts not present in this checkout")
class BreakoutEventConsistencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.canonical = json.loads(CANONICAL_TABLE.read_text(encoding="utf-8"))
        from openpyxl import load_workbook
        cls.wb = load_workbook(str(WORKBOOK), read_only=True, data_only=True)

    def test_canonical_table_internal_plus_external_equals_total(self):
        c = self.canonical
        self.assertEqual(c["internal_count"] + c["external_count"], c["canonical_event_count"])

    def test_sheet_39_qualifying_row_count_matches_canonical_total(self):
        ws = self.wb["39_V3_BREAKOUT_INVENTORY"]
        rows = list(ws.iter_rows(values_only=True))
        header, data_rows = rows[0], rows[1:]
        qualifying = [
            r for r in data_rows
            if r[0] and r[1] and "NEGATIVE CONTROL" not in str(r[1])
        ]
        self.assertEqual(len(qualifying), self.canonical["canonical_event_count"])

    def test_readme_addendum_states_the_current_canonical_count(self):
        ws = self.wb["00_READ_ME"]
        addendum_text = " ".join(
            str(ws.cell(row=r, column=1).value or "")
            for r in range(1, ws.max_row + 1)
            if "breakout event" in str(ws.cell(row=r, column=1).value or "").lower()
        )
        total = self.canonical["canonical_event_count"]
        self.assertIn(
            f"to {total} breakout events", addendum_text,
            f"00_READ_ME addendum does not mention the current canonical total ({total}) — "
            "it likely still states a stale count from before the last breakout-inventory update",
        )

    def test_forensic_report_v3_cites_current_canonical_count(self):
        text = (V3_DIR / "SMALL-CHANNEL-BREAKOUT-FORENSICS.md").read_text(encoding="utf-8")
        total = self.canonical["canonical_event_count"]
        self.assertIn(f"{total}", text)


if __name__ == "__main__":
    unittest.main()
