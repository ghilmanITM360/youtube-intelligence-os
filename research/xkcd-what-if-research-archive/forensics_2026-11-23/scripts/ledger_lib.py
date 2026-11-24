"""Machine-measured shot and visual-event ledgers from frame differences (no viewing, no interpretation).
Per frame i>=1: d = |gray[i]-gray[i-1]| on a downscaled gray frame. changed fraction = share of pixels with d > T_PIX.
HARD_CUT frame: changed fraction >= CUT_FRAC. ACTIVE frame: changed fraction >= ACT_FRAC (and not a cut). Active frames within GAP frames merge into one event.
Run with: uv run --no-project --with numpy python <script>."""
import glob, subprocess, numpy as np
LIB = '/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
P = dict(T_PIX=24, ACT_FRAC=0.0004, CUT_FRAC=0.08, CUT_BW=0.5, CUT_BH=0.5, GAP=2)  # frozen after tuning on 5 campaign videos (see ledger_tune*.py)

def media(vid): return glob.glob(LIB + f'*[[]{vid}[]].mp4')[0]

def probe(path):
    o = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,nb_frames', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout.strip().split(',')
    w, h, r, n = int(o[0]), int(o[1]), o[2].split('/'), o[3]
    return w, h, int(r[0]) / int(r[1]), (int(n) if n.isdigit() else None)

def frames(path, w, h):
    sw, sh = (256, 144) if w >= h else (144, 256)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={sw}:{sh}:flags=area,format=gray', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], stdout=subprocess.PIPE)
    n = sw * sh; buf = b''; out = []
    while True:
        b = p.stdout.read(n * 64)
        if not b: break
        buf += b; k = len(buf) // n
        out.append(np.frombuffer(buf[:k * n], np.uint8).reshape(k, sh, sw)); buf = buf[k * n:]
    p.wait(); return np.concatenate(out), sw, sh

def measure(path, **kw):
    q = {**P, **kw}; w, h, fps, _ = probe(path); F, sw, sh = frames(path, w, h)
    F16 = F.astype(np.int16); D = np.abs(F16[1:] - F16[:-1]) > q['T_PIX']
    frac = D.reshape(len(D), -1).mean(1)
    dark = (F < 96).reshape(len(F), -1).sum(1).astype(np.int64); ink = (dark[1:] - dark[:-1]) / (sw * sh)
    bbox = []
    for k in range(len(D)):
        if frac[k] >= q['ACT_FRAC']:
            r = np.where(D[k].any(1))[0]; c = np.where(D[k].any(0))[0]
            bbox.append((c[0] / sw, r[0] / sh, (c[-1] + 1) / sw, (r[-1] + 1) / sh))
        else: bbox.append(None)
    cut = np.array([bool(f >= q['CUT_FRAC'] and b and (b[2] - b[0]) >= q['CUT_BW'] and (b[3] - b[1]) >= q['CUT_BH']) for f, b in zip(frac, bbox)]); act = frac >= q['ACT_FRAC']  # a cut frame is also an event frame
    return dict(fps=fps, n=len(F), w=w, h=h, sw=sw, sh=sh, frac=frac, ink=ink, bbox=bbox, cut=cut, act=act, q=q)

def segments(m):
    """Return (cuts, events). cuts: frame indices (index of first frame of new shot). events: dicts."""
    q = m['q']; cuts = [int(i) + 1 for i in np.where(m['cut'])[0]]
    cuts = [c for j, c in enumerate(cuts) if j == 0 or c - cuts[j - 1] > 2]  # a cut spanning 2 frames counts once
    ev, cur = [], None
    for k in np.where(m['act'])[0]:
        f = int(k) + 1
        if cur and f - cur['end_frame'] <= q['GAP'] + 1: cur['end_frame'] = f; cur['idx'].append(int(k))
        else:
            if cur: ev.append(cur)
            cur = dict(start_frame=f, end_frame=f, idx=[int(k)])
    if cur: ev.append(cur)
    for e in ev:
        bb = [m['bbox'][i] for i in e['idx'] if m['bbox'][i]]
        e['bbox'] = (min(b[0] for b in bb), min(b[1] for b in bb), max(b[2] for b in bb), max(b[3] for b in bb))
        e['peak_frac'] = float(max(m['frac'][i] for i in e['idx'])); e['ink'] = float(sum(m['ink'][i] for i in e['idx']))
        e['frames'] = e['end_frame'] - e['start_frame'] + 1
        e['has_cut'] = any(bool(m['cut'][i]) for i in e['idx'])
    return cuts, ev
