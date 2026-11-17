from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import sys
p=Path(__file__).resolve().parents[1]; scene=sys.argv[1]
files=sorted((p/'exports/scenes').glob(scene+'-*.png'))
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',22)
review=Image.new('RGB',(len(files)*380,760),'#d4d5ca');d=ImageDraw.Draw(review)
for i,f in enumerate(files):
 im=Image.open(f).convert('RGBA');im.thumbnail((360,640));review.paste(im,(i*380+10,60),im)
 d.text((i*380+10,15),f.stem,fill='#203336',font=font)
 d.text((i*380+10,715),'360 × 640 phone review',fill='#203336',font=font)
(p/'reviews').mkdir(exist_ok=True);review.save(p/'reviews'/f'{scene}.png')
files=sorted((p/'exports/assets').glob('*.png'));cols=6;cw=240;ch=290
sheet=Image.new('RGB',(cols*cw,((len(files)+cols-1)//cols)*ch),'#e5e1d7');d=ImageDraw.Draw(sheet)
small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',13)
for i,f in enumerate(files):
 x=(i%cols)*cw;y=(i//cols)*ch;im=Image.open(f).convert('RGBA');im.thumbnail((220,240));sheet.paste(im,(x+(cw-im.width)//2,y+8),im)
 name=f.stem
 for j in range(0,len(name),30):d.text((x+8,y+250+(j//30)*15),name[j:j+30],fill='#203336',font=small)
sheet.save(p/'FULL_ASSET_CONTACT_SHEET.png')
print('Review sheets updated',scene)
