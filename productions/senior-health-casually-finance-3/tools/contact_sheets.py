from pathlib import Path
from PIL import Image,ImageDraw
import math
R=Path(__file__).resolve().parents[1]
for p in sorted(R.glob('0*')):
 for name,files,cols,thumb in [('HERO_CONTACT_SHEET',[p/'scene_states'/f'S{i:02d}_end.png' for i in [1,3,4]],3,(350,622)),('ALL_SCENES',sorted((p/'scene_states').glob('*_end.png')),4,(270,480)),('ASSET_CONTACT_SHEET',sorted((p/'assets/png').glob('*.png')),4,(260,260))]:
  cw,ch=thumb[0]+20,thumb[1]+45;sheet=Image.new('RGB',(cw*cols,ch*math.ceil(len(files)/cols)),'#e6e5df');d=ImageDraw.Draw(sheet)
  for n,f in enumerate(files):
   im=Image.open(f).convert('RGBA');im.thumbnail(thumb);x=(n%cols)*cw+10;y=(n//cols)*ch+10
   sheet.paste(im,(x+(thumb[0]-im.width)//2,y),im);d.text((x,y+thumb[1]+8),f.stem,fill='black')
  sheet.save(p/'qa'/f'{name}.png')
print('contact sheets rebuilt')
