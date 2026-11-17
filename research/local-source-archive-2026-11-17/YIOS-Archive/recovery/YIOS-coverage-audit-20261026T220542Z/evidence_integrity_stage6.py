import json,collections,hashlib
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd');D=json.load(open(O/'checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'));meta={}
for p in O.glob('checkpoints/DRIVE_METADATA_*.json'):
 for x in json.load(open(p)):meta[x['target']['id']]=x['result']['structuredContent']
checks=[];archive=[]
def findmd(x,id):
 out=[]
 def walk(v):
  if isinstance(v,dict):
   if v.get('id')==id and ('parent_ids' in v or 'size' in v):out.append(v)
   for y in v.values():walk(y)
  elif isinstance(v,list):
   for y in v:walk(y)
 walk(x);return out
for a in D['objects']:
 cur=meta[a['remote_id']];rec=json.load(open(a['verification_receipt']));opts=findmd(rec,a['remote_id']);expect=opts[-1] if opts else {}
 if a['batch']=='batch-0035':
  opts=[json.load(open(p))['after'] for p in (R/'batch-0035').glob('move-*.json')];expect=next(x for x in opts if x['id']==a['remote_id'])
 problems=[]
 for k in ['title','size','created_time','modified_time','parent_ids']:
  if k in expect and str(expect[k])!=str(cur.get(k)):problems.append(k)
 checks.append({'id':a['remote_id'],'receipt':a['verification_receipt'],'metadata_fields_checked':[k for k in ['title','size','created_time','modified_time','parent_ids'] if k in expect],'status':'FAIL' if problems else 'PASS','differences':problems,'note':'No source hash claimed from metadata; full byte receipt separately validated'})
 if a.get('package_manifest'):
  md=json.load(open(a['package_manifest']));rr=next(x for x in rec['files'] if x.get('remote_id')==a['remote_id']);ret=rr['retrieval'];members=md['members'];n=len(members);b=sum(x['bytes'] for x in members);passed=ret.get('package_source_members_verified')==n and ret.get('package_uncompressed_member_bytes_verified')==b
  archive.append({'archive_source':a['source'],'remote_id':a['remote_id'],'manifest':a['package_manifest'],'member_count':n,'member_bytes':b,'receipt_member_count':ret.get('package_source_members_verified'),'receipt_member_bytes':ret.get('package_uncompressed_member_bytes_verified'),'status':'PASS' if passed else 'FAIL','v7':Path(a['source']).name.startswith('040')})
V=[x for x in archive if x['v7']];out={'objects_checked':len(checks),'metadata_pass':sum(x['status']=='PASS' for x in checks),'metadata_failures':[x for x in checks if x['status']!='PASS'],'archives':archive,'archive_check_pass':all(x['status']=='PASS' for x in archive),'all_archive_members':sum(x['member_count'] for x in archive),'v7_package_count':len(V),'v7_members':sum(x['member_count'] for x in V),'v7_member_bytes':sum(x['member_bytes'] for x in V),'metadata_rows':checks};(O/'evidence/REMOTE_METADATA_AND_ARCHIVE_RECEIPT_RECONCILIATION.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ['archives','metadata_rows']},indent=2))
