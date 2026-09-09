import json
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import report_packaging_intelligence as report  # noqa: E402


class PackagingIntelligenceTests(unittest.TestCase):
    def test_title_features_detect_question_numeric_and_extreme_framing(self):
        features = report.extract_title_features(
            "What if ALL the Sun's power were focused at 90% strength?"
        )

        self.assertTrue(features["question_form"])
        self.assertTrue(features["what_if_construction"])
        self.assertTrue(features["has_number"])
        self.assertTrue(features["extreme_condition"])
        self.assertEqual(features["question_marks"], 1)

    def test_title_features_are_reproducible(self):
        title = "Could you survive a nanosecond on the Sun?"

        self.assertEqual(
            report.extract_title_features(title),
            report.extract_title_features(title),
        )

    def test_archetype_aggregation_is_deterministic_and_format_separated(self):
        items = [
            report.title_item("VID-1", "What if Earth vanished?", "LONG_FORM", 2.0),
            report.title_item("VID-2", "What if Mars vanished?", "SHORT_FORM", 1.0),
            report.title_item("VID-3", "How high can waves go?", "SHORT_FORM", 3.0),
        ]

        first = report.aggregate_title_archetypes(items)

        self.assertEqual(first, report.aggregate_title_archetypes(items))
        what_if = next(row for row in first if row["archetype_id"] == "WHAT_IF_SCENARIO")
        self.assertEqual(what_if["format_mix"], {"LONG_FORM": 1, "SHORT_FORM": 1})
        self.assertEqual(
            set(what_if["performance_by_format"]), {"LONG_FORM", "SHORT_FORM"}
        )

    def test_package_evidence_rejects_unknown_video(self):
        package = {
            "package_id": "PKG-1",
            "historical_support": {
                "canonical_video_ids": ["VID-MISSING"],
                "title_archetype_ids": ["WHAT_IF_SCENARIO"],
            },
        }

        with self.assertRaisesRegex(ValueError, "unknown canonical video"):
            report.validate_package_evidence(
                [package], {"VID-1"}, {"WHAT_IF_SCENARIO"}
            )

    def test_missing_thumbnail_is_never_marked_inspectable(self):
        row = report.thumbnail_record("VID-1", None, None)

        self.assertFalse(row["inspectable"])
        self.assertEqual(row["visual_observation_status"], "NOT_AVAILABLE")
        self.assertNotIn("text_present", row)

    def test_registered_url_without_local_file_is_not_inspectable(self):
        row = report.thumbnail_record(
            "VID-1", "https://i.ytimg.com/vi/example/maxresdefault.jpg", None
        )

        self.assertFalse(row["inspectable"])
        self.assertEqual(row["visual_observation_status"], "REMOTE_REFERENCE_ONLY")

    def test_private_metrics_and_prohibited_scores_are_absent(self):
        forbidden = {
            "algorithm_package_score",
            "ctr",
            "ctr_score",
            "guaranteed_winner",
            "predicted_ctr",
            "watch_time",
        }
        payload = {
            "title_features": report.extract_title_features("What if Earth vanished?"),
            "limitations": report.LIMITATIONS,
        }

        keys = report.recursive_keys(payload)
        self.assertTrue(forbidden.isdisjoint(keys))

    def test_json_output_is_deterministic(self):
        payload = {"z": 1, "a": [2, 1]}

        self.assertEqual(report.render_json(payload), report.render_json(payload))
        self.assertEqual(list(json.loads(report.render_json(payload))), ["a", "z"])

    def test_live_pilot_accounts_for_all_titles_without_mutation(self):
        root = Path(__file__).resolve().parents[1]
        topic_path = root / "data/intelligence/channels/CH-000004/topic-opportunity-intelligence-2026-09-09.json"
        with report.connect() as conn:
            before = conn.execute("SELECT COUNT(*) FROM content_classifications").fetchone()[0]
            payload = report.build_historical_report(conn, topic_path)
            after = conn.execute("SELECT COUNT(*) FROM content_classifications").fetchone()[0]

        self.assertEqual(payload["evidence_snapshot"]["canonical_item_count"], 83)
        self.assertEqual(payload["evidence_snapshot"]["titles_accounted_for"], 83)
        self.assertEqual(len(payload["title_features"]), 83)
        self.assertEqual(payload["evidence_snapshot"]["thumbnail_urls_registered"], 83)
        self.assertEqual(payload["evidence_snapshot"]["inspectable_thumbnails"], 0)
        self.assertTrue({
            "published_at", "age_days", "transcript_status", "thumbnail_url",
            "thumbnail_inspectable", "packaging_screenshot_evidence",
        } <= set(payload["title_features"][0]))
        self.assertEqual(before, after, 546)

    def test_committed_pilot_packages_are_complete_and_traceable(self):
        root = Path(__file__).resolve().parents[1]
        artifact = root / "data/intelligence/channels/CH-000004/packaging-intelligence-pilot-2026-09-09.json"
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        canonical_ids = {row["video_id"] for row in payload["title_features"]}
        archetype_ids = {row["archetype_id"] for row in payload["title_archetypes"]}
        packages = [
            package
            for opportunity in payload["opportunity_packages"]
            for package in opportunity["recommended_test_set"]
        ]

        self.assertEqual(len(payload["opportunity_packages"]), 5)
        self.assertEqual(len(packages), 15)
        self.assertTrue(all(len(row["recommended_test_set"]) == 3 for row in payload["opportunity_packages"]))
        self.assertEqual(len({row["package_id"] for row in packages}), 15)
        report.validate_package_evidence(packages, canonical_ids, archetype_ids)
        self.assertEqual(payload["evidence_snapshot"]["titles_accounted_for"], 83)
        self.assertEqual(payload["evidence_snapshot"]["inspectable_thumbnails"], 0)
        topic = root / "data/intelligence/channels/CH-000004/topic-opportunity-intelligence-2026-09-09.json"
        with report.connect() as conn:
            live = report.build_historical_report(conn, topic)
        for key in (
            "title_feature_summary", "title_features", "title_archetypes",
            "thumbnail_features", "thumbnail_archetypes", "pair_patterns",
        ):
            self.assertEqual(payload[key], live[key])


if __name__ == "__main__":
    unittest.main()
