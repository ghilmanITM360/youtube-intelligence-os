#!/usr/bin/env python3
"""Validate evidence, integrity, and control totals for YouTube channel registry."""

from __future__ import annotations

import argparse
import json
import sqlite3
import tempfile
from pathlib import Path

from scripts.build_youtube_channel_registry import build_database, build_model, connect_readonly


EXPECTED = {
    "canonical_channels": 70,
    "raw_submissions": 67,
    "target_channels": 63,
    "channels_with_video_data": 41,
    "identity_only_channels": 29,
    "standard_packages": 36,
    "historical_channels": 5,
    "stored_outside_targets": 7,
    "datasets": 26,
    "videos": 1939,
    "real_transcripts": 1928,
    "placeholders": 11,
    "description_gaps": 14,
    "non_channel_subjects": 7,
    "intelligence_coverage_rows": 560,
    "data_layer_rows": 770,
    "visual_coverage_rows": 70,
}

REQUIRED_VIEWS = {
    "v_channel_status",
    "v_completed_channels",
    "v_pending_channels",
    "v_channel_data_gaps",
    "v_original_target_progress",
    "v_added_target_progress",
    "v_dataset_summary",
    "v_video_transcript_status",
    "v_channel_artifacts",
    "v_intelligence_coverage",
}


def scalar(connection: sqlite3.Connection, sql: str) -> int:
    return connection.execute(sql).fetchone()[0]


def validate_database(root: Path, database: Path) -> dict:
    connection = connect_readonly(database)
    try:
        controls = {
            "canonical_channels": scalar(connection, "SELECT count(*) FROM channels"),
            "raw_submissions": scalar(connection, "SELECT count(*) FROM submissions"),
            "target_channels": scalar(connection, "SELECT count(*) FROM channels WHERE target_group<>'OUTSIDE_TARGET'"),
            "channels_with_video_data": scalar(connection, "SELECT count(DISTINCT canonical_channel_id) FROM videos"),
            "identity_only_channels": scalar(connection, "SELECT count(*) FROM channels WHERE source_group='IDENTITY_ONLY'"),
            "standard_packages": scalar(connection, "SELECT count(*) FROM channels WHERE source_group='STANDARD_PACKAGE'"),
            "historical_channels": scalar(connection, "SELECT count(*) FROM channels WHERE source_group='HISTORICAL_CATALOG'"),
            "stored_outside_targets": scalar(connection, "SELECT count(*) FROM channels WHERE target_group='OUTSIDE_TARGET' AND extraction_status<>'NOT_EXTRACTED'"),
            "datasets": scalar(connection, "SELECT count(*) FROM datasets"),
            "videos": scalar(connection, "SELECT count(*) FROM videos"),
            "real_transcripts": scalar(connection, "SELECT count(*) FROM transcripts WHERE is_placeholder=0"),
            "placeholders": scalar(connection, "SELECT count(*) FROM transcripts WHERE is_placeholder=1"),
            "description_gaps": scalar(connection, "SELECT count(*) FROM videos WHERE description IS NULL AND COALESCE(description_unavailable_reason,'') NOT LIKE 'Description verified present in historical coverage;%'"),
            "non_channel_subjects": scalar(connection, "SELECT count(*) FROM non_channel_subjects"),
            "intelligence_coverage_rows": scalar(connection, "SELECT count(*) FROM intelligence_coverage"),
            "data_layer_rows": scalar(connection, "SELECT count(*) FROM channel_data_layers"),
            "visual_coverage_rows": scalar(connection, "SELECT count(*) FROM visual_coverage"),
        }
        errors = [f"{key}: expected {expected}, found {controls[key]}" for key, expected in EXPECTED.items() if controls[key] != expected]
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            errors.append("PRAGMA integrity_check failed")
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        if foreign_keys:
            errors.append(f"PRAGMA foreign_key_check found {len(foreign_keys)} rows")
        views = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='view'")}
        missing_views = sorted(REQUIRED_VIEWS - views)
        if missing_views:
            errors.append("Missing views: " + ", ".join(missing_views))
        checks = {
            "duplicate_channel_ids": "SELECT count(*)-count(DISTINCT canonical_channel_id) FROM channels",
            "duplicate_video_ids": "SELECT count(*)-count(DISTINCT youtube_video_id) FROM videos",
            "identity_only_with_videos": "SELECT count(*) FROM channels c WHERE source_group='IDENTITY_ONLY' AND EXISTS (SELECT 1 FROM videos v WHERE v.canonical_channel_id=c.canonical_channel_id)",
            "identity_only_with_packages": "SELECT count(*) FROM channels WHERE source_group='IDENTITY_ONLY' AND package_status<>'NO_PACKAGE'",
            "generated_intelligence_without_evidence": "SELECT count(*) FROM intelligence_coverage WHERE generated_artifact_available=1 AND (evidence_path='' OR evidence_path IS NULL)",
            "generated_intelligence_marked_unavailable": "SELECT count(*) FROM intelligence_coverage WHERE generated_artifact_available=1 AND status IN ('DATA_READY','NOT_AVAILABLE','NOT_APPLICABLE')",
            "null_transcript_without_reason": "SELECT count(*) FROM transcripts WHERE transcript_text IS NULL AND unavailable_reason IS NULL",
            "forensic_channel_count": "SELECT count(*) FROM visual_coverage WHERE visual_evidence_level='FORENSIC_VIDEO_EVIDENCE'",
            "thumbnail_evidence_channel_count": "SELECT count(*) FROM visual_coverage WHERE visual_evidence_level IN ('THUMBNAIL_EVIDENCE','FORENSIC_VIDEO_EVIDENCE')",
            "title_only_historical_channel_count": "SELECT count(*) FROM channels WHERE source_group='HISTORICAL_CATALOG' AND thumbnail_metadata_status='NONE'",
            "first_party_ingested_count": "SELECT count(*) FROM channels WHERE first_party_analytics_status='INGESTED'",
        }
        expected_checks = {
            "duplicate_channel_ids": 0,
            "duplicate_video_ids": 0,
            "identity_only_with_videos": 0,
            "identity_only_with_packages": 0,
            "generated_intelligence_without_evidence": 0,
            "generated_intelligence_marked_unavailable": 0,
            "null_transcript_without_reason": 0,
            "forensic_channel_count": 1,
            "thumbnail_evidence_channel_count": 3,
            "title_only_historical_channel_count": 2,
            "first_party_ingested_count": 0,
        }
        check_results = {name: scalar(connection, sql) for name, sql in checks.items()}
        errors.extend(f"{name}: expected {expected_checks[name]}, found {value}" for name, value in check_results.items() if value != expected_checks[name])
        xkcd = connection.execute(
            "SELECT canonical_channel_id,keyframe_count,registered_source_video_count,timestamped_visual_observation_count FROM visual_coverage WHERE visual_evidence_level='FORENSIC_VIDEO_EVIDENCE'"
        ).fetchone()
        if xkcd != ("UC6IxnFzHofFJ5X2PycSMsww", 107, 3, 107):
            errors.append(f"Forensic channel mismatch: {xkcd}")
        xkcd_datasets = scalar(connection, "SELECT count(*) FROM dataset_channels WHERE canonical_channel_id='UC6IxnFzHofFJ5X2PycSMsww'")
        if xkcd_datasets != 5:
            errors.append(f"xkcd dataset relationships: expected 5, found {xkcd_datasets}")
        for evidence_path, in connection.execute(
            "SELECT evidence_path FROM intelligence_coverage WHERE generated_artifact_available=1 UNION SELECT evidence_path FROM channel_data_layers"
        ):
            local = evidence_path.split("::", 1)[0]
            if local.startswith("data/") or local.startswith("docs/"):
                if not (root / local).exists():
                    errors.append(f"Missing evidence path: {local}")
        return {"status": "PASS" if not errors else "FAIL", "controls": controls, "checks": check_results, "errors": errors}
    finally:
        connection.close()


def validate_idempotence(root: Path) -> dict:
    model = build_model(root)
    with tempfile.TemporaryDirectory() as directory:
        database = Path(directory) / "registry.db"
        first = build_database(root, database, model)
        second = build_database(root, database, model)
    return {"status": "PASS" if first == second else "FAIL", "first": first, "second": second}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--database", type=Path)
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
    database = args.database or root / "data/catalog/youtube_channel_registry.db"
    result = validate_database(root, database)
    result["idempotence"] = validate_idempotence(root)
    if result["idempotence"]["status"] != "PASS":
        result["status"] = "FAIL"
        result["errors"].append("Second build changed domain table counts")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
