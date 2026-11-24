"""CT_SCAN pilot, stage 1 (machine): source manifest, per-frame table for EVERY native frame, state intervals, event windows + sheets.
usage: uv run --no-project --with numpy python scripts/ct_pilot.py <video_id>"""
import csv, hashlib, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import ledger_lib as L

v = sys.argv[1]
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = f'{R}/ct_scan_pilot_{v}'; os.makedirs(O + '/windows', exist_ok=True)
p = L.media(v)

# 1 manifest ---------------------------------------------------------------
pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', p], capture_output=True, text=True).stdout)
fr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'frame=best_effort_timestamp_time,pict_type,key_frame', '-of', 'compact=p=0', p], capture_output=True, text=True).stdout.strip().split('\n')
fr = [dict(kv.split('=') for kv in x.split('|') if '=' in kv) for x in fr]
pts = [float(x['best_effort_timestamp_time']) for x in fr]; pict = [x.get('pict_type', '') for x in fr]
d = [round(b - a, 5) for a, b in zip(pts, pts[1:])]
sha = hashlib.sha256(open(p, 'rb').read()).hexdigest()
vs = [s for s in pr['streams'] if s['codec_type'] == 'video'][0]
man = dict(video_id=v, path=p, sha256=sha, size_bytes=int(pr['format']['size']), duration_s=float(pr['format']['duration']), codec=vs['codec_name'],
           width=vs['width'], height=vs['height'], r_frame_rate=vs['r_frame_rate'], avg_frame_rate=vs['avg_frame_rate'], nb_frames_probe=vs.get('nb_frames'),
           decoded_frame_count=len(pts), pts_first=pts[0], pts_last=pts[-1], distinct_frame_intervals_s=sorted(set(d)), constant_frame_rate=len(set(d)) <= 2,
           has_audio=any(s['codec_type'] == 'audio' for s in pr['streams']), audio_review='UNAVAILABLE (no listening)', status='MEASURED')
json.dump(man, open(O + '/source_manifest.json', 'w'), indent=1)

# 2 per-frame table (frame k has a diff against frame k-1; frame 0 has none) ----
m = L.measure(p); cuts, ev = L.segments(m); n = m['n']
assert n == len(pts), (n, len(pts))
evid = [''] * n
for i, e in enumerate(ev):
    for f in range(e['start_frame'], e['end_frame'] + 1): evid[f] = f'E{i+1:03d}'
cutset = set(cuts)
import numpy as np
F_, _, _ = L.frames(p, m['w'], m['h']); F16 = F_.astype(np.int16); D2 = np.abs(F16[1:] - F16[:-1]) > 2; c2 = D2.reshape(len(D2), -1).sum(1)
fe = []; cur = None
for f in [k + 1 for k in range(len(c2)) if c2[k] >= 15 and not evid[k + 1]]:
    if cur and f - cur[1] <= 3: cur[1] = f
    else:
        if cur: fe.append(cur)
        cur = [f, f]
if cur: fe.append(cur)
faint = []
for i, (a, b) in enumerate(fe, 1):
    for f in range(a, b + 1):
        if not evid[f]: evid[f] = f'F{i:03d}'
    U = D2[a - 1:b].any(0); r_ = np.where(U.any(1))[0]; c_ = np.where(U.any(0))[0]
    faint.append(dict(id=f'F{i:03d}', start_frame=a, end_frame=b, frames=b - a + 1, peak=float(c2[a - 1:b].max()) / (m['sw'] * m['sh']), bbox=(c_[0] / m['sw'], r_[0] / m['sh'], (c_[-1] + 1) / m['sw'], (r_[-1] + 1) / m['sh'])))
with open(O + '/per_frame_table.csv', 'w', newline='') as o:
    w = csv.writer(o); w.writerow(['frame', 'pts_s', 'pict_type', 'changed_fraction_vs_prev', 'ink_delta', 'bbox_x0', 'bbox_y0', 'bbox_x1', 'bbox_y1', 'cut_candidate', 'state', 'event_id'])
    for f in range(n):
        if f == 0: w.writerow([0, pts[0], pict[0], '', '', '', '', '', '', 0, 'HOLD', '']); continue
        k = f - 1; b = m['bbox'][k] or ('', '', '', '')
        w.writerow([f, pts[f], pict[f], f"{m['frac'][k]:.6f}", f"{m['ink'][k]:.5f}", *[(f'{x:.3f}' if x != '' else '') for x in b], int(f in cutset), ('EVENT' if evid[f].startswith('E') else 'FAINT') if evid[f] else 'HOLD', evid[f]])

# 3 state intervals (every frame belongs to exactly one) --------------------
iv = []; s = 0
for f in range(1, n + 1):
    if f == n or bool(evid[f]) != bool(evid[s]) or (evid[f] and evid[f] != evid[s]):
        iv.append((s, f - 1, ('EVENT' if evid[s].startswith('E') else 'FAINT') if evid[s] else 'HOLD', evid[s])); s = f
assert sum(b - a + 1 for a, b, _, _ in iv) == n
with open(O + '/state_intervals.csv', 'w', newline='') as o:
    w = csv.writer(o); w.writerow(['interval', 'start_frame', 'end_frame', 'frames', 'start_pts_s', 'end_pts_s', 'state', 'event_id'])
    for i, (a, b, st, e) in enumerate(iv, 1): w.writerow([i, a, b, b - a + 1, pts[a], pts[b], st, e])

# 4 event table + windows --------------------------------------------------
fps = m['fps']; rows = []
for i, e in enumerate(ev, 1):
    a, b = e['start_frame'], e['end_frame']; bb = e['bbox']
    take = sorted({max(a - 1, 0), min(b + 1, n - 1)} | {round(a + (b - a) * t / 5) for t in range(6)})
    take = take[:8]
    rows.append(dict(kind='STRONG',event_id=f'E{i:03d}', start_frame=a, end_frame=b, frames=e['frames'], start_pts_s=pts[a], end_pts_s=pts[b], peak_changed_fraction=round(e['peak_frac'], 5),
                     bbox=f'{bb[0]:.2f},{bb[1]:.2f},{bb[2]:.2f},{bb[3]:.2f}', has_cut_candidate=int(e['has_cut']), window_frames=' '.join(map(str, take))))
for e in faint:
    a, b = e['start_frame'], e['end_frame']; bb = e['bbox']
    take = sorted({max(a - 1, 0), min(b + 1, n - 1)} | {round(a + (b - a) * t / 5) for t in range(6)})[:8]
    rows.append(dict(kind='FAINT', event_id=e['id'], start_frame=a, end_frame=b, frames=e['frames'], start_pts_s=pts[a], end_pts_s=pts[b], peak_changed_fraction=round(e['peak'], 5),
                     bbox=f'{bb[0]:.2f},{bb[1]:.2f},{bb[2]:.2f},{bb[3]:.2f}', has_cut_candidate=0, window_frames=' '.join(map(str, take))))
rows.sort(key=lambda r: r['start_frame'])
with open(O + '/events_machine.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
W, H = 200, 112
for i, r in enumerate(rows, 1):
    fr_ = [int(x) for x in r['window_frames'].split()]
    sel = '+'.join(f'eq(n\\,{x})' for x in fr_)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-vf', f'select={sel},scale={W}:{H},tile={len(fr_)}x1', '-frames:v', '1', f"{O}/windows/{r['event_id']}.jpg"], check=True)
per = 6
for s in range(0, len(rows), per):
    ids = [r['event_id'] for r in rows[s:s + per]]; ins = []
    for e in ids: ins += ['-i', f'{O}/windows/{e}.jpg']
    fc = ''.join(f'[{k}:v]pad=1600:{H}[p{k}];' for k in range(len(ids))) + ''.join(f'[p{k}]' for k in range(len(ids))) + f'vstack={len(ids)}[o]'
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + ins + ['-filter_complex', fc, '-map', '[o]', f'{O}/sheet_{s//per+1:02d}.jpg'], check=True)
print(json.dumps({k: man[k] for k in ('sha256', 'duration_s', 'avg_frame_rate', 'decoded_frame_count', 'constant_frame_rate', 'distinct_frame_intervals_s')}))
print('frames', n, 'strong events', sum(r['kind']=='STRONG' for r in rows), 'faint events', len(faint), 'event+faint frames', sum(r['frames'] for r in rows), 'cuts', len(cuts), 'intervals', len(iv), 'sheets', (len(rows) + per - 1) // per)
