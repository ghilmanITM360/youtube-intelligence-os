#!/usr/bin/env python3
"""Normalize validated What If forensic rows into local, reviewable staging."""
import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

from source_adapters.what_if_forensic_brain import TABLE_IDS, load_brain
from validate_what_if_source_contract import DEFAULT_CONTRACT, sha256

ROOT = Path(__file__).resolve().parents[1]
TRANSFORMATION_VERSION = "what-if-forensic-staging/1"
DEFAULT_OUTPUT = ROOT / "data/staging/what-if-forensic/v1.0.0"


class StagingError(ValueError):
    pass


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def catalog_identities(catalog_path):
    uri = Path(catalog_path).resolve().as_uri() + "?mode=ro"
    with closing(sqlite3.connect(uri, uri=True)) as connection:
        connection.execute("PRAGMA query_only=ON")
        rows = connection.execute(
            "SELECT youtube_video_id FROM videos WHERE channel_id = ? ORDER BY youtube_video_id",
            ("CH-000004",),
        ).fetchall()
    ids = {row[0] for row in rows}
    if len(ids) != len(rows):
        raise StagingError("duplicate What If catalog identity")
    return ids


def normalize(brain, catalog_ids):
    contract = brain["contract"]
    source_by_slug = {entry["forensic_slug"]: entry for entry in contract["sources"]}
    if len(source_by_slug) != len(contract["sources"]):
        raise StagingError("duplicate source slug")
    eligible = {}
    excluded = []
    for entry in contract["sources"]:
        youtube_id = entry["canonical_youtube_video_id"]
        if entry["mapping_status"] == "VERIFIED" and youtube_id in catalog_ids:
            eligible[entry["forensic_slug"]] = entry
        else:
            reason = "UNRESOLVED_IDENTITY" if not youtube_id else "NOT_REGISTERED_IN_CATALOG"
            excluded.append({"source_video_id": entry["source_video_id"],
                             "candidate_youtube_video_id": entry["candidate_youtube_video_id"],
                             "reason": reason})
    tables = {}
    excluded_rows = 0
    for table, local_id in TABLE_IDS.items():
        accepted = []
        for row_number, row in enumerate(brain["tables"][table], start=2):
            entry = eligible.get(row["VIDEO_SLUG"])
            if entry is None:
                excluded_rows += 1
                continue
            timing = {key: value for key, value in row.items()
                      if (key.endswith("_SEC") or key.endswith("_MS")) and value not in (None, "")}
            accepted.append({
                "canonical_youtube_video_id": entry["canonical_youtube_video_id"],
                "channel_id": "CH-000004",
                "source_release": contract["source_release"],
                "source_video_id": entry["source_video_id"],
                "forensic_slug": entry["forensic_slug"],
                "source_table": table,
                "source_row_id": row[local_id],
                "source_table_row_number": row_number,
                "observation_type": table.removeprefix("MASTER_"),
                "claim_kind": "SOURCE_DECLARED_FORENSIC_RECORD",
                "confidence": row.get("CONFIDENCE") or None,
                "timing": timing,
                "source_reference": f"production_intelligence_brain/01_master_data/{table}.csv#row={row_number}",
                "source_media_sha256": entry["sha256"],
                "transformation_version": TRANSFORMATION_VERSION,
                "source_fields": row,
            })
        tables[table] = accepted
    return tables, excluded, excluded_rows


def build_manifest(brain, catalog_ids, tables, excluded, excluded_rows, table_files):
    return {
        "schema_version": "1",
        "transformation_version": TRANSFORMATION_VERSION,
        "source_release": brain["contract"]["source_release"],
        "source_release_manifest_sha256": brain["contract"]["release_manifest_sha256"],
        "catalog_identity_sha256": hashlib.sha256(
            ("\n".join(sorted(catalog_ids)) + "\n").encode()).hexdigest(),
        "catalog_video_count": len(catalog_ids),
        "accepted_sources": len(brain["contract"]["sources"]) - len(excluded),
        "unresolved_sources": sum(e["reason"] == "UNRESOLVED_IDENTITY" for e in excluded),
        "not_registered_sources": sum(e["reason"] == "NOT_REGISTERED_IN_CATALOG" for e in excluded),
        "rejected_sources": 0,
        "accepted_rows": sum(len(rows) for rows in tables.values()),
        "excluded_rows": excluded_rows,
        "rejected_rows": 0,
        "excluded": excluded,
        "tables": table_files,
    }


def stage(brain, catalog_path, output):
    catalog_ids = catalog_identities(catalog_path)
    tables, excluded, excluded_rows = normalize(brain, catalog_ids)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".what-if-stage-", dir=output.parent) as temporary:
        temporary = Path(temporary)
        table_files = {}
        for table, rows in tables.items():
            filename = f"{table}.jsonl"
            path = temporary / filename
            path.write_text("".join(canonical_json(row) + "\n" for row in rows), encoding="utf-8")
            table_files[table] = {"file": filename, "rows": len(rows),
                                  "sha256": sha256(path), "size_bytes": path.stat().st_size}
        manifest = build_manifest(brain, catalog_ids, tables, excluded, excluded_rows, table_files)
        (temporary / "manifest.json").write_text(canonical_json(manifest) + "\n", encoding="utf-8")
        if output.exists():
            expected = {path.name: sha256(path) for path in temporary.iterdir()}
            actual = {path.name: sha256(path) for path in output.iterdir() if path.is_file()}
            if actual != expected:
                raise StagingError(canonical_json({
                    "status": "DIFF_REQUIRES_REVIEW", "expected": expected, "existing": actual,
                    "accepted_rows": manifest["accepted_rows"],
                    "excluded_rows": manifest["excluded_rows"]}))
            return {"status": "UNCHANGED", "manifest": manifest}
        os.replace(temporary, output)
        return {"status": "CREATED", "manifest": manifest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, default=os.environ.get("YIOS_WHAT_IF_CORPUS_ROOT"))
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--catalog", type=Path, default=ROOT / "data/catalog/youtube_inventory.db")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.corpus_root is None:
        parser.error("set YIOS_WHAT_IF_CORPUS_ROOT or pass --corpus-root")
    try:
        result = stage(load_brain(args.corpus_root, args.contract), args.catalog, args.output)
    except (StagingError, OSError, KeyError, ValueError, sqlite3.Error) as exc:
        parser.exit(1, f"staging failed: {exc}\n")
    manifest = result["manifest"]
    print(canonical_json({"status": result["status"], "accepted_sources": manifest["accepted_sources"],
                          "accepted_rows": manifest["accepted_rows"],
                          "unresolved_sources": manifest["unresolved_sources"],
                          "not_registered_sources": manifest["not_registered_sources"],
                          "rejected_rows": manifest["rejected_rows"],
                          "excluded_rows": manifest["excluded_rows"],
                          "table_rows": {key: value["rows"] for key, value in manifest["tables"].items()}}))


if __name__ == "__main__":
    main()
