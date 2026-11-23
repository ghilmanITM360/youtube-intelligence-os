"""Independent playback-scale checks for calendar / SH003 burst / SH003 bubble (at two diameters) / SH004 man against source frames."""
import json, os, sys, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_sprite_vs_source as V
SP = V.SP; META = json.load(open(os.path.join(SP, 'sprites_meta.json')))
def comp(name, scale=1.0, bgc=(253, 253, 253)):
    im = Image.open(os.path.join(SP, name + '.png')); m = META[name]
    if scale != 1: im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    cx, cy = m['x0'] + m['w'] / 2, m['y0'] + m['h'] / 2; bg = Image.new('RGBA', (1080, 1920), bgc + (255,)); bg.alpha_composite(im, (round(cx - im.width / 2), round(cy - im.height / 2))); return bg.convert('RGB')
def score(sprite_img, frame, box, tag, outdir, ink_thr=110):
    pv = np.array(sprite_img.crop(box)); F = V.frames(frame, frame, box)[0]
    pa = np.array(Image.fromarray(pv).convert('L')) < ink_thr; sa = np.array(Image.fromarray(F).convert('L')) < ink_thr
    pd, sd = V.dil(pa), V.dil(sa); nonbg = lambda x: (np.abs(x.astype(int) - 253).sum(-1) > 40)
    ps, ss = nonbg(pv), nonbg(F); iou = float((ps & ss).sum() / max(1, (ps | ss).sum()))
    r = dict(tag=tag, frame=frame, src_ink_in3=round(float((sa & pd).sum() / max(1, sa.sum())), 3), spr_ink_in3=round(float((pa & sd).sum() / max(1, pa.sum())), 3), nonbg_iou=round(iou, 3), mean_abs_rgb=round(float(np.abs(pv.astype(int) - F.astype(int)).mean()), 2))
    d = np.full(pv.shape, 255, 'uint8'); d[ss & ~ps] = (230, 40, 40); d[ps & ~ss] = (40, 80, 230); d[ps & ss] = (0, 0, 0)
    Image.fromarray(np.concatenate([F, pv, d], 1)).save(os.path.join(outdir, 'val_%s.png' % tag)); return r
if __name__ == '__main__':
    out = os.path.join(SP, 'validation'); os.makedirs(out, exist_ok=True); R = []
    R.append(score(comp('calendar'), 420, (110, 890, 290, 1045), 'calendar_f420', out))
    R.append(score(comp('burst_particles'), 235, (270, 740, 830, 1180), 'burst_f235', out))
    R.append(score(comp('man_brown'), 340, (100, 855, 380, 1270), 'man_f340', out))
    # bubble over white at diameters measured in source: f229 d=493 (scale 1), f210 d=376, f190 d=251 (+ dollar behind -> compare non-bg silhouette only)
    for f, D in ((229, 493), (210, 376), (190, 251)):
        R.append(score(comp('bubble_disc', D / 493.0), f, (280, 700, 800, 1210), 'bubble_f%d' % f, out))
    json.dump(R, open(os.path.join(out, 'misc_validation.json'), 'w'), indent=1); [print(r) for r in R]
