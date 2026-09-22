#!/usr/bin/env python3
"""Build normalized YouTube channel ledgers and a separate SQLite registry."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import sys
import zipfile
from collections import defaultdict
from pathlib import Path


RAW_AUTHORITY = "data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json"
IDENTITY_EVIDENCE = "data/manifests/YOUTUBE_CHANNEL_IDENTITY_EVIDENCE.json"
COVERAGE_LEDGER = "docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv"
SCHEMA = "data/catalog/channel_registry/schema.sql"
VERIFIED_AT = "2026-09-14"
STATUSES = {
    "COMPLETE",
    "COMPLETE_WITH_LIMITATIONS",
    "PARTIAL",
    "IDENTITY_VERIFIED_DATA_NOT_EXTRACTED",
    "PENDING_IDENTITY_RESOLUTION",
    "UNAVAILABLE_OR_DELETED",
}

csv.field_size_limit(sys.maxsize)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_id(*parts) -> int:
    return int(hashlib.sha256("\0".join("" if part is None else str(part) for part in parts).encode()).hexdigest()[:15], 16)


def as_int(value) -> int:
    if value in (None, "", "NOT_AVAILABLE", "N/A", "Unavailable"):
        return 0
    return int(float(str(value).replace(",", "")))


def nullable_int(value) -> int | None:
    return None if value in (None, "", "NOT_AVAILABLE", "N/A", "Unavailable") else as_int(value)


def duration_seconds(row: dict) -> int:
    if row.get("duration_seconds") not in (None, ""):
        return as_int(row["duration_seconds"])
    parts = [int(part) for part in row.get("duration", "0").split(":")]
    return sum(value * 60 ** index for index, value in enumerate(reversed(parts)))


def canonical_id(value: str) -> str | None:
    match = re.search(r"(?:^| / )(UC[A-Za-z0-9_-]{22})$", value or "")
    return match.group(1) if match else None


def normalized_lookup(url: str) -> str:
    return url.rstrip("/").removesuffix("/videos").rsplit("/", 1)[-1].lstrip("@").lower()


def read_coverage(root: Path) -> list[dict]:
    with (root / COVERAGE_LEDGER).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def channel_limitations(row: dict) -> list[str]:
    limitations = []
    dataset = row["Dataset"]
    if dataset == "DS-000022":
        limitations.append("Original Actor raw output and run/dataset IDs were not supplied for the source package.")
    if as_int(row["Placeholders"]):
        limitations.append(f"{as_int(row['Placeholders'])} transcript placeholders have explicit unavailable reasons.")
    missing_descriptions = as_int(row["Videos"]) - as_int(row["Descriptions"])
    if missing_descriptions:
        limitations.append(f"{missing_descriptions} videos have no public description.")
    if dataset == "DS-000001":
        limitations.append("Historical catalog does not classify regular, Shorts, and livestream counts.")
    if dataset == "DS-000017":
        limitations.append("Editing/visual coverage is limited to registered forensic evidence.")
    return limitations


def coverage_metrics(root: Path, row: dict | None) -> dict:
    if not row:
        return {
            "dataset_ids": [], "video_count": 0, "regular_videos": 0,
            "shorts": 0, "livestreams": 0, "descriptions": 0,
            "real_transcripts": 0, "placeholders": 0, "missing_transcripts": 0,
            "workbook_path": None, "transcript_zip_path": None,
        }
    package = row["Package path"] not in ("", "NOT_APPLICABLE")
    package_path = row["Package path"] if package else None
    workbook_path = transcript_zip_path = None
    if package_path:
        package_dir = root / package_path
        workbooks = sorted(package_dir.glob("*.xlsx"))
        archives = sorted(package_dir.glob("*.zip"))
        if len(workbooks) != 1 or len(archives) != 1:
            raise ValueError(f"Expected one workbook and transcript ZIP in {package_path}")
        workbook_path = workbooks[0].relative_to(root).as_posix()
        transcript_zip_path = archives[0].relative_to(root).as_posix()
    return {
        "dataset_ids": [row["Dataset"]],
        "video_count": as_int(row["Videos"]),
        "regular_videos": as_int(row["Regular"]),
        "shorts": as_int(row["Shorts"]),
        "livestreams": as_int(row["Live"]),
        "descriptions": as_int(row["Descriptions"]),
        "real_transcripts": as_int(row["Real transcripts"]),
        "placeholders": as_int(row["Placeholders"]),
        "missing_transcripts": as_int(row["Missing transcripts"]),
        "workbook_path": workbook_path,
        "transcript_zip_path": transcript_zip_path,
    }


def historical_dataset_links(root: Path) -> dict[str, list[str]]:
    connection = sqlite3.connect(root / "data/catalog/youtube_inventory.db")
    try:
        rows = connection.execute(
            """
            SELECT c.youtube_channel_id,l.dataset_id
            FROM channels c JOIN channel_dataset_links l USING(channel_id)
            ORDER BY c.youtube_channel_id,l.dataset_id
            """
        )
        result = defaultdict(list)
        for identifier, dataset_id in rows:
            result[identifier].append(dataset_id)
        return dict(result)
    finally:
        connection.close()


def inventory_only_channels(root: Path, represented_ids: set[str]) -> list[dict]:
    """Return canonical inventory channels missing from registry authorities."""
    connection = sqlite3.connect(root / "data/catalog/youtube_inventory.db")
    connection.row_factory = sqlite3.Row
    records = []
    try:
        for channel in connection.execute(
            "SELECT channel_id,youtube_channel_id,handle,display_name,channel_url,created_from_dataset_id FROM channels ORDER BY channel_id"
        ):
            identifier = channel["youtube_channel_id"]
            if not identifier or identifier in represented_ids:
                continue
            video_rows = list(connection.execute(
                """
                SELECT v.video_id,v.youtube_video_id,v.created_from_dataset_id,
                       s.description,s.thumbnail_url,s.video_type
                FROM videos v
                LEFT JOIN video_snapshots s ON s.video_id=v.video_id
                WHERE v.channel_id=?
                ORDER BY v.video_id
                """,
                (channel["channel_id"],),
            ))
            videos = {row["video_id"]: row for row in video_rows}
            video_ids = set(videos)
            dataset_ids = {
                row[0]
                for row in connection.execute(
                    "SELECT dataset_id FROM channel_dataset_links WHERE channel_id=?",
                    (channel["channel_id"],),
                )
                if row[0]
            }
            dataset_ids.update(row["created_from_dataset_id"] for row in videos.values() if row["created_from_dataset_id"])
            transcript_video_ids = {
                row[0]
                for row in connection.execute(
                    "SELECT DISTINCT video_id FROM transcripts WHERE video_id IN (SELECT video_id FROM videos WHERE channel_id=?) AND availability_status='AVAILABLE'",
                    (channel["channel_id"],),
                )
            }
            types = [str(row["video_type"] or "").lower() for row in videos.values()]
            records.append({
                "canonical_channel_id": identifier,
                "channel_name": channel["display_name"],
                "current_handle": channel["handle"],
                "canonical_url": channel["channel_url"] or f"https://www.youtube.com/channel/{identifier}",
                "primary_dataset_id": channel["created_from_dataset_id"],
                "dataset_ids": sorted(dataset_ids),
                "video_count": len(video_ids),
                "regular_videos": sum(value in {"video", "regular"} for value in types),
                "shorts": sum(value in {"short", "shorts"} for value in types),
                "livestreams": sum("live" in value or "stream" in value for value in types),
                "descriptions": sum(bool(row["description"]) for row in videos.values()),
                "real_transcripts": len(transcript_video_ids & video_ids),
                "placeholders": 0,
                "missing_transcripts": len(video_ids - transcript_video_ids),
                "workbook_path": None,
                "transcript_zip_path": None,
            })
    finally:
        connection.close()
    return records


def package_thumbnail_url_counts(root: Path, channels: list[dict]) -> dict[str, int]:
    counts = defaultdict(int)
    for dataset_id in ("DS-000020", "DS-000021", "DS-000023", "DS-000024", "DS-000025", "DS-000027", "DS-000028"):
        path = next((root / "data/extracted/channel-data" / dataset_id / "combined").glob("*_master.csv"))
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                if row["thumbnail_url"]:
                    counts[row["channel_id"]] += 1
    from openpyxl import load_workbook
    for channel in channels:
        if channel["primary_dataset_id"] != "DS-000022":
            continue
        book = load_workbook(root / channel["workbook_path"], read_only=True, data_only=True)
        try:
            sheet = book["All Videos"]
            headers = [cell.value for cell in next(sheet.iter_rows(min_row=4, max_row=4))]
            thumbnail_index = headers.index("Thumbnail URL")
            counts[channel["canonical_channel_id"]] = sum(
                bool(row[thumbnail_index]) for row in sheet.iter_rows(min_row=5, values_only=True) if row[1]
            )
        finally:
            book.close()
    return dict(counts)


def enrich_visual_coverage(root: Path, channels: list[dict], subjects: list[dict]) -> None:
    thumbnail_counts = package_thumbnail_url_counts(root, channels)
    internal_by_id = {}
    for identifier, row in ((canonical_id(row["Canonical ID"]), row) for row in read_coverage(root)):
        if identifier and " / " in row["Canonical ID"]:
            internal_by_id[identifier] = row["Canonical ID"].split(" / ")[0]
    for channel in channels:
        identifier = channel["canonical_channel_id"]
        internal = internal_by_id.get(identifier)
        thumbnail_url_count = thumbnail_counts.get(identifier, 0)
        downloaded_thumbnail_count = 0
        screenshot_count = keyframe_count = source_video_count = timestamped_count = 0
        evidence_path = channel["identity_evidence_source"]
        limitation = "No downloaded visual evidence is registered."
        if internal:
            package_files = sorted((root / "data/intelligence/channels" / internal).glob("packaging-intelligence*.json"))
            if package_files:
                packages = [(path, json.loads(path.read_text(encoding="utf-8"))) for path in package_files]
                package_path, package = max(packages, key=lambda item: len(item[1].get("thumbnail_snapshots", [])))
                snapshots = package.get("thumbnail_snapshots", [])
                thumbnail_url_count = max(thumbnail_url_count, len(snapshots))
                downloaded_thumbnail_count = len(snapshots)
                evidence_path = package_path.relative_to(root).as_posix()
                limitation = "; ".join(package.get("limitations", [])) or None
            if internal == "CH-000003":
                screenshot_count = 7
            if internal == "CH-000004":
                editing_path = root / "data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json"
                editing = json.loads(editing_path.read_text(encoding="utf-8"))
                measured = editing["measured_features"]
                keyframe_count = sum(item["keyframe_count"] for item in measured)
                source_video_count = editing["availability"]["forensic_video_count"]
                timestamped_count = sum(item["visual_state_count"] for item in measured)
                evidence_path = editing_path.relative_to(root).as_posix()
                limitation = "; ".join(editing["limitations"])
        if source_video_count:
            level = "FORENSIC_VIDEO_EVIDENCE"
            editing_status = "PARTIAL"
        elif downloaded_thumbnail_count:
            level = "THUMBNAIL_EVIDENCE"
            editing_status = "NOT_AVAILABLE"
        elif thumbnail_url_count:
            level = "THUMBNAIL_URL_ONLY"
            editing_status = "NOT_AVAILABLE"
            limitation = "Thumbnail URLs are metadata only; no downloaded thumbnail or forensic video evidence is registered."
        else:
            level = "NONE"
            editing_status = "NOT_AVAILABLE"
        channel["thumbnail_metadata_status"] = "COMPLETE" if thumbnail_url_count else "NONE"
        channel["visual_asset_status"] = level
        channel["forensic_video_status"] = "AVAILABLE_WITH_LIMITATIONS" if source_video_count else "NOT_AVAILABLE"
        channel["visual_coverage"] = {
            "thumbnail_url_count": thumbnail_url_count,
            "downloaded_thumbnail_count": downloaded_thumbnail_count,
            "screenshot_count": screenshot_count,
            "keyframe_count": keyframe_count,
            "registered_source_video_count": source_video_count,
            "timestamped_visual_observation_count": timestamped_count,
            "visual_evidence_level": level,
            "editing_visual_intelligence_status": editing_status,
            "evidence_path": evidence_path,
            "limitation_reason": limitation,
        }
    for subject in subjects:
        match = re.search(r"\((\d+) screenshots\)", subject["evidence_source"])
        subject.update({
            "screenshot_count": int(match.group(1)) if match else 0,
            "visual_evidence_level": "SCREENSHOT_ONLY_UNMAPPED",
            "evidence_path": subject["evidence_source"].split(" (")[0],
        })


def build_model(root: Path) -> dict:
    raw = json.loads((root / RAW_AUTHORITY).read_text(encoding="utf-8"))
    official = json.loads((root / IDENTITY_EVIDENCE).read_text(encoding="utf-8"))["entries"]
    official_by_url = {item["submitted_url"]: item for item in official}
    coverage = read_coverage(root)
    historical_links = historical_dataset_links(root)
    canonical_rows = [(canonical_id(row["Canonical ID"]), row) for row in coverage]
    canonical_rows = [(identifier, row) for identifier, row in canonical_rows if identifier]
    by_lookup = {}
    for identifier, row in canonical_rows:
        by_lookup[identifier.lower()] = (identifier, row)
        if row["Handle"].startswith("@"):
            by_lookup[row["Handle"].lstrip("@").lower()] = (identifier, row)

    submissions = []
    channel_groups = defaultdict(set)
    channel_submissions = defaultdict(list)
    target_identity = {}
    for raw_row in raw["submissions"]:
        normalized = raw_row["normalized_url"]
        found = by_lookup.get(normalized_lookup(normalized))
        if found:
            identifier, evidence_row = found
            identity = {
                "canonical_channel_id": identifier,
                "channel_name": evidence_row["Channel"],
                "current_handle": evidence_row["Handle"] if evidence_row["Handle"].startswith("@") else None,
                "canonical_url": f"https://www.youtube.com/channel/{identifier}",
                "evidence_source": COVERAGE_LEDGER,
                "verified_at": VERIFIED_AT,
                "handle_unavailable_reason": None,
                "coverage_row": evidence_row,
            }
        else:
            evidence = official_by_url.get(normalized)
            if not evidence:
                raise ValueError(f"No identity evidence for {normalized}")
            identifier = evidence["canonical_channel_id"]
            identity = {
                **evidence,
                "evidence_source": evidence["evidence_source"],
                "verified_at": VERIFIED_AT,
                "coverage_row": None,
            }
        group = "ORIGINAL_TARGET" if raw_row["batch"] == "A" else "ADDED_TARGET"
        channel_groups[identifier].add(group)
        channel_submissions[identifier].append(raw_row["global_row"])
        target_identity[identifier] = identity
        submissions.append({
            **raw_row,
            "canonical_channel_id": identifier,
            "identity_status": "DUPLICATE_INPUT" if raw_row["is_exact_duplicate"] else "VERIFIED",
            "evidence_source": identity["evidence_source"],
            "verified_at": VERIFIED_AT,
        })

    channels = []
    for identifier, identity in target_identity.items():
        evidence_row = identity["coverage_row"]
        metrics = coverage_metrics(root, evidence_row)
        primary_dataset_id = evidence_row["Dataset"] if evidence_row else None
        source_group = "STANDARD_PACKAGE" if metrics["workbook_path"] else ("HISTORICAL_CATALOG" if evidence_row else "IDENTITY_ONLY")
        if source_group == "HISTORICAL_CATALOG":
            metrics["dataset_ids"] = historical_links.get(identifier, metrics["dataset_ids"])
        limitations = channel_limitations(evidence_row) if evidence_row else []
        if metrics["video_count"]:
            status = "COMPLETE_WITH_LIMITATIONS" if limitations else "COMPLETE"
        else:
            status = "IDENTITY_VERIFIED_DATA_NOT_EXTRACTED"
        groups = channel_groups[identifier]
        target_group = "ORIGINAL_TARGET" if "ORIGINAL_TARGET" in groups else "ADDED_TARGET"
        channels.append({
            "canonical_channel_id": identifier,
            "channel_name": identity["channel_name"],
            "current_handle": identity.get("current_handle"),
            "canonical_url": identity["canonical_url"],
            "source_group": source_group,
            "primary_dataset_id": primary_dataset_id,
            "target_group": target_group,
            "status": status,
            "completed_tick": "✓" if status == "COMPLETE" else "",
            "identity_evidence_source": identity["evidence_source"],
            "verified_at": identity["verified_at"],
            "handle_unavailable_reason": identity.get("handle_availability_reason"),
            "limitations": limitations,
            "submission_rows": channel_submissions[identifier],
            "identity_status": "VERIFIED",
            "extraction_status": status if metrics["video_count"] else "NOT_EXTRACTED",
            "package_status": "STANDARD_PACKAGE" if source_group == "STANDARD_PACKAGE" else ("HISTORICAL_FORMAT" if source_group == "HISTORICAL_CATALOG" else "NO_PACKAGE"),
            "video_metadata_status": ("COMPLETE_WITH_LIMITATIONS" if primary_dataset_id == "DS-000001" else "COMPLETE") if metrics["video_count"] else "NONE",
            "description_status": "COMPLETE" if metrics["video_count"] and metrics["descriptions"] == metrics["video_count"] else ("PARTIAL" if metrics["descriptions"] else "NONE"),
            "transcript_status": "COMPLETE_WITH_PLACEHOLDERS" if metrics["placeholders"] else ("COMPLETE_REAL" if metrics["video_count"] and metrics["real_transcripts"] == metrics["video_count"] else ("PARTIAL" if metrics["real_transcripts"] else "NONE")),
            "intelligence_status": "PARTIAL" if source_group == "HISTORICAL_CATALOG" else ("DATA_READY" if source_group == "STANDARD_PACKAGE" else "NOT_AVAILABLE"),
            "first_party_analytics_status": "SCHEMA_READY_NO_DATA",
            **metrics,
        })

    target_ids = set(target_identity)
    for identifier, row in canonical_rows:
        if identifier in target_ids:
            continue
        metrics = coverage_metrics(root, row)
        primary_dataset_id = row["Dataset"]
        source_group = "STANDARD_PACKAGE" if metrics["workbook_path"] else "HISTORICAL_CATALOG"
        if source_group == "HISTORICAL_CATALOG":
            metrics["dataset_ids"] = historical_links.get(identifier, metrics["dataset_ids"])
        limitations = channel_limitations(row)
        status = "COMPLETE_WITH_LIMITATIONS" if limitations else "COMPLETE"
        channels.append({
            "canonical_channel_id": identifier,
            "channel_name": row["Channel"],
            "current_handle": row["Handle"] if row["Handle"].startswith("@") else None,
            "canonical_url": f"https://www.youtube.com/channel/{identifier}",
            "source_group": source_group,
            "primary_dataset_id": primary_dataset_id,
            "target_group": "OUTSIDE_TARGET",
            "status": status,
            "completed_tick": "✓" if status == "COMPLETE" else "",
            "identity_evidence_source": COVERAGE_LEDGER,
            "verified_at": VERIFIED_AT,
            "handle_unavailable_reason": None,
            "limitations": limitations,
            "submission_rows": [],
            "identity_status": "VERIFIED",
            "extraction_status": status,
            "package_status": "STANDARD_PACKAGE" if source_group == "STANDARD_PACKAGE" else "HISTORICAL_FORMAT",
            "video_metadata_status": "COMPLETE_WITH_LIMITATIONS" if primary_dataset_id == "DS-000001" else "COMPLETE",
            "description_status": "COMPLETE" if metrics["descriptions"] == metrics["video_count"] else "PARTIAL",
            "transcript_status": "COMPLETE_WITH_PLACEHOLDERS" if metrics["placeholders"] else ("COMPLETE_REAL" if metrics["real_transcripts"] == metrics["video_count"] else "PARTIAL"),
            "intelligence_status": "PARTIAL" if source_group == "HISTORICAL_CATALOG" else "DATA_READY",
            "first_party_analytics_status": "SCHEMA_READY_NO_DATA",
            **metrics,
        })

    represented_ids = {row["canonical_channel_id"] for row in channels}
    inventory_channels = inventory_only_channels(root, represented_ids)
    for inventory in inventory_channels:
        limitations = ["Canonical acquisition is registered in the inventory; no standard channel package exists yet."]
        video_count = inventory["video_count"]
        missing_descriptions = video_count - inventory["descriptions"]
        channels.append({
            "canonical_channel_id": inventory["canonical_channel_id"],
            "channel_name": inventory["channel_name"],
            "current_handle": inventory["current_handle"],
            "canonical_url": inventory["canonical_url"],
            "source_group": "HISTORICAL_CATALOG",
            "primary_dataset_id": inventory["primary_dataset_id"],
            "target_group": "OUTSIDE_TARGET",
            "status": "COMPLETE_WITH_LIMITATIONS" if video_count else "IDENTITY_VERIFIED_DATA_NOT_EXTRACTED",
            "completed_tick": "",
            "identity_evidence_source": "data/catalog/youtube_inventory.db",
            "verified_at": VERIFIED_AT,
            "handle_unavailable_reason": None,
            "limitations": limitations,
            "submission_rows": [],
            "identity_status": "VERIFIED",
            "extraction_status": "COMPLETE_WITH_LIMITATIONS" if video_count else "NOT_EXTRACTED",
            "package_status": "HISTORICAL_FORMAT" if video_count else "NO_PACKAGE",
            "video_metadata_status": "COMPLETE" if video_count else "NONE",
            "description_status": "COMPLETE" if video_count and not missing_descriptions else ("PARTIAL" if inventory["descriptions"] else "NONE"),
            "transcript_status": "COMPLETE_REAL" if video_count and inventory["real_transcripts"] == video_count else ("PARTIAL" if inventory["real_transcripts"] else "NONE"),
            "intelligence_status": "PARTIAL" if video_count else "NOT_AVAILABLE",
            "first_party_analytics_status": "SCHEMA_READY_NO_DATA",
            **{key: value for key, value in inventory.items() if key not in {"canonical_channel_id", "channel_name", "current_handle", "canonical_url", "primary_dataset_id"}},
        })

    resolved_names = {re.sub(r"[^a-z0-9]", "", row["channel_name"].lower()) for row in inventory_channels}
    screenshot_rows = [
        row for row in coverage
        if canonical_id(row["Canonical ID"]) is None
        and row["Dataset"] in {f"DS-{n:06d}" for n in range(3, 11)}
        and re.sub(r"[^a-z0-9]", "", row["Channel"].lower()) not in resolved_names
    ]
    subjects = [{
        "subject_id": f"SUBJ-{index:06d}",
        "subject_name": row["Channel"],
        "canonical_channel_id": None,
        "identity_status": "PENDING_IDENTITY_RESOLUTION",
        "evidence_source": row["Raw evidence"],
        "dataset_id": row["Dataset"],
        "limitation": "Screenshot-only subject; canonical YouTube identity and video population are not established.",
    } for index, row in enumerate(screenshot_rows, 1)]

    package_rows = [row for _, row in canonical_rows if int(row["Dataset"].split("-")[1]) >= 20]
    enrich_visual_coverage(root, channels, subjects)
    capabilities, intelligence_coverage = _intelligence_records(root, {"channels": channels})
    first_party_evidence = "data/intelligence/system/first-party-analytics-capability-status-2026-09-11.json"
    for channel in channels:
        evidence = channel["identity_evidence_source"]
        data_evidence = channel["workbook_path"] or evidence
        visual = channel["visual_coverage"]
        channel["layer_evidence"] = {
            "identity_status": {"evidence_path": evidence, "limitation_reason": channel["handle_unavailable_reason"]},
            "extraction_status": {"evidence_path": data_evidence, "limitation_reason": "; ".join(channel["limitations"]) or ("Identity verified; extraction not started." if channel["video_count"] == 0 else None)},
            "package_status": {"evidence_path": data_evidence, "limitation_reason": None if channel["package_status"] == "STANDARD_PACKAGE" else ("Historical catalog format; no new-style package." if channel["package_status"] == "HISTORICAL_FORMAT" else "No package because extraction has not started.")},
            "video_metadata_status": {"evidence_path": data_evidence, "limitation_reason": "No stored video metadata." if channel["video_count"] == 0 else ("Historical video type is unavailable." if channel["primary_dataset_id"] == "DS-000001" else None)},
            "description_status": {"evidence_path": data_evidence, "limitation_reason": None if channel["description_status"] == "COMPLETE" else (f"{channel['video_count'] - channel['descriptions']} videos lack public descriptions." if channel["video_count"] else "No stored videos.")},
            "transcript_status": {"evidence_path": channel["transcript_zip_path"] or data_evidence, "limitation_reason": f"{channel['placeholders']} explicit transcript placeholders." if channel["placeholders"] else ("No stored transcripts." if channel["video_count"] == 0 else None)},
            "thumbnail_metadata_status": {"evidence_path": visual["evidence_path"], "limitation_reason": None if channel["thumbnail_metadata_status"] == "COMPLETE" else "No canonical thumbnail reference."},
            "visual_asset_status": {"evidence_path": visual["evidence_path"], "limitation_reason": visual["limitation_reason"]},
            "forensic_video_status": {"evidence_path": visual["evidence_path"], "limitation_reason": visual["limitation_reason"]},
            "intelligence_status": {"evidence_path": "data/intelligence/system/youtube-intelligence-os-v1-capabilities-2026-09-11.json", "limitation_reason": "Capability-level rows preserve generated, data-ready, and unavailable states."},
            "first_party_analytics_status": {"evidence_path": first_party_evidence, "limitation_reason": "No real YouTube Studio or Analytics export is ingested."},
        }

    controls = {
        "submitted_rows": len(submissions),
        "normalized_url_identities": len({row["normalized_url"] for row in submissions}),
        "canonical_target_channels": len(target_ids),
        "all_canonical_channels": len(channels),
        "source_groups": {
            "standard_packages": sum(row["source_group"] == "STANDARD_PACKAGE" for row in channels),
            "historical_catalog": sum(row["source_group"] == "HISTORICAL_CATALOG" for row in channels),
            "identity_only": sum(row["source_group"] == "IDENTITY_ONLY" for row in channels),
        },
        "visual_evidence": {
            "forensic_channels": sum(row["visual_asset_status"] == "FORENSIC_VIDEO_EVIDENCE" for row in channels),
            "thumbnail_evidence_channels": sum(row["visual_asset_status"] in {"THUMBNAIL_EVIDENCE", "FORENSIC_VIDEO_EVIDENCE"} for row in channels),
            "title_only_historical_channels": sum(row["source_group"] == "HISTORICAL_CATALOG" and row["thumbnail_metadata_status"] == "NONE" for row in channels),
            "unmapped_screenshot_subjects": len(subjects),
        },
        "package_layer": {
            "channels": len(package_rows),
            "unique_videos": sum(as_int(row["Videos"]) for row in package_rows),
            "real_transcripts": sum(as_int(row["Real transcripts"]) for row in package_rows),
            "placeholders": sum(as_int(row["Placeholders"]) for row in package_rows),
            "missing_descriptions": sum(as_int(row["Videos"]) - as_int(row["Descriptions"]) for row in package_rows),
        },
    }
    if controls["canonical_target_channels"] != len({row["canonical_channel_id"] for row in submissions}):
        raise ValueError("Canonical target deduplication failed")
    channels.sort(key=lambda row: ({"ORIGINAL_TARGET": 0, "ADDED_TARGET": 1, "OUTSIDE_TARGET": 2}[row["target_group"]], min(row["submission_rows"] or [999]), row["channel_name"].lower()))
    return {
        "schema_version": 2,
        "generated_at": VERIFIED_AT,
        "controls": controls,
        "channels": channels,
        "submissions": submissions,
        "subjects": subjects,
        "intelligence_capabilities": capabilities,
        "intelligence_coverage": intelligence_coverage,
    }


def _dataset_records(root: Path) -> list[dict]:
    records = []
    paths = sorted(
        path for path in (root / "data/manifests").glob("DS-*.md")
        if re.fullmatch(r"DS-\d{6}\.md", path.name)
    )
    for path in paths:
        dataset_id = path.stem
        text = path.read_text(encoding="utf-8")
        heading = next((line.removeprefix("# ").strip() for line in text.splitlines() if line.startswith("# ")), dataset_id)
        records.append({"dataset_id": dataset_id, "dataset_name": heading, "manifest_path": path.relative_to(root).as_posix(), "evidence_scope": None, "limitations": None})
    return records


def _parse_structured_transcript(text: str) -> tuple[str, bool, str | None]:
    if "\nDESCRIPTION\n" in text and "\nTRANSCRIPT\n" in text:
        marker = re.search(r"\n={5,}\nTRANSCRIPT\n={5,}\n", text)
        if not marker:
            raise ValueError("Structured transcript has no valid TRANSCRIPT section")
        body = text[marker.end():].strip()
        lower = body.lower()
        placeholder = body.startswith("(") and any(value in lower for value in (
            "no transcript available", "members-only video", "captions unavailable",
            "captions disabled", "video unavailable", "actor extraction failed",
        ))
        return body, placeholder, body if placeholder else None
    return text.strip(), False, None


def _historical_records(root: Path) -> tuple[list[dict], list[dict], list[dict]]:
    source = sqlite3.connect(root / "data/catalog/youtube_inventory.db")
    source.row_factory = sqlite3.Row
    sql = """
      SELECT v.youtube_video_id,c.youtube_channel_id,v.canonical_url,v.created_from_dataset_id AS dataset_id,
             s.title,s.published_at,s.duration_seconds,s.video_type,s.views,s.likes,s.comments,
             s.description,s.thumbnail_url,t.availability_status,t.caption_type,t.language,t.word_count,
             t.canonical_reference,t.transcript_sha256,t.notes,sf.archive_member_path
      FROM videos v JOIN channels c ON c.channel_id=v.channel_id
      JOIN video_snapshots s ON s.video_id=v.video_id
      JOIN transcripts t ON t.video_id=v.video_id AND t.dataset_id=v.created_from_dataset_id
      JOIN source_files sf ON sf.file_id=t.archive_member_file_id
    """
    videos, transcripts, memberships = [], [], []
    try:
        for row in source.execute(sql):
            reference = row["canonical_reference"] or (
                "data/raw/competitors/DS-000001/Transcripts_All_159_Videos.zip::"
                + row["archive_member_path"]
            )
            path_part, separator, member = reference.partition("::")
            source_path = Path(path_part)
            if source_path.is_absolute():
                if source_path.is_relative_to(root):
                    relative_path = source_path.relative_to(root)
                elif "/data/" in source_path.as_posix():
                    relative_path = Path("data") / source_path.as_posix().split("/data/", 1)[1]
                else:
                    raise ValueError(f"Historical source is outside repository data: {source_path}")
            else:
                relative_path = source_path
            local_path = (root / relative_path).resolve()
            if not local_path.is_relative_to(root.resolve()) or not local_path.is_file():
                raise FileNotFoundError(f"Historical source missing in selected repository: {relative_path}")
            portable_reference = relative_path.as_posix() + (f"::{member}" if separator else "")
            if separator:
                with zipfile.ZipFile(local_path) as archive:
                    text = archive.read(member).decode("utf-8")
            else:
                text = local_path.read_text(encoding="utf-8")
            body, parsed_placeholder, reason = _parse_structured_transcript(text)
            description = row["description"]
            if description is None and "\nDESCRIPTION\n" in text:
                description_marker = re.search(r"\n={5,}\nDESCRIPTION\n={5,}\n", text)
                transcript_marker = re.search(r"\n={5,}\nTRANSCRIPT\n={5,}\n", text)
                if description_marker and transcript_marker:
                    description = text[description_marker.end():transcript_marker.start()].strip() or None
            placeholder = parsed_placeholder or row["availability_status"] != "AVAILABLE"
            if placeholder and not reason:
                reason = row["notes"] or body
            videos.append({
                "youtube_video_id": row["youtube_video_id"], "canonical_channel_id": row["youtube_channel_id"],
                "canonical_url": row["canonical_url"], "title": row["title"], "published_at": row["published_at"],
                "duration_seconds": row["duration_seconds"], "video_type": row["video_type"], "views": row["views"],
                "likes": row["likes"], "comments": row["comments"], "description": description,
                "description_unavailable_reason": None if description is not None else "Description unavailable in historical catalog.",
                "thumbnail_url": row["thumbnail_url"], "raw_json": None,
            })
            transcripts.append({
                "youtube_video_id": row["youtube_video_id"], "dataset_id": row["dataset_id"],
                "transcript_text": body, "word_count": row["word_count"], "language": row["language"],
                "caption_type": row["caption_type"], "is_placeholder": int(placeholder), "unavailable_reason": reason,
                "evidence_locator": portable_reference,
                "transcript_sha256": row["transcript_sha256"] or sha256_bytes(body.encode("utf-8")),
            })
            memberships.append({"dataset_id": row["dataset_id"], "youtube_video_id": row["youtube_video_id"], "evidence_locator": portable_reference})
    finally:
        source.close()
    return videos, transcripts, memberships


def _combined_package_records(root: Path) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    videos, transcripts, memberships, runs = [], [], [], []
    verified_missing_descriptions = {
        item["video_id"]
        for item in json.loads((root / "data/manifests/DS-000020-description-recovery-verification.json").read_text(encoding="utf-8"))["items"]
    }
    for dataset_id in ("DS-000020", "DS-000021", "DS-000023", "DS-000024", "DS-000025", "DS-000027", "DS-000028"):
        path = next((root / "data/extracted/channel-data" / dataset_id / "combined").glob("*_master.csv"))
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                video_id = row["video_id"]
                channel_id = row["channel_id"]
                description = None if video_id in verified_missing_descriptions else (row["description"] or None)
                transcript_text = row["transcript_plaintext"] or None
                unavailable = row["transcript_unavailable_reason"] or None
                raw_fields = {key: value for key, value in row.items() if key.startswith("actor_") or key in {"subtitles_json", "ai_summary", "ai_description"}}
                videos.append({
                    "youtube_video_id": video_id, "canonical_channel_id": channel_id,
                    "canonical_url": row["canonical_youtube_video_url"], "title": row["video_title"],
                    "published_at": row["publication_date_time"] or None,
                    "duration_seconds": duration_seconds(row), "video_type": row["content_type"] or None,
                    "views": nullable_int(row["view_count"]), "likes": nullable_int(row["like_count"]),
                    "comments": nullable_int(row["comment_count"]), "description": description,
                    "description_unavailable_reason": None if description else "Verified no public description.",
                    "thumbnail_url": row["thumbnail_url"] or None,
                    "raw_json": json.dumps(raw_fields, ensure_ascii=False, sort_keys=True),
                })
                placeholder = transcript_text is None
                transcripts.append({
                    "youtube_video_id": video_id, "dataset_id": dataset_id, "transcript_text": transcript_text,
                    "word_count": len(transcript_text.split()) if transcript_text else 0,
                    "language": row["subtitle_languages"] or None, "caption_type": row["subtitle_types"] or None,
                    "is_placeholder": int(placeholder), "unavailable_reason": unavailable,
                    "evidence_locator": path.relative_to(root).as_posix(),
                    "transcript_sha256": sha256_bytes(transcript_text.encode("utf-8")) if transcript_text else None,
                })
                memberships.append({"dataset_id": dataset_id, "youtube_video_id": video_id, "evidence_locator": path.relative_to(root).as_posix()})
                run_id = row["actor_run_id"]
                if run_id and not any(item["actor_run_id"] == run_id for item in runs):
                    runs.append({"actor_run_id": run_id, "actor_dataset_id": row["actor_dataset_id"] or None, "dataset_id": dataset_id, "actor_name": "streamers/youtube-scraper", "evidence_path": path.relative_to(root).as_posix(), "run_status": "SUCCEEDED", "raw_json": None})
    return videos, transcripts, memberships, runs


def _ds22_records(root: Path, model: dict) -> tuple[list[dict], list[dict], list[dict]]:
    from openpyxl import load_workbook

    channels_by_package = {Path(row["workbook_path"]).parent.as_posix(): row for row in model["channels"] if row["primary_dataset_id"] == "DS-000022"}
    videos, transcripts, memberships = [], [], []
    for package_dir in sorted((root / "data/extracted/channel-data/DS-000022/packages").iterdir()):
        if not package_dir.is_dir():
            continue
        rel_dir = package_dir.relative_to(root).as_posix()
        channel = channels_by_package[rel_dir]
        workbook_path = next(package_dir.glob("*.xlsx"))
        zip_path = next(package_dir.glob("*.zip"))
        book = load_workbook(workbook_path, read_only=True, data_only=True)
        try:
            video_sheet = book["All Videos"]
            headers = [cell.value for cell in next(video_sheet.iter_rows(min_row=4, max_row=4))]
            description_sheet = book["Descriptions"]
            description_headers = [cell.value for cell in next(description_sheet.iter_rows(min_row=4, max_row=4))]
            descriptions = {str(dict(zip(description_headers, values))["Video ID"]): dict(zip(description_headers, values))["Full Description"] for values in description_sheet.iter_rows(min_row=5, values_only=True) if values[1]}
            workbook_rows = [dict(zip(headers, values)) for values in video_sheet.iter_rows(min_row=5, values_only=True) if values[1]]
        finally:
            book.close()
        with zipfile.ZipFile(zip_path) as archive:
            by_video = {}
            for member in archive.namelist():
                if member == "INDEX.txt":
                    continue
                text = archive.read(member).decode("utf-8")
                body, placeholder, reason = _parse_structured_transcript(text)
                headers = dict(re.findall(r"^([^:\n]+?)\s*:\s*(.*)$", text.split("\n==========", 1)[0], re.MULTILINE))
                by_video[headers["Video ID"]] = (member, headers, body, placeholder, reason)
        for row in workbook_rows:
            video_id = str(row["Video ID"])
            member, headers, body, placeholder, reason = by_video[video_id]
            description = descriptions.get(video_id)
            videos.append({
                "youtube_video_id": video_id, "canonical_channel_id": channel["canonical_channel_id"],
                "canonical_url": f"https://www.youtube.com/watch?v={video_id}", "title": row["Title"],
                "published_at": str(row["Published (UTC)"]) if row["Published (UTC)"] else None,
                "duration_seconds": nullable_int(row["Sec"]), "video_type": "video", "views": nullable_int(row["Views"]),
                "likes": nullable_int(row["Likes"]), "comments": nullable_int(row["Comments"]), "description": description,
                "description_unavailable_reason": None if description else "Description unavailable in supplied package.",
                "thumbnail_url": row["Thumbnail URL"], "raw_json": json.dumps({key: value for key, value in row.items() if value is not None}, default=str, ensure_ascii=False, sort_keys=True),
            })
            transcripts.append({
                "youtube_video_id": video_id, "dataset_id": "DS-000022", "transcript_text": body,
                "word_count": as_int(row["Transcript Words"]), "language": headers.get("Language"),
                "caption_type": headers.get("Caption type"), "is_placeholder": int(placeholder),
                "unavailable_reason": reason,
                "evidence_locator": f"{zip_path.relative_to(root).as_posix()}::{member}",
                "transcript_sha256": sha256_bytes(body.encode("utf-8")),
            })
            memberships.append({"dataset_id": "DS-000022", "youtube_video_id": video_id, "evidence_locator": workbook_path.relative_to(root).as_posix()})
    return videos, transcripts, memberships


def _artifact_records(root: Path, model: dict) -> list[dict]:
    records = []
    registered_datasets = {row["dataset_id"] for row in _dataset_records(root)}
    channel_by_package = {Path(row["workbook_path"]).parent.as_posix(): row["canonical_channel_id"] for row in model["channels"] if row["workbook_path"]}
    for path in sorted((root / "data/extracted/channel-data").rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        match = re.search(r"(DS-\d{6})", rel)
        dataset_id = match.group(1) if match else None
        channel_id = next((identifier for package, identifier in channel_by_package.items() if rel.startswith(package + "/")), None)
        suffix = path.suffix.lower()
        if suffix == ".xlsx":
            artifact_type = "WORKBOOK" if channel_id else "COMBINED_XLSX"
        elif suffix == ".zip":
            artifact_type = "TRANSCRIPT_ZIP"
        elif suffix == ".json":
            artifact_type = "COMBINED_JSON" if "/combined/" in rel else "VALIDATION_JSON"
        elif suffix == ".csv":
            artifact_type = "COMBINED_CSV" if "/combined/" in rel else "VALIDATION_CSV"
        else:
            artifact_type = "VALIDATION_REPORT"
        records.append({"dataset_id": dataset_id, "canonical_channel_id": channel_id, "artifact_type": artifact_type, "repository_path": rel, "sha256": sha256_file(path), "availability_status": "AVAILABLE", "unavailable_reason": None})
    for path in sorted((root / "data/raw/channel-data").rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        match = re.search(r"(DS-\d{6})", rel)
        dataset_id = match.group(1) if match else None
        records.append({
            "dataset_id": dataset_id if dataset_id in registered_datasets else None,
            "canonical_channel_id": None,
            "artifact_type": "RAW_ACTOR_EVIDENCE" if "/apify/" in rel else "RAW_SOURCE_EVIDENCE",
            "repository_path": rel,
            "sha256": sha256_file(path),
            "availability_status": "AVAILABLE",
            "unavailable_reason": None,
        })
    for path in sorted((root / "data/manifests").glob("DS-0000*")):
        if path.is_file():
            match = re.match(r"(DS-\d{6})", path.name)
            if match:
                records.append({"dataset_id": match.group(1), "canonical_channel_id": None, "artifact_type": "MANIFEST", "repository_path": path.relative_to(root).as_posix(), "sha256": sha256_file(path), "availability_status": "AVAILABLE", "unavailable_reason": None})
    return records


def _intelligence_records(root: Path, model: dict) -> tuple[list[dict], list[dict]]:
    capabilities = [
        ("TOPIC_OPPORTUNITY", "Topic Opportunity Intelligence"),
        ("PACKAGING", "Packaging, Title, and Thumbnail Intelligence"),
        ("HOOK", "Hook Intelligence"),
        ("SCRIPT", "Script Intelligence"),
        ("EDITING_VISUAL", "Editing and Visual Intelligence"),
        ("UNIFIED_ORCHESTRATION", "Unified Orchestration"),
        ("CHANNEL_STRATEGY", "Channel Strategy Intelligence"),
        ("FIRST_PARTY_ANALYTICS", "First-party Analytics Ingestion Readiness"),
    ]
    historical: dict[str, str] = {}
    for row in read_coverage(root):
        identifier = canonical_id(row["Canonical ID"])
        internal = (row["Canonical ID"].split(" / ")[0] if " / " in row["Canonical ID"] else None)
        if identifier and internal and internal.startswith("CH-"):
            historical[identifier] = internal
    system_capabilities = "data/intelligence/system/youtube-intelligence-os-v1-capabilities-2026-09-11.json"
    first_party = "data/intelligence/system/first-party-analytics-capability-status-2026-09-11.json"
    calibration = "data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json"
    records = []
    for channel in model["channels"]:
        identifier = channel["canonical_channel_id"]
        internal = historical.get(identifier)
        channel_dir = root / "data/intelligence/channels" / internal if internal else None
        patterns = {
            "TOPIC_OPPORTUNITY": "topic-opportunity-intelligence*.json",
            "PACKAGING": "packaging-intelligence*.json",
            "HOOK": "hook-script-intelligence*.json",
            "SCRIPT": "hook-script-intelligence*.json",
            "EDITING_VISUAL": "editing-visual-intelligence*.json",
            "CHANNEL_STRATEGY": "channel-strategy-diagnosis*.json",
        }
        for capability_id, _ in capabilities:
            paths: list[Path] = []
            if capability_id == "UNIFIED_ORCHESTRATION" and internal:
                paths = sorted((root / "data/intelligence/plans").glob(f"{internal}-*-content-intelligence-v1.json"))
            elif capability_id == "CHANNEL_STRATEGY" and internal == "CH-000003":
                paths = [root / "data/intelligence/cross-channel/health-channel-strategy-benchmark-2026-09-11.json"]
            elif capability_id in patterns and channel_dir and channel_dir.is_dir():
                paths = sorted(channel_dir.glob(patterns[capability_id]))
            if capability_id == "FIRST_PARTY_ANALYTICS":
                status, input_available, generated, evidence, limitation = (
                    "DATA_READY", False, False, first_party,
                    "Schema and ingestion code are ready, but no real YouTube Studio or Analytics export is ingested.",
                )
            elif paths:
                status = "VALIDATED"
                limitation = None
                if capability_id == "PACKAGING" and internal in {"CH-000001", "CH-000002"}:
                    status = "PARTIAL"
                    limitation = "Title-only packaging intelligence; canonical thumbnail references are absent."
                elif capability_id == "EDITING_VISUAL":
                    status = "PARTIAL"
                    limitation = "Only three canonical videos have registered forensic visual-temporal evidence."
                elif capability_id == "CHANNEL_STRATEGY":
                    status = "PARTIAL"
                    limitation = "Generalized on two channels per niche; no heuristic is a robust cross-niche pattern."
                elif capability_id in {"HOOK", "SCRIPT"}:
                    limitation = "Untimed transcripts use positional approximations; timing is not exact."
                input_available = True
                generated = True
                evidence = paths[-1].relative_to(root).as_posix()
            elif channel["source_group"] == "STANDARD_PACKAGE" and capability_id in {"TOPIC_OPPORTUNITY", "PACKAGING", "HOOK", "SCRIPT"}:
                status, input_available, generated, evidence, limitation = (
                    "DATA_READY", True, False, channel["workbook_path"],
                    "Required public package inputs exist; no channel-specific intelligence artifact is generated.",
                )
            else:
                status, input_available, generated, evidence, limitation = (
                    "NOT_AVAILABLE", False, False, system_capabilities,
                    "Required input evidence or generated channel-specific artifact is unavailable.",
                )
                if capability_id == "CHANNEL_STRATEGY":
                    evidence = calibration
                if capability_id == "EDITING_VISUAL":
                    evidence = channel["visual_coverage"]["evidence_path"]
                    limitation = "No registered forensic video evidence; transcripts and thumbnail URLs are not substitutes."
            records.append({
                "canonical_channel_id": identifier,
                "capability_id": capability_id,
                "status": status,
                "input_data_available": bool(input_available),
                "generated_artifact_available": bool(generated),
                "evidence_path": evidence,
                "limitation_reason": limitation,
                "last_verified_at": VERIFIED_AT,
            })
    return [{"capability_id": item[0], "capability_name": item[1]} for item in capabilities], records


def _actor_run_records(root: Path, package_runs: list[dict]) -> list[dict]:
    records = {row["actor_run_id"]: row for row in package_runs}
    source = sqlite3.connect(root / "data/catalog/youtube_inventory.db")
    source.row_factory = sqlite3.Row
    try:
        for row in source.execute("SELECT actor_run_id,default_dataset_id,dataset_id,actor_name,run_status,input_json FROM apify_source_runs"):
            records[row["actor_run_id"]] = {
                "actor_run_id": row["actor_run_id"], "actor_dataset_id": row["default_dataset_id"],
                "dataset_id": row["dataset_id"], "actor_name": row["actor_name"],
                "evidence_path": f"data/manifests/apify/{row['actor_run_id']}.json",
                "run_status": row["run_status"], "raw_json": row["input_json"],
            }
    finally:
        source.close()
    for path in sorted((root / "data/manifests").glob("DS-00002*_CONFIG.json")):
        config = json.loads(path.read_text(encoding="utf-8"))
        for key in ("run", "recoveryRun"):
            run = config.get(key)
            if run:
                records[run["id"]] = {
                    "actor_run_id": run["id"], "actor_dataset_id": run.get("datasetId"),
                    "dataset_id": config["datasetId"], "actor_name": "streamers/youtube-scraper",
                    "evidence_path": path.relative_to(root).as_posix(), "run_status": run.get("status"),
                    "raw_json": json.dumps(run, sort_keys=True),
                }
    description_recovery = json.loads((root / "data/manifests/DS-000020-description-recovery-verification.json").read_text(encoding="utf-8"))
    records[description_recovery["actor_run_id"]] = {
        "actor_run_id": description_recovery["actor_run_id"], "actor_dataset_id": description_recovery["apify_dataset_id"],
        "dataset_id": "DS-000020", "actor_name": description_recovery["actor"],
        "evidence_path": "data/manifests/DS-000020-description-recovery-verification.json",
        "run_status": "SUCCEEDED", "raw_json": json.dumps(description_recovery, sort_keys=True),
    }
    recovery = json.loads((root / "data/extracted/channel-data/DS-000022/recovery/dmUFY1GHENjMdqsB9/recovery_clean.json").read_text(encoding="utf-8"))
    records[recovery["run_id"]] = {
        "actor_run_id": recovery["run_id"], "actor_dataset_id": recovery.get("dataset_id"),
        "dataset_id": "DS-000022", "actor_name": "streamers/youtube-scraper",
        "evidence_path": "data/extracted/channel-data/DS-000022/recovery/dmUFY1GHENjMdqsB9/recovery_clean.json",
        "run_status": "SUCCEEDED", "raw_json": json.dumps({key: value for key, value in recovery.items() if key != "items"}, sort_keys=True),
    }
    return list(records.values())


def _all_records(root: Path, model: dict):
    historical = _historical_records(root)
    combined = _combined_package_records(root)
    ds22 = _ds22_records(root, model)
    videos = historical[0] + combined[0] + ds22[0]
    transcripts = historical[1] + combined[1] + ds22[1]
    memberships = historical[2] + combined[2] + ds22[2]
    by_id = {}
    for video in videos:
        existing = by_id.get(video["youtube_video_id"])
        if existing and existing["canonical_channel_id"] != video["canonical_channel_id"]:
            raise ValueError(f"Video {video['youtube_video_id']} has conflicting channels")
        if not existing:
            by_id[video["youtube_video_id"]] = video
    return list(by_id.values()), transcripts, memberships, _actor_run_records(root, combined[3])


def connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _upsert(connection: sqlite3.Connection, table: str, row: dict, conflict: tuple[str, ...]) -> None:
    columns = list(row)
    updates = [column for column in columns if column not in conflict]
    action = (
        "DO UPDATE SET " + ",".join(f"{column}=excluded.{column}" for column in updates)
        if updates else "DO NOTHING"
    )
    sql = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join('?' for _ in columns)}) ON CONFLICT ({','.join(conflict)}) {action}"
    connection.execute(sql, [row[column] for column in columns])


def table_counts(connection: sqlite3.Connection) -> dict:
    tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'transcript_fts%' ORDER BY name")]
    return {table: connection.execute(f"SELECT count(*) FROM {table}").fetchone()[0] for table in tables}


def _validate_foreign_key_inputs(model: dict, datasets: list[dict], videos: list[dict]) -> None:
    channel_ids = {row["canonical_channel_id"] for row in model["channels"]}
    dataset_ids = {row["dataset_id"] for row in datasets}
    for video in videos:
        if video["canonical_channel_id"] not in channel_ids:
            raise ValueError(
                f"video {video['youtube_video_id']} references missing channel {video['canonical_channel_id']}"
            )
    for channel in model["channels"]:
        for dataset_id in channel["dataset_ids"]:
            if dataset_id not in dataset_ids:
                raise ValueError(
                    f"channel {channel['canonical_channel_id']} references missing dataset {dataset_id}"
                )


def build_database(root: Path, database_path: Path, model: dict | None = None) -> dict:
    model = model or build_model(root)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = database_path.with_name(database_path.name + ".tmp")
    temporary_path.unlink(missing_ok=True)
    connection = connect(temporary_path)
    counts = None
    try:
        connection.executescript((root / SCHEMA).read_text(encoding="utf-8"))
        videos, transcripts, memberships, actor_runs = _all_records(root, model)
        artifacts = _artifact_records(root, model)
        datasets = _dataset_records(root)
        _validate_foreign_key_inputs(model, datasets, videos)
        capabilities = model["intelligence_capabilities"]
        intelligence = model["intelligence_coverage"]
        with connection:
            for dataset in datasets:
                _upsert(connection, "datasets", dataset, ("dataset_id",))
            for channel in model["channels"]:
                _upsert(connection, "channels", {
                    "canonical_channel_id": channel["canonical_channel_id"], "channel_name": channel["channel_name"],
                    "current_handle": channel["current_handle"], "canonical_url": channel["canonical_url"],
                    "source_group": channel["source_group"],
                    "target_group": channel["target_group"], "status": channel["status"], "completed_tick": channel["completed_tick"],
                    "identity_status": channel["identity_status"], "extraction_status": channel["extraction_status"],
                    "package_status": channel["package_status"], "video_metadata_status": channel["video_metadata_status"],
                    "description_status": channel["description_status"], "transcript_status": channel["transcript_status"],
                    "thumbnail_metadata_status": channel["thumbnail_metadata_status"], "visual_asset_status": channel["visual_asset_status"],
                    "forensic_video_status": channel["forensic_video_status"], "intelligence_status": channel["intelligence_status"],
                    "first_party_analytics_status": channel["first_party_analytics_status"],
                    "identity_verified_at": channel["verified_at"], "identity_evidence_source": channel["identity_evidence_source"],
                    "handle_unavailable_reason": channel["handle_unavailable_reason"], "limitations": "; ".join(channel["limitations"]) or None,
                }, ("canonical_channel_id",))
                _upsert(connection, "identity_evidence", {
                    "evidence_id": stable_id(channel["canonical_channel_id"], channel["identity_evidence_source"]),
                    "canonical_channel_id": channel["canonical_channel_id"],
                    "source_type": "REPOSITORY" if channel["identity_evidence_source"] == COVERAGE_LEDGER else "OFFICIAL_YOUTUBE",
                    "source_locator": channel["identity_evidence_source"], "verified_at": channel["verified_at"],
                    "observed_name": channel["channel_name"], "observed_handle": channel["current_handle"], "raw_json": None,
                }, ("evidence_id",))
                for dataset_id in channel["dataset_ids"]:
                    relationship = "PACKAGE_CHANNEL" if channel["source_group"] == "STANDARD_PACKAGE" else ("CANONICAL_CHANNEL" if dataset_id == channel["primary_dataset_id"] else "FORENSIC_EVIDENCE")
                    _upsert(connection, "dataset_channels", {"dataset_id": dataset_id, "canonical_channel_id": channel["canonical_channel_id"], "relationship": relationship}, ("dataset_id", "canonical_channel_id", "relationship"))
                for layer_name, layer in channel["layer_evidence"].items():
                    _upsert(connection, "channel_data_layers", {
                        "canonical_channel_id": channel["canonical_channel_id"], "layer_name": layer_name,
                        "status": channel[layer_name], "evidence_path": layer["evidence_path"],
                        "limitation_reason": layer["limitation_reason"], "last_verified_at": channel["verified_at"],
                    }, ("canonical_channel_id", "layer_name"))
                _upsert(connection, "visual_coverage", {
                    "canonical_channel_id": channel["canonical_channel_id"], **channel["visual_coverage"]
                }, ("canonical_channel_id",))
                for field, reason in (
                    ("videos", "Identity verified; channel data not extracted." if channel["video_count"] == 0 else None),
                    ("current_handle", channel["handle_unavailable_reason"]),
                ):
                    if reason:
                        _upsert(connection, "availability_gaps", {"canonical_channel_id": channel["canonical_channel_id"], "field_name": field, "unavailable_reason": reason, "evidence_source": channel["identity_evidence_source"]}, ("canonical_channel_id", "field_name", "unavailable_reason"))
            for item in model["submissions"]:
                _upsert(connection, "submissions", {key: int(value) if key == "is_exact_duplicate" else value for key, value in item.items()}, ("global_row",))
                _upsert(connection, "channel_aliases", {"alias_id": stable_id(item["canonical_channel_id"], item["original_url"], item["global_row"]), "canonical_channel_id": item["canonical_channel_id"], "alias_url": item["original_url"], "alias_kind": "SUBMITTED_URL", "submission_global_row": item["global_row"]}, ("alias_id",))
            for channel in model["channels"]:
                _upsert(connection, "channel_aliases", {"alias_id": stable_id(channel["canonical_channel_id"], channel["canonical_url"], None), "canonical_channel_id": channel["canonical_channel_id"], "alias_url": channel["canonical_url"], "alias_kind": "CANONICAL_URL", "submission_global_row": None}, ("alias_id",))
            for subject in model["subjects"]:
                _upsert(connection, "non_channel_subjects", {key: subject[key] for key in ("subject_id", "subject_name", "canonical_channel_id", "identity_status", "evidence_source", "limitation")}, ("subject_id",))
                _upsert(connection, "subject_datasets", {"subject_id": subject["subject_id"], "dataset_id": subject["dataset_id"]}, ("subject_id", "dataset_id"))
            for video in videos:
                _upsert(connection, "videos", video, ("youtube_video_id",))
                if video["description"] is None:
                    _upsert(connection, "availability_gaps", {"canonical_channel_id": video["canonical_channel_id"], "field_name": f"video:{video['youtube_video_id']}:description", "unavailable_reason": video["description_unavailable_reason"], "evidence_source": video["canonical_url"]}, ("canonical_channel_id", "field_name", "unavailable_reason"))
                for field in ("duration_seconds", "video_type", "views", "likes", "comments"):
                    if video[field] is None:
                        _upsert(connection, "availability_gaps", {"canonical_channel_id": video["canonical_channel_id"], "field_name": f"video:{video['youtube_video_id']}:{field}", "unavailable_reason": "Value unavailable in stored source evidence.", "evidence_source": video["canonical_url"]}, ("canonical_channel_id", "field_name", "unavailable_reason"))
            for membership in memberships:
                _upsert(connection, "dataset_videos", membership, ("dataset_id", "youtube_video_id"))
            for transcript in transcripts:
                _upsert(connection, "transcripts", transcript, ("youtube_video_id", "dataset_id"))
                if transcript["language"] or transcript["caption_type"]:
                    _upsert(connection, "subtitle_tracks", {"subtitle_track_id": stable_id(transcript["youtube_video_id"], transcript["dataset_id"], transcript["language"], transcript["caption_type"]), "youtube_video_id": transcript["youtube_video_id"], "dataset_id": transcript["dataset_id"], "language": transcript["language"], "track_type": transcript["caption_type"], "raw_json": None}, ("subtitle_track_id",))
            for run in actor_runs:
                _upsert(connection, "actor_runs", run, ("actor_run_id",))
            for artifact in artifacts:
                artifact = {"artifact_id": stable_id(artifact["dataset_id"], artifact["canonical_channel_id"], artifact["artifact_type"], artifact["repository_path"]), **artifact}
                _upsert(connection, "artifacts", artifact, ("artifact_id",))
            for capability in capabilities:
                _upsert(connection, "intelligence_capabilities", capability, ("capability_id",))
            for item in intelligence:
                _upsert(connection, "intelligence_coverage", item, ("canonical_channel_id", "capability_id"))
            metadata = {
                "generated_at": VERIFIED_AT,
                "source_payload_sha256": json.loads((root / RAW_AUTHORITY).read_text())["controls"]["ordered_payload_sha256"],
                "historical_catalog_sha256": sha256_file(root / "data/catalog/youtube_inventory.db"),
                "fts5_enabled": "0",
            }
            try:
                connection.execute("CREATE VIRTUAL TABLE IF NOT EXISTS transcript_fts USING fts5(transcript_text)")
                connection.execute("DELETE FROM transcript_fts")
                connection.execute("INSERT INTO transcript_fts(rowid,transcript_text) SELECT transcript_id,transcript_text FROM transcripts WHERE transcript_text IS NOT NULL AND is_placeholder=0")
                metadata["fts5_enabled"] = "1"
            except sqlite3.OperationalError:
                pass
            for key, value in metadata.items():
                _upsert(connection, "registry_metadata", {"key": key, "value": value}, ("key",))
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        if integrity != "ok" or foreign_keys:
            raise ValueError(f"Registry validation failed: integrity={integrity}, foreign_keys={foreign_keys[:5]}")
        counts = table_counts(connection)
    finally:
        connection.close()
        if counts is None:
            temporary_path.unlink(missing_ok=True)
    os.replace(temporary_path, database_path)
    return counts


def write_normalized_outputs(root: Path, model: dict) -> None:
    normalized = root / "data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json"
    csv_path = root / "data/manifests/YOUTUBE_CHANNEL_TARGETS.csv"
    md_path = root / "data/manifests/YOUTUBE_CHANNEL_TARGETS.md"
    normalized.parent.mkdir(parents=True, exist_ok=True)
    normalized.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = [
        "canonical_channel_id", "channel_name", "current_handle", "canonical_url", "source_group", "target_group", "status", "completed_tick",
        "identity_status", "extraction_status", "package_status", "video_metadata_status", "description_status", "transcript_status",
        "thumbnail_metadata_status", "visual_asset_status", "forensic_video_status", "intelligence_status", "first_party_analytics_status",
        "dataset_ids", "video_count", "regular_videos", "shorts", "livestreams", "descriptions", "real_transcripts", "placeholders",
        "missing_transcripts", "thumbnail_url_count", "downloaded_thumbnail_count", "screenshot_count", "keyframe_count",
        "registered_source_video_count", "timestamped_visual_observation_count", "visual_evidence_path",
        "workbook_path", "transcript_zip_path", "identity_evidence_source", "verified_at", "limitations", "submission_rows",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for channel in model["channels"]:
            row = {key: channel.get(key) for key in fields}
            visual = channel["visual_coverage"]
            for key in (
                "thumbnail_url_count", "downloaded_thumbnail_count", "screenshot_count", "keyframe_count",
                "registered_source_video_count", "timestamped_visual_observation_count",
            ):
                row[key] = visual[key]
            row["visual_evidence_path"] = visual["evidence_path"]
            for key in ("dataset_ids", "limitations", "submission_rows"):
                row[key] = " | ".join(map(str, row[key]))
            writer.writerow(row)
    status_counts = defaultdict(int)
    for channel in model["channels"]:
        if channel["target_group"] != "OUTSIDE_TARGET":
            status_counts[channel["status"]] += 1
    lines = [
        "# YouTube Channel Targets", "", f"Verified: {VERIFIED_AT}", "",
        f"- Submitted rows: {model['controls']['submitted_rows']}",
        f"- Normalized URL identities: {model['controls']['normalized_url_identities']}",
        f"- Canonical target channels: {model['controls']['canonical_target_channels']}",
        f"- Complete: {status_counts['COMPLETE']}",
        f"- Complete with limitations: {status_counts['COMPLETE_WITH_LIMITATIONS']}",
        f"- Identity verified, data not extracted: {status_counts['IDENTITY_VERIFIED_DATA_NOT_EXTRACTED']}",
        "", "Status is target-registry progress only. Independent extraction, package, transcript, visual, intelligence, and first-party fields remain separate in CSV, JSON, SQLite, and workbook.",
        "", "| Target group | Source group | Extraction | Package | Transcript | Visual evidence | Intelligence | First-party Analytics | Channel | Videos | Datasets |",
        "|---|---|---|---|---|---|---|---|---|---:|---|",
    ]
    for channel in model["channels"]:
        lines.append(f"| {channel['target_group']} | {channel['source_group']} | {channel['extraction_status']} | {channel['package_status']} | {channel['transcript_status']} | {channel['visual_asset_status']} | {channel['intelligence_status']} | {channel['first_party_analytics_status']} | [{channel['channel_name']}]({channel['canonical_url']}) | {channel['video_count']} | {', '.join(channel['dataset_ids']) or 'None'} |")
    lines.extend(["", "## Screenshot-only subjects", ""])
    lines.extend(f"- {subject['subject_name']} ({subject['dataset_id']}): {subject['limitation']}" for subject in model["subjects"])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--database", type=Path)
    parser.add_argument("--write-ledgers", action="store_true")
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
    model = build_model(root)
    if args.write_ledgers:
        write_normalized_outputs(root, model)
    database = args.database or root / "data/catalog/youtube_channel_registry.db"
    counts = build_database(root, database, model)
    print(json.dumps({"database": str(database), "controls": model["controls"], "table_counts": counts}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
