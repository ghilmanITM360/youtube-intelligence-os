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
    assert all(row["deep_investigation_state"] in {"PREVIOUSLY_REPORTED_DEEP_REVIEW", "NOT_YET_DEEPLY_INVESTIGATED"} for row in payload["videos"])
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
