from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv, math, re
import numpy as np

root=Path(__file__).resolve().parents[2]; qa=root/'assets/qa'; rows=list(csv.DictReader((root/'assets/MANIFEST.csv').open()))
choices={}
for r in rows:
    if not r['filename'].startswith(('assets/gen/','assets/vec/')) or r['mode'] not in ('RGBA','RGB'): continue
    id=r['asset_id']
    if id.startswith('CHR-P'):
        a=np.array(Image.open(root/r['filename']).getchannel('A'));ys=np.nonzero((a>200).any(axis=1))[0];score=abs(int(ys.max())-1102)
        if id in choices and score >= choices[id][0]: continue
        choices[id]=(score,r)
    else: choices[id]=(0,r)
selected=[v[1] for k,v in sorted(choices.items()) if k!='PIPE-02' and k!='CHR-MS01']
cut=qa/'cutouts';cut.mkdir(exist_ok=True)
for r in selected:
    im=Image.open(root/r['filename']).convert('RGBA')
    if r['mode']!='RGBA':continue
    im.thumbnail((512,512),Image.Resampling.LANCZOS)
    strip=Image.new('RGB',(im.width*3,im.height))
    for i,bg in enumerate(('#FFFFFF','#0C0C0C','#FF00FF')):
        panel=Image.new('RGBA',im.size,bg);panel.alpha_composite(im);strip.paste(panel.convert('RGB'),(i*im.width,0))
    strip.save(cut/(r['asset_id']+'.png'))
font=ImageFont.load_default(); cols=8;cw=250;ch=240; h=math.ceil(len(selected)/cols)*ch
for bg,name in [('#FFFFFF','CONTACT_SHEET-v2.png'),('#0C0C0C','CONTACT_SHEET_DARK-v2.png')]:
    out=Image.new('RGB',(cols*cw,h),bg);d=ImageDraw.Draw(out)
    for i,r in enumerate(selected):
        x=(i%cols)*cw;y=(i//cols)*ch;im=Image.open(root/r['filename']).convert('RGBA');im.thumbnail((cw-20,ch-45),Image.Resampling.LANCZOS)
        out.paste(im,(x+(cw-im.width)//2,y+30),im);d.text((x+7,y+7),r['asset_id']+' '+Path(r['filename']).stem,fill=('black' if bg=='#FFFFFF' else 'white'),font=font)
    out.save(qa/name)
(qa/'review_selection.csv').write_text('asset_id,filename,status\n'+''.join(f"{r['asset_id']},{r['filename']},{r['status']}\n" for r in selected))
print(f'{len(selected)} review assets; {sum(r["mode"]=="RGBA" for r in selected)} cutout strips; review selection is not approval')
