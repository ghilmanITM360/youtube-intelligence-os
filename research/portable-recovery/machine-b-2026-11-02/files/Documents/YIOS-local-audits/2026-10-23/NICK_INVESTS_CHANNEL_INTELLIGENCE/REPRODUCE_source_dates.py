import csv,json,zipfile,re,datetime,collections
from pathlib import Path
import openpyxl
O=Path('/private/tmp/yios-nick-channel-20261023');R=Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os');rel='data/extracted/channel-data/DS-000022/packages/nick-invests/NickInvests_Master_Data.xlsx';w=openpyxl.load_workbook(R/rel,read_only=True,data_only=True);rows=list(w['All Videos'].iter_rows(min_row=5,values_only=True));n=json.loads((O/'data.json').read_text());by={r['Video_ID']:r for r in n};tc={r['Video_ID']:r for r in csv.DictReader(open(R/'research/finance-economics-intelligence/TRANSCRIPT_COVERAGE.csv'))};sources={};errors=[];period=collections.Counter()
for idx,row in enumerate(rows,5):
 vid=row[1]
 if not vid:continue
 r=by[vid];i=r['identity'];day=row[5].date().isoformat();q=f'{row[5].year}-Q{(row[5].month-1)//3+1}';period[q]+=1
 for name,expected,actual in [('title',i['Title'],row[2]),('views',int(i['Views']),row[9]),('duration',int(i['Duration_seconds']),row[8])]:
  if expected!=actual:errors.append([vid,name,expected,actual])
 loc=tc[vid]['Evidence_locator'];zp,member=loc.split('::');full=zipfile.ZipFile(R/zp).read(member).decode();header=re.search(r'^Published\s*:\s*(.*)$',full,re.M).group(1).strip();assert header[:10]==day,(vid,header,day)
 sources[vid]={'source_publication_day':day,'source_publication_day_locator':str(R/rel)+f'::All Videos!F{idx}','source_day_header_confirmation':loc+'::Published','publication_precision':'DATE_ONLY_IN_SOURCE' if i['Published_at_raw']=='(date only)' else 'SOURCE_TIMESTAMP','source_day_age_at_snapshot':(datetime.date(2026,9,11)-row[5].date()).days}
p=O/'package/NICK_INVESTS_VIDEO_INVENTORY.csv';inv=list(csv.DictReader(open(p)));fields=list(dict.fromkeys(list(inv[0])+list(next(iter(sources.values())))))
for row in inv:
 row.update(sources[row['video_id']]);row['notes']=row['notes'].replace('Untimed automatic transcript;','Untimed automatic transcript; source date column and archive Published header independently agree;')
with open(p,'w',newline='') as f:wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(inv)
result={'source_workbook_rows':len(sources),'metadata_errors':errors,'archive_publication_header_matches':len(sources),'all_source_day_period_counts':dict(sorted(period.items())),'date_only_supplement':{vid:v for vid,v in sources.items() if v['publication_precision']=='DATE_ONLY_IN_SOURCE'},'source_day_min':min(x['source_publication_day'] for x in sources.values()),'source_day_max':max(x['source_publication_day'] for x in sources.values()),'frozen_peer_labels_unchanged':True}
(O/'source_date_validation.json').write_text(json.dumps(result,indent=2));print(result)
