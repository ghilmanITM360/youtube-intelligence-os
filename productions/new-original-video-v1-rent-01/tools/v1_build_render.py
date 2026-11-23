"""V1 Rent 0-75 s segment: builds the scene spec from Take 2 word timings + V1-local approved registry, renders with the existing
CH001 renderer (render_scene.py comp_shot) at 1920x1080 / 30 fps, muxes the Take 2 audio.
  python3 tools/v1_build_render.py [--frames N] [--out PATH] [--spec-only]
Sources of every figure: RESEARCH_DOSSIER.md C-01..C-05 (verified), C-02 (Zillow, status B)."""
import json, os, subprocess, sys, math, hashlib
PS = '/Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance/CHANNEL_VISUAL_AUDIT/CHANNEL_001/PRODUCTION_SYSTEM'
sys.path.insert(0, PS)
import render_scene as rs
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = HERE + '/v1_assets'
WAV = HERE + '/audio/take2/v1_rent_take2.wav'
WAV_SHA = '3ef0297814e610d64f2ebc30e41bdac1df934edcbe437648c354930081c14b6e'
DUR = 75.0; FPS = 30
HELV = '/System/Library/Fonts/Helvetica.ttc'
rs.FONTS['sans'] = (HELV, 0); rs.FONTS['sans_bold'] = (HELV, 1)
INK = (31, 36, 48); OLIVE = (91, 107, 58); CREAM = (244, 237, 225); CORAL = (232, 96, 76); GREY = (217, 210, 195); GREYTXT = (86, 90, 100); OLIVE_L = (163, 174, 127)


# ---------- extra element types (card / grow) on top of the existing renderer ----------
_orig_draw = rs.draw_proc
def draw_proc(el, t):
    ty = el['type']
    if ty == 'card':
        w, h = int(round(el['w'])), int(round(el['h'])); im = Image.new('RGBA', (w + 8, h + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle([4, 4, w + 3, h + 3], radius=el.get('radius', 28), fill=tuple(el.get('fill', CREAM)) + (255,), outline=tuple(INK) + (255,), width=el.get('ow', 4)); return im
    if ty == 'grow':
        w, h = int(round(el['w'])), int(round(el['h'])); k = rs.ease(el.get('ease', 'out'), (t - el.get('t0', 0)) / el.get('dur', 1.0))
        im = Image.new('RGBA', (w + 8, h + 8), (0, 0, 0, 0))
        if k <= 0.002: return im
        d = ImageDraw.Draw(im); box = [4, 4, w + 3, h + 3]
        if el.get('dir', 'right') == 'up': box[1] = 4 + h - max(2, h * k)
        else: box[2] = 4 + max(2, w * k)
        d.rounded_rectangle(box, radius=el.get('radius', 6), fill=tuple(el['fill']) + (255,), outline=tuple(INK) + (255,), width=el.get('ow', 3)); return im
    return _orig_draw(el, t)
rs.draw_proc = draw_proc


# ---------- registry resolution (sha verified) ----------
def reg_file(aid):
    r = [x for x in json.load(open(ROOT + '/asset_registry.json')) if x['id'] == aid and x.get('status') == 'approved'][-1]
    p = os.path.join(ROOT, r['file'])
    if hashlib.sha256(open(p, 'rb').read()).hexdigest() != r['sha256']: raise SystemExit('checksum mismatch ' + aid)
    return p


# ---------- element helpers ----------
els = []
def add(**e): els.append(e); return e
def tw(text, size, font='sans_bold'): return rs.font(font, size).getlength(text)
def fade_out(e, t_end, dur=0.3):
    e['keys'] = e.get('keys', []) + [dict(t=0, opacity=1, ease='linear'), dict(t=t_end - dur, opacity=1, ease='linear'), dict(t=t_end, opacity=0, ease='linear')]
    e['exit'] = dict(t=t_end); return e
def text(s, x, y, size, t0, t1=None, color=INK, font='sans_bold', left=False, layer=10, pre=0.0, enter='fade', dur=0.25, id=None):
    cx = x + tw(s, size, font) / 2 if left else x
    e = add(type='text', text=s, x=cx, y=y, size=size, font=font, color=list(color), layer=layer, enter=dict(preset=enter, t=t0, dur=dur), id=id or 'tx%d' % len(els))
    if t1: fade_out(e, t1)
    return e
def counter(to, x, y, size, t0, dur, t1=None, color=INK, suffix='%', left_w=None, layer=10, dec=1):
    cx = x + (left_w / 2 if left_w else 0)
    e = add(type='counter', **{'from': 0, 'to': to}, t0=t0, dur=dur, dec=dec, suffix=suffix, x=cx, y=y, size=size, font='sans_bold', color=list(color), layer=layer, enter=dict(preset='cut', t=t0), id='ct%d' % len(els))
    if t1: fade_out(e, t1)
    return e
def grow(x0, y, w, h, fill, t0, dur, direction='right', t1=None, layer=8, ow=3, radius=6, ease='out'):
    # x0,y = left/top of the final shape
    e = add(type='grow', w=w, h=h, fill=list(fill), dir=direction, t0=t0, dur=dur, x=x0 + w / 2 + 4 - 4, y=y + h / 2, layer=layer, ow=ow, radius=radius, ease=ease, enter=dict(preset='cut', t=t0), id='gr%d' % len(els))
    if t1: fade_out(e, t1)
    return e
def box(x0, y0, w, h, outline, t0, t1=None, ow=8, layer=11):
    e = add(type='panel', w=int(round(w)), h=int(round(h)), fill=None, outline=list(outline), outline_w=ow, x=x0 + w / 2, y=y0 + h / 2, layer=layer, enter=dict(preset='pop', t=t0, dur=0.3), id='bx%d' % len(els))
    if t1: fade_out(e, t1)
    return e

# ---------- layout ----------
CARD = dict(x0=520, y0=24, w=1360, h=524)
CX0 = CARD['x0'] + 50           # content left
SRC = (96, 98, 108)
def source(lines, t0, t1=None, y0=488):
    for i, ln in enumerate(lines): text(ln, CX0, y0 + i * 32, 28, t0, t1, color=SRC, font='sans', left=True, layer=12)

def build():
    words = json.load(open(HERE + '/audio/take2/t2_words_merged.json'))
    # --- backdrop, character, card ---
    add(asset=reg_file('v1_bg_room'), x=960, y=540, layer=0, enter=dict(preset='cut', t=0), id='room')
    add(asset=reg_file('v1_bg_room_table'), x=1535, y=928, scale=0.348, layer=1, enter=dict(preset='cut', t=0), id='table')
    bob = []; n = int(DUR / 0.7) + 2
    for i in range(n): bob.append(dict(t=round(i * 0.7, 3), y=700 + (4 if i % 2 else -4), scale=0.303 + (0.0015 if i % 2 else -0.0015), ease='in_out'))
    bill, neutral = reg_file('v1_ch_p3_bill_closed'), reg_file('v1_ch_p1_neutral_closed')
    add(asset=bill, poses=[dict(t=0, asset=bill), dict(t=16.4, asset=neutral), dict(t=63.6, asset=bill), dict(t=70.2, asset=neutral)], x=330, y=700, scale=0.303, keys=bob, layer=4, enter=dict(preset='cut', t=0), id='mara')
    add(type='card', w=CARD['w'], h=CARD['h'], x=CARD['x0'] + CARD['w'] / 2 + 4, y=CARD['y0'] + CARD['h'] / 2 + 4, layer=5, enter=dict(preset='fade', t=0.2, dur=0.5), id='card')

    # ===== SH1 hook 0-16.4: two bars =====
    T1 = 16.4
    text('Rent inflation, 12 months to September 2026', 1200, 58, 34, 0.7, T1, color=GREYTXT, font='sans')
    base, maxh, bw = 385, 190, 170
    bx = [1000, 1420]; v = [2.8, 2.7]
    # BLS bar (starts at "rose", 3.92), Zillow bar (starts at "rose", 8.21)
    grow(bx[0] - 150, base, bx[1] - bx[0] + 300, 6, INK, 2.4, 0.6, 'right', T1, ow=1, radius=2, layer=7)
    text('U.S. official rent index (BLS)', bx[0], 422, 26, 2.39, T1, font='sans')
    grow(bx[0] - bw / 2, base - maxh, bw, maxh, OLIVE, 3.9, 1.3, 'up', T1)
    counter(2.8, bx[0], 135, 88, 4.28, 1.0, T1, color=OLIVE)
    text('Zillow typical rent', bx[1], 422, 26, 5.47, T1, font='sans')
    h2 = maxh * 2.7 / 2.8
    grow(bx[1] - bw / 2, base - h2, bw, h2, CORAL, 8.2, 1.1, 'up', T1)
    counter(2.7, bx[1], 135, 88, 8.51, 0.9, T1, color=CORAL)
    text('≈', 1210, 270, 120, 14.32, T1, color=INK, enter='pop')
    text('almost the', 1210, 335, 26, 14.9, T1, font='sans', color=GREYTXT)
    text('same answer', 1210, 365, 26, 15.0, T1, font='sans', color=GREYTXT)
    source(['Source: BLS CPI release, Oct 14, 2026, Table 1 (rent, 12-mo change).',
            'Source: Zillow Group release, Oct 6, 2026 (typical U.S. rent, 12-mo).'], 2.4, T1)

    # ===== SH2 question 16.4-32.4 =====
    T2 = 32.4
    text('Both say about 3%.', 1200, 150, 64, 16.6, 22.4)
    text('Why does rent feel bigger?', 1200, 270, 72, 17.93, 22.4, color=CORAL, enter='pop')
    text('They answer a different question', 1200, 190, 62, 22.6, 27.3)
    text('from the one you are asking.', 1200, 275, 62, 24.87, 27.3, color=CORAL)
    text('This video:', 1200, 130, 34, 27.54, T2, font='sans', color=GREYTXT)
    text('what a rent number measures,', 1200, 215, 58, 28.4, T2)
    text('and what it leaves out.', 1200, 300, 58, 30.5, T2, color=CORAL)

    # ===== SH3 CPI 32.6-39.7 =====
    T3 = 39.8
    text('Consumer Price Index (CPI)', 1200, 105, 58, 33.0, T3, enter='pop')
    text('published every month by the Bureau of Labor Statistics', 1200, 170, 32, 33.2, T3, font='sans', color=GREYTXT)
    tile_w, tile_h, gap = 150, 120, 28; tx0 = 1200 - (7 * tile_w + 6 * gap) / 2
    for i in range(7):
        x0 = tx0 + i * (tile_w + gap)
        grow(x0, 245, tile_w, tile_h, GREY, 35.4 + i * 0.12, 0.35, 'up', T3, radius=18, ow=3, layer=8)
    rx0 = tx0 + 3 * (tile_w + gap)
    grow(rx0, 245, tile_w, tile_h, CORAL, 38.0, 0.35, 'up', T3, radius=18, ow=4, layer=9)
    text('Rent', rx0 + tile_w / 2, 305, 40, 38.1, T3, color=(255, 255, 255), layer=12)
    text('one piece of the CPI basket', 1200, 410, 30, 38.4, T3, font='sans', color=GREYTXT)
    source(['Source: BLS Consumer Price Index release, Oct 14, 2026.'], 33.0, T3, y0=506)

    # ===== SH4 weights 39.9-75.0 =====
    BX, BW_, BY, BH = CX0 + 60, 1200, 185, 100    # bar frame
    pct = lambda p: BW_ * p / 100.0
    rent, oer, shel = 7.728, 25.902, 35.323
    oth = shel - rent - oer
    text('What the CPI is made of (relative importance, August 2026)', 1200, 68, 32, 39.95, None, font='sans', color=GREYTXT)
    grow(BX, BY, BW_, BH, GREY, 40.4, 1.0, 'right', layer=7)            # whole CPI
    text('The whole index', BX + BW_ - 150, 312, 28, 40.9, None, font='sans', color=GREYTXT)
    grow(BX, BY, pct(rent), BH, CORAL, 44.4, 0.9, 'right', layer=9)    # rent of primary residence
    text('Rent of primary residence', BX, 110, 28, 44.0, None, font='sans', left=True)
    counter(7.7, BX, 150, 56, 46.4, 0.8, None, color=CORAL, left_w=tw('7.7%', 56))
    grow(BX + pct(rent), BY, pct(oer), BH, OLIVE, 49.4, 1.0, 'right', layer=9)  # OER
    ocx = BX + pct(rent) + pct(oer) / 2
    text("Owners' equivalent rent", ocx, 312, 28, 49.6, None, font='sans')
    counter(25.9, ocx, 352, 56, 53.1, 0.8, None, color=OLIVE)
    grow(BX + pct(rent) + pct(oer), BY, pct(oth), BH, OLIVE_L, 56.5, 0.8, 'right', layer=9)  # smaller shelter items
    bl, br = BX, BX + pct(shel)
    grow(bl, 386, br - bl, 8, INK, 59.5, 0.8, 'right', layer=9, ow=1, radius=3)
    text('Shelter', 880 - 100, 430, 44, 59.6, None, enter='fade')
    counter(35.3, 880 + 30, 430, 52, 60.26, 1.0, None, color=INK, left_w=tw('35.3%', 56))
    box(BX - 5, BY - 5, pct(shel) + 10, BH + 10, CORAL, 63.9, 70.2, ow=8)
    text('About one third of the index', 1480, 405, 38, 66.6, 70.3, color=CORAL)
    text('Slow rent, slow headline inflation', 1480, 405, 36, 70.5, None, color=CORAL)
    source(['Source: BLS CPI release, Oct 14, 2026, Table 1 (Aug 2026 weights).',
            'Light sliver (about 1.7%) = other shelter items, derived: 35.3 \u2212 7.7 \u2212 25.9.'], 40.2, None, y0=488)

    spec = dict(w=1920, h=1080, fps=FPS, motion_fps=FPS, bg=list(CREAM), shots=[dict(start=0, dur=DUR, elements=els)])
    return spec, words


def main():
    out = HERE + '/out/V1_RENT_segment_0-75s_take2.mp4'
    if '--out' in sys.argv: out = sys.argv[sys.argv.index('--out') + 1]
    assert hashlib.sha256(open(WAV, 'rb').read()).hexdigest() == WAV_SHA, 'audio checksum mismatch'
    spec, words = build(); json.dump(spec, open(HERE + '/spec/seg_0_75_spec.json', 'w'), indent=1)
    errs = rs.validate(spec)
    if errs: raise SystemExit('VALIDATION FAILED\n' + '\n'.join(errs))
    if '--spec-only' in sys.argv: return
    if '--still' in sys.argv:   # --still T1,T2,... writes out/stills/t_<T>.png
        os.makedirs(HERE + '/out/stills', exist_ok=True)
        for ts in sys.argv[sys.argv.index('--still') + 1].split(','):
            rs.comp_shot(spec, spec['shots'][0], float(ts)).convert('RGB').save(HERE + '/out/stills/t_%s.png' % ts)
        return
    total = round(DUR * FPS)
    if '--frames' in sys.argv: total = min(total, int(sys.argv[sys.argv.index('--frames') + 1]))
    start = int(sys.argv[sys.argv.index('--start') + 1]) if '--start' in sys.argv else 0
    cmd = ['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', str(FPS), '-i', '-',
           '-ss', '%.3f' % (start / FPS), '-t', '%.3f' % (total / FPS), '-i', WAV,
           '-map', '0:v', '-map', '1:a', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
           '-af', 'aresample=48000,afade=t=out:st=%.3f:d=0.3' % max(0, (total - start) / FPS - 0.3), '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    shot = spec['shots'][0]
    for f in range(start, total):
        t = f / FPS
        im = rs.comp_shot(spec, shot, t).convert('RGB'); p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
    print('rendered frames', start, '->', total, out)

if __name__ == '__main__': main()
