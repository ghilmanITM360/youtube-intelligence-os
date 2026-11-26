"""Visual consistency sheet: every production look side by side (Codex art + real-data spheres + Claude graphics).
usage: ~/.venvs/uepipe/bin/python tools/art_consistency_sheet.py <dir with cs_earth.png cs_graphic.png cs_graphic2.png stills>"""
import sys, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, 'animation')); os.chdir(ROOT)
from uemotion.canvas import Canvas
from uemotion import space as S
SP = sys.argv[1].rstrip('/') + '/'
S.preload_real()
cv = Canvas(0.5, 1, bg=(10, 12, 20)); S.draw_sphere(cv, (540, 960), 420, 'moon'); moon = cv.to_image().convert('RGB').crop((50, 230, 490, 730))
def cut(path, box=None, bg=(26, 28, 36)):
    im = Image.open(path).convert('RGBA')
    if box: im = im.crop(box)
    b = Image.new('RGBA', im.size, bg + (255,)); b.alpha_composite(im); return b.convert('RGB')
refl = 'codex_handoff/runs/B5PR2/interaction_reflector_cubes.png' if os.path.exists('codex_handoff/runs/B5PR2/interaction_reflector_cubes.png') else 'codex_handoff/guides_construction/RETRO_004_MASTER_34_candidate.png'
tiles = [('Earth: NASA maps + Codex clouds', Image.open(SP + 'cs_earth.png').convert('RGB').crop((40, 200, 500, 700))),
         ('Moon: LRO colour map', moon),
         ('Lunar ground: Codex B3M', cut('codex_handoff/runs/B3M/lunar_env_master.png', (0, 250, 1024, 1536))),
         ('Observatory: Codex B4M', cut('codex_handoff/runs/B4M/observatory_exterior_master.png', (0, 400, 1024, 1536))),
         ('Telescope: Codex B4L (graded)', cut('codex_handoff/runs/B4L/obs_telescope.png', (150, 200, 850, 1260))),
         ('Astronaut: Codex B5M', cut('codex_handoff/runs/B5M/astronaut_master_34.png', (0, 40, 1024, 1536))),
         ('Reflector: Codex', cut(refl)),
         ('Interaction: Codex B5P', cut('codex_handoff/runs/B5P/astro_retro_interaction.png', (0, 40, 1024, 1536))),
         ('Graphics: journey (P08)', Image.open(SP + 'cs_graphic2.png').convert('RGB')),
         ('Graphics: d = ct/2 (P12)', Image.open(SP + 'cs_graphic.png').convert('RGB'))]
W, H = 360, 420; sheet = Image.new('RGB', (W * 5, (H + 40) * 2 + 120), (14, 16, 24)); d = ImageDraw.Draw(sheet)
f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 18); F = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 30)
d.text((20, 20), 'SLOT 07 visual consistency sheet', font=F, fill=(235, 235, 240))
d.text((20, 64), 'Codex art = near-photoreal illustration; spheres = real NASA/LRO maps; graphics = flat vector. One Sun upper-left; warm = outbound, cool = return.', font=f, fill=(170, 176, 190))
for k, (lab, im) in enumerate(tiles):
    im = im.copy(); im.thumbnail((W - 16, H - 16)); x = (k % 5) * W; y = 120 + (k // 5) * (H + 40)
    sheet.paste(im, (x + (W - im.width) // 2, y + (H - im.height) // 2)); d.text((x + 10, y + H + 6), lab, font=f, fill=(220, 220, 230))
os.makedirs('qa/art', exist_ok=True); sheet.save('qa/art/ART_CONSISTENCY_SHEET_2026-11-26.png'); print('wrote qa/art/ART_CONSISTENCY_SHEET_2026-11-26.png')
