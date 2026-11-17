import hashlib, json
from pathlib import Path

BASE = Path(__file__).resolve().parent
C = BASE / "corrections" / "NICK_260"


def test_nick260_correction_layer():
    rec = json.loads((C / "NICK_260_CORRECTION_2026-11-01.json").read_text())
    for key in ("original_packet", "original_receipts"):
        copy = BASE / rec[key]["copy"]
        assert hashlib.sha256(copy.read_bytes()).hexdigest() == rec[key]["sha256"]
    packet = json.loads((BASE / "audit-batches" / "NICK_260.json").read_text())
    receipts = json.loads((BASE / "audit-batches" / "NICK_260_READ_RECEIPTS.json").read_text())
    claims = {c["claim_id"]: c for c in packet["reviews"][0]["script"]["claim_audit"]}
    assert "12.70%" in claims["C17"]["assessment"] and "VERIFIED" in claims["C17"]["assessment"]
    assert "16.19%" in claims["C20"]["assessment"] and "14.26%" in claims["C20"]["assessment"]
    ids = {s["source_id"] for s in receipts["primary_source_receipts"]}
    assert {"NYF4Q", "NYFX25Q4", "NYFPDF25Q4"} <= ids
    original = json.loads((C / "ORIGINAL_NICK_260.json").read_text())
    oc = {c["claim_id"]: c for c in original["reviews"][0]["script"]["claim_audit"]}
    # only C17 and C20 changed among the claims
    assert [k for k in oc if oc[k] != claims[k]] == ["C17", "C20"]
