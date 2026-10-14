"""Materialize or verify research-only tables; historical canonical masters stay separate."""
import collections,csv,hashlib,json,sys
from pathlib import Path
D=Path(__file__).resolve().parents[1];M=D/'03_MASTER_DATA';write='--write' in sys.argv
if write:M.mkdir(exist_ok=True)
packages=[]
for q in sorted((D/'02_VIDEO_FORENSICS').glob('*/QA.json')):
 if json.loads(q.read_text())['status']=='PASS_STRUCTURAL':packages.append(q.parent)
index={};names=['VISUAL_TIMELINE.csv','ASSET_OBSERVATIONS.csv','MOTION_SEQUENCES.csv','STORY_AND_EDITING_BEATS.csv','AUDIO_VISUAL_EVENTS.csv']
for n in names:
 rows=[];fields=None;counts={}
 for p in packages:
  with (p/n).open() as f:
   z=csv.DictReader(f);current=list(z)
   if fields is None:fields=z.fieldnames
   assert fields==z.fieldnames,(p,n,'schema mismatch')
   rows+=current;counts[p.name]=len(current)
 dest=M/('MASTER_'+n)
 if write:
  with dest.open('w',newline='') as f:z=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');z.writeheader();z.writerows(rows)
 with dest.open() as f:actual=list(csv.DictReader(f))
 canon=lambda rr:collections.Counter(tuple(x[k] for k in fields) for x in rr)
 assert canon(actual)==canon(rows),n
 index[n]={'rows':len(rows),'per_video':counts,'master_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
summary={'scope':'Research-only Big Short and Greece schema; historical six remain in original ten masters, not mixed or duplicated here.','packages':[p.name for p in packages],'tables':index,'total_rows':sum(x['rows'] for x in index.values()),'historical_master_rows_separate':18091}
if write:(M/'RECONCILIATION.json').write_text(json.dumps(summary,indent=2)+'\n')
else:assert json.loads((M/'RECONCILIATION.json').read_text())==summary
s=json.loads((D/'STATUS.json').read_text());assert set(s['new_structural_completed'])=={p.name for p in packages};assert s['structural_total']==len(set(s['historical_structural_completed'])|{p.name for p in packages})
print('PASS research master reconciliation:',len(packages),'packages,',len(names),'tables,',summary['total_rows'],'rows; total structural',s['structural_total'])
