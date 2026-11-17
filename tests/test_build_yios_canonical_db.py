import importlib.util, json, sqlite3
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "build_yios_canonical_db.py"
spec = importlib.util.spec_from_file_location("canon", P)
canon = importlib.util.module_from_spec(spec)
spec.loader.exec_module(canon)


def test_normalizers():
    assert canon.count("116K") == 116000 and canon.count("17,215,098 views") == 17215098 and canon.count("14400") == 14400
    assert canon.count(None) is None and canon.count("n/a") is None
    assert canon.hms("01:02:03") == 3723 and canon.hms("12:34") == 754 and canon.hms("") is None
    assert canon.handle("Foo") == "@Foo" and canon.handle("@Foo") == "@Foo" and canon.handle("") is None
    assert canon.pdate("2024-05-01T10:20:30.123Z") == ("2024-05-01", "2024-05-01T10:20:30Z", "SECOND_UTC")
    assert canon.pdate("2024-05-01 10:20:30") == ("2024-05-01", None, "DATETIME_TZ_UNKNOWN")
    assert canon.pdate("2024-05-01") == ("2024-05-01", None, "DATE")
    assert canon.pdate("(date only)") is None  # corrupt placeholder found in registry/finance


def test_caption_kind_and_language():
    assert canon.kind_of("user_generated") == "CREATOR" and canon.kind_of("en_creator") == "CREATOR"
    assert canon.kind_of("en-orig_auto") == "AUTO" and canon.kind_of("auto_generated, user_generated") == "MIXED"
    assert canon.kind_of("NONE AVAILABLE") == "NONE" and canon.kind_of(None) == "UNKNOWN"
    assert canon.lang1("en, en-US") == "en" and canon.lang1("-") is None


def test_every_source_spelling_is_mapped_and_build_reconciles(tmp_path, monkeypatch):
    monkeypatch.setattr(canon, "OUT", str(tmp_path / "c.db"))
    monkeypatch.setattr(canon, "MANIFEST", str(tmp_path / "m.json"))
    canon.build()  # raises SystemExit on an unmapped video_type spelling or an orphan channel
    assert canon.verify()
    h1 = json.load(open(tmp_path / "m.json"))["logical_sha256"]
    canon.build()
    assert json.load(open(tmp_path / "m.json"))["logical_sha256"] == h1  # deterministic rebuild
    db = sqlite3.connect(tmp_path / "c.db")
    assert db.execute("select count(*) from videos where video_type_basis='INFERRED_FROM_VIDEOS_TAB' and video_type<>'LONG'").fetchone()[0] == 0
    assert db.execute("select count(*) from channels where channel_id not like 'UC%'").fetchone()[0] == 0
