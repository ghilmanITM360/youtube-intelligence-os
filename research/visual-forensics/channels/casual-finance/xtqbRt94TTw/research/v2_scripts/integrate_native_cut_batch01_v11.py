"""Curate six native adjacent cut onsets, retaining every old sealed layer."""
from pathlib import Path
import base64
import collections
import csv
import datetime
import hashlib
import json

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S = R / 'session_20261105'
review_ref = 'native_cut_batch01_v1/OUT_native_cut_batch01_resume_v2.json'
review = json.loads((R / review_ref).read_text())
proof = json.loads((S / 'native_cut_batch01_resume_independent_return_audit_v1.json').read_text())
assert proof['actual_native_fullframe_returns'] == 12 and proof['actual_bytehash_order_multiplicity_and_1920x1080'] == 'PASS'
assert hashlib.sha256((R / review_ref).read_bytes()).hexdigest() == proof['saved_output_sha256']
assert hashlib.sha256((R / 'native_cut_batch01_v1/OUT_native_cut_batch01_v1.json').read_bytes()).hexdigest() == '5717e79642984ac9bdd32e625b92dfd573a49bf21918ec7b961075b3dcf2d644'
assert review['status'] == 'COMPLETE_FOR_SUPPLIED_SCOPE' and not review['pending_case_ids']
def load_csv(rel):
    with (R / rel).open() as f:
        return list(csv.DictReader(f))
def write_csv(rel, rows):
    p = R / rel
    assert not p.exists()
    with p.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
events = load_csv('integrated_v4/visual_event_ledger_v10.csv')
by_id = {r['event_id']: r for r in events}
changed = []
for ruling in review['items']:
    row = by_id[ruling['id']]
    n = ruling['onset_frame_or_bracket']['frame']
    assert ruling['shot_boundary'] == 'YES' and int(row['source_start_frame']) == n
    assert row['timing_precision'] == 'MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET'
    row.update(description=ruling['description'], visual_onset_verified_frame=str(n),
               shot_boundary_claim='YES', timing_precision='EXACT_NATIVE_CUT_ONSET;NOT_WHOLE_SHOT_DURATION',
               review_scope='NATIVE_ADJACENT_PAIR;RAW_FIRST_PASS_PRESERVED', cut_adjudication_ref=review_ref+'#'+ruling['id'],
               cut_adjudication_precision='EXACT_NATIVE_ADJACENT_PAIR_ONSET_ONLY', pre_ambiguous_shot_claim='YES')
    changed.append(ruling['id'])
assert len(events) == len(by_id) == 948
write_csv('integrated_v4/visual_event_ledger_v11.csv', events)
shots = load_csv('production_v1/shot_ledger_PARTIAL_v3.csv')
for ruling in review['items']:
    n = ruling['onset_frame_or_bracket']['frame']
    assert not any(int(x['start_frame']) == n for x in shots)
    shots.append(dict(video_id='xtqbRt94TTw', shot_id=f'ONSET_{n}', start_frame=str(n), start_pts_seconds=str((n+1)/24),
                      end_frame='UNVERIFIED', end_pts_seconds='UNVERIFIED', transition='SHOT_CUT',
                      verification='native adjacent fullframe pair; independently audited actual return bytes; onset only',
                      source_ref=review_ref+'#'+ruling['id'], description=ruling['description'],
                      limitations='Partial cut inventory; no whole-shot duration, intervening transition inventory or shot statistics.'))
shots.sort(key=lambda x:int(x['start_frame']))
assert len(shots) == len({x['start_frame'] for x in shots}) == 37
write_csv('production_v1/shot_ledger_PARTIAL_v4.csv', shots)
motion = load_csv('production_v1/motion_camera_facial_index_PARTIAL_v5.csv')
for row in motion:
    if row['id'] in changed:
        ruling = next(x for x in review['items'] if x['id'] == row['id'])
        n = ruling['onset_frame_or_bracket']['frame']
        row.update(motion_status='NATIVE_CUT_ONSET_VERIFIED;NOT_TRAJECTORY_REVIEW',
                   timing_scope=f'Native adjacent{n-1}/{n} discontinuity only; no full shot/motion duration',
                   validation='Independent returned image bytehash/order/multiplicity/native dimensions PASS; root spot EP0028 separately recorded',
                   curated_motion_review=review_ref+'#'+row['id'], curated_observed_change=ruling['description'])
write_csv('production_v1/motion_camera_facial_index_PARTIAL_v6.csv', motion)
queue = json.loads((R / 'session_20261104/global_native_remaining_queue_v3.json').read_text())
queue.update(baseline_event_ledger='integrated_v4/visual_event_ledger_v11.csv', current_candidate_only_rows=729,
             partially_verified_cut_onsets=37, candidate_only_items=[x for x in queue['candidate_only_items'] if x['event_id'] not in changed],
             next_pending_native_batch='native_cut_batch02_v1;24paths12cases prepared; consult actual saved output/reviewer state before resume')
assert len(queue['candidate_only_items']) == sum(r['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for r in events) == 729
(S / 'global_native_remaining_queue_v4.json').write_text(json.dumps(queue, indent=2)+'\n')
stats=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), event_ledger_version='v11', event_rows=948, unique_event_ids=948,
           partition_unchanged='integrated_v4/frame_partition_v5.csv', changed_event_ids=changed, new_verified_native_cut_onsets=6,
           partial_verified_cut_onsets=37, global_candidate_only_timing_rows_remaining=729, new_reviewer_native_fullframe_returns=12,
           root_repeat_spot_displays=2, root_spot_event_id='EP0028', semantic_correction='Before720 is two side-by-side release pages and narrator; after721 removes pages and restages narrator beside laptop. Old singular-page and I-frame pixel assertion superseded only in curated layer.',
           actual_listening_seconds=0, CT_SCAN_COMPLETE=False, limitations='Native adjacency and partial cut inventory only; whole-shot durations/global temporal/motion/production/audio gates remain incomplete.')
(S / 'native_cut_batch01_integration_v11_stats.json').write_text(json.dumps(stats, indent=2)+'\n')
print('INTEGRATED',len(changed),'cut onsets;37partial inventory;729candidate-only;old layers unchanged;NOT_CT_COMPLETE')
