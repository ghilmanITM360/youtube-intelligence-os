"""Only three frames explicitly requested by the completed native pair review."""
from pathlib import Path
import hashlib
import json
import datetime
import cv2

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'compound_cut_followup_v1';assert not D.exists()
base=R/'native_cut_batch02_v1/OUT_native_cut_batch02_v1.json';o=json.loads(base.read_text())
source=Path('/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4')
h='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66';assert hashlib.sha256(source.read_bytes()).hexdigest()==h
frames={n for x in o['extra_exact_frames_needed'] for n in x['frames']};assert frames=={1641,1642,2770}
D.mkdir();cap=cv2.VideoCapture(str(source));assert cap.isOpened();requests=[]
for n in range(max(frames)+1):
    ok,f=cap.read();assert ok and round(cap.get(cv2.CAP_PROP_POS_FRAMES))==n+1
    if n in frames:
        p=D/f'f{n:05d}_native.png';assert cv2.imwrite(str(p),f)
        requests.append(dict(frame=n,source_pts_s=(n+1)/24,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),width=1920,height=1080,scale='NATIVE_FULLFRAME1920x1080'))
cap.release()
(D/'items.json').write_text(json.dumps(dict(source_sha256=h,source_path=str(source),recorded_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),decode_method='Full nonseeking OpenCV0–2770 positions checked; same existing source-to-PNG pipeline',base_review=str(base.relative_to(R)),base_review_sha256=hashlib.sha256(base.read_bytes()).hexdigest(),cases=o['extra_exact_frames_needed'],new_view_requests=requests,status='PREPARED_NOT_VIEWED',actual_listening_seconds=0,CT_SCAN_COMPLETE=False),indent=2)+'\n')
(D/'BRIEF.md').write_text('''Start only on root dispatch after batch02 reviewer stops. Exactly3requested new native fullframes1641/1642/2770. EP0054 supplied1596/1597 already reviewed as same-viewer scroll; read1641/1642 to test endpoint. If same later table/presenter state, do NOT guess earliercut; request smallest adaptive exactframes/bisection within1598–1641 or retain uncertainty. EP0082 reuse your already-reviewed2769 observation without redisplay and compare new2770. Distinguish PDF foreground overlay, retained article backdrop, white margins/presenter removal; white-alone is not cut evidence. Correct old claim only as supported. One case then freshusage; stop83primary/near95weekly. No priorimage redisplay/extraction/newagents/Git/locks/schedulers/source/oldoutput edits.
Write OUT_compound_cut_followup_v1.json with source_sha256,status,items(id,boundary_verdict,observed_frames,description,exact_onset_or_unknown,event_taxonomy,confidence,limitations),new_evidence_reads(path,sha256,scale,successful,witness),reused_prior_receipts,pending_paths,extra_exact_frames_needed,actual_listening_seconds0,CT_SCAN_COMPLETEfalse,usage_at_stop. Stop after3newreads.
''')
print('PREPARED_NOT_VIEWED3native endpoint tests; no onset assumed')
