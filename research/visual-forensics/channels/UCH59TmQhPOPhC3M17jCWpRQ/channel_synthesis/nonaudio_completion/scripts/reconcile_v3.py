# Reconciliation rule set R-v3 (2026-11-05, session 15f69c1b). Appends columns to DENSE_REVIEW_LEDGER_<vid>_v2.csv; every N16 column is left unchanged
# (asserted against the N16 commit blob). Fixes: R1 of blind_reconcile.py set CHARACTER automatically for LOW STATIC_HOLD + boundary cut; a cut at end+1
# belongs to the next state and can never decide the interior class. R3 (LOW tile rows adopt blind) kept but flagged when M3 conflicts.
import csv, json, subprocess, io, collections, hashlib
from pathlib import Path
N = Path(__file__).resolve().parents[1]; M = N / 'method_v3'; R = N / 'r13_blind'; VIDS = ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']
REPO = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'; BASE = '16bd0cc708b45ddb2e9b70873e37dfe9ffd786aa'; PFX = 'research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/channel_synthesis/nonaudio_completion/dense_review/'
A = {r['interval_id']: r for r in csv.DictReader(open(M / 'NATIVE_ADJUDICATION_ORCH.csv'))}
B2 = {r['interval_id']: r for r in csv.DictReader(open(R / 'batch2/BLIND_REVIEW_B2.csv'))}; B2M = {r['interval_id']: r for r in csv.DictReader(open(R / 'batch2/BLIND_ADJUDICATION_MEASURE.csv'))}
def det(m3, loc):   # deterministic interior suggestion from measurement alone; never uses the end+1 cut
    if m3 == 'CAMERA_FRAMEWIDE': return 'MIXED' if loc else 'CAMERA'
    if m3 == 'WHOLE_CONTENT_MOVE': return 'WHOLE_CONTENT_MOVE'
    if m3 == 'NO_CAMERA': return 'LOCAL_CHANGE' if loc else 'STATIC_HOLD'
    if m3 == 'OBJECT_MOVE': return 'LOCAL_CHANGE'
    return 'UNRESOLVED'
coarse = lambda c: {'CHARACTER': 'LOCAL_CHANGE', 'INTRA_SHOT_STATE': 'LOCAL_CHANGE', 'GRAPHIC_TEXT': 'LOCAL_CHANGE', 'LIGHT_COLOR': 'LOCAL_CHANGE'}.get(c, c)
rec = []; S = {}
for vid in VIDS:
    rows = list(csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}_v2.csv'))); old = subprocess.check_output(['git', 'show', f'{BASE}:{PFX}DENSE_REVIEW_LEDGER_{vid}_v2.csv'], cwd=REPO).decode()
    O = list(csv.DictReader(io.StringIO(old))); oc = list(O[0]); assert [{k: r[k] for k in oc} for r in rows] == O, vid
    C = {r['interval_id']: r for r in csv.DictReader(open(M / f'CAMERA_M3_{vid}.csv'))}; out = []
    for r0 in O:
        r = dict(r0); i = r['interval_id']; c = C[i]; m3 = c['camera_m3']; loc = int(c['local_change_after_comp']); led = r['event_class']; b1 = r['reconcile']; prev = r['adjudicated_event_class']; note = ''; flag = ''
        d = det(m3, loc); attr = 'CAMERA' if m3 == 'CAMERA_FRAMEWIDE' else 'CAMERA_VS_SLIDE_UNRESOLVED' if m3 == 'WHOLE_CONTENT_MOVE' else 'NOT_CAMERA' if m3 in ('NO_CAMERA', 'OBJECT_MOVE') else 'UNRESOLVED' if m3 != 'NOT_APPLICABLE' else 'NOT_APPLICABLE'
        if i in A: fin, basis, attr, note = A[i]['final_class'], 'NATIVE_ORCH', A[i]['camera_attribution'], A[i]['native_observation']
        else:
            fin, basis = prev, ('RECONCILE_N16' if b1 else 'LEDGER')
            if b1 == 'BLIND_ADOPTED_NATIVE_CROP' and ((prev == 'CAMERA' and m3 in ('NO_CAMERA', 'OBJECT_MOVE')) or (m3 == 'CAMERA_FRAMEWIDE' and prev not in ('CAMERA', 'MIXED'))): flag = 'R3_M3_CONFLICT_UNRESOLVED'
        camled = led in ('CAMERA', 'DIGITAL_ZOOM') or 'CAMERA' in r['camera_claim_crosscheck'].split(' ')[0]
        vs = 'LEDGER_CAMERA_SUPPORTED' if camled and m3 == 'CAMERA_FRAMEWIDE' else 'LEDGER_CAMERA_M3_NOT_CAMERA' if camled and m3 in ('NO_CAMERA', 'OBJECT_MOVE') else 'LEDGER_CAMERA_M3_OTHER' if camled else 'UNNAMED_FRAMEWIDE_MOVE' if m3 == 'CAMERA_FRAMEWIDE' else 'UNNAMED_WHOLE_CONTENT_MOVE' if m3 == 'WHOLE_CONTENT_MOVE' else 'NO_CONFLICT'
        r.update(camera_m3=m3, m3_moved_share=c['moved_share'], m3_max_link_residual=c['max_link_residual'], m3_interior_suggestion=d, camera_m3_vs_ledger=vs, blind2_event_class=B2[i]['event_class'] if i in B2 else '', blind2_camera=B2[i]['camera_move'] if i in B2 else '', blind2_what=B2[i]['what_changes'][:200] if i in B2 else '', final_event_class=fin, final_camera_attribution=attr, final_basis=basis, final_flag=flag, final_note=note, final_rule_version='R-v3/M3 (post-hoc, 2026-11-05)')
        out.append(r)
        if i in B2 or b1: rec.append(dict(video=vid, interval_id=i, batch='B2' if i in B2 else 'B1', ledger_class=led, blind_class=B2[i]['event_class'] if i in B2 else r['blind_event_class'], v2_adjudicated=prev if i not in B2 else '', final_class=fin, final_camera_attribution=attr, camera_m2=r['camera_measured_v2'], camera_m3=m3, m3_suggestion=d, basis=basis, flag=flag, changed_from_v2='YES' if i not in B2 and fin != prev else '', note=note))
    with open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}_v2.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    S[vid] = dict(rows=len(out), final=dict(collections.Counter(r['final_event_class'] for r in out)), m3=dict(collections.Counter(r['camera_m3'] for r in out)), m3_vs_ledger=dict(collections.Counter(r['camera_m3_vs_ledger'] for r in out)), r3_conflict=sum(r['final_flag'] != '' for r in out))
with open(R / 'BLIND_RECONCILIATION_v3.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rec[0])); w.writeheader(); w.writerows(rec)
b2 = [r for r in rec if r['batch'] == 'B2']; b1 = [r for r in rec if r['batch'] == 'B1']
nat = [r for r in rec if r['interval_id'] in A]; agree = sum(1 for r in nat if r['m3_suggestion'] == coarse(r['final_class'])); dis = [(r['interval_id'], r['final_class'], r['m3_suggestion'], r['camera_m3']) for r in nat if r['m3_suggestion'] != coarse(r['final_class'])]
camclaims = [(r['interval_id'], r['final_camera_attribution'], r['camera_m3']) for r in nat if r['camera_m3'] == 'CAMERA_FRAMEWIDE']
K = list(csv.DictReader(open(M / 'HELDOUT_KEY_local.csv'))); H = {r['hid']: r for r in csv.DictReader(open(M / 'HELDOUT_LABELS_ORCH.csv'))}; mp = {'CAMERA_FRAMEWIDE': {'CAM'}, 'WHOLE_CONTENT_MOVE': {'WCM'}, 'NO_CAMERA': {'NONE', 'LOCAL'}, 'OBJECT_MOVE': {'LOCAL', 'LAYERED', 'NONE'}}
hd = []; 
for k in K: hd.append(dict(hid=k['hid'], interval_id=k['interval_id'], camera_m3=k['camera_m3'], orch_label=H[k['hid']]['orch_label'], match=int(H[k['hid']]['orch_label'] in mp[k['camera_m3']]), note=H[k['hid']]['note']))
with open(M / 'HELDOUT_RESULT.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(hd[0])); w.writeheader(); w.writerows(hd)
out = dict(batch2=dict(rows=len(b2), ledger_static_confirmed=sum(r['final_class'] == 'STATIC_HOLD' for r in b2), ledger_static_corrected=sum(r['final_class'] != 'STATIC_HOLD' for r in b2), blind_class_upheld=sum(r['blind_class'] == r['final_class'] for r in b2), blind_class_differs=sum(r['blind_class'] != r['final_class'] for r in b2), final=dict(collections.Counter(r['final_class'] for r in b2)), attribution=dict(collections.Counter(r['final_camera_attribution'] for r in b2))),
    batch1=dict(rows=len(b1), changed_from_v2=[(r['interval_id'], r['v2_adjudicated'], r['final_class']) for r in b1 if r['changed_from_v2'] == 'YES'], r3_rows=sum(1 for r in b1 if r['basis'] == 'RECONCILE_N16' and 'BLIND' in str(r)), r3_conflicts=[r['interval_id'] for r in b1 if r['flag']]),
    m3_vs_native=dict(rows=len(nat), agree=agree, disagreements=dis, framewide_claims=camclaims), heldout={g: dict(n=sum(1 for h in hd if h['camera_m3'] == g), match=sum(h['match'] for h in hd if h['camera_m3'] == g), misses=[(h['hid'], h['interval_id'], h['orch_label']) for h in hd if h['camera_m3'] == g and not h['match']]) for g in mp}, by_video=S)
json.dump(out, open(R / 'BLIND_RECONCILIATION_v3_summary.json', 'w'), indent=1); print(json.dumps(out))
