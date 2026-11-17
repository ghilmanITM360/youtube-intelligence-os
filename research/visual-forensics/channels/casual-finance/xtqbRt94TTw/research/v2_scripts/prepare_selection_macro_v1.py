"""Bounded first-line selection trace, with explicit reuse of reviewed motion ROIs."""
from pathlib import Path
import cv2
import numpy as np
import json
import hashlib
import datetime

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'selection_macro_review_v1';assert not D.exists();D.mkdir()
source='/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4'
prior=json.loads((R/'motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json').read_text())
old_reads={x['path']:x for x in prior['evidence_reads']}
old_frames=set(range(8003,8009))|set(range(8033,8046))
old_refs=[]
for item in prior['items']:
    if item['id'] not in {'SUB101','SUB103'}:continue
    for path in item['evidence_paths']:
        x=old_reads[path]
        if x['scale'].startswith('NATIVE'):
            old_refs.append(x)
assert len(old_refs)==19
cap=cv2.VideoCapture(source);assert cap.isOpened();records=[];images=[];box=[171,570,1595,684]
for n in range(8046):
    ok,frame=cap.read();assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES))==n+1
    if n<7996:continue
    roi=frame[570:685,171:1596];path=D/f'f{n:05d}_nativeROI.png';assert cv2.imwrite(str(path),roi)
    band=frame[604:628,171:1596].astype(np.int16)
    mask=(band[:,:,0]>120)&(band[:,:,0]-band[:,:,2]>40)&(band[:,:,0]-band[:,:,1]>20)
    dense=np.flatnonzero(mask.sum(axis=0)>=12)
    records.append({'frame':n,'source_pts_s':(n+1)/24,'dense_blue_left_source_x':int(dense[0]+171) if len(dense) else None,
                    'dense_blue_right_source_x':int(dense[-1]+171) if len(dense) else None,'dense_blue_pixel_count':int(mask.sum()),
                    'decoded_position_after_read':n+1})
    images.append({'frame':n,'source_pts_s':(n+1)/24,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                   'width':1425,'height':115,'scale':'NATIVE_1to1_ROI_NOT_FULLFRAME',
                   'request_new_actual_view':n not in old_frames,'coverage_note':'First-line full-width ROI. Old SUB103 views only covered its right-end subregion; old observations must not be relabelled as a fresh full-width view.'})
    if n==7996:
        context=D/'f07996_context960.jpg';assert cv2.imwrite(str(context),cv2.resize(frame,(960,540)),[cv2.IMWRITE_JPEG_QUALITY,95])
        context_record={'frame':n,'path':str(context),'sha256':hashlib.sha256(context.read_bytes()).hexdigest(),'scale':'SCALED_CONTEXT960x540','width':960,'height':540}
cap.release()
manifest={'source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',
          'recorded_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'window_frames':[7996,8045],'ROI_xyxy_inclusive':box,
          'decode_method':'Full non-seeking OpenCV source decode from frame0 through8045, checked frame positions; same declared conversion pipeline as previously audited native evidence. No interpolation/seek.',
          'measurement_rule':'SourceY604:627,X171:1595; B>120,B-R>40,B-G>20; densecolumn pixelcount>=12. Heuristic selection-mask measurement, not source curves/true color.',
          'all50_prepared_ROIs':images,'new_view_requests':[x for x in images if x['request_new_actual_view']],
          'new_context_view_request':context_record,'prior19_native_ROI_receipts_reusable_without_repeat':old_refs,
          'prior_review':'motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json; separately byte-audited in session_20261104/motion_missing_fields_independent_audit_v1.json',
          'measurements':records,'actual_listening_seconds':0,'status':'PREPARED_NOT_NEWLY_VIEWED'}
(D/'items.json').write_text(json.dumps(manifest,indent=2)+'\n')
positive=[x for x in records if x['dense_blue_right_source_x'] is not None]
changes=[(a['frame'],b['frame'],a['dense_blue_right_source_x'],b['dense_blue_right_source_x']) for a,b in zip(records,records[1:]) if a['dense_blue_right_source_x']!=b['dense_blue_right_source_x']]
print(json.dumps({'prepared_ROIs':50,'new_native_view_requests':len(manifest['new_view_requests']),'old_native_receipts_reused':len(old_refs),'new_scaled_contexts':1,'first_dense_blue_frame':positive[0]['frame'] if positive else None,'edge_changes':changes}))
