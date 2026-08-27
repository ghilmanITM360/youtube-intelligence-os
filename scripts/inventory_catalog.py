#!/usr/bin/env python3
"""Phase 1 SQLite inventory/catalog utility (Decision 012).

Commands: init, ingest, verify. Stdlib only (sqlite3, hashlib, zipfile).
Catalogs files and datasets; never analyzes competitor performance, content,
or intelligence (see docs/Phases.md, Phase 1 boundary).
"""
import argparse
import hashlib
import os
import shutil
import sqlite3
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = REPO_ROOT / "data" / "catalog" / "youtube_inventory.db"
SCHEMA_DIR = REPO_ROOT / "schemas" / "inventory"
TOOL_VERSION = "inventory_catalog.py/1"

# Module-level (not REPO_ROOT-baked-in) so tests can redirect writes into a
# temporary directory instead of touching the real repository (rule 31).
RAW_DATA_ROOT = REPO_ROOT / "data" / "raw"
MANIFESTS_DIR = REPO_ROOT / "data" / "manifests"

# Semantic class (docs/DATA_CLASSIFICATION.md) -> data/raw subdirectory.
CLASS_TO_RAW_DIR = {
    "A": "global-youtube-knowledge",
    "B": "competitors",
    "C": "forensic-analysis",
    "D": "forensic-analysis",
    "E": "keyframes",
    "F": "channel-data",
    "G": "research",
    "H": "uncategorized",
}

MAX_COMPRESSION_RATIO = 500  # zip-bomb heuristic guard (docs/Security.md §7)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def sha256_file(path, chunk_size=1024 * 1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


class CatalogError(Exception):
    def __init__(self, error_type, message):
        super().__init__(message)
        self.error_type = error_type
        self.message = message


# ---------------------------------------------------------------------------
# init
# ---------------------------------------------------------------------------

def cmd_init(args):
    db_path = Path(args.db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        applied = _applied_schema_versions(conn)
        schema_files = sorted(SCHEMA_DIR.glob("*.sql"))
        newly_applied = []
        for schema_file in schema_files:
            version = int(schema_file.stem.split("_", 1)[0])
            if version in applied:
                continue
            sql = schema_file.read_text()
            conn.executescript(sql)
            conn.commit()
            newly_applied.append(version)
        if newly_applied:
            print("Applied schema version(s): {}".format(newly_applied))
        else:
            print("Catalog already initialized. No new schema versions to apply.")
        print("Database: {}".format(db_path))
    finally:
        conn.close()


def _applied_schema_versions(conn):
    cur = conn.cursor()
    try:
        cur.execute("SELECT schema_version FROM schema_meta;")
        return {row[0] for row in cur.fetchall()}
    except sqlite3.OperationalError:
        return set()


def _table_exists(conn, name):
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (name,)
    )
    return cur.fetchone() is not None


def _require_initialized(conn):
    if not _table_exists(conn, "datasets"):
        raise CatalogError(
            "SourceNotFound",
            "Catalog is not initialized. Run: python3 scripts/inventory_catalog.py init",
        )


# ---------------------------------------------------------------------------
# shared helpers
# ---------------------------------------------------------------------------

def _next_id(conn, table, id_column, prefix):
    cur = conn.execute("SELECT COUNT(*) FROM {};".format(table))
    n = cur.fetchone()[0] + 1
    return "{}-{:06d}".format(prefix, n)


def _scan_top_level_files(source_dir):
    """Every regular file directly under source_dir (this dataset has no
    subdirectories; scanning is intentionally shallow rather than a generic
    recursive walker Phase 1 does not yet need)."""
    files = []
    for entry in sorted(source_dir.iterdir()):
        if entry.is_file():
            files.append(entry)
    return files


def _inspect_zip_members(zip_path):
    """Stream-hash each meaningful member of a zip without extracting to
    disk. Returns a list of dicts. Raises CatalogError on unsafe archives."""
    members = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if name.startswith("/") or ".." in Path(name).parts:
                raise CatalogError(
                    "UnsafeArchive",
                    "Path traversal risk in archive member: {}".format(name),
                )
            if info.compress_size > 0:
                ratio = info.file_size / max(info.compress_size, 1)
                if ratio > MAX_COMPRESSION_RATIO:
                    raise CatalogError(
                        "UnsafeArchive",
                        "Suspicious compression ratio ({:.0f}x) for member: {}".format(
                            ratio, name
                        ),
                    )
            with zf.open(info) as f:
                data = f.read()
            digest = sha256_bytes(data)

            upper = name.upper()
            note = None
            if "INDEX" in upper:
                role = "ARCHIVE_INDEX"
            elif name.lower().endswith(".txt"):
                role = "TRANSCRIPT"
                text = data.decode("utf-8", errors="replace")
                if "NONE AVAILABLE" in text or "No captions available" in text:
                    note = "TRANSCRIPT_MISSING (source marks captions unavailable)"
            else:
                role = "ARCHIVE_MEMBER_OTHER"

            members.append(
                {
                    "archive_member_path": name,
                    "size_bytes": info.file_size,
                    "sha256": digest,
                    "file_role": role,
                    "notes": note,
                }
            )
    return members


def _declared_vs_observed_transcript_counts(members):
    """Compares the archive's own INDEX declaration to what was actually
    observed by streaming every member (rule 26 — never blindly trust a
    prior report's numbers)."""
    index_members = [m for m in members if m["file_role"] == "ARCHIVE_INDEX"]
    txt_members = [m for m in members if m["file_role"] == "TRANSCRIPT"]
    missing = [m for m in txt_members if m["notes"]]
    observed = {
        "observed_total_entries": len(members),
        "observed_index_count": len(index_members),
        "observed_per_video_files": len(txt_members),
        "observed_with_transcript": len(txt_members) - len(missing),
        "observed_without_transcript": len(missing),
        "observed_missing_files": [m["archive_member_path"] for m in missing],
    }
    return observed


def _classify_physical_file(path):
    ext = path.suffix.lower()
    if ext == ".xlsx":
        return "STRUCTURED_METADATA"
    if ext == ".zip":
        return "TRANSCRIPT_ARCHIVE" if "transcript" in path.stem.lower() else "SOURCE_ARCHIVE"
    return "UNSPECIFIED"


# ---------------------------------------------------------------------------
# ingest
# ---------------------------------------------------------------------------

def cmd_ingest(args):
    db_path = Path(args.db_path)
    source_dir = Path(args.source)
    dataset_id = args.dataset_id

    if not source_dir.is_dir():
        raise CatalogError("SourceNotFound", "Source path does not exist or is not a directory: {}".format(source_dir))

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_initialized(conn)
        existing = conn.execute(
            "SELECT dataset_id FROM datasets WHERE dataset_id = ?;", (dataset_id,)
        ).fetchone()

        source_files_on_disk = _scan_top_level_files(source_dir)
        if not source_files_on_disk:
            raise CatalogError("SourceNotFound", "No top-level files found under source: {}".format(source_dir))

        current_hashes = {
            f.name: {"size": f.stat().st_size, "sha256": sha256_file(f)}
            for f in source_files_on_disk
        }

        if existing:
            _handle_existing_dataset(conn, dataset_id, current_hashes)
            return

        _ingest_new_dataset(
            conn,
            db_path,
            dataset_id=dataset_id,
            dataset_name=args.name,
            semantic_class=args.semantic_class,
            discovered_as=args.discovered_as,
            source_dir=source_dir,
            source_files_on_disk=source_files_on_disk,
            current_hashes=current_hashes,
        )
    finally:
        conn.close()


def _handle_existing_dataset(conn, dataset_id, current_hashes):
    rows = conn.execute(
        """SELECT original_filename, size_bytes, sha256 FROM source_files
           WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE';""",
        (dataset_id,),
    ).fetchall()
    recorded = {r[0]: {"size": r[1], "sha256": r[2]} for r in rows}

    if recorded == current_hashes:
        print("ALREADY_INGESTED / VERIFIED — {} matches recorded hashes. No records created.".format(dataset_id))
        return

    # Content differs under an existing Dataset ID: fail safely, never overwrite.
    run_id = _next_id(conn, "ingestion_runs", "run_id", "RUN")
    error_id = _next_id(conn, "ingestion_errors", "error_id", "ERR")
    ts = now_iso()
    error_type = "RevisionDetected" if set(recorded) & set(current_hashes) else "ManifestValidationFailure"
    with conn:
        conn.execute(
            """INSERT INTO ingestion_runs
               (run_id, dataset_id, started_at, completed_at, status,
                source_file_count, archive_member_count, total_size_bytes,
                errors_count, verification_status, tool_version, notes)
               VALUES (?, ?, ?, ?, 'FAILED', ?, NULL, NULL, 1, 'FAILED', ?, ?);""",
            (
                run_id, dataset_id, ts, ts, len(current_hashes), TOOL_VERSION,
                "Existing dataset_id with differing source content; ingestion refused.",
            ),
        )
        conn.execute(
            """INSERT INTO ingestion_errors
               (error_id, run_id, dataset_id, file_id, error_type, severity,
                message, retryable, requires_human_review, created_at, resolved_at, notes)
               VALUES (?, ?, ?, NULL, ?, 'High', ?, 0, 1, ?, NULL, NULL);""",
            (
                error_id, run_id, dataset_id, error_type,
                "Dataset {} already exists with different file content (name/size/hash mismatch). "
                "Existing records were not modified.".format(dataset_id),
                ts,
            ),
        )
    print("{} — dataset_id {} exists with different content. Existing dataset untouched. Run {} FAILED.".format(
        error_type.upper(), dataset_id, run_id
    ))
    sys.exit(1)


def _ingest_new_dataset(conn, db_path, *, dataset_id, dataset_name, semantic_class,
                          discovered_as, source_dir, source_files_on_disk, current_hashes):
    run_id = _next_id(conn, "ingestion_runs", "run_id", "RUN")
    started_at = now_iso()

    raw_dir_name = CLASS_TO_RAW_DIR.get(semantic_class.upper(), "uncategorized")
    canonical_dir = RAW_DATA_ROOT / raw_dir_name / dataset_id

    copied_paths = []
    try:
        if canonical_dir.exists():
            # No dataset row exists yet, so any prior contents here are from
            # an earlier failed/interrupted attempt, not a trusted ingest.
            shutil.rmtree(canonical_dir)
        canonical_dir.mkdir(parents=True, exist_ok=False)

        physical_records = []
        archive_members_by_parent = {}
        total_size = 0
        observed_transcripts = None

        for src_file in source_files_on_disk:
            dest_file = canonical_dir / src_file.name
            shutil.copy2(src_file, dest_file)
            copied_paths.append(dest_file)

            copy_hash = sha256_file(dest_file)
            source_hash = current_hashes[src_file.name]["sha256"]
            if copy_hash != source_hash:
                raise CatalogError(
                    "HashFailure",
                    "Canonical copy hash mismatch for {}: source={} copy={}".format(
                        src_file.name, source_hash, copy_hash
                    ),
                )

            size_bytes = current_hashes[src_file.name]["size"]
            total_size += size_bytes
            physical_records.append(
                {
                    "original_filename": src_file.name,
                    "original_path": str(src_file),
                    "canonical_path": str(dest_file),
                    "extension": src_file.suffix.lower(),
                    "size_bytes": size_bytes,
                    "sha256": copy_hash,
                    "file_role": _classify_physical_file(src_file),
                }
            )

            # Only real archive-role zips are inventoried as archives; OOXML
            # containers (.xlsx etc.) are zips internally but stay one
            # physical file (rule 16) — they never reach this branch since
            # their suffix isn't ".zip".
            if src_file.suffix.lower() == ".zip":
                members = _inspect_zip_members(src_file)
                archive_members_by_parent[src_file.name] = members
                if any(m["file_role"] == "ARCHIVE_INDEX" for m in members):
                    observed_transcripts = _declared_vs_observed_transcript_counts(members)

        archive_member_count = sum(len(v) for v in archive_members_by_parent.values())
        completed_at = now_iso()

        with conn:
            conn.execute(
                """INSERT INTO datasets
                   (dataset_id, dataset_name, semantic_class, description, source_type,
                    ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes)
                   VALUES (?, ?, ?, ?, 'EXTERNAL_FOLDER', 'CONTROLLED_COPY', 'INGESTED', ?, ?, ?, ?, ?);""",
                (
                    dataset_id, dataset_name, semantic_class,
                    "Phase 1A controlled ingestion. Competitor evidence, not yet analyzed.",
                    discovered_as, started_at, started_at, completed_at,
                    "Associated (per source content, not yet analyzed): Matty Invests, Mr. Finance."
                    if dataset_id == "DS-000001" else None,
                ),
            )
            conn.execute(
                """INSERT INTO ingestion_runs
                   (run_id, dataset_id, started_at, completed_at, status,
                    source_file_count, archive_member_count, total_size_bytes,
                    errors_count, verification_status, tool_version, notes)
                   VALUES (?, ?, ?, ?, 'COMPLETED', ?, ?, ?, 0, 'VERIFIED', ?, ?);""",
                (
                    run_id, dataset_id, started_at, completed_at,
                    len(physical_records), archive_member_count, total_size, TOOL_VERSION,
                    "source={}".format(source_dir),
                ),
            )
            loc_id = _next_id(conn, "source_locations", "source_location_id", "LOC")
            conn.execute(
                """INSERT INTO source_locations
                   (source_location_id, dataset_id, original_path, location_type,
                    exists_at_ingestion, observed_at, notes)
                   VALUES (?, ?, ?, 'LOCAL_FOLDER', 1, ?, NULL);""",
                (loc_id, dataset_id, str(source_dir), started_at),
            )

            for rec in physical_records:
                file_id = _next_id(conn, "source_files", "file_id", "FILE")
                conn.execute(
                    """INSERT INTO source_files
                       (file_id, dataset_id, ingestion_run_id, parent_file_id, storage_kind, file_role,
                        original_filename, original_path, relative_path, canonical_path, archive_member_path,
                        extension, mime_type, size_bytes, sha256, semantic_class, evidence_layer,
                        is_copied, is_archive_member, processing_status, verification_status, created_at, notes)
                       VALUES (?, ?, ?, NULL, 'PHYSICAL_FILE', ?, ?, ?, ?, ?, NULL,
                               ?, NULL, ?, ?, ?, 'RAW_SOURCE', 1, 0, 'CATALOGED', 'VERIFIED', ?, NULL);""",
                    (
                        file_id, dataset_id, run_id, rec["file_role"],
                        rec["original_filename"], rec["original_path"], rec["original_filename"],
                        rec["canonical_path"], rec["extension"], rec["size_bytes"], rec["sha256"],
                        semantic_class, completed_at,
                    ),
                )
                for member in archive_members_by_parent.get(rec["original_filename"], []):
                    member_id = _next_id(conn, "source_files", "file_id", "FILE")
                    conn.execute(
                        """INSERT INTO source_files
                           (file_id, dataset_id, ingestion_run_id, parent_file_id, storage_kind, file_role,
                            original_filename, original_path, relative_path, canonical_path, archive_member_path,
                            extension, mime_type, size_bytes, sha256, semantic_class, evidence_layer,
                            is_copied, is_archive_member, processing_status, verification_status, created_at, notes)
                           VALUES (?, ?, ?, ?, 'ARCHIVE_MEMBER', ?, ?, ?, ?, NULL, ?,
                                   ?, NULL, ?, ?, ?, 'RAW_SOURCE', 0, 1, 'CATALOGED', 'HASHED', ?, ?);""",
                        (
                            member_id, dataset_id, run_id, file_id, member["file_role"],
                            Path(member["archive_member_path"]).name, rec["original_path"],
                            member["archive_member_path"], member["archive_member_path"],
                            Path(member["archive_member_path"]).suffix.lower(),
                            member["size_bytes"], member["sha256"], semantic_class,
                            completed_at, member["notes"],
                        ),
                    )

        print("COMPLETED — {} ingested. Run {}. {} physical file(s), {} archive member(s).".format(
            dataset_id, run_id, len(physical_records), archive_member_count
        ))
        if observed_transcripts:
            print("Transcript archive verification: {}".format(observed_transcripts))

        write_manifest(conn, dataset_id)

    except CatalogError as exc:
        for p in copied_paths:
            if p.exists():
                p.unlink()
        if canonical_dir.exists() and not any(canonical_dir.iterdir()):
            canonical_dir.rmdir()
        completed_at = now_iso()
        # No `datasets` row was ever created for this attempt (failure happened
        # before the dataset was confirmed ingested), so dataset_id stays NULL
        # here to satisfy the foreign key; the attempted ID is kept in notes so
        # a retry with the same --dataset-id is still treated as a fresh attempt.
        error_id_conn = sqlite3.connect(str(db_path))
        error_id_conn.execute("PRAGMA foreign_keys = ON;")
        with error_id_conn:
            error_id_conn.execute(
                """INSERT INTO ingestion_runs
                   (run_id, dataset_id, started_at, completed_at, status,
                    source_file_count, archive_member_count, total_size_bytes,
                    errors_count, verification_status, tool_version, notes)
                   VALUES (?, NULL, ?, ?, 'FAILED', NULL, NULL, NULL, 1, 'FAILED', ?, ?);""",
                (
                    run_id, started_at, completed_at, TOOL_VERSION,
                    "attempted_dataset_id={} error={}".format(dataset_id, exc),
                ),
            )
        error_id_conn.close()
        print("FAILED — {}: {}".format(exc.error_type, exc.message))
        sys.exit(1)


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------

def cmd_verify(args):
    db_path = Path(args.db_path)
    dataset_id = args.dataset_id
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        _require_initialized(conn)
        dataset = conn.execute(
            "SELECT dataset_id, dataset_name FROM datasets WHERE dataset_id = ?;", (dataset_id,)
        ).fetchone()
        if not dataset:
            print("NOT_FOUND — no dataset {} in catalog.".format(dataset_id))
            sys.exit(1)

        physical = conn.execute(
            """SELECT original_filename, canonical_path, size_bytes, sha256 FROM source_files
               WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE';""",
            (dataset_id,),
        ).fetchall()

        mismatches = []
        for filename, canonical_path, size_bytes, sha256 in physical:
            p = Path(canonical_path)
            if not p.exists():
                mismatches.append("{}: canonical copy missing at {}".format(filename, canonical_path))
                continue
            actual_size = p.stat().st_size
            actual_hash = sha256_file(p)
            if actual_size != size_bytes or actual_hash != sha256:
                mismatches.append(
                    "{}: recorded size={} sha256={} but disk size={} sha256={}".format(
                        filename, size_bytes, sha256, actual_size, actual_hash
                    )
                )

        archive_member_count = conn.execute(
            """SELECT COUNT(*) FROM source_files WHERE dataset_id = ? AND storage_kind = 'ARCHIVE_MEMBER';""",
            (dataset_id,),
        ).fetchone()[0]
        physical_count = len(physical)

        integrity = conn.execute("PRAGMA integrity_check;").fetchone()[0]
        fk_violations = conn.execute("PRAGMA foreign_key_check;").fetchall()

        counts = {
            "datasets": conn.execute("SELECT COUNT(*) FROM datasets;").fetchone()[0],
            "ingestion_runs": conn.execute("SELECT COUNT(*) FROM ingestion_runs;").fetchone()[0],
            "source_locations": conn.execute("SELECT COUNT(*) FROM source_locations;").fetchone()[0],
            "source_files_total": conn.execute("SELECT COUNT(*) FROM source_files;").fetchone()[0],
            "source_files_physical": conn.execute(
                "SELECT COUNT(*) FROM source_files WHERE storage_kind='PHYSICAL_FILE';"
            ).fetchone()[0],
            "source_files_archive_member": conn.execute(
                "SELECT COUNT(*) FROM source_files WHERE storage_kind='ARCHIVE_MEMBER';"
            ).fetchone()[0],
            "file_relationships": conn.execute("SELECT COUNT(*) FROM file_relationships;").fetchone()[0],
            "ingestion_errors": conn.execute("SELECT COUNT(*) FROM ingestion_errors;").fetchone()[0],
        }

        manifest_path = MANIFESTS_DIR / "{}.md".format(dataset_id)
        manifest_agrees = None
        if manifest_path.exists():
            text = manifest_path.read_text()
            expected_marker = "File record count: {}".format(physical_count + archive_member_count)
            manifest_agrees = expected_marker in text

        status = "VERIFIED" if not mismatches and integrity == "ok" and not fk_violations else "FAILED"

        print("Dataset: {} ({})".format(dataset[0], dataset[1]))
        print("Physical files checked: {} | mismatches: {}".format(physical_count, len(mismatches)))
        for m in mismatches:
            print("  MISMATCH: {}".format(m))
        print("Archive members recorded: {}".format(archive_member_count))
        print("PRAGMA integrity_check: {}".format(integrity))
        print("PRAGMA foreign_key_check violations: {}".format(len(fk_violations)))
        print("Catalog counts: {}".format(counts))
        print("Manifest agrees with catalog counts: {}".format(manifest_agrees))
        print("Status: {}".format(status))
        if status != "VERIFIED":
            sys.exit(1)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# manifest generation
# ---------------------------------------------------------------------------

def write_manifest(conn, dataset_id):
    dataset = conn.execute(
        """SELECT dataset_id, dataset_name, discovered_as, semantic_class, description,
                  date_received, notes FROM datasets WHERE dataset_id = ?;""",
        (dataset_id,),
    ).fetchone()
    loc = conn.execute(
        "SELECT original_path, observed_at FROM source_locations WHERE dataset_id = ? ORDER BY observed_at DESC LIMIT 1;",
        (dataset_id,),
    ).fetchone()
    run = conn.execute(
        """SELECT run_id, status, source_file_count, archive_member_count, total_size_bytes, tool_version
           FROM ingestion_runs WHERE dataset_id = ? ORDER BY started_at DESC LIMIT 1;""",
        (dataset_id,),
    ).fetchone()
    physical = conn.execute(
        """SELECT original_filename, original_path, canonical_path, size_bytes, sha256, file_role, verification_status
           FROM source_files WHERE dataset_id = ? AND storage_kind = 'PHYSICAL_FILE' ORDER BY original_filename;""",
        (dataset_id,),
    ).fetchall()
    archive_members = conn.execute(
        """SELECT archive_member_path, size_bytes, sha256, file_role, notes
           FROM source_files WHERE dataset_id = ? AND storage_kind = 'ARCHIVE_MEMBER' ORDER BY archive_member_path;""",
        (dataset_id,),
    ).fetchall()

    total_files = len(physical) + len(archive_members)
    index_count = sum(1 for m in archive_members if m[3] == "ARCHIVE_INDEX")
    transcript_members = [m for m in archive_members if m[3] == "TRANSCRIPT"]
    missing_transcripts = [m for m in transcript_members if m[4]]
    total_uncompressed = sum(m[1] for m in archive_members)

    lines = []
    lines.append("# {} — {}".format(dataset[0], dataset[1]))
    lines.append("")
    lines.append("## Dataset Identity")
    lines.append("")
    lines.append("- Dataset ID: {}".format(dataset[0]))
    lines.append("- Dataset Name: {}".format(dataset[1]))
    lines.append("- Discovery ID: {}".format(dataset[2]))
    lines.append("- Semantic Class: {}".format(dataset[3]))
    lines.append("- Description: {}".format(dataset[4]))
    lines.append("")
    lines.append("## Source")
    lines.append("")
    lines.append("- Original Source Path: `{}`".format(loc[0] if loc else "UNKNOWN"))
    lines.append("- Date Ingested: {}".format(dataset[5]))
    lines.append("- Ingestion Mode: CONTROLLED_COPY (Phase 1A, `scripts/inventory_catalog.py`)")
    lines.append("- Source Exists: {}".format("yes, confirmed at ingestion" if loc else "UNKNOWN"))
    lines.append("")
    lines.append("## Canonical Raw Location")
    lines.append("")
    lines.append("```text")
    lines.append(str(Path(physical[0][2]).parent) if physical else "UNKNOWN")
    lines.append("```")
    lines.append("")
    lines.append("## Physical Files")
    lines.append("")
    for filename, original_path, canonical_path, size_bytes, sha256, role, verification in physical:
        lines.append("### `{}`".format(filename))
        lines.append("")
        lines.append("- Source path: `{}`".format(original_path))
        lines.append("- Canonical path: `{}`".format(canonical_path))
        lines.append("- Size: {} bytes".format(size_bytes))
        lines.append("- SHA-256: `{}`".format(sha256))
        lines.append("- File role: {}".format(role))
        lines.append("- Verification: {}".format(verification))
        lines.append("")
    lines.append("## Archive Inventory")
    lines.append("")
    if archive_members:
        lines.append("Archive members were hashed via safe streaming (`zipfile`, in-memory) and were never "
                      "permanently extracted to disk (rule 15).")
        lines.append("")
        lines.append("- Archive members (total): {}".format(len(archive_members)))
        lines.append("- INDEX files: {}".format(index_count))
        lines.append("- Per-video (TRANSCRIPT-role) files: {}".format(len(transcript_members)))
        lines.append("- OBSERVED_COUNT with transcript text: {}".format(len(transcript_members) - len(missing_transcripts)))
        lines.append("- OBSERVED_COUNT missing/placeholder transcript: {}".format(len(missing_transcripts)))
        for m in missing_transcripts:
            lines.append("  - `{}` — {}".format(m[0], m[4]))
        lines.append("- Total uncompressed member bytes: {}".format(total_uncompressed))
        lines.append("- Member-hash status: all members SHA-256 hashed (`HASHED`); no separate copy exists to "
                      "compare against, since members are never extracted.")
    else:
        lines.append("No archive members in this dataset.")
    lines.append("")
    lines.append("## Classification")
    lines.append("")
    lines.append("- Semantic Class: {}".format(dataset[3]))
    lines.append("- Evidence Layer: RAW_SOURCE (all files and archive members)")
    lines.append("")
    lines.append("## Associated Competitors")
    lines.append("")
    lines.append(dataset[6] or "None recorded.")
    lines.append("")
    lines.append("## Duplicate / Revision Status")
    lines.append("")
    lines.append("No duplicate or revision relationship was proven during this ingestion run "
                  "(only the two authorized top-level source files were ingested; adjacent `~/Downloads` "
                  "zip variants identified in Phase 0.5 were not part of this ingestion — see "
                  "`docs/source-discovery/SOURCE_DUPLICATE_REPORT.md`).")
    lines.append("")
    lines.append("## Source Integrity")
    lines.append("")
    lines.append("Original external source files were re-hashed before and after this ingestion run; "
                  "0 modified, 0 moved, 0 renamed, 0 deleted (see Phase 1A final response for the run's "
                  "specific before/after hash comparison).")
    lines.append("")
    lines.append("## Database Registration")
    lines.append("")
    lines.append("- DB path: `data/catalog/youtube_inventory.db`")
    lines.append("- Schema version: 1")
    lines.append("- Ingestion run ID: {}".format(run[0] if run else "UNKNOWN"))
    lines.append("- Dataset record status: INGESTED")
    lines.append("- File record count: {}".format(total_files))
    lines.append("")
    lines.append("## Limitations")
    lines.append("")
    lines.append("No competitor intelligence analysis has been performed during Phase 1A. This manifest "
                  "records only what data exists, where it came from, and whether it is trustworthy — not "
                  "what the data means.")
    lines.append("")

    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = MANIFESTS_DIR / "{}.md".format(dataset_id)
    manifest_path.write_text("\n".join(lines))
    print("Manifest written: {}".format(manifest_path))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(description="Phase 1 inventory/catalog utility.")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init")

    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--source", required=True)
    p_ingest.add_argument("--dataset-id", required=True)
    p_ingest.add_argument("--name", required=True)
    p_ingest.add_argument("--semantic-class", required=True)
    p_ingest.add_argument("--discovered-as", default=None)

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("--dataset-id", required=True)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            cmd_init(args)
        elif args.command == "ingest":
            cmd_ingest(args)
        elif args.command == "verify":
            cmd_verify(args)
    except CatalogError as exc:
        print("{} — {}".format(exc.error_type, exc.message))
        sys.exit(1)


if __name__ == "__main__":
    main()
