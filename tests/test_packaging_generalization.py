import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackagingGeneralizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.channels = {
            channel_id: json.loads((
                ROOT / f"data/intelligence/channels/{channel_id}/packaging-intelligence-2026-09-10.json"
            ).read_text(encoding="utf-8"))
            for channel_id in ("CH-000001", "CH-000002", "CH-000003")
        }
        cls.comparison = json.loads((
            ROOT / "data/intelligence/cross-channel/packaging-comparison-2026-09-10.json"
        ).read_text(encoding="utf-8"))

    def test_all_canonical_titles_are_accounted_for(self):
        expected = {"CH-000001": 94, "CH-000002": 65, "CH-000003": 32}
        for channel_id, item_count in expected.items():
            snapshot = self.channels[channel_id]["evidence_snapshot"]
            self.assertEqual(snapshot["canonical_item_count"], item_count)
            self.assertEqual(snapshot["titles_accounted_for"], item_count)

    def test_thumbnail_gaps_and_current_snapshots_are_distinguished(self):
        for channel_id in ("CH-000001", "CH-000002"):
            payload = self.channels[channel_id]
            self.assertEqual(payload["archetype_scope"], "TITLE_ONLY_ARCHETYPE")
            self.assertEqual(payload["evidence_snapshot"]["thumbnail_evidence_state"], "THUMBNAIL_REFERENCE_GAP")
            self.assertEqual(payload["visual_features"], [])
        health = self.channels["CH-000003"]
        self.assertEqual(health["evidence_snapshot"]["acquired_thumbnails"], 32)
        self.assertEqual(len(health["visual_features"]), 32)
        self.assertTrue(all(row["interpretation_state"] == "AI_INTERPRETATION" for row in health["visual_features"]))

    def test_six_packages_per_channel_are_traceable_and_long_form_ab_eligible(self):
        for payload in self.channels.values():
            canonical_ids = {row["video_id"] for row in payload["title_features"]}
            packages = [
                package
                for opportunity in payload["opportunity_packages"]
                for package in opportunity["recommended_test_set"]
            ]
            self.assertEqual(len(packages), 6)
            self.assertTrue(all(package["evidence_state"] == "HYPOTHESIS_FOR_TESTING" for package in packages))
            self.assertTrue(all(package["native_ab_eligible"] == "YES" for package in packages))
            self.assertTrue(all(set(package["historical_support"]["video_ids"]) <= canonical_ids for package in packages))

    def test_comparison_preserves_temporal_and_causal_guardrails(self):
        self.assertEqual(self.comparison["generalization_verdict"], "PASS")
        self.assertEqual(self.comparison["temporal_guardrail"]["verified_historical_pairs"], 0)
        self.assertEqual(self.comparison["temporal_guardrail"]["current_snapshot_pairs"], 32)
        self.assertEqual(self.comparison["guardrails"]["causal_claims_created"], 0)
        self.assertEqual(
            self.comparison["temporal_guardrail"]["historical_causal_package_analysis"],
            "NOT_SUPPORTED",
        )


if __name__ == "__main__":
    unittest.main()
