"""Read-only adapter for the canonical What If forensic brain release.

Only the release manifest, source index/map, and eight canonical master tables
are read. MP4s are hashed by the source-contract validator, never imported.
"""
import argparse
import csv
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_what_if_source_contract import (
    ContractError, DEFAULT_CONTRACT, safe_path, sha256, validate,
)

TABLE_IDS = {
    "MASTER_WORDS": "WORD_ID",
    "MASTER_SENTENCES": "SENTENCE_ID",
    "MASTER_SHOTS": "SHOT_ID",
    "MASTER_STATES": "STATE_ID",
    "MASTER_MOTIONS": "MOTION_ID",
    "MASTER_ASSETS": "ASSET_ID",
    "MASTER_AUDIO_EVENTS": "AUDIO_EVENT_ID",
    "MASTER_AUDIO_VISUAL_SYNC": "SYNC_ID",
}


def load_brain(corpus_root, contract_path=DEFAULT_CONTRACT):
    """Return verified canonical rows; never writes to the corpus or catalog."""
    corpus_root = Path(corpus_root).resolve()
    contract_path = Path(contract_path)
    summary = validate(contract_path, corpus_root)
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    brain = safe_path(corpus_root, contract["brain_relative_path"])
    release = json.loads((brain / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
    files = {}
    for item in release["files"]:
        relative = item["relative_path"]
        if relative in files:
            raise ContractError(f"duplicate release path: {relative}")
        files[relative] = item
    slugs = {source["forensic_slug"] for source in contract["sources"]}
    if len(slugs) != len(contract["sources"]):
        raise ContractError("duplicate forensic slug in source crosswalk")
    tables = {}
    for table, local_id in TABLE_IDS.items():
        relative = f"01_master_data/{table}.csv"
        entry = files.get(relative)
        if not entry or entry.get("canonical") is not True:
            raise ContractError(f"missing canonical release table: {relative}")
        path = safe_path(brain, relative)
        if not path.is_file() or path.stat().st_size != entry["size_bytes"] or sha256(path) != entry["sha256"]:
            raise ContractError(f"release table missing or changed: {relative}")
        with path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            if not reader.fieldnames or not {"VIDEO_SLUG", local_id}.issubset(reader.fieldnames):
                raise ContractError(f"missing required columns in {relative}")
            rows = list(reader)
        seen = set()
        for row_number, row in enumerate(rows, start=2):
            slug, identifier = row["VIDEO_SLUG"], row[local_id]
            if slug not in slugs or not identifier:
                raise ContractError(f"unknown slug or missing ID at {relative}:{row_number}")
            key = (slug, identifier)
            if key in seen:
                raise ContractError(f"duplicate local row ID in {relative}: {key}")
            seen.add(key)
        tables[table] = rows
    return {"summary": summary, "contract": contract, "tables": tables}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, default=os.environ.get("YIOS_WHAT_IF_CORPUS_ROOT"))
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    args = parser.parse_args()
    if args.corpus_root is None:
        parser.error("set YIOS_WHAT_IF_CORPUS_ROOT or pass --corpus-root")
    try:
        result = load_brain(args.corpus_root, args.contract)
    except (ContractError, OSError, KeyError, ValueError) as exc:
        parser.exit(1, f"forensic release invalid: {exc}\n")
    print(json.dumps({"source_release": result["summary"]["source_release"],
                      "sources": result["summary"]["sources"],
                      "tables": {key: len(value) for key, value in result["tables"].items()}},
                     sort_keys=True))


if __name__ == "__main__":
    main()
