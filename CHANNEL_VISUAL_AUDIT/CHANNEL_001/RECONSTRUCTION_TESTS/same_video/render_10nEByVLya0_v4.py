"""Same-video visual reconstruction of CasuallyFinance 10nEByVLya0 (frames 0-1659, 1080x1920, 30 fps).
All art is drawn here with PIL primitives (original). No source pixels are read. Third-party items in the
reference (photos, memes, screenshots) are replaced by labelled original stand-ins.
Timing source: visual_states.csv (state boundaries) + ASR word times (captions). Usage: render_10nEByVLya0.py OUT.mp4 [max_frame]
"""
import csv, json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SS = 1080, 1920, 30, 2
Y0, Y1 = 640, 1300                      # content band in frame coords (drawn at SS x)
BG = (253, 253, 253)
WS = os.path.expanduser('~/YIOS-local-audits/2026-11-08-10nEByVLya0-deep-ct-scan/')
ST = {r['visual_state_id']: (int(r['start_frame']), int(r['end_frame'])) for r in csv.DictReader(open(WS + 'visual_states.csv'))}
FD = '/System/Library/Fonts/Supplemental/'
CAPF = ImageFont.truetype(FD + 'Comic Sans MS Bold.ttf', 58)
def hand(sz): return ImageFont.truetype(FD + 'ChalkboardSE.ttc', sz, index=0)
def comic(sz): return ImageFont.truetype(FD + 'Comic Sans MS Bold.ttf', sz)
BLK, RED, GRN, TEAL = (14, 14, 14), (200, 40, 45), (88, 108, 52), (122, 184, 191)

# ---------- captions from ASR words ----------
words = []
for s in json.load(open(WS + 'audio/10nEByVLya0_small_en.json'))['segments']:
    for w in s['words']: words.append((w['word'].strip(), w['start']))
chunks, cur = [], []
for i, (t, s) in enumerate(words):
    if cur and (s - cur[-1][1] > 0.22 or len(cur) >= 5): chunks.append(cur); cur = []
    cur.append((t, s))
chunks.append(cur)
EV = [int(r['start_frame']) for r in csv.DictReader(open(WS + 'caption_event_ledger.csv'))]
WS_ = [x[1] for x in words]
_d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
def caption(f):
    ev = [e for e in EV if e <= f]
    if not ev: return None
    t = ev[-1] / FPS + 0.04
    idx = max([i for i, w in enumerate(WS_) if w <= t] or [-1])
    if idx < 0: return None
    # v4 chunk rule (read from 16 ref frames): chunk starts after a punctuation-ended word; max 2 lines at 800 px, then new chunk
    j = idx
    while j > 0 and not words[j - 1][0][-1] in ',.?!' and chunk_lines(j - 1, idx) <= 2: j -= 1
    if f / FPS > WS_[idx] + 0.9: return None
    e = idx
    while e + 1 < len(WS_) and not words[e][0][-1] in ',.?!' and chunk_lines(j, e + 1) <= 2: e += 1
    return [words[k][0] for k in range(j, idx + 1)], [words[k][0] for k in range(j, e + 1)]
def chunk_lines(a, b):
    n, cur = 1, []
    for k in range(a, b + 1):
        if _d.textlength(' '.join(cur + [words[k][0]]), font=CAPF) > 800 and cur: n += 1; cur = [words[k][0]]
        else: cur.append(words[k][0])
    return n
def caption_old(f):
    t = f / FPS
    for c in chunks:
        nxt = c[-1][1] + 0.5
        if c[0][1] <= t < nxt:
            shown = [w for w, s in c if s <= t]
            return ' '.join(shown) if shown else None
    return None

# ---------- helpers (coordinates are frame px; d draws at SS x on the band) ----------
class Cv:
    def __init__(s):
        s.im = Image.new('RGB', (W * SS, (Y1 - Y0) * SS), BG); s.d = ImageDraw.Draw(s.im)
    def p(s, x, y): return (x * SS, (y - Y0) * SS)
    def line(s, pts, w, col=BLK): s.d.line([s.p(*q) for q in pts], fill=col, width=int(w * SS), joint='curve')
    def ell(s, cx, cy, rx, ry, fill=None, outline=BLK, w=8):
        a = s.p(cx - rx, cy - ry); b = s.p(cx + rx, cy + ry); s.d.ellipse([a, b], fill=fill, outline=outline, width=int(w * SS) if outline else 0)
    def rect(s, x0, y0, x1, y1, fill=None, outline=None, w=6, r=0):
        a = s.p(x0, y0); b = s.p(x1, y1)
        if r: s.d.rounded_rectangle([a, b], radius=r * SS, fill=fill, outline=outline, width=int(w * SS))
        else: s.d.rectangle([a, b], fill=fill, outline=outline, width=int(w * SS))
    def poly(s, pts, fill=None, outline=None, w=4): s.d.polygon([s.p(*q) for q in pts], fill=fill, outline=outline)
    def text(s, x, y, t, font, fill=BLK, anchor='mm'):
        f = font.font_variant(size=font.size * SS); s.d.text(s.p(x, y), t, font=f, fill=fill, anchor=anchor)
    def out(s): return s.im.resize((W, Y1 - Y0), Image.LANCZOS)

def ease(k): k = max(0., min(1., k)); return 1 - (1 - k) ** 3
def prog(f, a, n): return ease((f - a) / n)

def qmark(c, x, y, r=105):
    c.ell(x, y, r, r, fill=BLK, outline=None); c.text(x, y + 4, '?', comic(int(r * 1.35)), (255, 255, 255))
def chart(c, x, y, w=220):
    h = w * .78; c.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2, fill=(236, 246, 250), outline=BLK, w=5)
    for col, ys in (((200, 40, 45), (.1, -.1, .2, -.25, .05)), ((60, 150, 80), (-.2, .15, -.05, .2, -.15)), ((60, 90, 200), (.15, -.2, .1, -.1, .2))):
        c.line([(x - w * .4 + i * w * .2, y + ys[i] * h * .8) for i in range(5)], 4, col)
def bag(c, x, y, s=1.0):
    c.ell(x, y + 18 * s, 38 * s, 36 * s, fill=GRN, outline=BLK, w=5); c.poly([(x - 20 * s, y - 12 * s), (x + 20 * s, y - 12 * s), (x + 10 * s, y - 28 * s), (x - 10 * s, y - 28 * s)], fill=GRN)
    c.line([(x - 22 * s, y - 14 * s), (x + 22 * s, y - 14 * s)], 5); c.text(x, y + 20 * s, '$', comic(int(36 * s)), (230, 240, 200))
def stick(c, x, ytop=870, face='neutral', arms='shrug', lean=0, sweat=False):
    hx, hy = x + lean * .4, ytop + 110
    c.line([(hx + 8, hy + 78), (x + 12 + lean, ytop + 395)], 12)
    ay = ytop + 300
    if arms == 'shrug':
        c.line([(x - 140 + lean, ay - 25), (x - 55, ay + 10), (x - 25 + lean * .5, ay + 40), (x + 5, ay - 30)], 11)
        c.line([(x + 15, ay - 10), (x + 70, ay + 45), (x + 110, ay - 10), (x + 125, ay - 70)], 11)
    elif arms == 'down':
        c.line([(x + 5, ay - 20), (x - 60, ay + 60), (x - 120, ay + 110)], 11); c.line([(x + 15, ay - 20), (x + 70, ay + 60), (x + 120, ay + 110)], 11)
    else:
        c.line([(x + 5, ay - 20), (x - 50, ay - 90), (x - 90, ay - 150)], 11); c.line([(x + 15, ay - 20), (x + 70, ay + 40), (x + 40, ay + 90)], 11)
    c.ell(hx, hy, 78, 76, fill=(211, 173, 130), outline=BLK, w=9)
    c.poly([(hx - 88, hy - 20), (hx - 80, hy - 85), (hx - 20, hy - 110), (hx + 50, hy - 95), (hx + 85, hy - 55), (hx + 75, hy - 30), (hx + 40, hy - 60), (hx - 20, hy - 45), (hx - 50, hy - 5)], fill=(108, 74, 50), outline=BLK)
    ey = hy - 5; c.ell(hx - 25, ey, 5, 6, fill=BLK, outline=None); c.ell(hx + 22, ey, 5, 6, fill=BLK, outline=None)
    if face == 'worried': c.line([(hx - 25, hy + 35), (hx, hy + 28), (hx + 25, hy + 36)], 5); c.line([(hx - 38, ey - 18), (hx - 12, ey - 26)], 4)
    elif face == 'happy': c.line([(hx - 25, hy + 28), (hx, hy + 42), (hx + 25, hy + 28)], 5)
    else: c.line([(hx - 20, hy + 30), (hx + 18, hy + 32)], 5)
    if sweat: c.ell(hx + 70, hy - 10, 8, 14, fill=(120, 190, 235), outline=BLK, w=3)
def stick_blk(c, x, face='neutral', arms='hips', ytop=820):
    # v3: geometry measured on ref f525 (head 180x170 egg centre (540,870), body stroke ~5, short legs, thin arms, scribbled hair cap)
    dx = x - 540; dy = ytop - 820
    P = lambda px, py: (px + dx, py + dy)
    c.line([P(535, 950), P(533, 1125)], 5)
    c.line([P(538, 1003), P(490, 1025), P(528, 1048)], 5)
    c.line([P(543, 1005), P(570, 1045), P(610, 1052)], 5)
    c.line([P(533, 1125), P(480, 1177)], 5); c.line([P(533, 1125), P(595, 1178)], 5)
    hx, hy = P(540, 870)
    c.ell(hx, hy, 90, 85, fill=(250, 215, 185), outline=BLK, w=6)
    c.poly([P(463, 800), P(500, 782), P(550, 770), P(600, 775), P(628, 790), P(605, 800), P(560, 795), P(510, 805), P(470, 825)], fill=BLK)
    for ex in (-30, 28): c.ell(hx + ex, hy - 12, 5, 6, fill=BLK, outline=None)
    if face == 'happy': c.line([(hx - 42, hy + 8), (hx - 15, hy + 22), (hx + 30, hy + 20)], 8)
    else: c.line([(hx - 40, hy + 12), (hx - 5, hy + 24), (hx + 28, hy + 22)], 6)
def earth(c, x, y, r=170, burning=False, swirl=False):
    c.ell(x, y, r, r, fill=(40, 90, 170), outline=BLK, w=9)
    c.poly([(x - r * .5, y - r * .3), (x - r * .1, y - r * .6), (x + r * .3, y - r * .2), (x + r * .1, y + r * .3), (x - r * .4, y + r * .2)], fill=(70, 150, 70))
    c.ell(x - r * .3, y - r * .1, r * .2, r * .24, fill=(255, 255, 255), outline=BLK, w=5); c.ell(x + r * .3, y - r * .1, r * .2, r * .24, fill=(255, 255, 255), outline=BLK, w=5)
    if swirl:
        for ex in (x - r * .3, x + r * .3):
            for k in range(3): c.ell(ex, y - r * .1, r * (.16 - .05 * k), r * (.16 - .05 * k), fill=None, outline=BLK, w=3)
    else:
        for ex in (x - r * .3, x + r * .3): c.ell(ex, y - r * .1, r * .06, r * .08, fill=BLK, outline=None)
    if burning:
        for fx, fy, s in ((x - r * .9, y + r * .5, 1), (x + r * .85, y - r * .7, .9), (x - r * .5, y - r * 1.0, .7)):
            c.poly([(fx - 60 * s, fy + 70 * s), (fx - 20 * s, fy - 20 * s), (fx + 5 * s, fy - 90 * s), (fx + 30 * s, fy - 10 * s), (fx + 70 * s, fy + 70 * s)], fill=(240, 130, 30), outline=BLK)
def years(c, f, xs, ys=968, fs=100):
    for x, t in xs: c.text(x, ys, t, hand(fs))
def arrow_l(c, x, y, L=160, col=RED):
    c.line([(x + L / 2, y), (x - L / 2, y)], 16, col); c.line([(x - L / 2 + 38, y - 36), (x - L / 2, y), (x - L / 2 + 38, y + 36)], 16, col)
def calendar(c, x, y):
    c.rect(x - 62, y - 50, x + 62, y + 52, fill=(244, 244, 244), outline=BLK, w=8, r=10); c.rect(x - 58, y - 46, x + 58, y - 14, fill=RED)
    for i in range(3): c.line([(x - 40 + i * 40, y - 62), (x - 40 + i * 40, y - 40)], 6)
    for cx_, cy_ in ((x - 30, y + 8), (x + 22, y + 8), (x - 30, y + 36), (x + 22, y + 36), (x - 4, y + 36)): c.rect(cx_ - 10, cy_ - 10, cx_ + 10, cy_ + 10, fill=RED, outline=BLK, w=3, r=4)
def photo(c, x0, y0, x1, y1, tone=(150, 170, 190), label=None):
    c.rect(x0, y0, x1, y1, fill=tone, outline=None)
    mx = (x0 + x1) / 2; c.ell(mx, y0 + (y1 - y0) * .38, (x1 - x0) * .17, (x1 - x0) * .2, fill=(225, 205, 185), outline=None)
    c.poly([(x0 + (x1 - x0) * .15, y1), (x0 + (x1 - x0) * .25, y0 + (y1 - y0) * .68), (x1 - (x1 - x0) * .25, y0 + (y1 - y0) * .68), (x1 - (x1 - x0) * .15, y1)], fill=(60, 70, 90))
    if label: c.text(mx, y1 + 18, label, comic(22), (90, 90, 90))
def blackstone(c, x, y, w=250, h=96): c.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2, fill=(12, 12, 12)); c.text(x, y, 'ORIG-LOGO', comic(36), (255, 255, 255))
def article(c, x0, y0, x1, y1):
    c.rect(x0, y0, x1, y1, fill=(252, 244, 240), outline=(210, 200, 195), w=2)
    for i in range(9): c.rect(x0 + 24, y0 + 26 + i * 22, x1 - 24 - (60 if i % 4 == 3 else 0), y0 + 34 + i * 22, fill=(170, 165, 165))
def candles(c, x0, y0, x1, y1, f):
    c.rect(x0, y0, x1, y1, fill=(255, 255, 255), outline=(200, 200, 200), w=2)
    import random; r = random.Random(7); v = .55
    for i in range(34):
        v += r.uniform(-.09, .07) + (-.05 if i < 8 else .02)
        xx = x0 + 20 + i * ((x1 - x0 - 40) / 34); yy = y1 - 30 - max(.05, min(.95, v)) * (y1 - y0 - 60); up = r.random() > .45
        c.line([(xx, yy - 14), (xx, yy + 14)], 2, (60, 60, 60)); c.rect(xx - 4, yy - 7, xx + 4, yy + 7, fill=(40, 160, 90) if up else (210, 60, 60))
def skyline(c, x, y):
    for i, (dx, hh) in enumerate(((-90, 150), (-50, 220), (0, 280), (50, 190), (95, 130))): c.rect(x + dx - 22, y - hh, x + dx + 22, y, fill=(150, 160, 175), outline=BLK, w=4)
def speech(c, x, y, w, h, t, tail=(0, 0), fs=34):
    c.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2, fill=(255, 255, 255), outline=BLK, w=6, r=60)
    c.text(x, y, t, comic(fs))

def label_box(c, f, a, text, x, y):
    pass

# ---------- per-frame composition ----------
def S(a): return ST[a]
def scene(c, f):
    g = lambda k: ST[k]
    s2, s3 = g('S002'), g('S003')
    if f < g('S002')[0]: return
    if f <= g('S003')[1]:   # question-mark scroll, chart pops in
        off = (f - s2[0]) * 15.5
        for i in range(-2, 8):
            x = 1250 + i * 272 - off
            if f >= s3[0] and abs(x - 540) < 190: continue
            qmark(c, x, 952)
        if f >= s3[0]:
            k = ease((f - s3[0]) / 3); chart(c, 540, 975, 240 * k + 1)
        return
    if f <= g('S008')[1]:   # chart left, money bag right, small ? circles
        k = ease((f - g('S004')[0]) / 7); chart(c, 540 - 310 * k, 960, 240 - 20 * k); bag(c, 960 if f >= g('S004')[0] + 2 else 540, 1100, 1.1)
        for sid, (x, y, r) in (('S005', (120, 768, 36)), ('S006', (336, 1140, 36)), ('S007', (888, 856, 36))):
            if f >= g(sid)[0]: qmark(c, x, y, int(r * min(1, 1 + 0 * ease((f - g(sid)[0]) / 2))))
        if f >= g('S008')[0]: qmark(c, 540, 1000, int(40 + 110 * ease((f - g('S008')[0]) / 6)))
        return
    if f <= g('S012')[1]:   # dollar sign, bubble inflates and pops
        b0, b1 = g('S010')
        if f < b0: c.text(540, 960, '$', comic(200), (70, 150, 150)); return
        if f < g('S011')[0]:
            r = 20 + 160 * ease((f - b0) / (b1 - b0)); c.ell(540, 960, r, r, fill=TEAL, outline=(90, 150, 160), w=8); c.ell(540 - r * .35, 960 - r * .3, r * .25, r * .4, fill=(200, 235, 240), outline=None); c.text(540, 960, '$', comic(200), (40, 110, 115)); return
        if f <= g('S011')[1]:
            k = (f - g('S011')[0]) / 12
            for a in range(10): ang = a * 36 * math.pi / 180; c.ell(540 + math.cos(ang) * (180 + 120 * k), 960 + math.sin(ang) * (180 + 120 * k), 12 * (1 - k) + 2, 12 * (1 - k) + 2, fill=TEAL, outline=None)
        c.text(540, 960, '$', comic(200), (40, 110, 115)); return
    if f <= g('S016')[1]:   # stick man and Earth
        stick(c, 525, 870, 'neutral', 'shrug')
        if f >= g('S014')[0]:
            k = ease((f - g('S014')[0]) / 14); earth(c, 540 + 640 * (1 - k) + 300, 1030, 130, sweat := False)
            if f >= g('S016')[0]: c.ell(840 + 0, 905, 9, 15, fill=(120, 190, 235), outline=BLK, w=3)
        return
    if f <= g('S019')[1]:   # timeline
        if f < g('S018')[0]:
            off = (f - g('S017')[0]) * 22
            for i, yr in enumerate(('2012', '2011', '2010', '2009', '2008', '2007')):
                x = 440 + 560 * 0 + (i - 5) * 0 + (4 - i) * 560 + 560 - off
                years(c, f, [(x, yr)], fs=100)
                if i < 5: arrow_l(c, x - 280, 968)
        else:
            years(c, f, [(440, '2007'), (1000, '2008')]); arrow_l(c, 720, 968)
            if f >= g('S019')[0]:
                k = ease((f - g('S019')[0]) / 3); calendar(c, 198, 970 + 12 * (1 - k)); c.text(200, 861, 'June', hand(46))
        return
    if f <= g('S021')[1]:   # Wall Street sign + stand-in clips, then "The market:" clip
        if f <= g('S020')[1]:
            k = ease((f - g('S020')[0]) / 6); xo = -300 * (1 - k)
            c.rect(40 + xo, 680, 100 + xo, 1130, fill=(86, 100, 140), outline=BLK, w=6)
            c.rect(110 + xo, 700, 830 + xo, 960, fill=(22, 28, 52), outline=BLK, w=6, r=8); c.text(430 + xo, 835, 'WALL', hand(150), (245, 245, 245)); c.text(740 + xo, 790, 'ST', comic(46), (245, 245, 245))
            if f >= g('S020')[0] + 6: photo(c, 410, 1000, 710, 1208, (120, 130, 160)); c.rect(720, 1000, 1032, 1208, fill=(110, 30, 40))
        else:
            c.text(300, 772, 'The market:', hand(56))
            c.rect(292, 840, 788, 1172, fill=(40, 24, 20)); earth(c, 540, 1020, 0)
            for i, (fx, s_) in enumerate(((380, 1.1), (540, 1.5), (700, 1.1))): c.poly([(fx - 70 * s_, 1172), (fx - 20 * s_, 1020), (fx, 900), (fx + 30 * s_, 1020), (fx + 70 * s_, 1172)], fill=(240, 120, 30))
            c.ell(540, 1100, 60, 70, fill=(190, 40, 40), outline=None)
        return
    if f <= g('S022')[1]: stick_blk(c, 540, 'happy'); return
    if f <= g('S025')[1]:   # Blackstone, founders
        blackstone(c, 540, 700 + 40 if False else 740)
        photo(c, 430, 800, 740, 1100, (140, 160, 185), 'Steven S. (stand-in)')
        if f >= g('S025')[0]: photo(c, 470, 840, 780, 1140, (170, 150, 150), 'Peter P. (stand-in)')
        return
    if f <= g('S026')[1]: stick_blk(c, 540, 'happy'); return
    if f <= g('S027')[1]:   # yacht stand-in with money bags
        c.rect(300, 790, 780, 1060, fill=(150, 190, 215)); c.poly([(420, 1010), (660, 1010), (700, 940), (390, 940)], fill=(245, 245, 245), outline=BLK); c.line([(540, 940), (540, 830)], 5); c.poly([(540, 830), (540, 930), (620, 930)], fill=(245, 245, 245), outline=BLK)
        bag(c, 255, 1010); bag(c, 845, 1010, 1.0); return
    if f <= g('S028')[1]: stick_blk(c, 540, 'neutral'); return
    if f <= g('S033')[1]:   # baby / newborn bubbles
        if f < g('S031')[0]:
            c.rect(0, 740, 1080, 1290, fill=(235, 235, 235)); c.rect(0, 1100, 1080, 1290, fill=(120, 160, 175)); c.rect(700, 760, 1080, 1010, fill=(130, 190, 215))
            c.ell(300, 1040, 70, 70, fill=(160, 110, 70), outline=BLK, w=6); c.ell(300, 1090, 90, 60, fill=(120, 190, 235), outline=BLK, w=6)
            if f >= g('S030')[0]: speech(c, 780, 1000, 340, 190, 'And my baby\nwill be called...', fs=30)
        else:
            c.rect(0, 740, 1080, 1290, fill=(225, 215, 190)); c.ell(380, 1010, 250, 260, fill=(120, 185, 215), outline=BLK, w=10); c.ell(380, 1010, 110, 130, fill=(215, 175, 150), outline=BLK, w=8)
            if f != g('S032')[0]: speech(c, 820, 1010, 330, 180, 'Peter\nPeterson!', fs=34)
        return
    if f <= g('S034')[1]: stick_blk(c, 540, 'neutral'); return
    if f <= g('S039')[1]:   # article with logo, portraits, banknotes
        article(c, 90, 860, 780, 1150)
        if f >= g('S036')[0]: blackstone(c, 840, 835, 210, 80)
        if f >= g('S037')[0]: photo(c, 560, 1090, 700, 1235, (140, 160, 185))
        if f >= g('S038')[0]: photo(c, 720, 1090, 860, 1235, (170, 150, 150))
        if f >= g('S039')[0]:
            c.rect(95, 905, 400, 930, fill=(250, 235, 90))
            for i in range(6): c.rect(250 + i * 80, 640 + ((f - g('S039')[0]) * 14 + i * 90) % 520, 330 + i * 80, 690 + ((f - g('S039')[0]) * 14 + i * 90) % 520, fill=(130, 190, 120), outline=BLK, w=3)
        return
    if f <= g('S042')[1]:
        if f < g('S041')[0]: years(c, f, [(440, '2007'), (1000, '2008')]); arrow_l(c, 720, 968); calendar(c, 198, 970); c.text(200, 861, 'June', hand(46))
        else:
            k = prog(f, g('S041')[0], 20); years(c, f, [(440 + 560 * (1 - k) - 560 * 0, '2007'), (1000, '2008')]); arrow_l(c, 720, 968)
        return
    if f <= g('S043')[1]: earth(c, 540, 1010, 270, burning=True, swirl=True); return
    if f <= g('S046')[1]:   # red tiles accumulate
        n = 1 if f < g('S045')[0] else min(6, 1 + (f - g('S045')[0]) // 3 + 1)
        pos = ((150, 1000), (480, 880), (700, 980), (230, 1150), (560, 1120), (820, 1130))
        for i in range(n):
            x, y = pos[i]; c.rect(x - 150, y - 80, x + 150, y + 80, fill=(150, 25, 35)); c.text(x, y, 'not stonks', comic(32), (230, 230, 230)); c.ell(x - 90, y, 40, 55, fill=(60, 60, 70), outline=None)
        return
    if f <= g('S050')[1]:   # candlestick + red arrow + 90% + worried
        candles(c, 220, 760, 880, 1230, f)
        if f >= g('S048')[0]: k = prog(f, g('S048')[0], 20); c.line([(300, 900 + 180 * k), (330, 940 + 180 * k)], 10, RED); c.poly([(310, 940 + 180 * k), (345, 920 + 180 * k), (320, 985 + 180 * k)], fill=RED)
        if f >= g('S049')[0]: c.text(700, 900, '90%', comic(70), RED)
        if f >= g('S050')[0]: stick(c, 880, 1000, 'worried', 'down')
        return
    if f <= g('S054')[1]:   # search-result card
        x = 540; xo = 0
        c.rect(150, 880, 930, 1010, fill=(34, 36, 42), outline=None, r=10); c.text(330, 910, 'Orig-Co - Search result', comic(22), (200, 200, 200)); c.text(540, 960, "World's Largest Alternative Asset Manager", comic(28), (240, 240, 245))
        if f >= g('S052')[0]: c.ell(540, 960, 360, 62, fill=None, outline=RED, w=8)
        if g('S051')[0] <= f < g('S053')[1]:
            k = 0 if f < g('S053')[0] else prog(f, g('S053')[0], 30)
            if k < 1: blackstone(c, 760 + 420 * k, 1110 + 60 * k, 270, 100)
        return
    if f <= g('S059')[1] + 20 or True:   # table page, peeking man, yellow column, check, skyline, crowd bubble
        c.rect(380, 690, 700, 1290, fill=(250, 250, 250), outline=(190, 190, 190), w=2)
        for i in range(34): c.rect(395, 705 + i * 17, 690, 713 + i * 17, fill=(185, 185, 185))
        if g('S056')[0] <= f < g('S057')[0]: k = prog(f, g('S056')[0], 12); stick(c, 120 - 200 * (1 - k), 900, 'neutral', 'point')
        if f >= g('S057')[0]: c.rect(395, 705, 470, 705 + min(580, 580 * prog(f, g('S057')[0], 24)), fill=(250, 232, 80))
        if f >= g('S059')[0]: c.line([(780, 1030), (830, 1090), (940, 960)], 24, (40, 170, 80))
        if f >= g('S060')[0]:
            skyline(c, 840, 1260 if False else 1250); speech(c, 780, 800, 380, 150, 'You should', fs=34)
        return

def frame(f):
    c = Cv(); scene(c, f)
    im = Image.new('RGB', (W, H), BG); im.paste(c.out(), (0, Y0))
    t = caption(f)
    if t:
        vis, full = t; d = ImageDraw.Draw(im)
        lines = [[]]
        for w in full:
            if d.textlength(' '.join(lines[-1] + [w]), font=CAPF) > 800: lines.append([w])
            else: lines[-1].append(w)
        # v3 (measured on 21 ref frames): block centred y~1353, pitch 62, lines centred x~531, words revealed left-to-right
        n = len(vis); k = 0
        for i, ln in enumerate(lines):
            y = 1353 + (i - (len(lines) - 1) / 2) * 62
            x0 = 531 - d.textlength(' '.join(ln), font=CAPF) / 2
            shown = ln[:max(0, n - k)]; k += len(ln)
            if shown: d.text((x0, y), ' '.join(shown), font=CAPF, fill=BLK, anchor='lm')
    return im

if __name__ == '__main__':
    out = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 1660
    p = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '14', out], stdin=subprocess.PIPE)
    for f in range(n): p.stdin.write(frame(f).tobytes())
    p.stdin.close(); p.wait(); print('rendered', n, 'frames ->', out)
