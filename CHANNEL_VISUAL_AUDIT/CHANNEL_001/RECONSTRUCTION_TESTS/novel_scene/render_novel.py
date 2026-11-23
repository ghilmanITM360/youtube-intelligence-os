"""CH001 novel-scene generalization tests (original topics, original art, no source pixels).
NS1 'Inflation eats your cash' (character scene, 9 s) and NS2 'Compound interest' (chart/data scene, 9 s).
Grammar applied from 05_VISUAL_DNA.md / 09_CHARACTER_SYSTEM.md: #FDFDFD canvas, art in y640-1300, black 5-14 px outlines,
flat fills, one accent per beat, hard cuts + pop-ins, Comic-style 58 px caption block (centre y1353, pitch 62, wrap 800).
Usage: render_novel.py OUT_DIR  -> NS1.mp4, NS2.mp4 (silent)."""
import importlib.util, math, os, subprocess, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r6', os.path.join(HERE, '..', 'same_video', 'render_10nEByVLya0_v6.py'))
R = importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
Cv, ease, stick, bag, qmark, hand, comic, mono, BLK, RED, W, H, Y0, FPS, CAPF = (getattr(R, k) for k in 'Cv ease stick bag qmark hand comic mono BLK RED W H Y0 FPS CAPF'.split())
BLUE, GOLD = (60, 90, 200), (235, 190, 50)

# --- caption: words timed evenly; chunk breaks after punctuation words (v4 rule); wrap 800; block centre y1353 ---
def caption_frame(im, f, words):
    vis = [w for w, t in words if t <= f]
    if not vis: return
    chunks, cur = [], []
    for w, t in words:
        cur.append((w, t))
        if w[-1] in '.,?!:': chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    ch = [c for c in chunks if c[0][1] <= f][-1]; full = [w for w, _ in ch]; n = sum(1 for _, t in ch if t <= f)
    d = ImageDraw.Draw(im); lines = [[]]
    for w in full:
        if d.textlength(' '.join(lines[-1] + [w]), font=CAPF) > 800: lines.append([w])
        else: lines[-1].append(w)
    k = 0
    for i, ln in enumerate(lines):
        y = 1353 + (i - (len(lines) - 1) / 2) * 62; x0 = 531 - d.textlength(' '.join(ln), font=CAPF) / 2
        shown = ln[:max(0, n - k)]; k += len(ln)
        if shown: d.text((x0, y), ' '.join(shown), font=CAPF, fill=BLK, anchor='lm')

def words(text, start, per=7):
    out, t = [], start
    for w in text.split(): out.append((w, t)); t += per + (6 if w[-1] in '.,?!:' else 0)
    return out

def burger(c, x, y, s=1.0):   # original cash-stack icon (rect + $)
    c.rect(x - 90 * s, y - 50 * s, x + 90 * s, y + 50 * s, fill=(150, 205, 140), outline=BLK, w=6, r=8)
    c.ell(x, y, 34 * s, 34 * s, fill=(190, 230, 175), outline=BLK, w=5); c.text(x, y + 3, '$', comic(max(8, int(44 * s))), (40, 110, 50))

# ---------------- NS1: character scene ----------------
NS1_W = words("Your cash sits still. Prices keep climbing, so every year it buys less.", 8)
def ns1(c, f):
    if f < 60:                       # cut-in stick man + cash stack pops (f6)
        stick(c, 400, 780, 'neutral', 'shrug')
        if f >= 6: k = ease((f - 6) / 4); burger(c, 780, 980, 1.2 * k + .01)
    elif f < 130:                    # price tag pops, cash shrinks (accent red arrow)
        stick(c, 400, 780, 'neutral', 'shrug')
        k = ease((f - 60) / 40); burger(c, 780, 980, 1.2 - .6 * k)
        c.rect(600, 760, 800, 840, fill=(255, 235, 230), outline=BLK, w=6, r=10); c.text(700, 800, '$5 -> $7', hand(46), RED)
        c.line([(700, 850), (700, 900)], 8, RED); c.poly([(680, 895), (720, 895), (700, 930)], fill=RED)
    elif f < 200:                    # worried face, small cash, question mark pops
        stick(c, 400, 780, 'neutral', 'shrug', sweat=True); burger(c, 780, 990, .6)
        if f >= 140: qmark(c, 640, 770, int(20 + 60 * ease((f - 140) / 6)))
    else:                            # hard cut: big red arrow down + text card
        c.text(540, 900, 'cash value', hand(80)); c.line([(540, 960), (540, 1170)], 16, RED); c.poly([(480, 1150), (600, 1150), (540, 1240)], fill=RED)

# ---------------- NS2: chart / data scene ----------------
NS2_W = words("Now invest early. Money earns, then the earnings earn too.", 8)
def ns2(c, f):
    c.text(540, 705, 'Compound growth', hand(70))
    if f < 20: return
    x0, y0, x1, y1 = 140, 1205, 940, 800
    c.line([(x0, y0), (x1, y0)], 8); c.line([(x0, y0), (x0, y1)], 8)       # axes
    t = min(1, (f - 20) / 150)
    for i in range(8):
        h = 28 * (1.38 ** i); bx = x0 + 40 + i * 92
        k = ease(t * 8 - i)
        if k > .01:
            hh = min(h, 420) * k; c.rect(bx, y0 - hh, bx + 64, y0, fill=(235, 190, 50) if i < 7 else (80, 170, 90), outline=BLK, w=5)
    if f >= 190: c.text(760, 790, '10x', hand(120), (60, 140, 70))
    if f >= 40: c.text(250, 1240, 'year 1', hand(36));
    if f >= 170: c.text(870, 1240, 'year 30', hand(36))

def render(name, fn, wd, n, out):
    p = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '14', os.path.join(out, name + '.mp4')], stdin=subprocess.PIPE)
    for f in range(n):
        c = Cv(); fn(c, f); im = Image.new('RGB', (W, H), (253, 253, 253)); im.paste(c.out(), (0, Y0)); caption_frame(im, f, wd); p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait(); print(name, n, 'frames')

if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    render('NS1_inflation_cash', ns1, NS1_W, 270, out); render('NS2_compound_growth', ns2, NS2_W, 270, out)
