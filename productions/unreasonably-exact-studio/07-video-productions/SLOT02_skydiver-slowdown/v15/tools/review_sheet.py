"""Review contact sheet: picture + caption overlay composited at given V15 film seconds, labelled with the time.
  .venv/bin/python tools/review_sheet.py OUT.png T1 T2 ... [--cols 6] [--w 300]
"""
import sys, io
from pathlib import Path
sys.argv, args = [sys.argv[0]], sys.argv[1:]
ns = {'__file__': str(Path(__file__).with_name('v15.py')), '__name__': 'sheet'}
exec(open(Path(__file__).with_name('v15.py')).read(), ns)
from PIL import Image, ImageDraw
cols, w = 6, 300
if '--cols' in args: i = args.index('--cols'); cols = int(args[i + 1]); del args[i:i + 2]
if '--w' in args: i = args.index('--w'); w = int(args[i + 1]); del args[i:i + 2]
out, times = args[0], [float(x) for x in args[1:]]
h = w * 16 // 9
def png(surf):
    b = io.BytesIO(); surf.write_to_png(b); b.seek(0); return Image.open(b).convert('RGBA')
tiles = []
for t in times:
    im = png(ns['frame_surface'](t)); im.alpha_composite(png(ns['caption_surface'](t)))
    im = im.convert('RGB').resize((w, h), Image.LANCZOS); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 58, 16), fill='black'); d.text((3, 2), f'{t:6.2f}s', fill='white'); tiles.append(im)
rows = (len(tiles) + cols - 1) // cols
sheet = Image.new('RGB', (cols * w, rows * h), 'white')
for i, im in enumerate(tiles): sheet.paste(im, ((i % cols) * w, (i // cols) * h))
sheet.save(out); print(out)
