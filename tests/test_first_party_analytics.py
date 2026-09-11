import hashlib
import importlib
import json
import sqlite3
import sys
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ingest_youtube_analytics as analytics  # noqa: E402
import plan_intelligence_refresh as planner  # noqa: E402
import report_first_party_channel_diagnosis as diagnosis  # noqa: E402

FIXTURES = ROOT / "tests/fixtures/youtube_analytics"
DB = ROOT / "data/catalog/youtube_inventory.db"


def _write_xlsx(path, fixture="retention_curve.json"):
    source = json.loads((FIXTURES / fixture).read_text(encoding="utf-8"))
    rows = [source["headers"]] + source["rows"]
    strings = []
    cells = []
    for row_index, row in enumerate(rows, 1):
        row_cells = []
        for col_index, value in enumerate(row, 1):
            strings.append(str(value))
            column = chr(64 + col_index)
            row_cells.append(f'<c r="{column}{row_index}" t="s"><v>{len(strings)-1}</v></c>')
        cells.append(f'<row r="{row_index}">{"".join(row_cells)}</row>')
    shared = "".join(f"<si><t>{value}</t></si>" for value in strings)
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("[Content_Types].xml", "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\"/>")
        archive.writestr("xl/workbook.xml", """<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Retention" sheetId="1" r:id="rId1"/></sheets></workbook>""")
        archive.writestr("xl/_rels/workbook.xml.rels", """<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>""")
        archive.writestr("xl/sharedStrings.xml", f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(strings)}" uniqueCount="{len(strings)}">{shared}</sst>')
        archive.writestr("xl/worksheets/sheet1.xml", f'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>{"".join(cells)}</sheetData></worksheet>')


def _normalize(path, **overrides):
    options = {
        "channel_id": "CH-000002",
        "ownership_context": "FIRST_PARTY",
        "db_path": DB,
        "observation_start": "2026-08-01",
        "observation_end": "2026-08-31",
        "date_range_kind": "CUSTOM_RANGE",
        "export_date": "2026-09-11",
        "ingested_at": "2026-09-11T00:00:00Z",
    }
    options.update(overrides)
    return analytics.normalize_export(path, **options)


def _metric(payload, name):
    return next(row for snapshot in payload["SNAPSHOTS"] for row in snapshot["METRICS"] if row["METRIC_NAME"] == name)


def test_csv_import_schema_unknown_columns_and_no_fabrication():
    payload = _normalize(FIXTURES / "video_performance.csv")
    snapshot = payload["SNAPSHOTS"][0]
    assert snapshot["REPORT_TYPE"] == "VIDEO_PERFORMANCE"
    assert snapshot["SCHEMA_MAPPING"]["UNKNOWN_COLUMNS"] == ["Mystery metric"]
    assert {row["METRIC_NAME"] for row in snapshot["METRICS"]} == {
        "VIEWS", "IMPRESSIONS", "IMPRESSIONS_CTR", "WATCH_TIME_HOURS",
        "AVERAGE_VIEW_DURATION", "AVERAGE_PERCENTAGE_VIEWED", "INTRO_30S_PERCENTAGE",
    }
    assert "RETENTION_PERCENTAGE" not in {row["METRIC_NAME"] for row in snapshot["METRICS"]}
    assert snapshot["ROW_RESULTS"][0]["UNMAPPED_SOURCE_FIELDS"] == {"Mystery metric": "kept"}


def test_tsv_import_and_traffic_search_dimensions():
    payload = _normalize(FIXTURES / "traffic_sources.tsv")
    snapshot = payload["SNAPSHOTS"][0]
    assert snapshot["REPORT_TYPE"] == "TRAFFIC_SOURCES"
    assert snapshot["ROWS_READ"] == 3
    assert {row["DIMENSIONS"].get("TRAFFIC_SOURCE") for row in snapshot["METRICS"]} >= {
        "YouTube Search", "Browse features", "External"
    }
    assert any(row["DIMENSIONS"].get("SEARCH_TERM") == "retirement investing" for row in snapshot["METRICS"])


def test_xlsx_import_preserves_retention_curve(tmp_path):
    source = tmp_path / "retention.xlsx"
    _write_xlsx(source)
    payload = _normalize(source)
    snapshot = payload["SNAPSHOTS"][0]
    points = [row for row in snapshot["METRICS"] if row["METRIC_NAME"] == "RETENTION_PERCENTAGE"]
    assert snapshot["REPORT_TYPE"] == "AUDIENCE_RETENTION_CURVE"
    assert [(row["DIMENSIONS"]["ELAPSED_VIDEO_TIME"], row["METRIC_VALUE"]) for row in points] == [
        ("00:00", 100.0), ("00:30", 68.0), ("01:00", 55.0)
    ]


def test_snapshot_provenance_date_range_and_determinism():
    first = _normalize(FIXTURES / "video_performance.csv")
    second = _normalize(FIXTURES / "video_performance.csv")
    assert first == second
    snapshot = first["SNAPSHOTS"][0]
    assert snapshot["OBSERVATION_START"] == "2026-08-01"
    assert snapshot["OBSERVATION_END"] == "2026-08-31"
    assert snapshot["DATE_RANGE_KIND"] == "CUSTOM_RANGE"
    metric = _metric(first, "IMPRESSIONS_CTR")
    assert metric["PROVENANCE"]["SOURCE_SHA256"] == first["SOURCE_FILE"]["SOURCE_SHA256"]
    assert metric["SOURCE_LOCATOR"].endswith("#row=2")


def test_video_matching_priority_and_ambiguous_title():
    catalog = [
        {"VIDEO_ID": "VID-1", "YOUTUBE_VIDEO_ID": "abc123xyz01", "TITLE": "Same", "PUBLISHED_DATE": "2026-08-01", "CANONICAL_URL": "https://youtu.be/abc123xyz01"},
        {"VIDEO_ID": "VID-2", "YOUTUBE_VIDEO_ID": "def456xyz02", "TITLE": "Same", "PUBLISHED_DATE": "2026-08-02", "CANONICAL_URL": "https://youtu.be/def456xyz02"},
    ]
    assert analytics.match_video({"YOUTUBE_VIDEO_ID": "abc123xyz01"}, catalog)["STATUS"] == "MATCHED"
    assert analytics.match_video({"VIDEO_URL": "https://www.youtube.com/watch?v=def456xyz02"}, catalog)["VIDEO_ID"] == "VID-2"
    assert analytics.match_video({"TITLE": "Same"}, catalog)["STATUS"] == "AMBIGUOUS"
    assert analytics.match_video({"TITLE": "Same", "PUBLISHED_DATE": "2026-08-02"}, catalog)["VIDEO_ID"] == "VID-2"
    assert analytics.match_video({"TITLE": "Missing"}, catalog)["STATUS"] == "UNMATCHED"


def test_first_party_ownership_and_viewer_pii_rejected(tmp_path):
    with pytest.raises(analytics.AnalyticsImportError, match="FIRST_PARTY"):
        _normalize(FIXTURES / "video_performance.csv", ownership_context="COMPETITOR")
    pii = tmp_path / "pii.csv"
    pii.write_text("Viewer email,Views\nperson@example.com,1\n", encoding="utf-8")
    with pytest.raises(analytics.AnalyticsImportError, match="viewer-level"):
        _normalize(pii)


def test_ingest_copies_raw_additively_and_versions_snapshot(tmp_path):
    raw_root, output_root = tmp_path / "raw", tmp_path / "normalized"
    result = analytics.ingest_export(
        FIXTURES / "video_performance.csv", "CH-000002", "FIRST_PARTY", DB,
        raw_root, output_root, observation_start="2026-08-01", observation_end="2026-08-31",
        date_range_kind="CUSTOM_RANGE", export_date="2026-09-11", ingested_at="2026-09-11T00:00:00Z",
    )
    assert result["IMPORT_STATUS"] == "IMPORTED"
    copied = Path(result["RAW_LOCATOR"])
    assert copied.read_bytes() == (FIXTURES / "video_performance.csv").read_bytes()
    assert hashlib.sha256(copied.read_bytes()).hexdigest() == result["SOURCE_SHA256"]
    again = analytics.ingest_export(
        FIXTURES / "video_performance.csv", "CH-000002", "FIRST_PARTY", DB,
        raw_root, output_root, observation_start="2026-08-01", observation_end="2026-08-31",
        date_range_kind="CUSTOM_RANGE", export_date="2026-09-11", ingested_at="2026-09-11T00:00:00Z",
    )
    assert again["IMPORT_STATUS"] == "EXACT_DUPLICATE"
    with pytest.raises(analytics.AnalyticsImportError, match="different snapshot metadata"):
        analytics.ingest_export(
            FIXTURES / "video_performance.csv", "CH-000002", "FIRST_PARTY", DB,
            raw_root, output_root, observation_start="2026-07-01", observation_end="2026-07-31",
            date_range_kind="CUSTOM_RANGE", export_date="2026-09-11", ingested_at="2026-09-11T00:00:00Z",
        )


def test_source_dates_are_inferred_and_unmatched_video_metrics_rejected(tmp_path):
    source = tmp_path / "daily.csv"
    source.write_text("Video ID,Date,Views\nmissing00001,2026-08-02,5\nmissing00002,2026-08-03,7\n", encoding="utf-8")
    payload = _normalize(source, observation_start=None, observation_end=None, date_granularity="UNKNOWN")
    snapshot = payload["SNAPSHOTS"][0]
    assert (snapshot["OBSERVATION_START"], snapshot["OBSERVATION_END"], snapshot["DATE_GRANULARITY"]) == ("2026-08-02", "2026-08-03", "DAY")
    assert snapshot["METRICS"] == []
    assert payload["VALIDATION"]["VIDEO_UNMATCHED"] == 2
    assert payload["VALIDATION"]["ROWS_REJECTED"] == 2


def _diagnostic_payload():
    payload = _normalize(FIXTURES / "video_performance.csv")
    return diagnosis.build_diagnosis(payload, public_context={
        "VID-000001": {"FORMAT": "LONG_FORM", "PUBLIC_VIEWS": 1000, "TOPIC": "BUSINESS_ECONOMICS"},
        "VID-000002": {"FORMAT": "LONG_FORM", "PUBLIC_VIEWS": 800, "TOPIC": "BUSINESS_ECONOMICS"},
    }, competitor_ids=["CH-000001"], generated_at="2026-09-11T00:00:00Z")


def test_ctr_impressions_use_relative_cohort_not_universal_threshold():
    report = _diagnostic_payload()
    by_video = {row["VIDEO_ID"]: row for row in report["VIDEO_DIAGNOSES"]}
    assert by_video["VID-000001"]["PACKAGING_DIAGNOSIS"] == "HIGH_IMPRESSIONS_LOW_CTR"
    assert by_video["VID-000002"]["PACKAGING_DIAGNOSIS"] == "LOW_IMPRESSIONS_HIGH_CTR"
    assert report["METHODOLOGY"]["CTR_THRESHOLD"] == "CHANNEL_FORMAT_DATE_RANGE_RELATIVE_MEDIAN"
    assert "UNIVERSAL" not in json.dumps(report)


def test_intro_diagnosis_action_confidence_and_no_causal_claim():
    report = _diagnostic_payload()
    row = next(row for row in report["VIDEO_DIAGNOSES"] if row["VIDEO_ID"] == "VID-000002")
    assert row["INTRO_DIAGNOSIS"] == "STRONG_PACKAGE_WEAK_INTRO"
    assert row["ACTION"] == {"ACTION_TYPE": "FIX", "TARGET": "INTRO"}
    assert row["CONFIDENCE"] in {"LOW", "MEDIUM", "HIGH"}
    assert row["CONCLUSION_TYPE"] == "OBSERVED_FIRST_PARTY_ASSOCIATION"
    assert row["MISSING_EVIDENCE"]


def test_private_metrics_never_leak_into_competitor_comparison():
    report = _diagnostic_payload()
    benchmark = report["OWN_VS_COMPETITOR"]
    assert benchmark["SELECTED_COMPETITORS"] == ["CH-000001"]
    assert "IMPRESSIONS_CTR" in benchmark["PRIVATE_ONLY_DIMENSIONS"]
    assert not set(benchmark["PRIVATE_ONLY_DIMENSIONS"]) & set(benchmark["SHARED_PUBLIC_DIMENSIONS"])
    assert benchmark["COMPETITOR_PRIVATE_METRICS"] == "NOT_AVAILABLE"


def test_traffic_source_and_search_term_diagnosis():
    payload = _normalize(FIXTURES / "traffic_sources.tsv")
    report = diagnosis.build_diagnosis(payload, public_context={}, generated_at="2026-09-11T00:00:00Z")
    assert report["TRAFFIC_SOURCE_DIAGNOSIS"] == "SEARCH_LED"
    assert report["SEARCH_TERM_EVIDENCE"] == ["retirement investing"]


def test_audience_segments_and_longitudinal_state():
    payload = _normalize(FIXTURES / "video_performance.csv")
    snapshot = payload["SNAPSHOTS"][0]
    template = dict(snapshot["METRICS"][0])
    snapshot["METRICS"] += [
        {**template, "VIDEO_ID": None, "METRIC_NAME": "NEW_VIEWERS", "METRIC_VALUE": 600, "UNIT": "COUNT"},
        {**template, "VIDEO_ID": None, "METRIC_NAME": "CASUAL_VIEWERS", "METRIC_VALUE": 250, "UNIT": "COUNT"},
        {**template, "VIDEO_ID": None, "METRIC_NAME": "REGULAR_VIEWERS", "METRIC_VALUE": 150, "UNIT": "COUNT"},
    ]
    report = diagnosis.build_diagnosis(payload, public_context={}, generated_at="2026-09-11T00:00:00Z")
    assert report["AUDIENCE_SEGMENT_DIAGNOSIS"] == "NEW_VIEWER_LED"
    assert report["AUDIENCE_SEGMENT_NOTE"].endswith("not direct ranking signals.")
    assert report["LONGITUDINAL_FIRST_PARTY_TREND"] == "NOT_AVAILABLE"


def test_multiple_snapshot_longitudinal_ready():
    payload = _normalize(FIXTURES / "video_performance.csv")
    second = json.loads(json.dumps(payload["SNAPSHOTS"][0]))
    second["ANALYTICS_SNAPSHOT_ID"] += "-B"
    second["OBSERVATION_START"] = "2026-09-01"
    second["OBSERVATION_END"] = "2026-10-01"
    for metric in second["METRICS"]:
        metric["ANALYTICS_SNAPSHOT_ID"] = second["ANALYTICS_SNAPSHOT_ID"]
        metric["DATE_START"] = "2026-09-01"
        metric["DATE_END"] = "2026-10-01"
    payload["SNAPSHOTS"].append(second)
    report = diagnosis.build_diagnosis(payload, public_context={}, generated_at="2026-09-11T00:00:00Z")
    assert report["LONGITUDINAL_FIRST_PARTY_TREND"] == "AVAILABLE"
    assert report["LONGITUDINAL_TRAJECTORIES"]


def test_refresh_trigger_has_first_party_diagnosis_and_no_global_calibration():
    layers = planner.affected_layers("NEW_FIRST_PARTY_ANALYTICS")
    assert "FIRST_PARTY_DIAGNOSIS" in layers
    assert {"TOPIC", "PACKAGING", "HOOK_SCRIPT", "SUCCESS_FAILURE", "CHANNEL_STRATEGY", "PUBLIC_METRIC_TRAJECTORY", "BLUEPRINT", "UNIFIED_PLAN"} <= set(layers)
    assert "CROSS_NICHE_CALIBRATION" not in layers
    assert "TRAINING_CALIBRATION" not in layers


def test_import_does_not_mutate_production_db_or_data(tmp_path):
    db_before = hashlib.sha256(DB.read_bytes()).hexdigest()
    raw_before = sorted(str(path) for path in (ROOT / "data/raw").rglob("*"))
    analytics.ingest_export(
        FIXTURES / "traffic_sources.tsv", "CH-000002", "FIRST_PARTY", DB,
        tmp_path / "raw", tmp_path / "out", observation_start="2026-08-01",
        observation_end="2026-08-31", date_range_kind="CUSTOM_RANGE",
        export_date="2026-09-11", ingested_at="2026-09-11T00:00:00Z",
    )
    assert hashlib.sha256(DB.read_bytes()).hexdigest() == db_before
    assert sorted(str(path) for path in (ROOT / "data/raw").rglob("*")) == raw_before


def test_importer_and_diagnosis_modules_have_no_network_clients():
    for module in (analytics, diagnosis):
        source = Path(module.__file__).read_text(encoding="utf-8")
        assert not any(name in source for name in ("requests", "urllib", "httpx", "aiohttp"))


def test_capability_status_is_generated_from_live_contract():
    expected = json.loads((ROOT / "data/intelligence/system/first-party-analytics-capability-status-2026-09-11.json").read_text(encoding="utf-8"))
    assert analytics.build_capability_status() == expected


def test_unknown_localized_headers_surface_without_guessing(tmp_path):
    source = tmp_path / "localized.csv"
    source.write_text("Vídeo,Vistas\nabc,10\n", encoding="utf-8")
    payload = _normalize(source)
    snapshot = payload["SNAPSHOTS"][0]
    assert snapshot["REPORT_TYPE"] == "UNKNOWN_REPORT"
    assert snapshot["SCHEMA_MAPPING"]["UNKNOWN_COLUMNS"] == ["Vistas", "Vídeo"]
    assert snapshot["ROW_RESULTS"][0]["UNMAPPED_SOURCE_FIELDS"] == {"Vídeo": "abc", "Vistas": "10"}
