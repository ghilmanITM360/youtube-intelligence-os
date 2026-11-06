from pathlib import Path
import subprocess,json
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).parent;s=json.loads((P/'SOURCE_VERIFICATION.json').read_text())['path'];pr=subprocess.Popen(['ffmpeg','-v','error','-i',s,'-vf',"select='between(n,1485,1595)',crop=52:888:1438:124",'-fps_mode','passthrough','-pix_fmt','rgb24','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE);rows=[];pics={}
for n in range(1485,1596):
 d=pr.stdout.read(52*888*3);a=np.frombuffer(d,np.uint8).reshape(888,52,3);m=a.min(2)>180;yy,xx=np.where(m);rows.append({'frame':n,'white_pixels_in_dark_margin':int(m.sum()),'bbox':None if not len(xx)else[int(xx.min()+1438),int(yy.min()+124),int(xx.max()+1438),int(yy.max()+124)]})
 if n in [1488,1489,1510,1511,1515,1516,1517,1520,1557,1583,1588,1589,1590,1591,1592]:pics[n]=Image.fromarray(a)
assert pr.wait()==0;(P/'pdf_pointer_margin_measurements.json').write_text(json.dumps({'method':'crop52:888:1438:124 beforeRGB24; white minRGB>180 in dark page-right margin. Pointer semantics via native crop, textI-beam not measured by this ROI.','rows':rows},indent=2)+'\n');o=Image.new('RGB',(len(pics)*90,914),'#ddd');dr=ImageDraw.Draw(o)
for j,(n,im)in enumerate(pics.items()):o.paste(im,(j*90,26));dr.text((j*90,5),str(n),fill='black')
o.save(P/'pdf_margin_native_pointers.jpg',quality=98);print([(r['frame'],r['bbox'])for r in rows if r['frame']in list(range(1488,1492))+list(range(1509,1531))+list(range(1582,1596))])
