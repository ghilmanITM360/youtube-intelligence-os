#!/usr/bin/env python3
"""Review search harness (own copy; prior audit files untouched). For each topic|query run YouTube search with upload-date filters
(none/year/month/week/today/hour; unauthenticated, hl=en gl=US) via yt-dlp flat, then read each hit's watch page ytInitialPlayerResponse
for publishDate/views/length/channel. Window membership is computed from publishDate later, not from the filter label."""
import json,re,subprocess,sys,gzip,urllib.request,urllib.parse,datetime,time,os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YT='/private/tmp/claude-501/venv/bin/yt-dlp'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15'
SP={'none':('',6),'year':('EgIIBQ%3D%3D',5),'month':('EgIIBA%3D%3D',6),'week':('EgIIAw%3D%3D',5),'today':('EgIIAg%3D%3D',4),'hour':('EgIIAQ%3D%3D',3)}
def get(u):
    rq=urllib.request.Request(u,headers={'User-Agent':UA,'Accept-Language':'en-US,en;q=0.9','Accept-Encoding':'gzip','Cookie':'CONSENT=YES+1'})
    for i in range(3):
        try:
            r=urllib.request.urlopen(rq,timeout=30);b=r.read()
            if r.headers.get('Content-Encoding')=='gzip':b=gzip.decompress(b)
            return b.decode('utf-8','replace')
        except Exception: time.sleep(2+i*3)
def meta(v):
    h=get('https://www.youtube.com/watch?v='+v)
    if not h:return None
    m=re.search(r'ytInitialPlayerResponse\s*=\s*(\{.+?\});(?:var|</script>)',h,re.S)
    if not m:return None
    try:d=json.loads(m.group(1))
    except Exception:return None
    mf=d.get('microformat',{}).get('playerMicroformatRenderer',{});vd=d.get('videoDetails',{})
    return dict(publishDate=mf.get('publishDate'),lengthSeconds=vd.get('lengthSeconds'),viewCount=vd.get('viewCount'),title=vd.get('title'),
      channel=vd.get('author'),channelId=vd.get('channelId'),isShortsEligible=mf.get('isShortsEligible'),status=d.get('playabilityStatus',{}).get('status'))
def search(q,sp,n):
    u='https://www.youtube.com/results?search_query='+urllib.parse.quote_plus(q)+('&sp='+sp if sp else '')+'&hl=en&gl=US'
    p=subprocess.run([YT,'--flat-playlist','--no-warnings','--playlist-end',str(n),'--print','%(id)s\t%(channel)s\t%(title)s',u],capture_output=True,text=True)
    return [l.split('\t',2) for l in p.stdout.splitlines() if l.count('\t')>=2]
Q=[l.rstrip('\n').split('|') for l in open(sys.argv[1]) if l.strip()]
cache={};out=D+'/raw/search_raw_review_'+os.path.basename(sys.argv[1]).replace('.txt','')+'.jsonl'
with open(out,'a') as f:
    for topic,q in Q:
        for flt,(sp,n) in SP.items():
            if flt=='year': continue
            ts=datetime.datetime.now(datetime.timezone.utc).isoformat();res=search(q,sp,n)
            for rank,(vid,ch,t) in enumerate(res,1):
                if vid not in cache: time.sleep(1.2);cache[vid]=meta(vid)
                f.write(json.dumps(dict(topic=topic,query=q,filter=flt,rank=rank,retrieved_at=ts,video_id=vid,channel=ch,title=t,meta=cache[vid]))+'\n')
            f.flush()
        print(topic,q,flush=True)
