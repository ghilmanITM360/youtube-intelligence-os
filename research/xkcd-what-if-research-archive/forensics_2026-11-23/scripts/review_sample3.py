"""Extend the review sample from 60 to 108 shots (48 new, seed 31), cells 61-108. Prioritisation: strata first, inside a stratum the videos with the fewest already-sampled shots come first (so every ledger video ends with at least one viewed shot where it has an eligible boundary).
Strata: format (LONG/SHORT) x absolute strength (<0.3 low, >=0.3 high), 9 each; videos with fewest sampled shots first.
Cell = [frame 0.25 s before shot start | keyframe | frame 0.25 s after start]."""
import csv, os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from ledger_lib import media

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = R + '/ledgers_measured'; O = R + '/review_sample'
idx = {r['video_id']: r for r in csv.DictReader(open(L + '/INDEX.csv'))}
done = {(r['video_id'], r['shot_id']) for r in csv.DictReader(open(O + '/SAMPLE.csv'))} | {(r['video_id'], r['shot_id']) for r in csv.DictReader(open(O + '/SAMPLE2.csv'))}
cnt = {}
for v, _ in done: cnt[v] = cnt.get(v, 0) + 1
shots = [r for r in csv.DictReader(open(L + '/ALL_SHOT_LEDGER.csv'))
         if r['shot_id'] != 'SH001' and r['keyframe'] and r['boundary_strength'] and (r['video_id'], r['shot_id']) not in done]
rnd = random.Random(31)
pick = []
for fmt in ('LONG', 'SHORT'):
    for low in (True, False):
        pool = [s for s in shots if idx[s['video_id']]['format'] == fmt and (float(s['boundary_strength']) < 0.3) == low]
        rnd.shuffle(pool); chosen = []
        for s in sorted(pool, key=lambda s: cnt.get(s['video_id'], 0)):
            if len(chosen) == 12: break
            chosen.append(s); cnt[s['video_id']] = cnt.get(s['video_id'], 0) + 1
        pick += [(fmt, s) for s in chosen]
rnd.shuffle(pick)
pick.sort(key=lambda x: x[0] != 'LONG')  # long first, mixed strength inside

def grab(path, t, out, w):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{max(t,0):.3f}', '-i', path, '-frames:v', '1', '-vf', f'scale={w}:-2', out], check=True)

def sheet(ns, cols, name):
    ins = []
    for n in ns: ins += ['-i', f'{O}/cells/{n:02d}.jpg']
    rws = (len(ns) + cols - 1) // cols; fc = []
    for r in range(rws):
        sub = list(range(r * cols, min(len(ns), (r + 1) * cols)))
        fc.append((f'[{sub[0]}:v]copy[r{r}]' if len(sub) == 1 else ''.join(f'[{i}:v]' for i in sub) + f'hstack={len(sub)}[r{r}]'))
    fc.append(''.join(f'[r{r}]' for r in range(rws)) + f'vstack={rws}[o]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', ';'.join(fc), '-map', '[o]', name], check=True)

rows = []
for k, (fmt, s) in enumerate(pick, 61):
    v = s['video_id']; p = media(v); st = float(s['start_pts_seconds']); w = 384 if fmt == 'LONG' else 162
    c = f'{O}/cells/{k:02d}'
    grab(p, st - 0.25, c + '_a.jpg', w); grab(p, st + 0.25, c + '_c.jpg', w)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f"{L}/{v}/{s['keyframe']}", '-vf', f'scale={w}:-2', c + '_b.jpg'], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', c + '_a.jpg', '-i', c + '_b.jpg', '-i', c + '_c.jpg', '-filter_complex', 'hstack=3', c + '.jpg'], check=True)
    rows.append(dict(n=k, fmt=fmt, video_id=v, shot_id=s['shot_id'], start=st, end=float(s['end_pts_seconds']),
                     boundary_strength=s['boundary_strength'], asr_text=s['asr_text'][:200]))
w = csv.DictWriter(open(O + '/SAMPLE3.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for j in range(61, 85, 6): sheet(list(range(j, j + 6)), 1, f'{O}/b3_long_{(j-61)//6+1}.jpg')
for j in range(85, 109, 6): sheet(list(range(j, j + 6)), 2, f'{O}/b3_short_{(j-85)//6+1}.jpg')
print(len(rows), 'new cells', sum(r['fmt'] == 'LONG' for r in rows), 'long;', len({r['video_id'] for r in rows}), 'videos')
