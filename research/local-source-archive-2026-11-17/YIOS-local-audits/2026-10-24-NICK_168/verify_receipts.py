from pathlib import Path
import json,hashlib,subprocess,math,io,shutil
from openpyxl import load_workbook
R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';O=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_168');P='7e7c14016141977cd77fda48bcc6650aa6c3f517';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();r=json.loads((B/'audit-batches/NICK_168_READ_RECEIPTS.json').read_text());s=(O/'canonical-transcript.txt').read_text();rr=r['receipts'][0]
assert rr['Text_SHA256']==sha(O/'canonical-transcript.txt');assert rr['character_count']==len(s)
assert len(r['financial_claim_locations'])==39;ids={x['source_id'] for x in r['primary_source_receipts']};assert len(ids)==16
for c in r['financial_claim_locations']:
 assert c['original_quote']==s[c['start_char']:c['end_char']]
 assert set(c['source_ids'])<=ids
for source in r['primary_source_receipts']:
 assert source['publication_applicability'] in ['AVAILABLE_AT_VIDEO_PUBLICATION','LATER_RETROSPECTIVE_EVIDENCE','CURRENT_GUIDANCE_WITH_UNVERIFIED_HISTORICAL_VINTAGE','UNVERIFIED_OR_UNAVAILABLE']
 if 'saved_source_path' in source:assert sha(Path(source['saved_source_path']))==source['saved_source_sha256']
n=json.loads((O/'numbers.json').read_text());balance=50000.;paid_interest=0
for k in range(1,85):
 interest=balance*.07/12;paid_interest+=interest;balance+=interest-n['M84']
 if k==12:assert abs(balance-n['balance12'])<1e-7
assert abs(balance)<1e-7;assert abs(paid_interest-n['interest84'])<1e-7
account=0.
for k in range(360):account=account*(1+.08/12)+700
assert abs(account-n['FV700_8_360'])<1e-6
assert abs(n['income_10percent']*.1/12-(n['M48_40K']+185+n['fuel_monthly']+90+90))<1e-8
# Unchanged accepted-parent byte proof for the explicitly unrelated full-suite failure.
old=subprocess.check_output(['git','show',P+':.gitattributes'],cwd=R);actual=(R/'.gitattributes').read_bytes();assert old==actual
f=json.loads(Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_167/full-regression-baseline-failure.json').read_text());f.update(accepted_parent=P,unchanged_from_parent=True,bytes=len(actual),sha256=sha(R/'.gitattributes'),full_pytest_this_session='460 passed;1 failed;5 warnings;38.11 seconds;sole known DS-000028-F020 SIZE_MISMATCH/SHA_MISMATCH; no new failing test')
(O/'full-regression-baseline-failure.json').write_text(json.dumps(f,indent=2)+'\n')
# Compare all workbook cell values and styles to accepted source workbook, allowing only dependent cells.
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
 for addr in diff[name]:
  cell=z[name][addr];assert z[name].cell(cell.row,1).value=='TdNH3QP3qao',(name,addr)
for name in ['Combined Dashboard','All Finance Videos','Channel Directory','Detailed Research']:
 p=Path('/tmp')/('finance-1612-'+name.replace(' ','-')+'.png');out=O/('workbook-after-'+name.replace(' ','-')+'.png');shutil.copyfile(p,out);assert sha(p)==sha(out)
(O/'receipt-verification.json').write_text(json.dumps({'claims_exact_quotes':39,'source_ids':16,'calculations':9,'iterative_amortization_and_accumulation':'PASS','source_vintage_labels':'PASS','all_workbook_cell_value_changes':diff,'workbook_style_changes':0,'tables_and_freeze_panes':'PRESERVED','known_full_suite_failure':'PRE_EXISTING_PARENT_BYTES_IDENTICAL'},indent=2)+'\n');print('PASS:39 quotes/16 sources/9 receipts; independent iterative arithmetic; workbook unrelated cells/styles preserved')
