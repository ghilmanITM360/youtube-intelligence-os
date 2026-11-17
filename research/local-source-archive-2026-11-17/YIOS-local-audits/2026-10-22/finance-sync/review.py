import json,sqlite3,sys,csv,subprocess,hashlib
from pathlib import Path
import openpyxl
root=Path.cwd(); b=root/'research/finance-economics-intelligence'; out=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-22/finance-sync'); sys.path.insert(0,str(b))
from validate_audit_966 import strict_receipt_errors
ledger=[json.loads(l) for l in (b/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()]; target=next(r for r in ledger if r['Video_ID']=='SsHQ-TtXhRQ')
con=sqlite3.connect('file:'+str(root/'data/catalog/youtube_channel_registry.db')+'?mode=ro&immutable=1',uri=True)
text=con.execute('select transcript_text from transcripts where youtube_video_id=?',('SsHQ-TtXhRQ',)).fetchone()[0]
master={r['Video_ID']:r for r in csv.DictReader((b/'VIDEO_MASTER.csv').open())}; errors=strict_receipt_errors(target,text,master); assert not errors,errors
(out/'NICK_165-canonical-transcript.txt').write_text(text)
payload=json.loads(subprocess.check_output([str(root/'.venv/bin/python'),'-B',str(b/'build_combined_workbook_data.py')]))
wb=openpyxl.load_workbook(b/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx',read_only=True,data_only=True); rows=[r for r in wb['All Finance Videos'].iter_rows(min_row=5,values_only=True) if r[0]]
by={r['video_id']:r for r in payload['all_videos']}; assert len(rows)==1612 and {r[0] for r in rows}==set(by)
assert all(r[26]==by[r[0]]['audit_status'] and r[6]==by[r[0]]['population_layer'] for r in rows)
complete={'COMPLETE_LIMITED_EVIDENCE','COMPLETE_EVIDENCE_BACKED'}; untouched=next(r['Video_ID'] for r in ledger if all(v=='NOT_STARTED' for k,v in r['statuses'].items() if k!='PERFORMANCE_REVIEW'))
# independently derive rather than reuse published results
r=.07/12; pmt=63000*r/(1-(1+r)**-72)
calc={'loan_payment':pmt,'loan_total_payments':pmt*72,'loan_interest':pmt*72-63000,'truck_all_in_with_down_payment':pmt*72+7000,'lump_35650_year_30_at_7_percent':35650*1.07**30,'annual_2400_year_30_at_7_percent':2400*((1.07**30-1)/.07),'monthly_1076_year_35_at_7_percent':1076*((1+r)**420-1)/r,'monthly_1076_year_35_at_10_percent':1076*((1+.10/12)**420-1)/(.10/12)}
receipt=json.loads((b/'audit-batches/NICK_165_READ_RECEIPTS.json').read_text()); recorded=receipt['calculation_receipts'][1]['results']; assert all(abs(v-recorded[k])<.01 for k,v in calc.items())
res={'workbook_population_and_statuses_match_jsonl_projection':True,'next_untouched_original':untouched,'receipt_errors':errors,'transcript_chars':len(text),'transcript_sha256':hashlib.sha256(text.encode()).hexdigest(),'independent_calculations':calc,'finding':'NICK_165 prose says 271355 for 35650 at 7%/30y; receipt correctly says 271376.8922709018. Proposed prose correction 271377; no change to overall conclusion.'}
(out/'review-checks.json').write_text(json.dumps(res,indent=2)); print(json.dumps(res,indent=2))
