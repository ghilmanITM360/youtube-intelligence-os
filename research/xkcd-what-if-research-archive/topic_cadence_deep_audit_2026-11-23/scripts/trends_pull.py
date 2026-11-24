#!/usr/bin/env python3
"""Google Trends pull via the public explore/widgetdata endpoints (unofficial, cookie from trends home). Records query,property,geo,time,category,retrieved_at.
Index is relative (0-100 of the peak within each request), NOT search volume. Each request is single-term unless an anchor batch is used."""
import json,subprocess,urllib.parse,datetime,time,sys,os
CJ='/private/tmp/claude-501/cj_trends.txt'
def curl(url,params=None):
    cmd=['curl','-sS','-m','25','-A','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)','-b',CJ,'-c',CJ]
    if params: cmd+=['-G',url]+sum([['--data-urlencode',f'{k}={v}'] for k,v in params.items()],[])
    else: cmd+=[url]
    return subprocess.run(cmd,capture_output=True,text=True).stdout
curl('https://trends.google.com/trends/?geo=US')
def pull(terms,prop,time_,geo='',cat=0):
    req={"comparisonItem":[{"keyword":t,"geo":geo,"time":time_} for t in terms],"category":cat,"property":prop}
    r=curl('https://trends.google.com/trends/api/explore',{'hl':'en-US','tz':'-300','req':json.dumps(req)})
    try: w=json.loads(r[5:])['widgets']
    except Exception: return {'error':'explore_failed','raw':r[:120]}
    ts=[x for x in w if x['id']=='TIMESERIES'][0]
    d=curl('https://trends.google.com/trends/api/widgetdata/multiline',{'hl':'en-US','tz':'-300','req':json.dumps(ts['request']),'token':ts['token']})
    try: pts=json.loads(d[5:])['default']['timelineData']
    except Exception: return {'error':'data_failed','raw':d[:120]}
    return {'terms':terms,'property':prop or 'web','geo':geo or 'Worldwide','time':time_,'category':cat,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'n_points':len(pts),'values':[[p['formattedAxisTime'],p['value'],p.get('hasData')] for p in pts]}
TERMS=['terminal velocity','neutron star','moon tides','speed of light','orbital velocity','apophis','voyager 1','mars helicopter','jupiter','SETI','raindrop','kettle']
out=open(os.path.join(os.path.dirname(__file__),'..','raw','trends_raw.jsonl'),'a')
for t in TERMS:
    for prop in ('youtube',''):
        for tm in ('today 12-m','today 3-m'):
            r=pull([t],prop,tm); r['query']=t; out.write(json.dumps(r)+'\n'); out.flush()
            print(t,prop or 'web',tm,r.get('n_points',r.get('error')),flush=True); time.sleep(1.5)
