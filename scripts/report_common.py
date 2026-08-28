"""Shared helpers for the read-only corpus status reporting scripts:
report_corpus_status.py, report_channel_coverage.py, report_dataset_matrix.py.

These scripts only SELECT from the existing catalog (data/catalog/youtube_inventory.db)
and the manifests it was generated from. No ingestion, no schema changes, no writes,
no competitor strategy analysis, no topic recommendations — read-only reporting only.
"""
import json
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import inventory_catalog as ic  # noqa: E402


def connect(db_path=None):
    conn = sqlite3.connect(str(db_path or ic.DEFAULT_DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def md_table(headers, rows):
    """rows: iterable of sequences, aligned with headers. None renders as empty cell."""
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join("" if v is None else str(v) for v in row) + " |")
    return lines


def emit(payload, markdown_lines, as_json):
    """payload: JSON-serializable dict for --json. markdown_lines: list[str] for the
    human-readable report. Exactly one is printed, so both output modes stay in sync
    with the same underlying query results (built by the same caller)."""
    if as_json:
        print(json.dumps(payload, indent=2, default=str))
    else:
        print("\n".join(markdown_lines))
