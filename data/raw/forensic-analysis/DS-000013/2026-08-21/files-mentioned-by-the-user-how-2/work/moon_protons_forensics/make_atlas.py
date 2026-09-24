from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps


root = Path(__file__).resolve().parents[2]
source = root / "outputs/moon_protons_forensics/keyframes"
destination = root / "outputs/moon_protons_forensics"
files = sorted(source.glob("V*.jpg"))
font = ImageFont.load_default(size=24)
columns, rows_per_page = 4, 2
cell_width, cell_height = 390, 760
per_page = columns * rows_per_page
for page, start in enumerate(range(0, len(files), per_page), 1):
    batch = files[start : start + per_page]
    canvas = Image.new("RGB", (columns * cell_width, rows_per_page * cell_height), "#111111")
    draw = ImageDraw.Draw(canvas)
    for index, path in enumerate(batch):
        image = Image.open(path).convert("RGB")
        image = ImageOps.contain(image, (cell_width - 18, cell_height - 60), Image.Resampling.LANCZOS)
        x = index % columns * cell_width + (cell_width - image.width) // 2
        y = index // columns * cell_height + 48
        canvas.paste(image, (x, y))
        draw.text((index % columns * cell_width + 10, index // columns * cell_height + 10), path.stem.replace("_", "  "), fill="white", font=font)
    canvas.save(destination / f"keyframe_atlas_{page:02d}.jpg", quality=92)
print(f"pages={math.ceil(len(files) / per_page)}")
