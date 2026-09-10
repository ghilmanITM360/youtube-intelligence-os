import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import report_hook_script_intelligence as report  # noqa: E402


class HookScriptUnitTests(unittest.TestCase):
    def test_timing_quality_distinguishes_exact_segment_and_position_only(self):
        exact = {"text": "One two", "segments": [{"start": 0, "end": 1, "words": [
            {"word": "One", "start": 0, "end": .4},
            {"word": "two", "start": .5, "end": .9},
        ]}]}
        partial = {"text": "One two", "segments": [{"start": 0, "end": 1, "words": [
            {"word": "One", "start": 0, "end": .4}, {"word": "two"},
        ]}]}
        segment = {"text": "One two", "segments": [{"start": 0, "end": 1, "text": "One two"}]}

        self.assertEqual(report.timing_quality(exact), "EXACT_TIMESTAMPED")
        self.assertEqual(report.timing_quality(partial), "SEGMENT_TIMESTAMPED")
        self.assertEqual(report.timing_quality(segment), "SEGMENT_TIMESTAMPED")
        self.assertEqual(report.timing_quality({"text": "One two"}), "POSITIONAL_ONLY")
        self.assertEqual(report.timing_quality({}), "INSUFFICIENT_TIMING")

    def test_mixed_timed_and_text_segments_fall_back_without_dropping_text(self):
        transcript = {"segments": [
            {"start": 0, "end": 10, "words": [{"word": "timed", "start": 1, "end": 2}]},
            {"start": 10, "end": 20, "text": "text only"},
        ]}

        self.assertEqual(report.timing_quality(transcript), "SEGMENT_TIMESTAMPED")
        self.assertEqual(report.extract_window(transcript, 0, 30, 60)["text"], "timed text only")

    def test_exact_first_30_second_window_uses_timestamps(self):
        transcript = {"segments": [{"start": 0, "end": 35, "words": [
            {"word": "early", "start": 5, "end": 6},
            {"word": "late", "start": 31, "end": 32},
        ]}]}
        window = report.extract_window(transcript, 0, 30, 60)

        self.assertEqual(window["timing_state"], "EXACT_TIMESTAMPED")
        self.assertEqual(window["text"], "early")

    def test_position_only_window_is_explicit_approximation(self):
        transcript = {"text": "one two three four five six"}
        window = report.extract_window(transcript, 0, 30, 60)

        self.assertEqual(window["timing_state"], "POSITIONAL_APPROXIMATION")
        self.assertEqual(window["text"], "one two three")

    def test_missing_timestamps_never_gain_exact_seconds(self):
        features = report.measured_hook_features(
            {"text": "Why now? Because constraints matter."}, "Why Constraints Matter", 60
        )

        self.assertEqual(features["evidence_state"], "DERIVED_METRIC")
        self.assertEqual(features["first_question"]["timing_state"], "POSITIONAL_APPROXIMATION")
        self.assertNotIn("exact_seconds", features["first_question"])

    def test_question_and_premise_detection_are_deterministic(self):
        transcript = {"text": "First context. Why does the Moon move? The Moon moves because gravity acts."}
        first = report.measured_hook_features(transcript, "Why Does the Moon Move?", 90)

        self.assertEqual(first, report.measured_hook_features(transcript, "Why Does the Moon Move?", 90))
        self.assertEqual(first["question_count"], 1)
        self.assertIsNotNone(first["central_premise_position"])

    def test_script_structure_has_source_traceability(self):
        structure = report.derive_script_structure(
            "What if gravity stopped? First define gravity. Suppose Earth stays intact. "
            "The force becomes zero. Therefore the atmosphere escapes. That is the answer."
        )

        self.assertGreaterEqual(len(structure["sequence"]), 4)
        self.assertTrue(all(segment["evidence"]["excerpt"] for segment in structure["segments"]))
        self.assertTrue(all(segment["evidence_state"] == "AI_INTERPRETATION" for segment in structure["segments"]))

    def test_curiosity_payoff_map_uses_traceable_sentences(self):
        result = report.curiosity_payoff_map(
            "Could gravity stop? First define the force. Therefore the atmosphere escapes."
        )

        self.assertEqual(result["initial_open_question"], "Could gravity stop?")
        self.assertEqual(result["intermediate_payoffs"], ["Therefore the atmosphere escapes."])
        self.assertEqual(result["evidence"]["initial_open_question"]["sentence_index"], 0)
        self.assertEqual(result["evidence"]["intermediate_payoffs"][0]["sentence_index"], 2)

    def test_format_aggregation_stays_separate(self):
        rows = [
            {"format": "LONG_FORM", "hook_archetype": "DIRECT_QUESTION", "channel_median_ratio": 2},
            {"format": "SHORT_FORM", "hook_archetype": "DIRECT_QUESTION", "channel_median_ratio": .5},
        ]
        result = report.aggregate_hook_archetypes(rows)

        self.assertEqual({row["format_context"] for row in result}, {"LONG_FORM", "SHORT_FORM"})
        self.assertTrue(all(row["interpretation_state"] == "AI_INTERPRETATION" for row in result))

    def test_counter_examples_require_contradictory_performance(self):
        rows = [
            {"format": "LONG_FORM", "hook_archetype": "DIRECT_QUESTION", "channel_median_ratio": 2, "video_id": "A"},
            {"format": "LONG_FORM", "hook_archetype": "DIRECT_QUESTION", "channel_median_ratio": 1.8, "video_id": "B"},
        ]
        result = report.aggregate_hook_archetypes(rows)[0]

        self.assertEqual(result["counter_examples"], [])

    def test_continuity_checks_are_distinct_and_labeled(self):
        checks = report.continuity_checks(
            "moon gravity", "Moon gravity explained", "Why does gravity shape the Moon?",
            "Gravity shapes the Moon", "gravity moon",
        )

        self.assertEqual(checks["evidence_state"], "DERIVED_LEXICAL_CHECK")
        self.assertEqual(checks["continuity"], "COHERENT")
        self.assertEqual(
            set(checks) - {"evidence_state", "continuity"},
            {"topic_match", "semantic_match", "promise_match", "stakes_alignment", "payoff_alignment"},
        )

    def test_report_prohibits_private_retention_metrics(self):
        self.assertFalse(report.PRIVATE_METRICS & report.ALLOWED_OUTPUT_KEYS)
        forbidden = {"retention", "ctr", "impressions", "watch_time", "average_view_duration"}
        self.assertFalse(forbidden & report.recursive_keys({"safe": {"views": 1}}))

    def test_continuity_detects_match_and_mismatch(self):
        self.assertEqual(report.continuity_state("moon gravity", "Moon?", "gravity on moon", "moon gravity payoff"), "COHERENT")
        self.assertEqual(report.continuity_state("moon gravity", "Retirement", "taxes", "pensions"), "MISMATCH")

    def test_json_is_deterministic(self):
        value = {"z": 1, "a": [2, 1]}
        self.assertEqual(report.render_json(value), report.render_json(value))
        self.assertEqual(list(json.loads(report.render_json(value))), ["a", "z"])

    def test_core_has_no_channel_or_niche_specific_branch(self):
        source = (ROOT / "scripts/report_hook_script_intelligence.py").read_text(encoding="utf-8").lower()
        for forbidden in ("ch-000004", "xkcd", "solar", "earthquake"):
            self.assertNotIn(forbidden, source)


class HookScriptArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = ROOT / "data/intelligence/channels/CH-000004/hook-script-intelligence-pilot-2026-09-10.json"

    def test_pilot_accounts_for_all_transcripts_and_formats(self):
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        snapshot = payload["evidence_snapshot"]
        self.assertEqual(snapshot["canonical_item_count"], 83)
        self.assertEqual(snapshot["transcripts_accounted_for"], 83)
        self.assertEqual(snapshot["formats"], {"LONG_FORM": 27, "SHORT_FORM": 56})
        self.assertEqual(sum(payload["timing_quality"]["counts"].values()), 83)

    def test_generated_objects_are_exact_and_traceable(self):
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        canonical_ids = {row["video_id"] for row in payload["hook_features"]}
        self.assertEqual(len(payload["selected_opportunities"]), 2)
        self.assertEqual(len(payload["hook_hypotheses"]), 6)
        self.assertEqual(len(payload["script_blueprints"]), 2)
        self.assertEqual(len(payload["content_blueprints"]), 2)
        selected_ids = {row["opportunity_id"] for row in payload["selected_opportunities"]}
        self.assertEqual(
            {opportunity_id: sum(row["opportunity_id"] == opportunity_id for row in payload["hook_hypotheses"])
             for opportunity_id in selected_ids},
            {opportunity_id: 3 for opportunity_id in selected_ids},
        )
        self.assertEqual(
            {opportunity_id: sum(row["opportunity_id"] == opportunity_id for row in payload["script_blueprints"])
             for opportunity_id in selected_ids},
            {opportunity_id: 1 for opportunity_id in selected_ids},
        )
        self.assertEqual(len(payload["package_hook_script_links"]), 6)
        self.assertTrue(all(row["evidence_state"] == "HYPOTHESIS_FOR_TESTING" for row in payload["hook_hypotheses"]))
        self.assertTrue(all(set(row["supporting_video_ids"]) <= canonical_ids for row in payload["hook_hypotheses"]))
        self.assertTrue(all(row["continuity"] == "COHERENT" for row in payload["package_hook_script_links"]))
        self.assertTrue(all(
            "visual_revalidation" in package
            for opportunity in payload["selected_opportunities"]
            for package in opportunity["recommended_test_set"]
        ))

    def test_no_fabricated_retention_or_unlabeled_interpretation(self):
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(payload["guardrails"]["retention_claims_created"], 0)
        self.assertEqual(payload["guardrails"]["private_retention_available"], False)
        self.assertTrue(all(row["interpretation_state"] == "AI_INTERPRETATION" for row in payload["hook_features"]))
        self.assertTrue(all(row["structure"]["interpretation_state"] == "AI_INTERPRETATION" for row in payload["script_features"]))
        self.assertTrue(all(row["interpretation_state"] == "AI_INTERPRETATION" for row in payload["script_features"]))
        self.assertTrue(all(not report.PRIVATE_METRICS & set(row) for row in payload["hook_features"]))
        self.assertTrue(all(
            row["interpretation_state"] == "AI_INTERPRETATION"
            for row in payload["hook_archetypes"] + payload["script_archetypes"]
        ))
        self.assertTrue(all(
            row["evidence_state"] == "DERIVED_LEXICAL_CHECK"
            for row in payload["package_hook_script_links"]
        ))

    def test_public_performance_and_payoff_evidence_are_traceable(self):
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertTrue(all({
            "views", "views_per_day", "channel_relative_performance",
            "format_relative_performance", "family_relative_performance",
            "likes_per_view", "comments_per_view",
        } <= set(row["public_performance"]) for row in payload["hook_features"]))
        self.assertTrue(all(
            row["curiosity_payoff_map"]["interpretation_state"] == "AI_INTERPRETATION"
            and row["curiosity_payoff_map"]["evidence"]["initial_open_question"]
            and row["curiosity_payoff_map"]["evidence"]["main_payoff"]
            for row in payload["script_features"]
        ))
        self.assertEqual(
            sum(row["item_count"] for row in payload["performance_associations"]["by_performance_band"]),
            83,
        )


if __name__ == "__main__":
    unittest.main()
