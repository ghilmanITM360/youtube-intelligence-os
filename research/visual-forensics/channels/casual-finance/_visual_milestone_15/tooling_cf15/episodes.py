# usage: episodes.py WS [thr=0.0006] [gap=3] -> WS/tables/episodes.csv  (CANDIDATES only; need visual confirmation)
import csv, sys, json
ws = sys.argv[1]; THR = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0006; GAP = int(sys.argv[3]) if len(sys.argv) > 3 else 3
r = list(csv.DictReader(open(f'{ws}/tables/frame_metrics.csv')))
fr = [(int(x['frame']), float(x['pts_time']), float(x['changed_frac_thr10']), float(x['mean_abs_diff']), int(x['fullres_changed_px_thr25'])) for x in r]
act = [f[0] for f in fr if f[2] >= THR or f[4] >= 300]
eps = []; cur = None
for i in act:
    if cur and i - cur[1] <= GAP: cur[1] = i
    else:
        if cur: eps.append(cur)
        cur = [i, i]
if cur: eps.append(cur)
out = []
for k, (a, b) in enumerate(eps):
    seg = [f for f in fr if a <= f[0] <= b]
    out.append(dict(ep=f'EP{k+1:04d}', start_frame=a, end_frame=b, start_pts=fr[a][1], end_pts=fr[b][1], n=b-a+1, peak_frac=round(max(s[2] for s in seg), 4), sum_frac=round(sum(s[2] for s in seg), 3), peak_mad=round(max(s[3] for s in seg), 2), peak_fullres_px=max(s[4] for s in seg)))
with open(f'{ws}/tables/episodes.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print(len(out), 'episodes; active frames', len(act), 'of', len(fr), '; quiet frames', len(fr) - len(act))
