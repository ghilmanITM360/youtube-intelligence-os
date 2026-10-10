#!/usr/bin/env python3
"""Phase 1B structured source registration (Decisions 014, 015).

Turns a Phase 1A-ingested dataset's raw files into structured catalog
entities (channels, videos, snapshots, transcripts) with field-level
provenance. Stdlib only, aside from scripts/source_adapters/ which parses
DS-000001's specific workbook/archive shape.

Never analyzes competitor strategy, generates topics, or scores content —
see docs/Phases.md Phase 1B boundary. Reuses scripts/inventory_catalog.py
for hashing/id/time helpers and its CatalogError taxonomy rather than
duplicating them (`inventory_catalog.py` stays responsible for file/dataset
inventory; this script owns structured registration only — rule 35).
"""
import argparse
import sqlite3
import sys
import zipfile
from collections import Counter
from pathlib import Path

import inventory_catalog
from inventory_catalog import (
    CatalogError, DEFAULT_DB_PATH, now_iso, resolve_canonical_path, sha256_bytes, sha256_file,
)
from source_adapters import youtube_master_data as ymd

TOOL_VERSION = "register_structured_source.py/1"

# rule 47: only these fields get provenance rows — internal ids/timestamps don't.
CHANNEL_FIELDS = [("Channel ID", "youtube_channel_id"), ("Handle", "handle"), ("Channel Name", "display_name"), ("Channel URL", "channel_url")]
CHANNEL_SNAPSHOT_FIELDS = [("Subscribers", "subscriber_count"), ("Total Videos (YouTube)", "video_count")]
VIDEO_FIELDS = [("Video ID", "youtube_video_id"), ("Video URL", "canonical_url")]
VIDEO_SNAPSHOT_FIELDS = [
    ("Title", "title", "SOURCE_EXTRACTED"),
    ("Published (UTC)", "published_at", "SOURCE_EXTRACTED"),
    ("Sec", "duration_seconds", "SOURCE_EXTRACTED"),
    ("Views", "views", "SOURCE_EXTRACTED"),
    ("Likes", "likes", "SOURCE_EXTRACTED"),
    ("Comments", "comments", "SOURCE_EXTRACTED"),
    ("Views/Day", "views_per_day", "SOURCE_COMPUTED"),
    ("Engagement", "engagement_rate", "SOURCE_COMPUTED"),
    ("Desc Chars", "description_char_count", "SOURCE_EXTRACTED"),
    ("Transcript Words", "transcript_word_count", "SOURCE_EXTRACTED"),
]
TRANSCRIPT_HEADER_FIELDS = ["availability_status", "caption_type", "language", "word_count"]

BASE_PRODUCER_CONTRACT = {
    "channel_fields": {field for _label, field in CHANNEL_FIELDS},
    "channel_snapshot_fields": {field for _label, field in CHANNEL_SNAPSHOT_FIELDS},
    "video_fields": {field for _label, field in VIDEO_FIELDS},
    "video_snapshot_fields": {field for _label, field, _origin in VIDEO_SNAPSHOT_FIELDS},
    "transcript_fields": set(TRANSCRIPT_HEADER_FIELDS),
}

PRODUCER_CONTRACTS = {
    TOOL_VERSION: BASE_PRODUCER_CONTRACT,
    "apify_youtube_ingest.py/1": {
        **BASE_PRODUCER_CONTRACT,
        "video_snapshot_fields": {
            "title", "published_at", "duration_seconds", "views", "likes", "comments",
            "description", "description_char_count", "thumbnail_url", "video_type",
            "transcript_word_count",
        },
        "transcript_fields": {
            "availability_status", "caption_type", "language", "word_count",
            "canonical_reference", "format",
        },
    },
    "register_supplied_channel.py/1": {
        **BASE_PRODUCER_CONTRACT,
        "video_snapshot_fields": {
            "title", "published_at", "duration_seconds", "views", "likes", "comments",
            "description", "description_char_count", "thumbnail_url", "video_type",
            "transcript_word_count", "views_per_day", "engagement_rate",
        },
        "transcript_fields": {
            "availability_status", "caption_type", "language", "word_count",
            "canonical_reference", "timing_quality",
        },
    },
}

# V2 requires provenance for observed values and preserves absent optional observations.
PRODUCER_CONTRACTS["register_supplied_channel.py/2"] = {
    **PRODUCER_CONTRACTS["register_supplied_channel.py/1"],
    "nullable_video_snapshot_fields": PRODUCER_CONTRACTS["register_supplied_channel.py/1"]["video_snapshot_fields"] - {"title"},
    "nullable_channel_snapshot_fields": {"subscriber_count", "video_count"},
}

EVIDENCE_LAYER = {
    "SOURCE_EXTRACTED": "EXTRACTED_FACT",
    "SOURCE_COMPUTED": "MEASURED_FACT",
    "TRANSCRIPT_METADATA": "EXTRACTED_FACT",
}


class IdSeq:
    def __init__(self, conn, table, prefix):
        self.n = conn.execute("SELECT COUNT(*) FROM {};".format(table)).fetchone()[0]
        self.prefix = prefix
        self.created = 0

    def next(self):
        self.n += 1
        self.created += 1
        return "{}-{:06d}".format(self.prefix, self.n)


def to_int(raw, field_name):
    if raw is None or raw == "":
        return None
    try:
        return int(float(raw))
    except (TypeError, ValueError):
        raise CatalogError("MalformedData", "Could not parse integer field {}: {!r}".format(field_name, raw))


def to_float(raw, field_name):
    if raw is None or raw == "":
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        raise CatalogError("MalformedData", "Could not parse decimal field {}: {!r}".format(field_name, raw))


def normalize_published_at(raw):
    if not raw:
        return None
    return raw.replace(" ", "T") + "Z"  # column is explicitly labeled "(UTC)" — no tz invented


def _require_v2(conn):
    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()}
    if "channels" not in tables:
        raise CatalogError("SourceNotFound", "Schema version 2 not applied. Run: python3 scripts/inventory_catalog.py init")


# ---------------------------------------------------------------------------
# register
# ---------------------------------------------------------------------------

def cmd_register(args):
    db_path = Path(args.db_path)
    dataset_id = args.dataset_id
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_v2(conn)
        dataset = conn.execute("SELECT dataset_id, status FROM datasets WHERE dataset_id = ?;", (dataset_id,)).fetchone()
        if not dataset:
            raise CatalogError("SourceNotFound", "Dataset {} not found in catalog.".format(dataset_id))

        physical = conn.execute(
            """SELECT file_id, original_filename, canonical_path, sha256, file_role
               FROM source_files WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE';""",
            (dataset_id,),
        ).fetchall()
        xlsx_row = next((r for r in physical if r[4] == "STRUCTURED_METADATA"), None)
        zip_row = next((r for r in physical if r[4] == "TRANSCRIPT_ARCHIVE"), None)
        if not xlsx_row or not zip_row:
            raise CatalogError(
                "SourceNotFound",
                "Dataset {} is missing an expected STRUCTURED_METADATA or TRANSCRIPT_ARCHIVE physical file.".format(dataset_id),
            )

        # Changed-source detection (rule 39) — before parsing anything.
        for _, filename, canonical_path, recorded_sha256, _role in physical:
            p = resolve_canonical_path(canonical_path)
            if not p.exists():
                raise CatalogError("SourceNotFound", "Canonical file missing: {}".format(canonical_path))
            actual = sha256_file(p)
            if actual != recorded_sha256:
                raise CatalogError(
                    "RevisionDetected",
                    "Canonical file {} hash changed since Phase 1A ingestion (recorded={}, actual={}). "
                    "Registration refused under this Dataset ID.".format(filename, recorded_sha256, actual),
                )

        # Idempotency (rule 38).
        prior = conn.execute(
            """SELECT run_id FROM ingestion_runs
               WHERE dataset_id = ? AND run_type = 'STRUCTURED_REGISTRATION' AND status = 'COMPLETED'
               ORDER BY started_at DESC LIMIT 1;""",
            (dataset_id,),
        ).fetchone()
        if prior:
            print("ALREADY_REGISTERED / VERIFIED — {} was already structurally registered by run {}. "
                  "Source hashes still match; no records created.".format(dataset_id, prior[0]))
            return

        xlsx_path, zip_path = Path(xlsx_row[2]), Path(zip_row[2])
        wb = ymd.read_workbook(xlsx_path)
        scraped_date = ymd.find_scraped_date(wb["banner_lines"])
        transcript_members = ymd.read_transcript_archive(zip_path)

        archive_rows = conn.execute(
            """SELECT file_id, archive_member_path FROM source_files
               WHERE dataset_id = ? AND storage_kind = 'ARCHIVE_MEMBER' AND file_role = 'TRANSCRIPT';""",
            (dataset_id,),
        ).fetchall()
        archive_file_id_by_path = {path: file_id for file_id, path in archive_rows}

        reconciliation = _reconcile(wb["videos"], transcript_members)
        _register_transaction(
            conn, dataset_id, wb, scraped_date, transcript_members,
            archive_file_id_by_path, reconciliation, db_path,
        )
    except CatalogError as exc:
        _log_failed_run(db_path, dataset_id, exc)
        print("FAILED — {}: {}".format(exc.error_type, exc.message))
        sys.exit(1)
    finally:
        conn.close()


def _reconcile(workbook_videos, transcript_members):
    wb_ids = [v["Video ID"][0] for v in workbook_videos]
    arc_ids = [m["video_id"] for m in transcript_members]
    wb_counts, arc_counts = Counter(wb_ids), Counter(arc_ids)
    return {
        "workbook_video_ids": sorted(set(wb_ids)),
        "archive_video_ids": sorted(set(arc_ids)),
        "matched": sorted(set(wb_ids) & set(arc_ids)),
        "workbook_only": sorted(set(wb_ids) - set(arc_ids)),
        "archive_only": sorted(set(arc_ids) - set(wb_ids)),
        "duplicate_workbook_ids": sorted(i for i, c in wb_counts.items() if c > 1),
        "duplicate_archive_ids": sorted(i for i, c in arc_counts.items() if c > 1),
    }


def _register_transaction(conn, dataset_id, wb, scraped_date, transcript_members,
                           archive_file_id_by_path, reconciliation, db_path):
    run_id = IdSeq(conn, "ingestion_runs", "RUN").next()
    started_at = now_iso()
    transcripts_by_video_id = {}
    for m in transcript_members:
        transcripts_by_video_id.setdefault(m["video_id"], m)  # first occurrence wins on duplicates

    channel_ids = IdSeq(conn, "channels", "CH")
    snapshot_ids = IdSeq(conn, "channel_snapshots", "CS")
    video_ids = IdSeq(conn, "videos", "VID")
    video_snapshot_ids = IdSeq(conn, "video_snapshots", "VS")
    transcript_ids = IdSeq(conn, "transcripts", "TR")
    provenance_ids = IdSeq(conn, "field_provenance", "PR")

    # Everything below is one transaction: on any exception nothing commits
    # (rule 43). `with conn` rolls back automatically before the exception
    # reaches cmd_register's except handler, so _log_failed_run's separate
    # connection never collides with a still-open write transaction here.
    with conn:
        counts, warnings = _do_register(
            conn, dataset_id, wb, scraped_date, transcripts_by_video_id, archive_file_id_by_path,
            reconciliation, run_id, started_at, channel_ids, snapshot_ids, video_ids,
            video_snapshot_ids, transcript_ids, provenance_ids,
        )

    print("COMPLETED — {} structurally registered. Run {}.".format(dataset_id, run_id))
    print("Counts: {}".format(counts))
    if warnings:
        print("Warnings ({}):".format(len(warnings)))
        for w in warnings:
            print("  - {}".format(w))
    print("Reconciliation: matched={} workbook_only={} archive_only={} duplicate_workbook_ids={} duplicate_archive_ids={}".format(
        len(reconciliation["matched"]), len(reconciliation["workbook_only"]), len(reconciliation["archive_only"]),
        len(reconciliation["duplicate_workbook_ids"]), len(reconciliation["duplicate_archive_ids"])))

    _write_manifest_addendum(conn, dataset_id, run_id, counts, reconciliation, warnings)


def _do_register(conn, dataset_id, wb, scraped_date, transcripts_by_video_id, archive_file_id_by_path,
                  reconciliation, run_id, started_at, channel_ids, snapshot_ids, video_ids,
                  video_snapshot_ids, transcript_ids, provenance_ids):
    conn.execute(
        """INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status,
           source_file_count, archive_member_count, total_size_bytes, errors_count, verification_status,
           tool_version, run_type, notes)
           VALUES (?, ?, ?, NULL, 'STARTED', NULL, NULL, NULL, 0, NULL, ?, 'STRUCTURED_REGISTRATION', NULL);""",
        (run_id, dataset_id, started_at, TOOL_VERSION),
    )

    provenance_rows = []

    def add_provenance(target_col, target_id, field_name, locator, value_origin, extraction_method,
                        observed_at=None, source_file_id=None):
        cols = {"channel_id": None, "channel_snapshot_id": None, "video_id": None,
                "video_snapshot_id": None, "transcript_id": None}
        cols[target_col] = target_id
        provenance_rows.append((
            provenance_ids.next(), dataset_id, run_id, source_file_id,
            cols["channel_id"], cols["channel_snapshot_id"], cols["video_id"],
            cols["video_snapshot_id"], cols["transcript_id"],
            field_name, locator, value_origin, EVIDENCE_LAYER[value_origin],
            extraction_method, observed_at, started_at, None,
        ))

    warnings = []
    errors_to_log = []

    channel_name_to_id = {}
    for display_name, fields in wb["channels"].items():
        channel_id = channel_ids.next()
        youtube_channel_id = fields.get("Channel ID", (None,))[0]
        handle = fields.get("Handle", (None,))[0]
        channel_url = fields.get("Channel URL", (None,))[0]
        conn.execute(
            """INSERT INTO channels (channel_id, youtube_channel_id, handle, display_name, channel_url,
               created_from_dataset_id, created_at, updated_at, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL);""",
            (channel_id, youtube_channel_id, handle, display_name, channel_url, dataset_id, started_at, started_at),
        )
        for field_label, target_attr in CHANNEL_FIELDS:
            if field_label not in fields:
                continue
            value, row_num, col = fields[field_label]
            locator = "YouTube_Master_Data.xlsx#Channel Overview!row={},column={}".format(row_num, col)
            add_provenance("channel_id", channel_id, target_attr, locator, "SOURCE_EXTRACTED", "xlsx_cell_read")

        channel_snapshot_id = snapshot_ids.next()
        subscriber_count = to_int(fields.get("Subscribers", (None,))[0], "Subscribers")
        video_count = to_int(fields.get("Total Videos (YouTube)", (None,))[0], "Total Videos (YouTube)")
        conn.execute(
            """INSERT INTO channel_snapshots (channel_snapshot_id, channel_id, dataset_id, registration_run_id,
               observed_at, subscriber_count, video_count, created_at, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL);""",
            (channel_snapshot_id, channel_id, dataset_id, run_id, scraped_date, subscriber_count, video_count, started_at),
        )
        for field_label, target_attr in CHANNEL_SNAPSHOT_FIELDS:
            if field_label not in fields:
                continue
            value, row_num, col = fields[field_label]
            locator = "YouTube_Master_Data.xlsx#Channel Overview!row={},column={}".format(row_num, col)
            add_provenance("channel_snapshot_id", channel_snapshot_id, target_attr, locator, "SOURCE_EXTRACTED", "xlsx_cell_read", observed_at=scraped_date)

        channel_name_to_id[display_name] = channel_id

    for entry in reconciliation["archive_only"]:
        warnings.append("Archive-only video ID (no workbook row, no video registered): {}".format(entry))
        errors_to_log.append(("EvidenceConflict", "Low", "Archive video ID {} has no matching workbook row.".format(entry)))
    for entry in reconciliation["duplicate_archive_ids"]:
        warnings.append("Duplicate archive video ID (first occurrence used): {}".format(entry))
        errors_to_log.append(("EvidenceConflict", "Low", "Archive video ID {} appears in more than one transcript member.".format(entry)))

    processed_video_ids = set()
    for v in wb["videos"]:
        youtube_video_id = v["Video ID"][0]
        if youtube_video_id in processed_video_ids:
            warnings.append("Duplicate workbook video ID (first row used): {}".format(youtube_video_id))
            errors_to_log.append(("EvidenceConflict", "Low", "Workbook video ID {} appears in more than one row.".format(youtube_video_id)))
            continue
        processed_video_ids.add(youtube_video_id)

        channel_display = v["Channel"][0]
        channel_id = channel_name_to_id.get(channel_display)
        if not channel_id:
            # Not a two-source disagreement (EvidenceConflict) — there is no
            # valid channel_id to attach this row to at all, so it halts.
            raise CatalogError("MalformedData", "Video {} references unrecognized channel '{}' (no matching Channel Overview entry)".format(youtube_video_id, channel_display))

        transcript_meta = transcripts_by_video_id.get(youtube_video_id)
        if transcript_meta and transcript_meta["channel"] != channel_display:
            warnings.append("Channel mismatch for video {}: workbook='{}' transcript='{}'".format(
                youtube_video_id, channel_display, transcript_meta["channel"]))
            errors_to_log.append(("EvidenceConflict", "Medium",
                "Video {}: workbook channel '{}' disagrees with transcript header channel '{}'.".format(
                    youtube_video_id, channel_display, transcript_meta["channel"])))

        video_id = video_ids.next()
        canonical_url = v["Video URL"][0]
        conn.execute(
            """INSERT INTO videos (video_id, youtube_video_id, channel_id, canonical_url,
               created_from_dataset_id, created_at, updated_at, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, NULL);""",
            (video_id, youtube_video_id, channel_id, canonical_url, dataset_id, started_at, started_at),
        )
        for field_label, target_attr in VIDEO_FIELDS:
            value, row_num, col = v[field_label]
            locator = "YouTube_Master_Data.xlsx#All Videos!row={},column={}".format(row_num, col)
            add_provenance("video_id", video_id, target_attr, locator, "SOURCE_EXTRACTED", "xlsx_cell_read")

        video_snapshot_id = video_snapshot_ids.next()
        snap_values = {}
        for field_label, target_attr, origin in VIDEO_SNAPSHOT_FIELDS:
            raw_value, row_num, col = v[field_label]
            if target_attr == "published_at":
                parsed = normalize_published_at(raw_value)
            elif target_attr in ("duration_seconds", "views", "likes", "comments",
                                  "description_char_count", "transcript_word_count"):
                parsed = to_int(raw_value, field_label)
            elif target_attr in ("views_per_day", "engagement_rate"):
                parsed = to_float(raw_value, field_label)
            else:
                parsed = raw_value
            snap_values[target_attr] = parsed
            locator = "YouTube_Master_Data.xlsx#All Videos!row={},column={}".format(row_num, col)
            add_provenance("video_snapshot_id", video_snapshot_id, target_attr, locator, origin, "xlsx_cell_read", observed_at=scraped_date)

        conn.execute(
            """INSERT INTO video_snapshots (video_snapshot_id, video_id, dataset_id, registration_run_id,
               observed_at, published_at, title, duration_seconds, views, likes, comments,
               views_per_day, engagement_rate, description_char_count, transcript_word_count, created_at, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL);""",
            (video_snapshot_id, video_id, dataset_id, run_id, scraped_date, snap_values["published_at"],
             snap_values["title"], snap_values["duration_seconds"], snap_values["views"], snap_values["likes"],
             snap_values["comments"], snap_values["views_per_day"], snap_values["engagement_rate"],
             snap_values["description_char_count"], snap_values["transcript_word_count"], started_at),
        )

        if not transcript_meta:
            warnings.append("Workbook-only video, no transcript registered: {}".format(youtube_video_id))
            errors_to_log.append(("TranscriptFailure", "Medium", "Video {} has no matching transcript archive member.".format(youtube_video_id)))
            continue

        archive_member_path = transcript_meta["archive_member_path"]
        archive_file_id = archive_file_id_by_path.get(archive_member_path)
        if not archive_file_id:
            raise CatalogError("MissingProvenance", "No Phase 1A archive-member record for {}".format(archive_member_path))

        transcript_id = transcript_ids.next()
        word_count = to_int(transcript_meta["word_count"], "Word count")
        conn.execute(
            """INSERT INTO transcripts (transcript_id, video_id, dataset_id, registration_run_id,
               archive_member_file_id, availability_status, caption_type, language, word_count,
               transcript_sha256, description_present, created_at, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, NULL);""",
            (transcript_id, video_id, dataset_id, run_id, archive_file_id,
             transcript_meta["availability_status"], transcript_meta["caption_type"],
             transcript_meta["language"], word_count, int(transcript_meta["description_present"]), started_at),
        )
        for field_name in TRANSCRIPT_HEADER_FIELDS:
            locator = "Transcripts_All_159_Videos.zip::{}#header:{}".format(archive_member_path, field_name)
            add_provenance("transcript_id", transcript_id, field_name, locator, "TRANSCRIPT_METADATA",
                            "transcript_header_parse", source_file_id=archive_file_id)

    conn.executemany(
        """INSERT INTO field_provenance (provenance_id, dataset_id, registration_run_id, source_file_id,
           channel_id, channel_snapshot_id, video_id, video_snapshot_id, transcript_id,
           field_name, source_locator, value_origin, evidence_layer, extraction_method, observed_at, created_at, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
        provenance_rows,
    )

    completed_at = now_iso()
    conn.execute(
        """UPDATE ingestion_runs SET completed_at = ?, status = 'COMPLETED', errors_count = ?,
           verification_status = 'VERIFIED', notes = ? WHERE run_id = ?;""",
        (completed_at, len(errors_to_log),
         "channels={} videos={} transcripts={} provenance_rows={}".format(
             len(channel_name_to_id), len(processed_video_ids), transcript_ids.created, len(provenance_rows)),
         run_id),
    )
    for error_type, severity, message in errors_to_log:
        error_id = IdSeq(conn, "ingestion_errors", "ERR").next()
        conn.execute(
            """INSERT INTO ingestion_errors (error_id, run_id, dataset_id, file_id, error_type, severity,
               message, retryable, requires_human_review, created_at, resolved_at, notes)
               VALUES (?, ?, ?, NULL, ?, ?, ?, 0, 1, ?, NULL, NULL);""",
            (error_id, run_id, dataset_id, error_type, severity, message, completed_at),
        )

    conn.execute(
        "UPDATE datasets SET status = 'STRUCTURED_REGISTERED', updated_at = ? WHERE dataset_id = ?;",
        (completed_at, dataset_id),
    )

    counts = {
        "channels": len(channel_name_to_id),
        "channel_snapshots": snapshot_ids.created,
        "videos": video_ids.created,
        "video_snapshots": video_snapshot_ids.created,
        "transcripts": transcript_ids.created,
        "field_provenance": len(provenance_rows),
    }
    return counts, warnings


def _log_failed_run(db_path, dataset_id, exc):
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        run_id = IdSeq(conn, "ingestion_runs", "RUN").next()
        ts = now_iso()
        with conn:
            conn.execute(
                """INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status,
                   source_file_count, archive_member_count, total_size_bytes, errors_count,
                   verification_status, tool_version, run_type, notes)
                   VALUES (?, ?, ?, ?, 'FAILED', NULL, NULL, NULL, 1, 'FAILED', ?, 'STRUCTURED_REGISTRATION', ?);""",
                (run_id, dataset_id, ts, ts, TOOL_VERSION, "error={}".format(exc)),
            )
            error_id = IdSeq(conn, "ingestion_errors", "ERR").next()
            conn.execute(
                """INSERT INTO ingestion_errors (error_id, run_id, dataset_id, file_id, error_type, severity,
                   message, retryable, requires_human_review, created_at, resolved_at, notes)
                   VALUES (?, ?, ?, NULL, ?, 'High', ?, 0, 1, ?, NULL, NULL);""",
                (error_id, run_id, dataset_id, exc.error_type, exc.message, ts),
            )
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# manifest addendum
# ---------------------------------------------------------------------------

MANIFEST_SECTION_MARKER = "## Phase 1B Structured Registration"


def _write_manifest_addendum(conn, dataset_id, run_id, counts, reconciliation, warnings):
    manifest_path = inventory_catalog.MANIFESTS_DIR / "{}.md".format(dataset_id)
    text = manifest_path.read_text() if manifest_path.exists() else ""
    if MANIFEST_SECTION_MARKER in text:
        text = text.split(MANIFEST_SECTION_MARKER, 1)[0].rstrip() + "\n"

    available = conn.execute(
        "SELECT COUNT(*) FROM transcripts WHERE dataset_id=? AND availability_status='AVAILABLE';", (dataset_id,)
    ).fetchone()[0]
    unavailable = conn.execute(
        "SELECT COUNT(*) FROM transcripts WHERE dataset_id=? AND availability_status='UNAVAILABLE';", (dataset_id,)
    ).fetchone()[0]

    lines = [text.rstrip(), "", MANIFEST_SECTION_MARKER, ""]
    lines.append("- Registration run ID: {}".format(run_id))
    lines.append("- Schema version: 2")
    lines.append("- Registered channels: {}".format(counts["channels"]))
    lines.append("- Registered channel snapshots: {}".format(counts["channel_snapshots"]))
    lines.append("- Registered videos: {}".format(counts["videos"]))
    lines.append("- Registered video snapshots: {}".format(counts["video_snapshots"]))
    lines.append("- Transcript records: {} (AVAILABLE: {}, UNAVAILABLE: {})".format(
        counts["transcripts"], available, unavailable))
    lines.append("- Field provenance rows: {}".format(counts["field_provenance"]))
    lines.append("")
    lines.append("### Source Reconciliation")
    lines.append("")
    lines.append("- Workbook video IDs: {}".format(len(reconciliation["workbook_video_ids"])))
    lines.append("- Archive video IDs: {}".format(len(reconciliation["archive_video_ids"])))
    lines.append("- Matched: {}".format(len(reconciliation["matched"])))
    lines.append("- Workbook-only: {}".format(len(reconciliation["workbook_only"])))
    lines.append("- Archive-only: {}".format(len(reconciliation["archive_only"])))
    lines.append("- Duplicate workbook IDs: {}".format(len(reconciliation["duplicate_workbook_ids"])))
    lines.append("- Duplicate archive IDs: {}".format(len(reconciliation["duplicate_archive_ids"])))
    lines.append("")
    lines.append("### Warnings / Conflicts")
    lines.append("")
    if warnings:
        for w in warnings:
            lines.append("- {}".format(w))
    else:
        lines.append("None.")
    lines.append("")
    lines.append("### Limitations")
    lines.append("")
    lines.append("No competitor strategy analysis, topic generation, or content scoring was performed. "
                 "This section records structured source registration only — what values exist, where they "
                 "came from, and whether workbook/archive evidence agrees.")
    lines.append("")

    manifest_path.write_text("\n".join(lines))
    print("Manifest updated: {}".format(manifest_path))


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------

def _producer_contract(tool_version):
    return PRODUCER_CONTRACTS.get(tool_version)


def _provenance_coverage(conn, dataset_id, counts, contract):
    if not contract:
        return False, None
    targets = (
        ("channel_id", "channels", "channel_fields"),
        ("channel_snapshot_id", "channel_snapshots", "channel_snapshot_fields"),
        ("video_id", "videos", "video_fields"),
        ("video_snapshot_id", "video_snapshots", "video_snapshot_fields"),
        ("transcript_id", "transcripts", "transcript_fields"),
    )
    expected_total = 0
    actual_total = 0
    valid = True
    for target_column, count_key, fields_key in targets:
        expected_fields = contract[fields_key]
        rows = conn.execute(
            "SELECT {},field_name FROM field_provenance "
            "WHERE dataset_id=? AND {} IS NOT NULL".format(target_column, target_column),
            (dataset_id,),
        ).fetchall()
        actual_total += len(rows)
        by_target = {}
        for target_id, field_name in rows:
            by_target.setdefault(target_id, []).append(field_name)
        expected_by_target = {}
        nullable_key = {"video_snapshot_id": "nullable_video_snapshot_fields",
                        "channel_snapshot_id": "nullable_channel_snapshot_fields"}.get(target_column)
        if nullable_key:
            for field in contract.get(nullable_key, set()):
                for target_id, value in conn.execute(
                    "SELECT {},{} FROM {} WHERE dataset_id=?".format(target_column, field, count_key), (dataset_id,),
                ):
                    if value is None:
                        expected_by_target.setdefault(target_id, set(expected_fields)).discard(field)
        empty_targets = {target_id for target_id, fields in expected_by_target.items() if not fields}
        if len(set(by_target) | empty_targets) != counts[count_key]:
            valid = False
        expected_total += counts[count_key] * len(expected_fields) - sum(
            len(expected_fields) - len(fields) for fields in expected_by_target.values()
        )
        for target_id, fields in by_target.items():
            expected = expected_by_target.get(target_id, expected_fields)
            if len(fields) != len(expected) or set(fields) != expected:
                valid = False
    return valid, actual_total / expected_total if expected_total else None


def _manifest_agrees(text, counts, tool_version):
    if tool_version == TOOL_VERSION:
        return (
            "Registered videos: {}".format(counts["videos"]) in text
            and "Field provenance rows: {}".format(counts["field_provenance"]) in text
        )
    if tool_version == "apify_youtube_ingest.py/1":
        video_marker = (
            "Registered videos: {}".format(counts["videos"]) in text
            or "Registered content items: {}".format(counts["videos"]) in text
        )
        transcript_marker = "Transcripts: AVAILABLE {}, UNAVAILABLE {}".format(
            counts["transcripts_available"], counts["transcripts_unavailable"]
        )
        return video_marker and transcript_marker in text
    if tool_version in {"register_supplied_channel.py/1", "register_supplied_channel.py/2"}:
        return (
            "Canonical videos: {}".format(counts["videos"]) in text
            and "Available transcripts: {}".format(counts["transcripts_available"]) in text
        )
    return False

def cmd_verify(args):
    db_path = Path(args.db_path)
    dataset_id = args.dataset_id
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_v2(conn)
        run = conn.execute(
            """SELECT run_id, status, tool_version FROM ingestion_runs
               WHERE dataset_id = ? AND run_type = 'STRUCTURED_REGISTRATION'
               ORDER BY started_at DESC LIMIT 1;""",
            (dataset_id,),
        ).fetchone()
        if not run:
            print("NOT_REGISTERED — no structured registration run found for {}.".format(dataset_id))
            sys.exit(1)

        # Re-verify canonical raw files still match (rule 57).
        physical = conn.execute(
            """SELECT original_filename, canonical_path, sha256 FROM source_files
               WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE';""",
            (dataset_id,),
        ).fetchall()
        hash_mismatches = []
        for filename, canonical_path, recorded_sha256 in physical:
            p = resolve_canonical_path(canonical_path)
            if not p.exists() or sha256_file(p) != recorded_sha256:
                hash_mismatches.append(filename)

        counts = {}
        dataset_id_column = {
            "channels": "created_from_dataset_id", "channel_snapshots": "dataset_id",
            "videos": "created_from_dataset_id", "video_snapshots": "dataset_id",
            "transcripts": "dataset_id", "field_provenance": "dataset_id",
        }
        for table, column in dataset_id_column.items():
            counts[table] = conn.execute(
                "SELECT COUNT(*) FROM {} WHERE {} = ?;".format(table, column), (dataset_id,)
            ).fetchone()[0]
        if run[2] == "register_supplied_channel.py/2":
            counts["channels"] = conn.execute(
                "SELECT COUNT(DISTINCT channel_id) FROM channel_dataset_links WHERE dataset_id=?",
                (dataset_id,),
            ).fetchone()[0]
        counts["transcripts_available"] = conn.execute(
            "SELECT COUNT(*) FROM transcripts WHERE dataset_id=? AND availability_status='AVAILABLE';", (dataset_id,)
        ).fetchone()[0]
        counts["transcripts_unavailable"] = conn.execute(
            "SELECT COUNT(*) FROM transcripts WHERE dataset_id=? AND availability_status='UNAVAILABLE';", (dataset_id,)
        ).fetchone()[0]

        contract = _producer_contract(run[2])
        provenance_valid, coverage = _provenance_coverage(conn, dataset_id, counts, contract)

        integrity = conn.execute("PRAGMA integrity_check;").fetchone()[0]
        fk_violations = conn.execute("PRAGMA foreign_key_check;").fetchall()

        manifest_path = inventory_catalog.MANIFESTS_DIR / "{}.md".format(dataset_id)
        manifest_agrees = None
        if manifest_path.exists():
            text = manifest_path.read_text()
            manifest_agrees = _manifest_agrees(text, counts, run[2])

        pending_valid = True
        if run[2] == "register_supplied_channel.py/2":
            pending_ids = [row[0] for row in conn.execute(
                "SELECT v.youtube_video_id FROM videos v JOIN video_snapshots s USING(video_id) "
                "WHERE s.dataset_id=? AND NOT EXISTS (SELECT 1 FROM transcripts t WHERE t.video_id=v.video_id AND t.dataset_id=?) ORDER BY v.youtube_video_id",
                (dataset_id, dataset_id),
            )]
            declarations = [row[0] for row in conn.execute(
                "SELECT message FROM ingestion_errors WHERE dataset_id=? AND run_id=? AND error_type='TranscriptPending' ORDER BY message",
                (dataset_id, run[0]),
            )]
            expected_declarations = ["Canonical identity registered; transcript evidence pending: {}".format(value) for value in pending_ids]
            pending_valid = declarations == expected_declarations
            pending_valid = pending_valid and manifest_path.exists() and (
                "Transcript pending: {} ({})".format(len(pending_ids), ", ".join(pending_ids) or "none") in text
            )
        status = "VERIFIED" if (
            not hash_mismatches and integrity == "ok" and not fk_violations
            and provenance_valid and manifest_agrees and pending_valid
        ) else "FAILED"

        print("Registration run: {} ({})".format(run[0], run[1]))
        print("Raw file hash mismatches: {}".format(hash_mismatches or "none"))
        print("Counts: {}".format(counts))
        print("Field provenance coverage: {}".format("{:.1%}".format(coverage) if coverage is not None else "N/A"))
        print("PRAGMA integrity_check: {}".format(integrity))
        print("PRAGMA foreign_key_check violations: {}".format(len(fk_violations)))
        print("Manifest agrees with catalog counts: {}".format(manifest_agrees))
        print("Status: {}".format(status))
        if status != "VERIFIED":
            sys.exit(1)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# legacy provenance backfill
# ---------------------------------------------------------------------------

def cmd_backfill_workbook_provenance(args):
    db_path = Path(args.db_path)
    dataset_id = args.dataset_id
    if dataset_id != "DS-000001":
        print("FAILED — this backfill is restricted to DS-000001.")
        sys.exit(1)

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_v2(conn)
        workbooks = conn.execute(
            """SELECT file_id, canonical_path, sha256 FROM source_files
               WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE'
                 AND file_role = 'STRUCTURED_METADATA'
                 AND original_filename = 'YouTube_Master_Data.xlsx';""",
            (dataset_id,),
        ).fetchall()
        if len(workbooks) != 1:
            raise CatalogError(
                "SourceNotFound",
                "Expected exactly one canonical DS-000001 workbook; found {}.".format(len(workbooks)),
            )

        workbook_file_id, canonical_path, recorded_sha256 = workbooks[0]
        workbook_path = resolve_canonical_path(canonical_path)
        if not workbook_path.exists():
            raise CatalogError("SourceNotFound", "Canonical workbook missing: {}".format(canonical_path))
        actual_sha256 = sha256_file(workbook_path)
        if actual_sha256 != recorded_sha256:
            raise CatalogError(
                "RevisionDetected",
                "Canonical workbook hash changed since ingestion (recorded={}, actual={}).".format(
                    recorded_sha256, actual_sha256
                ),
            )

        null_count = conn.execute(
            "SELECT COUNT(*) FROM field_provenance WHERE dataset_id = ? AND source_file_id IS NULL;",
            (dataset_id,),
        ).fetchone()[0]
        workbook_null_count = conn.execute(
            """SELECT COUNT(*) FROM field_provenance
               WHERE dataset_id = ? AND source_file_id IS NULL
                 AND source_locator LIKE 'YouTube_Master_Data.xlsx#%';""",
            (dataset_id,),
        ).fetchone()[0]
        if null_count != workbook_null_count:
            raise CatalogError(
                "MalformedData",
                "DS-000001 has {} NULL provenance links but only {} workbook locators; no rows changed.".format(
                    null_count, workbook_null_count
                ),
            )

        with conn:
            corrected = conn.execute(
                """UPDATE field_provenance SET source_file_id = ?
                   WHERE dataset_id = ? AND source_file_id IS NULL
                     AND source_locator LIKE 'YouTube_Master_Data.xlsx#%';""",
                (workbook_file_id, dataset_id),
            ).rowcount
        print("COMPLETED — {} workbook provenance link(s) backfilled to {}.".format(
            corrected, workbook_file_id
        ))
    except CatalogError as exc:
        print("FAILED — {}: {}".format(exc.error_type, exc.message))
        sys.exit(1)
    finally:
        conn.close()


def cmd_backfill_transcript_provenance(args):
    db_path = Path(args.db_path)
    dataset_id = args.dataset_id
    if dataset_id != "DS-000001":
        print("FAILED — this backfill is restricted to DS-000001.")
        sys.exit(1)

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_v2(conn)
        rows = conn.execute(
            """SELECT t.transcript_id, v.youtube_video_id, t.archive_member_file_id,
                      t.transcript_sha256, t.canonical_reference,
                      sf.dataset_id, sf.storage_kind, sf.file_role, sf.archive_member_path, sf.sha256,
                      parent.file_id, parent.dataset_id, parent.storage_kind, parent.file_role,
                      parent.canonical_path, parent.sha256
               FROM transcripts t
               JOIN videos v ON v.video_id = t.video_id
               LEFT JOIN source_files sf ON sf.file_id = t.archive_member_file_id
               LEFT JOIN source_files parent ON parent.file_id = sf.parent_file_id
               WHERE t.dataset_id = ? AND t.availability_status = 'AVAILABLE'
               ORDER BY t.transcript_id;""",
            (dataset_id,),
        ).fetchall()
        if not rows:
            raise CatalogError("SourceNotFound", "No AVAILABLE DS-000001 transcripts found.")
        if len({row[2] for row in rows}) != len(rows):
            raise CatalogError("MissingProvenance", "AVAILABLE transcripts do not map one-to-one to archive members.")

        parents = {(row[10], row[14], row[15]) for row in rows}
        if len(parents) != 1 or None in next(iter(parents)):
            raise CatalogError("MissingProvenance", "AVAILABLE transcripts do not resolve to one canonical archive.")
        _parent_file_id, canonical_path, recorded_archive_sha256 = next(iter(parents))
        archive_path = resolve_canonical_path(canonical_path)
        if not archive_path.exists():
            raise CatalogError("SourceNotFound", "Canonical transcript archive missing: {}".format(canonical_path))
        actual_archive_sha256 = sha256_file(archive_path)
        if actual_archive_sha256 != recorded_archive_sha256:
            raise CatalogError(
                "RevisionDetected",
                "Canonical transcript archive hash changed since ingestion (recorded={}, actual={}).".format(
                    recorded_archive_sha256, actual_archive_sha256
                ),
            )

        parsed_members = ymd.read_transcript_archive(archive_path)
        parsed_by_path = {member["archive_member_path"]: member for member in parsed_members}
        if len(parsed_by_path) != len(parsed_members):
            raise CatalogError("MissingProvenance", "Transcript archive contains duplicate member paths.")

        updates = []
        with zipfile.ZipFile(archive_path) as archive:
            member_counts = Counter(archive.namelist())
            for row in rows:
                (transcript_id, youtube_video_id, _archive_member_file_id,
                 existing_hash, existing_reference, source_dataset_id, storage_kind,
                 file_role, member_path, recorded_member_sha256, _parent_file_id,
                 parent_dataset_id, parent_storage_kind, parent_file_role,
                 _parent_path, _parent_sha256) = row
                if (
                    source_dataset_id != dataset_id
                    or storage_kind != "ARCHIVE_MEMBER"
                    or file_role != "TRANSCRIPT"
                    or parent_dataset_id != dataset_id
                    or parent_storage_kind != "PHYSICAL_FILE"
                    or parent_file_role != "TRANSCRIPT_ARCHIVE"
                    or not member_path
                    or not recorded_member_sha256
                    or member_counts[member_path] != 1
                ):
                    raise CatalogError(
                        "MissingProvenance",
                        "Transcript {} has an invalid archive-member source relationship.".format(transcript_id),
                    )
                member_meta = parsed_by_path.get(member_path)
                if not member_meta or member_meta["video_id"] != youtube_video_id:
                    raise CatalogError(
                        "MissingProvenance",
                        "Transcript {} archive-member identity does not match its video.".format(transcript_id),
                    )
                actual_member_sha256 = sha256_bytes(archive.read(member_path))
                reference = "{}::{}".format(canonical_path, member_path)
                if actual_member_sha256 != recorded_member_sha256:
                    raise CatalogError(
                        "RevisionDetected",
                        "Archive member hash changed for {} (recorded={}, actual={}).".format(
                            member_path, recorded_member_sha256, actual_member_sha256
                        ),
                    )
                if existing_hash not in (None, actual_member_sha256) or existing_reference not in (None, reference):
                    raise CatalogError(
                        "RevisionDetected",
                        "Transcript {} has conflicting existing provenance values.".format(transcript_id),
                    )
                updates.append((actual_member_sha256, reference, transcript_id, dataset_id))

        with conn:
            conn.executemany(
                """UPDATE transcripts
                   SET transcript_sha256 = COALESCE(transcript_sha256, ?),
                       canonical_reference = COALESCE(canonical_reference, ?)
                   WHERE transcript_id = ? AND dataset_id = ? AND availability_status = 'AVAILABLE';""",
                updates,
            )
        print("COMPLETED — {} AVAILABLE transcript provenance row(s) verified/backfilled.".format(len(updates)))
    except CatalogError as exc:
        print("FAILED — {}: {}".format(exc.error_type, exc.message))
        sys.exit(1)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(description="Phase 1B structured source registration utility.")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    sub = parser.add_subparsers(dest="command", required=True)

    p_register = sub.add_parser("register")
    p_register.add_argument("--dataset-id", required=True)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("--dataset-id", required=True)

    p_backfill = sub.add_parser("backfill-workbook-provenance")
    p_backfill.set_defaults(dataset_id="DS-000001")

    p_transcript_backfill = sub.add_parser("backfill-transcript-provenance")
    p_transcript_backfill.set_defaults(dataset_id="DS-000001")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "register":
        cmd_register(args)
    elif args.command == "verify":
        cmd_verify(args)
    elif args.command == "backfill-workbook-provenance":
        cmd_backfill_workbook_provenance(args)
    elif args.command == "backfill-transcript-provenance":
        cmd_backfill_transcript_provenance(args)


if __name__ == "__main__":
    main()
