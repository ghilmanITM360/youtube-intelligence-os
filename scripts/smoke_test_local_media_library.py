#!/usr/bin/env python3
"""Exercise one local media asset per channel without retaining frames."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--inventory", type=Path, default=Path("research/media-library/SOURCE_INVENTORY.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("research/media-library/SMOKE_TEST_REPORT.json"))
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()
    inventory_path = args.inventory if args.inventory.is_absolute() else repo_root / args.inventory
    output_path = args.output if args.output.is_absolute() else repo_root / args.output
    selected: dict[str, dict] = {}
    caption_counts: dict[str, int] = {}
    for line in inventory_path.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        channel = record["source_channel"]
        caption_counts.setdefault(channel, 0)
        if record["asset_type"] in {"CAPTION", "TRANSCRIPT"}:
            caption_counts[channel] += 1
        if record["asset_type"] == "VIDEO" and channel not in selected:
            selected[channel] = record

    results = []
    failures = 0
    for channel, record in selected.items():
        media_path = repo_root / record["local_media_path"]
        with tempfile.TemporaryDirectory(prefix="yios-media-smoke-") as temporary_directory:
            frame_path = Path(temporary_directory) / "frame.jpg"
            completed = subprocess.run(
                [
                    "ffmpeg",
                    "-v",
                    "error",
                    "-ss",
                    "1",
                    "-i",
                    str(media_path),
                    "-frames:v",
                    "1",
                    "-vf",
                    "scale='min(640,iw)':-2",
                    str(frame_path),
                ],
                check=False,
                capture_output=True,
                text=True,
                timeout=120,
            )
            frame_ok = completed.returncode == 0 and frame_path.is_file() and frame_path.stat().st_size > 0
            if not frame_ok:
                failures += 1
            results.append(
                {
                    "source_channel": channel,
                    "local_media_path": record["local_media_path"],
                    "source_sha256": record["sha256"],
                    "metadata_read": not bool(record["ffprobe_error"]),
                    "representative_frame_extracted": frame_ok,
                    "representative_frame_sha256": sha256_file(frame_path) if frame_ok else "",
                    "representative_frame_retained": False,
                    "frame_error": completed.stderr.strip(),
                    "caption_status": "LOCALLY_AVAILABLE" if caption_counts[channel] else "NOT_AVAILABLE_IN_SOURCE_FOLDER",
                    "caption_file_count": caption_counts[channel],
                }
            )
    payload = {
        "schema_version": 1,
        "channels_tested": len(results),
        "failures": failures,
        "frame_policy": "ONE_640PX_FRAME_PER_CHANNEL_EXTRACTED_TO_TEMPORARY_STORAGE_AND_DELETED",
        "results": results,
    }
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
