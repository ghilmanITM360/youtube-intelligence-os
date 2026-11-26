"""For the largest sub-threshold changes in HOLD frames of the span, render [previous frame | frame | amplified difference]."""
import csv, os, subprocess, sys, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import ledger_lib as L
v = '9VG0yqq_PHM'; R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D = f'{R}/ct_scan_pilot_{v}/span_960_1679'
rows = list(csv.DictReader(open(D + '/fullres_changes.csv')))
hold = [r for r in rows if r['machine_state'] == 'HOLD' and int(r['px_gt8']) >= 15]
runs = []; cur = []
for r in hold:
    f = int(r['frame'])
    if cur and f - int(cur[-1]['frame']) <= 2: cur.append(r)
    else:
        if cur: runs.append(cur)
        cur = [r]
if cur: runs.append(cur)
print('HOLD frames with >=15 px >8 grey:', len(hold), 'in', len(runs), 'runs; run lengths', [len(x) for x in runs])
print('runs (start frame, frames, peak px, bbox of peak):', [(int(x[0]['frame']), len(x), max(int(y['px_gt8']) for y in x), max(x, key=lambda y: int(y['px_gt8']))['bbox_gt8']) for x in runs])
# render the 8 runs with the largest peak
top = sorted(runs, key=lambda x: -max(int(y['px_gt8']) for y in x))[:8]
p = L.media(v); w, h, _, _ = L.probe(p)
def frame(n):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'select=eq(n\\,{n}),format=gray', '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.uint8).reshape(h, w)
os.makedirs(D + '/diff', exist_ok=True)
for x in top:
    r = max(x, key=lambda y: int(y['px_gt8'])); n = int(r['frame'])
    a, b = frame(n - 1), frame(n); d = np.abs(a.astype(np.int16) - b.astype(np.int16)); amp = 255 - np.minimum(d * 8, 255).astype(np.uint8)
    for name, arr in (('a', a), ('b', b), ('d', amp)): open(f'{D}/diff/{n}_{name}.pgm', 'wb').write(b'P5 %d %d 255\n' % (w, h) + arr.tobytes())
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + sum([['-i', f'{D}/diff/{n}_{k}.pgm'] for k in 'abd'], []) + ['-filter_complex', '[0:v]scale=480:-2[a];[1:v]scale=480:-2[b];[2:v]scale=480:-2[d];[a][b][d]hstack=3', f'{D}/diff/diff_{n}.jpg'], check=True)
    for k in 'abd': os.remove(f'{D}/diff/{n}_{k}.pgm')
print('rendered', [int(max(x, key=lambda y: int(y['px_gt8']))['frame']) for x in top])
