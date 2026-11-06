from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];cmd=['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,1405,1478)',crop=1500:170:170:180",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];pr=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];images={}
for n in range(1405,1479):
 d=pr.stdout.read(1500*170*3);x=np.frombuffer(d,np.uint8).reshape(170,1500,3);m=(x[:,:,0]>150)&(x[:,:,1]>150)&(x[:,:,2]<100);yy,xx=np.where(m);rows.append({'frame':n,'RGB_roi_sha256':hashlib.sha256(d).hexdigest(),'yellow_text_pixels':int(m.sum()),'bbox':None if not len(xx)else list(map(int,[xx.min()+170,yy.min()+180,xx.max()+170,yy.max()+180]))})
 if n in list(range(1405,1416))+[1420,1434,1437,1442,1450,1455,1460,1465,1470,1475,1478]:images[n]=Image.fromarray(x)
assert pr.wait()==0;(P/'headline_measurements.json').write_text(json.dumps({'method':'Native crop1500:170:170:180 beforeRGB24;maskR/G>150B<100. Selected native views verify highlight semantics; no audio inference.','rows':rows},indent=2)+'\n')
for name,ss in [('headline_onset',list(images)[:11]),('headline_sweep',list(images)[11:])]:
 out=Image.new('RGB',(1500,len(ss)*195),'#ddd');dr=ImageDraw.Draw(out)
 for i,n in enumerate(ss):out.paste(images[n],(0,i*195+25));dr.text((6,i*195+6),f'Native{n} ROI1:1',fill='black')
 out.save(P/(name+'.jpg'),quality=97)
print([(r['frame'],r['yellow_text_pixels'],r['bbox'])for r in rows])
