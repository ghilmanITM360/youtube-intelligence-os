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
def mono(sz): return ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', sz, index=0)
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
CANDLES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candles.json')))
EV = [int(r['start_frame']) for r in csv.DictReader(open(WS + 'caption_event_ledger.csv'))]
WS_ = [x[1] for x in words]
_d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
# E38 (v14): ref changes the caption at 190 ledger events but ASR timing maps several to the same word; spread duplicates onto the next unrevealed word without overrunning the next distinct word
_raw = [max([i for i, w in enumerate(WS_) if w <= e / FPS + 0.04] or [-1]) for e in EV]
EVIDX = []
for k, r in enumerate(_raw):
    prev = EVIDX[-1] if EVIDX else -1
    nxt = next((x for x in _raw[k + 1:] if x > r), len(WS_))
    EVIDX.append(r if r > prev else (prev + 1 if prev + 1 < nxt else prev))
# v21 (E43): caption TEXT, case and timing read from the reference by OCR at every caption event (caption_ocr_10nE.json) instead of ASR words (ASR gave Sentence-case, wrong words/timing; found by independent visual review)
_OC = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'caption_ocr_10nE.json')))
_EVT = []   # (frame, visible words, chunk id)
_chunk_full = {}
_cid = -1; _prev = []
for r in _OC:
    w = ' '.join(r['lines']).split()
    if w and not (_prev and w[:len(_prev)] == _prev): _cid += 1
    if w: _chunk_full[_cid] = w if len(w) >= len(_chunk_full.get(_cid, [])) else _chunk_full[_cid]
    _EVT.append((r['f'], w, _cid)); _prev = w
def caption(f):
    ev = [e for e in _EVT if e[0] <= f]
    if not ev or not ev[-1][1]: return None
    return ev[-1][1], _chunk_full[ev[-1][2]]
def chunk_lines(a, b): return 1
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
    def poly(s, pts, fill=None, outline=None, w=4):
        s.d.polygon([s.p(*q) for q in pts], fill=fill)
        if outline: s.line(list(pts) + [pts[0]], w, outline)
    def text(s, x, y, t, font, fill=BLK, anchor='mm', sw=0):
        f = font.font_variant(size=font.size * SS); s.d.text(s.p(x, y), t, font=f, fill=fill, anchor=anchor, stroke_width=int(sw * SS), stroke_fill=fill)
    def rline(s, pts, w, col):   # v16: round-cap polyline
        s.line(pts, w, col)
        for q in pts: s.ell(q[0], q[1], w / 2, w / 2, fill=col, outline=None)
    def out(s): return s.im.resize((W, Y1 - Y0), Image.LANCZOS)

def ease(k): k = max(0., min(1., k)); return 1 - (1 - k) ** 3
def prog(f, a, n): return ease((f - a) / n)

def qmark(c, x, y, r=105):
    c.ell(x, y, r, r, fill=BLK, outline=None); c.text(x, y + 4, '?', comic(int(r * 1.35)), (255, 255, 255))
def chart(c, x, y, w=220):
    h = w * .78; c.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2, fill=(236, 246, 250), outline=BLK, w=5)
    for col, ys in (((200, 40, 45), (.1, -.1, .2, -.25, .05)), ((60, 150, 80), (-.2, .15, -.05, .2, -.15)), ((60, 90, 200), (.15, -.2, .1, -.1, .2))):
        c.line([(x - w * .4 + i * w * .2, y + ys[i] * h * .8) for i in range(5)], 4, col)
def chart2(c, cx, cy, w, h, ix=None):
    c.rect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, fill=(205, 225, 245), outline=BLK, w=6)
    ix = cx if ix is None else ix; iw, ih = w * .64, h * .57
    if iw < 20: return
    for col, ys in (((200, 40, 45), (.1, -.1, .2, -.25, .05)), ((48, 150, 60), (-.2, .15, -.05, .2, -.15)), ((60, 90, 200), (.15, -.2, .1, -.1, .2))):
        c.line([(ix - iw / 2 + i * iw / 4, cy + ys[i] * ih * .8) for i in range(5)], max(3, w / 55), col)
def dollar(c, x, y, sz=205):
    f = comic(sz).font_variant(size=sz * SS); c.d.text(c.p(x, y), '$', font=f, fill=(48, 150, 50), anchor='mm', stroke_width=int(6 * SS), stroke_fill=BLK)
def moneybag(c, x, y, w=134, h=194):   # v19 (E40): ref moneybag: dark green sack, tied neck with 2 knots, thick outline, yellow $ with black stroke
    c.ell(x, y + h * .12, w / 2, h * .38, fill=(112, 142, 108), outline=BLK, w=8)
    c.poly([(x - w * .2, y - h * .22), (x + w * .2, y - h * .22), (x + w * .34, y - h * .46), (x + w * .1, y - h * .42), (x, y - h * .5), (x - w * .1, y - h * .42), (x - w * .34, y - h * .46)], fill=(112, 142, 108), outline=BLK, w=8)
    c.rect(x - w * .24, y - h * .26, x + w * .24, y - h * .2, fill=(60, 60, 60), outline=None)
    f_ = comic(int(h * .5)).font_variant(size=int(h * .5) * SS); c.d.text(c.p(x, y + h * .14), '$', font=f_, fill=(240, 220, 60), anchor='mm', stroke_width=int(5 * SS), stroke_fill=BLK)
def bag(c, x, y, s=1.0):
    c.ell(x, y + 18 * s, 38 * s, 36 * s, fill=GRN, outline=BLK, w=5); c.poly([(x - 20 * s, y - 12 * s), (x + 20 * s, y - 12 * s), (x + 10 * s, y - 28 * s), (x - 10 * s, y - 28 * s)], fill=GRN)
    c.line([(x - 22 * s, y - 14 * s), (x + 22 * s, y - 14 * s)], 5); c.text(x, y + 20 * s, '$', comic(int(36 * s)), (230, 240, 200))
def stick(c, x, ytop=870, face='neutral', arms='shrug', lean=0, sweat=False):
    # v5 (E3): head rx80 ry60, scribbly brown hair cap, asymmetric arms, all measured on ref f345 (head centre rel. offsets)
    hx, hy = x + lean * .4, ytop + 115
    R = lambda pts: [(hx + u, hy + v) for u, v in pts]
    c.line(R([(8, 60), (18, 300)]), 8)
    if arms == 'shrug':
        c.line(R([(8, 94), (-10, 134), (-27, 162), (-52, 142), (-82, 132), (-112, 132)]), 9)
        c.line(R([(13, 96), (43, 119), (78, 156), (103, 104), (113, 84), (123, 79)]), 9)
    elif arms == 'down':
        c.line(R([(8, 94), (-50, 175), (-110, 225)]), 9); c.line(R([(13, 96), (70, 175), (120, 225)]), 9)
    else:
        c.line(R([(8, 94), (-45, 20), (-85, -40)]), 9); c.line(R([(13, 96), (70, 150), (40, 200)]), 9)
    c.ell(hx, hy - 12, 80, 72, fill=(211, 173, 130), outline=BLK, w=8)
    hair = [(-110, -36), (-114, -74), (-97, -98), (-67, -111), (-27, -124), (-17, -111), (18, -114), (58, -104), (86, -100), (96, -81), (90, -54), (73, -38), (58, -51), (28, -66), (-7, -74), (-42, -68), (-67, -46), (-82, -11), (-97, -1)]
    c.poly(R(hair), fill=(108, 78, 54), outline=BLK, w=8)
    c.line(R(hair + [hair[0]]), 8)
    for ex in (-7, 34): c.ell(hx + ex, hy - 13, 7, 10, fill=BLK, outline=None)
    if face == 'worried': c.line([(hx - 20, hy + 24), (hx, hy + 17), (hx + 22, hy + 24)], 5); c.line([(hx - 20, hy - 34), (hx + 2, hy - 42)], 4)
    elif face == 'happy': c.line([(hx - 20, hy + 17), (hx, hy + 30), (hx + 22, hy + 17)], 5)
    else: c.line([(hx - 14, hy + 19), (hx + 15, hy + 20)], 5)
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
def earth(c, x, y, r=222, burning=False, swirl=False, sweat=False, look=0):
    # v5: measured on ref f345 (centre (700,305) r222). Navy ocean, green land, white clouds, big eyes, optional sweat drop. Hand-built polygons.
    if r <= 0: return
    k = r / 222.
    T = lambda pts: [(x + (px - 700) * k, y + (py - 305) * k) for px, py in pts]
    c.ell(x, y, r, r, fill=(33, 52, 108), outline=BLK, w=10)
    DK, GR, WH = (18, 30, 78), (58, 118, 54), (236, 238, 240)
    for pts, col in [
        ([(520, 200), (560, 170), (640, 210), (610, 290), (560, 330), (520, 300)], DK),
        ([(600, 420), (680, 450), (780, 470), (720, 500), (620, 480)], DK),
        ([(650, 200), (720, 185), (790, 170), (850, 200), (880, 270), (900, 330), (880, 420), (820, 460), (770, 430), (740, 400), (700, 330), (660, 260)], GR),
        ([(490, 330), (540, 350), (560, 400), (520, 440), (490, 420)], GR),
        ([(600, 135), (700, 122), (790, 128), (730, 152), (640, 168)], GR),
        ([(520, 262), (548, 182), (590, 162), (602, 200), (612, 250), (582, 272), (540, 272)], WH),
        ([(582, 132), (640, 108), (740, 110), (790, 122), (742, 132), (662, 152), (622, 172), (602, 150)], WH),
        ([(822, 150), (860, 172), (890, 232), (880, 252), (850, 212), (802, 200)], WH),
        ([(540, 356), (600, 362), (650, 392), (700, 420), (790, 426), (822, 442), (800, 472), (700, 482), (600, 472), (560, 442), (546, 400)], WH),
        ([(640, 510), (740, 496), (800, 490), (752, 516), (682, 522)], WH),
        ([(888, 340), (910, 330), (902, 372), (872, 402), (860, 390)], WH),
    ]:
        c.poly(T(pts), fill=col, outline=BLK, w=4)
    ex = lambda cx, cy, rx, ry: c.ell(x + (cx - 700) * k, y + (cy - 305) * k, rx * k, ry * k, fill=(250, 250, 250), outline=BLK, w=6)
    ex(668, 317, 30, 38); ex(742, 310, 30, 38)
    for cx, cy in ((668 + look, 314), (748 + look, 310)):
        if swirl:
            for q in range(3): c.ell(x + (cx - 700) * k, y + (cy - 305) * k, (22 - 7 * q) * k, (22 - 7 * q) * k, fill=None, outline=BLK, w=3)
        else: c.ell(x + (cx - 700) * k, y + (cy - 305) * k, 10 * k, 15 * k, fill=BLK, outline=None)
    if sweat:
        c.poly(T([(818, 188), (836, 222), (840, 245), (818, 272), (796, 250), (798, 222)]), fill=(80, 200, 230), outline=BLK, w=4)
    if burning:
        for fx, fy, s_ in ((x - r * .9, y + r * .5, 1), (x + r * .85, y - r * .7, .9), (x - r * .5, y - r * 1.0, .7)):
            c.poly([(fx - 60 * s_, fy + 70 * s_), (fx - 20 * s_, fy - 20 * s_), (fx + 5 * s_, fy - 90 * s_), (fx + 30 * s_, fy - 10 * s_), (fx + 70 * s_, fy + 70 * s_)], fill=(240, 130, 30), outline=BLK)
def years(c, f, xs, ys=968, fs=100):   # v16 (E4): ref digits = unslashed-zero monoline (Courier New + 1px stroke), NOT Menlo (slashed 0)
    for x, t in xs: c.text(x, ys + 4, t, ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 97), sw=2.2)
ARR = (188, 28, 46)
def arrow_l(c, x, y, L=155, col=ARR):   # v16 (E4): ref arrow 20 px round-cap, flat chevron head (dx38, dy26)
    x += 6; c.rline([(x + L / 2, y), (x - L / 2, y)], 20, col); c.rline([(x - L / 2 + 38, y - 26), (x - L / 2, y), (x - L / 2 + 38, y + 26)], 20, col)
def calendar(c, x, y):
    c.rect(x - 62, y - 50, x + 62, y + 52, fill=(244, 244, 244), outline=BLK, w=8, r=10); c.rect(x - 58, y - 46, x + 58, y - 14, fill=RED)
    for i in range(3): c.line([(x - 40 + i * 40, y - 62), (x - 40 + i * 40, y - 40)], 6)
    for cx_, cy_ in ((x - 30, y + 8), (x + 22, y + 8), (x - 30, y + 36), (x + 22, y + 36), (x - 4, y + 36)): c.rect(cx_ - 10, cy_ - 10, cx_ + 10, cy_ + 10, fill=RED, outline=BLK, w=3, r=4)
def photo(c, x0, y0, x1, y1, tone=(150, 170, 190), label=None):
    c.rect(x0, y0, x1, y1, fill=tone, outline=None)
    mx = (x0 + x1) / 2; c.ell(mx, y0 + (y1 - y0) * .38, (x1 - x0) * .17, (x1 - x0) * .2, fill=(225, 205, 185), outline=None)
    c.poly([(x0 + (x1 - x0) * .15, y1), (x0 + (x1 - x0) * .25, y0 + (y1 - y0) * .68), (x1 - (x1 - x0) * .25, y0 + (y1 - y0) * .68), (x1 - (x1 - x0) * .15, y1)], fill=(60, 70, 90))
    if label: c.text(mx, y1 + 18, label, comic(22), (90, 90, 90))
def blackstone(c, x, y, w=250, h=96, label='ORIG-LOGO'):
    c.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2, fill=(12, 12, 12))
    c.text(x, y, label, TNR(40) if label != 'ORIG-LOGO' else comic(36), (255, 255, 255))

TNR = lambda z: ImageFont.truetype('/System/Library/Fonts/Supplemental/Times New Roman.ttf', z)
def fit_line(c, x, y, words, font, width, fill=BLK):   # v18 (E39): original filler text, truncated to the measured ref line width
    d = c.d; ln = ''
    for w in words:
        t = (ln + ' ' + w).strip()
        if d.textlength(t, font=font.font_variant(size=font.size * SS)) / SS > width: break
        ln = t
    c.text(x, y, ln, font, fill, anchor='lm')
FILL = ('Last spring the two founders of Harbor Group took their own firm public, raising about $2.6 billion from the proceeds and from the sale of shares to the state. '
        'Every number in this practice page is invented filler text for a layout test and carries no real information about any company or any person at all.').split()
def article2(c):   # v18 (E39): ref f870 layout: pink synopsis panel x166-900 y820-926, bold header, 3 sans lines, 4 serif body lines, typewriter source line
    c.rect(166, 820, 900, 926, fill=(252, 244, 240), outline=None)
    c.text(188, 846, 'Synopsis', ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 14, index=1), anchor='lm')
    H = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 14)
    for i, wd in enumerate((668, 600, 506)): fit_line(c, 188, 866 + i * 19, FILL[i * 3:] + FILL, H, wd)
    for i in range(4): fit_line(c, 168, 970 + 36 * i, FILL[i * 4:] + FILL, TNR(15), 732 if i < 3 else 120)
    c.text(168, 1134, 'Source: Orig Daily News', ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 15), anchor='lm')
def banknote(c, x, y, ang, w=104, h=54):
    import math as m
    ca, sa = m.cos(m.radians(ang)), m.sin(m.radians(ang))
    P = lambda dx, dy: (x + dx * ca - dy * sa, y + dx * sa + dy * ca)
    c.poly([P(-w / 2, -h / 2), P(w / 2, -h / 2), P(w / 2, h / 2), P(-w / 2, h / 2)], fill=(150, 190, 140), outline=BLK, w=3)
    c.text(*P(0, 0), '$', comic(max(10, int(h * .62))), (214, 205, 90))
import random as _rnd
def table(c, x0, y0):   # v19 (E41): original filler data table; geometry measured on ref f1470 (page 364x498, header y712-740, rows y~740-1190 pitch ~8.6, columns right-aligned at +55,109,157,199,241,295,355)
    r = _rnd.Random(7); T = TNR(8); B = ImageFont.truetype('/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf', 9)
    c.text(x0 + 182, y0 + 8, 'Table 1: Mean First-day Returns and Money Left on the Table, 1980-2025', B)
    for i in range(4): fit_line(c, x0 + 6, y0 + 22 + i * 9, FILL[i * 5:] + FILL, TNR(8), 352)
    for j, hdr in enumerate(('Year', 'Number', 'Equal', 'Proceeds', 'Median', 'Amount', 'Aggregate')): c.text(x0 + (30, 109, 157, 199, 241, 295, 355)[j] - (14 if j else 0), y0 + 66, hdr, T)
    for i in range(46):
        yy = y0 + 80 + i * 8.6; c.text(x0 + 41, yy, str(1980 + i), T, anchor='rm')
        for j, cx in enumerate((109, 157, 199, 241, 295, 355)): c.text(x0 + cx, yy, ('%d' % r.randint(20, 480), '%.1f%%' % r.uniform(5, 40), '%.1f%%' % r.uniform(5, 40), '%.1f%%' % r.uniform(3, 30), '$%.2f billion' % r.uniform(.1, 9), '$%.1f billion' % r.uniform(.5, 40))[j], T, anchor='rm')
    c.text(x0 + 64, y0 + 497, 'Source: Orig Daily News Data', ImageFont.truetype('/System/Library/Fonts/Supplemental/Courier New.ttf', 9))
def article(c, x0, y0, x1, y1, n=9):
    c.rect(x0, y0, x1, y1, fill=(252, 244, 240), outline=(210, 200, 195), w=2)
    for i in range(n): c.rect(x0 + 24, y0 + 26 + i * 22, x1 - 24 - (60 if i % 4 == 3 else 0), y0 + 34 + i * 22, fill=(170, 165, 165))
def candles(c, x0, y0, x1, y1, f):
    # v5 (E8): candle bodies extracted from ref f1212 (extract_candles.py -> candles.json); drawn in own plain style, no platform UI
    c.rect(235, 745, 830, 1170, fill=(255, 255, 255), outline=(222, 222, 222), w=2)
    for yy in range(800, 1170, 70): c.line([(235, yy), (830, yy)], 1, (236, 236, 236))
    # v10 (E27): measured on ref f1210: header text x244-400 y688-760, right axis labels x804-840 every 36 px y724-1188, bottom axis labels y1172-1204 pitch 48 (x364-764) + wide label x244-336; original generic text only
    HV = lambda z, b=0: ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', z, index=1 if b else 0)
    # v17 (E8): measured on ref f1212: header text 12 px tall x245-376, axis labels only 6 px tall (x805-842, pitch 36 from y723), year labels 9 px tall pitch 48, logo 17 px tall x245-341 y1176-1192
    c.text(245, 718, 'Orig Index Co. . 1M . EXCH', HV(15), anchor='lm')
    for k in range(14): c.text(805, 726 + 36 * k, '%d.00%%' % (20 - 10 * k), HV(9), anchor='lm')
    for i in range(10): c.text(366 + 48 * i, 1203, str(2009 + i), HV(11, 1))
    c.rect(245, 1177, 263, 1192, fill=BLK); c.text(268, 1184, 'OrigView', HV(15, 1), anchor='lm')
    for q in CANDLES:
        col = (200, 60, 72) if q['c'] == 'r' else (58, 150, 122)
        xm = (q['x0'] + q['x1']) / 2
        c.line([(xm, q['t'] - 4), (xm, q['b'] + 4)], 1, col)
        c.rect(q['x0'] - .5, q['t'], q['x1'] + 1.5, max(q['b'], q['t'] + 2), fill=col, outline=None)
def spiral(c, cx, cy, rx, ry, turns=2.4, w=4):
    import math as m
    pts = [(cx + rx * (t / (turns * 2 * m.pi)) * m.cos(t), cy + ry * (t / (turns * 2 * m.pi)) * m.sin(t)) for t in [i * .15 for i in range(int(turns * 2 * m.pi / .15) + 1)]]
    c.line(pts, w)
def earth_burn(c, f):
    # v5 (E9): measured on ref f1132 (centre (528,980) r368, spiral eyes, flames TR + BL changing every 10 frames)
    X, Y, K = 528, 980, 1.0
    T = lambda pts, dy=0: [(px, py + 600 + dy) for px, py in pts]
    c.ell(X, Y, 368, 368, fill=(38, 58, 112), outline=BLK, w=12)
    DK, GR, WH = (20, 34, 82), (66, 128, 62), (236, 238, 240)
    for pts, col in [
        ([(200, 260), (330, 330), (410, 470), (450, 560), (330, 600), (240, 520), (190, 400)], DK),
        ([(450, 260), (520, 190), (600, 160), (700, 190), (780, 300), (800, 400), (770, 500), (720, 560), (640, 540), (600, 480), (560, 400), (480, 380), (440, 330)], GR),
        ([(180, 320), (260, 400), (330, 470), (250, 540), (190, 500)], GR),
        ([(480, 95), (560, 70), (660, 85), (700, 150), (600, 140), (520, 160)], GR),
        ([(320, 90), (400, 60), (560, 60), (500, 110), (440, 140), (420, 190), (380, 210), (330, 150)], WH),
        ([(230, 240), (300, 150), (360, 200), (370, 300), (320, 320), (290, 270), (240, 300)], WH),
        ([(270, 455), (330, 470), (420, 520), (470, 540), (560, 525), (500, 500), (420, 440), (390, 420), (380, 440)], WH),
        ([(440, 580), (600, 565), (710, 570), (720, 600), (670, 640), (560, 655), (440, 650), (410, 620)], WH),
        ([(800, 520), (840, 440), (870, 410), (860, 450), (820, 520)], WH),
    ]:
        c.poly(T(pts), fill=col, outline=BLK, w=5)
    for ex, ey in ((475, 375), (600, 368)):
        c.ell(ex, ey + 600, 48, 78, fill=(252, 252, 252), outline=BLK, w=7); spiral(c, ex, ey + 600, 32, 54)
    j = (f // 10) % 2 * 10
    c.poly(T([(650, 60), (700, 120), (670, 180), (700, 260), (760, 310), (850, 290), (930, 200 - j), (972, 60)]), fill=(222, 120, 25))
    c.poly(T([(730, 110), (780, 70 + j), (790, 150), (870, 160), (830, 230), (760, 250), (720, 200)]), fill=(238, 198, 60))
    c.poly(T([(70, 620), (100, 560), (150, 480), (180, 330 + j), (215, 420), (250, 400), (260, 470), (320, 560), (410, 630), (420, 662), (70, 662)]), fill=(222, 120, 25))
    c.poly(T([(195, 580), (260, 550 - j), (300, 580), (330, 620), (290, 662), (195, 662)]), fill=(238, 198, 60))
def bedroom(c, f):
    # v5 (E7): measured from ref f754 (half-scale tile coords x2); original art
    c.rect(0, 656, 1080, 1262, fill=(236, 236, 238))
    c.poly([(780, 1060), (1080, 1030), (1080, 1262), (800, 1262)], fill=(150, 152, 158))
    c.rect(680, 656, 1080, 940, fill=(146, 198, 222)); c.poly([(700, 656), (1080, 656), (1080, 790)], fill=(50, 122, 150))
    c.line([(940, 780), (1080, 700)], 10, (255, 255, 255)); c.line([(980, 800), (1080, 740)], 8, (255, 255, 255))
    c.rect(0, 656, 90, 800, fill=(232, 176, 186), outline=BLK, w=4); c.rect(70, 690, 150, 840, fill=(225, 214, 190), outline=BLK, w=4)
    c.poly([(60, 1090), (740, 1100), (760, 1130), (40, 1130)], fill=(222, 212, 180), outline=BLK, w=4)
    c.poly([(0, 1130), (760, 1125), (770, 1262), (0, 1262)], fill=(126, 188, 198), outline=BLK, w=5)
    c.line([(260, 1170), (285, 1210), (300, 1260)], 4); c.line([(490, 1160), (510, 1210), (500, 1260)], 4)
    c.ell(300, 960, 78, 48, fill=(244, 242, 234), outline=BLK, w=5); c.ell(540, 985, 80, 52, fill=(244, 242, 234), outline=BLK, w=5)
    c.poly([(350, 1000), (480, 1000), (500, 1110), (340, 1110)], fill=(72, 172, 190), outline=BLK, w=5)
    c.ell(410, 895, 96, 88, fill=(150, 96, 58), outline=BLK, w=6)
    c.ell(412, 912, 40, 46, fill=(250, 215, 185), outline=BLK, w=5); c.ell(400, 904, 4, 5, fill=BLK, outline=None); c.ell(428, 904, 4, 5, fill=BLK, outline=None); c.line([(402, 930), (416, 936), (428, 928)], 3)
    c.ell(430, 1040, 56, 38, fill=(96, 166, 226), outline=BLK, w=5)
    if f >= ST['S030'][0]:
        c.ell(770, 960, 160, 100, fill=(255, 255, 255), outline=BLK, w=6); c.poly([(650, 960), (600, 985), (660, 1010)], fill=(255, 255, 255), outline=BLK, w=4)
        c.text(770, 960, 'And my baby\nwill be called...', mono(27))
def baby_close(c, f):
    # v5 (E7): measured on ref f802 (crop y0=640). Face region is a generic original face (E1 stand-in for third-party photo).
    Y = 640
    P = lambda pts: [(x, y + Y) for x, y in pts]
    c.rect(0, 655, 1080, 1265, fill=(222, 214, 190))
    c.poly(P([(0, 15), (1080, 15), (1080, 205), (700, 225), (400, 250), (165, 255), (0, 265)]), fill=(122, 166, 174), outline=BLK, w=10)
    c.line(P([(235, 600), (240, 430)]), 44); c.line(P([(930, 340), (1020, 370), (1090, 430)]), 20)
    c.poly(P([(165, 230), (175, 170), (215, 120), (300, 60), (400, 30), (480, 40), (545, 90), (620, 170), (700, 230), (760, 255), (840, 270), (930, 330), (940, 420), (930, 500), (935, 560), (925, 622), (780, 625), (640, 625), (450, 625), (380, 540), (320, 450), (250, 360), (190, 300), (170, 260)]), fill=(142, 194, 215), outline=BLK, w=14)
    c.ell(425, 252 + Y, 125, 120, fill=BLK, outline=None); c.ell(425, 252 + Y, 112, 108, fill=(222, 185, 150), outline=None)
    c.ell(385, 240 + Y, 34, 22, fill=None, outline=(70, 70, 70), w=4); c.ell(470, 232 + Y, 34, 22, fill=None, outline=(70, 70, 70), w=4)
    c.ell(385, 242 + Y, 6, 6, fill=BLK, outline=None); c.ell(470, 234 + Y, 6, 6, fill=BLK, outline=None); c.line([(395, 320 + Y), (440, 326 + Y)], 5)
    if f != ST['S032'][0]:
        c.ell(790, 395 + Y, 160, 128, fill=(255, 255, 255), outline=BLK, w=12); c.poly(P([(650, 470), (700, 500), (660, 590)]), fill=(255, 255, 255), outline=BLK, w=8)
        c.text(790, 400 + Y, 'Peter\nPeterson!', hand(50))
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
    # v6: SH001-SH003 rebuilt from measurements (ref f12-f248): circles d220 pitch 272 scroll 2.3 px/frame; chart 490x324 in the row
    if f <= g('S003')[1]:   # question-mark row scrolls left; chart enters the row at f70
        slide = 0
        off = 2.3 * max(0, f - 20)
        for k in range(-1, 9):
            x = 282 + 272 * (k - 1) - off + 0 + slide
            qmark(c, x, 952, 110)
        if f < 22:   # E32: reference row fills left->right at ~65 px/frame (edge 412@f12, 672@f16, 932@f20)
            ed = max(150, 412 + 65 * (f - 12))
            if ed < 1100: c.rect(ed, 640, 1100, 1300, fill=(253, 253, 253), outline=None, w=0)
        if f >= s3[0]:
            cx = 575 - 2.3 * (f - 70); kk = ease((f - s3[0]) / 3)
            chart2(c, cx, 966, 490 * kk + 1, 324 * kk + 1, ix=cx if f < 72 else 541)
        return
    if f <= g('S008')[1]:   # chart left (226x180 @227,970), money bag right (138x156), small ? (d104), big ? (d224)
        chart2(c, 227, 970, 226, 180)
        bag(c, 935, 1082, 1.85)
        for sid, (x, y) in (('S005', (124, 771)), ('S006', (888, 857)), ('S007', (335, 1139))):
            if f >= g(sid)[0]: qmark(c, x, y, 52)
        if f >= g('S008')[0]: qmark(c, 562, 955, int(30 + 82 * ease((f - g('S008')[0]) / 6)))
        return
    if f <= g('S012')[1]:   # dollar sign (green, black outline, 118x229 @ (542,955)); bubble r=130+3.25*(f-192)
        b0, b1 = g('S010')
        if f >= b0 and f < g('S011')[0]:
            r = max(8, 130 + 3.25 * (f - 192)); ry = r; cy_ = 957 - r + ry; c.ell(537, cy_, r, ry, fill=(125, 186, 198), outline=(60, 150, 125), w=6); c.ell(537 - r * .45, 957 - r * .4, r * .12, r * .22, fill=(205, 232, 236), outline=None)
        if g('S011')[0] <= f <= g('S011')[1]:
            k = (f - g('S011')[0]) / 12
            for a_ in range(14): ang = a_ * 360 / 14 * math.pi / 180; c.ell(552 + math.cos(ang) * 245, 956 + math.sin(ang) * 245, 14 * (1 - k) + 3, 14 * (1 - k) + 3, fill=(120, 180, 180), outline=None)
        dollar(c, 542, 941)
        return
    if f <= g('S016')[1]:   # stick man and Earth (v5: man slides left 525->232 over S014; Earth lands at f312-319 at (700,965) r222; sweat from S016)
        km = min(1, max(0, (f - 302) / 16))   # v10 (E25): ref man slides LINEARLY ~18 px/frame f302-318
        stick(c, 525 - 293 * km, 880, 'neutral', 'shrug')
        if f >= 319:   # v10: ref Earth hard-cuts in at f319 (bbox already final)
            earth(c, 700, 965, 222, sweat=f >= g('S016')[0], look=(6 if f >= g('S016')[0] else 0))
        return
    if f <= g('S019')[1]:   # timeline
        if f < 399:
            # v17 (E4, measured via arrow centroids on ref f366-f400): strip moves RIGHT 80 px per DISTINCT frame; ref content is 24 fps in a 30 fps file (dup every 5th frame, offsets 2 mod 5 from cut f366); lands f399.
            # final arrow centres 726/1237/1741/2237/2805 (gaps 511/504/496/568, not uniform 560); years sit 274 px right of the preceding arrow, 2007 at 440.
            k_ = f - 366; sh = 80 * (26 - (k_ - (k_ + 3) // 5))
            AF = [726, 1237, 1741, 2237, 2805]; YF = [440, 1000, 1481, 1980, 2511]   # 2009/2010 trimmed -30/-35 px after visual check at f380
            for yr, xf in zip(('2007', '2008', '2009', '2010', '2011'), YF): years(c, f, [(xf - sh, yr)], fs=100)
            for a in AF: arrow_l(c, a - sh - 6, 968)
        else:
            years(c, f, [(440, '2007'), (1000, '2008')]); arrow_l(c, 720, 968)
            if f >= g('S019')[0]:
                k = ease((f - g('S019')[0]) / 3); calendar(c, 198, 970 + 12 * (1 - k)); c.text(200, 861, 'June', hand(46))
        return
    if f <= g('S021')[1]:   # Wall Street sign + stand-in clips, then "The market:" clip
        if f <= g('S020')[1]:
            k = ease((f - g('S020')[0]) / 6); xo = -300 * (1 - k)
            c.rect(-6 + xo, 656, 128 + xo, 1263, fill=(80, 96, 112), outline=BLK, w=6)   # v6: pole x0-128 full band (ref f458)
            c.rect(122 + xo, 690, 821 + xo, 1000, fill=(32, 48, 48), outline=BLK, w=6, r=8); c.text(470 + xo, 850, 'WALL', hand(170), (245, 245, 245)); c.text(740 + xo, 800, 'ST', comic(50), (245, 245, 245))
            if f >= g('S020')[0] + 6: photo(c, 426, 1002, 708, 1212, (120, 130, 160)); photo(c, 748, 1002, 1030, 1212, (110, 60, 70))
        else:
            c.text(532, 773, 'The market:', hand(56))
            c.rect(292, 840, 788, 1172, fill=(40, 24, 20)); earth(c, 540, 1020, 0)
            for i, (fx, s_) in enumerate(((380, 1.1), (540, 1.5), (700, 1.1))): c.poly([(fx - 70 * s_, 1172), (fx - 20 * s_, 1020), (fx, 900), (fx + 30 * s_, 1020), (fx + 70 * s_, 1172)], fill=(240, 120, 30))
            c.ell(540, 1100, 60, 70, fill=(190, 40, 40), outline=None)
        return
    if f <= g('S022')[1]: stick_blk(c, 540, 'happy'); return
    if f <= g('S025')[1]:   # Blackstone, founders
        blackstone(c, 540, 773, 336, 130)   # v8 (ref f553-f613): logo 336x130, portraits (258,882)-(508,1200) and (586,882)-(855,1200)
        if f >= g('S024')[0]:   # v10 (E30): ref has a small text column x36-232 y964-1196 and a one-line note y1212-1228 left of the portraits (words as bars, no source text)
            for ln in range(7):
                yy = 970 + ln * 36
                for x0_, x1_ in ((36, 80), (92, 144), (160, 216)): c.rect(x0_, yy, x1_, yy + 12, fill=(40, 40, 40))
            c.rect(36, 1214, 232, 1226, fill=(60, 60, 60))
        if f >= g('S024')[0]: photo(c, 258, 882, 508, 1200, (140, 160, 185), 'Steven S. (stand-in)')
        if f >= g('S025')[0]: photo(c, 586, 882, 855, 1200, (170, 150, 150), 'Peter P. (stand-in)')
        return
    if f <= g('S026')[1]: stick_blk(c, 540, 'happy'); return
    if f <= g('S027')[1]:   # yacht stand-in with money bags
        # v19 (E40): visual check showed ref = photo x240-840 y810-1110 + THREE big moneybags (~135x190, thick outline, yellow $) + street lamp right; stand-in was a small 480x270 boat card and 50 px bags
        c.rect(240, 810, 840, 1110, fill=(150, 185, 205)); c.rect(240, 930, 840, 1110, fill=(95, 135, 155)); c.ell(420, 980, 45, 55, fill=(235, 190, 160), outline=None); c.poly([(380, 1110), (400, 1020), (470, 1020), (500, 1110)], fill=(240, 240, 240))
        c.rect(789, 905, 801, 1110, fill=(20, 20, 20)); c.rect(772, 905, 818, 975, fill=(235, 235, 220), outline=BLK, w=6, r=8)
        for bx, by in ((180, 1040), (275, 1082), (852, 1072)): moneybag(c, bx, by)
        return
    if f <= g('S028')[1]: stick_blk(c, 540, 'neutral'); return
    if f <= g('S033')[1]:   # baby / newborn bubbles
        if f < g('S031')[0]: bedroom(c, f)
        else: baby_close(c, f)
        return
    if f <= g('S034')[1]: stick_blk(c, 540, 'neutral'); return
    if f <= g('S039')[1]:   # article with logo, portraits, banknotes
        if f >= g('S039')[0]: c.rect(592, 1032, 890, 1052, fill=(250, 235, 90))   # ref: yellow highlight sits on body line 3
        article2(c)   # v18: replaces grey bars (E39 true cause: stand-in bars were 2x the ref ink; ref text is tiny serif)
        if f >= g('S036')[0]: blackstone(c, 859, 763, 234, 94, 'Orig Group')   # ref logo box 236x94
        if f >= g('S037')[0]: photo(c, 543, 1085, 709, 1263, (140, 160, 185))
        if f >= g('S038')[0]: photo(c, 761, 1085, 939, 1263, (170, 150, 150))
        if f >= 962:   # v18: ref notes spawn from f~962, 12-22 alive, fall ~8 px/frame, tilted, outlined, with $ (trajectories UNVERIFIED; count/area measured)
            for i in range(28):   # visual check v18a: 2-per-3-frames spawn was too dense (20 alive vs ~8 at f990 in ref) and notes too big; ref sizes vary ~50-100 px
                s_ = int(962 + 3.3 * i); yy = 670 + 8 * (f - s_); k_ = .5 + .75 * ((i * 0.618) % 1)
                if f >= s_ and yy < 1000: banknote(c, 70 + (i * 397) % 940, yy, ((i * 53) % 50) - 25, 104 * k_, 54 * k_)
        return
    if f <= g('S042')[1]:
        # v10 (E24): measured linear scroll 24 px per moving frame f1065-1086, held frames 1068/1073/1078/1083, total 432 px; calendar+years+arrows scroll as one strip
        mv = sum(1 for i in range(1065, min(f, 1086) + 1) if i not in (1068, 1073, 1078, 1083))
        sh = 24 * mv
        calendar(c, 198 - sh, 970); c.text(200 - sh, 861, 'June', hand(46))
        years(c, f, [(444 - sh, '2007'), (992 - sh, '2008'), (1492 - sh, '2009')]); arrow_l(c, 726 - sh, 968); arrow_l(c, 1236 - sh, 968)
        return
    if f <= g('S043')[1]: earth_burn(c, f); return
    if f <= g('S046')[1]:   # red tiles accumulate
        # v10 (E31): tiles measured on ref dark mass: first 352x220 at (96,732) f1161; extents reach x964/y1016 f1164, y1204 f1167, y712 f1170, x1012 f1174
        TL = ((96, 732, 448, 952, 1161), (612, 796, 964, 1016, 1164), (160, 984, 512, 1204, 1167), (480, 712, 832, 932, 1170), (660, 952, 1012, 1172, 1174), (330, 860, 682, 1080, 1178))
        for x0_, y0_, x1_, y1_, t0 in TL:
            if f >= t0:
                c.rect(x0_, y0_, x1_, y1_, fill=(150, 25, 35)); c.text((x0_ + x1_) / 2, (y0_ + y1_) / 2, 'not stonks', comic(32), (230, 230, 230)); c.ell(x0_ + 60, (y0_ + y1_) / 2, 40, 55, fill=(60, 60, 70), outline=None)
        return
    if f <= g('S050')[1]:   # candlestick + red arrow + 90% + worried
        candles(c, 220, 760, 880, 1230, f)
        if f >= g('S048')[0]:
            k = max(0., min(1., (f - 1227) / 24)); tx, ty = 250 + 85 * k, 830 + 300 * k   # v17 (E8): ref arrow moves LINEARLY f1227->f1251 (centroid 821->1110), not eased
            c.line([(tx + 48, ty - 62), (tx + 6, ty - 8)], 12, RED); c.poly([(tx, ty), (tx + 34, ty - 6), (tx + 4, ty - 42)], fill=RED)
        if f >= g('S049')[0]: c.text(400, 895, '90%', hand(125), RED)
        if f >= g('S050')[0]:
            # v17 (E8): ref f1285: head blob 198x187 centre (717,1078), hair = black scribble band upper-left, asymmetric dot eyes, open D-mouth, chin-hand stick lines
            O = lambda pts: [(520 + x, 900 + y) for x, y in pts]
            c.ell(717, 1078, 99, 93, fill=(250, 215, 185), outline=BLK, w=7)
            c.poly(O([(92, 165), (95, 130), (110, 100), (150, 75), (190, 60), (215, 65), (210, 82), (188, 95), (165, 110), (145, 135), (130, 160), (105, 168)]), fill=BLK)
            c.ell(667, 1059, 6, 7, fill=BLK, outline=None); c.ell(724, 1024, 6, 7, fill=BLK, outline=None)
            c.poly(O([(168, 222), (180, 188), (205, 178), (232, 182), (235, 195), (215, 215), (190, 228)]), fill=(190, 118, 122), outline=BLK, w=4)
            c.line(O([(183, 243), (183, 302), (243, 316)]), 5); c.line(O([(238, 222), (268, 262), (243, 316)]), 5); c.line(O([(243, 316), (262, 362)]), 5)
        return
    if f <= g('S054')[1]:   # search-result card
        # v8 (ref f1300-f1450): card x220-860 y760-922; logo 377x146 at (601-978,1002-1148) slides out right over S053
        c.rect(220, 760, 860, 922, fill=(34, 36, 42), outline=None, r=10); c.text(400, 795, 'Orig-Co - Search result', comic(22), (200, 200, 200)); c.text(540, 860, "World's Largest Alternative Asset Manager", comic(28), (240, 240, 245))
        if f >= g('S052')[0]: c.ell(540, 841, 300, 62, fill=None, outline=RED, w=8)
        if g('S051')[0] <= f < g('S053')[1]:
            cxl = 790 + 10 * max(0, f - 1390)   # v10 (E26): ref right edge +10 px/frame from f1390, fully out by f1437
            if cxl - 188 < 1080: blackstone(c, cxl, 1075 + 0.4 * max(0, f - 1390), 377, 146)
        return
    if f <= g('S059')[1] + 20 or True:   # table page, peeking man, yellow column, check, skyline, crowd bubble
        # v7 (ref f1465-f1600): page 364x498 slides 355 -> 101 over f1470-1559; yellow column sweeps y774-1143; check (332-523,1046-1216); skyline/bubble right
        x0 = 355 - 254 * ease((f - 1537) / 12)   # ref: static to f1537, ease-out slide f1538-1549
        table(c, x0, 712)   # v19 (E41): ref table is ~46 rows of tiny serif numbers, NO outline; old version had black frame + grey bars
        if f < 1534: stick_blk(c, 136, 'happy', 'hips', ytop=850)   # v19: ref man is the BLACK-haired smiling stickman, already in frame at f1470 (old render drew brown man sliding in)
        elif f < 1540: stick_blk(c, 136 - 300 * ease((f - 1534) / 6), 'happy', 'hips', ytop=850)
        if f >= g('S057')[0]: c.rect(x0 + 13, 774, x0 + 86, 774 + 369 * min(1, prog(f, g('S057')[0], 24)), fill=(250, 232, 80))
        if f >= g('S059')[0]: c.line([(332, 1130), (400, 1216), (523, 1046)], 26, (40, 170, 80))
        if f >= g('S060')[0]:   # v19 (E41): ref f1620: blue glass building x690-994 y794-994 with brown sign (GIGANTIC BUSINESS) above; round bubble x556-820 y974-1204 with tail up-right; clip window inside
            for (bx0, by0, bx1, by1) in ((756, 800, 924, 862), (722, 862, 960, 928), (690, 928, 994, 1000)):   # stepped blue glass tiers (ref f1620)
                c.rect(bx0, by0, bx1, by1, fill=(100, 150, 185), outline=BLK, w=6)
                for i in range(3): c.line([(bx0 + 20 + i * (bx1 - bx0) / 3, by1 - 6), (bx0 + 50 + i * (bx1 - bx0) / 3, by0 + 6)], 8, (160, 195, 215))
            c.rect(756, 716, 924, 786, fill=(120, 62, 30), outline=BLK, w=5)
            for i, wd in enumerate(('GIGANTIC', 'BUSINESS')): c.d.text(c.p(840, 738 + i * 30), wd, font=comic(34).font_variant(size=34 * SS), fill=(250, 250, 250), anchor='mm', stroke_width=int(3 * SS), stroke_fill=(230, 120, 30))
            c.poly([(770, 1070), (830, 1010), (850, 1090)], fill=(255, 255, 255), outline=BLK, w=6)
            c.ell(688, 1090, 132, 115, fill=(255, 255, 255), outline=BLK, w=6); c.text(688, 1018, 'You should', comic(30))
            c.rect(600, 1056, 796, 1170, fill=(70, 66, 66), outline=None); c.text(698, 1150, 'CLIP STAND-IN', comic(16), (240, 240, 240))
        return

# v20 (E42b): ref motion is authored at 24 fps in a 30 fps file; frames in dup_mask (measured on ref, every 5th frame inside motion runs, phase per segment) repeat the previous frame
DUPS = set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dup_mask_10nE.json'))))
def frame(f):
    while f in DUPS: f -= 1
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
