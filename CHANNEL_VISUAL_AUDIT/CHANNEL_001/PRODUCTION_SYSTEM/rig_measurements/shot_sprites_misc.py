"""Complete sprites for: calendar icon (SH005/017), SH003 bubble disc + burst particles, SH004 brown-haired man. Drawn from measured geometry (coarse polylines /
circle+capsule parameters, +-2px); no source pixels are copied. `python3 shot_sprites_misc.py measure` re-measures the man outline from the reference frame (needs LMDIR)."""
import os, sys, json
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); PS = os.path.dirname(HERE); OUT = os.path.join(PS, 'shot_sprites'); S = 4
INK = (6, 6, 6, 255)
def new(box):
    W, H = (box[2] - box[0]) * S, (box[3] - box[1]) * S; im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); return im, ImageDraw.Draw(im), (lambda p: ((p[0] - box[0]) * S, (p[1] - box[1]) * S))
def line(d, P, pts, w, col=INK):
    q = [P(p) for p in pts]; d.line(q, fill=col, width=round(w * S), joint='curve'); r = w * S / 2
    for x, y in (q[0], q[-1]): d.ellipse([x - r, y - r, x + r, y + r], fill=col)
def fin(im): return im.resize((im.width // S, im.height // S), Image.LANCZOS)
def catmull(pts, n=10):
    P_ = [pts[0]] + list(pts) + [pts[-1]]; out = []
    for i in range(1, len(P_) - 2):
        p0, p1, p2, p3 = map(np.array, (P_[i - 1], P_[i], P_[i + 1], P_[i + 2]))
        for t in np.linspace(0, 1, n, endpoint=False): out.append(tuple(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3)))
    out.append(tuple(P_[-2])); return out
# ---------------- calendar (measured bbox x133-261,y901-1029; red header 143-251 x 918-935; 5 red tiles 14x14 with ink ring)
def calendar():
    box = (125, 895, 270, 1035); im, d, P = new(box); RED = (198, 62, 52, 255); GREY = (242, 242, 242, 255)
    d.rounded_rectangle([P((133, 910)), P((261, 1029))], radius=12 * S, fill=INK)                 # outer ink body (measured outer bbox x133-261,y910-1029)
    d.rounded_rectangle([P((142, 944)), P((250, 1020))], radius=5 * S, fill=GREY)                 # grey page (x142-250,y944-1020)
    d.rounded_rectangle([P((143, 918)), P((251, 936))], radius=4 * S, fill=RED)                   # red header (x143-251,y918-935)
    for x in (154, 183, 213, 241): line(d, P, [(x, 903), (x, 919)], 5.5)
    for (cx, cy) in ((196.5, 962), (230.5, 962), (164, 996.5), (196.5, 996.5), (230.5, 996.5)):
        d.rounded_rectangle([P((cx - 11, cy - 11)), P((cx + 11, cy + 11))], radius=7 * S, fill=INK); d.rounded_rectangle([P((cx - 7, cy - 7)), P((cx + 7, cy + 7))], radius=4 * S, fill=RED)
    return fin(im), box
# ---------------- SH003 bubble disc (alpha .62 teal, solved from over-white/over-black samples) + two highlight crescents; base diameter 493 at centre (536.5,954.5)
BUB = (29, 143, 150); BUBA = round(.62 * 255); HIL = (155, 213, 222)
def bubble():
    cx, cy, D = 536.5, 954.5, 493; box = (int(cx - D / 2 - 6), int(cy - D / 2 - 6), int(cx + D / 2 + 6), int(cy + D / 2 + 6)); im, d, P = new(box)
    d.ellipse([P((cx - D / 2, cy - D / 2 + 3)), P((cx + D / 2, cy + D / 2 - 3))], fill=BUB + (BUBA,))
    u = D / 376.0; ox, oy = 537, 955   # highlight geometry measured at f210 (d=376), scaled to base diameter
    def T(x, y): return (cx + (x - ox) * u, cy + (y - oy) * u)
    for pts, w in (([(508, 826), (462, 850), (425, 900), (422, 972)], 52), ([(668, 975), (650, 1030), (606, 1072), (586, 1080)], 30)):
        line(d, P, catmull([T(*p) for p in pts]), w * u, HIL + (BUBA,))
    return fin(im), box
# ---------------- SH003 burst particles (f230-242 static): circles (centre,r), capsules (p0,p1,w); teal (118,187,192) + highlight (196,230,236)
TEAL = (118, 187, 192, 255); LT = (196, 230, 236, 255)
def burst():
    box = (280, 740, 830, 1175); im, d, P = new(box)
    for (cx, cy, r) in ((391.5, 773.5, 25.5), (616, 852, 25.5), (789, 962, 25.5), (377, 1074, 40.5), (535.5, 1140.5, 25.5)):
        d.ellipse([P((cx - r, cy - r)), P((cx + r, cy + r))], fill=TEAL)
        d.ellipse([P((cx - .62 * r, cy - .66 * r)), P((cx - .08 * r, cy - .02 * r))], fill=LT)       # big highlight upper-left
        d.ellipse([P((cx + .36 * r, cy + .26 * r)), P((cx + .62 * r, cy + .52 * r))], fill=LT)       # small dot lower-right
    for (a, b, w) in (((299, 953), (371, 953), 17), ((513, 781), (513, 872), 17), ((640, 1053), (703, 1112), 17)):
        line(d, P, [a, b], w, TEAL); line(d, P, [(a[0] + (b[0] - a[0]) * .18, a[1] + (b[1] - a[1]) * .18), (a[0] + (b[0] - a[0]) * .7, a[1] + (b[1] - a[1]) * .7)], w * .45, LT)
    return fin(im), box
# ---------------- SH004 brown-haired man (traced outline + hand-read arms); neutral face
def man():
    TR = json.load(open(os.path.join(HERE, 'man_traced.json'))); box = (100, 855, 380, 1265); im, d, P = new(box)
    TAN = (206, 172, 138, 255); BROWN = (102, 79, 57, 255)
    cx, cy = TR['ring_c']; ring = [(cx + r * np.cos(np.deg2rad(t)), cy - r * np.sin(np.deg2rad(t))) for t, r in zip(TR['ring_deg'], TR['ring_r'])]
    q = [P(p) for p in ring]; d.polygon(q, fill=TAN); d.line(q + [q[0]], fill=INK, width=round(11 * S), joint='curve')
    hair = [tuple(p) for p in TR['hair_top']] + [tuple(p) for p in TR['hair_bot'][::-1]]; hq = [P(p) for p in hair]
    d.line(hq + [hq[0]], fill=INK, width=round(22 * S), joint='curve'); d.polygon(hq, fill=BROWN)    # fill edge measured -> ink band outside
    for (ex, ey, rx, ry) in ((221, 985, 7, 10.5), (267, 985, 6.5, 10.5)): d.ellipse([P((ex - rx, ey - ry)), P((ex + rx, ey + ry))], fill=INK)
    line(d, P, [(222, 1015), (246, 1017)], 8.5)
    line(d, P, [(237, 1056), (240, 1090), (246, 1180), (250, 1262)], 9); d.rectangle([P((244, 1258)), P((256, 1266))], fill=(0, 0, 0, 0))
    line(d, P, catmull([(239, 1090), (222, 1112), (206, 1148), (203, 1160), (186, 1146), (150, 1130), (121, 1127)]), 9)
    line(d, P, catmull([(240, 1090), (272, 1108), (298, 1136), (314, 1157), (326, 1128), (338, 1085), (358, 1072)]), 9)
    return fin(im), box

# ---------------- SH004 Earth (same body art as SH018, scaled to measured d=448 at centre (700,964); no flames) with googly (A) / lidded+sweat (B) eyes
def earth_small(state):
    import shot_sprites_earth as E
    tr = {'body': json.load(open(os.path.join(HERE, 'earth004_traced.json')))}; ox, oy = 700.0, 964.0   # natively traced (not the SH018 globe scaled)
    def T(p): return (p[0], p[1])
    box = (470, 735, 935, 1195); im, d, P = new(box)
    def poly(pts, fill, w=0):
        q = [P(T(p)) for p in E.chaikin(pts, 2)]
        if w: d.line(q + [q[0]], fill=INK, width=round(2 * w * S), joint='curve')
        d.polygon(q, fill=fill)
    d.ellipse([P((ox - 224, oy - 224)), P((ox + 224, oy + 224))], fill=E.PAL['navy'])
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    for q_ in tr['body']['ocean']: ld.polygon([P(T(p_)) for p_ in E.chaikin(q_, 2)], fill=E.PAL['ocean'])
    mk = Image.new('L', im.size, 0); ImageDraw.Draw(mk).ellipse([P((ox - 220, oy - 220)), P((ox + 220, oy + 220))], fill=255)
    lay.putalpha(Image.fromarray((np.array(lay.getchannel('A')).astype(int) * np.array(mk).astype(int) // 255).astype('uint8'))); im.alpha_composite(lay)
    for q_ in tr['body']['green']: poly(q_, E.PAL['green'], 6.4)
    for q_ in tr['body']['ice']: poly(q_, E.PAL['ice'], 6.4)
    d.ellipse([P((ox - 224, oy - 224)), P((ox + 224, oy + 224))], outline=INK, width=round(9 * S))
    W = (252, 252, 252, 255)
    for (x0, x1, px, py) in (((642, 697), (714, 769), None, None),)[0:0] or []: pass
    eyes = ((669.5, 972.5), (741.5, 972.5)); pup = {'A': ((653.5, 974.5), (724.5, 970.5)), 'B': ((669, 974.5), (739.5, 974.5))}[state]
    for (ex, ey), (qx, qy) in zip(eyes, pup):
        el = Image.new('RGBA', im.size, (0, 0, 0, 0)); ed = ImageDraw.Draw(el)
        ed.ellipse([P((ex - 27.5, 929)), P((ex + 27.5, 1016))], fill=W, outline=INK, width=round(5.5 * S))
        yl, yr = (952, 944) if ex < 700 else (944, 952)
        if state == 'B': ed.polygon([P((ex - 32, 920)), P((ex + 32, 920)), P((ex + 32, yr)), P((ex - 32, yl))], fill=(0, 0, 0, 0))   # lidded: erase everything above the slanted lid line
        im.alpha_composite(el); d = ImageDraw.Draw(im)
        if state == 'B': line(d, P, [(ex - 28, yl), (ex + 28, yr)], 6)
        d.ellipse([P((qx - 8.5, qy - 11.5)), P((qx + 8.5, qy + 11.5))], fill=INK)
    if state == 'B':
        drop = [(826, 851), (838, 872), (848, 897), (843, 917), (826, 929), (808, 918), (803, 898), (813, 872)]
        q = [P(p) for p in catmull(drop + [drop[0], drop[1]], 6)]; d.polygon(q, fill=(81, 195, 217, 255)); d.line(q, fill=INK, width=round(5 * S), joint='curve')
    return fin(im), box

# ---------------- bare "$" (SH003 f243+; the approved prop_dollar_sign is the in-bubble composite, not this) : two bars + S curve, measured centrelines, green 11px on ink 21px
def dollar():
    box = (475, 835, 612, 1080); im, d, P = new(box); G = (48, 152, 52, 255)
    Sc = [(572, 917), (562, 899), (542, 889), (519, 890), (503, 905), (498, 925), (510, 938), (538, 945), (567, 955), (586, 970), (590, 985), (576, 1001), (548, 1007), (520, 1004), (502, 992), (494, 978)]
    paths = [[(521, 853), (521, 1042)], [(540, 852), (556, 1061)], catmull(Sc, 8)]
    for pts in paths: line(d, P, pts, 21, INK)
    for pts in paths: line(d, P, pts, 11, G)
    return fin(im), box

# ---------------- red left arrow (SH005/SH017 timeline): measured red bbox x640-813,y930-1003, shaft y958-977, colour (199,42,45)
def arrow():
    box = (630, 920, 825, 1015); im, d, P = new(box); R = (199, 42, 45, 255)
    line(d, P, [(650, 967.5), (803.5, 967.5)], 19, R); line(d, P, [(688, 939.5), (649.5, 967.5), (688, 993.5)], 19, R)
    return fin(im), box
def measure():
    LM = os.environ['LMDIR']; a = np.array(Image.open(LM + '/g340.png').convert('RGB')).astype(int)
    brown = (np.abs(a - np.array([102, 79, 57])).sum(-1) < 22); ink = a.sum(-1) < 150
    from PIL import ImageFilter
    brown = np.array(Image.fromarray((brown * 255).astype('uint8')).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))) > 0   # opening: drops black/tan anti-alias blends that mimic brown
    sub = np.zeros_like(brown); sub[860:1000, 100:340] = True; brown &= sub
    top, bot = [], []
    for x in range(100, 335, 2):
        c = np.where(brown[:, x])[0]
        if len(c): top.append((x, int(c.min()))); bot.append((x, int(c.max())))
    cx, cy = 232, 995; ring_deg = list(range(0, 360, 5)); rr = []
    for t in ring_deg:
        dd = np.deg2rad(t); best = 0
        for r in range(50, 110):
            x, y = int(round(cx + r * np.cos(dd))), int(round(cy - r * np.sin(dd)))
            if 0 <= y < 1920 and ink[y, x] and not brown[y, x]: best = r
        rr.append(best)
    rr = np.array(rr, float); rr0 = rr.copy(); med = np.array([np.median([rr[(j + k) % len(rr)] for k in range(-3, 4)]) for j in range(len(rr))])
    bad = (rr < 55) | (np.abs(rr - med) > 6) | ((np.array(ring_deg) >= 250) & (np.array(ring_deg) <= 290)); bad0 = bad.copy(); good = np.where(~bad)[0]; n = len(rr)
    rr = np.interp(np.arange(n), np.r_[good - n, good, good + n], np.r_[rr[good], rr[good], rr[good]])
    ok = np.array(ring_deg); pts_ = np.array([(cx + r * np.cos(np.deg2rad(t)), cy - r * np.sin(np.deg2rad(t))) for t, r, b in zip(ring_deg, [float(v) for v in rr0], bad0) if not b])
    A_ = np.c_[2 * pts_, np.ones(len(pts_))]; sol = np.linalg.lstsq(A_, (pts_ ** 2).sum(1), rcond=None)[0]; fcx, fcy = sol[0], sol[1]; fr = float(np.sqrt(sol[2] + fcx ** 2 + fcy ** 2))
    print('head circle fit', fcx, fcy, fr)
    json.dump(dict(ring_c=[float(fcx), float(fcy)], ring_deg=ring_deg, ring_r=[round(fr - 5.5, 1)] * len(ring_deg), hair_top=top, hair_bot=bot), open(os.path.join(HERE, 'man_traced.json'), 'w')); print('man measured', len(top))
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'measure': measure()
    meta = json.load(open(os.path.join(OUT, 'sprites_meta.json')))
    for name, fn in (('calendar', calendar), ('bubble_disc', bubble), ('burst_particles', burst), ('man_brown', man), ('dollar_bare', dollar), ('arrow_left', arrow), ('earth_sh004_A', lambda: earth_small('A')), ('earth_sh004_B', lambda: earth_small('B'))):
        im, box = fn(); im.save(os.path.join(OUT, name + '.png')); meta[name] = dict(x0=box[0], y0=box[1], w=im.width, h=im.height)
    json.dump(meta, open(os.path.join(OUT, 'sprites_meta.json'), 'w'), indent=1); print('ok')
