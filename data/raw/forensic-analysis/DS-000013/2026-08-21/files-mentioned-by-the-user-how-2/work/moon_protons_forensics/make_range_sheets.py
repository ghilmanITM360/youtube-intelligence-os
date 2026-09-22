from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from forensic_metrics import frame_time_from_name


root = Path(__file__).resolve().parent
frames = sorted((root / "proxy_frames").glob("frame_*ms.jpg"))
ranges = [
    (0.0, 8.0),
    (8.0, 19.75),
    (19.5, 26.5),
    (26.25, 39.25),
    (38.75, 46.75),
    (46.5, 63.75),
    (63.5, 73.25),
    (73.0, 88.25),
]
font = ImageFont.load_default(size=17)
for range_index, (start_time, end_time) in enumerate(ranges, 1):
    selected = [path for path in frames if start_time <= frame_time_from_name(path.name) < end_time]
    for page, offset in enumerate(range(0, len(selected), 32), 1):
        batch = selected[offset : offset + 32]
        columns, cell_w, cell_h = 8, 190, 350
        canvas = Image.new("RGB", (columns * cell_w, math.ceil(len(batch) / columns) * cell_h), "#111111")
        draw = ImageDraw.Draw(canvas)
        for index, path in enumerate(batch):
            image = Image.open(path).convert("RGB")
            image = ImageOps.contain(image, (cell_w - 8, cell_h - 38), Image.Resampling.LANCZOS)
            x = index % columns * cell_w + (cell_w - image.width) // 2
            y = index // columns * cell_h + 28
            canvas.paste(image, (x, y))
            draw.text((index % columns * cell_w + 5, index // columns * cell_h + 4), f"{frame_time_from_name(path.name):06.2f}", fill="white", font=font)
        canvas.save(root / "analysis" / f"range_{range_index:02d}_{page:02d}.jpg", quality=92)
print("range_sheets_complete")
