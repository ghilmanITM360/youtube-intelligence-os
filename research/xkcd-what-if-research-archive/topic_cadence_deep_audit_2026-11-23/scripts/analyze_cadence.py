#!/usr/bin/env python3
"""UPLOAD_INVENTORY.csv + CHANNEL_UPLOAD_CADENCE.csv from (a) deep watch-page crawl rows (exact timestamps; crawl partly killed by HTTP 429) and (b) RSS 15-newest rows.
T (observation) = first RSS observation time. Window = (T-N d, T]  (lower exclusive, upper inclusive). Day for bursts = Asia/Karachi calendar date."""
import json,csv,glob,os,statistics as st,datetime as dt,collections
A=os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-23-what-if-topic-cadence-deep-audit')
PKT=dt.timezone(dt.timedelta(hours=5)); UTC=dt.timezone.utc
rss=[json.loads(l) for l in open(A+'/raw/rss_rows.jsonl')]
T=min(dt.datetime.fromisoformat(r['observed_at']) for r in rss)
info=json.load(open(A+'/raw/rss_channel_info.json')); subs=json.load(open(A+'/raw/subs_search.json'))
CORE={'UC6IxnFzHofFJ5X2PycSMsww','UCphTF9wHwhCt-BzIq-s4V-g','UCESitBa9MCU0T8h6moQe6SQ','UCdiuNtuJid5x40JU58RP6jQ'}
deepchan={}
for f in glob.glob(A+'/raw/channels_raw_*.json'): deepchan.update(json.load(open(f)))
deep={}
for l in open(A+'/raw/uploads_raw.jsonl'):
    r=json.loads(l)
    if r['meta'] and r['meta'].get('publishDate'): deep[(r['channel_id'],r['video_id'])]=r
inv={}
for (cid,v),r in deep.items():
    m=r['meta']; d=dt.datetime.fromisoformat(m['publishDate'])
    inv[(cid,v)]=dict(channel_id=cid,video_id=v,title=m.get('title') or r['tab_title'],format={'videos':'Long','shorts':'Short','streams':'Live'}[r['tab']],classification_method='YouTube channel tab: '+r['tab'],
        published_at=d.isoformat(),duration_s=m.get('lengthSeconds') or '',views=m.get('viewCount') or '',source='watch-page microformat (exact, with offset)',view_observed_at=r['observed_at'])
for r in rss:
    k=(r['channel_id'],r['video_id'])
    if k in inv:
        inv[k]['also_in_rss']='yes'; 
        d1=dt.datetime.fromisoformat(inv[k]['published_at']).astimezone(UTC); d2=dt.datetime.fromisoformat(r['published_utc'])
        inv[k]['rss_vs_watchpage_time_match']='match' if abs((d1-d2).total_seconds())<2 else f'DIFF {(d1-d2).total_seconds()}s'
        continue
    inv[k]=dict(channel_id=r['channel_id'],video_id=r['video_id'],title=r['title'],format=r['format'],classification_method='YouTube tab membership (first 80 of /shorts and /videos) ; Unknown if in neither',
        published_at=r['published_utc'],duration_s='',views=r['views'] or '',source='YouTube RSS feed (exact UTC time)',view_observed_at=r['observed_at'])
rows=[]
for k,v in inv.items():
    d=dt.datetime.fromisoformat(v['published_at'])
    v['channel']=info[k[0]]['name']; v['url']=f'https://www.youtube.com/watch?v={k[1]}'; v['published_pkt_date']=d.astimezone(PKT).date().isoformat(); v['published_utc']=d.astimezone(UTC).isoformat()
    v['evidence_quality']='A: first-party public page, exact timestamp'
    rows.append(v)
fn=['channel_id','channel','video_id','url','title','format','classification_method','published_at','published_utc','published_pkt_date','duration_s','views','view_observed_at','source','also_in_rss','rss_vs_watchpage_time_match','evidence_quality']
with open(A+'/UPLOAD_INVENTORY.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fn,extrasaction='ignore'); w.writeheader(); w.writerows(sorted(rows,key=lambda r:(r['channel'],r['published_utc']),reverse=False))
print('inventory rows',len(rows),'unique keys',len(inv),'rss/watch time mismatches',sum(1 for r in rows if str(r.get('rss_vs_watchpage_time_match','')).startswith('DIFF')),'matches',sum(1 for r in rows if r.get('rss_vs_watchpage_time_match')=='match'))
W=[7,30,90,180,365]
goodcnt=collections.Counter((cid,r['tab']) for (cid,v),r in deep.items())
# overlay tab status from throttle-aware resume crawl logs (original channels_raw tab status came from the 429-damaged crawl)
import re,ast
for lf in sorted(glob.glob(A+'/raw/crawl_resume_run*.log')):
    for l in open(lf):
        m=re.match(r"(\S+) (videos|shorts) (\{.*\})",l.strip())
        if not m: continue
        cid,tab,d=m.group(1),m.group(2),ast.literal_eval(m.group(3))
        if d.get('throttled'): continue
        deepchan.setdefault(cid,{}).setdefault('tabs',{})[tab]=dict(listed=d['listed'],fetched=max(goodcnt[(cid,tab)],1),crossed_cutoff=d['crossed_cutoff'],exhausted=d['exhausted'],cutoff_days=d['cutoff_days'])
rss_oldest={}
for r in rss: rss_oldest[r['channel_id']]=min(rss_oldest.get(r['channel_id'],dt.datetime.max.replace(tzinfo=UTC)),dt.datetime.fromisoformat(r['published_utc']))
def cov(cid,fmt,N):
    lo=T-dt.timedelta(days=N)
    tabs=deepchan.get(cid,{}).get('tabs')
    tabname='videos' if fmt=='Long' else 'shorts'
    if tabs and fmt in('Long','Short') and goodcnt[(cid,tabname)]>=0.9*tabs[tabname]['fetched'] and tabs[tabname]['fetched']>0 or (tabs and fmt in('Long','Short') and tabs[tabname]['listed']==0):
        t=tabs[tabname]; cut=t.get('cutoff_days') or (365 if cid in CORE else 180)
        if t['listed']==0: return 'Complete (tab empty)'
        if t.get('exhausted'): return 'Complete (full public tab listing)'
        if t.get('crossed_cutoff') and N<=cut: return 'Complete for window (deep crawl crossed cutoff)'
        return 'Lower bound'
    if fmt=='Live': return 'UNKNOWN (live/premiere tab not collected)'
    return 'Complete for window (RSS reaches before window start)' if rss_oldest[cid]<=lo else 'Lower bound (RSS=15 newest only)'
by=collections.defaultdict(list)
for r in rows: by[(r['channel_id'],r['format'])].append(r)
out=[]
for cid,cm in info.items():
    for fmt in('Long','Short','Unknown'):
        rs=sorted(by.get((cid,fmt),[]),key=lambda r:r['published_utc'],reverse=True)
        for N in W:
            lo=T-dt.timedelta(days=N); inw=[r for r in rs if lo<dt.datetime.fromisoformat(r['published_utc'])<=T]
            c=cov(cid,fmt,N) if fmt!='Unknown' else 'n/a'
            ds=[dt.datetime.fromisoformat(r['published_utc']) for r in inw]
            gaps=[(a-b).total_seconds()/86400 for a,b in zip(ds,ds[1:])]
            days=collections.Counter(d.astimezone(PKT).date() for d in ds)
            vs=[int(r['views']) for r in inw if str(r['views']).isdigit()]
            out.append(dict(channel=cm['name'],channel_id=cid,subscribers_search_snapshot=subs.get(cid,'UNAVAILABLE'),format=fmt,window_days=N,window_start_exclusive_pkt=lo.astimezone(PKT).isoformat(timespec='minutes'),
              window_end_inclusive_pkt=T.astimezone(PKT).isoformat(timespec='minutes'),count_observed=len(inw),coverage=c,per_week=round(len(inw)/(N/7),2),per_30d=round(len(inw)/(N/30),2),
              median_gap_days=round(st.median(gaps),2) if len(gaps)>=2 else '',min_gap_days=round(min(gaps),2) if gaps else '',max_gap_days=round(max(gaps),2) if gaps else '',
              same_day_burst_days=sum(1 for v in days.values() if v>1),max_same_day=max(days.values()) if days else 0,median_lifetime_views_in_window=int(st.median(vs)) if vs else ''))
with open(A+'/CHANNEL_UPLOAD_CADENCE.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print('cadence rows',len(out),'T=',T.astimezone(PKT).isoformat())
