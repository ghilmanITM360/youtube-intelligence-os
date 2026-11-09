import csv,subprocess
from PIL import Image,ImageChops
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-31-0ll9rEtoRrs-deep-ct-scan'
V="/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The World's Safest Market Is Breaking - Casual Finance (720p, h264).mp4"
for r in csv.DictReader(open('candidates.csv')):
    p=int(r['pre_frame']);o=f"pre2/{r['id']}.jpg"
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str((p+1)/24-0.02),'-i',V,'-frames:v','1','-vf','scale=512:288',o],stderr=subprocess.DEVNULL)
    a=Image.open(o).convert('L').resize((128,72));b=Image.open(f"{R}/frames/stable/{r['id']}.jpg").convert('L').resize((128,72))
    d=ImageChops.difference(a,b);s=sum(d.getdata())/(128*72)
    print(r['id'],r['n'],r['has_I'],round(s,2))
