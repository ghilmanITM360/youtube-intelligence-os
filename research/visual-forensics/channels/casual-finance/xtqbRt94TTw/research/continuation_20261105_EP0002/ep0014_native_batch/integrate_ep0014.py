# Additive: writes native_observations.json, visual_event_ledger_v26.csv, CURRENT_NATIVE_QUEUE_v2.json. v25/queue v1 untouched.
import csv, json, hashlib, glob, os, sys
import numpy as np
from PIL import Image
E=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); B=os.path.join(E,'ep0014_native_batch')
SRC="/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4"
def blue(x): r,g,b=x[...,0],x[...,1],x[...,2]; return (b>150)&(b-r>60)&(b-g>20)
rows=[]
for p in sorted(glob.glob(B+'/frames/f*.png')):
    f=int(os.path.basename(p)[1:6]); x=np.asarray(Image.open(p).convert('RGB')).astype(int)[430:460,130:330]
    m=blue(x); xs=np.nonzero(m)[1]
    rows.append({'frame':f,'pts':f/24,'blue_pixels':int(m.sum()),'x_left':int(xs.min()+130) if m.sum() else None,'x_right':int(xs.max()+130) if m.sum() else None,'sha256':hashlib.sha256(open(p,'rb').read()).hexdigest()})
onset=next(r['frame'] for r in rows if r['blue_pixels']>0)
obs={'video_id':'xtqbRt94TTw','source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66','source_path':SRC,
 'extraction':'ffmpeg select=between(n,296,312) fps_mode passthrough start_number 296 (native 1920x1080 PNG)',
 'method':'Date ROI y430-460 x130-330 RGB blue threshold b>150,b-r>60,b-g>20 (measured) + 2x nearest crop strip date_native303-312_x2.png viewed by Claude session 2547cbe6 (visual)',
 'measurements':rows,
 'visual_observations':{'303':'arrow pointer right of date, no selection','304':'I-beam cursor at right end of 2026, no selection','305':'blue selection on final digit 6 (first selected frame)','306':'selection covers full 2026','307':', 2026','308':'29, 2026','309':'hold 29, 2026 (cursor moves only)','310':'ly 29, 2026','311':'uly 29, 2026','312':'full July 29, 2026 selected; arrow pointer returns lower-left'},
 'rulings':{'SUB006':{'exact_native_visual_onset_frame':onset,'cursor_ibeam_first_frame':304,'note':'first-pass window 303-304 was cursor precursor; blue selection onset is 305'},
            'EP0014':{'ruling':'CONTINUATION_OF_SUB006_DRAG_NOT_INDEPENDENT_ONSET','frame':306,'note':'306 is the second frame of one continuous right-to-left drag 305-312 (309 single-frame hold); full date reached 312; hold after 312 not measured'}},
 'unknowns':['selection hold/removal after 312 not inspected','cursor path inferred from visible glyphs only; no source-editor claim'],
 'audio':'NOT_LISTENED','ct_scan_complete':False}
assert onset==305, onset
json.dump(obs,open(B+'/native_observations.json','w'),indent=1)
L=os.path.join(E,'visual_event_ledger_v25.csv'); rd=list(csv.DictReader(open(L,newline='')))
fn=list(rd[0].keys()); hit=0
for r in rd:
    if r['event_id']=='SUB006':
        r.update(source_start_frame='305',source_end_frame='312',source_start_pts=str(305/24),source_end_exclusive_pts=str(313/24),visual_onset_verified_frame='305',observed_change_first_frame='305',observed_change_last_frame='312',timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',original_candidate_start_frame='303',original_candidate_end_frame='304',evidence=B+'/native_observations.json',macro_review_ref=B+'/native_observations.json#SUB006',description='Blue date selection: I-beam at end of date 304; selection onset on final 6 at 305; drags right-to-left continuously to full "July 29, 2026" at 312 (hold 309).'); hit+=1
    if r['event_id']=='EP0014':
        r.update(parent_gesture_id='SUB006',visual_onset_verified_frame='306',observed_change_first_frame='306',observed_change_last_frame='306',timing_precision='EXACT_NATIVE_VISUAL_ONSET_AND_BOUNDED_LAST_CHANGE',review_scope='TARGETED_NATIVE_BOUNDARY_AND_OBJECT_ROI_REVIEW',bounds_role='CONTINUATION_PHASE_OF_PARENT_GESTURE',original_candidate_start_frame='306',original_candidate_end_frame='306',evidence=B+'/native_observations.json',macro_review_ref=B+'/native_observations.json#EP0014',description="Selection reaches full '2026' at 306 as a continuation phase of SUB006 drag (not an independent onset)."); hit+=1
assert hit==2
with open(os.path.join(E,'visual_event_ledger_v26.csv'),'w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=fn); w.writeheader(); w.writerows(rd)
q=json.load(open(os.path.join(E,'CURRENT_NATIVE_QUEUE.json')))
q['items']=[i for i in q['items'] if i['event_id'] not in ('SUB006','EP0014')]; q['count']=len(q['items']); q['baseline']='visual_event_ledger_v26.csv'
q['next_atomic_operation']='EP0015 f337 pose/highlight compound (with SUB007/SUB008 neighbours): reuse ep0014_native_batch frames 296-312 first, extract only 313-345 native; then continue queue order. Do not repeat SUB006/EP0014 (resolved v26) or accepted EP0002/opening/date/cursor phases.'
json.dump(q,open(os.path.join(E,'CURRENT_NATIVE_QUEUE_v2.json'),'w'),indent=1)
print('onset',onset,'queue',q['count'])
