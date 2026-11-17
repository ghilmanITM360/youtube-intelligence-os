import os,stat,csv,json,gzip,hashlib,collections,subprocess,re,time
from pathlib import Path
O=Path(__file__).parent;H=Path('/Users/ghilmankhan');P=H/'workprojects/youtube-intelligence-os';R=H/'YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd';D=json.load(open(O/'checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'));E=H/'YIOS-local-audits/2026-10-25-machine-a-phase0';env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def dump(n,x): (O/n).write_text(json.dumps(x,indent=2))
def readcsv(p):return list(csv.DictReader(open(p)))
rows=readcsv(O/'checkpoints/STAGE1_LOCAL_CENSUS.csv')+readcsv(O/'checkpoints/STAGE1B_REFERENCED_CENSUS.csv');seen=set();rows=[x for x in rows if not(x['path'] in seen or seen.add(x['path']))]
for x in rows:
 for k in ['bytes','allocated_bytes','device','inode','nlink','mtime_ns','ctime_ns']:x[k]=int(x[k])
 x['dataless']=x['dataless']=='True'
files=[x for x in rows if x['kind'] in ['regular','symlink']];bylocal={x['path']:x for x in files}
old={x['path']:x for x in csv.DictReader(gzip.open(E/'files.csv.gz','rt'))};cache=json.load(open(E/'hashes.json'))
hashrecords={};hashbytes=0;budget=1_500_000_000
# Exact original raw retrieval/member records provide stable inode/device/mtime/ctime identity.
statclaims=collections.defaultdict(list)
for a in D['members']+D['aliases']:
 statclaims[a['source_absolute']].append({'sha256':a['sha256'],'stat':a.get('source_stat',{}),'evidence':a.get('verification_status','verified alias')})
for p in R.glob('batch-*/RECEIPT.json'):
 for a in json.load(open(p)).get('files',[]):
  statclaims[a['source_absolute']].append({'sha256':a.get('fresh_sha256') or a.get('sha256'),'stat':a.get('fresh_stat',{}),'evidence':str(p)})
for a in D['objects']:
 if a['batch']=='pilot':
  pilot=json.load(open(a['verification_receipt']))
  for b in pilot['files']:
   if b['source']==a['source']:statclaims[a['source']].append({'sha256':a['sha256'],'stat':{'st_size':b['bytes'],'st_mtime_ns':b['refreshed_mtime_ns'],'st_ctime_ns':b['refreshed_ctime_ns'],'st_ino':b['refreshed_inode']},'evidence':a['verification_receipt']})
# Git trees are content-addressed publication evidence; retrieval is separately flagged.
blobrefs=collections.defaultdict(list);remotepaths=collections.defaultdict(list);remotetrees={}
for p in O.glob('evidence/REMOTE_TREE_*.txt'):
 t=json.load(open(p));assert not t.get('truncated');label=p.stem.replace('REMOTE_TREE_','');remotetrees[label]=t
 for a in t['tree']:
  if a['type']=='blob':blobrefs[a['sha']].append(label+':'+t['sha']);remotepaths[a['path']].append((label,a))
for p in O.glob('evidence/LOCAL_TREE_*.txt'):
 sha=p.stem.replace('LOCAL_TREE_','')
 for line in p.read_text().splitlines():
  z=line.split('\t',1)
  if len(z)!=2:continue
  f=z[0].split()
  if len(f)==4 and f[1]=='blob':blobrefs[f[2]].append('LIVE_ADVERTISED_LOCAL_TREE:'+sha)
index={}
for b in (O/'evidence/GIT_TRACKED_INDEX.txt').read_bytes().split(b'\0'):
 if not b:continue
 a,n=b.decode().split('\t',1);mode,oid,stage=a.split();index[n]={'oid':oid,'mode':mode,'stage':stage}
ignored=set((O/'evidence/GIT_IGNORED.txt').read_text().split('\0'));untracked=set((O/'evidence/GIT_UNTRACKED.txt').read_text().split('\0'))
# Pointer inspection uses only small local Git blobs. Missing partial-clone objects remain unmodified.
small={}
for t in remotetrees.values():
 for a in t['tree']:
  if a['type']=='blob' and a.get('size',9999)<300:small[a['sha']]=a
for p in O.glob('evidence/LOCAL_TREE_*.txt'):
 for line in p.read_text().splitlines():
  z=line.split('\t',1);f=z[0].split()
  if len(z)==2 and len(f)==4 and f[1]=='blob' and f[3].isdigit() and int(f[3])<300:small[f[2]]={'path':z[1]}
pointer_by_blob={};pointererrors=[]
proc=subprocess.Popen(['git','cat-file','--batch'],cwd=P,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
for oid,a in small.items():
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();header=proc.stdout.readline().decode().strip()
 if header.endswith(' missing'):continue
 f=header.split()
 if len(f)!=3:pointererrors.append(header);continue
 n=int(f[2]);b=proc.stdout.read(n);proc.stdout.read(1)
 if b.startswith(b'version https://git-lfs.github.com/spec/v1\n'):
  m=re.search(rb'oid sha256:([a-f0-9]{64})\nsize (\d+)',b)
  if m:pointer_by_blob[oid]={'sha256':m[1].decode(),'bytes':int(m[2]),'git_pointer_blob':oid,'path':a['path'],'remote_lfs_status':'LFS_POINTER_ONLY_REMOTE_BYTES_UNVERIFIED'}
proc.stdin.close();proc.wait()
dump('evidence/LFS_POINTER_IDENTITIES.json',list(pointer_by_blob.values()))
# Historical independent GitHub byte retrievals permit stronger claims than tree membership alone.
retrieved=set()
for p in [E/'remote-retrieval-verification.json']:
 for a in json.load(open(p)):
  if a.get('status')=='PASS':retrieved.add(a.get('retrieved_sha256'))
for p in (H/'YIOS-local-audits/2026-10-25-machine-a-phase1b').glob('*PUBLICATION_RECEIPT.json'):
 def walk(v):
  if isinstance(v,dict):
   for k in ['retrieved_sha256','remote_sha256']:
    if isinstance(v.get(k),str):retrieved.add(v[k])
   for z in v.values():walk(z)
  elif isinstance(v,list):
   for z in v:walk(z)
 walk(json.load(open(p)))
for p in O.glob('evidence/FINANCE_AUTHORITY_*.json'):retrieved.add(json.load(open(p)).get('sha256'))
# Remote object metadata must be owner-only and in one of the independently checked private parents.
meta={}
for p in O.glob('checkpoints/DRIVE_METADATA_*.json'):
 for a in json.load(open(p)):meta[a['target']['id']]=a.get('result',{}).get('structuredContent',{})
parentmeta={x['id']:x.get('result',{}).get('structuredContent',{}) for x in json.load(open(O/'evidence/DRIVE_PARENT_METADATA.json'))}
def private(m):
 ps=m.get('permissions',[])
 return m.get('shared') is False and len(ps)==1 and ps[0].get('role')=='owner' and ps[0].get('emailAddress')=='kgk2930@gmail.com'
metadata_issues=[]
for id,m in meta.items():
 if not private(m):metadata_issues.append({'id':id,'problem':'OWNER_ONLY_NOT_ESTABLISHED'})
 for pa in m.get('parent_ids',[]):
  if not private(parentmeta.get(pa,{})):metadata_issues.append({'id':id,'problem':'PARENT_NOT_PRIVATE','parent':pa})
dump('evidence/DRIVE_PRIVACY_VALIDATION.json',{'objects':len(meta),'private_objects':sum(private(x) for x in meta.values()),'parents':len(parentmeta),'issues':metadata_issues})
map_path=collections.defaultdict(list);map_hash=collections.defaultdict(list)
for a in D['objects']:
 m=meta.get(a['remote_id'],{});rec={'id':a['remote_id'],'sha256':a['sha256'],'bytes':a['bytes'],'source':a['source'],'member':'','receipt':a['verification_receipt'],'status':'DRIVE_FULL_BYTES_SHA256_VERIFIED','folder':'|'.join(m.get('parent_ids',[])),'private':private(m),'batch':a['batch'],'verified':True};map_path[a['source']].append(rec);map_hash[(a['sha256'],a['bytes'])].append(rec)
for a in D['members']+D['aliases']:
 id=a.get('remote_archive_id') or a.get('remote_id');m=meta.get(id,{});member=a.get('archive_member','');rec={'id':id,'sha256':a['sha256'],'bytes':a['bytes'],'source':a['source_absolute'],'member':member,'receipt':a.get('source_package_manifest') or ('%s/%s/RECEIPT.json'%(R,a.get('batch',''))),'status':'DRIVE_ARCHIVE_AND_MEMBERS_VERIFIED' if member else 'DRIVE_PATH_ALIAS_VERIFIED','folder':'|'.join(m.get('parent_ids',[])),'private':private(m),'batch':a.get('batch','pilot alias'),'verified':True};map_path[a['source_absolute']].append(rec);map_hash[(a['sha256'],a['bytes'])].append(rec)
# Historical Machine B source manifests, never direct filesystem access.
bclaims=collections.defaultdict(list);badditional=[];Broot='/Users/ghilmanislam360/Documents/youtube-intelligence-os'
bmanifest=json.load(open(O/'evidence/FINANCE_MANIFEST_01.json'))
for a in bmanifest['sources']:
 bclaims[a['sha256']].append({'source':a['path'],'bytes':a.get('bytes'),'authority':'FINANCE_MANIFEST_01.json:sources; source date2026-10-23','status':'MACHINE_B_HANDOFF_VERIFIED'})
for a in bmanifest['all_registered_image_hashes']+bmanifest['competitor_visual_samples']:
 h=a.get('sha256') or a.get('image_sha256');path=a.get('path') or a.get('image_path');bclaims[h].append({'source':path,'bytes':None,'authority':'FINANCE_MANIFEST_01.json:registered images;2026-10-23','status':'MACHINE_B_HANDOFF_VERIFIED'})
for a in [json.loads(x) for x in (O/'evidence/MEDIA_LIBRARY_01.jsonl').read_text().splitlines()]:
 bclaims[a['sha256']].append({'source':a['external_source_path'],'bytes':int(a['byte_count']),'authority':'MEDIA_LIBRARY_01.jsonl at78e8fd2;historical2026-10-20 registry, latest handed off2026-10-23','status':'MACHINE_B_HANDOFF_VERIFIED','library_path':Broot+'/'+a['local_media_path']})
for path,h in json.load(open(O/'evidence/FINANCE_MANIFEST_00.json'))['source_hashes'].items():bclaims[h].append({'source':Broot+'/'+path,'bytes':None,'authority':'FINANCE_MANIFEST_00.json frozen2026-10-16;reconfirmed MachineB2026-10-23','status':'MACHINE_B_HANDOFF_VERIFIED'})
# Full stat-stable hashing is bounded; no cache/dependency/Git-internal reads, no dataless hydration.
for i,a in enumerate(files):
 p=a['path'];v={'sha256':'','git_blob_sha1':'','status':'HASH_NOT_COMPUTED','evidence':''}
 if a['kind']=='symlink':v.update(status='SYMLINK_NO_TARGET_READ')
 elif a['dataless']:v.update(status='DATALESS_PLACEHOLDER_BYTES_NOT_LOCAL')
 elif a['category'] in ['dependency-cache','os-metadata','git-internals']:v.update(status='NO_CONTENT_READ_METADATA_ONLY')
 else:
  for c in statclaims.get(p,[]):
   s=c['stat'];mapping={'st_size':'bytes','st_mtime_ns':'mtime_ns','st_ctime_ns':'ctime_ns','st_ino':'inode','st_dev':'device'}
   if c['sha256'] and s and all(a[mapping[k]]==v for k,v in s.items() if k in mapping) and all(k in s for k in ['st_size','st_mtime_ns','st_ino']):v.update(sha256=c['sha256'],status='REUSED_SHA256_EXACT_STABLE_IDENTITY',evidence=c['evidence']);break
  b=old.get(p);c=cache.get(p)
  if not v['sha256'] and b and c and c.get('stable_during_read') and all(a[k]==int(b[j]) for k,j in [('bytes','bytes'),('mtime_ns','mtime_ns'),('inode','inode'),('device','dev')]):v.update(sha256=c['sha256'],git_blob_sha1=c.get('git_blob_sha1',''),status='REUSED_SHA256_PHASE0_STAT_STABLE',evidence=str(E/'hashes.json')+' + files.csv.gz inode/device/size/mtime')
  # Hash small uncovered source assets and current critical LFS catalog once; bounded 1.5GB.
  limit=200_000_000 if p==str(P/'data/catalog/youtube_channel_registry.db') else 10_000_000
  if (not v['sha256'] or (not v['git_blob_sha1'] and a['bytes']<=limit)) and a['bytes']<=limit and hashbytes+a['bytes']<=budget:
   try:
    before=os.stat(p);h=hashlib.sha256();g=hashlib.sha1();g.update(b'blob '+str(a['bytes']).encode()+b'\0')
    with open(p,'rb') as f:
     for z in iter(lambda:f.read(1024*1024),b''):h.update(z);g.update(z)
    after=os.stat(p);hashbytes+=a['bytes'];stable=all(getattr(before,k)==getattr(after,k) for k in ['st_ino','st_size','st_mtime_ns','st_ctime_ns']) and after.st_size==a['bytes'] and after.st_mtime_ns==a['mtime_ns']
    if stable:v.update(sha256=h.hexdigest(),git_blob_sha1=g.hexdigest(),status='FRESH_SHA256_STABLE_READ',evidence='Audit bounded read; before/after inode/size/mtime/ctime')
    else:v.update(sha256='',git_blob_sha1='',status='CHANGED_DURING_AUDIT_READ',evidence='Not used for coverage')
   except Exception as e:v.update(status='CONTENT_READ_BLOCKED',evidence=str(e))
 hashrecords[p]=v
 if i%10000==0:print('hash',i,'bytes',hashbytes,flush=True)
dump('checkpoints/STAGE4_HASH_EVIDENCE.json',{'hash_bytes_read':hashbytes,'budget':budget,'files':hashrecords})
# Machine-readable full matrix for every enumerated file/link; all path populations separate from content identities.
cols=['source_group','root_directory','relative_path','absolute_path','logical_asset_id','file_type','classification','local_machine_a_presence','machine_a_size','machine_a_sha256','machine_a_hash_evidence','machine_b_presence_evidence','machine_b_evidence_authority','git_tracked_status','git_commit_ref','git_blob_sha1','git_lfs_status','drive_remote_id','drive_folder','drive_receipt_reference','archive_member_reference','independent_hash_verification_status','duplicate_alias_group','original_recoverability','privacy_sensitivity','restore_test_status','coverage_confidence','risk_level','recommended_next_action','allocated_bytes','device','inode','nlink','mtime_ns','dataless','category','drive_status','coverage_status','risk_reason']
result=[];pathasset={};shaassets=collections.defaultdict(list)
for a in files:
 p=a['path'];rel=a['relative'];h=hashrecords[p];sha=h['sha256'];blob=h['git_blob_sha1'];tracked='EXTERNAL_LOCAL_SOURCE';ref='';lfs='NONE_DETECTED'
 if a['root']==str(P):tracked='GIT_INTERNAL' if a['category']=='git-internals' else 'TRACKED' if rel in index else 'IGNORED_LOCAL_SOURCE' if rel in ignored else 'UNTRACKED_LOCAL'
 if blob in blobrefs:ref='|'.join(sorted(set(blobrefs[blob])));gitstatus='PUSHED_GIT_BLOB'
 else:gitstatus=tracked
 ix=index.get(rel) if a['root']==str(P) else None
 if ix and ix['oid'] in pointer_by_blob:
  ptr=pointer_by_blob[ix['oid']];lfs=ptr['remote_lfs_status']+';LOCAL_PAYLOAD_'+('SHA256_VERIFIED' if sha==ptr['sha256'] else 'UNVERIFIED');gitstatus='LFS_POINTER_ONLY_REMOTE_BYTES_UNVERIFIED';ref='|'.join(sorted(set(blobrefs[ix['oid']])));blob=ix['oid']
 if '/.git/lfs/objects/' in p and re.fullmatch('[0-9a-f]{64}',Path(p).name):lfs='LOCAL_LFS_PHYSICAL_OBJECT_NAME_ONLY_UNVERIFIED'
 maps=map_hash.get((sha,a['bytes']),[]) if sha else []
 direct=[m for m in maps if m['source']==p];m=(direct or maps or [{}])[0]
 good=bool(m.get('verified') and m.get('private'));gitretrieved=sha in retrieved
 cls='SOURCE_OR_EVIDENCE';risk='HIGH';status='LOCAL ONLY';why='No proven independent original-byte recovery copy';action='Owner source-specific preservation plan; hash any unresolved large source before future transfer'
 if a['category']=='dependency-cache':cls='REPRODUCIBLE_CANDIDATE';risk='LOW';status='PROVISIONALLY COVERED';why='Dependency/cache path; exact rebuild and version inputs not validated';action='Validate lockfiles/runtime reconstruction before declaring NOT REQUIRED'
 elif a['category']=='os-metadata':cls='OS_METADATA';risk='LOW';status='NOT REQUIRED';why='Finder view metadata; not YIOS research/production input';action='No preservation required for project recovery'
 elif a['category']=='git-internals':cls='GIT_RECOVERY_INTERNAL';risk='HIGH';status='PROVISIONALLY COVERED';why='Pack/ref/LFS recovery state may contain unique commits or stash; path bytes not unique source coverage';action='Preserve in place; reconcile unique commits/stash/LFS with owner before any new backup scope'
 elif '/YIOS-Research-Export-' in p:cls='DERIVED_EXPORT_WITH_EMBEDDED_SOURCE_COPIES';risk='MEDIUM';why='Export/source archives derived from multiple refs; independent recovery of this exact export not established';action='Recover underlying Git/LFS originals first; validate exact export regeneration or preserve unique source.gz records'
 elif 'selected-evidence-packages' in p or 'ct-evidence-packages' in p:cls='LOSSLESS_RECOVERY_PACKAGE';risk='MEDIUM'
 elif a['category'] in ['media','database'] or (a['root']==str(P) and tracked=='UNTRACKED_LOCAL'):risk='CRITICAL'
 if good:status='SAFE';risk='LOW';why='Full remote original SHA256 or exact decompressed member verified; current source identity/hash matches';action='Retain source and private receipts; test complete dependency restoration separately'
 elif ref and lfs=='NONE_DETECTED':status='SAFE' if gitretrieved else 'PROVISIONALLY COVERED';risk='LOW' if gitretrieved else 'MEDIUM';why='Normal Git blob content matches live advertised tree; '+('full independent byte retrieval recorded' if gitretrieved else 'current full byte retrieval not repeated for this blob');action='Use exact published commit/blob for recovery; independent clean restore still required'
 if a['dataless']:status='BLOCKED';risk='HIGH' if a['category'] in ['media','database','archive'] else 'MEDIUM';why='macOS SF_DATALESS placeholder; logical length is not local resident bytes or proven cloud recovery';action='Owner-approved iCloud original retrieval/hash under bounded separate scope; find checksum-identical resident/remote copy first'
 if a['kind']=='symlink':status='BLOCKED' if not Path(p).exists() else 'PROVISIONALLY COVERED';risk='HIGH' if not Path(p).exists() else 'LOW';why='Symlink recorded; target never followed; '+('target unavailable' if not Path(p).exists() else 'target dependency needs authorized root evidence');action='Restore link plus exact target; never infer target bytes from link'
 if lfs.startswith('LFS_POINTER_ONLY'):status='LOCAL ONLY';risk='CRITICAL';why='Git publishes pointer only; full remote LFS payload not independently verified';action='Owner-authorized exact LFS download verification or private payload backup; no LFS fetch during audit'
 asset=('sha256:'+sha+':'+str(a['bytes'])) if sha else 'path:'+hashlib.sha256(p.encode()).hexdigest();pathasset[p]=asset
 bc=bclaims.get(sha,[]) if sha else [];bs='MACHINE_B_HANDOFF_VERIFIED' if bc else 'MACHINE_B_NOT_ACCESSIBLE';ba='|'.join(sorted(set(b['authority'] for b in bc)))
 x=dict(zip(cols,['']*len(cols)));x.update(source_group=Path(a['root']).name,root_directory=a['root'],relative_path=rel,absolute_path=p,logical_asset_id=asset,file_type=a['extension'],classification=cls,local_machine_a_presence='DATALESS_PLACEHOLDER' if a['dataless'] else 'SYMLINK_ONLY' if a['kind']=='symlink' else 'MACHINE_A_VERIFIED',machine_a_size=a['bytes'],machine_a_sha256=sha,machine_a_hash_evidence=h['status']+';'+h['evidence'],machine_b_presence_evidence=bs,machine_b_evidence_authority=ba,git_tracked_status=gitstatus,git_commit_ref=ref,git_blob_sha1=blob,git_lfs_status=lfs,drive_remote_id=m.get('id',''),drive_folder=m.get('folder',''),drive_receipt_reference=m.get('receipt',''),archive_member_reference=m.get('member',''),independent_hash_verification_status=m.get('status','') if good else 'GIT_FULL_BYTES_RETRIEVAL_VERIFIED' if gitretrieved else 'REMOTE_TREE_MEMBERSHIP_ONLY' if ref else 'NOT_ESTABLISHED',duplicate_alias_group=asset if sha else '',original_recoverability='REMOTE_RECOVERY_VERIFIED' if good or gitretrieved else 'PROVISIONAL_GIT_CONTENT_ADDRESSED' if ref and lfs=='NONE_DETECTED' else 'BACKUP_GAP',privacy_sensitivity='PRIVATE_YIOS_RESEARCH_OWNER_ONLY',restore_test_status='NOT_TESTED_THIS_AUDIT',coverage_confidence='HIGH' if good or gitretrieved else 'BOUNDED_METADATA_OR_HISTORY',risk_level=risk,recommended_next_action=action,allocated_bytes=a['allocated_bytes'],device=a['device'],inode=a['inode'],nlink=a['nlink'],mtime_ns=a['mtime_ns'],dataless=a['dataless'],category=a['category'],drive_status=m.get('status','DRIVE_NOT_IN_APPROVED_SCOPE') if good else 'DRIVE_NOT_IN_APPROVED_SCOPE',coverage_status=status,risk_reason=why)
 result.append(x)
 if sha:shaassets[sha].append(x)
# Additional MachineB-only manifest-backed source identities deduped by content hash + length where known.
for sha,claims in bclaims.items():
 if sha in shaassets:continue
 c=claims[0];path=c['source'];rel=path[len(Broot)+1:] if path.startswith(Broot+'/') else path;remote=remotepaths.get(rel,[]);sz=c.get('bytes');m=(map_hash.get((sha,sz),[]) or [{}])[0] if sz is not None else {};good=bool(m.get('verified') and m.get('private'));x=dict(zip(cols,['']*len(cols)))
 x.update(source_group='MACHINE_B_HANDOFF_ONLY',root_directory=Broot if path.startswith(Broot) else str(Path(path).parent),relative_path=rel,absolute_path=path,logical_asset_id='sha256:'+sha+':'+str(sz if sz is not None else 'SIZE_UNKNOWN'),file_type=Path(path).suffix,classification='MANIFEST_BACKED_SOURCE',local_machine_a_presence='NOT_HASH_MATCHED_IN_CENSUS',machine_a_size='',machine_a_sha256=sha,machine_a_hash_evidence='SHA256_DECLARED_IN_MACHINE_B_HANDOFF; not MachineA source hash',machine_b_presence_evidence='MACHINE_B_HANDOFF_VERIFIED',machine_b_evidence_authority='|'.join(sorted(set(a['authority'] for a in claims))),git_tracked_status='REMOTE_PATH_PRESENT_CONTENT_SHA256_NOT_RECONCILED' if remote else 'UNAVAILABLE',git_commit_ref='|'.join(a[0]+':'+remotetrees[a[0]]['sha'] for a in remote),git_lfs_status='REMOTE_BYTES_UNVERIFIED',drive_remote_id=m.get('id',''),drive_folder=m.get('folder',''),drive_receipt_reference=m.get('receipt',''),archive_member_reference=m.get('member',''),independent_hash_verification_status=m.get('status','NOT_ESTABLISHED'),duplicate_alias_group='sha256:'+sha,original_recoverability='REMOTE_RECOVERY_VERIFIED' if good else 'BACKUP_GAP',privacy_sensitivity='PRIVATE_OWNER_ONLY',restore_test_status='NOT_TESTED',coverage_confidence='HISTORICAL_HANDOFF_ONLY',risk_level='LOW' if good else 'HIGH',recommended_next_action='MachineB owner fresh inventory/hash and independent original retrieval required; do not infer missing from MachineA absence',drive_status=m.get('status','DRIVE_NOT_IN_APPROVED_SCOPE'),coverage_status='SAFE' if good else 'PROVISIONALLY COVERED' if remote else 'BLOCKED',risk_reason='Historical MachineB fingerprint, no direct access; current byte availability not established')
 result.append(x)
# Write requested machine-readable artifact set.
def csvout(name,rr,cs=cols):
 with open(O/name,'x') as f:
  w=csv.DictWriter(f,fieldnames=cs,extrasaction='ignore');w.writeheader();w.writerows(rr)
csvout('ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv',result)
csvout('MACHINE_A_B_SOURCE_CROSSWALK.csv',result)
csvout('DRIVE_BACKUP_COVERAGE_MATRIX.csv',result)
csvout('GITHUB_AND_LFS_RECOVERY_STATUS.csv',[x for x in result if x['git_commit_ref'] or x['git_tracked_status'] in ['TRACKED','UNTRACKED_LOCAL','IGNORED_LOCAL_SOURCE','GIT_INTERNAL']])
# Folder coverage: root plus every directory subtree, non-additive rollups explicitly labelled.
folder=collections.defaultdict(list)
for x in result:
 if x['source_group']=='MACHINE_B_HANDOFF_ONLY':continue
 root=x['root_directory'];rel=Path(x['relative_path']);folder[(root,'.')].append(x)
 for i in range(1,len(rel.parts)):folder[(root,str(Path(*rel.parts[:i])))].append(x)
fr=[]
for (root,rel),rr in sorted(folder.items()):
 dirs=sum(a['kind']=='directory' and a['root']==root and (rel=='.' or a['relative']==rel or a['relative'].startswith(rel+'/')) for a in rows)
 counts=collections.Counter(x['coverage_status'] for x in rr);fr.append({'root_directory':root,'relative_directory':rel,'scope':'FULL_METADATA_CENSUS_SUBTREE_NONADDITIVE','file_and_link_count':len(rr),'directory_count':dirs,'logical_bytes':sum(int(x['machine_a_size']) for x in rr),'allocated_path_bytes':sum(int(x['allocated_bytes']) for x in rr),'allocated_unique_inode_bytes':sum({(x['device'],x['inode']):int(x['allocated_bytes']) for x in rr}.values()),'dataless_count':sum(x['dataless'] for x in rr),'safe_count':counts['SAFE'],'provisional_count':counts['PROVISIONALLY COVERED'],'local_only_count':counts['LOCAL ONLY'],'blocked_count':counts['BLOCKED'],'not_required_count':counts['NOT REQUIRED'],'media_count':sum(x['category']=='media' for x in rr),'large_media_ge_100MB_count':sum(x['category']=='media' and int(x['machine_a_size'])>=100_000_000 for x in rr),'database_count':sum(x['category']=='database' for x in rr),'archive_count':sum(x['category']=='archive' for x in rr),'symlink_count':sum(x['local_machine_a_presence']=='SYMLINK_ONLY' for x in rr),'hardlinked_paths':sum(int(x['nlink'])>1 for x in rr),'file_types':json.dumps(dict(collections.Counter(x['file_type'] for x in rr)),sort_keys=True),'coverage_status':'FULLY_BACKED_UP_VERIFIED' if counts['SAFE']==len(rr) else 'PARTIAL_OR_UNVERIFIED','classification_note':'Metadata complete does not mean every byte read; dataless counts are placeholders; overlapping subtree rows must never be summed'})
csvout('FOLDER_BY_FOLDER_COVERAGE.csv',fr,list(fr[0]))
dups=[]
for sha,rr in shaassets.items():
 if len(rr)>1:dups.append({'group':'sha256:'+sha,'basis':'EXACT_SHA256_AND_SIZE','paths':json.dumps([x['absolute_path'] for x in rr]),'path_count':len(rr),'source_bytes_once':rr[0]['machine_a_size'],'same_inode_count':len(set((x['device'],x['inode']) for x in rr)),'additional_unique_coverage':0,'action':'Preserve all copies; no deletion authorized'})
for a in files:
 if a['kind']=='symlink':dups.append({'group':a['path'],'basis':'SYMLINK_NOT_FOLLOWED','paths':json.dumps([a['path'],a['symlink_target']]),'path_count':1,'additional_unique_coverage':0,'action':'Target separately checked; never count link as target bytes'})
dups.append({'group':'BATCH31_APPROVED_EXTRA','basis':'INDEPENDENT_REMOTE_SHA256','paths':json.dumps(['1_I0MqlstrAynSWTsPnOTuZOzr5eueJtv','127DXG7Ih9tw61aFNGL0tGzwt4dc0no_A']),'path_count':2,'source_bytes_once':404830,'additional_unique_coverage':0,'action':'Keep both unchanged; exact uploader attribution remains UNRESOLVED'})
csvout('DUPLICATES_ALIASES_AND_OVERLAPS.csv',dups,sorted(set(k for x in dups for k in x)))
risks=[x for x in result if x['coverage_status'] not in ['SAFE','NOT REQUIRED'] and x['category'] not in ['dependency-cache','os-metadata']]
csvout('MISSING_CRITICAL_ASSETS.csv',risks)
stats={'metadata_regular_files':sum(x['kind']=='regular' for x in rows),'metadata_symlinks':sum(x['kind']=='symlink' for x in rows),'metadata_directories':sum(x['kind']=='directory' for x in rows),'logical_path_bytes':sum(x['bytes'] for x in rows if x['kind']=='regular'),'dataless_files':sum(x['dataless'] for x in files),'dataless_logical_bytes':sum(x['bytes'] for x in files if x['dataless']),'machine_b_additional_content_identities':sum(x['source_group']=='MACHINE_B_HANDOFF_ONLY' for x in result),'machine_b_direct_access':False,'coverage_rows':len(result),'coverage_status':dict(collections.Counter(x['coverage_status'] for x in result)),'risk_levels':dict(collections.Counter(x['risk_level'] for x in risks)),'known_sha256_content_identities':len(shaassets),'hash_bytes_read':hashbytes,'lfs_pointer_identities':len(pointer_by_blob),'drive_unique_source_paths':len(map_path),'drive_representations':sum(len(x) for x in map_path.values()),'source_census_non_atomic':True}
important=[x for x in result if x['source_group']!='MACHINE_B_HANDOFF_ONLY' and x['category'] not in ['git-internals','dependency-cache','os-metadata'] and x['local_machine_a_presence']!='SYMLINK_ONLY']
stats['important_path_count']=len(important);stats['important_logical_bytes']=sum(int(x['machine_a_size']) for x in important);stats['important_resident_bytes']=sum(int(x['machine_a_size']) for x in important if not x['dataless']);stats['important_status']=dict(collections.Counter(x['coverage_status'] for x in important));stats['git_pushed_matching_local_files']=sum(x['git_tracked_status']=='PUSHED_GIT_BLOB' for x in result);stats['git_pushed_matching_local_bytes']=sum(int(x['machine_a_size']) for x in result if x['git_tracked_status']=='PUSHED_GIT_BLOB' and x['machine_a_size']!='');stats['drive_matched_local_paths']=sum(bool(x['drive_remote_id']) and x['source_group']!='MACHINE_B_HANDOFF_ONLY' for x in result)
dump('checkpoints/STAGE4_SUMMARY.json',stats);print(json.dumps(stats,indent=2))
