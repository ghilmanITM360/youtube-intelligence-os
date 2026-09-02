#!/usr/bin/env python3
"""Register controlled CONTENT_TOPIC / CONTENT_FORMAT classification batches."""
import argparse
import json
import re
import sqlite3
from pathlib import Path

import inventory_catalog as ic


TOPIC_VOCABULARY = frozenset({
    "BUSINESS_ECONOMICS",
    "CARDIOVASCULAR_HEALTH",
    "HEALTHY_AGING",
    "METABOLIC_HEALTH",
    "PERSONAL_FINANCE",
    "RETIREMENT_PLANNING",
    "SCIENCE_HYPOTHETICALS",
    "STEM_EXPLANATIONS",
})
FORMAT_VOCABULARY = frozenset({"SHORT_FORM", "LONG_FORM"})
SHORT_FORM_MAX_SECONDS = 180
FORMAT_METHOD_VERSION = "duration-seconds-v1"
BATCH_ID_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9-]*$")

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

EVIDENCE_SELECT = (
    "SELECT v.video_id,v.youtube_video_id,v.channel_id,c.handle,vs.dataset_id,"
    "vs.video_snapshot_id,vs.observed_at,vs.title,vs.description,vs.duration_seconds,"
    "t.archive_member_file_id,t.transcript_sha256,t.canonical_reference,"
    "tf.sha256 AS transcript_file_sha256,tf.canonical_path AS transcript_path,"
    "tf.verification_status AS transcript_verification,fp.source_file_id AS metadata_file_id,"
    "fp.source_locator AS duration_locator,fp.value_origin AS duration_origin,"
    "mf.sha256 AS metadata_sha256,mf.canonical_path AS metadata_path,"
    "mf.verification_status AS metadata_verification "
    "FROM videos v JOIN channels c ON c.channel_id=v.channel_id "
    "JOIN video_snapshots vs ON vs.video_id=v.video_id "
    "JOIN transcripts t ON t.video_id=v.video_id AND t.dataset_id=vs.dataset_id "
    "JOIN source_files tf ON tf.file_id=t.archive_member_file_id "
    "JOIN field_provenance fp ON fp.video_snapshot_id=vs.video_snapshot_id "
    "AND fp.field_name='duration_seconds' "
    "JOIN source_files mf ON mf.file_id=fp.source_file_id "
)


def _verified_evidence(conn, item, canonical=False):
    where = "WHERE v.video_id=? AND v.youtube_video_id=? AND t.availability_status='AVAILABLE' "
    params = [item["video_id"], item["youtube_video_id"]]
    if not canonical:
        where += "AND vs.dataset_id=? AND vs.video_snapshot_id=? "
        params.extend((item["dataset_id"], item["video_snapshot_id"]))
    rows = conn.execute(
        EVIDENCE_SELECT + where + "ORDER BY vs.observed_at DESC,vs.video_snapshot_id DESC",
        params,
    ).fetchall()
    if canonical and rows:
        rows = [row for row in rows if row["video_snapshot_id"] == rows[0]["video_snapshot_id"]]
    if len(rows) != 1:
        raise ic.CatalogError(
            "AmbiguousIdentity",
            "Content item must resolve to one canonical snapshot, available transcript, and duration source",
        )
    row = rows[0]
    if not row["title"] or not row["description"] or row["duration_seconds"] is None:
        raise ic.CatalogError("SourceNotFound", "Content item lacks title, description, or duration evidence")
    if (
        not row["canonical_reference"]
        or row["transcript_sha256"] != row["transcript_file_sha256"]
        or row["transcript_verification"] != "VERIFIED"
        or row["metadata_verification"] != "VERIFIED"
        or row["duration_origin"] != "SOURCE_EXTRACTED"
    ):
        raise ic.CatalogError("HashFailure", "Content provenance is incomplete or unverified")
    for path_key, hash_key in (("transcript_path", "transcript_file_sha256"),
                               ("metadata_path", "metadata_sha256")):
        path = Path(row[path_key]) if row[path_key] else None
        if not path or not path.is_file() or ic.sha256_file(path) != row[hash_key]:
            raise ic.CatalogError("HashFailure", "Content source file failed existence/hash verification")
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
            raise ic.CatalogError("EvidenceConflict", "Existing classification ID has different values")
        return False
    conflict = conn.execute(
        "SELECT classification_id FROM content_classifications "
        "WHERE video_id=? AND classification_dimension=? "
        "AND classification_status IN ('PROPOSED','VERIFIED')",
        (values[1], values[4]),
    ).fetchone()
    if conflict:
        raise ic.CatalogError("EvidenceConflict", "Content item already has an active classification for this dimension")
    try:
        conn.execute(
            "INSERT INTO content_classifications ({},created_at) VALUES ({},?)".format(
                ",".join(columns), ",".join("?" for _ in columns)
            ),
            values + (ic.now_iso(),),
        )
    except sqlite3.IntegrityError as exc:
        raise ic.CatalogError("EvidenceConflict", "Classification violates duplicate/conflict protection") from exc
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


def load_batch_manifest(path):
    path = Path(path)
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ic.CatalogError("ManifestValidationFailure", "Could not read classification manifest") from exc
    if not isinstance(manifest, dict) or not isinstance(manifest.get("items"), list):
        raise ic.CatalogError("ManifestValidationFailure", "Classification manifest must contain an items list")
    return manifest.get("batch_id"), manifest["items"]


def _validate_batch(batch_id, items, batch_size):
    if not isinstance(batch_size, int) or isinstance(batch_size, bool) or batch_size < 1:
        raise ic.CatalogError("ManifestValidationFailure", "Batch size must be a positive integer")
    if not isinstance(batch_id, str) or not BATCH_ID_PATTERN.fullmatch(batch_id):
        raise ic.CatalogError("ManifestValidationFailure", "Batch ID must contain only A-Z, 0-9, and hyphens")
    if not items:
        raise ic.CatalogError("ManifestValidationFailure", "Classification batch must contain items")
    seen_video_ids = set()
    seen_youtube_ids = set()
    for item in items:
        if not isinstance(item, dict) or any(not item.get(key) for key in ("video_id", "youtube_video_id", "topic")):
            raise ic.CatalogError("ManifestValidationFailure", "Each item requires video_id, youtube_video_id, and topic")
        if item["topic"] not in TOPIC_VOCABULARY:
            raise ic.CatalogError("ManifestValidationFailure", "Topic is outside the controlled vocabulary")
        if item["video_id"] in seen_video_ids or item["youtube_video_id"] in seen_youtube_ids:
            raise ic.CatalogError("ManifestValidationFailure", "Classification batch contains duplicate identities")
        seen_video_ids.add(item["video_id"])
        seen_youtube_ids.add(item["youtube_video_id"])


def _active_classifications(conn, video_id):
    rows = conn.execute(
        "SELECT classification_dimension,classification_value FROM content_classifications "
        "WHERE video_id=? AND classification_status IN ('PROPOSED','VERIFIED')",
        (video_id,),
    ).fetchall()
    active = {}
    for row in rows:
        if row["classification_dimension"] in active:
            raise ic.CatalogError("EvidenceConflict", "Content item has duplicate active classifications")
        active[row["classification_dimension"]] = row["classification_value"]
    return active


def _select_batch(conn, items, batch_size):
    selected = []
    for item in items[:batch_size]:
        evidence = _verified_evidence(conn, item, canonical=True)
        content_format = "SHORT_FORM" if evidence["duration_seconds"] <= SHORT_FORM_MAX_SECONDS else "LONG_FORM"
        proposed = {"CONTENT_TOPIC": item["topic"], "CONTENT_FORMAT": content_format}
        active = _active_classifications(conn, item["video_id"])
        for dimension, value in active.items():
            if dimension in proposed and proposed[dimension] != value:
                raise ic.CatalogError(
                    "EvidenceConflict", "Existing {} classification conflicts with the batch".format(dimension)
                )
        missing = tuple(dimension for dimension in ("CONTENT_TOPIC", "CONTENT_FORMAT") if dimension not in active)
        if not missing:
            continue
        selected.append({"item": item, "evidence": evidence, "values": proposed, "dimensions": missing})
    return selected


def _batch_values(batch_id, selected, dimension, assignment_source):
    item = selected["item"]
    evidence = selected["evidence"]
    value = selected["values"][dimension]
    prefix = "CC-{}-{}".format(batch_id, item["video_id"].removeprefix("VID-"))
    if dimension == "CONTENT_TOPIC":
        return (
            prefix + "-TOPIC", item["video_id"], evidence["dataset_id"],
            evidence["archive_member_file_id"], dimension, value,
            "AI_INTERPRETATION", "PROPOSED",
            "video_snapshot:{}#title,description;source_file:{}#full_text".format(
                evidence["video_snapshot_id"], evidence["archive_member_file_id"]
            ),
            "ai_assisted_title_description_transcript_review", None, "NON_REPRODUCIBLE",
            "Batch interpretation recorded in {}; model/prompt execution was not preserved for exact reproduction.".format(
                assignment_source or "an in-memory assignment"
            ),
        )
    return (
        prefix + "-FORMAT", item["video_id"], evidence["dataset_id"],
        evidence["metadata_file_id"], dimension, value,
        "MEASURED_FACT", "VERIFIED", evidence["duration_locator"] + "#duration_seconds",
        "duration_seconds_threshold", FORMAT_METHOD_VERSION, "REPRODUCIBLE",
        "SHORT_FORM <= {} seconds; LONG_FORM > {} seconds; observed duration={} seconds.".format(
            SHORT_FORM_MAX_SECONDS, SHORT_FORM_MAX_SECONDS, evidence["duration_seconds"]
        ),
    )


def classify_batch(db_path, items, batch_id, batch_size, dry_run=False, assignment_source=None):
    items = tuple(items)
    _validate_batch(batch_id, items, batch_size)
    db_path = Path(db_path).resolve()
    conn = sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True) if dry_run else sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        if not ic._table_exists(conn, "content_classifications"):
            raise ic.CatalogError("SourceNotFound", "Schema v8 content_classifications is not initialized")
        if not conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='index' "
            "AND name='uq_content_classifications_active_dimension'"
        ).fetchone():
            raise ic.CatalogError("SourceNotFound", "Schema v9 duplicate protection is not initialized")
        if not dry_run:
            conn.execute("BEGIN IMMEDIATE")
        selected = _select_batch(conn, items, batch_size)
        created = 0
        if not dry_run:
            for candidate in selected:
                for dimension in candidate["dimensions"]:
                    created += _insert_exact(
                        conn, _batch_values(batch_id, candidate, dimension, assignment_source)
                    )
            conn.commit()
        return {
            "dry_run": dry_run,
            "items": len(selected),
            "classifications": sum(len(candidate["dimensions"]) for candidate in selected),
            "created": created,
            "selected": tuple({
                "video_id": candidate["item"]["video_id"],
                "youtube_video_id": candidate["item"]["youtube_video_id"],
                "channel_id": candidate["evidence"]["channel_id"],
                "handle": candidate["evidence"]["handle"],
                "title": candidate["evidence"]["title"],
                "dimensions": tuple(
                    (dimension, candidate["values"][dimension]) for dimension in candidate["dimensions"]
                ),
            } for candidate in selected),
        }
    except Exception:
        if not dry_run:
            conn.rollback()
        raise
    finally:
        conn.close()


def _positive_int(value):
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", default=str(ic.DEFAULT_DB_PATH))
    parser.add_argument("--manifest", help="JSON batch manifest; omit to rerun the original five-item pilot")
    parser.add_argument("--batch-size", type=_positive_int, default=25)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if args.manifest:
            batch_id, items = load_batch_manifest(args.manifest)
            result = classify_batch(
                args.db_path, items, batch_id, args.batch_size,
                dry_run=args.dry_run, assignment_source=args.manifest,
            )
            print("{} — {} items, {} rows ({} created)".format(
                "DRY-RUN" if args.dry_run else "CLASSIFIED",
                result["items"], result["classifications"], result["created"],
            ))
            for item in result["selected"]:
                dimensions = ", ".join("{}={}".format(*pair) for pair in item["dimensions"])
                print("{} | {} | {} | {}".format(item["video_id"], item["handle"], dimensions, item["title"]))
        else:
            if args.dry_run:
                raise ic.CatalogError("ManifestValidationFailure", "Dry-run requires a batch manifest")
            result = classify_pilot(args.db_path)
            print("CLASSIFIED — {items} items, {classifications} rows ({created} created)".format(**result))
    except ic.CatalogError as exc:
        raise SystemExit("FAILED — {}: {}".format(exc.error_type, exc.message))


if __name__ == "__main__":
    main()
