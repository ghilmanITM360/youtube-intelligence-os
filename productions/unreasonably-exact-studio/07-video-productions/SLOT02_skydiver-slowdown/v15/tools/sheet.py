"""Contact sheet of PNG stills: python tools/sheet.py out.png cols w files..."""
import sys
from PIL import Image, ImageDraw
out, cols, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); fs = sys.argv[4:]
h = int(w * 16 / 9); rows = (len(fs) + cols - 1) // cols
S = Image.new('RGB', (cols * w, rows * (h + 18)), 'white'); d = ImageDraw.Draw(S)
for i, f in enumerate(fs):
    im = Image.open(f).convert('RGB').resize((w, h)); x, y = (i % cols) * w, (i // cols) * (h + 18)
    S.paste(im, (x, y + 18)); d.text((x + 4, y + 3), f.split('/')[-1], fill=(0, 0, 0))
S.save(out)
