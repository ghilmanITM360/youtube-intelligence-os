"""Independent playback-scale check: every source frame of a shot vs the sprite pasted at its placement on white.
Ink = luminance<110, tolerance 3px (dilate 7x7). Reports per-frame min/mean of both-direction coverage plus peach-fill colour distance. Writes side-by-side + diff PNG."""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter
SRC = "/Users/ghilmankhan/workprojects/videos in mp3/CasuallyFinance/The IPO Boom Is the Danger Sign [10nEByVLya0].mp4"
PS = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SP = os.path.join(PS, 'shot_sprites')
def frames(a, b, box):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0; w2, h2 = w + w % 2, h + h % 2   # ffmpeg rounds odd crops (4:2:0): read even, slice back
    cmd = ['ffmpeg', '-v', 'error', '-i', SRC, '-vf', 'select=between(n\\,%d\\,%d),crop=%d:%d:%d:%d' % (a, b, w2, h2, x0, y0), '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    return np.frombuffer(subprocess.check_output(cmd), np.uint8).reshape(-1, h2, w2, 3)[:, :h, :w]
def dil(m, k=7): return np.array(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.MaxFilter(k))) > 0
def check(sprite, name, a, b, box, outdir):
    im = Image.open(os.path.join(SP, sprite + '.png')); m = json.load(open(os.path.join(SP, 'sprites_meta.json')))[sprite]
    bg = Image.new('RGBA', (1080, 1920), (253, 253, 253, 255)); bg.alpha_composite(im, (m['x0'], m['y0']))
    pv = np.array(bg.convert('RGB').crop(box)); pa = np.array(Image.fromarray(pv).convert('L')) < 110; pd = dil(pa)
    F = frames(a, b, box); res = []
    for i, f in enumerate(F):
        sa = np.array(Image.fromarray(f).convert('L')) < 110; sd = dil(sa)
        res.append((float((sa & pd).sum() / sa.sum()), float((pa & sd).sum() / pa.sum())))
    # fill colour: face interior sample (centre of head) mean abs diff
    cy, cx = 880 - box[1], 540 - box[0]
    col = float(np.abs(F[len(F) // 2][cy - 20:cy + 20, cx - 20:cx + 20].astype(int) - pv[cy - 20:cy + 20, cx - 20:cx + 20].astype(int)).mean())
    r = np.array(res); out = dict(shot=name, sprite=sprite, frames=len(F), src_within3_min=round(r[:, 0].min(), 3), src_within3_mean=round(r[:, 0].mean(), 3),
                                 sprite_within3_min=round(r[:, 1].min(), 3), sprite_within3_mean=round(r[:, 1].mean(), 3), face_fill_abs_diff=round(col, 1))
    mid = F[len(F) // 2]; sa = np.array(Image.fromarray(mid).convert('L')) < 110
    d = np.full(pv.shape, 255, 'uint8'); d[sa & ~pa] = (230, 40, 40); d[pa & ~sa] = (40, 80, 230); d[pa & sa] = 0
    sheet = np.concatenate([mid, pv, d], 1); Image.fromarray(sheet).save(os.path.join(outdir, 'val_%s_%s.png' % (name, sprite)))
    return out
if __name__ == '__main__':
    outdir = os.path.join(PS, 'shot_sprites', 'validation'); os.makedirs(outdir, exist_ok=True)
    box = (420, 750, 660, 1200)
    R = [check('hips_B_happy', 'SH008', 511, 540, box, outdir), check('hips_A_happy', 'SH010', 631, 663, box, outdir),
         check('hips_A_neutral', 'SH012', 707, 729, box, outdir), check('hips_A_neutral', 'SH015', 825, 849, box, outdir)]
    json.dump(R, open(os.path.join(outdir, 'hips_validation.json'), 'w'), indent=1); [print(r) for r in R]
