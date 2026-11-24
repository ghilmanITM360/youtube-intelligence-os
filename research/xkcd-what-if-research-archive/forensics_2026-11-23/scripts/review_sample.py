"""Pick a stratified sample of measured shots and build review sheets.
Each cell = [frame just before shot start | shot keyframe | frame just after shot start].
Seed fixed. Writes review_sample/SAMPLE.csv and sheets."""
import csv, os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from ledger_lib import media

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = R + '/ledgers_measured'
O = R + '/review_sample'; os.makedirs(O + '/cells', exist_ok=True)
idx = {r['video_id']: r for r in csv.DictReader(open(L + '/INDEX.csv'))}
shots = [r for r in csv.DictReader(open(L + '/ALL_SHOT_LEDGER.csv'))
         if r['shot_id'] != 'SH001' and r['keyframe'] and r['boundary_strength']]
rnd = random.Random(7)
pick = []
for fmt, n in (('LONG', 12), ('SHORT', 12)):
    vids = sorted(v for v, r in idx.items() if r['format'] == fmt and r['status'].startswith('MEASURED'))
    rnd.shuffle(vids)
    for i, v in enumerate(vids[:n]):
        pool = [s for s in shots if s['video_id'] == v]
        pool.sort(key=lambda s: float(s['boundary_strength']))
        # alternate low-strength and high-strength shots to test strength later
        half = len(pool) // 2
        pool = pool[:half] if i % 2 == 0 else pool[half:]
        pick.append((fmt, rnd.choice(pool)))

def grab(path, t, out, w):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(t,0):.3f}', '-i', path, '-frames:v', '1',
                    '-vf', f'scale={w}:-2', out], check=True)

rows = []
for k, (fmt, s) in enumerate(pick, 1):
    v = s['video_id']; p = media(v)
    st = float(s['start_pts_seconds']); en = float(s['end_pts_seconds'])
    w = 384 if fmt == 'LONG' else 162
    c = f'{O}/cells/{k:02d}'
    grab(p, st - 0.25, c + '_a.jpg', w)
    grab(p, st + 0.25, c + '_c.jpg', w)
    subprocess.run(['cp', f"{L}/{v}/{s['keyframe']}", c + '_k_src.jpg'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', c + '_k_src.jpg', '-vf', f'scale={w}:-2', c + '_b.jpg'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', c + '_a.jpg', '-i', c + '_b.jpg', '-i', c + '_c.jpg',
                    '-filter_complex', 'hstack=3', c + '.jpg'], check=True)
    rows.append(dict(n=k, fmt=fmt, video_id=v, shot_id=s['shot_id'], start=st, end=en,
                     boundary_strength=s['boundary_strength'], asr_text=s['asr_text'][:200]))
w = csv.DictWriter(open(O + '/SAMPLE.csv', 'w', newline=''), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(rows)

def sheet(ns, cols, name):
    ins = [];
    for n in ns: ins += ['-i', f'{O}/cells/{n:02d}.jpg']
    rws = (len(ns) + cols - 1) // cols
    lay = '|'.join(f'{(i%cols)}_0' if False else '' for i in range(0))  # unused
    # build with hstack per row then vstack
    parts = []; fc = []
    for r in range(rws):
        sub = list(range(r * cols, min(len(ns), (r + 1) * cols)))
        if len(sub) == 1: fc.append(f'[{sub[0]}:v]copy[r{r}]')
        else: fc.append(''.join(f'[{i}:v]' for i in sub) + f'hstack={len(sub)}[r{r}]')
    fc.append(''.join(f'[r{r}]' for r in range(rws)) + f'vstack={rws}[o]' if rws > 1 else '[r0]copy[o]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', ';'.join(fc), '-map', '[o]', name], check=True)

for j in range(0, 12, 6):
    sheet(list(range(1 + j, 7 + j)), 1, f'{O}/long_{j//6+1}.jpg')
for j in range(12, 24, 6):
    sheet(list(range(1 + j, 7 + j)), 2, f'{O}/short_{(j-12)//6+1}.jpg')
print(len(rows), 'cells; sheets: long_1,2 short_1,2')
