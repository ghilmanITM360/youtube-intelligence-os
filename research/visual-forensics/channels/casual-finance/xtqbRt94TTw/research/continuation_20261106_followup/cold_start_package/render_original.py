"""Standalone original bounded reconstruction. Inputs: spec JSON + system font only.
No source-evidence/media reads. Outputs remain outside Git.
"""
import json,sys,hashlib
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
spec=json.loads(Path(sys.argv[1]).read_text());out=Path(sys.argv[2]);out.mkdir(exist_ok=False)
C=spec['palette'];W,H=spec['canvas'];F=spec['font']
def font(n):return ImageFont.truetype(F,n)
def card(d,box,title,subtitle):
 d.rounded_rectangle(box,radius=16,fill=C['card']);x,y,_,_=box
 d.rectangle((x+22,y+22,x+28,y+142),fill=C['accent']);d.text((x+48,y+30),title,font=font(36),fill='white');d.text((x+48,y+95),subtitle,font=font(25),fill='#d6e4e5')
def opening(n):
 im=Image.new('RGB',(W,H),C['background']);d=ImageDraw.Draw(im);o=spec['opening_original_v1']
 if n>=1:
  dy=round(496*max(0,(12-n)/11));a,b=o['building_x'];d.polygon([(a,680+dy),(960,580+dy),(b,680+dy)],fill=C['building'],outline=C['ink'],width=8)
  d.rectangle((a+30,680+dy,b-30,1120+dy),fill=C['building'],outline=C['ink'],width=8)
  if n>=12:
   for cx,cy in o['eyes_centers']:
    d.ellipse((cx-44,cy-58,cx+44,cy+58),fill='white',outline=C['ink'],width=7);d.ellipse((cx-10,cy-10,cx+10,cy+10),fill=C['ink'])
   d.text((735,950),'MONETARY COUNCIL',font=font(37),fill=C['ink'])
 if n>=6:
  y=round(-178+(210+178)*min(1,(n-6)/17));x=round(125-15*max(0,min(1,(n-23)/9)));card(d,(x,y,x+650,y+180),*o['card1_text'])
 if n>=32:card(d,tuple(o['card2_box']),*o['card2_text'])
 return im
def bulletin(n):
 im=Image.new('RGB',(W,H),C['background']);d=ImageDraw.Draw(im);o=spec['bulletin_entry_original_v1'];box=tuple(o['page_box'])
 d.rounded_rectangle(box,radius=20,fill='white',outline=C['ink'],width=6);d.rectangle((96,90,1260,235),fill=C['card']);d.text((145,126),o['page_title'],font=font(54),fill='white');d.text((145,270),o['subtitle'],font=font(27),fill=C['ink']);d.text((145,350),o['date'],font=font(32),fill=C['ink'])
 for i,line in enumerate(o['body']):d.text((145,470+i*110),line,font=font(35),fill=C['ink'])
 d.text((145,890),'Illustrative content - no source screenshot',font=font(27),fill=C['ink']);a=o['presenter'];cx,cy=a['head_center'];r=a['radius']
 d.rounded_rectangle((cx-r,cy-r,cx+r,cy+r),radius=65,fill=C['skin'],outline=C['ink'],width=9)
 for ex in [cx-55,cx+55]:d.ellipse((ex-12,cy-35,ex+12,cy-11),fill=C['ink'])
 d.arc((cx-80,cy-15,cx+80,cy+90),0,180,fill=C['ink'],width=9);d.line((cx,cy+r,cx,1080),fill=C['ink'],width=9);d.line((cx,875,cx-110,950),fill=C['ink'],width=9);d.line((cx,875,cx+95,945,cx+40,1000),fill=C['ink'],width=9);d.line(tuple(tuple(v)for v in a['pointer_endpoints']),fill='#6a5148',width=9)
 return im
manifest=[]
for group,frames,renderer in [('opening',range(37),opening),('bulletin',range(301,304),bulletin)]:
 (out/group).mkdir()
 for n in frames:
  path=out/group/f'f{n:05d}.png';im=renderer(n);im.save(path);manifest.append({'group':group,'frame':n,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(out/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
