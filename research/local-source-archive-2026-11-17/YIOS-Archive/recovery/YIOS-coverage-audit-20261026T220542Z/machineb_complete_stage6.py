import json,csv,collections,hashlib
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd');rows=list(csv.DictReader(open(O/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));cols=list(rows[0])+['machine_b_size','machine_b_source_paths','machine_b_evidence_date'];sources=[];B='/Users/ghilmanislam360/Documents/youtube-intelligence-os';d=json.load(open(O/'evidence/FINANCE_MANIFEST_01.json'))
for x in d['sources']:sources.append({'path':x['path'],'sha256':x['sha256'],'bytes':x.get('bytes'),'date':'2026-10-23','authority':'FINANCE_MANIFEST_01.json:sources;333 declared source fingerprints','category':'FINANCE_RESEARCH_SOURCE'})
for x in d['all_registered_image_hashes']+d['competitor_visual_samples']:sources.append({'path':x.get('path') or x.get('image_path'),'sha256':x.get('sha256') or x.get('image_sha256'),'bytes':None,'date':'2026-10-23','authority':'FINANCE_MANIFEST_01.json:registered thumbnail hashes','category':'FINANCE_THUMBNAIL'})
for x in [json.loads(a) for a in (O/'evidence/MEDIA_LIBRARY_01.jsonl').read_text().splitlines()]:sources.append({'path':x['external_source_path'],'library_path':B+'/'+x['local_media_path'],'sha256':x['sha256'],'bytes':int(x['byte_count']),'date':'2026-10-21T09:26:31+05:00 registry commit; handoff2026-10-23','authority':'MEDIA_LIBRARY_01.jsonl;live ref78e8fd2; SOURCE_MANIFEST_SHA256.json verified','category':'MACHINE_B_ORIGINAL_MEDIA'})
for path,h in json.load(open(O/'evidence/FINANCE_MANIFEST_00.json'))['source_hashes'].items():sources.append({'path':B+'/'+path,'sha256':h,'bytes':None,'date':'Frozen2026-10-16;MachineB confirmation2026-10-23','authority':'FINANCE_MANIFEST_00.json:26 immutable fingerprints','category':'FROZEN_FINANCE_INPUT'})
for x in json.load(open(O/'evidence/FINANCE_MANIFEST_02.json'))['external_only_files']:sources.append({'path':x['historical_machine_b_path'],'sha256':x['sha256'],'bytes':x['bytes'],'date':'2026-10-23','authority':'FINANCE_MANIFEST_02.json:external_only_files; '+x['reason'],'category':'MACHINE_B_EXTERNAL_SUPPORT'})
# Source registry checksum independently matches live Git blob bytes available locally.
manifest=json.load(open(O/'evidence/MEDIA_LIBRARY_03.json'));mh=hashlib.sha256((O/'evidence/MEDIA_LIBRARY_01.jsonl').read_bytes()).hexdigest();assert mh==manifest['SOURCE_INVENTORY.jsonl']
bs=collections.defaultdict(list)
for s in sources:bs[s['sha256']].append(s)
# Hash-key Git blob provenance from the earlier exact-blob source export, reconciled with fresh advertised trees.
blobrefs=collections.defaultdict(set)
for p in O.glob('evidence/LOCAL_TREE_*.txt'):
 sha=p.stem.replace('LOCAL_TREE_','')
 for line in p.read_text().splitlines():
  z=line.split('\t',1);f=z[0].split()
  if len(z)==2 and len(f)==4 and f[1]=='blob':blobrefs[f[2]].add(sha)
for p in O.glob('evidence/REMOTE_TREE_*.txt'):
 t=json.load(open(p))
 for x in t['tree']:
  if x['type']=='blob':blobrefs[x['sha']].add(t['sha'])
sha2git={}
for x in json.load(open('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21/SOURCE_INDEX.json')):
 if x.get('sha256') and x.get('blob') in blobrefs:sha2git[x['sha256']]={'blob':x['blob'],'refs':sorted(blobrefs[x['blob']])}
localsha={x['machine_a_sha256'] for x in rows if x['local_machine_a_presence']=='MACHINE_A_VERIFIED' and x['machine_a_sha256']};existing={x['machine_a_sha256'] for x in rows};base=rows[0]
for sha,ss in bs.items():
 if sha not in existing:
  s=ss[0];sz=next((x['bytes'] for x in ss if x['bytes'] is not None),None);x={k:'' for k in cols};x.update(source_group='MACHINE_B_HANDOFF_ONLY',root_directory=str(Path(s['path']).parent),relative_path=Path(s['path']).name,absolute_path=s['path'],logical_asset_id='sha256:'+sha+':'+str(sz if sz is not None else 'SIZE_UNKNOWN'),file_type=Path(s['path']).suffix,classification='MANIFEST_BACKED_SOURCE',local_machine_a_presence='NOT_HASH_MATCHED_IN_CENSUS',machine_a_sha256=sha,machine_a_hash_evidence='MACHINE_B_DECLARED_SOURCE_HASH;notMachineA bytes',machine_b_presence_evidence='MACHINE_B_HANDOFF_VERIFIED',git_tracked_status='UNAVAILABLE',git_lfs_status='REMOTE_BYTES_UNVERIFIED',independent_hash_verification_status='NOT_ESTABLISHED',original_recoverability='BACKUP_GAP',privacy_sensitivity='PRIVATE_OWNER_ONLY',restore_test_status='NOT_TESTED',coverage_confidence='HISTORICAL_HANDOFF_ONLY',risk_level='MEDIUM' if s['category']=='MACHINE_B_EXTERNAL_SUPPORT' else 'HIGH',recommended_next_action='MachineB owner fresh bounded source census and independent copy verification; no source writes authorized',drive_status='DRIVE_NOT_IN_APPROVED_SCOPE',coverage_status='BLOCKED',risk_reason='Manifest records exact historical bytes; no directMachineB source or remote full bytes checked');rows.append(x)
for x in rows:
 sha=x['machine_a_sha256'];ss=bs.get(sha,[]);sz=next((a['bytes'] for a in ss if a['bytes'] is not None),None)
 x.update(machine_b_size=sz if sz is not None else '',machine_b_source_paths=json.dumps(sorted(set(a['path'] for a in ss)),ensure_ascii=False) if ss else '',machine_b_evidence_date='|'.join(sorted(set(a['date'] for a in ss))))
 if ss:x['machine_b_evidence_authority']='|'.join(sorted(set(a['authority'] for a in ss)));x['machine_b_presence_evidence']='MACHINE_B_HANDOFF_VERIFIED'
 if x['source_group']=='MACHINE_B_HANDOFF_ONLY' and sha in sha2git:
  g=sha2git[sha];x.update(git_tracked_status='PUSHED_GIT_BLOB',git_blob_sha1=g['blob'],git_commit_ref='|'.join(g['refs']),coverage_status='PROVISIONALLY COVERED',risk_level='MEDIUM',original_recoverability='PROVISIONAL_GIT_CONTENT_ADDRESSED',independent_hash_verification_status='HISTORICAL_SOURCE_SHA256_TO_GIT_BLOB_LIVE_TREE_MATCH',risk_reason='Historical sourceSHA256 maps to exactGitblob present in a fresh advertised tree; full current byte retrieval and MachineB source access not performed')
def write(n,rr,cc=cols):
 with open(O/n,'w') as f:w=csv.DictWriter(f,fieldnames=cc,extrasaction='ignore');w.writeheader();w.writerows(rr)
for n in ['ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv','MACHINE_A_B_SOURCE_CROSSWALK.csv','DRIVE_BACKUP_COVERAGE_MATRIX.csv']:write(n,rows)
write('GITHUB_AND_LFS_RECOVERY_STATUS.csv',[x for x in rows if x['git_commit_ref'] or x['git_lfs_status'] not in ['NONE_DETECTED',''] or x['git_tracked_status'] in ['TRACKED','UNTRACKED_LOCAL','IGNORED_LOCAL_SOURCE','GIT_INTERNAL']]);write('MISSING_CRITICAL_ASSETS.csv',[x for x in rows if x['coverage_status'] not in ['SAFE','NOT REQUIRED'] and x['category'] not in ['dependency-cache','os-metadata']])
# One row per historical manifest source path, with dedup logical IDs; all source bytes stay historical.
allrows=[]
for s in sources:
 matches=[x for x in rows if x['machine_a_sha256']==s['sha256'] and x['source_group']!='MACHINE_B_HANDOFF_ONLY'];maps=[x for x in matches if x['drive_remote_id']];g=sha2git.get(s['sha256'],{});allrows.append({**s,'logical_asset_id':'sha256:'+s['sha256'],'machine_b_status':'MACHINE_B_HANDOFF_VERIFIED','machine_b_direct_access':False,'machine_a_hash_matched_paths':json.dumps([x['absolute_path'] for x in matches]),'drive_remote_ids':'|'.join(sorted(set(x['drive_remote_id'] for x in maps))),'git_blob':g.get('blob',''),'git_refs':'|'.join(g.get('refs',[])),'source_current_availability':'MACHINE_B_NOT_ACCESSIBLE','recovery_status':'REMOTE_RECOVERY_VERIFIED' if maps else 'PROVISIONAL_GIT_CONTENT_ADDRESSED' if g else 'BACKUP_GAP'})
write('MACHINE_B_MANIFEST_SOURCE_IDENTITIES.csv',allrows,sorted(set(k for x in allrows for k in x)))
unique={sha:next((x['bytes'] for x in ss if x['bytes'] is not None),None) for sha,ss in bs.items()};bextra={sha:sz for sha,sz in unique.items() if sha not in localsha};media=[x for x in allrows if x['category']=='MACHINE_B_ORIGINAL_MEDIA'];out={'manifest_path_representations':len(sources),'deduplicated_manifest_hash_identities':len(bs),'known_size_identities':sum(x is not None for x in unique.values()),'known_size_bytes':sum(x for x in unique.values() if x is not None),'unknown_size_identities':sum(x is None for x in unique.values()),'hash_overlap_machine_a_identities':sum(sha in localsha for sha in bs),'additional_not_hashmatched_machine_a_identities':len(bextra),'additional_known_bytes':sum(x for x in bextra.values() if x is not None),'additional_unknown_size_identities':sum(x is None for x in bextra.values()),'historical_media_paths':len(media),'historical_media_logical_bytes':sum(x['bytes'] for x in media),'historical_media_drive_covered_paths':sum(bool(x['drive_remote_ids']) for x in media),'historical_media_current_machine_a_hash_overlap_paths':sum(x['machine_a_hash_matched_paths']!='[]' for x in media),'MachineB_directly_scanned_files':0,'current_unpublished_MachineB_data':'UNAVAILABLE; no total can be inferred','dates_correction':'MEDIA_LIBRARY registry commit is2026-10-21T09:26:31+05:00; earlierStage4draft2026-10-20 label superseded by exactGitcommitdate; latest authority handoff2026-10-23'};(O/'evidence/MACHINE_B_COVERAGE_SUMMARY.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
