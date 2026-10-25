#!/usr/bin/env python3
"""Self-contained validator for what_if_all_visible_light_was_a_single_beam.
Run: python3 00_source/verify.py   (from this video's project root)
Stdlib only. Prints PASS or raises AssertionError on the first failure.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read_csv(name):
    with open(ROOT / "02_analysis" / name, newline="") as f:
        return list(csv.DictReader(f))

def read_text(rel):
    return (ROOT / rel).read_text()

# ---- Timeline coverage ----
timeline = read_csv("TIMELINE.csv")
assert len(timeline) == 33, f"expected 33 states, got {len(timeline)}"
rows = sorted(timeline, key=lambda r: int(r["IN"]))
expected_in = 0
total_frames = 0
for r in rows:
    in_f, out_f = int(r["IN"]), int(r["OUT"])
    assert in_f == expected_in, f"gap/overlap before state {r['STATE_ID']}: expected IN={expected_in}, got {in_f}"
    assert out_f >= in_f, f"invalid range in state {r['STATE_ID']}"
    dur_frames = int(r["DURATION"].split("/")[0])
    assert dur_frames == out_f - in_f + 1, f"duration mismatch in state {r['STATE_ID']}"
    expected_in = out_f + 1
    total_frames += dur_frames
assert total_frames == 3718, f"total frames {total_frames} != 3718"
assert rows[-1]["OUT"] == "3717", "timeline does not reach the last frame (3717)"

shots = sorted(set(r["SHOT_ID"] for r in timeline), key=lambda s: int(s[1:]))
assert shots == [f"S{n:02d}" for n in range(1, 16)], f"unexpected shot set: {shots}"

# ---- Asset manifest ----
assets = read_csv("ASSET_MANIFEST.csv")
assert len(assets) == 30, f"expected 30 assets, got {len(assets)}"
asset_ids = set(a["ASSET_ID"] for a in assets)
assert len(asset_ids) == 30, "duplicate ASSET_ID found"

def split_ids(s):
    return [x.strip() for x in s.split(";") if x.strip()]

referenced_assets = set()
for r in timeline:
    referenced_assets |= set(split_ids(r["ASSET_IDS"]))
missing = referenced_assets - asset_ids
assert not missing, f"TIMELINE references unknown asset IDs: {missing}"

# ---- Motion events ----
motions = read_csv("MOTION_EVENTS.csv")
assert len(motions) == 18, f"expected 18 motion events, got {len(motions)}"
motion_ids = set(m["MOTION_ID"] for m in motions)
assert motion_ids == {f"A{n:02d}" for n in range(1, 19)}, f"unexpected motion ID set: {sorted(motion_ids)}"
for m in motions:
    assert m["SHOT_ID"] in shots, f"motion {m['MOTION_ID']} references unknown shot {m['SHOT_ID']}"
    assert int(m["OUT"]) >= int(m["IN"]), f"motion {m['MOTION_ID']} has invalid IN/OUT"

# every non-static-hold state's MOTION_IDS field (when not N/A) must resolve
referenced_motions = set()
for r in timeline:
    for mid in split_ids(r["MOTION_IDS"]):
        if mid.startswith("A") and mid[1:].isdigit():
            referenced_motions.add(mid)
missing_m = referenced_motions - motion_ids
assert not missing_m, f"TIMELINE references unknown motion IDs: {missing_m}"

# ---- CapCut guide ----
capcut = read_text("03_capcut/CAPCUT_REBUILD.md")
for s in shots:
    assert re.search(rf"^## {s} ", capcut, re.M), f"CAPCUT_REBUILD.md missing header for {s}"
for mid in sorted(motion_ids):
    assert mid in capcut, f"CAPCUT_REBUILD.md never references motion {mid}"

# ---- Image prompts ----
img_prompts = read_text("04_image_to_video/IMAGE_PROMPTS.md")
img_headers = re.findall(r"^## (IMG\d+)$", img_prompts, re.M)
assert len(img_headers) == 13, f"expected 13 IMG headers, got {len(img_headers)}"
assert img_headers == [f"IMG{n:02d}" for n in range(1, 14)], f"unexpected/non-sequential IMG headers: {img_headers}"
assert img_prompts.count("TEXT BAKED: NO") == 12, "expected 12 standalone image prompts declaring TEXT BAKED: NO (IMG08 is a reuse stub with no prompt of its own)"

# ---- Animation prompts ----
anim = read_text("04_image_to_video/ANIMATION_PROMPTS.md")
anim_headers = re.findall(r"^## (A\d+)$", anim, re.M)
assert set(anim_headers) == motion_ids, f"ANIMATION_PROMPTS.md headers {sorted(anim_headers)} != motion set {sorted(motion_ids)}"
for block in re.split(r"^## A\d+$", anim, flags=re.M)[1:]:
    m = re.search(r"ANIMATION PROMPT:\s*(.+?)(?:\n##|\Z)", block, re.S)
    assert m, "a motion block is missing its ANIMATION PROMPT line"
    prompt_text = m.group(1).strip()
    assert 1 <= len(prompt_text) <= 500, f"animation prompt out of 1-500 char range ({len(prompt_text)} chars)"

# ---- I2V guide ----
i2v = read_text("04_image_to_video/I2V_REBUILD.md")
for s in shots:
    assert re.search(rf"^## {s} ", i2v, re.M), f"I2V_REBUILD.md missing header for {s}"

# ---- Audio map sanity ----
audio_map = read_text("05_audio/AUDIO_MAP.md")
assert "UNAVAILABLE" in audio_map, "AUDIO_MAP.md should record that transcript is unavailable"
assert audio_map.count("75.226") + audio_map.count("75.2") >= 1, "AUDIO_MAP.md missing first measured silence gap"

# ---- Cross-project markdown link check ----
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md_file in ROOT.rglob("*.md"):
    text = md_file.read_text(errors="ignore")
    for target in link_re.findall(text):
        if target.startswith("http") or target.startswith("#"):
            continue
        target_path = (md_file.parent / target.split("#")[0]).resolve()
        assert target_path.exists(), f"{md_file.relative_to(ROOT)} has a broken link to {target}"

# ---- RUN_STATE.json counts (if present and populated) ----
run_state_path = ROOT / "RUN_STATE.json"
if run_state_path.exists():
    run_state = json.loads(run_state_path.read_text())
    counts = run_state.get("counts")
    if counts:
        assert counts["shots"] == 15
        assert counts["visual_states"] == 33
        assert counts["unique_assets"] == 30
        assert counts["motion_events"] == 18
        assert counts["unique_images"] == 13

print("PASS: timeline coverage, asset/motion ID cross-refs, CapCut shot+motion coverage, "
      "image/animation prompt counts and length limits, I2V shot coverage, audio map sanity, "
      "and file links.")
