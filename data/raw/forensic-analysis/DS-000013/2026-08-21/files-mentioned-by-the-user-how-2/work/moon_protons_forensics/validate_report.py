from __future__ import annotations

import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "outputs/What_if_the_Moon_were_made_of_Protons_forensic_blueprint.md"
OUTPUTS = ROOT / "outputs"

if not REPORT.exists():
    raise AssertionError(f"report is missing: {REPORT}")

text = REPORT.read_text()
cards = re.split(r"(?=^## V\d{2} — )", text, flags=re.M)[1:]
assert len(cards) == 39, f"expected 39 cards, found {len(cards)}"

for card in cards:
    card_id = re.match(r"## (V\d{2})", card).group(1)
    sections = [int(value) for value in re.findall(r"^### (\d+)\.", card, flags=re.M)]
    assert sections == list(range(1, 29)), f"{card_id}: section sequence {sections}"
    assert "**EXACT STANDALONE IMAGE PROMPT:**" in card, f"{card_id}: missing image prompt"
    assert "**BAKE TEXT:**" in card, f"{card_id}: missing text decision"

event_cards = re.findall(r"^#### ANIMATION (A\d{2})", text, flags=re.M)
assert event_cards == [f"A{index:02d}" for index in range(1, 29)], event_cards

prompts = re.findall(
    r'^\*\*AI PROMPT:\*\* “([^”]*)”\s+\*\*CHARACTER COUNT:\*\* (\d+) / 500\s+\*\*STATUS:\*\* PASS',
    text,
    flags=re.M,
)
assert len(prompts) == 28, f"expected 28 prompts, found {len(prompts)}"
for prompt, reported_count in prompts:
    assert len(prompt) == int(reported_count), (len(prompt), reported_count, prompt)
    assert len(prompt) <= 500, f"prompt exceeds limit: {len(prompt)}"

links = re.findall(r"\]\((moon_protons_forensics/keyframes/[^)]+\.jpg)\)", text)
assert len(links) == 39, f"expected 39 keyframe links, found {len(links)}"
assert all((OUTPUTS / link).exists() for link in links), "missing report keyframe link"

keyframes = sorted((OUTPUTS / "moon_protons_forensics/keyframes").glob("V*.jpg"))
assert len(keyframes) == 39, len(keyframes)
for keyframe in keyframes:
    with Image.open(keyframe) as image:
        assert image.size == (720, 1280), (keyframe.name, image.size)

atlases = sorted((OUTPUTS / "moon_protons_forensics").glob("keyframe_atlas_*.jpg"))
assert len(atlases) == 5, len(atlases)
assert all(atlas.stat().st_size > 50_000 for atlas in atlases)

assert len(re.findall(r"^\| B\d{2} \|", text, flags=re.M)) == 16, "script beat count"
assert len(re.findall(r"^\| S\d{2} \|", text, flags=re.M)) >= 14, "EDL count"
assert "VISUAL CARDS: 39/39" in text
assert "MOTION EVENTS IDENTIFIED: 28/28" in text
assert "AI PROMPTS ≤500: 28/28" in text
for forbidden in ("TODO", "PLACEHOLDER", "AUTO / 500"):
    assert forbidden not in text, forbidden
assert REPORT.stat().st_size > 180_000, REPORT.stat().st_size

print(f"cards={len(cards)}")
print(f"events={len(event_cards)}")
print(f"prompts={len(prompts)}")
print(f"max_prompt_chars={max(len(prompt) for prompt, _ in prompts)}")
print(f"keyframes={len(keyframes)}")
print(f"atlas_pages={len(atlases)}")
print(f"bytes={REPORT.stat().st_size}")
print(f"words={len(text.split())}")
print("VALIDATION PASS")
