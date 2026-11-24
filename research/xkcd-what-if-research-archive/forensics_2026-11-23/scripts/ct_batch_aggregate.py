"""Aggregate ct_scan_batch/<id>/summary.json -> ct_scan_batch/BATCH_SUMMARY.csv and print channel-level medians per format."""
import csv, glob, json, os, statistics as st
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B = R + '/ct_scan_batch'
rows = [json.load(open(f)) for f in sorted(glob.glob(B + '/*/summary.json'))]
w = csv.DictWriter(open(B + '/BATCH_SUMMARY.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print('videos', len(rows), 'frames', sum(r['frames'] for r in rows), 'non-constant fps', [r['video_id'] for r in rows if not r['constant_fps']])
for fmt in ('LONG', 'SHORT'):
    s = [r for r in rows if r['fmt'] == fmt]
    if not s: continue
    print(fmt, len(s), 'videos', sum(r['frames'] for r in s), 'frames')
    for k in ('hold_pct', 'zero_gt2_transitions_pct', 'hold_frames_ge15px_pct', 'faint_events', 'strong_events', 'residual_runs', 'candidate_runs'):
        x = [r[k] for r in s]; print(f'  {k}: min {min(x)} median {st.median(x)} max {max(x)} sum {round(sum(x),1)}')
