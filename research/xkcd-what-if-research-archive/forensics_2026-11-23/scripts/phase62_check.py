"""Validation montage for phase62_style: frame | ink mask | red+other accent mask, for 8 frames chosen at fixed ranks of stroke width. usage: uv run --no-project --with numpy --with pillow --with scipy --with scikit-image python scripts/phase62_check.py"""
import csv, os, numpy as np
from PIL import Image
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = list(csv.DictReader(open(A + '/06_STYLE_MEASUREMENTS_125.csv')))
R = [r for r in R if r['stroke_px'] != 'nan']; R.sort(key=lambda r: float(r['stroke_px']))
pick = [R[int(i * (len(R) - 1) / 7)] for i in range(8)]
tiles = []
for r in pick:
    im = Image.open(A + '/' + r['frame_ref']).convert('RGB'); a = np.asarray(im).astype(np.int16)
    bg = np.array([int(x) for x in r['bg_rgb'].split(',')]); nonbg = np.abs(a - bg).sum(2) > 60; mx = a.max(2); mn = a.min(2); sat = (mx - mn) / np.maximum(mx, 1); lum = a @ np.array([.299, .587, .114])
    ink = nonbg & (sat < .25) & ((lum > 150) if int(r['dark_bg']) else (lum < 110)); acc = nonbg & (sat > .45) & (mx > 90)
    m = np.full(a.shape, 255, np.uint8); m[ink] = 0; m[acc] = (220, 40, 40)
    w = 360; s = lambda x: x.resize((w, int(x.height * w / x.width)))
    t = Image.new('RGB', (w * 2, max(s(im).height, 200)), 'white'); t.paste(s(im), (0, 0)); t.paste(s(Image.fromarray(m)), (w, 0))
    tiles.append((t, f"{r['video_id']} t={r['t_s']} stroke={r['stroke_px']} red={r['red_stroke_px']} neg={r['negative_space']}"))
H = max(t.height for t, _ in tiles) + 14; sheet = Image.new('RGB', (720 * 2, H * 4), 'white')
from PIL import ImageDraw
d = ImageDraw.Draw(sheet)
for i, (t, cap) in enumerate(tiles): x, y = (i % 2) * 720, (i // 2) * H; sheet.paste(t, (x, y + 12)); d.text((x + 2, y), cap, fill='black')
sheet.save(A + '/phase62_style/validation_sheet.jpg', quality=85); print(sheet.size)
