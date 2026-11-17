"""Aggregate existing frozen recovery mappings; no new inventory or source writes."""
from pathlib import Path
import json, hashlib, datetime, subprocess, shutil
R=Path(__file__).parent
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    with p.open('x') as f:json.dump(v,f,indent=2)
    p.chmod(0o400)
state=json.loads(subprocess.check_output(['python3',str(R/'continue_backup.py'),'state','{}'],text=True))
assert state['uploaded_bytes_including_controls']==state['verified_bytes_including_controls']
base=R/'recovery-20261026-machine-b-handoff'
objects=list(read(base/'SOURCE_TO_DRIVE_INVENTORY.json')['files']);members=[];aliases=[];batches=[]
for d in sorted(R.glob('batch-*')):
    if int(d.name.split('-')[1])<10:continue
    receipt=read(d/'RECEIPT.json');assert receipt['status']=='VERIFIED'
    for l in (d/'SHA256SUMS').read_text().splitlines():
        h,n=l.split('  ',1);assert sha(d/n)==h,(d,n)
    batches.append({'batch':receipt['batch'],'status':receipt['status'],'whole_batch_acceptance':receipt.get('whole_batch_acceptance','VERIFIED'),'receipt_path':str(d/'RECEIPT.json'),'receipt_sha256':sha(d/'RECEIPT.json')})
    for x in receipt['files']:
        objects.append({'source':x['source_absolute'],'restore_relative':x['restore_relative'],'bytes':x['bytes'],'sha256':x['fresh_sha256'],'remote_id':x['remote_id'],'remote_url':x['remote_url'],'batch':d.name,'status':'VERIFIED','package_manifest':x.get('package_manifest'),'duplicate_of_verified':x.get('duplicate_of_verified',False),'verification_receipt':str(d/'RECEIPT.json')})
        if x.get('package_manifest'):
            pm=read(x['package_manifest']);assert x['retrieval']['package_source_members_verified']==len(pm['members'])
            for m in pm['members']:
                members.append(dict(m,remote_archive_id=x['remote_id'],remote_archive_sha256=x['fresh_sha256'],archive_member=m['restore_relative'],verification_status='COMPLETE_REMOTE_DECOMPRESSION_MEMBER_SHA256_VERIFIED',batch=d.name))
            for alias in pm.get('duplicate_aliases',[]):aliases.append(dict(alias,source_package_remote_id=x['remote_id'],source_package_manifest=x['package_manifest']))
controls=[]
for p in sorted(R.glob('CONTROL-UPLOAD-*.json')):
    u=read(p);v=read(R/('CONTROL-VERIFY-'+p.name[len('CONTROL-UPLOAD-'): ]));assert v['status']=='VERIFIED' and u['remote_id']==v['remote_id'] and u['uploaded_bytes']==v['retrieved_bytes'] and u['sha256']==v['sha256']
    controls.append({k:u[k] for k in ['remote_id','remote_url','source_path','sha256','uploaded_bytes']})
exception=read(R/'batch-0031/EXCEPTION_APPROVAL.json');extra=exception['extra_physical_bytes']
done={x['source'] for x in objects};plan=max(R.glob('ORDERED_PLAN_V*.json'),key=lambda p:int(p.stem.rsplit('_V',1)[1]));pending=[x for x in read(plan)['files'] if x['source_absolute'] not in done]
summary=dict(state,confirmed_uploaded_and_selected_verified_bytes_including_controls=state['uploaded_bytes_including_controls'],physical_remote_verified_bytes_including_duplicate=state['verified_bytes_including_controls']+extra,extra_physical_bytes=extra,extra_unique_source_coverage=0,remaining_genuinely_unuploaded_objects=len(pending),remaining_genuinely_unuploaded_payload_bytes=sum(x['bytes'] for x in pending),archive_member_representations=len(members),archive_member_logical_bytes=sum(x['bytes'] for x in members),explicit_pilot_aliases=len(aliases),coverage_count_basis='Path representations, not deduplicated content count; archive logical bytes never added to physical totals',mac_free_bytes=shutil.disk_usage(R).free)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ');d=R/('checkpoint-'+stamp);d.mkdir(mode=0o700)
repo='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
git={k:subprocess.check_output(cmd,cwd=repo,text=True).strip() for k,cmd in [('head',['git','rev-parse','HEAD']),('branch',['git','branch','--show-current']),('all_local_and_cached_remote_refs',['git','show-ref']),('stashes',['git','stash','list','--format=%H']),('tracked_status',['git','status','--porcelain','-uno'])]}
git['limitations']='Read-only snapshot; no fetch; cached remote refs do not prove absence of other-Mac unpushed work; PR heads not re-fetched. No source/Git/PR writes by operator.'
inventory={'summary_before_this_control':summary,'objects':objects,'archive_members':members,'exact_duplicate_pilot_aliases':aliases,'verified_controls':controls,'batch_receipts':batches,'batch31_exception':exception,'git_snapshot':git,'ordered_plan':{'path':str(plan),'sha256':sha(plan),'pending':pending}}
save(d/'SOURCE_TO_DRIVE_INVENTORY.json',inventory);save(d/'SUMMARY.json',summary);save(d/'GIT_READ_ONLY_SNAPSHOT.json',git)
text='# YIOS Machine A verified recovery handoff\n\nBatch31 CLOSED_WITH_APPROVED_EXCEPTION_UNATTRIBUTED_DUPLICATE. Both identified404830-byte copies remain unchanged. Owner account actor established; exact uploader client/session and duplication mechanism UNRESOLVED permanently. The extra copy has zero additional unique source coverage and404830 extra physical bytes. Original BLOCKED receipts remain immutable. This is a specific owner exception; every future integrity, ownership, privacy, quota and verification gate remains mandatory.\n\nAll locators below derive from existing frozen receipts and successful complete remote SHA verification; archive member entries passed streamed decompression and member SHA checks. Aliases refer to previously verified exact pilot content. This is file-level cloud recovery; independent-machine disaster recovery, complete production/runtime recovery and Machine B writer acceptance are not certified. Preserve source originals and all untracked/ignored evidence. No Finance audits or production writes; Machine B Finance/expansion/channel ownership and protected Claude873b9a27 Visual ownership remain untouched. No PR36/44 merge/closure, branch/worktree/stash/LFS changes, public sharing, cleanup or credits used.\n\nAccount kgk2930@gmail.com; approved owner-only private yios hierarchy. Physical capacity ceiling12,000,000,000bytes; Drive reserve2,000,000,000bytes with conservative UI rounding/binary bound plus100MB buffer. Refresh usage, quota, disk5GB headroom, overlap/source stability before every next upload. Legacy helper totals exclude the accepted404830 extra copy: always add it for physical gates. Never reupload4014-4016. Latest immutable checkpoint and actual unfinished batch receipts supersede stale historical sequence examples.\n\nTotals below precede this Markdown control; its uploaded and full independently verified bytes are added only by separate CONTROL-UPLOAD/VERIFY receipts. The initial recovery inventory is preserved as supplied; archive-member table aggregates subsequent frozen batch manifests and is not a new discovery scan.\n\n```json\n'+json.dumps(inventory,indent=2)+'\n```\n'
p=d/f'YIOS_FULL_VERIFIED_EXCEPTION_AWARE_{stamp}.md'
with p.open('x') as f:f.write(text)
p.chmod(0o400)
print(json.dumps({'checkpoint_dir':str(d),'handoff_path':str(p),'handoff_bytes':p.stat().st_size,'handoff_sha256':sha(p),'summary':summary}))
