import csv
from PIL import Image,ImageDraw
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-31-0ll9rEtoRrs-deep-ct-scan'
ds=list(csv.DictReader(open('disputes.csv')))
im0=Image.open(f"{R}/disputes/{ds[0]['id']}.jpg");print(im0.size)
w,h=im0.size
for k in range(0,len(ds),8):
    im=Image.new('RGB',(w,h*8),'white');d=ImageDraw.Draw(im)
    for j,r in enumerate(ds[k:k+8]):
        im.paste(Image.open(f"{R}/disputes/{r['id']}.jpg"),(0,j*h));d.text((2,j*h+2),r['id']+' f'+r['cut_frame'],fill='red')
    im.save(f"crops/disp_{k//8}.jpg",quality=88)
