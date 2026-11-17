"""Bounded public YouTube page capture; no API, credentials, or pagination."""
import csv
import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE=Path(__file__).resolve().parent
HANDLES=['MoneyMacro','HowMoneyWorks','Pensioncraft','PBoyle','EconomicsExplained','ModernMBA']


def walk(value):
    if isinstance(value,dict):
        yield value
        for item in value.values(): yield from walk(item)
    elif isinstance(value,list):
        for item in value: yield from walk(item)


def text(value):
    if not isinstance(value,dict): return ''
    return value.get('simpleText') or ''.join(x.get('text','') for x in value.get('runs',[]))


def main():
    target=BASE/'landscape-evidence';target.mkdir(exist_ok=True)
    channels=[];videos=[]
    for handle in HANDLES:
        saved=target/(handle+'-videos-v2.json')
        if saved.exists(): record=json.loads(saved.read_text())
        else:
            url='https://www.youtube.com/@'+handle+'/videos?hl=en'
            record={'url':url,'retrieved_at':datetime.now(timezone.utc).isoformat(),'status':'UNAVAILABLE','videos':[]}
            try:
                req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
                with urllib.request.urlopen(req,timeout=25) as response: payload=response.read()
                match=re.search(r'var ytInitialData = (.*?);</script>',payload.decode())
                if not match: raise ValueError('No public initial data')
                data=json.loads(match[1]);meta=data.get('metadata',{}).get('channelMetadataRenderer',{})
                record.update({'status':'PUBLIC_FIRST_PAGE_ONLY','page_sha256':hashlib.sha256(payload).hexdigest(),
                    'channel_id':meta.get('externalId',''),'name':meta.get('title',''),'description':meta.get('description',''),
                    'keywords':meta.get('keywords',''),'channel_url':meta.get('channelUrl','')})
                seen=set()
                for node in walk(data.get('contents',{})):
                    lock=node.get('lockupViewModel')
                    if lock and lock.get('contentType')=='LOCKUP_CONTENT_TYPE_VIDEO':
                        ident=lock.get('contentId')
                        if ident in seen: continue
                        seen.add(ident)
                        metadata=lock.get('metadata',{}).get('lockupMetadataViewModel',{})
                        parts=[p.get('text',{}).get('content','') for row in metadata.get('metadata',{}).get('contentMetadataViewModel',{}).get('metadataRows',[]) for p in row.get('metadataParts',[])]
                        thumb=lock.get('contentImage',{}).get('thumbnailViewModel',{})
                        badges=[n['thumbnailBadgeViewModel'].get('text','') for n in walk(thumb.get('overlays',[])) if 'thumbnailBadgeViewModel' in n]
                        record['videos'].append({'video_id':ident,'title':metadata.get('title',{}).get('content',''),
                            'views_display':parts[0] if parts else '', 'published_relative':parts[1] if len(parts)>1 else '',
                            'duration_display':badges[0] if badges else '', 'thumbnail_urls':thumb.get('image',{}).get('sources',[])})
                    v=node.get('videoRenderer')
                    if not v or v.get('videoId') in seen:continue
                    seen.add(v.get('videoId'))
                    record['videos'].append({'video_id':v.get('videoId'),'title':text(v.get('title')),
                        'views_display':text(v.get('viewCountText')),'published_relative':text(v.get('publishedTimeText')),
                        'duration_display':text(v.get('lengthText')),'thumbnail_urls':v.get('thumbnail',{}).get('thumbnails',[])})
            except Exception as exc:record['error']=type(exc).__name__+': '+str(exc)[:160]
            saved.write_text(json.dumps(record,indent=2)+'\n')
        channels.append({'Handle':handle,'Channel_ID':record.get('channel_id',''),'Name':record.get('name',''),
            'Depth':'TIER_B_FIRST_PAGE' if record['videos'] else 'TIER_C_ACCESS_GAP','URL':record['url'],
            'Retrieved_at':record['retrieved_at'],'Visible_videos':len(record['videos']),
            'Status':record['status'],'Growth':'UNKNOWN_SINGLE_SNAPSHOT','Evidence':str(saved.relative_to(BASE))})
        for v in record['videos']:
            videos.append(dict(Channel_ID=record.get('channel_id',''),Channel=record.get('name',''),
                Video_ID=v['video_id'],Title=v['title'],Views_display=v['views_display'],Published_relative=v['published_relative'],
                Duration_display=v['duration_display'],Format_basis='VIDEOS_TAB',Snapshot=record['retrieved_at'],
                Performance_tier='INSUFFICIENT_DATA',Evidence=str(saved.relative_to(BASE))))
    for name,rows in [('LANDSCAPE_CHANNELS.csv',channels),('LANDSCAPE_VIDEOS.csv',videos)]:
        if rows:
            with (BASE/name).open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    print(json.dumps(channels,indent=2))


if __name__=='__main__':main()
