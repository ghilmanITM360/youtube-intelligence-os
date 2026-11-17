"""Regression test for the AI-slop risk gate's pure checks (scripts/check_slop_risk.py)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from check_slop_risk import ROOT, evaluate, front_matter, is_script, project_of, split_sources  # noqa: E402

ORIGINAL = ("We measured our own grip strength every morning for thirty days and logged each reading in a notebook. "
            "The numbers drifted upward after the second week once we added a simple towel squeeze before breakfast. ") * 6
COMPETITOR = ("Last night you went to bed feeling perfectly fine no chest pain no dizziness nothing unusual at all "
              "but your body was quietly sending a signal that most seniors over sixty completely ignore every day ") * 6
SRC = "\n\n## Sources\n- our grip log, 2026-10\n"


def rules(findings, level):
    return {f['rule'] for f in findings if f['level'] == level}


def test_clean_original_script_passes():
    f = evaluate(ORIGINAL + SRC, 'Our 30-day grip test', [('C/v1', COMPETITOR)], [('C/v1', 'Over 60? Never ignore this')], [], [])
    assert not rules(f, 'FAIL'), f


def test_copied_script_title_persona_and_missing_sources_fail():
    text = "As a doctor I see this daily. " + COMPETITOR + " In today's video let's dive in, it's important to note this."
    f = evaluate(text, 'Over 60? Never Ignore This!', [('C/v1', COMPETITOR)], [('C/v1', 'over 60  never ignore this')], [], [])
    assert {'R1', 'R2', 'R5', 'R6'} <= rules(f, 'FAIL'), f
    assert 'R3' in rules(f, 'WARN'), f


def test_verified_presenter_and_image_hash():
    f = evaluate("As a doctor I measured this. " + ORIGINAL + SRC, 't', [], [], [('ref.jpg', 0b1011)], [],
                 images=[('ours.png', 0b1011)], verified_presenter=True)
    assert 'R6' not in rules(f, 'FAIL') and 'R7' in rules(f, 'FAIL'), f


def test_sources_section_excluded_from_body():
    body, ok = split_sources("text\nSources:\n- a\n")
    assert ok and 'Sources' not in body
    assert split_sources("text\n## Sources\n\n")[1] is False
    assert split_sources("text\nSources: FACT_CHECK.md\n")[1] is True
    assert split_sources("Sources and claim IDs are elsewhere.")[1] is False


def test_reuse_of_our_own_other_project_fails():
    own = [('productions/other/FINAL_SCRIPT.md', 'Our 30-day grip test', ORIGINAL + SRC)]
    f = evaluate(ORIGINAL + SRC, 'Our 30-day grip test', [], [], [], own)
    assert {'R2', 'R4'} <= rules(f, 'FAIL'), f


def test_front_matter_and_script_paths():
    meta, body = front_matter("---\ntitle: A: B\nchannel: CH-000001\n---\nHello\n")
    assert meta == {'title': 'A: B', 'channel': 'CH-000001'} and body == 'Hello\n'
    assert front_matter("no header")[0] == {}
    assert is_script(ROOT / 'productions/fs-01/experiment/FINAL_SCRIPT.md')
    assert project_of(ROOT / 'productions/fs-01/experiment/FINAL_SCRIPT.md') == 'fs-01'
    assert not is_script(ROOT / 'productions/fs-01/FACT_CHECK.md')
    assert not is_script(ROOT / 'research/x/SCRIPT_INTELLIGENCE.md')
    assert not is_script(ROOT / 'productions/fs-01/FINAL_SCRIPT.md.slop-risk.json')
