#!/usr/bin/env python3
"""Plan deterministic, downstream-only intelligence refreshes.

Reads canonical SQLite state and derived artifacts. Never writes files or DB rows.
"""
import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data/catalog/youtube_inventory.db"
INTELLIGENCE_DIR = ROOT / "data/intelligence"
REGISTRY_PATH = INTELLIGENCE_DIR / "system/intelligence-freshness-registry.json"

RUN_ORDER = [
    "CANONICAL", "CLASSIFICATION", "TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING",
    "SUCCESS_FAILURE", "PUBLIC_METRIC_TRAJECTORY", "CHANNEL_STRATEGY", "BENCHMARK",
    "TRAINING_KNOWLEDGE", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION",
    "BLUEPRINT", "UNIFIED_PLAN",
]

DEPENDENCIES = {
    "CANONICAL": [],
    "CLASSIFICATION": ["CANONICAL"],
    "TOPIC": ["CANONICAL", "CLASSIFICATION"],
    "PACKAGING": ["CANONICAL", "TOPIC"],
    "HOOK_SCRIPT": ["TOPIC", "PACKAGING"],
    "EDITING": ["PACKAGING", "HOOK_SCRIPT"],
    "SUCCESS_FAILURE": ["TOPIC"],
    "PUBLIC_METRIC_TRAJECTORY": ["CANONICAL"],
    "CHANNEL_STRATEGY": ["TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "SUCCESS_FAILURE"],
    "BENCHMARK": ["CHANNEL_STRATEGY"],
    "TRAINING_KNOWLEDGE": [],
    "TRAINING_CALIBRATION": ["CHANNEL_STRATEGY", "TRAINING_KNOWLEDGE"],
    "CROSS_NICHE_CALIBRATION": ["TRAINING_CALIBRATION"],
    "BLUEPRINT": ["BENCHMARK", "CROSS_NICHE_CALIBRATION"],
    "UNIFIED_PLAN": ["TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "CHANNEL_STRATEGY", "BLUEPRINT"],
}

CHANGE_CATEGORIES = [
    "NEW_DATASET", "NEW_CHANNEL", "NEW_VIDEO", "NEW_TRANSCRIPT", "TRANSCRIPT_RECOVERED",
    "NEW_PUBLIC_METRIC_SNAPSHOT", "NEW_THUMBNAIL_REFERENCE", "NEW_THUMBNAIL_BINARY",
    "NEW_FORENSIC_EVIDENCE", "NEW_CLASSIFICATION", "CLASSIFICATION_CORRECTION",
    "NEW_EXTERNAL_VALIDATION", "NEW_TRAINING_KNOWLEDGE", "NEW_FIRST_PARTY_ANALYTICS",
]

FIRST_PARTY_ANALYTICS_FIELDS = [
    "CTR", "IMPRESSIONS", "RETENTION", "AVD", "WATCH_TIME", "TRAFFIC_SOURCES",
    "NEW_CASUAL_REGULAR", "AUDIENCE_OVERLAP",
]

# Field-sensitive invalidation. Example: transcript text changes Topic transcript
# patterns but not visual Packaging, despite Packaging consuming other Topic fields.
CHANGE_IMPACTS = {
    "NEW_DATASET": ["CANONICAL"],
    "NEW_CHANNEL": ["CANONICAL", "TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_VIDEO": ["CANONICAL", "CLASSIFICATION", "TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_TRANSCRIPT": ["TOPIC", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "TRANSCRIPT_RECOVERED": ["TOPIC", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_PUBLIC_METRIC_SNAPSHOT": ["TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "PUBLIC_METRIC_TRAJECTORY", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_THUMBNAIL_REFERENCE": ["PACKAGING", "CHANNEL_STRATEGY", "BENCHMARK", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_THUMBNAIL_BINARY": ["PACKAGING", "CHANNEL_STRATEGY", "BENCHMARK", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_FORENSIC_EVIDENCE": ["EDITING", "CHANNEL_STRATEGY", "BENCHMARK", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_CLASSIFICATION": ["CLASSIFICATION", "TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "CLASSIFICATION_CORRECTION": ["CLASSIFICATION", "TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_EXTERNAL_VALIDATION": ["TOPIC", "CHANNEL_STRATEGY", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_TRAINING_KNOWLEDGE": ["TRAINING_KNOWLEDGE", "TRAINING_CALIBRATION", "CHANNEL_STRATEGY", "BENCHMARK", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
    "NEW_FIRST_PARTY_ANALYTICS": ["SUCCESS_FAILURE", "PUBLIC_METRIC_TRAJECTORY", "CHANNEL_STRATEGY", "BENCHMARK", "TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN"],
}

ARTIFACT_LAYER = {
    "TOPIC": {"TOPIC"},
    "PACKAGING": {"PACKAGING"},
    "HOOK_SCRIPT": {"HOOK_SCRIPT"},
    "EDITING": {"EDITING"},
    "CHANNEL_STRATEGY": {"SUCCESS_FAILURE", "CHANNEL_STRATEGY"},
    "BENCHMARK": {"BENCHMARK"},
    "TRAINING_KNOWLEDGE": {"TRAINING_KNOWLEDGE"},
    "CROSS_NICHE_CALIBRATION": {"TRAINING_CALIBRATION", "CROSS_NICHE_CALIBRATION"},
    "BLUEPRINT": {"BLUEPRINT"},
    "UNIFIED_PLAN": {"UNIFIED_PLAN"},
    "CAPABILITY_REGISTRY": {"UNIFIED_PLAN"},
    "CROSS_CHANNEL_COMPARISON": {"BENCHMARK"},
    "EDITING_AVAILABILITY": {"EDITING"},
}

REPLAYABLE_TYPES = {
    "TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "CHANNEL_STRATEGY", "BENCHMARK",
    "CROSS_NICHE_CALIBRATION", "BLUEPRINT", "UNIFIED_PLAN", "CAPABILITY_REGISTRY",
    "EDITING_AVAILABILITY",
}


def _hash_bytes(value):
    return hashlib.sha256(value).hexdigest()


def file_hash(path):
    return _hash_bytes(Path(path).read_bytes())


def stable_hash(value):
    return _hash_bytes(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str).encode())


def connect_ro(path=DB_PATH):
    path = Path(path).resolve()
    conn = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def git_head(root=ROOT):
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def affected_layers(change_type):
    if change_type not in CHANGE_IMPACTS:
        raise ValueError(f"unsupported change category: {change_type}")
    wanted = set(CHANGE_IMPACTS[change_type])
    return [layer for layer in RUN_ORDER if layer in wanted]


def _query_dependency(conn, channel_id, kind):
    queries = {
        "CANONICAL_VIDEO": (
            "SELECT v.video_id,v.youtube_video_id,v.channel_id,v.canonical_url,v.created_from_dataset_id "
            "FROM videos v WHERE v.channel_id=? ORDER BY v.video_id", (channel_id,)),
        "TRANSCRIPT": (
            "SELECT t.transcript_id,t.video_id,t.dataset_id,t.availability_status,t.caption_type,t.language,"
            "t.word_count,t.transcript_sha256,t.transcript_format,t.transcript_source,t.canonical_reference,t.timing_quality,"
            "sf.sha256 AS source_sha256 FROM transcripts t JOIN videos v ON v.video_id=t.video_id "
            "LEFT JOIN source_files sf ON sf.file_id=t.archive_member_file_id WHERE v.channel_id=? ORDER BY t.transcript_id", (channel_id,)),
        "PUBLIC_METRIC_SNAPSHOT": (
            "SELECT s.video_snapshot_id,s.video_id,s.dataset_id,s.observed_at,s.published_at,s.title,s.duration_seconds,"
            "s.views,s.likes,s.comments,s.views_per_day,s.engagement_rate,s.description_char_count,s.transcript_word_count,"
            "s.description,s.video_type FROM video_snapshots s JOIN videos v ON v.video_id=s.video_id "
            "WHERE v.channel_id=? ORDER BY s.video_id,s.observed_at,s.video_snapshot_id", (channel_id,)),
        "THUMBNAIL_REFERENCE": (
            "SELECT 'snapshot' source,s.video_id,s.observed_at,s.thumbnail_url FROM video_snapshots s JOIN videos v ON v.video_id=s.video_id "
            "WHERE v.channel_id=? AND s.thumbnail_url IS NOT NULL UNION ALL "
            "SELECT 'evidence',t.video_id,t.observed_at,t.thumbnail_url FROM thumbnail_evidence t JOIN videos v ON v.video_id=t.video_id "
            "WHERE v.channel_id=? ORDER BY 2,3,4", (channel_id, channel_id)),
        "CLASSIFICATION": (
            "SELECT c.classification_id,c.video_id,c.dataset_id,c.source_file_id,c.classification_dimension,c.classification_value,"
            "c.evidence_layer,c.classification_status,c.source_locator,c.classification_method,c.method_version,c.reproducibility_status "
            "FROM content_classifications c JOIN videos v ON v.video_id=c.video_id WHERE v.channel_id=? ORDER BY c.classification_id", (channel_id,)),
    }
    if kind == "FORENSIC_EVIDENCE":
        dataset_ids = [row[0] for row in conn.execute(
            "SELECT d.dataset_id FROM channel_dataset_links l JOIN datasets d ON d.dataset_id=l.dataset_id "
            "WHERE l.channel_id=? AND d.semantic_class='C' ORDER BY d.dataset_id", (channel_id,))]
        rows = [{"record_type": "DATASET", "dataset_id": dataset_id} for dataset_id in dataset_ids]
        if dataset_ids:
            marks = ",".join("?" for _ in dataset_ids)
            rows += [{"record_type": "SOURCE_FILE", **dict(row)} for row in conn.execute(
                f"SELECT dataset_id,file_id,sha256,size_bytes,processing_status FROM source_files WHERE dataset_id IN ({marks}) ORDER BY dataset_id,file_id",
                dataset_ids)]
            rows += [{"record_type": "VISUAL_ASSET", **dict(row)} for row in conn.execute(
                f"SELECT dataset_id,visual_asset_id,sha256,frame_sequence_id,frame_index,visual_state_cluster_id FROM visual_assets WHERE dataset_id IN ({marks}) ORDER BY dataset_id,visual_asset_id",
                dataset_ids)]
    elif kind == "TRAINING_KNOWLEDGE":
        rows = [dict(row) for row in conn.execute(
            "SELECT dataset_id,file_id,sha256,size_bytes,verification_status FROM source_files "
            "WHERE dataset_id IN ('DS-000011','DS-000018') ORDER BY dataset_id,file_id")]
    else:
        sql, params = queries[kind]
        rows = [dict(row) for row in conn.execute(sql, params)]
    return {
        "ref": f"canonical:{channel_id}:{kind}" if channel_id else f"canonical:GLOBAL:{kind}",
        "sha256": stable_hash(rows),
        "version_reference": {
            "row_count": len(rows),
            "first_id": next(iter(rows[0].values())) if rows else None,
            "last_id": next(iter(rows[-1].values())) if rows else None,
        },
    }


def _file_group_dependency(ref, paths):
    rows = [{"path": str(path.relative_to(ROOT)), "sha256": file_hash(path)} for path in sorted(set(paths)) if path.is_file()]
    return {"ref": ref, "sha256": stable_hash(rows), "version_reference": {"file_count": len(rows), "paths": [r["path"] for r in rows]}}


def canonical_dependency(conn, channel_id, kind):
    if kind == "THUMBNAIL_BINARY":
        dataset_ids = [row[0] for row in conn.execute(
            "SELECT dataset_id FROM channel_dataset_links WHERE channel_id=? UNION SELECT created_from_dataset_id FROM channels WHERE channel_id=?",
            (channel_id, channel_id))]
        paths = [path for dataset_id in dataset_ids for path in (ROOT / "data/manifests").glob(f"{dataset_id}-thumbnail-snapshot-*.json")]
        paths += list((INTELLIGENCE_DIR / "channels" / channel_id).glob("thumbnail-visual-annotations*.json"))
        return _file_group_dependency(f"files:{channel_id}:THUMBNAIL_BINARY", paths)
    if kind == "EXTERNAL_VALIDATION":
        paths = list((INTELLIGENCE_DIR / "channels" / channel_id).glob("*validation*.json"))
        paths += list((INTELLIGENCE_DIR / "channels" / channel_id).glob("*validation*.md"))
        return _file_group_dependency(f"files:{channel_id}:EXTERNAL_VALIDATION", paths)
    return _query_dependency(conn, channel_id, kind)


def _pick_current(paths):
    paths = list(paths)
    if not paths:
        return None
    non_pilot = sorted(path for path in paths if "pilot" not in path.name)
    return (non_pilot or sorted(paths))[-1]


def discover_current_artifacts(root=ROOT):
    base = Path(root) / "data/intelligence"
    paths = []
    patterns = {
        "topic-opportunity-intelligence*.json",
        "packaging-intelligence*.json",
        "hook-script-intelligence*.json",
        "editing-visual-intelligence*.json",
        "channel-strategy-diagnosis*.json",
    }
    for channel_dir in sorted((base / "channels").glob("CH-*")):
        for pattern in patterns:
            selected = _pick_current(channel_dir.glob(pattern))
            if selected:
                paths.append(selected)
    paths += sorted((base / "plans").glob("*-content-intelligence-v1*.json"))
    paths += sorted((base / "blueprints").glob("*.json"))
    paths += sorted((base / "cross-channel").glob("*-channel-strategy-benchmark-*.json"))
    paths += sorted((base / "cross-channel").glob("editing-intelligence-availability-*.json"))
    paths += sorted(path for path in (base / "system").glob("*.json") if path.name != REGISTRY_PATH.name)
    grouped = {}
    for path in set(paths):
        payload = _payload(path)
        identity = (
            artifact_type(path), tuple(artifact_channels(path, payload)), payload.get("schema_version"),
            payload.get("niche"), payload.get("opportunity_id"),
        )
        grouped.setdefault(identity, []).append(path)
    return sorted(_pick_current(group) for group in grouped.values())


def artifact_type(path):
    name = Path(path).name
    if "topic-opportunity-intelligence" in name:
        return "TOPIC"
    if "packaging-intelligence" in name:
        return "PACKAGING"
    if "hook-script-intelligence" in name:
        return "HOOK_SCRIPT"
    if "editing-visual-intelligence" in name:
        return "EDITING"
    if "channel-strategy-diagnosis" in name:
        return "CHANNEL_STRATEGY"
    if "channel-strategy-benchmark" in name:
        return "BENCHMARK"
    if "strategy-blueprint" in name:
        return "BLUEPRINT"
    if "content-intelligence-v1" in name:
        return "UNIFIED_PLAN"
    if "strategy-training-knowledge" in name:
        return "TRAINING_KNOWLEDGE"
    if "cross-niche-strategy-calibration" in name:
        return "CROSS_NICHE_CALIBRATION"
    if "capabilities" in name:
        return "CAPABILITY_REGISTRY"
    if "editing-intelligence-availability" in name:
        return "EDITING_AVAILABILITY"
    return "CROSS_CHANNEL_COMPARISON"


def _payload(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def artifact_channels(path, payload=None):
    payload = payload or _payload(path)
    found = set(re.findall(r"CH-\d{6}", str(Path(path))))
    for key in ("channel_id", "channel_ids", "benchmark_channels"):
        value = payload.get(key)
        if isinstance(value, str):
            found.update(re.findall(r"CH-\d{6}", value))
        elif isinstance(value, list):
            found.update(re.findall(r"CH-\d{6}", json.dumps(value)))
    found.update(re.findall(r"CH-\d{6}", json.dumps(payload.get("channel", {}))))
    found.update(re.findall(r"CH-\d{6}", json.dumps(payload.get("channels", []))))
    found.update(re.findall(r"CH-\d{6}", json.dumps(payload.get("target_channel", {}))))
    found.update(re.findall(r"CH-\d{6}", json.dumps(payload.get("niches", {}))))
    return sorted(found)


def _artifact_dep(path):
    return {"ref": f"artifact:{path.relative_to(ROOT)}", "sha256": file_hash(path), "version_reference": _payload(path).get("schema_version")}


def _code_dep(filename):
    path = ROOT / "scripts" / filename
    return {"ref": f"code:scripts/{filename}", "sha256": file_hash(path), "version_reference": None}


def _current_for(channel_id, kind, paths):
    return _pick_current(path for path in paths if artifact_type(path) == kind and channel_id in artifact_channels(path))


def source_dependencies(path, conn, all_paths):
    kind = artifact_type(path)
    payload = _payload(path)
    channels = artifact_channels(path, payload)
    deps = []

    def canonical(kinds):
        for channel_id in channels:
            for dependency_kind in kinds:
                deps.append(canonical_dependency(conn, channel_id, dependency_kind))

    def upstream(kinds):
        for channel_id in channels:
            for upstream_kind in kinds:
                candidate = _current_for(channel_id, upstream_kind, all_paths)
                if candidate and candidate != path:
                    deps.append(_artifact_dep(candidate))

    if kind == "TOPIC":
        canonical(["CANONICAL_VIDEO", "TRANSCRIPT", "PUBLIC_METRIC_SNAPSHOT", "CLASSIFICATION", "EXTERNAL_VALIDATION"])
    elif kind == "PACKAGING":
        canonical(["CANONICAL_VIDEO", "PUBLIC_METRIC_SNAPSHOT", "THUMBNAIL_REFERENCE", "THUMBNAIL_BINARY"])
        upstream(["TOPIC"])
    elif kind == "HOOK_SCRIPT":
        canonical(["TRANSCRIPT", "PUBLIC_METRIC_SNAPSHOT"])
        upstream(["TOPIC", "PACKAGING"])
    elif kind == "EDITING":
        canonical(["FORENSIC_EVIDENCE"])
        upstream(["TOPIC", "PACKAGING", "HOOK_SCRIPT"])
    elif kind == "CHANNEL_STRATEGY":
        upstream(["TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING"])
        training = next((p for p in all_paths if artifact_type(p) == "TRAINING_KNOWLEDGE"), None)
        if training:
            deps.append(_artifact_dep(training))
    elif kind in ("BENCHMARK", "CROSS_CHANNEL_COMPARISON"):
        upstream(["TOPIC", "PACKAGING", "HOOK_SCRIPT", "CHANNEL_STRATEGY"])
    elif kind == "BLUEPRINT":
        upstream(["CHANNEL_STRATEGY", "BENCHMARK"])
    elif kind == "UNIFIED_PLAN":
        upstream(["TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "CHANNEL_STRATEGY", "BLUEPRINT"])
    elif kind == "TRAINING_KNOWLEDGE":
        deps.append(_query_dependency(conn, None, "TRAINING_KNOWLEDGE"))
    elif kind == "CROSS_NICHE_CALIBRATION":
        for candidate in all_paths:
            if artifact_type(candidate) in ("CHANNEL_STRATEGY", "TRAINING_KNOWLEDGE"):
                deps.append(_artifact_dep(candidate))
    elif kind in ("CAPABILITY_REGISTRY", "EDITING_AVAILABILITY"):
        for candidate in all_paths:
            if candidate != path and artifact_type(candidate) in ("TOPIC", "PACKAGING", "HOOK_SCRIPT", "EDITING", "UNIFIED_PLAN"):
                deps.append(_artifact_dep(candidate))
    generators = {
        "TOPIC": "report_topic_opportunity.py",
        "PACKAGING": "report_packaging_intelligence.py",
        "HOOK_SCRIPT": "report_hook_script_intelligence.py",
        "EDITING": "report_editing_visual_intelligence.py",
        "EDITING_AVAILABILITY": "report_editing_visual_intelligence.py",
        "CHANNEL_STRATEGY": "report_channel_strategy_intelligence.py",
        "BENCHMARK": "report_channel_strategy_intelligence.py",
        "TRAINING_KNOWLEDGE": "report_channel_strategy_intelligence.py",
        "CROSS_NICHE_CALIBRATION": "report_channel_strategy_intelligence.py",
        "BLUEPRINT": "report_channel_strategy_intelligence.py",
        "UNIFIED_PLAN": "run_youtube_intelligence.py",
        "CAPABILITY_REGISTRY": "run_youtube_intelligence.py",
    }
    if kind in generators:
        deps.append(_code_dep(generators[kind]))
    unique = {dep["ref"]: dep for dep in deps}
    return [unique[key] for key in sorted(unique)]


def _global_state(conn):
    channels = [dict(row) for row in conn.execute(
        "SELECT channel_id,youtube_channel_id,handle,display_name,created_from_dataset_id FROM channels ORDER BY channel_id")]
    datasets = [dict(row) for row in conn.execute(
        "SELECT dataset_id,dataset_name,semantic_class,source_type,status FROM datasets ORDER BY dataset_id")]
    return {
        "channels": {"sha256": stable_hash(channels), "ids": [row["channel_id"] for row in channels]},
        "datasets": {"sha256": stable_hash(datasets), "ids": [row["dataset_id"] for row in datasets]},
    }


def build_freshness_registry(root=ROOT, db_path=None, generated_at="2026-09-11T00:00:00Z", generated_from_commit=None):
    root = Path(root)
    paths = discover_current_artifacts(root)
    with connect_ro(db_path or root / "data/catalog/youtube_inventory.db") as conn:
        records = []
        for index, path in enumerate(paths, 1):
            payload = _payload(path)
            kind = artifact_type(path)
            records.append({
                "ARTIFACT_ID": f"INTEL-{index:04d}",
                "PATH": str(path.relative_to(root)),
                "ARTIFACT_TYPE": kind,
                "CHANNEL_IDS": artifact_channels(path, payload),
                "SOURCE_DEPENDENCIES": source_dependencies(path, conn, paths),
                "GENERATED_FROM_COMMIT": generated_from_commit or git_head(root),
                "GENERATED_AT": payload.get("generated_on") or generated_at,
                "CURRENT_STATUS": "CURRENT",
                "STALE_REASON": None,
                "RECOMMENDED_REFRESH": sorted(ARTIFACT_LAYER.get(kind, {kind}), key=RUN_ORDER.index),
                "ARTIFACT_SHA256": file_hash(path),
            })
        state = _global_state(conn)
    return {
        "schema_version": "intelligence-freshness-registry-1",
        "generated_at": generated_at,
        "generated_from_commit": generated_from_commit or git_head(root),
        "invalidation_basis": "CANONICAL_IDS_HASHES_AND_UPSTREAM_ARTIFACT_HASHES_NOT_MTIME",
        "dependency_graph": DEPENDENCIES,
        "supported_change_categories": CHANGE_CATEGORIES,
        "status_taxonomy": ["CURRENT", "STALE", "PARTIALLY_STALE", "BLOCKED", "UNKNOWN"],
        "first_party_analytics_future_seam": FIRST_PARTY_ANALYTICS_FIELDS,
        "canonical_state": state,
        "historical_artifacts_excluded": sorted(
            str(path.relative_to(root)) for path in (root / "data/intelligence/cross-channel").glob("*.json")
            if path not in paths
        ),
        "artifacts": records,
    }


def resolve_dependency(dep, conn):
    ref = dep["ref"]
    if ref.startswith("artifact:"):
        path = ROOT / ref.split(":", 1)[1]
        return _artifact_dep(path) if path.is_file() else {"ref": ref, "sha256": None, "version_reference": None}
    if ref.startswith("canonical:"):
        _, channel_id, kind = ref.split(":", 2)
        return _query_dependency(conn, None if channel_id == "GLOBAL" else channel_id, kind)
    if ref.startswith("files:"):
        _, channel_id, kind = ref.split(":", 2)
        return canonical_dependency(conn, channel_id, kind)
    if ref.startswith("code:"):
        path = ROOT / ref.split(":", 1)[1]
        return {"ref": ref, "sha256": file_hash(path) if path.is_file() else None, "version_reference": None}
    raise ValueError(f"unknown dependency ref: {ref}")


def _reason_from_ref(ref):
    names = {
        "TRANSCRIPT": "NEW_TRANSCRIPT_EVIDENCE",
        "PUBLIC_METRIC_SNAPSHOT": "NEW_PUBLIC_METRIC_SNAPSHOT",
        "THUMBNAIL_REFERENCE": "NEW_THUMBNAIL_REFERENCE",
        "THUMBNAIL_BINARY": "NEW_THUMBNAIL_BINARY",
        "FORENSIC_EVIDENCE": "NEW_FORENSIC_EVIDENCE",
        "CLASSIFICATION": "CLASSIFICATION_CHANGED",
        "EXTERNAL_VALIDATION": "NEW_EXTERNAL_VALIDATION",
        "CANONICAL_VIDEO": "CANONICAL_VIDEO_CHANGED",
        "TRAINING_KNOWLEDGE": "NEW_TRAINING_KNOWLEDGE",
    }
    return next((reason for key, reason in names.items() if key in ref), "UPSTREAM_ARTIFACT_CHANGED")


def _matches_layers(record, layers):
    return bool(ARTIFACT_LAYER.get(record["ARTIFACT_TYPE"], {record["ARTIFACT_TYPE"]}) & set(layers))


def _since_commit_changes(since_commit, root=ROOT):
    names = subprocess.check_output(["git", "diff", "--name-only", f"{since_commit}..HEAD"], cwd=root, text=True).splitlines()
    changes = []
    for name in names:
        channel = next(iter(re.findall(r"CH-\d{6}", name)), None)
        if name.startswith("data/manifests/classifications/"):
            change = "NEW_CLASSIFICATION"
        elif "thumbnail" in name:
            change = "NEW_THUMBNAIL_BINARY"
        elif name.startswith("data/manifests/"):
            change = "NEW_DATASET"
        elif "training" in name:
            change = "NEW_TRAINING_KNOWLEDGE"
        else:
            continue
        changes.append({"change_type": change, "channel_id": channel, "source_path": name})
    return changes


def build_refresh_plan(registry, root=ROOT, db_path=None, channel=None, simulated_changes=None, replay=False, since_commit=None):
    root = Path(root)
    records = registry.get("artifacts", [])
    changes = list(simulated_changes or [])
    if since_commit:
        changes.extend(_since_commit_changes(since_commit, root))
    stale = {}
    with connect_ro(db_path or root / "data/catalog/youtube_inventory.db") as conn:
        current_state = _global_state(conn)
        snapshot_rows = conn.execute(
            "SELECT v.channel_id,COUNT(DISTINCT s.observed_at) snapshots FROM videos v "
            "JOIN video_snapshots s ON s.video_id=v.video_id GROUP BY v.channel_id ORDER BY v.channel_id").fetchall()
        longitudinal = {
            row["channel_id"]: {
                "snapshot_count": row["snapshots"],
                "LONGITUDINAL_TREND": "AVAILABLE" if row["snapshots"] >= 2 else "NOT_AVAILABLE",
            }
            for row in snapshot_rows if not channel or row["channel_id"] == channel
        }
        if current_state["channels"]["sha256"] != registry["canonical_state"]["channels"]["sha256"]:
            changes.append({"change_type": "NEW_CHANNEL", "channel_id": None, "source": "CANONICAL_CHANNEL_SET_CHANGED"})
        if current_state["datasets"]["sha256"] != registry["canonical_state"]["datasets"]["sha256"]:
            changes.append({"change_type": "NEW_DATASET", "channel_id": None, "source": "CANONICAL_DATASET_SET_CHANGED"})
        for record in records:
            path = root / record["PATH"]
            reasons = []
            if not path.is_file():
                reasons.append("ARTIFACT_MISSING")
            elif file_hash(path) != record["ARTIFACT_SHA256"]:
                reasons.append("ARTIFACT_HASH_CHANGED")
            for dependency in record["SOURCE_DEPENDENCIES"]:
                current = resolve_dependency(dependency, conn)
                if current["sha256"] != dependency["sha256"]:
                    reasons.append(_reason_from_ref(dependency["ref"]))
            if reasons:
                stale[record["PATH"]] = sorted(set(reasons))

    selected_changes = [change for change in changes if not channel or change.get("channel_id") in (None, channel)]
    impacted = set()
    for change in selected_changes:
        impacted.update(affected_layers(change["change_type"]))
    selected = []
    unchanged = []
    for record in records:
        channel_match = not channel or channel in record["CHANNEL_IDS"] or not record["CHANNEL_IDS"]
        replay_match = replay and (not channel or channel in record["CHANNEL_IDS"]) and record["ARTIFACT_TYPE"] in REPLAYABLE_TYPES
        change_match = channel_match and _matches_layers(record, impacted)
        stale_match = channel_match and record["PATH"] in stale
        if replay_match or change_match or stale_match:
            reasons = stale.get(record["PATH"], [])
            if replay_match:
                reasons = sorted(set(reasons + ["CONTROLLED_REPLAY"]))
            reasons += sorted({change["change_type"] for change in selected_changes if _matches_layers(record, affected_layers(change["change_type"]))})
            stale_status = "STALE" if any(reason in ("ARTIFACT_MISSING", "ARTIFACT_HASH_CHANGED") for reason in reasons) else "PARTIALLY_STALE"
            selected.append({**record, "CURRENT_STATUS": stale_status if stale_match else "CURRENT", "STALE_REASON": sorted(set(reasons))})
        else:
            unchanged.append(record)
    run_layers = sorted({layer for record in selected for layer in ARTIFACT_LAYER.get(record["ARTIFACT_TYPE"], {record["ARTIFACT_TYPE"]})}, key=RUN_ORDER.index)
    return {
        "schema_version": "intelligence-refresh-plan-1",
        "status": "REFRESH_REQUIRED" if selected else "NO_REFRESH_REQUIRED",
        "channel_filter": channel,
        "trigger_changes": selected_changes,
        "replay": replay,
        "layers_affected": [layer for layer in RUN_ORDER if layer in impacted or layer in run_layers],
        "run_order": run_layers,
        "artifacts_considered": len(records),
        "artifacts_to_refresh": selected,
        "artifacts_unchanged": unchanged,
        "artifacts_refreshed": [],
        "stale_artifacts": stale,
        "blocked_layers": ["FIRST_PARTY_ANALYTICS_INGESTION_NOT_BUILT"] if any(c["change_type"] == "NEW_FIRST_PARTY_ANALYTICS" for c in selected_changes) else [],
        "longitudinal_status": longitudinal,
        "invariants": {
            "network_calls": 0,
            "canonical_db_mutations": 0,
            "raw_evidence_mutations": 0,
            "historical_artifact_overwrites": 0,
        },
    }


def heuristic_changes(old, new):
    key = lambda row: (row.get("rule_id"), row.get("archetype_kind"), row.get("archetype_id"))
    before = {key(row): row for row in old.get("heuristics", [])}
    changes = []
    for row in new.get("heuristics", []):
        previous = before.get(key(row))
        if previous and (previous.get("CROSS_NICHE_RESULT"), previous.get("CONFIDENCE")) != (row.get("CROSS_NICHE_RESULT"), row.get("CONFIDENCE")):
            old_evidence = previous.get("COUNTER_EVIDENCE", {})
            new_evidence = row.get("COUNTER_EVIDENCE", {})
            changes.append({
                "HEURISTIC": ":".join(filter(None, key(row))),
                "PREVIOUS_STATUS": previous.get("CROSS_NICHE_RESULT"),
                "NEW_STATUS": row.get("CROSS_NICHE_RESULT"),
                "SUPPORTING_NICHES": sorted(k.removesuffix("_RESULT") for k, value in row.items() if k.endswith("_RESULT") and k != "CROSS_NICHE_RESULT" and value in ("CORPUS_SUPPORTED", "CORPUS_PARTIALLY_SUPPORTED")),
                "SUPPORTING_CHANNELS": sorted({obs["channel_id"] for group in row.get("COUNTER_EVIDENCE", {}).values() for obs in group if obs.get("median_channel_relative", 0) >= 1}),
                "CONTRADICTING_CHANNELS": sorted({obs["channel_id"] for group in row.get("COUNTER_EVIDENCE", {}).values() for obs in group if obs.get("median_channel_relative", 1) < 1}),
                "SAMPLE_DEPTH": sum(obs.get("item_count", 0) for group in row.get("COUNTER_EVIDENCE", {}).values() for obs in group),
                "EVIDENCE_ADDED": new_evidence if new_evidence != old_evidence else {},
                "EVIDENCE_REMOVED": old_evidence if new_evidence != old_evidence else {},
                "WHY_CHANGED": row.get("reason", "RECALIBRATED_FROM_CURRENT_CORPUS"),
                "CONFIDENCE_CHANGE": {"from": previous.get("CONFIDENCE"), "to": row.get("CONFIDENCE")},
            })
    return changes


def action_changes(old, new):
    before = {row.get("TARGET"): row for row in old.get("actions", [])}
    changes = []
    for row in new.get("actions", []):
        previous = before.get(row.get("TARGET"))
        if previous and (previous.get("ACTION_TYPE"), previous.get("CONFIDENCE")) != (row.get("ACTION_TYPE"), row.get("CONFIDENCE")):
            changes.append({
                "TARGET": row.get("TARGET"), "OLD_ACTION": previous.get("ACTION_TYPE"), "NEW_ACTION": row.get("ACTION_TYPE"),
                "WHY_CHANGED": row.get("WHY"), "NEW_EVIDENCE": row.get("INTERNAL_EVIDENCE"),
                "EVIDENCE_ADDED": row.get("INTERNAL_EVIDENCE"),
                "EVIDENCE_REMOVED": previous.get("INTERNAL_EVIDENCE") if previous.get("INTERNAL_EVIDENCE") != row.get("INTERNAL_EVIDENCE") else None,
                "CONFIDENCE_CHANGE": {"from": previous.get("CONFIDENCE"), "to": row.get("CONFIDENCE")},
            })
    return changes


def blueprint_changes(old, new):
    fields = {
        "POSITIONING": "positioning", "PILLARS": "core_content_pillars", "ROBUST_PATTERNS": "robust_cross_channel_patterns",
        "NICHE_SPECIFIC_PATTERNS": "channel_specific_patterns_to_avoid_copying", "AVOID": "weak_or_conflicting_patterns",
        "UNDEREXPLOITED_GAPS": "underexploited_opportunities", "EXPERIMENT_CATEGORIES": "first_10_experiment_categories",
    }
    return [{
        "FIELD": label, "PREVIOUS_STATE": old.get(field), "NEW_STATE": new.get(field),
        "EVIDENCE_ADDED": new.get(field), "EVIDENCE_REMOVED": old.get(field),
        "WHY_CHANGED": "UPSTREAM_EVIDENCE_CHANGED", "CONFIDENCE_CHANGE": "RECOMPUTED_FROM_CURRENT_EVIDENCE",
    }
            for label, field in fields.items() if old.get(field) != new.get(field)]


def summarize_plan(plan):
    return {
        "status": plan["status"],
        "channel_filter": plan["channel_filter"],
        "changes": plan["trigger_changes"],
        "run_order": plan["run_order"],
        "artifacts_considered": plan["artifacts_considered"],
        "artifacts_to_refresh": [{"path": row["PATH"], "type": row["ARTIFACT_TYPE"], "why": row["STALE_REASON"]} for row in plan["artifacts_to_refresh"]],
        "artifacts_skipped": len(plan["artifacts_unchanged"]),
        "blocked_layers": plan["blocked_layers"],
        "invariants": plan["invariants"],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel")
    parser.add_argument("--since-commit")
    parser.add_argument("--simulate-change", action="append", choices=CHANGE_CATEGORIES)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--registry", default=str(REGISTRY_PATH))
    parser.add_argument("--output", help="Write full machine plan; stdout remains concise.")
    parser.add_argument("--write-registry", action="store_true", help="Explicitly rebuild freshness baseline.")
    args = parser.parse_args(argv)
    if args.write_registry:
        registry = build_freshness_registry()
        REGISTRY_PATH.write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(REGISTRY_PATH)
        return 0
    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    simulations = [{"change_type": value, "channel_id": args.channel} for value in args.simulate_change or []]
    plan = build_refresh_plan(registry, channel=args.channel, simulated_changes=simulations, replay=args.replay, since_commit=args.since_commit)
    if args.output:
        Path(args.output).write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summarize_plan(plan), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
