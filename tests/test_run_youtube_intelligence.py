import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_youtube_intelligence as orch  # noqa: E402


class CaseAFullEvidenceTests(unittest.TestCase):
    """CH-000004 / CH-000004-OP-001: full evidence chain, Editing available."""

    @classmethod
    def setUpClass(cls):
        cls.plan = orch.build_plan("CH-000004", "CH-000004-OP-001", generated_on="2026-09-11")

    def test_composes_from_existing_editing_blueprint_without_recreating_intelligence(self):
        self.assertEqual(self.plan["generation_state"], "COMPOSED_FROM_EXISTING_BLUEPRINT")

    def test_all_layers_present(self):
        self.assertTrue(self.plan["opportunity"]["topic"])
        self.assertTrue(self.plan["packaging"]["title_hypotheses"])
        self.assertTrue(self.plan["hook"]["hook_hypotheses"])
        self.assertTrue(self.plan["script"]["script_blueprint"])

    def test_editing_available_with_blueprint(self):
        self.assertEqual(self.plan["editing"]["status"], "AVAILABLE")
        self.assertIsNotNone(self.plan["editing"]["blueprint"])
        self.assertIsNone(self.plan["editing"]["reason"])

    def test_package_hook_script_linkage_matches_source_ids(self):
        hook = self.plan["hook"]["selected_hook"]
        script = self.plan["script"]["selected_script"]
        package = self.plan["packaging"]["selected_package"]
        self.assertEqual(hook["package_link"], package["package_id"])
        self.assertIn(hook["hook_id"], script["hook_links"])

    def test_coherence_is_fully_coherent(self):
        self.assertEqual(self.plan["coherence"]["overall"], "COHERENT")
        for dimension, verdict in self.plan["coherence"]["dimensions"].items():
            self.assertIn(verdict, ("PASS", "NOT_APPLICABLE"), dimension)

    def test_no_private_metrics_fabricated(self):
        for metric, value in self.plan["global"]["unavailable_metrics"].items():
            self.assertEqual(value, "NOT_AVAILABLE", metric)

    def test_deterministic_output(self):
        second = orch.build_plan("CH-000004", "CH-000004-OP-001", generated_on="2026-09-11")
        self.assertEqual(json.dumps(self.plan, sort_keys=True), json.dumps(second, sort_keys=True))


class CaseBDegradedEvidenceTests(unittest.TestCase):
    """CH-000005 / strongest candidate: no forensic evidence -> Editing NOT_AVAILABLE."""

    @classmethod
    def setUpClass(cls):
        cls.plan = orch.build_plan("CH-000005", "CH-000005-CAND-001", generated_on="2026-09-11")

    def test_assembles_from_separate_layers(self):
        self.assertEqual(self.plan["generation_state"], "ASSEMBLED_FROM_LAYERS")

    def test_topic_packaging_hook_script_available(self):
        self.assertTrue(self.plan["opportunity"]["topic"])
        self.assertTrue(self.plan["packaging"]["title_hypotheses"])
        self.assertTrue(self.plan["hook"]["hook_hypotheses"])
        self.assertTrue(self.plan["script"]["script_blueprint"])

    def test_editing_not_available_with_reason(self):
        self.assertEqual(self.plan["editing"]["status"], "NOT_AVAILABLE")
        self.assertEqual(self.plan["editing"]["reason"], "NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE")
        self.assertIsNone(self.plan["editing"]["blueprint"])
        self.assertEqual(self.plan["editing"]["channel_wide_editing_style"], "NOT_SUPPORTED")

    def test_workflow_does_not_hide_partial_hook_script_linkage(self):
        dims = self.plan["coherence"]["dimensions"]
        self.assertIn(dims["HOOK_PROMISE_MATCH"], ("PASS", "PARTIAL"))
        self.assertIn(dims["SCRIPT_PAYOFF_MATCH"], ("PASS", "PARTIAL"))
        self.assertEqual(dims["EDITING_VISUAL_MATCH"], "NOT_APPLICABLE")
        self.assertIn(self.plan["coherence"]["overall"], ("COHERENT", "PARTIAL"))

    def test_medical_validation_required_for_health_channel_without_external_validation(self):
        self.assertTrue(self.plan["global"]["medical_validation_required"])
        self.assertEqual(self.plan["opportunity"]["external_validation"], "NOT_AVAILABLE")

    def test_no_private_metrics_fabricated(self):
        for metric, value in self.plan["global"]["unavailable_metrics"].items():
            self.assertEqual(value, "NOT_AVAILABLE", metric)

    def test_deterministic_output(self):
        second = orch.build_plan("CH-000005", "CH-000005-CAND-001", generated_on="2026-09-11")
        self.assertEqual(json.dumps(self.plan, sort_keys=True), json.dumps(second, sort_keys=True))


class LayerDiscoveryTests(unittest.TestCase):
    def test_finds_current_non_pilot_artifacts_for_ch4(self):
        cdir = orch.channel_dir("CH-000004")
        packaging = orch.find_packaging_artifact(cdir)
        self.assertNotIn("pilot", packaging.name)

    def test_editing_artifact_absent_for_channel_without_forensic_evidence(self):
        cdir = orch.channel_dir("CH-000005")
        self.assertIsNone(orch.find_editing_artifact(cdir))

    def test_unknown_channel_rejected(self):
        with self.assertRaises(orch.OrchestrationError):
            orch.channel_dir("CH-999999")


class RejectionTests(unittest.TestCase):
    def test_mismatched_opportunity_across_channels_rejected(self):
        with self.assertRaises(orch.OrchestrationError):
            orch.build_plan("CH-000004", "CH-000005-CAND-001")

    def test_nonexistent_opportunity_rejected(self):
        with self.assertRaises(orch.OrchestrationError):
            orch.build_plan("CH-000004", "CH-000004-OP-999")


class CapabilityRegistryTests(unittest.TestCase):
    def test_registry_lists_all_canonical_channels_with_editing_status(self):
        registry = orch.build_capability_registry()
        channel_ids = {row["channel_id"] for row in registry["channels"]}
        self.assertEqual(
            channel_ids,
            {"CH-000001", "CH-000002", "CH-000003", "CH-000004", "CH-000005"},
        )
        by_id = {row["channel_id"]: row for row in registry["channels"]}
        self.assertEqual(by_id["CH-000004"]["EDITING"]["status"], "WORKING_WITH_LIMITATIONS")
        self.assertEqual(by_id["CH-000005"]["EDITING"]["status"], "NOT_AVAILABLE")


if __name__ == "__main__":
    unittest.main()
