from pathlib import Path
import cv2,csv,json,hashlib
cv2.setNumThreads(1)
p=Path('.')
src=json.loads((p/'source_manifest.json').read_text())['source_path']
S={r['state_v4']:r for r in csv.DictReader((p/'tables/states_v5_draft.csv').open())}
pts={int(r['frame']):r['pts_time'] for r in csv.DictReader((p/'FULL_FRAME_MEASUREMENTS.csv').open())}
groups={'W001_label_panel':list(range(698,728)), 'W010_interval':list(range(1531,2072,30))+[2071]}
for key in ['W002','W004','W009','W041','W045','W058','W059','W063']:
 a=int(S[key]['start']); groups[key+'_boundary']=list(range(a-16,a+13))
cap=cv2.VideoCapture(src); rows=[]
for group,fs in groups.items():
 d=p/'frames/checkpoint_M'/group; d.mkdir(parents=True,exist_ok=True)
 thumbs=[]
 for f in fs:
  path=d/f'f{f}.png'
  if not path.exists():
   cap.set(cv2.CAP_PROP_POS_FRAMES,f);ok,im=cap.read();assert ok
   assert im.shape[:2]==(1080,1920)
   assert cv2.imwrite(str(path),im)
  else: im=cv2.imread(str(path))
  rows.append({'group':group,'frame':f,'pts_s':pts[f],'native_png':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
  tile=cv2.resize(im,(640,360));cv2.putText(tile,f'f{f} | {pts[f]} s',(8,22),cv2.FONT_HERSHEY_SIMPLEX,.6,(0,0,255),2);thumbs.append(tile)
 for j in range(0,len(thumbs),6):
  t=thumbs[j:j+6]
  import numpy as np
  while len(t)<6:t.append(np.full_like(t[0],255))
  sheet=np.vstack([np.hstack(t[k:k+2]) for k in range(0,6,2)])
  cv2.imwrite(str(d/f'sheet_{j//6+1:02}.jpg'),sheet)
cap.release()
with (p/'tables/m_supplement_frames.csv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('native frames',len(rows),'groups',list(groups))
