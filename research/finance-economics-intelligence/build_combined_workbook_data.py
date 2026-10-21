#!/usr/bin/env python3
"""Normalize the authoritative Finance universe for the combined workbook."""
from __future__ import annotations

import csv
import io
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UNIVERSE = ROOT / "reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv"
CHANNELS = ROOT / "reconciliation-all-repository-2026-10-21/CHANNEL_DIRECTORY.csv"
CASUAL_COMMIT = "fb1e56d03e5ad53086c74247cd2972b262d09b78"
CASUAL_PATH = "research/casually-finance-success-playbook/VIDEO_PERFORMANCE.csv"
DIMS = ("TITLE", "THUMBNAIL", "SCRIPT", "TOPIC", "PERFORMANCE", "VIRALITY")
COMPLETE_STATUSES = {"COMPLETE_EVIDENCE_BACKED", "COMPLETE_LIMITED_EVIDENCE"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def git_csv(commit: str, path: str) -> list[dict[str, str]]:
    text = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True)
    return list(csv.DictReader(io.StringIO(text)))


def as_number(value: str | None):
    if value in (None, "", "UNKNOWN", "NOT_FETCHED"):
        return None
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return None


def main() -> None:
    universe = read_csv(UNIVERSE)
    channels = read_csv(CHANNELS)
    audits = {r["identity"]["Video_ID"]: r for r in map(json.loads, (ROOT / "VIDEO_AUDIT_966.jsonl").read_text().splitlines())}
    exp12 = {r["video_id"]: r for r in read_csv(ROOT / "expansion-12-channel-2026-10-20/FINANCE_EXPANSION_MASTER.csv")}
    monkey = {r["video_id"]: r for r in read_csv(ROOT / "expansion-monkey-explains-1999-2026-10-21/FINANCE_EXPANSION_MASTER.csv")}
    landscape = {r["Video_ID"]: r for r in read_csv(ROOT / "LANDSCAPE_VIDEOS.csv")}
    casual = {r["Video_ID"]: r for r in git_csv(CASUAL_COMMIT, CASUAL_PATH)}
    ids = [r["video_id"] for r in universe]
    assert len(universe) == len(set(ids)) == 1612

    all_rows = []
    for u in universe:
        vid, layer = u["video_id"], u["population_layer"]
        published = duration = views = likes = comments = snapshot = description = ""
        fmt = ""
        statuses = {d: "NOT_STARTED" for d in DIMS}
        if layer == "FROZEN_ORIGINAL_966":
            a = audits[vid]; i = a["identity"]
            published, duration, views, likes, comments = i["Published_at_raw"], i["Duration_seconds"], i["Views"], i["likes"], i["comments"]
            snapshot, description, fmt = i["Metric_snapshot_date"], i.get("description", ""), i["Format"]
            statuses = {d: a["statuses"][f"{d}_REVIEW"] for d in DIMS}
        elif layer == "EXPANSION_12_CHANNEL_197":
            r = exp12[vid]
            published, duration, views, likes, comments = r["publication_timestamp_utc"], r["duration_seconds"], r["view_count"], r["like_count"], r["comment_count"]
            snapshot, description, fmt = r["metadata_retrieval_timestamp_utc"], r["description"], r["video_type"]
        elif layer == "EXPANSION_MONKEY_63":
            r = monkey[vid]
            published, duration, views, likes, comments = r["publication_timestamp_utc"], r["duration_seconds"], r["view_count"], r["like_count"], r["comment_count"]
            snapshot, description, fmt = r["metadata_retrieval_timestamp_utc"], r["description"], r["video_type"]
        elif u["source_dataset"] == "LANDSCAPE_VIDEOS.csv":
            r = landscape[vid]
            duration, views, snapshot, fmt = r["Duration_display"], r["Views_display"], r["Snapshot"], r["Format_basis"]
        else:
            r = casual[vid]
            published, duration, views, snapshot, fmt = r["Publish_Date"], r["Duration_Sec"], r["Public_Views"], r["Snapshot_Date"], r["Format"]
        audit_status = ("DEEP_AUDIT_COMPLETE" if all(s in COMPLETE_STATUSES for s in statuses.values())
                        else "NOT_DEEP_AUDITED") if layer == "FROZEN_ORIGINAL_966" else u["audit_status"]
        row = {**u, "audit_status": audit_status,
               "publication_date": published, "duration": as_number(duration) if str(duration).replace('.', '', 1).isdigit() else duration,
               "views": as_number(views) or views, "likes": as_number(likes), "comments": as_number(comments),
               "metric_snapshot": snapshot, "format": fmt, "description": description, **{f"{d.lower()}_review_status": statuses[d] for d in DIMS}}
        all_rows.append(row)

    deep = sum(r["audit_status"] == "DEEP_AUDIT_COMPLETE" for r in all_rows)
    layers = Counter(r["population_layer"] for r in all_rows)
    channel_status = Counter(r["status"] for r in channels)
    assert layers == Counter({"FROZEN_ORIGINAL_966": 966, "EXPANSION_12_CHANNEL_197": 197,
                              "EXPANSION_MONKEY_63": 63, "REPOSITORY_RECONCILIATION_2026_10_21": 386})
    assert channel_status == Counter({"VIDEO_DATASET_INCLUDED": 27, "IDENTITY_ONLY_NEEDS_DATA": 10,
                                     "VIDEO_DATASET_EXCLUDED_AFTER_INDIVIDUAL_CLASSIFICATION": 5})
    detail = []
    for vid, a in audits.items():
        detail.append({"video_id": vid, "channel": a["identity"]["Channel"], "title": a["identity"]["Title"],
                       "batch_id": a["batch_id"], "deep_audit_status": next(r["audit_status"] for r in all_rows if r["video_id"] == vid),
                       "statuses": a["statuses"], "title_research": a["title"], "thumbnail_research": a["thumbnail"],
                       "script_research": a["script"], "topic_research": a["topic"], "performance_research": a["performance"],
                       "virality_research": a["virality"], "event_research": a["event"], "private_metrics": a["private_metrics"]})
    payload = {"all_videos": all_rows, "channels": channels, "details": detail,
               "summary": {"total": len(all_rows), "deep_audited": deep, "pending": len(all_rows) - deep,
                           "layers": dict(layers), "channel_status": dict(channel_status)}}
    json.dump(payload, sys.stdout, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    main()
