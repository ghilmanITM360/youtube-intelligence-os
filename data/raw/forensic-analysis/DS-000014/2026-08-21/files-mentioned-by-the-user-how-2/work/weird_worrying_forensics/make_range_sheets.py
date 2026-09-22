from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps

from forensic_analysis import parse_frame_time


root = Path(__file__).resolve().parent
paths = sorted((root / "proxy_frames").glob("frame_*ms.jpg"))
out = root / "analysis" / "ranges"
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default(size=16)

for page, start in enumerate(range(0, len(paths), 36), 1):
    batch = paths[start : start + 36]
    columns, cell_w, cell_h = 9, 130, 250
    canvas = Image.new("RGB", (columns * cell_w, math.ceil(len(batch) / columns) * cell_h), "#111111")
    draw = ImageDraw.Draw(canvas)
    for cell, path in enumerate(batch):
        frame = Image.open(path).convert("RGB")
        frame = ImageOps.contain(frame, (cell_w - 8, cell_h - 34), Image.Resampling.LANCZOS)
        left = cell % columns * cell_w
        top = cell // columns * cell_h
        canvas.paste(frame, (left + (cell_w - frame.width) // 2, top + 26))
        draw.text((left + 4, top + 4), f"{parse_frame_time(path.name):05.2f}s", fill="white", font=font)
    canvas.save(out / f"range_{page:02d}.jpg", quality=92)

print(f"range_pages={math.ceil(len(paths) / 36)}")
