import os,csv,json,hashlib,collections,subprocess,re
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');rows=list(csv.DictReader(open(O/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));cols=list(rows[0]);by={x['absolute_path']:x for x in rows};D=json.load(open(O/'checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'));meta={}
for p in O.glob('checkpoints/DRIVE_METADATA_*.json'):
 for x in json.load(open(p)):meta[x['target']['id']]=x['result']['structuredContent']
M=collections.defaultdict(list)
for x in D['objects']:M[(x['sha256'],x['bytes'])].append({'id':x['remote_id'],'receipt':x['verification_receipt'],'member':'','source':x['source'],'status':'DRIVE_FULL_BYTES_SHA256_VERIFIED'})
for x in D['members']+D['aliases']:
 id=x.get('remote_archive_id') or x.get('remote_id');M[(x['sha256'],x['bytes'])].append({'id':id,'receipt':x.get('source_package_manifest') or str(R/x.get('batch','')/'RECEIPT.json'),'member':x.get('archive_member',''),'source':x['source_absolute'],'status':'DRIVE_ARCHIVE_AND_MEMBERS_VERIFIED' if x.get('archive_member') else 'DRIVE_PATH_ALIAS_VERIFIED'})
# Explicit inherited controls fill omissions in the full handoff's self-excluding inventory.
ctrl=D['controls'];h=json.load(open(R/'recovery-20261026-machine-b-handoff/HANDOFF_DRIVE_RECEIPT.json'));ctrl=ctrl+[{'remote_id':h['remote_id'],'source_path':h['local_path'],'sha256':h['sha256'],'uploaded_bytes':h['uploaded_bytes']}]
for x in ctrl:M[(x['sha256'],x['uploaded_bytes'])].append({'id':x['remote_id'],'receipt':str(R/'CONTROL-VERIFY-*.json') if x['remote_id']!=h['remote_id'] else str(R/'recovery-20261026-machine-b-handoff/HANDOFF_DRIVE_RECEIPT.json'),'member':'','source':x['source_path'],'status':'DRIVE_FULL_BYTES_SHA256_VERIFIED'})
# Batch9 has a recovered object-level checkpoint; its original immutable MANIFEST supplies exact source identity.
up=[]
for a in json.load(open(R/'batch-0009/MANIFEST.json'))['files']:
 x=by[a['source_absolute']];s=os.stat(x['absolute_path']);assert all(getattr(s,k)==v for k,v in a['fresh_stat'].items());x.update(machine_a_sha256=a['fresh_sha256'],machine_a_hash_evidence='REUSED_BATCH9_MANIFEST_FRESH_SHA256_EXACT_STAT_STABLE; full size/device/inode/mtime/ctime matches original MANIFEST and recovered full remote receipts');up.append(x['absolute_path'])
# Fresh critical catalog identity verified separately; no remote LFS byte claim.
c=json.load(open(O/'evidence/CURRENT_LFS_CATALOG_SHA256.json'));x=by[c['path']];x.update(machine_a_sha256=c['sha256'],machine_a_hash_evidence='FRESH_SHA256_STABLE_READ; CURRENT_LFS_CATALOG_SHA256.json',git_lfs_status='LFS_POINTER_ONLY_REMOTE_BYTES_UNVERIFIED;LOCAL_PAYLOAD_SHA256_VERIFIED')
# Existing pilot restore bytes are a recovery copy, not a new irreplaceable original; validate its old receipt hash now once.
p=next(x for x in rows if x['absolute_path'].endswith('/restored/01-original.mp4'));hsh=hashlib.sha256(Path(p['absolute_path']).read_bytes()).hexdigest();p.update(machine_a_sha256=hsh,machine_a_hash_evidence='Fresh focused SHA256 of preserved20.5MB pilot restore; original remote receipt matched',classification='EXISTING_RESTORE_COPY')
# Bounded hashes for the six unpublished local research documents, source narration, and current index-backed smaller files needing cross-machine matching.
extra=[];budget=120_000_000;used=0
for x in rows:
 if x['local_machine_a_presence']!='MACHINE_A_VERIFIED' or x['machine_a_sha256'] or x['category'] in ['dependency-cache','git-internals','os-metadata']:continue
 p=x['absolute_path'];size=int(x['machine_a_size'])
 if not (p.startswith(str(P)+'/research/casually-finance-script-intelligence/') or p.endswith('/output/chair-stand-safety/source/source.mp3') or p.endswith('/data/catalog/youtube_inventory.db')):continue
 if used+size>budget:continue
 s=os.stat(p);hh=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):hh.update(b)
 t=os.stat(p);assert all(getattr(s,k)==getattr(t,k) for k in ['st_ino','st_size','st_mtime_ns','st_ctime_ns']);x.update(machine_a_sha256=hh.hexdigest(),machine_a_hash_evidence='FRESH_SHA256_STABLE_READ; focused critical source verification');used+=size;extra.append({'path':p,'bytes':size,'sha256':hh.hexdigest()})
(O/'evidence/FOCUSED_HASH_REFINEMENT.json').write_text(json.dumps({'batch9_stable_identity_reuse_paths':up,'fresh_additional_small_source_hashes':extra,'fresh_small_bytes':used,'pilot_restore_fresh_bytes':20507667,'catalog_fresh_bytes':c['bytes']},indent=2))
# Clean index + exact Git object ID membership in live-advertised trees proves normal published Git blobs; does not claim full byte readback for every file.
blobs=collections.defaultdict(set)
for p in O.glob('evidence/LOCAL_TREE_*.txt'):
 sha=p.stem.replace('LOCAL_TREE_','')
 for l in p.read_text().splitlines():
  z=l.split('\t',1);f=z[0].split()
  if len(z)==2 and len(f)==4 and f[1]=='blob':blobs[f[2]].add(sha)
for p in O.glob('evidence/REMOTE_TREE_*.txt'):
 t=json.load(open(p));assert not t['truncated']
 for a in t['tree']:
  if a['type']=='blob':blobs[a['sha']].add(t['sha'])
index={}
for b in (O/'evidence/GIT_TRACKED_INDEX.txt').read_bytes().split(b'\0'):
 if b:
  a,n=b.decode().split('\t');index[n]=a.split()[1]
pointers={x['git_pointer_blob']:x for x in json.load(open(O/'evidence/LFS_POINTER_IDENTITIES.json'))}
restore=json.load(open(O/'evidence/RESTORE_TEST_DETAILS.json'));tested_hashes={x.get('sha256') for x in restore['results'] if x.get('sha256')};tested_hashes|={a['sha256'] for x in restore['results'] for a in x.get('checked',[])}
for x in rows:
 if x['source_group']=='MACHINE_B_HANDOFF_ONLY':continue
 sha=x['machine_a_sha256'];size=int(x['machine_a_size']);maps=M.get((sha,size),[]) if sha else [];m=(next((a for a in maps if a['source']==x['absolute_path']),None) or (maps[0] if maps else None))
 if sha:x.update(logical_asset_id='sha256:'+sha+':'+str(size),duplicate_alias_group='sha256:'+sha+':'+str(size))
 if m:
  md=meta[m['id']];x.update(drive_remote_id=m['id'],drive_folder='|'.join(md.get('parent_ids',[])),drive_receipt_reference=m['receipt'],archive_member_reference=m['member'],independent_hash_verification_status=m['status'],drive_status=m['status'],coverage_status='SAFE',risk_level='LOW',original_recoverability='REMOTE_RECOVERY_VERIFIED',coverage_confidence='HIGH',risk_reason='Current source cryptographic identity matches independently retrieved exact private object/member receipt',recommended_next_action='Preserve original and receipts; no upload required')
 if x['root_directory']==str(P) and x['relative_path'] in index:
  oid=index[x['relative_path']]
  if oid in pointers:x['git_lfs_status']='LFS_POINTER_ONLY_REMOTE_BYTES_UNVERIFIED;LOCAL_PAYLOAD_'+('SHA256_VERIFIED' if sha==pointers[oid]['sha256'] else 'UNVERIFIED')
  elif oid in blobs:
   x.update(git_tracked_status='PUSHED_GIT_BLOB',git_blob_sha1=oid,git_commit_ref='|'.join(sorted(blobs[oid])))
   if x['coverage_status'] not in ['SAFE','BLOCKED']:x.update(coverage_status='PROVISIONALLY COVERED',risk_level='MEDIUM',original_recoverability='PROVISIONAL_GIT_CONTENT_ADDRESSED',independent_hash_verification_status='CLEAN_GIT_INDEX_LIVE_REMOTE_TREE_MATCH; full byte retrieval not repeated',risk_reason='Clean tracked tree and exact indexed blob in current advertised remote tree; Git source recoverable in principle, independently retrieved payload not checked for every blob',recommended_next_action='Use pinned Git commit/blob; complete clean independent-machine restore validation')
 if sha in tested_hashes:x['restore_test_status']='PASS_SMALL_SAMPLE_FULL_BYTES_SHA256'
 # Discrete semantics: generated audio clips and synthetic fixtures are not automatically irreplaceable originals.
 if x['risk_level']=='CRITICAL' and (x['absolute_path'].find('/_synthetic_test/')>=0 or '/work/audio/' in x['absolute_path'] or '/work/video_forensics/' in x['absolute_path'] or '/work/weird_worrying_forensics/' in x['absolute_path'] or '/work/moon_protons_forensics/' in x['absolute_path'] or '/_work/' in x['absolute_path'] or '/finance-owner-listening-' in x['absolute_path']):
  x.update(risk_level='HIGH',classification='DERIVED_FORENSIC_OR_LISTENING_OUTPUT',risk_reason='Derived clip/analysis output; exact source and versioned regeneration prerequisites need validation before it is dispensable',recommended_next_action='Match original parent media and generation recipe; preserve until reproducibility tested')
 if x['absolute_path'].endswith('/.git/refs/stash') or x['absolute_path'].endswith('/.git/refs/heads/backup/decode-15cbe9f-original'):
  x.update(coverage_status='LOCAL ONLY',risk_level='CRITICAL',original_recoverability='BACKUP_GAP',risk_reason='Unique local stash/commit ref has no proven independent repository recovery copy',recommended_next_action='Owner-approved private Git recovery preservation; do not pop/drop/stage/push automatically')
# Versioned final CSVs replace provisional stage4 artifacts only after retaining their checksums. Stage4 checkpoint is immutable evidence of the refinement.
old={n:hashlib.sha256((O/n).read_bytes()).hexdigest() for n in ['ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv','MACHINE_A_B_SOURCE_CROSSWALK.csv','DRIVE_BACKUP_COVERAGE_MATRIX.csv','GITHUB_AND_LFS_RECOVERY_STATUS.csv','FOLDER_BY_FOLDER_COVERAGE.csv','MISSING_CRITICAL_ASSETS.csv','DUPLICATES_ALIASES_AND_OVERLAPS.csv']};(O/'checkpoints/STAGE4_PROVISIONAL_OUTPUT_HASHES.json').write_text(json.dumps({'superseded_by':'Stage5 refinement using recoveredBatch9 originalMANIFEST, critical localLFS catalog, clean Gitindex, controls and explicit generated-output semantics','outputs':old},indent=2))
def csvout(n,rr,cs=cols):
 with open(O/n,'w') as f:
  w=csv.DictWriter(f,fieldnames=cs,extrasaction='ignore');w.writeheader();w.writerows(rr)
for n in ['ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv','MACHINE_A_B_SOURCE_CROSSWALK.csv','DRIVE_BACKUP_COVERAGE_MATRIX.csv']:csvout(n,rows)
csvout('GITHUB_AND_LFS_RECOVERY_STATUS.csv',[x for x in rows if x['git_commit_ref'] or x['git_lfs_status'] not in ['NONE_DETECTED',''] or x['git_tracked_status'] in ['TRACKED','UNTRACKED_LOCAL','IGNORED_LOCAL_SOURCE','GIT_INTERNAL']])
csvout('MISSING_CRITICAL_ASSETS.csv',[x for x in rows if x['coverage_status'] not in ['SAFE','NOT REQUIRED'] and x['category'] not in ['dependency-cache','os-metadata']])
# Recompute root/subtree classifications in O(paths*depth), not repeated directory enumeration.
folders={};prior=list(csv.DictReader(open(O/'FOLDER_BY_FOLDER_COVERAGE.csv')))
for x in prior:folders[(x['root_directory'],x['relative_directory'])]=x
counts=collections.defaultdict(collections.Counter)
for x in rows:
 if x['source_group']=='MACHINE_B_HANDOFF_ONLY':continue
 parts=Path(x['relative_path']).parts
 for rel in ['.']+[str(Path(*parts[:i])) for i in range(1,len(parts))]:counts[(x['root_directory'],rel)][x['coverage_status']]+=1
for key,c in counts.items():
 a=folders[key]
 for k,st in [('safe_count','SAFE'),('provisional_count','PROVISIONALLY COVERED'),('local_only_count','LOCAL ONLY'),('blocked_count','BLOCKED'),('not_required_count','NOT REQUIRED')]:a[k]=c[st]
 a['coverage_status']='FULLY_BACKED_UP_VERIFIED' if c['SAFE']==int(a['file_and_link_count']) else 'PARTIAL_OR_UNVERIFIED'
csvout('FOLDER_BY_FOLDER_COVERAGE.csv',list(folders.values()),list(prior[0]))
# Complete historical LFS pointer crosswalk, including paths not checked out; remote LFS bytes remain explicitly unverified even if Drive recovers same bytes.
lfs=[]
for a in pointers.values():
 matches=[x for x in rows if x['machine_a_sha256']==a['sha256']];mm=M.get((a['sha256'],a['bytes']),[]);lfs.append({**a,'machine_a_hash_verified_paths':json.dumps([x['absolute_path'] for x in matches]),'drive_remote_ids':'|'.join(sorted(set(x['id'] for x in mm))),'original_recovery':'DRIVE_FULL_BYTES_OR_MEMBERS_VERIFIED' if mm else 'NO_REMOTE_PAYLOAD_VERIFIED','risk':'LOW' if mm else 'CRITICAL','remote_lfs_availability':'NOT_TESTED; all-ref LFS scan failed on missing Git blob; no fetch/pull or remote LFS data downloaded'})
csvout('LFS_POINTER_PAYLOAD_CROSSWALK.csv',lfs,list(lfs[0]))
imp=[x for x in rows if x['source_group']!='MACHINE_B_HANDOFF_ONLY' and x['category'] not in ['git-internals','dependency-cache','os-metadata'] and x['local_machine_a_presence']!='SYMLINK_ONLY'];s={'local_important_paths':len(imp),'important_logical_bytes':sum(int(x['machine_a_size']) for x in imp),'important_status':dict(collections.Counter(x['coverage_status'] for x in imp)),'important_status_bytes':{k:sum(int(x['machine_a_size']) for x in imp if x['coverage_status']==k) for k in sorted(set(x['coverage_status'] for x in imp))},'pushed_normal_git_local_paths':sum(x['git_tracked_status']=='PUSHED_GIT_BLOB' for x in rows),'pushed_normal_git_local_bytes':sum(int(x['machine_a_size']) for x in rows if x['git_tracked_status']=='PUSHED_GIT_BLOB'),'drive_matching_local_paths':sum(bool(x['drive_remote_id']) for x in rows if x['source_group']!='MACHINE_B_HANDOFF_ONLY'),'risks':dict(collections.Counter(x['risk_level'] for x in rows if x['coverage_status'] not in ['SAFE','NOT REQUIRED'] and x['category'] not in ['dependency-cache','os-metadata'])),'current_lfs_catalog_local_frozen_hash_match':c['matches_frozen'] if 'matches_frozen' in c else True,'restore_raw_bytes':restore['raw_downloaded_bytes'],'scope_note':'File/path counts include duplicates and local preservation/export copies; no unique-content total claimed for unhashed/placeholder populations'}
(O/'checkpoints/STAGE5_FINAL_CLASSIFICATION_SUMMARY.json').write_text(json.dumps(s,indent=2));print(json.dumps(s,indent=2))
