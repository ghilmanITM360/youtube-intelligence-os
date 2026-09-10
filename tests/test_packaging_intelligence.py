import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import report_packaging_intelligence as report  # noqa: E402


def item(video_id, title, ratio=1.0, format_name="LONG_FORM"):
    return {
        "canonical_fact": {
            "video_id": video_id, "title": title, "format": format_name,
            "views": 100, "published_at": "2026-01-01", "transcript_status": "AVAILABLE",
        },
        "derived_metric": {
            "views_per_day": 10, "channel_median_ratio": ratio,
            "family_median_ratio": ratio, "like_rate": None,
            "comment_rate": None, "age_days": 10,
        },
        "observation": {"performance_band": "NORMAL_RANGE", "topic_family": "FAMILY"},
    }


class PackagingIntelligenceTests(unittest.TestCase):
    def test_title_features_work_across_domains(self):
        finance = report.extract_title_features("7 Retirement Risks Nobody Talks About")
        health = report.extract_title_features("Over 60? Warning Signs You Should Never Ignore")

        self.assertTrue(finance["has_number"])
        self.assertTrue(finance["warning_or_risk"])
        self.assertTrue(health["question_form"])
        self.assertTrue(health["audience_or_life_stage"])
        self.assertTrue(health["warning_or_risk"])

    def test_archetype_aggregation_is_deterministic_and_format_separated(self):
        items = [
            report.title_item("VID-1", "Why Costs Rise", "LONG_FORM", 2.0),
            report.title_item("VID-2", "Why Risks Rise", "SHORTS", 1.0),
            report.title_item("VID-3", "7 Risks to Know", "SHORTS", 3.0),
        ]
        first = report.aggregate_title_archetypes(items)

        self.assertEqual(first, report.aggregate_title_archetypes(items))
        explanatory = next(row for row in first if row["archetype_id"] == "EXPLANATORY")
        warning = next(row for row in first if row["archetype_id"] == "WARNING_OR_RISK")
        self.assertEqual(explanatory["format_mix"], {"LONG_FORM": 1})
        self.assertEqual(warning["format_mix"], {"SHORTS": 2})

    def test_arbitrary_channel_and_missing_thumbnails_are_safe(self):
        topic = {
            "channel": {"channel_id": "CH-X", "dataset_id": "DS-X", "display_name": "Any Channel"},
            "evidence_snapshot": {
                "metric_cutoff": "2026-01-10", "transcripts_available": 2,
                "formats": {"LONG_FORM": 2},
            },
            "items": [item("VID-1", "Why Costs Rise", 2), item("VID-2", "3 Costs to Watch", 1)],
            "internal_candidates": [{
                "candidate_id": "CAND-1", "topic": "Costs", "specific_angle": "Why operating costs rise",
                "supporting_video_ids": ["VID-1"], "performance_signal": "2x channel median",
                "counter_evidence": "Observational only", "initial_confidence": "MEDIUM",
            }],
        }
        payload = report.build_report(topic)

        self.assertEqual(payload["channel"]["channel_id"], "CH-X")
        self.assertEqual(payload["evidence_snapshot"]["titles_accounted_for"], 2)
        self.assertEqual(payload["evidence_snapshot"]["thumbnail_evidence_state"], "THUMBNAIL_REFERENCE_GAP")
        self.assertEqual(payload["thumbnail_archetypes"], [])
        self.assertEqual(payload["package_archetypes"], [])

    def test_visual_schema_requires_ai_label_and_temporal_uncertainty(self):
        row = {
            "video_id": "VID-1", "interpretation_state": "AI_INTERPRETATION",
            "temporal_alignment_state": "TEMPORAL_ALIGNMENT_UNKNOWN", "format": "LONG_FORM",
        }
        self.assertEqual(report.validate_visual_annotations([row], {"VID-1"}), [row])
        row["interpretation_state"] = "MEASURED"
        with self.assertRaisesRegex(ValueError, "AI_INTERPRETATION"):
            report.validate_visual_annotations([row], {"VID-1"})

    def test_package_evidence_is_traceable_and_never_predictive(self):
        candidate = {
            "candidate_id": "CAND-1", "topic": "Costs", "specific_angle": "Why costs rise",
            "supporting_video_ids": ["VID-1"], "performance_signal": "2x channel median",
            "counter_evidence": "One snapshot", "initial_confidence": "MEDIUM",
        }
        packages = report.generate_package_hypotheses(
            "CH-X", candidate, {"VID-1"}
        )

        self.assertEqual(len(packages), 3)
        self.assertTrue(all(row["evidence_state"] == "HYPOTHESIS_FOR_TESTING" for row in packages))
        self.assertTrue(all(row["native_ab_eligible"] == "YES" for row in packages))
        self.assertTrue(all(row["historical_support"]["video_ids"] == ["VID-1"] for row in packages))

    def test_acquisition_and_visual_support_stay_channel_and_item_scoped(self):
        topic = {
            "channel": {"channel_id": "CH-X", "dataset_id": "DS-X", "display_name": "Any Channel"},
            "evidence_snapshot": {"metric_cutoff": "2026-01-10", "transcripts_available": 1, "formats": {"LONG_FORM": 1}},
            "items": [item("VID-1", "Why Costs Rise", 2)],
            "internal_candidates": [{
                "candidate_id": "CAND-1", "topic": "Costs", "specific_angle": "Why costs rise",
                "supporting_video_ids": ["VID-1"], "performance_signal": "2x channel median",
                "counter_evidence": "Observational only", "initial_confidence": "MEDIUM",
            }],
        }
        with self.assertRaisesRegex(ValueError, "channel does not match"):
            report.build_report(topic, {"channel_id": "CH-Y", "snapshots": []})

        packages = report.generate_package_hypotheses(
            "CH-X", report.normalize_candidate(topic["internal_candidates"][0]), {"VID-1"}, {"VID-OTHER"}
        )
        self.assertTrue(all(package["visual_support"]["video_ids"] == [] for package in packages))

    def test_json_output_is_deterministic_and_core_has_no_niche_branches(self):
        payload = {"z": 1, "a": [2, 1]}
        source = (ROOT / "scripts/report_packaging_intelligence.py").read_text(encoding="utf-8").lower()

        self.assertEqual(report.render_json(payload), report.render_json(payload))
        self.assertEqual(list(json.loads(report.render_json(payload))), ["a", "z"])
        for forbidden in ("xkcd", "retirement_title", "health_warning_title", "finance_specific", "ch-000"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
