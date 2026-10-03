"""Regression tests guarding against two confirmed Senior Health V3 research
defects recurring: a fabricated Google Trends claim (GT-20) and a breakout
event population miscount (29 vs. the correct 28). Both were found and fixed
by an independent audit on 2026-09-25 (STAGE2-CORRECTION-LEDGER.md, NC-03/NC-05).

This research tree (docs/research/senior-health-2026-09-25/) is not yet part
of the production pipeline and is currently untracked pending an explicit
decision on where to commit it; this test is written against its current
on-disk location so the checks are real and runnable now, not deferred.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V3_DIR = ROOT / "docs/research/senior-health-2026-09-25/forensic-v3"


def _skip_if_missing():
    return not V3_DIR.is_dir()


@unittest.skipIf(_skip_if_missing(), "senior-health forensic-v3 research tree not present")
class GT20FabricationRegressionTest(unittest.TestCase):
    """GT-20 ('how often should seniors shower') was fabricated in the original
    pass: claimed a post-video rise to means of 16.7-20, but the real raw
    series is flat 0 for all 262 weeks except one unrelated 2022 spike."""

    def test_raw_series_is_flat_zero_in_the_claimed_rise_window(self):
        raw_path = V3_DIR / "trends-raw/GT-20.json"
        data = json.loads(raw_path.read_text(encoding="utf-8"))
        points = data["points"]
        self.assertEqual(len(points), 262)
        # the originally-claimed rise window: the last 12 weeks of the series
        last_12 = points[-12:]
        self.assertTrue(
            all(p["value"] == 0 for p in last_12),
            "GT-20's claimed Aug-Sep 2026 rise window must remain flat 0 in the "
            "raw evidence; a nonzero value here would mean either the raw file "
            "was altered or a genuinely new Trends signal appeared and the "
            "correction needs re-review, not a silent revert.",
        )
        nonzero = [p for p in points if p["value"] > 0]
        self.assertEqual(
            len(nonzero), 1,
            "exactly one isolated non-zero point is expected (Mar 2022, value 100, "
            "unrelated to the claimed 2026 event); any other count means the raw "
            "file changed and the fabrication finding must be re-verified.",
        )

    def test_workbook_no_longer_states_the_fabricated_mean(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl not available")
        wb_path = V3_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"
        wb = openpyxl.load_workbook(wb_path, data_only=False)
        # 11_GOOGLE_TRENDS!J21 is GT-20's last_12w_mean; must be 0, not the
        # fabricated 8.3
        self.assertEqual(wb["11_GOOGLE_TRENDS"]["J21"].value, 0)
        # 12_TREND_ATTRIBUTION!G31/G32 are GT-20's mean_90d_after for its two
        # matched videos; must be 0, not the fabricated 16.7/20
        self.assertEqual(wb["12_TREND_ATTRIBUTION"]["G31"].value, 0)
        self.assertEqual(wb["12_TREND_ATTRIBUTION"]["G32"].value, 0)

    def test_workbook_readme_cell_is_not_an_accidental_formula(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl not available")
        wb_path = V3_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"
        wb = openpyxl.load_workbook(wb_path, data_only=False)
        value = wb["00_READ_ME"]["A49"].value
        self.assertIsNotNone(value)
        self.assertFalse(
            value.startswith("="),
            "00_READ_ME!A49 must not start with '=' - openpyxl/Excel treats any "
            "such cell as a formula, not text, silently breaking a decorative "
            "header (NC-06).",
        )


@unittest.skipIf(_skip_if_missing(), "senior-health forensic-v3 research tree not present")
class BreakoutEventPopulationReconciliationTest(unittest.TestCase):
    """The breakout event total was miscounted as 29 (23 internal + 6 external)
    in the original pass; the underlying per-case data actually summed to 28
    (23 internal + 5 external) after the NC-05 correction. On 2026-09-25, 9
    further internal events were added from Better Health While Aging
    (DS-000033), a newly acquired channel, bringing the total to 37 (32
    internal + 5 external). This guards the canonical event table and its
    downstream restatements against the same class of aggregate-vs-underlying
    mismatch (NC-05) while tolerating legitimate growth from new acquisitions."""

    def test_canonical_table_has_explicit_identity_keys_and_reconciles(self):
        table_path = V3_DIR / "cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json"
        data = json.loads(table_path.read_text(encoding="utf-8"))
        events = data["events"]
        self.assertEqual(len(events), 37)
        self.assertEqual(data["internal_count"], 32)
        self.assertEqual(data["external_count"], 5)
        self.assertEqual(
            sum(1 for e in events if e["source"] == "internal"), 32
        )
        self.assertEqual(
            sum(1 for e in events if e["source"] == "external"), 5
        )
        # every event must carry a unique identity key
        event_ids = [e["event_id"] for e in events]
        self.assertEqual(len(event_ids), len(set(event_ids)))
        # every internal event must carry a real canonical_channel_id and video_id
        for e in events:
            if e["source"] == "internal":
                self.assertTrue(e["channel_id"])
                self.assertTrue(e["video_id"])
        # 2026-09-25 Case 13 deep-dive: all 9 Better Health While Aging events
        # must carry the supplementary time-matched local baseline multiple.
        bhwa_ids = {
            "MpohFGvHZHI", "JUCiIDVTshA", "16n80OQCVSM", "XX5Kw2OotL0",
            "k-3BY-naQ0M", "Ev-i_E_MlTo", "8_depH-gT4o", "R7uXQBjnTjk",
            "OCWvaUcSPOU",
        }
        bhwa_events = [e for e in events if e["video_id"] in bhwa_ids]
        self.assertEqual(len(bhwa_events), 9)
        for e in bhwa_events:
            self.assertTrue(e.get("local_baseline_multiple"))

    def test_no_dependent_markdown_still_states_the_stale_29_6_count_as_fact(self):
        # any mention of the old "29 (23+6)" figure is fine IF it sits inside a
        # sentence that also marks it as a corrected/historical claim (the
        # master brief requires preserving the error as a labelled audit
        # record, not scrubbing it) - it is only a regression if the number
        # appears with no such marker nearby, i.e. restated as current fact.
        stale_pattern = re.compile(r"29\s*\(23\s*internal\s*\+\s*6\s*external", re.IGNORECASE)
        bare_stale = re.compile(r"\b29 breakout events\b")
        correction_markers = re.compile(
            r"NC-05|corrected|correction|retracted|superseded|misstated|"
            r"miscounted|prior claim|original(ly)?|an earlier|was wrong|"
            r"arithmetic error",
            re.IGNORECASE,
        )
        offenders = []
        for md_path in V3_DIR.glob("*.md"):
            text = md_path.read_text(encoding="utf-8")
            for m in list(stale_pattern.finditer(text)) + list(bare_stale.finditer(text)):
                window = text[max(0, m.start() - 200): m.end() + 200]
                if not correction_markers.search(window):
                    offenders.append((md_path.name, text[max(0, m.start()-40):m.end()+40]))
        self.assertEqual(
            offenders, [],
            f"these files state the corrected-away '29 (23+6)' breakout count "
            f"with no nearby correction marker, i.e. as current fact: {offenders}",
        )


@unittest.skipIf(_skip_if_missing(), "senior-health forensic-v3 research tree not present")
class MasterInventoryRegressionTest(unittest.TestCase):
    """The 2026-09-25 master inventory must keep BHWA's exact historical Shorts
    gap, keep the own channel out of competitor classes, and never count a
    removed or excluded lead as needing paid acquisition."""

    def setUp(self):
        path = V3_DIR / "SENIOR-HEALTH-MASTER-INVENTORY.json"
        self.rows = {r["ref"]: r for r in json.loads(path.read_text(encoding="utf-8"))["channels"]}

    def test_bhwa_missing_shorts_are_the_four_verified_ids(self):
        r = self.rows["UCFpxvukIqCAUA7YizI-q9Dw"]
        self.assertEqual(r["class"], "B")
        self.assertEqual(sorted(r["missing_shorts_ids"]),
                         sorted(["-SMFhfZrjm0", "U6kI1V6CQVs", "5Jqvsfq6UBo", "x0Z5ziQNtWQ"]))
        self.assertEqual(r["gap_kinds"], {"shorts": "HISTORICAL_GAP"})

    def test_own_channel_is_separate(self):
        self.assertEqual(self.rows["UCQIzqH7QZ9viBYpOFqgSXMg"]["class"], "OWN")
        self.assertEqual(sum(r["class"] == "OWN" for r in self.rows.values()), 1)

    def test_excluded_leads_need_no_spend_and_ids_are_unique(self):
        for r in self.rows.values():
            if r["class"] == "F":
                self.assertEqual(r["required_new_results"], 0, r["ref"])
        ids = [r["canonical_channel_id"] for r in self.rows.values() if r["canonical_channel_id"]]
        self.assertEqual(len(ids), len(set(ids)))


INVENTORY_2026_09_28 = V3_DIR / "SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json"


@unittest.skipIf(not INVENTORY_2026_09_28.exists(), "2026-09-28 master inventory not present")
class MasterInventory20260928RegressionTest(unittest.TestCase):
    """The 2026-09-28 inventory keeps every 2026-09-25 lead, keeps the own channel
    separate, never proposes spend on excluded leads, and its report totals are the
    sum of its rows."""

    CATEGORIES = {"ACQUIRED_COMPLETE_AT_SNAPSHOT", "ACQUIRED_WITH_HISTORICAL_GAPS", "ACQUIRED_WITH_NEW_PUBLIC_UPLOADS",
                  "PARTIALLY_ACQUIRED", "QUALIFIED_PENDING", "HEALTH_RELEVANT_IDENTITY_ONLY", "ADJACENT_HEALTH_REFERENCE",
                  "UNVERIFIED_IDENTITY", "REMOVED_OR_UNAVAILABLE", "EXCLUDED_BY_REVIEW", "OWN_CHANNEL"}

    def setUp(self):
        self.rows = json.loads(INVENTORY_2026_09_28.read_text(encoding="utf-8"))["channels"]
        self.by_ref = {r["ref"]: r for r in self.rows}

    def test_every_2026_09_25_lead_is_still_accounted_for(self):
        old = json.loads((V3_DIR / "SENIOR-HEALTH-MASTER-INVENTORY.json").read_text(encoding="utf-8"))["channels"]
        self.assertEqual({r["ref"] for r in old} - set(self.by_ref), set())

    def test_categories_ids_and_own_channel(self):
        self.assertTrue({r["inventory_category"] for r in self.rows} <= self.CATEGORIES)
        ids = [r["canonical_channel_id"] for r in self.rows if r["canonical_channel_id"]]
        self.assertEqual(len(ids), len(set(ids)))
        own = [r for r in self.rows if r["inventory_category"] == "OWN_CHANNEL"]
        self.assertEqual([r["canonical_channel_id"] for r in own], ["UCQIzqH7QZ9viBYpOFqgSXMg"])
        self.assertEqual(own[0]["required_new_results"], 0)

    def test_excluded_need_no_spend_and_qualified_pending_are_the_fourteen(self):
        for r in self.rows:
            if r["inventory_category"] in ("REMOVED_OR_UNAVAILABLE", "EXCLUDED_BY_REVIEW", "OWN_CHANNEL"):
                self.assertEqual(r["required_new_results"], 0, r["ref"])
        self.assertEqual(sum(r["inventory_category"] == "QUALIFIED_PENDING" for r in self.rows), 14)

    def test_collected_metadata_belongs_to_its_channel(self):
        for r in self.rows:
            self.assertEqual(r.get("meta_channel_id_mismatch_ids") or [], [], r["ref"])

    def test_report_category_counts_match_rows(self):
        report = (V3_DIR / "SENIOR-HEALTH-MASTER-INVENTORY-REPORT-2026-09-28.md").read_text(encoding="utf-8")
        from collections import Counter
        for category, count in Counter(r["inventory_category"] for r in self.rows).items():
            self.assertIn(f"{category} {count}", report)


if __name__ == "__main__":
    unittest.main()
