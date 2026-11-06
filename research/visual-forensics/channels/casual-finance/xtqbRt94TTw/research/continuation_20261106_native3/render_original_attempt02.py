"""Casual Finance Video006 original procedural reconstruction. Only spec and font inputs."""
from pathlib import Path
import sys,json,hashlib
from PIL import Image,ImageDraw,ImageFont
s=json.loads(Path(sys.argv[1]).read_text());O=Path(sys.argv[2]);O.mkdir(exist_ok=False);C=s['palette'];font=lambda n:ImageFont.truetype(s['font'],n)
def robot(im,x,y,desk=False):
 d=ImageDraw.Draw(im);d.rounded_rectangle((x,y,x+280,y+250),radius=55,fill=C['skin'],outline=C['ink'],width=8);d.rounded_rectangle((x+38,y+80,x+242,y+143),radius=12,fill=C['ink']);d.ellipse((x+75,y+97,x+98,y+120),fill=C['accent']);d.ellipse((x+180,y+97,x+203,y+120),fill=C['accent']);d.arc((x+84,y+157,x+196,y+210),0,180,fill=C['ink'],width=7);d.rectangle((x+100,y+250,x+180,y+430),fill=C['card'])
 if desk:
  d.rounded_rectangle((x+38,y+80,x+242,y+143),radius=12,outline=C['accent'],width=5)
  d.rectangle((x-65,y+400,x+685,y+455),fill=C['accent'],outline=C['ink'],width=7);d.rectangle((x+330,y+245,x+640,y+410),fill=C['card'],outline=C['ink'],width=6)
  for i in range(3):d.ellipse((x+425+i*38,y+315,x+441+i*38,y+331),fill=C['skin'])
 else:d.line((x+20,y+340,x+340,y+200),fill=C['accent'],width=14)
def bio(n):
 im=Image.new('RGB',tuple(s['canvas']),C['background']);robot(im,250,360);t=s['systems']['G005.01'];xs=dict(t['card_left_track']);x=xs.get(n,t['final_x']);d=ImageDraw.Draw(im)
 if n>=750:
  d.polygon([(x,112),(x+230,112),(x+260,200),(x+260,332),(x+230,420),(x,420)],fill=C['card'])
  for k in range(3):d.ellipse((x+52+k*55,245,x+80+k*55,273),fill=C['accent'])
  d.text((x+300,145),t['copy'][0],font=font(48),fill=C['ink']);d.text((x+300,225),t['copy'][1],font=font(26),fill=C['card']);d.text((x+300,285),t['copy'][2],font=font(30),fill=C['ink']);d.line((x,475,x+890,475),fill=C['building'],width=5)
  for i,line in enumerate(t['copy'][3:]):d.text((x,535+i*62),line,font=font(35),fill=C['ink'])
 return im
def quote(n):
 if n==836:return bio(766)
 im=Image.new('RGB',tuple(s['canvas']),C['background']);d=ImageDraw.Draw(im);t=s['systems']['G006.01']
 for i,line in enumerate(t['copy'][:2]):d.text((175,160+i*68),line,font=font(42),fill=C['ink'])
 d.text((175,340),t['copy'][2],font=font(27),fill=C['card']);robot(im,1040,490,True)
 if n>=839:
  right=dict(t['arrow_right_track']).get(n,663);off=right-663
  for x,h in zip(t['bars_x'],t['bars_heights']):d.rectangle((x+off,t['bar_base']-h,x+off+t['bar_width'],t['bar_base']),fill='#2c817f')
 return im
manifest=[]
for name,rg,fn in [('G005',[749,769],bio),('G006',[836,862],quote)]:
 D=O/name;D.mkdir()
 for n in range(rg[0],rg[1]+1):
  p=D/f'f{n:05}.png';fn(n).save(p);manifest.append({'system':name,'frame':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
