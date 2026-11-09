from pathlib import Path
import json,sys,hashlib,math
from PIL import Image,ImageDraw,ImageFont
s=json.loads(Path(sys.argv[1]).read_text());o=Path(sys.argv[2]);o.mkdir(exist_ok=False);t=s['token'];ys=dict(t['y_centers']);rows=[]
for n in range(1119,1161):
 im=Image.new('RGB',tuple(s['canvas']),'#f8faf8');d=ImageDraw.Draw(im)
 for i,h in enumerate([350,220,300,200,125]):d.rectangle((1100+i*100,650-h,1122+i*100,650),fill='#2c817f')
 if n>=1120:
  x=t['center_x'];y=ys.get(n,t['hold_y']);r=t['radius'];pts=[(round(x+r*math.cos(math.pi*k/3)),round(y+r*math.sin(math.pi*k/3)))for k in range(6)];d.polygon(pts,fill=t['color']);d.text((x-69,y+54),'RATE',font=ImageFont.truetype(s['font'],42),fill='white')
  if n>=1141:
   d.rounded_rectangle((x-80,y-65,x+80,y+20),radius=8,fill=t['visor']);d.line((x-62,y-13,x-15,y-33),fill=t['color'],width=9);d.line((x+15,y-33,x+62,y-13),fill=t['color'],width=9)
 for first,box in zip(s['vouchers']['onsets'],s['vouchers']['boxes']):
  if n>=first:
   d.rounded_rectangle(box,radius=12,fill=s['vouchers']['color'],outline=t['color'],width=5);d.text((box[0]+20,box[1]+25),'CREDIT',font=ImageFont.truetype(s['font'],35),fill=t['color']);d.text((box[0]+20,box[1]+75),'ILLUSTRATIVE',font=ImageFont.truetype(s['font'],22),fill=t['color'])
 p=o/f'f{n:05}.png';im.save(p);rows.append({'frame':n,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(o/'render_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
