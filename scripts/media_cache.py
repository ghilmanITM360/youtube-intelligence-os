#!/usr/bin/env python3
"""Build and consume the checksum-verified, selective YIOS media manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


FIELDS = [
    "source_channel", "video_id", "asset_type", "relative_path", "byte_count",
    "sha256", "rights_status", "github_release_tag", "github_asset_name",
]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def load_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def select(rows: list[dict[str, str]], channel: str | None, video_id: str | None) -> list[dict[str, str]]:
    selected = [
        row for row in rows
        if (channel is not None and row["source_channel"].casefold() == channel.casefold())
        or (video_id is not None and row["video_id"] == video_id)
    ]
    if not selected:
        raise SystemExit("no manifest entry matched the requested channel or Video ID")
    return selected


def verified(path: Path, row: dict[str, str]) -> bool:
    return path.is_file() and path.stat().st_size == int(row["byte_count"]) and digest(path) == row["sha256"]


def build_manifest(inventory: Path, output: Path) -> None:
    records = [json.loads(line) for line in inventory.read_text(encoding="utf-8").splitlines()]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for record in records:
            writer.writerow({
                "source_channel": record["source_channel"],
                "video_id": record["video_id"],
                "asset_type": record["asset_type"],
                "relative_path": record["original_relative_path"],
                "byte_count": record["byte_count"],
                "sha256": record["sha256"],
                "rights_status": record["rights_access_classification"],
                "github_release_tag": "",
                "github_asset_name": "",
            })
    print(f"wrote {len(records)} entries to {output}")


def cache_path(cache_root: Path, row: dict[str, str]) -> Path:
    return cache_root / row["relative_path"]


def fetch(rows: list[dict[str, str]], cache_root: Path, media_root: Path | None, repository: str) -> None:
    for row in rows:
        destination = cache_path(cache_root, row)
        if verified(destination, row):
            print(f"verified cached: {destination}")
            continue
        source = media_root / row["relative_path"] if media_root else None
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="yios-media-fetch-", dir=destination.parent) as temporary:
            staged = Path(temporary) / destination.name
            if source and source.is_file():
                shutil.copyfile(source, staged)
            elif row["github_release_tag"] and row["github_asset_name"]:
                subprocess.run([
                    "gh", "release", "download", row["github_release_tag"], "--repo", repository,
                    "--pattern", row["github_asset_name"], "--output", str(staged),
                ], check=True)
            else:
                raise SystemExit(
                    f"no authorized source for {row['relative_path']}; remote upload is not configured"
                )
            if not verified(staged, row):
                raise SystemExit(f"checksum or size mismatch: {row['relative_path']}")
            os.replace(staged, destination)
        print(f"fetched and verified: {destination}")


def purge(rows: list[dict[str, str]], cache_root: Path) -> None:
    root = cache_root.resolve()
    for row in rows:
        target = cache_path(root, row).resolve()
        if root not in target.parents:
            raise SystemExit(f"refusing cache escape: {target}")
        if target.is_file():
            target.unlink()
            print(f"removed cache file: {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("build-manifest", "fetch", "verify", "purge"))
    parser.add_argument("--manifest", type=Path, default=Path("research/media-library/REMOTE_MEDIA_MANIFEST.csv"))
    parser.add_argument("--inventory", type=Path, default=Path("research/media-library/SOURCE_INVENTORY.jsonl"))
    parser.add_argument("--channel")
    parser.add_argument("--video-id")
    parser.add_argument("--media-root", type=Path, default=Path(os.environ["YIOS_MEDIA_ROOT"]) if os.environ.get("YIOS_MEDIA_ROOT") else None)
    parser.add_argument("--cache-root", type=Path, default=Path(os.environ.get("YIOS_MEDIA_CACHE", ".cache/yios-media")))
    parser.add_argument("--repository", default="ghilmanITM360/youtube-intelligence-os")
    args = parser.parse_args()
    if args.action == "build-manifest":
        build_manifest(args.inventory, args.manifest)
        return 0
    if bool(args.channel) == bool(args.video_id):
        parser.error("provide exactly one of --channel or --video-id")
    rows = select(load_manifest(args.manifest), args.channel, args.video_id)
    if args.action == "fetch":
        fetch(rows, args.cache_root, args.media_root, args.repository)
    elif args.action == "verify":
        failures = [row["relative_path"] for row in rows if not verified(cache_path(args.cache_root, row), row)]
        print(json.dumps({"selected": len(rows), "verified": len(rows) - len(failures), "failures": failures}, indent=2))
        return 1 if failures else 0
    else:
        purge(rows, args.cache_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
