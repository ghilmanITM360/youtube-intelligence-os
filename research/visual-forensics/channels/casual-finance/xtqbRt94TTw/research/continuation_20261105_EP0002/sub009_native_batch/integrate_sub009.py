# Additive: writes sub009_native_batch/native_observations.json, visual_event_ledger_v29.csv, CURRENT_NATIVE_QUEUE_v5.json. v28/queue v4 untouched.
# Reuses ep0015 native frames 336-345; new extraction 346-405 (ffmpeg select=between(n,346,405), fps_mode passthrough, start_number 346).
import csv, json, glob, os, hashlib
import numpy as np
from PIL import Image
E=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B=os.path.join(E,'sub009_native_batch')
paths={int(os.path.basename(p)[1:6]):p for p in glob.glob(E+'/ep0015_native_batch/frames/f*.png')+glob.glob(B+'/frames/f*.png')}
rows=[];prev=None
for f in range(336,406):
    x=np.asarray(Image.open(paths[f]).convert('RGB')).astype(int)
    y=(x[...,0]>200)&(x[...,1]>180)&(x[...,2]<120); ys,xs=np.where(y)
    if prev is None: d=None; dbox=None
    else:
        m=np.abs(x-prev).sum(2)>60; my,mx=np.where(m); d=int(m.sum()); dbox=[int(mx.min()),int(mx.max()),int(my.min()),int(my.max())] if len(mx) else None
    prev=x
    rows.append({'frame':f,'yellow_pixels':int(y.sum()),'yellow_x_right':int(xs.max()) if len(xs) else None,'yellow_y':[int(ys.min()),int(ys.max())] if len(ys) else None,
                 'changed_pixels_vs_prev':d,'changed_bbox_xyxy':dbox,'sha256':hashlib.sha256(open(paths[f],'rb').read()).hexdigest()})
R={r['frame']:r for r in rows}
# positive: sweep grows monotonically 338->377 on one line (y 600-619), ends at x 853; cursor-only motion 378-396; static 397-405
assert R[337]['yellow_pixels']==0 and R[338]['yellow_pixels']>0, 'highlight onset 338 (EP0015)'
assert all(R[f]['yellow_x_right']>R[f-1]['yellow_x_right'] for f in range(339,378)), 'sweep growth 339-377'
assert R[377]['yellow_x_right']==853 and all(R[f]['yellow_x_right']==853 for f in range(377,406)), 'sweep complete 377'
assert all(R[f]['yellow_y']==[600,619] for f in range(338,406)), 'single line'
assert all(50<=R[f]['changed_pixels_vs_prev']<=200 for f in range(378,397)), 'cursor motion 378-396'
assert all(R[f]['changed_pixels_vs_prev']<=6 for f in range(397,406)), 'static 397-405'
# negative: nothing changes in the stick-figure/pointer area (x>900) after the EP0015 pose at 337; no yellow growth after 377
fr={f:np.asarray(Image.open(paths[f]).convert('RGB')).astype(int) for f in range(337,406)}
right={f:int((np.abs(fr[f]-fr[f-1]).sum(2)>60)[:,900:].sum()) for f in range(338,406)}
ptr={f:int((np.abs(fr[f]-fr[f-1]).sum(2)>60)[450:1080,1100:1600].sum()) for f in range(338,406)}
assert all(v==0 for v in ptr.values()), 'pointer/figure ROI x1100-1600 y450-1080 unchanged 338-405'
assert right[338]<=4 and all(right[f]==0 for f in range(339,406)), 'only 4px header residue at 338 right of x900'
assert max(R[f]['yellow_pixels'] for f in range(377,406))-R[377]['yellow_pixels']<60, 'no new highlight after 377'
obs={'video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',
 'extraction':'reused ep0015_native_batch/frames 336-345; new ffmpeg select=between(n,346,405) fps_mode passthrough start_number 346 (60 native 1920x1080 PNG, local only); alignment check: re-extracted 345 pixel-identical to ep0015 f00345',
 'method':'Full-frame yellow threshold r>200,g>180,b<120 (as ep0015) + changed px (>60 abs RGB) vs prev with bbox (measured) + native ROI strip x100-900 y520-700 of 338,350,365,377,378,381,385,390,396,398 and half-scale overview f377 viewed by Claude scheduled session b69509dd (visual)',
 'measurements':rows,
 'visual_observations':{'338':'small yellow on Th of The; I-beam cursor at line start','350-365':'highlight extends left-to-right; arrow cursor near line end / mid line','377':'full first body line highlighted to vote:; I-beam on second line near 3-1/2 to','378-381':'I-beam then arrow move right near percent / line end','385-390':'arrow moves up then left over highlighted line','396-398':'arrow rests below-left near Share; static','pointer':'stick-figure diagonal pointer unchanged 338-405'},
 'rulings':{'SUB009':{'class':'CONTINUATION_PHASE_OF_PARENT_GESTURE','parent':'EP0015','highlight_onset':338,'sweep_complete':377,'cursor_move':[378,396],'static_from':397,
   'note':'highlight onset 338 already credited to EP0015 (pose 337 + highlight 338); SUB009 is the sweep body ~18 px/frame 339-377 to x=853 then cursor drift 378-396; static 397; no new content'}},
 'unknowns':['4 scattered changed px at 338 in header banner x931-1219 y108-301 (one frame after the 13053-px pose swap at 337; likely encoder residue, not an object event)','yellow count +46 px at 383 then settles ~11234 (cursor overlap with highlight, likely)','cursor path sampled visually on 8 of 19 frames','highlight is a synthetic overlay; no text-selection claim'],
 'audio':'NOT_LISTENED','ct_scan_complete':False}
json.dump(obs,open(B+'/native_observations.json','w'),indent=1)
rd=list(csv.DictReader(open(os.path.join(E,'visual_event_ledger_v28.csv'),newline=''))); fn=list(rd[0].keys()); hit=0
for r in rd:
    if r['event_id']=='SUB009':
        r.update(review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',evidence=B+'/native_observations.json',
                 visual_onset_verified_frame='338',original_candidate_start_frame='339',original_candidate_end_frame='396',observed_change_first_frame='338',observed_change_last_frame='396',
                 bounds_role='CONTINUATION_PHASE_OF_PARENT_GESTURE',parent_gesture_id='EP0015',macro_review_ref=B+'/native_observations.json#SUB009',
                 description="Yellow highlight (onset 338, credited to EP0015) sweeps first body line left-to-right 339-377 to 'vote:' (x=853); cursor moves 378-396; static 397; pointer held.")
        hit+=1
assert hit==1
with open(os.path.join(E,'visual_event_ledger_v29.csv'),'w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=fn); w.writeheader(); w.writerows(rd)
q=json.load(open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v4.json')))
q['items']=[i for i in q['items'] if i['event_id']!='SUB009']; q['count']=len(q['items']); q['baseline']='visual_event_ledger_v29.csv'
q['next_atomic_operation']='Next queue item (first item of CURRENT_NATIVE_QUEUE_v5.json); extract only its bounded native window. Do not repeat SUB006-SUB009/EP0014/EP0015.'
json.dump(q,open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v5.json'),'w'),indent=1)
print('queue',q['count'],'next',[i['event_id'] for i in q['items'][:3]])
