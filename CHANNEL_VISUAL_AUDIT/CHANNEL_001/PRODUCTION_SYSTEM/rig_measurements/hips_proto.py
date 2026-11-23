"""Hips pose prototype v3: ONE silhouette drawn from measured landmarks (rig_measurements/hips_landmarks.json),
then split into layers; verifies layers recompose to the whole and compares to the source at playback scale.
Prototype = diagnostic / spec art, NOT a registered asset."""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); PS = os.path.dirname(HERE)
LM = json.load(open(os.path.join(HERE, 'hips_landmarks.json'))); K = LM['k_canvas_per_src']; SS = 2
W = 2048; STROKE = round(4.5 * K)
def C(x, y): return (round(1024 + (x - 535.5) * K), round(320 + (y - 953) * K))
def curve(pts, n=24):
    """quadratic/cubic-ish smooth path through control pts via Catmull-Rom"""
    P = [pts[0]] + list(pts) + [pts[-1]]; out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = map(np.array, (P[i - 1], P[i], P[i + 1], P[i + 2]))
        for t in np.linspace(0, 1, n, endpoint=False):
            out.append(tuple(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3)))
    out.append(tuple(P[-2])); return out
def layer(paths):
    im = Image.new('L', (W * SS, W * SS), 0); d = ImageDraw.Draw(im); r = STROKE * SS / 2
    for pts in paths:
        pts = [(x * SS, y * SS) for x, y in pts]
        d.line(pts, fill=255, width=STROKE * SS, joint='curve')
        for x, y in (pts[0], pts[-1]): d.ellipse([x - r, y - r, x + r, y + r], fill=255)
    a = im.resize((W, W), Image.LANCZOS); out = Image.new('RGBA', (W, W), (14, 14, 14, 0)); out.putalpha(a); return out
A = LM['src']['A']; B = LM['src']['B_right']
spine = [C(535.5, 953), C(534, 1040), C(532, 1126)]
layers = {
 'rig_torso': [spine],
 'rig_arm_left_hips': [[C(*A['L_sh']), C(*A['L_elbow']), C(*A['L_hand'])]],
 'rig_arm_right_hips': [[C(*A['R_sh']), C(*A['R_elbow']), C(*A['R_hand'])]],
 'rig_arm_right_hips_B': [[C(*B['R_sh']), C(*B['R_elbow']), C(*B['R_hand'])]],
 'rig_legs': [curve([C(532, 1126), C(515, 1140), C(495, 1160), C(481, 1175), C(478, 1172)]), curve([C(532, 1126), C(552, 1137), C(580, 1162), C(596, 1180)])],
}
def compose(names):
    base = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    for n in names: base = Image.alpha_composite(base, LAYERS[n])
    return base
LAYERS = {n: layer(p) for n, p in layers.items()}
HK = 729 / 184.0   # head-canvas px per source px (approved heads: 729 px visible height <-> 184 src px)
def H(x, y): return (521 + (x - 535.5) * HK, 887 + (y - 953) * HK)
PEACH = (250, 212, 180, 255); INK = (14, 14, 14, 255)
def head_layers(mouth='happy'):
    """black-haired reference head (SH008-SH022) drawn on a 1024 head canvas, neck anchor (521,887) like char_head"""
    S = 2; N = 1024 * S; out = {}
    def new(): im = Image.new('RGBA', (N, N), (0, 0, 0, 0)); return im, ImageDraw.Draw(im)
    def sc(p): return tuple(v * S for v in H(*p))
    im, d = new(); (x0, y0), (x1, y1) = sc((454, 790)), sc((629, 951))
    d.ellipse([x0, y0, x1, y1], fill=PEACH, outline=INK, width=round(5 * HK * S)); out['face'] = im
    im, d = new()
    hair = [(465, 820), (462, 807), (470, 800), (480, 790), (486, 783), (495, 775), (505, 773), (512, 768), (530, 766), (545, 768), (560, 764), (580, 765), (595, 771), (583, 775), (575, 783), (560, 785), (545, 790), (530, 794), (520, 800), (505, 808), (495, 815), (475, 825)]
    d.polygon([sc(p) for p in hair], fill=INK)
    out['hair'] = im
    im, d = new(); r = 5.2 * HK * S
    for (ex, ey) in ((508.5, 836), (568, 826)): cx, cy = sc((ex, ey)); d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)
    mw = round(5.5 * HK * S)
    pts = [(497, 874), (506, 884), (520, 893), (540, 898), (566, 897)] if mouth == 'happy' else [(505, 887), (541, 886), (577, 886)]
    d.line([sc(p) for p in pts], fill=INK, width=mw, joint='curve')
    out['mouth_eyes'] = im
    return {k: v.resize((1024, 1024), Image.LANCZOS) for k, v in out.items()}
def to_source(body, mouth='happy', size=(1080, 1920)):
    bg = Image.new('RGBA', size, (255, 255, 255, 255))
    s = body.resize((round(W / K), round(W / K)), Image.LANCZOS); bg.alpha_composite(s, (round(535.5 - 1024 / K), round(953 - 320 / K)))
    hs = round(1024 / HK)
    for n, l in head_layers(mouth).items():
        l = l.resize((hs, hs), Image.LANCZOS); bg.alpha_composite(l, (round(535.5 - 521 / HK), round(953 - 887 / HK)))
    return bg.convert('RGB')
if __name__ == '__main__':
    out = os.path.join(HERE, 'prototype'); os.makedirs(out, exist_ok=True)
    for n, im in LAYERS.items(): im.save(os.path.join(out, n + '.png'))
    for m in ('happy', 'neutral'):
        for n, im in head_layers(m).items(): im.save(os.path.join(out, 'head_%s_%s.png' % (m, n)))
    res = {}
    for tag, names, frame in (('A', ['rig_torso', 'rig_arm_left_hips', 'rig_arm_right_hips', 'rig_legs'], 647), ('B', ['rig_torso', 'rig_arm_left_hips', 'rig_arm_right_hips_B', 'rig_legs'], 520)):
        whole = compose(names)
        pv = to_source(whole, 'happy' if tag in ('A', 'B') else 'neutral'); pv.save(os.path.join(out, 'proto_%s_playback.png' % tag))
        ref = Image.open(os.environ['LMDIR'] + '/f%d.png' % frame).convert('RGB')
        box = (380, 955, 700, 1230)
        a = np.array(pv.crop(box).convert('L')) < 110; b = np.array(ref.crop(box).convert('L')) < 110
        iou = (a & b).sum() / max(1, (a | b).sum())
        # tolerant overlap: dilate 3px
        from PIL import ImageFilter
        da = np.array(Image.fromarray((a * 255).astype('uint8')).filter(ImageFilter.MaxFilter(7))) > 0
        db = np.array(Image.fromarray((b * 255).astype('uint8')).filter(ImageFilter.MaxFilter(7))) > 0
        cov_ref = (b & da).sum() / b.sum(); cov_proto = (a & db).sum() / a.sum()
        res[tag] = dict(frame=frame, body_iou=round(float(iou), 3), ref_ink_within3px_of_proto=round(float(cov_ref), 3), proto_ink_within3px_of_ref=round(float(cov_proto), 3))
        cmp = Image.new('RGB', (640 * 3, 560), 'white')
        for i, im in enumerate((ref.crop((380, 760, 700, 1230)), pv.crop((380, 760, 700, 1230)))): cmp.paste(im.resize((640, 940))[:, :560] if False else im.resize((380, 560)), (i * 400, 0))
        diff = Image.new('RGB', (320, 470), 'white'); full_a = np.array(pv.crop((380, 760, 700, 1230)).convert('L')) < 110; full_b = np.array(ref.crop((380, 760, 700, 1230)).convert('L')) < 110
        arr = np.full((470, 320, 3), 255, 'uint8'); arr[full_b & ~full_a] = (230, 40, 40); arr[full_a & ~full_b] = (40, 80, 230); arr[full_a & full_b] = (0, 0, 0)
        Image.fromarray(arr).resize((380, 560)).save(os.path.join(out, 'diff_%s.png' % tag)); cmp.save(os.path.join(out, 'cmp_%s.png' % tag))
        # layers recompose to whole
        rec = np.array(Image.alpha_composite(Image.new('RGBA', (W, W), (0, 0, 0, 0)), whole).getchannel('A')); res[tag]['layers_alpha_max'] = int(rec.max())
    json.dump(res, open(os.path.join(HERE, 'hips_proto_report.json'), 'w'), indent=1); print(json.dumps(res, indent=1))
