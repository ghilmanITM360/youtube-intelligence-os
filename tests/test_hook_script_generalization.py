import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import report_hook_script_intelligence as report  # noqa: E402
from report_common import connect  # noqa: E402


class GeneralizedChannelArtifactTests(unittest.TestCase):
    """CH-000001/002/003 use the same generic reporter as CH-000004/005 --
    no channel-specific branch, measured-only (interpretations=None) mode."""

    CHANNELS = {
        "CH-000001": "data/intelligence/channels/CH-000001/hook-script-intelligence-2026-09-11.json",
        "CH-000002": "data/intelligence/channels/CH-000002/hook-script-intelligence-2026-09-11.json",
        "CH-000003": "data/intelligence/channels/CH-000003/hook-script-intelligence-2026-09-11.json",
    }

    def _payload(self, channel_id):
        return json.loads((ROOT / self.CHANNELS[channel_id]).read_text(encoding="utf-8"))

    def test_no_channel_or_niche_specific_branch_in_core_reporter(self):
        source = (ROOT / "scripts/report_hook_script_intelligence.py").read_text(encoding="utf-8").lower()
        for forbidden in ("ch-000001", "ch-000002", "ch-000003", "matty", "mr finance", "aliza"):
            self.assertNotIn(forbidden, source)

    def test_all_generalized_channels_produce_working_capability_verdict(self):
        for channel_id in self.CHANNELS:
            payload = self._payload(channel_id)
            self.assertEqual(payload["schema_version"], "hook-script-intelligence-1")
            self.assertEqual(payload["capability_verdict"], "PASS")

    def test_archetypes_only_present_where_evidence_supports(self):
        for channel_id in self.CHANNELS:
            payload = self._payload(channel_id)
            self.assertGreater(len(payload["hook_archetypes"]), 0)
            self.assertGreater(len(payload["script_archetypes"]), 0)
            for archetype in payload["hook_archetypes"] + payload["script_archetypes"]:
                self.assertGreaterEqual(archetype["item_count"], 1)
                self.assertIn("counter_examples", archetype)

    def test_no_private_metrics_fabricated_in_generalized_artifacts(self):
        forbidden = {"retention", "ctr", "impressions", "watch_time", "average_view_duration",
                     "unique_viewers", "traffic_sources", "subscriber_conversion"}
        for channel_id in self.CHANNELS:
            payload = self._payload(channel_id)
            self.assertFalse(forbidden & report.recursive_keys(payload))
            self.assertEqual(payload["guardrails"]["private_retention_available"], False)
            self.assertEqual(payload["guardrails"]["retention_claims_created"], 0)

    def test_ch1_unavailable_transcript_is_disclosed_not_silently_dropped(self):
        payload = self._payload("CH-000001")
        snapshot = payload["evidence_snapshot"]
        self.assertEqual(snapshot["canonical_item_count"], 94)
        self.assertEqual(snapshot["transcripts_accounted_for"], 93)
        self.assertEqual(snapshot["unavailable_transcripts"], ["VID-000148"])
        self.assertTrue(any("VID-000148" in item for item in payload["limitations"]))

    def test_ch2_and_ch3_have_no_unavailable_transcripts(self):
        for channel_id in ("CH-000002", "CH-000003"):
            payload = self._payload(channel_id)
            self.assertEqual(payload["evidence_snapshot"]["unavailable_transcripts"], [])


@unittest.skipUnless((ROOT / "data/raw/competitors/DS-000001").exists(), "requires ignored historical transcript archive")
class ArchiveMemberTranscriptReadTests(unittest.TestCase):
    """CH-000001/002 store transcripts inside a zip (ARCHIVE_MEMBER source_files),
    unlike CH-000004/005's physical files -- the shared reporter must read both."""

    def test_load_canonical_rows_resolves_archive_and_physical_storage(self):
        with connect() as conn:
            ch1_rows = report.load_canonical_rows(conn, "CH-000001")
            ch4_rows = report.load_canonical_rows(conn, "CH-000004")
        self.assertTrue(any(r["transcript_storage_kind"] == "ARCHIVE_MEMBER" for r in ch1_rows))
        self.assertTrue(all(r["transcript_storage_kind"] == "PHYSICAL_FILE" for r in ch4_rows if r["availability_status"] == "AVAILABLE"))

    def test_read_canonical_transcript_raw_handles_both_kinds(self):
        with connect() as conn:
            ch1_rows = report.load_canonical_rows(conn, "CH-000001")
        available = [r for r in ch1_rows if r["availability_status"] == "AVAILABLE"][0]
        text = report.read_canonical_transcript_raw(available)
        self.assertIn("TRANSCRIPT", text)

    def test_unavailable_transcript_row_is_never_read(self):
        with connect() as conn:
            ch1_rows = report.load_canonical_rows(conn, "CH-000001")
        unavailable = [r for r in ch1_rows if r["video_id"] == "VID-000148"][0]
        self.assertEqual(unavailable["availability_status"], "UNAVAILABLE")
        self.assertFalse(unavailable["canonical_reference"])


if __name__ == "__main__":
    unittest.main()
