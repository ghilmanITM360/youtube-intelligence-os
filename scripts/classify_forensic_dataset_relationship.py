#!/usr/bin/env python3
"""Record the proven DS-000012/DS-000015 same-source relationship."""
import argparse
import json
import sqlite3
from pathlib import Path

import inventory_catalog as ic


DEFAULT_MANIFEST = ic.REPO_ROOT / "data/manifests/relationships/DSREL-000001.json"
EXPECTED_DATASETS = ("DS-000012", "DS-000015")


def record_relationship(db_path=ic.DEFAULT_DB_PATH, manifest_path=DEFAULT_MANIFEST):
    manifest_path = Path(manifest_path)
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    relationships = payload.get("forensic_dataset_relationships", [])
    if len(relationships) != 1:
        raise ic.CatalogError("ManifestValidationFailure", "Expected exactly one forensic dataset relationship")
    relationship = relationships[0]
    if tuple(relationship.get("dataset_ids", [])) != EXPECTED_DATASETS:
        raise ic.CatalogError("AmbiguousIdentity", "Forensic dataset relationship IDs do not match the proven pair")
    if relationship.get("relationship_type") != "SAME_SOURCE_INDEPENDENT_ANALYSIS":
        raise ic.CatalogError("EvidenceConflict", "Unexpected forensic dataset relationship classification")

    links = {
        link.get("dataset_id"): link
        for link in payload.get("forensic_relationships", [])
        if link.get("dataset_id") in EXPECTED_DATASETS
    }
    if set(links) != set(EXPECTED_DATASETS) or any(
        link.get("status") != "PROVEN"
        or link.get("youtube_video_id") != relationship.get("youtube_video_id")
        or link.get("source_sha256") != relationship.get("source_sha256")
        for link in links.values()
    ):
        raise ic.CatalogError("AmbiguousIdentity", "The two proven source-identity links do not agree")

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        if not ic._table_exists(conn, "dataset_relationships"):
            raise ic.CatalogError("SourceNotFound", "Schema v7 dataset_relationships table is not initialized")
        datasets = conn.execute(
            "SELECT dataset_id FROM datasets WHERE dataset_id IN (?, ?) ORDER BY dataset_id",
            EXPECTED_DATASETS,
        ).fetchall()
        if tuple(row["dataset_id"] for row in datasets) != EXPECTED_DATASETS:
            raise ic.CatalogError("SourceNotFound", "Both forensic datasets must remain independently registered")

        reports = relationship.get("canonical_reports", [])
        if {report.get("dataset_id") for report in reports} != set(EXPECTED_DATASETS):
            raise ic.CatalogError("ManifestValidationFailure", "Canonical report evidence is incomplete")
        for report in reports:
            row = conn.execute(
                "SELECT canonical_path,sha256,verification_status FROM source_files "
                "WHERE dataset_id=? AND relative_path=?",
                (report["dataset_id"], report["relative_path"]),
            ).fetchone()
            if (
                not row
                or row["sha256"] != report.get("sha256")
                or row["verification_status"] != "VERIFIED"
                or not row["canonical_path"]
                or ic.sha256_file(ic.resolve_canonical_path(row["canonical_path"])) != report.get("sha256")
            ):
                raise ic.CatalogError("HashFailure", "Canonical report evidence failed verification")

        values = (
            relationship["relationship_id"], EXPECTED_DATASETS[0], EXPECTED_DATASETS[1],
            relationship["relationship_type"], relationship["confidence"], relationship["status"],
            relationship["evidence"], relationship["source_locator"], ic.now_iso(), relationship.get("notes"),
        )
        with conn:
            conn.execute(
                "INSERT OR IGNORE INTO dataset_relationships "
                "(relationship_id,from_dataset_id,to_dataset_id,relationship_type,confidence,status,evidence,"
                "source_locator,created_at,notes) VALUES (?,?,?,?,?,?,?,?,?,?)",
                values,
            )
        row = conn.execute(
            "SELECT * FROM dataset_relationships WHERE relationship_id=?", (relationship["relationship_id"],)
        ).fetchone()
        expected = values[:8] + values[9:]
        actual = tuple(row[key] for key in (
            "relationship_id", "from_dataset_id", "to_dataset_id", "relationship_type",
            "confidence", "status", "evidence", "source_locator", "notes",
        )) if row else None
        if actual != expected:
            raise ic.CatalogError("EvidenceConflict", "Existing dataset relationship conflicts with the proven record")
        return dict(row)
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", default=str(ic.DEFAULT_DB_PATH))
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    args = parser.parse_args()
    try:
        row = record_relationship(args.db_path, args.manifest)
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit("FAILED — ManifestValidationFailure: {}".format(type(exc).__name__))
    except ic.CatalogError as exc:
        raise SystemExit("FAILED — {}: {}".format(exc.error_type, exc.message))
    print("{} — {} {} {}".format(
        row["status"], row["from_dataset_id"], row["relationship_type"], row["to_dataset_id"]
    ))


if __name__ == "__main__":
    main()
