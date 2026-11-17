import json,hashlib,subprocess,io
from pathlib import Path
from collections import Counter
import openpyxl
out=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-22/finance-sync'); root=Path.cwd(); base=root/'research/finance-economics-intelligence'
a=json.loads((out/'before.json').read_text()); b=json.loads((out/'after.json').read_text())
assert a['untracked']==b['untracked']; assert a['ignored']==b['ignored']; assert a['stash']==b['stash']; assert a['local_only']==b['local_only']; assert b['tracked']==''
refs=lambda d:dict(line.split(' ',1) for line in d['refs'].splitlines())
x,y=refs(a),refs(b); changed={k:[x[k],y[k]] for k in x if x[k]!=y[k]}; assert list(changed)==['refs/heads/research/finance-economics-intelligence']
frozen=json.loads((base/'audit-baseline/MANIFEST.json').read_text()); mismatches=[p for p,h in frozen['source_hashes'].items() if hashlib.sha256((root/p).read_bytes()).hexdigest()!=h]; assert not mismatches
assert hashlib.sha256((base/'audit-baseline/VIDEO_MASTER.csv').read_bytes()).hexdigest()==frozen['frozen_master_sha256']
hashes={}
for name in ['FINANCE_1612_COMBINED_INTELLIGENCE.xlsx','VIDEO_AUDIT_966.jsonl']:
 p=base/name; local=hashlib.sha256(p.read_bytes()).hexdigest(); published=hashlib.sha256(subprocess.check_output(['git','show',b['head']+':'+str(p.relative_to(root))])).hexdigest(); assert local==published; hashes[name]=local
payload=json.loads(subprocess.check_output([str(root/'.venv/bin/python'),'-B',str(base/'build_combined_workbook_data.py')]))
assert len(payload['all_videos'])==len({r['video_id'] for r in payload['all_videos']})==1612
wb=openpyxl.load_workbook(base/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx',read_only=True,data_only=True)
ws=wb['All Finance Videos']; rows=list(ws.iter_rows(values_only=True)); print('Workbook headers:',rows[3]); print('Workbook first data:',rows[4][:8]); print('Payload keys:',list(payload['all_videos'][0]));
print('Workbook sheets:',wb.sheetnames)
result={'evidence_hashes_unchanged':True,'other_branch_refs_stash_local_only_commits_unchanged':True,'changed_refs':changed,'source_fingerprints':len(frozen['source_hashes']),'source_mismatches':mismatches,'hashes':hashes,'population':len(payload['all_videos']),'layers':dict(Counter(r['population_layer'] for r in payload['all_videos'])),'deep_complete':sum(r['audit_status']=='DEEP_AUDIT_COMPLETE' for r in payload['all_videos']),'validation':{k:v for k,v in json.loads((base/'VALIDATION_966.json').read_text()).items() if k in ['validation','errors','next_master_order_id','source_hashes_checked']}}
(out/'validation.json').write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
