#!/usr/bin/env python3
"""Build the cross-channel YouTube master tracker workbook.

Python/openpyxl port of scripts/build_youtube_channel_master_tracker.mjs.
The original Node generator requires @oai/artifact-tool, which is not an
available project dependency on this machine; this port reproduces the same
sheet names, columns, values, and hyperlink contract using only openpyxl and
the stdlib sqlite3 module, driven by the same normalized registry JSON and
registry database as the source of truth.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

GITHUB_BASE = "https://github.com/ghilmanITM360/youtube-intelligence-os/blob/main/"
NAVY = "1F4E78"


def excel_text(value) -> str:
    return str(value if value is not None else "").replace('"', '""')


def hyperlink_formula(url: str, label: str = "Open") -> str:
    return f'=HYPERLINK("{excel_text(url)}","{excel_text(label)}")'


def clean_evidence_path(root: Path, value: str) -> str:
    first = str(value or "").split("; ")[0].split("#")[0]
    first = re.sub(r":row=.*$", "", first)
    if first.startswith("https://"):
        return first
    match = re.match(r"^data/raw/competitors/(DS-\d{6})$", first)
    candidate = f"data/manifests/{match.group(1)}.md" if match else first
    if not candidate.startswith(("data/", "docs/", "scripts/")):
        raise ValueError(f"No repository evidence path: {value}")
    if not (root / candidate).is_file():
        raise FileNotFoundError(f"Evidence file missing: {candidate}")
    return candidate


def repo_formula(root: Path, value: str, label: str = "Evidence") -> str:
    text = str(value or "")
    url = text if text.startswith("https://") else GITHUB_BASE + clean_evidence_path(root, text)
    return hyperlink_formula(url, label)


def yes(condition) -> str:
    return "✓" if condition else "No"


def shorten(value, limit: int = 220) -> str:
    text = str(value or "").strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def as_date(value: str):
    from datetime import date

    return date.fromisoformat(value)


def sqlite_rows(database_path: Path, sql: str) -> list[dict]:
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    try:
        return [dict(row) for row in connection.execute(sql)]
    finally:
        connection.close()


HEADER_FILL = PatternFill("solid", fgColor=NAVY)
HEADER_FONT = Font(name="Arial", size=10, bold=True, color="FFFFFF")
LINK_FONT = Font(name="Arial", size=10, color="0563C1")
TITLE_FONT = Font(name="Arial", size=14, bold=True, color=NAVY)


def add_table(sheet, headers: list[str], rows: list[list], table_name: str) -> int:
    end_row = 4 + len(rows)
    for column, header in enumerate(headers, start=1):
        cell = sheet.cell(4, column, header)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row_index, row in enumerate(rows, start=5):
        for column, value in enumerate(row, start=1):
            sheet.cell(row_index, column, value)
    if rows:
        end_column = sheet.cell(4, len(headers)).column_letter
        table = Table(displayName=table_name, ref=f"A4:{end_column}{end_row}")
        table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
        sheet.add_table(table)
    sheet.freeze_panes = "A5"
    return end_row


def title(sheet, text: str, note: str = "") -> None:
    sheet.sheet_view.showGridLines = False
    sheet.cell(2, 1, text).font = TITLE_FONT
    if note:
        sheet.cell(3, 1, note).font = Font(name="Arial", size=10, italic=True, color="595959")


def build_workbook(root: Path, model: dict, database_path: Path) -> Workbook:
    datasets = sqlite_rows(
        database_path,
        """
        SELECT d.dataset_id,d.dataset_name,d.manifest_path,d.evidence_scope,d.limitations,
               count(distinct dc.canonical_channel_id) channel_count,
               count(distinct dv.youtube_video_id) video_count
        FROM datasets d
        LEFT JOIN dataset_channels dc ON dc.dataset_id=d.dataset_id
        LEFT JOIN dataset_videos dv ON dv.dataset_id=d.dataset_id
        GROUP BY d.dataset_id
        ORDER BY d.dataset_id
        """,
    )
    channel_by_id = {row["canonical_channel_id"]: row for row in model["channels"]}
    submissions_by_channel: dict[str, list] = {}
    for row in model["submissions"]:
        submissions_by_channel.setdefault(row["canonical_channel_id"], []).append(row)
    coverage_by_channel: dict[str, dict[str, dict]] = {}
    for row in model["intelligence_coverage"]:
        coverage_by_channel.setdefault(row["canonical_channel_id"], {})[row["capability_id"]] = row

    def display_status(row: dict, capability: str) -> str:
        return coverage_by_channel.get(row["canonical_channel_id"], {}).get(capability, {}).get("status", "NOT_AVAILABLE")

    workbook = Workbook()
    workbook.remove(workbook.active)
    sheet_names = [
        "Dashboard", "All Channels", "Pending Channels", "Data Coverage", "Visual Evidence",
        "Datasets", "Submitted URLs", "Intelligence Coverage", "Definitions",
    ]
    for name in sheet_names:
        workbook.create_sheet(name)

    all_channels = workbook["All Channels"]
    title(all_channels, "YouTube channel registry",
          "Identity, extraction, package, transcript, visual, intelligence, and first-party analytics states are independent.")
    all_headers = [
        "Canonical Channel ID", "Channel Name", "Current Handle", "YouTube Link", "Target Membership",
        "Target Batch", "Identity Verified", "Video Data Available", "Extraction Status",
        "Standard Package Available", "Historical-Format Data Available", "Saved Video Count",
        "Real Transcripts", "Transcript Placeholders", "Missing Descriptions", "Transcript Status",
        "Thumbnail URLs Available", "Downloaded Thumbnail Evidence", "Forensic Video Evidence",
        "Topic Intelligence", "Packaging Intelligence", "Hook Intelligence", "Script Intelligence",
        "Editing/Visual Intelligence", "Unified Orchestration", "Channel Strategy",
        "First-Party Analytics", "Evidence Links", "Dataset IDs", "Limitations", "Last Verified",
    ]
    all_rows = []
    for row in model["channels"]:
        submissions = submissions_by_channel.get(row["canonical_channel_id"], [])
        batches = ", ".join(dict.fromkeys(item["batch"] for item in submissions)) or "—"
        missing_descriptions = 0 if row["descriptions"] is None else row["video_count"] - row["descriptions"]
        all_rows.append([
            row["canonical_channel_id"], row["channel_name"], row["current_handle"] or "—",
            hyperlink_formula(row["canonical_url"], "YouTube"), row["target_group"], batches,
            yes(row["identity_status"] == "VERIFIED"), yes(row["video_count"] > 0), row["extraction_status"],
            yes(row["package_status"] == "STANDARD_PACKAGE"), yes(row["package_status"] == "HISTORICAL_FORMAT"),
            row["video_count"], row["real_transcripts"], row["placeholders"], missing_descriptions,
            row["transcript_status"], yes(row["visual_coverage"]["thumbnail_url_count"] > 0),
            yes(row["visual_coverage"]["downloaded_thumbnail_count"] > 0),
            yes(row["visual_coverage"]["visual_evidence_level"] == "FORENSIC_VIDEO_EVIDENCE"),
            display_status(row, "TOPIC_OPPORTUNITY"), display_status(row, "PACKAGING"),
            display_status(row, "HOOK"), display_status(row, "SCRIPT"), display_status(row, "EDITING_VISUAL"),
            display_status(row, "UNIFIED_ORCHESTRATION"), display_status(row, "CHANNEL_STRATEGY"),
            row["first_party_analytics_status"],
            repo_formula(root, row["workbook_path"] or row["visual_coverage"]["evidence_path"] or row["identity_evidence_source"]),
            ", ".join(row["dataset_ids"]) or "—",
            shorten(row["limitations"] or row["handle_unavailable_reason"]), as_date(row["verified_at"]),
        ])
    all_end = add_table(all_channels, all_headers, all_rows, "AllChannelsTable")
    for column in ("D", "AB"):
        for r in range(5, all_end + 1):
            all_channels[f"{column}{r}"].font = LINK_FONT
    all_channels.freeze_panes = "D5"

    pending = workbook["Pending Channels"]
    title(pending, "Channels awaiting extraction", "Identity is verified for identity-only rows. Video extraction and package creation have not started.")
    identity_only = [row for row in model["channels"] if row["source_group"] == "IDENTITY_ONLY"]
    pending_rows = [[
        row["channel_name"], hyperlink_formula(row["canonical_url"], "YouTube"), row["canonical_channel_id"],
        row["target_group"], "No video data",
        "Run authorized channel extraction; then build and validate a standard package.",
        row["extraction_status"], row["package_status"], "NOT_GENERATED", row["visual_asset_status"],
    ] for row in identity_only]
    pending_end = add_table(pending, [
        "Channel Name", "Channel URL", "Canonical ID", "Target Group", "Video Data Status",
        "Required Next Action", "Extraction Status", "Package Status", "Intelligence Status", "Visual Evidence",
    ], pending_rows, "PendingChannelsTable")
    for r in range(5, pending_end + 1):
        pending[f"B{r}"].font = LINK_FONT

    data_coverage = workbook["Data Coverage"]
    title(data_coverage, "Channel data coverage", "Availability marks are evidence-derived. A raw input does not imply a generated intelligence artifact.")
    actor_datasets = {"DS-000017", "DS-000020", "DS-000021", "DS-000023", "DS-000024", "DS-000025", "DS-000027"}
    data_rows = []
    for row in model["channels"]:
        capability_rows = list(coverage_by_channel.get(row["canonical_channel_id"], {}).values())
        data_rows.append([
            row["canonical_channel_id"], row["channel_name"], yes(row["identity_status"] == "VERIFIED"),
            yes(bool(row["channel_name"] and row["canonical_url"])), yes(row["video_count"] > 0),
            row["description_status"], yes(row["video_count"] > 0), row["transcript_status"],
            yes(row["package_status"] == "STANDARD_PACKAGE"), yes(row["package_status"] == "HISTORICAL_FORMAT"),
            yes(any(dataset_id in actor_datasets for dataset_id in row["dataset_ids"])),
            "✓" if row["dataset_ids"] else "Identity evidence only",
            yes(any(item["generated_artifact_available"] for item in capability_rows)),
        ])
    add_table(data_coverage, [
        "Canonical ID", "Channel", "Identity", "Channel Metadata", "Video Metadata", "Descriptions", "Metrics",
        "Transcripts", "Standard Package", "Historical Data", "Raw Actor Evidence", "Manifest / Checksums",
        "Intelligence Artifacts",
    ], data_rows, "DataCoverageTable")

    visual = workbook["Visual Evidence"]
    title(visual, "Visual evidence coverage", "Thumbnail URLs, downloaded thumbnails, screenshots, and forensic video evidence are not interchangeable.")
    visual_headers = [
        "Channel / Subject", "Canonical ID", "YouTube Link", "Thumbnail URL Count", "Downloaded Thumbnails",
        "Screenshots", "Keyframes", "Source Videos", "Timestamped Observations", "Evidence Level",
        "Editing/Visual Intelligence", "Evidence Link", "Limitation",
    ]
    visual_rows = []
    for row in model["channels"]:
        coverage = row["visual_coverage"]
        visual_rows.append([
            row["channel_name"], row["canonical_channel_id"], hyperlink_formula(row["canonical_url"], "YouTube"),
            coverage["thumbnail_url_count"], coverage["downloaded_thumbnail_count"], coverage["screenshot_count"],
            coverage["keyframe_count"], coverage["registered_source_video_count"],
            coverage["timestamped_visual_observation_count"], coverage["visual_evidence_level"],
            coverage["editing_visual_intelligence_status"], repo_formula(root, coverage["evidence_path"]),
            shorten(coverage["limitation_reason"]),
        ])
    visual_end = add_table(visual, visual_headers, visual_rows, "ChannelVisualEvidenceTable")
    for r in range(5, visual_end + 1):
        visual[f"C{r}"].font = LINK_FONT
        visual[f"L{r}"].font = LINK_FONT
    subject_title_row = visual_end + 1
    subject_header_row = subject_title_row + 1
    visual.cell(subject_title_row, 1, "Unmapped screenshot-only subjects").font = Font(name="Arial", size=12, bold=True, color=NAVY)
    for column, header in enumerate(visual_headers, start=1):
        cell = visual.cell(subject_header_row, column, header)
        cell.fill = PatternFill("solid", fgColor="548235")
        cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    subject_first_row = subject_header_row + 1
    for offset, row in enumerate(model["subjects"]):
        r = subject_first_row + offset
        visual.cell(r, 1, row["subject_name"])
        visual.cell(r, 2, "—")
        visual.cell(r, 3, "—")
        for column in (4, 5, 7, 8, 9):
            visual.cell(r, column, 0)
        visual.cell(r, 6, row["screenshot_count"])
        visual.cell(r, 10, row["visual_evidence_level"])
        visual.cell(r, 11, "NOT_APPLICABLE")
        visual.cell(r, 12, repo_formula(root, row["evidence_path"])).font = LINK_FONT
        visual.cell(r, 13, shorten(row["limitation"]))
    subject_last_row = subject_first_row + len(model["subjects"]) - 1
    if model["subjects"]:
        end_column = visual.cell(subject_header_row, len(visual_headers)).column_letter
        subject_table = Table(displayName="UnmappedScreenshotSubjectsTable", ref=f"A{subject_header_row}:{end_column}{subject_last_row}")
        subject_table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium4", showRowStripes=True)
        visual.add_table(subject_table)

    dataset_sheet = workbook["Datasets"]
    title(dataset_sheet, "Registered datasets", "Registered manifest datasets are included. Channel and video counts preserve many-to-many membership.")
    dataset_rows = [[
        row["dataset_id"], row["dataset_name"], row["channel_count"], row["video_count"],
        repo_formula(root, row["manifest_path"], "Manifest"), row["evidence_scope"] or "—", shorten(row["limitations"]),
    ] for row in datasets]
    dataset_end = add_table(dataset_sheet, [
        "Dataset ID", "Dataset Name", "Channel Count", "Video Count", "Manifest", "Evidence Scope", "Limitations",
    ], dataset_rows, "DatasetsTable")
    for r in range(5, dataset_end + 1):
        dataset_sheet[f"E{r}"].font = LINK_FONT

    submitted = workbook["Submitted URLs"]
    title(submitted, "Submitted YouTube URLs", "All submitted rows remain in authoritative order. Exact duplicates retain their prior-row references.")
    submitted_rows = [[
        row["global_row"], row["batch"], row["batch_row"], row["original_url"],
        hyperlink_formula(row["original_url"], "Original"), hyperlink_formula(row["normalized_url"], "Normalized"),
        yes(row["is_exact_duplicate"]), row["duplicate_of_global_row"] if row["duplicate_of_global_row"] is not None else "—",
        row["canonical_channel_id"], channel_by_id.get(row["canonical_channel_id"], {}).get("channel_name", ""),
        row["identity_status"], repo_formula(root, row["evidence_source"]), as_date(row["verified_at"]),
    ] for row in model["submissions"]]
    submitted_end = add_table(submitted, [
        "Global Row", "Batch", "Batch Row", "Original URL", "Original Link", "Normalized Link", "Exact Duplicate",
        "Duplicate Of Global Row", "Canonical ID", "Channel Name", "Identity Status", "Evidence Link", "Verified At",
    ], submitted_rows, "SubmittedUrlsTable")
    for column in ("E", "F", "L"):
        for r in range(5, submitted_end + 1):
            submitted[f"{column}{r}"].font = LINK_FONT

    intelligence = workbook["Intelligence Coverage"]
    title(intelligence, "Intelligence capability coverage",
          f"{len(model['intelligence_coverage'])} rows represent eight capabilities for {len(model['channels'])} channels; they do not represent completed reports.")
    intelligence_rows = [[
        row["canonical_channel_id"], channel_by_id.get(row["canonical_channel_id"], {}).get("channel_name", ""),
        row["capability_id"], row["status"], yes(row["input_data_available"]), yes(row["generated_artifact_available"]),
        clean_evidence_path(root, row["evidence_path"]), repo_formula(root, row["evidence_path"]),
        shorten(row["limitation_reason"]), as_date(row["last_verified_at"]),
    ] for row in model["intelligence_coverage"]]
    add_table(intelligence, [
        "Canonical ID", "Channel", "Capability", "Status", "Input Data Available", "Analysis Artifact Generated",
        "Evidence Path", "Evidence Link", "Limitation", "Last Verified",
    ], intelligence_rows, "IntelligenceCoverageTable")

    definitions = workbook["Definitions"]
    title(definitions, "Definitions and status rules",
          "These definitions prevent identity resolution, extraction, packages, visual evidence, intelligence, and analytics from being conflated.")
    definitions_rows = [
        ["Identity verified", "Canonical YouTube channel ID is proven by repository or official-page evidence."],
        ["Video data available", "One or more unique videos are stored for the canonical channel."],
        ["STANDARD_PACKAGE", "Validated new-style workbook and transcript ZIP package."],
        ["HISTORICAL_FORMAT", "Stored historical catalog data; not a new-style standard package."],
        ["NO_PACKAGE", "No standardized or historical channel package is registered."],
        ["COMPLETE", "Extraction evidence meets the applicable package or historical controls."],
        ["COMPLETE_WITH_LIMITATIONS", "Stored extraction is usable but an explicit transcript, description, or format limitation remains."],
        ["PARTIAL", "Some required extraction evidence exists; coverage is incomplete."],
        ["NOT_EXTRACTED", "Identity is verified, but channel video extraction has not started."],
        ["COMPLETE_REAL", "Every stored video has a real transcript."],
        ["COMPLETE_WITH_PLACEHOLDERS", "Every stored video has a transcript row, but one or more are explicit placeholders."],
        ["THUMBNAIL_URL_ONLY", "Thumbnail metadata URL exists; no downloaded thumbnail evidence is registered."],
        ["THUMBNAIL_EVIDENCE", "Downloaded thumbnail or screenshot evidence is registered."],
        ["FORENSIC_VIDEO_EVIDENCE", "Registered source video and timestamped/keyframe observations support editing analysis."],
        ["SCREENSHOT_ONLY_UNMAPPED", "Screenshot subject remains separate because no canonical YouTube channel identity is proven."],
        ["VALIDATED", "Generated capability artifact passed its documented validation scope."],
        ["AVAILABLE", "Generated capability artifact exists; validation is not universal."],
        ["PARTIAL", "Generated capability output exists with a material documented limitation."],
        ["DATA_READY", "Required input data or schema exists, but no channel-specific analysis artifact is generated."],
        ["NOT_AVAILABLE", "Required input or generated artifact is unavailable."],
        ["SCHEMA_READY_NO_DATA", "First-party ingestion schema is ready; no real YouTube Studio/Analytics export is ingested."],
        ["Public metrics", "Public views, likes, comments, and subscriber counts are not first-party YouTube Analytics."],
        ["Completion tick", "A check mark applies only to the specific availability column in which it appears."],
    ]
    add_table(definitions, ["Term", "Definition"], definitions_rows, "DefinitionsTable")

    dashboard = workbook["Dashboard"]
    title(dashboard, "YouTube channel registry dashboard", "Formula-linked controls. Each card measures one evidence layer.")
    dashboard.sheet_view.showGridLines = False
    left_labels = [
        "Canonical registry channels", "Target channels", "Channels with video data",
        "Standard package channels", "Historical-format channels", "Identity-only channels",
        "Full forensic visual channels",
    ]
    right_labels = [
        "Thumbnail-evidence intelligence channels", "Title-only packaging channels",
        "Unmapped screenshot subjects", "Stored unique videos", "Real transcripts",
        "Transcript placeholders", "Missing public descriptions",
    ]
    for offset, label in enumerate(left_labels):
        dashboard.cell(5 + offset, 1, label)
    for offset, label in enumerate(right_labels):
        dashboard.cell(5 + offset, 4, label)
    left_formulas = [
        f"=COUNTA('All Channels'!$A$5:$A${all_end})",
        f'=COUNTIFS(\'All Channels\'!$E$5:$E${all_end},"<>OUTSIDE_TARGET")',
        f'=COUNTIFS(\'All Channels\'!$H$5:$H${all_end},"✓")',
        f'=COUNTIFS(\'All Channels\'!$J$5:$J${all_end},"✓")',
        f'=COUNTIFS(\'All Channels\'!$K$5:$K${all_end},"✓")',
        f'=COUNTIFS(\'All Channels\'!$I$5:$I${all_end},"NOT_EXTRACTED")',
        f'=COUNTIFS(\'All Channels\'!$S$5:$S${all_end},"✓")',
    ]
    right_formulas = [
        f'=COUNTIFS(\'All Channels\'!$R$5:$R${all_end},"✓")',
        f'=COUNTIFS(\'All Channels\'!$K$5:$K${all_end},"✓",\'All Channels\'!$Q$5:$Q${all_end},"No")',
        f"=COUNTA('Visual Evidence'!$A${subject_first_row}:$A${subject_last_row})",
        f"=SUM('All Channels'!$L$5:$L${all_end})",
        f"=SUM('All Channels'!$M$5:$M${all_end})",
        f"=SUM('All Channels'!$N$5:$N${all_end})",
        f"=SUM('All Channels'!$O$5:$O${all_end})",
    ]
    for offset, formula in enumerate(left_formulas):
        dashboard.cell(5 + offset, 2, formula)
    for offset, formula in enumerate(right_formulas):
        dashboard.cell(5 + offset, 5, formula)
    dashboard.cell(14, 1, "Interpretation")
    dashboard.cell(15, 1, "Raw data availability is not the same as generated intelligence.")
    dashboard.cell(16, 1, "Public scraped metrics are not first-party YouTube Analytics.")

    return workbook


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    model = json.loads((root / "data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json").read_text(encoding="utf-8"))
    database_path = root / "data/catalog/youtube_channel_registry.db"
    output = args.output or root / "data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx"
    workbook = build_workbook(root, model, database_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output)
    print(json.dumps({"workbookPath": str(output), "sheets": len(workbook.sheetnames)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
