"""Data-driven scene renderer: JSON spec + PNG assets -> MP4.  python3 render_scene.py SPEC.json OUT.mp4 [--frames N]
No per-video frame ladders. Elements: asset | text | counter | bars | arrow. Enter presets: cut pop fade slide_left/right/up/down.
Keyframe tracks (x,y,scale,rot,opacity) cover travel/rotate/scale. poses[] = pose switching. repeat = conveyor row. reveal = mask wipe.
camera keys = zoom/pan. motion_fps=24 quantises motion time (observed authoring pattern E42b). Hard cuts between shots (observed grammar)."""
import json, math, os, subprocess, sys, hashlib
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FD = '/System/Library/Fonts/Supplemental/'
FONTS = {'hand': (FD + 'ChalkboardSE.ttc', 0), 'hand_light': (FD + 'ChalkboardSE.ttc', 2), 'comic': (FD + 'Comic Sans MS.ttf', None), 'comic_bold': (FD + 'Comic Sans MS Bold.ttf', None)}
_fc = {}
def font(name, size):
    k = (name, size)
    if k not in _fc:
        p, i = FONTS[name]; _fc[k] = ImageFont.truetype(p, size, index=i) if i is not None else ImageFont.truetype(p, size)
    return _fc[k]
def clamp(k): return max(0., min(1., k))
EASE = {'linear': lambda k: k, 'out': lambda k: 1 - (1 - k) ** 3, 'in_out': lambda k: 3 * k * k - 2 * k ** 3,
        'out_back': lambda k: 1 + 2.2 * (k - 1) ** 3 + 1.2 * (k - 1) ** 2}
def ease(name, k): return EASE[name](clamp(k))
_ac = {}
def resolve(ref, root=None):
    """Plain paths pass through (old specs keep working). 'asset:<id>' or 'asset:<family>/<variant>' resolves through asset_registry.json,
    only to entries with status approved (or legacy entries that predate status). Candidates/superseded never resolve."""
    if not ref.startswith('asset:'): return ref
    root = root or HERE; i = ref[6:].replace('/', '_', 1) if '/' in ref else ref[6:]
    try: reg = json.load(open(os.path.join(root, 'asset_registry.json')))
    except FileNotFoundError: reg = []
    hit = [r for r in reg if r['id'] == i and r.get('status', 'legacy') in ('approved', 'legacy')]
    if not hit: raise KeyError('no approved registry asset "%s" (from %s)' % (i, ref))
    return hit[-1]['file']
def asset_scale(ref, root=None):
    """registry entries may carry render_scale (candidate px -> legacy scene px) so swapping an asset id keeps scene geometry"""
    if not ref.startswith('asset:'): return 1.0
    root = root or HERE; i = ref[6:].replace('/', '_', 1) if '/' in ref else ref[6:]
    return float(next((r.get('render_scale', 1.0) for r in json.load(open(os.path.join(root, 'asset_registry.json'))) if r['id'] == i and r.get('status', 'legacy') in ('approved', 'legacy')), 1.0))
def load(path):
    path = resolve(path)
    if path not in _ac: _ac[path] = Image.open(os.path.join(HERE, path)).convert('RGBA')
    return _ac[path]

def track(keys, prop, t, default):
    ks = [k for k in keys if prop in k]
    if not ks: return default
    if t <= ks[0]['t']: return ks[0][prop]
    for a, b in zip(ks, ks[1:]):
        if t <= b['t']:
            e = ease(b.get('ease', 'in_out'), (t - a['t']) / max(1e-6, b['t'] - a['t'])); return a[prop] + (b[prop] - a[prop]) * e
    return ks[-1][prop]

def enter_state(el, t):
    """returns (alpha, scale_mul, dx, dy) from the enter preset"""
    en = el.get('enter', {'preset': 'cut', 't': 0}); t0 = en.get('t', 0); d = en.get('dur', .25); p = en.get('preset', 'cut')
    if t < t0: return 0, 1, 0, 0
    k = clamp((t - t0) / d) if d else 1
    if p == 'cut': return 1, 1, 0, 0
    if p == 'pop': return 1, max(.001, ease('out_back', k)), 0, 0
    if p == 'fade': return ease('out', k), 1, 0, 0
    off = en.get('dist', 700); e = 1 - ease('out', k)
    return 1, 1, {'slide_left': -off, 'slide_right': off}.get(p, 0) * e, {'slide_up': -off, 'slide_down': off}.get(p, 0) * e

def draw_proc(el, t):
    """procedural elements -> RGBA image sized to content, centred at 0,0"""
    ty = el['type']
    if ty == 'text':
        f = font(el.get('font', 'hand'), el.get('size', 60)); w, h = int(f.getlength(el['text'])) + 40, int(el.get('size', 60) * 1.6)
        im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ImageDraw.Draw(im).text((w / 2, h / 2), el['text'], font=f, fill=tuple(el.get('color', (14, 14, 14))), anchor='mm', stroke_width=el.get('stroke', 0), stroke_fill=(14, 14, 14)); return im
    if ty == 'counter':
        a, b = el['from'], el['to']; t0, d = el.get('t0', 0), el.get('dur', 1.0); v = a + (b - a) * ease('out', (t - t0) / d)
        txt = el.get('prefix', '') + (('{:,.' + str(el.get('dec', 0)) + 'f}').format(v)) + el.get('suffix', '')
        return draw_proc(dict(type='text', text=txt, font=el.get('font', 'comic_bold'), size=el.get('size', 120), color=el.get('color', (14, 14, 14)), stroke=el.get('stroke', 0)), t)
    if ty == 'bars':
        vals = el['values']; W_, H_ = el.get('w', 800), el.get('h', 420); gap = W_ / len(vals); im = Image.new('RGBA', (W_ + 20, H_ + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.line([(10, H_ + 10), (W_ + 10, H_ + 10)], fill=(14, 14, 14, 255), width=8); d.line([(10, 10), (10, H_ + 10)], fill=(14, 14, 14, 255), width=8)
        t0, dur, st = el.get('t0', 0), el.get('dur', 1.2), el.get('stagger', .12); mx = max(vals)
        for i, v in enumerate(vals):
            k = ease('out', (t - t0 - i * st) / dur)
            if k <= .001: continue
            hh = v / mx * (H_ - 20) * k; x0 = 10 + i * gap + gap * .15
            d.rectangle([x0, H_ + 10 - hh, x0 + gap * .7, H_ + 10], fill=tuple(el.get('colors', [(235, 190, 50)])[i % len(el.get('colors', [0]))]) + (255,), outline=(14, 14, 14, 255), width=5)
        return im
    if ty == 'panel':   # labelled flat shape: stand-in for third-party media / blocked-asset slate (never a production asset)
        w, h = el.get('w', 400), el.get('h', 300); im = Image.new('RGBA', (w + 4, h + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        fl = el.get('fill', (200, 200, 200)); fill = tuple(fl) + (int(255 * el.get('alpha', 1)),) if fl else None; ow = el.get('outline_w', 0); oc = tuple(el.get('outline', (14, 14, 14))) + (255,)
        (d.ellipse if el.get('shape') == 'ellipse' else d.rectangle)([2, 2, w + 1, h + 1], fill=fill, outline=oc if ow else None, width=ow)
        if el.get('label'):
            f = font('comic', el.get('label_size', 34)); lines = el['label'].split('\n')
            for i, ln in enumerate(lines): d.text((w / 2, h / 2 + (i - (len(lines) - 1) / 2) * el.get('label_size', 34) * 1.25), ln, font=f, fill=tuple(el.get('label_color', (14, 14, 14))), anchor='mm')
        return im
    if ty == 'arrow':
        L = el.get('len', 300); k = ease('out', (t - el.get('t0', 0)) / el.get('dur', .4)); l = max(2, L * k); col = tuple(el.get('color', (200, 40, 45))) + (255,)
        im = Image.new('RGBA', (160, int(L) + 120), (0, 0, 0, 0)); d = ImageDraw.Draw(im); cx = 80; d.line([(cx, 10), (cx, 10 + l)], fill=col, width=18)
        d.polygon([(cx - 55, 10 + l - 10), (cx + 55, 10 + l - 10), (cx, 10 + l + 70)], fill=col); return im
    raise ValueError(ty)

def render_element(el, t, mt):
    """t = shot-local time (real); mt = quantised motion time. returns (img RGBA, cx, cy) or None"""
    en_a, en_s, dx, dy = enter_state(el, t + 1e-6 if el.get('enter', {}).get('preset', 'cut') == 'cut' else mt)   # hard cuts land on the real 30fps frame; eased motion stays on the 24fps grid
    ex = el.get('exit')
    if ex and t >= ex['t'] - 1e-6: return None
    if en_a <= 0: return None
    keys = el.get('keys', [])
    if 'poses' in el and 'asset' in el:
        a = el['asset']
        for p in el['poses']:
            if t >= p['t'] - 1e-6: a = p['asset']
        img = load(a)
    elif 'asset' in el: img = load(el['asset'])
    else:
        if 'poses' in el:   # procedural element: the latest pose's fields override (stepped state swap, e.g. SH018 two-state boil)
            for p in el['poses']:
                if t >= p['t'] - 1e-6: el = dict(el, **{k: v for k, v in p.items() if k != 't'})
        img = draw_proc(el, mt)
    ref = a if ('poses' in el and 'asset' in el) else el.get('asset', '')
    sc = track(keys, 'scale', mt, el.get('scale', 1)) * en_s * asset_scale(ref); rot = track(keys, 'rot', mt, el.get('rot', 0)); op = track(keys, 'opacity', mt, 1) * en_a
    cx = track(keys, 'x', mt, el.get('x', 540)) + dx; cy = track(keys, 'y', mt, el.get('y', 960)) + dy
    if 'reveal' in el:
        rv = el['reveal']; k = ease('out', (mt - rv['t']) / rv.get('dur', .5)); w, h = img.size; img = img.crop((0, 0, max(1, int(w * k)), h)); cx -= (w - img.size[0]) / 2 * sc
    if abs(sc - 1) > 1e-3: img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.LANCZOS)
    if abs(rot) > .01: img = img.rotate(rot, expand=True, resample=Image.BICUBIC)
    if op < .999: a = img.getchannel('A').point(lambda v: int(v * op)); img = img.copy(); img.putalpha(a)
    return img, cx, cy

def comp_shot(spec, shot, t):
    mt = math.floor(t * spec['motion_fps'] + 1e-6) / spec['motion_fps'] if spec.get('motion_fps') else t
    base = Image.new('RGBA', (spec['w'], spec['h']), tuple(spec.get('bg', (253, 253, 253))) + (255,))
    for el in sorted(shot['elements'], key=lambda e: e.get('layer', 0)):
        rp = el.get('repeat')
        reps = [(0, 0)] if not rp else [(i * rp['pitch'] - ((mt - rp.get('t0', 0)) * rp.get('speed', 0)) % (rp['pitch'] * rp['count']), 0) for i in range(rp['count'] + 1)]
        for ox, oy in reps:
            e2 = dict(el); e2['x'] = el.get('x', 540) + ox; e2['y'] = el.get('y', 960) + oy
            if rp: e2['x'] = el.get('x', 0) + ox
            r = render_element(e2, t, mt)
            if not r: continue
            img, cx, cy = r; base.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2))) if 0 <= cx - img.width / 2 and 0 <= cy - img.height / 2 and cx + img.width / 2 <= spec['w'] and cy + img.height / 2 <= spec['h'] else paste_clip(base, img, cx, cy)
    cam = shot.get('camera')
    if cam:
        z = track(cam['keys'], 'zoom', mt, 1); px = track(cam['keys'], 'x', mt, spec['w'] / 2); py = track(cam['keys'], 'y', mt, spec['h'] / 2)
        if abs(z - 1) > 1e-3 or px != spec['w'] / 2 or py != spec['h'] / 2:
            cw, ch = spec['w'] / z, spec['h'] / z; x0 = min(max(0, px - cw / 2), spec['w'] - cw); y0 = min(max(0, py - ch / 2), spec['h'] - ch)
            base = base.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((spec['w'], spec['h']), Image.LANCZOS)
    return base

def paste_clip(base, img, cx, cy):
    x, y = int(cx - img.width / 2), int(cy - img.height / 2); W_, H_ = base.size
    sx0, sy0 = max(0, -x), max(0, -y); sx1, sy1 = min(img.width, W_ - x), min(img.height, H_ - y)
    if sx1 > sx0 and sy1 > sy0: base.alpha_composite(img.crop((sx0, sy0, sx1, sy1)), (max(0, x), max(0, y)))

def draw_caption(im, spec, t):
    cap = spec.get('caption')
    if not cap: return
    ev = [e for e in cap['events'] if e['t'] <= t]
    if not ev: return
    e = ev[-1]; end = e.get('end')
    if end is not None and t >= end: return
    words = e.get('full', e['text']).split(); shown_n = len(e['text'].split()); nxt = [x['t'] for x in cap['events'] if x['t'] > e['t']]
    span = (end if end is not None else (nxt[0] if nxt else e['t'] + 1.5)) - e['t']
    n = shown_n if not cap.get('word_reveal') else max(1, min(len(words), int(1 + (t - e['t']) / max(.05, span) * len(words))))
    f = font(cap.get('font', 'comic'), cap.get('size', 57)); d = ImageDraw.Draw(im); lines = [[]]
    for w in words:
        if d.textlength(' '.join(lines[-1] + [w]), font=f) > cap.get('wrap', 800) and lines[-1]: lines.append([w])
        else: lines[-1].append(w)
    k = 0
    for i, ln in enumerate(lines):
        y = cap.get('y', 1353) + (i - (len(lines) - 1) / 2) * cap.get('pitch', 62); x0 = spec['w'] / 2 - d.textlength(' '.join(ln), font=f) / 2
        shown = ln[:max(0, n - k)]; k += len(ln)
        if shown: d.text((x0, y), ' '.join(shown), font=f, fill=(14, 14, 14), anchor='lm', stroke_width=cap.get('stroke', 1), stroke_fill=(14, 14, 14))

def validate(spec):
    errs = []
    def chk(p):
        try: q = resolve(p)
        except KeyError as e: errs.append('unresolved asset ' + str(e)); return
        if not os.path.exists(os.path.join(HERE, q)): errs.append('missing asset ' + q)
    for s in spec['shots']:
        ids = set()
        for el in s['elements']:
            if el.get('id') in ids: errs.append('dup element id ' + str(el.get('id')))
            ids.add(el.get('id'))
            if 'asset' in el: chk(el['asset'])
            for p in el.get('poses', []):
                if 'asset' in p: chk(p['asset'])
            if 'asset' not in el and 'type' not in el: errs.append('element without asset/type ' + str(el.get('id')))
    ends = [s['start'] + s['dur'] for s in spec['shots']]
    if any(abs(a - s['start']) > 1e-6 for a, s in zip(ends, spec['shots'][1:])): errs.append('shots not contiguous')
    return errs

def main():
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]; errs = validate(spec)
    if errs: print('VALIDATION FAILED', *errs, sep='\n  '); sys.exit(1)
    fps = spec['fps']; total = round(spec['shots'][-1]['start'] * fps + spec['shots'][-1]['dur'] * fps)
    if '--frames' in sys.argv: total = min(total, int(sys.argv[sys.argv.index('--frames') + 1]))
    p = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (spec['w'], spec['h']), '-r', str(fps), '-i', '-', '-vf', 'scale=out_color_matrix=bt709:out_range=tv', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv', '-crf', '14', out], stdin=subprocess.PIPE)
    for f in range(total):
        t = f / fps; shot = [s for s in spec['shots'] if s['start'] <= t + 1e-9][-1]
        im = comp_shot(spec, shot, t - shot['start']).convert('RGB'); draw_caption(im, spec, t); p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
    pr = subprocess.run(['/opt/homebrew/bin/ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_frames', '-show_entries', 'stream=width,height,r_frame_rate,nb_read_frames', '-of', 'json', out], capture_output=True, text=True)
    info = json.loads(pr.stdout)['streams'][0]; print('rendered', total, 'frames', info)
if __name__ == '__main__': main()
