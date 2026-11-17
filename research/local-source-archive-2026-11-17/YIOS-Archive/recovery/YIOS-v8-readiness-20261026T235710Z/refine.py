import os,csv,json,hashlib,collections,subprocess
from pathlib import Path
O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');allrows=list(csv.DictReader(open(A/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')))
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
safe=collections.defaultdict(list)
for r in allrows:
 if r['machine_a_sha256'] and r['coverage_status']=='SAFE':safe[r['machine_a_sha256']].append({'path':r['absolute_path'],'remote_id':r['drive_remote_id'],'receipt':r['drive_receipt_reference'],'git_ref':r['git_commit_ref']})
tri=list(csv.DictReader(open(O/'LOCAL_ONLY_RISK_TRIAGE.csv')));changed=[];newhashbytes=0
for r in tri:
 p=Path(r['source_path']);b=p.stat()
 if not r['sha256']:
  h=sha(p);newhashbytes+=b.st_size;a=p.stat();r['sha256']=h;r['hash_evidence']='FRESH_FULL_SHA256_STABLE_READ' if (b.st_size,b.st_mtime_ns,b.st_ino)==(a.st_size,a.st_mtime_ns,a.st_ino) else 'SOURCE_CHANGED_DURING_READ';
  if 'CHANGED' in r['hash_evidence']:changed.append(str(p))
 if r['sha256'] in safe:
  r['classification']='HASH_IDENTICAL_VERIFIED_REMOTE_ORIGINAL';r['priority']='NO_UPLOAD';r['reason']='Current stable source SHA matches sealed independently verified original coverage';r['receipt']=json.dumps(safe[r['sha256']])
 r['dedup_group']='sha256:'+r['sha256']+':'+r['size']
with open(O/'LOCAL_ONLY_RISK_TRIAGE.csv','w') as f:w=csv.DictWriter(f,fieldnames=tri[0]);w.writeheader();w.writerows(tri)
summary={}
for g,pattern in [('recovery_status','/yios-recovery-status/'),('forensic_research','/CasuallyFinance-Forensic-Research/')]:
 ss=[r for r in tri if pattern in r['source_path']];unique={r['dedup_group']:r for r in ss};summary[g]={'paths':len(ss),'unique_content_identities':len(unique),'unique_content_bytes':sum(int(x['size']) for x in unique.values()),'verified_remote_matched_paths':sum(x['classification']=='HASH_IDENTICAL_VERIFIED_REMOTE_ORIGINAL' for x in ss),'classification':dict(collections.Counter(x['classification'] for x in ss)),'not_classified_original_uniqueness':'Hash uniqueness within bounded group is not proof of irreplaceable original authorship'}
summary.update(newly_hashed_bytes=newhashbytes,changed_during_reads=changed);(O/'evidence/HIGH_VALUE_HASH_TRIAGE_SUMMARY.json').write_text(json.dumps(summary,indent=2))
# Read-only provider lookup of two required bundle base commits, no Git fetch/write.
reqs=[]
for oid in ['e25dc63fc101390867ebf1495bba726ba9797fb6','31ea9a53a6b4c9a1b74a3478ce16e510fdf06e10']:
 r=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/commits/'+oid],capture_output=True);d={'oid':oid,'api_exit':r.returncode,'available':r.returncode==0}
 if r.returncode==0:
  j=json.loads(r.stdout);d.update(tree=j['tree']['sha'],parents=[x['sha'] for x in j['parents']]);(O/'evidence'/('BUNDLE_BASE_COMMIT_'+oid+'.json')).write_bytes(r.stdout)
 reqs.append(d)
(O/'evidence/BUNDLE_BASE_REMOTE_AVAILABILITY.json').write_text(json.dumps(reqs,indent=2))
# Add exact refs for all 29 pointers from immutable previously inspected tree files.
lf=list(csv.DictReader(open(O/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv')));trees=[(p.name,p.read_text()) for p in (A/'evidence').glob('LOCAL_TREE_*.txt')]
for r in lf:
 matches=[n.removeprefix('LOCAL_TREE_').removesuffix('.txt') for n,t in trees if r['pointer_blob_sha1'] in t];r['git_ref_evidence']+='; exact available commit trees: '+','.join(matches)
with open(O/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv','w') as f:w=csv.DictWriter(f,fieldnames=lf[0]);w.writeheader();w.writerows(lf)
# Link tiny iCloud restored bytes to established equivalent hashes / published blob IDs; no source reread.
ss=json.load(open(O/'evidence/ICLOUD_READ_SAMPLE.json'));trees=[]
for p in (A/'evidence').glob('REMOTE_TREE_*.txt'):
 try:trees.append((p.name,json.load(open(p))['tree']))
 except:pass
for r in ss:
 if r['result']!='FULL_BYTES_READ':continue
 b=Path(r['scratch']).read_bytes();oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();r['verified_remote_original_equivalents']=safe.get(r['sha256'],[]);r['published_git_tree_matches']=[{'tree':n,'path':x['path'],'blob':oid} for n,t in trees for x in t if x.get('sha')==oid];r['timestamp_delta_ns']=r['after_mtime_ns']-r['before_mtime_ns'];r['version_consistency']='Historical byte hash match' if r['verified_remote_original_equivalents'] else 'Remote read succeeded; historical original version hash not established';r['content_writes_by_audit']=0
(O/'evidence/ICLOUD_READ_SAMPLE_RECONCILED.json').write_text(json.dumps(ss,indent=2));print(json.dumps(summary,indent=2));print('bundle base',reqs)
