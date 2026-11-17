import pandas as pd,urllib.request,os,concurrent.futures as cf
v=pd.read_pickle('out/videos_feat.pkl')
def one(r):
    vid,url=r
    out={'video_id':vid}
    try:
        req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Mozilla/5.0'}); 
        with urllib.request.urlopen(req,timeout=20) as x: out['recorded_url_status']=x.status; out['recorded_url_bytes']=x.headers.get('Content-Length')
    except Exception as e: out['recorded_url_status']=getattr(e,'code',str(e)[:40])
    p=f'thumbs/{vid}.jpg'
    if not os.path.exists(p):
        try:
            req=urllib.request.Request(f'https://i.ytimg.com/vi/{vid}/mqdefault.jpg',headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=20) as x: open(p,'wb').write(x.read())
        except Exception as e: out['dl_err']=getattr(e,'code',str(e)[:40])
    out['dl_ok']=os.path.exists(p); return out
with cf.ThreadPoolExecutor(10) as ex: R=list(ex.map(one,zip(v.video_id,v.thumbnail_url)))
pd.DataFrame(R).to_csv('out/thumbnail_accessibility.csv',index=False)
print(pd.DataFrame(R).recorded_url_status.value_counts(), pd.DataFrame(R).dl_ok.value_counts())
