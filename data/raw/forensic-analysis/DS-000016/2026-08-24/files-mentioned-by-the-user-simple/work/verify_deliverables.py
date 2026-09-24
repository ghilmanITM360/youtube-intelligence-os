import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path


root = Path(__file__).resolve().parent.parent
out = root / "outputs"
failures = []


def require(condition, message):
    if not condition:
        failures.append(message)


required = [
    "forensic_report.md",
    "visual_reconstruction_cards.md",
    "visual_catalog.csv",
    "animation_prompts.csv",
    "edl.csv",
    "script_beats.md",
    "transcript.txt",
    "transcript.srt",
    "transcript.json",
    "shot_manifest.json",
    "audio_summary.json",
    "audio_envelope.csv",
    "audio_envelope.png",
]
for name in required:
    require((out / name).is_file(), f"missing required file: {name}")

cards = (out / "visual_reconstruction_cards.md").read_text(encoding="utf-8")
report = (out / "forensic_report.md").read_text(encoding="utf-8")
visual_ids = re.findall(r"^# (V\d{3}) —", cards, re.MULTILINE)
require(visual_ids == [f"V{i:03d}" for i in range(1, 254)], "visual card IDs missing, duplicated or out of order")
for section in range(1, 29):
    count = len(re.findall(rf"^## {section}\.", cards, re.MULTILINE))
    require(count == 253, f"section {section} appears {count} times instead of 253")

placeholder_pattern = re.compile(r"\{(?:text_value|state_end|motion|shot|visual|index|prompt)[^\n}]*\}")
require(not placeholder_pattern.search(cards), "unresolved template placeholder in visual cards")
require(not placeholder_pattern.search(report), "unresolved template placeholder in report")

prompt_rows = list(csv.DictReader((out / "animation_prompts.csv").open(encoding="utf-8")))
require(len(prompt_rows) == 253, f"animation prompt rows: {len(prompt_rows)}")
moving_prompts = [row for row in prompt_rows if row["animation_id"] != "N/A"]
require(len(moving_prompts) == 225, f"moving prompt rows: {len(moving_prompts)}")
for row in prompt_rows:
    actual = 0 if row["ai_prompt"] == "N/A" else len(row["ai_prompt"])
    require(actual == int(row["character_count"]), f"prompt count mismatch: {row['shot_id']}")
    require(actual <= 500, f"prompt exceeds 500 characters: {row['shot_id']} ({actual})")
    require(row["status"] == "PASS", f"prompt not marked PASS: {row['shot_id']}")

catalog = list(csv.DictReader((out / "visual_catalog.csv").open(encoding="utf-8")))
edl = list(csv.DictReader((out / "edl.csv").open(encoding="utf-8")))
require(len(catalog) == 253, f"catalog rows: {len(catalog)}")
require(len(edl) == 253, f"EDL rows: {len(edl)}")
for left, right in zip(edl, edl[1:]):
    require(left["out"] == right["in"], f"EDL discontinuity: {left['shot_id']} → {right['shot_id']}")

manifest = json.loads((out / "shot_manifest.json").read_text(encoding="utf-8"))
require(len(manifest) == 253, f"manifest shots: {len(manifest)}")
require(manifest[0]["in_timestamp"] == "00:00:00.000", "manifest does not start at zero")
require(manifest[-1]["out_timestamp"] == "00:14:03.636", "manifest has wrong end time")
classes = Counter(item["global_motion_estimate"]["classification"].split("+")[0] for item in manifest)
require(classes == Counter({"content_shifts_down_camera_up": 77, "content_shifts_up_camera_down": 75, "digital_push_in": 73, "static_hold": 28}), f"motion counts differ: {dict(classes)}")

transcript = json.loads((out / "transcript.json").read_text(encoding="utf-8"))
require(len(transcript["segments"]) == 282, f"transcript segments: {len(transcript['segments'])}")
require(transcript["language"] == "en", f"transcript language: {transcript['language']}")

audio = json.loads((out / "audio_summary.json").read_text(encoding="utf-8"))
require(audio["sample_rate"] == 16000, f"audio analysis sample rate: {audio['sample_rate']}")
require(abs(audio["duration_seconds"] - 843.650625) < 0.05, f"audio duration: {audio['duration_seconds']}")

evidence = out / "evidence"
require(len(list(evidence.glob("shot_montage_*.jpg"))) == 16, "shot montage page count differs")
require(len(list(evidence.glob("motion_triplets_*.jpg"))) == 32, "motion triplet page count differs")
require((evidence / "overview_contact_sheet.jpg").is_file(), "overview contact sheet missing")
reference_frames = list((evidence / "reference_frames").glob("*.jpg"))
require(len(reference_frames) == 253, f"reference frame count: {len(reference_frames)}")
for item in manifest:
    require((evidence / "reference_frames" / item["sample_files"]["mid"]).is_file(), f"missing reference frame for {item['shot_id']}")

required_report_sections = [
    "## Executive finding",
    "## Pass 0 — media inspection",
    "## Engine A — script intelligence",
    "## Engine B — visual intelligence",
    "## Engine C — reconstruction and motion intelligence",
    "## Audio intelligence",
    "## Engine D — master synthesis",
    "## Completeness audit",
    "## Final quality gate",
    "## Limitations stated exactly",
]
for heading in required_report_sections:
    require(heading in report, f"missing report section: {heading}")

if failures:
    print(f"FAIL: {len(failures)} verification error(s)")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)

total_bytes = sum(path.stat().st_size for path in out.rglob("*") if path.is_file())
print("PASS: deliverable verification complete")
print("253 visual cards × 28 required sections")
print("225 moving prompts; all character counts match and all are ≤500")
print("253 EDL rows; contiguous from 00:00:00.000 to 00:14:03.636")
print(f"Motion classes verified: {dict(classes)}")
print("49 contact/motion evidence sheets + 253 reference frames")
print(f"Total deliverable size: {total_bytes} bytes")
