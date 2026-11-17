"""Native macro audit plus a bounded graphic-variant track; no new shot count."""
from pathlib import Path
import base64
import collections
import csv
import hashlib
import json
import cv2
import numpy as np

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan');D=R/'selection_macro_review_v1';S=R/'session_20261104'
raw=D/'OUT_selection_macro_review_v1.json';assert hashlib.sha256(raw.read_bytes()).hexdigest()=='7d2aa4c52ea55b7c483eee8f48426fc7cff93ff3e755a6f4e9555dd1bdb11a14'
m=json.loads((D/'items.json').read_text());o=json.loads(raw.read_text());assert not o['pending_new_image_paths'] and o['actual_listening_seconds']==0 and o['CT_SCAN_COMPLETE'] is False
given={x['path']:x for x in m['new_view_requests']+[m['new_context_view_request']]};reads={x['path']:x for x in o['new_evidence_reads']}
assert set(given)==set(reads) and len(reads)==32
for path,x in reads.items():assert x['successful'] and x['witness'] and hashlib.sha256(Path(path).read_bytes()).hexdigest()==x['sha256']==given[path]['sha256']
prior={x['path']:x for x in m['prior19_native_ROI_receipts_reusable_without_repeat']}
assert len(o['reused_prior_evidence_reads'])==19
for x in o['reused_prior_evidence_reads']:assert x['reused_without_new_display'] and x['sha256']==prior[x['path']]['sha256']
logs=[]
for p in Path('/Users/ghilmankhan/.codex/sessions/2026/11').glob('*/*.jsonl'):
    with p.open() as f:meta=json.loads(f.readline())
    if meta.get('payload',{}).get('agent_path')=='/root/targeted_adjudication':logs.append(p)
assert len(logs)==1
actual=[]
for line in logs[0].open():
    event=json.loads(line);x=event.get('payload',{})
    if event.get('timestamp','')<m['recorded_UTC'] or x.get('type')!='custom_tool_call_output' or not isinstance(x.get('output'),list):continue
    for b in x['output']:
        if b.get('type')!='input_image':continue
        url=b.get('image_url');url=url.get('url') if isinstance(url,dict) else url
        if isinstance(url,str) and url.startswith('data:'):actual.append({'call_id':x['call_id'],'sha256':hashlib.sha256(base64.b64decode(url.split(',',1)[1])).hexdigest()})
assert len(actual)==32 and collections.Counter(x['sha256'] for x in actual)==collections.Counter(x['sha256'] for x in reads.values())
def mask_measure(image,start,end):
    band=image[start-570:end-570+1].astype(np.int16);mask=(band[:,:,0]>120)&(band[:,:,0]-band[:,:,2]>40)&(band[:,:,0]-band[:,:,1]>20);cols=np.flatnonzero(mask.sum(axis=0)>=12)
    return {'left_source_x':int(cols[0]+171) if len(cols) else None,'right_source_x':int(cols[-1]+171) if len(cols) else None,'qualifying_pixel_count':int(mask.sum())}
files={x['frame']:x for x in m['all50_prepared_ROIs']}
for point in m['measurements']:
    im=cv2.imread(files[point['frame']]['path']);a=mask_measure(im,604,627)
    assert [a['left_source_x'],a['right_source_x'],a['qualifying_pixel_count']]==[point['dense_blue_left_source_x'],point['dense_blue_right_source_x'],point['dense_blue_pixel_count']]
second=json.loads((D/'new_ROI_line_mask_measurements_v1.json').read_text())['rows'];assert len(second)==31
for point in second:
    im=cv2.imread(files[point['frame']]['path'])
    assert mask_measure(im,604,627)==point['first_line'] and mask_measure(im,628,650)==point['second_line']
proof={'new_actual_returns':actual,'actual_new_native_ROI':31,'actual_new_scaled_context':1,'reused_prior_native_ROI':19,'bytehash_multiplicity':'PASS',
       'first_line_mask_points_independently_reproduced':50,'new_second_line_mask_points_reproduced':31,'actual_listening_seconds':0,
       'limitation':'50numeric mask points do not mean50newfullwidthROIviews; no nativefullframe/physical mouse button/easing/truecolor claim'}
(S/'selection_macro_independent_audit_v1.json').write_text(json.dumps(proof,indent=2)+'\n')
phases=[('PRE_NO_SELECTION',7996,8001),('ONE_LINE_RANGE_EXPANDING',8002,8016),('TWO_LINE_RANGE_EXPANDING',8017,8024),
        ('TWO_LINE_RANGE_HELD',8025,8025),('ONE_LINE_CONTRACT_AND_REFINE',8026,8028),('ONE_LINE_RANGE_HELD',8029,8036),('ONE_LINE_SHORTENED_HELD',8037,8045)]
variants=[];counts=collections.Counter()
for index,(name,start,end) in enumerate(phases,1):
    counts.update(range(start,end+1));variants.append(dict(variant_id=f'SEL_V{index:02}',track='BOUNDED_INTRA_SHOT_SELECTION_ONLY',
       underlying_owner_state='S0167',dominant_composition_group='S0165',start_frame=start,end_frame=end,start_pts=(start+1)/24,end_exclusive_pts=(end+2)/24,
       n_frames=end-start+1,phase=name,source_ref='selection_macro_review_v1/OUT_selection_macro_review_v1.json',
       evidence_scope='31newnativeROI+19priornativeROIobservations+50firstlinemaskmeasurements;not50newfullwidthviews',
       limit='Only7996–8045 track; finalselectionremovalunknown; notnewshots/dominantcompositioncount'))
assert set(counts)==set(range(7996,8046)) and set(counts.values())=={1}
def readcsv(path):
    with path.open() as f:return list(csv.DictReader(f))
def writecsv(path,rows):
    assert not path.exists()
    with path.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
writecsv(R/'integrated_v4/selection_graphic_variants_v1.csv',variants)
events=readcsv(R/'integrated_v4/visual_event_ledger_v5.csv')
for row in events:
    row.update(parent_gesture_id='',macro_review_ref='',native_vs_firstpass_conflict='',pre_macro_record_ref='')
    if row['event_id'] in {'EP0233','SUB101','EP0234','SUB103'}:
        row['parent_gesture_id']=o['macro_id'];row['macro_review_ref']='selection_macro_review_v1/OUT_selection_macro_review_v1.json'
    if row['event_id']=='EP0233':
        row.update(pre_macro_record_ref=row['source_ref'],visual_onset_verified_frame=8002,review_scope='NATIVE_ROI_ONSET8001EMPTY_8002BLUE',timing_precision='SOURCEFRAME_APPEARANCE_VERIFIED;NOT_MOUSE_BUTTON_TIMING')
    if row['event_id']=='EP0234':
        row.update(pre_macro_record_ref=row['source_ref'],description='Selection fills first line and wraps into second line at8017; second-line extent grows through8024, holds8025, then contracts to one line8026. Endpoint refinement8027–8028 belongs parentgesture track. Candidatewindow8009–8026 retained; not cursor teleportation/easing proof.',
                   native_vs_firstpass_conflict='Raw firstpass saidsecond/laterlinesunchanged; nativeROIprovessecond-line blue8017–8025. Rawkeptimmutable.',
                   review_scope='NATIVE_ROI_FIRST_SECOND_LINE_REVIEW;ORIGINAL_CANDIDATE_WINDOW_RETAINED',source_ref='selection_macro_review_v1/OUT_selection_macro_review_v1.json',bounds_role='CANDIDATE_FRAGMENT;FULL_PARENT_PHASES_IN_SELECTION_VARIANT_TRACK')
writecsv(R/'integrated_v4/visual_event_ledger_v6.csv',events)
motion=readcsv(R/'production_v1/motion_camera_facial_index_PARTIAL_v2.csv')
for row in motion:
    row['parent_gesture_review']=''
    if row['id'] in {'EP0233','SUB101','EP0234','SUB103'}:row['parent_gesture_review']='selection_macro_review_v1/OUT_selection_macro_review_v1.json'
    if row['id']=='EP0234':
        row.update(type='TEXT_SELECTION_RANGE_WRAP_AND_CONTRACT',motion_status='NATIVE_ROI_MACRO_PHASE_REVIEWED;CANDIDATE_FRAGMENT',
                   path=json.dumps(o['motion_object']['path']),easing='UNKNOWN',duration_note=o['motion_object']['duration_note'],
                   curated_observed_change='Two-line selection excursion8017–8025 and contraction8026; contradicts originalsecondlineunchangedclaim. Firstlinewidthjump is range-wrap logic, not measured cursorvelocity.',
                   curated_motion_review='selection_macro_review_v1/OUT_selection_macro_review_v1.json',curated_motion_object=json.dumps(o['motion_object']))
writecsv(R/'production_v1/motion_camera_facial_index_PARTIAL_v3.csv',motion)
conflict={'candidate':'EP0234','raw_claim':'second and later lines unchanged','ruling':'CONTRADICTED_IN_NATIVE_ROI_SECOND_LINE_SELECTION8017–8025',
          'raw_source':'agents/shard_5/OUT_shard_5.json','curated_source':'selection_macro_review_v1/OUT_selection_macro_review_v1.json',
          'raw_file_unchanged':True,'dominant_frame_partition':'v4unchanged; boundedselectionvariants separate','cursor_velocity_from_line_width_jump':'NOT_ESTABLISHED',
          'selection_removal':'UNKNOWN_BEYOND8045','easing':'UNKNOWN','event_rows':len(events),'bounded_graphic_variant_rows':7,'CT_SCAN_COMPLETE':False}
(S/'selection_macro_integration_v6_stats.json').write_text(json.dumps(conflict,indent=2)+'\n');print(json.dumps(conflict))
