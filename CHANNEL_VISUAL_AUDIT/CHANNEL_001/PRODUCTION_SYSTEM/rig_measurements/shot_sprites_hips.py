"""Complete hips pose sprites (whole figure, playback scale 1080x1920 coords, drawn 4x supersampled). Drawn procedurally from MEASURED landmarks
(hips_landmarks.json + hips_traced.json: coarse polylines/radial profile, +-1.5px). No source pixels are copied. Not a reusable rig."""
import os, json
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); PS = os.path.dirname(HERE); OUT = os.path.join(PS, 'shot_sprites'); os.makedirs(OUT, exist_ok=True)
LM = json.load(open(os.path.join(HERE, 'hips_landmarks.json'))); TR = json.load(open(os.path.join(HERE, 'hips_traced.json')))
BOX = (420, 750, 660, 1200); S = 4; INK = (14, 14, 14, 255); PEACH = (250, 212, 180, 255)
def sm(pts, n=3):   # light smoothing of a measured polyline
    p = np.array(pts, float); q = p.copy()
    for i in range(len(p)): q[i] = p[max(0, i - n // 2):i + n // 2 + 1].mean(0)
    q[0], q[-1] = p[0], p[-1]; return [tuple(v) for v in q]
def catmull(pts, n=10):
    P = [pts[0]] + list(pts) + [pts[-1]]; out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = map(np.array, (P[i - 1], P[i], P[i + 1], P[i + 2]))
        for t in np.linspace(0, 1, n, endpoint=False): out.append(tuple(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3)))
    out.append(tuple(P[-2])); return out
def draw(arm_R, mouth, bw=4.5):
    W, H = (BOX[2] - BOX[0]) * S, (BOX[3] - BOX[1]) * S
    def P(p): return ((p[0] - BOX[0]) * S, (p[1] - BOX[1]) * S)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    def line(pts, w=bw):
        pts = [P(p) for p in pts]; d.line(pts, fill=INK, width=round(w * S), joint='curve'); r = w * S / 2
        for x, y in (pts[0], pts[-1]): d.ellipse([x - r, y - r, x + r, y + r], fill=INK)
    A = LM['src']['A']; B = LM['src']['B_right']
    # head
    cx, cy = TR['head_ring_c']; ring = [(cx + r * np.cos(np.deg2rad(t)), cy - r * np.sin(np.deg2rad(t))) for t, r in zip(TR['head_ring_deg'], TR['head_ring_r'])]
    d.polygon([P(p) for p in ring], fill=PEACH); line(ring + [ring[0], ring[1]], bw)
    hair = [(x, y) for x, y in TR['hair_top']] + [(x, y) for x, y in TR['hair_bot'][::-1]]
    d.polygon([P(p) for p in hair], fill=INK)
    for e in (TR['eyeL'], TR['eyeR']):
        x, y = P(e[:2]); r = e[2] * S; d.ellipse([x - r, y - r, x + r, y + r], fill=INK)
    line(sm(TR['mouth_' + mouth]), 6.5)
    # body (landmark-derived)
    line([(535.5, 953), (534, 1040), (532, 1126)])
    line([A['L_sh'], A['L_elbow'], A['L_hand']]); line([A['R_sh'], A['R_elbow'], A['R_hand']] if arm_R == 'A' else [B['R_sh'], B['R_elbow'], B['R_hand']])
    line(catmull(sm([(532, 1126)] + TR['legL'], 3))); line(catmull(sm([(532, 1126)] + TR['legR'], 3)))
    return im.resize((W // S, H // S), Image.LANCZOS)
meta = {}
for name, arm, mouth in (('hips_A_happy', 'A', 'happy'), ('hips_A_neutral', 'A', 'neutral'), ('hips_B_happy', 'B', 'happy')):
    im = draw(arm, mouth); im.save(os.path.join(OUT, name + '.png')); meta[name] = dict(x0=BOX[0], y0=BOX[1], w=im.width, h=im.height)
json.dump(meta, open(os.path.join(OUT, 'sprites_meta.json'), 'w'), indent=1); print(meta)
