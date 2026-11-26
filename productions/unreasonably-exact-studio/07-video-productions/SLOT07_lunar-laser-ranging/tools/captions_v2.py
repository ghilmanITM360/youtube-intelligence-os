"""V2 captions: cue building, SRT, three candidate treatments, comparison sheet, and burn-in onto a clean render.

Typography decision record: CAPTION_TYPOGRAPHY_DECISION in renders/roughcut_v2/CAPTION_STYLE_NOTES.md.
The xkcd fonts (ipython/xkcd-font, CC BY-NC 3.0) are NOT used: non-commercial licence. Candidates are SIL OFL 1.1 fonts
from github.com/google/fonts (assets/fonts/*/OFL.txt). They are approximations of a hand-lettered feel, not the xkcd face.

  python tools/captions_v2.py srt OUT.srt
  python tools/captions_v2.py compare OUT.png still1.png still2.png still3.png
  python tools/captions_v2.py burn IN.mp4 OUT.mp4 [A|B|C]
"""
import os, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, 'animation'))
from uemotion.narration import NAR
F = os.path.join(ROOT, 'assets', 'fonts')
STYLES = {
    'A': dict(name='A  Comic Neue Bold, white, soft shadow, no card', font=F + '/comicneue/ComicNeue-Bold.ttf', size=70, fill=(255, 255, 255),
              stroke=3, stroke_fill=(10, 14, 28), shadow=10, card=None, scrim=False),
    'B': dict(name='B  Patrick Hand, warm white, thin outline, low scrim', font=F + '/patrickhand/PatrickHand-Regular.ttf', size=80, fill=(246, 240, 228),
              stroke=4, stroke_fill=(8, 10, 18), shadow=0, card=None, scrim=True),
    'C': dict(name='C  Kalam Bold on a translucent bar', font=F + '/kalam/Kalam-Bold.ttf', size=66, fill=(255, 255, 255),
              stroke=0, stroke_fill=None, shadow=0, card=(8, 12, 26, 140), scrim=False),
}
MAX_W, CY, LINE_GAP = 900, 1650, 1.16          # design units (1080 x 1920); CY 1650 (86 %): below the Earth-limb station (y ~1500) so no science point is covered

# ------------------------------------------------------------------ cues
def cues(max_chars=40):
    ph = [dict(p) for p in NAR.phrases]
    merged = []
    for p in ph:                                                # merge a very short phrase ("Now,", "And") into the next one
        if merged and merged[-1].get('_short') and p['start'] - merged[-1]['end'] < 0.7:
            q = merged.pop(); p = dict(p, first=q['first'], start=q['start'])
        words = NAR.words[p['first']:p['last'] + 1]
        p['_short'] = len(' '.join(w['word'] for w in words)) <= 8 and words[-1]['word'].endswith(',') or words[-1]['word'] == 'And'
        merged.append(p)
    import itertools, math
    out = []
    for p in merged:                                            # balanced split: fewest chunks, then the most even, breaking at punctuation when possible
        words = NAR.words[p['first']:p['last'] + 1]; L = len(' '.join(w['word'] for w in words)); k = max(1, math.ceil(L / max_chars))
        best = None
        for cuts in itertools.combinations(range(1, len(words)), k - 1):
            parts = [words[i:j] for i, j in zip((0,) + cuts, cuts + (len(words),))]
            lens = [len(' '.join(w['word'] for w in q)) for q in parts]
            if max(lens) > max_chars + 4: continue
            score = max(lens) - min(lens) * 0.3 - 8 * sum(q[-1]['word'][-1] in ',.?' for q in parts[:-1])
            if best is None or score < best[0]: best = (score, parts)
        out += best[1] if best else [words]
    res = []
    for c in out:
        res.append(dict(text=' '.join(w['word'] for w in c), start=c[0]['start'] - 0.05, end=c[-1]['end'] + 0.35))
    for a, b in zip(res, res[1:]): a['end'] = min(a['end'], b['start'] - 0.04)
    return res

def srt(path):
    def ts(t): t = max(0, t); h, r = divmod(t, 3600); m, s = divmod(r, 60); return '%02d:%02d:%02d,%03d' % (h, m, int(s), round((s - int(s)) * 1000) % 1000)
    with open(path, 'w') as f:
        for i, c in enumerate(cues(), 1): f.write('%d\n%s --> %s\n%s\n\n' % (i, ts(c['start']), ts(c['end']), c['text']))

# ------------------------------------------------------------------ drawing
_fc = {}
def font(st, k):
    key = (st['font'], int(st['size'] * k))
    if key not in _fc: _fc[key] = ImageFont.truetype(st['font'], key[1])
    return _fc[key]

def lines_for(text, f, maxw):
    ws = text.split();
    if f.getlength(text) <= maxw: return [text]
    best = None
    for k in range(1, len(ws)):
        a, b = ' '.join(ws[:k]), ' '.join(ws[k:]); m = max(f.getlength(a), f.getlength(b))
        if m <= maxw and (best is None or m < best[0]): best = (m, [a, b])
    return best[1] if best else [text]

def render_cue(text, st, W, H):
    """RGBA overlay (full frame) for one cue at full opacity."""
    k = W / 1080; f = font(st, k); ls = lines_for(text, f, MAX_W * k); lh = st['size'] * k * LINE_GAP
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    y0 = CY * k - lh * (len(ls) - 1) / 2
    if st['scrim']:                                             # low gradient: darkest under the text, gone by mid-frame
        g = np.zeros((H, W, 4), np.uint8); yy = np.arange(H)[:, None]
        a = np.clip((yy - (y0 - 2.2 * lh)) / (2.0 * lh), 0, 1) * np.clip(((y0 + len(ls) * lh + 2.6 * lh) - yy) / (1.6 * lh), 0, 1) * 110
        g[..., 3] = a.astype(np.uint8); ov = Image.alpha_composite(ov, Image.fromarray(g, 'RGBA')); d = ImageDraw.Draw(ov)
    if st['card']:
        wmax = max(f.getlength(l) for l in ls); pad = 26 * k
        d.rounded_rectangle((W / 2 - wmax / 2 - pad, y0 - lh / 2 - pad * 0.5, W / 2 + wmax / 2 + pad, y0 + lh * (len(ls) - 0.5) + pad * 0.5), radius=int(24 * k), fill=st['card'])
    if st['shadow']:
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
        for i, l in enumerate(ls): sd.text((W / 2 + 2 * k, y0 + i * lh + 4 * k), l, font=f, fill=(0, 0, 0, 200), anchor='mm', stroke_width=int(st['stroke'] * k) + 2, stroke_fill=(0, 0, 0, 200))
        ov = Image.alpha_composite(ov, sh.filter(ImageFilter.GaussianBlur(st['shadow'] * k))); d = ImageDraw.Draw(ov)
    for i, l in enumerate(ls):
        d.text((W / 2, y0 + i * lh), l, font=f, fill=st['fill'], anchor='mm', stroke_width=int(st['stroke'] * k), stroke_fill=st['stroke_fill'])
    return ov

def alpha_at(c, t, fade=0.12):
    return float(np.clip((t - c['start']) / fade, 0, 1) * np.clip((c['end'] - t) / fade, 0, 1))

# ------------------------------------------------------------------ commands
def compare(out, stills, times):
    cs = cues(); tiles = []
    for sk, st in STYLES.items():
        row = []
        for p, t in zip(stills, times):
            im = Image.open(p).convert('RGBA'); W, H = im.size
            c = next(c for c in cs if c['start'] <= t <= c['end'] + 0.3)
            row.append(Image.alpha_composite(im, render_cue(c['text'], st, W, H)).convert('RGB'))
        tiles.append((st['name'], row))
    W, H = tiles[0][1][0].size; lab = 60; sheet = Image.new('RGB', (W * len(stills), (H + lab) * len(tiles)), (245, 245, 245)); d = ImageDraw.Draw(sheet)
    lf = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 30)
    for r, (name, row) in enumerate(tiles):
        d.text((16, r * (H + lab) + 14), name, font=lf, fill=(20, 20, 20))
        for i, im in enumerate(row): sheet.paste(im, (i * W, r * (H + lab) + lab))
    sheet.save(out); print('wrote', out, sheet.size)

def burn(inp, out, sk='A', fps=30):
    st = STYLES[sk]; cs = cues()
    W, H = [int(x) for x in subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', inp], capture_output=True, text=True).stdout.strip().split(',')]
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', inp, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, H), '-r', str(fps), '-i', '-', '-i', inp,
                            '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', out], stdin=subprocess.PIPE)
    cache = {}; i = 0; n = W * H * 3
    while True:
        buf = dec.stdout.read(n)
        if len(buf) < n: break
        t = i / fps; i += 1
        c = next((c for c in cs if c['start'] - 0.15 <= t <= c['end'] + 0.15), None)
        a = alpha_at(c, t) if c else 0
        if a > 0:
            if c['text'] not in cache: cache = {c['text']: np.asarray(render_cue(c['text'], st, W, H)).astype(np.float32)}
            ov = cache[c['text']]; fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
            al = ov[..., 3:4] / 255 * a; buf = (fr * (1 - al) + ov[..., :3] * al).astype(np.uint8).tobytes()
        enc.stdin.write(buf)
    enc.stdin.close(); enc.wait(); dec.wait(); print('wrote', out, i, 'frames')

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'srt': srt(sys.argv[2])
    elif cmd == 'compare': compare(sys.argv[2], sys.argv[3:6], [float(x) for x in sys.argv[6:9]])
    elif cmd == 'burn': burn(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else 'A')
    elif cmd == 'list':
        for c in cues(): print('%6.2f %6.2f  %s' % (c['start'], c['end'], c['text']))
