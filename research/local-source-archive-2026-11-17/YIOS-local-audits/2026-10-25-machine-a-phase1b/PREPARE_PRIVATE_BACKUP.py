"""Read-only source checks; writes only named external planning artifacts. No transport."""
import csv, gzip, hashlib, json, os, plistlib, shutil, stat, subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path

HOME=Path('/Users/ghilmankhan')
B=HOME/'YIOS-local-audits/2026-10-25-machine-a-phase1b'
P0=B.parent/'2026-10-25-machine-a-phase0'
REPO=HOME/'workprojects/youtube-intelligence-os'
NOW=datetime.now().astimezone().isoformat()
def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()
def run(args):
    r=subprocess.run(args,capture_output=True,text=True,cwd=REPO)
    return {'code':r.returncode,'stdout':r.stdout.strip(),'stderr':r.stderr.strip()}
def save(n,j): (B/n).write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
measure=json.loads((B/'STORAGE_READINESS_MEASUREMENTS.json').read_text())
roots=[Path(x['path']) for x in measure['roots'] if x['path']!=str(REPO)]
extras=[REPO/x for x in ['finance-short-02-visual-calibration','productions','research/casually-finance-script-intelligence','.git/lfs/objects']]
scope=roots+extras
excluded=[Path(x) for x in json.loads((P0/'scope.json').read_text())['excluded'] if 'offline-map' in x]
seed={}
with gzip.open(P0/'classified-files.csv.gz','rt') as f:
    for row in csv.DictReader(f):
        if any(Path(row['path']).is_relative_to(p) for p in scope):seed[row['path']]=row
overlap={x['source']:x for x in json.loads((B/'STORAGE_PUBLISHED_SOURCE_OVERLAP.json').read_text())['verified']}
pilot_paths=[
 HOME/'Downloads/videos in mp3/CasuallyFinance/Brace For Impact. - Casual Finance (720p, h264).mp4',
 HOME/'workprojects/yio-cf-editing-forensics-local-evidence/JsK53moCyZA/gray.npy',
 HOME/'YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan/EVIDENCE_SHA256SUMS_checkpoint6',
 HOME/'Movies/CapCut/User Data/Projects/com.lveditor.draft/0921/Timelines/21FC2601-3B1E-48EF-82D9-EABE38430012/draft_info.json',
]
pilot=[]
for i,p in enumerate(pilot_paths):
    before=p.stat(); sha=digest(p); after=p.stat()
    assert (before.st_size,before.st_mtime_ns,before.st_ino)==(after.st_size,after.st_mtime_ns,after.st_ino)
    old=seed.get(str(p),{}).get('sha256')
    if old: assert sha==old,('PILOT_SOURCE_CHANGED',str(p))
    if i==0: assert sha=='b07b2a4b55e2b83d717b8cb6e4ac7dcbb44726bf595356d0288617183cfa5bc5'
    if i==2: assert sha=='70e1fb80edcaaddfd58c81b2772805bc5c4af9c0c97b48cbb8bcb593eefe361e'
    pilot.append({'source':str(p),'restore_relative':'machine-a/'+str(p.relative_to(HOME)),
      'bytes':after.st_size,'sha256':sha,'object_key':'sha256/'+sha[:2]+'/'+sha,
      'role':['original Video 003 reference MP4','gray.npy evidence; exact regeneration NOT_VERIFIED','checkpoint 6 checksum manifest; not a new full checkpoint verification','editable CapCut timeline; standalone editing BLOCKED by dependencies'][i],
      'mtime_ns':after.st_mtime_ns,'inode':after.st_ino,'status':'SOURCE_HASH_VERIFIED; UPLOAD_NOT_AUTHORIZED; RESTORE_NOT_EXECUTED'})
pilothash={x['source']:x for x in pilot}
save('PRIVATE_BACKUP_PILOT.json',{'created':NOW,'destination':None,'execution_authorized':False,'files':pilot,'total_bytes':sum(x['bytes'] for x in pilot)})

# Reconcile known roots by names/stat only. Reuse prior hashes; never hash the media library.
# This is a transport manifest, not a new research/content audit. Symlinks are never followed.
rows=[]; errors=[]; dirs=[]
def priority(p):
    s=str(p)
    if any(x in p.parts for x in ['node_modules','.venv','__pycache__','.cache','visual-ct-scan-venv']):return 'C_CONDITIONAL_RUNTIME'
    if p.suffix.lower() in ['.mp4','.mp3','.wav','.npy','.png','.jpg','.jpeg','.webp','.mov'] or '/com.lveditor.draft/' in s or 'deep-ct-scan' in s or 'ct-scan-video' in s:return 'A_EVIDENCE'
    return 'B_RECOVERY_PROVENANCE'
def add(p,root):
    try: st=p.lstat()
    except OSError as e:errors.append({'path':str(p),'error':type(e).__name__});return
    old=seed.get(str(p),{}); same=bool(old) and old.get('bytes')==str(st.st_size) and old.get('mtime_ns')==str(st.st_mtime_ns)
    fresh=pilothash.get(str(p)); published=overlap.get(str(p))
    sha=(fresh or {}).get('sha256') or (old.get('sha256') if same else None)
    status='FRESH_PILOT_HASH' if fresh else ('PRIOR_HASH_METADATA_MATCH_ONLY' if sha else 'HASH_REQUIRED_BEFORE_TRANSFER')
    if published and st.st_size==published['bytes'] and not sha:
        # Preserve receipt hash as baseline; do not claim fresh content verification.
        sha=published['sha256'];status='PRIOR_PUBLICATION_RECEIPT_HASH_NOT_REFRESHED'
    symlink=stat.S_ISLNK(st.st_mode)
    if symlink: sha=None;status='SYMLINK_TARGET_RECORDED_NOT_CONTENT_HASH'
    rel='machine-a/'+str(p.relative_to(HOME))
    rec={'source_absolute':str(p),'restore_relative':rel,'root':str(root),'kind':'symlink' if symlink else 'regular',
      'bytes':st.st_size,'allocated_path_bytes':st.st_blocks*512,'mtime_ns':st.st_mtime_ns,'device':st.st_dev,'inode':st.st_ino,'nlink':st.st_nlink,
      'sha256':sha,'hash_status':status,'object_key':('sha256/'+sha[:2]+'/'+sha) if sha else None,
      'priority':priority(p),'provenance':'Phase 0 inventory + bounded known-root name/stat reconciliation '+NOW,
      'publication':{'destination':published['destination'],'receipt':'STORAGE_PUBLISHED_SOURCE_OVERLAP.json'} if published else None,
      'binary_restore_status':'NOT_VERIFIED','upload_status':'NOT_AUTHORIZED','actual_reclaimable_bytes':None}
    if symlink:rec.update(symlink_target=os.readlink(p),target_exists=p.exists())
    if p.name in ['settings.local.json','credentials','id_rsa','id_ed25519'] or '.ssh' in p.parts:rec['upload_status']='HELD_PRIVACY_REVIEW_REQUIRED'
    rows.append(rec)
for root in scope:
    if not root.exists():errors.append({'path':str(root),'error':'ROOT_MISSING'});continue
    for parent,ds,fs in os.walk(root,followlinks=False):
        parent=Path(parent)
        for d in list(ds):
            p=parent/d
            if any(p==x or p.is_relative_to(x) for x in excluded):ds.remove(d);continue
            if p.is_symlink():add(p,root);ds.remove(d)
        # Snapshot excludes newly generated planning artifacts to avoid self-reference.
        for n in fs:
            p=parent/n
            if parent==B and (n.startswith('PRIVATE_BACKUP') or n=='PREPARE_PRIVATE_BACKUP.py'):continue
            add(p,root)
        dirs.append('machine-a/'+str(parent.relative_to(HOME)))
assert len({x['restore_relative'] for x in rows})==len(rows)
assert all('..' not in Path(x['restore_relative']).parts and not Path(x['restore_relative']).is_absolute() for x in rows)
with gzip.open(B/'PRIVATE_BACKUP_OBJECT_MANIFEST.jsonl.gz','wt',encoding='utf-8') as f:
    for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
save('PRIVATE_BACKUP_DIRECTORIES.json',sorted(set(dirs)))
regular=[x for x in rows if x['kind']=='regular']; unique={}
for x in regular:unique[(x['device'],x['inode'])]=x['allocated_path_bytes']
scope_summary={'created':NOW,'scope_roots':[str(x) for x in scope],'excluded':[str(x) for x in excluded],
 'records':len(rows),'regular_files':len(regular),'symlinks':len(rows)-len(regular),'errors':errors,
 'logical_bytes':sum(x['bytes'] for x in regular),'allocated_path_bytes':sum(x['allocated_path_bytes'] for x in regular),
 'unique_inode_allocated_bytes':sum(unique.values()),'APFS_exclusive_extent_bytes':None,
 'hash_status_counts':dict(Counter(x['hash_status'] for x in rows)),
 'priorities':{p:{'files':sum(x['priority']==p for x in regular),'logical_bytes':sum(x['bytes'] for x in regular if x['priority']==p)} for p in sorted(set(x['priority'] for x in regular))},
 'self_exclusion':'New PRIVATE_BACKUP* outputs and PREPARE_PRIVATE_BACKUP.py excluded from object snapshot; include via final receipt in later approved transfer.',
 'hash_gate':'All non-fresh hashes are comparison baselines only. Missing hashes and source stability must be resolved in an approved bounded transfer batch.',
 'directory_gate':'Directory paths retained separately; ACLs, xattrs, resource forks, creation times and executable modes need export/restore acceptance before a full backup claim.',
 'actual_reclaimable_bytes':None,'executed_uploads':0,'restored_objects':0}
save('PRIVATE_BACKUP_SCOPE.json',scope_summary)

disk=plistlib.loads(subprocess.check_output(['diskutil','list','-plist','external']))
images=plistlib.loads(subprocess.check_output(['hdiutil','info','-plist']))
image_devices={e.get('dev-entry','').removeprefix('/dev/') for i in images.get('images',[]) for e in i.get('system-entities',[])}
devices=[x['DeviceIdentifier'] for x in disk.get('AllDisksAndPartitions',[])]
discovery={'created':NOW,'mounted_volume_count':len(list(Path('/Volumes').iterdir())),
 'external_disk_entries':len(devices),'all_external_entries_are_mounted_disk_images':all(x in image_devices for x in devices),
 'physical_external_backup_detected':False if all(x in image_devices for x in devices) else 'UNKNOWN',
 'time_machine':run(['tmutil','destinationinfo']), 'local_filevault':run(['fdesetup','status']),
 'tools':{t:bool(shutil.which(t)) for t in ['rclone','restic','borg','aws','gcloud','az']},
 'configuration_presence':{s:(HOME/s).exists() for s in ['.config/rclone/rclone.conf','.aws/config','.aws/credentials','.config/gcloud','.config/restic','.config/borg','Library/Application Support/Google/DriveFS']},
 'cloudstorage_children':len(list((HOME/'Library/CloudStorage').iterdir())),
 'icloud_container_present':(HOME/'Library/Mobile Documents/com~apple~CloudDocs').exists(),
 'google_drive':{'profile_read_authenticated':True,'identifiers_omitted':True,'shared_drives_observed':0,'quota':'NOT_VERIFIED; available connector has no quota endpoint','private_upload_scope':'NOT_VERIFIED','retention':'NOT_VERIFIED','billing':'NOT_VERIFIED','independent_restore':'NOT_EXECUTED'},
 'qualified_destinations':0,'destination_acceptance':'BLOCKED','storage_charges_incurred':False,
 'df':run(['df','-k',str(HOME)])}
save('PRIVATE_BACKUP_DESTINATION_DISCOVERY.json',discovery)

handles=run(['lsof','-nP','-Fpcfan']);hits=[];pid=command=fd=''
for line in handles['stdout'].splitlines():
    if line.startswith('p'):pid=line[1:]
    elif line.startswith('c'):command=line[1:]
    elif line.startswith('f'):fd=line[1:]
    elif line.startswith('n') and any(line[1:]==str(r) or line[1:].startswith(str(r)+'/') for r in [REPO]+roots):hits.append({'pid':pid,'command':command,'fd':fd,'path':line[1:]})
checks={'created':NOW,'head':run(['git','rev-parse','HEAD']),'branch':run(['git','branch','--show-current']),
 'status':run(['git','status','--porcelain=v1']),'stash':run(['git','rev-parse','refs/stash']),
 'worktrees':run(['git','worktree','list','--porcelain']), 'upstream':run(['git','rev-parse','@{upstream}']),
 'remote_refs':run(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/what-if-archive-main-integration','refs/heads/research/finance-economics-intelligence','refs/heads/research/casually-finance-editing-forensics','refs/heads/research/what-if-brain-preservation-batch1']),
 'pr44':json.loads(run(['gh','pr','view','44','--repo','ghilmanITM360/youtube-intelligence-os','--json','number,state,isDraft,headRefOid,baseRefOid,url'])['stdout']),
 'ci':json.loads(run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/actions/runs/40222549945','--jq','{id,status,conclusion,head_sha}'])['stdout']),
 'open_handles':hits,'ownership_limits':'No other local source handles observed except this Codex helpers/inspection. This is not a distributed Machine B lock or proof of dormant dependency absence.',
 'missing_dependencies':[{**x,'exists':Path(x['path']).exists()} for x in json.loads((B/'STORAGE_DEPENDENCY_EXISTENCE.json').read_text())],
 'resources_initial':{'five_hour_used_percent':67,'weekly_used_percent':16,'paid_credit_balance':0,'context':'adequate; no expensive analysis or compaction needed'}}
assert checks['head']['stdout']=='badec432bbf5610748123b3f0e0bcb9cdb25fa10'
assert checks['stash']['stdout']=='5b6c3042679400b16aa1024b79058b71dade0ab9'
assert all(x.startswith('?? ') for x in checks['status']['stdout'].splitlines())
save('PRIVATE_BACKUP_VERIFICATION.json',checks)
print(json.dumps({'pilot_files':len(pilot),'pilot_bytes':sum(x['bytes'] for x in pilot),'scope':scope_summary,'destination_qualified':0},indent=2))
