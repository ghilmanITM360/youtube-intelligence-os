#!/usr/bin/env python3
"""Independent upload census. Python 3.9. Observation time T = script start (Asia/Karachi, UTC+5).
Method: list channel tabs /videos /shorts /streams with yt-dlp --flat-playlist (tab = YouTube's own format classification),
then read each watch page's ytInitialPlayerResponse (publishDate w/ offset, viewCount, lengthSeconds, isShortsEligible).
Stops a tab after 6 consecutive items older than the cutoff (365d core, 180d others). Output: raw/uploads_raw.jsonl + raw/channels_raw.json."""
import json,re,subprocess,sys,gzip,urllib.request,datetime,time,os,concurrent.futures as cf
OUT=os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-23-what-if-topic-cadence-deep-audit/raw')
YTDLP='/private/tmp/claude-501/venv/bin/yt-dlp'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15'
T=datetime.datetime.now(datetime.timezone.utc)
CORE={'UC6IxnFzHofFJ5X2PycSMsww','UCphTF9wHwhCt-BzIq-s4V-g','UCESitBa9MCU0T8h6moQe6SQ','UCdiuNtuJid5x40JU58RP6jQ'}
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept-Language':'en-US,en;q=0.9','Accept-Encoding':'gzip','Cookie':'CONSENT=YES+1'})
    for i in range(3):
        try:
            r=urllib.request.urlopen(req,timeout=30); b=r.read()
            if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
            return b.decode('utf-8','replace')
        except Exception as e: err=e; time.sleep(1+i)
    return None
def flat(cid,tab):
    p=subprocess.run([YTDLP,'--flat-playlist','--no-warnings','--print','%(id)s\t%(title)s',f'https://www.youtube.com/channel/{cid}/{tab}'],capture_output=True,text=True)
    rows=[l.split('\t',1) for l in p.stdout.splitlines() if '\t' in l]
    return rows, (p.stderr.strip()[-200:] if not rows else '')
def meta(vid):
    h=get(f'https://www.youtube.com/watch?v={vid}')
    if not h: return None
    m=re.search(r'ytInitialPlayerResponse\s*=\s*(\{.+?\});(?:var|</script>)',h,re.S)
    if not m: return None
    try: d=json.loads(m.group(1))
    except Exception: return None
    mf=d.get('microformat',{}).get('playerMicroformatRenderer',{}); vd=d.get('videoDetails',{})
    return dict(publishDate=mf.get('publishDate'),uploadDate=mf.get('uploadDate'),lengthSeconds=vd.get('lengthSeconds') or mf.get('lengthSeconds'),
      viewCount=vd.get('viewCount') or mf.get('viewCount'),isShortsEligible=mf.get('isShortsEligible'),isLiveContent=vd.get('isLiveContent'),
      live=bool(mf.get('liveBroadcastDetails')),title=vd.get('title'),status=d.get('playabilityStatus',{}).get('status'))
def subs(cid):
    h=get(f'https://www.youtube.com/channel/{cid}')
    if not h: return None,None
    m=re.search(r'"subscriberCountText":\{[^}]*?"content":"([^"]+)"',h) or re.search(r'([\d.,]+[KMB]?) subscribers',h)
    n=re.search(r'<meta property="og:title" content="([^"]+)"',h)
    return (m.group(1) if m else None),(n.group(1) if n else None)
def pd(s):
    try: return datetime.datetime.fromisoformat(s)
    except Exception: return None
def run(cid,fout,chans):
    cutoff=T-datetime.timedelta(days=365 if cid in CORE else 180)
    sc,nm=subs(cid); chans[cid]={'subscribers_text':sc,'name':nm,'observed_at':T.isoformat(),'tabs':{}}
    for tab,fmt in (('videos','Long'),('shorts','Short'),('streams','Live')):
        rows,err=flat(cid,tab); chans[cid]['tabs'][tab]={'listed':len(rows),'err':err,'fetched':0,'crossed_cutoff':False}
        old=0; i=0
        while i<len(rows) and old<6:
            chunk=rows[i:i+8]; i+=8
            with cf.ThreadPoolExecutor(4) as ex: res=list(ex.map(lambda r: meta(r[0]),chunk))
            for (vid,title),m in zip(chunk,res):
                rec=dict(channel_id=cid,video_id=vid,tab=tab,format=fmt,tab_title=title,meta=m,observed_at=T.isoformat())
                fout.write(json.dumps(rec)+'\n'); fout.flush(); chans[cid]['tabs'][tab]['fetched']+=1
                d=pd(m['publishDate']) if m else None
                if d and d<cutoff: old+=1
                elif d: old=0
        chans[cid]['tabs'][tab]['crossed_cutoff']=old>=6
        chans[cid]['tabs'][tab]['exhausted']= i>=len(rows) and old<6
        print(cid,tab,chans[cid]['tabs'][tab],flush=True)
if __name__=='__main__':
    ids=sys.argv[1:]; chans={}
    with open(OUT+'/uploads_raw.jsonl','a') as fout:
        for cid in ids: run(cid,fout,chans)
    json.dump(chans,open(OUT+f'/channels_raw_{ids[0]}.json','w'),indent=1)
