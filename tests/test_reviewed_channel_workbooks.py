"""Adapter never invents metrics, and the committed workbooks satisfy the importer's own contract."""
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_reviewed_channel_workbooks as adapter  # noqa: E402
import register_supplied_channel as importer  # noqa: E402
from inventory_catalog import CatalogError  # noqa: E402

VID = "aaaaaaaaaaa"
SPEC = {"slug": "t", "commit": "c", "path": "p", "source_label": "test", "scraped": "04 Nov 2026",
        "channel": {"Channel Name": "T", "Handle": "@t", "Channel ID": "UCt", "Channel URL": "https://www.youtube.com/@t"},
        "fields": {"Video ID": "id", "Title": "title", "Sec": "sec", "Views": "views", "Likes": "likes",
                   "Comments": "comments", "Thumbnail URL": "thumb", "Full Description": "text"},
        "published": lambda r: adapter.to_utc(r["when"])}


def source(**overrides):
    return {"id": VID, "title": "T", "sec": "10", "views": "5", "likes": "UNAVAILABLE_LOGGED_OUT_PLAYER", "comments": "",
            "thumb": "UNKNOWN", "text": "UNKNOWN", "when": "2026-11-03T10:00:17-08:00", **overrides}


def test_unknown_stays_empty_and_literal_zero_stays_zero():
    row = adapter.video_row(SPEC, source(views="0"))
    assert row["Likes"] is None and row["Comments"] is None and row["Thumbnail URL"] is None and row["Full Description"] is None
    assert row["Views"] == 0


def test_garbage_metric_raises_instead_of_guessing():
    with pytest.raises(ValueError):
        adapter.video_row(SPEC, source(views="3.1M views"))


def test_shorts_url_and_offset_are_normalized():
    row = adapter.video_row(SPEC, source())
    assert row["Video URL"] == "https://www.youtube.com/watch?v=" + VID
    assert row["Published (UTC)"] == "2026-11-03T18:00:17Z"


def test_suppressed_value_is_emptied_for_that_video_only():
    spec = {**SPEC, "suppress": {(VID, "Views"): "reason"}}
    assert adapter.video_row(spec, source())["Views"] is None
    assert adapter.video_row(spec, source(id="bbbbbbbbbbb"))["Views"] == 5


def test_round_trip_detects_changed_value(tmp_path):
    rows = [adapter.video_row(SPEC, source())]
    path = tmp_path / "w.xlsx"
    adapter.write_workbook(path, SPEC, rows)
    adapter.verify(path, SPEC, rows)
    with pytest.raises(AssertionError):
        adapter.verify(path, SPEC, [{**rows[0], "Views": 6}])


@pytest.mark.parametrize("spec", adapter.SPECS, ids=lambda s: s["slug"])
def test_committed_workbook_loads_through_the_importer(spec, tmp_path):
    folder = ROOT / "research/registry-ingestion" / spec["slug"]
    review = json.loads((folder / "REVIEW.json").read_text(encoding="utf-8"))
    workbook = folder / f"{spec['slug']}_reviewed.xlsx"
    assert hashlib.sha256(workbook.read_bytes()).hexdigest() == review["workbook_sha256"]
    assert review["source"]["commit"] == spec["commit"]
    book, name, channel, transcripts = importer.load_source(workbook, tmp_path, review["transcript_pending_ids"])
    assert name == spec["channel"]["Channel Name"] and channel["Channel ID"][0] == spec["channel"]["Channel ID"]
    assert len(book["videos"]) == review["videos"] and transcripts == {}
    with pytest.raises(CatalogError):
        importer.load_source(workbook, tmp_path, review["transcript_pending_ids"][1:])
