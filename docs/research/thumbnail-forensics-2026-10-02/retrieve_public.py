"""Resume zero-spend public evidence acquisition; never marks visual inspection."""
import concurrent.futures, csv, json, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from acquire_registered_thumbnails import fetch_registered
u=json.loads((OUT/'thumbnail-universe.json').read_text())
log=OUT/'public-retrieval.jsonl'
prior=[json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
done={r['youtube_video_id'] for r in prior}
queue=[r for r in u if r['classification']=='URL_ONLY_THUMBNAIL' and r['youtube_video_id'] not in done and r.get('mapping_confidence')=='EXACT_YOUTUBE_VIDEO_ID']
def fetch(r):
 urls=r.get('all_thumbnail_urls') or [r['thumbnail_url']]
 hosts={urlparse(x).hostname for x in urls}
 attempts=[]
 for url in urls:
  rec=dict(video_id=r.get('video_id') or r['youtube_video_id'],format=r.get('format','UNKNOWN'),dataset_id=r.get('source_dataset') or 'catalogued-public',url_recorded_at='',title=r.get('title',''),title_observed_at=r.get('metrics_observed_at',''),thumbnail_url=url)
  result=fetch_registered(rec,set(urls),hosts,OUT/'public-current',datetime.now(timezone.utc).isoformat(),set(),attempts=1)
  attempts.append(result)
  if result.get('sha256'): break
 return dict(youtube_video_id=r['youtube_video_id'],reference_Thumbnail_ID=r['Thumbnail_ID'],attempts=attempts,success=bool(result.get('sha256')),snapshot=result)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool, log.open('a') as f:
 for i,res in enumerate(pool.map(fetch,queue),1):
  f.write(json.dumps(res,ensure_ascii=False)+'\n');f.flush()
  if i%50==0:print(f'{i}/{len(queue)} saved',flush=True)
print('Acquisition complete; visual inspection remains pending.',flush=True)
