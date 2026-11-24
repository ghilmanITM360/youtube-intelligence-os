#!/usr/bin/env python3
"""Merge watch-page publish date/views into TOPIC_RESEARCH_EVIDENCE.csv (from raw/search_hits_meta.jsonl, from raw/pre_meta backup so it is idempotent)."""
import csv,json,os,datetime as dt,statistics as st,collections
A=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
meta={}
for l in open(A+'/raw/search_hits_meta.jsonl'):
    r=json.loads(l)
    if r['meta'] and r['meta'].get('publishDate'): meta[r['video_id']]=r
rows=list(csv.DictReader(open(A+'/raw/TOPIC_RESEARCH_EVIDENCE.pre_meta.csv')))
T=dt.datetime.fromisoformat('2026-11-23T21:33:37+05:00')
fn=list(rows[0].keys())+['views_lifetime_at_fetch','views_fetched_at_utc','age_days_at_fetch','duration_s','format_hint','metadata_status']
for r in rows:
    v=r['result_url'].split('v=')[-1]; x=meta.get(v)
    if x:
        m=x['meta']; d=dt.datetime.fromisoformat(m['publishDate']); fa=dt.datetime.fromisoformat(x['fetched_at'])
        r['publish_time']=m['publishDate']; r['views']=m.get('viewCount') or 'UNAVAILABLE'; r['views_lifetime_at_fetch']=r['views']; r['views_fetched_at_utc']=x['fetched_at']
        r['age_days_at_fetch']=f"{(fa-d).total_seconds()/86400:.1f}"; r['duration_s']=m.get('lengthSeconds') or ''
        r['format_hint']='isShortsEligible=%s (YouTube flag; not a format classification)'%m.get('isShortsEligible'); r['metadata_status']='OBSERVED (watch-page player response)'
        r['window_basis']=r['window_basis'].split(';')[0].replace('publish date NOT independently verified (watch page fetch was HTTP 429-throttled)','')+'; publish date and views now read from watch page (exact time with offset)'
        r['evidence_quality']='A-: first-party public page; search rank/filter = YouTube-attributed'
    else:
        r.update(views_lifetime_at_fetch='UNAVAILABLE',views_fetched_at_utc='',age_days_at_fetch='',duration_s='',format_hint='',metadata_status='UNAVAILABLE (watch page failed/removed)')
with open(A+'/TOPIC_RESEARCH_EVIDENCE.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fn); w.writeheader(); w.writerows(rows)
# per-topic descriptive stats, unique videos only
by=collections.defaultdict(dict)
for r in rows:
    if r['metadata_status'].startswith('OBSERVED'): by[r['topic_id']][r['result_url']]=r
out=['topic_id,unique_videos_with_metadata,published_last_30d,published_last_90d,median_age_days,median_lifetime_views,max_lifetime_views,median_views_for_last_90d_uploads']
for t,d in sorted(by.items()):
    a=[float(x['age_days_at_fetch']) for x in d.values()]; v=[int(x['views']) for x in d.values() if x['views'].isdigit()]
    r90=[int(x['views']) for x in d.values() if float(x['age_days_at_fetch'])<=90 and x['views'].isdigit()]
    out.append(f"{t},{len(d)},{sum(1 for x in a if x<=30)},{sum(1 for x in a if x<=90)},{st.median(a):.0f},{st.median(v) if v else ''},{max(v) if v else ''},{st.median(r90) if r90 else ''}")
open(A+'/TOPIC_SEARCH_SATURATION_STATS.csv','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
print('rows',len(rows),'with meta',sum(1 for r in rows if r['metadata_status'].startswith('OBSERVED')))
