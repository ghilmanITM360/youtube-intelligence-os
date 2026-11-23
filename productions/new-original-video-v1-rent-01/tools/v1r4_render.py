"""V1 Rent R4: long-form-grammar re-block of the 0-75 s segment (R3 baseline untouched).
White canvas, hard-cut beats, thin-body host (rig layers), hand-drawn graphics, stepped 24 fps content in a 30 fps file.
  python3 tools/v1r4_render.py --still 2.0,4.5 [--dur 16.5]     # stills to out_r4/stills
  python3 tools/v1r4_render.py --dur 16.5 --out out_r4/proof.mp4  # proof
  python3 tools/v1r4_render.py --out out_r4/V1_RENT_R4_0-75s.mp4  # full
  python3 tools/v1r4_render.py --storyboard                       # writes STORYBOARD_R4_75s.md
Numbers/sources: SEGMENT_0_75_CLAIM_REGISTER.md (C-01..C-05). Narration: Take 2 wav, timings from t2_words_merged.json."""
import json, os, sys, math, hashlib, subprocess
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v1r4_make_provisional_rig import wob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS, CFPS = 1920, 1080, 30, 24
BG = (253, 253, 253); INK = (31, 36, 48); RED = (216, 44, 44); OLIVE = (91, 107, 58); BLUE = (70, 140, 190)
ORANGE = (240, 150, 60); GREYF = (226, 226, 226); GREYT = (70, 74, 84); OLIVE_L = (176, 188, 140); PAPER = (255, 255, 255)
WAV = HERE + '/audio/take2/v1_rent_take2.wav'
WAV_SHA = '3ef0297814e610d64f2ebc30e41bdac1df934edcbe437648c354930081c14b6e'
MARKER = '/System/Library/Fonts/MarkerFelt.ttc'; HELV = '/System/Library/Fonts/Helvetica.ttc'
_fc = {}
FD = HERE + '/v1r4_assets/fonts_ofl/'
NUMFONT = None; PLAINFONT = None  # R9: set to an OFL file name in fonts_ofl/ to override numerals / source tags; None = R7 behaviour
def font(kind, size):
    """OFL fonts (Patrick Hand = labels/numerals, Caveat Brush = display words, Helvetica = source tags unless PLAINFONT is set). Apple Marker Felt/Chalkboard dropped: no redistributable licence."""
    k = (kind, size)
    if k not in _fc:
        if kind == 'num' and NUMFONT: _fc[k] = ImageFont.truetype(FD + NUMFONT, size)
        elif kind == 'plain' and PLAINFONT: _fc[k] = ImageFont.truetype(FD + PLAINFONT, size)
        else: _fc[k] = ImageFont.truetype(FD + 'caveatbrush_CaveatBrush-Regular.ttf', size) if kind == 'wide' else ImageFont.truetype(FD + 'patrickhand_PatrickHand-Regular.ttf', int(size * (1.18 if kind == 'hand' else 1.0))) if kind in ('hand', 'num') else ImageFont.truetype(HELV, size)
    return _fc[k]

# ---------------- rig ----------------
RIG = HERE + '/v1r4_assets/rig' if os.path.exists(HERE + '/v1r4_assets/rig/rig_anchors.json') else HERE + '/v1r4_assets/provisional'
ANCH = json.load(open(RIG + '/rig_anchors.json')); _rc = {}
def host_img(pose, head, s):
    k = (pose, head, s)
    if k in _rc: return _rc[k]
    b = Image.open('%s/rig_body_%s.png' % (RIG, pose)); h = Image.open('%s/rig_head_%s.png' % (RIG, head))
    bn = ANCH['rig_body_%s.png' % pose]['neck']; hc = ANCH['rig_head_%s.png' % head]['chin']
    b = b.resize((int(b.width * s), int(b.height * s)), Image.LANCZOS); h = h.resize((int(h.width * s), int(h.height * s)), Image.LANCZOS)
    top = int(hc[1] * s); canvas = Image.new('RGBA', (b.width, b.height + top), (0, 0, 0, 0))
    canvas.alpha_composite(b, (0, top)); nx, ny = int(bn[0] * s), int(bn[1] * s) + top
    canvas.alpha_composite(h, (nx - int(hc[0] * s), ny - int(hc[1] * s)))
    _rc[k] = (canvas, nx, ny); return _rc[k]

# ---------------- drawing helpers (2x supersampled, hand wobble) ----------------
S2 = 2
def layer(w, h): return Image.new('RGBA', (int(w * S2), int(h * S2)), (0, 0, 0, 0))
def done(im): return im.resize((im.width // S2, im.height // S2), Image.LANCZOS)
def poly(d, pts, w, col, seed=1, amp=3.0, n=8, ox=0, oy=0):
    p = wob(pts, amp, seed, n); p = [((x + ox) * S2, (y + oy) * S2) for x, y in p]
    d.line(p, fill=col + (255,), width=int(w * S2), joint='curve'); r = w * S2 / 2
    for x, y in (p[0], p[-1]): d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,))
def partial(pts, p):
    if p >= 1: return pts
    L = [math.dist(a, b) for a, b in zip(pts, pts[1:])]; tot = sum(L) * max(p, 0.001); out = [pts[0]]
    for (a, b), l in zip(zip(pts, pts[1:]), L):
        if tot >= l: out.append(b); tot -= l
        else: out.append((a[0] + (b[0] - a[0]) * tot / l, a[1] + (b[1] - a[1]) * tot / l)); break
    return out

class It:
    def __init__(s, t0, fn, mode='pop', dur=0.3, steps=5): s.t0, s.fn, s.mode, s.dur, s.steps, s.cache = t0, fn, mode, dur, steps, {}
    def get(s, p):
        k = round(p * s.steps) if s.mode == 'draw' else 0
        if k not in s.cache: s.cache[k] = s.fn(k / s.steps if s.mode == 'draw' else 1.0)
        return s.cache[k]
POP = [0.6, 1.1, 1.0]

def paste_pop(canvas, it, tq):
    age = tq - it.t0
    if age < 0: return
    if it.mode == 'dyn':
        r = it.fn(tq)
        if r: canvas.paste(r[0], (int(r[1]), int(r[2])), r[0])
        return
    if it.mode == 'draw': p = min(1.0, age / it.dur); im, x, y = it.get(p); canvas.paste(im, (int(x), int(y)), im); return
    im, x, y = it.get(1.0); fi = int(age * CFPS + 1e-6)
    if it.mode == 'pop' and fi < 2:
        sc = POP[fi]; w, h = int(im.width * sc), int(im.height * sc); im = im.resize((max(1, w), max(1, h)), Image.LANCZOS)
        x, y = x + (it.get(1.0)[0].width - w) / 2, y + (it.get(1.0)[0].height - h) / 2
    canvas.paste(im, (int(x), int(y)), im)

# ---------------- element builders ----------------
def txt(s, x, y, size, color=INK, t0=0, kind='hand', anchor='c', rot=0, mode='pop'):
    def f(_):
        ft = font(kind, size); lines = s.split('\n'); lh = int(size * 1.15); wmax = max(ft.getlength(l) for l in lines)
        asc, desc = ft.getmetrics(); oh = lh * len(lines) + 30; need = int(10 + (len(lines) - 1) * lh + asc + desc + 10)  # R9: never clip descenders; placement still uses the old height so nothing moves
        im = Image.new('RGBA', (int(wmax) + 40, max(oh, need)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        for i, l in enumerate(lines):
            ox = (wmax - ft.getlength(l)) / 2 if anchor == 'c' else 0
            d.text((20 + ox, 10 + i * lh), l, font=ft, fill=color + (255,), stroke_width=(max(2, size // 50) if kind == 'num' else 0), stroke_fill=color + (255,))
        if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
        px = x - im.width / 2 if anchor == 'c' else x - 20
        return im, px, y - (im.height if rot else oh) / 2
    return It(t0, f, mode)

def rect(x, y, w, h, fill, t0=0, ow=8, seed=1, amp=3.0, dash=False, mode='pop'):
    def f(_):
        im = layer(w + 60, h + 60); d = ImageDraw.Draw(im); pts = [(30, 30), (30 + w, 30), (30 + w, 30 + h), (30, 30 + h), (30, 30)]
        p = wob(pts, amp, seed, 14); p[-1] = p[0]; pp = [(a * S2, b * S2) for a, b in p]
        if fill is not None: d.polygon(pp, fill=fill + (255,))
        d.line(pp, fill=INK + (255,), width=ow * S2, joint='curve')
        return done(im), x - 30, y - 30
    return It(t0, f, mode)

def stroke_item(pts, t0, col=RED, w=10, dur=0.3, steps=5, seed=3, amp=3.0):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; x0, y0 = min(xs) - 30, min(ys) - 30
    def f(p):
        im = layer(max(xs) - min(xs) + 60, max(ys) - min(ys) + 60); d = ImageDraw.Draw(im)
        poly(d, partial(pts, p), w, col, seed, amp, ox=-x0, oy=-y0)
        return done(im), x0, y0
    return It(t0, f, 'draw', dur, steps)

def ellipse_pts(cx, cy, rx, ry, a0=-110, sweep=380):
    return [(cx + rx * math.cos(math.radians(a0 + sweep * i / 40)), cy + ry * math.sin(math.radians(a0 + sweep * i / 40))) for i in range(41)]
def circ(cx, cy, rx, ry, t0, col=RED, w=10): return stroke_item(ellipse_pts(cx, cy, rx, ry), t0, col, w, 0.3, 5)
def numcirc(s, x, y, size, t0): return circ(x, y + 0.07 * size, font('num', size).getlength(s) / 2 * 1.22 + 14, size * 0.68, t0)
def arrow(x0, y0, x1, y1, t0, col=RED, w=10):
    a = math.atan2(y1 - y0, x1 - x0); L = 34; h1 = (x1 - L * math.cos(a - 0.5), y1 - L * math.sin(a - 0.5)); h2 = (x1 - L * math.cos(a + 0.5), y1 - L * math.sin(a + 0.5))
    return stroke_item([(x0, y0), (x1, y1), h1, (x1, y1), h2], t0, col, w, 0.3, 5)
def bracket(x0, x1, y, t0, col=INK, w=8, up=True):
    d = -26 if up else 26; return stroke_item([(x0, y + d), (x0, y), (x1, y), (x1, y + d)], t0, col, w, 0.35, 5)

def dyn(t0, fn): return It(t0, fn, 'dyn')
def host(states, x, feet, s, t0=0):
    """states: [(t, pose, head)] stepped swaps; x = neck x, feet = sole y"""
    def f(tq):
        cur = [st for st in states if st[0] <= tq] or [states[0]]; _, pose, head = cur[-1]
        im, nx, ny = host_img(pose, head, s); neck_y = feet - 1165 * s
        return im, x - nx, neck_y - ny
    return dyn(t0, f)

def bg_img(path, t0=0):
    im = Image.open(path).convert('RGBA'); return It(t0, lambda _: (im, 0, 0), 'static')

def source(lines, t0, left=True, y=None):
    ys = y or (H - 24 - 56 * len(lines)); its = []
    for i, ln in enumerate(lines):
        ft = font('plain', 44); w = ft.getlength(ln)
        x = 64 if left else 700
        its.append(txt(ln, x, ys + i * 56 + 24, 44, GREYT, t0, 'plain', 'l', mode='static'))
    return its

# ---------------- beats ----------------
class Beat:
    def __init__(s, a, b, desc, nar): s.a, s.b, s.desc, s.nar, s.items = a, b, desc, nar, []
    def add(s, *its): s.items.extend(its); return s
BEATS = []
def B(a, b, desc, nar): bt = Beat(a, b, desc, nar); BEATS.append(bt); return bt

BLS_SRC = ['Source: BLS, CPI release Oct 14, 2026, Table 1']
ZIL_SRC = ['Source: Zillow Group release Oct 6, 2026 (typical U.S. rent)']
CX = (980, 1600); BASE = 760; KPP = 120; BWID = 240
def bar(i, v, col, t0, ow=8): h = int(v * KPP); return rect(CX[i] - BWID // 2, BASE - h, BWID, h, col, t0, ow, seed=11 + i, mode='static')
def numtxt(i, v, col, t0): return txt('%.1f%%' % v, CX[i], BASE - int(v * KPP) - 95, 140, col, t0, 'num')
def axis(t0): return stroke_item([(800, BASE + 4), (1790, BASE + 4)], t0, INK, 9, 0.25, 4, 5, 2)

def build():
    PRE = -1.0
    # 1 hook 0-3.1
    b = B(0.0, 3.1, 'Hero host on white; title pops', 'In the year to September, the official U.S. rent index')
    b.add(host([(0, 'down', 'neutral')], 470, 1010, 0.46),
          txt('Rent inflation', 1330, 330, 130, INK, 0.5, 'wide'), txt('12 months to September 2026', 1330, 480, 66, GREYT, 0.9))
    # 2 BLS bar 3.1-5.4
    b = B(3.1, 5.4, 'BLS bar 2.8% + red circle', 'rent index rose 2.8%')
    b.add(host([(3.1, 'point', 'neutral')], 330, 1010, 0.34), txt('12-month change in rent', 1300, 150, 64, GREYT, 3.2), axis(3.3),
          txt('Official rent\nindex (BLS)', CX[0], 845, 64, INK, 3.4), bar(0, 2.8, OLIVE, 3.9), numtxt(0, 2.8, OLIVE, 4.3), numcirc('2.8%', CX[0], BASE - int(2.8 * KPP) - 95, 140, 4.8),
          *source(BLS_SRC, 3.4, False))
    # 3 Zillow house 5.4-8.1
    b = B(5.4, 8.1, 'Zillow named: house icon + label', "Zillow's own measure of typical market rent")
    def house(_):
        im = layer(520, 480); d = ImageDraw.Draw(im)
        poly(d, [(40, 220), (260, 40), (480, 220)], 12, INK, 4, 3, ox=0, oy=0); poly(d, [(80, 210), (80, 440), (440, 440), (440, 210)], 12, INK, 5, 3)
        d.polygon([(80 * S2, 215 * S2), (80 * S2, 440 * S2), (440 * S2, 440 * S2), (440 * S2, 215 * S2), (260 * S2, 70 * S2)], fill=BLUE + (255,))
        poly(d, [(40, 220), (260, 40), (480, 220)], 12, INK, 4, 3); poly(d, [(80, 215), (80, 440), (440, 440), (440, 215)], 12, INK, 5, 3)
        d.rectangle([220 * S2, 300 * S2, 300 * S2, 440 * S2], fill=PAPER + (255,)); poly(d, [(220, 440), (220, 300), (300, 300), (300, 440)], 9, INK, 6, 2)
        return done(im), 1000, 330
    b.add(txt('Zillow', 1260, 250, 150, BLUE, 5.5, 'wide'), It(5.7, house), txt('typical market rent', 1260, 880, 72, INK, 7.3))
    # 4 same 12 months 8.1-12.0
    b = B(8.1, 12.0, 'Both bars; Zillow pops; "same 12 months" bracket', "rose 2.7% over the same 12 months")
    b.add(axis(PRE), txt('Official rent\nindex (BLS)', CX[0], 845, 64, INK, PRE), bar(0, 2.8, OLIVE, PRE), numtxt(0, 2.8, OLIVE, PRE),
          txt('Zillow\ntypical rent', CX[1], 845, 64, INK, 8.15), bar(1, 2.7, BLUE, 8.2), numtxt(1, 2.7, BLUE, 8.5),
          txt('the same 12 months', 1290, 140, 74, INK, 9.8), bracket(CX[0] - 120, CX[1] + 120, 205, 10.1, INK, 8, False),
          *source(['Source: BLS, CPI release Oct 14, 2026, Table 1', 'Source: Zillow Group, Oct 6, 2026 (typical U.S. rent)'], 8.2, True))
    # 5 two measures, two sources 12.0-14.3
    b = B(12.0, 14.3, 'Hero host (shrug/smirk); two stacked hand labels', 'Two different measures, from two different sources')
    b.add(host([(12.0, 'shrug', 'neutral'), (13.7, 'shrug', 'smirk')], 470, 1010, 0.46), txt('Two measures', 1330, 360, 130, INK, 12.1, 'wide'), txt('Two sources', 1330, 560, 130, INK, 12.85, 'wide'))
    # 6 almost the same 14.3-16.5
    b = B(14.3, 16.5, 'Both bars + big approx sign', 'almost the same answer')
    b.add(host([(14.3, 'point', 'smirk')], 330, 1010, 0.34), axis(PRE), txt('Official rent\nindex (BLS)', CX[0], 845, 64, INK, PRE), bar(0, 2.8, OLIVE, PRE), numtxt(0, 2.8, OLIVE, PRE),
          txt('Zillow\ntypical rent', CX[1], 845, 64, INK, PRE), bar(1, 2.7, BLUE, PRE), numtxt(1, 2.7, BLUE, PRE),
          stroke_item([(1230 + i * 12, 430 + 14 * math.sin(i * 0.9)) for i in range(14)], 14.35, RED, 10, 0.2, 4, 7, 0), stroke_item([(1230 + i * 12, 485 + 14 * math.sin(i * 0.9)) for i in range(14)], 14.55, RED, 10, 0.2, 4, 8, 0), txt('almost the\nsame answer', 1290, 620, 60, RED, 15.0), *source(['Source: BLS, CPI release Oct 14, 2026, Table 1', 'Source: Zillow Group, Oct 6, 2026 (typical U.S. rent)'], PRE, False))
    # 7 both say about 3% 16.5-17.9
    b = B(16.5, 17.9, 'Hero host shrug; "about 3%"', 'So if both say about 3%,')
    b.add(host([(16.5, 'shrug', 'neutral')], 470, 1010, 0.46), txt('Both say', 1330, 330, 100, INK, 16.55), txt('about 3%', 1330, 530, 190, OLIVE, 16.95, 'num'), *source(['Source: BLS, CPI release Oct 14, 2026, Table 1', 'Source: Zillow Group, Oct 6, 2026 (typical U.S. rent)'], PRE, False))
    # 8 room: why feel bigger 17.9-22.5
    b = B(17.9, 22.5, 'ROOM plate beat: worried host, rent bill, red ?', 'why does rent feel like a bigger number than that?')
    room = HERE + '/v1_assets/approved/v1_bg_room@b5094b60.png'
    def bill(_):
        im = layer(380, 480); d = ImageDraw.Draw(im); pts = [(25, 25), (355, 25), (355, 455), (25, 455), (25, 25)]; p = wob(pts, 3, 21, 12); p[-1] = p[0]
        pp = [(a * S2, b_ * S2) for a, b_ in p]; d.polygon(pp, fill=PAPER + (255,)); d.line(pp, fill=INK + (255,), width=8 * S2, joint='curve')
        d.text((60 * S2, 55 * S2), 'RENT', font=font('wide', 90 * S2), fill=INK + (255,))
        for i in range(5): poly(d, [(60, 210 + i * 45), (320 - (i % 2) * 70, 210 + i * 45)], 6, GREYT, 30 + i, 1.5)
        return done(im).rotate(-6, resample=Image.BICUBIC, expand=True), 1250, 400
    b.add(bg_img(room, PRE), host([(17.9, 'down', 'worried')], 560, 985, 0.5),
          rect(760, 50, 1060, 150, PAPER, 17.9, 8, 41), txt('Why does rent feel bigger?', 1290, 125, 84, INK, 18.0), It(19.2, bill), txt('?', 1560, 380, 260, RED, 20.4, 'wide'))
    # 9 different question 22.5-25.0
    b = B(22.5, 25.0, 'Host point; "They answer a DIFFERENT question"', 'Because they are answering a different question')
    b.add(host([(22.5, 'point', 'smirk')], 330, 1010, 0.34), txt('They answer', 1290, 290, 100, INK, 22.7), txt('a DIFFERENT', 1290, 470, 140, RED, 23.7, 'wide'), txt('question', 1290, 650, 120, INK, 24.5))
    # 10 the one you are asking 25.0-27.5
    b = B(25.0, 27.5, 'Host point/smile; "than the one YOU are asking" + red circle', 'from the one you are asking')
    b.add(host([(25.0, 'point', 'smile')], 330, 1010, 0.34), txt('the one', 1290, 290, 100, INK, 25.1), txt('YOU', 1290, 480, 200, RED, 25.5, 'wide'), txt('are asking', 1290, 680, 100, INK, 25.9), circ(1290, 480, 220, 110, 26.4))
    # 11 what a rent number measures 27.5-30.4
    b = B(27.5, 30.4, 'Text + ruler icon', 'This video is about what a rent number actually measures,')
    def ruler(_):
        im = layer(760, 160); d = ImageDraw.Draw(im); pts = [(20, 20), (740, 20), (740, 140), (20, 140), (20, 20)]; p = wob(pts, 3, 51, 14); p[-1] = p[0]; pp = [(a * S2, b_ * S2) for a, b_ in p]
        d.polygon(pp, fill=(250, 220, 120, 255)); d.line(pp, fill=INK + (255,), width=8 * S2, joint='curve')
        for i in range(1, 18): poly(d, [(20 + i * 40, 20), (20 + i * 40, 60 if i % 2 else 85)], 6, INK, 60 + i, 1.0)
        return done(im), 890, 640
    b.add(host([(27.5, 'down', 'neutral')], 330, 1010, 0.34), txt('This video:', 1260, 200, 64, GREYT, 27.55), txt('What a rent number', 1260, 360, 110, INK, 28.3), txt('MEASURES', 1260, 500, 120, RED, 29.8, 'wide'), It(29.85, ruler))
    # 12 leaves out 30.4-32.9
    b = B(30.4, 32.9, 'Dashed empty box with ?; "what it leaves out"', 'and what it leaves out.')
    def dashed(_):
        im = layer(600, 420); d = ImageDraw.Draw(im)
        for (x0, y0, x1, y1) in [(30, 30, 570, 30), (570, 30, 570, 390), (570, 390, 30, 390), (30, 390, 30, 30)]:
            L = math.dist((x0, y0), (x1, y1)); n = int(L / 40)
            for i in range(0, n, 2): poly(d, [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n), (x0 + (x1 - x0) * (i + 1) / n, y0 + (y1 - y0) * (i + 1) / n)], 9, INK, 70 + i, 1.2, 2)
        return done(im), 960, 330
    b.add(host([(30.4, 'shrug', 'smirk'), (31.5, 'shrug', 'worried')], 330, 1010, 0.34), txt('and what', 1260, 190, 90, INK, 30.5), txt('it leaves out', 1260, 280, 90, RED, 31.1), It(31.3, dashed), txt('?', 1260, 520, 260, RED, 31.5, 'wide'))
    # 13a every month BLS 32.9-35.5
    b = B(32.9, 35.5, 'Calendar icon + BLS name', 'Every month, the Bureau of Labor Statistics')
    def cal(_):
        im = layer(520, 480); d = ImageDraw.Draw(im); pts = [(30, 50), (490, 50), (490, 450), (30, 450), (30, 50)]; p = wob(pts, 3, 81, 14); p[-1] = p[0]; pp = [(a * S2, b_ * S2) for a, b_ in p]
        d.polygon(pp, fill=PAPER + (255,)); d.rectangle([30 * S2, 50 * S2, 490 * S2, 130 * S2], fill=RED + (255,)); d.line(pp, fill=INK + (255,), width=8 * S2, joint='curve')
        for r in range(3):
            for c in range(4): d.rounded_rectangle([(65 + c * 105) * S2, (160 + r * 95) * S2, (130 + c * 105) * S2, (225 + r * 95) * S2], radius=10 * S2, outline=INK + (255,), width=5 * S2)
        return done(im), 940, 300
    b.add(host([(32.9, 'point', 'neutral')], 330, 1010, 0.34), txt('Every month', 1200, 200, 110, INK, 33.0), It(33.15, cal), txt('Bureau of Labor Statistics (BLS)', 1250, 880, 70, INK, 33.7))
    # 13b CPI 35.5-38.0
    b = B(35.5, 38.0, 'Document icon "CPI" + name + source', 'publishes the Consumer Price Index.')
    def doc(_):
        im = layer(400, 520); d = ImageDraw.Draw(im); pts = [(30, 30), (370, 30), (370, 490), (30, 490), (30, 30)]; p = wob(pts, 3, 91, 14); p[-1] = p[0]; pp = [(a * S2, b_ * S2) for a, b_ in p]
        d.polygon(pp, fill=PAPER + (255,)); d.line(pp, fill=INK + (255,), width=8 * S2, joint='curve')
        d.text((70 * S2, 70 * S2), 'CPI', font=font('wide', 130 * S2), fill=OLIVE + (255,))
        for i in range(6): poly(d, [(70, 260 + i * 36), (330 - (i % 3) * 50, 260 + i * 36)], 6, GREYT, 95 + i, 1.5)
        return done(im), 640, 250
    b.add(It(35.6, doc), txt('Consumer\nPrice Index', 1380, 380, 120, INK, 35.7, 'wide'), txt('(CPI)', 1380, 600, 100, OLIVE, 36.8, 'wide'), *source(['Source: BLS, CPI release Oct 14, 2026'], 36.7))
    # 14 one piece 38.0-39.9
    b = B(38.0, 39.9, 'CPI document with a "Rent" tag pulled out (no sizes implied)', 'Rent is one piece of it.')
    b.add(It(PRE, doc), rect(1230, 395, 360, 150, ORANGE, 38.1, 8, 120), txt('Rent', 1410, 470, 100, INK, 38.2, 'wide'), arrow(1215, 470, 1090, 470, 38.6), txt('one piece of it', 1400, 680, 100, INK, 38.3))
    # 15 look at weights 39.9-41.3
    b = B(39.9, 41.3, 'Hero host smile; "The weights"', 'Look at the weights.')
    b.add(host([(39.9, 'down', 'smile')], 470, 1010, 0.46), txt('Look at the', 1330, 380, 100, INK, 40.0), txt('WEIGHTS', 1330, 540, 160, RED, 40.3, 'wide'))
    # weights chart
    BX, BW_, BY, BH = 360, 1200, 430, 140
    pct = lambda p: BW_ * p / 100.0; rent, oer, shel = 7.728, 25.902, 35.323; oth = shel - rent - oer
    wsrc = ['Source: BLS, CPI release Oct 14, 2026, Table 1', 'Relative importance, August 2026 weights']
    def wbase(t_whole, pre=False):
        t = PRE if pre else t_whole
        return [txt('What the CPI is made of', 960, 150, 84, INK, PRE if pre else 41.3), txt('(relative importance, August 2026)', 960, 245, 54, GREYT, PRE if pre else 41.5),
                rect(BX, BY, BW_, BH, GREYF, t, 8, 131), *source(wsrc, PRE if pre else 41.4)]
    b = B(41.3, 44.3, 'Whole-CPI bar (grey) + title', 'In the August 2026 weights, the item called')
    b.add(*wbase(41.8), txt('whole CPI = 100%', 960, 700, 70, INK, 43.0))
    b = B(44.3, 49.3, 'Rent segment + 7.7% + circle', 'Rent of Primary Residence is 7.7% of the whole index')
    b.add(*wbase(0, True), rect(BX, BY, pct(rent), BH, ORANGE, 44.4, 8, 132), txt('Rent of primary residence', BX + 360, 360, 56, INK, 44.9), arrow(BX + 140, 395, BX + 70, 425, 45.7), txt('7.7%', BX + 90, 700, 160, ORANGE, 46.4, 'num'), numcirc('7.7%', BX + 90, 700, 160, 47.3))
    ox0 = BX + pct(rent)
    b = B(49.3, 52.5, "Owners' equivalent rent segment + label", "Owner's equivalent rent, the rent a homeowner would pay")
    b.add(*wbase(0, True), rect(BX, BY, pct(rent), BH, ORANGE, PRE, 8, 132), rect(ox0, BY, pct(oer), BH, OLIVE, 49.4, 8, 133),
          txt("Owners' equivalent rent", ox0 + pct(oer) / 2 + 160, 355, 56, INK, 49.6), txt('what a homeowner would pay\nto rent their own home', 960, 760, 58, GREYT, 50.4))
    b = B(52.5, 55.8, '25.9% number + circle', 'for their own home, is another 25.9%.')
    b.add(*wbase(0, True), rect(BX, BY, pct(rent), BH, ORANGE, PRE, 8, 132), rect(ox0, BY, pct(oer), BH, OLIVE, PRE, 8, 133),
          txt("Owners' equivalent rent", ox0 + pct(oer) / 2 + 160, 355, 56, INK, PRE), txt('25.9%', ox0 + pct(oer) / 2, 700, 160, OLIVE, 53.4, 'num'), numcirc('25.9%', ox0 + pct(oer) / 2, 700, 160, 54.3))
    sx0 = ox0 + pct(oer)
    def wseg(): return [rect(BX, BY, pct(rent), BH, ORANGE, PRE, 8, 132), rect(ox0, BY, pct(oer), BH, OLIVE, PRE, 8, 133)]
    b = B(55.8, 59.4, 'Light sliver = a few smaller items', 'Together, with a few smaller items, the BLS group called')
    b.add(*wbase(0, True), *wseg(), rect(sx0, BY, pct(oth), BH, OLIVE_L, 56.9, 6, 134), txt('a few smaller items', 1000, 360, 56, INK, 57.0), arrow(900, 395, sx0 + 12, 430, 57.6),
          txt('(about 1.7%, derived: 35.3 minus 7.7 minus 25.9)', 960, 760, 50, GREYT, 58.0))
    b = B(59.4, 63.7, 'Shelter bracket + 35.3% + circle', 'Shelter is 35.3% of the entire CPI.')
    sw = pct(shel)
    b.add(*wbase(0, True), *wseg(), rect(sx0, BY, pct(oth), BH, OLIVE_L, PRE, 6, 134), bracket(BX, BX + sw, 610, 59.5, INK, 9, True),
          txt('Shelter', BX + sw / 2, 668, 100, INK, 59.6, 'wide'), txt('35.3%', BX + sw / 2, 795, 150, INK, 60.3, 'num'), numcirc('35.3%', BX + sw / 2, 795, 150, 61.3), txt('of the entire CPI', BX + sw + 470, 795, 64, INK, 61.7))
    # 21 not a side detail 63.7-66.5
    b = B(63.7, 66.5, 'Hero host shrug/surprised; "Not a side detail"', 'So, the rent number is not a side detail.')
    b.add(host([(63.7, 'shrug', 'surprised')], 470, 1010, 0.46), txt('Not a', 1330, 340, 130, INK, 64.5), txt('side detail', 1330, 520, 150, RED, 64.8, 'wide'))
    # 22 a third 66.5-70.3
    b = B(66.5, 70.3, 'Pie with ~1/3 wedge; "about 1/3 of the index = housing"', 'About a third of the inflation figure that reaches the news is housing.')
    cx, cy, R = 640, 560, 270
    def pie(p):
        im = layer(2 * R + 80, 2 * R + 80); d = ImageDraw.Draw(im); box = [40 * S2, 40 * S2, (40 + 2 * R) * S2, (40 + 2 * R) * S2]
        d.ellipse(box, fill=GREYF + (255,)); sweep = 360 * shel / 100.0 * p
        if sweep > 1: d.pieslice(box, -90, -90 + sweep, fill=ORANGE + (255,))
        d.ellipse(box, outline=INK + (255,), width=10 * S2)
        if sweep > 1:
            for a in (-90, -90 + sweep): d.line([(40 + R) * S2, (40 + R) * S2, (40 + R + R * math.cos(math.radians(a))) * S2, (40 + R + R * math.sin(math.radians(a))) * S2], fill=INK + (255,), width=8 * S2)
        return done(im), cx - R - 40, cy - R - 40
    b.add(It(66.7, pie, 'draw', 1.0, 6), txt('about 1/3', 1380, 360, 190, INK, 66.8, 'wide'), txt('of the inflation index', 1380, 520, 80, INK, 67.9), txt('= housing', 1380, 690, 130, RED, 69.0, 'wide'),
          *source(['Source: BLS, CPI release Oct 14, 2026, Table 1', 'Shelter 35.3% of the CPI (Aug 2026 weights)'], 66.9))
    # 23-24 slow
    b = B(70.3, 72.4, 'Host point/smirk; "rent moves slowly" + slow line', 'When the rent measure moves slowly,')
    b.add(host([(70.3, 'point', 'smirk')], 330, 1010, 0.34), txt('When rent moves', 1290, 300, 100, INK, 70.4), txt('slowly', 1290, 460, 170, RED, 71.2, 'wide'))
    b = B(72.4, 75.0, 'Host smile; "headline inflation moves slowly too"', 'headline inflation moves slowly with it.')
    b.add(host([(72.4, 'down', 'smile')], 470, 1010, 0.46), txt('Headline inflation', 1330, 330, 100, INK, 72.5), txt('moves slowly too', 1330, 490, 120, RED, 73.1, 'wide'))
    return BEATS

def beat_at(beats, tq):
    for b in beats:
        if b.a <= tq + 1e-6 < b.b: return b
    return beats[-1]

def render(beats, tq):
    cv = Image.new('RGB', (W, H), BG); b = beat_at(beats, tq)
    for it in b.items: paste_pop(cv, it, tq)
    return cv

def storyboard(beats):
    L = ['# V1 Rent R4 storyboard (long-form grammar re-block of the 0-75 s Take 2 narration)', '',
         'Generated by `tools/v1r4_render.py --storyboard`. Narration, timings, figures and sources unchanged from R3 (`SEGMENT_0_75_CLAIM_REGISTER.md`). White canvas default; room plate in 1 beat; hard cut between all beats; objects pop at the word; no idle bob; no rolling counters.', '',
         '| # | Time (s) | Dur | Narration (Take 2) | Visual |', '|---|---|---|---|---|']
    for i, b in enumerate(beats, 1): L.append('| %d | %.1f-%.1f | %.1f | %s | %s |' % (i, b.a, b.b, b.b - b.a, b.nar, b.desc))
    d = [b.b - b.a for b in beats]; L += ['', 'Beats: %d; mean %.2f s, median %.2f s, min %.1f, max %.1f. Hard cuts at beat boundaries: %d.' % (len(beats), sum(d) / len(d), sorted(d)[len(d) // 2], min(d), max(d), len(beats) - 1)]
    return '\n'.join(L)

def main():
    a = sys.argv; dur = float(a[a.index('--dur') + 1]) if '--dur' in a else 75.0
    beats = build()
    if '--storyboard' in a: open(HERE + '/STORYBOARD_R4_75s.md', 'w').write(storyboard(beats) + '\n'); print('storyboard written'); return
    od = os.environ.get('R_STILLS', HERE + '/out_r4'); os.makedirs(od + '/stills', exist_ok=True)
    if '--still' in a:
        for ts in a[a.index('--still') + 1].split(','): render(beats, math.floor(float(ts) * CFPS + 1e-6) / CFPS).save('%s/stills/r4_%s.png' % (od, ts));
        return
    out = a[a.index('--out') + 1] if '--out' in a else od + '/V1_RENT_R4.mp4'
    out = out if os.path.isabs(out) else HERE + '/' + out
    assert hashlib.sha256(open(WAV, 'rb').read()).hexdigest() == WAV_SHA, 'audio checksum mismatch'
    n = round(dur * FPS)
    cmd = ['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', str(FPS), '-i', '-', '-t', '%.3f' % (n / FPS), '-i', WAV,
           '-map', '0:v', '-map', '1:a', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
           '-af', 'aresample=48000,afade=t=out:st=%.3f:d=0.3' % max(0, n / FPS - 0.3), '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); last = None
    for f in range(n):
        tq = math.floor(f / FPS * CFPS + 1e-6) / CFPS
        if tq != last: im = render(beats, tq).tobytes(); last = tq
        p.stdin.write(im)
    p.stdin.close(); p.wait(); print('rendered', n, 'frames ->', out)

if __name__ == '__main__': main()
