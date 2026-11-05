"""Prepare twelve unresolved candidate adjacency cases; extraction is not review."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import cv2

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D = R / 'native_cut_batch02_v1'
assert not D.exists()
source = Path('/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4')
source_hash = '030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66'
assert hashlib.sha256(source.read_bytes()).hexdigest() == source_hash
ids = ['EP0032', 'EP0046', 'EP0050', 'EP0054', 'EP0058', 'EP0059', 'EP0063', 'EP0069', 'EP0077', 'EP0082', 'EP0097', 'EP0101']
events = {r['event_id']: r for r in csv.DictReader((R / 'integrated_v4/visual_event_ledger_v10.csv').open())}
items = []
for event_id in ids:
    event = events[event_id]
    assert event['shot_boundary_claim'] == 'YES' and not event['visual_onset_verified_frame']
    n = int(event['source_start_frame'])
    items.append(dict(id=event_id, event=event, frames=[n-1, n]))
frames = {n for item in items for n in item['frames']}
D.mkdir()
cap = cv2.VideoCapture(str(source))
assert cap.isOpened()
requests = []
for n in range(max(frames)+1):
    ok, frame = cap.read()
    assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES)) == n+1
    if n in frames:
        assert frame.shape == (1080, 1920, 3)
        path = D / f'f{n:05d}_native.png'
        assert cv2.imwrite(str(path), frame)
        requests.append(dict(frame=n, source_pts_s=(n+1)/24, path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(), width=1920, height=1080, scale='NATIVE_FULLFRAME1920x1080'))
cap.release()
assert len(requests) == 24
out = dict(recorded_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(), source_path=str(source), source_sha256=source_hash,
           decode_method=f'Full nonseeking OpenCV0–{max(frames)}, source position checked; same existing declared BGR-to-PNG pipeline; no interpolation',
           baseline_event_ledger='integrated_v4/visual_event_ledger_v10.csv', items=items, new_view_requests=requests,
           status='PREPARED_NOT_VIEWED', actual_listening_seconds=0, CT_SCAN_COMPLETE=False)
(D / 'items.json').write_text(json.dumps(out, indent=2)+'\n')
(D / 'BRIEF.md').write_text('''Start only on explicit root dispatch after prior reviewer stops. Twelve unresolved candidate cut claims, twenty-four supplied native images. Review one complete adjacent pair then check fresh usage. Stop NEW reads at83% primary or near95% weekly; no paid/reset credits. Save incremental receipts and exact pending IDs/paths on stop.
Describe literal before/after and decide shot YES/NO/UNDETERMINED. Separate full scene replacement, graphics/character substitutions, scrolling and camera/subject movement. The supplied candidate is NOT a proven onset: compound windows EP0032/EP0046/EP0050/EP0054 may begin with motion rather than the later cut. If pair does not establish the cut, retain uncertainty and request the smallest exact additional frames; never assign a cut mechanically to candidate start. White background alone neither proves nor refutes a cut. Native adjacency confirms only this boundary, not entire compound event or shot duration.
Use only new_view_requests in items.json. No extra extraction, no old images, no new agents. Write OUT_native_cut_batch02_v1.json with source_sha256, status, items(id,shot_boundary,event_type,onset_frame_or_bracket,description,confidence,evidence_paths,limitations), new_evidence_reads(path,sha256,scale,successful,witness/tool-call), pending_new_image_paths,pending_case_ids,extra_exact_frames_needed,actual_listening_seconds0,CT_SCAN_COMPLETEfalse,usage_at_stop. No Git/locks/schedulers/source or prior-output writes. Stop after this bounded output.
''')
print('PREPARED_NOT_VIEWED', len(items), 'cases', len(requests), 'native frames')
