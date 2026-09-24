from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/moon_protons_forensics"
OUTPUTS = ROOT / "outputs"
REPORT = OUTPUTS / "What_if_the_Moon_were_made_of_Protons_forensic_blueprint.md"
failures: list[str] = []
results: list[str] = []


def check(condition: bool, message: str) -> None:
    status = "PASS" if condition else "FAIL"
    results.append(f"{status}\t{message}")
    if not condition:
        failures.append(message)


text = REPORT.read_text()
cards = re.split(r"(?=^## V\d{2} — )", text, flags=re.M)[1:]
check(len(cards) == 39, f"39 visual cards (found {len(cards)})")
bad_sections = []
for card in cards:
    card_id = re.match(r"## (V\d{2})", card).group(1)
    headings = [int(value) for value in re.findall(r"^### (\d+)\.", card, flags=re.M)]
    if headings != list(range(1, 29)):
        bad_sections.append((card_id, headings))
check(not bad_sections, f"1–28 sequence in every visual card (bad {len(bad_sections)})")

events = re.findall(r"^#### ANIMATION (A\d{2})", text, flags=re.M)
check(events == [f"A{index:02d}" for index in range(1, 29)], f"28 unique ordered animation cards (found {len(events)})")
prompts = re.findall(
    r'^\*\*AI PROMPT:\*\* “([^”]*)”\s+\*\*CHARACTER COUNT:\*\* (\d+) / 500\s+\*\*STATUS:\*\* PASS',
    text,
    flags=re.M,
)
bad_prompts = [(len(prompt), int(reported)) for prompt, reported in prompts if len(prompt) != int(reported) or len(prompt) > 500]
check(len(prompts) == 28 and not bad_prompts, f"28 exact animation-prompt counts <=500 (max {max((len(p) for p, _ in prompts), default=0)})")

image_prompts = text.count("**EXACT STANDALONE IMAGE PROMPT:**")
bake_decisions = text.count("**BAKE TEXT:**")
check(image_prompts == 39, f"39 standalone image prompts (found {image_prompts})")
check(bake_decisions == 39, f"39 text bake/overlay decisions (found {bake_decisions})")

links = re.findall(r"\]\((moon_protons_forensics/keyframes/[^)]+\.jpg)\)", text)
missing = [link for link in links if not (OUTPUTS / link).exists()]
check(len(links) == 39 and not missing, f"39 report keyframe links resolve (found {len(links)}, missing {len(missing)})")

keyframes = sorted((OUTPUTS / "moon_protons_forensics/keyframes").glob("V*.jpg"))
bad_dimensions = []
for path in keyframes:
    with Image.open(path) as image:
        if image.size != (720, 1280):
            bad_dimensions.append((path.name, image.size))
check(len(keyframes) == 39 and not bad_dimensions, f"39 full-resolution 720x1280 keyframes (found {len(keyframes)})")

atlases = sorted((OUTPUTS / "moon_protons_forensics").glob("keyframe_atlas_*.jpg"))
check(len(atlases) == 5 and all(path.stat().st_size > 50_000 for path in atlases), f"5 nonempty atlas pages (found {len(atlases)})")

proxy_manifest = (WORK / "proxy_frames/manifest.tsv").read_text().splitlines()
dense_manifest = (WORK / "dense_frames/manifest.tsv").read_text().splitlines()
check(len(proxy_manifest) == 354, f"353 proxy frames plus header (lines {len(proxy_manifest)})")
check(len(dense_manifest) == 2117, f"2,116 dense frames plus header (lines {len(dense_manifest)})")

transcript = json.loads((WORK / "transcript.json").read_text())
check(len(transcript.get("segments", [])) == 24, f"24 transcript segments (found {len(transcript.get('segments', []))})")
ocr_lines = (WORK / "ocr_selected.tsv").read_text().splitlines()
check(len(ocr_lines) == 107, f"106 selected-frame OCR detections plus header (lines {len(ocr_lines)})")
state_manifest = (WORK / "state_manifest.tsv").read_text().splitlines()
check(len(state_manifest) == 40, f"39 visual states plus header (lines {len(state_manifest)})")

check(len(re.findall(r"^\| S\d{2} \|", text, flags=re.M)) >= 14, "14-shot EDL present")
check(len(re.findall(r"^\| B\d{2} \|", text, flags=re.M)) == 16, "16 script beats present")
check("PERSISTENT ASSETS: 31" in text, "31 persistent assets audited")
check("MOTION EVENTS IDENTIFIED: 28/28" in text, "motion completeness audit agrees")
check("AI PROMPTS ≤500: 28/28" in text, "prompt completeness audit agrees")
check("EDL: COMPLETE" in text and "MASTER SYNTHESIS: COMPLETE" in text, "EDL and master synthesis complete")

required_engines = ["ENGINE A", "ENGINE B", "ENGINE C", "ENGINE D", "Audio map", "Thumbnail frame candidates", "Shorts candidates", "Final quality gate"]
check(all(label in text for label in required_engines), "all required engine/extraction/quality-gate sections present")
for forbidden in ("TODO", "PLACEHOLDER", "AUTO / 500", "TBD", "implement later", "fill in details"):
    check(forbidden not in text, f"no unresolved marker: {forbidden}")
check(REPORT.stat().st_size > 500_000, f"report is substantive ({REPORT.stat().st_size} bytes)")

results.append(f"SUMMARY\tfailures={len(failures)} cards={len(cards)} events={len(events)} prompts={len(prompts)} keyframes={len(keyframes)} words={len(text.split())}")
if failures:
    results.append("VERIFICATION FAIL\t" + " | ".join(failures))
    output = "\n".join(results) + "\n"
    (WORK / "verification.txt").write_text(output)
    print(output, end="")
    raise SystemExit(1)
results.append("VERIFICATION PASS\tall checks")
output = "\n".join(results) + "\n"
(WORK / "verification.txt").write_text(output)
print(output, end="")
