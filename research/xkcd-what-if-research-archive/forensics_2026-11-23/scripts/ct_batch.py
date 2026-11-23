"""CT_SCAN machine stage for one video, NO viewing: manifest, per-frame table (256x144 strong/faint layers + full-resolution diff counts),
state intervals, event/faint list, HOLD-residual runs, summary.json. Output: ct_scan_batch/<video_id>/. Status MEASURED, NOT_VIEWED.
usage: uv run --no-project --with numpy python scripts/ct_batch.py <video_id>"""
import csv, json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import ledger_lib as L

v = sys.argv[1]
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = f'{R}/ct_scan_batch/{v}'; os.makedirs(O, exist_ok=True)
p = L.media(v)
probe = {r['video_id']: r for r in csv.DictReader(open(R + '/media_probe_88.csv'))}.get(v, {})

# manifest (per-frame PTS from ffprobe; sha256 from the Phase 2 probe table)
fr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'frame=best_effort_timestamp_time,pict_type', '-of', 'compact=p=0', p], capture_output=True, text=True).stdout.strip().split('\n')
fr = [dict(kv.split('=') for kv in x.split('|') if '=' in kv) for x in fr]
pts = [float(x['best_effort_timestamp_time']) for x in fr]; pict = [x.get('pict_type', '') for x in fr]
dts = sorted({round(b - a, 5) for a, b in zip(pts, pts[1:])})

m = L.measure(p); cuts, ev = L.segments(m); n = m['n']; w, h = m['w'], m['h']
assert n == len(pts), (n, len(pts))
json.dump(dict(video_id=v, path=p, sha256=probe.get('sha256', ''), width=w, height=h, fps=m['fps'], decoded_frames=n, pts_first=pts[0], pts_last=pts[-1],
               distinct_frame_intervals_s=dts, constant_frame_rate=len(dts) <= 2, status='MEASURED_NOT_VIEWED', audio_review='UNAVAILABLE'), open(O + '/source_manifest.json', 'w'), indent=1)

# state layers (same rules as ct_pilot.py)
evid = [''] * n
for i, e in enumerate(ev):
    for f in range(e['start_frame'], e['end_frame'] + 1): evid[f] = f'E{i+1:03d}'
F_, _, _ = L.frames(p, w, h); F16 = F_.astype(np.int16); D2 = np.abs(F16[1:] - F16[:-1]) > 2; c2 = D2.reshape(len(D2), -1).sum(1)
fe = []; cur = None
for f in [k + 1 for k in range(len(c2)) if c2[k] >= 15 and not evid[k + 1]]:
    if cur and f - cur[1] <= 3: cur[1] = f
    else:
        if cur: fe.append(cur)
        cur = [f, f]
if cur: fe.append(cur)
for i, (a, b) in enumerate(fe, 1):
    for f in range(a, b + 1):
        if not evid[f]: evid[f] = f'F{i:03d}'
state = ['HOLD'] * n
for f in range(n):
    if evid[f]: state[f] = 'EVENT' if evid[f][0] == 'E' else 'FAINT'

# full-resolution pass: every frame vs previous frame
pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', 'format=gray', '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], stdout=subprocess.PIPE)
sz = w * h; prev = None; fr_rows = [(0, 0, 0, '')]; k = 0
while True:
    b = pr.stdout.read(sz)
    if len(b) < sz: break
    cur_ = np.frombuffer(b, np.uint8).reshape(h, w).astype(np.int16)
    if prev is not None:
        d = np.abs(cur_ - prev); g8 = d > 8; n8 = int(g8.sum())
        bb = ''
        if n8 >= 15:
            ys, xs = np.where(g8); bb = f'{xs.min()/w:.2f},{ys.min()/h:.2f},{(xs.max()+1)/w:.2f},{(ys.max()+1)/h:.2f}'
        fr_rows.append((int((d > 2).sum()), n8, int((d > 24).sum()), bb))
    prev = cur_; k += 1
pr.stdout.close(); pr.wait()
assert k == n, (k, n)

with open(O + '/per_frame_table.csv', 'w', newline='') as o:
    cw = csv.writer(o); cw.writerow(['frame', 'pts_s', 'pict_type', 'strong_changed_fraction', 'px_gt2', 'px_gt8', 'px_gt24', 'bbox_gt8', 'cut_candidate', 'state', 'event_id'])
    cs = set(cuts)
    for f in range(n):
        cw.writerow([f, pts[f], pict[f], '' if f == 0 else f"{m['frac'][f-1]:.6f}", *fr_rows[f], int(f in cs), state[f], evid[f]])

iv = []; s = 0
for f in range(1, n + 1):
    if f == n or evid[f] != evid[s]:
        iv.append((s, f - 1, state[s], evid[s])); s = f
with open(O + '/state_intervals.csv', 'w', newline='') as o:
    cw = csv.writer(o); cw.writerow(['interval', 'start_frame', 'end_frame', 'frames', 'start_pts_s', 'end_pts_s', 'state', 'event_id'])
    for i, (a, b, st, e) in enumerate(iv, 1): cw.writerow([i, a, b, b - a + 1, pts[a], pts[b], st, e])

# HOLD residual runs: HOLD frames with >=15 px above 8 grey levels, merged when <=3 frames apart (pilot: such runs were codec noise except tiny drawn objects)
res = [f for f in range(1, n) if state[f] == 'HOLD' and fr_rows[f][1] >= 15]
runs = []
for f in res:
    if runs and f - runs[-1][1] <= 3: runs[-1][1] = f
    else: runs.append([f, f])
with open(O + '/hold_residual_runs.csv', 'w', newline='') as o:
    cw = csv.writer(o); cw.writerow(['run', 'start_frame', 'end_frame', 'frames_with_change', 'peak_px_gt8', 'candidate_for_viewing'])
    for i, (a, b) in enumerate(runs, 1):
        fs = [f for f in res if a <= f <= b]; pk = max(fr_rows[f][1] for f in fs)
        cw.writerow([i, a, b, len(fs), pk, int(pk >= 150)])  # 150 px: heuristic from the pilot (noise runs <=121 px, drawn eye pairs ~200 px); NOT validated

tr = n - 1; hold = [f for f in range(1, n) if state[f] == 'HOLD']
S = dict(video_id=v, fmt='LONG' if w >= h else 'SHORT', frames=n, duration_s=round(pts[-1], 2), strong_events=len(ev), cuts=len(cuts), faint_events=len(fe),
         hold_pct=round(100 * sum(s_ == 'HOLD' for s_ in state) / n, 1), zero_gt2_transitions_pct=round(100 * sum(r[0] == 0 for r in fr_rows[1:]) / tr, 1),
         hold_frames_ge15px_pct=round(100 * len(res) / max(len(hold), 1), 1), residual_runs=len(runs), candidate_runs=sum(max(fr_rows[f][1] for f in range(a, b + 1) if f in set(res)) >= 150 for a, b in runs),
         constant_fps=len(dts) <= 2, status='MEASURED_NOT_VIEWED')
json.dump(S, open(O + '/summary.json', 'w'))
print(json.dumps(S))
