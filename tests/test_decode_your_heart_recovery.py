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


def test_completeness_matrix_separates_sampling_from_audiovisual_audit():
    reg = json.loads(REGISTER.read_text())
    matrix = reg["completeness_matrix"]
    for dim, counts in matrix.items():
        assert sum(counts.values()) == 56, dim
    assert matrix["complete_audiovisual_audit"] == {"NOT_VERIFIED": 56}
    assert matrix["actual_spoken_audio_review"] == {"NOT_VERIFIED": 56}
    no_curve = {r["video_id"] for r in reg["records"] if r["evidence_dimensions"]["retention_curve"] != "AVAILABLE"}
    assert len(no_curve) == 10
    for r in reg["records"]:
        if r["video_id"] in no_curve:
            assert r["investigation_status"] == "LIMITED_BY_UNAVAILABLE_EVIDENCE"
            assert r["retention_investigation"]["status"] != "CONTENT_LINKED_COMPLETE"


def test_uq3_black_tail_correction_is_active():
    reg = json.loads(REGISTER.read_text())
    rec = next(r for r in reg["records"] if r["video_id"] == "Uq3T8YZgyTw")
    assert "does not recur" in rec["playback_audit"]["possible_explanation"]


def test_studio_export_reconciliation():
    m = _module()
    if not m.EXTENDED_STUDIO_ARCHIVE.exists():
        return  # private export absent on this machine
    assert set(m.LIVE_STUDIO_METRICS) == {r["id"] for r in json.loads(m.DATASET.read_text())}
    assert [e["title"] for e in m.EXTENDED_STUDIO_EXTRA_ROWS] == ["Post"]
    rec = m.reconcile_browser_rows()
    assert rec["mismatches_beyond_display_rounding"] == []
    assert len(rec["previously_missing_now_exported"]) == 9
    prov = json.loads((m.STUDIO_DIR_0928 / "studio-export-provenance.json").read_text())
    for name, meta in prov["files"].items():
        assert m.sha256(m.STUDIO_DIR_0928 / name) == meta["sha256"], name


CHECKPOINT = ROOT / "docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json"


def test_final_validation_corrections_are_active():
    chk = json.loads(CHECKPOINT.read_text())
    fv = chk["final_validation_2026_09_28"]
    audit = {c["id"]: c["status"] for c in fv["claim_audit"]}
    assert audit["A"] == "CORRECTED" and audit["A2"] == "WITHDRAWN" and audit["B"] == "CORRECTED" and audit["D"] == "CORRECTED"
    text = json.dumps(chk["diagnosis"])
    assert "binding constraint" not in text.replace("LOW that audience development is currently the binding constraint", "")
    assert "largely South Asian" not in text and "qbwCkH_GqhU 1.65%" not in text
    assert "more than 6 months in the past year" in fv["youtube_definitions"]["regular_viewers"]


def test_priority_reviews_never_claim_heard_audio():
    reg = json.loads(REGISTER.read_text())
    reviewed = [r for r in reg["records"] if r["priority_review_2026_09_28"]]
    assert 8 <= len(reviewed) <= 12 == reg["counts"]["priority_reviews"]
    for r in reviewed:
        assert r["evidence_dimensions"]["actual_spoken_audio_review"] == "NOT_VERIFIED"
        assert r["evidence_dimensions"]["complete_audiovisual_audit"] == "NOT_VERIFIED"
    assert reg["counts"]["complete_audiovisual_audits_verified"] == 0


def test_medical_reviews_cite_known_references_and_flag_aspirin():
    chk = json.loads(CHECKPOINT.read_text())
    fv = chk["final_validation_2026_09_28"]
    refs = set(fv["medical_references"])
    for c in fv["medical_claim_reviews"]:
        cited = {t.strip() for t in c["evidence"].split(";")} & refs
        if c["priority"] in ("IMMEDIATE", "HIGH") and c["verdict"] != "TITLE_CONTENT_MISMATCH":
            assert cited, c
    aspirin = [c for c in fv["medical_claim_reviews"] if c["video_id"] == "HzFdyjyEFTY" and c["priority"] == "IMMEDIATE"]
    assert aspirin and "doctor" in aspirin[0]["alternative_wording"]
