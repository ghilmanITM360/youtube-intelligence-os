"""Claude composite (documented, non-destructive): map the 10x10 corner-cube array (assets/retro/retro_array_assembled_1254.png,
100 Codex Batch-0b cube parts assembled by Claude) into the plain dark panel of Codex's B5PR reflector layer with a perspective warp.
Why: the real Apollo 11 panel shows 100 round cube openings (AS11-40-5952); Codex's one-defect edit B5PR2 re-rendered the whole
object (IoU 0.327) and was rejected. Panel quad measured on the dark region of B5PR (approxPolyDP), inset 3 %.
usage: ~/.venvs/uepipe/bin/python tools/composite_reflector_array.py"""
import os
import numpy as np, cv2
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets/rigs/astronaut_retro/interaction_reflector_only.png')
ARR = os.path.join(ROOT, 'assets/retro/retro_array_assembled_1254.png')
OUT = os.path.join(ROOT, 'assets/rigs/astronaut_retro/interaction_reflector_arraycomp.png')
r = np.asarray(Image.open(SRC).convert('RGBA')).astype(np.float32)
dark = ((r[..., :3].mean(2) < 70) & (r[..., 3] > 200)).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(dark); k = 1 + np.argmax(st[1:, 4]); m = (lab == k).astype(np.uint8) * 255
c = max(cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea)
q = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True).reshape(-1, 2).astype(np.float32)
assert len(q) == 4, 'panel is not a quad: %s' % q
q = q[np.argsort(np.arctan2(q[:, 1] - q[:, 1].mean(), q[:, 0] - q[:, 0].mean()))]          # sort by angle: TL? -> order below
ctr = q.mean(0); q = ctr + (q - ctr) * 0.97
# order: top-left (min x+y), top-right, bottom-right, bottom-left in image terms of the panel's own axes
s = q.sum(1); d = q[:, 0] - q[:, 1]
TL, BR = q[np.argmin(s)], q[np.argmax(s)]; TR, BL = q[np.argmax(d)], q[np.argmin(d)]
a = np.asarray(Image.open(ARR).convert('RGBA')).astype(np.float32); x0, y0, x1, y1 = Image.open(ARR).getbbox()
H = cv2.getPerspectiveTransform(np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1]]), np.float32([TL, TR, BR, BL]))
w = cv2.warpPerspective(a, H, (r.shape[1], r.shape[0]), flags=cv2.INTER_AREA, borderMode=cv2.BORDER_CONSTANT)
w[..., :3] *= 0.78                                                     # panel faces away from the Sun a little: match the frame's shade
al = (w[..., 3:4] / 255) * (r[..., 3:4] / 255)
out = r.copy(); out[..., :3] = w[..., :3] * al + r[..., :3] * (1 - al)
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), 'RGBA').save(OUT)
iou = ((out[..., 3] > 128) & (r[..., 3] > 128)).sum() / ((out[..., 3] > 128) | (r[..., 3] > 128)).sum()
print('wrote', OUT, 'quad', np.round([TL, TR, BR, BL]).tolist(), 'silhouette IoU vs B5PR %.3f' % iou)
