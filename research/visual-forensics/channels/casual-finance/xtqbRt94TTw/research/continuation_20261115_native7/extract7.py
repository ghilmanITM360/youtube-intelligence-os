from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((Path(__file__).parent.parent/'Casual-Finance-Video006-native3-20261106/SOURCE_VERIFICATION.json').read_text())['path']
def window(a,b,selected,name):
 D=P/name;D.mkdir(exist_ok=True);cmd=['ffmpeg','-v','error','-i',src,'-vf',f"select='between(n,{a},{b})'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];proc=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];prev=None;imgs={}
 for n in range(a,b+1):
  data=proc.stdout.read(1920*1080*3);assert len(data)==1920*1080*3
  x=np.frombuffer(data,np.uint8).reshape(1080,1920,3);d=None if prev is None else np.abs(x.astype(np.int16)-prev.astype(np.int16));mask=None if d is None else d.sum(2)>60
  yy,xx=([],[])if mask is None else np.where(mask)
  rows.append({'frame':n,'pts_fraction':f'{n+1}/24','decoded_RGB_sha256':hashlib.sha256(data).hexdigest(),'changed_gt60':None if mask is None else int(mask.sum()),'changed_bbox':None if not len(xx)else list(map(int,[xx.min(),yy.min(),xx.max(),yy.max()])),'maximum_channel_delta':None if d is None else int(d.max())})
  if n in selected:
   im=Image.fromarray(x);im.save(D/f'f{n:05}.jpg',quality=97);imgs[n]=im.copy()
  prev=x.copy()
 assert proc.wait()==0
 (D/'measurements.json').write_text(json.dumps({'decode_command':cmd,'method':'Full native decoded RGB24 SHA; adjacent pixel sum abs RGB difference >60, max channel delta. Measurements do not establish semantic or audio status.','rows':rows},indent=2)+'\n')
 w,h=640,360;sheet=Image.new('RGB',(w*2,((len(imgs)+1)//2)*(h+24)),'#ddd');dr=ImageDraw.Draw(sheet)
 for j,(n,im)in enumerate(imgs.items()):
  im.thumbnail((w,h));cx=j%2*w;cy=j//2*(h+24);sheet.paste(im,(cx,cy+24));dr.text((cx+8,cy+6),f'Native {n}, fullframe shown1/3',fill='black')
 sheet.save(P/(name+'_overview.jpg'),quality=95)
 print(name,[(r['frame'],r['changed_gt60'],r['changed_bbox'],r['maximum_channel_delta'])for r in rows]if b-a<10 else f'{len(rows)} native frames measured, {len(imgs)} displayed samples prepared')

window(2510,2545,{2510,2514,2515,2516,2518,2519,2520,2522,2525,2528,2530,2533,2534,2536,2540,2545},'ep0079_2510_2545')
