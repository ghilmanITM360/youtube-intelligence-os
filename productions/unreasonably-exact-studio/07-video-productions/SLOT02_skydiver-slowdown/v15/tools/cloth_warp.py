"""V15 mesh deformation for the side rig (1920x819 canvas): seam-free secondary motion on one continuous image.

One smooth displacement field D(x, y) is sampled on a 32 px grid and applied with PIL's MESH transform, so the art
bends rather than separating. Nothing is cut out, so joints cannot open and parts cannot detach.

  knees  : each shin + boot rotates a few degrees about its knee (weight ramps 0 at the knee -> 1 at the boot)
  wrists : each hand rotates about its wrist (only at rest pose; the lift sprites own the forearm)
  cloth  : travelling ripples on trousers, sleeves and shirt; amplitude follows aerodynamic load (drag/weight)
  rigid  : pack, harness hardware, head/neck and boots' soles keep weight 0 for cloth (the pack never deforms)

Run directly for a self-check (rest field = identity, pack region stays fixed under maximum load).
"""
import math
import numpy as np
from PIL import Image

GRID = 32
W0, H0 = 1920, 819
# (knee, boot) for the far/upper leg and the near/lower leg, canvas px (measured on side_lift_00 + grid sheet)
LEGS = [((470, 455), (345, 255)), ((285, 520), (190, 365))]
WRISTS = [((1690, 385), (1800, 350)), ((1650, 575), (1790, 560))]
CLOTH = [  # (x0, y0, x1, y1, weight): soft boxes
    (215, 370, 770, 710, 1.0),     # trousers
    (1290, 330, 1680, 690, .8),    # sleeves
    (780, 430, 1260, 625, .45),    # shirt below the pack
]
RIGID = [(1000, 330, 140), (1360, 300, 235), (300, 300, 110), (180, 370, 95), (1580, 570, 45)]  # pack, head, boots, watch (x, y, r)
PACK_BOX = (735, 255, 1175, 415)

_gx, _gy = np.meshgrid(np.arange(0, W0 + GRID, GRID, dtype=float), np.arange(0, H0 + GRID, GRID, dtype=float))

def _soft_box(x0, y0, x1, y1, f=60.0):
    sx = np.clip(np.minimum(_gx - x0, x1 - _gx) / f, 0, 1); sy = np.clip(np.minimum(_gy - y0, y1 - _gy) / f, 0, 1)
    return (sx * sx * (3 - 2 * sx)) * (sy * sy * (3 - 2 * sy))

def _cloth_weight():
    w = np.zeros_like(_gx)
    for x0, y0, x1, y1, k in CLOTH: w = np.maximum(w, k * _soft_box(x0, y0, x1, y1))
    for x, y, r in RIGID:
        d = np.hypot(_gx - x, _gy - y); w *= np.clip((d - r) / 60.0, 0, 1)
    px0, py0, px1, py1 = PACK_BOX
    w *= 1 - _soft_box(px0 - 30, py0 - 30, px1 + 30, py1 + 40, 30)
    return w
CW = _cloth_weight()

def _limb(knee, tip, ang_deg, sigma=95.0):
    """Displacement rotating the segment knee->tip by ang about the knee, weight smooth along and across the axis."""
    kx, ky = knee; ax, ay = tip[0] - kx, tip[1] - ky; L = math.hypot(ax, ay); ux, uy = ax / L, ay / L
    rx, ry = _gx - kx, _gy - ky
    s = np.clip((rx * ux + ry * uy) / L, 0, 1.25); along = np.clip(s / 0.8, 0, 1); along = along * along * (3 - 2 * along)
    perp = rx * -uy + ry * ux; across = np.exp(-.5 * (perp / sigma) ** 2)
    behind = np.clip((rx * ux + ry * uy) / 40.0 + 1, 0, 1)     # nothing moves on the hip side of the knee
    reach = np.clip((1.7 * L - np.hypot(rx, ry)) / (.4 * L), 0, 1)   # fades out past the boot, empty sky stays put
    w = along * across * behind * reach
    a = math.radians(ang_deg) * w; c, sn = np.cos(a), np.sin(a)
    return (c * rx - sn * ry + kx) - _gx, (sn * rx + c * ry + ky) - _gy

def field(t, load, hands=1.0, seed=0):
    """Displacement (dx, dy) on the grid. load = aerodynamic drag/weight (0 at rest .. ~1 at speed)."""
    load = max(0.0, min(1.2, load))
    calm = .35 + .65 * load
    dx = np.zeros_like(_gx); dy = np.zeros_like(_gx)
    def osc(f, ph, a): return a * (math.sin(t * f * 6.283 + ph) * .65 + math.sin(t * f * 2.31 * 6.283 + ph * 1.9) * .35)
    for i, (k, tip) in enumerate(LEGS):        # knees: independent, slow, small (pose stays the fixed nominal arch)
        ex, ey = _limb(k, tip, osc(.21 + .06 * i, seed + 1.7 * i, 2.6 * calm))
        dx += ex; dy += ey
    if hands > 0:
        for i, (w, tip) in enumerate(WRISTS):  # wrists: hand trims in the airflow
            ex, ey = _limb(w, tip, osc(.37 + .05 * i, seed + 3.1 + i, 4.0 * calm) * hands, sigma=70)
            dx += ex; dy += ey
    if load > .02:                             # cloth: ripples travel tail-ward (air streams past, body moves through it)
        amp = 1.0 + 4.2 * load ** 1.3; om = 2.0 + 5.5 * load
        ph = _gx / 95.0 + t * om + .6 * np.sin(_gy / 70.0 + t * 1.3)
        rip = np.sin(ph) * .7 + np.sin(ph * 2.13 + 1.1) * .3
        dy += CW * amp * rip
        dx += CW * amp * .35 * np.cos(ph * .8 + .4)
    return dx, dy

def warp(img, t, load, hands=1.0, seed=0):
    """Return img (RGBA PIL, 1920x819) deformed by field(t, load). Inverse map: dest vertex samples src at v - D(v)."""
    dx, dy = field(t, load, hands, seed)
    sx, sy = _gx - dx, _gy - dy
    mesh = []
    ny, nx = _gx.shape
    for j in range(ny - 1):
        for i in range(nx - 1):
            box = (int(_gx[j, i]), int(_gy[j, i]), int(_gx[j, i + 1]), int(_gy[j + 1, i]))
            quad = (sx[j, i], sy[j, i], sx[j + 1, i], sy[j + 1, i], sx[j + 1, i + 1], sy[j + 1, i + 1], sx[j, i + 1], sy[j, i + 1])
            mesh.append((box, quad))
    return img.transform(img.size, Image.MESH, mesh, Image.BICUBIC)

if __name__ == '__main__':
    import sys
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    im = Image.open(ROOT / 'assets/v12rig/side_lift_00.png').convert('RGBA')
    dx, dy = field(0.0, 0.0, hands=0)
    lg = _limb(LEGS[0][0], LEGS[0][1], 0.0)
    assert np.abs(lg[0]).max() < 1e-9, 'zero angle = identity'
    for t in np.linspace(0, 20, 41):
        dx, dy = field(t, 1.1)
        m = _soft_box(*PACK_BOX, 1) > .5
        assert np.abs(dx[m]).max() < .35 and np.abs(dy[m]).max() < .35, 'pack stays rigid'
        hm = np.hypot(_gx - 1360, _gy - 300) < 235
        assert np.abs(dy[hm]).max() < 1.0, 'head/neck region stays registered with the separate head layer'
        assert np.hypot(dx, dy).max() < 16, 'deformation stays small'
    out = ROOT / 'qa/rig_v15'; out.mkdir(parents=True, exist_ok=True)
    tiles = []
    for t, ld in ((0, 0), (1.0, .5), (1.7, 1.0), (2.3, 1.0)):
        w = warp(im, t, ld); bg = Image.new('RGBA', im.size, (170, 200, 230, 255)); bg.alpha_composite(w); tiles.append(bg.convert('RGB').resize((960, 410)))
    sheet = Image.new('RGB', (1920, 820)); [sheet.paste(tl, ((i % 2) * 960, (i // 2) * 410)) for i, tl in enumerate(tiles)]
    sheet.save(out / 'warp_states.png')
    print('cloth_warp self-check ok ->', out / 'warp_states.png')
