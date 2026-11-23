from pathlib import Path
import hashlib, json, io
import ctypes.util
f=ctypes.util.find_library
ctypes.util.find_library=lambda n:'/opt/homebrew/lib/libcairo.2.dylib' if n=='cairo' else f(n)
import cairosvg
from PIL import Image, ImageDraw
src=Path(__file__).resolve().parent.parent
out=Path(__file__).resolve().parent
names=['rig_head_worried','rig_head_smirk','rig_body_down','rig_body_shrug','rig_body_point']
for name in names:
 s=(src/(name+'.svg')).read_text()
 if name=='rig_head_worried':
  old='M 493 345 Q 520 316 548 332 M 742 332 Q 768 318 797 347 M 620 494 Q 635 476 650 487 Q 664 497 681 483'
  new='M 490 344 Q 516 322 549 301 M 741 301 Q 774 322 800 344 M 606 505 Q 650 465 694 505'
  assert old in s;s=s.replace(old,new)
 if name=='rig_head_smirk':
  old='M 490 329 Q 519 307 549 327 M 742 347 Q 770 337 797 349 M 619 481 Q 652 490 683 464'
  new='M 489 310 Q 518 285 550 308 M 742 346 Q 770 337 797 349 M 602 481 C 630 489 659 496 692 462'
  assert old in s;s=s.replace(old,new)
 if name.startswith('rig_body'):
  old='fill="#5b6b3a" stroke-width="27"'
  assert old in s;s=s.replace(old,'fill="#72864a" stroke-width="17"')
 (out/(name+'.svg')).write_text(s)
 png=cairosvg.svg2png(bytestring=s.encode(),scale=2)
 im=Image.open(io.BytesIO(png)).convert('RGBA'); im.resize((im.width//2,im.height//2),Image.Resampling.LANCZOS).save(out/(name+'.png'))
# Compose same anchor geometry, unchanged heads in source
heads=['neutral','smile','worried','surprised','smirk']; bodies=['down','shrug','point']
def load(n):
 p=out/(n+'.png');return Image.open(p if p.exists() else src/(n+'.png')).convert('RGBA')
def figure(h,b):
 body=load('rig_body_'+b);head=load('rig_head_'+h); c=Image.new('RGBA',(1500,1951)); bx=0 if b=='point' else 100
 c.alpha_composite(body,(bx,651));c.alpha_composite(head,(750-350,70));return c
sheet=Image.new('RGB',(1920,1080),'white');d=ImageDraw.Draw(sheet)
for row,b in enumerate(bodies):
 for col,h in enumerate(heads):
  im=figure(h,b); im.thumbnail((310,300),Image.Resampling.LANCZOS); x=col*384+(384-im.width)//2; y=row*360+35
  sheet.paste(im,(x,y),im);d.text((col*384+8,row*360+8),b+' / '+h,fill='black')
sheet.save(out/'all_15_alignment_1080p.jpg',quality=95)
# Large and phone-size expression comparison alongside original
sheet=Image.new('RGB',(1920,1080),'white');d=ImageDraw.Draw(sheet)
for row,h in enumerate(['worried','smirk']):
 for col,version in enumerate(['original','corrected']):
  p=(src if version=='original' else out)/('rig_head_'+h+'.png');im=Image.open(p).convert('RGBA'); im.thumbnail((400,400),Image.Resampling.LANCZOS)
  x=col*470+40;y=row*520+55;sheet.paste(im,(x,y),im);d.text((x,y-25),h+' '+version,fill='black')
  tiny=figure(h,'down') if version=='corrected' else None
  if tiny is not None:
   tiny.thumbnail((110,180),Image.Resampling.LANCZOS);sheet.paste(tiny,(1250,y+50),tiny);d.text((1390,y+100),'phone scale: 180 px figure',fill='black')
sheet.save(out/'expression_comparison_1080p.jpg',quality=95)
files=[out/(n+'.'+ext) for n in names for ext in ['svg','png']]
with (out/'SHA256SUMS.txt').open('w') as f:
 for p in files+[out/'all_15_alignment_1080p.jpg',out/'expression_comparison_1080p.jpg']:
  f.write(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n')
for p in files:
 if p.suffix=='.png':
  im=Image.open(p);print(p.name, im.size, im.mode, im.getchannel('A').getextrema(), im.getbbox())
