#!/usr/bin/env python3
"""Materialize importer-shaped workbooks from sources pinned by Git commit, for scripts/register_supplied_channel.py.

Copies values only. A value the source does not know stays empty, never 0. Nothing is computed except converting a
timestamp to UTC and an ID to its watch URL. Writes no database. Needs the pinned commits in the local object store.
Usage: python scripts/build_reviewed_channel_workbooks.py
"""
import csv
import hashlib
import io
import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research/registry-ingestion"
sys.path.insert(0, str(ROOT / "scripts"))
from source_adapters import youtube_master_data as ymd  # noqa: E402

UNKNOWN = {"", "UNKNOWN", "NULL", "NONE", "N/A", "NA", "NOT_AVAILABLE", "UNAVAILABLE"}
VIDEO_COLUMNS = ["#", "Video ID", "Title", "Video URL", "Published (UTC)", "Sec", "Views", "Likes", "Comments",
                 "Views/Day", "Engagement", "Desc Chars", "Transcript Words", "Transcript File", "Thumbnail URL"]
APIFY_FIELDS = {"Video ID": "video_id", "Title": "title", "Published (UTC)": "publication_timestamp_utc",
                "Sec": "duration_seconds", "Views": "view_count", "Likes": "like_count", "Comments": "comment_count",
                "Views/Day": "views_per_day", "Engagement": "engagement_rate", "Thumbnail URL": "thumbnail_url",
                "Full Description": "description"}
SUSPECT_ZERO = "Actor returned 0 with commentsTurnedOff false on a partial row (description null) at 238,267 views. " \
               "Kept empty as unverified; the source value is preserved in its own file."
SPECS = [
    {"slug": "casual-finance", "commit": "1adfdeb9462023b39fa62b9a54da12ccd874ae16",
     "path": "research/casually-finance-video-inventory/CASUALLY_FINANCE_VIDEO_INVENTORY.csv",
     "channel": {"Channel Name": "Casual Finance", "Handle": "@CasuallyFinance", "Channel ID": "UCrNfRFWnLC3tCy1TnyhVQ7g",
                 "Channel URL": "https://www.youtube.com/@CasuallyFinance"},
     "scraped": "19 Oct 2026", "source_label": "PR #37 yt-dlp inventory",
     "fields": {"Video ID": "Video ID", "Title": "Video Title", "Sec": "Duration (sec)", "Views": "Views", "Likes": "Likes",
                "Comments": "Comments", "Thumbnail URL": "Thumbnail URL", "Full Description": "Description"},
     "published": lambda r: f"{r['Upload Date']}T{r['Upload Time (UTC)']}Z"},
    {"slug": "barely-evolved", "commit": "c4212c90ecd57fe9416da2948a95669050366512", "path": "research/barely-evolved-metadata/VIDEO_MASTER.csv",
     "channel": {"Channel Name": "Barely Evolved", "Handle": "@BarelyEvolved", "Channel ID": "UCH59TmQhPOPhC3M17jCWpRQ",
                 "Channel URL": "https://www.youtube.com/channel/UCH59TmQhPOPhC3M17jCWpRQ",
                 "Subscribers": 111000, "Total Videos (YouTube)": 4},
     "scraped": "20 Oct 2026", "source_label": "PR #43 Apify export", "fields": APIFY_FIELDS,
     "suppress": {("4X3xd3MDZro", "Comments"): SUSPECT_ZERO, ("4X3xd3MDZro", "Engagement"): "Derived from the suspect comment count."}},
    {"slug": "primitive-education", "commit": "967ea707a0d7198754d132a978962baa96073f49", "path": "research/youtube-12-channel-metadata/ALL_PUBLIC_VIDEOS.csv",
     "where": ("channel_id", "UCsuQtyrMiUPdHUQ8WaqsFvQ"),
     "channel": {"Channel Name": "Primitive Education", "Handle": "@PrimitiveEducation", "Channel ID": "UCsuQtyrMiUPdHUQ8WaqsFvQ",
                 "Channel URL": "https://www.youtube.com/channel/UCsuQtyrMiUPdHUQ8WaqsFvQ"},
     "scraped": "20 Oct 2026", "source_label": "PR #39 Apify export", "fields": APIFY_FIELDS},
    {"slug": "xkcd-what-if-census-6", "commit": "3bd92e6ac578b9699a725a96ec129f2c97b4263c",
     "path": "research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv",
     "only": {"35KZm1yiyIE", "NxVdO7M2YdM", "TIDHee_Q5Gk", "XwJAbyn5uGY", "alBQCm0QpJg", "alkJ7xScBiw"},
     "channel": {"Channel Name": "xkcd's What If?", "Handle": "@xkcd_whatif", "Channel ID": "UC6IxnFzHofFJ5X2PycSMsww",
                 "Channel URL": "https://www.youtube.com/channel/UC6IxnFzHofFJ5X2PycSMsww"},
     "scraped": "04 Nov 2026", "source_label": "visual-forensics census",
     "fields": {"Video ID": "video_id", "Title": "title", "Sec": "duration_s", "Views": "views_player", "Likes": "likes",
                "Comments": "comments", "Thumbnail URL": "thumbnail_ref"},
     "published": lambda r: to_utc(r["publish_datetime"])},
]


def known(value):
    """Source value, or None when the source does not know it. UNAVAILABLE_* markers are unknown too."""
    text = (value or "").strip()
    return None if text.upper() in UNKNOWN or text.upper().startswith("UNAVAILABLE_") else value


def to_utc(stamp):
    return datetime.fromisoformat(stamp).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def number(value):
    return None if value is None else float(value) if "." in value else int(value)


def video_row(spec, source):
    """One workbook record. Metric text that is neither known-unknown nor numeric raises instead of guessing."""
    fields = spec["fields"]
    vid = source[fields["Video ID"]]
    row = {column: known(source[name]) for column, name in fields.items()}
    if "published" in spec:
        row["Published (UTC)"] = spec["published"](source)
    for suppressed_vid, column in spec.get("suppress", {}):
        if suppressed_vid == vid:
            row[column] = None
    for column in ("Sec", "Views", "Likes", "Comments", "Views/Day", "Engagement"):
        row[column] = number(row.get(column))
    row["Video URL"] = "https://www.youtube.com/watch?v=" + vid
    return row


def read_source(spec, show=None):
    show = show or (lambda c, p: subprocess.run(["git", "-C", str(ROOT), "show", f"{c}:{p}"], capture_output=True, check=True).stdout)
    data = show(spec["commit"], spec["path"])
    csv.field_size_limit(10**9)
    rows = list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline="")))
    if "where" in spec:
        rows = [r for r in rows if r[spec["where"][0]] == spec["where"][1]]
    if "only" in spec:
        rows = [r for r in rows if r[spec["fields"]["Video ID"]] in spec["only"]]
    return data, rows


def write_workbook(path, spec, rows):
    book = openpyxl.Workbook()
    overview = book.active
    overview.title = "Channel Overview"
    overview.append([f"Source: {spec['source_label']} at {spec['commit']}. Scraped {spec['scraped']}. Reviewed materialization; not a new crawl."])
    overview.append(["Field", "Value"])
    for field, value in spec["channel"].items():
        overview.append([field, value])
    videos = book.create_sheet("All Videos")
    videos.append(VIDEO_COLUMNS)
    descriptions = book.create_sheet("Descriptions")
    descriptions.append(["#", "Video ID", "Full Description"])
    for index, row in enumerate(rows, 1):
        videos.append([index if column == "#" else row.get(column) for column in VIDEO_COLUMNS])
        descriptions.append([index, row["Video ID"], row.get("Full Description")])
    book.save(path)


def verify(path, spec, rows):
    """Read the workbook back with the importer's own parser and compare every copied value."""
    parsed = ymd.read_workbook(path)
    assert list(parsed["channels"]) == [spec["channel"]["Channel Name"]]
    assert ymd.find_scraped_date(parsed["banner_lines"]), "importer needs a scrape date"
    assert len(parsed["videos"]) == len(rows) and len({v["Video ID"][0] for v in parsed["videos"]}) == len(rows)
    for got, want in zip(parsed["videos"], rows):
        for column in ("Video ID", "Title", "Video URL", "Published (UTC)", "Thumbnail URL", "Full Description"):
            assert (got.get(column, (None,))[0] or None) == (want.get(column) or None), (want["Video ID"], column)
        for column in ("Sec", "Views", "Likes", "Comments"):
            value = got[column][0]
            assert (None if value in (None, "") else float(value)) == want.get(column), (want["Video ID"], column)
        for column in ("Views/Day", "Engagement"):  # openpyxl writes 16 significant digits
            value, expected = got[column][0], want.get(column)
            assert (value in (None, "") and expected is None) or math.isclose(float(value), expected, rel_tol=1e-12), (want["Video ID"], column)
        assert not got["Transcript File"][0] and got["Transcript Words"][0] in (None, "")


def build(spec, output=OUTPUT, show=None):
    data, sources = read_source(spec, show)
    rows = [video_row(spec, s) for s in sources]
    folder = output / spec["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    workbook = folder / f"{spec['slug']}_reviewed.xlsx"
    write_workbook(workbook, spec, rows)
    verify(workbook, spec, rows)
    columns = [c for c in VIDEO_COLUMNS if c not in ("#", "Desc Chars", "Transcript Words", "Transcript File")] + ["Full Description"]
    review = {
        "status": "MACHINE_CHECKED_OWNER_REVIEW_PENDING",
        "source": {"commit": spec["commit"], "path": spec["path"], "sha256": hashlib.sha256(data).hexdigest(), "label": spec["source_label"]},
        "workbook_sha256": hashlib.sha256(workbook.read_bytes()).hexdigest(),
        "videos": len(rows), "channel": spec["channel"], "scraped": spec["scraped"],
        "empty_because_source_lacks": {c: sum(r.get(c) is None for r in rows) for c in columns if any(r.get(c) is None for r in rows)},
        "always_empty": ["Desc Chars", "Transcript Words", "Transcript File"],
        "suppressed": [{"video_id": k[0], "column": k[1], "reason": v} for k, v in spec.get("suppress", {}).items()],
        "transcript_pending_ids": sorted(r["Video ID"] for r in rows),
    }
    (folder / "REVIEW.json").write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return review


if __name__ == "__main__":
    for spec in SPECS:
        result = build(spec)
        print(spec["slug"], result["videos"], "videos, empty:", result["empty_because_source_lacks"])
