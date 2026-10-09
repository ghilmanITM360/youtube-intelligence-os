import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import test_stage_what_if_forensics as staging_fixtures
from stage_what_if_forensics import StagingError, stage
from promote_what_if_forensics import promote


@pytest.fixture
def evidence():
    fixture = staging_fixtures.StagingTests()
    fixture.setUp()
    for table, values in fixture.brain["tables"].items():
        row = values[0]
        row["START_SEC"] = "0"
        row["END_SEC"] = "4"
        if table == "MASTER_SHOTS":
            row["DURATION_SEC"] = "4"
        if table == "MASTER_MOTIONS":
            row["ACTION"] = "Reveal"
        if table == "MASTER_ASSETS":
            row["TYPE"] = "diagram"
        if table == "MASTER_AUDIO_VISUAL_SYNC":
            row["OFFSET_MS"] = "120"
    stage(fixture.brain, fixture.catalog, fixture.output)
    fixture.index = fixture.root / "index.json"
    promote(fixture.output, fixture.catalog, fixture.index)
    yield fixture
    fixture.doCleanups()


def test_pacing_and_recommendations_retain_source_evidence(evidence):
    import query_what_if_forensics as query
    result = query.query_evidence(evidence.output, evidence.catalog, evidence.index)
    assert result["video_count"] == 1
    assert result["observation_count"] == 8
    video = result["videos"][0]
    assert video["youtube_video_id"] == "existing001"
    assert video["shot_pacing"]["mean_duration_seconds"] == 4
    assert video["shot_pacing"]["changes_per_minute"] == 0
    assert video["narration_visual_sync"]["median_offset_ms"] == 120
    assert video["motion_types"]["Reveal"] == 1
    assert video["asset_types"]["diagram"] == 1
    assert len(video["tables"]) == 8
    recommendation = result["recommendations"][0]
    assert recommendation["claim_kind"] == "EVIDENCE_BACKED_HYPOTHESIS"
    assert recommendation["evidence"][0]["source_row_id"] == "ROW1"
    assert recommendation["evidence"][0]["source_video_id"] == "SRC01"
    assert recommendation["evidence"][0]["confidence"] is None
    assert "#row=2" in recommendation["evidence"][0]["source_reference"]


def test_query_rejects_tampered_stage(evidence):
    import query_what_if_forensics as query
    (evidence.output / "MASTER_SHOTS.jsonl").write_text("{}\n")
    with pytest.raises(StagingError, match="changed or missing"):
        query.query_evidence(evidence.output, evidence.catalog, evidence.index)


def test_query_rejects_index_drift(evidence):
    import query_what_if_forensics as query
    payload = json.loads(evidence.index.read_text())
    payload["video_count"] = 100
    evidence.index.write_text(json.dumps(payload))
    with pytest.raises(StagingError, match="promoted index"):
        query.query_evidence(evidence.output, evidence.catalog, evidence.index)


def test_query_excludes_unmatched_ids_and_invalid_durations(evidence):
    import query_what_if_forensics as query
    assert query.query_evidence(evidence.output, evidence.catalog, evidence.index,
                                ["newvideo001"])["videos"] == []
    evidence.brain["tables"]["MASTER_SHOTS"][0]["END_SEC"] = "nan"
    evidence.brain["tables"]["MASTER_SHOTS"][0]["DURATION_SEC"] = "nan"
    output = evidence.root / "invalid-stage"
    stage(evidence.brain, evidence.catalog, output)
    index = evidence.root / "invalid-index.json"
    promote(output, evidence.catalog, index)
    result = query.query_evidence(output, evidence.catalog, index)
    assert result["videos"][0]["shot_pacing"]["mean_duration_seconds"] is None
    assert not any(row.get("kind") == "SHOT_PACING" for row in result["recommendations"])


def test_production_blueprint_consumes_matching_forensic_rows(evidence):
    import run_youtube_intelligence as orchestrator
    plan = {"channel_id": "CH-000004", "opportunity": {"internal_evidence": ["existing001"]},
            "editing": {"blueprint": {"hook_id": "HOOK1"}},
            "global": {"provenance": {}}}
    orchestrator.attach_forensic_guidance(plan, evidence.output, evidence.catalog, evidence.index)
    assert plan["editing"]["blueprint"]["forensic_guidance"][0]["evidence"][0]["source_row_id"] == "ROW1"
    assert plan["editing"]["forensic_consumption"]["channel_samples_added"] == 0
    assert plan["editing"]["blueprint"]["hook_id"] == "HOOK1"


def test_missing_stage_is_explicit_and_other_channels_unchanged(evidence):
    import run_youtube_intelligence as orchestrator
    plan = {"channel_id": "CH-000004", "opportunity": {"internal_evidence": []},
            "editing": {"blueprint": None}, "global": {"provenance": {}}}
    orchestrator.attach_forensic_guidance(plan, evidence.root / "missing", evidence.catalog, evidence.index)
    assert plan["editing"]["forensic_consumption"]["status"] == "NOT_AVAILABLE"
    plan["channel_id"] = "CH-000003"
    plan["editing"].pop("forensic_consumption")
    orchestrator.attach_forensic_guidance(plan, evidence.output, evidence.catalog, evidence.index)
    assert "forensic_consumption" not in plan["editing"]


def test_forensic_enrichment_updates_unavailable_warning(evidence):
    import run_youtube_intelligence as orchestrator
    plan = {"channel_id": "CH-000004", "opportunity": {"internal_evidence": ["existing001"]},
            "editing": {"status": "NOT_AVAILABLE", "reason": "OLD_REASON", "blueprint": None},
            "global": {"provenance": {}, "warnings": ["EDITING NOT_AVAILABLE: OLD_REASON", "KEEP_ME"]}}
    orchestrator.attach_forensic_guidance(plan, evidence.output, evidence.catalog, evidence.index)
    assert plan["editing"]["status"] == "AVAILABLE"
    assert plan["global"]["warnings"] == ["KEEP_ME"]


def test_sync_guidance_preserves_signed_offset_evidence(evidence):
    import query_what_if_forensics as query
    result = query.query_evidence(evidence.output, evidence.catalog, evidence.index)
    sync = [row for row in result["recommendations"] if row.get("kind") == "NARRATION_VISUAL_SYNC"]
    assert len(sync) == 1
    assert sync[0]["observed_median_offset_ms"] == 120
    assert sync[0]["evidence"][0]["source_table"] == "MASTER_AUDIO_VISUAL_SYNC"


def test_guidance_uses_all_eight_source_tables(evidence):
    import query_what_if_forensics as query
    result = query.query_evidence(evidence.output, evidence.catalog, evidence.index)
    tables = {ref["source_table"] for row in result["recommendations"] for ref in row["evidence"]}
    assert tables == {"MASTER_WORDS", "MASTER_SENTENCES", "MASTER_SHOTS", "MASTER_STATES",
                      "MASTER_MOTIONS", "MASTER_ASSETS", "MASTER_AUDIO_EVENTS", "MASTER_AUDIO_VISUAL_SYNC"}
