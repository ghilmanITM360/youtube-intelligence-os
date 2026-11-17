import pathlib,json,csv,subprocess,hashlib,io
from openpyxl import load_workbook
R=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';O=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-NICK_170');V='ULkTn-jHBBc';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=[json.loads(s) for s in subprocess.check_output(['git','show','8fa0fe28f0870b2717d08a4099e1c4425a66429c:research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl'],cwd=R,text=True).splitlines()];new=[json.loads(s) for s in (B/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()];assert len(old)==len(new)==966;assert [a['Video_ID'] for a,z in zip(old,new) if a!=z]==[V]
assert {x['Video_ID'] for x in new}=={x['Video_ID'] for x in csv.DictReader((B/'audit-baseline/VIDEO_IDS.csv').open())}
frozen=json.loads((B/'audit-baseline/MANIFEST.json').read_text());assert len(frozen['source_hashes'])==26
for p,d in frozen['source_hashes'].items():assert sha(R/p)==d,p
for filename in ['VIDEO_AUDIT_966.csv','VIDEO_COMPLETION_MATRIX.csv','SCRIPT_ANALYSIS_966.csv','THUMBNAIL_ANALYSIS_966.csv','TITLE_ANALYSIS_966.csv','TOPIC_ANALYSIS_966.csv','VIRALITY_INTELLIGENCE_966.csv']:
 a=list(csv.DictReader(io.StringIO(subprocess.check_output(['git','show','8fa0fe28f0870b2717d08a4099e1c4425a66429c:'+str((B/filename).relative_to(R))],cwd=R,text=True))));z=list(csv.DictReader((B/filename).open()));assert [x['Video_ID'] for x,y in zip(a,z) if x!=y]==[V],filename
payload=json.loads(subprocess.check_output([str(R/'.venv/bin/python'),str(B/'build_combined_workbook_data.py')],text=True));assert len(payload['all_videos'])==1612;assert len({x['video_id'] for x in payload['all_videos']})==1612
exp=[x for x in payload['all_videos'] if x['population_layer']!='FROZEN_ORIGINAL_966'];assert len(exp)==646 and not any(x['audit_status']=='DEEP_AUDIT_COMPLETE' for x in exp)
# The expansion/universe source bytes must equal accepted Git checkpoint.
for rel in ['expansion-12-channel-2026-10-20/EXPANSION_AUDIT_197.jsonl','expansion-monkey-explains-1999-2026-10-21/EXPANSION_AUDIT_63.jsonl','reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv']:
 p=B/rel
 if p.exists():assert p.read_bytes()==subprocess.check_output(['git','show','8fa0fe28f0870b2717d08a4099e1c4425a66429c:'+str(p.relative_to(R))],cwd=R)
w=load_workbook(B/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx',read_only=True,data_only=True);assert w.sheetnames==['Combined Dashboard','All Finance Videos','Channel Directory','Detailed Research'];assert [w.worksheets[0].cell(i,2).value for i in range(5,10)]==[1612,446,1166,27,42]
allrows=list(w['All Finance Videos'].iter_rows(min_row=5,values_only=True));assert len(allrows)==1612 and len({x[0] for x in allrows})==1612;assert sum(x[26]=='DEEP_AUDIT_COMPLETE' for x in allrows)==446
by={r['Video_ID']:r for r in new};detail=list(w['Detailed Research'].iter_rows(min_row=5,values_only=True));assert len(detail)==966
for cells in detail:
 source=by[cells[0]];assert json.loads(cells[15])==source['statuses']
 for col,section in zip(range(16,24),['title','thumbnail','script','topic','performance','virality','event','private_metrics']):assert json.loads(cells[col])==source[section],(cells[0],section)
error_strings={'#REF!','#DIV/0!','#VALUE!','#NAME?','#N/A','#NUM!','#NULL!','#SPILL!','#CALC!'};maxlen=0
for sheet in w:
 for row in sheet.iter_rows():
  for c in row:
   v=c.value
   if isinstance(v,str):
    assert '[object Object]' not in v,(sheet.title,c.coordinate);assert v not in error_strings,(sheet.title,c.coordinate);maxlen=max(maxlen,len(v));assert len(v)<=32767
   assert c.data_type!='e',(sheet.title,c.coordinate)
target_detail_row=next(i+5 for i,x in enumerate(detail) if x[0]==V);w.close()
# New packet must contain no authoring placeholders. Existing incomplete universe retains honest PENDING values.
for p in [B/'audit-batches/NICK_170.json',B/'audit-batches/NICK_170_READ_RECEIPTS.json']:
 raw=p.read_text();assert not any(v in raw for v in ['TODO','TBD','[object Object]','INSERT_HERE'])
report={'source_fingerprints':'26/26 PASS','original_ids':'966/966 preserved','expansions':'646 identities/metadata-only preserved','combined_unique_ids':1612,'jsonl_changed_video_ids':[V],'projection_changed_rows':'exactly one target row in each of seven CSVs','completed':446,'remaining':1166,'pending_originals':520,'pending_expansions':646,'registered_channels':42,'workbook_sheets':4,'workbook_jsonl_section_consistency':'966 rows x8 sections PASS','formula_errors_and_object_placeholders':0,'max_cell_characters':maxlen,'target_detailed_research_excel_row':target_detail_row,'ledger_sha256':sha(B/'VIDEO_AUDIT_966.jsonl'),'workbook_sha256':sha(B/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'),'audit_sha256':sha(B/'audit-batches/NICK_170.json'),'receipt_sha256':sha(B/'audit-batches/NICK_170_READ_RECEIPTS.json'),'native_excel_recalculation':'NOT_TESTED','full_regression':'SEE_CURRENT_FULL_PYTEST_LOG;PRE_EXISTING_DS000028_F020_TRACKED_SEPARATELY'}
(O/'final-integrity.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
