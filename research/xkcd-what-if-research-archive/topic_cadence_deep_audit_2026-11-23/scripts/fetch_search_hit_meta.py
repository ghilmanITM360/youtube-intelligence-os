#!/usr/bin/env python3
"""Fetch exact publish date/views for unique YouTube search-hit video ids (watch page, unauthenticated). Single thread, 2.5 s spacing, 90 s backoff after 3 empty results; resumable; never records empty rows."""
import json,sys,os,time,datetime
sys.path.insert(0,os.path.dirname(__file__))
import crawl_uploads as c
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out=A+'/raw/search_hits_meta.jsonl'
done=set()
if os.path.exists(out): done={json.loads(l)['video_id'] for l in open(out)}
for l in open(A+'/raw/uploads_raw.jsonl'):
    r=json.loads(l)
    if r['meta'] and r['meta'].get('publishDate') and r['video_id'] not in done:
        open(out,'a').write(json.dumps(dict(video_id=r['video_id'],meta=r['meta'],fetched_at=r.get('fetched_at') or r['observed_at'],source='reused from uploads_raw'))+'\n'); done.add(r['video_id'])
ids=[i for i in open(A+'/raw/search_hit_ids.txt').read().split() if i not in done]
print('todo',len(ids),flush=True); fails=0
f=open(out,'a')
for n,v in enumerate(ids):
    m=None
    for a in range(3):
        time.sleep(2.5); m=c.meta(v)
        if m and m.get('publishDate'): break
        m=None
        if a<2: time.sleep(90 if fails>=3 else 5)
    if m:
        fails=0; f.write(json.dumps(dict(video_id=v,meta=m,fetched_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),source='watch page'))+'\n'); f.flush()
    else:
        fails+=1; f.write(json.dumps(dict(video_id=v,meta=None,fetched_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),source='FAILED (unavailable/private/throttled)'))+'\n'); f.flush()
        if fails>=8: print('stopping: repeated failures (throttle?)',flush=True); break
    if n%50==0: print(n,len(ids),flush=True)
print('done',flush=True)
