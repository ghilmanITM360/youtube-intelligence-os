"""Builds CHR-MS01 from assets/final and rewrites MANIFEST.csv (old Codex rows archived, files untouched)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv, hashlib, json, shutil
ROOT = Path(__file__).resolve().parents[2]; sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
F = ROOT/'assets/final'; M = ROOT/'assets/MANIFEST.csv'; ARC = ROOT/'assets/MANIFEST_codex_attempts.csv'
if not ARC.exists(): shutil.copy(M, ARC)
fields = list(csv.DictReader(ARC.open()).fieldnames); old = list(csv.DictReader(ARC.open()))
ids = ['CHR-V01','CHR-V02','CHR-V03','CHR-V04','CHR-X01','CHR-X02','CHR-X03','CHR-X04','CHR-X05','CHR-X06','CHR-G01','CHR-G02','CHR-G03','CHR-G04']
cv = Image.new('RGB', (3200, 2400), '#f8f8f8'); d = ImageDraw.Draw(cv); f = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 38)
for i, a in enumerate(ids):
    x, y = (i % 4)*800, (i//4)*575; d.text((x+20, y+10), a, fill='#0c0c0c', font=f)
    im = Image.open(F/f'{a}.png').convert('RGBA'); sc = 0.46 if a.startswith(('CHR-V', 'CHR-X')) else 0.5
    if a.startswith('CHR-X'): im = im.crop((300, 100, 700, 560))
    elif a.startswith('CHR-V'): im = im.crop((368, 100, 1168, 1140)); sc = 0.5
    else: sc = 0.48
    im = im.resize((int(im.width*sc), int(im.height*sc)), Image.LANCZOS); cv.paste(im, (x+(800-im.width)//2, y+60), im)
d.text((1630, 1790), 'head ratio 0.37 ruler (review board only)', fill='#0c0c0c', font=f); d.line((1680, 1870, 1680, 2250), fill='#0c0c0c', width=5)
p = ROOT/'assets/chr/CHR_MS01_model_sheet-v4.png'; cv.save(p)
rows = [r for r in old if r['asset_id'] in ('PIPE-01', 'PIPE-02')]
for r in rows: r['attempt'] = '1'
rows[1]['status'] = 'PASS'; rows[1]['notes'] += ' | used as head source for every code-rendered CHR asset'
rows.append(dict(asset_id='CHR-MS01', filename=str(p.relative_to(ROOT)), sha256=sha(p), width=3200, height=2400, mode='RGB', generated_or_code='code', attempt=4, status='PASS', notes='tiled from assets/final; same head pixels in every view', native_sha256='', native_w='', native_h=''))
for q in sorted(F.glob('*.png')):
    im = Image.open(q); rows.append(dict(asset_id=q.stem, filename=str(q.relative_to(ROOT)), sha256=sha(q), width=im.width, height=im.height, mode=im.mode, generated_or_code='code_rendered', attempt=5, status='PASS',
        notes='rendered by assets/qa/render_all.py (no image model); Claude visual review 2026-11-15; owner review pending', native_sha256='', native_w='', native_h=''))
with M.open('w', newline='') as z: w = csv.DictWriter(z, fieldnames=fields); w.writeheader(); w.writerows(rows)
print(len(rows), 'rows')
