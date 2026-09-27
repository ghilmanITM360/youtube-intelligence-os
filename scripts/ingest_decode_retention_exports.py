#!/usr/bin/env python3
"""Ingest authorized YouTube Studio audience-retention exports for DS-000032."""

from __future__ import annotations

import csv
import difflib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
STUDIO = ROOT / "data/raw/first-party/youtube-studio/DS-000032/2026-09-27"
CONTENT_EXPORT = STUDIO / "studio-advanced-content-lifetime.zip"
DOWNLOADS = Path("/Users/ghilmankhan/Downloads")
DEST = STUDIO / "audience-retention-by-video"
OUT = STUDIO / "audience-retention-analysis.json"


def normalize(value: str) -> str:
    value = value.lower().replace("—", " ").replace("–", " ").replace("|", " ").replace("_", " ")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def load_video_index() -> dict[str, dict[str, object]]:
    with ZipFile(CONTENT_EXPORT) as archive:
        rows = list(csv.DictReader(archive.read("Table data.csv").decode("utf-8-sig").splitlines()))
    videos: dict[str, dict[str, object]] = {}
    for row in rows:
        video_id = row["Content"].strip()
        if not video_id or video_id in {"Total", "FjK6DU-HmZg"}:
            continue
        videos[video_id] = {
            "video_id": video_id,
            "title": row["Video title"],
            "duration_seconds": int(row["Duration"] or 0),
            "views": int(row["Views"] or 0),
        }
    return videos


def exported_title(path: Path) -> str:
    return re.sub(
        r"^Audience retention \d{4}-\d{2}-\d{2}_\d{4}-\d{2}-\d{2} ",
        "",
        re.sub(r" \(\d+\)$", "", path.stem),
    )


def match_exports(videos: dict[str, dict[str, object]]) -> dict[str, tuple[Path, float]]:
    candidates = sorted(DOWNLOADS.glob("Audience retention*.zip"), key=lambda p: p.stat().st_mtime)
    matched: dict[str, tuple[Path, float]] = {}
    for path in candidates:
        title = exported_title(path)
        score, video_id = max(
            (difflib.SequenceMatcher(None, normalize(title), normalize(str(row["title"]))).ratio(), video_id)
            for video_id, row in videos.items()
        )
        if score >= 0.82:
            matched[video_id] = (path, score)
    return matched


def read_retention(path: Path) -> list[tuple[int, float]]:
    with ZipFile(path) as archive:
        rows = list(csv.DictReader(archive.read("All.csv").decode("utf-8-sig").splitlines()))
    return [
        (int(float(row["Video position (%)"])), float(row["Absolute audience retention (%)"]))
        for row in rows
        if row.get("Absolute audience retention (%)") not in (None, "")
    ]


def format_timestamp(seconds: float) -> str:
    seconds = max(0, round(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def summarize(points: list[tuple[int, float]], duration: int) -> dict[str, object]:
    if not points:
        return {
            "curve_status": "EXPORTED_NO_CURVE",
            "curve_limitation": "Studio export contained an All.csv header but no retention rows.",
            "curve_point_count": 0,
            "retention_at_start_percent": None,
            "retention_at_3_seconds_percent": None,
            "retention_at_5_seconds_percent": None,
            "retention_at_30_seconds_percent": None,
            "retention_30_seconds_source_position_percent": None,
            "retention_at_midpoint_percent": None,
            "retention_at_end_percent": None,
            "retention_end_source_position_percent": None,
            "largest_step_dips": [],
            "largest_step_spikes": [],
            "curve_points": [],
        }
    by_position = dict(points)
    def nearest_at(seconds: int) -> tuple[int, float] | tuple[None, None]:
        if not duration or seconds > duration:
            return (None, None)
        position = round(seconds / duration * 100)
        return min(points, key=lambda point: abs(point[0] - position))

    nearest_3 = nearest_at(3)
    nearest_5 = nearest_at(5)
    nearest_30 = nearest_at(30)
    changes = [
        {
            "from_position_percent": left[0],
            "to_position_percent": right[0],
            "change_points": round(right[1] - left[1], 2),
            "timestamp": format_timestamp(right[0] / 100 * duration),
        }
        for left, right in zip(points, points[1:])
    ]
    dips = sorted(changes, key=lambda item: item["change_points"])[:3]
    spikes = sorted(changes, key=lambda item: item["change_points"], reverse=True)[:3]
    return {
        "curve_status": "AVAILABLE",
        "curve_limitation": None,
        "curve_point_count": len(points),
        "retention_at_start_percent": by_position.get(0),
        "retention_at_3_seconds_percent": nearest_3[1],
        "retention_at_5_seconds_percent": nearest_5[1],
        "retention_at_30_seconds_percent": nearest_30[1],
        "retention_30_seconds_source_position_percent": nearest_30[0],
        "retention_at_midpoint_percent": by_position.get(50),
        "retention_at_end_percent": points[-1][1],
        "retention_end_source_position_percent": points[-1][0],
        "largest_step_dips": dips,
        "largest_step_spikes": spikes,
        "curve_points": [{"position_percent": p, "retention_percent": v} for p, v in points],
    }


def main() -> None:
    videos = load_video_index()
    matched = match_exports(videos)
    DEST.mkdir(parents=True, exist_ok=True)
    records = []
    for video_id, row in videos.items():
        if video_id not in matched:
            records.append({**row, "status": "NOT_EXPORTED", "reason": "No matching Studio retention ZIP recovered."})
            continue
        source, score = matched[video_id]
        destination = DEST / f"{video_id}.zip"
        shutil.copy2(source, destination)
        points = read_retention(destination)
        summary = summarize(points, int(row["duration_seconds"]))
        records.append(
            {
                **row,
                "status": "AVAILABLE",
                "source_export": str(destination.relative_to(ROOT)),
                "source_download_name": source.name,
                "title_match_score": round(score, 4),
                **summary,
            }
        )
    payload = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dataset_id": "DS-000032",
        "channel_id": "UCQIzqH7QZ9viBYpOFqgSXMg",
        "source_period": "Since uploaded through 2026-09-27",
        "record_count": len(records),
        "available_count": sum(record["status"] == "AVAILABLE" for record in records),
        "curve_available_count": sum(record.get("curve_status") == "AVAILABLE" for record in records),
        "exported_no_curve_count": sum(record.get("curve_status") == "EXPORTED_NO_CURVE" for record in records),
        "not_exported_count": sum(record["status"] != "AVAILABLE" for record in records),
        "records": records,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({key: payload[key] for key in ("record_count", "available_count", "curve_available_count", "exported_no_curve_count", "not_exported_count")}, indent=2))
    for record in records:
        if record["status"] != "AVAILABLE":
            print("NOT_EXPORTED", record["video_id"], record["title"])


if __name__ == "__main__":
    main()
