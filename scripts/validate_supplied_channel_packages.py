#!/usr/bin/env python3
"""Validate supplied five-sheet YouTube workbooks and transcript ZIPs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse


REQUIRED_SHEETS = ["Channel Overview", "All Videos", "Descriptions", "Verification", "Analysis"]
VIDEO_HEADERS = [
    "#", "Video ID", "Title", "Video URL", "Published (UTC)", "Date", "Day",
    "Duration", "Sec", "Views", "Likes", "Comments", "Like Rate", "Comment Rate",
    "Engagement", "Views/Day", "Transcript Words", "Words/Min", "Desc Chars",
    "Desc Links", "Hashtags", "Caption Type", "Transcript File", "Thumbnail URL",
    "Members Only", "Paid", "Comments Off", "Age Restr.",
]
DESCRIPTION_HEADERS = [
    "#", "Video ID", "Title", "Hashtags", "Link Count", "Description Links (URLs)", "Full Description",
]
REQUIRED_TRANSCRIPT_HEADERS = [
    "Channel", "Title", "Video ID", "URL", "Published", "Duration", "Views", "Likes",
    "Comments", "Hashtags", "Caption type", "Language", "Word count",
]
FORMULA_ERRORS = {"#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NUM!", "#NULL!", "#SPILL!", "#CALC!"}
NO_DESCRIPTION_MARKERS = {
    "no public description", "no description has been added to this video.", "verified no public description",
}
HEADER_RE = re.compile(r"^([^:\n]+?)\s*:\s*(.*)$")
SECTION_RE = re.compile(r"^={10,}\s*$", re.MULTILINE)
HYPERLINK_RE = re.compile(r'^=HYPERLINK\(\s*"((?:[^"]|"")*)"\s*,', re.IGNORECASE)
TRANSCRIPT_WORD_RE = re.compile(r"[^\W_]+(?:['’_-][^\W_]+)*", re.UNICODE)


class ValidationError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def youtube_id_from_url(value: str) -> str | None:
    try:
        parsed = urlparse(str(value))
    except ValueError:
        return None
    host = parsed.netloc.lower().removeprefix("www.")
    if parsed.scheme not in {"http", "https"}:
        return None
    if host == "youtu.be":
        return parsed.path.strip("/") or None
    if host not in {"youtube.com", "m.youtube.com"}:
        return None
    if parsed.path == "/watch":
        return parse_qs(parsed.query).get("v", [None])[0]
    if parsed.path.startswith(("/shorts/", "/live/")):
        return parsed.path.split("/", 2)[2].split("/", 1)[0]
    return None


def youtube_id_from_cell(cached_value, formula_value) -> str | None:
    """Resolve a YouTube ID from a plain URL or an Excel HYPERLINK formula."""
    direct = youtube_id_from_url(str(cached_value))
    if direct:
        return direct
    match = HYPERLINK_RE.match(str(formula_value))
    if not match:
        return None
    return youtube_id_from_url(match.group(1).replace('""', '"'))


def count_transcript_words(text: str) -> int:
    """Match the package generator's Unicode letter/number tokenization."""
    return len(TRANSCRIPT_WORD_RE.findall(text))


def parse_transcript_text(text: str, member: str) -> dict:
    if "\nDESCRIPTION\n" not in text or "\nTRANSCRIPT\n" not in text:
        raise ValidationError(f"{member}: DESCRIPTION or TRANSCRIPT section missing")
    transcript_marker = re.search(r"\n={10,}\nTRANSCRIPT\n={10,}\n", text)
    description_marker = re.search(r"\n={10,}\nDESCRIPTION\n={10,}\n", text)
    if not transcript_marker or not description_marker or description_marker.start() >= transcript_marker.start():
        raise ValidationError(f"{member}: malformed DESCRIPTION/TRANSCRIPT section order")
    header_text = text[:description_marker.start()]
    headers = {}
    for line in header_text.splitlines():
        match = HEADER_RE.match(line)
        if match:
            headers[match.group(1).strip()] = match.group(2).strip()
    missing = [key for key in REQUIRED_TRANSCRIPT_HEADERS if key not in headers]
    if missing:
        raise ValidationError(f"{member}: transcript headers missing {missing}")
    body = text[transcript_marker.end():].strip()
    if not body:
        raise ValidationError(f"{member}: transcript body empty")
    try:
        declared_words = int(headers["Word count"].replace(",", ""))
    except ValueError as exc:
        raise ValidationError(f"{member}: invalid Word count") from exc
    actual_words = count_transcript_words(body)
    lower_body = body.lower()
    unavailability_markers = (
        "no transcript available",
        "members-only video",
        "captions unavailable",
        "captions disabled",
        "video unavailable",
        "actor extraction failed",
    )
    placeholder = (
        declared_words == 0
        and "NONE" in headers["Caption type"].upper()
        and body.startswith("(")
        and any(marker in lower_body for marker in unavailability_markers)
    )
    if not placeholder and declared_words != actual_words:
        raise ValidationError(f"{member}: transcript word count {actual_words} != declared {declared_words}")
    return {
        "headers": headers,
        "description": text[description_marker.end():transcript_marker.start()].strip(),
        "transcript": body,
        "word_count": 0 if placeholder else actual_words,
        "placeholder": placeholder,
    }


def _find_overview_value(sheet, label: str):
    for row in sheet.iter_rows():
        if row and row[0].value == label:
            return row[1].value if len(row) > 1 else None
    return None


def _formula_cache_errors(formula_book, value_book) -> tuple[list[str], int]:
    errors, formula_count = [], 0
    for formula_sheet, value_sheet in zip(formula_book.worksheets, value_book.worksheets):
        for row in formula_sheet.iter_rows():
            for cell in row:
                if cell.data_type != "f":
                    continue
                formula_count += 1
                cached = value_sheet[cell.coordinate].value
                if cached is None or (isinstance(cached, str) and cached in FORMULA_ERRORS):
                    errors.append(f"{formula_sheet.title}!{cell.coordinate} cached={cached!r}")
    return errors, formula_count


def has_expected_video_filter(sheet, expected_ref: str) -> bool:
    """Accept either worksheet auto-filter or an Excel table over the video rows."""
    if sheet.auto_filter.ref == expected_ref:
        return True
    return any(sheet.tables[name].ref == expected_ref for name in sheet.tables.keys())


def validate_pair(spec: dict) -> dict:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise ValidationError("openpyxl is required; use bundled workspace Python") from exc

    channel = str(spec["channel"])
    expected = int(spec["expected_count"])
    workbook_path = Path(spec["workbook"])
    zip_path = Path(spec["zip"])
    for path in (workbook_path, zip_path):
        if not path.is_file():
            raise ValidationError(f"{channel}: missing file {path}")
    if spec.get("workbook_sha256") and sha256_file(workbook_path) != spec["workbook_sha256"]:
        raise ValidationError(f"{channel}: workbook SHA-256 mismatch")
    if spec.get("zip_sha256") and sha256_file(zip_path) != spec["zip_sha256"]:
        raise ValidationError(f"{channel}: ZIP SHA-256 mismatch")

    formula_book = load_workbook(workbook_path, data_only=False, read_only=False)
    value_book = load_workbook(workbook_path, data_only=True, read_only=False)
    try:
        if formula_book.sheetnames != REQUIRED_SHEETS:
            raise ValidationError(f"{channel}: sheet order {formula_book.sheetnames!r}")
        videos_sheet = formula_book["All Videos"]
        values_sheet = value_book["All Videos"]
        headers = [videos_sheet.cell(4, column).value for column in range(1, 29)]
        if headers != VIDEO_HEADERS:
            raise ValidationError(f"{channel}: All Videos headers differ")
        descriptions_sheet = formula_book["Descriptions"]
        description_headers = [descriptions_sheet.cell(4, column).value for column in range(1, 8)]
        if description_headers != DESCRIPTION_HEADERS:
            raise ValidationError(f"{channel}: Descriptions headers differ")
        if str(videos_sheet.freeze_panes) != "D5":
            raise ValidationError(f"{channel}: freeze panes {videos_sheet.freeze_panes!r}")

        rows = []
        video_url_formulas = []
        for row_number in range(5, videos_sheet.max_row + 1):
            video_id = videos_sheet.cell(row_number, 2).value
            if video_id in (None, ""):
                continue
            rows.append({header: values_sheet.cell(row_number, index + 1).value for index, header in enumerate(VIDEO_HEADERS)})
            video_url_formulas.append(videos_sheet.cell(row_number, 4).value)
        if len(rows) != expected:
            raise ValidationError(f"{channel}: workbook videos {len(rows)} != expected {expected}")
        ids = [str(row["Video ID"]) for row in rows]
        duplicates = sorted(video_id for video_id, count in Counter(ids).items() if count > 1)
        if duplicates:
            raise ValidationError(f"{channel}: duplicate video IDs {duplicates}")
        expected_filter_ref = f"A4:AB{4 + expected}"
        if not has_expected_video_filter(videos_sheet, expected_filter_ref):
            table_refs = [videos_sheet.tables[name].ref for name in videos_sheet.tables.keys()]
            raise ValidationError(
                f"{channel}: filter range missing; worksheet={videos_sheet.auto_filter.ref!r}, tables={table_refs!r}"
            )

        numeric_columns = ["Sec", "Views", "Likes", "Comments", "Transcript Words", "Desc Chars", "Desc Links"]
        invalid_rows = []
        missing_fields = []
        transcript_names = []
        for row, video_url_formula in zip(rows, video_url_formulas):
            video_id = str(row["Video ID"])
            if not row["Title"]:
                invalid_rows.append(f"{video_id}: title missing")
            if youtube_id_from_cell(row["Video URL"], video_url_formula) != video_id:
                invalid_rows.append(f"{video_id}: invalid video URL")
            if not isinstance(row["Date"], (int, float, date, datetime)):
                invalid_rows.append(f"{video_id}: Date not typed")
            for column in numeric_columns:
                if row[column] in (None, "", "N/A", "Unavailable"):
                    missing_fields.append({"video_id": video_id, "field": column, "value": row[column]})
                elif not isinstance(row[column], (int, float)):
                    invalid_rows.append(f"{video_id}: {column} not numeric")
            if not row["Transcript File"]:
                invalid_rows.append(f"{video_id}: transcript filename missing")
            transcript_names.append(str(row["Transcript File"]))
        if invalid_rows:
            raise ValidationError(f"{channel}: " + "; ".join(invalid_rows[:20]))

        description_rows = {}
        missing_descriptions = []
        for row_number in range(5, descriptions_sheet.max_row + 1):
            video_id = descriptions_sheet.cell(row_number, 2).value
            if not video_id:
                continue
            video_id = str(video_id)
            description = descriptions_sheet.cell(row_number, 7).value
            description_rows[video_id] = description
            if description in (None, ""):
                missing_descriptions.append(video_id)
        if set(description_rows) != set(ids):
            raise ValidationError(f"{channel}: Descriptions video IDs do not match All Videos")

        cache_errors, formula_count = _formula_cache_errors(formula_book, value_book)
        if cache_errors:
            raise ValidationError(f"{channel}: formula cache errors: {cache_errors[:20]}")
    finally:
        formula_book.close()
        value_book.close()

    with zipfile.ZipFile(zip_path) as archive:
        corrupt_member = archive.testzip()
        if corrupt_member:
            raise ValidationError(f"{channel}: corrupt ZIP member {corrupt_member}")
        members = archive.namelist()
        if any("/" in name or "\\" in name for name in members):
            raise ValidationError(f"{channel}: ZIP has enclosing directory")
        if any("__MACOSX" in name or name.startswith(".") or name.endswith((".tmp", "~")) for name in members):
            raise ValidationError(f"{channel}: ZIP contains metadata or temporary file")
        if members.count("INDEX.txt") != 1:
            raise ValidationError(f"{channel}: ZIP must contain exactly one INDEX.txt")
        transcript_members = [name for name in members if name != "INDEX.txt"]
        if len(transcript_members) != expected or len(members) != expected + 1:
            raise ValidationError(f"{channel}: ZIP member counts {len(transcript_members)}/{len(members)}")
        if len(transcript_members) != len(set(transcript_members)):
            raise ValidationError(f"{channel}: duplicate transcript filenames")
        if set(transcript_members) != set(transcript_names):
            raise ValidationError(f"{channel}: workbook transcript filenames do not match ZIP")
        index_text = archive.read("INDEX.txt").decode("utf-8")
        parsed = {}
        for name in transcript_members:
            try:
                text = archive.read(name).decode("utf-8")
            except UnicodeDecodeError as exc:
                raise ValidationError(f"{channel}: {name} is not UTF-8") from exc
            result = parse_transcript_text(text, name)
            video_id = result["headers"]["Video ID"]
            if video_id not in ids or not name.startswith(tuple(f"{number:03d}_{video_id}_" for number in range(1, expected + 1))):
                raise ValidationError(f"{channel}: {name} video ID mapping invalid")
            if result["headers"]["Channel"] != channel:
                raise ValidationError(f"{channel}: {name} channel header differs")
            if youtube_id_from_url(result["headers"]["URL"]) != video_id:
                raise ValidationError(f"{channel}: {name} URL differs")
            if name not in index_text:
                raise ValidationError(f"{channel}: INDEX missing {name}")
            parsed[video_id] = result
        if set(parsed) != set(ids):
            raise ValidationError(f"{channel}: transcript IDs do not match workbook")

    workbook_titles = {str(row["Video ID"]): str(row["Title"]) for row in rows}
    title_mismatches = [video_id for video_id, item in parsed.items() if item["headers"]["Title"] != workbook_titles[video_id]]
    if title_mismatches:
        raise ValidationError(f"{channel}: transcript title mismatches {title_mismatches}")
    overview_book = load_workbook(workbook_path, read_only=True)
    try:
        channel_name = _find_overview_value(overview_book["Channel Overview"], "Channel Name")
    finally:
        overview_book.close()
    if channel_name != channel:
        raise ValidationError(f"{channel}: workbook Channel Name is {channel_name!r}")

    return {
        "channel": channel,
        "workbook": str(workbook_path),
        "zip": str(zip_path),
        "workbook_bytes": workbook_path.stat().st_size,
        "zip_bytes": zip_path.stat().st_size,
        "workbook_sha256": sha256_file(workbook_path),
        "zip_sha256": sha256_file(zip_path),
        "video_count": len(ids),
        "unique_video_ids": len(set(ids)),
        "transcript_files": len(parsed),
        "placeholder_transcripts": sum(1 for item in parsed.values() if item["placeholder"]),
        "placeholder_video_ids": sorted(video_id for video_id, item in parsed.items() if item["placeholder"]),
        "zip_members": len(parsed) + 1,
        "formula_count": formula_count,
        "missing_descriptions": missing_descriptions,
        "missing_fields": missing_fields,
        "video_ids": ids,
        "status": "VALID",
    }


def write_markdown(report: dict, path: Path) -> None:
    lines = [
        f"# {report['dataset_id']} Package Validation Report", "",
        f"- Packages: {len(report['packages'])}",
        f"- Workbook video rows: {report['total_videos']}",
        f"- Unique video IDs: {report['total_unique_video_ids']}",
        f"- Transcript files: {report['total_transcript_files']}",
        f"- Placeholder transcript files: {report['total_placeholder_transcripts']}",
        f"- ZIP members: {report['total_zip_members']}",
        f"- Formula cells with usable cached values: {report['total_formula_cells']}",
        f"- Missing descriptions: {report['total_missing_descriptions']}",
        "- Apify recovery: Not performed by validator; preserved missing-value evidence is listed below.",
    ]
    apify = report.get("apify")
    if apify:
        lines.extend([
            f"- Original Actor raw JSON: `{apify['raw_json']}`",
            f"- Actor run ID: `{apify['actor_run_id']}`",
            f"- Apify dataset ID: `{apify['dataset_id']}`",
        ])
    else:
        lines.append("- Original Actor raw JSON and Actor run IDs: Not supplied.")
    lines.extend([
        "",
        "| Channel | Videos | Transcript files | ZIP members | Missing descriptions | Status |", "|---|---:|---:|---:|---:|---|",
    ])
    for item in report["packages"]:
        lines.append(f"| {item['channel']} | {item['video_count']} | {item['transcript_files']} | {item['zip_members']} | {len(item['missing_descriptions'])} | {item['status']} |")
    lines.extend(["", "## Missing field evidence", "", "| Channel | Video ID | Field | Stored value |", "|---|---|---|---|"])
    missing = [(item["channel"], gap) for item in report["packages"] for gap in item["missing_fields"]]
    if missing:
        for channel, gap in missing:
            lines.append(f"| {channel} | `{gap['video_id']}` | {gap['field']} | {gap['value']} |")
    else:
        lines.append("| None |  |  |  |")
    lines.extend(["", "## Placeholder transcript evidence", ""])
    placeholders = [(item["channel"], video_id) for item in report["packages"] for video_id in item["placeholder_video_ids"]]
    if placeholders:
        lines.extend(f"- {channel}: `{video_id}`" for channel, video_id in placeholders)
    else:
        lines.append("None.")
    lines.extend(["", "## Validation scope", "", "Checked exact sheet order and columns, typed IDs/dates/numbers, freeze panes, filters, formula caches/errors, description reconciliation, valid video URLs, ZIP integrity/root structure, UTF-8, required transcript sections and headers, exact transcript word counts or explicit placeholders, filename/ID/title/channel mapping, and complete INDEX listings.", ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--report-json", type=Path)
    parser.add_argument("--report-md", type=Path)
    parser.add_argument("--overlap-csv", type=Path)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    packages = [validate_pair(spec) for spec in config["packages"]]
    all_ids = [video_id for item in packages for video_id in item["video_ids"]]
    duplicate_ids = sorted(video_id for video_id, count in Counter(all_ids).items() if count > 1)
    if duplicate_ids:
        raise ValidationError(f"cross-package duplicate video IDs: {duplicate_ids}")
    report = {
        "dataset_id": config["dataset_id"],
        "apify": config.get("apify"),
        "packages": packages,
        "total_videos": len(all_ids),
        "total_unique_video_ids": len(set(all_ids)),
        "total_transcript_files": sum(item["transcript_files"] for item in packages),
        "total_placeholder_transcripts": sum(item["placeholder_transcripts"] for item in packages),
        "total_zip_members": sum(item["zip_members"] for item in packages),
        "total_formula_cells": sum(item["formula_count"] for item in packages),
        "total_missing_descriptions": sum(len(item["missing_descriptions"]) for item in packages),
    }
    overlaps = []
    new_ids = set(all_ids)
    for comparison in config.get("compare_datasets", []):
        other_ids = set(comparison["video_ids"])
        overlap = sorted(new_ids & other_ids)
        overlaps.append({"dataset_id": comparison["dataset_id"], "overlap_count": len(overlap), "video_ids": overlap})
    report["overlaps"] = overlaps
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.report_md:
        write_markdown(report, args.report_md)
    if args.overlap_csv:
        args.overlap_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.overlap_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["new_dataset_id", "compared_dataset_id", "overlap_count", "video_id"])
            for item in overlaps:
                if item["video_ids"]:
                    for video_id in item["video_ids"]:
                        writer.writerow([config["dataset_id"], item["dataset_id"], item["overlap_count"], video_id])
                else:
                    writer.writerow([config["dataset_id"], item["dataset_id"], 0, ""])
    print(json.dumps({key: value for key, value in report.items() if key != "packages"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValidationError, KeyError, ValueError, zipfile.BadZipFile) as exc:
        print(f"VALIDATION_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
