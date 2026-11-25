"""Full-resolution, every-frame check of a span (default 720 frames from frame 960 = 40.0-70.0 s of the pilot video) and 48-per-sheet frame sheets.
usage: uv run --no-project --with numpy python scripts/ct_span.py <video_id> <start_frame> <count>"""
import csv, os, subprocess, sys, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import ledger_lib as L
v, a, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = f'{R}/ct_scan_pilot_{v}/span_{a}_{a+n-1}'; os.makedirs(O, exist_ok=True)
p = L.media(v); w, h, fps, _ = L.probe(p)
ma, mn = (a, n) if a > 0 else (1, n - 1)  # frame 0 has no predecessor
# full-resolution grey frames a-1 .. a+n-1 (one extra so frame a has a predecessor)
pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'select=between(n\\,{ma-1}\\,{ma+mn-1}),format=gray', '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], stdout=subprocess.PIPE)
sz = w * h; prev = None; rows = []
for k in range(mn + 1):
    b = pr.stdout.read(sz)
    if len(b) < sz: break
    cur = np.frombuffer(b, np.uint8).reshape(h, w).astype(np.int16)
    if prev is not None:
        d = np.abs(cur - prev); ys, xs = np.where(d > 8)
        rows.append((ma + k - 1, int((d > 2).sum()), int((d > 8).sum()), int((d > 24).sum()),
                     f'{xs.min()/w:.2f},{ys.min()/h:.2f},{(xs.max()+1)/w:.2f},{(ys.max()+1)/h:.2f}' if len(xs) else ''))
    prev = cur
pr.stdout.close(); pr.wait()
state = {int(r['frame']): (r['state'], r['event_id']) for r in csv.DictReader(open(f'{R}/ct_scan_pilot_{v}/per_frame_table.csv'))}
with open(O + '/fullres_changes.csv', 'w', newline='') as o:
    cw = csv.writer(o); cw.writerow(['frame', 'px_gt2', 'px_gt8', 'px_gt24', 'bbox_gt8', 'machine_state', 'machine_event'])
    for r in rows: cw.writerow([*r, *state[r[0]]])
hold = [r for r in rows if state[r[0]][0] == 'HOLD']
print('frames', len(rows), 'machine states', {s: sum(state[r[0]][0] == s for r in rows) for s in ('HOLD', 'FAINT', 'EVENT')})
print('HOLD frames with full-res change: >2:', sum(r[1] > 0 for r in hold), ' >8:', sum(r[2] > 0 for r in hold), ' >8 and >=15 px:', sum(r[2] >= 15 for r in hold), ' >24:', sum(r[3] > 0 for r in hold), 'of', len(hold))
print('top HOLD frames by px_gt8:', sorted([(r[2], r[0], r[4]) for r in hold], reverse=True)[:12])
# sheets: every frame, 48 per sheet (8x6) at 192x108
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-vf', f'select=between(n\\,{a}\\,{a+n-1}),scale=192:108,tile=8x6', '-fps_mode', 'passthrough', f'{O}/sheet_%02d.jpg'], check=True)
print('sheets', len([f for f in os.listdir(O) if f.startswith('sheet')]))
