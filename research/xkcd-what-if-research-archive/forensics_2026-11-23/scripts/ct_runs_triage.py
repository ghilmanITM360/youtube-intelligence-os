"""Triage of candidate HOLD-residual runs (peak >=150 px above 8 grey levels) by shape: bbox share of frame and fill = peak px / bbox px.
Compact change = small bbox; scattered speckle = huge bbox, tiny fill (codec-noise pattern in the pilot). Writes ct_scan_batch/CANDIDATE_RUNS_TRIAGE.csv.
usage: uv run --no-project --with numpy python scripts/ct_runs_triage.py"""
import csv, glob, json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B = R + '/ct_scan_batch'
out = []
for d in sorted(glob.glob(B + '/*/hold_residual_runs.csv')):
    v = d.split('/')[-2]; M = json.load(open(f'{B}/{v}/source_manifest.json')); W, H = M['width'], M['height']
    pf = {int(r['frame']): r for r in csv.DictReader(open(f'{B}/{v}/per_frame_table.csv'))}
    for r in csv.DictReader(open(d)):
        if r['candidate_for_viewing'] != '1': continue
        a, b = int(r['start_frame']), int(r['end_frame'])
        fs = [f for f in range(a, b + 1) if pf[f]['bbox_gt8'] and pf[f]['state'] == 'HOLD']
        bbs = [tuple(map(float, pf[f]['bbox_gt8'].split(','))) for f in fs]
        x0, y0, x1, y1 = min(x[0] for x in bbs), min(x[1] for x in bbs), max(x[2] for x in bbs), max(x[3] for x in bbs)
        pk = int(r['peak_px_gt8']); peakf = max(fs, key=lambda f: int(pf[f]['px_gt8'])); share = (x1 - x0) * (y1 - y0)
        cls = 'COMPACT' if share < 0.02 else ('MID' if share < 0.15 else 'SCATTERED')
        out.append(dict(video_id=v, fmt='LONG' if W >= H else 'SHORT', run=r['run'], start=a, end=b, peak_frame=peakf, peak_px=pk, bbox=f'{x0:.3f},{y0:.3f},{x1:.3f},{y1:.3f}',
                        bbox_share=round(share, 4), fill=round(pk / max(share * W * H, 1), 5), shape=cls))
w = csv.DictWriter(open(B + '/CANDIDATE_RUNS_TRIAGE.csv', 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
for c in ('COMPACT', 'MID', 'SCATTERED'): print(c, sum(o['shape'] == c for o in out), 'videos', len({o['video_id'] for o in out if o['shape'] == c}))
