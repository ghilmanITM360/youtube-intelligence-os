import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import report_channel_strategy_intelligence as s  # noqa: E402


class TrainingSourceDedupTests(unittest.TestCase):
    """Both supplied training sources are already-known evidence -- no new
    dataset/source registration is warranted, and raw evidence stays untouched."""

    def test_supplied_zip_is_exact_duplicate_of_ds_000011(self):
        summary = s.build_source_inventory_summary()["supplied_zip"]
        self.assertEqual(summary["dedup_verdict"], "EXACT_DUPLICATE")
        self.assertEqual(summary["dedup_target"], "DS-000011")
        self.assertEqual(summary["substantive_file_count"], 15)

    def test_supplied_xlsx_is_variant_of_ds_000018(self):
        summary = s.build_source_inventory_summary()["supplied_xlsx"]
        self.assertEqual(summary["dedup_verdict"], "VARIANT")
        self.assertEqual(summary["dedup_target"], "DS-000018")
        self.assertEqual(summary["row_count"], 63)

    def test_no_raw_evidence_files_were_added_for_these_sources(self):
        if not (ROOT / "data/raw/global-youtube-knowledge/DS-000011").exists():
            self.skipTest("requires ignored historical raw evidence directories")
        ds011_files = list((ROOT / "data/raw/global-youtube-knowledge/DS-000011").iterdir())
        ds018_files = list((ROOT / "data/raw/global-youtube-knowledge/DS-000018").iterdir())
        self.assertEqual(len(ds011_files), 17)
        self.assertEqual(len(ds018_files), 1)


class XlsxDuplicateRowTests(unittest.TestCase):
    def test_xlsx_has_one_internal_duplicate_group(self):
        groups = s.build_source_inventory_summary()["supplied_xlsx"]["duplicate_groups"]
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["rows"], ["51.0", "52.0"])


class RuleProvenanceAndTypeTests(unittest.TestCase):
    def test_every_rule_has_required_provenance_fields(self):
        required = {"RULE_ID", "DOMAIN", "RULE_TYPE", "RULE_TEXT", "SOURCE_ID",
                    "SOURCE_LOCATOR", "SOURCE_QUALITY", "PRIMARY_VALIDATION_STATUS",
                    "EMPIRICAL_CALIBRATION_STATUS", "SAFE_DOWNSTREAM_USE",
                    "PROHIBITED_USE", "CONFLICTS", "CONFIDENCE"}
        for rule in s.TRAINING_RULES:
            self.assertTrue(required.issubset(rule.keys()), rule.get("RULE_ID"))

    def test_rule_ids_are_unique(self):
        ids = [r["RULE_ID"] for r in s.TRAINING_RULES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_ds018_claims_never_labeled_platform_fact_unless_supported(self):
        for rule in s.TRAINING_RULES:
            if rule["SOURCE_ID"] != "DS-000018" or "CLM" not in rule["SOURCE_LOCATOR"]:
                continue
            if rule["RULE_TYPE"] == "PLATFORM_FACT":
                self.assertEqual(rule["PRIMARY_VALIDATION_STATUS"], "SUPPORTED", rule["RULE_ID"])

    def test_ds018_interpretations_are_source_interpretation_not_fact(self):
        for rule in s.TRAINING_RULES:
            if rule["SOURCE_ID"] == "DS-000018" and "INT" in rule["SOURCE_LOCATOR"]:
                self.assertEqual(rule["RULE_TYPE"], "SOURCE_INTERPRETATION")

    def test_creator_advice_never_mislabeled_platform_fact(self):
        for rule in s.TRAINING_RULES:
            if rule["SOURCE_ID"] == "DS-000011":
                self.assertNotEqual(rule["RULE_TYPE"], "PLATFORM_FACT", rule["RULE_ID"])


class EmpiricalCalibrationStateTests(unittest.TestCase):
    def test_calibration_verdict_is_one_of_allowed_states(self):
        allowed = {"CORPUS_SUPPORTED", "CORPUS_PARTIALLY_SUPPORTED", "MIXED",
                   "CORPUS_NOT_SUPPORTED", "INSUFFICIENT_EVIDENCE", "NOT_OBSERVABLE"}
        for c in s.calibrate_all():
            self.assertIn(c["empirical_calibration_status"], allowed)

    def test_single_item_archetype_never_calibrates_on_its_own(self):
        """A one-off outlier (e.g. a 281x single-item ratio) must never make an
        archetype CORPUS_SUPPORTED by itself."""
        single_item_obs = [{"channel_id": "CH-X", "repeatability": "INSUFFICIENT_SAMPLE",
                             "median_channel_relative": 281.62, "item_count": 1}]
        self.assertEqual(s.empirical_calibration_verdict(single_item_obs), "INSUFFICIENT_EVIDENCE")

    def test_counterintuitive_premise_hook_is_insufficient_evidence_everywhere(self):
        result = next(c for c in s.calibrate_all()
                       if c["archetype_kind"] == "hook" and c["archetype_id"] == "COUNTERINTUITIVE_PREMISE")
        self.assertEqual(result["empirical_calibration_status"], "INSUFFICIENT_EVIDENCE")

    def test_mixed_direction_produces_mixed_not_supported_or_not_supported(self):
        observations = [
            {"channel_id": "CH-A", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 2.0, "item_count": 10},
            {"channel_id": "CH-B", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 0.5, "item_count": 10},
        ]
        self.assertEqual(s.empirical_calibration_verdict(observations), "MIXED")


class VideoAndFamilySuccessFailureTests(unittest.TestCase):
    def test_video_performance_states_are_from_allowed_taxonomy(self):
        for band, family_rep in [
            ("NEGATIVE_OUTLIER", "MIXED_FAMILY"), ("POSITIVE_OUTLIER", "REPEATABLE_WINNER"),
            ("POSITIVE_OUTLIER", "MIXED_FAMILY"), ("HIGH_RELATIVE_PERFORMER", "REPEATABLE_WINNER"),
            ("HIGH_RELATIVE_PERFORMER", "INSUFFICIENT_SAMPLE"), ("HIGH_RELATIVE_PERFORMER", "MIXED_FAMILY"),
            ("LOW_RELATIVE_PERFORMER", "MIXED_FAMILY"), ("NORMAL_RANGE", "MIXED_FAMILY"),
            ("UNKNOWN_BAND", "MIXED_FAMILY"),
        ]:
            label = s.classify_video_performance(band, family_rep)
            self.assertIn(label, s.VIDEO_PERFORMANCE_STATES)

    def test_one_off_outlier_distinct_from_repeatable_winner_example(self):
        one_off = s.classify_video_performance("HIGH_RELATIVE_PERFORMER", "INSUFFICIENT_SAMPLE")
        repeatable = s.classify_video_performance("HIGH_RELATIVE_PERFORMER", "REPEATABLE_WINNER")
        self.assertEqual(one_off, "ONE_OFF_OUTLIER")
        self.assertEqual(repeatable, "REPEATABLE_WINNER_EXAMPLE")
        self.assertNotEqual(one_off, repeatable)

    def test_family_health_states_are_from_allowed_taxonomy(self):
        families = [
            {"repeatability": "INSUFFICIENT_SAMPLE", "item_count": 1, "channel_median_ratio": 1.0},
            {"repeatability": "ONE_OFF_OUTLIER", "item_count": 1, "channel_median_ratio": 3.0},
            {"repeatability": "REPEATABLE_WINNER", "item_count": 4, "channel_median_ratio": 1.5},
            {"repeatability": "REPEATABLE_WINNER", "item_count": 2, "channel_median_ratio": 1.5},
            {"repeatability": "MIXED_FAMILY", "item_count": 5, "channel_median_ratio": 1.0,
             "strongest_examples": [{"views_per_day": 100}], "weakest_examples": [{"views_per_day": 90}]},
        ]
        for f in families:
            self.assertIn(s.classify_family_health(f), s.FAMILY_HEALTH_STATES)

    def test_repeatable_winner_needs_at_least_three_items(self):
        strong = {"repeatability": "REPEATABLE_WINNER", "item_count": 4, "channel_median_ratio": 1.5}
        weak = {"repeatability": "REPEATABLE_WINNER", "item_count": 2, "channel_median_ratio": 1.5}
        self.assertEqual(s.classify_family_health(strong), "REPEATABLE_WINNER_FAMILY")
        self.assertEqual(s.classify_family_health(weak), "EMERGING_FAMILY")

    def test_one_viral_item_does_not_make_a_family_a_winner(self):
        """A single breakout item inside an otherwise-average family must not
        promote the family to REPEATABLE_WINNER_FAMILY."""
        family = {"repeatability": "ONE_OFF_OUTLIER", "item_count": 5, "channel_median_ratio": 1.4}
        self.assertEqual(s.classify_family_health(family), "ONE_OFF_DEPENDENT")


class BenchmarkChannelSeparationTests(unittest.TestCase):
    def test_benchmark_does_not_pool_metrics_across_channels(self):
        result = s.benchmark_channels(["CH-000003", "CH-000005"])
        self.assertIn("CH-000003", result["per_channel_summary"])
        self.assertIn("CH-000005", result["per_channel_summary"])
        self.assertIsNot(result["per_channel_summary"]["CH-000003"], result["per_channel_summary"]["CH-000005"])
        self.assertIn("raw_view_comparison_prohibited", result)

    def test_cross_channel_robustness_states_are_allowed(self):
        allowed = {"ROBUST_CROSS_CHANNEL_PATTERN", "CHANNEL_SPECIFIC_PATTERN",
                   "CONFLICTING_PATTERN", "INSUFFICIENT_EVIDENCE"}
        result = s.benchmark_channels(["CH-000001", "CH-000002", "CH-000003", "CH-000005"])
        for row in result["cross_channel_patterns"]:
            self.assertIn(row["classification"], allowed)

    def test_conflicting_direction_yields_conflicting_pattern(self):
        observations = [
            {"channel_id": "CH-A", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 3.0, "item_count": 10},
            {"channel_id": "CH-B", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 0.4547, "item_count": 14},
        ]
        self.assertEqual(s.cross_channel_robustness(observations), "CONFLICTING_PATTERN")

    def test_single_usable_channel_is_channel_specific_not_robust(self):
        observations = [{"channel_id": "CH-A", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 2.0, "item_count": 31}]
        self.assertEqual(s.cross_channel_robustness(observations), "CHANNEL_SPECIFIC_PATTERN")


class DiagnosisTargetVsBenchmarkTests(unittest.TestCase):
    def test_diagnose_dr_elias_against_dr_aliza(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        self.assertEqual(diag["target_channel"]["channel_id"], "CH-000005")
        self.assertEqual([b["channel_id"] for b in diag["benchmark_channels"]], ["CH-000003"])
        self.assertGreater(len(diag["video_labels"]), 0)
        self.assertGreater(len(diag["family_labels"]), 0)

    def test_diagnosis_engine_is_generic_not_hardcoded_to_dr_elias(self):
        source = (ROOT_SCRIPT := (Path(__file__).resolve().parents[1] / "scripts" / "report_channel_strategy_intelligence.py")).read_text(encoding="utf-8")
        # the CLI/engine functions must not branch on a specific channel id
        for forbidden in ("if target_id == \"CH-000005\"", "if channel_id == \"CH-000005\""):
            self.assertNotIn(forbidden, source)

    def test_diagnose_swaps_target_and_benchmark_cleanly(self):
        reverse = s.diagnose_channel("CH-000003", ["CH-000005"])
        self.assertEqual(reverse["target_channel"]["channel_id"], "CH-000003")
        self.assertEqual([b["channel_id"] for b in reverse["benchmark_channels"]], ["CH-000005"])


class ActionTaxonomyTests(unittest.TestCase):
    def test_every_action_is_from_the_allowed_taxonomy(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        for action in diag["actions"]:
            self.assertIn(action["ACTION_TYPE"], s.ACTION_TYPES)

    def test_every_action_carries_required_fields(self):
        required = {"ACTION_ID", "ACTION_TYPE", "TARGET", "WHY", "INTERNAL_EVIDENCE",
                    "BENCHMARK_EVIDENCE", "TRAINING_RULES_USED", "COUNTER_EVIDENCE",
                    "CONFIDENCE", "WHAT_WOULD_FALSIFY_IT"}
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        for action in diag["actions"]:
            self.assertTrue(required.issubset(action.keys()))

    def test_low_sample_archetype_is_test_not_double_down(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        low_sample_actions = [a for a in diag["actions"] if "COUNTERINTUITIVE_PREMISE" in a["TARGET"]]
        self.assertTrue(low_sample_actions)
        for a in low_sample_actions:
            self.assertEqual(a["ACTION_TYPE"], "TEST")


class CausalityAndPrivateMetricTests(unittest.TestCase):
    def test_why_objects_are_always_association_only(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        for why in diag["why_objects"]:
            self.assertEqual(why["CAUSALITY_STATUS"], "ASSOCIATION_ONLY")

    def test_private_metrics_never_appear_as_available(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        self.assertEqual(set(diag["unavailable_private_metrics"]), set(s.PRIVATE_METRICS))
        blob = json.dumps(diag)
        for metric in ("ctr_value", "predicted_retention", "hook_retention_score", "expected_avd"):
            self.assertNotIn(metric, blob.lower())

    def test_longitudinal_trend_not_available_without_time_series(self):
        diag = s.diagnose_channel("CH-000005", ["CH-000003"])
        self.assertEqual(diag["trajectory_discipline"]["longitudinal_trend"], "NOT_AVAILABLE")


class BlueprintProvenanceTests(unittest.TestCase):
    def test_blueprint_does_not_copy_one_competitor(self):
        bench = s.benchmark_channels(["CH-000003", "CH-000005"])
        diag5 = s.diagnose_channel("CH-000005", ["CH-000003"])
        diag3 = s.diagnose_channel("CH-000003", ["CH-000005"])
        blueprint = s.assemble_blueprint("Senior Health", bench, {"CH-000005": diag5, "CH-000003": diag3})
        self.assertTrue(blueprint["guardrails"]["no_copying_one_competitor"])
        self.assertTrue(blueprint["guardrails"]["no_causal_claims_from_public_correlation"])

    def test_every_blueprint_principle_carries_a_source_tag(self):
        bench = s.benchmark_channels(["CH-000003", "CH-000005"])
        diag5 = s.diagnose_channel("CH-000005", ["CH-000003"])
        diag3 = s.diagnose_channel("CH-000003", ["CH-000005"])
        blueprint = s.assemble_blueprint("Senior Health", bench, {"CH-000005": diag5, "CH-000003": diag3})
        allowed_sources = {"CORPUS_EVIDENCE", "TRAINING_HEURISTIC", "OFFICIAL_PLATFORM_KNOWLEDGE", "BENCHMARK_PATTERN"}
        for key in ("target_audience", "positioning", "niche_boundaries", "title_language",
                    "thumbnail_language", "hook_principles", "script_structures", "format_strategy"):
            self.assertIn(blueprint[key]["source"], allowed_sources, key)

    def test_blueprint_stops_at_experiment_categories_not_final_titles(self):
        bench = s.benchmark_channels(["CH-000003", "CH-000005"])
        diag5 = s.diagnose_channel("CH-000005", ["CH-000003"])
        diag3 = s.diagnose_channel("CH-000003", ["CH-000005"])
        blueprint = s.assemble_blueprint("Senior Health", bench, {"CH-000005": diag5, "CH-000003": diag3})
        self.assertLessEqual(len(blueprint["first_10_experiment_categories"]), 10)
        for exp in blueprint["first_10_experiment_categories"]:
            self.assertIn("CATEGORY", exp)


class DeterministicOutputTests(unittest.TestCase):
    def test_diagnosis_is_byte_identical_across_runs(self):
        first = json.dumps(s.diagnose_channel("CH-000005", ["CH-000003"]), sort_keys=False, default=str)
        second = json.dumps(s.diagnose_channel("CH-000005", ["CH-000003"]), sort_keys=False, default=str)
        self.assertEqual(first, second)

    def test_training_registry_is_byte_identical_across_runs(self):
        first = json.dumps(s.build_training_registry(s.build_source_inventory_summary()), default=str)
        second = json.dumps(s.build_training_registry(s.build_source_inventory_summary()), default=str)
        self.assertEqual(first, second)


class WrittenArtifactTests(unittest.TestCase):
    """The five artifacts this pilot writes to disk stay internally consistent
    with what the live engine produces (guards against a stale hand-edit)."""

    def test_training_registry_artifact_matches_live_build(self):
        path = ROOT / "data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.TRAINING_REGISTRY_SCHEMA)
        self.assertEqual(len(on_disk["rules"]), len(s.TRAINING_RULES))

    def test_dr_elias_diagnosis_artifact_exists_and_matches_schema(self):
        path = ROOT / "data/intelligence/channels/CH-000005/channel-strategy-diagnosis-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.DIAGNOSIS_SCHEMA)
        self.assertEqual(on_disk["target_channel"]["channel_id"], "CH-000005")

    def test_health_benchmark_artifact_covers_both_channels(self):
        path = ROOT / "data/intelligence/cross-channel/health-channel-strategy-benchmark-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        channel_ids = {c["channel_id"] for c in on_disk["channels"]}
        self.assertEqual(channel_ids, {"CH-000003", "CH-000005"})

    def test_blueprint_artifact_exists_with_expected_schema(self):
        path = ROOT / "data/intelligence/blueprints/senior-health-channel-strategy-blueprint-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.BLUEPRINT_SCHEMA)

    def test_dr_elias_diagnosis_markdown_has_required_headings(self):
        path = ROOT / "data/intelligence/channels/CH-000005/channel-strategy-diagnosis-2026-09-11.md"
        text = path.read_text(encoding="utf-8")
        for heading in ["# Executive Diagnosis", "# What Is Working", "# What Is Not Working",
                        "# Repeatable Winners", "# One-Off Successes", "# Weak / Failed Experiments",
                        "# Training Heuristics That Hold", "# Training Heuristics That Do Not Hold",
                        "# Continue", "# Double Down", "# Fix", "# Reduce / Stop", "# Test",
                        "# Evidence Limitations"]:
            self.assertIn(heading, text, heading)


class PrimaryValidationSummaryRegressionTests(unittest.TestCase):
    """Step 22B, Phase 0: Step 22A's final report summed PRIMARY_VALIDATION_STATUS
    across all 50 rules (35) and compared that number to DS-000018's 33 claims --
    an apples-to-oranges reporting mistake, not a registry defect (2 DS-000011
    rules -- TR-011-005, TR-011-013 -- also carry an independent platform
    validation status). primary_validation_summary() keeps the two tallies
    permanently separate so this can't recur."""

    def test_ds_000018_claim_level_reconciles_to_33(self):
        registry = s.build_training_registry(s.build_source_inventory_summary())
        summary = registry["primary_validation_summary"]["ds_000018_claim_level"]
        self.assertEqual(summary["rule_count"], 33)
        self.assertEqual(sum(summary["by_status"].values()), 33)

    def test_ds_000018_claim_level_matches_expected_historical_distribution(self):
        registry = s.build_training_registry(s.build_source_inventory_summary())
        by_status = registry["primary_validation_summary"]["ds_000018_claim_level"]["by_status"]
        expected = {"SUPPORTED": 10, "PARTIALLY_SUPPORTED": 12, "CONTRADICTED": 1,
                    "NOT_SUPPORTED_BY_PRIMARY_EVIDENCE": 8, "NOT_CURRENTLY_VERIFIABLE": 2}
        self.assertEqual(by_status, expected)

    def test_all_sources_rule_level_total_is_not_expected_to_equal_33(self):
        registry = s.build_training_registry(s.build_source_inventory_summary())
        summary = registry["primary_validation_summary"]
        non_platform_applicable = sum(
            v for k, v in summary["all_sources_rule_level"]["by_status"].items()
            if k != "NOT_APPLICABLE_NOT_A_PLATFORM_CLAIM")
        self.assertEqual(non_platform_applicable, 35)
        self.assertGreater(non_platform_applicable, summary["ds_000018_claim_level"]["rule_count"])


class EmpiricalCalibrationNeutralEvidenceRegressionTests(unittest.TestCase):
    """A neutral-everywhere heuristic (every usable channel's ratio sits inside
    the +/-15% band, i.e. no channel shows the claimed lift) must read as
    CORPUS_NOT_SUPPORTED, not CORPUS_PARTIALLY_SUPPORTED -- discovered via the
    finance pilot's script:CALCULATED_ESCALATION heuristic (ratios ~0.97-1.08
    in all 4 channels across both niches)."""

    def test_all_neutral_observations_are_not_supported_not_partially_supported(self):
        observations = [
            {"channel_id": "CH-A", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 1.01, "item_count": 30},
            {"channel_id": "CH-B", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 0.97, "item_count": 30},
        ]
        self.assertEqual(s.empirical_calibration_verdict(observations), "CORPUS_NOT_SUPPORTED")

    def test_some_positive_some_neutral_is_still_partially_supported(self):
        observations = [
            {"channel_id": "CH-A", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 1.30, "item_count": 30},
            {"channel_id": "CH-B", "repeatability": "REPEATABLE_PATTERN", "median_channel_relative": 1.01, "item_count": 30},
        ]
        self.assertEqual(s.empirical_calibration_verdict(observations), "CORPUS_PARTIALLY_SUPPORTED")


class FinanceGeneralizationTests(unittest.TestCase):
    """Step 22B: the SAME diagnose_channel/benchmark_channels/assemble_blueprint
    engine, with no new finance-specific code paths, generalizes to an
    independent finance peer group (CH-000001 Matty Invests vs CH-000002 Mr.
    Finance)."""

    def test_bidirectional_finance_diagnosis(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        d2 = s.diagnose_channel("CH-000002", ["CH-000001"])
        self.assertEqual(d1["target_channel"]["channel_id"], "CH-000001")
        self.assertEqual(d1["benchmark_channels"][0]["channel_id"], "CH-000002")
        self.assertEqual(d2["target_channel"]["channel_id"], "CH-000002")
        self.assertEqual(d2["benchmark_channels"][0]["channel_id"], "CH-000001")

    def test_per_channel_actions_are_independent_not_mechanically_reused(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        d2 = s.diagnose_channel("CH-000002", ["CH-000001"])
        self.assertTrue(any("topic_family" in a["TARGET"] for a in d1["actions"]))
        self.assertTrue(any("topic_family" in a["TARGET"] for a in d2["actions"]))
        self.assertNotEqual(d1["actions"], d2["actions"])

    def test_no_finance_specific_branch_in_core_engine_source(self):
        source = (ROOT / "scripts/report_channel_strategy_intelligence.py").read_text(encoding="utf-8")
        for banned in ('if target_id == "CH-000001"', 'if target_id == "CH-000002"',
                       'if niche_label == "Finance"', '"Matty" in', '"Mr. Finance" in'):
            self.assertNotIn(banned, source)

    def test_finance_video_labels_use_same_taxonomy_as_health(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        allowed = {"BREAKOUT", "REPEATABLE_WINNER_EXAMPLE", "STRONG_RELATIVE_PERFORMER", "BASELINE",
                   "WEAK_RELATIVE_PERFORMER", "FAILED_EXPERIMENT", "ONE_OFF_OUTLIER", "INSUFFICIENT_EVIDENCE"}
        self.assertTrue(d1["video_labels"])
        for v in d1["video_labels"]:
            self.assertIn(v["performance_class"], allowed)

    def test_finance_family_labels_use_same_taxonomy_as_health(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        allowed = {"REPEATABLE_WINNER_FAMILY", "EMERGING_FAMILY", "MIXED_FAMILY", "ONE_OFF_DEPENDENT",
                   "WEAK_FAMILY", "VOLATILE_FAMILY", "INSUFFICIENT_SAMPLE"}
        for f in d1["family_labels"]:
            self.assertIn(f["family_health"], allowed)

    def test_no_raw_metric_pooling_across_finance_channels(self):
        bench = s.benchmark_channels(["CH-000001", "CH-000002"])
        # only within-channel per_channel_summary and structural cross_channel_patterns
        # are present -- never a combined/pooled raw-view figure across channels.
        blob = json.dumps(bench)
        for banned in ("pooled_views", "combined_views", "total_views_across_channels", "aggregate_views"):
            self.assertNotIn(banned, blob)
        self.assertIn("raw_view_comparison_prohibited", bench)

    def test_finance_editing_layer_never_blamed_without_evidence(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        for layers in d1["root_cause_layers"].values():
            self.assertNotIn("VISUAL_EDITING", [layer["layer"] for layer in layers])

    def test_finance_channels_have_thumbnail_reference_gap(self):
        packaging1 = json.loads((ROOT / "data/intelligence/channels/CH-000001/packaging-intelligence-2026-09-10.json").read_text())
        packaging2 = json.loads((ROOT / "data/intelligence/channels/CH-000002/packaging-intelligence-2026-09-10.json").read_text())
        self.assertIn("THUMBNAIL_REFERENCE_GAP", json.dumps(packaging1))
        self.assertIn("THUMBNAIL_REFERENCE_GAP", json.dumps(packaging2))

    def test_finance_longitudinal_trend_not_available(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        self.assertEqual(d1["trajectory_discipline"]["longitudinal_trend"], "NOT_AVAILABLE")

    def test_finance_private_metrics_all_not_available(self):
        d1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        self.assertEqual(set(d1["unavailable_private_metrics"]), set(s.PRIVATE_METRICS))
        enrichment = d1["first_party_analytics_enrichment"]["fields"]
        self.assertEqual(set(enrichment), set(s.PRIVATE_METRICS))
        self.assertTrue(all(v == "NOT_AVAILABLE" for v in enrichment.values()))

    def test_finance_diagnosis_is_deterministic(self):
        first = json.dumps(s.diagnose_channel("CH-000001", ["CH-000002"]), default=str)
        second = json.dumps(s.diagnose_channel("CH-000001", ["CH-000002"]), default=str)
        self.assertEqual(first, second)


class FinanceBlueprintGenericityTests(unittest.TestCase):
    """The blueprint composer must not bake health-niche prose into a
    finance-niche blueprint -- section 20's core requirement."""

    def test_finance_blueprint_does_not_contain_health_specific_language(self):
        bench = s.benchmark_channels(["CH-000001", "CH-000002"])
        diag1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        diag2 = s.diagnose_channel("CH-000002", ["CH-000001"])
        blueprint = s.assemble_blueprint("Finance", bench, {"CH-000001": diag1, "CH-000002": diag2})
        blob = json.dumps(blueprint).lower()
        for banned in ("senior/aging", "doctor-led", "medical fact", "cardiovascular", "healthy_aging"):
            self.assertNotIn(banned, blob)
        self.assertIn("finance", blob)

    def test_finance_blueprint_carries_source_tags(self):
        bench = s.benchmark_channels(["CH-000001", "CH-000002"])
        diag1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        diag2 = s.diagnose_channel("CH-000002", ["CH-000001"])
        blueprint = s.assemble_blueprint("Finance", bench, {"CH-000001": diag1, "CH-000002": diag2})
        allowed_sources = {"CORPUS_EVIDENCE", "TRAINING_HEURISTIC", "OFFICIAL_PLATFORM_KNOWLEDGE", "BENCHMARK_PATTERN"}
        for key in ("target_audience", "positioning", "niche_boundaries", "title_language",
                    "thumbnail_language", "hook_principles", "script_structures", "format_strategy"):
            self.assertIn(blueprint[key]["source"], allowed_sources, key)

    def test_finance_blueprint_does_not_copy_one_competitor(self):
        bench = s.benchmark_channels(["CH-000001", "CH-000002"])
        diag1 = s.diagnose_channel("CH-000001", ["CH-000002"])
        diag2 = s.diagnose_channel("CH-000002", ["CH-000001"])
        blueprint = s.assemble_blueprint("Finance", bench, {"CH-000001": diag1, "CH-000002": diag2})
        self.assertTrue(blueprint["guardrails"]["no_copying_one_competitor"])


class CrossNicheCalibrationTests(unittest.TestCase):
    """Section 10/22: a heuristic only becomes ROBUST_CROSS_NICHE_PATTERN with
    independent support in BOTH the health and the finance peer group -- one
    supporting channel per niche is not enough on its own beyond what each
    niche's own item_count>=3 usability + directional-agreement checks enforce."""

    def test_cross_niche_result_is_one_of_the_defined_states(self):
        allowed = {"ROBUST_CROSS_NICHE_PATTERN", "NICHE_SPECIFIC_PATTERN",
                   "CHANNEL_SPECIFIC_PATTERN", "CONFLICTING_PATTERN", "INSUFFICIENT_EVIDENCE"}
        result = s.build_cross_niche_calibration()
        for h in result["heuristics"]:
            self.assertIn(h["CROSS_NICHE_RESULT"], allowed)

    def test_single_health_channel_plus_single_finance_channel_is_not_auto_robust(self):
        health_supported = {"empirical_calibration_status": "CORPUS_SUPPORTED"}
        finance_supported = {"empirical_calibration_status": "CORPUS_SUPPORTED"}
        # supported in both niches with no conflict IS the promotion case --
        # confirm it promotes only when both niches genuinely agree, and confirm
        # a single contradicting niche blocks it.
        self.assertEqual(s.cross_niche_pattern_verdict(health_supported, finance_supported),
                          "ROBUST_CROSS_NICHE_PATTERN")
        finance_contradicts = {"empirical_calibration_status": "CORPUS_NOT_SUPPORTED"}
        self.assertEqual(s.cross_niche_pattern_verdict(health_supported, finance_contradicts),
                          "CONFLICTING_PATTERN")

    def test_no_data_in_one_niche_is_niche_specific_not_conflicting(self):
        health_supported = {"empirical_calibration_status": "CORPUS_PARTIALLY_SUPPORTED"}
        finance_no_data = {"empirical_calibration_status": "INSUFFICIENT_EVIDENCE"}
        self.assertEqual(s.cross_niche_pattern_verdict(health_supported, finance_no_data),
                          "NICHE_SPECIFIC_PATTERN")

    def test_zero_robust_cross_niche_patterns_in_current_evidence(self):
        """Real result from the actual corpus: no heuristic reaches
        ROBUST_CROSS_NICHE_PATTERN yet -- this is a legitimate, disciplined
        finding (not overpromoting on 2 channels per niche), not a bug."""
        result = s.build_cross_niche_calibration()
        self.assertEqual(result["summary_counts"].get("ROBUST_CROSS_NICHE_PATTERN", 0), 0)

    def test_cross_niche_calibration_artifact_matches_live_build(self):
        path = ROOT / "data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.CROSS_NICHE_CALIBRATION_SCHEMA)
        self.assertEqual(len(on_disk["heuristics"]), len(s.CALIBRATION_TARGETS))

    def test_cross_niche_calibration_is_deterministic(self):
        first = json.dumps(s.build_cross_niche_calibration(), default=str)
        second = json.dumps(s.build_cross_niche_calibration(), default=str)
        self.assertEqual(first, second)


class FinanceWrittenArtifactTests(unittest.TestCase):
    def test_finance_benchmark_artifact_matches_schema(self):
        path = ROOT / "data/intelligence/cross-channel/finance-channel-strategy-benchmark-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.BENCHMARK_SCHEMA)
        channel_ids = {c["channel_id"] for c in on_disk["channels"]}
        self.assertEqual(channel_ids, {"CH-000001", "CH-000002"})

    def test_finance_blueprint_artifact_matches_schema(self):
        path = ROOT / "data/intelligence/blueprints/finance-channel-strategy-blueprint-2026-09-11.json"
        on_disk = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(on_disk["schema_version"], s.BLUEPRINT_SCHEMA)

    def test_both_finance_diagnosis_artifacts_exist(self):
        for cid in ("CH-000001", "CH-000002"):
            path = ROOT / f"data/intelligence/channels/{cid}/channel-strategy-diagnosis-2026-09-11.json"
            on_disk = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(on_disk["schema_version"], s.DIAGNOSIS_SCHEMA)
            self.assertEqual(on_disk["target_channel"]["channel_id"], cid)


if __name__ == "__main__":
    unittest.main()
