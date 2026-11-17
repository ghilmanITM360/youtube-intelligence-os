from pathlib import Path
import json,hashlib,subprocess,io,math,csv,statistics
from openpyxl import load_workbook
R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=R/'research/finance-economics-intelligence';O=Path(__file__).parent;P='8fa0fe28f0870b2717d08a4099e1c4425a66429c';V='ULkTn-jHBBc';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((B/'audit-batches/NICK_170_READ_RECEIPTS.json').read_text());s=(O/'canonical-transcript.txt').read_text();rr=r['receipts'][0]
assert rr['Text_SHA256']==sha(O/'canonical-transcript.txt');assert rr['character_count']==len(s)==19179
assert len(r['financial_claim_locations'])==39;ids={x['source_id'] for x in r['primary_source_receipts']};assert len(ids)==20
for c in r['financial_claim_locations']:
 assert c['original_quote']==s[c['start_char']:c['end_char']]
 assert set(c['source_ids'])<=ids
cursor=0
for a,b in rr['read_character_ranges']:assert a==cursor and b>a;cursor=b
assert cursor==len(s)
assert len(r['six_method_locations'])==6
for source in r['primary_source_receipts']:assert source['publication_applicability'] in ['AVAILABLE_AT_VIDEO_PUBLICATION','LATER_RETROSPECTIVE_EVIDENCE','CURRENT_GUIDANCE_WITH_UNVERIFIED_HISTORICAL_VINTAGE','UNVERIFIED_OR_UNAVAILABLE']
calcs={c['calculation_id']:c for c in r['calculation_receipts']};assert len(calcs)==15
# Independent yearly cash-flow/balance identities, separate from the saved receipt generator.
for k in ['K03','K06','K09','K12']:
 d=calcs[k]
 entries=d['results'].get('loan_scenarios',{}) if k=='K03' else {'one':d['results'].get('loan',d['results'].get('mortgage'))}
 for key,l in entries.items():
  if k=='K03':p=200000;rate=float(key)
  else:p=d['inputs'].get('loan',d['inputs'].get('P'));rate=d['inputs'].get('own_APR',d['inputs'].get('APR'))
  assert abs(l['total_payments']-l['interest_paid']-l['principal_repaid'])<1e-5
  assert abs(p-l['principal_repaid']-l['balance'])<1e-5
  pv=sum(l['monthly_payment']/(1+rate/12)**j for j in range(1,l['months']+1))+l['balance']/(1+rate/12)**l['months'];assert abs(pv-p)<1e-5
lo=calcs['K03']['results']['loan_scenarios']['0.06']
for case in calcs['K04']['results']:
 pricegain=case['ending_value']-250000;sale=.06*case['ending_value'];profit=pricegain+10*case['annual_NOI']-lo['interest_paid']-sale
 assert abs(profit-case['leveraged_total_profit'])<1e-5
assert calcs['K03']['results']['exact_narrated_equity']==174000
assert abs(calcs['K07']['results']['full_sale_tax']-952000)<1e-7
sale=calcs['K07']['results']['equalcash_sale_gross'];assert abs(sale-(sale*.8*.238)-3000000)<1e-7
for case in calcs['K09']['results']['scenarios']:
 i=(1+case['annual_investment_return'])**(1/12)-1;a=200000;b=0;pmt=calcs['K09']['results']['mortgage']['monthly_payment']
 for _ in range(360):a*=1+i;b=b*(1+i)+pmt
 assert abs(a-case['keep_loan_invest200K_terminal'])<1e-5
 assert abs(b-case['payoff_now_invest_freed_monthly_payment_terminal'])<1e-5
# Reconstruct peers again from immutable baseline, with Channel_ID rather than channel label.
master=list(csv.DictReader((B/'audit-baseline/VIDEO_MASTER.csv').open()));target=next(x for x in master if x['Video_ID']==V)
peers=[p for p in master if p['Video_ID']!=V and p['Channel_ID']==target['Channel_ID'] and p['Format']==target['Format'] and p['Metric_snapshot_date']==target['Metric_snapshot_date'] and p['Age_days'] and float(p['Age_days'])>=7 and .5<=float(p['Age_days'])/float(target['Age_days'])<=2]
peers.sort(key=lambda p:(abs(float(p['Age_days'])-float(target['Age_days'])),p['Video_ID']));peers=peers[:10];f=calcs['K15']['results'];assert [p['Video_ID'] for p in peers]==f['peer_ids_10']
for n in [10,5]:
 den=statistics.median(int(p['Views'])/float(p['Age_days']) for p in peers[:n]);ratio=int(target['Views'])/float(target['Age_days'])/den;assert abs(ratio-f['peer_ratio_'+str(n)])<1e-12
actual=(R/'.gitattributes').read_bytes();assert actual==subprocess.check_output(['git','show',P+':.gitattributes'],cwd=R)
(O/'full-regression-baseline-failure.json').write_text(json.dumps(dict(file='.gitattributes',accepted_parent=P,unchanged_from_parent=True,bytes=len(actual),sha256=sha(R/'.gitattributes'),known_failure='DS-000028-F020 expected627bytes/1970079d0da551fe6400b93d55c5f8cf9be2beeb628089457be11a6d0a79f43d;actual895bytes/93d4461c54929f06d8977a3741b20dbf788bcfffbb4d2f2234027e914a230222',handling='PRESERVED_UNRELATED_PRE_EXISTING_FAILURE;SEE_FRESH_FULL_PYTEST_LOG'),indent=2)+'\n')
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
assert not style,style[:10];assert not diff['Channel Directory']
for name in ['All Finance Videos','Detailed Research']:
 for addr in diff[name]:assert z[name].cell(z[name][addr].row,1).value==V,(name,addr)
(O/'receipt-verification.json').write_text(json.dumps({'claims_exact_quotes':39,'source_ids':20,'calculations':15,'independent_payment_PV_balance_cashflow_recurrence_and_peers':'PASS','source_vintage_labels':'PASS','all_workbook_cell_value_changes':diff,'workbook_style_changes':0,'tables_and_freeze_panes':'PRESERVED','known_full_suite_failure':'PRE_EXISTING_PARENT_BYTES_IDENTICAL'},indent=2)+'\n')
print('PASS:39quotes/20sources/15calculations;independent loan PV, cashflow, investment recurrence, peer reproduction;unrelated workbook values/styles preserved')
