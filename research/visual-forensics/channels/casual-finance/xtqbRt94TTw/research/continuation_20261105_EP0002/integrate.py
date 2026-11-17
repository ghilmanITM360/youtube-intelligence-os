from pathlib import Path
import csv, json, hashlib, copy

P = Path(__file__).parent
B = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
def save(name, data):
    (P/name).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
def csvsave(name, rows):
    with (P/name).open('w') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def pts(n): return (n+1)/24

observations = {
 'channel':'Casual Finance','video_id':'xtqbRt94TTw',
 'source_sha256':json.loads((P/'source_identity.json').read_text())['sha256'],
 'scope':{'newly_decoded_source_frames':[37,83], 'prior_accepted_endpoint':36,
          'fullframe_native_views':[38,39,40,48,49,64,65,81,82,83],
          'native_pixel_coin_ROI_contiguous':[37,64], 'native_pixel_eyes_ROI_contiguous':[37,64],
          'scaled_fullframe_context_sheets':[[37,64],[65,83]],
          'not_claimed':'Every fullframe viewed at native display scale; entire-video 100ms/native semantic pass'},
 'qualified_prior_review':'agents/gap_review_01/OUT_gap_review_01.json#G001,G002,G003; opening_macro_native_v1/OUT_opening_macro_native_v1.json',
 'objects':[
  {'id':'OPEN_PERCENT_COIN','onset_frame':39,'onset_pts':pts(39),'before_frame':38,
   'first_orange_fill_frame':40,'first_orange_fill_pts':pts(40),
   'first_fully_detached_frame':53,'before_detached_frame':52,
   'last_translation_frame':59,'hold_verified_frames':[60,64],
   'appearance':'Black rim first becomes exposed along right roof slope at39; orange fill first40. White/yellow percent glyph is carried with the disc, progressively revealed by roof occlusion.',
   'motion':'Upward translation behind stationary foreground roof. Visible orange bbox top decreases612 at40 to288 at59; x bounds824..1080 stable after43. No observed scale/rotation change or overshoot in this window. Late steps diminish to2px from58 to59.',
   'geometry_measurement':'orange_bbox_measurements.json; RGB threshold describes visible fill, not hidden full object or production curve',
   'unknown':'Offscreen/fully occluded movement before39, exact source easing preset, rig and source layers; no lifecycle exit established beyond83'},
  {'id':'OPEN_CARD_NBC','onset_frame':49,'onset_pts':pts(49),'before_frame':48,
   'first_full_visible_frame':49,'hold_verified_frames':[49,83],
   'motion':'Complete near-horizontal dark card appears in a single adjacent-frame step at right. No visible sliding-entry phase in37-49.',
   'literal_source_text':{'label':'NBC News','headline':'Fed raises interest rates for first time since 2023, defying Trump as inflation mounts','body':'“The plain fact is that inflation is too high and has been for too long,” Federal Reserve Chair Kevin Warsh said. 0 seconds of 0 seconds.','relative_time':'23 hours ago'},
   'text_status':'Visible source-video text only, not authenticated news/economic facts'},
  {'id':'OPEN_BUILDING_EYES','status':'OBSERVED_UPWARD_POSE_HOLD','frames':[37,64],
   'description':'Pupils remain high within two open oval eyes. No new upward gaze change, blink or deformation observed in native contiguous eye ROIs. Prior accepted pose exists through36; do not invent gaze onset37.',
   'limitation':'Difference vs old OpenCV-decoded36 includes decoder/color differences; static_anchor_metrics is diagnostic, not exact pixel equality proof.'},
  {'id':'OPEN_CARD_FOX','onset_frame':65,'onset_pts':pts(65),'before_frame':64,
   'first_full_visible_frame':65,'hold_verified_frames':[65,83],
   'description':'Complete counterclockwise-tilted Fox Business card pops into lower left below NYT card. No new shot.',
   'literal_source_headline':'Federal Reserve hikes interest rates for first time since 2023 amid stubborn inflation'},
  {'id':'OPEN_CARD_WSJ','onset_frame':82,'onset_pts':pts(82),'before_frame':81,
   'first_full_visible_frame':82,'hold_verified_frames':[82,83],
   'description':'Complete clockwise-tilted WSJ card pops into lower right. No new shot.',
   'literal_source_headline':'Fed Delivers First Rate Hike in Years With Unanimous Vote'}],
 'static_anchors':'Building body/roof and earlier NYT/Conduit cards retain their placements. Independent moving coin against retained anchors supports object motion; no camera movement observed.',
 'corrections':['EP0002 candidate37 is not first visible coin: exact rim39/fill40.', 'Third card entry is discrete full appearance49, not an observed rightward sliding entrance.', 'Building upward eyes are retained pose, not a newly verified reaction in37-59.', 'S0002 draft x≈.75 coin and stick-man description do not match bounded source: coin center≈952/1920=.496, no separate stick-man in37-83.'],
 'actual_listening_seconds':0,'audio':'BLOCKED_NO_QUALIFIED_LISTENING','CT_SCAN_COMPLETE':False,
 'reviewer':'root Codex; internal source review, not independent signoff'}
save('native_observations.json',observations)

rows=list(csv.DictReader((B/'integrated_v4/visual_event_ledger_v15.csv').open()))
before=copy.deepcopy(rows); patches={
 'EP0002':(39,59,'Coin black rim exposed39/orange40; full separation53; upward movement ends59 then hold60-64. Third complete NBC card appears49; eyes retain upward pose.','COMPOUND_OBJECT_MOTION_AND_DISCRETE_ADDITION'),
 'EP0003':(65,65,'Complete tilted Fox Business card appears lower-left65; absent64. Existing composition retained.','ADDITIVE_ENTRY'),
 'EP0004':(82,82,'Complete tilted WSJ card appears lower-right82; absent81. Existing composition retained.','ADDITIVE_ENTRY')}
for r in rows:
    if r['event_id'] not in patches: continue
    first,last,desc,kind=patches[r['event_id']]
    r.update(original_candidate_start_frame=r['source_start_frame'], original_candidate_end_frame=r['source_end_frame'],
             source_start_frame=str(first),source_end_frame=str(last),source_start_pts=str(pts(first)),source_end_exclusive_pts=str(pts(last+1)),
             visual_onset_verified_frame=str(first),observed_change_first_frame=str(first),observed_change_last_frame=str(last),
             description=desc,event_class=kind,review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',
             timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',
             evidence=str(P/'native_observations.json'),macro_review_ref=str(P/'native_observations.json'),
             bounds_role='COMPOUND_EVENT_WITH_SEPARATE_OBJECT_TRACKS' if r['event_id']=='EP0002' else 'EXACT_ADJACENT_NATIVE_ADDITION',
             native_vs_firstpass_conflict='See native_observations corrections; prior raw firstpass preserved')
csvsave('visual_event_ledger_v16.csv',rows)
candidate=lambda rr:sum(x['timing_precision']=='MEASURED_CANDIDATE_WINDOW_NOT_EXACT_VISUAL_ONSET' for x in rr)
assert candidate(before)==712 and candidate(rows)==709
assert len(rows)==len({x['event_id'] for x in rows})==948
assert [x['event_id'] for x,y in zip(before,rows) if x!=y]==list(patches)

part=list(csv.DictReader((B/'integrated_v4/frame_partition_v6.csv').open()))
for r in part:
    if r['interval_id'] in ['G002.01','S0002']:
        r.update(semantic_status='TARGETED_NATIVE_OBJECT_AND_FACIAL_ROI_SEMANTICS_VERIFIED_WITH_FULLFRAME_CONTEXT',
                 source_ref=str(P/'native_observations.json'),boundary_precision='ORIGINAL_NUMERIC_INTERVAL_RETAINED_EXACT_SUBEVENT_TRACKS_SEPARATE',
                 description='Native37-38 no exposed coin; rim39, fill40; complete NBC card49; coin detached53, final move59; hold60-64; eyes hold upward. See object tracks; interval is not a shot.')
csvsave('frame_partition_v7.csv',part)
assert sum(int(r['n_frames']) for r in part)==19862
assert len(part)==627 and len({r['state_id'] for r in part})==475

prior_spec=json.loads((B/'reconstruction_test_v2/SPEC.json').read_text())
gap=json.loads((B/'agents/gap_review_01/OUT_gap_review_01.json').read_text())
g003=next(x for x in gap['items'] if x['id']=='G003')
specs=[]
for i,seg in enumerate(g003['segments'][:3],1):
    specs.append({'state_id':f'G003N0{i}','source_start_frame':seg['start'],'source_end_frame':seg['end'],
       'source_start_pts':pts(seg['start']),'source_end_exclusive_pts':pts(seg['end']+1),
       'observed_source_description':seg['description'],'source_review_ref':'agents/gap_review_01/OUT_gap_review_01.json#G003',
       'source_native_evidence_frames':seg['evidence_frames'],'source_boundary_precision':seg['boundary_precision'],
       'original_design_ref':'reconstruction_test_v2/SPEC.json','original_asset_system':prior_spec,
       'original_image_prompt':f'Original 1920x1080 editorial diagram. Four navy rounded rectangular faces with block bodies around a cream-field elliptical teal table; fixed character centers {prior_spec["character_centers"]}, table center960,760 axes660,140. '+(['No speech panel.','Upper-right coral speech panel reading PLAN A.','Upper-left coral speech panel reading PLAN B; remove PLAN A.'][i-1])+' No competitor character, brand, headline or source dialogue.',
       'animation':{'source_frame_range':[seg['start'],seg['end']], 'original_local_frame_range':[seg['start']-226,seg['end']-226],
                    'entry':['Full diagram cut at226','Discrete PLAN A addition262','Discrete PLAN A removal and PLAN B replacement279'][i-1],
                    'hold':'Characters, eyes, table, background, palette and geometry STATIC within state; text exact, no morphing.',
                    'exit':['Retain diagram for next speech state262','Retain diagram; replace speech state279','Cut to next independent composition301'][i-1]},
       'layer_map':['cream field','fixed table','four original figures','one speech panel if specified'],
       'camera':'Fixed 2D framing; no pan, zoom, focus shift or depth parallax specified',
       'continuity':'Same four original asset IDs and fixed character/table coordinates across G003N01-03',
       'acceptance':['Correct speech-panel state at226/261/262/278/279/300 source-aligned indices','No character/table drift or unintended text/object additions','Retain source-research observations separately from original proposal'],
       'prior_bounded_reconstruction_evidence':'reconstruction_test_v2/independent_QA_completed.json; accepted75-frame original test not rerun',
       'status':'SPECIFICATION_PRESENT_EVIDENCE_BACKED_ORIGINAL_PROPOSAL;GLOBAL_PRODUCTION_QA_NOT_PASSED',
       'audio':'BLOCKED; no heard cues or sync','actual_listening_seconds':0})
save('G003_missing_state_specifications.json',{'states':specs,'new_source_review':False,'reuse_reason':'Qualified native G003 boundaries and existing original75-frame test already accepted; fill missing state-to-spec mappings without repeated full review','CT_SCAN_COMPLETE':False})

idx=json.loads((B/'production_integrated_v1/integrated_production_interval_index_v4.json').read_text())
idx['source_partition']=str(P/'frame_partition_v7.csv')
for sid in [s['state_id'] for s in specs]:
    assert sid in idx['missing_state_ids'];idx['missing_state_ids'].remove(sid)
for r in idx['rows']:
    if r['state_id'] in [s['state_id'] for s in specs]:
        r.update(production_status='NEW_ORIGINAL_STATE_SPEC_PRESENT_GLOBAL_QA_PENDING', original_spec_ref=str(P/'G003_missing_state_specifications.json')+'#'+r['state_id'],animation_static_anchor_status='EXPLICIT_SPEC_PLUS_PRIOR_BOUNDED_TEST;NOT_GLOBAL_PASS')
    if r['interval_id']=='G002.01':
        r.update(source_observation_ref=str(P/'native_observations.json'),source_description=patches['EP0002'][2],source_boundary_precision='EXACT_NATIVE_SUBEVENTS_WITHIN_UNCHANGED_INTERVAL',production_status='EXPLICIT_ORIGINAL_EXTENDED_SPAN_SPEC_PRESENT_BOUNDED_RENDER_QA_PENDING',original_spec_ref=str(P/'RECONSTRUCTION_CRITERIA_FROZEN.json'),animation_static_anchor_status='SOURCE_ROI_VERIFIED;ORIGINAL_RENDER_PENDING')
idx['supplemental_missing_state_specs']=str(P/'G003_missing_state_specifications.json')
idx['remaining_missing_original_specs']=len(idx['missing_state_ids'])
idx['extended_span_resolution']={'resolved_specification_interval_ids':['G002.01'],'render_acceptance':'PENDING','remaining_original_list_count':len(idx['prior_draft_span_extended_intervals'])-1,'definition':'Explicit source-bounded original specification; full production signoff remains separate'}
assert len(idx['missing_state_ids'])==25
save('integrated_production_interval_index_v5.json',idx)
save('batch_validation.json',{'event_rows':948,'candidate_only_before':712,'candidate_only_after':709,'resolved_event_ids':list(patches),'partition_rows':627,'distinct_states':475,'frames_once':19862,'new_specifications':3,'missing_specs_before':28,'missing_specs_after':25,'extended_span_spec_resolved':1,'extended_span_qa':'PENDING_RENDER','global_100ms_native_semantics':'PARTIAL','actual_listening_seconds':0,'CT_SCAN_COMPLETE':False})
print('PASS event timing712->709; missing state specs28->25; extended G002 specification written, render pending')
