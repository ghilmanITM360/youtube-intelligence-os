from pathlib import Path
import json,subprocess,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;src=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];refs={r['frame']:r['decoded_RGB_sha256']for r in json.loads((P/'profile_1983_2087/measurements.json').read_text())['rows']};proc=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf',"select='between(n,1983,2087)'",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE);rows=[];crops={}
for n in range(1983,2088):
 raw=proc.stdout.read(1920*1080*3);assert hashlib.sha256(raw).hexdigest()==refs[n];x=np.frombuffer(raw,np.uint8).reshape(1080,1920,3);z=x.astype('int16');m=(z[:,:,0]>180)&(z[:,:,1]>100)&(z[:,:,1]<220)&(z[:,:,2]<140)&(z[:,:,0]-z[:,:,2]>70);yy,xx=np.where(m);rows.append({'frame':n,'amber_mask_pixels':int(m.sum()),'amber_bbox':None if not len(xx)else list(map(int,[xx.min(),yy.min(),xx.max(),yy.max()]))})
 if n in {1993,1994,1995}:crops[n]=Image.fromarray(x).crop((1820,290,1920,650))
 if n in {2070,2071,2072,2081,2082,2083}:crops[n]=Image.fromarray(x).crop((360,625,1510,670))
assert proc.wait()==0
for ns,name in [([1993,1994,1995],'profile_firstvisible_native.png'),([2070,2071,2072,2081,2082,2083],'parallel_amber_native.png')]:
 ims=[crops[n]for n in ns];w=max(im.width for im in ims);h=sum(im.height+24 for im in ims);s=Image.new('RGB',(w,h),'#ddd');d=ImageDraw.Draw(s);y=0
 for n,im in zip(ns,ims):d.text((3,y+4),str(n),fill='black');s.paste(im,(0,y+24));y+=im.height+24
 s.save(P/name)
(P/'profile_boundary_supplement.json').write_text(json.dumps({'source_hashes_match_all105':True,'method':'Whole-native RGB amber detector R>180 100<G<220 B<140 R-B>70; includes portrait before exit, so cannot equal highlight count until card gone. Lossless native1:1 crops resolve edge-onset and highlight endpoints.','rows':rows},indent=2)+'\n')
print('105 hashes match; lossless boundary crops ready')
