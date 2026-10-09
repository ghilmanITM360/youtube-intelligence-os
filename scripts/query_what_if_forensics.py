#!/usr/bin/env python3
"""Query validated promoted forensic evidence without changing source or catalog."""
import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from promote_what_if_forensics import DEFAULT_OUTPUT as DEFAULT_INDEX, build_index
from stage_what_if_forensics import DEFAULT_OUTPUT as DEFAULT_STAGE, ROOT, StagingError, canonical_json


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None


def interval(row):
    timing = row["timing"]
    start, end = number(timing.get("START_SEC")), number(timing.get("END_SEC"))
    return (start, end) if start is not None and end is not None and 0 <= start < end else None


def reference(row):
    return {key: row[key] for key in (
        "canonical_youtube_video_id", "source_video_id", "forensic_slug", "source_release",
        "source_table", "source_row_id", "source_reference", "confidence", "source_media_sha256",
        "transformation_version", "claim_kind",
    )}


def query_evidence(stage_dir, catalog_path, index_path, video_ids=None):
    """Validate every staged byte against promotion, then summarize selected videos.

    Metrics describe sampled source records, not complete-video coverage or
    performance effects. Recommendations are explicitly testable hypotheses.
    """
    index = build_index(stage_dir, catalog_path)
    promoted = json.loads(Path(index_path).read_text(encoding="utf-8"))
    if index != promoted:
        raise StagingError("promoted index differs from current validated stage")
    selected = None if video_ids is None else set(video_ids)
    grouped = defaultdict(lambda: defaultdict(list))
    for table in index["table_counts"]:
        for line in (Path(stage_dir) / f"{table}.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            youtube_id = row["canonical_youtube_video_id"]
            if selected is None or youtube_id in selected:
                grouped[youtube_id][table].append(row)
    videos, recommendations = [], []
    for youtube_id, tables in sorted(grouped.items()):
        shots = tables["MASTER_SHOTS"]
        valid_shots = [(row, interval(row)) for row in shots if interval(row)]
        durations = [end - start for _, (start, end) in valid_shots]
        coverage = sum(durations)
        offsets = [number(row["source_fields"].get("OFFSET_MS"))
                   for row in tables["MASTER_AUDIO_VISUAL_SYNC"]]
        offsets = [value for value in offsets if value is not None]
        opening = {table: [row for row in rows
                           if interval(row) and interval(row)[0] < 30]
                   for table, rows in tables.items()}
        # Preserve exact measured events; descriptions remain source declarations.
        audio = [{"start_seconds": interval(row)[0], "end_seconds": interval(row)[1],
                  "type": row["source_fields"].get("TYPE"), "evidence": reference(row)}
                 for row in tables["MASTER_AUDIO_EVENTS"] if interval(row)]
        states = [{"start_seconds": interval(row)[0],
                   "visual_function": row["source_fields"].get("VISUAL_FUNCTION"),
                   "camera_state": row["source_fields"].get("CAMERA_STATE"),
                   "evidence": reference(row)}
                  for row in sorted(tables["MASTER_STATES"],
                                    key=lambda r: number(r["timing"].get("START_SEC")) or 0)
                  if interval(row)]
        # Aggregates include compact IDs/row locators for every contributing row.
        table_evidence = {table: {
            "count": len(rows),
            "staging_manifest_sha256": index["staging_manifest_sha256"],
            "source_row_ids": [row["source_row_id"] for row in rows],
            "source_row_numbers": [row["source_table_row_number"] for row in rows],
            "confidence_values": sorted({str(row["confidence"]) for row in rows}),
            "source_reference": f"production_intelligence_brain/01_master_data/{table}.csv",
        } for table, rows in tables.items() if table not in {"MASTER_WORDS", "MASTER_SENTENCES"}}
        # Word/sentence detail is bounded to the opening, not raw narration text.
        for table in ("MASTER_WORDS", "MASTER_SENTENCES"):
            table_evidence[table] = {"count": len(tables[table]),
                                     "opening_evidence": [reference(row) for row in opening[table]]}
        mean = statistics.mean(durations) if durations else None
        first_row = next(iter(tables.values()))[0]
        videos.append({
            "youtube_video_id": youtube_id, "source_video_id": first_row["source_video_id"],
            "forensic_slug": first_row["forensic_slug"], "source_release": index["source_release"],
            "claim_kind": "SOURCE_DECLARED_FORENSIC_RECORD", "tables": table_evidence,
            "shot_pacing": {"shot_count": len(shots), "valid_timed_shots": len(durations),
                            "mean_duration_seconds": mean,
                            "sampled_duration_seconds": coverage,
                            "changes_per_minute": (max(len(durations) - 1, 0) * 60 / coverage
                                                   if coverage else None),
                            "coverage": "SOURCE_SAMPLED_SHOTS_NOT_COMPLETE_VIDEO"},
            "visual_state_progression": states,
            "motion_types": dict(Counter(row["source_fields"].get("ACTION") or "UNKNOWN"
                                         for row in tables["MASTER_MOTIONS"])),
            "motion_relationships": dict(Counter(row["source_fields"].get("RELATIONSHIP") or "UNKNOWN"
                                                 for row in tables["MASTER_MOTIONS"])),
            "asset_types": dict(Counter(row["source_fields"].get("TYPE") or "UNKNOWN"
                                        for row in tables["MASTER_ASSETS"])),
            "audio_event_timing": audio,
            "narration_visual_sync": {"event_count": len(tables["MASTER_AUDIO_VISUAL_SYNC"]),
                                      "valid_offset_count": len(offsets),
                                      "median_offset_ms": statistics.median(offsets) if offsets else None},
            "opening_pacing": {"window_seconds": 30,
                               "word_count": len(opening["MASTER_WORDS"]),
                               "sentence_count": len(opening["MASTER_SENTENCES"]),
                               "shot_count": len(opening["MASTER_SHOTS"]),
                               "state_count": len(opening["MASTER_STATES"]),
                               "motion_count": len(opening["MASTER_MOTIONS"])},
        })
        if mean is not None:
            recommendations.append({
                "claim_kind": "EVIDENCE_BACKED_HYPOTHESIS",
                "youtube_video_id": youtube_id,
                "recommendation": f"Test shot pacing near {mean:.2f} seconds per sampled shot when the example's explanatory structure fits the planned segment; review the cited states and narration before adoption.",
                "evidence": [reference(row) for row, _ in valid_shots],
                "confidence": "LIMITED_SOURCE_SAMPLE",
                "performance_effect": "NOT_ESTABLISHED",
            })
    recurring = defaultdict(list)
    for video in videos:
        for asset_type in video["asset_types"]:
            recurring[asset_type].append(video["youtube_video_id"])
    return {"status": "AVAILABLE", "channel_id": "CH-000004",
            "recurring_asset_types": [{"asset_type": key, "video_ids": value,
                                       "unique_video_count": len(value)}
                                      for key, value in sorted(recurring.items()) if len(value) > 1],
            "video_count": len(videos),
            "observation_count": sum(len(rows) for tables in grouped.values() for rows in tables.values()),
            "channel_samples_added": 0, "videos": videos, "recommendations": recommendations,
            "staging_manifest_sha256": index["staging_manifest_sha256"],
            "limitations": ["Source-declared forensic records; no independently verified causal performance effects.",
                            "Counts measure supplied observations, not complete timelines or independent channel samples."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, default=DEFAULT_STAGE)
    parser.add_argument("--catalog", type=Path, default=ROOT / "data/catalog/youtube_inventory.db")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--video-id", action="append")
    args = parser.parse_args()
    try:
        print(canonical_json(query_evidence(args.stage, args.catalog, args.index, args.video_id)))
    except (StagingError, OSError, KeyError, ValueError) as exc:
        parser.exit(1, f"forensic query failed: {exc}\n")


if __name__ == "__main__":
    main()
