"""The frozen Finance audit stays on its original registry bytes while the live registry may change."""
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research/finance-economics-intelligence"
sys.path.insert(0, str(BASE))
import validate_audit_966 as audit  # noqa: E402

ORIGINAL = "39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654"
KEY = "data/catalog/youtube_channel_registry.db"
VIDEO = "aaaaaaaaaaa"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def test_original_hash_and_copy_were_not_replaced():
    assert json.loads((BASE / "audit-baseline/MANIFEST.json").read_text())["source_hashes"][KEY] == ORIGINAL
    assert sha(audit.FROZEN_REGISTRY.read_bytes()) == ORIGINAL


@pytest.fixture
def sources(tmp_path, monkeypatch):
    frozen, other = tmp_path / "frozen.db", tmp_path / "other.csv"
    frozen.write_bytes(b"frozen")
    other.write_bytes(b"other")
    (tmp_path / "data/catalog").mkdir(parents=True)
    (tmp_path / KEY).write_bytes(b"a newer registry")
    monkeypatch.setattr(audit, "FROZEN_REGISTRY", frozen)
    monkeypatch.setattr(audit, "ROOT", tmp_path)
    return {"frozen": frozen, "other": other, "hashes": {KEY: sha(b"frozen"), "other.csv": sha(b"other")}}


def test_newer_live_registry_is_not_drift(sources):
    assert audit.source_drift_errors(sources["hashes"]) == []


def test_changed_frozen_copy_is_drift_even_if_live_matches(sources, tmp_path):
    sources["frozen"].write_bytes(b"replaced")
    (tmp_path / KEY).write_bytes(b"frozen")
    assert audit.source_drift_errors(sources["hashes"]) == ["source drift " + KEY]


def test_missing_frozen_copy_is_drift(sources):
    sources["frozen"].unlink()
    assert audit.source_drift_errors(sources["hashes"]) == ["source drift " + KEY]


def test_other_frozen_source_still_drifts(sources):
    sources["other"].write_bytes(b"changed")
    assert audit.source_drift_errors(sources["hashes"]) == ["source drift other.csv"]


def live_db(tmp_path, videos, transcripts):
    path = tmp_path / "live.db"
    con = sqlite3.connect(path)
    con.execute("create table videos(youtube_video_id)")
    con.execute("create table transcripts(youtube_video_id, transcript_text)")
    con.executemany("insert into videos values (?)", [(v,) for v in videos])
    con.executemany("insert into transcripts values (?,?)", transcripts)
    con.commit()
    con.close()
    return path


ROWS = [{"Video_ID": VIDEO, "script": {"source": {"Text_SHA256": sha(b"spoken text")}}},
        {"Video_ID": "bbbbbbbbbbb", "script": {"source": {}}}]


def test_live_registry_may_gain_videos(tmp_path):
    db = live_db(tmp_path, [VIDEO, "bbbbbbbbbbb", "ccccccccccc"], [(VIDEO, "spoken text")])
    assert audit.current_registry_errors(ROWS, db) == []


@pytest.mark.parametrize("videos,transcripts,message", [
    ([VIDEO], [(VIDEO, "spoken text")], "current registry lost video bbbbbbbbbbb"),
    ([VIDEO, "bbbbbbbbbbb"], [(VIDEO, "edited text")], "current registry changed transcript " + VIDEO),
    ([VIDEO, "bbbbbbbbbbb"], [], "current registry changed transcript " + VIDEO),
    ([VIDEO, "bbbbbbbbbbb"], [(VIDEO, None)], "current registry changed transcript " + VIDEO),
])
def test_live_registry_must_keep_audited_evidence(tmp_path, videos, transcripts, message):
    assert audit.current_registry_errors(ROWS, live_db(tmp_path, videos, transcripts)) == [message]


def test_unreadable_live_registry_fails_cleanly(tmp_path):
    bad = tmp_path / "bad.db"
    bad.write_bytes(b"not a database")
    assert audit.current_registry_errors(ROWS, bad)[0].startswith("current registry unreadable")
    assert audit.current_registry_errors(ROWS, tmp_path / "missing.db")[0].startswith("current registry unreadable")
