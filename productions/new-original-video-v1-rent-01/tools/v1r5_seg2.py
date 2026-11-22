"""V1 Rent segment 2 (75.0-122.3 s): the BLS rent method (S016-S028). Same grammar/engine as R4 (tools/v1r4_render.py).
  python3 tools/v1r5_seg2.py --still 77,81 | --storyboard | --out out_r5/V1_RENT_R5_75-122s.mp4
Facts: BLS factsheet 'Owners' equivalent rent and rent' (claim register C-07..C-09, SEGMENT_75_122_CLAIM_REGISTER.md). No figure is invented: no example numbers."""
import os, sys, math, hashlib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1r4_render as r
from v1r4_render import *
T0, T1 = 75.0, 122.3
r.BEATS = []
SRC = ["Source: BLS factsheet:", "Owners' equivalent rent and rent"]
BL = (70, 140, 190)

def mini_house(x, y, w, col, t0, seed=1, mode='pop'):
    def f(_):
        h = int(w * 0.85); im = layer(w + 40, h + 40); d = ImageDraw.Draw(im); o = 20
        body = [(o + w * .1, o + h * .45), (o + w * .1, o + h), (o + w * .9, o + h), (o + w * .9, o + h * .45)]
        d.polygon([(a * S2, b * S2) for a, b in body + [(o + w * .5, o + h * .08)]], fill=col + (255,))
        poly(d, [(o, o + h * .5), (o + w * .5, o + h * .05), (o + w, o + h * .5)], 7, INK, seed, 2, ox=0, oy=0)
        poly(d, body + [body[0]], 7, INK, seed + 1, 2)
        d.rectangle([(o + w * .42) * S2, (o + h * .65) * S2, (o + w * .58) * S2, (o + h) * S2], fill=PAPER + (255,)); poly(d, [(o + w * .42, o + h), (o + w * .42, o + h * .65), (o + w * .58, o + h * .65), (o + w * .58, o + h)], 5, INK, seed + 2, 1)
        return done(im), x - w / 2 - 20, y - h / 2 - 20
    return It(t0, f, mode)

def paper(x, y, w, h, word, t0, col=INK, size=90, mode='pop', seed=3):
    def f(_):
        im = layer(w + 60, h + 60); d = ImageDraw.Draw(im); pts = [(30, 30), (30 + w, 30), (30 + w, 30 + h), (30, 30 + h), (30, 30)]; p = wob(pts, 3, seed, 14); p[-1] = p[0]; pp = [(a * S2, b * S2) for a, b in p]
        d.polygon(pp, fill=PAPER + (255,)); d.line(pp, fill=INK + (255,), width=8 * S2, joint='curve')
        d.text((60 * S2, 55 * S2), word, font=font('wide', size * S2), fill=col + (255,))
        for i in range(max(2, (h - 190) // 40)): poly(d, [(60, 190 + i * 40), (w - 40 - (i % 3) * 50, 190 + i * 40)], 6, GREYT, seed + i, 1.5)
        return done(im), x - w / 2 - 30, y - h / 2 - 30
    return It(t0, f, mode)

def chip(x, y, w, h, text, fill, t0, size=70, tcol=INK, seed=5, mode='pop', kind='hand'):
    return [rect(x - w // 2, y - h // 2, w, h, fill, t0, 7, seed, mode=mode), txt(text, x, y, size, tcol, t0, kind, mode=mode)]

def build():
    PRE = -1.0
    # 1 method intro 75.0-79.9
    b = B(75.0, 79.9, 'Hero host; "The method" title', "Here is the method, from the BLS's own explanation of how it measures rent.")
    b.add(host([(75.0, 'down', 'smile')], 470, 1010, 0.46), txt('The method', 1330, 330, 150, INK, 75.3, 'wide'), txt('straight from the BLS', 1330, 480, 80, GREYT, 76.1), txt('how it measures rent', 1330, 600, 90, RED, 77.8), *source(SRC, 76.3, False))
    # 2 not every apartment 79.9-82.4
    grid = [(790 + c * 270, 250 + rr * 190) for rr in range(3) for c in range(4)]
    b = B(79.9, 82.4, 'Grid of 12 small houses; "Not every apartment"', 'The BLS does not look at every apartment.')
    b.add(*[mini_house(x, y, 190, GREYF, 80.0 + i * 0.07, 40 + i) for i, (x, y) in enumerate(grid)], txt('Not every apartment', 1260, 830, 110, RED, 80.9, 'wide'), txt('illustration, not to scale', 1500, 945, 50, GREYT, 80.0), *source(SRC, 80.0))
    # 3 a sample 82.4-84.7
    pick = [2, 6, 11]
    b = B(82.4, 84.7, 'Same grid; a few houses turn blue = the sample', 'It takes a sample of rental units.')
    b.add(*[mini_house(x, y, 190, BL if i in pick else GREYF, (82.9 + 0.12 * pick.index(i)) if i in pick else PRE, 40 + i) for i, (x, y) in enumerate(grid)], txt('a sample', 1260, 830, 120, BL, 82.8, 'wide'), txt('illustration, not to scale', 1500, 945, 50, GREYT, PRE), *source(SRC, PRE))
    # 4 priced every six months 84.7-87.3
    b = B(84.7, 87.3, 'Host point; sampled house + price tag + "every 6 months"', 'Each sampled unit is priced every six months')
    b.add(host([(84.7, 'point', 'neutral')], 330, 1010, 0.34), mini_house(1000, 480, 330, BL, 85.0, 60), *chip(1000, 740, 260, 100, 'price', ORANGE, 85.4, 64, INK, 61),
          txt('every 6 months', 1560, 470, 120, RED, 86.2, 'wide'), arrow(1230, 420, 1330, 420, 86.4), *source(SRC, PRE, False))
    # 5 lease 87.3-90.1
    b = B(87.3, 90.1, 'Lease document; "fixes the rent for a term"', 'because a lease fixes the rent for a term.')
    b.add(paper(760, 520, 400, 520, 'LEASE', 87.4, INK, 100, seed=70), txt('fixes the rent', 1380, 380, 110, INK, 87.9, 'wide'), txt('for a term', 1380, 540, 130, RED, 88.9, 'wide'), *source(SRC, PRE))
    # 6 six panels 90.1-93.3
    b = B(90.1, 93.3, 'Six panel boxes (3x2)', 'The sample is split into six groups, called panels.')
    px = [(620 + c * 340, 400 + rr * 270) for rr in range(2) for c in range(3)]
    b.add(txt('The sample, split into six', 960, 160, 80, GREYT, 90.3), *[x for i, (cx, cy) in enumerate(px) for x in chip(cx, cy, 300, 200, 'Panel %d' % (i + 1), BL if i == 0 else GREYF, 91.2 + i * 0.2, 64, INK, 80 + i)], txt('PANELS', 960, 890, 150, RED, 92.4, 'wide'), *source(SRC, PRE))
    # 7 panel 1: Jan and Jul 93.3-96.8
    ROWY = [380, 540, 700]; LX, C1, C2 = 760, 1190, 1540
    b = B(93.3, 96.8, 'Panel 1 row: January and July, with a 6-month arrow', 'One panel is priced in January and again in July.')
    b.add(*chip(LX, ROWY[0], 300, 120, 'Panel 1', BL, 93.5, 70, INK, 90), *chip(C1, ROWY[0], 250, 120, 'January', ORANGE, 94.5, 66, INK, 91), *chip(C2, ROWY[0], 250, 120, 'July', ORANGE, 95.8, 66, INK, 92),
          arrow(C1 + 140, ROWY[0], C2 - 140, ROWY[0], 95.4), txt('priced', 1190, 235, 70, GREYT, 94.0), *source(SRC, PRE))
    # 8 panel 2 + so on 96.8-99.5
    b = B(96.8, 99.5, 'Table: Panel 1 Jan/Jul, Panel 2 Feb/Aug, "and so on"', 'The next in February and August and so on.')
    b.add(*chip(LX, ROWY[0], 300, 120, 'Panel 1', BL, PRE, 70, INK, 90), *chip(C1, ROWY[0], 250, 120, 'January', ORANGE, PRE, 66, INK, 91), *chip(C2, ROWY[0], 250, 120, 'July', ORANGE, PRE, 66, INK, 92),
          *chip(LX, ROWY[1], 300, 120, 'Panel 2', BL, 96.9, 70, INK, 93), *chip(C1, ROWY[1], 250, 120, 'February', ORANGE, 97.2, 66, INK, 94), *chip(C2, ROWY[1], 250, 120, 'August', ORANGE, 98.0, 66, INK, 95),
          txt('and so on', 1100, 720, 100, GREYT, 98.7), *source(SRC, PRE))
    # 9a stepping months 99.5-101.4
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    def stepper(tq):
        k = min(1, max(0, int((tq - 99.6) / 0.5))); im = layer(1300, 420); d = ImageDraw.Draw(im)
        for i in range(6):
            x0 = 20 + i * 200; col = ORANGE if i == k else GREYF
            d.rounded_rectangle([x0 * S2, 150 * S2, (x0 + 185) * S2, (150 + 150) * S2], radius=18 * S2, fill=col + (255,), outline=INK + (255,), width=7 * S2)
        im = done(im); d2 = ImageDraw.Draw(im); d2.text((20 + k * 200 + 92 - font('num', 56).getlength('Panel %d' % (k + 1)) / 2, 208), 'Panel %d' % (k + 1), font=font('num', 56), fill=INK + (255,))
        d2.text((650 - font('wide', 130).getlength(months[k]) / 2, 0), months[k], font=font('wide', 130), fill=RED + (255,))
        return im, 310, 380
    b = B(99.5, 100.6, 'Month steps Jan->Feb; a different panel lights each month', 'So, every month,')
    b.add(dyn(99.5, stepper), txt('every month', 960, 230, 90, INK, 99.7), *source(SRC, PRE))
    # 9b one-sixth 101.4-103.6
    b = B(100.6, 103.6, '"1/6" big + "gets a new price"', 'one-sixth of the sample gets a new price.')
    b.add(txt('1/6', 960, 380, 330, RED, 100.7, 'num'), txt('of the sample', 960, 600, 100, INK, 101.6), *chip(960, 800, 520, 130, 'gets a new price', ORANGE, 102.2, 72, INK, 99), *source(SRC, PRE))
    # 10 arithmetic 103.6-105.9
    b = B(103.6, 105.9, 'Host shrug/smirk; "The arithmetic"', 'Then comes the arithmetic.')
    b.add(host([(103.6, 'shrug', 'smirk')], 470, 1010, 0.46), txt('Then the', 1330, 380, 100, INK, 104.0), txt('arithmetic', 1330, 540, 160, RED, 104.3, 'wide'))
    # 11 formula 105.9-109.3
    RX0, RX1, RY = 1050, 1700, 470
    rad = [(RX0 - 50, RY + 90), (RX0 - 20, RY + 125), (RX0 + 30, RY - 20), (RX1, RY - 20)]
    b = B(105.9, 109.3, 'monthly change = 6th root of ratio', 'The monthly change is the sixth root of this ratio.')
    b.add(txt('monthly\nchange', 500, 520, 90, INK, 105.9), txt('=', 790, 530, 130, INK, 106.5, 'wide'), stroke_item(rad, 106.8, INK, 10, 0.35, 5, 71, 2), txt('6', RX0 - 5, RY - 60, 70, RED, 107.0, 'wide'), txt('ratio', (RX0 + RX1) / 2 + 20, 540, 130, INK, 107.9, 'wide'), *source(SRC, PRE))
    # 12 ratio definition 109.3-114.6
    b = B(109.3, 114.6, 'ratio = today avg rent in panel / avg rent of same units 6 months earlier', "Today's average rent in the panel divided by the average rent for the same units six months earlier.")
    b.add(txt('ratio', 480, 520, 130, INK, 109.3, 'wide'), txt('=', 700, 525, 120, INK, 109.4, 'wide'), txt("today's average rent\nin the panel", 1250, 370, 80, ORANGE, 109.5),
          stroke_item([(920, 545), (1600, 545)], 110.6, INK, 9, 0.3, 4, 72, 2), txt('average rent, same units,', 1250, 650, 80, INK, 111.4), txt('6 months earlier', 1250, 760, 90, RED, 113.0, 'wide'), *source(SRC, PRE))
    # 13 6-month -> 1-month 114.6-118.9
    b = B(114.6, 118.9, '6-month change -> (sixth root) -> 1-month change', 'A sixth root turns a six-month change into a one-month change.')
    b.add(txt('sixth root', 1125, 330, 100, RED, 114.8, 'wide'), arrow(960, 500, 1290, 500, 115.0, RED, 12), *chip(660, 500, 520, 170, '6-month change', GREYF, 115.4, 70, INK, 110), *chip(1590, 500, 520, 170, '1-month change', ORANGE, 116.9, 70, INK, 111), *source(SRC, PRE))
    # 14 chained 118.9-122.3
    b = B(118.9, 122.3, 'Host smile; monthly changes chained into the index', 'Those monthly changes are chained together to build the index.')
    cx = [760, 1060, 1360, 1660]
    b.add(host([(118.9, 'down', 'smile')], 330, 1010, 0.34), *[x for i, c in enumerate(cx) for x in chip(c, 400, 200, 120, ['Jan', 'Feb', 'Mar', 'Apr'][i], GREYF, 119.5 + i * 0.3, 60, INK, 120 + i)],
          *[arrow(cx[i] + 110, 400, cx[i + 1] - 110, 400, 119.8 + i * 0.3, INK, 8) for i in range(3)], txt('monthly changes, chained', 1210, 270, 80, GREYT, 119.8),
          arrow(1210, 480, 1210, 640, 120.9), *chip(1210, 740, 440, 150, 'the index', ORANGE, 121.4, 80, INK, 130, kind='wide'), *source(SRC, PRE, False))
    return r.BEATS

def main():
    a = sys.argv; beats = build()
    if '--storyboard' in a:
        t = r.storyboard(beats).replace('V1 Rent R4 storyboard (long-form grammar re-block of the 0-75 s Take 2 narration)', 'V1 Rent R5 storyboard, segment 2 (75.0-122.3 s, Take 2 S016-S028)'); open(HERE + '/STORYBOARD_R5_75-122s.md', 'w').write(t + '\n'); print('ok'); return
    od = HERE + '/out_r5'; os.makedirs(od + '/stills', exist_ok=True)
    if '--still' in a:
        for ts in a[a.index('--still') + 1].split(','): render(beats, math.floor(float(ts) * CFPS + 1e-6) / CFPS).save('%s/stills/r5_%s.png' % (od, ts))
        return
    out = a[a.index('--out') + 1] if '--out' in a else od + '/V1_RENT_R5_75-122s.mp4'; out = out if os.path.isabs(out) else HERE + '/' + out
    assert hashlib.sha256(open(WAV, 'rb').read()).hexdigest() == WAV_SHA; dur = T1 - T0; n = round(dur * FPS)
    cmd = ['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', str(FPS), '-i', '-', '-ss', '%.3f' % T0, '-t', '%.3f' % (n / FPS), '-i', WAV,
           '-map', '0:v', '-map', '1:a', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
           '-af', 'aresample=48000,afade=t=out:st=%.3f:d=0.3' % max(0, n / FPS - 0.3), '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); last = None
    for f in range(n):
        tq = math.floor((T0 + f / FPS) * CFPS + 1e-6) / CFPS
        if tq != last: im = render(beats, tq).tobytes(); last = tq
        p.stdin.write(im)
    p.stdin.close(); p.wait(); print('rendered', n, 'frames ->', out)
if __name__ == '__main__': main()
