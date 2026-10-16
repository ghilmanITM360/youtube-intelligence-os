import csv,hashlib,openpyxl
from pathlib import Path
p=Path('research/finance-economics-intelligence');master=list(csv.DictReader((p/'VIDEO_MASTER.csv').open()));out=[]
for r in csv.DictReader(open('data/manifests/DS-000022_SOURCE_ARTIFACTS.csv')):
 if r['file_type']!='XLSX' or r['channel'] not in ['Carl Invests','Lucas Grant','Nick Invests','Bob Invests']:continue
 path=Path(r['repository_source_path']);before=hashlib.sha256(path.read_bytes()).hexdigest();assert before==r['sha256']
 w=openpyxl.load_workbook(path,read_only=True,data_only=True);statement=w['Channel Overview']['A2'].value
 assert 'Scraped 11 Sep 2026' in statement
 values=list(w['All Videos'].values);headers=values[3];source={x[1]:dict(zip(headers,x)) for x in values[4:] if x[1]}
 selected=[x for x in master if x['Channel']==r['channel']];assert set(source)=={x['Video_ID'] for x in selected}
 for x in selected:
  s=source[x['Video_ID']];assert (int(x['Views']) if x['Views'] else None)==(None if s['Views']=='N/A' else s['Views']);assert x['Title']==s['Title'];assert x['Published_at_raw']==s['Published (UTC)'],(x['Video_ID'],x['Published_at_raw'],s['Published (UTC)'])
 out.append(dict(Channel_ID=selected[0]['Channel_ID'],Channel=r['channel'],Dataset='DS-000022',Metric_snapshot_date='2026-09-11',Snapshot_precision='SOURCE_DECLARED_SCRAPE_DAY_TIMEZONE_UNKNOWN',Source_path=str(path),Source_SHA256=before,Source_cell='Channel Overview!A2',Exact_statement=statement,Verified_video_rows=len(selected),Verified_fields='Video_ID|Title|Views|Published_at_raw',Limit='User-provided formatted export; underlying original Actor run unavailable; day precision only'))
 w.close();assert hashlib.sha256(path.read_bytes()).hexdigest()==before
with (p/'METRIC_DATE_EVIDENCE.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]),lineterminator='\n');w.writeheader();w.writerows(out)
print('Verified source dates and metadata:',sum(x['Verified_video_rows'] for x in out))
