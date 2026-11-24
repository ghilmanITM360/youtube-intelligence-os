"""Build machine-measured shot + visual-event ledgers for the 20 long videos and 24 Shorts that have media but no campaign ledger.
Output: ../ledgers_measured/<video_id>/{shot_ledger.csv, visual_event_ledger.csv, summary.json, keyframes/}, plus ALL_* and INDEX.
Interpretation columns are left EMPTY and marked NOT_VIEWED: nothing here is viewed or judged. Read-only on repo and media."""
import csv, glob, json, subprocess, statistics as st, hashlib
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import ledger_lib as L
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent; D = OUT / 'ledgers_measured'; D.mkdir(exist_ok=True)
probe = {r['video_id']: r for r in csv.DictReader(open(OUT / 'media_probe_88.csv'))}
M = list(csv.DictReader(open(C / 'campaign/campaign_matrix.csv')))
has = lambda v: (C / 'videos' / v / 'shot_ledger.csv').exists()
targets = [(r['video_id'], r['format']) for r in M if not has(r['video_id'])]
SH = ['video_id', 'shot_id', 'start_pts_seconds', 'end_pts_seconds', 'start_frame', 'end_frame', 'duration_s', 'boundary_evidence', 'boundary_strength', 'events_in_shot', 'events_per_min', 'asr_words', 'asr_text', 'keyframe', 'evidence_label', 'subject', 'setting', 'framing', 'camera_motion', 'graphics_text', 'narrative_function', 'interpretation_status']
EV = ['video_id', 'shot_id', 'event_id', 'start_pts_seconds', 'end_pts_seconds', 'start_frame', 'end_frame', 'frames', 'event_scope', 'event_tempo', 'ink_direction', 'ink_delta', 'peak_changed_fraction', 'bbox_x0', 'bbox_y0', 'bbox_x1', 'bbox_y1', 'contains_shot_boundary_candidate', 'event_class', 'evidence_label', 'interpretation_status']
def asr(v, fmt):
    f = (OUT / ('phase7b_asr' if fmt == 'LONG_FORM' else 'phase7c_asr') / f'{v}.json')
    if not f.exists(): return None
    return [dict(a=s['offsets']['from'] / 1000, b=s['offsets']['to'] / 1000, t=s['text'].strip()) for s in json.load(open(f))['transcription']]
A_S, A_E, idx = [], [], []
for v, fmt in targets:
    short = fmt != 'LONG_FORM'
    if v not in probe:
        idx.append(dict(video_id=v, format='SHORT' if short else 'LONG', status='UNAVAILABLE_NO_MEDIA')); continue
    path = L.media(v); m = L.measure(path); cuts, ev = L.segments(m); fps = m['fps']; n = m['n']
    bounds = [0] + cuts + [n]; vd = D / v; (vd / 'keyframes').mkdir(parents=True, exist_ok=True)
    seg = asr(v, fmt); shots = []
    for k in range(len(bounds) - 1):
        a, b = bounds[k], bounds[k + 1]; sid = f'SH{k+1:03d}'; mid = round(((a + b) / 2) / fps, 3)
        kf = f'keyframes/{sid}.jpg'
        ok = False
        for tt in (mid, max(mid - 0.5, 0), max(mid - 1.5, 0), 0):
            r = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(tt), '-i', path, '-frames:v', '1', '-vf', 'scale=480:-1' if not short else 'scale=-1:480', str(vd / kf)], capture_output=True)
            if r.returncode == 0 and (vd / kf).exists() and (vd / kf).stat().st_size > 0: ok = True; break
        if not ok: kf = ''
        t0, t1 = a / fps, b / fps; sg = [s for s in (seg or []) if t0 <= (s['a'] + s['b']) / 2 < t1]
        txt = ' '.join(s['t'] for s in sg)
        shots.append(dict(video_id=v, shot_id=sid, start_pts_seconds=round(t0, 4), end_pts_seconds=round(t1, 4), start_frame=a, end_frame=b - 1, duration_s=round(t1 - t0, 3),
            boundary_evidence='video start' if k == 0 else 'MEASURED frame-difference shot-boundary candidate', boundary_strength='' if k == 0 else round(float(m['frac'][a - 1]), 3),
            events_in_shot=0, events_per_min='', asr_words=len(txt.split()), asr_text=txt[:240], keyframe=kf, evidence_label='MEASURED (frame differences; not viewed)',
            subject='', setting='', framing='', camera_motion='', graphics_text='', narrative_function='', interpretation_status='NOT_VIEWED'))
    evs = []
    for j, e in enumerate(ev):
        sidx = max(i for i, s in enumerate(shots) if s['start_frame'] <= e['start_frame']); bb = e['bbox']; area = (bb[2] - bb[0]) * (bb[3] - bb[1])
        evs.append(dict(video_id=v, shot_id=shots[sidx]['shot_id'], event_id=f'E{j+1:04d}', start_pts_seconds=round(e['start_frame'] / fps, 4), end_pts_seconds=round((e['end_frame'] + 1) / fps, 4),
            start_frame=e['start_frame'], end_frame=e['end_frame'], frames=e['frames'], event_scope='FULL_FRAME' if area >= .6 else ('REGIONAL' if area >= .15 else 'LOCAL'),
            event_tempo='INSTANT' if e['frames'] <= 3 else 'PROGRESSIVE', ink_direction='INK_ADDED' if e['ink'] > .001 else ('INK_REMOVED' if e['ink'] < -.001 else 'INK_NEUTRAL'),
            ink_delta=round(e['ink'], 4), peak_changed_fraction=round(e['peak_frac'], 4), bbox_x0=round(bb[0], 3), bbox_y0=round(bb[1], 3), bbox_x1=round(bb[2], 3), bbox_y1=round(bb[3], 3),
            contains_shot_boundary_candidate=e['has_cut'], event_class='UNCLASSIFIED', evidence_label='MEASURED (frame differences; not viewed)', interpretation_status='NOT_VIEWED'))
        shots[sidx]['events_in_shot'] += 1
    for s in shots: s['events_per_min'] = round(s['events_in_shot'] / (s['duration_s'] / 60), 1) if s['duration_s'] else ''
    for name, rows, cols in (('shot_ledger.csv', shots, SH), ('visual_event_ledger.csv', evs, EV)):
        with open(vd / name, 'w', newline='') as o: w = csv.DictWriter(o, fieldnames=cols); w.writeheader(); w.writerows(rows)
    A_S += shots; A_E += evs; dur = n / fps; sd = [s['duration_s'] for s in shots]
    cam = C / 'videos' / v / 'tables'
    xchk = {}
    if (cam / 'segments_v1.csv').exists():
        xchk['campaign_activity_segments'] = sum(1 for r in csv.DictReader(open(cam / 'segments_v1.csv')) if r['kind'] == 'ACTIVITY')
        xchk['campaign_scenedetect_scenes'] = sum(1 for _ in csv.DictReader(open(cam / 'scenedetect_candidates.csv')))
    summ = dict(video_id=v, format='SHORT' if short else 'LONG', source_sha256=probe[v]['sha256'], fps=fps, frames=n, duration_s=round(dur, 2), shots=len(shots), shot_boundary_candidates=len(cuts), events=len(evs),
        median_shot_s=round(st.median(sd), 2), events_per_min=round(len(evs) / (dur / 60), 1), asr='whisper.cpp small.en (uncertified)' if seg else 'none', params=L.P,
        campaign_cross_check=xchk, status='MEASURED_LEDGER_NOT_VIEWED')
    json.dump(summ, open(vd / 'summary.json', 'w'), indent=1)
    idx.append(dict(video_id=v, format=summ['format'], status=summ['status'], duration_s=summ['duration_s'], shots=len(shots), events=len(evs), median_shot_s=summ['median_shot_s'], events_per_min=summ['events_per_min'], **xchk))
    print('done', v, len(shots), len(evs), flush=True)
for name, rows, cols in (('ALL_SHOT_LEDGER.csv', A_S, SH), ('ALL_EVENT_LEDGER.csv', A_E, EV)):
    with open(D / name, 'w', newline='') as o: w = csv.DictWriter(o, fieldnames=cols); w.writeheader(); w.writerows(rows)
keys = sorted({k for r in idx for k in r}, key=lambda k: ['video_id', 'format', 'status', 'duration_s', 'shots', 'events', 'median_shot_s', 'events_per_min'].index(k) if k in ['video_id', 'format', 'status', 'duration_s', 'shots', 'events', 'median_shot_s', 'events_per_min'] else 99)
with open(D / 'INDEX.csv', 'w', newline='') as o: w = csv.DictWriter(o, fieldnames=keys); w.writeheader(); w.writerows(idx)
print('ALL DONE', len(idx), 'videos,', len(A_S), 'shots,', len(A_E), 'events', flush=True)
