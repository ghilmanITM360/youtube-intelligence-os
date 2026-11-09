"""Index the still-open blue-selection/focus transition without claiming views."""
from pathlib import Path
import datetime
import hashlib
import json
import cv2
import numpy as np

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'selection_focus_boundary_v1'
assert not D.exists()
source=Path('/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4')
h='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'
assert hashlib.sha256(source.read_bytes()).hexdigest()==h
frames={8057,8084,8085,8086}
D.mkdir()
cap=cv2.VideoCapture(str(source));assert cap.isOpened()
measurements=[];requests=[]
for n in range(8133):
    ok,frame=cap.read();assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES))==n+1
    if n>=8046:
        band=frame[604:628,171:1596].astype(np.int16)
        mask=(band[:,:,0]>120)&(band[:,:,0]-band[:,:,2]>40)&(band[:,:,0]-band[:,:,1]>20)
        dense=np.flatnonzero(mask.sum(axis=0)>=12)
        measurements.append(dict(frame=n,source_pts_s=(n+1)/24,dense_blue_pixels=int(mask.sum()),
                                 dense_blue_left_source_x=int(dense[0]+171) if len(dense) else None,
                                 dense_blue_right_source_x=int(dense[-1]+171) if len(dense) else None))
    if n in frames:
        path=D/f'f{n:05d}_native.png';assert cv2.imwrite(str(path),frame)
        requests.append(dict(frame=n,source_pts_s=(n+1)/24,path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                             width=1920,height=1080,scale='NATIVE_FULLFRAME1920x1080'))
cap.release()
out=dict(recorded_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_path=str(source),source_sha256=h,
         decode_method='Full nonseeking OpenCV0–8132, positions checked; existing same-pipeline BGR-to-PNG; no interpolation',
         status='PREPARED_NOT_VIEWED',new_view_requests=requests,measurements=measurements,
         measurement_rule='Fixed source first-line band y604:627,x171:1595; B>120,B-R>40,B-G>20, columns>=12pixels. Heuristic indexing only; band loses correspondence if page scales/translates. Neither absence nor presence alone establishes deselection, focus or meaning.',
         prior_evidence_to_reuse_without_redisplay=['selection_macro_review_v1/OUT_selection_macro_review_v1.json','motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json'],
         actual_listening_seconds=0,CT_SCAN_COMPLETE=False)
(D/'items.json').write_text(json.dumps(out,indent=2)+'\n')
(D/'BRIEF.md').write_text('''Start only on root dispatch after previous reviewer stops. This is the unresolved selection-removal/focus boundary beyond8045, not a repeat of initial range wrap/cursor reviews. Four new fullframes8057/8084/8085/8086; prior source8057 was viewed only as a small cursor ROI, so distinguish new full context from repeat area. Read supplied native frames in two2-image batches, fresh usage each; stop83primary/near95weekly, save partial receipts. Before/after8084/8085 adjacency may distinguish selection color/focus state versus whole selected range disappearance and host/desk removal. Fixed-band numeric mask is an index; page movement can move content outside the band. Do not infer physical mouse clicks, application focus, continuous absence or exact easing from a color change alone. Literal OBSERVED colors/selected text retained or gone plus native boundary; implementation inferred/unknown. Reuse old initial-selection observations without redisplay.
Write OUT_selection_focus_boundary_v1.json: source_sha256,status,per_frame_observations,selection_visible_lifecycle,host_desk_transition,static_anchors,known_vs_unknown,confidence,limitations,new_evidence_reads(path,sha256,scale,successful,witness),pending_paths,extra_exact_frames_needed,actual_listening_seconds0,CT_SCAN_COMPLETEfalse,usage_at_stop. No extra extraction/newagents/Git/locks/schedulers/source/prioroutputs. Stop after this bounded4image task.
''')
changes=[(a['frame'],b['frame'],a['dense_blue_pixels'],b['dense_blue_pixels']) for a,b in zip(measurements,measurements[1:]) if (a['dense_blue_right_source_x'] is None)!=(b['dense_blue_right_source_x'] is None)]
print('PREPARED_NOT_VIEWED4native,87numericpoints;dense-band-positive/negative changes',changes)
