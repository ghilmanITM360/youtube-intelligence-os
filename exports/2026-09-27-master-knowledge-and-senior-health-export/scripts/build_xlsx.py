#!/usr/bin/env python3
"""Build YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.xlsx from master_data.json.
Read-only against repo source data; only writes the .xlsx in this export directory.
"""
import json
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

HERE = Path(__file__).resolve().parent.parent
DATA = json.loads((HERE / "master_data.json").read_text())
OUT = HERE / "YOUTUBE-KNOWLEDGE-AND-SENIOR-HEALTH-COMPLETE-DATA.xlsx"

FONT_NAME = "Calibri"
HEADER_FILL = PatternFill("solid", fgColor="1F4E5F")
HEADER_FONT = Font(name=FONT_NAME, bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(name=FONT_NAME, bold=True, size=16, color="1F4E5F")
SUBTITLE_FONT = Font(name=FONT_NAME, size=11, italic=True, color="555555")
BODY_FONT = Font(name=FONT_NAME, size=10)
WRAP = Alignment(wrap_text=True, vertical="top")

wb = Workbook()
wb.remove(wb.active)


def add_table_sheet(name, headers, rows, widths=None, wrap_cols=None, freeze="A2"):
    """rows: list of lists (already stringified/typed for cells)."""
    ws = wb.create_sheet(name[:31])
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    for r in rows:
        ws.append(r)
    for r in range(2, len(rows) + 2):
        for c in range(1, len(headers) + 1):
            ws.cell(row=r, column=c).font = BODY_FONT
            if wrap_cols and c in wrap_cols:
                ws.cell(row=r, column=c).alignment = WRAP
    ws.freeze_panes = freeze
    if rows:
        last_col = get_column_letter(len(headers))
        ref = f"A1:{last_col}{len(rows) + 1}"
        safe_name = "T" + "".join(ch for ch in name if ch.isalnum())[:28]
        tbl = Table(displayName=safe_name, ref=ref)
        tbl.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
        ws.add_table(tbl)
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    else:
        for i in range(1, len(headers) + 1):
            ws.column_dimensions[get_column_letter(i)].width = 22
    return ws


def truthy(v):
    return "" if v is None else v


# ---------------------------------------------------------------- 01_READ_ME
ws = wb.create_sheet("01_READ_ME")
ws.column_dimensions["A"].width = 110
lines = [
    ("YOUTUBE KNOWLEDGE & SENIOR HEALTH — COMPLETE DATA EXPORT", TITLE_FONT),
    ("Generated 2026-09-27 · branch research/senior-health-acquisition-phase-2 · read-only export, no source data modified", SUBTITLE_FONT),
    ("", BODY_FONT),
    ("WHAT THIS WORKBOOK IS", HEADER_FONT),
    ("A structured extraction of three global knowledge datasets (DS-000011, DS-000018, DS-000031) and the full Senior Health", BODY_FONT),
    ("channel/video inventory already registered in this repository's catalog, plus the user's own channel (Decode Your Heart -", BODY_FONT),
    ("Dr. Rehan, DS-000032). Every figure below was read directly from repo files at export time; where a figure could not be", BODY_FONT),
    ("verified on disk it is marked NOT_AVAILABLE rather than estimated.", BODY_FONT),
    ("", BODY_FONT),
    ("EVIDENCE-STATUS LABELS USED THROUGHOUT", HEADER_FONT),
    ("SOURCE_CLAIM / SOURCE_INTERPRETATION / SOURCE_RECOMMENDATION — DS-000018's own extraction-stage labels (what the source text asserts)", BODY_FONT),
    ("SUPPORTED / PARTIALLY_SUPPORTED / CONTRADICTED / NOT_SUPPORTED_BY_PRIMARY_EVIDENCE / NOT_CURRENTLY_VERIFIABLE — this project's later validation of DS-000018 claims against official YouTube sources", BODY_FONT),
    ("SOURCE_CONCEPT / SOURCE_HEURISTIC / SOURCE_FRAMEWORK / SOURCE_WORKFLOW / SOURCE_CLAIM / SOURCE_RECOMMENDATION / SOURCE_DIAGNOSTIC_RULE / SOURCE_SCORECARD / DERIVED_NORMALIZATION — DS-000031's own concept types", BODY_FONT),
    ("EXISTING_VERIFIED_MAPPING / EXISTING_HYPOTHESIS / SOURCE-BASED_OBSERVATION / NOT_YET_ANALYZED / INSUFFICIENT_EVIDENCE — knowledge-to-video mapping status (sheet 21)", BODY_FONT),
    ("ACQUIRED_DIRECT_COMPETITOR / QUALIFIED_PENDING_COMPETITOR / IDENTITY_ONLY / REMOVED_OR_UNVERIFIABLE / OWN_CHANNEL — channel classification (sheets 12-14, 22)", BODY_FONT),
    ("", BODY_FONT),
    ("WHAT IS DELIBERATELY NOT HERE (see supplemental-data-archive/ next to this workbook)", HEADER_FONT),
    ("Full transcript text is not pasted into this workbook — sheet 17 gives both the repo evidence_locator AND a portable path into", BODY_FONT),
    ("supplemental-data-archive/transcripts/<channel>/<video_id>.txt, where all 459 real transcript files are copied and self-contained.", BODY_FONT),
    ("Full DS-000018 tab text and DS-000011 source text are likewise archived (not pasted) — see supplemental-data-archive/ds-000018-full-tabs/ and /ds-000011-full-text/.", BODY_FONT),
    ("Private YouTube Studio analytics (impressions/CTR/retention/traffic-source/watch-time/revenue) — confirmed NOT INGESTED for every channel; never fabricated", BODY_FONT),
    ("Per-video topic/subtopic tags — no per-video classification exists in the repo; sheet 19 gives the cohort-level content-pillar taxonomy that does exist (6 pillars, not per-video)", BODY_FONT),
    ("Video-level historical snapshots — only one capture per video exists per channel acquisition run; sheet 16 documents this rather than inventing a time series", BODY_FONT),
    ("", BODY_FONT),
    ("SHEET INDEX", HEADER_FONT),
]
sheet_index = [
    "00_DASHBOARD - verified project/knowledge/channel coverage + charts",
    "02_DATASET_INVENTORY - DS-000011/018/031 manifest-level summary",
    "03_SOURCE_REGISTER - every original knowledge source (17+63+1 = 81 physical/logical sources), with per-tab claim counts",
    "04_ALL_KNOWLEDGE - unified index of all extracted knowledge units across 3 datasets (17 + 699 + 63 = 779)",
    "05_CREATIVE_KNOWLEDGE - DS-000011's 17 extracted rules",
    "05b_DS011_FULL_SOURCES - all 17 raw DS-000011 files with full original text archive paths",
    "06_CREATOR_CLAIMS - DS-000018's 699 claims (33 human-audited + 666 AI-extracted, all 63 tabs) + validation status",
    "07_STRATEGY_FRAMEWORKS - DS-000031's 63 concepts, each with its original source-segment excerpt",
    "08_FORMULAS - DS-000031's 15 source formulas + 12 numeric heuristics",
    "09_EXAMPLES - DS-000031's 9 example groups",
    "10_KNOWLEDGE_LINKS - DS-000031's 15 segment-level relationships",
    "11_CONTRADICTIONS - documented disagreements within/across datasets",
    "12_ALL_CHANNELS - all 69 known Senior Health leads",
    "13_ACQUIRED_CHANNELS - the 8 channels with complete standard packages",
    "14_PENDING_CHANNELS - 14 qualified-pending + 34 identity-only + 13 removed",
    "15_ALL_VIDEOS - all 460 video master records incl. descriptions + recovered thumbnail URLs",
    "16_VIDEO_SNAPSHOTS - historical snapshot policy (single capture per video)",
    "17_TRANSCRIPT_INDEX - 459 real transcript references, each with a self-contained archive path",
    "18_THUMBNAIL_INDEX - thumbnail URL coverage (459/460 recovered) + downloaded image archive paths (61/460)",
    "19_TOPICS - 6 cohort-level content pillars (not per-video)",
    "20_RESEARCH_COVERAGE - which channels have dedicated forensic analysis",
    "21_KNOWLEDGE_VIDEO_MAP - 57 existing knowledge-to-video mapping records",
    "22_OWN_CHANNEL - Dr. Rehan channel record",
    "23_OWN_CHANNEL_VIDEOS - Dr. Rehan's 56 videos incl. descriptions + thumbnails",
    "24_DATA_GAPS - every known gap/limitation",
    "25_SOURCE_TRACEABILITY - Phase-12 reconciliation matrix incl. the 2026-09-27 correction pass",
    "26_DATA_DICTIONARY - field definitions",
]
r = 1
for text, font in lines:
    ws.cell(row=r, column=1, value=text).font = font
    r += 1
for s in sheet_index:
    ws.cell(row=r, column=1, value="  " + s).font = BODY_FONT
    r += 1

# ---------------------------------------------------------- 02_DATASET_INVENTORY
rows = [
    ["DS-000011", "All Training Data of YouTube - Global Knowledge Corpus", "17", "16", "17 rules + 17 full-text sources archived", "PDF/DOCX/Markdown guides", "COPY, INGESTED", "2026-08-27"],
    ["DS-000018", "2026 Algorithm Update - Multi-Tab Creator Research Corpus", "63", "61", "699 (33 human-audited + 666 AI-extracted, 63/63 tabs atomized)", "Google Docs multi-tab ZIP snapshot", "STRUCTURED_REGISTERED", "2026-09-02"],
    ["DS-000031", "Creator Strategy, Audience Psychology & Experimentation Frameworks Corpus", "1 (70,730-byte corpus)", "1", "63 concepts / 15 formulas / 9 examples, 15/15 segments full-text archived", "Mixed Urdu/Roman-Urdu/English text file", "INGESTED, VERIFIED", "2026-09-24"],
]
add_table_sheet("02_DATASET_INVENTORY",
    ["Dataset ID", "Name", "Raw Source Count", "Unique Sources", "Extracted Knowledge Units", "Source Type", "Status", "Registered"],
    rows, widths=[12, 45, 16, 12, 24, 30, 20, 14])

# ---------------------------------------------------------- 03_SOURCE_REGISTER
import re as _re
additional_claims_by_tab = {}
for c in DATA["DS-000018"]["additional_claims"]:
    additional_claims_by_tab.setdefault(c.get("tab_file"), 0)
    additional_claims_by_tab[c.get("tab_file")] += 1
original_claims_by_tab_index = {}
for c in DATA["DS-000018"]["claims"]:
    m = _re.search(r"T(\d+)", c.get("Exact locator", ""))
    if m:
        idx = int(m.group(1))
        original_claims_by_tab_index[idx] = original_claims_by_tab_index.get(idx, 0) + 1

rows = []
for d in DATA["DS-000011"]["source_documents"]:
    rows.append(["DS-000011", d.get("document_id", ""), d.get("title", ""), d.get("document_type", ""),
                 d.get("evidence_type", ""), d.get("authorship", "UNKNOWN"), "UNKNOWN"])
for t in DATA["DS-000018"]["tabs"]:
    fname = Path(t["snapshot_member"]).name
    n_claims = additional_claims_by_tab.get(fname, 0) + original_claims_by_tab_index.get(t["index"], 0)
    rows.append(["DS-000018", f"T{t['index']:02d}", t.get("title", ""), "Google Doc tab (video transcript/script)",
                 "SOURCE_EXTRACTED", "Third-party YouTube creator/video",
                 f"{t.get('word_count', '')}w / {n_claims} claims / full text archived"])
rows.append(["DS-000031", "SRC-CORPUS-001", "Creator Strategy, Audience Psychology & Experimentation Corpus",
             "Mixed-language text file", "SOURCE_EXTRACTED", "UNKNOWN (user-supplied)", "70,730 bytes / full text archived"])
add_table_sheet("03_SOURCE_REGISTER",
    ["Dataset", "Source ID", "Title", "Type", "Evidence Type", "Author/Origin", "Word Count / Coverage"],
    rows, widths=[12, 14, 55, 30, 18, 30, 30], wrap_cols=[3])

# ---------------------------------------------------------- 04_ALL_KNOWLEDGE (unified, 113 rows)
rows = []
for r_ in DATA["DS-000011"]["knowledge_rules"]:
    rows.append(["DS-000011", r_.get("RULE_ID", ""), "RULE", r_.get("RULE_TEXT", "")[:200],
                 r_.get("SOURCE_LOCATOR", ""), r_.get("PRIMARY_VALIDATION_STATUS", "")])
for c in DATA["DS-000018"]["claims"]:
    text = c.get("Concise source claim") or c.get("Concise source interpretation") or c.get("Concise source recommendation", "")
    rows.append(["DS-000018", c.get("Claim ID", ""), c.get("assertion_type", ""), text[:200],
                 c.get("Exact locator", ""), c.get("prior_status_at_validation", "")])
for c in DATA["DS-000018"]["additional_claims"]:
    rows.append(["DS-000018", c.get("tab_file", ""), c.get("assertion_type", ""), c.get("claim_text", "")[:200],
                 c.get("approx_location", ""), c.get("prior_status_at_validation", "NOT_CURRENTLY_VERIFIABLE")])
for c in DATA["DS-000031"]["concepts"]:
    rows.append(["DS-000031", c.get("id", ""), c.get("type", ""), c.get("summary", c.get("name", ""))[:200],
                 ", ".join(c.get("segments", [])), c.get("status", "")])
add_table_sheet("04_ALL_KNOWLEDGE",
    ["Dataset", "Knowledge Unit ID", "Unit Type", "Text (truncated 200ch, full text on dataset-specific sheet)", "Source Locator", "Validation/Status"],
    rows, widths=[12, 18, 22, 70, 22, 30], wrap_cols=[4])

# ---------------------------------------------------------- 05_CREATIVE_KNOWLEDGE (DS-000011)
# Correction: the RULE_TEXT below is an AI-synthesized summary of its source document
# (SOURCE_QUALITY already discloses this). The full original text of every one of the 17
# source files (PDFs/DOCX/MD) is now recovered and archived — see the archive path column.
rows = []
for r_ in DATA["DS-000011"]["knowledge_rules"]:
    rows.append([r_.get("RULE_ID", ""), r_.get("DOMAIN", ""), r_.get("RULE_TYPE", ""), r_.get("RULE_TEXT", ""),
                 r_.get("SOURCE_LOCATOR", ""), r_.get("SOURCE_QUALITY", ""), r_.get("PRIMARY_VALIDATION_STATUS", ""),
                 r_.get("CONFIDENCE", ""), r_.get("PROHIBITED_USE", "")])
add_table_sheet("05_CREATIVE_KNOWLEDGE",
    ["Rule ID", "Domain", "Rule Type", "Rule Text", "Source Locator", "Source Quality", "Validation Status", "Confidence", "Prohibited Use"],
    rows, widths=[14, 16, 16, 60, 20, 16, 22, 12, 40], wrap_cols=[4, 9])

# --------------------------------------------------- 05b_DS011_FULL_SOURCES (17 raw files, full text)
rows = []
for s in DATA["DS-000011"]["fulltext_sources"]:
    archive_path = f"supplemental-data-archive/ds-000011-full-text/{s['filename']}.txt" if s.get("full_text") else ""
    rows.append([s["filename"], s["sha256"][:16], s["byte_size"], s.get("full_text_char_count", 0),
                 s.get("duplicate_of") or "", s["extraction_status"], archive_path])
add_table_sheet("05b_DS011_FULL_SOURCES",
    ["Filename", "SHA256 (16ch)", "Byte Size", "Extracted Text Chars", "Duplicate Of", "Extraction Status", "Full Text Archive Path"],
    rows, widths=[55, 18, 12, 18, 40, 20, 60], wrap_cols=[1, 7])

# ---------------------------------------------------------- 06_CREATOR_CLAIMS (DS-000018)
# BUG FIX (2026-09-27 correction): "Validated Status" previously received citation reference
# codes (e.g. "[R1], [R2]") from the wrong source field. "Validated Status" below is now the
# actual prior-audit status (SUPPORTED/PARTIALLY_SUPPORTED/etc); citation codes moved to their
# own "Evidence Citation Codes" column. Also now includes the 56-tab AI-extracted claims
# (previously only 7 of 63 tabs were claim-atomized) with an "Extraction Method" column so the
# original human-audited 33 stay distinguishable from the newly-added, not-yet-validated ones.
rows = []
for c in DATA["DS-000018"]["claims"]:
    rows.append([c.get("Claim ID", ""), c.get("assertion_type", ""), c.get("Theme", ""),
                 c.get("Concise source claim") or c.get("Concise source interpretation") or c.get("Concise source recommendation", ""),
                 c.get("Exact locator", ""), c.get("Verification / ambiguity", ""),
                 c.get("prior_status_at_validation", "NOT_VALIDATED_AT_CLAIM_LEVEL"),
                 c.get("evidence_citation_codes", ""), c.get("extraction_method", "")])
for c in DATA["DS-000018"]["additional_claims"]:
    rows.append([f"{c.get('tab_file','')}#{c.get('theme','')[:20]}", c.get("assertion_type", ""), c.get("theme", ""),
                 c.get("claim_text", ""), c.get("approx_location", ""),
                 c.get("quote", "") + (f" | qualifications: {c['qualifications_or_limitations']}" if c.get("qualifications_or_limitations") else ""),
                 c.get("prior_status_at_validation", "NOT_CURRENTLY_VERIFIABLE"),
                 c.get("numerical_assertion") or "", c.get("extraction_method", "")])
add_table_sheet("06_CREATOR_CLAIMS",
    ["Claim ID", "Assertion Type", "Theme", "Claim Text", "Source Locator (Tab, Timestamp)", "Verification/Ambiguity/Quote", "Validated Status", "Evidence Citation Codes / Numerical Assertion", "Extraction Method"],
    rows, widths=[24, 20, 24, 60, 24, 50, 26, 30, 34], wrap_cols=[4, 6, 8])

# ---------------------------------------------------------- 07_STRATEGY_FRAMEWORKS (DS-000031 concepts)
# Correction: "Summary" alone was a one-sentence AI paraphrase. "Original Segment Excerpt" now
# carries the actual original source text (truncated to 600 chars here; the full segment text
# is archived at supplemental-data-archive/ds-000031-source/ and sheet 07b has per-segment text).
rows = []
for c in DATA["DS-000031"]["concepts"]:
    excerpt = " | ".join(t.strip()[:600] for t in c.get("source_segment_full_text", {}).values() if t.strip())
    rows.append([c.get("id", ""), c.get("name", ""), c.get("type", ""), ", ".join(c.get("domains", [])),
                 ", ".join(c.get("segments", [])), c.get("summary", ""), excerpt, c.get("status", ""), c.get("use", "")])
add_table_sheet("07_STRATEGY_FRAMEWORKS",
    ["Concept ID", "Name", "Type", "Domains", "Segments", "AI Summary", "Original Segment Excerpt (source text)", "Status", "Use"],
    rows, widths=[10, 40, 26, 24, 16, 55, 90, 32, 26], wrap_cols=[6, 7])

# --------------------------------------------------- 07b_DS031_FULL_SEGMENTS (15 segments, full text)
rows = []
for s in DATA["DS-000031"]["segments"]:
    rows.append([s["id"], s.get("title", ""), s.get("kind", ""), f"{s['lines'][0]}-{s['lines'][1]}",
                 s.get("full_text_char_count", 0), "supplemental-data-archive/ds-000031-source/creator-strategy-audience-psychology-experimentation-corpus.txt",
                 s.get("full_text", "")])
add_table_sheet("07b_DS031_FULL_SEGMENTS",
    ["Segment ID", "Title", "Kind", "Line Range", "Char Count", "Source Archive Path", "Full Original Text"],
    rows, widths=[12, 40, 22, 14, 12, 75, 100], wrap_cols=[2, 7])

# ---------------------------------------------------------- 08_FORMULAS
rows = []
for f in DATA["DS-000031"]["formulas"]:
    rows.append(["FORMULA", f.get("id", ""), f.get("text", ""), f.get("concept", ""), f.get("type", ""), f.get("line", "")])
for h in DATA["DS-000031"]["numeric_heuristics"]:
    rows.append(["NUMERIC_HEURISTIC", h.get("id", ""), h.get("text", h.get("summary", "")), h.get("concept", ""), h.get("type", ""), h.get("line", "")])
add_table_sheet("08_FORMULAS",
    ["Kind", "ID", "Text", "Related Concept", "Type", "Source Line"],
    rows, widths=[18, 10, 70, 16, 20, 10], wrap_cols=[3])

# ---------------------------------------------------------- 09_EXAMPLES
rows = []
for e in DATA["DS-000031"]["examples"]:
    rows.append([e.get("id", ""), e.get("concept", ""), e.get("segment", ""), e.get("subject", ""), e.get("role", "")])
add_table_sheet("09_EXAMPLES", ["Example ID", "Related Concept", "Segment", "Subject", "Role/Illustrates"], rows,
    widths=[12, 16, 12, 30, 60], wrap_cols=[5])

# ---------------------------------------------------------- 10_KNOWLEDGE_LINKS
rows = []
for rel in DATA["DS-000031"]["relationships"]:
    if isinstance(rel, dict):
        rows.append([rel.get("segment", ""), json.dumps(rel, ensure_ascii=False)[:500]])
add_table_sheet("10_KNOWLEDGE_LINKS", ["Segment", "Relationship Record (raw)"], rows, widths=[14, 100], wrap_cols=[2])

# ---------------------------------------------------------- 11_CONTRADICTIONS
rows = [
    ["DS-000018 internal", "ALG26-CLM-018", "ALG26-CLM-005",
     "T01 creator claims Shorts and long-form use separate algorithms/audiences and should never share a channel; T39 (platform-attributed) describes viewer-specific coexistence when audience overlap exists.",
     "Both retained; not merged into one rule."],
    ["DS-000018 validation", "ALG26-CLM series", "primary validation pass",
     "Of 33 extracted claims, 1 was found CONTRADICTED and 8 NOT_SUPPORTED_BY_PRIMARY_EVIDENCE against official YouTube sources at the 2026-09-04 validation pass.",
     "See sheet 06 'Validated Status' column for the specific claim IDs."],
]
add_table_sheet("11_CONTRADICTIONS", ["Scope", "Item A", "Item B", "Nature of Disagreement", "Resolution/Status"], rows,
    widths=[20, 18, 18, 70, 40], wrap_cols=[4])

# ---------------------------------------------------------- 12_ALL_CHANNELS (69 leads)
rows = []
for c in DATA["senior_health_master_inventory"]["channels"]:
    rows.append([c.get("canonical_channel_id", ""), c.get("verified_name", c.get("recorded_name", "")), c.get("current_handle", ""),
                 c.get("canonical_url", ""), c.get("class", ""), c.get("senior_health_relevance", ""), c.get("live_status", ""),
                 c.get("subscribers", ""), c.get("header_videos", ""), c.get("live_regular", ""), c.get("live_shorts", ""),
                 c.get("live_streams", ""), c.get("registry_status", ""), c.get("package_status", ""),
                 ", ".join(c.get("dataset_ids", []) or []), c.get("repo_real_transcripts", ""), c.get("est_cost_usd", "")])
add_table_sheet("12_ALL_CHANNELS",
    ["Canonical ID", "Channel Name", "Handle", "URL", "Class", "Relevance", "Live Status", "Subscribers",
     "Header Videos", "Regular", "Shorts", "Streams", "Registry Status", "Package Status", "Dataset IDs",
     "Real Transcripts On File", "Est. Acquisition Cost USD"],
    rows, widths=[24, 32, 22, 42, 8, 20, 10, 12, 12, 10, 10, 10, 22, 18, 14, 18, 18])

# ------------------------------------------------------ 13_ACQUIRED_CHANNELS / 14_PENDING
acquired_ids = set(DATA["senior_health_channels"] and [c["canonical_channel_id"] for c in DATA["senior_health_channels"]])
rows = []
for c in DATA["senior_health_channels"]:
    videos = DATA["senior_health_videos_by_channel"][c["canonical_channel_id"]]
    real_t = sum(1 for v in videos for t in v["transcripts"] if not t["is_placeholder"])
    rows.append([c["canonical_channel_id"], c["channel_name"], c["current_handle"], c["canonical_url"],
                 c["classification"], c["status"], c["package_status"], c["video_metadata_status"],
                 c["transcript_status"], len(videos), real_t, c["thumbnail_metadata_status"],
                 c["visual_asset_status"], c["forensic_video_status"], c["intelligence_status"],
                 c["first_party_analytics_status"], c["limitations"] or ""])
add_table_sheet("13_ACQUIRED_CHANNELS",
    ["Canonical ID", "Channel Name", "Handle", "URL", "Classification", "Status", "Package Status",
     "Video Metadata", "Transcript Status", "Videos On File", "Real Transcripts", "Thumbnail Coverage",
     "Visual Asset Status", "Forensic Video Status", "Intelligence Status", "1st-Party Analytics", "Limitations"],
    rows, widths=[24, 30, 22, 42, 24, 22, 18, 16, 22, 12, 12, 18, 22, 20, 18, 20, 40], wrap_cols=[17])

pending_rows = [c for c in DATA["senior_health_master_inventory"]["channels"] if c.get("class") in ("E", "F")]
rows = []
for c in pending_rows:
    status = "IDENTITY_ONLY_OR_QUALIFIED_PENDING" if c["class"] == "E" else "REMOVED_OR_UNVERIFIABLE"
    rows.append([c.get("canonical_channel_id", c.get("ref", "")), c.get("verified_name", c.get("recorded_name", "")),
                 c.get("current_handle", ""), status, c.get("header_videos", ""), c.get("subscribers", ""),
                 c.get("live_status", ""), c.get("est_cost_usd", "")])
add_table_sheet("14_PENDING_CHANNELS",
    ["Canonical ID / Ref", "Channel Name", "Handle", "Classification", "Videos (observed)", "Subscribers", "Live Status", "Est. Cost USD"],
    rows, widths=[24, 32, 22, 32, 16, 14, 12, 14])

# ---------------------------------------------------------- 15_ALL_VIDEOS
rows = []
for cid, videos in DATA["senior_health_videos_by_channel"].items():
    cname = next(c["channel_name"] for c in DATA["senior_health_channels"] if c["canonical_channel_id"] == cid)
    is_own = cid == "UCQIzqH7QZ9viBYpOFqgSXMg"
    for v in videos:
        real_t = [t for t in v["transcripts"] if not t["is_placeholder"]]
        rows.append([
            cid, cname, "OWN_CHANNEL" if is_own else "COMPETITOR", v["youtube_video_id"], v["canonical_url"],
            v["title"], v.get("description") or "", v.get("description_unavailable_reason") or ("AVAILABLE" if v.get("description") else ""),
            v["published_at"], v["duration_seconds"], v["video_type"], v["views"], v["likes"],
            v["comments"], v.get("thumbnail_url") or "", v.get("thumbnail_url_source", ""),
            v.get("downloaded_thumbnail_local_path") or "",
            "YES" if real_t else "NO", real_t[0]["word_count"] if real_t else "",
            "NOT_YET_CLASSIFIED",
        ])
add_table_sheet("15_ALL_VIDEOS",
    ["Canonical Channel ID", "Channel Name", "Own/Competitor", "Video ID", "URL", "Title", "Description",
     "Description Status", "Published At", "Duration (s)", "Type", "Views", "Likes", "Comments", "Thumbnail URL",
     "Thumbnail Source", "Downloaded Thumbnail Path", "Real Transcript?", "Transcript Word Count", "Topic/Subtopic"],
    rows, widths=[24, 26, 14, 14, 42, 50, 70, 20, 22, 12, 10, 10, 8, 10, 46, 26, 46, 14, 18, 18], wrap_cols=[6, 7])

# ---------------------------------------------------------- 16_VIDEO_SNAPSHOTS
rows = [["ALL 8 CHANNELS", "Single capture per video (initial acquisition run)",
         "No repeated re-scrape / historical time-series metric exists in this repo for any Senior Health video. "
         "Views/likes/comments in sheet 15 are a one-time snapshot at acquisition time, not a cumulative-vs-interval "
         "distinction. Do not read a rising view count across sheets as a tracked delta - only one observation exists per video."]]
add_table_sheet("16_VIDEO_SNAPSHOTS", ["Scope", "Snapshot Policy", "Note"], rows, widths=[20, 40, 100], wrap_cols=[3])

# ---------------------------------------------------------- 17_TRANSCRIPT_INDEX
CHANNEL_SLUG = {
    "UCFpxvukIqCAUA7YizI-q9Dw": "better-health-while-aging", "UCQIzqH7QZ9viBYpOFqgSXMg": "own-channel-dr-rehan",
    "UCFuGMi0idGeyXl6wYK9hg7Q": "doctor-thomas", "UCMJxAeBJ0d1JC937de1eZ0Q": "dr-okoro",
    "UC356D-NzdnznBOftTpYoBLw": "dr-ares-senior", "UCQcBYZxFW7YwNMU8-DsT3Uw": "dr-elias-senior-health",
    "UCAYG0fzUyxv6OevH88qA45w": "senior-health-hub", "UCXZi5JVeuTluazF-fYqQgNA": "dr-aliza-wright",
}
rows = []
for cid, videos in DATA["senior_health_videos_by_channel"].items():
    cname = next(c["channel_name"] for c in DATA["senior_health_channels"] if c["canonical_channel_id"] == cid)
    slug = CHANNEL_SLUG[cid]
    for v in videos:
        if v["transcripts"]:
            for t in v["transcripts"]:
                archive_path = f"supplemental-data-archive/transcripts/{slug}/{v['youtube_video_id']}.txt" if not t["is_placeholder"] else ""
                rows.append([cid, cname, v["youtube_video_id"], v["title"], t["dataset_id"],
                             "PLACEHOLDER" if t["is_placeholder"] else "REAL", t["word_count"], t["language"],
                             t["caption_type"], t["unavailable_reason"] or "", t["evidence_locator"], archive_path])
        else:
            rows.append([cid, cname, v["youtube_video_id"], v["title"], "", "MISSING", "", "", "", "No transcript record", "", ""])
add_table_sheet("17_TRANSCRIPT_INDEX",
    ["Canonical Channel ID", "Channel Name", "Video ID", "Title", "Dataset ID", "Availability", "Word Count",
     "Language", "Caption Type", "Unavailable Reason", "Repo Evidence Locator", "Self-Contained Archive Path"],
    rows, widths=[24, 26, 14, 50, 12, 14, 12, 10, 16, 26, 60, 55], wrap_cols=[4, 11, 12])

# ---------------------------------------------------------- 18_THUMBNAIL_INDEX
# Correction: thumbnail_url is now recovered from raw acquisition source files wherever the
# database column was empty (459/460); "Downloaded Image Archive Path" is populated for the
# 61 videos (Dr. Aliza Wright 32/32, Dr. Elias 29/66) whose actual thumbnail image bytes were
# already fetched to disk in a prior forensic snapshot run and are now copied into the
# self-contained supplemental archive alongside this workbook.
rows = []
for c in DATA["senior_health_channels"]:
    cid = c["canonical_channel_id"]
    slug = CHANNEL_SLUG[cid]
    videos = DATA["senior_health_videos_by_channel"][cid]
    for v in videos:
        dl_path = ""
        if v.get("downloaded_thumbnail_local_path"):
            ext = v["downloaded_thumbnail_local_path"].rsplit(".", 1)[-1]
            dl_path = f"supplemental-data-archive/downloaded-thumbnails/{slug}/{v['youtube_video_id']}.{ext}"
        rows.append([cid, c["channel_name"], v["youtube_video_id"], v.get("thumbnail_url") or "",
                     v.get("thumbnail_url_source", ""), dl_path])
add_table_sheet("18_THUMBNAIL_INDEX",
    ["Canonical Channel ID", "Channel Name", "Video ID", "Thumbnail URL", "URL Source", "Downloaded Image Archive Path"],
    rows, widths=[24, 26, 14, 60, 32, 55], wrap_cols=[4])

# ---------------------------------------------------------- 19_TOPICS
import json as _json
pillars = _json.loads((HERE.parents[1] / "docs/research/senior-health-2026-09-25/06-content-pillars.json").read_text())
rows = []
for p in pillars:
    rows.append([p.get("pillar", ""), p.get("audience_desire", ""), p.get("evidence", ""), p.get("trend_evidence", ""),
                 p.get("psychology", ""), ", ".join(p.get("formats", []))])
ws19 = add_table_sheet("19_TOPICS",
    ["Content Pillar", "Audience Desire", "Evidence", "Trend Evidence", "Psychology", "Common Formats"],
    rows, widths=[30, 34, 60, 46, 40, 40], wrap_cols=[3, 4])
ws19.cell(row=len(rows) + 3, column=1,
    value="NOTE: this is a cohort-level content-pillar taxonomy from cross-channel forensic research, NOT a per-video topic tag. "
          "No per-video Topic/Subtopic classification exists in the repository for these 460 videos (see sheet 15, 'Topic/Subtopic' column = NOT_YET_CLASSIFIED).").font = BODY_FONT

# ---------------------------------------------------------- 20_RESEARCH_COVERAGE
coverage = {
    "Better Health While Aging": "DEDICATED_CHANNEL_DOSSIER (BETTER-HEALTH-WHILE-AGING-CHANNEL-DOSSIER.md)",
    "Dr. Aliza Wright | Advice": "CASE_STUDY_MENTION (SENIOR-HEALTH-CASE-STUDIES.md, forensic-v2 matched-pairs)",
    "Dr. Ares Senior": "CASE_STUDY_MENTION + TRACE_MATRIX video evidence",
    "Dr. Okoro": "CASE_STUDY_MENTION + TRACE_MATRIX video evidence",
    "Senior Health Hub": "CASE_STUDY_MENTION",
    "Doctor Thomas": "COHORT_LEVEL_ONLY (appears in master video table / content pillars, no dedicated profile)",
    "Dr. Elias Senior Health": "COHORT_LEVEL_ONLY (appears in master video table / content pillars, no dedicated profile)",
    "Decode Your Heart - Dr. Rehan": "OWN_CHANNEL_NO_COMPETITIVE_ANALYSIS (not benchmarked as a competitor per project rules)",
}
rows = [[k, v] for k, v in coverage.items()]
add_table_sheet("20_RESEARCH_COVERAGE", ["Channel", "Existing Individual Research Coverage"], rows, widths=[32, 90], wrap_cols=[2])

# ---------------------------------------------------------- 21_KNOWLEDGE_VIDEO_MAP
rows = []
for m in DATA["knowledge_video_mappings"]["DS-000011_trace_matrix"]:
    rows.append(["DS-000011", m.get("knowledge_unit", ""), m.get("framework", ""), m.get("videos_tested_against", ""),
                 m.get("observed_evidence", ""), m.get("counterexample", ""), "EXISTING_HYPOTHESIS" if "SUPPORTED_AS" in m.get("result", "") else m.get("result", "")])
for m in DATA["knowledge_video_mappings"]["DS-000018_claim_matrix"]:
    rows.append(["DS-000018", m.get("claim_id", ""), m.get("claim", ""), "", m.get("internal_senior_health_evidence", ""),
                 m.get("counterexample", ""), m.get("claim_status", "")])
for m in DATA["knowledge_video_mappings"]["DS-000031_framework_matrix"]:
    rows.append(["DS-000031", m.get("concept_ids", ""), m.get("framework", ""), "", m.get("internal_supporting_example", ""),
                 m.get("internal_counterexample", ""), "SOURCE-BASED_OBSERVATION"])
add_table_sheet("21_KNOWLEDGE_VIDEO_MAP",
    ["Dataset", "Knowledge Item ID(s)", "Framework/Claim", "Video(s) Referenced", "Supporting Evidence", "Contradictory/Counter Evidence", "Status"],
    rows, widths=[12, 20, 40, 30, 60, 50, 26], wrap_cols=[3, 4, 5, 6])

# ---------------------------------------------------------- 22_OWN_CHANNEL / 23_OWN_CHANNEL_VIDEOS
own = next(c for c in DATA["senior_health_channels"] if c["canonical_channel_id"] == "UCQIzqH7QZ9viBYpOFqgSXMg")
own_videos = DATA["senior_health_videos_by_channel"]["UCQIzqH7QZ9viBYpOFqgSXMg"]
regular = sum(1 for v in own_videos if v["video_type"] == "video")
shorts = sum(1 for v in own_videos if v["video_type"] == "shorts")
real_t = sum(1 for v in own_videos for t in v["transcripts"] if not t["is_placeholder"])
rows = [["Canonical Channel ID", own["canonical_channel_id"]], ["Channel Name", own["channel_name"]],
        ["Handle", own["current_handle"]], ["URL", own["canonical_url"]], ["Classification", "OWN_CHANNEL (not a competitor)"],
        ["Dataset ID", "DS-000032"], ["Videos on file", len(own_videos)], ["Regular videos", regular], ["Shorts", shorts],
        ["Real transcripts", real_t], ["Status", own["status"]], ["Package status", own["package_status"]],
        ["1st-party (Studio) analytics", own["first_party_analytics_status"] + " - not fabricated, no real export ingested"],
        ["Limitations", own["limitations"] or "None recorded"]]
add_table_sheet("22_OWN_CHANNEL", ["Field", "Value"], rows, widths=[30, 90], wrap_cols=[2])

rows = []
for v in own_videos:
    real = [t for t in v["transcripts"] if not t["is_placeholder"]]
    rows.append([v["youtube_video_id"], v["canonical_url"], v["title"], v.get("description") or "",
                 v["published_at"], v["duration_seconds"], v["video_type"], v["views"], v["likes"], v["comments"],
                 v.get("thumbnail_url") or "", v.get("thumbnail_url_source", ""),
                 "YES" if real else "NO", real[0]["word_count"] if real else ""])
add_table_sheet("23_OWN_CHANNEL_VIDEOS",
    ["Video ID", "URL", "Title", "Description", "Published At", "Duration (s)", "Type", "Views", "Likes", "Comments",
     "Thumbnail URL", "Thumbnail Source", "Real Transcript?", "Word Count"],
    rows, widths=[14, 42, 55, 70, 22, 12, 10, 10, 8, 10, 46, 26, 14, 12], wrap_cols=[3, 4])

# ---------------------------------------------------------- 24_DATA_GAPS
rows = [
    ["Doctor Thomas", "1 of 22 transcripts is a disclosed placeholder, not a real transcript", "transcript_status=COMPLETE_WITH_LIMITATIONS in registry"],
    ["All 8 acquired channels", "No first-party YouTube Studio analytics ingested (impressions/CTR/retention/traffic-source/watch-time/revenue all NOT_AVAILABLE)", "first-party-analytics-capability-status-2026-09-11.json: REAL_FIRST_PARTY_DATA_INGESTED=false"],
    ["All 460 videos", "No per-video topic/subtopic classification exists; only a 6-item cohort-level content-pillar taxonomy exists", "06-content-pillars.json is cohort-level, not per-video"],
    ["1 of 460 videos (BHWA 'DO THIS: 4 Types of Exercise in Aging', x0Z5ziQNtWQ)", "Thumbnail URL genuinely absent from every raw acquisition source checked (DB column + 3 raw Apify files) - not recovered, not fabricated", "sheet 18_THUMBNAIL_INDEX row for x0Z5ziQNtWQ"],
    ["399 of 460 videos", "Thumbnail URL recovered but no downloaded image bytes on disk - only Dr. Aliza Wright (32/32) and Dr. Elias (29/66) have actual downloaded thumbnail images from a prior forensic snapshot run", "sheet 18_THUMBNAIL_INDEX 'Downloaded Image Archive Path' column"],
    ["37 of 66 Dr. Elias videos", "Source acquisition (DrElias_Master_Data.xlsx) captured only 29 of the channel's 66 registered videos in full detail (description/thumbnail/transcript); the other 37 have DB metadata but no richer raw source file found", "data/raw/competitors/DS-000019/DrElias_Master_Data.xlsx header states '29 videos, 29 descriptions, 29 transcripts'"],
    ["All 460 videos", "Editing/Visual forensic intelligence NOT_AVAILABLE - the only channel with forensic video evidence registered project-wide is an unrelated channel (xkcd's What If?, not Senior Health)", "channels.forensic_video_status column"],
    ["Doctor Thomas, Dr. Elias Senior Health", "No dedicated channel dossier or case study exists (cohort-table mentions only)", "sheet 20_RESEARCH_COVERAGE"],
    ["61 of 69 known Senior Health leads", "Only 8 are fully acquired; 14 qualified-pending + 34 identity-only + 13 removed remain unacquired (no paid Apify run performed for this export, per Core Rule / task instruction)", "SENIOR-HEALTH-MASTER-INVENTORY-REPORT.md"],
    ["DS-000018 additional 666 claims (56 tabs)", "Extracted by AI grounded read-through of full source text, NOT by the human validation pass the original 33 claims went through; status is NOT_CURRENTLY_VERIFIABLE until a human audit reviews them", "sheet 06_CREATOR_CLAIMS 'Extraction Method' column"],
    ["Knowledge-to-video mapping", "57 existing mapping records found (13 DS-000011 + 33 DS-000018 + 11 DS-000031); this is not exhaustive - many concepts/claims have no video-level mapping yet (NOT_YET_ANALYZED)", "forensic-v2/*-MATRIX.json files"],
]
add_table_sheet("24_DATA_GAPS", ["Scope", "Gap/Limitation", "Evidence Reference"], rows, widths=[30, 90, 50], wrap_cols=[2, 3])

# ---------------------------------------------------------- 25_SOURCE_TRACEABILITY
recon = DATA["reconciliation"]
rows = [
    ["DS-000011", "Prior audit: 17 files / 16 unique", f"Observed: {recon['DS-000011']['observed_files']} files / {recon['DS-000011']['observed_rules']} knowledge rules / {recon['DS-000011']['fulltext_unique_sources']} full-text sources recovered", "NO DRIFT" if not recon["DS-000011"]["drift"] else "DRIFT DETECTED"],
    ["DS-000018 (2026-09-27 correction)", "2026-09-27 finding: only 33 claims existed, atomized from 7 of 63 tabs; 56 tabs had metadata only",
     f"Observed: {recon['DS-000018']['observed_tabs']} tabs, all with full text recovered; {recon['DS-000018']['tabs_claim_atomized']}/63 tabs now claim-atomized ({recon['DS-000018']['original_human_audited_claims']} original human-audited + {recon['DS-000018']['additional_ai_extracted_claims']} additional AI-extracted-unvalidated = {recon['DS-000018']['all_claims_combined']} total claims)",
     "GAP CLOSED: 56/56 previously-unprocessed tabs now claim-atomized (AI-extracted, not yet human-validated - see sheet 06 Extraction Method column)"],
    ["DS-000031", f"Prior audit: {recon['DS-000031']['prior_audit']}", f"Observed: {recon['DS-000031']['observed']}; {recon['DS-000031']['segments_with_fulltext_recovered']}/15 segments now carry full original source text (not just a 1-sentence summary)", "NO DRIFT" if not recon["DS-000031"]["drift"] else "DRIFT DETECTED"],
    ["Senior Health channels", "Old baseline (task prompt): 7 acquired competitors + 98 BHWA + 56 Dr Rehan",
     f"Observed: {recon['senior_health']['acquired_channels_incl_own']} channels acquired (7 competitors + 1 own) / {recon['senior_health']['total_unique_video_records']} total videos / {recon['senior_health']['total_real_transcripts']} real transcripts",
     "MATCHES on BHWA(98)/Dr.Rehan(56); old '7 competitors' excluded own channel, now counted separately"],
    ["Senior Health leads", "Old baseline: ~69 leads, later '14 qualified pending' (task prompt said 19-vs-14 reconciliation)",
     f"Observed: {recon['senior_health']['known_leads_total']} total leads, class distribution {recon['senior_health']['class_distribution']}",
     "MATCHES 69 total; '19' figure explicitly superseded per SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md"],
    ["Video-level fields (2026-09-27 correction)", "2026-09-27 finding: descriptions missing from master video sheet; only 64/460 thumbnail URLs exported; 0/56 Dr. Rehan thumbnails",
     f"Observed: {recon['senior_health']['total_descriptions_exported']}/460 descriptions exported, {recon['senior_health']['total_thumbnail_urls_recovered']}/460 thumbnail URLs recovered (1 genuinely unavailable), {recon['senior_health']['total_downloaded_thumbnail_files']}/460 downloaded thumbnail image files archived",
     "GAP CLOSED via read-only join against raw acquisition source files (dataset.json / xlsx / thumbnail-snapshot manifests) - see sheets 15, 18"],
]
add_table_sheet("25_SOURCE_TRACEABILITY", ["Corpus", "Prior Reported Baseline", "Directly Observed On Disk", "Reconciliation Outcome"], rows,
    widths=[24, 55, 65, 45], wrap_cols=[2, 3, 4])

# ---------------------------------------------------------- 26_DATA_DICTIONARY
rows = [
    ["canonical_channel_id", "Channels/Videos", "YouTube channel ID (UC...), stable primary key across the whole registry"],
    ["dataset_id", "All", "e.g. DS-000011/018/031/032/033 - the registered acquisition/ingestion batch a record belongs to"],
    ["video_type", "Videos", "'video' (regular/long-form) or 'shorts', assigned by classify_content_pilot / video_type_classification.py"],
    ["is_placeholder", "Transcripts", "1 = disclosed non-real placeholder transcript, 0 = a real captured transcript"],
    ["visual_asset_status", "Channels", "NONE / THUMBNAIL_URL_ONLY / THUMBNAIL_EVIDENCE / FORENSIC_VIDEO_EVIDENCE - how much visual evidence beyond the raw thumbnail URL exists"],
    ["forensic_video_status", "Channels", "AVAILABLE_WITH_LIMITATIONS / NOT_AVAILABLE - whether frame-level video forensic analysis (editing/visual intelligence) exists"],
    ["first_party_analytics_status", "Channels", "INGESTED / SCHEMA_READY_NO_DATA / NOT_CONFIGURED - whether a real private YouTube Studio export was ever ingested (currently none, project-wide)"],
    ["class (A-F, OWN)", "Master Inventory", "A=acquired direct competitor (pre-existing) / B=acquired direct competitor (recent) / C=partially acquired (empty) / D=qualified pending at DB level (empty) / E=qualified-pending or identity-only (48) / F=removed or unverifiable (13) / OWN=own channel"],
    ["SOURCE_CLAIM / SOURCE_INTERPRETATION / SOURCE_RECOMMENDATION", "DS-000018", "What kind of assertion the source text itself makes - not a verification status"],
    ["evidence_locator", "Transcripts", "File-path/hash reference to the real transcript on disk - the transcript text itself is not duplicated into this workbook"],
]
add_table_sheet("26_DATA_DICTIONARY", ["Field", "Applies To", "Definition"], rows, widths=[36, 20, 90], wrap_cols=[3])

# ---------------------------------------------------------- 00_DASHBOARD (built last so it can reference other sheets)
ws0 = wb.create_sheet("00_DASHBOARD", 0)
ws0.column_dimensions["A"].width = 40
ws0.column_dimensions["B"].width = 20
ws0.cell(row=1, column=1, value="YOUTUBE KNOWLEDGE & SENIOR HEALTH — VERIFIED COVERAGE DASHBOARD").font = TITLE_FONT
ws0.cell(row=2, column=1, value="All figures read directly from repo source files at export time (2026-09-27)").font = SUBTITLE_FONT

dash_rows = [
    ("DS-000011 unique sources (full text archived)", recon["DS-000011"]["fulltext_unique_sources"]),
    ("DS-000011 knowledge rules", recon["DS-000011"]["observed_rules"]),
    ("DS-000018 research tabs (63/63 claim-atomized)", recon["DS-000018"]["observed_tabs"]),
    ("DS-000018 claims: human-audited / AI-extracted / total", recon["DS-000018"]["all_claims_combined"]),
    ("DS-000031 concepts (15/15 segments full text)", recon["DS-000031"]["observed"]["concepts"]),
    ("DS-000031 formulas", recon["DS-000031"]["observed"]["formulas"]),
    ("Senior Health channels acquired (incl. own)", recon["senior_health"]["acquired_channels_incl_own"]),
    ("Total Senior Health video records", recon["senior_health"]["total_unique_video_records"]),
    ("Real transcripts on file (self-contained archive)", recon["senior_health"]["total_real_transcripts"]),
    ("Descriptions exported", recon["senior_health"]["total_descriptions_exported"]),
    ("Thumbnail URLs recovered", recon["senior_health"]["total_thumbnail_urls_recovered"]),
    ("Downloaded thumbnail image files archived", recon["senior_health"]["total_downloaded_thumbnail_files"]),
    ("Total known Senior Health leads", recon["senior_health"]["known_leads_total"]),
]
r0 = 4
ws0.cell(row=r0, column=1, value="Metric").font = HEADER_FONT
ws0.cell(row=r0, column=2, value="Value").font = HEADER_FONT
ws0.cell(row=r0, column=1).fill = HEADER_FILL
ws0.cell(row=r0, column=2).fill = HEADER_FILL
for name, val in dash_rows:
    r0 += 1
    ws0.cell(row=r0, column=1, value=name).font = BODY_FONT
    ws0.cell(row=r0, column=2, value=val).font = BODY_FONT
metrics_last_row = r0

# class distribution mini-table for pie chart
r0 += 2
ws0.cell(row=r0, column=1, value="Channel Class").font = HEADER_FONT
ws0.cell(row=r0, column=2, value="Count").font = HEADER_FONT
class_start = r0 + 1
for cls, cnt in recon["senior_health"]["class_distribution"].items():
    r0 += 1
    ws0.cell(row=r0, column=1, value=cls).font = BODY_FONT
    ws0.cell(row=r0, column=2, value=cnt).font = BODY_FONT
class_end = r0

# transcript coverage mini-table for bar chart
r0 += 2
cov_header_row = r0
ws0.cell(row=r0, column=1, value="Channel").font = HEADER_FONT
ws0.cell(row=r0, column=2, value="Videos").font = HEADER_FONT
ws0.cell(row=r0, column=3, value="Real Transcripts").font = HEADER_FONT
cov_start = r0 + 1
for c in DATA["senior_health_channels"]:
    videos = DATA["senior_health_videos_by_channel"][c["canonical_channel_id"]]
    real_t = sum(1 for v in videos for t in v["transcripts"] if not t["is_placeholder"])
    r0 += 1
    ws0.cell(row=r0, column=1, value=c["channel_name"]).font = BODY_FONT
    ws0.cell(row=r0, column=2, value=len(videos)).font = BODY_FONT
    ws0.cell(row=r0, column=3, value=real_t).font = BODY_FONT
cov_end = r0

pie = PieChart()
pie.title = "Senior Health Channel Classification (69 known leads)"
data = Reference(ws0, min_col=2, min_row=class_start - 1, max_row=class_end)
cats = Reference(ws0, min_col=1, min_row=class_start, max_row=class_end)
pie.add_data(data, titles_from_data=True)
pie.set_categories(cats)
ws0.add_chart(pie, "D4")

bar = BarChart()
bar.title = "Videos vs Real Transcripts per Acquired Channel"
bar.y_axis.title = "Count"
data = Reference(ws0, min_col=2, max_col=3, min_row=cov_header_row, max_row=cov_end)
cats = Reference(ws0, min_col=1, min_row=cov_start, max_row=cov_end)
bar.add_data(data, titles_from_data=True)
bar.set_categories(cats)
ws0.add_chart(bar, "D22")

wb.save(OUT)
print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes), {len(wb.sheetnames)} sheets: {wb.sheetnames}")
