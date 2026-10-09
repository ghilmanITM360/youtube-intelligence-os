#!/usr/bin/env python3
"""Promote a validated local stage to a small, evidence-only intelligence index."""
import argparse
import hashlib
import json
import os
from pathlib import Path

from source_adapters.what_if_forensic_brain import TABLE_IDS, load_brain
from stage_what_if_forensics import (
    DEFAULT_OUTPUT as DEFAULT_STAGE, ROOT, StagingError, canonical_json,
    catalog_identities, stage,
)
from validate_what_if_source_contract import DEFAULT_CONTRACT, sha256

DEFAULT_OUTPUT = ROOT / "data/intelligence/channels/CH-000004/forensic-observation-index-v1.json"


def build_index(stage_dir, catalog_path):
    stage_dir = Path(stage_dir)
    manifest_path = stage_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["schema_version"] != "1" or manifest["rejected_rows"] != 0:
        raise StagingError("stage schema or rejection status is not promotable")
    if set(manifest["tables"]) != set(TABLE_IDS):
        raise StagingError("stage table set differs from canonical forensic types")
    catalog_ids = catalog_identities(catalog_path)
    identity_digest = hashlib.sha256(
        ("\n".join(sorted(catalog_ids)) + "\n").encode()).hexdigest()
    if identity_digest != manifest["catalog_identity_sha256"]:
        raise StagingError("catalog identity set changed since staging")
    videos = {}
    keys = set()
    totals = {}
    for table in TABLE_IDS:
        meta = manifest["tables"][table]
        if meta["file"] != f"{table}.jsonl":
            raise StagingError(f"unexpected stage file for {table}")
        path = stage_dir / meta["file"]
        if not path.is_file() or path.stat().st_size != meta["size_bytes"] or sha256(path) != meta["sha256"]:
            raise StagingError(f"changed or missing stage table: {table}")
        count = 0
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                row = json.loads(line)
                count += 1
                youtube_id = row["canonical_youtube_video_id"]
                if (row["source_table"] != table or youtube_id not in catalog_ids
                        or row["channel_id"] != "CH-000004"
                        or row["source_release"] != manifest["source_release"]
                        or row["transformation_version"] != manifest["transformation_version"]
                        or row["claim_kind"] != "SOURCE_DECLARED_FORENSIC_RECORD"
                        or not row["source_row_id"] or not row["source_reference"]):
                    raise StagingError(f"invalid stage identity or provenance: {table}:{count}")
                key = (row["source_release"], row["source_video_id"], table, row["source_row_id"])
                if key in keys:
                    raise StagingError(f"duplicate stage observation: {key}")
                keys.add(key)
                item = videos.setdefault(youtube_id, {
                    "youtube_video_id": youtube_id,
                    "source_video_id": row["source_video_id"],
                    "forensic_slug": row["forensic_slug"],
                    "source_media_sha256": row["source_media_sha256"],
                    "table_counts": {name: 0 for name in TABLE_IDS},
                    "example_source_references": {},
                })
                if (item["source_video_id"] != row["source_video_id"]
                        or item["forensic_slug"] != row["forensic_slug"]
                        or item["source_media_sha256"] != row["source_media_sha256"]):
                    raise StagingError(f"conflicting source identity: {youtube_id}")
                item["table_counts"][table] += 1
                item["example_source_references"].setdefault(table, row["source_reference"])
        if count != meta["rows"]:
            raise StagingError(f"stage row count mismatch: {table}")
        totals[table] = count
    if sum(totals.values()) != manifest["accepted_rows"] or len(videos) != manifest["accepted_sources"]:
        raise StagingError("stage accepted totals do not match manifest")
    return {
        "schema_version": "forensic-observation-index-1",
        "channel_id": "CH-000004",
        "source_release": manifest["source_release"],
        "source_contract": "data/manifests/what-if-forensic-source-v1.json",
        "source_release_manifest_sha256": manifest["source_release_manifest_sha256"],
        "staging_manifest_sha256": sha256(manifest_path),
        "staging_manifest_reference": "data/staging/what-if-forensic/v1.0.0/manifest.json",
        "evidence_state": "SOURCE_DECLARED_FORENSIC_RECORD",
        "video_count": len(videos),
        "observation_count": sum(totals.values()),
        "table_counts": totals,
        "videos": [videos[key] for key in sorted(videos)],
        "held_sources": manifest["excluded"],
        "interpretation_policy": "These are source-declared observations, not independently verified measurements or new channel samples. Existing editing blueprints are not regenerated.",
    }


def promote(stage_dir, catalog_path, output):
    payload = build_index(stage_dir, catalog_path)
    rendered = canonical_json(payload) + "\n"
    output = Path(output)
    if output.exists():
        if output.read_text(encoding="utf-8") != rendered:
            raise StagingError("PROMOTION_CONFLICT: existing index differs; review before replacement")
        return "UNCHANGED", payload
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    if temporary.exists():
        raise StagingError("temporary promotion file already exists")
    try:
        temporary.write_text(rendered, encoding="utf-8")
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    return "CREATED", payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, default=os.environ.get("YIOS_WHAT_IF_CORPUS_ROOT"))
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--catalog", type=Path, default=ROOT / "data/catalog/youtube_inventory.db")
    parser.add_argument("--stage", type=Path, default=DEFAULT_STAGE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.corpus_root is None:
        parser.error("set YIOS_WHAT_IF_CORPUS_ROOT or pass --corpus-root")
    try:
        stage_result = stage(load_brain(args.corpus_root, args.contract), args.catalog, args.stage)
        if stage_result["status"] not in {"CREATED", "UNCHANGED"}:
            raise StagingError("stage is not validated")
        status, payload = promote(args.stage, args.catalog, args.output)
    except (StagingError, OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f"promotion failed: {exc}\n")
    print(canonical_json({"status": status, "video_count": payload["video_count"],
                          "observation_count": payload["observation_count"],
                          "table_counts": payload["table_counts"]}))


if __name__ == "__main__":
    main()
