"""contact sheet of stills: python3 tools/v1r4_sheet.py out.jpg img1 img2 ... (2 columns)"""
import sys
from PIL import Image
o, fs = sys.argv[1], sys.argv[2:]
ims = [Image.open(f).convert('RGB').resize((960, 540)) for f in fs]; cols = 2; rows = (len(ims) + 1) // 2
s = Image.new('RGB', (cols * 960 + 10, rows * 540 + 10 * rows), (120, 120, 120))
for i, im in enumerate(ims): s.paste(im, ((i % cols) * 970, (i // cols) * 550))
s.save(o, quality=88)
