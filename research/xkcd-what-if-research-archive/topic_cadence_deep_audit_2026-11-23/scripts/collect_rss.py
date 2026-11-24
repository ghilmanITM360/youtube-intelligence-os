#!/usr/bin/env python3
"""RSS-based collection (works while watch pages are 429-throttled). RSS = 15 newest uploads (all formats) with exact UTC publish time and views.
Format via YouTube tab membership (yt-dlp flat lists of /shorts and /videos, first 80 ids each)."""
import sys,os,json,subprocess,datetime,urllib.request,xml.etree.ElementTree as ET
sys.path.insert(0,os.path.dirname(__file__)); import crawl_uploads as c
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ns={'a':'http://www.w3.org/2005/Atom','m':'http://search.yahoo.com/mrss/','y':'http://www.youtube.com/xml/schemas/2015'}
def ids(cid,tab,n=80):
    p=subprocess.run([c.YTDLP,'--flat-playlist','--no-warnings','--playlist-end',str(n),'--print','%(id)s',f'https://www.youtube.com/channel/{cid}/{tab}'],capture_output=True,text=True)
    return set(p.stdout.split())
out=open(A+'/raw/rss_rows.jsonl','w'); info={}
for cid in [l.strip() for l in open(A+'/raw/channel_ids.txt')]+[l.strip() for l in open(A+'/raw/channel_ids_added.txt')]:
    x=urllib.request.urlopen(urllib.request.Request(f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}',headers={'User-Agent':c.UA}),timeout=30).read()
    obs=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=ET.fromstring(x); sh=ids(cid,'shorts'); lg=ids(cid,'videos')
    subs,nm=c.subs(cid); info[cid]={'name':t.find('a:title',ns).text,'subscribers_text':subs}
    es=t.findall('a:entry',ns)
    for e in es:
        v=e.find('y:videoId',ns).text; st=e.find('m:group/m:community/m:statistics',ns)
        fmt='Short' if v in sh else ('Long' if v in lg else 'Unknown')
        out.write(json.dumps(dict(channel_id=cid,video_id=v,title=e.find('a:title',ns).text,published_utc=e.find('a:published',ns).text,views=st.get('views') if st is not None else None,format=fmt,observed_at=obs,n_entries=len(es)))+'\n')
    print(cid,info[cid],len(es),flush=True)
json.dump(info,open(A+'/raw/rss_channel_info.json','w'),indent=1)
