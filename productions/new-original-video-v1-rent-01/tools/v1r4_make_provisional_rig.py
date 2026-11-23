"""Provisional (placeholder) host rig for the V1 Rent long-form proof. Procedural PIL drawing, original geometry, NOT Codex art.
Same file names/anchors as CODEX_HANDOFF_V2_LONGFORM_RIG.md so Codex files drop in (renderer prefers v1r4_assets/rig/).
  python3 tools/v1r4_make_provisional_rig.py"""
import json, math, os, random
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = HERE + '/v1r4_assets/provisional'
INK = (31, 36, 48, 255); OLIVE = (91, 107, 58, 255); SKIN = (240, 190, 150, 255); HAIR = (52, 38, 34, 255)
JEANS = (52, 60, 86, 255); WHITE = (255, 255, 255, 255)
S = 2  # supersample


def wob(pts, amp=5.0, seed=1, n=10):
    """densify a polyline and add smooth low-frequency wobble (hand-drawn feel)"""
    rnd = random.Random(seed); out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        for i in range(n):
            t = i / n; out.append([x0 + (x1 - x0) * t, y0 + (y1 - y0) * t])
    out.append(list(pts[-1])); ph = rnd.random() * 6.28
    for i, p in enumerate(out):
        p[0] += amp * math.sin(i * 0.55 + ph); p[1] += amp * math.cos(i * 0.47 + ph * 1.3)
    return out


def stroke(d, pts, w, col, seed=1, amp=5.0):
    p = wob(pts, amp, seed)
    p = [(x * S, y * S) for x, y in p]
    d.line(p, fill=col, width=int(w * S), joint='curve')
    r = w * S / 2
    for x, y in (p[0], p[-1]): d.ellipse([x - r, y - r, x + r, y + r], fill=col)


def blob(d, box, fill, ow=16, seed=1, shape='ellipse', radius=0):
    x0, y0, x1, y1 = [v * S for v in box]; o = ow * S
    if shape == 'ellipse':
        d.ellipse([x0 - o, y0 - o, x1 + o, y1 + o], fill=INK); d.ellipse([x0, y0, x1, y1], fill=fill)
    else:
        d.rounded_rectangle([x0 - o, y0 - o, x1 + o, y1 + o], radius=radius * S + o, fill=INK); d.rounded_rectangle([x0, y0, x1, y1], radius=radius * S, fill=fill)


def finish(im, size):
    return im.resize(size, Image.LANCZOS)


def body(pose):
    W, H = (1500, 1300) if pose == 'point' else (1300, 1300)
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    nx, ny = 650, 70; sh = ny + 50; hipy = 600
    lw = 45
    # legs (ink-jeans) and shoes
    for sgn, sd in ((-1, 3), (1, 4)):
        stroke(d, [(nx + sgn * 30, hipy), (nx + sgn * 60, 900), (nx + sgn * 75, 1175)], lw, JEANS, sd, 4)
        blob(d, [nx + sgn * 75 - 70 + (sgn * 30), 1160, nx + sgn * 75 + 70 + (sgn * 30), 1235], WHITE, 12, shape='rr', radius=30)
    # arms
    up = -20 if pose == 'shrug' else 0
    for sgn, sd in ((-1, 5), (1, 6)):
        s0 = (nx + sgn * 42, sh + up)
        if pose == 'down' or (pose == 'point' and sgn == -1):
            pts = [s0, (nx + sgn * 120, 330), (nx + sgn * 150, 570)]; hand = pts[-1]
        elif pose == 'shrug':
            pts = [s0, (nx + sgn * 210, 330), (nx + sgn * 300, 190)]; hand = pts[-1]
        else:  # point (viewer's right)
            pts = [s0, (nx + sgn * 330, 210), (nx + sgn * 680, 175)]; hand = pts[-1]
        stroke(d, pts, lw, INK, sd, 4)
        hx, hy = hand; blob(d, [hx - 36, hy - 36, hx + 36, hy + 36], SKIN, 12)
    # torso: narrow olive slab
    blob(d, [nx - 42, ny, nx + 42, hipy + 20], OLIVE, 14, shape='rr', radius=38)
    # collar hint
    stroke(d, [(nx - 22, ny + 18), (nx, ny + 70), (nx + 22, ny + 18)], 10, INK, 7, 1)
    return finish(im, (W, H))


def head(kind):
    W = H = 700
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = 350
    # hair behind: curls cluster, swept to viewer's right (side part)
    curls = [(210, 175, 70), (290, 130, 78), (380, 120, 80), (465, 150, 76), (525, 215, 66), (170, 255, 56)]
    for x, y, r in curls: d.ellipse([(x - r - 14) * S, (y - r - 14) * S, (x + r + 14) * S, (y + r + 14) * S], fill=INK)
    blob(d, [70, 140, 630, 670], SKIN, 20)
    for x, y, r in curls: d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=HAIR)
    # fringe curls in front of forehead, side part on viewer's left
    fr = [(260, 230, 52), (340, 215, 56), (425, 230, 50)]
    for x, y, r in fr: d.ellipse([(x - r - 12) * S, (y - r - 12) * S, (x + r + 12) * S, (y + r + 12) * S], fill=INK)
    for x, y, r in fr: d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=HAIR)
    ex = (275, 430, 425, 430)
    def eye(x, y, r=17): d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=INK)
    eye(ex[0], ex[1]); eye(ex[2], ex[3])
    brow = lambda a, b, w=15, sd=1: stroke(d, [a, b], w, INK, sd, 1.5)
    if kind == 'neutral':
        brow((235, 372), (315, 368)); brow((385, 368), (465, 372)); stroke(d, [(310, 545), (390, 545)], 14, INK, 3, 1.5)
    elif kind == 'smile':
        brow((235, 365), (315, 358)); brow((385, 358), (465, 365))
        stroke(d, [(280, 520), (320, 565), (380, 565), (420, 520)], 14, INK, 4, 1.5)
    elif kind == 'worried':
        brow((235, 385), (318, 345)); brow((382, 345), (465, 385))
        stroke(d, [(295, 560), (322, 538), (350, 560), (378, 538), (405, 560)], 13, INK, 5, 1.2)
    elif kind == 'surprised':
        brow((235, 335), (315, 322)); brow((385, 322), (465, 335))
        d.ellipse([(322) * S, (520) * S, (378) * S, (590) * S], fill=INK)
        d.ellipse([(333) * S, (531) * S, (367) * S, (579) * S], fill=(120, 60, 60, 255))
    elif kind == 'smirk':
        brow((235, 380), (315, 372)); brow((385, 335), (465, 352), 15, 9)
        stroke(d, [(300, 560), (360, 548), (415, 515)], 14, INK, 6, 1.2)
    return finish(im, (W, H))


def main():
    os.makedirs(OUT, exist_ok=True); anchors = {}
    for p in ('down', 'shrug', 'point'):
        im = body(p); im.save('%s/rig_body_%s.png' % (OUT, p)); anchors['rig_body_%s.png' % p] = dict(neck=[650, 70], size=list(im.size))
    for k in ('neutral', 'smile', 'worried', 'surprised', 'smirk'):
        im = head(k); im.save('%s/rig_head_%s.png' % (OUT, k)); anchors['rig_head_%s.png' % k] = dict(chin=[350, 650], size=list(im.size))
    json.dump(anchors, open(OUT + '/rig_anchors.json', 'w'), indent=1)
    print('wrote', len(anchors), 'files to', OUT)

if __name__ == '__main__': main()
