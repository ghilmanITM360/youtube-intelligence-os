import csv
from PIL import Image,ImageDraw
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-31-0ll9rEtoRrs-deep-ct-scan'
ids="EP0335 EP0337 EP0339 EP0341 EP0342 EP0343 EP0344 EP0346 EP0347 EP0348 EP0350 EP0351 EP0352 EP0354 EP0355 EP0356 EP0363 EP0364 EP0365 EP0366 EP0367 EP0368 EP0369 EP0371 EP0372 EP0373 EP0376 EP0382 EP0385 EP0386 EP0388 EP0391 EP0392 EP0336 EP0331 EP0333 EP0340".split()
W,H=512,288
for k in range(0,len(ids),6):
    im=Image.new('RGB',(W*2,H*3),'white');d=ImageDraw.Draw(im)
    for j,i in enumerate(ids[k:k+6]):
        c,rw=j%2,j//2
        a=Image.open(f"pre2/{i}.jpg");b=Image.open(f"{R}/frames/stable/{i}.jpg").resize((W,H))
        # side by side halves: pre left half-size, stable right half-size
        a=a.resize((W//2,H//2));b=b.resize((W//2,H//2))
        x=c*W;y=rw*H
        im.paste(a,(x,y));im.paste(b,(x+W//2,y))
        d.text((x+2,y+2),i+' PRE | STABLE',fill='red')
        d.rectangle((x,y,x+W-1,y+H//2-1),outline='gray')
    im=im.crop((0,0,W*2,H*3//2*1+0)) if False else im
    im.save(f"crops/n_{k//6}.jpg",quality=88)
print(len(ids))
