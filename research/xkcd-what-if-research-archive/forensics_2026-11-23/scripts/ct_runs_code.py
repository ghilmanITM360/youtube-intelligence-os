"""Writes ct_scan_batch/run_review/REVIEWED_RUNS.csv from my manual coding of view_01-13 (compact+mid, 153 cells) and control_01-03 (36 random scattered cells). Self-review, one coder.
REAL_SMALL_OBJECT = a small drawn mark, character or stroke appears or is added (visible in the peak frame and in the x8 difference as a compact blob). UNCERTAIN = tiny blob, cannot tell. NOISE = speckle or faint outline with no compact blob."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = R + '/ct_scan_batch/run_review'
REAL = {1,9,10,11,12,13,20,24,25,26,27,29,30,31,32,33,34,40,47,52,53,58,65,66,67,68,71,74,77,78,83,84,85,86,88,91,95,96,105,110,111,112,114,115,116,118,119,121,123,128,133,135,136,138,144,145,146,152}
UNC = {2,23,106,113}
out = []
for r in csv.DictReader(open(O + '/view_cells.csv')):
    n = int(r['_n']); out.append(dict(r, sheet='view', code='REAL_SMALL_OBJECT' if n in REAL else 'UNCERTAIN' if n in UNC else 'NOISE'))
for r in csv.DictReader(open(O + '/control_cells.csv')): out.append(dict(r, sheet='control', code='NOISE'))
w = csv.DictWriter(open(O + '/REVIEWED_RUNS.csv', 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
v = [o for o in out if o['sheet'] == 'view']
for sh in ('COMPACT', 'MID'):
    s = [o for o in v if o['shape'] == sh]; print(sh, len(s), {c: sum(o['code'] == c for o in s) for c in ('REAL_SMALL_OBJECT', 'UNCERTAIN', 'NOISE')})
print('control', len(out) - len(v), 'all NOISE')
real = [o for o in v if o['code'] == 'REAL_SMALL_OBJECT']
print('real runs', len(real), 'videos', len({o['video_id'] for o in real}), 'long', sum(o['fmt'] == 'LONG' for o in real), 'short', sum(o['fmt'] == 'SHORT' for o in real))
