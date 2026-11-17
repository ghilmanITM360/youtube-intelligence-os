#!/usr/bin/env python3
"""Inventory and optionally ingest user-supplied local channel media.

Raw media remain private and Git-ignored. The generated manifests are small,
reproducible text artifacts that preserve provenance and expose stable
project-relative paths to local consumers.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


CHANNELS = (
    "CasuallyFinance",
    "casual_economics",
    "xkcd Channel",
    "PrimateEconomics-MP4",
    "BarelyEvolved-MP4",
    "PrimitiveEducation-MP4",
    "MonkeBiznis-MP4",
)
VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".webm"}
AUDIO_EXTENSIONS = {".mp3", ".m4a", ".wav", ".aac", ".flac"}
CAPTION_EXTENSIONS = {".srt", ".vtt", ".sbv", ".ass"}
TRANSCRIPT_EXTENSIONS = {".txt"}
STRUCTURED_EXTENSIONS = {".json", ".jsonl", ".csv"}
VIDEO_ID_RE = re.compile(r"\[([A-Za-z0-9_-]{11})\](?=\.[^.]+$)")
RIGHTS_STATUS = "USER_SUPPLIED_THIRD_PARTY_PRIVATE_RESEARCH_NO_REDISTRIBUTION"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in VIDEO_EXTENSIONS:
        return "VIDEO"
    if suffix in AUDIO_EXTENSIONS:
        return "AUDIO"
    if suffix in CAPTION_EXTENSIONS:
        return "CAPTION"
    if suffix in TRANSCRIPT_EXTENSIONS:
        return "TRANSCRIPT"
    if suffix in STRUCTURED_EXTENSIONS:
        return "STRUCTURED"
    return "AUXILIARY"


def extract_video_id(path: Path) -> tuple[str, str, str]:
    match = VIDEO_ID_RE.search(path.name)
    if match:
        return match.group(1), "HIGH", "FILENAME_BRACKETED_YOUTUBE_ID"
    return "", "UNKNOWN", "NO_RELIABLE_ID_IN_FILENAME"


def ffprobe(path: Path) -> tuple[dict[str, Any], str]:
    command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration,format_name:stream=index,codec_type,codec_name,width,height,avg_frame_rate",
        "-of",
        "json",
        str(path),
    ]
    try:
        completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {}, f"FFPROBE_EXECUTION_ERROR: {exc}"
    if completed.returncode:
        return {}, f"FFPROBE_FAILED_{completed.returncode}: {completed.stderr.strip()}"
    try:
        return json.loads(completed.stdout), ""
    except json.JSONDecodeError as exc:
        return {}, f"FFPROBE_JSON_ERROR: {exc}"


def stream_summary(probe: dict[str, Any]) -> dict[str, str]:
    streams = probe.get("streams", [])
    videos = [stream for stream in streams if stream.get("codec_type") == "video"]
    audios = [stream for stream in streams if stream.get("codec_type") == "audio"]
    video = videos[0] if videos else {}
    audio = audios[0] if audios else {}
    duration = probe.get("format", {}).get("duration", "")
    return {
        "duration_seconds": duration,
        "width": str(video.get("width", "")),
        "height": str(video.get("height", "")),
        "fps": str(video.get("avg_frame_rate", "")),
        "video_codec": str(video.get("codec_name", "")),
        "audio_codec": str(audio.get("codec_name", "")),
        "format_name": str(probe.get("format", {}).get("format_name", "")),
        "video_stream_count": str(len(videos)),
        "audio_stream_count": str(len(audios)),
    }


def atomic_copy(source: Path, destination: Path, expected_sha256: str) -> tuple[str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        existing_hash = sha256_file(destination)
        if existing_hash == expected_sha256:
            return "VERIFIED_EXISTING", ""
        return "DESTINATION_CONFLICT", f"existing sha256 {existing_hash} does not match source"
    file_descriptor, temporary_name = tempfile.mkstemp(prefix=f".{destination.name}.", suffix=".part", dir=destination.parent)
    os.close(file_descriptor)
    temporary_path = Path(temporary_name)
    try:
        shutil.copy2(source, temporary_path)
        copied_hash = sha256_file(temporary_path)
        if copied_hash != expected_sha256:
            return "COPY_HASH_MISMATCH", f"temporary sha256 {copied_hash} does not match source"
        temporary_path.replace(destination)
        return "COPIED_VERIFIED", ""
    finally:
        temporary_path.unlink(missing_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build(
    source_root: Path,
    repo_root: Path,
    output_dir: Path,
    ingest: bool,
    media_root: Path | None = None,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    channel_rows: list[dict[str, Any]] = []
    ingest_root = media_root or repo_root / "data" / "local-channel-media"
    for channel in CHANNELS:
        channel_root = source_root / channel
        if not channel_root.is_dir():
            channel_rows.append({"source_channel": channel, "exists": False, "file_count": 0, "bytes": 0})
            continue
        channel_files = sorted(path for path in channel_root.rglob("*") if path.is_file() and not path.is_symlink())
        channel_bytes = 0
        for source_path in channel_files:
            relative_source_path = source_path.relative_to(source_root)
            byte_count = source_path.stat().st_size
            channel_bytes += byte_count
            digest = sha256_file(source_path)
            asset_type = classify(source_path)
            video_id, mapping_confidence, mapping_evidence = extract_video_id(source_path)
            probe, probe_error = ({}, "")
            if asset_type in {"VIDEO", "AUDIO"}:
                probe, probe_error = ffprobe(source_path)
            project_path = Path("data") / "local-channel-media" / relative_source_path
            preservation_status = "SOURCE_LINK_ONLY"
            copy_error = ""
            if ingest:
                copy_action, copy_error = atomic_copy(source_path, ingest_root / relative_source_path, digest)
                if copy_action in {"COPIED_VERIFIED", "VERIFIED_EXISTING"}:
                    preservation_status = "LOCAL_COPY_VERIFIED"
                else:
                    preservation_status = copy_action
            record = {
                "source_channel": channel,
                "asset_type": asset_type,
                "original_relative_path": relative_source_path.as_posix(),
                "external_source_path": str(source_path),
                "local_media_path": project_path.as_posix(),
                "byte_count": byte_count,
                "sha256": digest,
                "video_id": video_id,
                "mapping_confidence": mapping_confidence,
                "mapping_evidence": mapping_evidence,
                "rights_access_classification": RIGHTS_STATUS,
                "preservation_status": preservation_status,
                "copy_verified": preservation_status == "LOCAL_COPY_VERIFIED",
                "ffprobe_error": probe_error,
                "copy_error": copy_error,
                **stream_summary(probe),
            }
            records.append(record)
        channel_rows.append(
            {"source_channel": channel, "exists": True, "file_count": len(channel_files), "bytes": channel_bytes}
        )

    hash_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        hash_groups[record["sha256"]].append(record)
    duplicate_rows: list[dict[str, Any]] = []
    for digest, group in sorted(hash_groups.items()):
        if len(group) < 2:
            continue
        for index, record in enumerate(group, start=1):
            duplicate_rows.append(
                {
                    "duplicate_group": f"SHA256-{digest[:16]}",
                    "group_size": len(group),
                    "member_index": index,
                    "sha256": digest,
                    "source_channel": record["source_channel"],
                    "original_relative_path": record["original_relative_path"],
                    "video_id": record["video_id"],
                }
            )

    video_id_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record["video_id"]:
            video_id_groups[(record["source_channel"], record["video_id"])].append(record)
    crosswalk_rows: list[dict[str, Any]] = []
    for record in records:
        variant_count = len(video_id_groups.get((record["source_channel"], record["video_id"]), [])) if record["video_id"] else 0
        crosswalk_rows.append(
            {
                "source_channel": record["source_channel"],
                "video_id": record["video_id"],
                "mapping_confidence": record["mapping_confidence"],
                "mapping_evidence": record["mapping_evidence"],
                "quality_variant_count": variant_count,
                "original_relative_path": record["original_relative_path"],
                "local_media_path": record["local_media_path"],
                "sha256": record["sha256"],
            }
        )

    write_jsonl(output_dir / "SOURCE_INVENTORY.jsonl", records)
    write_csv(output_dir / "MEDIA_MASTER.csv", list(records[0].keys()) if records else [], records)
    write_csv(output_dir / "CHANNEL_DIRECTORY.csv", ["source_channel", "exists", "file_count", "bytes"], channel_rows)
    write_csv(
        output_dir / "VIDEO_ID_CROSSWALK.csv",
        ["source_channel", "video_id", "mapping_confidence", "mapping_evidence", "quality_variant_count", "original_relative_path", "local_media_path", "sha256"],
        crosswalk_rows,
    )
    write_csv(
        output_dir / "DUPLICATE_GROUPS.csv",
        ["duplicate_group", "group_size", "member_index", "sha256", "source_channel", "original_relative_path", "video_id"],
        duplicate_rows,
    )
    report = {
        "schema_version": 1,
        "source_root": str(source_root),
        "local_library_root": (
            ingest_root.relative_to(repo_root).as_posix()
            if ingest_root.is_relative_to(repo_root)
            else "YIOS_MEDIA_ROOT"
        ),
        "rights_access_classification": RIGHTS_STATUS,
        "ingest_requested": ingest,
        "channel_count_expected": len(CHANNELS),
        "channel_count_present": sum(row["exists"] for row in channel_rows),
        "file_count": len(records),
        "byte_count": sum(record["byte_count"] for record in records),
        "asset_type_counts": dict(sorted(Counter(record["asset_type"] for record in records).items())),
        "mapped_video_id_files": sum(bool(record["video_id"]) for record in records),
        "unmapped_video_id_files": sum(not record["video_id"] for record in records),
        "unique_mapped_channel_video_ids": len(video_id_groups),
        "duplicate_byte_groups": sum(len(group) > 1 for group in hash_groups.values()),
        "duplicate_byte_files": sum(len(group) for group in hash_groups.values() if len(group) > 1),
        "quality_variant_channel_video_ids": sum(
            len({record["sha256"] for record in group}) > 1 for group in video_id_groups.values()
        ),
        "ffprobe_errors": sum(bool(record["ffprobe_error"]) for record in records),
        "local_copy_verified": sum(record["preservation_status"] == "LOCAL_COPY_VERIFIED" for record in records),
        "copy_errors": sum(bool(record["copy_error"]) for record in records),
    }
    write_json(output_dir / "INGEST_REPORT.json", report)
    manifest_targets = [
        output_dir / "SOURCE_INVENTORY.jsonl",
        output_dir / "MEDIA_MASTER.csv",
        output_dir / "CHANNEL_DIRECTORY.csv",
        output_dir / "VIDEO_ID_CROSSWALK.csv",
        output_dir / "DUPLICATE_GROUPS.csv",
        output_dir / "INGEST_REPORT.json",
    ]
    write_json(
        output_dir / "SOURCE_MANIFEST_SHA256.json",
        {path.name: sha256_file(path) for path in manifest_targets},
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=Path("research/media-library"))
    parser.add_argument(
        "--media-root",
        type=Path,
        default=Path(os.environ["YIOS_MEDIA_ROOT"]) if os.environ.get("YIOS_MEDIA_ROOT") else None,
        help="durable media root; defaults to $YIOS_MEDIA_ROOT, then <repo>/data/local-channel-media",
    )
    parser.add_argument("--ingest", action="store_true")
    args = parser.parse_args()
    source_root = args.source_root.expanduser().resolve()
    repo_root = args.repo_root.expanduser().resolve()
    output_dir = args.output_dir if args.output_dir.is_absolute() else repo_root / args.output_dir
    if not source_root.is_dir():
        parser.error(f"source root does not exist: {source_root}")
    media_root = args.media_root.expanduser().resolve() if args.media_root else None
    report = build(source_root, repo_root, output_dir, args.ingest, media_root)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["copy_errors"] == 0 and report["ffprobe_errors"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
