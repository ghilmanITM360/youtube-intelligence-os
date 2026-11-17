"""Isolated integration guards; no fixture is an accepted production audit."""
import csv
import io
import json
from pathlib import Path
from zipfile import ZipFile

import openpyxl
import pytest
from openpyxl.worksheet.table import Table

from scripts.yios_integration import (
    IntegrationError, check_expected_head, guard_target_changes,
    patch_workbook, verify_csv_targets, verify_csv_projections, verify_workbook,
)


def ledger(*rows):
    return b"".join((json.dumps(r, sort_keys=True) + "\n").encode() for r in rows)


def row(vid, complete=False):
    return {"Video_ID": vid, "Channel_ID": "fixture-channel", "identity": {"Video_ID": vid},
            "statuses": {d + "_REVIEW": "COMPLETE_LIMITED_EVIDENCE" if complete else "NOT_STARTED"
                         for d in ("TITLE", "THUMBNAIL", "SCRIPT", "TOPIC", "PERFORMANCE", "VIRALITY")},
            "script": {"fixture": True}}


def test_two_different_packets_preserve_previously_integrated_rows():
    a, b, accepted = row("a"), row("b"), row("old", True)
    first = ledger(row("a", True), b, accepted)
    assert guard_target_changes(ledger(a, b, accepted), first, {"a"}) == ["a"]
    assert guard_target_changes(first, ledger(row("a", True), row("b", True), accepted), {"b"}) == ["b"]


def test_duplicate_accepted_unknown_and_identity_order_fail_closed():
    before = ledger(row("a", True), row("b"))
    with pytest.raises(IntegrationError, match="already accepted"):
        guard_target_changes(before, before, {"a"})
    with pytest.raises(IntegrationError, match="unknown"):
        guard_target_changes(before, before, {"unknown"})
    with pytest.raises(IntegrationError, match="identit"):
        guard_target_changes(before, ledger(row("b"), row("a", True)), {"b"})
    changed_old = row("a", True)
    changed_old["script"] = {"clobbered": True}
    with pytest.raises(IntegrationError, match="non-target"):
        guard_target_changes(before, ledger(changed_old, row("b", True)), {"b"})


def test_stale_checkout_cannot_publish():
    with pytest.raises(IntegrationError, match="stale"):
        check_expected_head("61f26b5c", "223f449")
    check_expected_head("223f449", "223f449")


def test_csv_preserves_raw_unchanged_records_and_multiline():
    before = b'Video_ID,analysis\r\nold,"keep\nthis"\r\na,old\r\nb,old\r\n'
    after = b'Video_ID,analysis\r\nold,"keep\nthis"\r\na,new\r\nb,old\r\n'
    assert verify_csv_targets(before, after, {"a"}) == ["a"]
    with pytest.raises(IntegrationError, match="header"):
        verify_csv_targets(before, after.replace(b"analysis", b"changed"), {"a"})
    with pytest.raises(IntegrationError, match="non-target"):
        verify_csv_targets(before, after.replace(b"b,old", b"b,new"), {"a"})


def workbook(path):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    for name in ["Combined Dashboard", "All Finance Videos", "Channel Directory", "Detailed Research"]:
        ws = wb.create_sheet(name)
        ws.freeze_panes = "C5"
        ws.column_dimensions["A"].width = 24
        ws.row_dimensions[5].height = 32
    ws = wb["All Finance Videos"]
    ws.append([])
    ws["A4"] = "Video ID"
    for n in range(2, 22):
        ws.cell(4, n, "Header " + str(n))
    ws["U4"] = "Title status"
    ws["A5"] = "a"
    ws["A6"] = "b"
    ws["U5"] = "NOT_STARTED"
    ws["U6"] = "NOT_STARTED"
    ws["U5"].number_format = "@"
    ws.add_table(Table(displayName="FixtureVideos", ref="A4:U6"))
    wb["Detailed Research"]["A5"] = "a"
    wb["Detailed Research"]["A6"] = "b"
    wb["Detailed Research"]["D5"] = "pending"
    wb["Detailed Research"]["D6"] = "pending"
    wb["Combined Dashboard"]["B6"] = "=COUNTIF('All Finance Videos'!AA5:AA6,\"DEEP_AUDIT_COMPLETE\")"
    wb["Combined Dashboard"]["B7"] = "=B5-B6"
    wb["Combined Dashboard"]["B5"] = 2
    wb.save(path)


def payload():
    dims = ["title", "thumbnail", "script", "topic", "performance", "virality"]
    return {"summary": {"total": 2, "deep_audited": 1, "pending": 1},
            "all_videos": [{"video_id": "a", "audit_status": "DEEP_AUDIT_COMPLETE",
                            "thumbnail_status": "AVAILABLE", "local_media_status": "fixture.jpg", "blocker": "",
                            **{d + "_review_status": "COMPLETE_LIMITED_EVIDENCE" for d in dims}},
                           {"video_id": "b", "audit_status": "NOT_DEEP_AUDITED",
                            **{d + "_review_status": "NOT_STARTED" for d in dims}}],
            "details": [{"video_id": "a", "batch_id": "FIXTURE_A", "deep_audit_status": "DEEP_AUDIT_COMPLETE",
                         "statuses": row("a", True)["statuses"],
                         **{d + "_research": {"analysis": "fixture", "review_scope": "FULL_STORED_TEXT"} for d in dims},
                         "event_research": {}, "private_metrics": {}}]}


def test_workbook_target_patch_preserves_formulas_tables_styles_dimensions_panes(tmp_path):
    before = tmp_path / "before.xlsx"
    after = tmp_path / "after.xlsx"
    workbook(before)
    after.write_bytes(before.read_bytes())
    report = patch_workbook(after, payload(), {"a"})
    assert report["native_excel_recalculation"] == "NOT_TESTED"
    verify_workbook(before, after, {"a"})
    old = openpyxl.load_workbook(before)
    new = openpyxl.load_workbook(after)
    assert new.sheetnames == old.sheetnames
    assert new["All Finance Videos"]["U5"].value == "COMPLETE_LIMITED_EVIDENCE"
    assert new["All Finance Videos"]["U6"].value == "NOT_STARTED"
    assert new["Detailed Research"]["D5"].value == "FIXTURE_A"
    assert new["Detailed Research"]["D6"].value == "pending"
    assert new["Combined Dashboard"]["B6"].value == old["Combined Dashboard"]["B6"].value
    for name in old.sheetnames:
        assert new[name].freeze_panes == old[name].freeze_panes
        assert new[name].column_dimensions["A"].width == old[name].column_dimensions["A"].width
        assert new[name].row_dimensions[5].height == old[name].row_dimensions[5].height
    assert new["All Finance Videos"]["U5"].style_id == old["All Finance Videos"]["U5"].style_id
    once = after.read_bytes()
    assert patch_workbook(after, payload(), {"a"})["changed_cells"] == []
    assert after.read_bytes() == once
    with ZipFile(before) as a, ZipFile(after) as b:
        assert a.read("xl/styles.xml") == b.read("xl/styles.xml")
        assert a.read("xl/tables/table1.xml") == b.read("xl/tables/table1.xml")
    new["All Finance Videos"]["U6"] = "clobbered"
    new.save(after)
    with pytest.raises(IntegrationError):
        verify_workbook(before, after, {"a"})


def test_all_existing_header_values_reconcile_to_jsonl():
    a = row("a")
    a["identity"].update({"Channel": "Fixture", "Title": "fixture title", "Views": "123"})
    a.update(title={"analysis": "first\nsecond", "nested": {"field": [1, 2]}}, thumbnail={},
             topic={}, performance={"Performance_tier": "TYPICAL", "Metric_snapshot_date": "fixture"},
             virality={}, event={}, private_metrics={}, batch_id="FIXTURE")
    data = io.StringIO(newline="")
    writer = csv.writer(data, lineterminator="\n")
    writer.writerow(["Video_ID", "analysis", "nested"])
    writer.writerow(["a", json.dumps(a["title"]["analysis"]), json.dumps(a["title"]["nested"], sort_keys=True)])
    csvs = {"TITLE_ANALYSIS_966.csv": data.getvalue().encode()}
    verify_csv_projections([a], csvs)
    with pytest.raises(IntegrationError, match="projection"):
        verify_csv_projections([a], {"TITLE_ANALYSIS_966.csv": csvs["TITLE_ANALYSIS_966.csv"].replace(b"first", b"WRONG")})


def test_visual_rejects_protected_and_existing_record_before_any_write(tmp_path):
    from scripts.yios_integration import prepare_visual
    with pytest.raises(IntegrationError, match="protected"):
        prepare_visual(tmp_path, {}, "5umJ63d3rzQ", "channel")
    path = tmp_path / "research/visual-forensics/channels/channel/new/OLD.md"
    path.parent.mkdir(parents=True)
    path.write_text("preserved")
    files = {str(path.relative_to(tmp_path)): b"clobber"}
    with pytest.raises(IntegrationError, match="collision"):
        prepare_visual(tmp_path, files, "new", "channel")
    assert path.read_text() == "preserved"


def test_two_packets_through_actual_builder_keep_other_965_records(tmp_path):
    import importlib.util
    import sqlite3
    from scripts.yios_integration import CSVS, LEDGER
    source = Path(__file__).resolve().parents[1] / "research/finance-economics-intelligence/build_audit_966.py"
    spec = importlib.util.spec_from_file_location("fixture_finance_builder", source)
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    base = tmp_path / "fixture-finance"
    base.mkdir()
    (base / "audit-baseline").mkdir()
    (base / "audit-batches").mkdir()
    builder.BASE, builder.ROOT = base, tmp_path
    ids = [f"fixture{i:04}" for i in range(966)]
    master = [{"Video_ID": vid, "Channel_ID": "fixture-channel", "Channel": "fixture", "Title": "fixture title",
               "Views": "123", "Performance_tier": "TYPICAL", "Peer_count": "0", "Lifetime_rate_ratio": "1",
               "Peer_Video_IDs": "", "Tier_basis": "fixture", "Metric_snapshot_date": "fixture",
               "Format": "video", "Age_days": "100"} for vid in ids]

    def write(name, rows, fields=None):
        with (base / name).open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields or list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    write("VIDEO_MASTER.csv", master)
    write("audit-baseline/VIDEO_IDS.csv", [{"Video_ID": vid, "Channel_ID": "fixture-channel"} for vid in ids])
    write("TRANSCRIPT_COVERAGE.csv", [{"Video_ID": vid, "Status": "TEXT_AVAILABLE"} for vid in ids])
    write("THUMBNAIL_COVERAGE.csv", [{"Video_ID": vid, "URL_status": "fixture"} for vid in ids])
    for name in ("SEMANTIC_REVIEWS.csv", "TITLE_SEMANTIC_REVIEWS.csv", "THUMBNAIL_REVIEWS.csv", "DEEP_SCRIPT_MAPS.csv"):
        write(name, [], ["Video_ID"])
    (base / "audit-batches/TRANSCRIPT_RECOVERY_001.json").write_text(json.dumps({"batch_id": "FIXTURE_RECOVERY", "attempts": [], "reviews": []}))
    db = tmp_path / "data/catalog/youtube_channel_registry.db"
    db.parent.mkdir(parents=True)
    with sqlite3.connect(db) as con:
        con.execute("CREATE TABLE videos(youtube_video_id TEXT, likes INTEGER, comments INTEGER, description TEXT, description_unavailable_reason TEXT)")
        con.executemany("INSERT INTO videos VALUES (?,0,0,'fixture','')", [(vid,) for vid in ids])
    builder.build()
    for index in (0, 1):
        previous = (base / LEDGER).read_bytes()
        csv_before = {n: (base / n).read_bytes() for n in CSVS}
        packet = {"batch_id": "FIXTURE_" + str(index), "reviews": [{"Video_ID": ids[index],
                  "statuses": row(ids[index], True)["statuses"], "title": {"analysis": "fixture only"}}]}
        (base / f"audit-batches/FIXTURE_{index}.json").write_text(json.dumps(packet))
        current = builder.build()
        assert guard_target_changes(previous, (base / LEDGER).read_bytes(), {ids[index]}) == [ids[index]]
        for name in CSVS:
            verify_csv_targets(csv_before[name], (base / name).read_bytes(), {ids[index]})
        verify_csv_projections(current, {n: (base / n).read_bytes() for n in CSVS})


def test_workbook_verifier_rejects_deleted_formula_in_allowed_counter_cell(tmp_path):
    from xml.etree import ElementTree as ET
    before, after = tmp_path / "before.xlsx", tmp_path / "after.xlsx"
    workbook(before)
    namespace = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with ZipFile(before) as original, ZipFile(after, "w") as changed:
        for item in original.infolist():
            data = original.read(item.filename)
            if item.filename == "xl/worksheets/sheet1.xml":
                root = ET.fromstring(data)
                for sheet_row in root.find(namespace + "sheetData"):
                    for cell in list(sheet_row):
                        if cell.attrib.get("r") == "B6":
                            sheet_row.remove(cell)
                data = ET.tostring(root)
            changed.writestr(item, data)
    with pytest.raises(IntegrationError, match="removed|formula"):
        verify_workbook(before, after, {"a"})
