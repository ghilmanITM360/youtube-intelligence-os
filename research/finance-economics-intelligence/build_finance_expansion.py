#!/usr/bin/env python3
"""Build the Finance expansion from the independently acquired 12-channel snapshot.

This is a derived-data builder. It never edits the frozen 966-video baseline and it
does not invoke Apify or any live acquisition service.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_SOURCE = Path("/private/tmp/yios-youtube-12-channel-metadata/research/youtube-12-channel-metadata")
OUT = HERE / "expansion-12-channel-2026-10-20"
SOURCE_COMMIT = "967ea707a0d7198754d132a978962baa96073f49"

ALL_FINANCE_CHANNELS = {
    "Primate Economics",
    "Logical Money",
    "Mark Invests",
    "Uncle Frank Retirement",
    "Uncle John Financial",
}

PRIMITIVE_ELIGIBLE = {
    "vakoysmESMQ", "wgaDgYbLo-A", "C_jSOXP_XWY", "Zc6Tj3XRXVc",
    "viFnpXCODwA", "5RYkAq7eMbg", "mdGDmmvtqWY", "6YHva7Me2ls",
    "W8AVd7RhTME", "cZYdi9aFv6I", "zNIGKQA7FMQ", "S0tDBKXjuKc",
    "RmTdnXHbI8s",
}

CHRONOFOLD_ELIGIBLE = {"-2_MAElCGCc", "nB3WRMupmW4"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        # Derived CSVs use repository-safe LF lines and remove only trailing
        # horizontal whitespace from embedded source-description lines. Raw
        # acquisition evidence remains untouched on the source branch.
        writer.writerows([
            {
                key: "\n".join(line.rstrip(" \t") for line in value.split("\n"))
                if isinstance(value, str) else value
                for key, value in row.items()
            }
            for row in rows
        ])


def classify(row: dict[str, str]) -> tuple[str, str, str, str]:
    channel, vid = row["channel_name"], row["video_id"]
    if channel in ALL_FINANCE_CHANNELS:
        return "INCLUDE", "HIGH", "FINANCE_CORE", "Channel is finance-specific and this video's title/description is directly about finance, investing, retirement, tax, money, or economics."
    if channel == "Primitive Education" and vid in PRIMITIVE_ELIGIBLE:
        topic = "ECONOMIC_SYSTEMS" if "Capitalism" in row["title"] else "HOUSING_FINANCE"
        return "INCLUDE", "HIGH", topic, "Title and available description directly address capitalism or mortgage mechanics."
    if channel == "Chronofold" and vid in CHRONOFOLD_ELIGIBLE:
        return "INCLUDE", "MEDIUM", "ECONOMIC_HISTORY", "Description explicitly frames national history through wealth, trade/resources, banking, or economic development; deep economic coverage is not yet audited."
    if channel == "monke":
        return "EXCLUDE", "HIGH", "OUT_OF_SCOPE_SELF_IMPROVEMENT", "Title and description concern health, habits, productivity, relationships, or self-improvement rather than finance/economics."
    if channel == "Unknown Frequencies":
        return "EXCLUDE", "HIGH", "OUT_OF_SCOPE_MILITARY_HISTORY", "Individual title/description is military, war, mythology, or general national history without a clear finance/economics focus."
    if channel == "What if 4k":
        return "EXCLUDE", "HIGH", "OUT_OF_SCOPE_HISTORY", "Individual title/description is military, ancient-history, or survival narrative; incidental pay/work details do not make it finance/economics research."
    if channel == "Timepiece History":
        return "EXCLUDE", "MEDIUM", "OUT_OF_SCOPE_GENERAL_HISTORY", "Individual title/description is a general national or empire history; any economic material is incidental rather than the stated subject."
    if channel == "Serious History":
        return "EXCLUDE", "MEDIUM", "OUT_OF_SCOPE_GENERAL_HISTORY", "Individual title/description is battle, biography, revenge, survival, or general history; wealth/corruption wording is incidental and not enough for inclusion."
    if channel == "Primitive Education":
        return "EXCLUDE", "HIGH", "OUT_OF_SCOPE_EDUCATION", "Individual title/description is science, relationships, slang, or general life education rather than finance/economics."
    raise ValueError(f"Unhandled channel: {channel}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE)
    args = ap.parse_args()
    source = args.source_root.resolve()
    videos_path = source / "ALL_PUBLIC_VIDEOS.csv"
    statuses_path = source / "CHANNEL_STATUS_REGISTER.csv"
    manifest_path = source / "AGGREGATE_MANIFEST.json"
    validation_path = source / "AGGREGATE_VALIDATION.json"
    reconciliation_path = source / "SOURCE_RECONCILIATION_REPORT.md"
    required = [videos_path, statuses_path, manifest_path, validation_path, reconciliation_path]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"Missing acquisition inputs: {missing}")

    videos = read_csv(videos_path)
    statuses = read_csv(statuses_path)
    baseline = read_csv(HERE / "audit-baseline" / "VIDEO_MASTER.csv")
    baseline_ids = {r["Video_ID"] for r in baseline}
    baseline_owner = {r["Video_ID"]: r["Channel_ID"] for r in baseline}
    if len(baseline) != 966 or len(baseline_ids) != 966:
        raise SystemExit("Frozen baseline is not exactly 966 unique Video_IDs")

    OUT.mkdir(exist_ok=True)
    decisions = []
    duplicate_rows = []
    expansion_rows = []
    for row in videos:
        decision, uncertainty, scope, reason = classify(row)
        duplicate = row["video_id"] in baseline_ids
        owner_match = "NOT_APPLICABLE"
        if duplicate:
            owner_match = str(baseline_owner[row["video_id"]] == row["channel_id"]).lower()
            duplicate_rows.append({
                "video_id": row["video_id"], "channel_id": row["channel_id"],
                "channel_name": row["channel_name"], "title": row["title"],
                "baseline_channel_id": baseline_owner[row["video_id"]],
                "channel_owner_match": owner_match,
                "disposition": "EXCLUDED_FROM_EXPANSION_AS_BASELINE_DUPLICATE",
            })
        completion = "METADATA_ONLY_NOT_DEEP_AUDITED"
        common = {
            "video_id": row["video_id"], "channel_id": row["channel_id"],
            "channel_name": row["channel_name"], "title": row["title"],
            "finance_decision": decision, "decision_uncertainty": uncertainty,
            "scope_label": scope, "decision_reason": reason,
            "duplicate_with_frozen_966": str(duplicate).lower(),
            "duplicate_channel_owner_match": owner_match,
            "expansion_disposition": "INCLUDE_UNIQUE_EXPANSION" if decision == "INCLUDE" and not duplicate else ("BASELINE_DUPLICATE" if duplicate else "OUT_OF_SCOPE"),
            "analysis_completion": completion,
            "transcript_status": "UNAVAILABLE_IN_METADATA_ACQUISITION" if row["captions_or_transcript_available"] != "true" else "ACTOR_REPORTED_AVAILABLE_NOT_INGESTED",
            "thumbnail_status": "REMOTE_URL_ONLY_NOT_REGISTERED_LOCALLY" if row["thumbnail_local_path"] == "UNKNOWN" else "LOCAL_PATH_REPORTED",
            "private_analytics_status": "NOT_AVAILABLE",
            "acquisition_commit": SOURCE_COMMIT,
            "actor_run_id": row["actor_run_id"], "actor_dataset_id": row["actor_dataset_id"],
            "raw_dataset_row_locator": row["raw_dataset_row_locator"],
            "metadata_retrieval_timestamp_utc": row["metadata_retrieval_timestamp_utc"],
        }
        decisions.append(common)
        if decision == "INCLUDE" and not duplicate:
            expansion_rows.append({**row, **common})

    fields = list(decisions[0])
    write_csv(OUT / "FINANCE_INCLUSION_CROSSWALK.csv", decisions, fields)
    write_csv(OUT / "DUPLICATE_OVERLAP_WITH_BASELINE.csv", duplicate_rows, list(duplicate_rows[0]))
    expansion_fields = list(videos[0]) + [f for f in fields if f not in videos[0]]
    write_csv(OUT / "FINANCE_EXPANSION_MASTER.csv", expansion_rows, expansion_fields)

    by_channel = defaultdict(list)
    for d in decisions:
        by_channel[d["channel_name"]].append(d)
    status_by_name = {r["display_name"]: r for r in statuses}
    summary = []
    for name in sorted(by_channel):
        rs = by_channel[name]
        st = status_by_name[name]
        summary.append({
            "channel_name": name, "channel_id": st["channel_id"],
            "captured": len(rs), "finance_eligible": sum(r["finance_decision"] == "INCLUDE" for r in rs),
            "baseline_duplicates": sum(r["duplicate_with_frozen_966"] == "true" for r in rs),
            "unique_expansion": sum(r["expansion_disposition"] == "INCLUDE_UNIQUE_EXPANSION" for r in rs),
            "excluded": sum(r["finance_decision"] == "EXCLUDE" for r in rs),
            "channel_verification": st["verified"], "acquisition_validation": st["validation_status"],
            "classification_basis": "INDIVIDUAL_VIDEO_TITLE_DESCRIPTION_METADATA",
        })
    write_csv(OUT / "CHANNEL_CLASSIFICATION_SUMMARY.csv", summary, list(summary[0]))

    validation = {
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_commit": SOURCE_COMMIT,
        "source_all_public_videos_sha256": sha256(videos_path),
        "source_channel_status_sha256": sha256(statuses_path),
        "source_aggregate_manifest_sha256": sha256(manifest_path),
        "source_aggregate_validation_sha256": sha256(validation_path),
        "source_reconciliation_report_sha256": sha256(reconciliation_path),
        "captured_rows": len(videos),
        "captured_unique_video_ids": len({r["video_id"] for r in videos}),
        "channels": len(by_channel),
        "frozen_baseline_rows": len(baseline),
        "frozen_baseline_unique_ids": len(baseline_ids),
        "eligible_acquisition_rows": sum(d["finance_decision"] == "INCLUDE" for d in decisions),
        "exact_duplicate_overlap": len(duplicate_rows),
        "duplicate_owner_mismatches": sum(r["channel_owner_match"] != "true" for r in duplicate_rows),
        "unique_finance_expansion_rows": len(expansion_rows),
        "combined_unique_research_population": len(baseline_ids) + len(expansion_rows),
        "expansion_deep_audited": 0,
        "decision_counts": dict(Counter(d["finance_decision"] for d in decisions)),
        "checks": {
            "source_445_unique": len(videos) == 445 == len({r["video_id"] for r in videos}),
            "twelve_channels": len(by_channel) == 12,
            "baseline_966_unique": len(baseline) == 966 == len(baseline_ids),
            "no_duplicate_expansion_ids": len(expansion_rows) == len({r["video_id"] for r in expansion_rows}),
            "all_duplicate_owners_match": all(r["channel_owner_match"] == "true" for r in duplicate_rows),
            "population_reconciles": len(baseline_ids) + len(expansion_rows) == len(baseline_ids | {r["video_id"] for r in expansion_rows}),
        },
    }
    if not all(validation["checks"].values()):
        validation["status"] = "FAIL"
    (OUT / "EXPANSION_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")

    source_register = {
        "source_branch": "research/youtube-12-channel-metadata",
        "source_commit": SOURCE_COMMIT,
        "source_pr": 39,
        "acquisition_repeated": False,
        "raw_evidence_mutated": False,
        "inputs": [{"path": p.name, "sha256": sha256(p)} for p in required],
        "limitations": [
            "Metadata acquisition is not a deep content audit.",
            "No transcript or thumbnail file was imported by this derived expansion build.",
            "No private YouTube analytics are available.",
            "MEDIUM decisions should be revisited when full transcripts are registered.",
        ],
    }
    (OUT / "SOURCE_PROVENANCE.json").write_text(json.dumps(source_register, indent=2) + "\n", encoding="utf-8")

    checksums = {}
    for p in sorted(OUT.iterdir()):
        if p.name != "FILE_CHECKSUMS_SHA256.json" and p.is_file():
            checksums[p.name] = sha256(p)
    (OUT / "FILE_CHECKSUMS_SHA256.json").write_text(json.dumps(checksums, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
