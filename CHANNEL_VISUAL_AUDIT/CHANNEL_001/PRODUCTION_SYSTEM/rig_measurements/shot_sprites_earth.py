"""SH018 Earth state sprites A/B. measure(): colour-class region geometry (coarse simplified polygons, +-2px) measured from two reference frames -> earth_traced.json.
draw(): re-draws the two states from those polygons + procedural circle/outlines/spiral eyes at 4x supersampling. No source pixels are copied into the sprites.
Body = union of both states (body is identical in the source; only the two flames change), flames are per-state."""
import os, sys, json, collections
sys.setrecursionlimit(50000)
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); PS = os.path.dirname(HERE); OUT = os.path.join(PS, 'shot_sprites')
PAL = dict(ocean=(10, 26, 68), navy=(36, 58, 106), green=(66, 124, 58), ice=(236, 236, 236), orange=(216, 122, 24), yellow=(236, 200, 60), cream=(240, 233, 202), ink=(6, 6, 6), bg=(253, 253, 253))
RECT = (40, 650, 1000, 1274); DS = 2; S = 4
def classify(rgb):
    keys = list(PAL); P = np.array([PAL[k] for k in keys], float); d = ((rgb[:, :, None, :].astype(float) - P[None, None]) ** 2).sum(-1)
    return np.array(keys)[d.argmin(-1)]
DIRS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
def label(m):
    h, w = m.shape; lab = np.zeros((h, w), int); n = 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and not lab[y, x]:
                n += 1; q = collections.deque([(y, x)]); lab[y, x] = n
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in DIRS:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not lab[ny, nx]: lab[ny, nx] = n; q.append((ny, nx))
    return lab, n
def trace(m):
    H, W = m.shape; P = np.zeros((H + 2, W + 2), bool); P[1:-1, 1:-1] = m
    ys, xs = np.where(P); s = (xs[0], ys[0]); c = s; b = (s[0] - 1, s[1]); pts = [c]; first = None
    for _ in range(200000):
        i = DIRS.index((b[0] - c[0], b[1] - c[1])); moved = False
        for k in range(1, 9):
            d = DIRS[(i + k) % 8]; nx, ny = c[0] + d[0], c[1] + d[1]
            if P[ny, nx]:
                pd = DIRS[(i + k - 1) % 8]; b = (c[0] + pd[0], c[1] + pd[1]); c = (nx, ny); moved = True; break
        if not moved: break
        if c == s and len(pts) > 2: break
        pts.append(c)
    return [(x - 1, y - 1) for x, y in pts]
def dp(pts, eps):
    P = np.array(pts, float); keep = np.zeros(len(P), bool); keep[0] = keep[-1] = True; st = [(0, len(P) - 1)]
    while st:
        i, j = st.pop()
        if j <= i + 1: continue
        a, b = P[i], P[j]; ab = b - a; n = np.hypot(*ab) or 1.0; q = P[i + 1:j] - a
        dist = np.abs(ab[0] * q[:, 1] - ab[1] * q[:, 0]) / n; k = int(dist.argmax())
        if dist[k] > eps: keep[i + 1 + k] = True; st += [(i, i + 1 + k), (i + 1 + k, j)]
    return [tuple(p) for p in P[keep]]
def chaikin(p, it=2):
    for _ in range(it):
        q = []
        for i in range(len(p)):
            a, b = np.array(p[i]), np.array(p[(i + 1) % len(p)]); q += [tuple(.75 * a + .25 * b), tuple(.25 * a + .75 * b)]
        p = q
    return p
def regions(cls, name, min_area, origin=None):
    origin = origin or RECT[:2]
    m = (cls == name); h, w = m.shape; d = DS
    m = m[:h // d * d, :w // d * d].reshape(h // d, d, w // d, d).mean((1, 3)) > .5   # majority downsample = noise filter
    lab, n = label(m); out = []
    for i in range(1, n + 1):
        comp = lab == i
        if comp.sum() * d * d < min_area: continue
        pts = trace(comp); arr = np.array(pts, float); k = int(np.argmax(((arr - arr[0]) ** 2).sum(1)))
        pts = dp(pts[:k + 1], 1.2)[:-1] + dp(pts[k:] + [pts[0]], 1.2)[:-1]
        out.append([[float(x * d + origin[0] + d / 2), float(y * d + origin[1] + d / 2)] for x, y in pts])
    return out
def measure():
    LM = os.environ['LMDIR']; cl = {}
    for st, f in (('A', 'g1110'), ('B', 'g1120')):
        rgb = np.array(Image.open('%s/%s.png' % (LM, f)).convert('RGB'))[RECT[1]:RECT[3], RECT[0]:RECT[2]]; cl[st] = classify(rgb)
    flame = lambda c: np.isin(c, ['orange', 'yellow', 'cream'])
    body = np.where(flame(cl['A']), cl['B'], cl['A']); body[flame(body)] = 'ocean'
    tr = dict(rect=RECT, body={}, flames={})
    for k, a in (('ocean', 500), ('green', 900), ('ice', 900)): tr['body'][k] = regions(body, k, a)   # base disc = light navy; dark-navy patches + land drawn over it
    # circle fit from ink extremes (rows near the equator)
    ink = (body == 'ink'); ys, xs = np.where(ink); xs = xs + RECT[0]; ys = ys + RECT[1]
    row = {}; 
    for y, x in zip(ys, xs): row.setdefault(y, []).append(x)
    y0 = min((y for y in row if 880 < y < 1060), key=lambda y: min(row[y])); xl = min(row[y0]); xr = max(max(v) for y, v in row.items() if 880 < y < 1060)
    tr['circle'] = dict(cx=(xl + xr) / 2, cy=float(y0), r=(xr - xl) / 2)
    for st in 'AB':
        u = cl[st].copy(); u[np.isin(u, ['yellow', 'cream'])] = 'orange'   # silhouette = union, so the orange layer has no hole where the inner flame sits
        tr['flames'][st] = dict(orange=regions(u, 'orange', 200), yellow=regions(cl[st], 'yellow', 200), cream=regions(cl[st], 'cream', 120))
    json.dump(tr, open(os.path.join(HERE, 'earth_traced.json'), 'w')); print('circle', tr['circle'], {k: len(v) for k, v in tr['body'].items()}, {s: {k: len(v) for k, v in f.items()} for s, f in tr['flames'].items()})
def spiral(cx, cy, r, turns=2.8, flip=1):
    pts = []
    for t in np.linspace(0, 1, 70): a = flip * t * turns * 2 * np.pi; rr = r * (.12 + .88 * t); pts.append((cx + rr * np.cos(a), cy + rr * np.sin(a) * 1.15))
    return pts
def draw(state):
    tr = json.load(open(os.path.join(HERE, 'earth_traced.json'))); x0, y0, x1, y1 = RECT; W, H = (x1 - x0) * S, (y1 - y0) * S
    def P(p): return ((p[0] - x0) * S, (p[1] - y0) * S)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); C = tr['circle']; ink = PAL['ink']
    def poly(pts, fill, outline=None, w=0, smooth=True):
        q = chaikin(pts, 2) if smooth else pts; q = [P(p) for p in q]
        if outline: d.line(q + [q[0]], fill=outline, width=round(2 * w * S), joint='curve')   # measured polygons are FILL edges: ink band sits outside them
        if fill: d.polygon(q, fill=fill)
    cx, cy, r = C['cx'], C['cy'], C['r']
    d.ellipse([P((cx - r, cy - r)), P((cx + r, cy + r))], fill=PAL['navy'])
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)   # dark patches are clipped to the globe (flame areas were back-filled as 'ocean' in the body mask)
    for p in tr['body']['ocean']: ld.polygon([P(q) for q in chaikin(p, 2)], fill=PAL['ocean'])
    mk = Image.new('L', im.size, 0); ImageDraw.Draw(mk).ellipse([P((cx - r + 4, cy - r + 4)), P((cx + r - 4, cy + r - 4))], fill=255)
    lay.putalpha(Image.fromarray((np.array(lay.getchannel('A')).astype(int) * np.array(mk).astype(int) // 255).astype('uint8'))); im.alpha_composite(lay)
    for p in tr['body']['green']: poly(p, PAL['green'], ink, 7)
    for p in tr['body']['ice']: poly(p, PAL['ice'], ink, 7)
    d.ellipse([P((cx - r, cy - r)), P((cx + r, cy + r))], outline=ink, width=round(10 * S))
    # spiral eyes (procedural): measured white ovals ~ (445-500, 905-1065) and (555-650, 905-1065)
    for ex, flip in ((472, 1), (602, -1)):
        d.ellipse([P((ex - 42, 907)), P((ex + 42, 1062))], fill=(252, 252, 252, 255), outline=ink, width=round(7 * S))
        pts = [P(p) for p in spiral(ex, 984, 34, flip=flip)]; d.line(pts, fill=ink, width=round(7.5 * S), joint='curve')
    for k, col in (('orange', PAL['orange']), ('yellow', PAL['yellow']), ('cream', PAL['cream'])):
        for p in tr['flames'][state][k]: poly(p, col)
    out = im.resize((W // S, H // S), Image.LANCZOS)
    return out
def measure_small():
    """SH004 Earth traced natively (it is NOT the SH018 globe scaled: different orientation/crop) from f330 (no sweat drop), box (470,735,935,1195)"""
    LM = os.environ['LMDIR']; o = (470, 735); rgb = np.array(Image.open('%s/f330s.png' % LM).convert('RGB'))[o[1]:1195, o[0]:935]; cl = classify(rgb)
    out = {k: regions(cl, k, a, o) for k, a in (('ocean', 150), ('green', 300), ('ice', 300))}
    json.dump(out, open(os.path.join(HERE, 'earth004_traced.json'), 'w')); print('earth004', {k: len(v) for k, v in out.items()})
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'measure_small': measure_small(); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'measure': measure()
    meta = json.load(open(os.path.join(OUT, 'sprites_meta.json')))
    for st in 'AB':
        im = draw(st)
        # source frame clips the whole element to the measured rect rows y656-1263 (flames and globe cut flat): apply the same clip
        a = np.array(im); a[:656 - RECT[1]] = 0; a[1263 - RECT[1] + 1:] = 0; im = Image.fromarray(a)
        im.save(os.path.join(OUT, 'earth_%s.png' % st)); meta['earth_' + st] = dict(x0=RECT[0], y0=RECT[1], w=im.width, h=im.height)
    json.dump(meta, open(os.path.join(OUT, 'sprites_meta.json'), 'w'), indent=1); print('ok')
