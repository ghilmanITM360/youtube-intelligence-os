# Merge per-video dense review (v1 tiles) + native-crop corrections (v2) into DENSE_REVIEW_LEDGER_<vid>.csv with density/limitations.
# Raw reviewer CSVs are not modified. usage: merge_dense_ledger.py VID
import csv, json, sys
from pathlib import Path
N = Path(__file__).resolve().parents[1]; vid = sys.argv[1]; D = N / 'dense_review'
iv = {r['interval_id']: r for r in csv.DictReader(open(N / 'dense/DENSE_INTERVAL_CLASSIFICATION_v1.csv')) if r['video'] == vid}
v1 = {r['interval_id']: r for r in csv.DictReader(open(D / f'DENSE_REVIEW_{vid}_v1.csv'))}
cf = D / f'DENSE_REVIEW_{vid}_v2_crop_corrections.csv'; v2 = {r['interval_id']: r for r in csv.DictReader(open(cf))} if cf.exists() else {}
pk = {r['interval_id']: r['tiles'] for r in csv.DictReader(open(D / f'PACK_INDEX_{vid}.csv'))}
ck = {r['interval_id']: r['frames'] for r in csv.DictReader(open(D / f'CROP_INDEX_{vid}.csv'))} if (D / f'CROP_INDEX_{vid}.csv').exists() else {}
cc = D / f'CAMERA_CLAIM_CROSSCHECK_{vid}.csv'; ccm = {r['interval_id']: r['verdict_vs_dense_measurement'] for r in csv.DictReader(open(cc))} if cc.exists() else {}
rows = []; miss = []
for iid, m in iv.items():
    a = v1.get(iid); c = v2.get(iid)
    if not a: miss.append(iid); continue
    n = int(m['n_frames']); seen = len([f for f in pk[iid].split() if int(m['start_frame']) <= int(f) <= int(m['end_frame'])])
    seen_c = len([f for f in ck.get(iid, '').split() if int(m['start_frame']) <= int(f) <= int(m['end_frame'])])
    fin = c if c and c['verdict'] in ('CONFIRMED', 'CORRECTED') else None
    status = ('VISUALLY_NAMED_NATIVE_CROP' if fin else 'UNRESOLVED_AFTER_CROP' if c else 'NEEDS_CROP_NOT_DONE' if a['needs_native_crop'] == 'YES' else 'VISUALLY_NAMED_TILES')
    rows.append(dict(video=vid, interval_id=iid, state=m['state'], start_frame=m['start_frame'], end_frame=m['end_frame'], n_frames=n,
        measured_class=m['dominant'], event_name=(fin or a)['event_name_v2' if fin else 'event_name'], event_class=(fin or a)['event_class_v2' if fin else 'event_class'],
        what_changes=(fin or a)['what_changes_v2' if fin else 'what_changes'], review_status=status, crop_verdict=c['verdict'] if c else '',
        interior_frames_seen_tiles=seen, interior_frames_seen_crop=seen_c, density=f'{max(seen, seen_c)}/{n} interior frames viewed',
        limitation=('all frames viewed' if max(seen, seen_c) >= n else 'changes between viewed frames are measured (dense CSV) but not visually seen'),
        camera_claim_crosscheck=('NOT_CORROBORATED (sum |dscale|<0.01 and |dx|<10 px: below tracker noise floor; treat camera claim as UNCERTAIN)' if ccm.get(iid) == 'NOT_SUPPORTED_BY_DENSE' else 'SUPPORTED by dense measurement' if iid in ccm else ''),
        v1_confidence=a['confidence'], v1_note=a['note'], v2_note=c['note'] if c else ''))
out = D / f'DENSE_REVIEW_LEDGER_{vid}.csv'
with open(out, 'w', newline='') as f: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
s = dict(video=vid, intervals=len(iv), rows=len(rows), missing_v1=miss, status=Counter(r['review_status'] for r in rows), crop_verdicts=Counter(r['crop_verdict'] for r in rows if r['crop_verdict']),
         all_frames_viewed=sum(r['limitation'] == 'all frames viewed' for r in rows))
(D / f'DENSE_REVIEW_LEDGER_{vid}_summary.json').write_text(json.dumps(s, indent=1)); print(json.dumps(s))
