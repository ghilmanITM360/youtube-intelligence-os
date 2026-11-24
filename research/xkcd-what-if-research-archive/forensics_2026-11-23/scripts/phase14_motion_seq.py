"""Phase 14: dense frame sequences for the 16 shots whose camera motion was only INFERRED from stills (K16/K20).
For each shot: 9 frames from start-0.25 s every 0.25 s (native-resolution extraction with ffmpeg -ss), global translation between consecutive frames by phase correlation
(grayscale, 1/4 scale) and the residual after undoing it; sheets are viewed by the reviewer. Translation + low residual = pan-like; no shift but large residual = content change / zoom / cut.
usage: uv run --no-project --with numpy --with pillow --with scikit-image python scripts/phase14_motion_seq.py"""
import csv, os, subprocess, json
import numpy as np
from PIL import Image, ImageDraw
from skimage.registration import phase_cross_correlation
from skimage.transform import resize
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = A + '/phase14_motion'; os.makedirs(O + '/frames', exist_ok=True)
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
S = [r for r in csv.DictReader(open(A + '/review_sample/REVIEWED_SAMPLE.csv')) if 'PAN_OR_ZOOM' in r['camera_motion']]
print(len(S), 'camera-move-inferred shots')
def grab(v, t, jp):
    if not os.path.exists(jp):
        tmp = jp + '.png'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(t, 0):.3f}', '-i', inv[v]['local_media_path'], '-frames:v', '1', tmp], check=True)
        Image.open(tmp).convert('RGB').save(jp, quality=85); os.remove(tmp)
res = []; sheets = []
for i, r in enumerate(S):
    v = r['video_id']; t0 = float(r['start']) - 0.25; ims = []; gs = []
    for k in range(9):
        t = t0 + 0.25 * k; jp = f'{O}/frames/{v}_{r["shot_id"]}_{k}.jpg'; grab(v, t, jp); im = Image.open(jp); ims.append((t, im)); gs.append(resize(np.asarray(im.convert('L'), float) / 255, (im.height // 4, im.width // 4)))
    meas = []
    for a, b in zip(gs, gs[1:]):
        sh, err, _ = phase_cross_correlation(a, b, upsample_factor=2)
        al = np.roll(b, (int(round(sh[0])), int(round(sh[1]))), (0, 1)); resid = float(np.abs(a - al).mean()); raw = float(np.abs(a - b).mean())
        meas.append(dict(dy=float(sh[0]) * 4, dx=float(sh[1]) * 4, raw=round(raw, 4), resid=round(resid, 4)))
    mx = max(meas, key=lambda m: abs(m['dx']) + abs(m['dy']))
    res.append(dict(n=i + 1, video_id=v, shot_id=r['shot_id'], start=r['start'], fmt=r['fmt'], max_shift_px=round(abs(mx['dx']) + abs(mx['dy']), 1), max_dx=round(mx['dx'], 1), max_dy=round(mx['dy'], 1), max_raw_diff=max(m['raw'] for m in meas), min_resid_at_max_shift=mx['resid'], steps=meas, subject=r['subject'], prior_inference=r['camera_motion']))
    w = 320; h = int(w * ims[0][1].height / ims[0][1].width)
    cv = Image.new('RGB', (w * 5, h * 2 + 18), 'white'); d = ImageDraw.Draw(cv); d.text((4, 2), f'#{i+1} {v} {r["shot_id"]} start {r["start"]} {r["fmt"]}', fill='black')
    for k, (t, im) in enumerate(ims):
        cv.paste(im.resize((w, h)), ((k % 5) * w, 18 + (k // 5) * h)); d.text(((k % 5) * w + 3, 20 + (k // 5) * h), f'{t:.2f}', fill='red')
    sheets.append(cv)
for j in range(0, len(sheets), 3):
    grp = sheets[j:j + 3]; H = sum(s.height for s in grp); cv = Image.new('RGB', (grp[0].width, H), 'white'); y = 0
    for s in grp: cv.paste(s, (0, y)); y += s.height
    cv.save(f'{O}/sheet_{j // 3 + 1}.jpg', quality=82)
json.dump(res, open(A + '/14_MOTION_SEQUENCE_16.json', 'w'), indent=1)
for x in res: print(x['n'], x['video_id'], x['shot_id'], x['fmt'], 'shift', x['max_shift_px'], 'rawdiff', x['max_raw_diff'], 'resid', x['min_resid_at_max_shift'])
