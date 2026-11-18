# Phase E/Five part C: opening-hook features, top vs below-median long videos within channel. Read-only. Run: python3 -I <this> from repo root.
import sqlite3,re,statistics as st
from datetime import date
c=sqlite3.connect('file:data/catalog/finance_economics_complete.db?mode=ro',uri=True)
ch={r[0]:r[1] for r in c.execute("select channel_id,name from channels")}
today=date(2026,11,18)
tx={}
for vid,t in c.execute("select video_id,text from transcripts where text is not null and length(text)>200"):
    tx.setdefault(vid,t)
by={}
for vid,cid,v,p,d,vt in c.execute("select video_id,channel_id,views,published,duration_seconds,video_type from videos where views is not null and published is not null"):
    if ch.get(cid)=='Mr. Finance' or vid not in tx: continue
    if (vt or '').upper()=='SHORT' or (d or 999)<=60: continue
    try: age=(today-date.fromisoformat(p[:10])).days
    except: continue
    if age<14: continue
    by.setdefault(cid,[]).append((vid,v))
w=lambda t,n:' '.join(t.split()[:n]).lower()
F={
 'first 40 words: number/amount':lambda t:bool(re.search(r'\d|million|billion|trillion|percent',w(t,40))),
 'first 40 words: question mark':lambda t:'?' in ' '.join(t.split()[:40]),
 'first 40 words: you/your':lambda t:bool(re.search(r'\byou(r)?\b',w(t,40))),
 'first 100 words: but/yet/except/however':lambda t:bool(re.search(r'\b(but|yet|except|however|instead)\b',w(t,100))),
 'greeting/intro in first 40 words':lambda t:bool(re.search(r"\b(welcome|hey|hi guys|hello|in this video|today we|today i)\b",w(t,40))),
 'first 40 words: "imagine"/"picture"':lambda t:bool(re.search(r'\b(imagine|picture this)\b',w(t,40))),
}
res={k:[0,0,0,0] for k in F}; wc={0:[],2:[]}; n=0
for cid,vs in by.items():
    if len(vs)<8: continue
    med=st.median(v for _,v in vs)
    if med<=0: continue
    n+=1
    for vid,v in vs:
        r=v/med; g=0 if r>=2 else (2 if r<1 else None)
        if g is None: continue
        t=tx[vid]; wc[g].append(len(t.split()))
        for k,f in F.items():
            res[k][g+1]+=1
            if f(t): res[k][g]+=1
print('channels',n)
for k,(a,b,cc,d) in res.items(): print(f'{k:45s} top {round(100*a/b)}% (n={b}) low {round(100*cc/d)}% (n={d})')
print('median transcript words top',st.median(wc[0]),'low',st.median(wc[2]))
