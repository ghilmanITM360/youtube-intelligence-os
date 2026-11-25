#!/usr/bin/env python3
"""YouTube search evidence harness. For each query and each upload-date filter (none/month/week/today/hour) take top-N results
(unauthenticated, hl=en gl=US, no cookies => no personalisation but US-server geography), then read each result's watch page for exact
publishDate/views. Window membership is computed later from the exact publishDate, NOT from the filter label. Output raw/search_raw.jsonl."""
import json,subprocess,sys,datetime,os,urllib.parse,concurrent.futures as cf
sys.path.insert(0,os.path.dirname(__file__))
import crawl_uploads as c
OUT=os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-23-what-if-topic-cadence-deep-audit/raw/search_raw.jsonl')
SP={'none':('',6),'month':('EgIIBA%3D%3D',6),'week':('EgIIAw%3D%3D',5),'today':('EgIIAg%3D%3D',4),'hour':('EgIIAQ%3D%3D',3)}
Q=[l.rstrip('\n').split('|') for l in open(sys.argv[1]) if l.strip()]  # topic|query
cache={}
def search(q,sp,n):
    u='https://www.youtube.com/results?search_query='+urllib.parse.quote_plus(q)+('&sp='+sp if sp else '')+'&hl=en&gl=US'
    p=subprocess.run([c.YTDLP,'--flat-playlist','--no-warnings','--playlist-end',str(n),'--print','%(id)s\t%(channel)s\t%(title)s',u],capture_output=True,text=True)
    return [l.split('\t',2) for l in p.stdout.splitlines() if l.count('\t')>=2]
def m(v):
    if v not in cache: cache[v]=c.meta(v)
    return cache[v]
with open(OUT,'a') as f:
    for topic,q in Q:
        for flt,(sp,n) in SP.items():
            ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
            res=search(q,sp,n)
            with cf.ThreadPoolExecutor(6) as ex: ms=list(ex.map(lambda r:m(r[0]),res))
            for rank,((vid,ch,t),mm) in enumerate(zip(res,ms),1):
                f.write(json.dumps(dict(topic=topic,query=q,filter=flt,rank=rank,retrieved_at=ts,video_id=vid,channel=ch,title=t,meta=mm))+'\n')
            f.flush()
        print(topic,q,flush=True)
