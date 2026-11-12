"""Blinded thumbnail review sheets for channels 032-036, 038-068.
Per channel: top-K and bottom-K long-form videos by PI (views if PI missing; Shorts-only channel -> Shorts),
shuffled, labelled A..H with title only (no PI/views). Key saved separately. Outputs to local audit folder."""
import pandas as pd, random, os, textwrap
from PIL import Image, ImageDraw, ImageFont
L=os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12')
v=pd.read_csv(L+'/out/unique_video_performance_database.csv',usecols=['video_id','title','views','is_short','PI','name'])
r=pd.read_csv('05_OWNER_QA/CHANNEL_TIER_RANKING.csv')[['channel_number','channel_name']]
os.makedirs(L+'/montage_blind',exist_ok=True)
font=ImageFont.load_default(size=15)
keys=[]
for n,name in r.itertuples(index=False):
    if not (32<=n<=36 or 38<=n<=68): continue
    d=v[v.name==name].copy()
    d=d[os.path.exists and d.video_id.map(lambda x:os.path.exists(f'{L}/thumbs/{x}.jpg'))]
    lf=d[~d.is_short.astype(bool)]
    d=lf if len(lf)>=2 else d
    col='PI' if d.PI.notna().sum()>=len(d)*0.8 else 'views'
    d=d.dropna(subset=[col]).sort_values(col,ascending=False)
    k=min(4,len(d)//2)
    if k<1: print('skip',n,name,len(d)); continue
    top=d.head(k).assign(grp='W'); bot=d.tail(k).assign(grp='L')
    s=pd.concat([top,bot]).sample(frac=1,random_state=n).reset_index(drop=True)
    s['tile']=[chr(65+i) for i in range(len(s))]; s['channel_number']=n; s['rank_col']=col
    keys.append(s[['channel_number','name','tile','video_id','title','views','PI','grp','rank_col']])
    cols=4; rows=(len(s)+cols-1)//cols; W,H,T=360,203,52
    im=Image.new('RGB',(cols*W,rows*(H+T)),'white'); dr=ImageDraw.Draw(im)
    for i,row in s.iterrows():
        x,y=(i%cols)*W,(i//cols)*(H+T)
        im.paste(Image.open(f'{L}/thumbs/{row.video_id}.jpg').convert('RGB').resize((W,H)),(x,y))
        dr.text((x+4,y+2),row.tile,fill='yellow',font=font,stroke_width=2,stroke_fill='black')
        dr.text((x+3,y+H+2),'\n'.join(textwrap.wrap(row.title,52)[:3]),fill='black',font=font)
    im.save(f'{L}/montage_blind/{n:03d}.png')
pd.concat(keys).to_csv(L+'/out/thumb_review_key.csv',index=False)
print(len(keys),'channels')
