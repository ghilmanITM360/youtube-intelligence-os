# Deterministic C1-C5 for style/full-scene RTs (criteria pre-registered in each test's PREREGISTERED_CRITERION.json).
# usage: evaluate_style_rt.py TEST_ID MP4 OUT.json   (TEST_ID in RT-V1-S01/RT-V2-S01/RT-V3-S01)
import csv, json, subprocess, sys, cv2, numpy as np
from pathlib import Path
H = Path(__file__).resolve().parent; PY = sys.executable; tid, mp4, out = sys.argv[1], sys.argv[2], Path(sys.argv[3])
pr = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,codec_name', '-of', 'json', mp4]))['streams'][0]
dcsv = out.with_suffix('.dense.csv'); subprocess.run([PY, H / 'dense_motion.py', mp4, dcsv], check=True, capture_output=True)
D = [{k: (float(v) if k not in ('residual_bbox',) and v != '' else v) for k, v in r.items()} for r in csv.DictReader(open(dcsv))]; n = len(D)
cap = cv2.VideoCapture(mp4); F = []
while True:
    ok, im = cap.read()
    if not ok: break
    F.append(im)
def frac(im, hexes, tol):
    px = im.reshape(-1, 3).astype(int); m = np.zeros(len(px), bool)
    for h in hexes:
        bgr = np.array([int(h[5:7], 16), int(h[3:5], 16), int(h[1:3], 16)]); m |= np.abs(px - bgr).sum(1) <= tol
    return round(float(m.mean()), 3)
def run(th):  # longest run of frames with |dscale|>th
    best, cur = (0, -1), None
    for r in D[1:]:
        if abs(r['dscale']) > th or abs(r['dx']) > 6: cur = (cur[0], int(r['frame'])) if cur and cur[1] == r['frame'] - 1 else (int(r['frame']), int(r['frame']))
        else: cur = None
        if cur and cur[1] - cur[0] > best[1] - best[0]: best = cur
    return best
C = {}; fmt = (pr['width'], pr['height'], pr['r_frame_rate'], pr['codec_name']) == (1920, 1080, '30000/1001', 'h264')
rng = {'RT-V1-S01': (156, 160), 'RT-V2-S01': (206, 210), 'RT-V3-S01': (177, 181)}[tid]
nf = int(subprocess.check_output(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', mp4]).decode().strip())
C['C1'] = dict(ok=fmt and rng[0] <= nf <= rng[1] and nf == n, got=pr, frames_ffprobe=nf, frames_decoded_cv2=n)
if tid == 'RT-V1-S01':
    a = frac(F[-1], ['#f8f8f8'], 40); b = frac(F[-1], ['#784828', '#885828'], 60); C['C2'] = dict(ok=a >= .55 and b >= .08, bg=a, brown=b)
    s, e = run(0.003); seg = [D[i]['dscale'] for i in range(s, e + 1)]; tot = sum(seg); L = len(seg); pk = int(np.argmax(np.abs(seg))) if seg else -1
    C['C3'] = dict(ok=-0.95 <= tot <= -0.70 and 11 <= L <= 17 and 20 <= s <= 28, run=(s, e), sum_dscale=round(tot, 3), length=L)
    C['C4'] = dict(ok=L > 2 and L // 3 <= pk < L - L // 3 and abs(seg[0]) < .6 * abs(seg[pk]) and abs(seg[-1]) < .6 * abs(seg[pk]), peak_offset=pk, profile=[round(x, 3) for x in seg])
    bad = [int(r['frame']) for r in D[1:] if (1 <= r['frame'] <= 19 or r['frame'] >= 45) and (abs(r['dscale']) >= .003 or abs(r['dx']) >= 2) and r['inliers'] >= 12]
    C['C5'] = dict(ok=not bad, camera_frames_outside=bad[:20])
elif tid == 'RT-V2-S01':
    m = F[n // 2]; a = frac(m, ['#68c8d8', '#68b8d8'], 50); g = frac(m, ['#789838'], 60); sk = frac(m, ['#c8f8f8', '#d8f8f8'], 50)
    C['C2'] = dict(ok=a >= .30 and g >= .08 and sk >= .08, water=a, grass=g, sky=sk)
    sd = sum(r['dscale'] for r in D[1:]); sx = sum(r['dx'] for r in D[1:]); C['C3'] = dict(ok=abs(sd) < .01 and abs(sx) < 15, sum_dscale=round(sd, 4), sum_dx=round(sx, 1))
    rf = [(int(r['frame']), r['residual_frac12']) for r in D[1:]]; on = []
    for f, v in sorted([x for x in rf if 40 <= x[0] <= 130], key=lambda x: -x[1]):
        if v > 0.0005 and all(abs(f - o) >= 20 for o in on): on.append(f)
    C['C4'] = dict(ok=len(on) >= 3, onsets=sorted(on)[:6])
    mv = [f for f, v in rf if f >= 130 and v > 0.0002]; longest = cur = 0; pf = None
    for f in mv: cur = cur + 1 if pf == f - 1 else 1; longest = max(longest, cur); pf = f
    C['C5'] = dict(ok=longest >= 40, longest_local_run=longest)
else:
    a = frac(F[-1], ['#484828', '#485828'], 50); t = frac(F[-1], ['#c89858'], 60); w = frac(F[-1], ['#683818'], 60)
    C['C2'] = dict(ok=a >= .25 and t >= .06 and w >= .05, board=a, wall=t, wood=w)
    # C3 v2 (pre-registered after source calibration): main push end = first f with scale[f+8]-scale[f] < 0.01 after the move starts
    tj = out.with_suffix('.traj.json'); subprocess.run([PY, H / 'cam_traj.py', mp4, '0', str(n - 1), tj], check=True, capture_output=True)
    A = json.loads(tj.read_text())['rows']; S = [r['scale'] for r in A]
    mv0 = next((i for i in range(len(S) - 8) if S[i + 8] - S[i] >= 0.01), 0)
    e = next((f for f in range(mv0, len(S) - 8) if S[f + 8] - S[f] < 0.01), len(S) - 1); scf = S[e]
    s = next(i for i, x in enumerate(S) if (x - 1) > .02 * (scf - 1)); R = A[s:e + 1]; sc = scf; tx = A[e]['tx']; L = e - s + 1
    C['C3'] = dict(ok=1.55 <= sc <= 1.85 and -800 <= tx <= -540 and 40 <= L <= 60 and 5 <= s <= 16, run=(s, e), scale=round(sc, 3), tx=round(tx), length=L)
    p = [(r['scale'] - 1) / (sc - 1) for r in R]; k = len(p); half = next(i for i, x in enumerate(p) if x >= .5) / (k - 1)
    C['C4'] = dict(ok=.35 <= half <= .6 and max(p[:max(1, int(.15 * k))]) < .15 and min(p[k - max(1, int(.15 * k)):]) > .85, half_at=round(half, 3), progress=[round(x, 2) for x in p[::4]])
    bad = [int(r['frame']) for r in D if r['frame'] >= e + 2 and (abs(r['dscale']) >= .003 or abs(r['dx']) >= 2) and r['inliers'] >= 12]
    extra = S[-1] / scf; C['C5'] = dict(ok=not bad and 1.0 <= extra <= 1.06, camera_frames_after=bad[:20], extra_scale=round(extra, 4))
res = dict(test=tid, mp4=mp4, criteria=C, deterministic='PASS' if all(v['ok'] for v in C.values()) else 'FAIL', C6='visual, recorded separately')
out.write_text(json.dumps(res, indent=1, default=lambda x: x if not hasattr(x, 'item') else x.item())); print(json.dumps({k: (v['ok'], {a: b for a, b in v.items() if a not in ('got', 'profile', 'progress')}) for k, v in C.items()}))
