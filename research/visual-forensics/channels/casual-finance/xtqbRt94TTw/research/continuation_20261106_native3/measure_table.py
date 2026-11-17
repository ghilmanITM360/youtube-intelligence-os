from pathlib import Path
import json,subprocess,hashlib
from PIL import Image,ImageDraw
import numpy as np
P=Path(__file__).parent;old=json.loads((P/'table_2280_2365/measurements.json').read_text());src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];cmd=['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,2280,2365)'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];p=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];D=P/'table_native';D.mkdir(exist_ok=True);prev=None
for n in range(2280,2366):
 data=p.stdout.read(1920*1080*3);assert len(data)==1920*1080*3;h=hashlib.sha256(data).hexdigest();assert h==old['rows'][n-2280]['decoded_RGB_sha256'];x=np.frombuffer(data,np.uint8).reshape(1080,1920,3);im=Image.fromarray(x);im.save(D/f'f{n:05}.png');row={'frame':n,'RGB24sha256':h,'pts_fraction':f'{n+1}/24'}
 masks={'blue':(x[:,:,2]>150)&(x[:,:,0]<100)&(x[:,:,1]<100),'magenta':(x[:,:,0]>150)&(x[:,:,2]>150)&(x[:,:,1]<130),'coin':(x[:,:,0]>190)&(x[:,:,1]>80)&(x[:,:,1]<210)&(x[:,:,2]<100)}
 for key,m in masks.items():
  yy,xx=np.where(m);row[key]={'pixels':len(xx),'bbox':None if len(xx)==0 else list(map(int,[xx.min(),yy.min(),xx.max(),yy.max()]))}
 if prev is not None:
  row['roi_changes']={}
  for key,(l,t,r,b)in {'table':[0,0,1400,1080],'cursor_margin':[1650,400,1919,750],'coin_area':[1450,0,1920,550]}.items():
   delta=np.abs(x[t:b,l:r].astype(np.int16)-prev[t:b,l:r].astype(np.int16));row['roi_changes'][key]=int((delta.sum(2)>60).sum())
 rows.append(row);prev=x.copy()
assert p.wait()==0
(P/'table_region_measurements.json').write_text(json.dumps({'command':cmd,'method':'86native fullRGBhashes reverified; blue B>150 R<100 G<100; magenta R/B>150 G<130; warmcoin R>190 80<G<210 B<100 (may include presenter before exit); not semanticverification alone.','rows':rows},indent=2)+'\n')
print('86rawnative hashes matched')
