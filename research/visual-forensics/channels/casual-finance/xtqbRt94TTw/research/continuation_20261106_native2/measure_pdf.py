from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];cmd=['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,1485,1595)'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];pr=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];prev=None;imgs={};metrics=json.loads((P/'pdf_1485_1595/measurements.json').read_text())['rows']
def bbox(m,x0,y0):
 yy,xx=np.where(m);return None if not len(xx)else list(map(int,[xx.min()+x0,yy.min()+y0,xx.max()+x0,yy.max()+y0]))
for j,n in enumerate(range(1485,1596)):
 data=pr.stdout.read(1920*1080*3);assert len(data)==1920*1080*3;assert hashlib.sha256(data).hexdigest()==metrics[j]['decoded_RGB_sha256'];x=np.frombuffer(data,np.uint8).reshape(1080,1920,3);diff=None if prev is None else np.abs(x.astype(np.int16)-prev.astype(np.int16)).sum(2)>60
 blue=x[620:690,845:1350];mask=(blue[:,:,2]>blue[:,:,0].astype(int)+15)&(blue[:,:,1]>blue[:,:,0].astype(int)+10)&(blue[:,:,0]<225)&(blue[:,:,1]>120)
 row={'frame':n,'source_full_RGB_sha256':hashlib.sha256(data).hexdigest(),'blue_text_pixels':int(mask.sum()),'blue_text_bbox':bbox(mask,845,620),'page_body_changed':None if diff is None else int(diff[124:1012,764:1436].sum()),'chrome_changed':None if diff is None else int(diff[69:124,413:1507].sum()),'all_changed':None if diff is None else int(diff.sum()),'all_change_bbox':None if diff is None else bbox(diff,0,0)}
 # pagegap at fixed x800: white page givesR>230; dark separator R<80, source-native everyframe
 column=x[124:1012,800];dark=(column.max(1)<80);segs=[];start=None
 for k,b in enumerate(dark):
  if b and start is None:start=k
  if start is not None and(not b or k==len(dark)-1):
   end=k if b else k-1
   if end-start>=5:segs.append([start+124,end+124])
   start=None
 row['page_gap_y_at_x800']=segs;rows.append(row)
 if 1532<=n<=1549:imgs[n]=Image.fromarray(x[615:700,840:1360]).copy()
 prev=x.copy()
assert pr.wait()==0
(P/'pdf_region_measurements.json').write_text(json.dumps({'method':'Full1920x1080RGB24 samepipeline as first extraction;111 rawhashes matched. Blue mask620:690y845:1350x B>R+15,G>R+10,R<225,G>120; pagebody/chrome difference sumabsRGB>60; pagegap fixedx800darkspan>=6. Numeric evidence not semantics.','rows':rows},indent=2)+'\n')
out=Image.new('RGB',(1040,9*110),'#ddd');d=ImageDraw.Draw(out)
for i,(n,im)in enumerate(imgs.items()):
 x=i%2*520;y=i//2*110;out.paste(im,(x,y+25));d.text((x+4,y+5),f'Native{n} textROI1:1',fill='black')
out.save(P/'pdf_selection_1532_1549.jpg',quality=98)
print([(r['frame'],r['all_changed'],r['page_gap_y_at_x800'],r['blue_text_pixels'],r['blue_text_bbox'])for r in rows])
