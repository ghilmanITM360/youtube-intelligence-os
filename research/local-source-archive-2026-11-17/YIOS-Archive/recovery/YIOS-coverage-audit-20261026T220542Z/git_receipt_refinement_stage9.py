from pathlib import Path
import json,csv,collections
O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-machine-a-phase1b');receipts={};arc=[]
for n in range(1,5):
 p=A/('BATCH%d_PUBLICATION_RECEIPT.json'%n);d=json.load(open(p));assert 'REMOTE_RETRIEVED' in d['status']
 for x in d['files']:
  oid=x.get('remote_blob_sha1') or x.get('remote_git_blob_sha1');h=x.get('sha256');assert oid and h
  receipts[oid]={'sha256':h,'bytes':int(x['bytes']),'receipt':str(p),'commit':d['commit']}
 arc.append({'batch':n,'files':len(d['files']),'bytes':sum(int(x['bytes']) for x in d['files']),'receipt':str(p)})
for x in json.load(open('/Users/ghilmankhan/YIOS-local-audits/2026-10-25-machine-a-phase0/remote-retrieval-verification.json')):
 if x.get('status')=='PASS':receipts[x['git_blob_sha1']]={'sha256':x['retrieved_sha256'],'bytes':x['retrieved_bytes'],'receipt':'phase0/remote-retrieval-verification.json','commit':x['live_ref']}
for p in list(O.glob('evidence/FINANCE_AUTHORITY_*.json'))+list(O.glob('evidence/FINANCE_MANIFEST_*.receipt.json')):
 d=json.load(open(p));receipts[d['git_blob_sha1']]={'sha256':d['sha256'],'bytes':d['bytes'],'receipt':str(p),'commit':d['commit']}
for x in json.load(open(O/'evidence/RESTORE_TEST_DETAILS.json'))['results']:
 if x['category']=='TRACKED_GIT_RESEARCH_ARTIFACT':receipts[x['git_blob_sha1']]={'sha256':x['sha256'],'bytes':x['recovered_bytes'],'receipt':'RESTORE_TEST_DETAILS.json','commit':x['remote_commit']}
rows=list(csv.DictReader(open(O/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));cols=list(rows[0]);updated=0
for x in rows:
 r=receipts.get(x['git_blob_sha1'])
 if r and x['git_tracked_status']=='PUSHED_GIT_BLOB' and x['coverage_status']!='SAFE' and x['local_machine_a_presence']!='DATALESS_PLACEHOLDER':
  x.update(coverage_status='SAFE',risk_level='LOW',original_recoverability='REMOTE_RECOVERY_VERIFIED',independent_hash_verification_status='GIT_FULL_BYTES_SHA256_RETRIEVAL_VERIFIED; '+r['receipt'],coverage_confidence='HIGH_EXACT_GIT_BLOB_AND_RETRIEVAL_RECEIPT',risk_reason='Exact content-addressed Git blob independently retrieved and SHA256 verified in preserved receipt; live advertised tree still contains identical blob',recommended_next_action='Use exact published blob/commit; preserve separate external media dependencies');updated+=1
 if r and x['git_blob_sha1']:x['recorded_source_sha256']=r['sha256']
def write(n,rs,cc=cols):
 with open(O/n,'w') as f:w=csv.DictWriter(f,fieldnames=cc,extrasaction='ignore');w.writeheader();w.writerows(rs)
for n in ['ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv','MACHINE_A_B_SOURCE_CROSSWALK.csv','DRIVE_BACKUP_COVERAGE_MATRIX.csv']:write(n,rows)
write('GITHUB_AND_LFS_RECOVERY_STATUS.csv',[x for x in rows if x['git_commit_ref'] or x['git_lfs_status'] not in ['NONE_DETECTED',''] or x['git_tracked_status'] in ['TRACKED','UNTRACKED_LOCAL','IGNORED_LOCAL_SOURCE','GIT_INTERNAL']]);write('MISSING_CRITICAL_ASSETS.csv',[x for x in rows if x['coverage_status'] not in ['SAFE','NOT REQUIRED'] and x['category'] not in ['dependency-cache','os-metadata']])
f=list(csv.DictReader(open(O/'FOLDER_BY_FOLDER_COVERAGE.csv')));c=collections.defaultdict(collections.Counter)
for x in rows:
 if x['source_group']=='MACHINE_B_HANDOFF_ONLY':continue
 parts=Path(x['relative_path']).parts
 for rel in ['.']+[str(Path(*parts[:i])) for i in range(1,len(parts))]:c[(x['root_directory'],rel)][x['coverage_status']]+=1
for a in f:
 for k,s in [('safe_count','SAFE'),('provisional_count','PROVISIONALLY COVERED'),('local_only_count','LOCAL ONLY'),('blocked_count','BLOCKED'),('not_required_count','NOT REQUIRED')]:a[k]=c[(a['root_directory'],a['relative_directory'])][s]
write('FOLDER_BY_FOLDER_COVERAGE.csv',f,list(f[0]));d={'independently_retrieved_git_blob_identities':len(receipts),'independently_retrieved_git_blob_bytes':sum(x['bytes'] for x in receipts.values()),'what_if_archive_original_publication_batches':arc,'what_if_397_files_bytes':sum(x['bytes'] for x in arc),'additional_current_inventory_rows_upgraded_by_exact_blob_receipts':updated,'retrievals_not_all_new_this_audit':True};(O/'evidence/GITHUB_INDEPENDENT_RETRIEVAL_SUMMARY.json').write_text(json.dumps(d,indent=2));print(json.dumps(d,indent=2))
