#!/usr/bin/env python3
"""One-off loader: reads a subagent's per-image semantic-inspection JSON
(schema: {"dataset_id": "DS-...", "images": [{"path": ..., ...}, ...]}) and
inserts one visual_observations row (OBSERVATION layer) per image, plus a
single dataset-level entity_classifications row summarizing content_domain /
packaging_style, with editing_style left UNKNOWN (screenshots never support
an editing-style claim — Phase 1C content-domain-vs-editing-style rule).
Idempotent per discovered_file (skips an image already loaded).
"""
import json
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import inventory_catalog as ic  # noqa: E402


def main():
    if len(sys.argv) not in (2, 3):
        print("usage: load_semantic_results.py <json_file> [content_domain]", file=sys.stderr)
        sys.exit(2)
    data = json.loads(Path(sys.argv[1]).read_text())
    dataset_id = data["dataset_id"]
    content_domain = sys.argv[2] if len(sys.argv) == 3 else None

    conn = sqlite3.connect(str(ic.DEFAULT_DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON;")

    already = {
        r[0] for r in conn.execute(
            "SELECT df.absolute_path FROM visual_observations vo "
            "JOIN visual_assets va ON va.visual_asset_id = vo.visual_asset_id "
            "JOIN discovered_files df ON df.discovered_file_id = va.discovered_file_id "
            "WHERE vo.observation_type = 'SEMANTIC_INSPECTION' AND df.dataset_id = ?;",
            (dataset_id,),
        ).fetchall()
    }

    inserted = 0
    missing_asset = []
    packaging_notes = []
    with conn:
        for img in data["images"]:
            path = img["path"]
            if path in already:
                continue
            row = conn.execute(
                "SELECT va.visual_asset_id FROM discovered_files df "
                "JOIN visual_assets va ON va.discovered_file_id = df.discovered_file_id "
                "WHERE df.absolute_path = ? AND df.dataset_id = ?;",
                (path, dataset_id),
            ).fetchone()
            if not row:
                missing_asset.append(path)
                continue
            visual_asset_id = row[0]
            obs_id = ic._next_id(conn, "visual_observations", "visual_observation_id", "VOBS")
            conn.execute(
                "INSERT INTO visual_observations (visual_observation_id, visual_asset_id, observation_type, "
                "observation_method, source_surface, extracted_text, confidence, structured_json, "
                "evidence_layer, observed_at, notes) VALUES (?, ?, 'SEMANTIC_INSPECTION', ?, NULL, NULL, NULL, "
                "?, 'OBSERVATION', ?, NULL);",
                (obs_id, visual_asset_id, "claude_native_vision_inspection", json.dumps(img), ic.now_iso()),
            )
            inserted += 1
            if img.get("visual_packaging_pattern_notes"):
                packaging_notes.append(img["visual_packaging_pattern_notes"])

        ds_row = conn.execute("SELECT semantic_class FROM datasets WHERE dataset_id = ?;", (dataset_id,)).fetchone()
        semantic_count = conn.execute(
            "SELECT COUNT(*) FROM visual_observations vo "
            "JOIN visual_assets va ON va.visual_asset_id = vo.visual_asset_id "
            "WHERE va.dataset_id = ? AND vo.observation_type = 'SEMANTIC_INSPECTION';",
            (dataset_id,),
        ).fetchone()[0]
        existing_class = conn.execute(
            "SELECT 1 FROM entity_classifications WHERE dataset_id = ? AND target_type = 'DATASET';",
            (dataset_id,),
        ).fetchone()
        if not existing_class and ds_row:
            cls_id = ic._next_id(conn, "entity_classifications", "classification_id", "EC")
            packaging_summary = " | ".join(packaging_notes[:5]) if packaging_notes else None
            conn.execute(
                "INSERT INTO entity_classifications (classification_id, dataset_id, target_type, target_ref, "
                "content_domain, sub_niche, target_audience, content_format, packaging_style, thumbnail_style, "
                "presenter_style, editing_style, evidence_layer, source_locator, created_at, notes) "
                "VALUES (?, ?, 'DATASET', ?, ?, NULL, NULL, 'YOUTUBE_VIDEO', ?, NULL, NULL, 'UNKNOWN', "
                "'OBSERVATION', ?, ?, 'editing_style is UNKNOWN: only channel/video-page screenshots exist for "
                "this dataset, never actual video frames, so no editing-grammar evidence is available (Phase 1C "
                "content-domain-vs-editing-style rule).');",
                (cls_id, dataset_id, dataset_id, content_domain,
                 packaging_summary, "aggregated from {} screenshot semantic inspections".format(semantic_count), ic.now_iso()),
            )
    print("dataset={} inserted={} missing_asset={}".format(dataset_id, inserted, len(missing_asset)))
    if missing_asset:
        for p in missing_asset:
            print("  MISSING visual_asset for path:", p)


if __name__ == "__main__":
    main()
