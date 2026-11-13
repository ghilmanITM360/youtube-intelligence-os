#!/usr/bin/env python3
"""Verbatim-script reuse detector (read-only DB). For a channel (queue n) finds, per video, the best-matching transcript in ANY other channel
by Jaccard of word 5-gram shingles over the first 200 words (timestamps stripped). usage: python3 script_reuse.py 09"""
import sqlite3,re,csv,sys,os
H=os.path.dirname(os.path.abspath(__file__))
n=sys.argv[1]; q={r['n']:r for r in csv.DictReader(open(f'{H}/queue.csv'))}; cid=q[n]['channel_id']
c=sqlite3.connect(f'file:{H}/../../data/catalog/senior_health_complete.db?mode=ro',uri=True)
def sh(t,k=5,w=200):
    t=re.sub(r'\[\d+\.\d+\]','',t); x=re.sub(r'[^a-z0-9 ]',' ',t.lower()).split()[:w]
    return {tuple(x[i:i+k]) for i in range(max(len(x)-k+1,0))}
rows=c.execute("select t.video_id,v.channel_id,v.title,v.published,v.views,t.text from transcripts t join videos v using(video_id)").fetchall()
S={r[0]:(sh(r[5]),r) for r in rows}
num={r['channel_id']:r['n'] for r in q.values()}
print('video,title,best_match_video,match_channel,match_date,jaccard')
for vid,(s,r) in S.items():
    if r[1]!=cid or not s: continue
    best=max(((len(s&o)/len(s|o),ov) for ov,(o,orr) in S.items() if orr[1]!=cid and o),default=(0,None))
    ov=best[1]; orr=S[ov][1] if ov else None
    print(f'{vid},"{r[2][:50]}",{ov},{num.get(orr[1],orr[1]) if orr else ""},{(orr[3] or "")[:10] if orr else ""},{best[0]:.2f}')
