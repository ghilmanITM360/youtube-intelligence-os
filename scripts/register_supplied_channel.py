#!/usr/bin/env python3
"""Register a supplied channel workbook plus loose transcript files."""

import argparse
import re
import shutil
import sqlite3
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

import inventory_catalog as ic
from inventory_catalog import CatalogError
from source_adapters import youtube_master_data as ymd

TOOL_VERSION = "register_supplied_channel.py/1"
TRANSCRIPT_RE = re.compile(r"\n=+\nTRANSCRIPT\n=+\n")


def next_id(conn, table, column, prefix, width=6):
    values = (row[0] for row in conn.execute("SELECT {} FROM {}".format(column, table)))
    numbers = [int(match.group(1)) for value in values if (match := re.fullmatch(re.escape(prefix) + r"-(\d+)", value or ""))]
    return "{}-{:0{}d}".format(prefix, max(numbers, default=0) + 1, width)


def as_int(value, field):
    if value in (None, ""):
        return None
    try:
        parsed = int(float(value))
    except (TypeError, ValueError) as exc:
        raise CatalogError("MalformedData", "{} is not an integer: {!r}".format(field, value)) from exc
    if parsed < 0:
        raise CatalogError("MalformedData", "{} cannot be negative".format(field))
    return parsed


def as_float(value, field):
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise CatalogError("MalformedData", "{} is not numeric: {!r}".format(field, value)) from exc


def published_at(video):
    value = video["Published (UTC)"][0]
    if value and value != "(date only)":
        return value.replace(" ", "T") + ("" if value.endswith("Z") else "Z")
    serial = as_float(video.get("Date", (None,))[0], "Date")
    return (datetime(1899, 12, 30) + timedelta(days=serial)).date().isoformat() if serial is not None else None


def parse_transcript(path):
    data = path.read_bytes()
    text = data.decode("utf-8")
    fields = ymd._parse_transcript_member_text(text)
    parts = TRANSCRIPT_RE.split(text, maxsplit=1)
    body = parts[1].strip() if len(parts) == 2 else ""
    if not body:
        raise CatalogError("MalformedData", "Transcript body is empty: {}".format(path.name))
    fields.update(path=path, size_bytes=len(data), sha256=ic.sha256_bytes(data), timing_quality="POSITIONAL_ONLY")
    return fields


def load_source(workbook_path, transcript_dir):
    workbook = ymd.read_workbook(workbook_path)
    if len(workbook["channels"]) != 1:
        raise CatalogError("AmbiguousIdentity", "Supplied channel workbook must establish exactly one channel")
    channel_name, channel = next(iter(workbook["channels"].items()))
    required_identity = {key: channel.get(key, (None,))[0] for key in ("Channel Name", "Handle", "Channel ID", "Channel URL")}
    if any(not value for value in required_identity.values()):
        raise CatalogError("AmbiguousIdentity", "Channel name, handle, YouTube channel ID, and URL are required")
    transcript_paths = sorted(path for path in transcript_dir.iterdir() if path.is_file() and path.name != "INDEX.txt")
    transcripts = [parse_transcript(path) for path in transcript_paths]
    workbook_ids = [row["Video ID"][0] for row in workbook["videos"]]
    transcript_ids = [row["video_id"] for row in transcripts]
    if any(count > 1 for count in Counter(workbook_ids).values()) or any(count > 1 for count in Counter(transcript_ids).values()):
        raise CatalogError("EvidenceConflict", "Duplicate video or transcript identity in supplied source")
    if set(workbook_ids) != set(transcript_ids):
        raise CatalogError("EvidenceConflict", "Workbook and transcript video IDs do not reconcile exactly")
    by_id = {row["video_id"]: row for row in transcripts}
    for video in workbook["videos"]:
        youtube_id = video["Video ID"][0]
        transcript = by_id[youtube_id]
        declared_file = video.get("Transcript File", (None,))[0]
        if declared_file != transcript["path"].name or transcript["channel"] != channel_name or transcript["title"] != video["Title"][0]:
            raise CatalogError("EvidenceConflict", "Transcript mapping mismatch for {}".format(youtube_id))
    return workbook, channel_name, channel, by_id


def resolve_channel(conn, channel):
    youtube_id = channel["Channel ID"][0]
    handle = channel["Handle"][0]
    url = channel["Channel URL"][0]
    matches = conn.execute(
        "SELECT channel_id,youtube_channel_id,handle,channel_url FROM channels "
        "WHERE youtube_channel_id=? OR lower(handle)=lower(?) OR lower(channel_url)=lower(?)",
        (youtube_id, handle, url),
    ).fetchall()
    ids = {row["channel_id"] for row in matches}
    if len(ids) > 1:
        raise CatalogError("AmbiguousIdentity", "Channel identity fields resolve to different canonical channels")
    if not matches:
        return None
    row = matches[0]
    if row["youtube_channel_id"] not in (None, youtube_id):
        raise CatalogError("EvidenceConflict", "Existing channel has conflicting YouTube channel ID")
    return row["channel_id"]


def write_manifest(conn, dataset_id, path):
    dataset = conn.execute("SELECT * FROM datasets WHERE dataset_id=?", (dataset_id,)).fetchone()
    channel = conn.execute("SELECT * FROM channels WHERE created_from_dataset_id=?", (dataset_id,)).fetchone()
    files = conn.execute("SELECT original_path,canonical_path,size_bytes,sha256,file_role FROM source_files WHERE dataset_id=? ORDER BY relative_path", (dataset_id,)).fetchall()
    run = conn.execute("SELECT run_id,started_at,completed_at FROM ingestion_runs WHERE dataset_id=? AND run_type='STRUCTURED_REGISTRATION' ORDER BY started_at DESC LIMIT 1", (dataset_id,)).fetchone()
    counts = dict(conn.execute(
        "SELECT 'videos',COUNT(*) FROM video_snapshots WHERE dataset_id=? UNION ALL SELECT 'transcripts',COUNT(*) FROM transcripts WHERE dataset_id=? UNION ALL SELECT 'thumbnails',COUNT(thumbnail_url) FROM video_snapshots WHERE dataset_id=?",
        (dataset_id, dataset_id, dataset_id),
    ).fetchall())
    lines = [
        "# {} — {}".format(dataset_id, dataset["dataset_name"]), "",
        "Generated from live catalog by `scripts/register_supplied_channel.py`.", "",
        "- Semantic class: `{}` — Competitor Evidence / Channel-Specific Intelligence".format(dataset["semantic_class"]),
        "- Status: `{}`".format(dataset["status"]),
        "- Ingestion run: `{}`".format(run["run_id"]),
        "- Registered channel: {} (`{}`, `{}`)".format(channel["display_name"], channel["handle"], channel["youtube_channel_id"]),
        "- Canonical videos: {}".format(counts["videos"]),
        "- Available transcripts: {} (`POSITIONAL_ONLY`)".format(counts["transcripts"]),
        "- Registered thumbnail references: {}".format(counts["thumbnails"]),
        "- Editing intelligence: `EDITING_INTELLIGENCE_NOT_AVAILABLE`", "",
        "## Source files", "",
        "| Role | Bytes | SHA-256 | Original path | Canonical path |", "|---|---:|---|---|---|",
    ]
    lines.extend("| {} | {} | `{}` | `{}` | `{}` |".format(row["file_role"], row["size_bytes"], row["sha256"], row["original_path"], row["canonical_path"]) for row in files)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def register(workbook_path, transcript_dir, db_path=ic.DEFAULT_DB_PATH, raw_root=None, manifest_dir=None, dataset_name=None):
    workbook_path, transcript_dir, db_path = Path(workbook_path).resolve(), Path(transcript_dir).resolve(), Path(db_path).resolve()
    if not workbook_path.is_file() or not transcript_dir.is_dir():
        raise CatalogError("SourceNotFound", "Workbook or transcript source path does not exist")
    workbook, channel_name, channel, transcripts = load_source(workbook_path, transcript_dir)
    source_paths = [workbook_path] + sorted(path for path in transcript_dir.iterdir() if path.is_file())
    source_hashes = {str(path): ic.sha256_file(path) for path in source_paths}
    raw_root = Path(raw_root or (ic.REPO_ROOT / "data/raw/competitors"))
    manifest_dir = Path(manifest_dir or (ic.REPO_ROOT / "data/manifests"))
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    canonical_dir = None
    try:
        if conn.execute("SELECT MAX(schema_version) FROM schema_meta").fetchone()[0] < 10:
            raise CatalogError("SourceNotFound", "Schema v10 required; run inventory_catalog.py init")
        source_set = set(source_hashes.values())
        overlap = {row[0] for row in conn.execute("SELECT sha256 FROM source_files WHERE sha256 IS NOT NULL") if row[0] in source_set}
        if overlap:
            raise CatalogError("EvidenceConflict", "Source hashes overlap existing catalog; review duplicate status before registration")
        dataset_id = next_id(conn, "datasets", "dataset_id", "DS")
        canonical_dir = raw_root / dataset_id
        if canonical_dir.exists():
            raise CatalogError("EvidenceConflict", "Canonical raw target already exists: {}".format(canonical_dir))
        existing_channel_id = resolve_channel(conn, channel)
        channel_id = existing_channel_id or next_id(conn, "channels", "channel_id", "CH")
        youtube_ids = [video["Video ID"][0] for video in workbook["videos"]]
        existing_videos = conn.execute("SELECT youtube_video_id,channel_id FROM videos WHERE youtube_video_id IN ({})".format(",".join("?" for _ in youtube_ids)), youtube_ids).fetchall()
        if existing_videos:
            raise CatalogError("EvidenceConflict", "One or more supplied videos already exist; no duplicate rows created")

        canonical_dir.mkdir(parents=True)
        canonical_workbook = canonical_dir / workbook_path.name
        canonical_transcripts = canonical_dir / "transcripts"
        canonical_transcripts.mkdir()
        shutil.copy2(workbook_path, canonical_workbook)
        for path in source_paths[1:]:
            shutil.copy2(path, canonical_transcripts / path.name)
        for source, digest in source_hashes.items():
            destination = canonical_workbook if source == str(workbook_path) else canonical_transcripts / Path(source).name
            if ic.sha256_file(destination) != digest:
                raise CatalogError("HashFailure", "Canonical copy differs from source: {}".format(source))

        ts = ic.now_iso()
        observed_at = ymd.find_scraped_date(workbook["banner_lines"])
        if not observed_at:
            raise CatalogError("MalformedData", "Workbook does not declare scrape date")
        file_run_id = next_id(conn, "ingestion_runs", "run_id", "RUN")
        structured_run_number = int(file_run_id.rsplit("-", 1)[1]) + 1
        structured_run_id = "RUN-{:06d}".format(structured_run_number)
        with conn:
            conn.execute(
                "INSERT INTO datasets VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (dataset_id, dataset_name or "{} — Supplied Canonical Channel Export".format(channel_name), "B", "Supplied workbook and complete loose transcript pack.", "EXTERNAL_FILES", "CONTROLLED_COPY", "STRUCTURED_REGISTERED", "User-supplied canonical channel evidence", ts, ts, ts, "All source bytes copied unchanged; no live crawl performed."),
            )
            conn.execute(
                "INSERT INTO ingestion_runs (run_id,dataset_id,started_at,completed_at,status,source_file_count,archive_member_count,total_size_bytes,errors_count,verification_status,tool_version,notes,run_type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (file_run_id, dataset_id, ts, ts, "COMPLETED", len(source_paths), 0, sum(path.stat().st_size for path in source_paths), 0, "VERIFIED", TOOL_VERSION, "Two supplied roots; every discovered file copied and hashed.", "FILE_INGESTION"),
            )
            conn.execute(
                "INSERT INTO ingestion_runs (run_id,dataset_id,started_at,completed_at,status,source_file_count,archive_member_count,total_size_bytes,errors_count,verification_status,tool_version,notes,run_type) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (structured_run_id, dataset_id, ts, ts, "COMPLETED", len(source_paths), 0, sum(path.stat().st_size for path in source_paths), 0, "VERIFIED", TOOL_VERSION, "29 workbook rows reconciled exactly to 29 transcript files.", "STRUCTURED_REGISTRATION"),
            )
            for original, kind in ((workbook_path, "LOCAL_FILE"), (transcript_dir, "LOCAL_FOLDER")):
                conn.execute("INSERT INTO source_locations VALUES (?,?,?,?,?,?,?)", (next_id(conn, "source_locations", "source_location_id", "LOC"), dataset_id, str(original), kind, 1, ts, None))

            file_ids = {}
            for source in source_paths:
                relative = workbook_path.name if source == workbook_path else "transcripts/{}".format(source.name)
                role = "STRUCTURED_METADATA" if source == workbook_path else "TRANSCRIPT_INDEX" if source.name == "INDEX.txt" else "TRANSCRIPT"
                file_id = next_id(conn, "source_files", "file_id", "FILE")
                destination = canonical_dir / relative
                file_ids[source.name] = file_id
                conn.execute(
                    "INSERT INTO source_files (file_id,dataset_id,ingestion_run_id,parent_file_id,storage_kind,file_role,original_filename,original_path,relative_path,canonical_path,archive_member_path,extension,mime_type,size_bytes,sha256,semantic_class,evidence_layer,is_copied,is_archive_member,processing_status,verification_status,created_at,notes) VALUES (?,?,?,NULL,'PHYSICAL_FILE',?,?,?,?,?,NULL,?,?,?,?,?,'RAW_SOURCE',1,0,'CATALOGED','VERIFIED',?,?)",
                    (file_id, dataset_id, file_run_id, role, source.name, str(source), relative, str(destination), source.suffix.lower(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" if source == workbook_path else "text/plain", source.stat().st_size, source_hashes[str(source)], "B", ts, "INGEST"),
                )

            def provenance(target_column, target_id, field, locator, source_file_id, origin="SOURCE_EXTRACTED", evidence="EXTRACTED_FACT", method="xlsx_cell_read"):
                targets = {name: None for name in ("channel_id", "channel_snapshot_id", "video_id", "video_snapshot_id", "transcript_id")}
                targets[target_column] = target_id
                conn.execute(
                    "INSERT INTO field_provenance VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (next_id(conn, "field_provenance", "provenance_id", "PR"), dataset_id, structured_run_id, source_file_id, targets["channel_id"], targets["channel_snapshot_id"], targets["video_id"], targets["video_snapshot_id"], targets["transcript_id"], field, locator, origin, evidence, method, observed_at, ts, None),
                )

            if not existing_channel_id:
                conn.execute("INSERT INTO channels VALUES (?,?,?,?,?,?,?,?,?)", (channel_id, channel["Channel ID"][0], channel["Handle"][0], channel_name, channel["Channel URL"][0], dataset_id, ts, ts, "Tier A supplied identity: exact name, handle, channel ID, and canonical URL."))
            workbook_file_id = file_ids[workbook_path.name]
            for label, field in (("Channel ID", "youtube_channel_id"), ("Handle", "handle"), ("Channel Name", "display_name"), ("Channel URL", "channel_url")):
                value, row, col = channel[label]
                provenance("channel_id", channel_id, field, "{}#Channel Overview!{}{}".format(workbook_path.name, col, row), workbook_file_id)
            conn.execute("INSERT OR IGNORE INTO channel_dataset_links VALUES (?,?,?,?,?,?,?)", (channel_id, dataset_id, "CREATED_FROM" if not existing_channel_id else "IDENTITY_EVIDENCE", "{}#Channel Overview!B5:B8".format(workbook_path.name), "EXTRACTED_FACT", ts, "Exact supplied channel identity."))
            conn.execute("INSERT OR IGNORE INTO channel_dataset_links VALUES (?,?,?,?,?,?,?)", (channel_id, dataset_id, "STRUCTURED_OBSERVATION", "{}#All Videos".format(workbook_path.name), "EXTRACTED_FACT", ts, None))
            snapshot_id = next_id(conn, "channel_snapshots", "channel_snapshot_id", "CS")
            conn.execute("INSERT INTO channel_snapshots VALUES (?,?,?,?,?,?,?,?,?)", (snapshot_id, channel_id, dataset_id, structured_run_id, observed_at, as_int(channel.get("Subscribers", (None,))[0], "Subscribers"), as_int(channel.get("Total Videos (YouTube)", (None,))[0], "Total Videos"), ts, "Supplied public channel observation."))
            for label, field in (("Subscribers", "subscriber_count"), ("Total Videos (YouTube)", "video_count")):
                value, row, col = channel[label]
                provenance("channel_snapshot_id", snapshot_id, field, "{}#Channel Overview!{}{}".format(workbook_path.name, col, row), workbook_file_id)

            for video in workbook["videos"]:
                youtube_id = video["Video ID"][0]
                transcript = transcripts[youtube_id]
                video_id = next_id(conn, "videos", "video_id", "VID")
                conn.execute("INSERT INTO videos VALUES (?,?,?,?,?,?,?,?)", (video_id, youtube_id, channel_id, video["Video URL"][0], dataset_id, ts, ts, "Created from supplied canonical workbook."))
                for label, field in (("Video ID", "youtube_video_id"), ("Video URL", "canonical_url")):
                    value, row, col = video[label]
                    provenance("video_id", video_id, field, "{}#All Videos!{}{}".format(workbook_path.name, col, row), workbook_file_id)
                values = {
                    "published_at": published_at(video), "title": video["Title"][0], "duration_seconds": as_int(video["Sec"][0], "Sec"),
                    "views": as_int(video["Views"][0], "Views"), "likes": as_int(video["Likes"][0], "Likes"), "comments": as_int(video["Comments"][0], "Comments"),
                    "views_per_day": as_float(video["Views/Day"][0], "Views/Day"), "engagement_rate": as_float(video["Engagement"][0], "Engagement"),
                    "description_char_count": as_int(video["Desc Chars"][0], "Desc Chars"), "transcript_word_count": as_int(video["Transcript Words"][0], "Transcript Words"),
                    "description": video.get("Full Description", (None,))[0], "video_type": "video", "thumbnail_url": video.get("Thumbnail URL", (None,))[0],
                }
                video_snapshot_id = next_id(conn, "video_snapshots", "video_snapshot_id", "VS")
                conn.execute(
                    "INSERT INTO video_snapshots (video_snapshot_id,video_id,dataset_id,registration_run_id,observed_at,published_at,title,duration_seconds,views,likes,comments,views_per_day,engagement_rate,description_char_count,transcript_word_count,created_at,notes,description,video_type,thumbnail_url) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (video_snapshot_id, video_id, dataset_id, structured_run_id, observed_at, values["published_at"], values["title"], values["duration_seconds"], values["views"], values["likes"], values["comments"], values["views_per_day"], values["engagement_rate"], values["description_char_count"], values["transcript_word_count"], ts, "Supplied public observation; rounded public likes remain source values.", values["description"], values["video_type"], values["thumbnail_url"]),
                )
                source_labels = {"published_at": "Published (UTC)", "title": "Title", "duration_seconds": "Sec", "views": "Views", "likes": "Likes", "comments": "Comments", "views_per_day": "Views/Day", "engagement_rate": "Engagement", "description_char_count": "Desc Chars", "transcript_word_count": "Transcript Words", "description": "Full Description", "thumbnail_url": "Thumbnail URL"}
                for field, label in source_labels.items():
                    if values[field] is None:
                        continue
                    _, row, col = video[label]
                    origin = "SOURCE_COMPUTED" if field in {"views_per_day", "engagement_rate"} else "SOURCE_EXTRACTED"
                    evidence = "MEASURED_FACT" if origin == "SOURCE_COMPUTED" else "EXTRACTED_FACT"
                    sheet = "Descriptions" if label == "Full Description" else "All Videos"
                    provenance("video_snapshot_id", video_snapshot_id, field, "{}#{}!{}{}".format(workbook_path.name, sheet, col, row), workbook_file_id, origin, evidence)
                provenance("video_snapshot_id", video_snapshot_id, "video_type", "{}#Channel Overview!B16:B17".format(workbook_path.name), workbook_file_id, "SOURCE_DECLARED")

                transcript_id = next_id(conn, "transcripts", "transcript_id", "TR")
                transcript_file_id = file_ids[transcript["path"].name]
                canonical_reference = str(canonical_transcripts / transcript["path"].name)
                conn.execute(
                    "INSERT INTO transcripts (transcript_id,video_id,dataset_id,registration_run_id,archive_member_file_id,availability_status,caption_type,language,word_count,transcript_sha256,description_present,created_at,notes,transcript_format,transcript_source,canonical_reference,timing_quality) VALUES (?,?,?,?,?,'AVAILABLE',?,?,?,?,?, ?,?,'plaintext','SUPPLIED_APIFY_EXPORT',?,'POSITIONAL_ONLY')",
                    (transcript_id, video_id, dataset_id, structured_run_id, transcript_file_id, transcript["caption_type"], transcript["language"], as_int(transcript["word_count"], "Word count"), transcript["sha256"], int(transcript["description_present"]), ts, "No transcript timestamps; description chapter markers are not transcript timing.", canonical_reference),
                )
                for field in ("availability_status", "caption_type", "language", "word_count", "canonical_reference", "timing_quality"):
                    provenance("transcript_id", transcript_id, field, "{}#header_or_body".format(transcript["path"].name), transcript_file_id, "TRANSCRIPT_METADATA", "EXTRACTED_FACT", "utf8_text_parse")

        manifest_path = manifest_dir / "{}.md".format(dataset_id)
        write_manifest(conn, dataset_id, manifest_path)
        return {"dataset_id": dataset_id, "channel_id": channel_id, "channel_name": channel_name, "run_id": structured_run_id, "video_count": len(workbook["videos"]), "transcript_count": len(transcripts), "file_count": len(source_paths), "total_bytes": sum(path.stat().st_size for path in source_paths), "manifest": str(manifest_path), "dedup_status": "EXISTING_CHANNEL_NEW_DATA" if existing_channel_id else "NEW_SOURCE"}
    except Exception:
        if canonical_dir and canonical_dir.exists() and not conn.execute("SELECT 1 FROM datasets WHERE dataset_id=?", (canonical_dir.name,)).fetchone():
            shutil.rmtree(canonical_dir)
        raise
    finally:
        conn.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", required=True)
    parser.add_argument("--transcripts", required=True)
    parser.add_argument("--db", default=str(ic.DEFAULT_DB_PATH))
    parser.add_argument("--raw-root")
    parser.add_argument("--manifest-dir")
    parser.add_argument("--dataset-name")
    args = parser.parse_args(argv)
    result = register(args.workbook, args.transcripts, args.db, args.raw_root, args.manifest_dir, args.dataset_name)
    print("COMPLETED — {dataset_id}, {channel_id}, {video_count} videos, {transcript_count} transcripts, run {run_id}".format(**result))


if __name__ == "__main__":
    main()
