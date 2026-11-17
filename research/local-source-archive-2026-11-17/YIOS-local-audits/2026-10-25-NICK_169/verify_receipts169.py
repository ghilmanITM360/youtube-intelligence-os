from pathlib import Path
import json,hashlib,subprocess,io,math
from openpyxl import load_workbook
R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';O=Path(__file__).parent;P='2bbc0a74c1f149c21168657c6e2209bd9e681101';V='Tg_n8zGC7qw';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((B/'audit-batches/NICK_169_READ_RECEIPTS.json').read_text());s=(O/'canonical-transcript.txt').read_text();rr=r['receipts'][0]
assert rr['Text_SHA256']==sha(O/'canonical-transcript.txt');assert rr['character_count']==len(s)==19509
assert len(r['financial_claim_locations'])==40;ids={x['source_id'] for x in r['primary_source_receipts']};assert len(ids)==13
for c in r['financial_claim_locations']:
 assert c['original_quote']==s[c['start_char']:c['end_char']]
 assert set(c['source_ids'])<=ids
cursor=0
for a,b in rr['read_character_ranges']:assert a==cursor and b>a;cursor=b
assert cursor==len(s)
for source in r['primary_source_receipts']:
 assert source['publication_applicability'] in ['AVAILABLE_AT_VIDEO_PUBLICATION','LATER_RETROSPECTIVE_EVIDENCE','CURRENT_GUIDANCE_WITH_UNVERIFIED_HISTORICAL_VINTAGE','UNVERIFIED_OR_UNAVAILABLE']
 if 'saved_source_path' in source:assert sha(Path(source['saved_source_path']))==source['saved_source_sha256']
calcs=r['calculation_receipts'];assert len(calcs)==9
# Independent recurrence checks, distinct from closed-form receipt generation.
for key,c in calcs[3]['results'].items():
 a,tail=key.split('_to');f,y=tail.split('_');y=int(y[:-5]);p=float(a);target=float(f);i=1.08**(1/12)-1
 for k in range(12*y):p=p*(1+i)+c
 assert abs(p-target)<1e-5,(key,p,target)
p=200000
for k in range(14):p+=p*.08
assert abs(p-calcs[4]['results']['FV_at49'])<1e-7
assert abs(25/130*100-calcs[5]['results']['arithmetic_percent'])<1e-10
assert abs(429800/5-calcs[6]['results']['downpayments'][0])<1e-7
for t in calcs[2]['results'].values():assert t>0
old=subprocess.check_output(['git','show',P+':.gitattributes'],cwd=R);actual=(R/'.gitattributes').read_bytes();assert old==actual
f=json.loads(Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_168/full-regression-baseline-failure.json').read_text());f.update(accepted_parent=P,unchanged_from_parent=True,bytes=len(actual),sha256=sha(R/'.gitattributes'),full_pytest_this_session='SEE_FULL_PYTEST_LOG')
(O/'full-regression-baseline-failure.json').write_text(json.dumps(f,indent=2)+'\n')
a=load_workbook(io.BytesIO(subprocess.check_output(['git','show',P+':research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx'],cwd=R)),data_only=False);z=load_workbook(B/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx',data_only=False);diff={};style=[]
for x,y in zip(a,z):
 assert x.title==y.title and x.max_row==y.max_row and x.max_column==y.max_column
 ds=[]
 for row1,row2 in zip(x,y):
  for c,d in zip(row1,row2):
   if c.value!=d.value:ds.append(c.coordinate)
   if c._style!=d._style:style.append((x.title,c.coordinate))
 diff[x.title]=ds
 assert x.freeze_panes==y.freeze_panes and set(x.tables)==set(y.tables)
assert not style,style[:10]
assert not diff['Channel Directory']
for name in ['All Finance Videos','Detailed Research']:
 for addr in diff[name]:assert z[name].cell(z[name][addr].row,1).value==V,(name,addr)
(O/'receipt-verification.json').write_text(json.dumps({'claims_exact_quotes':40,'source_ids':13,'calculations':9,'independent_monthly_annual_recurrence_and_division':'PASS','source_vintage_labels':'PASS','all_workbook_cell_value_changes':diff,'workbook_style_changes':0,'tables_and_freeze_panes':'PRESERVED','known_full_suite_failure':'PRE_EXISTING_PARENT_BYTES_IDENTICAL'},indent=2)+'\n')
print('PASS:40quotes/13sources/9receipts;independent recurrence checks;all unrelated workbook cells/styles preserved')
