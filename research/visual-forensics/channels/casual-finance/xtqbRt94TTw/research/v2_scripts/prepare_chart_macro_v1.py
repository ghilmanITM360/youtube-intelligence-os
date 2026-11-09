"""Native chart-tooltip samples <=100ms apart within a bounded interaction window."""
from pathlib import Path
import cv2
import numpy as np
import json
import hashlib
import datetime

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'chart_macro_review_v1';assert not D.exists();D.mkdir()
source='/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4'
prior=json.loads((R/'motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json').read_text())
old=next(x for x in prior['items'] if x['id']=='SUB151');receipts={x['path']:x for x in prior['evidence_reads']}
reuses=[receipts[x] for x in old['evidence_paths'] if receipts[x]['scale'].startswith('NATIVE')];assert len(reuses)==5
fullframes={17766}|set(range(17784,17883,2));requests=[];measurements=[];last=None
cap=cv2.VideoCapture(source);assert cap.isOpened()
for n in range(17883):
    ok,frame=cap.read();assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES))==n+1
    if n<17765:continue
    if last is not None:
        delta=np.abs(frame.astype(np.int16)-last.astype(np.int16));mask=np.any(delta>35,axis=2).astype(np.uint8)
        number,labels,stats,centroids=cv2.connectedComponentsWithStats(mask,8)
        comps=[{'xywh':[int(t) for t in stats[k,:4]],'area':int(stats[k,4])} for k in range(1,number) if stats[k,4]>=5]
        measurements.append({'frame':n,'source_pts_s':(n+1)/24,'changed_pixels_maxchannel_gt35':int(mask.sum()),'components_area_ge5':comps})
    last=frame.copy()
    if 17766<=n<=17778:
        crop=frame[757:861,138:313];path=D/f'f{n:05d}_cursor_nativeROI.png';assert cv2.imwrite(str(path),crop)
        requests.append({'frame':n,'source_pts_s':(n+1)/24,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                         'width':175,'height':104,'scale':'NATIVE_1to1_ROI_NOT_FULLFRAME','purpose':'Pre-SUB151 cursor presence/context at and after chart entry; compare to prior17779–17783nativeROI observations'})
    if n in fullframes:
        path=D/f'f{n:05d}_native.png';assert cv2.imwrite(str(path),frame)
        requests.append({'frame':n,'source_pts_s':(n+1)/24,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                         'width':1920,'height':1080,'scale':'NATIVE_FULLFRAME1920x1080','purpose':'Chart entry context' if n==17766 else 'Hover tooltip/title/annotation sample; adjacent requested fullframes2frames/83.333ms apart'})
cap.release()
manifest={'recorded_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':'030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66',
          'decode_method':'Full non-seeking OpenCV source decode0–17882, checked positions; declared same conversion pipeline; no interpolation/seek',
          'new_view_requests':requests,'reused_prior_native_ROI_receipts':reuses,'prior_review':'motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json#SUB151',
          'other_prior_boundary_to_reuse':'G116 prior gap review: red up57% first17875,17874absent; do not redo merely to establish that onset',
          'measurements':measurements,'measurement_limit':'maxchannel>35/connected-area>=5 are indexing heuristics, not semantic event labels or source curves; numerical RGB restricted to this pipeline',
          'temporal_scope':'17784–17882 fullframe samples every2originalframes=83.333ms, within this bounded4.125s interaction only; not global100ms coverage or exact timing of every tooltip',
          'actual_listening_seconds':0,'status':'PREPARED_NOT_VIEWED'}
(D/'items.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'new_nativefullframe_requests':len(fullframes),'new_nativeROI_requests':13,'prior_nativeROI_receipts_reused':5,'sequential_decode_frames':17883,'diffmeasurement_rows':len(measurements)}))
