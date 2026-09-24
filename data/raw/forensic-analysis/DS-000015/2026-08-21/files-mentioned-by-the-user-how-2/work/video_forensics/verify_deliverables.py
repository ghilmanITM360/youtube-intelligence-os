from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image


root = Path(__file__).resolve().parents[2]
outputs = root / "outputs"
report = outputs / "How_long_could_you_drive_towards_the_sunset_forensic_blueprint.md"
text = report.read_text()
failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        print(f"PASS\t{message}")
    else:
        print(f"FAIL\t{message}")
        failures.append(message)


cards = re.split(r"(?=^## V\d{2} — )", text, flags=re.M)[1:]
check(len(cards) == 34, f"34 visual cards (found {len(cards)})")
for card in cards:
    card_id = re.match(r"## (V\d{2})", card).group(1)
    sections = [int(x) for x in re.findall(r"^### C(\d+)\.", card, flags=re.M)]
    if sections != list(range(1, 27)):
        failures.append(f"{card_id} section sequence")
check(not any("section sequence" in f for f in failures), "C1–C26 sequence in every visual card")

prompts = re.findall(
    r'^\*\*ANIMATION PROMPT:\*\* “([^”]*)”  \n\*\*CHARACTER COUNT:\*\* (\d+) / 500',
    text,
    flags=re.M,
)
check(len(prompts) == 34, f"34 animation prompts (found {len(prompts)})")
bad_counts = [(len(p), int(c)) for p, c in prompts if len(p) != int(c) or int(c) > 500]
check(not bad_counts, f"animation prompt counts exact and <=500 (max {max(map(lambda x: int(x[1]), prompts), default=0)})")

links = re.findall(r"\]\((keyframes/[^)]+\.jpg)\)", text)
missing_links = [link for link in links if not (outputs / link).exists()]
check(len(links) == 34 and not missing_links, f"34 report keyframe links resolve (found {len(links)}, missing {len(missing_links)})")

keyframes = sorted((outputs / "keyframes").glob("V*.jpg"))
bad_dims = []
for path in keyframes:
    with Image.open(path) as image:
        if image.size != (720, 1280):
            bad_dims.append((path.name, image.size))
check(len(keyframes) == 34 and not bad_dims, f"34 full-resolution 720x1280 keyframes (found {len(keyframes)})")

atlases = sorted(outputs.glob("keyframe_atlas_*.jpg"))
check(len(atlases) == 5 and all(p.stat().st_size > 50_000 for p in atlases), f"5 non-empty keyframe atlas pages (found {len(atlases)})")

transcript = json.loads((root / "work/video_forensics/transcript.json").read_text())
check(len(transcript.get("segments", [])) == 44, f"44 transcript segments (found {len(transcript.get('segments', []))})")

dense_manifest = (root / "work/video_forensics/dense_frames/manifest.tsv").read_text().splitlines()
check(len(dense_manifest) == 3120, f"3,119 dense source frames plus header (lines {len(dense_manifest)})")

boundaries = (root / "work/video_forensics/analysis/refined_boundaries.tsv").read_text().splitlines()
check(len(boundaries) == 19, f"18 verified shot-transition candidates plus header (lines {len(boundaries)})")

for forbidden in ("AUTO / 500", "TODO", "PLACEHOLDER"):
    check(forbidden not in text, f"no unresolved marker: {forbidden}")

check(report.stat().st_size > 190_000, f"report is substantive ({report.stat().st_size} bytes)")

if failures:
    print(f"VERIFICATION FAILURES\t{len(failures)}")
    raise SystemExit(1)
print("VERIFICATION PASS\tall checks")
