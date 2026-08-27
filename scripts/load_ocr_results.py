#!/usr/bin/env python3
"""One-off loader: reads scripts/image_text_recognition.swift JSON output
files (one per discovered_file_id, named <id>.json) from a results
directory and inserts them into visual_observations as OCR-layer
EXTRACTED_FACT rows. Idempotent: skips a discovered_file_id that already
has an OCR observation.
"""
import json
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import inventory_catalog as ic  # noqa: E402


def main():
    if len(sys.argv) != 2:
        print("usage: load_ocr_results.py <results_dir>", file=sys.stderr)
        sys.exit(2)
    results_dir = Path(sys.argv[1])
    db_path = ic.DEFAULT_DB_PATH
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")

    already = {
        r[0] for r in conn.execute(
            "SELECT df.discovered_file_id FROM visual_observations vo "
            "JOIN visual_assets va ON va.visual_asset_id = vo.visual_asset_id "
            "JOIN discovered_files df ON df.discovered_file_id = va.discovered_file_id "
            "WHERE vo.observation_type = 'OCR';"
        ).fetchall()
    }

    inserted = 0
    skipped_dup = 0
    skipped_no_asset = 0
    with conn:
        for f in sorted(results_dir.glob("*.json")):
            discovered_file_id = f.stem
            if discovered_file_id in already:
                skipped_dup += 1
                continue
            row = conn.execute(
                "SELECT visual_asset_id FROM visual_assets WHERE discovered_file_id = ?;",
                (discovered_file_id,),
            ).fetchone()
            if not row:
                skipped_no_asset += 1
                continue
            visual_asset_id = row[0]
            data = json.loads(f.read_text())
            obs_id = ic._next_id(conn, "visual_observations", "visual_observation_id", "VOBS")
            conn.execute(
                "INSERT INTO visual_observations (visual_observation_id, visual_asset_id, observation_type, "
                "observation_method, source_surface, extracted_text, confidence, structured_json, "
                "evidence_layer, observed_at, notes) VALUES (?, ?, 'OCR', ?, NULL, ?, ?, ?, 'EXTRACTED_FACT', ?, NULL);",
                (obs_id, visual_asset_id, "apple_vision_VNRecognizeTextRequest_accurate",
                 data.get("fullText"), data.get("meanConfidence"), json.dumps(data.get("lines", [])),
                 ic.now_iso()),
            )
            inserted += 1
    print("Inserted {} OCR observations (skipped {} already-loaded, {} with no visual_asset).".format(
        inserted, skipped_dup, skipped_no_asset))


if __name__ == "__main__":
    main()
