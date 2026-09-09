import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import report_topic_opportunity_pilot as pilot  # noqa: E402


class TopicOpportunityPilotTests(unittest.TestCase):
    def test_normalization_is_deterministic_and_public_only(self):
        item = {
            "video_id": "VID-1",
            "published_at": "2026-08-01T00:00:00Z",
            "views": 1_000,
            "likes": 50,
            "comments": 10,
            "duration_seconds": 600,
        }
        first = pilot.normalize_item(item, "2026-08-11T00:00:00Z")
        second = pilot.normalize_item(item, "2026-08-11T00:00:00Z")

        self.assertEqual(first, second)
        self.assertEqual(first["age_days"], 10.0)
        self.assertEqual(first["views_per_day"], 100.0)
        self.assertEqual(first["like_rate"], 0.05)
        self.assertEqual(first["comment_rate"], 0.01)
        self.assertTrue(set(first).isdisjoint(pilot.UNAVAILABLE_METRICS))

    def test_tukey_outliers_use_log_velocity(self):
        values = [10, 11, 12, 13, 14, 15, 1000]
        flags = pilot.robust_outlier_flags(values)

        self.assertEqual(flags, ["TYPICAL"] * 6 + ["POSITIVE"])
        self.assertEqual(pilot.robust_outlier_flags([1, 2, 3]), ["INSUFFICIENT_SAMPLE"] * 3)

    def test_topic_family_aggregation_accounts_for_every_item(self):
        items = [
            {"video_id": "VID-1", "family": "MOBILITY", "views_per_day": 100.0, "title": "Safe walking after 70"},
            {"video_id": "VID-2", "family": "MOBILITY", "views_per_day": 20.0, "title": "Walking balance after 70"},
            {"video_id": "VID-3", "family": "MEDICATION", "views_per_day": 10.0, "title": "Medication safety"},
        ]
        families = pilot.aggregate_topic_families(items)

        self.assertEqual(sum(row["item_count"] for row in families), 3)
        self.assertEqual(families[0]["family"], "MOBILITY")
        self.assertEqual(families[0]["median_views_per_day"], 60.0)
        self.assertEqual(families[0]["video_ids"], ["VID-1", "VID-2"])
        self.assertEqual(families[0]["mean_title_token_jaccard"], 0.5)
        self.assertIsNone(families[1]["mean_title_token_jaccard"])

    def test_item_accounting_rejects_missing_or_duplicate_items(self):
        pilot.require_exact_item_set([{"video_id": "VID-1"}, {"video_id": "VID-2"}], 2)
        with self.assertRaisesRegex(ValueError, "expected 2 unique items"):
            pilot.require_exact_item_set([{"video_id": "VID-1"}], 2)
        with self.assertRaisesRegex(ValueError, "expected 2 unique items"):
            pilot.require_exact_item_set([{"video_id": "VID-1"}, {"video_id": "VID-1"}], 2)

    def test_json_output_is_stable(self):
        payload = {"z": 1, "a": [2, 1]}

        rendered = pilot.render_json(payload)

        self.assertEqual(rendered, pilot.render_json(payload))
        self.assertEqual(list(json.loads(rendered)), ["a", "z"])

    def test_live_channel_snapshot_accounts_for_every_item_without_private_metrics(self):
        with pilot.connect() as conn:
            report = pilot.build_report(conn)

        self.assertEqual(report["item_count"], 32)
        self.assertEqual(report["transcript_coverage"], 32)
        self.assertEqual(len(report["items"]), 32)
        self.assertEqual(sum(row["item_count"] for row in report["topic_families"]), 32)
        for item in report["items"]:
            self.assertTrue(set(item).isdisjoint(pilot.UNAVAILABLE_METRICS))


if __name__ == "__main__":
    unittest.main()
