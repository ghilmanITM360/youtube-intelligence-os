from audit import *
from data_audit import blob,tree,F
from openpyxl import load_workbook
import io,zipfile
def main():
 summary=[]
 for ref,label in [('origin/research/finance-economics-intelligence','canonical'),('origin/codex/finance-machine-a-owner-directed','machine-a-published')]:
  source=git('show',ref+':'+F+'VIDEO_AUDIT_966.jsonl');by={r['Video_ID']:r for r in map(json.loads,source.splitlines())};raw=run(['git','show',ref+':'+F+'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'],raw=True)['stdout']
  wb=load_workbook(io.BytesIO(raw),read_only=True,data_only=False);allrows=list(wb['All Finance Videos'].iter_rows(min_row=5,values_only=True));allrows=[r for r in allrows if r and r[0]];details=list(wb['Detailed Research'].iter_rows(min_row=5,values_only=True));details=[r for r in details if r and r[0]];channels=[r for r in wb['Channel Directory'].iter_rows(min_row=5,values_only=True) if r and r[0]]
  mismatches=[];badjson=[];truncated=[];formulas=0;errors=[]
  for row in allrows:
   if row[0] not in by:continue
   r=by[row[0]]
   for i,key in [(20,'TITLE_REVIEW'),(21,'THUMBNAIL_REVIEW'),(22,'SCRIPT_REVIEW'),(23,'TOPIC_REVIEW'),(24,'PERFORMANCE_REVIEW'),(25,'VIRALITY_REVIEW')]:
    if row[i]!=r['statuses'][key]:mismatches.append({'video':row[0],'dimension':key})
  detailfields={15:'statuses',16:'title',17:'thumbnail',18:'script',19:'topic',20:'performance',21:'virality',22:'event',23:'private_metrics'}
  for row in details:
   for i,key in detailfields.items():
    try:
     d=json.loads(row[i])
     if d!=by[row[0]][key]:mismatches.append({'video':row[0],'detail_field':key,'kind':'JSON_VALUE_DIFFERS'})
    except Exception:
     badjson.append({'video':row[0],'field':key,'characters':len(str(row[i])),'reason':'WORKBOOK_CELL_NOT_VALID_JSON'})
  for ws in wb:
   for row in ws.iter_rows():
    for c in row:
     if c.data_type=='f':formulas+=1
     if c.data_type=='e':errors.append({'sheet':ws.title,'cell':c.coordinate,'error_type':str(c.value)})
  universe=list(csv.DictReader(io.StringIO(git('show',ref+':'+F+'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv'))))
  cached=load_workbook(io.BytesIO(raw),read_only=True,data_only=True)
  dashboard={coord:cached['Combined Dashboard'][coord].value for coord in ['B5','B6','B7','B8','B9']}
  d={'label':label,'ref':ref,'sha':git('rev-parse',ref),'workbook_sha256':hashlib.sha256(raw).hexdigest(),'zip_integrity':zipfile.ZipFile(io.BytesIO(raw)).testzip(),'sheets':wb.sheetnames,'all_video_rows':len(allrows),'all_unique_video_ids':len({r[0] for r in allrows}),'accepted_workbook_rows':sum(r[26]=='DEEP_AUDIT_COMPLETE' for r in allrows),'detail_rows':len(details),'channel_directory_rows':len(channels),'formula_count':formulas,'error_type_cells':errors,'detail_or_status_mismatches':mismatches,'unparseable_detail_json_cells':badjson,'dashboard_cached_values':dashboard,'universe_csv_audit_status':dict(Counter(r['audit_status'] for r in universe)),'native_excel_recalculation':'NOT_TESTED','semantics':'Formula strings inspected and cached numeric values recorded; not a native Excel recalculation.'}
  summary.append(d)
 write('workbook_reconciliation.json',summary)
 # All tracked current-checkout workbooks: physical files and sheet row structure.
 inventory=[];seen={}
 for p in pathlist(['ls-files','-z'],ROOT):
  f=ROOT/p
  if f.suffix.lower() not in ['.xlsx','.xls'] or not f.is_file():continue
  h=sha(f);d={'path':str(f),'sha256':h,'bytes':f.stat().st_size}
  try:
   if h not in seen:
    w=load_workbook(f,read_only=True,data_only=False);sheets=[]
    for ws in w:
     occupied=sum(any(v is not None for v in row) for row in ws.iter_rows(values_only=True))
     sheets.append({'sheet':ws.title,'nonempty_rows_including_headers':occupied,'declared_max_row':ws.max_row,'declared_max_column':ws.max_column})
    seen[h]=sheets;w.close()
   d['sheets']=seen[h]
  except Exception as e:d['error']=type(e).__name__+': '+str(e)
  inventory.append(d)
 csvout('current_workbooks.csv',inventory)
 print(json.dumps([{'label':d['label'],'rows':d['all_video_rows'],'accepted':d['accepted_workbook_rows'],'mismatches':len(d['detail_or_status_mismatches']),'unparseable_detail_json_cells':len(d['unparseable_detail_json_cells']),'formula_error_cells':len(d['error_type_cells']),'universe_csv':d['universe_csv_audit_status']} for d in summary],indent=2));print('tracked workbooks',len(inventory),'unique hashes',len(seen))
if __name__=='__main__':main()
