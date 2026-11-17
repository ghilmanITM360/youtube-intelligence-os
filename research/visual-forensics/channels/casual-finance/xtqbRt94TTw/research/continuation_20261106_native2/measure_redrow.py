from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];refs={r['frame']:r['decoded_RGB_sha256']for r in json.loads((P/'redrow_2118_2157/measurements.json').read_text())['rows']};proc=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,2118,2157)'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE);rows=[];imgs={};prev=None;base=None
for n in range(2118,2158):
 raw=proc.stdout.read(1920*1080*3);assert hashlib.sha256(raw).hexdigest()==refs[n];x=np.frombuffer(raw,np.uint8).reshape(1080,1920,3);z=x[335:375,370:1510].astype('int16');m=(z[:,:,0]>180)&(z[:,:,0]-z[:,:,1]>20)&(z[:,:,1]-z[:,:,2]>10);yy,xx=np.where(m);r={'frame':n,'red_mask_pixels':int(m.sum()),'red_bbox':None if not len(xx)else list(map(int,[xx.min()+370,yy.min()+335,xx.max()+370,yy.max()+335]))}
 if n==2151:base=x.copy()
 if n>=2151:r['RGB_equals_2151']=bool(np.array_equal(x,base));r['max_channel_delta_from_2151']=int(np.abs(x.astype('int16')-base.astype('int16')).max())
 if n in {2121,2122,2123,2132,2133,2134,2151,2152,2153,2154}:imgs[n]=Image.fromarray(x).crop((370,335,1510,375))
 rows.append(r);prev=x.copy()
assert proc.wait()==0
s=Image.new('RGB',(1140,len(imgs)*64),'#ddd');d=ImageDraw.Draw(s)
for i,(n,im)in enumerate(imgs.items()):d.text((3,i*64+4),str(n),fill='black');s.paste(im,(0,i*64+24))
s.save(P/'redrow_native_boundaries.png');(P/'redrow_region_measurements.json').write_text(json.dumps({'method':'FullRGB SHA matched40sharedframes; red mask R>180,R-G>20,G-B>10, nativeROI370:1510,335:375. Firstvisible may precede high-saturation mask. 2151fullRGB exactcomparison retained. No semantic/audio inference from detector.','rows':rows},indent=2)+'\n');print('40hashes match; native boundaries ready')
