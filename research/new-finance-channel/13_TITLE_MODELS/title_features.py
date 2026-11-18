# Phase E: title feature lift within channel. Read-only on the DB. Run: python3 -I <this> from repo root.
import sqlite3,re,statistics as st,csv
c=sqlite3.connect('file:data/catalog/finance_economics_complete.db?mode=ro',uri=True)
ch={r[0]:r[1] for r in c.execute("select channel_id,name from channels")}
rows=c.execute("select channel_id,title,views,published,duration_seconds,video_type from videos where views is not null and published is not null").fetchall()
from datetime import date
today=date(2026,11,18)
by={}
for cid,t,v,p,d,vt in rows:
    if ch.get(cid)=='Mr. Finance': continue
    if (vt or '').upper()=='SHORT' or (d or 999)<=60: continue
    try: age=(today-date.fromisoformat(p[:10])).days
    except: continue
    if age<14: continue
    by.setdefault(cid,[]).append((t,v))
F={
 'starts Why/How/What':lambda t:bool(re.match(r'(why|how|what)\b',t,re.I)),
 'question mark':lambda t:'?' in t,
 'has number':lambda t:bool(re.search(r'\d',t)),
 'has $ or %':lambda t:bool(re.search(r'[$%]',t)),
 'has colon/dash':lambda t:bool(re.search(r'[:—\-]\s',t)),
 'ALL-CAPS word':lambda t:bool(re.search(r'\b[A-Z]{3,}\b',t)),
 'you/your':lambda t:bool(re.search(r'\b(you|your)\b',t,re.I)),
 'under 50 chars':lambda t:len(t)<50,
 '"Really/Actually/Real"':lambda t:bool(re.search(r'\b(really|actually|real|truth|secret)\b',t,re.I)),
}
res={k:[0,0,0,0] for k in F}  # hits_top,n_top,hits_low,n_low
n=0
for cid,vs in by.items():
    if len(vs)<8: continue
    med=st.median(v for _,v in vs)
    if med<=0: continue
    n+=1
    for t,v in vs:
        r=v/med
        grp=0 if r>=2 else (2 if r<1 else None)
        if grp is None: continue
        for k,f in F.items():
            res[k][grp+1]+=1
            if f(t): res[k][grp]+=1
out=[]
for k,(ht,nt,hl,nl) in res.items():
    out.append((k,ht/nt if nt else 0,hl/nl if nl else 0,nt,nl))
w=csv.writer(open('research/new-finance-channel/13_TITLE_MODELS/TITLE_FEATURE_LIFT_2026-11-18.csv','w'))
w.writerow(['feature','share_in_2x_plus','share_in_below_median','n_2x_plus','n_below'])
for r in out: w.writerow([r[0],f'{r[1]:.3f}',f'{r[2]:.3f}',r[3],r[4]])
print('channels',n)
for r in out: print(f'{r[0]:28s} top {r[1]:.0%} low {r[2]:.0%} n={r[3]}/{r[4]}')
