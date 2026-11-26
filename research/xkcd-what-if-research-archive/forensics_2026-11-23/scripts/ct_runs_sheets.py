"""Review sheets for candidate HOLD-residual runs. Cell = [frame before peak | peak frame | amplified (x8) difference], cropped to the padded run bbox, label on top.
12 cells per sheet (2 columns x 6). usage: uv run --no-project --with numpy --with pillow python scripts/ct_runs_sheets.py <name> <shape,shape..> [control_n] [exclude_cells_csv]
Writes ct_scan_batch/run_review/<name>_NN.jpg and <name>_cells.csv (cell number -> video/run/frame)."""
import csv, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__)); import ledger_lib as L
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B = R + '/ct_scan_batch'; O = B + '/run_review'; os.makedirs(O, exist_ok=True)
name, shapes = sys.argv[1], sys.argv[2].split(','); ctl = int(sys.argv[3]) if len(sys.argv) > 3 else 0
rows = [r for r in csv.DictReader(open(B + '/CANDIDATE_RUNS_TRIAGE.csv')) if r['shape'] in shapes]
if ctl: random.Random(5).shuffle(rows); rows = rows[:ctl]
if len(sys.argv) > 4:  # optional 4th arg: cells csv of runs already viewed, excluded here
    done = {(r['video_id'], r['run']) for r in csv.DictReader(open(sys.argv[4]))}; rows = [r for r in rows if (r['video_id'], r['run']) not in done]
rows.sort(key=lambda r: (r['video_id'], int(r['start'])))
CH = 150
def cell(r, fb, fp, W, H):
    x0, y0, x1, y1 = map(float, r['bbox'].split(',')); cx, cy = (x0 + x1) / 2 * W, (y0 + y1) / 2 * H
    bw, bh = max((x1 - x0) * W + 120, 0.2 * W), max((y1 - y0) * H + 120, 0.2 * H)
    asp = 1.6; bw, bh = (max(bw, bh * asp), max(bh, bw / asp)) if W >= H else (max(bw, bh * 0.6), max(bh, bw / 0.6))
    xa, ya = int(max(0, min(W - bw, cx - bw / 2))), int(max(0, min(H - bh, cy - bh / 2))); xb, yb = int(min(W, xa + bw)), int(min(H, ya + bh))
    a, b = fb[ya:yb, xa:xb], fp[ya:yb, xa:xb]
    d = np.clip(np.abs(b.astype(np.int16) - a.astype(np.int16)).max(2) * 8, 0, 255).astype(np.uint8); dd = np.stack([d] * 3, 2)
    ims = [Image.fromarray(x).resize((int(CH * (xb - xa) / (yb - ya)), CH)) for x in (a, b, dd)]
    im = Image.new('RGB', (sum(i.width for i in ims) + 8, CH + 14), 'white'); x = 0
    for i in ims: im.paste(i, (x, 14)); x += i.width + 4
    ImageDraw.Draw(im).text((2, 1), f"#{r['_n']} {r['video_id']} run{r['run']} f{r['peak_frame']} {r['peak_px']}px {r['shape']} share{r['bbox_share']}", fill='black'); return im
by = {}
for n, r in enumerate(rows, 1): r['_n'] = n; by.setdefault(r['video_id'], []).append(r)
cells = {}
for v, rs in by.items():
    p = L.media(v); w, h, _, _ = L.probe(p); need = sorted({int(r['peak_frame']) + k for r in rs for k in (-1, 0)})
    fr = {}
    for c in range(0, len(need), 40):  # chunk: a long select expression makes ffmpeg fail
        part = need[c:c + 40]; sel = '+'.join(f'eq(n\\,{x})' for x in part)
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'select={sel}', '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        assert len(raw) == len(part) * w * h * 3, (v, c, len(raw))
        fr.update({f: np.frombuffer(raw[i * w * h * 3:(i + 1) * w * h * 3], np.uint8).reshape(h, w, 3) for i, f in enumerate(part)})
    for r in rs: pk = int(r['peak_frame']); cells[r['_n']] = cell(r, fr[pk - 1], fr[pk], w, h)
for s in range(0, len(rows), 12):
    ns = list(range(s + 1, min(s + 13, len(rows) + 1))); cw = max(cells[n].width for n in ns)
    sh = Image.new('RGB', (cw * 2 + 10, 6 * (CH + 18)), (230, 230, 230))
    for k, n in enumerate(ns): sh.paste(cells[n], ((k % 2) * (cw + 10), (k // 2) * (CH + 18)))
    sh.save(f'{O}/{name}_{s//12+1:02d}.jpg', quality=85)
w = csv.DictWriter(open(f'{O}/{name}_cells.csv', 'w', newline=''), fieldnames=[k for k in rows[0]]); w.writeheader(); w.writerows(rows)
print(len(rows), 'cells', (len(rows) + 11) // 12, 'sheets')
