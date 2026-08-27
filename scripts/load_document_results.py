#!/usr/bin/env python3
"""One-off loader: reads a subagent's per-document characterization JSON
(schema: {"dataset_id": "DS-...", "documents": [...], "hook_pair_comparison": {...}})
and inserts one document_records row per document. Idempotent per
discovered_file (skips a document already loaded).
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
        print("usage: load_document_results.py <json_file>", file=sys.stderr)
        sys.exit(2)
    data = json.loads(Path(sys.argv[1]).read_text())
    dataset_id = data["dataset_id"]

    conn = sqlite3.connect(str(ic.DEFAULT_DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON;")

    already = {
        r[0] for r in conn.execute(
            "SELECT df.relative_path FROM document_records dr "
            "JOIN discovered_files df ON df.discovered_file_id = dr.discovered_file_id "
            "WHERE dr.dataset_id = ?;", (dataset_id,)
        ).fetchall()
    }

    inserted = 0
    missing = []
    with conn:
        for doc in data["documents"]:
            fname = doc["file_name"]
            if doc.get("document_type") == "REMOVE_DUPLICATE":
                continue  # accidental duplicate entry in the source JSON
            row = conn.execute(
                "SELECT df.discovered_file_id FROM discovered_files df "
                "WHERE df.dataset_id = ? AND df.relative_path = ?;",
                (dataset_id, fname),
            ).fetchone()
            if not row:
                missing.append(fname)
                continue
            discovered_file_id = row[0]
            if fname in already:
                continue
            notes = None
            if data.get("hook_pair_comparison") and fname in (
                data["hook_pair_comparison"].get("file_a"), data["hook_pair_comparison"].get("file_b")
            ):
                hp = data["hook_pair_comparison"]
                notes = "HOOK_PAIR_RELATIONSHIP={}: {}".format(hp["relationship"], hp["reasoning"])
            doc_id = ic._next_id(conn, "document_records", "document_id", "DOC")
            conn.execute(
                "INSERT INTO document_records (document_id, discovered_file_id, dataset_id, title, "
                "document_type, subject, knowledge_domains, evidence_type, authorship, "
                "ai_generated_indicators, relationship_notes, priority, revision_status, content_read, "
                "created_at, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?);",
                (doc_id, discovered_file_id, dataset_id, doc.get("title"), doc.get("document_type"),
                 doc.get("subject"), json.dumps(doc.get("knowledge_domains", [])), doc.get("evidence_type"),
                 doc.get("source_or_authorship_if_explicit"), doc.get("ai_generated_or_compiled_indicators"),
                 doc.get("relationship_to_other_docs"), doc.get("priority"), doc.get("revision_status"),
                 ic.now_iso(), notes),
            )
            inserted += 1
    print("dataset={} inserted={} missing={}".format(dataset_id, inserted, len(missing)))
    for m in missing:
        print("  MISSING discovered_file for:", m)


if __name__ == "__main__":
    main()
