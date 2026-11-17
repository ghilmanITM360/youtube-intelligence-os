#!/usr/bin/env python3
"""WI-0081 video v1: Codex GEN art + code layout/animation, timed to the supplied 98.3 s voiceover.
xkcd lens: white plate, 1-frame pops, 6-frame linear dissolves, no overshoot. Usage: build_video.py [still t1 t2 ...] | [render]"""
from pathlib import Path
import csv, subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont
R = Path(__file__).resolve().parents[1]; V = R/'video'
W, H, FPS, DUR = 1080, 1920, 24, 98.33
RED, INK, GREY = '#D7263D', '#111111', '#C4C4C4'
# best attempt per id (owner delegated the choice); overrides beat review_selection.csv
sel = {r['asset_id']: r['filename'] for r in csv.DictReader((R/'assets/qa/review_selection.csv').open())}
sel.update({'CHR-P04': 'assets/gen/CHR-P04-v7.png', 'CHR-P11': 'assets/gen/CHR-P11-v7.png', 'THM-02': 'assets/gen/THM-02-v4.png',
            'THR-01': 'assets/gen/THR-01-v4.png', 'WTR-04': 'assets/gen/WTR-04.png'})
_c = {}
def raw(i):
    if i not in _c: _c[i] = Image.open(R/sel[i]).convert('RGBA')
    return _c[i]
def crop(i):
    k = 'c'+i
    if k not in _c:
        a = raw(i)
        if i == 'MUG-01':   # near-white interior becomes transparent so the code water fill shows through
            bg = Image.new('RGBA', a.size, 'white'); bg.alpha_composite(a); lum = bg.convert('L').point(lambda v: 0 if v > 235 else 255)
            a = a.copy(); a.putalpha(Image.composite(a.getchannel('A'), Image.new('L', a.size, 0), lum))
        b = a.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox(); _c[k] = a.crop(b) if b else a
    return _c[k]
def fit(img, w=None, h=None):
    s = (h/img.height) if h else (w/img.width)
    return img.resize((max(1, round(img.width*s)), max(1, round(img.height*s))), Image.LANCZOS)
def put(im, img, cx, cy):  # centre placement
    im.alpha_composite(img, (round(cx-img.width/2), round(cy-img.height/2)))
def art(im, i, cx, cy, h=None, w=None): put(im, fit(crop(i), w=w, h=h), cx, cy)
FONT = '/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf'
def F(s): return ImageFont.truetype(FONT, s)
def T(im, s, cx, y, size=64, col=INK, anchor='mt'):
    ImageDraw.Draw(im).text((cx, y), s, font=F(size), fill=col, anchor=anchor, align='center')
def on(t, t0, t1=1e9): return t0 <= t < t1
def lin(t, t0, t1, a, b): return a + (b-a)*min(1, max(0, (t-t0)/(t1-t0)))
def step(t, t0, dt=.25): return int((t-t0)/dt) if t >= t0 else -1   # stepped motion (no easing)

# ---- characters: poses share one head-anchored 1536 canvas, so a pose swap never moves the head
def alien(im, pose, cx=250, feet=1790, s=.62):
    a = raw(pose); b = fit(a, w=round(1536*s)); im.alpha_composite(b, (round(cx-768*s), round(feet-1102*s)))

# ---- mug with flat water fill, built from MUG-01 line art (code water, grey #C4C4C4)
def interior(mug, y_water):
    lum = Image.new('L', mug.size, 255); bg = Image.new('RGBA', mug.size, 'white'); bg.alpha_composite(mug)
    g = bg.convert('L').point(lambda v: 0 if v < 200 else 255)
    m = Image.new('L', mug.size, 0); ImageDraw.Draw(m).rectangle((0, y_water, mug.width, mug.height), fill=255)
    g = Image.composite(g, Image.new('L', mug.size, 0), m)          # rows above the waterline are walls
    ImageDraw.floodfill(g, (int(mug.width*.42), int(y_water+(mug.height-y_water)*.4)), 128)
    return g.point(lambda v: 255 if v == 128 else 0)
def mug_scene(im, cx, cy, h=520, level=.42, spoon=0, angle=0, swirl=False, steam=False):
    mug = fit(crop('MUG-01'), h=h); x0, y0 = round(cx-mug.width/2), round(cy-mug.height/2)
    yw = round(mug.height*(1-level)); fill = Image.new('RGBA', mug.size, GREY); fill.putalpha(interior(mug, yw))
    im.alpha_composite(fill, (x0, y0))
    if swirl:
        d = ImageDraw.Draw(im); k = step(swirl, 0, .25) % 3
        for j in range(3):
            w = int(mug.width*(.34-.07*j)); yy = y0+yw+34+j*38; xs = x0+int(mug.width*.5)-w//2+(k*14 if j % 2 else -k*14)
            d.arc((xs, yy, xs+w, yy+24), 200, 340, fill=INK, width=6)
    if spoon:
        sp = fit(crop('SPN-01'), h=round(h*1.22)); pv = (sp.width//2, sp.height-4)            # pivot = bowl end
        lay = Image.new('RGBA', (sp.width*6, sp.height*2), (0, 0, 0, 0)); ox, oy = sp.width*3-pv[0], sp.height-pv[1]
        lay.alpha_composite(sp, (ox, oy)); lay = lay.rotate(-angle, center=(sp.width*3, sp.height), resample=Image.BICUBIC)
        px, py = cx+int(mug.width*.03), y0+mug.height-int(mug.height*.12)
        im.alpha_composite(lay, (px-sp.width*3, py-sp.height))
    im.alpha_composite(mug, (x0, y0))
    return x0, y0, mug.width, mug.height, yw
GAUGE = {}
def gauge(im, cx, cy, h, deg):             # THM-01 dial + THM-02 needle rotated about its hub
    d = fit(crop('THM-01'), h=h); put(im, d, cx, cy)
    n = crop('THM-02'); ys, xs = [], []
    hub = (n.width-3, n.height//2)                                        # hub = right end of the needle prop
    L = d.width*.34; s = L/n.width; n2 = fit(n, w=round(n.width*s)); pv = (n2.width-3, n2.height//2)
    lay = Image.new('RGBA', (n2.width*4, n2.width*4), (0, 0, 0, 0)); c = n2.width*2
    lay.alpha_composite(n2, (c-pv[0], c-pv[1]))
    lay = lay.rotate(-(deg-270), center=(c, c), resample=Image.BICUBIC)   # prop points left (=270 deg from up)
    im.alpha_composite(lay, (round(cx-c), round(cy-d.height*.20-c)))
NEEDLE_20 = -81
# ---- generic bits
def pop_text(im, t, t0, s, cx, y, size=70, col=INK):
    if on(t, t0): T(im, s, cx, y, size, col)
def ruler_w(im, t, t0, x=130, top=420, bot=1120):                 # persistent watt ruler (VEC): 0..1000 W
    if not on(t, t0): return
    d = ImageDraw.Draw(im); d.line((x, top, x, bot), fill=INK, width=8)
    for k in range(11):
        y = bot-(bot-top)*k/10; d.line((x, y, x+(36 if k % 5 == 0 else 22), y), fill=INK, width=8)
    T(im, 'W', x, top-80, 56, INK); T(im, '0', x+66, bot-16, 38); T(im, '500', x+84, (top+bot)//2-18, 38); T(im, '1000', x+98, top-16, 38)
def y_of_w(w, top=420, bot=1120): return bot-(bot-top)*w/1000

# ---- scenes: f(t) -> RGBA frame
def S1(t):  # 0.0-7.9 hook
    im = Image.new('RGBA', (W, H), 'white'); mug_scene(im, 540, 760, 520, .42, spoon=1, angle=-6)
    gauge(im, 880, 1080, 300, NEEDLE_20); alien(im, 'CHR-P01'); T(im, '20 °C', 880, 1260, 52)
    if on(t, .2): T(im, 'BOIL BY STIRRING?', 540, 130, 80)
    if on(t, 2.6):
        d = ImageDraw.Draw(im); d.line((110, 170, 470, 180), fill=RED, width=10)
    if on(t, 4.3): T(im, 'NO.', 880, 380, 130, RED)
    if on(t, 5.6): mug_scene(im, 540, 760, 520, .42, spoon=1, angle=(-1)**step(t, 5.6, .25)*14, swirl=t)
    return im
def S2(t):  # 7.9-18.6 energy -> heat
    im = Image.new('RGBA', (W, H), 'white'); a = (-1)**step(t, 7.9, .25)*14 if t < 17 else -6
    mug_scene(im, 540, 700, 520, .42, spoon=1, angle=a, swirl=t if t < 17 else 0); alien(im, 'CHR-P04')
    T(im, 'STIRRING ADDS ENERGY', 540, 130, 64)
    if on(t, 12.8, 17.0):
        art(im, 'HEAT-01', 520, 620, h=150); T(im, 'MOTION INTO HEAT', 700, 1010, 60, RED)
    if on(t, 15.8): T(im, 'SO THE IDEA IS SOUND…', 700, 1110, 52)
    if on(t, 17.4): T(im, '…THE AMOUNT IS NOT.', 700, 1200, 52, RED)
    gauge(im, 900, 1300, 260, NEEDLE_20+(3 if on(t, 15.1) else 0)); return im
def S3(t):  # 18.6-27.8 the 80-degree gap
    im = Image.new('RGBA', (W, H), 'white'); alien(im, 'CHR-P11', cx=300)
    art(im, 'JUG-01', 360, 760, h=400); art(im, 'THR-01', 760, 900, h=1000)
    T(im, '¼ LITER', 360, 1000, 56)
    if on(t, 20.7): T(im, '20 °C', 930, 1190, 64)
    if on(t, 22.5): T(im, '100 °C', 930, 380, 64)
    if on(t, 24.2):
        d = ImageDraw.Draw(im); d.line((640, 470, 640, 1120), fill=RED, width=10)
        for y in (470, 1120): d.line((620, y, 660, y), fill=RED, width=10)
        T(im, '80°', 560, 770, 80, RED)
    if on(t, 25.2): T(im, '84,000 J', 540, 190, 110, RED)
    return im
def S4(t):  # 27.8-31.4 power over two minutes
    im = Image.new('RGBA', (W, H), 'white'); ruler_w(im, t, 28.9, 180)
    art(im, 'CLK-01', 660, 1020, h=420); T(im, 'IN 2 MINUTES', 660, 770, 64)
    if on(t, 29.7):
        d = ImageDraw.Draw(im); y = y_of_w(700); d.ellipse((120, y-34, 240, y+34), outline=RED, width=9); T(im, '700 W', 520, int(y)-110, 90, RED)
    alien(im, 'CHR-P01'); return im
def S5(t):  # 31.4-34.4 bulbs
    im = Image.new('RGBA', (W, H), 'white'); ruler_w(im, t, 0, 180)
    d = ImageDraw.Draw(im); y = y_of_w(700); d.ellipse((120, y-34, 240, y+34), outline=RED, width=9)
    n = max(0, min(7, int((t-31.6)/.25)+1)) if t >= 31.6 else 0
    for k in range(n): art(im, 'BLB-01', 480+(k % 4)*150, 520+(k//4)*210, h=190)
    if n: T(im, '100 W', 480, 760+210*0-30, 40) if False else None
    if on(t, 32.3): T(im, '7 × 100 W', 640, 1010, 84, RED)
    alien(im, 'CHR-P01'); return im
def S6(t):  # 34.4-36.7 microwave
    im = Image.new('RGBA', (W, H), 'white'); ruler_w(im, t, 0, 180); y = y_of_w(700)
    ImageDraw.Draw(im).ellipse((120, y-34, 240, y+34), outline=RED, width=9)
    art(im, 'MWV-01', 640, y, w=640); T(im, 'ABOUT A MICROWAVE', 620, 330, 62); alien(im, 'CHR-P01'); return im
def S7(t):  # 36.7-39.3 horse
    im = Image.new('RGBA', (W, H), 'white'); ruler_w(im, t, 0, 180); y = y_of_w(700)
    ImageDraw.Draw(im).ellipse((120, y-34, 240, y+34), outline=RED, width=9)
    art(im, 'HRS-01', 640, y+10, w=640)
    if on(t, 38.1): T(im, '≈ 1 HORSEPOWER', 620, 1210, 74, RED)
    alien(im, 'CHR-P01'); return im
def S8(t):  # 39.3-45.7 Niagara
    im = Image.new('RGBA', (W, H), 'white'); art(im, 'NIA-03', 540, 760, w=1000)
    T(im, 'NIAGARA FALLS', 540, 190, 76)
    if on(t, 44.1): T(im, '+0.1 °C', 700, 1060, 110, RED)
    alien(im, 'CHR-P01'); return im
def S9(t):  # 45.7-54.6 spoon is tiny
    im = Image.new('RGBA', (W, H), 'white'); ruler_w(im, t, 0, 180); y0 = y_of_w(700)
    a = (-1)**step(t, 45.7, .25)*14
    mug_scene(im, 780, 900, 380, .42, spoon=1, angle=a, swirl=t); T(im, 'A HARD STIR', 640, 150, 66)
    if on(t, 47.7): ImageDraw.Draw(im).ellipse((172, y_of_w(1)-12, 196, y_of_w(1)+12), fill=INK); T(im, 'UNDER 1 W', 380, int(y_of_w(1))-150, 50, RED)
    if on(t, 49.8): art(im, 'BLB-01', 800, 400, h=190); T(im, '1/100 OF ONE BULB', 800, 510, 38)
    if on(t, 51.5): ImageDraw.Draw(im).ellipse((120, y0-34, 240, y0+34), outline=RED, width=9); T(im, '700 NEEDED', 470, int(y0)-120, 62, RED)
    alien(im, 'CHR-P01'); return im
def S10(t):  # 54.6-60.4 heat in = heat out
    im = Image.new('RGBA', (W, H), 'white'); a = (-1)**step(t, 54.6, .25)*14
    mug_scene(im, 540, 900, 560, .42, spoon=1, angle=a, swirl=t)
    art(im, 'HLS-03', 180, 760, h=130); T(im, 'SPOON IN', 180, 640, 46, RED)
    art(im, 'HLS-01', 790, 560, h=230); T(im, 'HEAT OUT', 820, 400, 50, RED)
    gauge(im, 900, 1230, 250, NEEDLE_20+(4 if on(t, 55.4) else 0)); T(im, 'SAME', 540, 1220, 70)
    alien(im, 'CHR-P04'); return im
def S11(t):  # 60.4-66.1 fast
    im = Image.new('RGBA', (W, H), 'white'); T(im, 'FAR FASTER THAN ANY HAND', 540, 230, 64)
    sp = fit(crop('SPN-04'), h=760);
    for k in range(3 if on(t, 61.2) else 0): im.alpha_composite(Image.eval(sp, lambda v: v//3) if False else sp, (540-sp.width//2-50*k+(0 if k == 0 else 0)-30, 480))
    if on(t, 63.0): T(im, 'TENS OF THOUSANDS', 720, 1300, 54, RED); T(im, 'OF STROKES A SECOND', 720, 1370, 54, RED)
    alien(im, 'CHR-P06'); return im
def S12(t):  # 66.1-71.2 cavitation
    im = Image.new('RGBA', (W, H), 'white'); art(im, 'CAV-02', 540, 760, w=960)
    if on(t, 67.2): T(im, 'CAVITATION', 540, 230, 84, RED)
    if on(t, 68.0): T(im, 'LOW PRESSURE BEHIND THE SPOON', 540, 1080, 52)
    if on(t, 70.3): T(im, 'VAPOR BUBBLES', 540, 1160, 60)
    alien(im, 'CHR-P01'); return im
def S13(t):  # 71.2-75.0 not boiling
    im = Image.new('RGBA', (W, H), 'white'); art(im, 'CAV-03', 560, 720, w=760); T(im, 'LOOKS LIKE BOILING…', 540, 230, 64)
    if on(t, 73.1): T(im, 'BUT IT’S PRESSURE, NOT HEAT', 540, 1080, 56, RED)
    if on(t, 73.1):
        d = ImageDraw.Draw(im); d.line((350, 820, 700, 1000), fill=RED, width=12); d.line((700, 820, 350, 1000), fill=RED, width=12)
    alien(im, 'CHR-P01'); return im
def S14(t):  # 75.0-79.3 splash cools
    im = Image.new('RGBA', (W, H), 'white'); art(im, 'WTR-04', 540, 700, w=900); T(im, 'SPLASHING SPREADS THE WATER', 540, 200, 56)
    if on(t, 76.8): art(im, 'HLS-02', 540, 1130, w=700); T(im, 'COOLS EVEN FASTER', 540, 1330, 66, RED)
    alien(im, 'CHR-P01'); return im
def S15(t):  # 79.3-86.0 measured tea
    im = Image.new('RGBA', (W, H), 'white'); T(im, 'SOMEONE MEASURED TEA', 540, 210, 66); art(im, 'MUG-R01', 540, 620, w=1000)
    for s, t0, x in (('STIR', 81.2, 220), ('DIP', 81.8, 540), ('NOTHING', 83.0, 860)):
        if on(t, t0): T(im, s, x, 800, 54)
    if on(t, 84.0):
        art(im, 'CHT-01', 540, 1180, w=560); T(im, 'ALL COOL ABOUT THE SAME', 540, 1450, 56, RED); T(im, '(illustrative)', 540, 1530, 38, '#848484')
    return im
def S16(t):  # 86.0-93.1 verdict
    im = Image.new('RGBA', (W, H), 'white'); mug_scene(im, 540, 840, 560, .42, spoon=1, angle=-6)
    gauge(im, 900, 1090, 280, NEEDLE_20 if t < 91.3 else NEEDLE_20+2)
    if on(t, 86.0): T(im, 'ORDINARY SPOON, OPEN CUP?', 540, 220, 56)
    if on(t, 88.3): T(im, 'NO.', 560, 1180, 140, RED)
    if on(t, 89.6): T(im, '≈ 20 °C', 900, 1260, 56)
    alien(im, 'CHR-P12' if on(t, 88.3) else 'CHR-P01'); return im
def S17(t):  # 93.1-98.33 sugar, hold
    im = Image.new('RGBA', (W, H), 'white'); mug_scene(im, 540, 840, 560, .42, spoon=1, angle=-6 if t < 93.9 else (-1)**step(t, 93.9, .25)*14, swirl=t if t > 93.9 else 0)
    x0, y0, mw, mh, yw = 214, 560, 653, 560, 325            # geometry of mug_scene(540, 840, h=560)
    surf = y0+yw; ft = .5; tt = t-93.6                                    # cube falls under gravity (y = y0 + g t^2/2), then sinks and dissolves
    if 0 <= tt < ft: art(im, 'SUG-01', 470, 330+(surf-330-50)*(tt/ft)**2, h=90)
    elif ft <= tt < ft+.7: art(im, 'SUG-01', 470, surf+30+130*(tt-ft)/.7, h=90)
    elif tt < ft+1.4: art(im, 'SUG-02', 470, surf+190, h=110)
    elif tt < ft+2.2: art(im, 'SUG-03', 470, surf+170, h=130)
    T(im, 'A SPOON IS FOR SUGAR.', 540, 210, 70)
    if on(t, 96.1): T(im, 'NOT BOILING.', 540, 1230, 70, RED)
    alien(im, 'CHR-P13' if t < 96.1 else 'CHR-P01'); return im
SC = [(0, S1), (7.9, S2), (18.6, S3), (27.8, S4), (31.4, S5), (34.4, S6), (36.7, S7), (39.3, S8), (45.7, S9), (54.6, S10), (60.4, S11),
      (66.1, S12), (71.2, S13), (75.0, S14), (79.3, S15), (86.0, S16), (93.1, S17), (DUR+1, None)]
DIS = 6/FPS
def frame(t):
    for i in range(len(SC)-1):
        s0, f = SC[i]; s1 = SC[i+1][0]
        if s0 <= t < s1:
            im = f(t)
            if i and t < s0+DIS:                                     # 6-frame linear dissolve from the previous scene's last frame
                prev = SC[i-1][1](s0-1/FPS); im = Image.blend(prev, im, (t-s0+1/FPS)/DIS)
            return im.convert('RGB')
def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'still':
        ts = [float(x) for x in sys.argv[2:]]; ims = [frame(t) for t in ts]; cols = min(4, len(ims)); rows = (len(ims)+cols-1)//cols
        sh = Image.new('RGB', (cols*360, rows*660), 'white'); d = ImageDraw.Draw(sh)
        for i, (t, im) in enumerate(zip(ts, ims)):
            th = im.resize((360, 640)); sh.paste(th, ((i % cols)*360, (i//cols)*660+20)); d.text(((i % cols)*360+4, (i//cols)*660+2), f't={t}', fill='red')
        sh.save(V/'stills.png'); return
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-i', str(R/'audio/WI0081_voiceover_user_generated_98s.wav'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                          '-c:a', 'aac', '-b:a', '160k', '-shortest', str(V/'WI0081_video_v1.mp4')], stdin=subprocess.PIPE)
    for n in range(round(DUR*FPS)): p.stdin.write(frame(n/FPS).tobytes())
    p.stdin.close(); p.wait()
if __name__ == '__main__': main()
