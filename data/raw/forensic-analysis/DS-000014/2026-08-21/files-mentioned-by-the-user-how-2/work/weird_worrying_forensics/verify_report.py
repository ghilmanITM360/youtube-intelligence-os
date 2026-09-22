from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent.parent
OUTPUTS = PROJECT / "outputs"
REPORT = OUTPUTS / "Weird_and_worrying_questions_forensic_blueprint.md"
SUMMARY = OUTPUTS / "weird_worrying_forensics" / "compliance_summary.txt"
VIDEO = Path("/Users/ghilmanislam360/Downloads/Weird and worrying questions.mp4")
SPEC = Path("/Users/ghilmanislam360/.codex/attachments/4bce5c5d-c67f-4826-91fa-e0dc192c3abf/pasted-text.txt")

errors = []
checks = []

video_hash = hashlib.sha256(VIDEO.read_bytes()).hexdigest()
spec_hash = hashlib.sha256(SPEC.read_bytes()).hexdigest()
if video_hash != "eafaf03040a83da4836eb51847d512f2616a8c6deb65d5ee5431a9cf7be574d7":
    errors.append("source video SHA-256 changed")
if spec_hash != "ac389faf066e66f71ae2e5a6530d7c3ec785a1434831706f6421dee521c8ce51":
    errors.append("request specification SHA-256 changed")
checks.append("source fingerprints: PASS" if not errors else "source fingerprints: FAIL")

with (ROOT / "state_manifest.tsv").open() as handle:
    states = list(csv.DictReader(handle, delimiter="\t"))
with (ROOT / "shot_manifest.tsv").open() as handle:
    shots = list(csv.DictReader(handle, delimiter="\t"))
with (ROOT / "asset_manifest.tsv").open() as handle:
    assets = list(csv.DictReader(handle, delimiter="\t"))
with (ROOT / "motion_manifest.tsv").open() as handle:
    events = list(csv.DictReader(handle, delimiter="\t"))
transcript = json.loads((ROOT / "transcript.json").read_text())
ocr_rows = list(csv.DictReader((ROOT / "ocr_selected.tsv").read_text().splitlines(), delimiter="\t"))

if (len(shots), len(states), len(assets), len(events), len(transcript["segments"]), len(ocr_rows)) != (7, 34, 33, 39, 8, 159):
    errors.append("manifest/transcript/OCR count mismatch")
checks.append(f"evidence counts: shots={len(shots)} states={len(states)} assets={len(assets)} events={len(events)} transcript_segments={len(transcript['segments'])} OCR={len(ocr_rows)}")

expected_visuals = [f"V{index:02d}" for index in range(1, 35)]
expected_events = [f"A{index:02d}" for index in range(1, 40)]
if [row["visual"] for row in states] != expected_visuals:
    errors.append("visual IDs are not complete and ordered")
if [row["animation"] for row in events] != expected_events:
    errors.append("animation IDs are not complete and ordered")

for index, state in enumerate(states):
    start = float(state["start"])
    end = float(state["end"])
    if end <= start:
        errors.append(f"non-positive state duration: {state['visual']}")
    if index and abs(start - float(states[index - 1]["end"])) > 0.001:
        errors.append(f"state timeline gap/overlap before {state['visual']}")
if abs(float(states[0]["start"])) > 0.001 or abs(float(states[-1]["end"]) - 47.502) > 0.001:
    errors.append("state timeline does not cover full source")
checks.append("state timeline coverage: PASS" if not any("state" in item and ("duration" in item or "timeline" in item) for item in errors) else "state timeline coverage: FAIL")

state_ids = set(expected_visuals)
incoming = {visual: 0 for visual in expected_visuals}
max_prompt = 0
for event in events:
    source = event["source"].split("/")[0]
    target = event["target"].split("/")[0]
    if source not in state_ids or target not in state_ids:
        errors.append(f"invalid event state link: {event['animation']}")
    incoming[target] += 1
    max_prompt = max(max_prompt, len(event["prompt"]))
    if len(event["prompt"]) > 500:
        errors.append(f"prompt ceiling exceeded: {event['animation']}")
if any(incoming[visual] == 0 for visual in expected_visuals[1:]):
    errors.append("one or more non-opening states have no incoming/loop event")
checks.append(f"event linkage and prompt ceiling: PASS (max {max_prompt}/500)" if max_prompt <= 500 else "event linkage and prompt ceiling: FAIL")

text = REPORT.read_text()
card_starts = list(re.finditer(r"^## (V\d{2}) — ", text, re.MULTILINE))
if [match.group(1) for match in card_starts] != expected_visuals:
    errors.append("report card order/count mismatch")
for index, match in enumerate(card_starts):
    end = card_starts[index + 1].start() if index + 1 < len(card_starts) else len(text)
    card = text[match.start() : end]
    numbered = [int(value) for value in re.findall(r"^### (\d+)\. ", card, re.MULTILINE)]
    if numbered != list(range(1, 29)):
        errors.append(f"28-section schema failure: {match.group(1)}")
if len(re.findall(r"^#### ANIMATION A\d{2}$", text, re.MULTILINE)) != 39:
    errors.append("rendered animation-card count mismatch")
if text.count("**STANDALONE IMAGE PROMPT:**") != 34 or text.count("**BAKE TEXT:** NO") != 34:
    errors.append("image prompt/text-decision count mismatch")
if "**STATUS:** FAIL" in text:
    errors.append("failed prompt status present")
for marker in ("TO" + "DO", "T" + "BD", "PLACE" + "HOLDER", "FILL" + " ME"):
    if marker in text.upper():
        errors.append(f"unresolved marker present: {marker}")
checks.append(f"report structure: cards={len(card_starts)} sections={len(card_starts) * 28} animation_cards=39")

keyframes = sorted((OUTPUTS / "weird_worrying_forensics" / "keyframes").glob("V*.jpg"))
if len(keyframes) != 34:
    errors.append("full-resolution keyframe count mismatch")
for path in keyframes:
    with Image.open(path) as image:
        if image.size != (720, 1280):
            errors.append(f"wrong keyframe dimensions: {path.name} {image.size}")
    if f"weird_worrying_forensics/keyframes/{path.name}" not in text:
        errors.append(f"report missing keyframe link: {path.name}")
checks.append(f"source images: {len(keyframes)}/34 at 720x1280 with report links")

visual_files = [
    OUTPUTS / "weird_worrying_forensics" / "state_atlas_01.jpg",
    OUTPUTS / "weird_worrying_forensics" / "state_atlas_02.jpg",
    OUTPUTS / "weird_worrying_forensics" / "transition_atlas_01.jpg",
    OUTPUTS / "weird_worrying_forensics" / "transition_atlas_02.jpg",
    OUTPUTS / "weird_worrying_forensics" / "transition_atlas_03.jpg",
    OUTPUTS / "weird_worrying_forensics" / "audio_envelope.png",
    OUTPUTS / "weird_worrying_forensics" / "spectrogram.png",
]
visual_dimensions = []
for path in visual_files:
    if not path.exists() or path.stat().st_size == 0:
        errors.append(f"missing/empty delivery visual: {path.name}")
        continue
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        visual_dimensions.append(f"{path.name}={image.width}x{image.height}")
checks.append("delivery visuals: " + ", ".join(visual_dimensions))

dense_rows = sum(1 for _ in (ROOT / "analysis" / "dense_metrics.tsv").open()) - 1
proxy_images = len(list((ROOT / "proxy_frames").glob("frame_*ms.jpg")))
dense_images = len(list((ROOT / "dense_frames").glob("frame_*ms.jpg")))
if (proxy_images, dense_images, dense_rows) != (191, 1141, 1141):
    errors.append("decoded frame/metric completeness mismatch")
checks.append(f"decoded evidence: proxy={proxy_images}/191 dense={dense_images}/1141 metric_rows={dense_rows}/1141")

required_report_tokens = [
    "# Engine A — Script Intelligence",
    "# Engine B — Visual Intelligence",
    "# Engine C — Reconstruction and Motion Intelligence",
    "# Editing Decision List",
    "# Audio Intelligence",
    "# Thumbnail and Shorts Extraction",
    "# Engine D — Master Production Synthesis",
    "# Zero-to-Final Rebuild Order",
    "VISUAL CARDS: 34/34",
    "AI PROMPTS ≤500: 39/39",
]
for token in required_report_tokens:
    if token not in text:
        errors.append(f"required report section/token missing: {token}")

status = "PASS" if not errors else "FAIL"
summary_lines = [
    "WEIRD AND WORRYING QUESTIONS — V7.0 COMPLIANCE SUMMARY",
    f"STATUS={status}",
    f"SOURCE_VIDEO_SHA256={video_hash}",
    f"REQUEST_SPEC_SHA256={spec_hash}",
    f"REPORT_BYTES={REPORT.stat().st_size}",
    *checks,
    f"ERROR_COUNT={len(errors)}",
]
summary_lines.extend(f"ERROR={error}" for error in errors)
SUMMARY.write_text("\n".join(summary_lines) + "\n")
print(SUMMARY.read_text(), end="")
if errors:
    raise SystemExit(1)
