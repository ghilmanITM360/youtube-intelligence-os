#!/usr/bin/env python3
"""Ingest aggregate YouTube Studio exports into private, versioned artifacts."""
import argparse
import csv
import hashlib
import json
import re
import shutil
import sqlite3
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from source_adapters import youtube_master_data as xlsx

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data/catalog/youtube_inventory.db"
RAW_ROOT = ROOT / "data/raw/inbox/first-party-analytics"
OUTPUT_ROOT = ROOT / "data/intelligence/first-party"
CAPABILITY_STATUS_PATH = ROOT / "data/intelligence/system/first-party-analytics-capability-status-2026-09-11.json"
SCHEMA_MAPPING_VERSION = "youtube-studio-export-mapping-1"
NORMALIZED_SCHEMA_VERSION = "first-party-analytics-normalized-1"

REPORT_TYPES = {
    "VIDEO_PERFORMANCE", "TRAFFIC_SOURCES", "REACH_IMPRESSIONS", "ENGAGEMENT",
    "AUDIENCE_RETENTION_SUMMARY", "AUDIENCE_RETENTION_CURVE", "AUDIENCE_SEGMENTS",
    "GEOGRAPHY", "SUBSCRIPTION_STATUS", "FORMAT_BREAKDOWN", "CHANNEL_SUMMARY",
    "UNKNOWN_REPORT",
}
DATE_RANGE_KINDS = {"LIFETIME", "FIRST_24H", "FIRST_7D", "FIRST_28D", "CUSTOM_RANGE", "ROLLING_28D", "OTHER", "UNKNOWN"}


class AnalyticsImportError(ValueError):
    pass


def _key(value):
    value = unicodedata.normalize("NFKC", str(value or "")).strip().lower().replace("%", " percentage ")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value).split())


HEADER_ALIASES = {
    # Identity and dates.
    "video id": "YOUTUBE_VIDEO_ID", "content id": "YOUTUBE_VIDEO_ID", "content": "YOUTUBE_VIDEO_ID",
    "video url": "VIDEO_URL", "url": "VIDEO_URL", "video title": "TITLE", "title": "TITLE",
    "published date": "PUBLISHED_DATE", "published time": "PUBLISHED_DATE", "video publish time": "PUBLISHED_DATE",
    "date": "DATE", "day": "DATE", "start date": "START_DATE", "end date": "END_DATE",
    # Dimensions.
    "traffic source": "TRAFFIC_SOURCE", "traffic source type": "TRAFFIC_SOURCE",
    "youtube search term": "SEARCH_TERM", "search term": "SEARCH_TERM",
    "geography": "GEOGRAPHY", "country": "GEOGRAPHY",
    "subscription status": "SUBSCRIPTION_STATUS", "content type": "FORMAT", "format": "FORMAT",
    "elapsed video time": "ELAPSED_VIDEO_TIME", "video time": "ELAPSED_VIDEO_TIME",
    "audience segment": "AUDIENCE_SEGMENT", "viewer type": "AUDIENCE_SEGMENT",
    # Metrics.
    "views": "VIEWS", "impressions": "IMPRESSIONS",
    "impressions click through rate percentage": "IMPRESSIONS_CTR", "impressions ctr percentage": "IMPRESSIONS_CTR",
    "impressions click through rate": "IMPRESSIONS_CTR", "impressions ctr": "IMPRESSIONS_CTR",
    "watch time hours": "WATCH_TIME_HOURS", "average view duration": "AVERAGE_VIEW_DURATION",
    "average percentage viewed percentage": "AVERAGE_PERCENTAGE_VIEWED", "average percentage viewed": "AVERAGE_PERCENTAGE_VIEWED",
    "unique viewers": "UNIQUE_VIEWERS", "subscribers gained": "SUBSCRIBERS_GAINED",
    "subscribers lost": "SUBSCRIBERS_LOST", "likes": "LIKES", "comments": "COMMENTS", "shares": "SHARES",
    "new viewers": "NEW_VIEWERS", "casual viewers": "CASUAL_VIEWERS", "regular viewers": "REGULAR_VIEWERS",
    "returning viewers": "RETURNING_VIEWERS", "audience retention percentage": "RETENTION_PERCENTAGE",
    "retention percentage": "RETENTION_PERCENTAGE", "intro 30s percentage": "INTRO_30S_PERCENTAGE",
    "intro 30 seconds percentage": "INTRO_30S_PERCENTAGE",
}

METRIC_UNITS = {
    "VIEWS": "COUNT", "IMPRESSIONS": "COUNT", "IMPRESSIONS_CTR": "PERCENT",
    "WATCH_TIME_HOURS": "HOURS", "AVERAGE_VIEW_DURATION": "SECONDS",
    "AVERAGE_PERCENTAGE_VIEWED": "PERCENT", "UNIQUE_VIEWERS": "COUNT",
    "SUBSCRIBERS_GAINED": "COUNT", "SUBSCRIBERS_LOST": "COUNT", "LIKES": "COUNT",
    "COMMENTS": "COUNT", "SHARES": "COUNT", "NEW_VIEWERS": "COUNT",
    "CASUAL_VIEWERS": "COUNT", "REGULAR_VIEWERS": "COUNT", "RETURNING_VIEWERS": "COUNT",
    "RETENTION_PERCENTAGE": "PERCENT", "INTRO_30S_PERCENTAGE": "PERCENT",
}
IDENTITY_FIELDS = {"YOUTUBE_VIDEO_ID", "VIDEO_URL", "TITLE"}
DIMENSION_FIELDS = {"TRAFFIC_SOURCE", "SEARCH_TERM", "GEOGRAPHY", "SUBSCRIPTION_STATUS", "FORMAT", "ELAPSED_VIDEO_TIME", "AUDIENCE_SEGMENT", "DATE"}
PROHIBITED_PERSONAL_FIELDS = {
    "email", "email address", "e mail", "viewer email", "viewer email address", "viewer id",
    "viewer name", "user id", "user email", "username", "phone", "phone number",
    "full name", "first name", "last name", "ip address",
}
EMAIL_RE = re.compile(r"\b[^\s@]+@[^\s@]+\.[^\s@]+\b")


def build_capability_status(generated_on="2026-09-11"):
    return {
        "schema_version": "first-party-analytics-capability-status-1",
        "generated_on": generated_on,
        "FIRST_PARTY_ANALYTICS_INGESTION": "READY",
        "OWN_CHANNEL_DIAGNOSTIC_ENRICHMENT": "READY_FOR_REAL_DATA",
        "LONGITUDINAL_FIRST_PARTY_INTELLIGENCE": "READY_WHEN_MULTIPLE_SNAPSHOTS_EXIST",
        "REAL_FIRST_PARTY_DATA_INGESTED": False,
        "production_status": "READY_FOR_REAL_FIRST_PARTY_EXPORT",
        "supported_formats": ["CSV", "TSV", "XLSX"],
        "normalized_storage": "PRIVATE_LOCAL_GITIGNORED_VERSIONED_ARTIFACTS",
        "canonical_db_mutation_required": False,
        "network_calls": 0,
        "test_evidence": "SYNTHETIC_FIXTURES_ONLY",
        "limitations": [
            "No real owned-channel export is present, so no production diagnosis exists.",
            "Localized headers outside the conservative alias map remain explicitly unmapped.",
            "Longitudinal conclusions require at least two compatible observed date ranges.",
        ],
    }


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _stable_id(prefix, *parts):
    digest = hashlib.sha256("\x1f".join(str(part or "") for part in parts).encode()).hexdigest()[:16].upper()
    return f"{prefix}-{digest}"


def _clean_row(headers, values):
    return {header: (values[index] if index < len(values) else "") for index, header in enumerate(headers)}


def _read_delimited(path, delimiter=None):
    with Path(path).open("r", encoding="utf-8-sig", newline="") as source:
        if delimiter is None:
            sample = source.read(8192)
            source.seek(0)
            try:
                delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
            except csv.Error:
                delimiter = ","
        rows = list(csv.reader(source, delimiter=delimiter))
    if not rows:
        raise AnalyticsImportError("analytics export is empty")
    headers = [str(value).strip() for value in rows[0]]
    return [{"SHEET": None, "HEADERS": headers, "ROWS": [
        {"ROW_NUMBER": index, "VALUES": _clean_row(headers, row)} for index, row in enumerate(rows[1:], 2)
        if any(str(value).strip() for value in row)
    ]}]


def _read_xlsx(path):
    import zipfile

    tables = []
    try:
        with zipfile.ZipFile(path) as archive:
            shared = xlsx._load_shared_strings(archive)
            for sheet, sheet_path in xlsx._resolve_sheet_paths(archive).items():
                rows = xlsx._read_sheet_rows(archive, sheet_path, shared)
                nonempty = [(number, cells) for number, cells in rows if any(value not in (None, "") for value in cells.values())]
                if not nonempty:
                    continue
                header_number, header_cells = nonempty[0]
                columns = sorted(header_cells, key=xlsx._col_to_num)
                headers = [str(header_cells[column] or "").strip() for column in columns]
                data = []
                for row_number, cells in nonempty[1:]:
                    values = [cells.get(column, "") for column in columns]
                    if any(value not in (None, "") for value in values):
                        data.append({"ROW_NUMBER": row_number, "VALUES": _clean_row(headers, values)})
                tables.append({"SHEET": sheet, "HEADERS": headers, "HEADER_ROW": header_number, "ROWS": data})
    except (OSError, zipfile.BadZipFile, KeyError, xlsx.SourceFormatError) as exc:
        raise AnalyticsImportError(f"invalid XLSX export: {exc}") from exc
    if not tables:
        raise AnalyticsImportError("analytics workbook has no non-empty sheets")
    return tables


def load_tables(path):
    path = Path(path)
    if not path.is_file():
        raise AnalyticsImportError(f"source file does not exist: {path}")
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return _read_delimited(path)
    if suffix == ".tsv":
        return _read_delimited(path, "\t")
    if suffix == ".xlsx":
        return _read_xlsx(path)
    raise AnalyticsImportError("supported analytics formats are CSV, TSV, and XLSX")


def build_schema_mapping(headers):
    if any(_key(header) in PROHIBITED_PERSONAL_FIELDS for header in headers):
        raise AnalyticsImportError("viewer-level personal data is not supported; use aggregate YouTube Analytics exports only")
    source_to_canonical = {header: HEADER_ALIASES[_key(header)] for header in headers if _key(header) in HEADER_ALIASES}
    duplicate_targets = {target for target in source_to_canonical.values() if list(source_to_canonical.values()).count(target) > 1}
    if duplicate_targets:
        raise AnalyticsImportError(f"multiple source headers map to same canonical field: {sorted(duplicate_targets)}")
    return {
        "VERSION": SCHEMA_MAPPING_VERSION,
        "SOURCE_TO_CANONICAL": source_to_canonical,
        "REQUIRED_COLUMNS": [],
        "OPTIONAL_COLUMNS": sorted(source_to_canonical),
        "UNKNOWN_COLUMNS": sorted(header for header in headers if header not in source_to_canonical),
    }


def detect_report_type(mapping):
    fields = set(mapping["SOURCE_TO_CANONICAL"].values())
    if {"RETENTION_PERCENTAGE", "ELAPSED_VIDEO_TIME"} <= fields:
        return "AUDIENCE_RETENTION_CURVE"
    if "TRAFFIC_SOURCE" in fields or "SEARCH_TERM" in fields:
        return "TRAFFIC_SOURCES"
    if fields & {"NEW_VIEWERS", "CASUAL_VIEWERS", "REGULAR_VIEWERS", "RETURNING_VIEWERS", "AUDIENCE_SEGMENT"}:
        return "AUDIENCE_SEGMENTS"
    if "GEOGRAPHY" in fields:
        return "GEOGRAPHY"
    if "SUBSCRIPTION_STATUS" in fields:
        return "SUBSCRIPTION_STATUS"
    if "FORMAT" in fields:
        return "FORMAT_BREAKDOWN"
    if "VIEWS" in fields and fields & IDENTITY_FIELDS:
        return "VIDEO_PERFORMANCE"
    if "INTRO_30S_PERCENTAGE" in fields or "RETENTION_PERCENTAGE" in fields:
        return "AUDIENCE_RETENTION_SUMMARY"
    if fields & {"IMPRESSIONS", "IMPRESSIONS_CTR"}:
        return "REACH_IMPRESSIONS"
    if fields & {"WATCH_TIME_HOURS", "AVERAGE_VIEW_DURATION", "AVERAGE_PERCENTAGE_VIEWED"}:
        return "ENGAGEMENT"
    if fields & set(METRIC_UNITS):
        return "CHANNEL_SUMMARY"
    return "UNKNOWN_REPORT"


def _read_catalog(channel_id, db_path):
    uri = Path(db_path).resolve().as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as conn:
        conn.row_factory = sqlite3.Row
        channel = conn.execute("SELECT channel_id FROM channels WHERE channel_id=?", (channel_id,)).fetchone()
        if not channel:
            raise AnalyticsImportError(f"unknown canonical channel: {channel_id}")
        rows = conn.execute(
            "SELECT v.video_id,v.youtube_video_id,v.canonical_url,s.title,s.published_at "
            "FROM videos v LEFT JOIN video_snapshots s ON s.video_snapshot_id=("
            "SELECT x.video_snapshot_id FROM video_snapshots x WHERE x.video_id=v.video_id "
            "ORDER BY x.observed_at DESC,x.video_snapshot_id DESC LIMIT 1) "
            "WHERE v.channel_id=? ORDER BY v.video_id", (channel_id,),
        ).fetchall()
    return [{
        "VIDEO_ID": row["video_id"], "YOUTUBE_VIDEO_ID": row["youtube_video_id"],
        "CANONICAL_URL": row["canonical_url"], "TITLE": row["title"],
        "PUBLISHED_DATE": (row["published_at"] or "")[:10] or None,
    } for row in rows]


def _video_id_from_url(value):
    match = re.search(r"(?:youtu\.be/|[?&]v=|/shorts/)([A-Za-z0-9_-]{11})(?:[^A-Za-z0-9_-]|$)", str(value or ""))
    return match.group(1) if match else None


def _normalized_title(value):
    value = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return " ".join(re.sub(r"[^\w]+", " ", value).split())


def match_video(identity, catalog):
    youtube_id = str(identity.get("YOUTUBE_VIDEO_ID") or "").strip()
    if youtube_id:
        matches = [row for row in catalog if row["YOUTUBE_VIDEO_ID"] == youtube_id]
        if len(matches) == 1:
            return {"STATUS": "MATCHED", "VIDEO_ID": matches[0]["VIDEO_ID"], "BASIS": "YOUTUBE_VIDEO_ID"}
        if len(matches) > 1:
            return {"STATUS": "AMBIGUOUS", "VIDEO_ID": None, "BASIS": "YOUTUBE_VIDEO_ID_CONFLICT"}
        return {"STATUS": "UNMATCHED", "VIDEO_ID": None, "BASIS": "YOUTUBE_VIDEO_ID"}
    source_url = str(identity.get("VIDEO_URL") or "").strip()
    if source_url:
        matches = [row for row in catalog if str(row.get("CANONICAL_URL") or "").strip() == source_url]
        if len(matches) == 1:
            return {"STATUS": "MATCHED", "VIDEO_ID": matches[0]["VIDEO_ID"], "BASIS": "CANONICAL_VIDEO_URL"}
        youtube_id = _video_id_from_url(source_url)
        matches = [row for row in catalog if row["YOUTUBE_VIDEO_ID"] == youtube_id] if youtube_id else []
        if len(matches) == 1:
            return {"STATUS": "MATCHED", "VIDEO_ID": matches[0]["VIDEO_ID"], "BASIS": "CANONICAL_URL_VIDEO_ID"}
        if len(matches) > 1:
            return {"STATUS": "AMBIGUOUS", "VIDEO_ID": None, "BASIS": "CANONICAL_URL_CONFLICT"}
        return {"STATUS": "UNMATCHED", "VIDEO_ID": None, "BASIS": "CANONICAL_VIDEO_URL"}
    title = str(identity.get("TITLE") or "").strip()
    if not title:
        return {"STATUS": "NOT_APPLICABLE", "VIDEO_ID": None, "BASIS": "CHANNEL_LEVEL_ROW"}
    published = str(identity.get("PUBLISHED_DATE") or "")[:10]
    exact = [row for row in catalog if row.get("TITLE") == title]
    if published:
        dated = [row for row in exact if row.get("PUBLISHED_DATE") == published]
        if len(dated) == 1:
            return {"STATUS": "MATCHED", "VIDEO_ID": dated[0]["VIDEO_ID"], "BASIS": "EXACT_TITLE_AND_DATE"}
    if exact:
        basis = "EXACT_TITLE_DATE_CONTEXT_MISSING" if not published else "EXACT_TITLE_DATE_MISMATCH_OR_MULTIPLE"
        return {"STATUS": "AMBIGUOUS", "VIDEO_ID": None, "BASIS": basis}
    normalized = _normalized_title(title)
    candidates = [row for row in catalog if _normalized_title(row.get("TITLE")) == normalized]
    if not published and candidates:
        return {"STATUS": "AMBIGUOUS", "VIDEO_ID": None, "BASIS": "NORMALIZED_TITLE_DATE_CONTEXT_MISSING"}
    candidates = [row for row in candidates if row.get("PUBLISHED_DATE") == published]
    if len(candidates) == 1:
        return {"STATUS": "MATCHED", "VIDEO_ID": candidates[0]["VIDEO_ID"], "BASIS": "NORMALIZED_TITLE_CONTROLLED_FALLBACK"}
    if len(candidates) > 1:
        return {"STATUS": "AMBIGUOUS", "VIDEO_ID": None, "BASIS": "NORMALIZED_TITLE_MULTIPLE"}
    return {"STATUS": "UNMATCHED", "VIDEO_ID": None, "BASIS": "TITLE"}


def _number(value, unit):
    text = str(value or "").strip()
    if not text or text in {"—", "-", "N/A", "n/a"}:
        return None
    if unit == "SECONDS" and ":" in text:
        parts = text.split(":")
        if len(parts) not in (2, 3) or any(not part.isdigit() for part in parts):
            raise AnalyticsImportError(f"invalid duration value: {text}")
        seconds = sum(int(part) * (60 ** index) for index, part in enumerate(reversed(parts)))
        return seconds
    cleaned = text.replace(",", "").replace("%", "").strip()
    try:
        number = float(cleaned)
    except ValueError as exc:
        raise AnalyticsImportError(f"invalid numeric metric value: {text}") from exc
    if number < 0:
        raise AnalyticsImportError(f"metric cannot be negative: {text}")
    return int(number) if unit == "COUNT" and number.is_integer() else number


def _mapped_values(values, mapping):
    return {canonical: values.get(source) for source, canonical in mapping["SOURCE_TO_CANONICAL"].items()}


def _date(value):
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return text


def normalize_export(source_path, channel_id, ownership_context, db_path=DB_PATH,
                     observation_start=None, observation_end=None, date_granularity="UNKNOWN",
                     date_range_kind="UNKNOWN", export_date=None, filters=None, dimensions=None,
                     report_type=None, ingested_at=None):
    if ownership_context != "FIRST_PARTY":
        raise AnalyticsImportError("CHANNEL_OWNERSHIP_CONTEXT must be FIRST_PARTY")
    if date_range_kind not in DATE_RANGE_KINDS:
        raise AnalyticsImportError(f"unsupported date-range kind: {date_range_kind}")
    if report_type and report_type not in REPORT_TYPES:
        raise AnalyticsImportError(f"unsupported report type: {report_type}")
    if observation_start and observation_end and observation_start > observation_end:
        raise AnalyticsImportError("observation start must not be after observation end")
    source_path = Path(source_path).resolve()
    if not source_path.is_file():
        raise AnalyticsImportError(f"source file does not exist: {source_path}")
    source_sha = _sha256(source_path)
    source_id = _stable_id("ANALYTICS-SOURCE", source_sha)
    catalog = _read_catalog(channel_id, db_path)
    ingested_at = ingested_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    snapshots = []
    totals = {"ROWS_READ": 0, "ROWS_ACCEPTED": 0, "ROWS_REJECTED": 0, "VIDEO_MATCHED": 0, "VIDEO_AMBIGUOUS": 0, "VIDEO_UNMATCHED": 0}
    unknown_columns = set()
    warnings = []
    for table in load_tables(source_path):
        mapping = build_schema_mapping(table["HEADERS"])
        if any(EMAIL_RE.search(str(row["VALUES"].get(column) or "")) for row in table["ROWS"] for column in mapping["UNKNOWN_COLUMNS"]):
            raise AnalyticsImportError("viewer-level personal data is not supported; unknown fields contain email-like values")
        detected = report_type or detect_report_type(mapping)
        unknown_columns.update(mapping["UNKNOWN_COLUMNS"])
        mapped_fields = set(mapping["SOURCE_TO_CANONICAL"].values())
        mapped_rows = [(source_row, _mapped_values(source_row["VALUES"], mapping)) for source_row in table["ROWS"]]
        source_starts = [_date(mapped.get("START_DATE") or mapped.get("DATE")) for _, mapped in mapped_rows]
        source_ends = [_date(mapped.get("END_DATE") or mapped.get("DATE")) for _, mapped in mapped_rows]
        table_start = observation_start or min((value for value in source_starts if value), default=None)
        table_end = observation_end or max((value for value in source_ends if value), default=None)
        if table_start and table_end and table_start > table_end:
            raise AnalyticsImportError("observation start must not be after observation end")
        table_granularity = "DAY" if date_granularity == "UNKNOWN" and "DATE" in mapped_fields else date_granularity
        requires_video = detected in {"VIDEO_PERFORMANCE", "REACH_IMPRESSIONS", "ENGAGEMENT", "AUDIENCE_RETENTION_SUMMARY", "AUDIENCE_RETENTION_CURVE"}
        mapping["REQUIRED_COLUMNS"] = ["ONE_OF:YOUTUBE_VIDEO_ID|VIDEO_URL|TITLE"] if requires_video else []
        snapshot_id = _stable_id(
            "ANALYTICS-SNAPSHOT", channel_id, source_sha, table["SHEET"], detected,
            table_start, table_end, date_range_kind, json.dumps(filters or {}, sort_keys=True),
        )
        metrics, row_results = [], []
        for source_row, mapped in mapped_rows:
            totals["ROWS_READ"] += 1
            identity = {key: mapped.get(key) for key in IDENTITY_FIELDS | {"PUBLISHED_DATE"}}
            match = match_video(identity, catalog)
            if match["STATUS"] == "MATCHED":
                totals["VIDEO_MATCHED"] += 1
            elif match["STATUS"] == "AMBIGUOUS":
                totals["VIDEO_AMBIGUOUS"] += 1
            elif match["STATUS"] == "UNMATCHED":
                totals["VIDEO_UNMATCHED"] += 1
            row_start = _date(mapped.get("START_DATE") or mapped.get("DATE") or table_start)
            row_end = _date(mapped.get("END_DATE") or mapped.get("DATE") or table_end)
            row_dimensions = {field: mapped[field] for field in DIMENSION_FIELDS if mapped.get(field) not in (None, "")}
            unmapped = {column: source_row["VALUES"].get(column) for column in mapping["UNKNOWN_COLUMNS"] if source_row["VALUES"].get(column) not in (None, "")}
            accepted_metrics = []
            if not requires_video or match["STATUS"] == "MATCHED":
                for source_header, canonical in mapping["SOURCE_TO_CANONICAL"].items():
                    if canonical not in METRIC_UNITS:
                        continue
                    value = _number(source_row["VALUES"].get(source_header), METRIC_UNITS[canonical])
                    if value is None:
                        continue
                    metric = {
                        "CHANNEL_ID": channel_id, "VIDEO_ID": match["VIDEO_ID"],
                        "ANALYTICS_SNAPSHOT_ID": snapshot_id, "METRIC_NAME": canonical,
                        "METRIC_VALUE": value, "UNIT": METRIC_UNITS[canonical],
                        "DATE_START": row_start, "DATE_END": row_end,
                        "DATE_RANGE_KIND": date_range_kind, "DATE_GRANULARITY": table_granularity,
                        "DIMENSIONS": row_dimensions,
                        "SOURCE_LOCATOR": f"{source_path.name}" + (f"#sheet={table['SHEET']}" if table["SHEET"] else "") + f"#row={source_row['ROW_NUMBER']}",
                        "PROVENANCE": {
                            "EVIDENCE_LAYER": "FIRST_PARTY_EXPORTED_ANALYTICS", "SOURCE_REPORT": detected,
                            "SOURCE_FILE_ID": source_id, "SOURCE_SHA256": source_sha,
                            "SOURCE_HEADER": source_header, "SOURCE_VALUE": source_row["VALUES"].get(source_header),
                            "EXTRACTION_METHOD": "DETERMINISTIC_HEADER_MAPPING",
                        },
                    }
                    metrics.append(metric)
                    accepted_metrics.append(canonical)
            accepted = bool(accepted_metrics)
            totals["ROWS_ACCEPTED" if accepted else "ROWS_REJECTED"] += 1
            row_results.append({
                "SOURCE_LOCATOR": f"row={source_row['ROW_NUMBER']}", "STATUS": "ACCEPTED" if accepted else "REJECTED",
                "VIDEO_MATCH": match, "METRICS_IMPORTED": accepted_metrics, "UNMAPPED_SOURCE_FIELDS": unmapped,
            })
        if detected == "UNKNOWN_REPORT":
            warnings.append(f"{table['SHEET'] or source_path.name}: no supported report schema detected")
        if not table_start or not table_end:
            warnings.append(f"{table['SHEET'] or source_path.name}: exact observation date range unavailable")
        snapshots.append({
            "ANALYTICS_SNAPSHOT_ID": snapshot_id, "CHANNEL_ID": channel_id,
            "SOURCE_FILE_ID": source_id, "REPORT_TYPE": detected, "SHEET": table["SHEET"],
            "EXPORT_DATE": export_date, "OBSERVATION_START": table_start, "OBSERVATION_END": table_end,
            "DATE_GRANULARITY": table_granularity, "DATE_RANGE_KIND": date_range_kind,
            "FILTERS": filters or {}, "DIMENSIONS": sorted(set(dimensions or []) | (mapped_fields & DIMENSION_FIELDS)),
            "SOURCE_SHA256": source_sha, "INGESTED_AT": ingested_at,
            "SCHEMA_MAPPING_VERSION": SCHEMA_MAPPING_VERSION, "SCHEMA_MAPPING": mapping,
            "ROWS_READ": len(table["ROWS"]), "METRICS": metrics, "ROW_RESULTS": row_results,
        })
    status = "READY" if totals["ROWS_REJECTED"] == 0 and sum(len(row["METRICS"]) for row in snapshots) else "PARTIAL"
    validation = {
        "IMPORT_STATUS": status, "SOURCE_FILES": [source_path.name],
        "REPORT_TYPES": sorted({row["REPORT_TYPE"] for row in snapshots}), **totals,
        "METRICS_IMPORTED": sorted({metric["METRIC_NAME"] for row in snapshots for metric in row["METRICS"]}),
        "UNKNOWN_COLUMNS": sorted(unknown_columns),
        "DATE_RANGES": sorted({(row["OBSERVATION_START"], row["OBSERVATION_END"], row["DATE_RANGE_KIND"]) for row in snapshots}, key=str),
        "WARNINGS": sorted(set(warnings)), "PROVENANCE_STATUS": "COMPLETE_FOR_ACCEPTED_ROWS",
    }
    return {
        "schema_version": NORMALIZED_SCHEMA_VERSION,
        "CHANNEL_ID": channel_id, "CHANNEL_OWNERSHIP_CONTEXT": ownership_context,
        "SOURCE_FILE": {
            "SOURCE_FILE_ID": source_id, "ORIGINAL_FILENAME": source_path.name,
            "SOURCE_PATH": str(source_path), "SOURCE_SHA256": source_sha,
            "SIZE_BYTES": source_path.stat().st_size, "FILE_TYPE": source_path.suffix.lower().lstrip(".").upper(),
        },
        "INGESTED_AT": ingested_at, "SCHEMA_MAPPING_VERSION": SCHEMA_MAPPING_VERSION,
        "SNAPSHOTS": snapshots, "VALIDATION": validation,
    }


def ingest_export(source_path, channel_id, ownership_context, db_path=DB_PATH, raw_root=RAW_ROOT,
                  output_root=OUTPUT_ROOT, **metadata):
    payload = normalize_export(source_path, channel_id, ownership_context, db_path=db_path, **metadata)
    source = Path(source_path).resolve()
    source_id = payload["SOURCE_FILE"]["SOURCE_FILE_ID"]
    raw_path = Path(raw_root) / channel_id / source_id / source.name
    output_dir = Path(output_root) / "channels" / channel_id
    normalized_path = output_dir / f"{source_id}-normalized.json"
    validation_path = output_dir / f"{source_id}-validation.json"
    if normalized_path.exists():
        existing = json.loads(normalized_path.read_text(encoding="utf-8"))
        if existing.get("SOURCE_FILE", {}).get("SOURCE_SHA256") != payload["SOURCE_FILE"]["SOURCE_SHA256"]:
            raise AnalyticsImportError(f"snapshot identity collision: {normalized_path}")
        old_ids = [row["ANALYTICS_SNAPSHOT_ID"] for row in existing.get("SNAPSHOTS", [])]
        new_ids = [row["ANALYTICS_SNAPSHOT_ID"] for row in payload["SNAPSHOTS"]]
        if old_ids != new_ids:
            raise AnalyticsImportError("source already imported with different snapshot metadata")
        return {
            "IMPORT_STATUS": "EXACT_DUPLICATE", "SOURCE_SHA256": payload["SOURCE_FILE"]["SOURCE_SHA256"],
            "RAW_LOCATOR": str(raw_path), "NORMALIZED_LOCATOR": str(normalized_path),
            "VALIDATION_LOCATOR": str(validation_path), "ANALYTICS_SNAPSHOT_IDS": new_ids,
            "REFRESH_CHANGE": None,
        }
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    if raw_path.exists() and _sha256(raw_path) != payload["SOURCE_FILE"]["SOURCE_SHA256"]:
        raise AnalyticsImportError(f"raw destination already exists with different bytes: {raw_path}")
    if not raw_path.exists():
        shutil.copyfile(source, raw_path)
    payload["SOURCE_FILE"]["RAW_LOCATOR"] = str(raw_path)
    normalized_path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    validation_path.write_text(json.dumps(payload["VALIDATION"], indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        **payload["VALIDATION"],
        "IMPORT_STATUS": "IMPORTED", "SOURCE_SHA256": payload["SOURCE_FILE"]["SOURCE_SHA256"],
        "RAW_LOCATOR": str(raw_path), "NORMALIZED_LOCATOR": str(normalized_path),
        "VALIDATION_LOCATOR": str(validation_path), "ANALYTICS_SNAPSHOT_IDS": [row["ANALYTICS_SNAPSHOT_ID"] for row in payload["SNAPSHOTS"]],
        "REFRESH_CHANGE": "NEW_FIRST_PARTY_ANALYTICS",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--ownership", required=True, choices=["FIRST_PARTY"])
    parser.add_argument("--report-type", choices=sorted(REPORT_TYPES))
    parser.add_argument("--export-date")
    parser.add_argument("--observation-start")
    parser.add_argument("--observation-end")
    parser.add_argument("--date-granularity", default="UNKNOWN")
    parser.add_argument("--date-range-kind", choices=sorted(DATE_RANGE_KINDS), default="UNKNOWN")
    parser.add_argument("--filter-json", default="{}")
    parser.add_argument("--dimension", action="append")
    args = parser.parse_args(argv)
    result = ingest_export(
        args.source, args.channel, args.ownership, report_type=args.report_type,
        export_date=args.export_date, observation_start=args.observation_start,
        observation_end=args.observation_end, date_granularity=args.date_granularity,
        date_range_kind=args.date_range_kind, filters=json.loads(args.filter_json), dimensions=args.dimension,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
