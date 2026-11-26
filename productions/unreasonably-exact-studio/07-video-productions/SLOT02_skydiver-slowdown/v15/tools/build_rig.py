"""V12 side-pose rig, built from the Codex V12 candidate partition + Codex generated raised/glance poses.

Codex delivered a disjoint partition (rest = master, AE 0) but no hidden overlap art, so free joint rotation
opens holes (Codex qa/upper_plus20.png, forearm_plus20.png). V12 therefore uses a constrained rig:

  head       : rotates <= 4 deg about the neck over a fixed neck/collar underlay (no hole at the collar)
  glance     : head replacement cut from Codex glance_generation.png (registered: legs alpha IoU 0.985)
  arm lift   : forearm+hand rotate 0 -> 22 deg about the underside of the elbow (fold stays closed; IoU 0.54 vs the
               raised drawing), two tiny swept-sleeve patches close the top notch and bottom slit, then a 2-frame
               dissolve into Codex raised_generation.png (registered: legs IoU 0.985), where the two match.
Pivots below were chosen by visual test on this sheet; they are NOT certified by Codex (PIVOTS.json = null).

Run from skydiver-slowdown/v15:  .venv/bin/python tools/build_rig.py
Writes assets/v12rig/*.png and qa/rig/*.png.
"""
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter, ImageChops

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'CODEX_V12_ART_PACKAGE'
OUT = ROOT / 'assets/v12rig'; OUT.mkdir(parents=True, exist_ok=True)
QA = ROOT / 'qa/rig'; QA.mkdir(parents=True, exist_ok=True)

NECK = (1352, 452)        # head pivot (visual test)
ELBOW = (1335, 668)       # forearm pivot at the underside of the elbow fold: the fold stays closed, the top tucks under the sleeve
PATCHES = [(1340, 547, 30), (1342, 668, 26)]   # small swept-sleeve fills: top notch and bottom slit
LIFT_ANGLE = 22
SLEEVE = (222, 214, 201, 255)
INK = (42, 43, 39, 255)

def L(name): return Image.open(P / f'character/side/side_{name}.png').convert('RGBA')
body, head, upper, fore, hand = L('body'), L('head'), L('near_upper_arm'), L('near_forearm'), L('near_hand')
raised = Image.open(P / 'sources/raised_generation.png').convert('RGBA')
glance_src = Image.open(P / 'sources/glance_generation.png').convert('RGBA')
master = Image.open(ROOT / 'codex_request/v11/side_body_v11_repaired.png').convert('RGBA')

def comp(*layers):
    out = Image.new('RGBA', (1920, 819), (0, 0, 0, 0))
    for l in layers: out = Image.alpha_composite(out, l)
    return out

def mask_of(img, thr=8): return Image.fromarray(((np.array(img)[..., 3] > thr) * 255).astype(np.uint8))
def apply_mask(img, m):
    a = np.array(img).copy(); a[..., 3] = (a[..., 3].astype(float) * np.array(m) / 255).astype(np.uint8); return Image.fromarray(a)

# ---- rest check: partition reassembles the master
rest = comp(body, upper, fore, hand, head)
diff = np.abs(np.array(rest).astype(int) - np.array(master).astype(int)).max()
print('rest reassembly max channel diff vs master:', diff)

# ---- head: neck underlay = lower part of the head layer (collar + neck), stays fixed
hm = np.array(head)
under = hm.copy(); yy = np.arange(819)[:, None]
under[..., 3] = np.where(yy > 330, under[..., 3], 0).astype(np.uint8)
neck_under = Image.fromarray(under)

# ---- glance head: cut from the registered generated pose with a feathered dilation of Codex's rough mask
gm = mask_of(Image.open(P / 'character/side/side_head_glance.png')).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(2))
glance = apply_mask(glance_src, gm)
# keep only head (not shoulder/arm fragments): restrict to the head's bounding region
g = np.array(glance); g[:, :1200, 3] = 0; g[500:, :, 3] = 0; glance = Image.fromarray(g)

# ---- body without head (rest) and lift sequence
def lifted(a):
    """Body-without-head with the near forearm+hand rotated a degrees (CCW = up) about the elbow."""
    fh = comp(fore, hand)
    layers = [body]
    if a > 0:
        disc = Image.new('L', (1920, 819), 0)
        from PIL import ImageDraw
        for px, py, r in PATCHES: ImageDraw.Draw(disc).ellipse((px - r, py - r, px + r, py + r), fill=255)
        disc = disc.filter(ImageFilter.GaussianBlur(2))
        sweep_ink = Image.new('RGBA', (1920, 819), (0, 0, 0, 0)); sweep = Image.new('RGBA', (1920, 819), (0, 0, 0, 0))
        for b in np.linspace(0, a, 8):
            m = mask_of(fh.rotate(b, center=ELBOW, resample=Image.BILINEAR))
            ink = Image.new('RGBA', (1920, 819), INK); ink.putalpha(m.filter(ImageFilter.MaxFilter(5)))
            fill = Image.new('RGBA', (1920, 819), SLEEVE); fill.putalpha(m.filter(ImageFilter.MinFilter(3)))
            sweep_ink = Image.alpha_composite(sweep_ink, ink); sweep = Image.alpha_composite(sweep, fill)
        layers += [apply_mask(sweep_ink, disc), apply_mask(sweep, disc)]
    layers += [fh.rotate(a, center=ELBOW, resample=Image.BICUBIC), upper]
    return comp(*layers)

def strip_head(img):
    hmask = mask_of(head).filter(ImageFilter.MaxFilter(5))
    a = np.array(img).copy(); a[..., 3] = np.where(np.array(hmask) > 0, 0, a[..., 3]); return Image.fromarray(a)

rest_nohead = lifted(0)
raised_nohead = strip_head(raised)
frames = []
ease = lambda u: u * u * (3 - 2 * u)
N_ROT, N_DIS = 7, 2
for k in range(N_ROT):
    frames.append(lifted(LIFT_ANGLE * ease((k + 1) / N_ROT)))
top = frames[-1]
for k in range(N_DIS):
    frames.append(Image.blend(top, raised_nohead, (k + 1) / N_DIS))
for i, f in enumerate([rest_nohead] + frames):
    f.save(OUT / f'side_lift_{i:02}.png')
neck_under.save(OUT / 'side_neck_underlay.png'); head.save(OUT / 'side_head.png'); glance.save(OUT / 'side_head_glance.png')
meta = dict(canvas=[1920, 819], neck_pivot=NECK, elbow_pivot=ELBOW, lift_angle_deg=LIFT_ANGLE, lift_frames=len(frames) + 1,
            rotation_frames=N_ROT, dissolve_frames=N_DIS, pivots_status='chosen by visual test in V12, not certified by Codex',
            draw_order=['side_lift_NN (body+arms, no head)', 'side_neck_underlay', 'side_head | side_head_glance'])
(OUT / 'RIG.json').write_text(json.dumps(meta, indent=1))

# ---- QA sheets on sky blue: every lift frame, and head at -4/0/+4 deg + glance
def on_blue(img, box=(1080, 120, 1880, 720)):
    bg = Image.new('RGBA', (1920, 819), (170, 200, 230, 255)); return Image.alpha_composite(bg, img).crop(box).convert('RGB')
def with_head(b, h, ang=0):
    return comp(b, neck_under, h.rotate(ang, center=NECK, resample=Image.BICUBIC))
seq = [rest_nohead] + frames
tiles = [on_blue(with_head(f, head if i < 5 else glance)) for i, f in enumerate(seq)]
W_, H_ = tiles[0].size; cols = 4; rows = (len(tiles) + cols - 1) // cols
sheet = Image.new('RGB', (W_ * cols, H_ * rows), 'white')
for i, t in enumerate(tiles): sheet.paste(t, ((i % cols) * W_, (i // cols) * H_))
sheet.resize((W_ * cols // 2, H_ * rows // 2)).save(QA / 'lift_sequence.png')
hs = [on_blue(with_head(rest_nohead, head, a), (1150, 80, 1650, 560)) for a in (-1.5, 0, 1.5)] + [on_blue(with_head(rest_nohead, glance), (1150, 80, 1650, 560))]
sheet = Image.new('RGB', (500 * 4, 480), 'white')
for i, t in enumerate(hs): sheet.paste(t, (i * 500, 0))
sheet.save(QA / 'head_range.png')
# zoomed elbow at full lift (seam check)
on_blue(with_head(frames[N_ROT - 1], head), (1200, 480, 1560, 720)).resize((720, 480)).save(QA / 'elbow_zoom_22deg.png')
print('wrote', len(seq), 'lift frames')
