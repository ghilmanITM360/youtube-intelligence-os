"""Authentic-document scene operation for the V1 renderer (CH001 closure).

Adds ONE reusable layer to the existing beat/It renderer (v1r4_render): document_item(spec, t0) returns a `dyn` item.
Nothing in v1r4_render / v1r9b is changed; existing scenes are untouched.

Contract
- The source capture is immutable (path + SHA-256 verified); every derived view is rendered per frame from it.
- Annotations live in DOCUMENT-LOCAL pixel coordinates. Each frame applies ONE transform (crop -> viewport) to the
  image and to every annotation, so a zoom/pan can never detach a mark from its passage.
- The crop must keep the viewport aspect ratio (no distortion); the layer is clipped to the viewport frame.
- Annotation events are frame-addressable: start_s (first mark pixel), complete_s (mark complete), exit_s (optional),
  mode instant (start==complete) or progressive. No default delay exists; timing comes from the spec (set from the
  verified narration clause).  `legible_s` = first moment the target passage is readable; marks may not start earlier.
- required_context rects must stay inside the crop while a mark is on screen (a crop may not hide qualifiers).
Spec: see doc_scene_schema.md next to this file (and the example in tests/)."""
import os, io, json, math, hashlib, random
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YELLOW = (255, 226, 0); RED = (216, 44, 44); INK = (31, 36, 48); GREYT = (70, 74, 84)
KINDS = {'highlight', 'underline', 'ellipse', 'arrow'}
SRC_REQUIRED = ['file', 'sha256', 'url', 'publisher', 'title', 'published', 'retrieved', 'rights', 'claim_ids']


class SpecError(ValueError):
    pass


def _sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()


def ease(u): u = min(1.0, max(0.0, u)); return u * u * (3 - 2 * u)


def crop_at(spec, t):
    ks = spec['camera']
    if t <= ks[0]['t']: return list(ks[0]['crop'])
    for a, b in zip(ks, ks[1:]):
        if t < b['t']:
            u = ease((t - a['t']) / (b['t'] - a['t'])) if b['t'] > a['t'] else 1.0
            return [a['crop'][i] + (b['crop'][i] - a['crop'][i]) * u for i in range(4)]
    return list(ks[-1]['crop'])


def to_view(spec, crop, p):
    vw, vh = spec['viewport']['w'], spec['viewport']['h']
    return ((p[0] - crop[0]) * vw / crop[2], (p[1] - crop[1]) * vh / crop[3])


def progress(a, t):
    if t < a['start_s']: return 0.0
    if a.get('exit_s') is not None and t >= a['exit_s']: return 0.0
    if a['mode'] == 'instant': return 1.0
    return min(1.0, (t - a['start_s']) / (a['complete_s'] - a['start_s']))


def validate_spec(spec, base_dir='.'):
    """Raises SpecError listing every problem. Returns the (image width, height)."""
    errs = []; src = spec.get('source', {})
    for k in SRC_REQUIRED:
        if k not in src or src[k] in ('', None, []): errs.append(f'source.{k} missing')
    path = os.path.join(base_dir, src.get('file', ''))
    W = H = 0
    if os.path.isfile(path):
        if src.get('sha256') and _sha(path) != src['sha256']: errs.append('source checksum does not match the file (capture altered or wrong file)')
        with Image.open(path) as _i: W, H = _i.size
    else: errs.append(f'source file not found: {path}')
    vp = spec.get('viewport') or {}
    for k in ('x', 'y', 'w', 'h'):
        if k not in vp: errs.append(f'viewport.{k} missing')
    cam = spec.get('camera') or []
    if not cam: errs.append('camera needs at least one keyframe')
    if vp.get('w') and vp.get('h') and W:
        va = vp['w'] / vp['h']
        for i, k in enumerate(cam):
            x, y, w, h = k['crop']
            if abs(w / h - va) / va > 0.01: errs.append(f'camera[{i}] crop aspect {w/h:.3f} != viewport {va:.3f} (would distort the source)')
            if x < 0 or y < 0 or x + w > W + 1e-6 or y + h > H + 1e-6: errs.append(f'camera[{i}] crop leaves the document')
        if [k['t'] for k in cam] != sorted(k['t'] for k in cam): errs.append('camera keyframes not time-ordered')
    tm = spec.get('timing', {})
    if 'legible_s' not in tm: errs.append('timing.legible_s missing (first moment the target passage is readable)')
    seen = set()
    for a in spec.get('annotations', []):
        i = a.get('id', '?')
        if i in seen: errs.append(f'duplicate annotation id {i}')
        seen.add(i)
        if a.get('kind') not in KINDS: errs.append(f'{i}: kind {a.get("kind")!r} not in {sorted(KINDS)}')
        if a.get('mode') not in ('instant', 'progressive'): errs.append(f'{i}: mode must be instant|progressive')
        if not a.get('passage') or not a.get('claim_id'): errs.append(f'{i}: passage text and claim_id required')
        elif a['claim_id'] not in src.get('claim_ids', []): errs.append(f'{i}: claim_id {a["claim_id"]} not among source.claim_ids')
        if a.get('mode') == 'instant' and a.get('complete_s') != a.get('start_s'): errs.append(f'{i}: instant needs complete_s == start_s')
        if a.get('mode') == 'progressive' and not a.get('complete_s', 0) > a.get('start_s', 0): errs.append(f'{i}: progressive needs complete_s > start_s')
        if 'legible_s' in tm and a.get('start_s', 0) < tm['legible_s']: errs.append(f'{i}: starts before the passage is legible ({tm["legible_s"]})')
        if a.get('exit_s') is not None and a['exit_s'] <= a.get('complete_s', 0): errs.append(f'{i}: exit_s must follow complete_s')
        pts = [a['from'], a['to']] if a.get('kind') == 'arrow' else [a['rect'][:2], [a['rect'][0] + a['rect'][2], a['rect'][1] + a['rect'][3]]] if 'rect' in a else []
        if not pts: errs.append(f'{i}: geometry missing (rect or from/to)')
        if W and any(p[0] < 0 or p[1] < 0 or p[0] > W or p[1] > H for p in pts): errs.append(f'{i}: geometry outside the document (document-local px)')
        # annotation must be visible (inside the crop) at its start and completion
        if cam and 'rect' in a:
            for tt in (a['start_s'], a['complete_s']):
                cx, cy, cw, ch = crop_at(spec, tt); r = a['rect']
                if r[0] < cx - 1e-6 or r[1] < cy - 1e-6 or r[0] + r[2] > cx + cw + 1e-6 or r[1] + r[3] > cy + ch + 1e-6:
                    errs.append(f'{i}: target is outside the visible crop at t={tt}')
    for j, rc in enumerate(spec.get('required_context', [])):
        for a in spec.get('annotations', []):
            t0, t1 = a['start_s'], a.get('exit_s') or spec.get('duration_s', a['complete_s'])
            if rc.get('annotation') not in (None, a['id']): continue
            for k in range(11):
                tt = t0 + (t1 - t0) * k / 10; cx, cy, cw, ch = crop_at(spec, tt); r = rc['rect']; ar = a['rect']
                if ar[0] + ar[2] <= cx or ar[1] + ar[3] <= cy or ar[0] >= cx + cw or ar[1] >= cy + ch: continue   # mark is out of view: nothing to keep in context
                if r[0] < cx - 1e-6 or r[1] < cy - 1e-6 or r[0] + r[2] > cx + cw + 1e-6 or r[1] + r[3] > cy + ch + 1e-6:
                    errs.append(f'required_context[{j}] ({rc.get("why", "")}) hidden by crop while {a["id"]} is on screen (t={tt:.2f})'); break
    if errs: raise SpecError('; '.join(errs))
    return W, H


_img_cache = {}
def _src_img(spec, base_dir):
    p = os.path.join(base_dir, spec['source']['file'])
    if p not in _img_cache: _img_cache[p] = Image.open(p).convert('RGB')
    return _img_cache[p]


def _wob(pts, amp, seed):
    rng = random.Random(seed); ph = [rng.uniform(0, 6.28) for _ in range(3)]
    return [(x + amp * math.sin(i * 0.7 + ph[0]), y + amp * math.cos(i * 0.9 + ph[1])) for i, (x, y) in enumerate(pts)]


def _partial(pts, p):
    if p >= 1: return pts
    L = [math.dist(a, b) for a, b in zip(pts, pts[1:])]; tot = sum(L) * max(p, 1e-3); out = [pts[0]]
    for (a, b), l in zip(zip(pts, pts[1:]), L):
        if tot >= l: out.append(b); tot -= l
        else: out.append((a[0] + (b[0] - a[0]) * tot / l, a[1] + (b[1] - a[1]) * tot / l)); break
    return out


def draw_annotations(spec, t, crop, S=2):
    """RGBA overlay at S x viewport size, annotation geometry mapped through the SAME crop transform as the image."""
    vw, vh = spec['viewport']['w'], spec['viewport']['h']; zoom = vw / crop[2]
    ov = Image.new('RGBA', (vw * S, vh * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    tv = lambda p: tuple(c * S for c in to_view(spec, crop, p))
    for a in spec.get('annotations', []):
        p = progress(a, t)
        if p <= 0: continue
        sw = a.get('stroke_doc_px', 3.5) * zoom * S
        if a['kind'] == 'highlight':
            x0, y0 = tv(a['rect'][:2]); x1, y1 = tv((a['rect'][0] + a['rect'][2], a['rect'][1] + a['rect'][3]))
            lay = Image.new('RGBA', ov.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([x0, y0, x0 + (x1 - x0) * p, y1], fill=YELLOW + (110,))
            ov = Image.alpha_composite(ov, lay); d = ImageDraw.Draw(ov)
        elif a['kind'] == 'underline':
            x, y, w, h = a['rect']; pts = _wob([(x, y + h + 2), (x + w * 0.5, y + h + 3), (x + w, y + h + 1)], 0.6, a['id'])
            pp = [tv(q) for q in _partial(pts, p)]; d.line(pp, fill=RED + (255,), width=max(2, int(sw)), joint='curve')
        elif a['kind'] == 'ellipse':
            x, y, w, h = a['rect']; cx, cy = x + w / 2, y + h / 2; rx, ry = w / 2 * 1.1 + 6, h / 2 * 1.12 + 3
            pts = [(cx + rx * math.cos(math.radians(-110 + 380 * i / 48)), cy + ry * math.sin(math.radians(-110 + 380 * i / 48))) for i in range(49)]
            pp = [tv(q) for q in _partial(_wob(pts, 1.4, a['id']), p)]; d.line(pp, fill=RED + (255,), width=max(2, int(sw)), joint='curve')
        elif a['kind'] == 'arrow':
            (x0, y0), (x1, y1) = a['from'], a['to']; ang = math.atan2(y1 - y0, x1 - x0); L = 18
            pts = [(x0, y0), (x1, y1), (x1 - L * math.cos(ang - 0.5), y1 - L * math.sin(ang - 0.5)), (x1, y1), (x1 - L * math.cos(ang + 0.5), y1 - L * math.sin(ang + 0.5))]
            pp = [tv(q) for q in _partial(pts, p)]; d.line(pp, fill=RED + (255,), width=max(2, int(sw)), joint='curve')
    return ov.resize((vw, vh), Image.LANCZOS)


def _font(size):
    f = HERE + '/v1r4_assets/fonts_ofl/atkinsonhyperlegible_AtkinsonHyperlegible-Regular.ttf'
    return ImageFont.truetype(f, size)


def render_layer(spec, t, base_dir=HERE, canvas=(1920, 1080)):
    """Transparent canvas-size RGBA with the clipped document view, its annotations and the source tag."""
    vp = spec['viewport']; crop = crop_at(spec, t)
    view = _src_img(spec, base_dir).resize((vp['w'], vp['h']), Image.LANCZOS, box=(crop[0], crop[1], crop[0] + crop[2], crop[1] + crop[3])).convert('RGBA')
    view = Image.alpha_composite(view, draw_annotations(spec, t, crop))
    out = Image.new('RGBA', canvas, (0, 0, 0, 0)); out.paste(view, (vp['x'], vp['y']))
    d = ImageDraw.Draw(out); d.rectangle([vp['x'] - 1, vp['y'] - 1, vp['x'] + vp['w'], vp['y'] + vp['h']], outline=(150, 150, 150, 255), width=2)
    s = spec['source']; tag = f"Source: {s['publisher']}, “{s['title']}”. Published/reviewed: {s['published']}. Retrieved {s['retrieved']}."
    ft = _font(spec.get('tag_px', 38)); words = tag.split(); lines = ['']
    for w in words:   # wrap to the viewport width so the full identity (publisher, title, dates) stays readable
        if ft.getlength((lines[-1] + ' ' + w).strip()) > vp['w']: lines.append(w)
        else: lines[-1] = (lines[-1] + ' ' + w).strip()
    for i, ln in enumerate(lines): d.text((vp['x'], vp['y'] + vp['h'] + 12 + i * int(ft.size * 1.2)), ln, font=ft, fill=GREYT + (255,))
    return out


def event_table(spec, fps=24):
    """Frame-addressable event log for QA (frames at content fps)."""
    f = lambda t: int(round(t * fps))
    rows = [('source_entry', 0, f(0)), ('target_legible', spec['timing']['legible_s'], f(spec['timing']['legible_s']))]
    for a in spec.get('annotations', []):
        rows += [(f"{a['id']}:onset", a['start_s'], f(a['start_s'])), (f"{a['id']}:complete", a['complete_s'], f(a['complete_s']))]
        if a.get('exit_s') is not None: rows.append((f"{a['id']}:exit", a['exit_s'], f(a['exit_s'])))
    for k in spec['camera']: rows.append(('camera_keyframe', k['t'], f(k['t'])))
    return sorted(rows, key=lambda r: r[1])


def document_item(spec, t0, base_dir=HERE):
    """Integrates with the existing beat renderer: beat.add(document_item(spec, t0))."""
    import v1r4_render as r
    validate_spec(spec, base_dir)
    return r.dyn(t0, lambda tq: (render_layer(spec, tq - t0, base_dir), 0, 0))
