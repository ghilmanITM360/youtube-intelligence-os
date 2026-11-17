import json,hashlib,os,re,collections
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd');C=R/'checkpoint-20261026T213404Z';D=json.load(open(C/'SOURCE_TO_DRIVE_INVENTORY.json'));Q=json.load(open(C/'CONTINUATION.json'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];seen=set()
def check(p,expect=None,kind='evidence'):
 p=Path(p)
 if str(p) in seen:return
 seen.add(str(p));x={'path':str(p),'kind':kind,'exists':p.exists()}
 if p.exists():x.update(bytes=p.stat().st_size,sha256=sha(p),expected_sha256=expect,status='PASS' if not expect or sha(p)==expect else 'FAIL')
 else:x['status']='MISSING'
 checks.append(x)
for p,e in [(R/'ORDERED_PLAN_V7.json',Q['plan_sha256']),(C/'CONTINUATION.json','72a99f3661265336e94889cdc6c608b2eb7b9933dd6c1586efe5a2e5ee559829'),(Q['batch31_exception_approval_receipt'],Q['batch31_exception_approval_sha256']),(Q['batch35_resolution_receipt'],Q['batch35_resolution_sha256']),(Q['latest_full_verified_control']['handoff_path'],Q['latest_full_verified_control']['handoff_sha256'])]:check(p,e)
for p in sorted(R.glob('batch-*/RECEIPT.json')):check(p,kind='batch_receipt')
for a in D['batch_receipts']:check(a['receipt_path'],a['receipt_sha256'],'batch_receipt')
# Validate exact verification receipts for every mapped object. Never re-download or rehash large originals here.
objs=[]
for x in D['objects']:
 p=Path(x['verification_receipt']);check(p,kind='object_verification');v=json.load(open(p));matches=[]
 def walk(y):
  if isinstance(y,dict):
   if (y.get('retrieved_sha256')==x['sha256'] and int(y.get('retrieved_bytes',-1))==x['bytes']) or (y.get('sha256')==x['sha256'] and int(y.get('independently_retrieved_bytes',-1))==x['bytes']):matches.append(True)
   for z in y.values():walk(z)
  elif isinstance(y,list):
   for z in y:walk(z)
 walk(v)
 # Exact original verification file may use a direct result/hash field; record unrecognized rather than fabricate pass.
 objs.append({**x,'receipt_sha256':sha(p),'receipt_hash_length_match':bool(matches)})
# Every verified control including final handoff, which is not self-included in its inventory.
controls=D['verified_controls']+[{'remote_id':Q['latest_full_verified_control']['remote_id'],'source_path':Q['latest_full_verified_control']['handoff_path'],'sha256':Q['latest_full_verified_control']['handoff_sha256'],'uploaded_bytes':Q['latest_full_verified_control']['handoff_bytes']}]
for p in R.glob('CONTROL-VERIFY-*.json'):check(p,kind='control_verification')
# SHA256 manifests validate small evidence entries; large media/package hashes reused only via stable source identity later.
manifest=[]
for p in sorted(set(list(R.glob('batch-*/SHA256SUMS'))+[C/'SHA256SUMS',R/'batch-0031/PARTIAL_SHA256SUMS',R/'batch-0035/PARTIAL_SHA256SUMS',R/'batch-0035/MOVE_POSTCLOSURE_SHA256SUMS'])):
 if not p.exists():continue
 check(p,kind='checksum_manifest')
 for line in p.read_text().splitlines():
  m=re.match(r'^([a-f0-9]{64})\s+\*?(.+)$',line)
  if not m:continue
  h,n=m.groups();t=Path(n) if n.startswith('/') else p.parent/n
  result='MISSING'
  if t.exists():
   if t.stat().st_size<=20_000_000:result='PASS' if sha(t)==h else 'FAIL'
   else:result='LARGE_HASH_NOT_REPEATED'
  manifest.append({'manifest':str(p),'target':str(t),'expected_sha256':h,'result':result})
# All transfer totals count exact unique accepted remote IDs, not archive-member bytes.
byid={x['remote_id']:x for x in objs};bycontrol={x['remote_id']:x for x in controls}
accepted=sum(x['bytes'] for x in byid.values())+sum(x['uploaded_bytes'] for x in bycontrol.values())
res={'baseline_expected':Q['accepted_selected_and_prior_verified_bytes_including_controls'],'accepted_sum_mapped_objects_and_controls':accepted,'object_count':len(byid),'object_bytes':sum(x['bytes'] for x in byid.values()),'control_count':len(bycontrol),'control_bytes':sum(x['uploaded_bytes'] for x in bycontrol.values()),'physical_with_duplicate':accepted+404830,'byte_match':accepted==Q['accepted_selected_and_prior_verified_bytes_including_controls'],'archive_member_representations':len(D['archive_members']),'archive_logical_bytes':sum(x['bytes'] for x in D['archive_members']),'v7_packages':sum(1 for x in objs if x.get('sequence',0)>=4023),'receipt_hash_length_matches':sum(x['receipt_hash_length_match'] for x in objs),'unrecognized_receipt_schema':[x['verification_receipt'] for x in objs if not x['receipt_hash_length_match']],'checks':checks,'manifest_results':dict(collections.Counter(x['result'] for x in manifest)),'historical_incidents':'Batch31 attribution unresolved under specific owner exception; Batch35 wrong destination corrected same IDs, original blocked evidence unchanged'}
(O/'evidence/V7_BASELINE_RECONCILIATION.json').write_text(json.dumps(res,indent=2));(O/'evidence/SHA_MANIFEST_ENTRY_CHECKS.json').write_text(json.dumps(manifest,indent=2));(O/'checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json').write_text(json.dumps({'objects':objs,'members':D['archive_members'],'aliases':D['exact_duplicate_pilot_aliases'],'controls':controls},indent=2))
targets=[{'id':x['remote_id'],'bytes':x['bytes'],'sha256':x['sha256'],'source':x['source']} for x in byid.values()]+[{'id':x['remote_id'],'bytes':x['uploaded_bytes'],'sha256':x['sha256'],'source':x['source_path']} for x in bycontrol.values()]+[{'id':Q['batch31_extra_remote_id'],'bytes':404830,'sha256':'e99f5577c066109a03da5d71fd6e4cb23f79f5c45d3eb6a3991a4aaf8dff2953','source':'EXTRA_DUPLICATE_ZERO_COVERAGE'}]
(O/'evidence/DRIVE_METADATA_TARGETS.json').write_text(json.dumps(targets));print(json.dumps({k:v for k,v in res.items() if k not in ['checks','unrecognized_receipt_schema']},indent=2));print('unrecognized',len(res['unrecognized_receipt_schema']))
