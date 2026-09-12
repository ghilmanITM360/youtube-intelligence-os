#!/usr/bin/env python3
"""Apply verified transcript-recovery outcomes without rewriting source artifacts.

This script updates a derived five-sheet workbook and transcript ZIP after a
targeted Actor run confirms that placeholder transcripts remain unavailable.
It edits workbook XML cells in place so formula text and cached values survive.
"""

from __future__ import annotations

import argparse
import csv
import json
import posixpath
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
DOC_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
XML_NS = "http://www.w3.org/XML/1998/namespace"
ET.register_namespace("", MAIN_NS)
ET.register_namespace("r", DOC_NS)


def _subtitle_plaintext(record: dict) -> tuple[str | None, str | None, str | None]:
    subtitles = record.get("subtitles")
    if not isinstance(subtitles, list):
        return None, None, None
    for subtitle in subtitles:
        if not isinstance(subtitle, dict):
            continue
        plaintext = subtitle.get("plaintext")
        if isinstance(plaintext, str) and plaintext.strip():
            return plaintext.strip(), subtitle.get("type"), subtitle.get("language")
    return None, None, None


def build_recovery_results(raw_records: list[dict], live_records: list[dict], run_id: str) -> list[dict]:
    """Join Actor and browser evidence by video ID and classify each result."""
    live_by_id = {str(item["video_id"]): item for item in live_records}
    results = []
    for record in raw_records:
        video_id = str(record.get("id") or "")
        if not video_id:
            raise ValueError("Actor recovery record has no video ID")
        live = live_by_id.get(video_id)
        if live is None:
            raise ValueError(f"No live-browser evidence for {video_id}")
        transcript, subtitle_type, language = _subtitle_plaintext(record)
        if transcript:
            recovery_result = "RECOVERED"
            reason = "Transcript plaintext recovered by targeted Actor run."
            actor_evidence = f"Actor run {run_id} returned subtitle plaintext."
        elif live.get("availability") == "MEMBERS_ONLY":
            recovery_result = "MEMBERS_ONLY_CAPTIONS_UNAVAILABLE"
            reason = (
                "Members-only video; unplayable without channel membership. "
                "YouTube displays 'Subtitles/closed captions unavailable'."
            )
            actor_evidence = (
                f"Actor run {run_id} returned subtitles=null and transcriptionUrl=null; "
                "run log: No subtitles found."
            )
        else:
            recovery_result = "ACTOR_EXTRACTION_FAILED_OR_UNKNOWN"
            reason = "Actor returned no transcript; browser evidence did not establish a more specific cause."
            actor_evidence = (
                f"Actor run {run_id} returned subtitles={record.get('subtitles')!r} and "
                f"transcriptionUrl={record.get('transcriptionUrl')!r}."
            )
        results.append({
            "video_id": video_id,
            "title": record.get("title"),
            "youtube_url": record.get("url"),
            "upload_date": record.get("date"),
            "view_count": record.get("viewCount"),
            "availability": live.get("availability"),
            "playable_without_membership": live.get("playable_without_membership"),
            "captions_visible": live.get("captions_visible"),
            "youtube_caption_control": live.get("youtube_caption_control"),
            "resolved_url": live.get("resolved_url"),
            "redirected": live.get("resolved_url") != record.get("url"),
            "subtitle_type": subtitle_type,
            "subtitle_language": language,
            "transcript_plaintext": transcript,
            "transcript_word_count": len(transcript.split()) if transcript else 0,
            "actor_evidence": actor_evidence,
            "verified_reason": reason,
            "recovery_result": recovery_result,
        })
    raw_ids = {item["video_id"] for item in results}
    live_ids = set(live_by_id)
    if raw_ids != live_ids:
        raise ValueError(f"Actor/live video ID mismatch: actor={sorted(raw_ids)}, live={sorted(live_ids)}")
    return sorted(results, key=lambda item: item["video_id"])


def _video_id_from_transcript(text: str) -> str | None:
    match = re.search(r"^Video ID\s+:\s*(\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def update_placeholder_archive(
    source_path: Path,
    output_path: Path,
    verified_reasons: dict[str, str],
    run_id: str,
) -> None:
    """Replace speculative placeholder wording and INDEX notes for verified gaps."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(source_path) as source, zipfile.ZipFile(output_path, "w") as output:
        for info in source.infolist():
            data = source.read(info.filename)
            if info.filename == "INDEX.txt":
                text = data.decode("utf-8")
                text = text.replace(
                    "Without transcript (view count hidden by creator, confirmed on 2 scrapes):",
                    "Without transcript (verified members-only; captions unavailable):",
                )
                text = text.replace(
                    "[NO TRANSCRIPT - view count hidden by creator]",
                    "[NO TRANSCRIPT - members-only; captions unavailable]",
                )
                data = text.encode("utf-8")
            elif info.filename.endswith(".txt"):
                text = data.decode("utf-8")
                video_id = _video_id_from_transcript(text)
                if video_id in verified_reasons:
                    text = re.sub(
                        r"^Caption type\s+:.*$",
                        "Caption type : NONE - members-only; captions unavailable",
                        text,
                        flags=re.MULTILINE,
                    )
                    marker = "TRANSCRIPT\n==============================================================================\n"
                    if marker not in text:
                        raise ValueError(f"{info.filename}: transcript marker missing")
                    prefix = text.split(marker, 1)[0] + marker
                    text = prefix + f"({verified_reasons[video_id]} Targeted Actor run {run_id} returned no subtitles.)\n"
                    data = text.encode("utf-8")
            output.writestr(info, data)


def _sheet_paths(archive: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels.findall(f"{{{PKG_NS}}}Relationship")
    }
    paths = {}
    for sheet in workbook.find(f"{{{MAIN_NS}}}sheets"):
        relation_id = sheet.attrib[f"{{{DOC_NS}}}id"]
        target = targets[relation_id].lstrip("/")
        paths[sheet.attrib["name"]] = (
            posixpath.normpath(target)
            if target.startswith("xl/")
            else posixpath.normpath(posixpath.join("xl", target))
        )
    return paths


def _set_inline_string(sheet_xml: bytes, coordinate: str, value: str) -> bytes:
    root = ET.fromstring(sheet_xml)
    cell = root.find(f".//{{{MAIN_NS}}}c[@r='{coordinate}']")
    if cell is None:
        raise ValueError(f"Workbook cell {coordinate} not found")
    for child in list(cell):
        if child.tag in {f"{{{MAIN_NS}}}v", f"{{{MAIN_NS}}}is"}:
            cell.remove(child)
    cell.set("t", "inlineStr")
    inline = ET.SubElement(cell, f"{{{MAIN_NS}}}is")
    text = ET.SubElement(inline, f"{{{MAIN_NS}}}t")
    text.set(f"{{{XML_NS}}}space", "preserve")
    text.text = value
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def update_workbook_annotations(
    source_path: Path,
    output_path: Path,
    affected_video_ids: set[str],
    run_id: str,
    dataset_id: str,
) -> None:
    """Patch annotation cells while leaving formulas and cached values untouched."""
    from openpyxl import load_workbook

    workbook = load_workbook(source_path, data_only=False, read_only=True)
    try:
        video_cells = {}
        matched_ids = set()
        videos = workbook["All Videos"]
        for row_number in range(5, videos.max_row + 1):
            video_id = videos.cell(row_number, 2).value
            if video_id and str(video_id) in affected_video_ids:
                matched_ids.add(str(video_id))
                video_cells[f"V{row_number}"] = "NONE - members-only; captions unavailable"
                video_cells[f"Y{row_number}"] = "Yes"

        replacements: dict[str, dict[str, str]] = {"Channel Overview": {}, "Verification": {}}
        for sheet_name in replacements:
            for row in workbook[sheet_name].iter_rows():
                for cell in row:
                    value = cell.value
                    if not isinstance(value, str):
                        continue
                    lowered = value.lower()
                    if (
                        "two separate scrapes" in lowered
                        or "two scrapes" in lowered
                        or "hidden view count" in lowered
                        or "scrape gap" in lowered
                    ):
                        if sheet_name == "Channel Overview":
                            replacement = (
                                f"2.  Ten videos are members-only and unplayable without channel membership. "
                                f"YouTube showed subtitles/closed captions unavailable on 13 Sep 2026; targeted "
                                f"Apify run {run_id} / dataset {dataset_id} returned no subtitles and null view counts."
                            )
                        elif value.startswith("Videos with hidden view count"):
                            replacement = "Videos verified members-only with captions unavailable"
                        elif "scrape gap" in lowered:
                            replacement = "Videos verified members-only with captions unavailable"
                        elif "view count" in lowered:
                            replacement = (
                                f"10 members-only videos returned null view counts in targeted run {run_id}; "
                                "YouTube pages were unplayable without membership"
                            )
                        else:
                            replacement = (
                                f"10 members-only videos returned no subtitles in targeted run {run_id}; "
                                "YouTube displayed subtitles/closed captions unavailable"
                            )
                        replacements[sheet_name][cell.coordinate] = replacement
    finally:
        workbook.close()

    if matched_ids != affected_video_ids:
        raise ValueError(
            f"Workbook matched {len(matched_ids)} of {len(affected_video_ids)} affected IDs"
        )

    with zipfile.ZipFile(source_path) as source, tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        with zipfile.ZipFile(source_path) as source, zipfile.ZipFile(temp_path, "w") as output:
            sheet_paths = _sheet_paths(source)
            patch_by_path = {
                sheet_paths["All Videos"]: video_cells,
                sheet_paths["Channel Overview"]: replacements["Channel Overview"],
                sheet_paths["Verification"]: replacements["Verification"],
            }
            for info in source.infolist():
                data = source.read(info.filename)
                for coordinate, value in patch_by_path.get(info.filename, {}).items():
                    data = _set_inline_string(data, coordinate, value)
                output.writestr(info, data)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(temp_path, output_path)
    finally:
        temp_path.unlink(missing_ok=True)


def _write_clean_json(path: Path, results: list[dict], run_metadata: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "actor": run_metadata["actorName"],
        "actor_id": run_metadata["actorId"],
        "run_id": run_metadata["runId"],
        "dataset_id": run_metadata["datasetId"],
        "status": run_metadata["status"],
        "results": results,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_results_csv(path: Path, results: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "video_id", "title", "youtube_url", "upload_date", "view_count", "availability",
        "playable_without_membership", "captions_visible", "youtube_caption_control", "resolved_url",
        "redirected", "transcript_word_count", "actor_evidence", "verified_reason", "recovery_result",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--transcript-zip", type=Path, required=True)
    parser.add_argument("--raw-json", type=Path, required=True)
    parser.add_argument("--live-evidence", type=Path, required=True)
    parser.add_argument("--run-metadata", type=Path, required=True)
    parser.add_argument("--output-workbook", type=Path, required=True)
    parser.add_argument("--output-transcript-zip", type=Path, required=True)
    parser.add_argument("--clean-json", type=Path, required=True)
    parser.add_argument("--results-csv", type=Path, required=True)
    args = parser.parse_args()

    raw_records = json.loads(args.raw_json.read_text(encoding="utf-8"))
    live_records = json.loads(args.live_evidence.read_text(encoding="utf-8"))
    run_metadata = json.loads(args.run_metadata.read_text(encoding="utf-8"))
    results = build_recovery_results(raw_records, live_records, run_metadata["runId"])
    if any(item["recovery_result"] == "RECOVERED" for item in results):
        raise ValueError("This tool records unavailable-transcript verification; recovered plaintext needs package merge support")
    reasons = {item["video_id"]: item["verified_reason"] for item in results}
    update_workbook_annotations(
        args.workbook,
        args.output_workbook,
        set(reasons),
        run_metadata["runId"],
        run_metadata["datasetId"],
    )
    update_placeholder_archive(
        args.transcript_zip,
        args.output_transcript_zip,
        reasons,
        run_metadata["runId"],
    )
    _write_clean_json(args.clean_json, results, run_metadata)
    _write_results_csv(args.results_csv, results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
