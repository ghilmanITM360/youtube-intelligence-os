"""Resolve a two-frame staged substitution; preserve unresolved PDF construction."""
from pathlib import Path
import csv,json,hashlib,copy,datetime
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
ref='compound_cut_followup_v1/OUT_compound_cut_followup_v1.json';o=json.loads((R/ref).read_text());proof=json.loads((S/'compound_cut_followup_independent_return_audit_v1.json').read_text())
assert proof['actual_native_fullframe_returns']==3 and proof['request_accounting_and_actual_bytehash_order_multiplicity_dimensions']=='PASS'
assert hashlib.sha256((R/ref).read_bytes()).hexdigest()==proof['saved_output_sha256']
assert {x['id'] for x in o['items']}=={'EP0054','EP0082'} and not o['pending_paths']
def load(p):return list(csv.DictReader((R/p).open()))
def write(p,rows):
    assert not (R/p).exists()
    with (R/p).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
events=load('integrated_v4/visual_event_ledger_v12.csv');ids={x['event_id']:x for x in events}
for ruling in o['items']:
    row=ids[ruling['id']];row.update(description=ruling['description'],cut_adjudication_ref=ref+'#'+ruling['id'])
    if ruling['id']=='EP0082':
        assert ruling['shot_boundary_as_single_full_replace']=='NO'
        row.update(shot_boundary_claim='NO',event_class='TWO_STAGE_FOREGROUND_REPLACEMENT_AND_BACKDROP_CLEAR',verdict='RECLASSIFIED',
                   visual_onset_verified_frame='2769',observed_change_first_frame='2769',observed_change_last_frame='2770',
                   timing_precision='EXACT_NATIVE_TWO_STAGE2769_2770;NOT_SINGLE_FULL_COMPOSITION_CUT',
                   cut_adjudication_precision='NATIVE2768_2769_2770_TWO_STAGE_REPLACEMENT',native_vs_firstpass_conflict='Raw single full-scene replacement claim superseded: old backdrop persists at2769, clears2770; new foreground persists.')
    else:
        row.update(event_class='DOCUMENT_SCROLL_ZOOM_WITH_ADDITIVE_HOST;EARLIER_CONSTRUCTION_TIMING_OPEN',shot_boundary_claim='UNDETERMINED',
                   native_vs_firstpass_conflict='1597 retained-viewer content repositioning;1642 presenter addition to already-visible enlarged table, matching prior nativeG013.02. No single full composition cut established; earlier construction remains open.',
                   cut_adjudication_precision='1596_1597_AND1641_1642_NATIVE_ENDPOINTS_REUSED_OR_REPEATED;NOT_FULL_WINDOW')
assert len(events)==len(ids)==948
write('integrated_v4/visual_event_ledger_v13.csv',events)
parts=load('integrated_v4/frame_partition_v5.csv');new=[]
for row in parts:
    if row['interval_id']!='S0051':new.append(row);continue
    assert (row['start'],row['end'])==('2769','2774')
    first=dict(row);first.update(interval_id='S0051_STAGE1_2769',state_id='S0051_STAGE1_2769',start='2769',end='2769',n_frames='1',
                                origin='NATIVE_STAGED_REPLACEMENT_REFINEMENT',semantic_status='NATIVE_ONE_FRAME_INTERMEDIATE_STATE_VERIFIED',
                                boundary_precision='EXACT_NATIVE2768_2769_2770',source_ref=ref+'#EP0082',
                                description='One-frame hybrid: new large PDF foreground and removed presenter while prior Conference Board article strip remains behind; existing PDF composition group, not a new shot.',
                                start_pts=str(2770/24),end_exclusive_pts=str(2771/24))
    second=dict(row);second.update(start='2770',n_frames='5',start_pts=str(2771/24),origin='NATIVE_START_WITH_EXISTING_DRAFT_HOLD',
                                  semantic_status='NATIVE_BACKDROP_CLEAR_ONSET;LATER_HOLD_RETAINS_FIRST_PASS_SCOPE',boundary_precision='EXACT_NATIVE_START2770;END_RETAINS_DRAFT2774',
                                  source_ref=ref+'#EP0082;tables/states_machine.csv#S0051',description='PDF foreground retained; old article backdrop clears to white at2770. Later2771–2774 hold retains prior first-pass status, not new all-frame review.')
    new.extend([first,second])
counts=[0]*19862
for x in new:
    for n in range(int(x['start']),int(x['end'])+1):counts[n]+=1
assert set(counts)=={1} and len(new)==627 and len({x['state_id'] for x in new})==475
write('integrated_v4/frame_partition_v6.csv',new)
groups=[]
for row in new:
    if groups and groups[-1]['composition_group']==row['composition_group']:
        g=groups[-1];g['end']=row['end'];g['end_exclusive_pts']=row['end_exclusive_pts'];g['n_frames']=str(int(g['n_frames'])+int(row['n_frames']))
        if row['state_id'] not in g['state_ids'].split(';'):g['state_ids']+=';'+row['state_id']
        g['interval_ids']+=';'+row['interval_id']
    else:groups.append(dict(composition_group=row['composition_group'],start=row['start'],end=row['end'],state_ids=row['state_id'],interval_ids=row['interval_id'],n_frames=row['n_frames'],start_pts=row['start_pts'],end_exclusive_pts=row['end_exclusive_pts']))
assert len(groups)==329
write('integrated_v4/composition_intervals_v6.csv',groups)
old=json.loads((R/'production_integrated_v1/integrated_production_interval_index_v3.json').read_text());byinterval={x['interval_id']:x for x in old['rows']};draft={x['state_id']:x for x in load('production_v1/per_state_production_spec_DRAFT_v4.csv')};rows=[];missing=set();extended=[]
for x in new:
    base=copy.deepcopy(byinterval.get(x['interval_id'],{}));prior=draft.get(x['state_id'])
    base.update(interval_id=x['interval_id'],state_id=x['state_id'],composition_group=x['composition_group'],start_frame=int(x['start']),end_frame=int(x['end']),source_observation_ref=x['source_ref'],source_description=x['description'],source_boundary_precision=x['boundary_precision'])
    if not prior:
        missing.add(x['state_id']);base.update(prior_draft_ref='',prior_draft_interval=None,source_representative_image='native_cut_batch02_v1/f02769_native.png' if x['state_id']=='S0051_STAGE1_2769' else base.get('source_representative_image',''),production_status='MISSING_ORIGINAL_PRODUCTION_SPEC;NATIVE_TRANSIENT_STATE_NOT_A_NEW_SHOT',animation_static_anchor_status='PENDING',actual_listening_seconds=0)
    elif int(x['start'])<int(prior['start_frame']) or int(x['end'])>int(prior['end_frame']):extended.append(x['interval_id'])
    rows.append(base)
old.update(source_partition='integrated_v4/frame_partition_v6.csv',interval_rows=len(rows),numeric_frames_once=19862,distinct_state_ids=475,composition_groups=329,missing_state_ids=sorted(missing),prior_draft_span_extended_intervals=extended,rows=rows,actual_new_visual_reads=0,
           native_transient_ref=ref+'#EP0082',limitations='Retrieval index only;28missing original specs and152extended spans, not production or all-frame semantic validation. Original draft447 unchanged.')
assert len(missing)==28 and len(extended)==152
(R/'production_integrated_v1/integrated_production_interval_index_v4.json').write_text(json.dumps(old,indent=2)+'\n')
q=json.loads((S/'global_native_remaining_queue_v5.json').read_text());q.update(baseline_event_ledger='integrated_v4/visual_event_ledger_v13.csv',current_candidate_only_rows=718,ambiguous_shot_claims_remaining=1,new_compound_cut_uncertainties=['EP0054'],next_pending_native_batch='EP0054 requested midpoint1619 only after prior native receipt lookup; selection focus separate bounded task')
q['candidate_only_items']=[x for x in q['candidate_only_items'] if x['event_id']!='EP0082']
assert len(q['candidate_only_items'])==sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)==718
(S/'global_native_remaining_queue_v6.json').write_text(json.dumps(q,indent=2)+'\n')
stats=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),event_ledger_version='v13',partition_version='v6',numeric_frames_once=19862,interval_rows=627,distinct_state_ids=475,composition_groups_not_shots=329,event_rows=948,
           source_derivative_display_instances=3,prior_native_source_frame_repeat_validation=[1641,1642],native_host_entry1642='RECONFIRMED_PRIOR_G013_NATIVE_PROOF;NOT_NEW_DISCOVERY',
           staged_replacement_frames=[2769,2770],new_transient_interval='S0051_STAGE1_2769',candidate_only_timing_rows_remaining=718,partial_verified_cut_onsets=47,
           missing_original_production_specs=28,extended_original_prompt_intervals=152,compound_unknown='EP0054 between1598and1641;candidate-startnotcut/endpointhostadditionnotcut',
           actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
(S/'compound_followup_integration_v13_stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print('V13/PARTITIONv6:19862once/627intervals/475states/329groups;2stagecase resolved;718candidate-only;47partialcuts;28productionmissing;CTfalse')
