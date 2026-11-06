# Additive: writes ep0015_native_batch/native_observations.json, visual_event_ledger_v27.csv, CURRENT_NATIVE_QUEUE_v3.json. v26/queue v2 untouched.
import csv, json, glob, os, hashlib
import numpy as np
from PIL import Image
E=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B=os.path.join(E,'ep0015_native_batch')
rows=[];prev=None
for p in sorted(glob.glob(B+'/frames/f*.png')):
    f=int(os.path.basename(p)[1:6]); x=np.asarray(Image.open(p).convert('RGB')).astype(int)
    y=int(((x[...,0]>200)&(x[...,1]>180)&(x[...,2]<120)).sum()); d=None if prev is None else int((np.abs(x-prev).sum(2)>60).sum()); prev=x
    rows.append({'frame':f,'yellow_pixels':y,'changed_pixels_vs_prev':d,'sha256':hashlib.sha256(open(p,'rb').read()).hexdigest()})
pose=max(rows[1:],key=lambda r:r['changed_pixels_vs_prev'])['frame']; hl=next(r['frame'] for r in rows if r['yellow_pixels']>0)
assert (pose,hl)==(337,338),(pose,hl)
obs={'video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',
 'extraction':'ffmpeg select=between(n,313,345) fps_mode passthrough start_number 313 (native 1920x1080 PNG, 33 frames, local only)',
 'method':'Full-frame yellow threshold r>200,g>180,b<120 and changed-pixel count (>60 abs RGB diff) vs previous frame (measured) + 3-frame half-scale strip 336-338 viewed by Claude session 88d103b4 (visual)',
 'measurements':rows,
 'visual_observations':{'336':'pointer arm low/horizontal, no yellow, date selection still blue','337':'pointer arm raised to diagonal toward first body line; no yellow','338':'small yellow highlight on first word The; arm unchanged'},
 'rulings':{'EP0015':{'pose_swap_exact_native_frame':337,'highlight_onset_exact_native_frame':338,'note':'compound split: pose onset 337 (changed px 13053 vs 1 at 336), yellow onset 338 (256 px) growing to 2149 at 345; highlight is a separate onset one frame after pose'},
            'SUB008':{'note':'measured small cursor-scale changes 327-335 (108-156 px/frame), pose static; consistent with cursor motion; not individually viewed'}},
 'unknowns':['highlight extent/end after 345 not measured','SUB007 313 and SUB008 cursor path not visually inspected','yellow threshold may miss anti-aliased edge'],
 'audio':'NOT_LISTENED','ct_scan_complete':False}
json.dump(obs,open(B+'/native_observations.json','w'),indent=1)
rd=list(csv.DictReader(open(os.path.join(E,'visual_event_ledger_v26.csv'),newline=''))); fn=list(rd[0].keys()); hit=0
for r in rd:
    if r['event_id']=='EP0015':
        r.update(visual_onset_verified_frame='337',observed_change_first_frame='337',observed_change_last_frame='338',timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',original_candidate_start_frame='337',original_candidate_end_frame='337',evidence=B+'/native_observations.json',macro_review_ref=B+'/native_observations.json#EP0015',description='Pointer arm swaps low to diagonal at 337 (exact); small yellow highlight on The starts one frame later at 338 and grows through 345.'); hit+=1
assert hit==1
with open(os.path.join(E,'visual_event_ledger_v27.csv'),'w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=fn); w.writeheader(); w.writerows(rd)
q=json.load(open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v2.json')))
q['items']=[i for i in q['items'] if i['event_id']!='EP0015']; q['count']=len(q['items']); q['baseline']='visual_event_ledger_v27.csv'
q['next_atomic_operation']='Next queue item after EP0015 in queue order (inspect CURRENT_NATIVE_QUEUE_v3.json first item); reuse ep0014/ep0015 native frames 296-345 before extracting. Do not repeat SUB006/EP0014/EP0015.'
json.dump(q,open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v3.json'),'w'),indent=1)
print('pose',pose,'hl',hl,'queue',q['count'])
