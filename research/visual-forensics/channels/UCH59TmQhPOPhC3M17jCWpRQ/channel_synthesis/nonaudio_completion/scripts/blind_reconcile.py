# Reconcile BLIND_REVIEW.csv (blind, frozen brief) with DENSE_REVIEW_LEDGER v1 and write ledger v2 (v1 kept unchanged).
# Rules, in order:
#  R1 a blind SHOT_CUT whose largest jump is at end+1 is the known next-state boundary (shown as the "after" tile), not a cut.
#  R2 identical class, or one side MIXED -> AGREE (ledger kept).
#  R3 LOW-confidence tile-only ledger rows: the blind native-crop naming is adopted (stronger evidence than 4 tiles).
#  R4 other differences: orchestrator adjudication on native frames (ORCH below) or, for taxonomy-only splits
#     (CHARACTER vs INTRA_SHOT_STATE on the same described change), recorded as TAXONOMY_SPLIT with ledger kept.
#  Camera: the measured chain verdict (dense/CAMERA_CHAIN_ALL_<vid>.csv) is added to every ledger row; for the 11 rows the
#  ledger flagged UNCERTAIN the resolution also uses r13_blind/CAMERA_CHAIN_CHECK.csv and the U0066 native overlay.
import csv, json, collections
from pathlib import Path
N = Path(__file__).resolve().parents[1]; R = N / 'r13_blind'
ORCH = {
 'uPQc-U0090': ('LEDGER_UPHELD', 'STATIC_HOLD', 'native f4740-f4756: hut holds within a few px; camera chain REJECTED; blind SHAKE not supported'),
 'uPQc-U0163': ('LEDGER_UPHELD', 'GRAPHIC_TEXT', 'native f9266-f9354: painting fades to blank by f9353 (blind missed the fade); pointer also shifts'),
 'mNLN-U0101': ('BLIND_ADOPTED', 'CHARACTER', 'native f4887-f4908: slight head/mouth tilt is visible; ledger "no visible change" too weak'),
 'mNLN-U0262': ('BOTH_PARTIAL', 'MIXED', 'native f14582-f14588: plot moves ~50 px left then settles on a blank background; camera vs object move not attributable (camera not established); blind "enters from right edge" not supported'),
}
TAX = {frozenset({'CHARACTER', 'INTRA_SHOT_STATE'}), frozenset({'GRAPHIC_TEXT', 'INTRA_SHOT_STATE'}), frozenset({'CAMERA', 'INTRA_SHOT_STATE'})}
CAM11 = {r['interval_id']: r for r in csv.DictReader(open(R / 'BLIND_ADJUDICATION_MEASURE.csv'))}
B = {r['interval_id']: r for r in csv.DictReader(open(R / 'BLIND_REVIEW.csv'))}; S = {r['interval_id']: r for r in csv.DictReader(open(R / 'BLIND_SAMPLE_INDEX.csv'))}
rec = []; summ = {}
for vid in ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']:
    L = list(csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}.csv'))); C = {r['interval_id']: r for r in csv.DictReader(open(N / f'dense/CAMERA_CHAIN_ALL_{vid}.csv'))}
    out = []
    for l in L:
        iid = l['interval_id']; c = C[iid]; row = dict(l)
        row.update(camera_measured_v2=c['camera_measured'], camera_scale=c['scale'], camera_centre_shift_px=c['centre_shift_px'], camera_inlier_spread=c['inlier_spread'])
        if 'UNCERTAIN' in l['camera_claim_crosscheck']:
            m = CAM11[iid]['camera_measured']
            res = 'CAMERA_VERIFIED_NATIVE_OVERLAY (orchestrator f3592 vs f3598: frame-wide outward edge displacement; scale 1.0048)' if iid == 'uPQc-U0066' else m
            row['camera_claim_resolution_v2'] = res
        else: row['camera_claim_resolution_v2'] = ''
        row.update(blind_sample='', blind_event_class='', blind_what='', reconcile='', adjudicated_event_class=row['event_class'], adjudication_note='')
        if iid in B:
            b = B[iid]; mj = CAM11[iid]; lc, bc = l['event_class'], b['event_class']
            if bc == 'SHOT_CUT' and mj['jump_at'] == 'NEXT_STATE_BOUNDARY': k, ac, note = 'AGREE_CUT_IS_STATE_BOUNDARY', (lc if l['v1_confidence'] != 'LOW' or lc != 'STATIC_HOLD' else 'CHARACTER'), f"blind cut at f{mj['max_jump_frame']} = end+1 (next state)"
            elif lc == bc or 'MIXED' in (lc, bc): k, ac, note = 'AGREE', lc, ''
            elif iid in ORCH: k, ac, note = ORCH[iid]
            elif l['v1_confidence'] == 'LOW' and l['review_status'] == 'VISUALLY_NAMED_TILES': k, ac, note = 'BLIND_ADOPTED_NATIVE_CROP', bc, 'LOW-confidence tile naming superseded by blind native-crop naming'
            elif frozenset({lc, bc}) in TAX: k, ac, note = 'TAXONOMY_SPLIT', lc, 'same described change, different class; ledger kept'
            elif lc == 'CAMERA' or bc == 'CAMERA':
                cam = c['camera_measured'] == 'CAMERA_VERIFIED' or row['camera_claim_resolution_v2'].startswith('CAMERA_VERIFIED')
                k, ac, note = 'CAMERA_BY_MEASUREMENT', ('MIXED' if cam else (bc if lc == 'CAMERA' else lc)), f"camera established={cam} (chain {c['camera_measured']}; {row['camera_claim_resolution_v2'][:40]}) + the other reviewer's non-camera change -> MIXED"
            else: k, ac, note = 'UNRECONCILED', lc, 'needs adjudication'
            # blind cut at boundary on a LOW STATIC_HOLD row: in-interval content is the blind's pre-cut description
            row.update(blind_sample=S[iid]['sample_reason'], blind_event_class=bc, blind_what=b['what_changes'][:200], reconcile=k, adjudicated_event_class=ac, adjudication_note=note)
            rec.append(dict(video=vid, interval_id=iid, sample_reason=S[iid]['sample_reason'], ledger_class=lc, ledger_conf=l['v1_confidence'], ledger_review=l['review_status'], blind_class=bc, blind_camera=b['camera_move'], camera_measured=c['camera_measured'], reconcile=k, adjudicated_class=ac, note=note))
        out.append(row)
    with open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}_v2.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    unc = [r for r in out if r['camera_claim_resolution_v2'] and not r['camera_claim_resolution_v2'].startswith(('CAMERA_VERIFIED', 'CAMERA_REJECTED'))]
    summ[vid] = dict(rows=len(out), camera_measured=dict(collections.Counter(r['camera_measured_v2'] for r in out)), camera_claims_uncertain_v1=sum(1 for r in out if r['camera_claim_resolution_v2']), camera_claims_still_uncertain=len(unc), blind_sampled=sum(1 for r in out if r['blind_sample']), reconcile=dict(collections.Counter(r['reconcile'] for r in out if r['reconcile'])))
with open(R / 'BLIND_RECONCILIATION.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rec[0])); w.writeheader(); w.writerows(rec)
tot = collections.Counter(r['reconcile'] for r in rec)
summ['all'] = dict(sampled=len(rec), reconcile=dict(tot), by_reason={k: dict(collections.Counter(r['reconcile'] for r in rec if r['sample_reason'] == k)) for k in ['RANDOM', 'LOW_TILES_ONLY', 'CAMERA_UNCERTAIN']})
json.dump(summ, open(R / 'BLIND_RECONCILIATION_summary.json', 'w'), indent=1); print(json.dumps(summ['all'], indent=1)); print({v: (summ[v]['camera_claims_still_uncertain']) for v in summ if v != 'all'})
for r in rec:
    if r['reconcile'] in ('UNRECONCILED', 'CAMERA_BY_MEASUREMENT'): print(r)
