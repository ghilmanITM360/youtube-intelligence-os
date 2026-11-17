import csv,json,collections,hashlib,re,statistics,datetime,zipfile,math
from pathlib import Path
R=Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os');P=R/'research/finance-economics-intelligence';O=Path('/private/tmp/yios-nick-channel-20261023');OUT=O/'package';OUT.mkdir(exist_ok=True)
def read(n): return list(csv.DictReader(open(P/n,encoding='utf-8-sig')))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=[json.loads(l) for l in open(P/'VIDEO_AUDIT_966.jsonl')]; n=[r for r in a if r['identity']['Channel']=='Nick Invests']; ids={r['Video_ID'] for r in n}; byid={r['Video_ID']:r for r in n};u=read('reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv');ub={r['video_id']:r for r in u};tc={r['Video_ID']:r for r in read('TRANSCRIPT_COVERAGE.csv')};master=read('VIDEO_MASTER.csv')
def deep(r):return all(v=='COMPLETE_LIMITED_EVIDENCE' for v in r['statuses'].values())
def number(s):
 try:return float(s)
 except:return None
# Transparent, overlapping title-derived tags; these do not assert transcript topic verification.
TOPICS={
'Housing':r'house|housing|homeowner|\bhome\b|mortgage|\brent\b|renting|real estate',
'Cars and transport':r'\bcar\b|\bcars\b|truck|commut|leasing|lease|pavement',
'Retirement':r'retir|401.?k|401\(k\)|rat race',
'Savings and milestones':r'(everything|life).*(changes|shifts)|what changes|sav(e|es|ing|ings|ed)|net worth|milestone|\$[\d,.]+[km]?\b.*(change|invested)|first.*(million|100|10)|compound|compounding|snowball',
'Investing':r'invest|\bstock|index fund|etfs?|dividend|portfolio|bonds|bitcoin|crypto|s&p|spacex|wealth shift',
'Debt and banking':r'\bdebt\b|loan|credit|bank|bills|financ(e|ing)|paying off|paid off',
'Earnings and work':r'income|paycheck|payday|paid\b|salary|salaries|job|career|promotion|degree|at work|raise|earning',
'Spending and lifestyle':r'buy|buying|spend|consum|habit|worth your money|waste|cheap|rich.*poor|looking poor|look rich|broke|afford|unsexy|stealth|wealthy|wealthier',
'Psychology and social comparison':r'psycholog|mindset|stress|anxiety|treat|friend|neighbor|coworker|seems richer|alone|quiet|gen x|millennial|gen z|financially free|financial freedom',
'Macro and insecurity':r'inflation|crisis|crash|collapse|ww3|world cup|econom|middle class|americ|us debt|warning|panic|impact|coming|wiped out',
'Population and age benchmarks':r'average|stat(s|istic)|by age|year old|your [2345]0|in your [2345]0|behind|compare|on track|top 50|signs.*better',
'Emergency liquidity':r'emergency|having cash|savings accounts|money finally feels safe',
}
PATTERNS={'Dollar amount':r'\$\s?[\d,]','Why opening':r'^why\b','What happens or changes':r'^what (happens|changes)|^how everything changes','Changes after threshold':r'(everything|life).*(changes|shifts)|what changes|milestones?','Warning or trap':r'trap|mistake|avoid|never|broke|poor|crash|collapse|brutal|cruel|wiped|warning','Numbered list':r'^\d+\b|these \d+|the \d+\b','Affordability':r'afford|how much (house|home|car)|salary actually buys','Comparison':r'\bvs\b|\bversus\b|rich vs|buy, lease|renting vs','Average or statistics':r'average|stat(s|istics)|by age|how.*compare','Step or routine':r'step.by.step|routine|payday|every time you get paid','Nobody or hidden gap':r'nobody|no one|hidden|silent|secret|won.t tell|don.t tell','Reaction compilation':r'react|let.s watch|minutes of people','Explicit year':r'2025|2026|2030','Fear headline':r'crash|collapse|crisis|wiped|panic|warning|not ready|brace|implod|impact|coming'}
def tags(t,d):return [k for k,v in d.items() if re.search(v,t,re.I)]
def calc(rows):
 v=[number(r['identity']['Views']) for r in rows];v=[x for x in v if x is not None];rr=[number(r['identity']['Lifetime_rate_ratio']) for r in rows];rr=[x for x in rr if x is not None];c=collections.Counter(r['identity']['Performance_tier'] for r in rows)
 return {'n':len(rows),'mean_views':round(statistics.mean(v),2) if v else None,'median_views':statistics.median(v) if v else None,'median_peer_ratio':round(statistics.median(rr),5) if rr else None,'eligible':len(rr),'strong':c['STRONG'],'typical':c['TYPICAL'],'weak':c['WEAK'],'insufficient':c['INSUFFICIENT_DATA'],'median_age_days':round(statistics.median(float(r['identity']['Age_days']) for r in rows if number(r['identity']['Age_days']) is not None),2) if rows else None,'median_duration_seconds':statistics.median(float(r['identity']['Duration_seconds']) for r in rows if number(r['identity']['Duration_seconds']) is not None) if rows else None}
for r in n:
 r['_topics']=tags(r['identity']['Title'],TOPICS) or ['Other personal finance'];r['_patterns']=tags(r['identity']['Title'],PATTERNS)
vsort=sorted(n,key=lambda r:float(r['identity']['Views']),reverse=True);total=sum(float(r['identity']['Views']) for r in n);outids={r['Video_ID'] for r in vsort[:4]}
summary={'overall':calc(n),'total_views':int(total),'min_views':int(vsort[-1]['identity']['Views']),'max_views':int(vsort[0]['identity']['Views']),'top1_share':float(vsort[0]['identity']['Views'])/total,'top10_share':sum(float(r['identity']['Views']) for r in vsort[:10])/total,'top10pct_share':sum(float(r['identity']['Views']) for r in vsort[:math.ceil(len(n)*.1)])/total,'without_top4':calc([r for r in n if r['Video_ID'] not in outids]),'top4_removed_ids':sorted(outids),'deep':sum(deep(r) for r in n),'script_complete':sum(r['statuses']['SCRIPT_REVIEW']=='COMPLETE_LIMITED_EVIDENCE' for r in n),'image_local':sum(bool(r['thumbnail'].get('image_path')) and (R/r['thumbnail']['image_path']).exists() for r in n),'topics':{},'patterns':{},'periods':{},'duration':{},'age':{},'competitors':{}}
for kind,defs in [('topics',TOPICS),('patterns',PATTERNS)]:
 for key in list(defs)+(['Other personal finance'] if kind=='topics' else []):
  rows=[r for r in n if key in r['_'+kind]]; d=calc(rows);d['without_top4']=calc([r for r in rows if r['Video_ID'] not in outids]);d['best_ids']=[r['Video_ID'] for r in sorted(rows,key=lambda r:float(r['identity']['Lifetime_rate_ratio'] or -1),reverse=True)[:3]];d['weak_ids']=[r['Video_ID'] for r in sorted(rows,key=lambda r:float(r['identity']['Lifetime_rate_ratio'] or 999))[:3]];d['all_ids']=[r['Video_ID'] for r in rows];summary[kind][key]=d
for r in n:
 
 try:t=datetime.datetime.fromisoformat(r['identity']['Published_at_raw'])
 except:continue
 q=f'{t.year}-Q{(t.month-1)//3+1}';summary['periods'].setdefault(q,[]).append(r)
summary['periods']={k:calc(v) for k,v in sorted(summary['periods'].items())}
for label,lo,hi in [('under_15min',0,900),('15_to_20min',900,1200),('20_to_25min',1200,1500),('25_to_30min',1500,1800),('30min_plus',1800,1e9)]:summary['duration'][label]=calc([r for r in n if lo<=float(r['identity']['Duration_seconds'])<hi])
for label,lo,hi in [('under_7days',0,7),('7_to_29days',7,30),('30_to_89days',30,90),('90_to_179days',90,180),('180days_plus',180,1e9)]:summary['age'][label]=calc([r for r in n if number(r['identity']['Age_days']) is not None and lo<=float(r['identity']['Age_days'])<hi])
for name in ['Nick Invests','Lucas Grant','Carl Invests','Brimm.','Primate Economics','Crayon Capital']:
 rows=[r for r in a if r['identity']['Channel']==name];summary['competitors'][name]=calc(rows);summary['competitors'][name]['snapshot_dates']=sorted(set(r['identity']['Metric_snapshot_date'] for r in rows));summary['competitors'][name]['deep']=sum(deep(r) for r in rows)
# CSV full registered population.
fields=['video_id','video_url','channel_id','title','publication_raw','duration_seconds','format','frozen_views','snapshot_date','snapshot_precision','age_days','topic_tags_title_proxy','title_pattern_tags','audit_status','audit_batch','script_review_status','transcript_status','transcript_locator','transcript_sha256','thumbnail_status','thumbnail_path','thumbnail_sha256','source_media_status','individual_audit_reference','evidence_level','peer_tier','peer_ratio','peer_count','peer_ids','population_layer','notes']
rows=[]
for r in n:
 i=r['identity'];th=r['thumbnail'];loc=th.get('image_path','');exists=bool(loc) and (R/loc).exists();lev='A' if deep(r) else 'B' if tc[r['Video_ID']]['Status']=='TEXT_AVAILABLE' else 'C';rows.append(dict(zip(fields,[r['Video_ID'],i['URL'],i['Channel_ID'],i['Title'],i['Published_at_raw'],i['Duration_seconds'],i['Format'],i['Views'],i['Metric_snapshot_date'],i['Snapshot_precision'],i['Age_days'],'|'.join(r['_topics']),'|'.join(r['_patterns']),'DEEP_COMPLETE_LIMITED_EVIDENCE' if deep(r) else 'NOT_DEEP_COMPLETE',r['batch_id'],r['statuses']['SCRIPT_REVIEW'],tc[r['Video_ID']]['Status'],tc[r['Video_ID']]['Evidence_locator'],tc[r['Video_ID']]['Text_SHA256'],'LOCAL_HASH_VERIFIED' if exists and sha(R/loc)==th.get('image_sha256') else 'NOT_VERIFIED',str(R/loc) if exists else '',sha(R/loc) if exists else '', 'NOT_AVAILABLE_REGISTERED_FORENSIC_VIDEO',str(P/'VIDEO_AUDIT_966.jsonl')+'::'+r['Video_ID'],lev,i['Performance_tier'],i['Lifetime_rate_ratio'],i['Peer_count'],i['Peer_Video_IDs'],ub[r['Video_ID']]['population_layer'],'Untimed automatic transcript; original channel completeness unknown; historical thumbnail unknown; topic tags overlap and are lexical proxies'])))
with open(OUT/'NICK_INVESTS_VIDEO_INVENTORY.csv','w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
# Full audit derived evidence to allow review without re-running individual audits.
with open(OUT/'EXISTING_AUDIT_STORYTELLING_MATRIX.csv','w',newline='') as f:
 fields2=['video_id','batch','deep_complete','script_status','script_scope','peer_tier','peer_ratio','opening','analysis','beat_map','ending','claim_audit','thumbnail_analysis','thumbnail_alignment'];w=csv.DictWriter(f,fields2);w.writeheader()
 for r in n:
  s=r['script'];th=r['thumbnail'];w.writerow(dict(zip(fields2,[r['Video_ID'],r['batch_id'],deep(r),r['statuses']['SCRIPT_REVIEW'],s.get('review_scope'),r['identity']['Performance_tier'],r['identity']['Lifetime_rate_ratio'],s.get('opening_words'),s.get('analysis'),json.dumps(s.get('beat_map'),ensure_ascii=False),s.get('ending_words'),json.dumps(s.get('claim_audit'),ensure_ascii=False),th.get('analysis'),th.get('content_correspondence')])))
# Descriptive aggregate matrix includes complete IDs, eligible denominators and outlier sensitivity.
with open(OUT/'NICK_INVESTS_PERFORMANCE_TOPIC_MATRIX.csv','w',newline='') as f:
 fields3=['group_type','group','n','eligible','mean_views','median_views','median_peer_ratio','strong','typical','weak','insufficient','median_age_days','median_duration_seconds','without_top4_n','without_top4_median_views','without_top4_median_peer_ratio','best_ids','weak_ids','all_ids'];w=csv.DictWriter(f,fields3);w.writeheader()
 for kind in ['topics','patterns','periods','duration','age']:
  for k,d in summary[kind].items():
   row={key:d.get(key,'') for key in fields3};row.update(group_type=kind,group=k);row.update({f'without_top4_{key}':d.get('without_top4',{}).get(key,'') for key in ['n','median_views','median_peer_ratio']})
   for key in ['best_ids','weak_ids','all_ids']:row[key]='|'.join(d.get(key,[]))
   w.writerow(row)
summary['checkpoint']={'finance_unique':len({r['video_id'] for r in u}),'original':sum(r['population_layer']=='FROZEN_ORIGINAL_966' for r in u),'expansion':sum(r['population_layer']!='FROZEN_ORIGINAL_966' for r in u),'deep_original':sum(deep(r) for r in a),'remaining_original':sum(not deep(r) for r in a),'remaining_expansion':sum(r['population_layer']!='FROZEN_ORIGINAL_966' and r['audit_status']!='DEEP_AUDIT_COMPLETE' for r in u),'registered_channels':len(read('reconciliation-all-repository-2026-10-21/CHANNEL_DIRECTORY.csv')),'next_untouched_original':next(r['Video_ID'] for r in a if all(r['statuses'][x+'_REVIEW']=='NOT_STARTED' for x in ['TITLE','SCRIPT','THUMBNAIL','TOPIC']))}
summary['population']={'original':len(n),'expansion':sum(r['channel_id']=='UCXzNNA2ngRpRiWvyA7eGd6w' and r['population_layer']!='FROZEN_ORIGINAL_966' for r in u),'level_A':sum(deep(r) for r in n),'level_B':sum(not deep(r) for r in n),'level_C':0,'level_D':0,'formats':dict(collections.Counter(r['identity']['Format'] for r in n)),'unique_transcript_hashes':len({tc[r['Video_ID']]['Text_SHA256'] for r in n}),'publication_min':min(r['identity']['Published_at_raw'] for r in n if r['identity']['Age_days']),'publication_max':max(r['identity']['Published_at_raw'] for r in n)}
(O/'summary.json').write_text(json.dumps(summary,indent=2));(O/'data.json').write_text(json.dumps(n));print(json.dumps({k:v for k,v in summary.items() if k not in ['topics','patterns']},indent=2))
print('TOPICS');[(print(k,{x:d[x] for x in ['n','median_views','median_peer_ratio','strong','weak','best_ids','weak_ids']})) for k,d in summary['topics'].items()]
print('PATTERNS');[(print(k,{x:d[x] for x in ['n','median_views','median_peer_ratio','strong','weak','best_ids','weak_ids']})) for k,d in summary['patterns'].items()]
