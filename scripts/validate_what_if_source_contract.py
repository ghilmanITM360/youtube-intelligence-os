#!/usr/bin/env python3
"""Validate the external What If v1 forensic release and YIOS identity crosswalk.

The corpus is read only. Its old ABSOLUTE_PATH values are deliberately ignored.
"""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path

DEFAULT_CONTRACT = Path(__file__).resolve().parents[1] / "data" / "manifests" / "what-if-forensic-source-v1.json"


class ContractError(ValueError):
    pass


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def safe_path(root, relative):
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ContractError(f"path escapes corpus root: {relative}")
    return candidate


def csv_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def validate(contract_path, corpus_root):
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    brain = corpus_root / contract["brain_relative_path"]
    release_path = safe_path(brain, "RELEASE_MANIFEST.json")
    if sha256(release_path) != contract["release_manifest_sha256"]:
        raise ContractError("release manifest hash mismatch")
    release = json.loads(release_path.read_text(encoding="utf-8"))
    if release["release_version"] != contract["source_release"]:
        raise ContractError("source release mismatch")
    release_files = {item["relative_path"]: item for item in release["files"]}
    for name, expected in contract["source_artifact_sha256"].items():
        actual = safe_path(brain, name)
        if not actual.is_file() or sha256(actual) != expected:
            raise ContractError(f"source artifact missing or changed: {name}")
        entry = release_files.get(name)
        if entry is None or entry["sha256"] != expected:
            raise ContractError(f"source artifact not in release: {name}")

    index = csv_rows(brain / "SOURCE_VIDEO_INDEX.csv")
    mapping = csv_rows(brain / "SOURCE_TO_FORENSIC_MAP.csv")
    entries = contract["sources"]
    if len(index) != 14 or len(mapping) != 14 or len(entries) != 14:
        raise ContractError("expected exactly 14 source rows in index, map, and contract")
    def unique(rows, key):
        values = [row[key] for row in rows]
        if len(set(values)) != len(values):
            raise ContractError(f"duplicate {key}")
        return {row[key]: row for row in rows}
    indexed = unique(index, "SOURCE_VIDEO_ID")
    mapped = unique(mapping, "SOURCE_VIDEO_ID")
    crosswalk = unique(entries, "source_video_id")
    if set(indexed) != set(mapped) or set(indexed) != set(crosswalk):
        raise ContractError("source IDs differ between index, map, and contract")
    canonical_ids = []
    for source_id, entry in crosswalk.items():
        source = indexed[source_id]
        source_map = mapped[source_id]
        filename = source["FILENAME"]
        if entry["filename"] != filename or source_map["SOURCE_FILENAME"] != filename:
            raise ContractError(f"filename mismatch: {source_id}")
        if entry["forensic_slug"] != source_map["VIDEO_SLUG"]:
            raise ContractError(f"forensic slug mismatch: {source_id}")
        if entry["relative_media_path"] != f"videos/{filename}":
            raise ContractError(f"unexpected media path: {source_id}")
        if entry["sha256"] != source["SHA256"] or entry["size_bytes"] != int(source["FILE_SIZE_BYTES"]):
            raise ContractError(f"source index mismatch: {source_id}")
        media = safe_path(corpus_root, entry["relative_media_path"])
        if not media.is_file():
            raise ContractError(f"missing media: {source_id}")
        if media.stat().st_size != entry["size_bytes"] or sha256(media) != entry["sha256"]:
            raise ContractError(f"media hash or size mismatch: {source_id}")
        state = entry["mapping_status"]
        candidate = entry["candidate_youtube_video_id"]
        canonical = entry["canonical_youtube_video_id"]
        if state not in {"VERIFIED", "UNRESOLVED", "REJECTED"}:
            raise ContractError(f"invalid mapping status: {source_id}")
        if state == "VERIFIED":
            if not canonical or canonical != candidate or not entry["mapping_evidence"]:
                raise ContractError(f"verified mapping lacks independent evidence: {source_id}")
            canonical_ids.append(canonical)
        elif canonical is not None:
            raise ContractError(f"unverified source has canonical ID: {source_id}")
    if len(canonical_ids) != len(set(canonical_ids)):
        raise ContractError("duplicate canonical assignment")
    return {"source_release": contract["source_release"], "sources": len(entries),
            "hashes_passed": len(entries), "verified": len(canonical_ids),
            "unresolved": sum(e["mapping_status"] == "UNRESOLVED" for e in entries),
            "rejected": sum(e["mapping_status"] == "REJECTED" for e in entries)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--corpus-root", type=Path, default=os.environ.get("YIOS_WHAT_IF_CORPUS_ROOT"))
    args = parser.parse_args()
    if args.corpus_root is None:
        parser.error("set YIOS_WHAT_IF_CORPUS_ROOT or pass --corpus-root")
    try:
        print(json.dumps(validate(args.contract, args.corpus_root.resolve()), sort_keys=True))
    except (ContractError, OSError, KeyError, ValueError) as exc:
        parser.exit(1, f"source contract invalid: {exc}\n")


if __name__ == "__main__":
    main()
