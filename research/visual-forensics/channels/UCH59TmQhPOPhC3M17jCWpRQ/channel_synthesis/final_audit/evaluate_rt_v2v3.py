# Independent evaluation of RT-V2-01 / RT-V3-01 renders: measured from rendered pixels, worker claims only used to locate windows.
# usage: python evaluate_rt_v2v3.py <RT folder> V2|V3   -> writes EVALUATION.json in that folder
import cv2, json, subprocess, sys, numpy as np
from pathlib import Path

d, kind = Path(sys.argv[1]), sys.argv[2]
tl = json.loads((d / 'timeline.json').read_text())
pr = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
     'stream=width,height,r_frame_rate,codec_name,nb_frames', '-of', 'json', str(d / 'rt.mp4')]))['streams'][0]
cap = cv2.VideoCapture(str(d / 'rt.mp4')); F = []
while True:
    ok, im = cap.read()
    if not ok: break
    F.append(im)
BOARD = np.array([0x3a, 0x4f, 0x3b])  # BGR of #3b4f3a
boxes = tl['boxes']

def content_rows(im, b):  # (top, bottom, height) of rows inside box holding non-board pixels
    x0, y0, x1, y1 = b; roi = im[y0:y1, x0:x1].astype(int)
    m = np.abs(roi - BOARD).sum(2) > 60; r = np.nonzero(m.sum(1) > 20)[0]
    return (y0 + int(r.min()), y0 + int(r.max()), int(r.max() - r.min() + 1)) if len(r) else (None, None, 0)

def diffs(a, b):
    return [float(np.abs(F[i].astype(int) - F[i - 1].astype(int)).mean()) for i in range(a, b + 1)]

crit = {'format': dict(ok=(pr['width'], pr['height'], pr['r_frame_rate'], pr['codec_name']) == (1920, 1080, '30000/1001', 'h264'), got=pr)}
px = F[len(F) // 2][100, 320]; crit['board_colour'] = dict(ok=bool(np.abs(px.astype(int) - BOARD).max() <= 6), got_bgr=px.tolist())

if kind == 'V2':
    s = tl['SQ_collapse_start']; win = range(max(1, s - 3), min(len(F), s + 10))
    h = {i: content_rows(F[i], boxes['panel'])[2] for i in win}; full = h[win[0]]
    moving = [i for i in win if h[i] != h[win[0]] and abs(h[i] - full) > 3]
    band = [i for i in moving if h[i] <= 0.3 * full]
    settled_after = next((i for i in win if i > (moving[-1] if moving else s) and abs(h[i] - full) <= 3), None)
    over = max(h.values()) > full * 1.02
    crit['M_SQUASH_SWAP'] = dict(ok=bool(moving) and 5 <= len(moving) <= 7 and 1 <= len(band) <= 3 and not over,
        heights=h, changed_frames=len(moving), band_frames=band, overshoot=over, band_frac=round(min(h.values()) / full, 3),
        want='collapse 2 + band 2 + expand 2 frames (+-1), band 0.20-0.25, no overshoot')
    a, b = tl['CAM_start'], tl['CAM_end']; dd = diffs(max(1, a - 3), min(len(F) - 1, b + 5))
    idx = list(range(max(1, a - 3), min(len(F) - 1, b + 5) + 1)); mv = [i for i, v in zip(idx, dd) if v > 0.3]
    held = [i for i in range(mv[0], mv[-1] + 1) if i not in mv] if mv else []
    seg = [v for i, v in zip(idx, dd) if i in mv]; pk = int(np.argmax(seg)) if seg else -1
    crit['M_CAMERA_PUSH_EASE'] = dict(ok=bool(mv) and 15 <= len(mv) <= 19 and not held and len(seg) // 3 <= pk < 2 * len(seg) // 3 + 1
        and seg[0] < seg[pk] * 0.7 and seg[-1] < seg[pk] * 0.7,
        moving_frames=len(mv), held_frames=held, peak_offset=pk, profile=[round(v, 2) for v in seg],
        want='16-18 moving frames, no held frames, ease-in-out peak in middle third')
else:
    s = tl['POP_new_onset']; win = range(max(1, s - 4), min(len(F), s + 12))
    h = {i: content_rows(F[i], boxes['panel'])[2] for i in win}; settled = h[win[-1]]
    on = next((i for i in win if i >= s - 1 and h[i] > 0 and h[i - 1] == 0), None)
    seq = [round(h[i] / settled, 3) for i in range(on, on + 6)] if on else []
    crit['M_INSET_POP_OVERSHOOT'] = dict(ok=bool(seq) and 0.70 <= seq[0] <= 0.84 and 1.03 <= max(seq[1:3]) <= 1.075 and all(abs(x - 1) <= 0.01 for x in seq[3:]),
        onset=on, height_fraction_seq=seq, heights=h, gap_frames=[i for i in win if h[i] == 0],
        want='0.77, ~1.055, ~1.05, then 1.00')
    p = tl['PIN_appear']; x0, y0, x1, y1 = boxes['element']
    ch = [float(np.abs(F[i][y0:y1, x0:x1].astype(int) - F[i - 1][y0:y1, x0:x1].astype(int)).mean()) for i in range(p - 3, p + 6)]
    big = [p - 3 + k for k, v in enumerate(ch) if v > 1.0]
    crit['M_SINGLE_FRAME_POP_IN'] = dict(ok=len(big) == 1, change_frames=big, per_frame_change=[round(v, 2) for v in ch],
        want='exactly one changing frame at appearance, no intermediate')
crit['claims'] = {k: v for k, v in tl.items() if k != 'boxes'}
res = {'test': d.name, 'frames': len(F), 'criteria': crit,
       'overall': 'PASS' if all(v.get('ok', True) for k, v in crit.items() if k != 'claims') else 'FAIL',
       'scope': 'timing/geometry of named modules only; style, characters, sound NOT tested'}
(d / 'EVALUATION.json').write_text(json.dumps(res, indent=1, default=int)); print(json.dumps(res, indent=1, default=int)[:2500])
