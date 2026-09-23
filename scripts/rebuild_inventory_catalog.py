#!/usr/bin/env python3
"""Rebuild a valid manifest-index inventory catalog from tracked evidence.

This creates a semantically useful catalog of datasets and manifest files.
It does not claim byte-identical recovery of historical operational rows whose
ignored raw sources are absent from a clean clone.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from scripts import inventory_catalog


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rebuild(root: Path, destination: Path) -> dict:
    manifests = sorted(
        path for path in (root / "data/manifests").glob("DS-*.md")
        if re.fullmatch(r"DS-\d{6}\.md", path.name)
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as directory:
        staged = Path(directory) / destination.name
        inventory_catalog.cmd_init(type("Args", (), {"db_path": str(staged)})())
        connection = sqlite3.connect(staged)
        connection.execute("PRAGMA foreign_keys=ON")
        created = _now()
        with connection:
            for index, manifest in enumerate(manifests, 1):
                dataset_id = manifest.stem
                text = manifest.read_text(encoding="utf-8")
                heading = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), dataset_id)
                run_id = f"REBUILD-{index:06d}"
                file_id = f"REBUILD-FILE-{index:06d}"
                relative = manifest.relative_to(root).as_posix()
                digest = hashlib.sha256(manifest.read_bytes()).hexdigest()
                connection.execute(
                    """INSERT INTO datasets
                       (dataset_id,dataset_name,semantic_class,description,source_type,ingestion_mode,status,
                        discovered_as,date_received,created_at,updated_at,notes)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (dataset_id, heading, "H", "Reconstructed from tracked durable manifest.", "MANIFEST",
                     "MANIFEST_RECONSTRUCTION", "MANIFEST_INDEXED", None, created, created, created,
                     "Operational/raw rows require their original ignored evidence and are not fabricated."),
                )
                connection.execute(
                    """INSERT INTO ingestion_runs
                       (run_id,dataset_id,started_at,completed_at,status,source_file_count,archive_member_count,
                        total_size_bytes,errors_count,verification_status,tool_version,notes,run_type)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (run_id, dataset_id, created, created, "COMPLETED", 1, 0, manifest.stat().st_size, 0,
                     "HASHED", "rebuild_inventory_catalog.py/1",
                     "Manifest-index reconstruction; not byte-identical historical recovery.", "FILE_INGESTION"),
                )
                connection.execute(
                    """INSERT INTO source_files
                       (file_id,dataset_id,ingestion_run_id,storage_kind,file_role,original_filename,original_path,
                        relative_path,canonical_path,extension,mime_type,size_bytes,sha256,semantic_class,
                        evidence_layer,is_copied,is_archive_member,processing_status,verification_status,created_at,notes)
                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (file_id, dataset_id, run_id, "PHYSICAL_FILE", "MANIFEST", manifest.name, relative,
                     relative, relative, ".md", "text/markdown", manifest.stat().st_size, digest, "H",
                     "DURABLE_MANIFEST", 0, 0, "REGISTERED", "HASHED", created,
                     "Tracked manifest indexes dataset identity and provenance."),
                )
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        schema_version = connection.execute("SELECT max(schema_version) FROM schema_meta").fetchone()[0]
        connection.close()
        if integrity != "ok" or foreign_keys:
            raise RuntimeError(f"Catalog validation failed: integrity={integrity}, foreign_keys={foreign_keys}")
        staged.replace(destination)
    return {"database": str(destination), "datasets": len(manifests), "schema_version": schema_version,
            "integrity_check": integrity, "foreign_key_violations": len(foreign_keys),
            "reproduction": "SEMANTIC_MANIFEST_INDEX_NOT_BYTE_IDENTICAL"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--database", type=Path)
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
    destination = args.database or root / "data/catalog/youtube_inventory.db"
    print(rebuild(root, destination.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
