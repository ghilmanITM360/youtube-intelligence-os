"""Original G004 system. Reads only specification and system font; no source/media assets."""
from pathlib import Path
import json,sys,hashlib
from PIL import Image,ImageDraw,ImageFont
S=json.loads(Path(sys.argv[1]).read_text());O=Path(sys.argv[2]);O.mkdir(exist_ok=False);C=S['palette'];T=S['original_system'];W,H=S['canvas']
def font(n):return ImageFont.truetype(S['font'],n)
def panel(im,box,title,right,n):
 x,y,r,b=box;d=ImageDraw.Draw(im);d.rounded_rectangle(box,radius=16,fill='white',outline=C['ink'],width=6);d.rectangle((x,y,r,y+145),fill=C['card']);d.text((x+45,y+34),'COUNCIL / '+title,font=font(43),fill='white');d.text((x+45,y+185),T['date'],font=font(26),fill=C['ink'])
 if right:
  frac=max(0,min(1,(n-574)/32))
  for i in range(3):
   x0,y0,x1,y1=T['highlight_local_bands'][i];f=frac if i<2 else max(0,min(1,(n-606)/16))
   if f>0:d.rectangle((x+x0,y+y0,x+x0+(x1-x0)*f,y+y1),fill=C['accent'])
 else:d.rectangle((x+45,y+510,min(r-45,x+760),y+536),fill='#eda645'if n>=609 else C['accent'])
 for i,line in enumerate(T['body']):d.text((x+45,y+510+i*41),line,font=font(28),fill=C['ink'])
 d.text((x+45,y+820),'Illustration only',font=font(26),fill=C['ink'])
def render(n):
 im=Image.new('RGB',(W,H),C['background'])
 if n<567:panel(im,T['initial_page_box'],'CYCLE A',False,n)
 else:
  t=min(1,(n-566)/18);initial=T['initial_page_box'];final=T['final_page_boxes'][0];left=tuple(round(a+(b-a)*t)for a,b in zip(initial,final));panel(im,left,'CYCLE A',False,n)
  if n<=575:x=round(-1000+(n-567)*25)
  elif n<584:x=round(-800+(n-575)*1802/9)
  else:x=1002
  panel(im,(x,90,x+865,1014),'CYCLE B',True,n)
 if n==565:
  d=ImageDraw.Draw(im);d.rounded_rectangle((1355,485,1665,795),radius=65,fill=C['skin'],outline=C['ink'],width=9);d.ellipse((1443,605,1467,629),fill=C['ink']);d.ellipse((1553,605,1577,629),fill=C['ink']);d.arc((1430,625,1590,730),0,180,fill=C['ink'],width=9);d.line((1510,795,1510,1080),fill=C['ink'],width=9)
 if 575<=n<584:
  ImageDraw.Draw(im).rectangle((0,600,87+(n-575)*12,619),fill=C['accent'])
 if n>=623:
  t=min(1,(n-623)/25);x=round(1080+650*t);y=round(820-90*t);ImageDraw.Draw(im).polygon([(x,y),(x+2,y+26),(x+9,y+19),(x+17,y+33),(x+23,y+29),(x+15,y+16),(x+27,y+15)],fill=C['ink'])
 return im
rows=[]
for n in range(565,651):
 p=O/f'f{n:05}.png';render(n).save(p);rows.append({'frame':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'render_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
