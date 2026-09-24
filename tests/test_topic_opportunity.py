import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import report_topic_opportunity as report  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REQUIRES_HISTORICAL = unittest.skipUnless(
    (ROOT / "data/raw/competitors/DS-000001").exists(),
    "requires ignored historical catalog evidence",
)


def family_item(video_id, title, velocity, transcript=""):
    return {
        "video_id": video_id,
        "canonical_topic": "TEST_TOPIC",
        "format": "LONG_FORM",
        "title": title,
        "published_at": "2026-08-01T00:00:00Z",
        "views_per_day": velocity,
        "transcript_text": transcript,
    }


class TopicOpportunityTests(unittest.TestCase):
    def test_normalization_uses_observation_date_and_handles_optional_metrics(self):
        item = {
            "video_id": "VID-1",
            "published_at": "2026-08-01T00:00:00Z",
            "views": 1_000,
            "likes": None,
            "comments": None,
        }

        first = report.normalize_item(item, "2026-08-11T00:00:00Z")

        self.assertEqual(first, report.normalize_item(item, "2026-08-11T00:00:00Z"))
        self.assertEqual(first["age_days"], 10.0)
        self.assertEqual(first["views_per_day"], 100.0)
        self.assertIsNone(first["like_rate"])
        self.assertIsNone(first["comment_rate"])

    def test_invalid_publish_date_does_not_use_today(self):
        item = {"video_id": "VID-1", "published_at": "(dateTonly)Z", "views": 10}

        normalized = report.normalize_item(item, "2026-08-11T00:00:00Z")

        self.assertIsNone(normalized["age_days"])
        self.assertIsNone(normalized["views_per_day"])
        self.assertEqual(normalized["normalization_status"], "INVALID_PUBLISHED_AT")

    def test_outlier_logic_and_small_sample_fallback_are_deterministic(self):
        values = [10, 11, 12, 13, 14, 15, 1000]

        self.assertEqual(
            report.robust_outlier_flags(values),
            ["NORMAL_RANGE"] * 6 + ["POSITIVE_OUTLIER"],
        )
        self.assertEqual(
            report.robust_outlier_flags([1, 2, 3]),
            ["INSUFFICIENT_SAMPLE"] * 3,
        )

    def test_topic_family_aggregation_accounts_for_every_item(self):
        items = [
            family_item("VID-1", "Moon power test", 100.0),
            family_item("VID-2", "Moon laser test", 20.0),
            family_item("VID-3", "Ocean pressure test", 10.0),
        ]

        report.assign_topic_families(items)
        families = report.aggregate_topic_families(items, 20.0)

        self.assertEqual(sum(row["item_count"] for row in families), 3)
        self.assertEqual(
            {video_id for row in families for video_id in row["video_ids"]},
            {"VID-1", "VID-2", "VID-3"},
        )

    def test_one_huge_item_with_weak_peers_is_not_repeatable_winner(self):
        members = [
            {"views_per_day": 1_000.0},
            {"views_per_day": 1.0},
            {"views_per_day": 1.0},
            {"views_per_day": 1.0},
        ]

        self.assertEqual(report.repeatability(members, 10.0), "WEAK_FAMILY")

    def test_missing_transcript_is_safe(self):
        items = [family_item("VID-1", "Moon power test", 10.0, transcript=None)]

        report.assign_topic_families(items)
        patterns = report.transcript_topic_patterns(items)

        self.assertEqual(patterns["available_items"], 0)
        self.assertEqual(patterns["recurring_terms"], [])

    @REQUIRES_HISTORICAL
    def test_live_arbitrary_channel_is_complete_and_read_only(self):
        with report.connect() as conn:
            before = conn.execute("SELECT COUNT(*) FROM content_classifications").fetchone()[0]
            payload = report.build_report(conn, "CH-000002")
            after = conn.execute("SELECT COUNT(*) FROM content_classifications").fetchone()[0]

        self.assertEqual(payload["channel"]["channel_id"], "CH-000002")
        self.assertEqual(payload["evidence_snapshot"]["canonical_item_count"], 65)
        self.assertEqual(len(payload["items"]), 65)
        self.assertEqual(before, after)

    @REQUIRES_HISTORICAL
    def test_candidate_evidence_is_traceable(self):
        with report.connect() as conn:
            payload = report.build_report(conn, "CH-000004")

        item_ids = {item["canonical_fact"]["video_id"] for item in payload["items"]}
        family_names = {family["topic_family"] for family in payload["topic_families"]}
        self.assertTrue(payload["internal_candidates"])
        for candidate in payload["internal_candidates"]:
            self.assertEqual(candidate["channel_id"], "CH-000004")
            self.assertTrue(set(candidate["supporting_video_ids"]) <= item_ids)
            self.assertIn(candidate["topic_family"], family_names)

    def test_json_output_is_stable(self):
        payload = {"z": 1, "a": [2, 1]}

        rendered = report.render_json(payload)

        self.assertEqual(rendered, report.render_json(payload))
        self.assertEqual(list(json.loads(rendered)), ["a", "z"])

    @REQUIRES_HISTORICAL
    def test_committed_channel_json_matches_live_generation(self):
        root = Path(__file__).resolve().parents[1]
        with report.connect() as conn:
            for channel_id in ("CH-000001", "CH-000002", "CH-000004"):
                expected = report.render_json(report.build_report(conn, channel_id, "2026-09-09"))
                artifact = root / "data" / "intelligence" / "channels" / channel_id / "topic-opportunity-intelligence-2026-09-09.json"
                actual = artifact.read_text(encoding="utf-8")
                self.assertEqual(actual, expected)
                for item in json.loads(actual)["items"]:
                    self.assertTrue(set(item["canonical_fact"]).isdisjoint(report.UNAVAILABLE_METRICS))
                    self.assertTrue(set(item["derived_metric"]).isdisjoint(report.UNAVAILABLE_METRICS))


if __name__ == "__main__":
    unittest.main()
