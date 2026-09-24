from __future__ import annotations

import csv
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from forensic_analysis import transition_marker


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent.parent
OUT = PROJECT / "outputs" / "weird_worrying_forensics"
KEYFRAMES = OUT / "keyframes"
OUT.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default(size=18)

with (ROOT / "state_manifest.tsv").open() as handle:
    states = list(csv.DictReader(handle, delimiter="\t"))
paths = {path.name[:3]: path for path in sorted(KEYFRAMES.glob("V*.jpg"))}

# Two chronological state-atlas pages.
for page, start in enumerate(range(0, len(states), 17), 1):
    batch = states[start : start + 17]
    columns, cell_w, cell_h = 5, 220, 420
    rows = math.ceil(len(batch) / columns)
    canvas = Image.new("RGB", (columns * cell_w, rows * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for index, state in enumerate(batch):
        image = Image.open(paths[state["visual"]]).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 12, cell_h - 58), Image.Resampling.LANCZOS)
        left = index % columns * cell_w
        top = index // columns * cell_h
        canvas.paste(image, (left + (cell_w - image.width) // 2, top + 50))
        draw.text((left + 7, top + 5), f"{state['visual']}  {float(state['representative']):06.3f}s", fill="white", font=font)
        draw.text((left + 7, top + 27), state["state"], fill="#9ed0ff", font=font)
    canvas.save(OUT / f"state_atlas_{page:02d}.jpg", quality=93)

# Three source→target transition pages, 11 pairs/page.
pairs = list(zip(states[:-1], states[1:], strict=True))
for page, start in enumerate(range(0, len(pairs), 11), 1):
    batch = pairs[start : start + 11]
    pairs_per_row, pair_w, row_h = 2, 550, 390
    canvas = Image.new("RGB", (pairs_per_row * pair_w, math.ceil(len(batch) / pairs_per_row) * row_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for index, (source, target) in enumerate(batch):
        pair_left = index % pairs_per_row * pair_w
        top = index // pairs_per_row * row_h
        source_image = ImageOps.contain(Image.open(paths[source["visual"]]).convert("RGB"), (190, 325), Image.Resampling.LANCZOS)
        target_image = ImageOps.contain(Image.open(paths[target["visual"]]).convert("RGB"), (190, 325), Image.Resampling.LANCZOS)
        canvas.paste(source_image, (pair_left + 15 + (190 - source_image.width) // 2, top + 50))
        canvas.paste(target_image, (pair_left + 345 + (190 - target_image.width) // 2, top + 50))
        draw.text((pair_left + 15, top + 6), f"{source['visual']} {source['state']}", fill="white", font=font)
        draw.text((pair_left + 345, top + 6), f"{target['visual']} {target['state']}", fill="white", font=font)
        draw.text((pair_left + 245, top + 182), transition_marker(), fill="#ffce73", font=font)
        draw.text((pair_left + 215, top + 210), f"{float(target['start']):06.3f}s", fill="#ffce73", font=font)
    canvas.save(OUT / f"transition_atlas_{page:02d}.jpg", quality=93)

shutil.copy2(ROOT / "analysis" / "audio_envelope.png", OUT / "audio_envelope.png")
shutil.copy2(ROOT / "analysis" / "spectrogram.png", OUT / "spectrogram.png")
print("state_atlases=2 transition_atlases=3 audio_visuals=2")
