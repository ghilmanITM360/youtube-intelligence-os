# Additive: writes sub007_008_native_batch/native_observations.json, visual_event_ledger_v28.csv, CURRENT_NATIVE_QUEUE_v4.json. v27/queue v3 untouched.
# Reuses existing native frames 303-338 (ep0014/ep0015 batches); no new extraction.
import csv, json, glob, os, hashlib
import numpy as np
from PIL import Image
E=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B=os.path.join(E,'sub007_008_native_batch')
paths={int(os.path.basename(p)[1:6]):p for p in glob.glob(E+'/ep0014_native_batch/frames/f*.png')+glob.glob(E+'/ep0015_native_batch/frames/f*.png')}
rows=[];prev=None
for f in range(303,339):
    x=np.asarray(Image.open(paths[f]).convert('RGB')).astype(int)
    roi=x[430:460,130:330]; b=(roi[...,2]>150)&(roi[...,2]-roi[...,0]>60)&(roi[...,2]-roi[...,1]>20); cols=np.where(b.any(0))[0]
    d=None if prev is None else int((np.abs(x-prev).sum(2)>60).sum()); prev=x
    rows.append({'frame':f,'blue_pixels':int(b.sum()),'blue_x_left':int(130+cols.min()) if len(cols) else None,'changed_pixels_vs_prev':d,'sha256':hashlib.sha256(open(paths[f],'rb').read()).hexdigest()})
R={r['frame']:r for r in rows}
# positive: selection left edge grows 308->312 (SUB006 continuation), then static 314-326; cursor motion 327-335; static 336
assert R[308]['blue_x_left']==170 and R[312]['blue_x_left']==142, 'selection growth'
assert all(R[f]['changed_pixels_vs_prev']<=2 for f in range(314,327)), 'static hold 314-326'
assert all(R[f]['changed_pixels_vs_prev']>=100 for f in (327,328,329,330,331,333,334,335)), 'cursor motion'
assert R[336]['changed_pixels_vs_prev']<=2 and R[337]['changed_pixels_vs_prev']>10000
# negative: no selection growth after 313 (left edge never moves left of 141), no motion between 314 and 326
assert min(R[f]['blue_x_left'] for f in range(313,339))>=141
assert next(f for f in range(314,339) if R[f]['changed_pixels_vs_prev']>=100)==327
obs={'video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',
 'extraction':'none; reused ep0014_native_batch/frames 303-312 and ep0015_native_batch/frames 313-338 (native 1920x1080 PNG)',
 'method':'Date ROI y430-460 x130-330 blue threshold (as ep0014) + full-frame changed px (>60 abs RGB) vs prev (measured) + native ROI crop strip x110-310 y410-670 of 307,308,312,313,314,326,327,329,331,333,335,336 viewed by Claude scheduled session 5c8c86e3 (visual)',
 'measurements':rows,
 'visual_observations':{'307':'I-beam inside date, partial selection','308':"'29, 2026' selected, I-beam",'312':'full July 29, 2026 selected; cursor now arrow left of date','313-326':'arrow static, selection kept','327-329':'arrow moves down-left toward Share','331-333':'arrow near second body line','335-336':'arrow at start of first body line The Federal Open Market...'},
 'rulings':{'SUB007':{'class':'CONTINUATION_PHASE_OF_PARENT_GESTURE','parent':'SUB006','note':'selection left edge 170->142 over 308-312 is the tail of the SUB006 right-to-left drag; I-beam to arrow at 312; 313 has 138 scattered px and 1px edge settle, visually identical to 312; not an independent onset'},
            'SUB008':{'class':'CURSOR_MOVE','exact_onset':327,'last_change':335,'note':'after 13 static frames (314-326 changed px<=2) arrow moves 327-335 down then up to first body line; selection kept; 336 static; EP0015 pose at 337'}},
 'unknowns':['blue count +12 px at 329 (1697->1709) unexplained, likely anti-alias near cursor','cursor exact path per frame only sampled visually (6 of 9 frames)'],
 'audio':'NOT_LISTENED','ct_scan_complete':False}
json.dump(obs,open(B+'/native_observations.json','w'),indent=1)
rd=list(csv.DictReader(open(os.path.join(E,'visual_event_ledger_v27.csv'),newline=''))); fn=list(rd[0].keys()); hit=0
common=dict(review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',evidence=B+'/native_observations.json')
for r in rd:
    if r['event_id']=='SUB007':
        r.update(common,visual_onset_verified_frame='308',original_candidate_start_frame='308',original_candidate_end_frame='313',observed_change_first_frame='308',observed_change_last_frame='313',bounds_role='CONTINUATION_PHASE_OF_PARENT_GESTURE',parent_gesture_id='SUB006',macro_review_ref=B+'/native_observations.json#SUB007',
                 description='Continuation of SUB006 drag: selection extends 308-312 to full July 29, 2026; I-beam becomes arrow at 312; 313 settle; not an independent onset.'); hit+=1
    elif r['event_id']=='SUB008':
        r.update(common,visual_onset_verified_frame='327',original_candidate_start_frame='327',original_candidate_end_frame='335',observed_change_first_frame='327',observed_change_last_frame='335',macro_review_ref=B+'/native_observations.json#SUB008',
                 description='Arrow cursor moves 327-335 (after static 314-326) from left of date down past Share to start of first body line; selection kept; no new content.'); hit+=1
assert hit==2
with open(os.path.join(E,'visual_event_ledger_v28.csv'),'w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=fn); w.writeheader(); w.writerows(rd)
q=json.load(open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v3.json')))
q['items']=[i for i in q['items'] if i['event_id'] not in ('SUB007','SUB008')]; q['count']=len(q['items']); q['baseline']='visual_event_ledger_v28.csv'
q['next_atomic_operation']='Next queue item (first item of CURRENT_NATIVE_QUEUE_v4.json); extract only its bounded native window. Do not repeat SUB006/EP0014/EP0015/SUB007/SUB008.'
json.dump(q,open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v4.json'),'w'),indent=1)
print('queue',q['count'],'next',[i['event_id'] for i in q['items'][:3]])
