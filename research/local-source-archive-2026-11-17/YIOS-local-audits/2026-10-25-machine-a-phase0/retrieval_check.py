import json,subprocess,base64,hashlib,collections
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');j=json.loads((O/'live_head_tree.txt').read_text());tree={x['path']:x for x in j['tree'] if x['type']=='blob'}
paths=['research/visual-forensics/channels/casual-finance/o3FQcd91MIs/research/v2/visual_ct_scan_report_v2.md','research/visual-forensics/channels/casual-finance/Uumnx2Fo6cE/research/STATE_BY_STATE_VISUAL_FORENSICS.md','research/finance-economics-intelligence/audit-batches/NICK_170.json','research/finance-economics-intelligence/audit-batches/NICK_170_READ_RECEIPTS.json','research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx','research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl','scripts/run_youtube_intelligence.py','data/manifests/what-if-forensic-source-v1.json']
results=[]
for path in paths:
 x=tree[path];p=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/blobs/'+x['sha']],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 result={'path':path,'live_ref':'1adb8129f689207552f0838414e5823e4255bde1','git_blob_sha1':x['sha'],'returncode':p.returncode}
 if p.returncode:result['error']=p.stderr.decode()
 else:
  v=json.loads(p.stdout);b=base64.b64decode(v['content']);digest=hashlib.sha256(b).hexdigest();local=hashlib.sha256((R/path).read_bytes()).hexdigest();result.update({'retrieved_bytes':len(b),'retrieved_sha256':digest,'local_sha256':local,'status':'PASS' if digest==local else 'MISMATCH'})
  # Keep only the verification receipt: remote bytes compared in memory, no duplicate payload retained.
 results.append(result)
(O/'remote-retrieval-verification.json').write_text(json.dumps(results,indent=2))
ledger=[json.loads(x) for x in (R/'research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl').read_text().splitlines() if x.strip()]
(O/'finance-ledger-shape.json').write_text(json.dumps({'rows':len(ledger),'keys':list(ledger[0]),'status_like_counts':{k:dict(collections.Counter(str(x.get(k)) for x in ledger)) for k in ledger[0] if 'status' in k.lower()},'nick170_rows':[x for x in ledger if 'ULkTn-jHBBc' in [str(v) for v in x.values()]]},indent=2))
print([(x['path'],x.get('status',x['returncode'])) for x in results])
