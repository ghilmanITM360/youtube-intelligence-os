from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path']
# Dedicated full-width native text ROI before RGB conversion, fixed pipeline.
cmd=['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,925,1060)',crop=1920:250:0:170",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];proc=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];imgs={};prev=None
for f in range(925,1061):
 data=proc.stdout.read(1920*250*3);assert len(data)==1920*250*3;x=np.frombuffer(data,np.uint8).reshape(250,1920,3);yellow=(x[:,:,0]>200)&(x[:,:,1]>180)&(x[:,:,2]<180)&(x[:,:,0].astype(int)-x[:,:,2].astype(int)>40);yy,xx=np.where(yellow);bins=[]
 for y0,y1 in [(200,240),(270,315),(340,380)]:
  m=yellow[y0-170:y1-170];ys,xs=np.where(m);bins.append({'y_range':[y0,y1-1],'pixels':int(m.sum()),'bbox':None if not len(xs)else list(map(int,[xs.min(),ys.min()+y0,xs.max(),ys.max()+y0]))})
 rows.append({'frame':f,'decoded_text_RGB_sha256':hashlib.sha256(data).hexdigest(),'yellow_total':int(yellow.sum()),'yellow_bbox':None if not len(xx)else list(map(int,[xx.min(),yy.min()+170,xx.max(),yy.max()+170])),'bands':bins})
 if f in list(range(927,934))+list(range(974,984))+list(range(1047,1057)):imgs[f]=Image.fromarray(x)
assert proc.wait()==0
(P/'quote_line_measurements.json').write_text(json.dumps({'method':'select925..1060,crop1920:250:0:170 BEFORE RGB24; yellow R>200,G>180,B<180,R-B>40. First perceptible anti-aliased pixel may precede hard yellow threshold. Numerical evidence qualified by native visual witnesses.','rows':rows},indent=2)+'\n')
for name,fs in [('native_onset_927_933',range(927,934)),('native_wrap_974_983',range(974,984)),('native_finish_1047_1056',range(1047,1057))]:
 out=Image.new('RGB',(960,len(fs)*150),'#ddd');dr=ImageDraw.Draw(out)
 for i,f in enumerate(fs):
  im=imgs[f].copy();im.thumbnail((960,125));out.paste(im,(0,i*150+25));dr.text((5,i*150+5),f'Native{f} fullwidth textROI halfscale',fill='black')
 out.save(P/(name+'.jpg'),quality=98)
print([(r['frame'],r['yellow_total'],r['yellow_bbox'])for r in rows if r['frame']<934 or 974<=r['frame']<984 or 1047<=r['frame']])
