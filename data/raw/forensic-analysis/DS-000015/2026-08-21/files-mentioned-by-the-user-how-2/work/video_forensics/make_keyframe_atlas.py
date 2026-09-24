from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

root = Path(__file__).resolve().parents[2]
source = root / "outputs" / "keyframes"
dest = root / "outputs"
files = sorted(source.glob("V*.jpg"))
font = ImageFont.load_default(size=24)
columns, rows_per_page = 4, 2
cell_w, cell_h = 390, 760
per_page = columns * rows_per_page
for page, start in enumerate(range(0, len(files), per_page), 1):
    batch = files[start : start + per_page]
    canvas = Image.new("RGB", (columns * cell_w, rows_per_page * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for i, path in enumerate(batch):
        image = Image.open(path).convert("RGB")
        image = ImageOps.contain(image, (cell_w - 18, cell_h - 60), Image.Resampling.LANCZOS)
        x = (i % columns) * cell_w + (cell_w - image.width) // 2
        y = (i // columns) * cell_h + 48
        canvas.paste(image, (x, y))
        draw.text(((i % columns) * cell_w + 10, (i // columns) * cell_h + 10), path.stem.replace("_", "  "), fill="white", font=font)
    canvas.save(dest / f"keyframe_atlas_{page:02d}.jpg", quality=92)
print(f"pages={math.ceil(len(files) / per_page)}")
