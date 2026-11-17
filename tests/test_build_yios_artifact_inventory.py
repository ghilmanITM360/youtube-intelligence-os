import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "build_yios_artifact_inventory.py"
spec = importlib.util.spec_from_file_location("inv", P)
inv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inv)


def test_area_and_role():
    assert inv.area("data/raw/channel-data/DS-000020/x.json") == "data/raw"
    assert inv.area("research/what-if-scripts/analysis/a.md") == "research/what-if-scripts"
    assert inv.area("README.md") == "README.md"
    assert inv.role("research/what-if-scripts/analysis/V001.md") == "what-if study"
    assert inv.role("data/raw/channel-data/DS-000020/transcripts/a.txt") == "transcript"
    assert inv.role("scripts/foo.py") == "other"


def test_id_regexes_match_exact_ids_only():
    assert inv.VID.findall("a dB10EUmjHyc b") == ["dB10EUmjHyc"]
    assert inv.VID.findall("a dB10EUmjHycX b") == []  # 12 chars: not an id
    uc = "UC" + "a" * 22
    assert inv.CHN.findall(f"x {uc} y") == [uc] and inv.CHN.findall(f"x {uc}Z y") == []
