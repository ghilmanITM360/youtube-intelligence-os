# Classify every frame of every uninspected interval from DENSE_MOTION_<vid>.csv (MEASURED, all frames, no sampling):
# CAM = global similarity motion (|dx|or|dy|>0.5 px or |dscale|>0.001, inliers>=30); LOC = residual after compensation >0.2% px; STATIC = neither.
# Per interval: frame counts, camera runs (length, held frames inside = stepped-camera signal), single-frame local spikes (swap/pop signal).
import csv, json
from pathlib import Path
H = Path(__file__).resolve().parents[1]; L = list(csv.DictReader(open(H / 'UNINSPECTED_INTERVALS_v1.csv'))); out = []; S = {}
for vid in ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']:
    D = {int(r['frame']): r for r in csv.DictReader(open(H / f'dense/DENSE_MOTION_{vid}.csv'))}
    def cls(f):
        r = D[f]; cam = int(r['inliers']) >= 30 and (abs(float(r['dx'])) > 0.5 or abs(float(r['dy'])) > 0.5 or abs(float(r['dscale'])) > 0.001)
        loc = float(r['residual_frac12']) > 0.002
        return 'BOTH' if cam and loc else 'CAM' if cam else 'LOC' if loc else 'STATIC'
    n = dict(frames=0, CAM=0, LOC=0, BOTH=0, STATIC=0, low_track=0)
    for iv in [x for x in L if x['video'] == vid]:
        a, b = int(iv['start_frame']), int(iv['end_frame']); c = [cls(f) for f in range(a, b + 1)]
        camf = [f for f, k in zip(range(a, b + 1), c) if k in ('CAM', 'BOTH')]
        runs = []
        for f in camf:
            if runs and f - runs[-1][1] <= 2: runs[-1][1] = f
            else: runs.append([f, f])
        held = sum(1 for r0, r1 in runs for f in range(r0, r1 + 1) if f not in camf)
        rf = [float(D[f]['residual_frac12']) for f in range(a - 1, b + 2) if f in D]
        spikes = [a - 1 + i for i in range(1, len(rf) - 1) if rf[i] > 0.01 and rf[i] > 4 * max(rf[i - 1], rf[i + 1], 1e-4)]
        lt = sum(1 for f in range(a, b + 1) if int(D[f]['inliers']) < 30)
        net = [round(sum(float(D[f][k]) for f in range(a, b + 1)), 2) for k in ('dx', 'dy')]
        dom = max(('CAM', 'LOC', 'BOTH', 'STATIC'), key=c.count)
        out.append({**iv, 'frames_measured': b - a + 1, 'cam_frames': c.count('CAM'), 'loc_frames': c.count('LOC'), 'both_frames': c.count('BOTH'), 'static_frames': c.count('STATIC'),
                    'low_tracking_frames': lt, 'camera_runs': ';'.join(f'{r0}-{r1}' for r0, r1 in runs), 'held_inside_camera_runs': held,
                    'net_camera_dx_dy_px': f'{net[0]},{net[1]}', 'local_single_frame_spikes': ';'.join(map(str, spikes)), 'dominant': dom,
                    'stepped_camera_flag': 'YES' if held >= 2 and len(runs) and max(r1 - r0 for r0, r1 in runs) >= 6 else 'NO'})
        for k in c: n[k] += 1
        n['frames'] += b - a + 1; n['low_track'] += lt
    S[vid] = n
with open(H / 'dense/DENSE_INTERVAL_CLASSIFICATION_v1.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
json.dump(S, open(H / 'dense/DENSE_INTERVAL_CLASSIFICATION_v1_summary.json', 'w'), indent=1); print(json.dumps(S, indent=1))
