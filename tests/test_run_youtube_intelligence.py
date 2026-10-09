import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_youtube_intelligence as orch  # noqa: E402


class ForensicIndexContractTests(unittest.TestCase):
    def test_rejects_index_video_absent_from_channel_catalog(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "forensic-observation-index-v1.json"
            path.write_text(json.dumps({
                "schema_version": "forensic-observation-index-1",
                "channel_id": "CH-000004", "video_count": 1,
                "videos": [{"youtube_video_id": "missing0001"}],
            }))
            conn = sqlite3.connect(":memory:")
            conn.row_factory = sqlite3.Row
            try:
                conn.execute("CREATE TABLE videos (youtube_video_id TEXT, channel_id TEXT)")
                with self.assertRaisesRegex(orch.OrchestrationError, "unregistered video identity"):
                    orch.registered_forensic_index(path, "CH-000004", conn)
            finally:
                conn.close()

FULL_HISTORICAL_CATALOG = (ROOT / "data/raw/competitors/DS-000001").exists()
REQUIRES_HISTORICAL = unittest.skipUnless(FULL_HISTORICAL_CATALOG, "requires ignored historical catalog evidence")


@REQUIRES_HISTORICAL
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
        index = self.plan["editing"]["forensic_observation_index"]
        self.assertEqual(index["video_count"], 10)
        self.assertEqual(index["observation_count"], 8327)
        self.assertFalse(index["used_in_existing_blueprint"])
        self.assertTrue(index["not_independent_channel_samples"])

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


@REQUIRES_HISTORICAL
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

    def test_registry_is_not_optimistic_about_packaging_visual_gap(self):
        by_id = {row["channel_id"]: row for row in orch.build_capability_registry()["channels"]}
        for channel_id in ("CH-000001", "CH-000002"):
            self.assertEqual(by_id[channel_id]["PACKAGING_TITLE"]["status"], "WORKING")
            self.assertEqual(by_id[channel_id]["PACKAGING_VISUAL"]["status"], "NOT_AVAILABLE")
            self.assertEqual(by_id[channel_id]["PACKAGING_VISUAL"]["reason"], "THUMBNAIL_REFERENCE_GAP")
            self.assertEqual(by_id[channel_id]["PACKAGING"]["status"], "WORKING_WITH_LIMITATIONS")

    def test_registry_reflects_working_visual_packaging_where_thumbnails_exist(self):
        by_id = {row["channel_id"]: row for row in orch.build_capability_registry()["channels"]}
        for channel_id in ("CH-000003", "CH-000004", "CH-000005"):
            self.assertEqual(by_id[channel_id]["PACKAGING_VISUAL"]["status"], "WORKING")

    def test_registry_lists_hook_script_as_working_for_all_channels_after_generalization(self):
        by_id = {row["channel_id"]: row for row in orch.build_capability_registry()["channels"]}
        for channel_id in ("CH-000001", "CH-000002", "CH-000003", "CH-000004", "CH-000005"):
            self.assertEqual(by_id[channel_id]["HOOK"]["status"], "WORKING")
            self.assertEqual(by_id[channel_id]["SCRIPT"]["status"], "WORKING")

    def test_registry_medical_validation_only_for_health_channels(self):
        by_id = {row["channel_id"]: row for row in orch.build_capability_registry()["channels"]}
        self.assertEqual(by_id["CH-000003"]["MEDICAL_VALIDATION"]["status"], "VALIDATION_REQUIRED")
        self.assertEqual(by_id["CH-000005"]["MEDICAL_VALIDATION"]["status"], "VALIDATION_REQUIRED")
        self.assertEqual(by_id["CH-000001"]["MEDICAL_VALIDATION"]["status"], "NOT_APPLICABLE")


@REQUIRES_HISTORICAL
class AllChannelOrchestrationTests(unittest.TestCase):
    """Every canonical channel must compose a plan using its own strongest
    existing candidate/opportunity -- no channel is forced to fail or to a
    fabricated COHERENT verdict."""

    OPPORTUNITIES = {
        "CH-000001": "CH-000001-CAND-001",
        "CH-000002": "CH-000002-CAND-001",
        "CH-000003": "CH-000003-CAND-001",
        "CH-000004": "CH-000004-OP-001",
        "CH-000005": "CH-000005-CAND-001",
    }

    def test_all_five_channels_compose_without_error(self):
        for channel_id, opportunity_id in self.OPPORTUNITIES.items():
            plan = orch.build_plan(channel_id, opportunity_id, generated_on="2026-09-11")
            self.assertEqual(plan["channel_id"], channel_id)
            self.assertIn(plan["coherence"]["overall"], ("COHERENT", "PARTIAL"))
            for metric, value in plan["global"]["unavailable_metrics"].items():
                self.assertEqual(value, "NOT_AVAILABLE", metric)

    def test_title_only_packaging_degrades_without_failing_workflow(self):
        plan = orch.build_plan("CH-000001", "CH-000001-CAND-001", generated_on="2026-09-11")
        self.assertTrue(plan["packaging"]["title_hypotheses"])
        self.assertNotEqual(plan["coherence"]["overall"], "INCOHERENT")


@REQUIRES_HISTORICAL
class CH5LinkageTests(unittest.TestCase):
    """CH-000005's per-opportunity linkage object must honestly reflect real
    evidence overlap -- never force a full match it cannot support."""

    @classmethod
    def setUpClass(cls):
        cls.plan = orch.build_plan("CH-000005", "CH-000005-CAND-001", generated_on="2026-09-11")

    def test_linkage_object_has_required_fields(self):
        linkage = self.plan["linkage"]
        for field in ("OPPORTUNITY_ID", "PACKAGE_LINKS", "HOOK_LINKS", "SCRIPT_BLUEPRINT_LINK",
                      "EVIDENCE_OVERLAP", "SEMANTIC_MATCH", "PROMISE_MATCH", "PAYOFF_MATCH", "LIMITATIONS"):
            self.assertIn(field, linkage)
        self.assertEqual(linkage["OPPORTUNITY_ID"], "CH-000005-CAND-001")

    def test_script_overlap_is_full_and_honestly_marked(self):
        linkage = self.plan["linkage"]
        evidence = set(linkage["EVIDENCE_OVERLAP"]["opportunity_evidence_video_ids"])
        script_overlap = set(linkage["EVIDENCE_OVERLAP"]["script_overlap_video_ids"])
        self.assertEqual(script_overlap, evidence)
        self.assertEqual(linkage["PAYOFF_MATCH"], "FULL_MATCH")

    def test_hook_overlap_is_partial_and_not_forced_to_full(self):
        linkage = self.plan["linkage"]
        evidence = set(linkage["EVIDENCE_OVERLAP"]["opportunity_evidence_video_ids"])
        hook_overlap = set(linkage["EVIDENCE_OVERLAP"]["hook_overlap_video_ids"])
        self.assertLess(hook_overlap, evidence)
        self.assertEqual(linkage["SEMANTIC_MATCH"], "PARTIAL_MATCH")
        self.assertEqual(linkage["PROMISE_MATCH"], "PARTIAL_MATCH")

    def test_overall_coherence_not_forced_coherent(self):
        self.assertEqual(self.plan["coherence"]["overall"], "PARTIAL")
        self.assertEqual(self.plan["coherence"]["dimensions"]["SCRIPT_PAYOFF_MATCH"], "PASS")
        self.assertEqual(self.plan["coherence"]["dimensions"]["HOOK_PROMISE_MATCH"], "PARTIAL")


class MedicalValidationStatusTests(unittest.TestCase):
    def test_health_channel_without_external_source_requires_validation(self):
        plan = orch.build_plan("CH-000005", "CH-000005-CAND-001", generated_on="2026-09-11")
        self.assertEqual(plan["global"]["medical_validation_status"], "VALIDATION_REQUIRED")
        self.assertEqual(plan["global"]["authoritative_sources"], [])

    def test_non_health_channel_is_not_applicable(self):
        plan = orch.build_plan("CH-000004", "CH-000004-OP-001", generated_on="2026-09-11")
        self.assertEqual(plan["global"]["medical_validation_status"], "NOT_APPLICABLE")
        self.assertEqual(plan["global"]["authoritative_sources"], [])


if __name__ == "__main__":
    unittest.main()
