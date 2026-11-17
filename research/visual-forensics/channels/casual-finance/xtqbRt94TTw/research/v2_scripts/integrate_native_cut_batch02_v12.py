"""Ten exact cut onsets; retain two compound-event uncertainties explicitly."""
from pathlib import Path
import csv
import json
import hashlib
import datetime

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
ref='native_cut_batch02_v1/OUT_native_cut_batch02_v1.json';o=json.loads((R/ref).read_text())
proof=json.loads((S/'native_cut_batch02_independent_return_audit_v1.json').read_text())
assert proof['actual_native_fullframe_returns']==24 and proof['actual_bytehash_order_multiplicity_and_1920x1080']=='PASS'
assert hashlib.sha256((R/ref).read_bytes()).hexdigest()==proof['saved_output_sha256']
assert o['status']=='COMPLETE_FOR_SUPPLIED_SCOPE' and not o['pending_case_ids']
def load(p):return list(csv.DictReader((R/p).open()))
def write(p,rows):
    assert not (R/p).exists()
    with (R/p).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
events=load('integrated_v4/visual_event_ledger_v11.csv');byid={x['event_id']:x for x in events}
yes=[x for x in o['items'] if x['shot_boundary']=='YES'];uncertain=[x for x in o['items'] if x['shot_boundary']=='UNDETERMINED']
assert len(yes)==10 and {x['id'] for x in uncertain}=={'EP0054','EP0082'}
for ruling in o['items']:
    row=byid[ruling['id']];assert row['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET'
    row.update(description=ruling['description'],shot_boundary_claim=ruling['shot_boundary'],cut_adjudication_ref=ref+'#'+ruling['id'],
               review_scope='NATIVE_ADJACENT_PAIR;RAW_FIRST_PASS_PRESERVED',pre_ambiguous_shot_claim='YES')
    if ruling['shot_boundary']=='YES':
        n=ruling['onset_frame_or_bracket']['frame'];assert int(row['source_start_frame'])==n
        row.update(visual_onset_verified_frame=str(n),timing_precision='EXACT_NATIVE_CUT_ONSET;NOT_WHOLE_COMPOUND_MOTION_OR_SHOT_DURATION',cut_adjudication_precision='EXACT_NATIVE_ADJACENT_PAIR_CUT_ONSET_ONLY')
    else:
        row.update(cut_adjudication_precision='NATIVE_SUPPLIED_ADJACENCY_ONLY;COMPOUND_CUT_ONSET_UNKNOWN',native_vs_firstpass_conflict='Candidate start not a full composition cut; compound cut timing remains unverified. Raw first-pass preserved.')
        if ruling['id']=='EP0054':
            row.update(event_class='VIEWER_CONTENT_REPOSITIONING_AND_UNVERIFIED_LATER_CUT',observed_change_first_frame='1597')
        else:
            row.update(event_class='FOREGROUND_PDF_SUBSTITUTION_WITH_RETAINED_ARTICLE_BACKDROP',observed_change_first_frame='2769')
assert len(events)==len(byid)==948
write('integrated_v4/visual_event_ledger_v12.csv',events)
shots=load('production_v1/shot_ledger_PARTIAL_v4.csv')
for x in yes:
    n=x['onset_frame_or_bracket']['frame'];assert not any(int(r['start_frame'])==n for r in shots)
    shots.append(dict(video_id='xtqbRt94TTw',shot_id=f'ONSET_{n}',start_frame=str(n),start_pts_seconds=str((n+1)/24),end_frame='UNVERIFIED',end_pts_seconds='UNVERIFIED',transition='SHOT_CUT',
                      verification='native adjacent pair; actual bytehash/order/multiplicity/dimensions independently audited; onset only',source_ref=ref+'#'+x['id'],description=x['description'],
                      limitations='Partial inventory only; full compound motion/whole-shot duration/intervening transitions unverified.'))
shots.sort(key=lambda x:int(x['start_frame']));assert len(shots)==len({r['start_frame'] for r in shots})==47
write('production_v1/shot_ledger_PARTIAL_v5.csv',shots)
motion=load('production_v1/motion_camera_facial_index_PARTIAL_v6.csv');rules={x['id']:x for x in o['items']}
for row in motion:
    if row['id'] in rules:
        x=rules[row['id']];row.update(curated_motion_review=ref+'#'+row['id'],curated_observed_change=x['description'],validation='Native actual return-byte audit PASS; whole motion/compound timing not certified')
        if x['shot_boundary']=='YES':row.update(motion_status='NATIVE_CUT_ONSET_VERIFIED;NOT_FULL_COMPOUND_TRAJECTORY',timing_scope='Exact supplied native pair cut onset; no whole-shot/compound duration')
        else:row.update(motion_status='PARTIAL_NATIVE_ADJACENCY;COMPOUND_CUT_UNRESOLVED',timing_scope='Native candidate-start observation; later compound cut unverified')
write('production_v1/motion_camera_facial_index_PARTIAL_v7.csv',motion)
q=json.loads((S/'global_native_remaining_queue_v4.json').read_text());completed={x['id'] for x in yes}
q.update(baseline_event_ledger='integrated_v4/visual_event_ledger_v12.csv',current_candidate_only_rows=719,partially_verified_cut_onsets=47,ambiguous_shot_claims_remaining=2,
         new_compound_cut_uncertainties=['EP0054','EP0082'],next_pending_native_batch='compound_cut_followup_v1;3requested native frames, read actual reviewer/output/return audit')
q['candidate_only_items']=[x for x in q['candidate_only_items'] if x['event_id'] not in completed]
for x in q['candidate_only_items']:
    if x['event_id'] in {'EP0054','EP0082'}:x.update(shot_claim='UNDETERMINED',status='CANDIDATE_COMPOUND_TIMING_RETAINED;SUPPLIED_NATIVE_ADJACENCY_PARTIALLY_RESOLVED',native_adjacency_review_ref=ref+'#'+x['event_id'])
assert len(q['candidate_only_items'])==sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)==719
(S/'global_native_remaining_queue_v5.json').write_text(json.dumps(q,indent=2)+'\n')
stats=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),event_ledger_version='v12',event_rows=948,unique_event_ids=948,
           new_native_pair_cases=12,new_native_source_returns=24,new_verified_cut_onsets=10,partial_verified_cut_onset_inventory=47,
           candidate_only_timing_rows_remaining=719,compound_cut_uncertainties=['EP0054','EP0082'],
           exact_onsets={x['id']:x['onset_frame_or_bracket']['frame'] for x in yes},
           source_description_corrections=['EP0046 already has incoming card strip at1255, not blank','EP0054 candidate1597 is retained-viewer content repositioning, later alleged cut unresolved','EP0082 retained article backdrop survives at2769 behind foreground PDF; full composition replacement not established'],
           independent_root_repeat_spots={'EP0046':[1254,1255],'EP0054':[1596,1597]},
           partition_unchanged='integrated_v4/frame_partition_v5.csv',raw_reviews_unchanged=True,actual_listening_seconds=0,CT_SCAN_COMPLETE=False,
           limitations='Ten native-cut onsets only. Two partially resolved compound rows retained in719candidate-only count, not mechanically promoted. No all-frame semantic/motion/production/AV completion.')
(S/'native_cut_batch02_integration_v12_stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print('INTEGRATED_V12:10cuts,47partialinventory;719candidate-only incl2compounduncertainties;CTfalse')
