"""Reuse four qualified old native cases and curate two new focus observations."""
from pathlib import Path
import csv,json,hashlib,datetime
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');S=R/'session_20261105'
reuse=json.loads((S/'additional_native_cut_semantic_reuse_audit_v2.json').read_text());assert reuse['bytehash_and_required_multiplicity']=='PASS' and reuse['actual_new_image_reads']==0
focusref='selection_focus_boundary_v1/OUT_selection_focus_boundary_v1.json';focus=json.loads((R/focusref).read_text());fp=json.loads((S/'selection_focus_boundary_independent_return_audit_v1.json').read_text())
assert fp['actual_native_fullframe_returns']==2 and fp['saved_output_sha256']==hashlib.sha256((R/focusref).read_bytes()).hexdigest()
lateref='pdf_late_zoom_native_v1/OUT_pdf_late_zoom_native_v1.json';late=json.loads((R/lateref).read_text());lp=json.loads((S/'pdf_late_zoom_native_independent_return_audit_v1.json').read_text())
assert lp['actual_native_fullframe_returns']==10 and lp['saved_output_sha256']==hashlib.sha256((R/lateref).read_bytes()).hexdigest()
def load(p):return list(csv.DictReader((R/p).open()))
def write(p,rows):
    assert not (R/p).exists()
    with (R/p).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
events=load('integrated_v4/visual_event_ledger_v13.csv');byid={x['event_id']:x for x in events};changed=[]
track=[]
for x in reuse['cases']:
    row=byid[x['event_id']];n=x['cut_onset_frame'];assert row['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET'
    row.update(description=x['curated_description'],visual_onset_verified_frame=str(n),cut_adjudication_ref='session_20261105/additional_native_cut_semantic_reuse_audit_v2.json#'+x['event_id'],
               cut_adjudication_precision='EXACT_EXISTING_NATIVE_CUT_ONSET_WITHIN_OR_AT_COMPOUND_WINDOW;OTHER_MOTION_PARTIAL',
               timing_precision='EXACT_SELECTED_NATIVE_BOUNDARIES_REUSED;COMPOUND_INTERIORS_OR_OFFSETS_SAMPLED',review_scope='QUALIFIED_HISTORICAL_NATIVE_OBSERVATION_REUSE;NO_NEW_SOURCE_VIEW')
    if x['event_id']=='EP0128':row.update(event_class='FRAGMENTATION_EXIT_THEN_LATER_CHART_CUT_AND_PAN',observed_change_first_frame='4245',native_vs_firstpass_conflict='Fragmentation4245 is not the chart cut; native chart cut is4270, not candidate start4245.')
    if x['event_id']=='EP0192':row.update(event_class='BANKNOTE_OVERLAY_THEN_LATER_HOST_CHALKBOARD_CUT',observed_change_first_frame='6771',native_vs_firstpass_conflict='Rain overlay6771 retains underlying composition; exact native cut is later6830.')
    changed.append(x['event_id']);track.append({'parent_event_id':x['event_id'],'macro_window':[int(row['source_start_frame']),int(row['source_end_frame'])],'cut_onset_frame':n,'qualified_old_native_frames':x['native_source_frames'],'source_ref':x['qualified_prior_review_ref'],'new_source_views':0,'limitation':'Partial native onsets within/at compound windows, not complete motion/shot duration'})
(R/'integrated_v4/reused_compound_cut_tracks_v2.json').write_text(json.dumps({'tracks':track,'new_source_reads':0,'actual_listening_seconds':0,'CT_SCAN_COMPLETE':False},indent=2)+'\n')
row=byid['EP0235'];assert row['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET'
row.update(description='Host/desk/laptop exit8085 is reused from qualifiedG063. Newly observed8057 and8086 both retain the same blue-selected Chatham/$830billion sentence; article is enlarged/repositioned8086. No removal/gray-selection state observed at these two samples. Later map entry8132 retains priorG063 native proof. Eventual selection offset/physical focus and complete zoom settling remain unknown.',
           macro_review_ref=focusref,review_scope='NEW_TWO_NATIVE_FULLFRAME_ENDPOINTS_PLUS_QUALIFIED_G063_REUSE',timing_precision='SELECTED_NATIVE_BLUE_SELECTION8057_8086;HOST_EXIT8085_REUSED;FULL_OFFSET_UNKNOWN',
           native_vs_firstpass_conflict='Raw gray-selection wording is not established by these observations.8086 is blue. Exact color at8084/8085 unknown from generic reused host-exit witness; no universal continuous-color claim.')
changed.append('EP0235')
doc={'parent_event_id':'EP0054','source_review':lateref,'native_window':[1631,1640],'construction':late['construction_verdict'],
     'shot_verdict_in_native_window':late['shot_cut_verdict_for_this_window'],'earlier_compound_gate':late['earlier_compound_gate'],
     'qualified_context_refs':['agents/gap_review_01/OUT_gap_review_01.json#G013','compound_cut_followup_v1/OUT_compound_cut_followup_v1.json#EP0054','pdf_transition_midpoint_v1/OUT_pdf_transition_midpoint_root_v1.json','pdf_transition_midpoint02_v1/OUT_pdf_transition_midpoint02_root_v1.json'],
     'entire_compound_native_certification':False,'actual_listening_seconds':0,'CT_SCAN_COMPLETE':False}
(R/'integrated_v4/document_zoom_track_v1.json').write_text(json.dumps(doc,indent=2)+'\n')
byid['EP0054'].update(macro_review_ref='integrated_v4/document_zoom_track_v1.json',native_vs_firstpass_conflict='Native1631–1640 progressive retained-table zoom/crop has no full-scene cut; chrome components exit1633/1636/1639;1642hostentry reusesG013. Early1598–1630 remains partially natively observed, whole compound not certified.')
assert len(events)==len(byid)==948
write('integrated_v4/visual_event_ledger_v14.csv',events)
shots=load('production_v1/shot_ledger_PARTIAL_v5.csv');added=[]
for x in reuse['cases']:
    n=x['cut_onset_frame']
    if any(int(z['start_frame'])==n for z in shots):continue
    added.append(n);shots.append(dict(video_id='xtqbRt94TTw',shot_id=f'ONSET_{n}',start_frame=str(n),start_pts_seconds=str((n+1)/24),end_frame='UNVERIFIED',end_pts_seconds='UNVERIFIED',transition='SHOT_CUT',
                      verification='Qualified old native adjacency and actual historical return bytes reused;0newviews',source_ref='session_20261105/additional_native_cut_semantic_reuse_audit_v2.json#'+x['event_id'],description=x['curated_description'],limitations='Exact cut within compound may differ from candidate window start; surrounding motion/shot duration incomplete.'))
shots.sort(key=lambda x:int(x['start_frame']));assert len(shots)==len({x['start_frame'] for x in shots})==50 and sorted(added)==[3810,4270,5448]
write('production_v1/shot_ledger_PARTIAL_v6.csv',shots)
motion=load('production_v1/motion_camera_facial_index_PARTIAL_v7.csv')
for row in motion:
    if row['id'] in changed:
        e=byid[row['id']];row.update(curated_motion_review=e['cut_adjudication_ref'] or focusref,curated_observed_change=e['description'],timing_scope=e['timing_precision'],validation='Qualified actual-return audit; selected source semantics only, no global pass')
    if row['id']=='EP0054':row.update(curated_motion_review='integrated_v4/document_zoom_track_v1.json',curated_observed_change='Native1631–1640 same-page zoom/reframe/crop;thumbnailfragmentsgone1633,outerdarksidebargone1636,finalguttergone1639. Movingthrough1640;earlywindow/fullsettleunknown.',timing_scope='Late consecutive native window only; earlier compound gate retained')
write('production_v1/motion_camera_facial_index_PARTIAL_v8.csv',motion)
q=json.loads((S/'global_native_remaining_queue_v6.json').read_text());q.update(baseline_event_ledger='integrated_v4/visual_event_ledger_v14.csv',current_candidate_only_rows=713,partially_verified_cut_onsets=50,
    candidate_only_items=[x for x in q['candidate_only_items'] if x['event_id'] not in changed],next_pending_native_batch='pdf_early_traversal_native_v1:31newnativeholes,inspectactualreviewer/output before resume')
q['open_other_timing_gates']=[x.replace('Selection removal beyond8045','Selection removal beyond8086;no gray state observed8057/8086') for x in q['open_other_timing_gates']]
assert len(q['candidate_only_items'])==sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in events)==713
(S/'global_native_remaining_queue_v7.json').write_text(json.dumps(q,indent=2)+'\n')
stats={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'event_ledger_version':'v14','event_rows':948,'partial_cut_onset_inventory':50,'new_inventory_native_cut_onsets_from_old_reads':added,
       'parent_compound_native_reuse_cases':4,'new_source_views_for_reuse':0,'candidate_only_timing_rows_remaining':713,'new_focus_native_fullframe_returns':2,'selection_visible_native_frames':[8057,8086],
       'selection_removal_frame':'UNKNOWN_AFTER8086','new_late_zoom_native_fullframe_returns':10,'late_zoom_native_window':[1631,1640],'late_zoom_whole_scene_cut':'NO_WITHIN_WINDOW;EARLY_COMPOUND_STILL_OPEN',
       'partition_version':'v6','numeric_frames_once':19862,'intervals':627,'distinct_states':475,'composition_groups_not_shots':329,'missing_original_production_specs':28,'extended_original_prompt_intervals':152,
       'source_derivative_displays_not_unique_source_frame_counts':True,'actual_listening_seconds':0,'CT_SCAN_COMPLETE':False}
(S/'native_reuse_focus_zoom_integration_v14_stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print('V14:50partialcutonsets/713candidate-only;0newviewsfor4reusecases;focusblue8086;latezoomresolved;earlywindowactive;CTfalse')
