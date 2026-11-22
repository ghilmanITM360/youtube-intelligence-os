"""Independent playback-scale check of the SH018 Earth state sprites against EVERY source frame f1105-f1159 (state A = f1105-14/25-34/45-54, B = f1115-24/35-44/55-59).
Per frame: ink coverage both ways (3px tolerance) + per-class pixel IoU (ocean/navy, green, ice, orange, yellow) on the same crop."""
import json, os, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_sprite_vs_source as V
import shot_sprites_earth as E
SP = V.SP; RECT = E.RECT
def cls(rgb): return E.classify(rgb)
def run():
    meta = json.load(open(os.path.join(SP, 'sprites_meta.json'))); out = []
    F = V.frames(1105, 1159, RECT)
    ims = {}
    for st in 'AB':
        im = Image.open(os.path.join(SP, 'earth_%s.png' % st)); m = meta['earth_' + st]
        bg = Image.new('RGBA', (1080, 1920), (253, 253, 253, 255)); bg.alpha_composite(im, (m['x0'], m['y0'])); ims[st] = np.array(bg.convert('RGB').crop(RECT))
    # rows outside the source clip (y<656 / y>1263) are white in the source: compare only inside
    inner = slice(656 - RECT[1], 1264 - RECT[1])
    rows = []
    for i, f in enumerate(F):
        fr = 1105 + i; st = 'A' if ((fr - 1105) // 10) % 2 == 0 else 'B'
        pv = ims[st][inner]; sv = f[inner]
        pa = np.array(Image.fromarray(pv).convert('L')) < 110; sa = np.array(Image.fromarray(sv).convert('L')) < 110
        pd, sd = V.dil(pa), V.dil(sa)
        pc, sc_ = cls(pv), cls(sv); ious = {}
        for k in ('green', 'ice', 'orange', 'yellow'):
            a, b = pc == k, sc_ == k; ious[k] = float((a & b).sum() / max(1, (a | b).sum()))
        rows.append(dict(frame=fr, state=st, src_ink_in3=float((sa & pd).sum() / sa.sum()), spr_ink_in3=float((pa & sd).sum() / pa.sum()), **ious,
                         pix_acc=float((pc == sc_).mean())))
        if fr in (1110, 1120):
            d = np.full(pv.shape, 255, 'uint8'); d[sa & ~pa] = (230, 40, 40); d[pa & ~sa] = (40, 80, 230); d[pa & sa] = 0
            Image.fromarray(np.concatenate([sv, pv, d], 1)).resize((1440, 304)).save(os.path.join(SP, 'validation', 'val_SH018_%d_%s.png' % (fr, st)))
    keys = [k for k in rows[0] if k not in ('frame', 'state')]
    summ = {s: {k: round(float(np.mean([r[k] for r in rows if r['state'] == s])), 3) for k in keys} for s in 'AB'}
    json.dump(dict(per_frame=rows, summary=summ), open(os.path.join(SP, 'validation', 'earth_validation.json'), 'w'), indent=1); print(json.dumps(summ, indent=1))
if __name__ == '__main__': os.makedirs(os.path.join(SP, 'validation'), exist_ok=True); run()
