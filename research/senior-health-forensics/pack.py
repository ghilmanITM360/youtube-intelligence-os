#!/usr/bin/env python3
"""Per-channel data pack from the local senior-health complete DB (read-only).
usage: python3 pack.py 01   -> writes packs/01_<id>.md + prints it. Facts only; interpretation is added by hand in reports/."""
import sqlite3,csv,sys,statistics as st,os,datetime
D=os.path.join(os.path.dirname(__file__),'../../data/catalog/senior_health_complete.db')
n=sys.argv[1]; q={r['n']:r for r in csv.DictReader(open(os.path.join(os.path.dirname(__file__),'queue.csv')))}[n]
cid=q['channel_id']; c=sqlite3.connect(f'file:{D}?mode=ro',uri=True)
ch=c.execute("select name,handle,subscribers,channel_total_videos,channel_total_views,joined,tier from channels where channel_id=?",(cid,)).fetchone()
V=c.execute("select video_id,title,substr(published,1,10),duration_seconds,video_type,views,likes,comments,has_transcript,published_source from videos where channel_id=? order by views desc",(cid,)).fetchall()
T={r[0]:r[1] for r in c.execute("select t.video_id,t.text from transcripts t join videos v using(video_id) where v.channel_id=?",(cid,))}
o=[]; P=o.append
P(f"# Data pack {n} — {q['channel']} ({cid})\n\nFacts from `data/catalog/senior_health_complete.db` (read-only). Views/likes/comments are the snapshot in that DB (DS-000034 player capture 2026-09-28 unless noted); live Chrome numbers are recorded separately in the report.\n")
P(f"Channel row: {ch}\n")
if not V: P("No videos in DB."); out='\n'.join(o); print(out); open(f'packs/{n}_{cid}.md','w').write(out); sys.exit()
N=len(V); f=lambda k:sum(1 for v in V if v[k] not in (None,''))
long=[v for v in V if (v[3] or 0)>=180 and v[4]!='shorts']
P(f"## Inventory\nsaved unique videos {N}; type split {dict((t,sum(1 for v in V if v[4]==t)) for t in set(v[4] for v in V))}; long (>=180s) {len(long)}\n")
P(f"coverage: titles {f(1)}/{N}, views {f(5)}/{N}, dates {f(2)}/{N}, durations {f(3)}/{N}, transcripts {sum(v[8] or 0 for v in V)}/{N} (DB flag) / {len(T)} text rows, thumbnails URL {N}/{N} (i.ytimg hqdefault)\n")
vs=[v[5] for v in V if v[5] is not None]
med=st.median(vs); tot=sum(vs); top3=sum(sorted(vs)[-3:])
ds=sorted(v[2] for v in V if v[2]); P(f"## Performance\nviews: median {med:,.0f}, mean {tot/len(vs):,.0f}, max {max(vs):,}, min {min(vs):,}; total {tot:,}; top-1 share {max(vs)/tot:.0%}, top-3 share {top3/tot:.0%}; dates {ds[0] if ds else '?'} → {ds[-1] if ds else '?'}\n")
if ds:
    d0=datetime.date.fromisoformat(ds[0]);d1=datetime.date.fromisoformat(ds[-1]);days=max((d1-d0).days,1);P(f"cadence: {N} videos over {days} days = {N/days*7:.1f}/week\n")
P("| # | id | date | dur s | views | x median | likes | cmts | title |\n|--|--|--|--|--|--|--|--|--|")
for i,v in enumerate(V,1): P(f"| {i} | {v[0]} | {v[2]} | {v[3]} | {v[5]:,} | {v[5]/med:.1f} | {v[6] or ''} | {v[7] or ''} | {v[1]} |")
# selection
S=[v for v in V if v[5] is not None]
strong=S[:5]; weak=S[-3:]; mid=sorted(S,key=lambda v:abs(v[5]-med))[:3]
P("\n## Chrome viewing plan (5 strong / 3 typical / 3 weak, by views)\n")
for lab,g in(('strong',strong),('typical',mid),('weak',weak)):
    for v in g: P(f"- {lab}: {v[0]} · {v[2]} · {v[5]:,} views · {v[1]}")
P("\n## Opening/ending text of selected videos (transcript; first 90 / last 45 words)\n")
for v in strong+mid+weak:
    t=T.get(v[0]); 
    if t: w=t.split(); P(f"**{v[0]}** OPEN: {' '.join(w[:90])}\n\nEND: {' '.join(w[-45:])}\n")
    else: P(f"**{v[0]}** no transcript in DB\n")
out='\n'.join(o); open(os.path.join(os.path.dirname(__file__),f'packs/{n}_{cid}.md'),'w').write(out); print(out)
