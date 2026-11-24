"""Join the 58 REAL_SMALL_OBJECT runs (ct_scan_batch/run_review/REVIEWED_RUNS.csv) to per-video ledgers WITHOUT editing any existing ledger file.
Writes: ledgers_measured/<id>/small_additions.csv (videos that have a ledger folder; adds shot_id), ledgers_small_additions_only/<id>/small_additions.csv (videos with no
ledger folder), and ledgers_measured/SMALL_ADDITIONS_ALL.csv. Description comes from small_descriptions.py (one reader, stills only).
usage: uv run --no-project python scripts/ledger_add_small.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from small_descriptions import DESC, SCAT_DESC
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = [r for f in ('REVIEWED_RUNS.csv', 'scat_REVIEWED_RUNS.csv') for r in csv.DictReader(open(R + '/ct_scan_batch/run_review/' + f)) if r['code'] == 'REAL_SMALL_OBJECT']
COLS = ['video_id', 'fmt', 'addition_id', 'hold_run_no', 'start_frame', 'end_frame', 'peak_frame', 'start_pts_s', 'end_pts_s', 'peak_pts_s', 'peak_px_gt8', 'bbox', 'bbox_share',
        'shape', 'shot_id', 'description', 'review_pass', 'event_class', 'evidence_label', 'interpretation_status', 'review_sheet']
EV = 'OBSERVED (one coder: still before/peak + x8 difference cell; not played back; description is a reading, not a measurement)'
by = {}
for r in rows: by.setdefault(r['video_id'], []).append(r)
allrows = []
for v, rs in sorted(by.items()):
    pts = {int(x['frame']): float(x['pts_s']) for x in csv.DictReader(open(f'{R}/ct_scan_batch/{v}/per_frame_table.csv'))}
    shots = []
    sf = f'{R}/ledgers_measured/{v}/shot_ledger.csv'
    if os.path.exists(sf): shots = [(int(s['start_frame']), int(s['end_frame']), s['shot_id']) for s in csv.DictReader(open(sf))]
    out = []
    for i, r in enumerate(sorted(rs, key=lambda x: int(x['start'])), 1):
        a, b, pk = int(r['start']), int(r['end']), int(r['peak_frame'])
        sh = next((s[2] for s in shots if s[0] <= pk <= s[1]), '' if shots else 'NO_SHOT_LEDGER')
        out.append(dict(video_id=v, fmt=r['fmt'], addition_id=f'A{i:03d}', hold_run_no=r['run'], start_frame=a, end_frame=b, peak_frame=pk, start_pts_s=pts[a], end_pts_s=pts[b], peak_pts_s=pts[pk],
                        peak_px_gt8=r['peak_px'], bbox=r['bbox'], bbox_share=r['bbox_share'], shape=r['shape'], shot_id=sh, description=(SCAT_DESC if r['sheet'] == 'scat' else DESC)[int(r['_n'])], review_pass='scattered' if r['sheet'] == 'scat' else 'compact_mid', event_class='SMALL_ADDITION_IN_HOLD',
                        evidence_label=EV, interpretation_status='CODED_REAL_DESCRIBED', review_sheet=f"run_review/{r['sheet']}_{(int(r['_n']) - 1) // 12 + 1:02d}.jpg cell {int(r['_n'])}"))  # 12 cells per sheet, _n numbers cells 1..153
    d = f'{R}/ledgers_measured/{v}' if shots else f'{R}/ledgers_small_additions_only/{v}'
    os.makedirs(d, exist_ok=True)
    with open(d + '/small_additions.csv', 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=COLS); w.writeheader(); w.writerows(out)
    allrows += out
with open(R + '/ledgers_measured/SMALL_ADDITIONS_ALL.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=COLS); w.writeheader(); w.writerows(allrows)
print('videos', len(by), 'additions', len(allrows), 'with ledger folder', sum(os.path.exists(f'{R}/ledgers_measured/{v}/shot_ledger.csv') for v in by),
      'long', sum(r['fmt'] == 'LONG' for r in allrows), 'short', sum(r['fmt'] == 'SHORT' for r in allrows))
