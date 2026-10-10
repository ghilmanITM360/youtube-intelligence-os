import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import plan_intelligence_refresh as planner  # noqa: E402
import refresh_youtube_intelligence as runner  # noqa: E402


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def test_dependency_graph_is_explicit_and_acyclic():
    assert set(planner.DEPENDENCIES) == set(planner.RUN_ORDER)
    seen = set()
    for layer in planner.RUN_ORDER:
        assert set(planner.DEPENDENCIES[layer]) <= seen
        seen.add(layer)


def test_transcript_change_invalidates_only_relevant_chain():
    layers = planner.affected_layers("NEW_TRANSCRIPT")
    assert {"TOPIC", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "UNIFIED_PLAN"} <= set(layers)
    assert "PACKAGING" not in layers
    assert "EDITING" not in layers


def test_thumbnail_change_does_not_invalidate_transcript_layers():
    layers = planner.affected_layers("NEW_THUMBNAIL_BINARY")
    assert {"PACKAGING", "CHANNEL_STRATEGY", "UNIFIED_PLAN"} <= set(layers)
    assert "TOPIC" not in layers
    assert "HOOK_SCRIPT" not in layers


def test_forensic_change_invalidates_editing_strategy_and_plan():
    layers = planner.affected_layers("NEW_FORENSIC_EVIDENCE")
    assert {"EDITING", "CHANNEL_STRATEGY", "UNIFIED_PLAN"} <= set(layers)
    assert "TOPIC" not in layers


def test_new_channel_has_peer_and_cross_niche_impact():
    layers = planner.affected_layers("NEW_CHANNEL")
    assert {"CHANNEL_STRATEGY", "BENCHMARK", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"} <= set(layers)


def test_metric_snapshot_refreshes_performance_and_longitudinal_layers():
    layers = planner.affected_layers("NEW_PUBLIC_METRIC_SNAPSHOT")
    assert {"TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "PUBLIC_METRIC_TRAJECTORY", "CHANNEL_STRATEGY"} <= set(layers)


def test_first_party_refresh_contract_is_integrated():
    assert {"IMPRESSIONS_CTR", "IMPRESSIONS", "RETENTION_PERCENTAGE", "AVERAGE_VIEW_DURATION", "WATCH_TIME_HOURS", "TRAFFIC_SOURCE", "NEW_VIEWERS", "CASUAL_VIEWERS", "REGULAR_VIEWERS"} <= set(planner.FIRST_PARTY_ANALYTICS_FIELDS)
    layers = planner.affected_layers("NEW_FIRST_PARTY_ANALYTICS")
    assert {"TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "FIRST_PARTY_DIAGNOSIS", "CHANNEL_STRATEGY", "BLUEPRINT", "UNIFIED_PLAN"} <= set(layers)
    assert "CROSS_NICHE_CALIBRATION" not in layers


def test_fresh_baseline_has_deterministic_refresh_plan():
    # Test a fresh baseline in memory. A committed historical baseline may
    # legitimately require refresh after append-only identity registration.
    # Do not relabel older analytical artifacts current merely to pass tests.
    registry = planner.build_freshness_registry()
    first = planner.build_refresh_plan(registry)
    second = planner.build_refresh_plan(registry)
    assert first == second
    assert first["status"] == "NO_REFRESH_REQUIRED"
    assert first["artifacts_to_refresh"] == []
    assert first["artifacts_refreshed"] == []


def test_simulation_preserves_unaffected_artifacts():
    registry = json.loads(planner.REGISTRY_PATH.read_text(encoding="utf-8"))
    plan = planner.build_refresh_plan(
        registry,
        channel="CH-000005",
        simulated_changes=[{"change_type": "NEW_TRANSCRIPT", "channel_id": "CH-000005"}],
    )
    changed = {row["ARTIFACT_TYPE"] for row in plan["artifacts_to_refresh"]}
    unchanged = {row["ARTIFACT_TYPE"] for row in plan["artifacts_unchanged"]}
    assert "HOOK_SCRIPT" in changed
    assert "PACKAGING" in unchanged


def test_heuristic_confidence_can_upgrade_and_downgrade():
    old = {"heuristics": [{"rule_id": "R1", "archetype_kind": "hook", "archetype_id": "A", "CROSS_NICHE_RESULT": "NICHE_SPECIFIC_PATTERN", "CONFIDENCE": "LOW"}]}
    robust = {"heuristics": [{"rule_id": "R1", "archetype_kind": "hook", "archetype_id": "A", "CROSS_NICHE_RESULT": "ROBUST_CROSS_NICHE_PATTERN", "CONFIDENCE": "MEDIUM"}]}
    mixed = {"heuristics": [{"rule_id": "R1", "archetype_kind": "hook", "archetype_id": "A", "CROSS_NICHE_RESULT": "CONFLICTING_PATTERN", "CONFIDENCE": "LOW"}]}
    assert planner.heuristic_changes(old, robust)[0]["NEW_STATUS"] == "ROBUST_CROSS_NICHE_PATTERN"
    assert planner.heuristic_changes(robust, mixed)[0]["NEW_STATUS"] == "CONFLICTING_PATTERN"


def test_strategy_action_version_change_is_explicit():
    old = {"actions": [{"TARGET": "topic_family:X", "ACTION_TYPE": "WATCH", "CONFIDENCE": "LOW"}]}
    new = {"actions": [{"TARGET": "topic_family:X", "ACTION_TYPE": "DOUBLE_DOWN", "CONFIDENCE": "MEDIUM"}]}
    change = planner.action_changes(old, new)[0]
    assert change["OLD_ACTION"] == "WATCH"
    assert change["NEW_ACTION"] == "DOUBLE_DOWN"
    assert change["CONFIDENCE_CHANGE"] == {"from": "LOW", "to": "MEDIUM"}


def test_blueprint_version_change_is_explicit():
    old = {"positioning": {"value": "A"}, "core_content_pillars": ["X"]}
    new = {"positioning": {"value": "B"}, "core_content_pillars": ["X", "Y"]}
    changes = planner.blueprint_changes(old, new)
    assert {row["FIELD"] for row in changes} == {"POSITIONING", "PILLARS"}


def test_dry_run_mutates_neither_db_nor_artifacts(capsys):
    db = ROOT / "data/catalog/youtube_inventory.db"
    before_db = file_hash(db)
    before_files = sorted((str(p.relative_to(ROOT)), file_hash(p)) for p in (ROOT / "data/intelligence").rglob("*") if p.is_file())
    assert runner.main(["--channel", "CH-000005", "--replay", "--dry-run"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert set(payload) == {
        "WHAT_WOULD_RUN", "WHY", "INPUT_ARTIFACTS", "OUTPUT_ARTIFACTS",
        "WHAT_WOULD_REMAIN_UNCHANGED",
    }
    assert file_hash(db) == before_db
    after_files = sorted((str(p.relative_to(ROOT)), file_hash(p)) for p in (ROOT / "data/intelligence").rglob("*") if p.is_file())
    assert after_files == before_files


def test_historical_artifact_preserved_when_successor_written(tmp_path):
    old = tmp_path / "diagnosis-2026-09-11.json"
    old.write_text('{"value":1}\n', encoding="utf-8")
    before = old.read_bytes()
    successor = runner.write_successor(old, {"value": 2}, "REFRESH-TEST")
    assert old.read_bytes() == before
    assert successor != old
    assert json.loads(successor.read_text()) == {"value": 2}


def test_run_report_is_deterministic_with_fixed_inputs():
    args = dict(
        run_id="REFRESH-TEST", trigger=[{"change_type": "NEW_TRANSCRIPT", "channel_id": "CH-000005"}],
        affected_channels=["CH-000005"], upstream_changes=["NEW_TRANSCRIPT"], refreshed=[], unchanged=["a.json"],
        conclusion_changes=[], confidence_changes=[], blocked_layers=[], test_result="PASS",
        db_integrity="ok", git_base_commit="abc",
    )
    assert runner.build_run_report(**args) == runner.build_run_report(**args)


def test_refresh_modules_contain_no_network_client_imports():
    combined = (planner.__file__ and Path(planner.__file__).read_text()) + Path(runner.__file__).read_text()
    for forbidden in ("import requests", "import urllib", "import socket", "httpx", "youtube.com"):
        assert forbidden not in combined


def test_cross_niche_refresh_reuses_unaffected_niche():
    old = json.loads((ROOT / "data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json").read_text())
    calls = []

    def calibrate(channels):
        calls.append(channels)
        return [{
            "rule_id": row["rule_id"], "archetype_kind": row["archetype_kind"], "archetype_id": row["archetype_id"],
            "empirical_calibration_status": row["HEALTH_RESULT"],
            "observations": row["COUNTER_EVIDENCE"]["health_observations"],
        } for row in old["heuristics"]]

    refreshed = runner.rebuild_cross_niche(old, ["CH-000005"], calibrate=calibrate)
    assert calls == [["CH-000003", "CH-000005"]]
    assert refreshed == old
