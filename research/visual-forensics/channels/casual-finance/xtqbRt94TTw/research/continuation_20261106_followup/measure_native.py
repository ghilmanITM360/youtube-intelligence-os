from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent
source=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path']
cmd=['ffmpeg','-v','error','-i',source,'-vf',"select='between(n,445,550)',crop=1640:510:100:550",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1']
proc=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];prev=None
for f in range(445,551):
 data=proc.stdout.read(1640*510*3);assert len(data)==1640*510*3
 x=np.frombuffer(data,dtype=np.uint8).reshape(510,1640,3);yellow=(x[:,:,0]>200)&(x[:,:,1]>180)&(x[:,:,2]<120)
 def box(mask):
  yy,xx=np.where(mask);return [int(xx.min()+100),int(yy.min()+550),int(xx.max()+100),int(yy.max()+550)]if len(xx)else None
 d=None if prev is None else np.abs(x.astype(int)-prev.astype(int)).sum(2)>60
 rows.append({'frame':f,'pts_fraction':str((f+1))+'/24','decoded_RGB_roi_sha256':hashlib.sha256(data).hexdigest(),'yellow_lower_880_920_pixels':int(yellow[330:371].sum()),'yellow_lower_880_920_bbox':box(yellow & (np.arange(510)[:,None]>=330)&(np.arange(510)[:,None]<371)),'changed_pixels':None if d is None else int(d.sum()),'changed_bbox':None if d is None else box(d),'pointer_face_changed':None if d is None else int(d[:,1000:].sum())})
 prev=x.copy()
assert proc.wait()==0
(P/'native_measurements.json').write_text(json.dumps({'method':'Decoded source RGB native ROI x100 y550 w1640 h510; previous-frame sum absolute RGB >60; yellow r>200 g>180 b<120. Measurements alone do not establish semantic status. PTS (n+1)/24 from source starts1/24. JPEG crops are viewing receipts; measurements use decoded RGB, not JPEG.','rows':rows},indent=2)+'\n')
for subset,name in [(list(range(448,464)),'onset_448_463'),(list(range(462,551,4))+[549,550],'sweep_462_550')]:
 thumbw,thumbh=820,255;sheet=Image.new('RGB',(1640,((len(subset)+1)//2)*280),'#dddddd');dr=ImageDraw.Draw(sheet)
 for j,f in enumerate(subset):
  im=Image.open(P/f'native_445_550/f{f:05d}.jpg');im.thumbnail((thumbw,thumbh));cx=(j%2)*820;cy=(j//2)*280;sheet.paste(im,(cx,cy+22));dr.text((cx+5,cy+4),f'Native {f}, ROI x100 y550, shown half-scale',fill='black')
 sheet.save(P/(name+'.jpg'),quality=95)
print([(r['frame'],r['changed_pixels'],r['changed_bbox'],r['yellow_lower_880_920_pixels'],r['yellow_lower_880_920_bbox'])for r in rows if r['frame']in list(range(448,464))+list(range(480,551,5))])
