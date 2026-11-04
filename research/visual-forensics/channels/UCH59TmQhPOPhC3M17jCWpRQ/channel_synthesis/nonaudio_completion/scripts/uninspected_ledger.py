# Exact ledger of frames with visible change (px_diff_ge12 > T at 320px) not covered by any prior visual inspection
# (motion strips, rep frames, v1 dense frames). Hard-cut boundary frames are excluded (boundary-reviewed separately).
import csv, glob, json, sys
from pathlib import Path
B = Path('/Users/ghilmankhan/YIOS-local-audits/barely-evolved')
V = {'uPQcyookL0Y': ('2026-11-02-uPQcyookL0Y-deep-ct-scan', 'tables/states_v6_draft.csv', 'state_v4', 'tables/o_motion_peaks_batch*.csv', 'tables/k_rep_frames_batch*.csv'),
     'mNLNb-Z4T0M': ('2026-11-03-mNLNb-Z4T0M-deep-ct-scan', 'tables/states_v1.csv', 'state', 'tables/motion_peaks_b*.csv', 'tables/rep_frames_b*.csv'),
     'GNaBxt_zIRA': ('2026-11-03-GNaBxt_zIRA-deep-ct-scan', 'tables/states_v1.csv', 'state', 'tables/motion_peaks_b*.csv', 'tables/rep_frames_b*.csv')}
T = int(sys.argv[1]) if len(sys.argv) > 1 else 50; GAP = 3
out = []; summ = {}
for vid, (d, stf, sk, mp, rp) in V.items():
    p = B / d
    fm = list(csv.DictReader(open(p / 'FULL_FRAME_MEASUREMENTS.csv')))
    st = list(csv.DictReader(open(p / stf))); starts = {int(s['start']) for s in st}
    owner = {}
    for s in st:
        for f in range(int(s['start']), int(s['end']) + 1): owner[f] = s[sk]
    seen = set()
    for f in glob.glob(str(p / mp)):
        for r in csv.DictReader(open(f)): seen |= {int(x) for x in r['strip_frames'].split(';') if x}
    for f in glob.glob(str(p / rp)):
        for r in csv.DictReader(open(f)): seen.add(int(r['frame']))
    if vid == 'uPQcyookL0Y':
        dj = json.loads((p / 'tables/v3_dense_frames_index.json').read_text())
        for v in dj.values():
            for x in (v if isinstance(v, list) else v.get('frames', [])):
                try: seen.add(int(x if not isinstance(x, dict) else x['frame']))
                except Exception: pass
    ch = [int(r['frame']) for r in fm if int(r['px_diff_ge12']) > T and int(r['frame']) not in starts]
    un = [f for f in ch if f not in seen]
    cl = []
    for f in un:
        if cl and f - cl[-1][1] <= GAP and owner[f] == owner[cl[-1][1]]: cl[-1][1] = f
        else: cl.append([f, f])
    for a, b in cl:
        out.append(dict(video=vid, interval_id=f'{vid[:4]}-U{len([o for o in out if o["video"]==vid])+1:04d}', state=owner[a], start_frame=a, end_frame=b,
                        n_frames=b - a + 1, peak_px_ge12=max(int(fm[f]['px_diff_ge12']) for f in range(a, b + 1))))
    summ[vid] = dict(frames=len(fm), change_frames=len(ch), previously_inspected_change_frames=len(ch) - len(un), uninspected_change_frames=len(un),
                     intervals=len(cl), inspected_frame_set=len(seen), threshold=f'px_diff_ge12>{T} (320px)', static_or_subthreshold_frames=len(fm) - len(ch) - len(starts))
o = B / 'channel_synthesis/nonaudio_completion'
with open(o / 'UNINSPECTED_INTERVALS_v1.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
(o / 'UNINSPECTED_INTERVALS_v1_summary.json').write_text(json.dumps(summ, indent=1)); print(json.dumps(summ, indent=1))
