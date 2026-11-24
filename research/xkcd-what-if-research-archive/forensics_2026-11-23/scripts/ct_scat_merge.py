"""Merge the 8 reader CSVs for the 1,443 scattered runs (run_review/scat_coded_*.csv) with my own re-check of every non-NOISE cell into run_review/scat_REVIEWED_RUNS.csv.
Re-check (2026-11-23, sheets scat_08/13/39/50/56/62/70/88/90/96/97/111/112/117 viewed): 3 of 19 reader REAL claims (cells 734, 1080, 1341: too small to read on the sheet) were downgraded to UNCERTAIN; the other 16 were kept.
usage: uv run --no-project python scripts/ct_scat_merge.py"""
import csv, glob, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = R + '/ct_scan_batch/run_review'
rd = {int(r['n']): r for f in glob.glob(O + '/scat_coded_*.csv') for r in csv.DictReader(open(f))}
assert sorted(rd) == list(range(1, 1444)), 'every cell must be coded exactly once'
DOWN = {734: 'tiny red dot, too small to read on the sheet', 1080: 'tiny dot beside the SVALBARD arrow, too small to read', 1341: 'bright digits in the difference but both stills show 2.28'}
cells = list(csv.DictReader(open(O + '/scat_cells.csv')))
out = []
for c in cells:
    n = int(c['_n']); r = rd[n]; code, note = r['code'], ''
    if code == 'REAL_SMALL_OBJECT' and n in DOWN: code, note = 'UNCERTAIN', DOWN[n]
    out.append({**{k: c[k] for k in ('video_id', 'fmt', 'run', 'start', 'end', 'peak_frame', 'peak_px', 'bbox', 'bbox_share', 'fill', 'shape', '_n')}, 'sheet': 'scat', 'code': code,
                'reader_code': r['code'], 'reader_description': r['description'], 'recheck_note': note})
w = csv.DictWriter(open(O + '/scat_REVIEWED_RUNS.csv', 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), Counter(r['code'] for r in out), 'reader codes', Counter(r['reader_code'] for r in out))
