"""Assemble RETRO_002 from Codex Batch 0b parts: instance one face-disc sprite (3 variants) on the 100 measured recess centres.
Outputs (Claude-made, 'assembled by Claude' not Codex art): assets/retro/retro_array_assembled_1254.png + _2508_resampled.png + instance list JSON.
usage: ~/.venvs/uepipe/bin/python tools/assemble_retro_array.py
"""
import json, os, random
import numpy as np
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(R, 'codex_handoff', 'deliveries', 'batch0b')
O = os.path.join(R, 'assets', 'retro'); os.makedirs(O, exist_ok=True)
plate = Image.open(os.path.join(B, 'retro_array_plate_empty.png')).convert('RGBA')
g = json.load(open(os.path.join(B, 'recess_grid.json')))
cs = g['centres']; assert len(cs) == 100, len(cs)
xs = sorted(c['x'] for c in cs); ys = sorted(c['y'] for c in cs)
px = np.median(np.diff(sorted({round(c['x']) // 20 for c in cs}))) # unused guard
cols = {}
for c in cs: cols.setdefault(c['col'], []).append(c['x'])
rows = {}
for c in cs: rows.setdefault(c['row'], []).append(c['y'])
pitch_x = np.mean(np.diff([np.mean(cols[k]) for k in sorted(cols)])); pitch_y = np.mean(np.diff([np.mean(rows[k]) for k in sorted(rows)]))
D = int(round(0.86 * min(pitch_x, pitch_y)))
discs = []
for n in 'abc':
    im = Image.open(os.path.join(B, 'retro_face_disc_%s.png' % n)).convert('RGBA')
    a = np.array(im.getchannel('A')); ys_, xs_ = np.where(a >= 128)
    im = im.crop((xs_.min(), ys_.min(), xs_.max() + 1, ys_.max() + 1)).resize((D, D), Image.LANCZOS)
    arr = np.array(im); arr[arr[..., 3] == 0, :3] = 0  # repaired by Claude: RGB 0 where alpha 0
    discs.append(Image.fromarray(arr))
random.seed(7); out = plate.copy(); inst = []
for c in sorted(cs, key=lambda c: (c['row'], c['col'])):
    k = random.choice([0, 0, 1, 2]) if True else 0
    out.alpha_composite(discs[k], (int(round(c['x'] - D / 2)), int(round(c['y'] - D / 2))))
    inst.append(dict(row=c['row'], col=c['col'], x=c['x'], y=c['y'], variant='abc'[k]))
assert len(inst) == 100
# repair by Claude: the generated panel is ~5% taller than wide; make it square (the real panel is square), keep canvas, record the y-scale
bb = out.getchannel('A').point(lambda v: 255 if v >= 128 else 0).getbbox(); w, h = bb[2] - bb[0], bb[3] - bb[1]
sq = out.crop(bb).resize((w, w), Image.LANCZOS); canvas = Image.new('RGBA', out.size, (0, 0, 0, 0))
canvas.alpha_composite(sq, (bb[0], bb[1] + (h - w) // 2)); out = canvas; yscale = w / h
out.save(os.path.join(O, 'retro_array_assembled_1254.png'))
out.resize((2508, 2508), Image.LANCZOS).save(os.path.join(O, 'retro_array_assembled_2508_resampled.png'))
json.dump(dict(y_scale_applied=yscale, note='instance x,y are PRE-squash plate coordinates', count=len(inst), disc_px=D, pitch_x=float(pitch_x), pitch_y=float(pitch_y), instances=inst), open(os.path.join(O, 'retro_array_instances.json'), 'w'), indent=1)
print('assembled 100 instances, disc %dpx, pitch %.1f x %.1f' % (D, pitch_x, pitch_y))
