import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import report_editing_visual_intelligence as report  # noqa: E402


class EditingVisualIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.topic = json.loads((
            ROOT / "data/intelligence/channels/CH-000004/topic-opportunity-intelligence-2026-09-09.json"
        ).read_text(encoding="utf-8"))
        cls.packaging = json.loads((
            ROOT / "data/intelligence/channels/CH-000004/packaging-intelligence-2026-09-09-v2.json"
        ).read_text(encoding="utf-8"))
        cls.hook_script = json.loads((
            ROOT / "data/intelligence/channels/CH-000004/hook-script-intelligence-pilot-2026-09-10.json"
        ).read_text(encoding="utf-8"))
        with report.connect() as conn:
            cls.payload = report.build_report(
                conn, "CH-000004", cls.topic, cls.packaging, cls.hook_script,
                generated_on="2026-09-11", repo_root=ROOT,
            )

    def test_discovers_registered_forensic_evidence_and_resolves_duplicate_video(self):
        rows = self.payload["evidence_matrix"]
        self.assertEqual({row["dataset_id"] for row in rows}, {
            "DS-000012", "DS-000013", "DS-000014", "DS-000015",
        })
        self.assertEqual(len({row["video_id"] for row in rows}), 3)
        sunset = [row for row in rows if row["youtube_video_id"] == "rGZ6TsXvi8E"]
        self.assertEqual(len(sunset), 2)
        self.assertEqual(sum(row["canonical_measurement_source"] for row in sunset), 1)
        self.assertEqual(
            {row["dataset_relationship_type"] for row in sunset},
            {"SAME_SOURCE_INDEPENDENT_ANALYSIS"},
        )

    def test_measured_feature_extraction_uses_timestamped_visual_states(self):
        features = self.payload["measured_features"]
        self.assertEqual(len(features), 3)
        self.assertTrue(all(row["evidence_state"] == "DERIVED_METRIC" for row in features))
        self.assertTrue(all(row["visual_state_count"] > 0 for row in features))
        self.assertTrue(all(row["visual_changes_per_minute"] > 0 for row in features))
        self.assertTrue(all(row["longest_static_hold_seconds"] > 0 for row in features))
        self.assertTrue(all(row["format"] == "SHORT_FORM" for row in features))

    def test_visual_timing_math_is_deterministic(self):
        first = report.derive_timing_features(65.0, [0.0, 10.0, 25.0, 40.0, 65.0], 2, 3)
        second = report.derive_timing_features(65.0, [0.0, 10.0, 25.0, 40.0, 65.0], 2, 3)
        self.assertEqual(first, second)
        self.assertEqual(first["visual_change_count"], 4)
        self.assertEqual(first["early_30s_visual_change_rate"], 4.0)
        self.assertEqual(first["early_60s_visual_change_rate"], 3.0)
        self.assertEqual(first["longest_static_hold_seconds"], 25.0)

    def test_no_thumbnail_or_transcript_fallback(self):
        with report.connect() as conn:
            for channel_id in ("CH-000001", "CH-000002", "CH-000003", "CH-000005"):
                availability = report.channel_availability(conn, channel_id, ROOT)
                self.assertEqual(availability["editing_intelligence_status"], "NOT_AVAILABLE")
                self.assertEqual(availability["reason"], "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE")
                self.assertEqual(availability["forensic_video_count"], 0)
        self.assertFalse(self.payload["guardrails"]["thumbnail_as_editing_evidence"])
        self.assertFalse(self.payload["guardrails"]["transcript_as_editing_evidence"])

    def test_interpretations_and_alignment_are_traceable(self):
        self.assertTrue(self.payload["visual_features"])
        self.assertTrue(all(
            row["evidence_state"] == "AI_INTERPRETATION"
            for row in self.payload["visual_features"]
        ))
        for row in self.payload["script_visual_alignment"]:
            self.assertEqual(row["evidence_state"], "AI_INTERPRETATION")
            self.assertTrue(row["video_id"])
            self.assertTrue(row["script_segment"])
            self.assertTrue(row["visual_evidence"])
            self.assertIsNotNone(row["timestamp_seconds"])
            self.assertTrue(row["frame_locator"])

    def test_exactly_two_coherent_full_content_blueprints(self):
        self.assertEqual(len(self.payload["editing_blueprints"]), 2)
        self.assertEqual(len(self.payload["full_content_blueprints"]), 2)
        for row in self.payload["full_content_blueprints"]:
            self.assertEqual(row["evidence_state"], "EVIDENCE_BACKED_HYPOTHESIS")
            self.assertEqual(row["cross_layer_coherence"]["overall"], "COHERENT")
            self.assertEqual(set(row["unavailable_metrics"]), report.UNAVAILABLE_METRICS)

    def test_guardrails_and_human_report_contract(self):
        self.assertFalse(self.payload["guardrails"]["retention_data_available"])
        self.assertEqual(self.payload["guardrails"]["causal_editing_claims"], 0)
        self.assertTrue(all(not row["causal_driver"] for row in self.payload["performance_associations"]))
        markdown = report.render_markdown(self.payload)
        for heading in (
            "# Scope", "# Evidence Availability", "# Measured Editing Features",
            "# Visual Patterns", "# Visual Archetypes", "# Editing Sequences",
            "# Script → Visual Alignment", "# Performance Associations",
            "# Counter-Evidence", "# Editing Blueprints", "# Full Content Blueprints",
            "# Evidence Gaps", "# Pilot Verdict",
        ):
            self.assertIn(heading, markdown)

    def test_output_and_all_channel_availability_are_deterministic(self):
        rendered = report.render_json(self.payload)
        self.assertEqual(rendered, report.render_json(self.payload))
        self.assertEqual(self.payload["pilot_verdict"], "PASS")
        self.assertEqual(self.payload["editing_intelligence_status"], "WORKING_WITH_FORENSIC_EVIDENCE")
        self.assertEqual(self.payload["channel_wide_editing_style"], "NOT_SUPPORTED")
        with report.connect() as conn:
            matrix = report.build_availability_matrix(conn, ROOT, "2026-09-11")
        self.assertEqual(len(matrix["channels"]), 5)
        self.assertEqual(
            next(row for row in matrix["channels"] if row["channel_id"] == "CH-000004")["editing_intelligence_status"],
            "WORKING_WITH_FORENSIC_EVIDENCE",
        )
        self.assertEqual(
            rendered,
            (ROOT / "data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json").read_text(encoding="utf-8"),
        )
        self.assertEqual(
            report.render_json(matrix),
            (ROOT / "data/intelligence/cross-channel/editing-intelligence-availability-2026-09-11.json").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
