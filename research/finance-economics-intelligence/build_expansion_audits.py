#!/usr/bin/env python3
"""Build the isolated Finance-expansion audit ledger from explicit analyst batches."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "expansion-12-channel-2026-10-20"
BATCHES = OUT / "audit-batches"
DIMENSIONS = ("TITLE", "THUMBNAIL", "SCRIPT", "TOPIC", "PERFORMANCE", "VIRALITY")
VALID_STATUSES = {
    "NOT_STARTED",
    "COMPLETE_LIMITED_EVIDENCE",
    "COMPLETE_EVIDENCE_BACKED",
    "BLOCKED_MISSING_SOURCE",
    "BLOCKED_INSUFFICIENT_COMPARABLE_DATA",
    "BLOCKED_INSUFFICIENT_EVIDENCE",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def completion(statuses: dict[str, str]) -> str:
    values = list(statuses.values())
    if all(value.startswith("COMPLETE_") for value in values):
        return "COMPLETE"
    if any(value.startswith("COMPLETE_") for value in values) and any(value.startswith("BLOCKED_") for value in values):
        return "BLOCKED_PARTIAL_EVIDENCE"
    return "METADATA_ONLY_NOT_STARTED"


def build() -> dict:
    master = read_csv(OUT / "FINANCE_EXPANSION_MASTER.csv")
    baseline = read_csv(HERE / "audit-baseline" / "VIDEO_IDS.csv")
    baseline_ids = {row["Video_ID"] for row in baseline}
    if len(master) != 197 or len({row["video_id"] for row in master}) != 197:
        raise ValueError("Expansion master must contain exactly 197 unique IDs")
    if {row["video_id"] for row in master} & baseline_ids:
        raise ValueError("Expansion ledger cannot overlap the frozen 966")

    reviews: dict[str, tuple[str, dict]] = {}
    for path in sorted(BATCHES.glob("*.json")):
        batch = json.loads(path.read_text(encoding="utf-8"))
        for review in batch["reviews"]:
            video_id = review["video_id"]
            if video_id in reviews:
                raise ValueError(f"Duplicate expansion audit review: {video_id}")
            reviews[video_id] = (batch["batch_id"], review)

    unknown = set(reviews) - {row["video_id"] for row in master}
    if unknown:
        raise ValueError(f"Unknown expansion audit IDs: {sorted(unknown)}")

    ledger = []
    for source in master:
        statuses = {f"{dimension}_REVIEW": "NOT_STARTED" for dimension in DIMENSIONS}
        row = {
            "video_id": source["video_id"],
            "channel_id": source["channel_id"],
            "channel_name": source["channel_name"],
            "title": source["title"],
            "acquisition_commit": source["acquisition_commit"],
            "metadata_snapshot_utc": source["metadata_retrieval_timestamp_utc"],
            "metadata_status": "REGISTERED_NOT_DEEP_AUDITED",
            "statuses": statuses,
            "deep_audit_completion": "METADATA_ONLY_NOT_STARTED",
            "batch_id": "EXPANSION_PENDING",
            "title_review": {},
            "thumbnail_review": {},
            "script_review": {},
            "topic_review": {},
            "performance_review": {},
            "virality_review": {},
            "private_analytics_status": "NOT_AVAILABLE",
        }
        if source["video_id"] in reviews:
            batch_id, review = reviews[source["video_id"]]
            if set(review["statuses"]) != set(statuses):
                raise ValueError(f"Status dimensions incomplete: {source['video_id']}")
            if set(review["statuses"].values()) - VALID_STATUSES:
                raise ValueError(f"Invalid status: {source['video_id']}")
            row.update({key: value for key, value in review.items() if key not in {"video_id", "statuses"}})
            row["statuses"] = review["statuses"]
            row["batch_id"] = batch_id
            row["deep_audit_completion"] = completion(review["statuses"])
        ledger.append(row)

    ledger_path = OUT / "EXPANSION_AUDIT_LEDGER.jsonl"
    ledger_path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in ledger), encoding="utf-8")
    counts = {
        "deep_audited": sum(row["deep_audit_completion"] == "COMPLETE" for row in ledger),
        "blocked_partial_evidence": sum(row["deep_audit_completion"] == "BLOCKED_PARTIAL_EVIDENCE" for row in ledger),
        "metadata_only_not_started": sum(row["deep_audit_completion"] == "METADATA_ONLY_NOT_STARTED" for row in ledger),
    }
    validation = {
        "status": "PASS",
        "registered_expansion_ids": len(ledger),
        **counts,
        "combined_unique_population": len(baseline_ids) + len(ledger),
        "chronofold_medium_uncertainty_pending": 2,
        "ledger_sha256": sha256(ledger_path),
        "checks": {
            "ledger_197_unique": len(ledger) == 197 == len({row["video_id"] for row in ledger}),
            "disjoint_from_frozen_966": not ({row["video_id"] for row in ledger} & baseline_ids),
            "combined_population_1163": len(baseline_ids) + len(ledger) == 1163,
            "completion_counts_reconcile": sum(counts.values()) == len(ledger),
            "deep_completion_not_inferred_from_metadata": counts["deep_audited"] == 0,
        },
        "limitations": [
            "A blocked partial review is not a completed deep audit.",
            "No private YouTube analytics are available.",
            "Chronofold inclusion remains medium uncertainty pending full transcripts.",
        ],
    }
    if not all(validation["checks"].values()):
        validation["status"] = "FAIL"
    (OUT / "EXPANSION_AUDIT_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    checksum_paths = [
        OUT / "EXPANSION_AUDIT_LEDGER.jsonl",
        OUT / "EXPANSION_AUDIT_VALIDATION.json",
        BATCHES / "EXPANSION_001.json",
        BATCHES / "EXPANSION_001_READ_RECEIPTS.json",
        OUT / "audit-evidence" / "HjlVexL2Lxk.jpg",
    ]
    checksums = {str(path.relative_to(OUT)): sha256(path) for path in checksum_paths}
    (OUT / "EXPANSION_AUDIT_CHECKSUMS_SHA256.json").write_text(
        json.dumps(checksums, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(validation, indent=2))
    return validation


if __name__ == "__main__":
    build()
