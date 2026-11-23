"""CH001 novel-scene tests v2 (visually grounded; original art only). Replaces the numerically-tuned NS5/NS6 (void: rectangles / random card montage did not look like the references).
Grammar measured by viewing refs 33NV, zLv, 3132dfa8, 1eTw, 02f598d4: white canvas, ONE focal subject per beat (photo plate / screenshot / cartoon prop / stick figure),
red-arrow + hand-lettered annotation, thick black outlines, hard cuts + pop-in.  NS5 = family B (uncaptioned, small mid-frame props), NS6 = family C (1 subject + hand-lettered caption).
Usage: render_novel5.py OUT_DIR -> NS5_v2_retire_early.mp4, NS6_v2_emergency_fund.mp4"""
import importlib.util, math, os, subprocess, sys
from PIL import Image, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('r19', os.path.join(HERE, '..', 'same_video', 'render_10nEByVLya0_v19.py')); R = importlib.util.module_from_spec(sp); sp.loader.exec_module(R)
R.Y0, R.Y1 = 0, 1920   # full-frame canvas (refs use the whole frame, not only the 655-1265 band)
Cv, ease, stick, stick_blk, hand, comic, BLK, RED, W, H, FPS, SS = (getattr(R, k) for k in 'Cv ease stick stick_blk hand comic BLK RED W H FPS SS'.split())
_p0 = Cv.p
def _p(s, x, y):   # per-beat prop scale about a centre: refs show props at 40-60% of frame width (measured on 3132/33NV contact sheets)
    k = getattr(s, 'sc', 1); cx, cy = getattr(s, 'sc_c', (540, 960)); return _p0(s, cx + (x - cx) * k, cy + (y - cy) * k)
Cv.p = _p
HF = lambda z: ImageFont.truetype('/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf', z)   # hand-lettered caption look
def lettered(c, x, y, lines, sz=76, col=BLK):
    old = getattr(c, 'sc', 1); c.sc = 1
    for i, t in enumerate(lines): c.text(x, y + i * sz * 1.12, t, HF(sz), col)
    c.sc = old
def pop(lf, n=6): return max(.05, ease(lf / n))
def bubble(c, x, y, w, h, lines, tail):
    c.ell(x, y, w / 2, h / 2, fill=(255, 255, 255), outline=BLK, w=6); c.poly(tail, fill=(255, 255, 255), outline=BLK, w=6)
    c.ell(x, y, w / 2 - 5, h / 2 - 5, fill=(255, 255, 255), outline=None)
    for i, t in enumerate(lines): c.text(x, y + (i - (len(lines) - 1) / 2) * 40, t, comic(32))
def eyes(c, x, y, s=1.0, look=0):
    for dx in (-30, 30): c.ell(x + dx * s, y, 24 * s, 30 * s, fill=(255, 255, 255), outline=BLK, w=5); c.ell(x + dx * s + look * 8, y + 4 * s, 8 * s, 11 * s, fill=BLK, outline=None)
def legs(c, x, y, s=1.0): c.line([(x - 22 * s, y), (x - 26 * s, y + 70 * s), (x - 4 * s, y + 74 * s)], 6); c.line([(x + 22 * s, y), (x + 26 * s, y + 70 * s), (x + 48 * s, y + 72 * s)], 6)

# ---------------- NS5 (family B): small characters/props mid-frame, no caption ----------------
def ns5(c, f):
    b, lf = divmod(f, 72); k = pop(lf)
    c.sc, c.sc_c = {1: 1.5, 2: 1.6, 3: 1.2}.get(b, 1), (540, 960)
    if b == 0: c.text(540, 960, 'In 2035', HF(96))
    elif b == 1:   # blob character (organic silhouette, glasses, legs) + tiny label
        pts = [(540 + 150 * k * math.cos(t) * (1 + .12 * math.sin(3 * t)), 960 + 105 * k * math.sin(t) * (1 + .1 * math.cos(2 * t))) for t in [i * .26 for i in range(25)]]
        legs(c, 520, 1040, k); c.poly(pts, fill=(60, 150, 70), outline=BLK, w=7); eyes(c, 520, 940, k); c.text(700, 880, 'save me', HF(30))
    elif b == 2:   # house prop
        c.rect(420, 920, 660, 1100, fill=(236, 170, 140), outline=BLK, w=7); c.poly([(396, 924), (540, 800), (684, 924)], fill=(70, 100, 190), outline=BLK, w=7)
        c.rect(500, 990, 580, 1100, fill=(120, 190, 215), outline=BLK, w=6); c.rect(440, 950, 490, 1000, fill=(210, 235, 245), outline=BLK, w=5); c.rect(590, 950, 640, 1000, fill=(210, 235, 245), outline=BLK, w=5)
    elif b == 3:   # stick man with phone + speech bubble (ref 33NV t~13)
        stick(c, 420, 840, 'neutral', 'shrug'); c.rect(455, 1010, 495, 1070, fill=(30, 30, 35), outline=BLK, w=4, r=6)
        bubble(c, 700, 800, 330, 170, ('Retire at 30?', 'I could try', 'it later...'), [(600, 870), (640, 900), (560, 930)])
    else:          # coin mascot with legs, small, off-centre (ref 33NV t~18)
        legs(c, 700, 960, .8); c.ell(700, 920, 62 * k, 62 * k, fill=(240, 160, 30), outline=BLK, w=6); c.text(700, 922, '$', comic(72), (255, 255, 255)); c.line([(640, 930), (600, 970)], 6); c.line([(760, 930), (800, 970)], 6)

# ---------------- NS6 (family C): one subject per beat + hand-lettered caption ----------------
def ns6(c, f):   # v2b: beats of 72 frames with staggered sub-events (ref 3132: bubble/second character/arrow pop in ~0.6 s apart inside one beat)
    b, lf = divmod(f, 72); k = pop(lf)
    c.sc, c.sc_c = {0: 1.28, 1: 1.45, 2: 1.35, 3: 1.2, 4: 1.2}[b], {0: (540, 760), 1: (540, 800), 2: (540, 880), 3: (540, 960), 4: (540, 700)}[b]
    if b == 0:   # portrait plate (stand-in) -> red arrow -> name -> caption
        c.rect(300, 520, 780, 1000, fill=(150, 154, 158)); c.ell(540, 720, 80, 95, fill=(205, 205, 208), outline=None); c.poly([(380, 1000), (420, 860), (660, 860), (700, 1000)], fill=(60, 64, 72))
        if lf >= 14: c.line([(350, 930), (340, 880), (370, 850)], 7, RED); c.poly([(355, 840), (385, 842), (366, 868)], fill=RED)
        if lf >= 30: c.text(450, 960, 'A. Example', comic(34), (255, 255, 255))
        if lf >= 8: lettered(c, 540, 1230, ('The head of the', 'central bank'))
    elif b == 1:  # badge -> pot -> caption
        c.ell(540, 620, 170, 170, fill=(60, 100, 170), outline=BLK, w=8); c.ell(540, 620, 130, 130, fill=(240, 240, 245), outline=BLK, w=5)
        c.poly([(540 + 70 * math.sin(i * 2.513), 620 - 70 * math.cos(i * 2.513)) for i in (0, 2, 4, 1, 3)], fill=(230, 190, 60), outline=BLK, w=4)
        if lf >= 16:
            for i in range(5): c.poly([(450 + i * 45, 905), (480 + i * 45, 860), (500 + i * 45, 905)], fill=(110, 185, 105), outline=BLK, w=4)
            c.ell(540, 990, 150, 95, fill=(212, 175, 55), outline=BLK, w=8); c.rect(400, 905, 680, 940, fill=(212, 175, 55), outline=BLK, w=6, r=10)
        if lf >= 36: c.line([(300, 1000), (250, 960), (270, 920)], 8, RED); c.poly([(262, 905), (292, 912), (268, 936)], fill=RED)
        if lf >= 8: lettered(c, 540, 1300, ('The answer is a pot', 'of money'))
    elif b == 2:  # caption, man slides in, bubble, second character
        lettered(c, 540, 300, ('He just needs a signature',), 66)
        if lf >= 6: sx = -260 * (1 - ease((lf - 6) / 10)); stick(c, 330 + sx, 800, 'neutral', 'point'); c.rect(430 + sx, 940, 520 + sx, 1070, fill=(255, 255, 255), outline=BLK, w=5); [c.line([(445 + sx, 965 + i * 26), (505 + sx, 965 + i * 26)], 3) for i in range(4)]
        if lf >= 28: bubble(c, 740, 720, 330, 190, ('Boss, could you', 'sign this?'), [(620, 790), (660, 830), (580, 850)])
        if lf >= 46: stick(c, 760, 1020, 'neutral', 'shrug'); c.rect(790, 1190, 830, 1250, fill=(120, 80, 50), outline=BLK, w=4, r=6)
    elif b == 3:  # card -> check -> caption
        c.rect(240, 760, 840, 1120, fill=(240, 170, 40), outline=BLK, w=8, r=22)
        if lf >= 12: c.rect(300, 840, 380, 900, fill=(220, 220, 225), outline=BLK, w=5, r=8); c.text(560, 990, 'XXXX XXXX XXXX', comic(44)); c.text(340, 1070, 'NAME', comic(34))
        if lf >= 30: c.line([(300, 1110), (390, 1200), (650, 960)], 30, (40, 170, 80)); c.ell(300, 1110, 15, 15, fill=(40, 170, 80), outline=None); c.ell(650, 960, 15, 15, fill=(40, 170, 80), outline=None)
        if lf >= 6: lettered(c, 540, 330, ('and the credit', 'card opens up.'))
    else:         # rotated plate (stand-in) + big bubble (ref 3132 t~14)
        a = math.radians(-35); P = lambda x, y: (540 + (x - 540) * math.cos(a) - (y - 700) * math.sin(a), 700 + (x - 540) * math.sin(a) + (y - 700) * math.cos(a))
        c.poly([P(300, 480), P(780, 480), P(780, 960), P(300, 960)], fill=(160, 150, 150)); c.ell(*P(540, 640), 70, 85, fill=(215, 195, 185), outline=None)
        lettered(c, 540, 220, ('The boss can spend it', 'without asking.'), 62)
        if lf >= 30: bubble(c, 400, 1180, 400, 230, ("I don't need", "y'all!"), [(560, 1130), (640, 1080), (610, 1170)])

def render(name, fn, n, out):
    p = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '14', os.path.join(out, name + '.mp4')], stdin=subprocess.PIPE)
    for f in range(n): c = Cv(); fn(c, f); p.stdin.write(c.out().tobytes())
    p.stdin.close(); p.wait(); print(name, n, 'frames')
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True); render('NS5_v2_retire_early', ns5, 360, out); render('NS6_v2_emergency_fund', ns6, 360, out)
