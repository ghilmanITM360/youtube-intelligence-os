#!/usr/bin/env python3
"""Register the five-item Phase 2 topic/format classification pilot."""
import argparse
import sqlite3
from pathlib import Path

import inventory_catalog as ic


TOPIC_VOCABULARY = frozenset({"CARDIOVASCULAR_HEALTH", "SCIENCE_HYPOTHETICALS"})
FORMAT_VOCABULARY = frozenset({"SHORT_FORM", "LONG_FORM"})
SHORT_FORM_MAX_SECONDS = 180
FORMAT_METHOD_VERSION = "duration-seconds-v1"

PILOT_ITEMS = (
    {"video_id": "VID-000179", "youtube_video_id": "tVl_NA5oEZI", "dataset_id": "DS-000006",
     "video_snapshot_id": "VS-000179", "topic": "CARDIOVASCULAR_HEALTH"},
    {"video_id": "VID-000189", "youtube_video_id": "nVK3T1g7F28", "dataset_id": "DS-000006",
     "video_snapshot_id": "VS-000189", "topic": "CARDIOVASCULAR_HEALTH"},
    {"video_id": "VID-000211", "youtube_video_id": "mEUqVgGf4e0", "dataset_id": "DS-000017",
     "video_snapshot_id": "VS-000211", "topic": "SCIENCE_HYPOTHETICALS"},
    {"video_id": "VID-000221", "youtube_video_id": "rGZ6TsXvi8E", "dataset_id": "DS-000017",
     "video_snapshot_id": "VS-000221", "topic": "SCIENCE_HYPOTHETICALS"},
    {"video_id": "VID-000231", "youtube_video_id": "4ZVtHknKuvg", "dataset_id": "DS-000017",
     "video_snapshot_id": "VS-000231", "topic": "SCIENCE_HYPOTHETICALS"},
)


def _verified_evidence(conn, item):
    rows = conn.execute(
        "SELECT vs.title,vs.description,vs.duration_seconds,t.archive_member_file_id,"
        "t.transcript_sha256,t.canonical_reference,tf.sha256 AS transcript_file_sha256,"
        "tf.canonical_path AS transcript_path,tf.verification_status AS transcript_verification,"
        "fp.source_file_id AS metadata_file_id,fp.source_locator AS duration_locator,"
        "fp.value_origin AS duration_origin,mf.sha256 AS metadata_sha256,"
        "mf.canonical_path AS metadata_path,mf.verification_status AS metadata_verification "
        "FROM videos v JOIN video_snapshots vs ON vs.video_id=v.video_id "
        "JOIN transcripts t ON t.video_id=v.video_id AND t.dataset_id=vs.dataset_id "
        "JOIN source_files tf ON tf.file_id=t.archive_member_file_id "
        "JOIN field_provenance fp ON fp.video_snapshot_id=vs.video_snapshot_id "
        "AND fp.field_name='duration_seconds' "
        "JOIN source_files mf ON mf.file_id=fp.source_file_id "
        "WHERE v.video_id=? AND v.youtube_video_id=? AND vs.dataset_id=? "
        "AND vs.video_snapshot_id=? AND t.availability_status='AVAILABLE'",
        (item["video_id"], item["youtube_video_id"], item["dataset_id"], item["video_snapshot_id"]),
    ).fetchall()
    if len(rows) != 1:
        raise ic.CatalogError("AmbiguousIdentity", "Pilot item must resolve to one available transcript and snapshot")
    row = rows[0]
    if not row["title"] or not row["description"] or row["duration_seconds"] is None:
        raise ic.CatalogError("SourceNotFound", "Pilot item lacks title, description, or duration evidence")
    if (
        not row["canonical_reference"]
        or row["transcript_sha256"] != row["transcript_file_sha256"]
        or row["transcript_verification"] != "VERIFIED"
        or row["metadata_verification"] != "VERIFIED"
        or row["duration_origin"] != "SOURCE_EXTRACTED"
    ):
        raise ic.CatalogError("HashFailure", "Pilot provenance is incomplete or unverified")
    for path_key, hash_key in (("transcript_path", "transcript_file_sha256"),
                               ("metadata_path", "metadata_sha256")):
        path = Path(row[path_key]) if row[path_key] else None
        if not path or not path.is_file() or ic.sha256_file(path) != row[hash_key]:
            raise ic.CatalogError("HashFailure", "Pilot source file failed existence/hash verification")
    return row


def _insert_exact(conn, values):
    columns = (
        "classification_id", "video_id", "dataset_id", "source_file_id",
        "classification_dimension", "classification_value", "evidence_layer",
        "classification_status", "source_locator", "classification_method",
        "method_version", "reproducibility_status", "notes",
    )
    existing = conn.execute(
        "SELECT {} FROM content_classifications WHERE classification_id=?".format(",".join(columns)),
        (values[0],),
    ).fetchone()
    if existing:
        if tuple(existing) != values:
            raise ic.CatalogError("EvidenceConflict", "Existing pilot classification conflicts with the requested row")
        return False
    conflict = conn.execute(
        "SELECT classification_id FROM content_classifications "
        "WHERE video_id=? AND classification_dimension=? "
        "AND classification_status IN ('PROPOSED','VERIFIED')",
        (values[1], values[4]),
    ).fetchone()
    if conflict:
        raise ic.CatalogError("EvidenceConflict", "Pilot item already has an active classification for this dimension")
    conn.execute(
        "INSERT INTO content_classifications ({},created_at) VALUES ({},?)".format(
            ",".join(columns), ",".join("?" for _ in columns)
        ),
        values + (ic.now_iso(),),
    )
    return True


def classify_pilot(db_path=ic.DEFAULT_DB_PATH, items=PILOT_ITEMS):
    if not items or len(items) > 5 or len({item["video_id"] for item in items}) != len(items):
        raise ic.CatalogError("ManifestValidationFailure", "Pilot must contain one to five distinct content items")
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        if not ic._table_exists(conn, "content_classifications"):
            raise ic.CatalogError("SourceNotFound", "Schema v8 content_classifications is not initialized")
        created = 0
        with conn:
            for item in items:
                if item["topic"] not in TOPIC_VOCABULARY:
                    raise ic.CatalogError("ManifestValidationFailure", "Topic is outside the pilot vocabulary")
                evidence = _verified_evidence(conn, item)
                content_format = (
                    "SHORT_FORM" if evidence["duration_seconds"] <= SHORT_FORM_MAX_SECONDS else "LONG_FORM"
                )
                if content_format not in FORMAT_VOCABULARY:
                    raise ic.CatalogError("ManifestValidationFailure", "Format is outside the pilot vocabulary")
                prefix = "CC-PILOT-{}".format(item["video_id"].removeprefix("VID-"))
                created += _insert_exact(conn, (
                    prefix + "-TOPIC", item["video_id"], item["dataset_id"],
                    evidence["archive_member_file_id"], "CONTENT_TOPIC", item["topic"],
                    "AI_INTERPRETATION", "PROPOSED",
                    "video_snapshot:{}#title,description;source_file:{}#full_text".format(
                        item["video_snapshot_id"], evidence["archive_member_file_id"]
                    ),
                    "ai_assisted_title_description_transcript_review", None,
                    "NON_REPRODUCIBLE",
                    "Pilot interpretation; model/prompt execution was not preserved for exact reproduction.",
                ))
                created += _insert_exact(conn, (
                    prefix + "-FORMAT", item["video_id"], item["dataset_id"],
                    evidence["metadata_file_id"], "CONTENT_FORMAT", content_format,
                    "MEASURED_FACT", "VERIFIED", evidence["duration_locator"] + "#duration_seconds",
                    "duration_seconds_threshold", FORMAT_METHOD_VERSION, "REPRODUCIBLE",
                    "SHORT_FORM <= {} seconds; LONG_FORM > {} seconds; observed duration={} seconds.".format(
                        SHORT_FORM_MAX_SECONDS, SHORT_FORM_MAX_SECONDS, evidence["duration_seconds"]
                    ),
                ))
        ids = tuple(
            "CC-PILOT-{}-{}".format(item["video_id"].removeprefix("VID-"), dimension)
            for item in items for dimension in ("TOPIC", "FORMAT")
        )
        count = conn.execute(
            "SELECT COUNT(*) FROM content_classifications WHERE classification_id IN ({})".format(
                ",".join("?" for _ in ids)
            ), ids,
        ).fetchone()[0]
        return {"items": len(items), "created": created, "classifications": count}
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", default=str(ic.DEFAULT_DB_PATH))
    args = parser.parse_args()
    try:
        result = classify_pilot(args.db_path)
    except ic.CatalogError as exc:
        raise SystemExit("FAILED — {}: {}".format(exc.error_type, exc.message))
    print("CLASSIFIED — {items} items, {classifications} rows ({created} created)".format(**result))


if __name__ == "__main__":
    main()
