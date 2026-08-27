#!/usr/bin/env python3
"""Phase 1C — recursive multi-source & multimodal batch registration.

Discovers every filesystem item inside the 12 authorized source roots,
hashes every file, assigns each item an explicit disposition (never silently
skipped — see schemas/inventory/003_multimodal_source_registration.sql), and
registers each resolved logical dataset through the same datasets /
ingestion_runs / source_files tables Phase 1A introduced. Stdlib only;
Pillow/Vision image work happens in separate subprocess helpers
(scripts/image_pipeline.py under .venv, scripts/image_text_recognition.swift)
so this script never needs anything beyond the standard library.

Usage:
  python3 scripts/register_batch.py discover [--dry-run]
  python3 scripts/register_batch.py register
  python3 scripts/register_batch.py verify --batch-id BATCH-000001
"""
import argparse
import hashlib
import json
import mimetypes
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import inventory_catalog as ic  # noqa: E402
from source_adapters import batch_rules as rules  # noqa: E402

DEFAULT_DB_PATH = ic.DEFAULT_DB_PATH
TOOL_VERSION = "register_batch.py/1"


def now_iso():
    return ic.now_iso()


# ---------------------------------------------------------------------------
# Discovery: walk every root, classify every entry, hash every file.
# ---------------------------------------------------------------------------

def sha256_file(path):
    return ic.sha256_file(path)


def classify_codex(relpath, is_dir):
    """Longest-prefix match against CODEX_RULES. relpath uses '/' separators
    and never a leading '/'. A TOOLING/NOISE directory-name match always
    wins, regardless of what dataset tree it happens to be nested inside.
    Falls back to NOISE for an unmatched directory (structural, never
    itself evidence) and HOLD for an unmatched file (never silently
    skipped — a signal to extend the rules, not a crash)."""
    basename = relpath.rsplit("/", 1)[-1]
    if basename == ".DS_Store":
        return "NOISE", None, "macOS Finder metadata file"
    if basename.startswith("._"):
        return "NOISE", None, "AppleDouble resource-fork sidecar file"

    segments = relpath.split("/")
    for name in segments:
        if name in rules.TOOLING_DIR_NAMES:
            return "TOOLING", None, "Nested dev-tool/cache directory ({}), not evidence".format(name)
        if name in rules.NOISE_DIR_NAMES:
            return "NOISE", None, "Nested junk/sidecar directory ({}), not evidence".format(name)

    best = None
    for prefix, disposition, dataset_key, reason in rules.CODEX_RULES:
        if relpath == prefix or relpath.startswith(prefix + "/"):
            if best is None or len(prefix) > len(best[0]):
                best = (prefix, disposition, dataset_key, reason)
    if best is None:
        if is_dir:
            return "NOISE", None, "Unmatched directory (structural, never itself evidence)"
        return "HOLD", None, "No batch rule matched this path — held for explicit human classification rather than guessed"
    _, disposition, dataset_key, reason = best
    if is_dir and disposition not in ("NOISE", "TOOLING", "SUPERSEDED", "HOLD"):
        return "NOISE", dataset_key, "Directory entry (structural) under: " + reason
    return disposition, dataset_key, reason


def walk_root(root_spec):
    """Yields dicts for every entry (FILE/DIR/SYMLINK) under root_spec['path'],
    never following symlinks. Computes sha256 for files only."""
    root_path = Path(root_spec["path"]).resolve()
    kind = root_spec["kind"]

    for dirpath, dirnames, filenames in os.walk(root_path, topdown=True, followlinks=False):
        dirpath_p = Path(dirpath)
        # Split dirnames into real dirs vs symlinked dirs (os.walk lists both
        # in dirnames but with followlinks=False it does not descend into
        # symlinked ones — we still need a discovered_files row for them).
        real_dirnames = []
        for name in list(dirnames):
            full = dirpath_p / name
            if full.is_symlink():
                yield _make_entry(root_spec, kind, full, root_path, "SYMLINK")
            else:
                real_dirnames.append(name)
                yield _make_entry(root_spec, kind, full, root_path, "DIR")
        dirnames[:] = real_dirnames

        for name in filenames:
            full = dirpath_p / name
            if full.is_symlink():
                yield _make_entry(root_spec, kind, full, root_path, "SYMLINK")
            else:
                yield _make_entry(root_spec, kind, full, root_path, "FILE")


def _make_entry(root_spec, kind, full_path, root_path, entry_type):
    relpath = full_path.relative_to(root_path).as_posix()
    size_bytes = None
    sha256 = None
    ext = None
    mime = None
    if entry_type == "FILE":
        try:
            size_bytes = full_path.stat().st_size
        except OSError:
            size_bytes = None
        ext = full_path.suffix.lower().lstrip(".") or None
        mime, _ = mimetypes.guess_type(str(full_path))
        try:
            sha256 = sha256_file(full_path)
        except OSError:
            sha256 = None

    if kind == "already_ingested":
        disposition, dataset_key, reason = "HOLD", None, "pending hash comparison against DS-000001"
    elif kind == "flat_dataset":
        if entry_type == "FILE":
            disposition, dataset_key, reason = "INGEST", root_spec["dataset_key"], "Flat single-dataset source folder"
        else:
            disposition, dataset_key, reason = "NOISE", root_spec["dataset_key"], "Directory entry (structural, not itself evidence)"
    elif kind == "codex":
        disposition, dataset_key, reason = classify_codex(relpath, entry_type == "DIR")
    else:
        raise ValueError("unknown root kind: {}".format(kind))

    return {
        "root_index": root_spec["index"],
        "entry_type": entry_type,
        "absolute_path": str(full_path),
        "relative_path": relpath,
        "extension": ext,
        "mime_type": mime,
        "size_bytes": size_bytes,
        "sha256": sha256,
        "disposition": disposition,
        "dataset_key": dataset_key,
        "reason": reason,
    }


# ---------------------------------------------------------------------------
# discover command — walk everything, resolve ROOT1 vs DS-000001, apply
# cross-root dedup, write the discovered_files ledger. No copying yet.
# ---------------------------------------------------------------------------

def cmd_discover(args):
    db_path = Path(args.db_path)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        ic._require_initialized(conn)
        batch_id = ic._next_id(conn, "source_batches", "batch_id", "BATCH")
        started_at = now_iso()

        all_entries = []
        root_stats = {}
        for root_spec in rules.ROOT_SPECS:
            path = Path(root_spec["path"])
            exists = path.exists()
            canonical = str(path.resolve()) if exists else None
            root_type = "DIR" if (exists and path.is_dir()) else ("FILE" if exists else None)
            entries = list(walk_root(root_spec)) if exists and root_type == "DIR" else []
            fcount = sum(1 for e in entries if e["entry_type"] == "FILE")
            dcount = sum(1 for e in entries if e["entry_type"] == "DIR")
            scount = sum(1 for e in entries if e["entry_type"] == "SYMLINK")
            total_size = sum(e["size_bytes"] or 0 for e in entries if e["entry_type"] == "FILE")
            root_stats[root_spec["index"]] = {
                "supplied_path": root_spec["path"],
                "canonical_path": canonical,
                "exists": exists,
                "root_type": root_type,
                "file_count": fcount,
                "dir_count": dcount,
                "symlink_count": scount,
                "total_size_bytes": total_size,
            }
            all_entries.extend(entries)
            print("ROOT {}: {} -> files={} dirs={} symlinks={} size={}B".format(
                root_spec["index"], root_spec["path"], fcount, dcount, scount, total_size))

        # --- ROOT 1: re-hash vs DS-000001, never re-ingest ---
        ds1_hashes = {
            row[0]: row[1]
            for row in conn.execute(
                "SELECT original_filename, sha256 FROM source_files "
                "WHERE dataset_id = 'DS-000001' AND storage_kind = 'PHYSICAL_FILE';"
            ).fetchall()
        }
        revision_detected = []
        for e in all_entries:
            if e["root_index"] != 1 or e["entry_type"] != "FILE":
                continue
            fname = Path(e["relative_path"]).name
            recorded = ds1_hashes.get(fname)
            if recorded is None:
                e["disposition"], e["reason"] = "UNSUPPORTED", "File not present in original DS-000001 ingestion record"
            elif recorded == e["sha256"]:
                e["disposition"], e["reason"] = "ALREADY_INGESTED", "Hash matches existing DS-000001 record exactly"
            else:
                e["disposition"], e["reason"] = "REVISION", "RevisionDetected: hash differs from recorded DS-000001 value"
                revision_detected.append(fname)

        if revision_detected:
            raise ic.CatalogError(
                "RevisionDetected",
                "ROOT 1 file(s) changed since Phase 1A ingestion, refusing to proceed: {}".format(revision_detected),
            )

        # --- cross-root exact-duplicate detection (evidence-bearing dispositions only) ---
        DEDUP_CANDIDATES = {"INGEST", "SUPPORTING_EVIDENCE", "SUPERSEDED"}
        by_hash = {}
        for idx, e in enumerate(all_entries):
            if e["entry_type"] != "FILE" or e["disposition"] not in DEDUP_CANDIDATES or not e["sha256"]:
                continue
            by_hash.setdefault(e["sha256"], []).append(idx)
        dup_of = {}
        for h, idxs in by_hash.items():
            if len(idxs) < 2:
                continue
            idxs_sorted = sorted(idxs, key=lambda i: (all_entries[i]["root_index"], all_entries[i]["relative_path"]))
            first = idxs_sorted[0]
            for i in idxs_sorted[1:]:
                all_entries[i]["disposition"] = "EXACT_DUPLICATE"
                all_entries[i]["reason"] = "Byte-identical (SHA-256) to another discovered file; all source locations preserved"
                dup_of[i] = first

        if args.dry_run:
            _print_coverage(all_entries)
            print("DRY RUN — no database writes performed.")
            return

        # --- persist: batch, roots, discovered_files ---
        with conn:
            conn.execute(
                "INSERT INTO source_batches (batch_id, batch_name, started_at, completed_at, status, root_count, tool_version, notes) "
                "VALUES (?, ?, ?, NULL, 'STARTED', ?, ?, ?);",
                (batch_id, "Phase 1C recursive multi-source & multimodal ingestion", started_at,
                 len(rules.ROOT_SPECS), TOOL_VERSION, None),
            )
            root_id_by_index = {}
            for root_spec in rules.ROOT_SPECS:
                idx = root_spec["index"]
                st = root_stats[idx]
                broot_id = ic._next_id(conn, "batch_roots", "batch_root_id", "BROOT")
                conn.execute(
                    "INSERT INTO batch_roots (batch_root_id, batch_id, root_index, supplied_path, canonical_path, "
                    "exists_at_discovery, root_type, file_count, dir_count, symlink_count, total_size_bytes, observed_at, notes) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (broot_id, batch_id, idx, st["supplied_path"], st["canonical_path"],
                     1 if st["exists"] else 0, st["root_type"], st["file_count"], st["dir_count"],
                     st["symlink_count"], st["total_size_bytes"], now_iso(), None),
                )
                root_id_by_index[idx] = broot_id

            discovered_ids = [None] * len(all_entries)
            rows = []
            for i, e in enumerate(all_entries):
                dfid = ic._next_id(conn, "discovered_files", "discovered_file_id", "DF")
                discovered_ids[i] = dfid
                rows.append((
                    dfid, batch_id, root_id_by_index[e["root_index"]], e["entry_type"], e["absolute_path"],
                    e["relative_path"], e["extension"], e["mime_type"], e["size_bytes"], e["sha256"],
                    None, None, e["disposition"], e["reason"], None, "RECORDED", now_iso(), None,
                ))
                # _next_id counts rows in the table; insert immediately so the
                # next call sees an incremented count (mirrors Phase 1A/1B's
                # existing _next_id usage pattern — no separate counter state).
                conn.execute(
                    "INSERT INTO discovered_files (discovered_file_id, batch_id, batch_root_id, entry_type, "
                    "absolute_path, relative_path, extension, mime_type, size_bytes, sha256, dataset_id, "
                    "source_file_id, disposition, disposition_reason, duplicate_of_discovered_file_id, "
                    "processing_status, created_at, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    rows[-1],
                )
            for i, first_idx in dup_of.items():
                conn.execute(
                    "UPDATE discovered_files SET duplicate_of_discovered_file_id = ? WHERE discovered_file_id = ?;",
                    (discovered_ids[first_idx], discovered_ids[i]),
                )

            conn.execute(
                "UPDATE source_batches SET completed_at = ?, status = 'COMPLETED' WHERE batch_id = ?;",
                (now_iso(), batch_id),
            )

        # Persist entries + id map for the register step.
        state = {
            "batch_id": batch_id,
            "entries": [dict(e, discovered_file_id=discovered_ids[i]) for i, e in enumerate(all_entries)],
        }
        state_path = ic.MANIFESTS_DIR / "batches" / (batch_id + "_state.json")
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(state))
        print("Batch {} discovery complete. {} entries recorded. State: {}".format(
            batch_id, len(all_entries), state_path))
        _print_coverage(all_entries)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# register command — allocate a real DS-id per resolved logical dataset,
# copy/reference canonical files, write source_files + dataset manifests.
# ---------------------------------------------------------------------------

def _dataset_meta(dataset_key):
    # Read rules.ROOT_SPECS/CODEX_DATASET_META live on every call (not cached
    # at import time) so tests can monkeypatch them, matching the same
    # redirectable-module-attribute pattern inventory_catalog.py already
    # uses for RAW_DATA_ROOT/MANIFESTS_DIR.
    flat_meta = {r["dataset_key"]: r for r in rules.ROOT_SPECS if r.get("kind") == "flat_dataset"}
    if dataset_key in flat_meta:
        m = flat_meta[dataset_key]
        return m["dataset_name"], m["semantic_class"], m["content_domain"], m["copy_mode"]
    m = rules.CODEX_DATASET_META[dataset_key]
    return m["dataset_name"], m["semantic_class"], m["content_domain"], m["copy_mode"]


def _should_copy(copy_mode, relative_path):
    if copy_mode == "COPY":
        return True
    if copy_mode == "REFERENCE":
        return False
    if copy_mode == "SELECTIVE_COPY":
        segments = relative_path.split("/")
        return not any(seg in rules.FRAME_DIR_MARKERS for seg in segments)
    raise ValueError("unknown copy_mode: {}".format(copy_mode))


def cmd_register(args):
    db_path = Path(args.db_path)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        ic._require_initialized(conn)
        state_path = ic.MANIFESTS_DIR / "batches" / (args.batch_id + "_state.json")
        state = json.loads(state_path.read_text())
        entries = state["entries"]

        by_key = {}
        for e in entries:
            k = e.get("dataset_key")
            if k:
                by_key.setdefault(k, []).append(e)

        summary = []
        for dataset_key in rules.REGISTRATION_ORDER:
            group = by_key.get(dataset_key, [])
            file_entries = [e for e in group if e["entry_type"] == "FILE"
                             and e["disposition"] in ("INGEST", "SUPPORTING_EVIDENCE", "SUPERSEDED")]
            if not file_entries:
                print("WARNING: no registerable entries found for dataset_key {}".format(dataset_key))
                continue
            existing = conn.execute(
                "SELECT dataset_id FROM datasets WHERE discovered_as = ?;", (dataset_key,)
            ).fetchone()
            if existing:
                print("{} already registered as {} — skipping (idempotent).".format(dataset_key, existing[0]))
                summary.append((dataset_key, existing[0], "ALREADY_REGISTERED"))
                continue
            dataset_id = _register_one_dataset(conn, db_path, args.batch_id, dataset_key, file_entries)
            summary.append((dataset_key, dataset_id, "REGISTERED"))

        print("")
        print("Registration summary:")
        for dataset_key, dataset_id, status in summary:
            print("  {} -> {} [{}]".format(dataset_key, dataset_id, status))
    finally:
        conn.close()


def _register_one_dataset(conn, db_path, batch_id, dataset_key, file_entries):
    dataset_name, semantic_class, content_domain, copy_mode = _dataset_meta(dataset_key)
    dataset_id = ic._next_id(conn, "datasets", "dataset_id", "DS")
    run_id = ic._next_id(conn, "ingestion_runs", "run_id", "RUN")
    started_at = now_iso()
    status = "HELD_FOR_REVIEW" if copy_mode == "REFERENCE" and semantic_class == "H" else "INGESTED"

    raw_dir_name = ic.CLASS_TO_RAW_DIR.get(semantic_class.upper(), "uncategorized")
    canonical_root = ic.RAW_DATA_ROOT / raw_dir_name / dataset_id

    records = []
    total_size = 0
    for e in file_entries:
        do_copy = _should_copy(copy_mode, e["relative_path"])
        canonical_path = None
        if do_copy:
            dest = canonical_root / e["relative_path"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(e["absolute_path"], dest)
            copy_hash = sha256_file(dest)
            if copy_hash != e["sha256"]:
                raise ic.CatalogError(
                    "HashFailure",
                    "Canonical copy hash mismatch for {}: source={} copy={}".format(
                        e["relative_path"], e["sha256"], copy_hash),
                )
            canonical_path = str(dest)
        total_size += e["size_bytes"] or 0
        records.append((e, canonical_path, do_copy))

    completed_at = now_iso()
    with conn:
        conn.execute(
            "INSERT INTO datasets (dataset_id, dataset_name, semantic_class, description, source_type, "
            "ingestion_mode, status, discovered_as, date_received, created_at, updated_at, notes) "
            "VALUES (?, ?, ?, ?, 'EXTERNAL_FOLDER', ?, ?, ?, ?, ?, ?, ?);",
            (dataset_id, dataset_name, semantic_class,
             "Phase 1C bulk multi-source ingestion ({}). Not yet analyzed.".format(batch_id),
             copy_mode, status, dataset_key, started_at, started_at, completed_at,
             "content_domain={}".format(content_domain) if content_domain else None),
        )
        conn.execute(
            "INSERT INTO ingestion_runs (run_id, dataset_id, started_at, completed_at, status, "
            "source_file_count, archive_member_count, total_size_bytes, errors_count, verification_status, "
            "tool_version, notes, run_type) VALUES (?, ?, ?, ?, 'COMPLETED', ?, 0, ?, 0, 'VERIFIED', ?, ?, 'FILE_INGESTION');",
            (run_id, dataset_id, started_at, completed_at, len(records), total_size, TOOL_VERSION,
             "batch={} dataset_key={} copy_mode={}".format(batch_id, dataset_key, copy_mode)),
        )
        loc_id = ic._next_id(conn, "source_locations", "source_location_id", "LOC")
        conn.execute(
            "INSERT INTO source_locations (source_location_id, dataset_id, original_path, location_type, "
            "exists_at_ingestion, observed_at, notes) VALUES (?, ?, ?, 'LOCAL_FOLDER', 1, ?, NULL);",
            (loc_id, dataset_id, os.path.dirname(records[0][0]["absolute_path"]) if records else "", started_at),
        )
        for e, canonical_path, do_copy in records:
            file_id = ic._next_id(conn, "source_files", "file_id", "FILE")
            conn.execute(
                "INSERT INTO source_files (file_id, dataset_id, ingestion_run_id, parent_file_id, storage_kind, "
                "file_role, original_filename, original_path, relative_path, canonical_path, archive_member_path, "
                "extension, mime_type, size_bytes, sha256, semantic_class, evidence_layer, is_copied, "
                "is_archive_member, processing_status, verification_status, created_at, notes) "
                "VALUES (?, ?, ?, NULL, 'PHYSICAL_FILE', ?, ?, ?, ?, ?, NULL, ?, ?, ?, ?, ?, 'RAW_SOURCE', ?, 0, "
                "'CATALOGED', 'VERIFIED', ?, ?);",
                (file_id, dataset_id, run_id, e["disposition"], Path(e["relative_path"]).name,
                 e["absolute_path"], e["relative_path"], canonical_path, e["extension"], e["mime_type"],
                 e["size_bytes"], e["sha256"], semantic_class, 1 if do_copy else 0, completed_at,
                 e["reason"]),
            )
            conn.execute(
                "UPDATE discovered_files SET dataset_id = ?, source_file_id = ? WHERE discovered_file_id = ?;",
                (dataset_id, file_id, e["discovered_file_id"]),
            )
    print("{} -> {} ({} files, {} bytes, copy_mode={}, {} copied)".format(
        dataset_key, dataset_id, len(records), total_size, copy_mode, sum(1 for _, _, c in records if c)))
    return dataset_id


# ---------------------------------------------------------------------------
# images command — Layer 1 (Pillow metadata + dhash) for every discovered
# image that survived dedup, then a lightweight perceptual/temporal cluster
# pass for the Codex forensic-video frame datasets only (not the flat
# competitor-screenshot datasets, where every screenshot is already its own
# distinct capture, not a video-frame sequence).
# ---------------------------------------------------------------------------

VENV_PYTHON = str(REPO_ROOT / ".venv" / "bin" / "python3")
IMAGE_PIPELINE = str(REPO_ROOT / "scripts" / "image_pipeline.py")
CODEX_FRAME_DATASET_KEYS = {
    "CODEX_SUNSET_V1", "CODEX_MOON_PROTONS", "CODEX_WEIRD_WORRYING",
    "CODEX_SUNSET_V2", "CODEX_RETIREE_ROUTINES",
}


def _hamming(a_hex, b_hex):
    return bin(int(a_hex, 16) ^ int(b_hex, 16)).count("1")


def cmd_images(args):
    import subprocess

    db_path = Path(args.db_path)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        rows = conn.execute(
            "SELECT discovered_file_id, dataset_id, absolute_path, sha256 FROM discovered_files "
            "WHERE batch_id = ? AND entry_type = 'FILE' AND disposition IN ('INGEST', 'SUPPORTING_EVIDENCE') "
            "AND lower(extension) IN ('jpg', 'jpeg', 'png') AND dataset_id IS NOT NULL;",
            (args.batch_id,),
        ).fetchall()
        already = {r[0] for r in conn.execute(
            "SELECT discovered_file_id FROM visual_assets;"
        ).fetchall()}
        todo = [r for r in rows if r[0] not in already]
        print("Images to process: {} (already done: {})".format(len(todo), len(already)))
        if not todo:
            return

        proc = subprocess.Popen(
            [VENV_PYTHON, IMAGE_PIPELINE, "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1,
        )
        stdin_text = "\n".join(r[2] for r in todo) + "\n"
        out, _ = proc.communicate(stdin_text)
        out_lines = out.splitlines()
        if len(out_lines) != len(todo):
            raise ic.CatalogError(
                "ExtractionFailure",
                "image_pipeline.py --batch returned {} lines for {} inputs".format(len(out_lines), len(todo)),
            )

        errors = 0
        with conn:
            for (discovered_file_id, dataset_id, abs_path, sha256), line in zip(todo, out_lines):
                result = json.loads(line)
                if "error" in result:
                    errors += 1
                    err_id = ic._next_id(conn, "ingestion_errors", "error_id", "ERR")
                    run = conn.execute(
                        "SELECT run_id FROM ingestion_runs WHERE dataset_id = ? ORDER BY run_id DESC LIMIT 1;",
                        (dataset_id,),
                    ).fetchone()
                    conn.execute(
                        "INSERT INTO ingestion_errors (error_id, run_id, dataset_id, file_id, error_type, severity, "
                        "message, retryable, requires_human_review, created_at, resolved_at, notes) "
                        "VALUES (?, ?, ?, NULL, 'ExtractionFailure', 'Medium', ?, 1, 0, ?, NULL, ?);",
                        (err_id, run[0] if run else None, dataset_id, result["error"], now_iso(), abs_path),
                    )
                    continue
                va_id = ic._next_id(conn, "visual_assets", "visual_asset_id", "VA")
                conn.execute(
                    "INSERT INTO visual_assets (visual_asset_id, discovered_file_id, dataset_id, sha256, "
                    "width_px, height_px, color_mode, image_format, orientation, exif_json, perceptual_hash, "
                    "perceptual_hash_algorithm, frame_sequence_id, frame_index, visual_state_cluster_id, "
                    "created_at, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, ?, NULL);",
                    (va_id, discovered_file_id, dataset_id, sha256, result["width_px"], result["height_px"],
                     result["color_mode"], result["image_format"], result["orientation"],
                     json.dumps(result["exif"]), result["dhash"], result["dhash_algorithm"], now_iso()),
                )
        print("Inserted {} visual_assets rows ({} extraction errors logged).".format(len(todo) - errors, errors))

        # --- perceptual/temporal clustering for Codex frame datasets ---
        for dataset_key in CODEX_FRAME_DATASET_KEYS:
            ds = conn.execute("SELECT dataset_id FROM datasets WHERE discovered_as = ?;", (dataset_key,)).fetchone()
            if not ds:
                continue
            dataset_id = ds[0]
            seq_rows = conn.execute(
                "SELECT va.visual_asset_id, va.perceptual_hash, df.relative_path FROM visual_assets va "
                "JOIN discovered_files df ON df.discovered_file_id = va.discovered_file_id "
                "WHERE va.dataset_id = ? ORDER BY df.relative_path;",
                (dataset_id,),
            ).fetchall()
            if not seq_rows:
                continue
            HAMMING_THRESHOLD = 6
            seq_id = "FSEQ-{}".format(dataset_id)
            cluster_idx = 0
            cluster_id = "{}-CLUSTER-{:04d}".format(dataset_id, cluster_idx)
            prev_hash = None
            with conn:
                for idx, (va_id, phash, relpath) in enumerate(seq_rows):
                    if prev_hash is not None and _hamming(prev_hash, phash) > HAMMING_THRESHOLD:
                        cluster_idx += 1
                        cluster_id = "{}-CLUSTER-{:04d}".format(dataset_id, cluster_idx)
                    conn.execute(
                        "UPDATE visual_assets SET frame_sequence_id = ?, frame_index = ?, visual_state_cluster_id = ? "
                        "WHERE visual_asset_id = ?;",
                        (seq_id, idx, cluster_id, va_id),
                    )
                    prev_hash = phash
            print("{}: {} frames -> {} visual-state clusters".format(dataset_key, len(seq_rows), cluster_idx + 1))
    finally:
        conn.close()


def _print_coverage(entries):
    total = len(entries)
    by_disp = {}
    for e in entries:
        by_disp[e["disposition"]] = by_disp.get(e["disposition"], 0) + 1
    print("TOTAL_DISCOVERED_FILES (all entry types) = {}".format(total))
    print("TOTAL_FILES_WITH_DISPOSITION = {}".format(sum(by_disp.values())))
    for disp in sorted(by_disp):
        print("  {}: {}".format(disp, by_disp[disp]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH))
    sub = parser.add_subparsers(dest="command", required=True)

    p_discover = sub.add_parser("discover")
    p_discover.add_argument("--dry-run", action="store_true")
    p_discover.set_defaults(func=cmd_discover)

    p_register = sub.add_parser("register")
    p_register.add_argument("--batch-id", required=True)
    p_register.set_defaults(func=cmd_register)

    p_images = sub.add_parser("images")
    p_images.add_argument("--batch-id", required=True)
    p_images.set_defaults(func=cmd_images)

    args = parser.parse_args()
    try:
        args.func(args)
    except ic.CatalogError as exc:
        print("FAILED — {}: {}".format(exc.error_type, exc.message))
        sys.exit(1)
