"""Blinded thumbnail sheets for 7 DB channels: 5 strongest + 5 weakest long videos (views, within channel), shuffled, tile letters only (no title/views). Key written separately."""
import csv,os,random
from PIL import Image,ImageDraw,ImageFont
L=os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12/thumbs')
OUT=os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12/blind_2026-11-13'); os.makedirs(OUT,exist_ok=True)
rows=list(csv.DictReader(open('../_analysis/openings_labeled_2026-11-13.csv')))
font=ImageFont.load_default(size=22); key=[]; miss=0
for ch in sorted({r['channel'] for r in rows}):
    d=sorted([r for r in rows if r['channel']==ch and os.path.exists(f"{L}/{r['video_id']}.jpg")],key=lambda r:-int(r['views'] or 0))
    miss+=sum(1 for r in rows if r['channel']==ch)-len(d)
    s=[dict(r,grp='S') for r in d[:5]]+[dict(r,grp='W') for r in d[-5:]]
    random.Random(sum(map(ord,ch))).shuffle(s)
    W,H=400,225; im=Image.new('RGB',(2*W,5*H),'white'); dr=ImageDraw.Draw(im)
    for i,r in enumerate(s):
        r['tile']=chr(65+i); x,y=(i%2)*W,(i//2)*H
        im.paste(Image.open(f"{L}/{r['video_id']}.jpg").convert('RGB').resize((W,H)),(x,y))
        dr.text((x+6,y+4),r['tile'],fill='yellow',font=font,stroke_width=2,stroke_fill='black')
        key.append({k:r[k] for k in('channel','tile','video_id','title','views','grp')})
    im.save(f"{OUT}/{ch.replace(' ','_')}.png")
csv.DictWriter(open(f'{OUT}/KEY_do_not_open_before_scoring.csv','w',newline=''),fieldnames=list(key[0])).writerows(key) if False else None
w=csv.DictWriter(open(f'{OUT}/KEY_do_not_open_before_scoring.csv','w',newline=''),fieldnames=list(key[0]));w.writeheader();w.writerows(key)
print('missing thumbs',miss,OUT)
