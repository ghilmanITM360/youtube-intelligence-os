from pathlib import Path
import json,tarfile,hashlib,io,os,datetime,shutil
R=Path(__file__).parent;plan=json.loads((R/'ORDERED_PLAN_V6.json').read_text());old=json.loads((R/'ORDERED_PLAN_V5.json').read_text());roots={x['source_absolute']:x['root'] for x in old['files']};proof=json.loads((R/'PILOT_ALIAS_REVALIDATION_20261026.json').read_text());groupindex=[];aliases=[]
def snap(p):
 s=os.stat(p,follow_symlinks=False);return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
for x in plan['files']:
 if not x.get('package_manifest') or '/selected-evidence-packages-' not in x['source_absolute']:continue
 m=json.loads(Path(x['package_manifest']).read_text());root=roots[m['members'][0]['source_absolute']];dups=[e for e in m['members'] if e['sha256']==proof['sha256'] and e['bytes']==proof['fresh_revalidation_downloaded_bytes']]
 if dups:
  m['members']=[e for e in m['members'] if e not in dups];m['duplicate_aliases']=[]
  for e in dups:
   assert snap(e['source_absolute'])==e['source_stat'] and sha(e['source_absolute'])==proof['sha256'];alias=dict(e,remote_id=proof['remote_id'],remote_url=proof['remote_url'],verification_basis='Fresh full source SHA-256 and length equal complete authenticated pilot-object revalidation; zero new upload; restore as separate original path');m['duplicate_aliases'].append(alias);aliases.append(alias)
  m['original_source_root']=root;m['supersedes_local_unuploaded_package']=x['source_absolute'];mb=json.dumps(m,indent=2,ensure_ascii=False).encode();mp=Path(x['package_manifest']).with_name(Path(x['package_manifest']).name.replace('.members.json','.dedup.members.json'));mp.write_bytes(mb);mp.chmod(0o400);archive=Path(x['source_absolute']).with_name(Path(x['source_absolute']).name.replace('.tar.gz','.dedup.tar.gz'));metadata_name=x['package_metadata_member']
  with tarfile.open(archive,'x:gz',format=tarfile.PAX_FORMAT,compresslevel=3) as tf:
   for e in m['members']:
    p=e['source_absolute'];assert snap(p)==e['source_stat'];ti=tf.gettarinfo(p,arcname=e['restore_relative']);ti.uid=ti.gid=0;ti.uname=ti.gname=''
    with open(p,'rb') as f:tf.addfile(ti,f)
    assert snap(p)==e['source_stat']
   ti=tarfile.TarInfo(metadata_name);ti.size=len(mb);ti.mode=0o400;tf.addfile(ti,io.BytesIO(mb))
  expected={e['restore_relative']:e for e in m['members']};expected[metadata_name]={'bytes':len(mb),'sha256':hashlib.sha256(mb).hexdigest()};seen=set()
  with tarfile.open(archive,'r:gz') as tf:
   for ti in tf:
    assert ti.isfile() and ti.name in expected and ti.name not in seen;h=hashlib.sha256();n=0
    with tf.extractfile(ti) as f:
     for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
    assert n==expected[ti.name]['bytes'] and h.hexdigest()==expected[ti.name]['sha256'];seen.add(ti.name)
  assert seen==set(expected)
  for e in m['members']+m['duplicate_aliases']:assert snap(e['source_absolute'])==e['source_stat']
  archive.chmod(0o400);s=snap(archive);x.update(source_absolute=str(archive),restore_relative='recovery-packages/'+archive.name,bytes=s['st_size'],mtime_ns=s['st_mtime_ns'],inode=s['st_ino'],device=s['st_dev'],proposed_destination_name=f"{x['sequence']:05d}__"+archive.name,package_manifest=str(mp),package_metadata_sha256=hashlib.sha256(mb).hexdigest(),package_metadata_bytes=len(mb),package_member_count=len(m['members']),package_member_bytes=sum(e['bytes'] for e in m['members']),package_duplicate_alias_count=len(dups),fresh_local_archive_sha256=sha(archive))
 x['package_original_source_root']=root;x['package_group_key']=x['backup_priority']+'|'+root+'|'+x['package_group'];groupindex.append({k:x.get(k) for k in ['sequence','source_absolute','package_group_key','package_original_source_root','package_group','package_part','package_group_parts','package_member_count','package_duplicate_alias_count','package_member_bytes','bytes','package_manifest']})
plan['package_rows']=[x for x in plan['files'] if x.get('package_manifest')];plan['planned_bytes']=sum(x['bytes'] for x in plan['files']);plan['ordering_revision']+=' V7: root/group/chunk keys explicit; three exact CapCut JSON content aliases removed from two never-uploaded archives and mapped to freshly independently revalidated pilot remote bytes. No originals or prior remote objects changed.'
p=R/'ORDERED_PLAN_V7.json'
with p.open('x') as f:json.dump(plan,f,indent=2,ensure_ascii=False)
p.chmod(0o400)
summary={'status':'LOCAL_PACKAGES_VERIFIED_REMOTE_UPLOAD_PENDING','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'packages':groupindex,'original_source_paths':3527,'unique_archive_source_members':sum(x['package_member_count'] for x in plan['files'] if '/selected-evidence-packages-' in x['source_absolute']),'exact_pilot_aliases':aliases,'compressed_archive_bytes':sum(x['bytes'] for x in plan['files'] if '/selected-evidence-packages-' in x['source_absolute']),'source_input_bytes':4934692936,'Mac_free_bytes':shutil.disk_usage(str(R)).free,'limitation':'Local packaging/readback is not cloud backup; require complete authenticated remote archive and member SHA-256 checks before VERIFIED. Group completeness requires every identified root/group/part and explicit remote companion.'}
p=R/'SELECTED_PACKAGE_GROUP_INDEX_20261026.json'
with p.open('x') as f:json.dump(summary,f,indent=2)
p.chmod(0o400);print(json.dumps({k:summary[k] for k in ['status','original_source_paths','unique_archive_source_members','compressed_archive_bytes','Mac_free_bytes']}))
