import csv,subprocess,os
from PIL import Image,ImageDraw
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-31-0ll9rEtoRrs-deep-ct-scan'
V="/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The World's Safest Market Is Breaking - Casual Finance (720p, h264).mp4"
rows=list(csv.DictReader(open('candidates.csv')))
for r in rows:
    p=f"pre/{r['id']}.jpg"
    if not os.path.exists(p):
        subprocess.run(['ffmpeg','-v','error','-ss',str((int(r['pre_frame'])+1)/24),'-i',V,'-frames:v','1','-vf','scale=512:288',p])
W,H=512,288
for k in range(0,len(rows),4):
    im=Image.new('RGB',(W*2,H*4),'white');d=ImageDraw.Draw(im)
    for j,r in enumerate(rows[k:k+4]):
        a=Image.open(f"pre/{r['id']}.jpg");b=Image.open(f"{R}/frames/stable/{r['id']}.jpg").resize((W,H))
        im.paste(a,(0,j*H));im.paste(b,(W,j*H))
        d.rectangle((0,j*H,170,j*H+14),fill='yellow');d.text((2,j*H+1),f"{r['id']} PRE f{r['pre_frame']}",fill='black')
        d.rectangle((W,j*H,W+190,j*H+14),fill='yellow');d.text((W+2,j*H+1),f"{r['id']} STABLE {r['start']}-{r['end']}",fill='black')
    im.save(f"crops/sheet_{k//4:02d}.jpg",quality=85)
# disputes
ds=list(csv.DictReader(open('disputes.csv')))
print(len(rows),len(ds))
