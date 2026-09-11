#!/usr/bin/env python3
"""Execute an affected-only intelligence refresh from canonical evidence."""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import plan_intelligence_refresh as planner  # noqa: E402
import report_channel_strategy_intelligence as strategy  # noqa: E402
import report_editing_visual_intelligence as editing  # noqa: E402
import report_hook_script_intelligence as hook_script  # noqa: E402
import report_packaging_intelligence as packaging  # noqa: E402
import report_topic_opportunity as topic  # noqa: E402
import run_youtube_intelligence as orchestrator  # noqa: E402

RUNS_DIR = ROOT / "data/intelligence/system/refresh-runs"
REFRESHABLE = {
    "TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "CHANNEL_STRATEGY", "BENCHMARK",
    "TRAINING_KNOWLEDGE", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN",
    "CAPABILITY_REGISTRY", "EDITING_AVAILABILITY",
}


def _render(payload):
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _semantic(value):
    volatile = {"generated_on", "generated_at", "generated_from_commit", "GENERATED_AT", "GENERATED_FROM_COMMIT"}
    if isinstance(value, dict):
        return {
            key: _semantic(item) for key, item in value.items()
            if key not in volatile and not (key == "unavailable_transcripts" and item == [])
        }
    if isinstance(value, list):
        return [_semantic(item) for item in value]
    return value


def semantic_equal(left, right):
    return _semantic(left) == _semantic(right)


def write_successor(current_path, payload, run_id):
    """Write a new version beside current artifact; never replace current bytes."""
    current_path = Path(current_path)
    candidate = current_path.with_name(f"{current_path.stem}-refresh-{run_id}{current_path.suffix}")
    index = 2
    while candidate.exists():
        candidate = current_path.with_name(f"{current_path.stem}-refresh-{run_id}-{index}{current_path.suffix}")
        index += 1
    candidate.write_text(_render(payload), encoding="utf-8")
    return candidate


def build_run_report(run_id, trigger, affected_channels, upstream_changes, refreshed, unchanged,
                     conclusion_changes, confidence_changes, blocked_layers, test_result,
                     db_integrity, git_base_commit):
    return {
        "schema_version": "intelligence-refresh-run-1",
        "RUN_ID": run_id,
        "TRIGGER": trigger,
        "AFFECTED_CHANNELS": sorted(affected_channels),
        "UPSTREAM_CHANGES": sorted(upstream_changes),
        "ARTIFACTS_REFRESHED": refreshed,
        "ARTIFACTS_UNCHANGED": unchanged,
        "CONCLUSIONS_CHANGED": conclusion_changes,
        "CONFIDENCE_CHANGES": confidence_changes,
        "BLOCKED_LAYERS": blocked_layers,
        "TEST_RESULT": test_result,
        "DB_INTEGRITY": db_integrity,
        "GIT_BASE_COMMIT": git_base_commit,
    }


def _path(value):
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def _current_payload(record):
    return json.loads(_path(record["PATH"]).read_text(encoding="utf-8"))


def _channel(record):
    if len(record["CHANNEL_IDS"]) != 1:
        raise ValueError(f"{record['ARTIFACT_TYPE']} needs one channel: {record['PATH']}")
    return record["CHANNEL_IDS"][0]


def _relative(path):
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def _registered_thumbnail_count(conn, channel_id):
    return conn.execute(
        "SELECT COUNT(DISTINCT vs.video_id) FROM video_snapshots vs JOIN videos v ON v.video_id=vs.video_id "
        "WHERE v.channel_id=? AND vs.thumbnail_url IS NOT NULL", (channel_id,)).fetchone()[0]


def rebuild_payload(record, generated_on):
    """Call existing pure builders. No acquisition, classification, or DB writes."""
    kind = record["ARTIFACT_TYPE"]
    old = _current_payload(record)
    if kind == "TOPIC":
        with planner.connect_ro() as conn:
            return topic.build_report(conn, _channel(record), generated_on)
    if kind == "PACKAGING":
        channel_id = _channel(record)
        cdir = orchestrator.channel_dir(channel_id)
        topic_path = orchestrator.find_topic_artifact(cdir)
        topic_payload = orchestrator.load_json(topic_path)
        provenance = old.get("provenance", {})
        acquisition_path = provenance.get("acquisition_manifest")
        acquisition = orchestrator.load_json(_path(acquisition_path)) if acquisition_path else None
        annotations_path = planner._pick_current(cdir.glob("thumbnail-visual-annotations*.json"))
        annotations = orchestrator.load_json(annotations_path) if annotations_path else None
        with planner.connect_ro() as conn:
            result = packaging.build_report(topic_payload, acquisition, annotations, _registered_thumbnail_count(conn, channel_id))
        result["generated_on"] = generated_on
        result["provenance"]["topic_artifact"] = _relative(topic_path)
        if acquisition_path:
            result["provenance"]["acquisition_manifest"] = acquisition_path
        return result
    if kind == "HOOK_SCRIPT":
        channel_id = _channel(record)
        cdir = orchestrator.channel_dir(channel_id)
        topic_payload = orchestrator.load_json(orchestrator.find_topic_artifact(cdir))
        packaging_payload = orchestrator.load_json(orchestrator.find_packaging_artifact(cdir))
        interpretation_path = planner._pick_current(cdir.glob("hook-script*interpretations*.json"))
        interpretations = orchestrator.load_json(interpretation_path) if interpretation_path else None
        with planner.connect_ro() as conn:
            result = hook_script.build_report(conn, channel_id, topic_payload, packaging_payload, None, interpretations)
        result["generated_on"] = generated_on
        return result
    if kind == "EDITING":
        channel_id = _channel(record)
        cdir = orchestrator.channel_dir(channel_id)
        with planner.connect_ro() as conn:
            return editing.build_report(
                conn, channel_id,
                orchestrator.load_json(orchestrator.find_topic_artifact(cdir)),
                orchestrator.load_json(orchestrator.find_packaging_artifact(cdir)),
                orchestrator.load_json(orchestrator.find_hook_script_artifact(cdir)),
                generated_on,
            )
    if kind == "CHANNEL_STRATEGY":
        channel_id = old["target_channel"]["channel_id"]
        peers = [row["channel_id"] for row in old.get("benchmark_channels", [])]
        result = strategy.diagnose_channel(channel_id, peers)
        result["generated_on"] = generated_on
        return result
    if kind == "BENCHMARK":
        result = strategy.benchmark_channels([row["channel_id"] for row in old["channels"]])
        result["generated_on"] = generated_on
        return result
    if kind == "TRAINING_KNOWLEDGE":
        result = strategy.build_training_registry(strategy.build_source_inventory_summary())
        result["generated_on"] = generated_on
        return result
    if kind == "CROSS_NICHE_CALIBRATION":
        result = strategy.build_cross_niche_calibration()
        result["generated_on"] = generated_on
        return result
    if kind == "BLUEPRINT":
        channel_ids = old["benchmark_channels"]
        benchmark = strategy.benchmark_channels(channel_ids)
        diagnoses = {cid: strategy.diagnose_channel(cid, [peer for peer in channel_ids if peer != cid]) for cid in channel_ids}
        result = strategy.assemble_blueprint(old["niche"], benchmark, diagnoses)
        result["generated_on"] = generated_on
        return result
    if kind == "UNIFIED_PLAN":
        return orchestrator.build_plan(old["channel_id"], old["opportunity_id"], generated_on=generated_on)
    if kind == "CAPABILITY_REGISTRY":
        return orchestrator.build_capability_registry(generated_on=generated_on)
    if kind == "EDITING_AVAILABILITY":
        with planner.connect_ro() as conn:
            return editing.build_availability_matrix(conn, ROOT, generated_on)
    raise ValueError(f"no safe builder for {kind}")


def _dry_run(plan):
    runnable = _sort_records([row for row in plan["artifacts_to_refresh"] if row["ARTIFACT_TYPE"] in REFRESHABLE])
    return {
        "WHAT_WOULD_RUN": [row["ARTIFACT_TYPE"] for row in runnable],
        "WHY": {row["PATH"]: row["STALE_REASON"] for row in runnable},
        "INPUT_ARTIFACTS": sorted({dep["ref"] for row in runnable for dep in row["SOURCE_DEPENDENCIES"]}),
        "OUTPUT_ARTIFACTS": [row["PATH"] for row in runnable],
        "WHAT_WOULD_REMAIN_UNCHANGED": [row["PATH"] for row in plan["artifacts_unchanged"]],
    }


def _sort_records(records):
    layer_index = {kind: min(planner.RUN_ORDER.index(layer) for layer in layers) for kind, layers in planner.ARTIFACT_LAYER.items()}
    return sorted(records, key=lambda row: (layer_index.get(row["ARTIFACT_TYPE"], len(planner.RUN_ORDER)), row["PATH"]))


def _db_state():
    db_path = planner.DB_PATH
    digest = hashlib.sha256(db_path.read_bytes()).hexdigest()
    with planner.connect_ro() as conn:
        integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        foreign_keys = len(conn.execute("PRAGMA foreign_key_check").fetchall())
        classifications = conn.execute("SELECT COUNT(*) FROM content_classifications").fetchone()[0]
    return {"sha256": digest, "integrity_check": integrity, "foreign_key_violations": foreign_keys, "content_classifications": classifications}


def execute(plan, run_id=None, generated_on=None):
    generated_on = generated_on or datetime.now(timezone.utc).date().isoformat()
    run_id = run_id or "REFRESH-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    before_db = _db_state()
    refreshed, unchanged, conclusions, confidence, blocked = [], [], [], [], list(plan.get("blocked_layers", []))
    records = _sort_records(plan["artifacts_to_refresh"])
    for record in records:
        if record["ARTIFACT_TYPE"] not in REFRESHABLE:
            blocked.append(f"NO_SAFE_BUILDER:{record['ARTIFACT_TYPE']}:{record['PATH']}")
            continue
        old = _current_payload(record)
        new = rebuild_payload(record, generated_on)
        if semantic_equal(old, new):
            unchanged.append(record["PATH"])
            continue
        successor = write_successor(_path(record["PATH"]), new, run_id)
        refreshed.append({"previous": record["PATH"], "successor": _relative(successor)})
        if record["ARTIFACT_TYPE"] == "CHANNEL_STRATEGY":
            changes = planner.action_changes(old, new)
            conclusions.extend(changes)
            confidence.extend(row["CONFIDENCE_CHANGE"] for row in changes)
        elif record["ARTIFACT_TYPE"] == "CROSS_NICHE_CALIBRATION":
            changes = planner.heuristic_changes(old, new)
            conclusions.extend(changes)
            confidence.extend(row["CONFIDENCE_CHANGE"] for row in changes)
        elif record["ARTIFACT_TYPE"] == "BLUEPRINT":
            conclusions.extend(planner.blueprint_changes(old, new))
    after_db = _db_state()
    if before_db != after_db:
        raise RuntimeError("canonical DB changed during refresh")
    report = build_run_report(
        run_id=run_id,
        trigger=plan.get("trigger_changes", []) or ([{"change_type": "CONTROLLED_REPLAY"}] if plan.get("replay") else []),
        affected_channels=sorted({channel for row in records for channel in row["CHANNEL_IDS"]}),
        upstream_changes=sorted({reason for row in records for reason in row.get("STALE_REASON", [])}),
        refreshed=refreshed,
        unchanged=unchanged,
        conclusion_changes=conclusions,
        confidence_changes=confidence,
        blocked_layers=sorted(set(blocked)),
        test_result="SEMANTIC_REPLAY_PASS" if plan.get("replay") and not refreshed else "NOT_RUN",
        db_integrity=after_db,
        git_base_commit=planner.git_head(),
    )
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = RUNS_DIR / f"{run_id}.json"
    if report_path.exists():
        raise FileExistsError(f"refresh run already exists: {report_path}")
    report_path.write_text(_render(report), encoding="utf-8")
    if refreshed:
        registry = planner.build_freshness_registry(generated_at=f"{generated_on}T00:00:00Z")
        planner.REGISTRY_PATH.write_text(_render(registry), encoding="utf-8")
    return report_path, report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan")
    parser.add_argument("--channel")
    parser.add_argument("--simulate-change", action="append", choices=planner.CHANGE_CATEGORIES)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--run-id")
    args = parser.parse_args(argv)
    if args.plan:
        plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    else:
        registry = json.loads(planner.REGISTRY_PATH.read_text(encoding="utf-8"))
        changes = [{"change_type": value, "channel_id": args.channel} for value in args.simulate_change or []]
        plan = planner.build_refresh_plan(registry, channel=args.channel, simulated_changes=changes, replay=args.replay)
    if args.dry_run:
        print(json.dumps(_dry_run(plan), indent=2, sort_keys=True))
        return 0
    if plan["status"] == "NO_REFRESH_REQUIRED":
        print(json.dumps({"status": "NO_REFRESH_REQUIRED"}, sort_keys=True))
        return 0
    path, report = execute(plan, run_id=args.run_id)
    print(json.dumps({"report": _relative(path), "result": report}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
