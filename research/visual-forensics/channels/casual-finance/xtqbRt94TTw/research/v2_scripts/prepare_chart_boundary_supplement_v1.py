"""Bounded exact-frame supplement; numerical masks are indexing, not visual rulings."""
from pathlib import Path
import datetime
import hashlib
import json

import cv2
import numpy as np

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D = R / 'chart_boundary_supplement_v1'
assert not D.exists()
D.mkdir()
source = Path('/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4')
source_hash = '030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'
assert hashlib.sha256(source.read_bytes()).hexdigest() == source_hash
frames = {17765, 17783, 17791, 17823, 17853, 17879, 17881, 17883, 17890}
cap = cv2.VideoCapture(str(source))
assert cap.isOpened()
requests, masks = [], []
for frame_index in range(max(frames) + 1):
    ok, frame = cap.read()
    assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES)) == frame_index + 1
    if frame_index >= 17765:
        band = frame[195:250, 190:1150]
        b, g, r = cv2.split(band)
        mask = (r > 180) & (g > 170) & (b < 160)
        cols = np.flatnonzero(mask.sum(axis=0) >= 10)
        masks.append(dict(frame=frame_index, pixels=int(mask.sum()),
                          left_x=int(cols[0] + 190) if len(cols) else None,
                          right_x=int(cols[-1] + 190) if len(cols) else None))
    if frame_index in frames:
        path = D / f'f{frame_index:05d}_native.png'
        assert cv2.imwrite(str(path), frame)
        requests.append(dict(frame=frame_index, source_pts_s=(frame_index + 1) / 24,
                             path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                             width=1920, height=1080, scale='NATIVE_FULLFRAME1920x1080'))
cap.release()
assert len(requests) == 9
out = dict(recorded_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           source_sha256=source_hash, source_path=str(source),
           decode_method='Full nonseeking OpenCV decode0–17890, positions checked; same declared RGB conversion pipeline; no interpolation',
           base_review='chart_macro_review_v1/OUT_chart_macro_review_v1.json',
           base_review_sha256='080fe01a3442213fb1a03b7753f0ebcbc1adb273272f8b31c779f3f7b3e4f3f4',
           new_view_requests=requests, yellow_title_mask_measurements=masks,
           mask_method='Source-frame band x190:1150/y195:250, BGR R>180/G>170/B<160; columns with >=10pixels. Indexing only, not semantic certification or true color.',
           prior_native_frames_to_reuse_without_redisplay=[17766, 17784, 17790, 17792, 17822, 17824, 17852, 17854, 17878, 17880, 17882],
           prior_exact_red_annotation_onset=17875,
           actual_listening_seconds=0, CT_SCAN_COMPLETE=False, status='PREPARED_NOT_VIEWED')
(D / 'items.json').write_text(json.dumps(out, indent=2) + '\n')
print('Prepared9newnativefullframes;126numericmaskpoints;prior64imageviewsnotrepeated')
