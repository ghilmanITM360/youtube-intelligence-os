"""Validate bounded motion evidence and version curated indexes; retain raw drafts."""
from pathlib import Path
import base64
import collections
import csv
import hashlib
import json
import cv2
import numpy as np

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'motion_missing_fields_review_v1'
S=R/'session_20261104'
raw=D/'OUT_motion_missing_fields_review_v1.json'
assert hashlib.sha256(raw.read_bytes()).hexdigest()=='c5baa2245214844fe92b785ee8b17a7befb7ef8739adb0c1b64d43d33ffe6ffd'
out=json.loads(raw.read_text()); manifest=json.loads((D/'extraction_manifest_v1.json').read_text())
want={x['id']:x for x in manifest['records']}; by={x['id']:x for x in out['items']}
assert set(by)==set(want)=={'SUB101','SUB103','SUB104','SUB151'} and len(out['items'])==4 and out['pending_ids']==[]
assert out['actual_listening_seconds']==0 and out['full_CT_claim'] is False
reads={x['path']:x for x in out['evidence_reads']}; assert len(reads)==len(out['evidence_reads'])==48
supplied={x['path']:x for item in want.values() for x in item['evidence_images']}
assert set(reads)==set(supplied)
for path,x in reads.items():
    assert x['successful'] and x['witness'].strip()
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==x['sha256']==supplied[path]['sha256']
for ident,x in by.items():
    assert isinstance(x['motion_object'],dict) and x['motion_object']['path'] and x['motion_object']['duration_note']
    assert x['motion_object']['easing']=='UNKNOWN' and x['evidence_paths'] and set(x['evidence_paths'])<=set(reads)
    for field in ['first_observed_change_frame','last_observed_change_frame','event_onset_frame','event_offset_frame']:
        n=x.get(field)
        assert n is None or want[ident]['pre_frame']<=n<=want[ident]['stable_frame']
    assert x['first_observed_change_frame']<=x['last_observed_change_frame']

# Ignore every old target-review image return, requiring new calls after this extraction.
logfiles=[]
for p in Path('/Users/ghilmankhan/.codex/sessions/2026/11').glob('*/*.jsonl'):
    with p.open() as f:meta=json.loads(f.readline())
    if meta.get('payload',{}).get('agent_path')=='/root/targeted_adjudication':logfiles.append(p)
assert len(logfiles)==1
actual=[]
for line in logfiles[0].open():
    event=json.loads(line); x=event.get('payload',{})
    if event.get('timestamp','')<manifest['recorded_UTC']:continue
    if x.get('type')!='custom_tool_call_output' or not isinstance(x.get('output'),list):continue
    for block in x['output']:
        if block.get('type')!='input_image':continue
        url=block.get('image_url');url=url.get('url') if isinstance(url,dict) else url
        if isinstance(url,str) and url.startswith('data:'):
            actual.append({'call_id':x['call_id'],'sha256':hashlib.sha256(base64.b64decode(url.split(',',1)[1])).hexdigest()})
need=collections.Counter(x['sha256'] for x in reads.values()); have=collections.Counter(x['sha256'] for x in actual)
assert need==have and len(actual)==48

# Independently reproduce the published local change measurements, without assigning semantic meaning to thresholds.
checks=[]
for ident,x in by.items():
    images={y['frame']:cv2.imread(y['path']) for y in want[ident]['evidence_images'] if y['scale'].startswith('NATIVE')}
    adjacent=x['frame_measurements']['adjacent']
    for row in adjacent:
        n=row['frame']
        if 'adjacent_delta_max' not in row:continue
        delta=np.abs(images[n].astype(np.int16)-images[n-1].astype(np.int16))
        count=int(np.any(delta>35,axis=2).sum()); maximum=int(delta.max())
        assert count==row['adjacent_pixels_delta_gt35'] and maximum==row['adjacent_delta_max'],(ident,n,count,maximum)
        checks.append({'id':ident,'frame':n,'count_delta_gt35':count,'max_delta':maximum})
proof={'items':4,'pending':0,'actual_returns':actual,'image_bytehash_multiplicity':'PASS','unique_image_paths':48,'distinct_image_hashes':len(need),
       'native_ROI_returns':40,'native_fullframe_returns':0,'scaled_context_returns':8,'recomputed_adjacent_measurements':checks,
       'source_decode_integrity':'88/88derivatives exact against full nonseeking same decoder; see sequential_same_decoder_seek_integrity_audit_v1.json',
       'actual_listening_seconds':0,'cross_pipeline_color_caveat':'Do not mix numerical RGB between OpenCV and systemFFmpeg conversions'}
(S/'motion_missing_fields_independent_audit_v1.json').write_text(json.dumps(proof,indent=2)+'\n')

def readcsv(path):
    with path.open() as f:return list(csv.DictReader(f))
def writecsv(path,rows):
    assert not path.exists()
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

motion=readcsv(R/'production_v1/motion_camera_facial_index_PARTIAL_v1.csv')
for row in motion:
    x=by.get(row['id']);row['curated_motion_review']='';row['curated_motion_object']='';row['curated_observed_change']=''
    if x:
        m=x['motion_object'];row.update(type=x['event_type'],verdict=x['verdict'],motion_status='NATIVE_ROI_BOUNDED_REVIEWED;GLOBAL_ONSET_SCOPE_PARTIAL',
                                      path=m['path'],easing=m['easing'],duration_note=m['duration_note'],curated_observed_change=x['observed_change'],
                                      validation='Independent nativeROIreview; rawfirstpass preserved; local threshold measurements reproduced; no exact curve/audio claim',
                                      curated_motion_review='motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json#'+row['id'],curated_motion_object=json.dumps(m))
writecsv(R/'production_v1/motion_camera_facial_index_PARTIAL_v2.csv',motion)
events=readcsv(R/'integrated_v4/visual_event_ledger_v4.csv')
for row in events:
    x=by.get(row['event_id'])
    row.update(original_candidate_start_frame='',original_candidate_end_frame='',observed_change_first_frame='',observed_change_last_frame='',motion_object='',bounds_role='INHERITED_FROM_V4')
    if x:
        row.update(original_candidate_start_frame=row['source_start_frame'],original_candidate_end_frame=row['source_end_frame'],
                   observed_change_first_frame=x['first_observed_change_frame'],observed_change_last_frame=x['last_observed_change_frame'],
                   event_class=x['event_type'],description=x['observed_change'],evidence=json.dumps(x['evidence_paths']),
                   review_scope='NATIVE_1to1_ROI_CONSECUTIVE_SEQUENCE_PLUS_SCALED_CONTEXT;NOT_FULLFRAME',
                   source_ref='motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json#'+x['id'],motion_object=json.dumps(x['motion_object']))
        if x.get('event_onset_frame') is not None and x.get('event_offset_frame') is not None:
            start=x['event_onset_frame'];end=x['event_offset_frame']
            row.update(source_start_frame=start,source_end_frame=end,source_start_pts=(start+1)/24,source_end_exclusive_pts=(end+2)/24,
                       visual_onset_verified_frame=start,timing_precision='NATIVE_ROI_SUBSTANTIVE_CHANGE_BOUNDS;THRESHOLD_AND_COLOR_PIPELINE_LIMITS',bounds_role='REVIEWED_SUBSTANTIVE_MOTION_BOUNDS')
        else:
            row.update(visual_onset_verified_frame='',timing_precision='CANDIDATE_WINDOW_RETAINED;TRUE_FULL_EVENT_ONSET_OFFSET_UNKNOWN',bounds_role='ORIGINAL_CANDIDATE_ONLY;OBSERVED_CHANGE_RANGE_SEPARATE')
writecsv(R/'integrated_v4/visual_event_ledger_v5.csv',events)
summary={'reviewed_missing_motion_objects':list(by),'normalized_motion_objects_missing':0,'raw_first_pass_missing_fields_retained':list(by),
         'native_ROI_exact_substantive_bounds':{'SUB103':[8034,8038],'SUB104':[8049,8057]},
         'full_event_bounds_still_unknown':['SUB101','SUB151'],'pure_SUB151_appearance_onset':'UNVERIFIED;translation confirmed; faint prewindow mark',
         'all_easing':'UNKNOWN','composition_partition':'v4unchanged19862once; no new shot count','event_rows':len(events),'motion_index_rows':len(motion),
         'status':'FOUR_BOUNDED_MOTION_SUPPLEMENTS_INTEGRATED;NOT_GLOBAL_CT_MOTION_PASS'}
(S/'motion_integration_v5_stats.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
