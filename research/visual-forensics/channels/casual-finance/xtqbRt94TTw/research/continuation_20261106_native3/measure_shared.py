from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];ranges=[(749,769,'bio'),(837,862,'quote'),(2183,2255,'scroll')];nums=[n for a,b,_ in ranges for n in range(a,b+1)];cmd=['ffmpeg','-v','error','-i',src,'-vf',"select='"+'+'.join(f'between(n,{a},{b})'for a,b,_ in ranges)+"'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'];p=subprocess.Popen(cmd,stdout=subprocess.PIPE);rows=[];prevs={}
regions={'bio':{'presenter':[0,200,800,1080],'card':[800,0,1920,1080]},'quote':{'text':[0,0,1920,480],'presenter':[900,480,1920,1080],'arrows':[250,480,750,1080]},'scroll':{'body':[380,180,1150,1010],'top':[340,60,1580,180],'presenter':[1300,450,1800,1080]}}
for a,b,name in ranges:
 D=P/(name+'_native');D.mkdir(exist_ok=True)
 oldname={'bio':'bio_749_766','quote':'quote_837_857','scroll':'scroll_2183_2218'}[name];old={r['frame']:r['decoded_RGB_sha256']for r in json.loads((P/oldname/'measurements.json').read_text())['rows']}
 for n in range(a,b+1):
  data=p.stdout.read(1920*1080*3);assert len(data)==1920*1080*3;x=np.frombuffer(data,np.uint8).reshape(1080,1920,3);h=hashlib.sha256(data).hexdigest();assert n not in old or h==old[n];im=Image.fromarray(x);im.save(D/f'f{n:05}.png');prev=prevs.get(name);row={'frame':n,'window':name,'pts_fraction':f'{n+1}/24','sha256_RGB24':h,'reused_hash_match':n in old,'regions':{}}
  for key,(l,t,r,bottom)in regions[name].items():
   reg=x[t:bottom,l:r];entry={}
   if prev is not None:
    d=np.abs(reg.astype(np.int16)-prev[t:bottom,l:r].astype(np.int16));entry={'changed_gt60':int((d.sum(2)>60).sum()),'max_channel':int(d.max())}
   row['regions'][key]=entry
  if name=='bio':
   mask=(x[60:470,:,0]<230)&(x[60:470,:,1]<230)&(x[60:470,:,2]<230);mask[:,:800]=False;yy,xx=np.where(mask);row['portrait_dark_bbox']=None if len(xx)==0 else [int(xx.min()),int(yy.min()+60),int(xx.max()),int(yy.max()+60)]
  if name=='quote':
   mask=(x[:,:,0]>130)&(x[:,:,1]<120)&(x[:,:,2]<120);yy,xx=np.where(mask);row['red_bbox']=None if len(xx)==0 else list(map(int,[xx.min(),yy.min(),xx.max(),yy.max()]));row['red_pixels']=len(xx)
  rows.append(row);prevs[name]=x.copy()
assert p.wait()==0
(P/'shared_measurements.json').write_text(json.dumps({'command':cmd,'definition':'Native full RGB SHA256; ROI sum abs RGB delta>60; max channel; bio dark bbox is support not semantic portrait-only mask; red R>130 G<120 B<120; numerical results do not establish semantic verification.','regions':regions,'rows':rows},indent=2)+'\n')
for name,ns in [('quote',list(range(837,863))),('scroll',list(range(2219,2256)))]:
 for k in range(0,len(ns),4):
  sel=ns[k:k+4];sheet=Image.new('RGB',(1280,768),'#ddd');dr=ImageDraw.Draw(sheet)
  for j,n in enumerate(sel):
   im=Image.open(P/(name+'_native')/f'f{n:05}.png');im.thumbnail((640,360));l=j%2*640;t=j//2*384;sheet.paste(im,(l,t+24));dr.text((l+5,t+5),str(n),fill='black')
  sheet.save(P/f'{name}_review_{k//4}.jpg',quality=96)
print('native region records',len(rows),'all75priorfullhashes matched')
