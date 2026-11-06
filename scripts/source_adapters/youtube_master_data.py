"""DS-000001 source adapter: parses YouTube_Master_Data.xlsx and
Transcripts_All_159_Videos.zip into plain dicts/lists for
scripts/register_structured_source.py.

openpyxl is not installed in this environment (rule 21); XLSX is a ZIP of
XML internally, so this reads it directly via stdlib zipfile + ElementTree
rather than adding a new dependency for one column-of-cells read.

Column positions are resolved from each sheet's own header row, never
hardcoded (rule 20) — a header rename or reorder fails loudly instead of
silently misreading a column.
"""
import re
import xml.etree.ElementTree as ET
import zipfile

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}
_CELL_REF_RE = re.compile(r"([A-Z]+)(\d+)")


class SourceFormatError(Exception):
    """Raised when the supplied workbook/archive doesn't match the expected
    DS-000001 shape (missing header, missing sheet, malformed row)."""


def _col_to_num(col):
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n


def _load_shared_strings(zf):
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return ["".join(t.text or "" for t in si.findall(".//m:t", NS)) for si in root.findall("m:si", NS)]


def _resolve_sheet_paths(zf):
    """sheet display name -> internal xl/worksheets/sheetN.xml path."""
    wb_root = ET.fromstring(zf.read("xl/workbook.xml"))
    rels_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {
        rel.get("Id"): rel.get("Target")
        for rel in rels_root.findall("r:Relationship", REL_NS)
    }
    r_ns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    paths = {}
    for sheet in wb_root.findall(".//m:sheets/m:sheet", NS):
        name = sheet.get("name")
        rid = sheet.get(r_ns)
        target = rid_to_target.get(rid)
        if not target:
            raise SourceFormatError("Sheet '{}' has no resolvable target in workbook.xml.rels".format(name))
        # OOXML allows package-absolute targets ("/xl/worksheets/sheet1.xml"); openpyxl writes them.
        target = target.lstrip("/")
        paths[name] = "xl/" + target if not target.startswith("xl/") else target
    return paths


def _read_sheet_rows(zf, sheet_path, shared_strings):
    """Returns list of (row_num, {col_letter: text_value})."""
    root = ET.fromstring(zf.read(sheet_path))
    rows = []
    for row in root.findall(".//m:sheetData/m:row", NS):
        row_num = int(row.get("r"))
        cells = {}
        for c in row.findall("m:c", NS):
            m = _CELL_REF_RE.match(c.get("r"))
            col = m.group(1)
            t = c.get("t")
            v_el = c.find("m:v", NS)
            is_el = c.find("m:is", NS)
            if t == "s" and v_el is not None:
                val = shared_strings[int(v_el.text)]
            elif t == "inlineStr" and is_el is not None:
                val = "".join(x.text or "" for x in is_el.findall(".//m:t", NS))
            elif v_el is not None:
                val = v_el.text
            else:
                val = None
            cells[col] = val
        rows.append((row_num, cells))
    return rows


def _find_header_row(rows, marker_col, marker_value):
    for row_num, cells in rows:
        if cells.get(marker_col) == marker_value:
            return row_num, cells
    raise SourceFormatError(
        "Could not find header row (column {} == {!r})".format(marker_col, marker_value)
    )


def parse_channel_overview(zf, sheet_path, shared_strings):
    """Returns (channels, banner_lines):
    channels = {channel_display_name: {field_name: (value, row_num, col_letter)}}
    banner_lines = column-A text from rows above the header (e.g. the
    'Source: ... Scraped 24 Aug 2026 ...' line)."""
    rows = _read_sheet_rows(zf, sheet_path, shared_strings)
    header_row_num, header_cells = _find_header_row(rows, "A", "Field")
    channel_cols = {col: name for col, name in header_cells.items() if col != "A" and name}

    banner_lines = [
        cells.get("A") for row_num, cells in rows
        if row_num < header_row_num and cells.get("A")
    ]

    # Supplied single-channel exports use ``Field | Value`` while the older
    # multi-channel workbook names each channel in the header row.
    if channel_cols == {"B": "Value"}:
        fields = {}
        for row_num, cells in rows:
            if row_num <= header_row_num or not cells.get("A") or cells.get("B") is None:
                continue
            fields[cells["A"]] = (cells["B"], row_num, "B")
        name = fields.get("Channel Name", (None,))[0]
        if not name:
            raise SourceFormatError("Single-channel overview is missing Channel Name")
        return {name: fields}, banner_lines

    result = {name: {} for name in channel_cols.values()}
    for row_num, cells in rows:
        if row_num <= header_row_num:
            continue
        field_name = cells.get("A")
        if not field_name:
            continue
        for col, channel_name in channel_cols.items():
            value = cells.get(col)
            if value is not None:
                result[channel_name][field_name] = (value, row_num, col)
    return result, banner_lines


def parse_all_videos(zf, sheet_path, shared_strings):
    """Returns list of dicts: {header_name: (value, row_num, col_letter)},
    one per data row that has a non-empty 'Video ID' cell (excludes the
    trailing totals row, which has no Video ID)."""
    rows = _read_sheet_rows(zf, sheet_path, shared_strings)
    header_row_num, header_cells = _find_header_row(rows, "A", "#")
    col_to_header = {col: name for col, name in header_cells.items() if name}
    header_to_col = {name: col for col, name in col_to_header.items()}
    if "Video ID" not in header_to_col:
        raise SourceFormatError("'All Videos' sheet is missing a 'Video ID' column header")

    video_id_col = header_to_col["Video ID"]
    records = []
    for row_num, cells in rows:
        if row_num <= header_row_num:
            continue
        if not cells.get(video_id_col):
            continue
        records.append({
            name: (cells.get(col), row_num, col)
            for col, name in col_to_header.items()
        })
    return records


def parse_descriptions(zf, sheet_path, shared_strings):
    rows = _read_sheet_rows(zf, sheet_path, shared_strings)
    header_row_num, header_cells = _find_header_row(rows, "A", "#")
    col_to_header = {col: name for col, name in header_cells.items() if name}
    video_id_col = next((col for col, name in col_to_header.items() if name == "Video ID"), None)
    if not video_id_col:
        raise SourceFormatError("'Descriptions' sheet is missing a 'Video ID' column header")
    return {
        cells[video_id_col]: {
            name: (cells.get(col), row_num, col) for col, name in col_to_header.items()
        }
        for row_num, cells in rows
        if row_num > header_row_num and cells.get(video_id_col)
    }


def read_workbook(xlsx_path):
    with zipfile.ZipFile(xlsx_path) as zf:
        shared_strings = _load_shared_strings(zf)
        sheet_paths = _resolve_sheet_paths(zf)
        for required in ("Channel Overview", "All Videos"):
            if required not in sheet_paths:
                raise SourceFormatError("Workbook is missing expected sheet: {}".format(required))
        channels, banner_lines = parse_channel_overview(zf, sheet_paths["Channel Overview"], shared_strings)
        videos = parse_all_videos(zf, sheet_paths["All Videos"], shared_strings)
        if len(channels) == 1:
            channel_name = next(iter(channels))
            for video in videos:
                video.setdefault("Channel", (channel_name, None, None))
        if "Descriptions" in sheet_paths:
            descriptions = parse_descriptions(zf, sheet_paths["Descriptions"], shared_strings)
            for video in videos:
                video.update(descriptions.get(video["Video ID"][0], {}))
    return {"channels": channels, "videos": videos, "banner_lines": banner_lines}


_SCRAPED_DATE_RE = re.compile(r"Scraped (\d{1,2} \w+ \d{4})")


def find_scraped_date(banner_lines):
    """Extracts the source-declared scrape date (e.g. '24 Aug 2026') from the
    banner text, rather than assuming today's date or hardcoding it."""
    import datetime

    for line in banner_lines:
        m = _SCRAPED_DATE_RE.search(line or "")
        if m:
            return datetime.datetime.strptime(m.group(1), "%d %b %Y").strftime("%Y-%m-%d")
    return None


# ---------------------------------------------------------------------------
# Transcript archive
# ---------------------------------------------------------------------------

_SEPARATOR_RE = re.compile(r"\n=+\n")
_HEADER_FIELD_MAP = {
    "channel": "Channel", "title": "Title", "video_id": "Video ID", "url": "URL",
    "published": "Published", "duration": "Duration", "views": "Views", "likes": "Likes",
    "comments": "Comments", "caption_type": "Caption type", "language": "Language",
    "word_count": "Word count",
}


def _parse_transcript_member_text(text):
    parts = _SEPARATOR_RE.split(text, maxsplit=4)
    if len(parts) < 5:
        raise SourceFormatError("Transcript member does not match expected header/section shape")
    header_block = parts[0]

    header = {}
    for line in header_block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        header[key.strip()] = value.strip()

    fields = {}
    for norm_key, source_key in _HEADER_FIELD_MAP.items():
        if source_key not in header:
            raise SourceFormatError("Transcript header missing expected field: {}".format(source_key))
        fields[norm_key] = header[source_key]

    description_and_content = parts[2]
    description_body = description_and_content.split("\nCONTENT\n", 1)[0].strip()
    fields["description_present"] = bool(description_body)
    fields["caption_type_raw"] = fields["caption_type"]
    fields["availability_status"] = "UNAVAILABLE" if fields["caption_type"] == "NONE AVAILABLE" else "AVAILABLE"
    return fields


def read_transcript_archive(zip_path):
    """Streams each per-video member (never INDEX.txt) and returns parsed
    header metadata. No permanent extraction to disk (rule 23)."""
    members = []
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if "INDEX" in name.upper() or not name.lower().endswith(".txt"):
                continue
            with zf.open(info) as f:
                text = f.read().decode("utf-8", errors="replace")
            fields = _parse_transcript_member_text(text)
            fields["archive_member_path"] = name
            members.append(fields)
    return members
