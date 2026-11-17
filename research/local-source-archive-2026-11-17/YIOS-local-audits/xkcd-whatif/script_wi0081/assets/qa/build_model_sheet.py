from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import csv,hashlib,sys
root=Path.cwd(); attempt=int(sys.argv[1]) if len(sys.argv)>1 else 1
items=[('CHR-V01','CHR_V01_front-v4.png'),('CHR-V02','CHR_V02_three_quarter-v4.png'),('CHR-V03','CHR_V03_profile-v2.png'),('CHR-V04','CHR_V04_back-v4.png'),('CHR-X01','CHR_X01_expr_neutral-v4.png'),('CHR-X02','CHR_X02_expr_curious.png'),('CHR-X03','CHR_X03_expr_surprised.png'),('CHR-X04','CHR_X04_expr_deadpan.png'),('CHR-X05','CHR_X05_expr_smug.png'),('CHR-X06','CHR_X06_expr_worried.png'),('CHR-G01','CHR_G01_grip_spoon_side.png'),('CHR-G02','CHR_G02_grip_spoon_top-v3.png'),('CHR-G03','CHR_G03_grip_point-v3.png'),('CHR-G04','CHR_G04_grip_pinch_cube.png')]
if attempt >= 2:
 items[0] = ('CHR-V01','CHR_V01_front-v5.png')
 items[1] = ('CHR-V02','CHR_V02_three_quarter-v5.png')
 items[2] = ('CHR-V03','CHR_V03_profile-v3.png')
 items[3] = ('CHR-V04','CHR_V04_back-v5.png')
if attempt >= 3:
 items[2] = ('CHR-V03','CHR_V03_profile-v4.png')
canvas=Image.new('RGB',(3200,2400),'#f8f8f8'); d=ImageDraw.Draw(canvas)
try:f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',38)
except OSError:f=ImageFont.load_default()
for i,(id,name) in enumerate(items):
 x=(i%4)*800;y=(i//4)*575;d.text((x+20,y+10),id,fill='#0c0c0c',font=f)
 im=Image.open(root/'assets/chr'/name).convert('RGBA'); im.thumbnail((740,500),Image.Resampling.LANCZOS);canvas.paste(im,(x+(800-im.width)//2,y+60),im)
 d.line((x+393,y+72,x+407,y+72),fill='#d7263d',width=2);d.line((x+400,y+65,x+400,y+79),fill='#d7263d',width=2)
d.text((1630,1790),'0.37 head / figure ratio',fill='#0c0c0c',font=f);d.line((1680,1870,1680,2250),fill='#0c0c0c',width=5);d.line((1655,1870,1705,1870),fill='#0c0c0c',width=5);d.line((1655,2011,1705,2011),fill='#d7263d',width=5);d.line((1655,2250,1705,2250),fill='#0c0c0c',width=5)
p=root/'assets/chr'/('CHR_MS01_model_sheet.png' if attempt==1 else f'CHR_MS01_model_sheet-v{attempt}.png');canvas.save(p)
m=root/'assets/MANIFEST.csv'
with m.open(newline='') as z:r=csv.DictReader(z);fields=r.fieldnames;rows=list(r)
rows.append(dict(asset_id='CHR-MS01',filename=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),width=3200,height=2400,mode='RGB',generated_or_code='code',attempt=attempt,status='FAILED',notes='STOP-CHECK: head/body proportions and baseline differ among views; see QA report.'))
with m.open('w',newline='') as z:w=csv.DictWriter(z,fieldnames=fields);w.writeheader();w.writerows(rows)
print(p)
