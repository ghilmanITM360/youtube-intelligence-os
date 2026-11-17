from pathlib import Path
import subprocess,json,hashlib
import numpy as np
P=Path(__file__).parent;s=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];cmd=['ffmpeg','-v','error','-i',s,'-vf',"select='between(n,1115,1144)',crop=640:850:0:200",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];pr=subprocess.Popen(cmd,stdout=subprocess.PIPE);r=[]
for n in range(1115,1145):
 d=pr.stdout.read(640*850*3);x=np.frombuffer(d,np.uint8).reshape(850,640,3);m=(x[:,:,0]>180)&(x[:,:,1]>80)&(x[:,:,1]<180)&(x[:,:,2]<100);yy,xx=np.where(m);r.append({'frame':n,'RGB_roi_sha256':hashlib.sha256(d).hexdigest(),'orange_pixels':int(m.sum()),'bbox':None if not len(xx)else[int(xx.min()),int(yy.min()+200),int(xx.max()),int(yy.max()+200)]})
assert pr.wait()==0;(P/'coin_measurements.json').write_text(json.dumps({'method':'crop640:850:0:200 BEFORE RGB24; orange R>180,80<G<180,B<100; bbox does not itself identify expression/semantic event','rows':r},indent=2)+'\n');print([(x['frame'],x['bbox'])for x in r])
