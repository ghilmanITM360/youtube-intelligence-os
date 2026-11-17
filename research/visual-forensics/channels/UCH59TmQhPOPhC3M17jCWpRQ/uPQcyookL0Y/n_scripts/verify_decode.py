import cv2,csv,json
from pathlib import Path
cv2.setNumThreads(1)
p=Path('.'); rows=list(csv.DictReader((p/'tables/k_rep_frames_batch04.csv').open())); lookup={int(r['frame']):r for r in rows}
cap=cv2.VideoCapture(json.loads((p/'source_manifest.json').read_text())['source_path']); mismatch=[]
for f in range(max(lookup)+1):
 ok,im=cap.read();assert ok
 if f in lookup:
  old=cv2.imread(lookup[f]['native_png']);
  if not (im==old).all():mismatch.append(f)
cap.release()
(p/'tables/n_batch04_decode_verification.json').write_text(json.dumps({'method':'OpenCV sequential decode from source frame 0 versus random-access extracted pixels; no new measurements or ASR','frames_checked':len(lookup),'mismatches':mismatch},indent=2)+'\n')
print('checked',len(lookup),'mismatches',mismatch)
