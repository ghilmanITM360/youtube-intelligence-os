#!/usr/bin/env python3
"""Throttle-aware resume after YouTube returned HTTP 429 to the parallel crawl. Single thread, 2.5 s spacing, backoff 90 s on failure.
Cutoffs (days): xkcd 400 (full listing), other core 180, rest 90. Adds fetched_at per row."""
import json,sys,os,time,datetime,collections
sys.path.insert(0,os.path.dirname(__file__))
import crawl_uploads as c
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUT={'UC6IxnFzHofFJ5X2PycSMsww':400,'UCphTF9wHwhCt-BzIq-s4V-g':180,'UCESitBa9MCU0T8h6moQe6SQ':180,'UCj5LSbbMjczTInjlL-e42fQ':180,'UCFoDdYfR-6E2bBdTXX77mIA':180}
T=c.T
have=collections.defaultdict(dict)
for l in open(A+'/raw/uploads_raw.jsonl'):
    r=json.loads(l); have[r['channel_id']][r['video_id']]=r
def fetch(vid):
    for i in range(3):
        m=c.meta(vid)
        if m: return m
        time.sleep(90)
    return None
order=sys.argv[1:]
out=open(A+'/raw/uploads_raw.jsonl','a'); st={}
for cid in order:
    cut=T-datetime.timedelta(days=CUT.get(cid,90)); st[cid]={}
    for tab,fmt in (('videos','Long'),('shorts','Short')):
        rows,err=c.flat(cid,tab); old=0; fails=0; n=0; crossed=False
        for vid,title in rows:
            if vid in have[cid]: m=have[cid][vid]['meta']
            else:
                time.sleep(2.5); m=fetch(vid)
                rec=dict(channel_id=cid,video_id=vid,tab=tab,format=fmt,tab_title=title,meta=m,observed_at=T.isoformat(),fetched_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
                if m: out.write(json.dumps(rec)+'\n'); out.flush(); have[cid][vid]=rec; n+=1
            if not m:
                fails+=1
                if fails>=3: break
                continue
            fails=0; d=c.pd(m['publishDate'])
            if d and d<cut: old+=1
            elif d: old=0
            if old>=6: crossed=True; break
        st[cid][tab]=dict(listed=len(rows),fetched_new=n,crossed_cutoff=crossed,exhausted=(not crossed and fails<3),throttled=fails>=3,cutoff_days=CUT.get(cid,90))
        print(cid,tab,st[cid][tab],flush=True)
    json.dump(st[cid],open(A+f'/raw/resume_status_{cid}.json','w'))
