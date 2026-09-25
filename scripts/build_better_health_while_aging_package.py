#!/usr/bin/env python3
"""Build the Better Health While Aging (DS-000033) standard channel package.

Reproduces the same five-sheet workbook + transcript ZIP contract used by
existing standard packages (DS-000028 / Dr. Okoro, DS-000029 / Doctor
Thomas, DS-000032 / Dr. Rehan). Combines two Apify runs: the original
94-video catalog acquisition (2026-09-25) and a 4-video targeted Shorts
backfill (2026-09-26, Priority A missing historical Shorts). Every one of
the 98 captured videos has a real YouTube caption track; no explicit
no-subtitle placeholder is needed here because none exists in the evidence.

This is a Senior Health competitor acquisition (Group C, P1 tier) — see
docs/research/senior-health-2026-09-25/forensic-v3/ACQUISITION-BACKLOG.md.
"""

from __future__ import annotations

import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parents[1]
RUNS = [
    {
        "raw_json": ROOT / "data/raw/competitors/DS-000033/apify/AuZ65QkXBmVIXcOn9/raw/dataset.json",
        "transcripts_dir": ROOT / "data/raw/competitors/DS-000033/apify/AuZ65QkXBmVIXcOn9/transcripts",
        "run_id": "AuZ65QkXBmVIXcOn9",
        "dataset_id": "ijadodx1EUhkjOrcp",
        "collection_date": "2026-09-25",
        "video_count": 94,
        "cost_usd": "$0.376",
        "cost_cap": "$0.45",
    },
    {
        "raw_json": ROOT / "data/raw/competitors/DS-000033/apify/Ll3gKxE3dXEeG4SDd/dataset.json",
        "transcripts_dir": ROOT / "data/raw/competitors/DS-000033/apify/Ll3gKxE3dXEeG4SDd/transcripts",
        "run_id": "Ll3gKxE3dXEeG4SDd",
        "dataset_id": "xCOQ0gj6iLVqCI9B5",
        "collection_date": "2026-09-26",
        "video_count": 4,
        "cost_usd": "$0.016",
        "cost_cap": "$0.02",
    },
]
PACKAGE_DIR = ROOT / "data/extracted/channel-data/DS-000033/packages/better-health-while-aging"
WORKBOOK_PATH = PACKAGE_DIR / "BetterHealthWhileAging_Master_Data.xlsx"
ZIP_PATH = PACKAGE_DIR / "BetterHealthWhileAging_Transcripts_98_Videos.zip"
CHANNEL_NAME = "Better Health While Aging"
CHANNEL_HANDLE = "@BetterHealthWhileAging"
CHANNEL_ID = "UCFpxvukIqCAUA7YizI-q9Dw"
COLLECTION_DATE = "2026-09-26"
PUBLIC_VIDEO_COUNT = sum(run["video_count"] for run in RUNS)

ALL_VIDEO_HEADERS = [
    "#", "Video ID", "Title", "Video URL", "Published (UTC)", "Date", "Day", "Duration", "Sec", "Views",
    "Likes", "Comments", "Like Rate", "Comment Rate", "Engagement", "Views/Day", "Transcript Words", "Words/Min",
    "Desc Chars", "Desc Links", "Hashtags", "Caption Type", "Transcript File", "Thumbnail URL", "Members Only", "Paid",
    "Comments Off", "Age Restr.",
]
DESCRIPTION_HEADERS = ["#", "Video ID", "Title", "Hashtags", "Link Count", "Description Links (URLs)", "Full Description"]
REQUIRED_SHEETS = ["Channel Overview", "All Videos", "Descriptions", "Verification", "Analysis"]

WORD_RE = re.compile(r"[^\W_]+(?:['’_-][^\W_]+)*", re.UNICODE)


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text or ""))


def content_type(record: dict) -> str:
    type_value = str(record.get("type") or "").lower()
    list_page = str(record.get("fromChannelListPage") or "").lower()
    url = str(record.get("url") or "").lower()
    if type_value in {"short", "shorts"} or list_page == "shorts" or "/shorts/" in url:
        return "Short"
    if type_value in {"streams", "stream", "live", "livestream"} or list_page in {"streams", "live"}:
        return "livestream"
    return "regular video"


def hashtags_for(record: dict) -> list[str]:
    actor_tags = [tag for tag in (record.get("hashtags") or []) if tag]
    text_tags = re.findall(r"#[^\W_]+", record.get("text") or "", re.UNICODE)
    seen, out = set(), []
    for tag in [*actor_tags, *text_tags]:
        tag = tag if str(tag).startswith("#") else f"#{tag}"
        if tag not in seen:
            seen.add(tag)
            out.append(tag)
    return out


def description_links_for(record: dict) -> list[str]:
    actor_links = [item for item in (record.get("descriptionLinks") or []) if item]
    text_links = re.findall(r"https?://[^\s<>\"']+", record.get("text") or "")
    seen, out = set(), []
    for link in [*actor_links, *text_links]:
        link = re.sub(r"[),.;]+$", "", str(link))
        if link not in seen:
            seen.add(link)
            out.append(link)
    return out


def clean_title_for_filename(title: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_") or "Untitled"
    return cleaned[:100].rstrip("_") or "Untitled"


def parse_duration(value: str) -> int:
    parts = [int(part) for part in value.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    hours, minutes, seconds = parts
    return hours * 3600 + minutes * 60 + seconds


def load_videos() -> list[dict]:
    records = []
    transcripts_by_id: dict[str, Path] = {}
    for run in RUNS:
        run_records = json.loads(run["raw_json"].read_text(encoding="utf-8"))
        records.extend(run_records)
        for record in run_records:
            transcripts_by_id[record["id"]] = run["transcripts_dir"] / f"{record['id']}.txt"
    seen_ids = [record["id"] for record in records]
    assert len(seen_ids) == len(set(seen_ids)), "duplicate video IDs across BHWA Apify runs"
    records.sort(key=lambda item: item["date"], reverse=True)
    videos = []
    for index, record in enumerate(records, start=1):
        video_id = record["id"]
        published = datetime.fromisoformat(record["date"].replace("Z", "+00:00"))
        duration_seconds = parse_duration(record["duration"])
        description = record.get("text") or ""
        transcript_path = transcripts_by_id[video_id]
        has_transcript = transcript_path.is_file()
        transcript_body = transcript_path.read_text(encoding="utf-8").strip() if has_transcript else ""
        subtitles = record.get("subtitles") or []
        choices = subtitles if isinstance(subtitles, list) else [subtitles]
        selected = next((x for x in choices if str(x.get("language", "")).lower().startswith("en")), (choices[0] if choices else {}))
        videos.append({
            "index": index,
            "id": video_id,
            "title": record["title"],
            "url": record["url"],
            "published": published,
            "duration": record["duration"],
            "seconds": duration_seconds,
            "views": int(record.get("viewCount") or 0),
            "likes": int(record.get("likes") or 0),
            "comments": int(record.get("commentsCount") or 0),
            "description": description,
            "links": description_links_for(record),
            "tags": hashtags_for(record),
            "content_type": content_type(record),
            "caption_type": selected.get("type") or ("NONE" if not has_transcript else "unspecified"),
            "language": selected.get("language") or ("NOT_AVAILABLE" if not has_transcript else "en"),
            "transcript": transcript_body,
            "words": word_count(transcript_body),
            "filename": f"{index:03d}_{video_id}_{clean_title_for_filename(record['title'])}.txt",
            "thumbnail": record.get("thumbnailUrl") or "",
            "members_only": bool(record.get("isMembersOnly")),
            "paid": bool(record.get("isPaidContent")),
            "comments_off": bool(record.get("commentsTurnedOff")),
            "age_restricted": bool(record.get("isAgeRestricted")),
            "has_transcript": has_transcript,
        })
    return videos


def add_table(sheet, ref: str, name: str) -> None:
    table = Table(displayName=name, ref=ref)
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    sheet.add_table(table)


def build_workbook(videos: list[dict]) -> Workbook:
    workbook = Workbook()
    workbook.remove(workbook.active)
    for name in REQUIRED_SHEETS:
        workbook.create_sheet(name)

    overview = workbook["Channel Overview"]
    no_descriptions = sum(1 for video in videos if not video["description"])
    real_transcripts = sum(1 for v in videos if v["has_transcript"])
    regular_count = sum(1 for v in videos if v["content_type"] == "regular video")
    shorts_count = sum(1 for v in videos if v["content_type"] == "Short")
    user_generated = sum(1 for v in videos if v["caption_type"] == "user_generated")
    auto_generated = sum(1 for v in videos if v["caption_type"] == "auto_generated")
    run_ids = ", ".join(run["run_id"] for run in RUNS)
    dataset_ids = ", ".join(run["dataset_id"] for run in RUNS)
    overview.append([f"{CHANNEL_NAME} — Full Channel Data Export"])
    overview.append([f"Source: Apify streamers/youtube-scraper | Packaged {COLLECTION_DATE} | "
                      f"{len(videos)} videos, {len(videos) - no_descriptions} public descriptions, "
                      f"{real_transcripts} transcripts"])
    overview.append([])
    overview.append(["Field", "Value"])
    for field, value in [
        ("Channel Name", CHANNEL_NAME),
        ("Handle", CHANNEL_HANDLE),
        ("Channel ID", CHANNEL_ID),
        ("Canonical Channel URL", f"https://www.youtube.com/channel/{CHANNEL_ID}"),
        ("Channel Category", "SENIOR_HEALTH_COMPETITOR — Group C, P1 tier acquisition"),
        ("Videos Captured", len(videos)),
        ("Regular Videos", regular_count),
        ("Shorts", shorts_count),
        ("Source Actor", "streamers/youtube-scraper"),
        ("Scrape Date", COLLECTION_DATE),
        ("Relevant Run IDs", run_ids),
        ("Relevant Dataset IDs", dataset_ids),
        ("Completeness Notes", f"{len(videos)} videos captured across {len(RUNS)} Apify runs "
                                f"(94-video initial catalog acquisition + 4-video Priority A Shorts backfill); "
                                f"0 duplicate IDs."),
        ("Transcript Notes", f"{real_transcripts}/{len(videos)} videos have a real YouTube transcript "
                              f"({user_generated} user-generated, {auto_generated} auto-generated captions; "
                              f"no paid AI transcription used); 0 videos have an explicit no-subtitle gap."),
    ]:
        overview.append([field, value])

    all_sheet = workbook["All Videos"]
    all_sheet.append([f"All {len(videos)} Videos (newest first)"])
    all_sheet.append(["Rates, Views/Day, and Words/Min are computed values."])
    all_sheet.append([])
    all_sheet.append(ALL_VIDEO_HEADERS)
    scrape_date = datetime.strptime(COLLECTION_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    for video in videos:
        views, likes, comments = video["views"], video["likes"], video["comments"]
        like_rate = likes / views if views else 0
        comment_rate = comments / views if views else 0
        engagement = (likes + comments) / views if views else 0
        days = max(1, (scrape_date.date() - video["published"].date()).days)
        views_per_day = views / days
        words_per_minute = (video["words"] / (video["seconds"] / 60)) if video["seconds"] else 0
        all_sheet.append([
            video["index"], video["id"], video["title"], video["url"],
            video["published"].strftime("%Y-%m-%d %H:%M:%S"), video["published"].date(),
            video["published"].strftime("%A"), video["duration"], video["seconds"],
            views, likes, comments, like_rate, comment_rate, engagement, views_per_day,
            video["words"], words_per_minute, len(video["description"]), len(video["links"]),
            len(video["tags"]), video["caption_type"], video["filename"], video["thumbnail"],
            "Yes" if video["members_only"] else "No", "Yes" if video["paid"] else "No",
            "Yes" if video["comments_off"] else "No", "Yes" if video["age_restricted"] else "No",
        ])
    add_table(all_sheet, f"A4:AB{4 + len(videos)}", "BetterHealthVideosTable")
    all_sheet.freeze_panes = "D5"

    descriptions = workbook["Descriptions"]
    descriptions.append([f"Full Video Descriptions — all {len(videos)} videos"])
    descriptions.append(["Complete description text plus hashtags and every recovered URL."])
    descriptions.append([])
    descriptions.append(DESCRIPTION_HEADERS)
    for video in videos:
        descriptions.append([
            video["index"], video["id"], video["title"],
            ", ".join(video["tags"]) or "—", len(video["links"]),
            "\n".join(video["links"]) if video["links"] else "—",
            video["description"] or "No public description has been added to this video.",
        ])
    add_table(descriptions, f"A4:G{4 + len(videos)}", "BetterHealthDescriptionsTable")
    descriptions.freeze_panes = "D5"

    verification = workbook["Verification"]
    verification.append(["Verification — completeness check"])
    verification.append([f"Every value below is computed from the registered {len(videos)}-video master and channel package data."])
    verification.append([])
    verification.append(["Check", "Value", "Result"])
    verification.append(["Videos captured across all runs", PUBLIC_VIDEO_COUNT,
                          f"Actor runs {', '.join(run['run_id'] for run in RUNS)} returned exactly "
                          f"{PUBLIC_VIDEO_COUNT} videos combined"])
    verification.append(["Videos captured", len(videos), "Matches combined Actor output exactly"])
    verification.append(["Real transcripts", real_transcripts, f"{real_transcripts}/{len(videos)} videos have YouTube captions"])
    verification.append(["Explicit transcript gaps", len(videos) - real_transcripts,
                          "None; every captured video has a YouTube caption track"])
    verification.append(["Duplicate video IDs", 0, "No duplicates across combined runs"])
    for run in RUNS:
        verification.append([f"Actual run cost ({run['run_id']})", run["cost_usd"], f"Under the {run['cost_cap']} approved cap"])

    analysis = workbook["Analysis"]
    analysis.append([f"Channel Analysis — {CHANNEL_NAME}"])
    analysis.append([f"Descriptive summary of {len(videos)} captured videos. No recommendations or strategy conclusions."])
    analysis.append([])
    analysis.append(["Metric", "Value"])
    total_views = sum(video["views"] for video in videos)
    analysis.append(["Videos published", len(videos)])
    analysis.append(["Total views (captured videos)", total_views])
    analysis.append(["Average views per video", round(total_views / len(videos), 1)])

    return workbook


def build_zip(videos: list[dict]) -> None:
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        index_lines = []
        for video in videos:
            if video["has_transcript"]:
                caption_type, language, word_count_value = video["caption_type"], video["language"], video["words"]
                body = video["transcript"]
            else:
                caption_type, language, word_count_value = "NONE", "NOT_AVAILABLE", 0
                body = ("(No transcript available. YouTube provides no captions or subtitles for this video; "
                        "Apify extraction confirmed no caption track exists.)")
            header_lines = [
                f"Channel      : {CHANNEL_NAME}",
                f"Title        : {video['title']}",
                f"Video ID     : {video['id']}",
                f"URL          : {video['url']}",
                f"Published    : {video['published'].strftime('%Y-%m-%dT%H:%M:%S.000Z')}",
                f"Duration     : {video['duration']}",
                f"Content type : {video['content_type']}",
                f"Views        : {video['views']}",
                f"Likes        : {video['likes']}",
                f"Comments     : {video['comments']}",
                f"Hashtags     : {', '.join(video['tags'])}",
                f"Caption type : {caption_type}",
                f"Language     : {language}",
                f"Word count   : {word_count_value}",
            ]
            separator = "=" * 78
            text = "\n".join(header_lines) + f"\n{separator}\nDESCRIPTION\n{separator}\n" + \
                (video["description"] or "No public description has been added to this video.") + \
                f"\n{separator}\nTRANSCRIPT\n{separator}\n" + body + "\n"
            archive.writestr(video["filename"], text)
            index_lines.append(f"{video['filename']} | {video['id']} | {video['title']}")
        archive.writestr("INDEX.txt", "\n".join(index_lines) + "\n")


def main() -> int:
    videos = load_videos()
    assert len(videos) == PUBLIC_VIDEO_COUNT, f"expected {PUBLIC_VIDEO_COUNT} videos, found {len(videos)}"
    assert sum(1 for v in videos if v["has_transcript"]) == PUBLIC_VIDEO_COUNT
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    build_workbook(videos).save(WORKBOOK_PATH)
    build_zip(videos)
    print(json.dumps({"workbook": str(WORKBOOK_PATH), "zip": str(ZIP_PATH), "videos": len(videos)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
