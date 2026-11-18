#!/usr/bin/env python3
"""Per-channel metrics from finance_economics_complete.db (read-only). Run from repo root: python3 -I <file>."""
import sqlite3,re,csv,statistics as st,os
from datetime import date
T=date(2026,11,18)
OUT='research/new-finance-channel/'
db=sqlite3.connect('file:data/catalog/finance_economics_complete.db?mode=ro',uri=True)
P0=['Casual Finance','Monkey Economics','MonkeyExplains','Crayon Capital','Capital Case','Paper Billions']
P1=['Primate Economics','PENNY','Neu','Built On You','Business Decoded','Nostalgic Wheels','Econ in a Nutshell','The Expensive Part','Brimm.','Modern MBA','Economics Explained','How Money Works','Money & Macro','Patrick Boyle','PensionCraft','Mr. Ranks','Finance ANALYST']
def d(p):
    m=re.match(r'(\d{4}-\d\d-\d\d)',p or ''); return date.fromisoformat(m.group(1)) if m else None
rows=[]; tops=[]
for pr,names in (('P0',P0),('P1',P1)):
    for n in names:
        cid=db.execute("select channel_id,subscribers from channels where name=?",(n,)).fetchone()
        if not cid: print('missing',n); continue
        vs=[]
        for vid,t,pub,dur,vw,vt,tx in db.execute("select video_id,title,published,duration_seconds,views,video_type,(select text from transcripts where video_id=videos.video_id limit 1) from videos where channel_id=?",(cid[0],)):
            dt=d(pub)
            if dt is None or vw is None: continue
            short=(vt or '').upper()=='SHORT' or (dur or 999)<=60
            vs.append(dict(id=vid,t=t or '',dt=dt,dur=dur or 0,v=vw,short=short,age=max((T-dt).days,1),tx=tx or ''))
        long_=[x for x in vs if not x['short']]; sh=[x for x in vs if x['short']]
        if not vs: continue
        med=st.median([x['v'] for x in long_]) if long_ else None
        rec=[x for x in long_ if x['age']>=14]
        out=[x for x in rec if med and x['v']>=2*med]
        l90=[x for x in vs if x['age']<=90]
        def feat(xs,f): return round(100*sum(1 for x in xs if f(x))/len(xs)) if xs else ''
        num=lambda x:bool(re.search(r'\d',x['t'])); q=lambda x:'?' in x['t']
        caps=lambda x:any(len(w)>=4 and w.isupper() for w in x['t'].split())
        wh=lambda x:bool(re.match(r'(why|how|what|who|when|is|are|can|will)\b',x['t'].strip().lower()))
        hk=[x for x in long_ if x['tx']]
        h40=lambda x:' '.join(x['tx'].split()[:40]).lower()
        rows.append(dict(priority=pr,channel=n,subs=cid[1] or '',videos=len(vs),longform=len(long_),shorts=len(sh),shorts_pct=round(100*len(sh)/len(vs)),first=min(x['dt'] for x in vs),last=max(x['dt'] for x in vs),per_30d_last90=round(len(l90)/3,1),
            med_long_views=int(med) if med else '',max_views=max(x['v'] for x in vs),med_long_min=round(st.median([x['dur'] for x in long_])/60,1) if long_ else '',
            med_views_per_day_long_14d=int(st.median([x['v']/x['age'] for x in rec])) if rec else '',outlier_2x_pct=round(100*len(out)/len(rec)) if rec else '',
            title_len_words=round(st.mean(len(x['t'].split()) for x in long_),1) if long_ else '',title_number_pct=feat(long_,num),title_question_pct=feat(long_,q),title_caps_pct=feat(long_,caps),title_wh_open_pct=feat(long_,wh),
            hook40_you_pct=feat(hk,lambda x:bool(re.search(r'\byou(r)?\b',h40(x)))),hook40_number_pct=feat(hk,lambda x:bool(re.search(r'\d|million|billion|trillion|percent',h40(x)))),hook40_question_pct=feat(hk,lambda x:'?' in ' '.join(x['tx'].split()[:40])),hook_n=len(hk)))
        for x in sorted(long_ or vs,key=lambda x:-x['v'])[:5]: tops.append([n,x['id'],x['t'],x['dt'],x['v'],round(x['dur']/60,1),'short' if x['short'] else 'long'])
w=csv.DictWriter(open(OUT+'03_PRIMARY_REFERENCE_CHANNELS/CHANNEL_METRICS_2026-11-18.csv','w',newline=''),fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
csv.writer(open(OUT+'03_PRIMARY_REFERENCE_CHANNELS/TOP_LONGFORM_VIDEOS_2026-11-18.csv','w',newline='')).writerows([['channel','video_id','title','published','views','minutes','type']]+tops)
for r in rows: print(r['priority'],r['channel'][:18].ljust(18),r['subs'],'v',r['videos'],'L',r['longform'],'S%',r['shorts_pct'],'/30d',r['per_30d_last90'],'med',r['med_long_views'],'min',r['med_long_min'],'vpd',r['med_views_per_day_long_14d'],'out%',r['outlier_2x_pct'],'num%',r['title_number_pct'],'q%',r['title_question_pct'],'wh%',r['title_wh_open_pct'],'caps%',r['title_caps_pct'],'hook you/num/q',r['hook40_you_pct'],r['hook40_number_pct'],r['hook40_question_pct'],r['hook_n'])
