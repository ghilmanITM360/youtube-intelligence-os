from pathlib import Path
import json,subprocess,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];out={}
for a,b,folder in [(1884,1922,'zigzag_1884_1922'),(1983,2087,'profile_1983_2087')]:
 refs={r['frame']:r['decoded_RGB_sha256'] for r in json.loads((P/folder/'measurements.json').read_text())['rows']};proc=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf',f"select='between(n,{a},{b})'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE);rows=[];prev=None
 for n in range(a,b+1):
  raw=proc.stdout.read(1920*1080*3);assert hashlib.sha256(raw).hexdigest()==refs[n];x=np.frombuffer(raw,np.uint8).reshape(1080,1920,3);r={'frame':n,'full_RGB_hash_reverified':True}
  if a==1884:
   z=x[100:700,900:1640].astype('int16');mask=(z[:,:,1]>100)&(z[:,:,1]>z[:,:,0]*1.4)&(z[:,:,1]>z[:,:,2]*1.2);yy,xx=np.where(mask);r.update({'green_pixels':int(mask.sum()),'green_bbox':None if not len(xx)else list(map(int,[xx.min()+900,yy.min()+100,xx.max()+900,yy.max()+100]))})
  else:
   for name,box in [('page',[110,150,870,1000]),('profile',[900,290,1920,930])]:
    xx1,yy1,xx2,yy2=box;z=x[yy1:yy2,xx1:xx2].astype('int16');v=None if prev is None else np.abs(z-prev[yy1:yy2,xx1:xx2].astype('int16')).sum(2)>60;r[name+'_changed_gt60']=None if v is None else int(v.sum())
   col=x[150:1000,800].astype('int16');m=(col[:,2]>col[:,0]+8)&(col[:,2]<190)&(col[:,0]<100);r['x800_darkblue_y']=(np.where(m)[0]+150).tolist()
   # Portrait warm-toned mask, only a reproducible detector; no semantic identity inference.
   z=x[290:930,900:1920].astype('int16');m=(z[:,:,0]>z[:,:,1]*1.12)&(z[:,:,0]>z[:,:,2]*1.2)&(z[:,:,1]>35)&(z[:,:,0]>65);yy,xx=np.where(m);r['warm_profile_bbox']=None if not len(xx)else list(map(int,[xx.min()+900,yy.min()+290,xx.max()+900,yy.max()+290]))
   if n in {1993,1994,1996,2000,2008,2012,2014,2016,2022,2024,2026,2027,2057,2058,2060,2066,2067,2070,2071,2072,2083}and not(P/folder/f'f{n:05}.jpg').exists():Image.fromarray(x).save(P/folder/f'f{n:05}.jpg',quality=97)
  rows.append(r);prev=x.copy()
 assert proc.wait()==0;out[folder]=rows
(P/'batch5_region_measurements.json').write_text(json.dumps({'method':'Re-decode shared windows once for region measurements and sparse extra boundary samples; all144 fullRGB hashes match original shared-window receipts. Green and warm-color masks are numerical detectors, not semantic proof. Page/profile diff sumabsRGB>60. Native source ROI viewed separately.','rows':out},indent=2)+'\n')
sets=[([1987,1988,1993,1994,1999,2007,2015,2016,2023,2026,2027],(0,0,1920,1080),'profile_phase1.jpg',.5),([2042,2043,2048,2049,2051,2052,2053,2054,2055,2063,2071,2082,2083],(70,140,900,1000),'profile_phase2_native.jpg',1)]
for ns,box,name,scale in sets:
 cw=int((box[2]-box[0])*scale);ch=int((box[3]-box[1])*scale);s=Image.new('RGB',(cw*2,((len(ns)+1)//2)*(ch+24)),'#ddd');d=ImageDraw.Draw(s)
 for i,n in enumerate(ns):
  im=Image.open(P/'profile_1983_2087'/f'f{n:05}.jpg').crop(box)
  if scale!=1:im=im.resize((cw,ch))
  px=i%2*cw;py=i//2*(ch+24);s.paste(im,(px,py+24));d.text((px+5,py+5),f'frame{n}; crop{box}; scale{scale}',fill='black')
 s.save(P/name,quality=98)
print('144 full-native hashes reverified; shared regional measurements and views ready')
