"""Illustrated composition boards: 3 panels per beat (start / development / payoff) with annotation overlays,
assembled into one sheet per scene. Panels are the animatic's own placeholder frames, so board and animatic cannot disagree.
Run through `python3 tools/animatic.py boards`.
"""
import math, os, textwrap
from PIL import Image, ImageDraw
import animatic as A

OUT = os.path.join(A.ROOT, 'storyboard', 'panels')
PW, PH = 360, 640                     # panel size on the sheet (1/3 scale)
LEFT, RIGHT, GAP = 440, 560, 10
BG = (22, 24, 30); INK = (230, 232, 238); SUB = (150, 156, 170)

def times(b):
    t0 = b['start'] + 0.05
    t2 = min(b['end'] - 0.05, max(b['anchor'] + 0.45, b['start'] + 0.6))
    return t0, (t0 + t2) / 2, t2

def annotated(t):
    cv, b, T = A.render(t, annotate=True, hud=False)
    im = cv.im.copy(); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = A.SAFE
    for i in range(0, int(x1 - x0), 40):                                           # dashed safe-area box
        d.line([(x0 + i, y0), (min(x1, x0 + i + 20), y0)], fill=(255, 220, 60), width=3)
        d.line([(x0 + i, y1), (min(x1, x0 + i + 20), y1)], fill=(255, 220, 60), width=3)
    for i in range(0, int(y1 - y0), 40):
        d.line([(x0, y0 + i), (x0, min(y1, y0 + i + 20))], fill=(255, 220, 60), width=3)
        d.line([(x1, y0 + i), (x1, min(y1, y0 + i + 20))], fill=(255, 220, 60), width=3)
    d.rectangle([A.CAP[0], A.CAP[1], A.CAP[2], A.CAP[3]], outline=(255, 70, 200), width=4)
    d.text((A.CAP[0] + 12, A.CAP[3] - 34), 'CAPTION BAND (provisional)', font=A.font(26, mono=True), fill=(255, 70, 200))
    for p0, p1, lab in cv.arrows:
        d.line([p0, p1], fill=(120, 255, 120), width=8)
        a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
        d.polygon([p1, (p1[0] - 36 * math.cos(a - 0.45), p1[1] - 36 * math.sin(a - 0.45)), (p1[0] - 36 * math.cos(a + 0.45), p1[1] - 36 * math.sin(a + 0.45))], fill=(120, 255, 120))
        if lab: d.text(((p0[0] + p1[0]) / 2 + 14, (p0[1] + p1[1]) / 2), lab, font=A.font(30), fill=(120, 255, 120))
    return im, cv.arrows

def wrap_lines(s, n): return textwrap.wrap(s, n) or ['']

def row(b):
    t0, t1, t2 = times(b); vm = b['vm']
    ims = []; arrows = []
    for t in (t0, t1, t2):
        im, ar = annotated(t); ims.append(im); arrows = ar or arrows
    h = PH + 40
    r = Image.new('RGB', (LEFT + 3 * (PW + GAP) + RIGHT, h), BG); d = ImageDraw.Draw(r)
    f = lambda n, m=False, bo=False: A.font(n, m, bo)
    y = 8
    d.text((10, y), '%s' % b['id'], font=f(34, True, True), fill=(255, 190, 90)); d.text((110, y + 6), '%.2f - %.2f s   anchor %.2f' % (b['start'], b['end'], b['anchor']), font=f(16, True), fill=SUB); y += 48
    for ln in wrap_lines('"%s"' % b['text'], 34): d.text((10, y), ln, font=f(22, False, True), fill=INK); y += 28
    y += 6
    for lab, key in (('MODEL', 'model_class'), ('VIEWER MUST UNDERSTAND', 'viewer_must_understand')):
        d.text((10, y), lab, font=f(15, True), fill=SUB); y += 20
        for ln in wrap_lines(vm.get(key, ''), 44): d.text((10, y), ln, font=f(18), fill=INK); y += 22
        y += 6
    cap = vm.get('motion_graphics', '')
    d.text((10, y), 'SCIENTIFIC GRAPHIC', font=f(15, True), fill=SUB); y += 20
    for ln in wrap_lines(cap, 46)[:4]: d.text((10, y), ln, font=f(18), fill=INK); y += 22
    for k, im in enumerate(ims):
        x = LEFT + k * (PW + GAP)
        r.paste(im.resize((PW, PH), Image.LANCZOS), (x, 0))
        d.rectangle([x, 0, x + PW - 1, PH - 1], outline=(70, 74, 90))
        d.text((x + 4, PH + 6), ['START', 'DEVELOPMENT', 'PAYOFF'][k] + '  %.2f s' % (t0, t1, t2)[k], font=f(18, True), fill=SUB)
    x = LEFT + 3 * (PW + GAP) + 8; y = 8
    def block(lab, txt, n=50, mx=6):
        nonlocal y
        d.text((x, y), lab, font=f(15, True), fill=SUB); y += 19
        for ln in wrap_lines(txt, n)[:mx]: d.text((x, y), ln, font=f(18), fill=INK); y += 22
        y += 6
    block('FOREGROUND', vm.get('foreground', ''), mx=2); block('MIDGROUND', vm.get('midground', ''), mx=2); block('BACKGROUND', vm.get('background', ''), mx=2)
    block('CAMERA', vm.get('camera', ''), mx=3); block('MOTION / REVEAL', vm.get('animation_action', ''), mx=5)
    block('MOTION DIRECTION (green arrows)', '; '.join(l for _, _, l in arrows if l) or 'static / graphic-internal', mx=3)
    block('CAPTION', 'provisional band y 1480-1730 of 1920; key subjects stay above y 1440 (safe box, yellow)', mx=3)
    block('ASSETS', vm.get('required_assets', ''), n=46, mx=6)
    return r, ims

def build():
    os.makedirs(OUT, exist_ok=True); os.makedirs(os.path.join(OUT, 'beats'), exist_ok=True)
    ids = [b['id'] for b in A.BEATS]; by = {b['id']: b for b in A.BEATS}
    from storyboard_data import SCENES
    rows = {}
    for b in A.BEATS:
        r, ims = row(b); rows[b['id']] = r
        for k, nm in enumerate(('start', 'dev', 'payoff')):
            ims[k].resize((540, 960), Image.LANCZOS).save(os.path.join(OUT, 'beats', '%s_%s.png' % (b['id'], nm)))
    for sid, nm, b0, b1, job in SCENES:
        seq = ids[ids.index(b0):ids.index(b1) + 1]
        w = rows[seq[0]].width; hdr = 70
        sheet = Image.new('RGB', (w, hdr + sum(rows[i].height for i in seq)), BG); d = ImageDraw.Draw(sheet)
        d.text((12, 10), '%s  %s' % (sid, nm.upper()), font=A.font(36, False, True), fill=(255, 190, 90))
        d.text((12, 48), '%s  |  beats %s-%s  |  placeholder boards from the animatic (not final art)' % (job, b0, b1), font=A.font(18), fill=SUB)
        y = hdr
        for i in seq: sheet.paste(rows[i], (0, y)); y += rows[i].height
        fn = os.path.join(OUT, '%s_%s.png' % (sid, nm.lower().replace(' ', '_').replace('?', '')))
        sheet.save(fn); print('wrote', fn, sheet.size)

if __name__ == '__main__':
    build()
