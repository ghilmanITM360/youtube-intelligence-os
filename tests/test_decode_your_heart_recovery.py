import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Video_Evidence_Register.json"


def _module():
    spec = importlib.util.spec_from_file_location("ddh", ROOT / "scripts/build_decode_your_heart_recovery.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_investigation_status_rules():
    m = _module()
    curve = {"curve_status": "AVAILABLE"}
    assert m.investigation_status("r9ZyUWyY4Lc", curve)[0] == "RETENTION_ANALYZED"
    base = {"comparison": "", "opening": "", "visuals": "", "editing": "", "closing": "", "possible_explanation": "", "alternative_explanation": ""}
    # Descriptive (non m:ss) anchors never count as complete playback.
    m.PRIORITY_PLAYBACK["x_desc"] = {**base, "duration_seconds": 40, "timestamps": ["0:00 a", "mid-video b", "0:40 c"]}
    assert m.investigation_status("x_desc", curve)[0] == "PARTIAL_PLAYBACK"
    # Long-form needs at least one numeric anchor per started minute.
    m.PRIORITY_PLAYBACK["x_thin"] = {**base, "duration_seconds": 362, "timestamps": ["0:00 a", "2:20 b", "6:02 c"]}
    assert m.investigation_status("x_thin", curve)[0] == "PARTIAL_PLAYBACK"
    assert m.investigation_status("EB3_A2b4a6o", curve)[0] == "RETENTION_ANALYZED"
    # Seek-sampled records must never be labelled as full playback.
    assert m.playback_audit("YVjbjcVo1is")["status"] == "SEEK_SAMPLED_AT_RETENTION_EVENTS"
    assert m.investigation_status("QfRaG71ZA_0", curve)[0] == "RETENTION_ANALYZED"
    assert m.investigation_status("QfRaG71ZA_0", None)[0] == "LIMITED_BY_UNAVAILABLE_EVIDENCE"


def test_register_counts_match_records():
    reg = json.loads(REGISTER.read_text())
    records = reg["records"]
    assert len(records) == 56 == len({r["video_id"] for r in records})
    counts = reg["counts"]["investigation_status"]
    assert sum(counts.values()) == 56
    for status, n in counts.items():
        assert sum(r["investigation_status"] == status for r in records) == n
    assert set(counts) == set(reg["investigation_status_definitions"])


def test_signal_pass_never_claims_complete_audiovisual_review():
    reg = json.loads(REGISTER.read_text())
    passed = [r for r in reg["records"] if r["completion_states"]["continuous_signal_pass"] != "NOT_STARTED"]
    assert passed and reg["counts"]["complete_audiovisual_audits_verified"] == 0
    for r in passed:
        assert r["playback_inspected"] == "SEEK_SAMPLED_AT_RETENTION_EVENTS"
        assert r["completion_states"]["complete_audiovisual_editing_review"] == "NOT_VERIFIED"
