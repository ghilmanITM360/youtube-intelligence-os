import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/research/senior-health-2026-09-25/forensic-v3/BETTER-HEALTH-WHILE-AGING-TRANSCRIPT-STRUCTURE.json"


def test_bhwa_structural_analysis_covers_all_98_and_separates_deep_review():
    subprocess.run(
        [sys.executable, "scripts/analyze_better_health_while_aging.py"],
        cwd=ROOT,
        check=True,
    )
    payload = json.loads(OUTPUT.read_text(encoding="utf-8"))
    assert payload["population"]["videos"] == 98
    assert payload["population"]["regular_videos"] == 80
    assert payload["population"]["shorts"] == 18
    assert payload["population"]["real_transcripts"] == 98
    assert len(payload["videos"]) == 98
    assert len({row["video_id"] for row in payload["videos"]}) == 98
    assert all(row["completion_state"] == "AUTOMATED_STRUCTURAL_ANALYSIS_COMPLETE" for row in payload["videos"])
    assert all(row["deep_investigation_state"] in {"VERIFIED_DEEP_INVESTIGATION", "NOT_YET_DEEPLY_INVESTIGATED"} for row in payload["videos"])
    assert sum(row["deep_investigation_state"] == "VERIFIED_DEEP_INVESTIGATION" for row in payload["videos"]) == 25
    assert all(row["opening_first_15_seconds"] for row in payload["videos"])
    assert all(row["script_structure"] for row in payload["videos"])


def test_bhwa_breakout_inventory_has_25_unique_ids_and_original_nine():
    subprocess.run(
        [sys.executable, "scripts/analyze_better_health_while_aging.py"],
        cwd=ROOT,
        check=True,
    )
    payload = json.loads(OUTPUT.read_text(encoding="utf-8"))
    breakouts = payload["breakout_inventory"]
    assert len(breakouts) == 25
    assert len({row["video_id"] for row in breakouts}) == 25
    assert sum(row["cohort"] == "ORIGINAL_NINE" for row in breakouts) == 9
    assert sum(row["cohort"] == "REMAINING_SIXTEEN" for row in breakouts) == 16


DEEP_OUTPUT = ROOT / "docs/research/senior-health-2026-09-25/forensic-v3/BETTER-HEALTH-WHILE-AGING-DEEP-INVESTIGATIONS.json"


def test_deep_breakout_investigations_have_required_coverage():
    payload = json.loads(DEEP_OUTPUT.read_text(encoding="utf-8"))
    cases = payload["breakout_investigations"]
    assert len(cases) == 25
    assert len({row["video_id"] for row in cases}) == 25
    required = {
        "identity_and_metrics", "title_analysis", "opening_and_audience",
        "timed_opening", "hook_and_psychology", "title_script_alignment",
        "script_progression", "authority_and_evidence", "curiosity_and_narrative_debt",
        "major_revelations", "practical_advice", "closing_and_cta",
        "matched_comparison", "supporting_evidence", "contradictory_evidence",
        "conclusion", "limitations", "transcript_review_state",
    }
    for row in cases:
        assert required.issubset(row), row["video_id"]
        assert row["transcript_review_state"] == "COMPLETE_TRANSCRIPT_REVIEWED"
        assert "evidence_locator" in row["identity_and_metrics"]


def test_matched_comparisons_and_visual_observations_are_explicit():
    payload = json.loads(DEEP_OUTPUT.read_text(encoding="utf-8"))
    comparisons = payload["comparison_investigations"]
    assert len(comparisons) >= 14
    assert len(comparisons) == len({row["comparison_video_id"] for row in comparisons})
    for row in comparisons:
        assert row["transcript_review_state"] == "COMPLETE_TRANSCRIPT_REVIEWED"
        assert row["comparison_quality"] in {"HIGH", "MEDIUM", "LOW"}
    visual = payload["thumbnail_inspections"]
    assert len(visual) >= 39
    assert len(visual) == len({row["video_id"] for row in visual})
    assert all(row["inspection_state"] == "VISUALLY_INSPECTED" for row in visual)


def test_research_layers_do_not_claim_private_analytics_or_causation():
    payload = json.loads(DEEP_OUTPUT.read_text(encoding="utf-8"))
    assert payload["first_party_analytics"]["status"] == "NOT_AVAILABLE"
    assert payload["causal_claims_authorized"] is False
    assert len(payload["historical_demand_investigations"]) >= 4
    assert len(payload["medical_claim_reviews"]) >= 7
    assert len(payload["knowledge_framework_applications"]) >= 8
