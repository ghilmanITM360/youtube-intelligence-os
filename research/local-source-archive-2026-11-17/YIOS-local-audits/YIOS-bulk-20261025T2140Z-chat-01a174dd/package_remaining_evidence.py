"""Lossless bounded packages for existing selected B/C source rows; no new inventory."""
from pathlib import Path
import json,hashlib,tarfile,io,datetime,os,stat,shutil,collections
R=Path(__file__).parent;D=R/'selected-evidence-packages-20261026';D.mkdir(mode=0o700)
plan=json.loads((R/'ORDERED_PLAN_V5.json').read_text());selected=[x for x in plan['files'] if not x.get('package_manifest') and x['backup_priority']!='A_ORIGINAL_MEDIA'];groups=collections.OrderedDict()
for x in selected:
 rel=Path(x['source_absolute']).relative_to(x['root']);is_b=x['backup_priority'].startswith('B_');key=(x['backup_priority'],x['root'],rel.parts[0] if is_b and len(rel.parts)>1 else '_selected_root')
 groups.setdefault(key,[]).append(x)
known=json.loads((R/'recovery-20261026-machine-b-handoff/SOURCE_TO_DRIVE_INVENTORY.json').read_text())['files']
for d in sorted(R.glob('batch-*')):
 if (d/'RECEIPT.json').exists() and int(d.name.split('-')[1])>=10:
  for x in json.loads((d/'RECEIPT.json').read_text())['files']:known.append({'source':x['source_absolute'],'sha256':x['fresh_sha256'],'bytes':x['bytes'],'remote_id':x['remote_id'],'remote_url':x['remote_url']})
def snap(p):
 s=os.stat(p,follow_symlinks=False);assert stat.S_ISREG(s.st_mode),'SOURCE_NOT_REGULAR'
 return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
packages=[];index=0;total_logical=0;total_packed=0
for (priority,root,group),originals in groups.items():
 # Keep each forensic video together (largest original selected file<175MB).
 # Editing chunks are bounded at80MB raw and300 entries to bound both archive and index.
 chunks=[];chunk=[];raw=0;is_b=priority.startswith('B_')
 for x in originals:
  if chunk and not is_b and (raw+x['bytes']>80000000 or len(chunk)>=300):chunks.append(chunk);chunk=[];raw=0
  chunk.append(x);raw+=x['bytes']
 if chunk:chunks.append(chunk)
 for part,chunk in enumerate(chunks,1):
  logical=sum(x['bytes'] for x in chunk);assert logical<=500000000,'PACKAGE_TOO_LARGE';assert shutil.disk_usage(str(D)).free>logical*1.1+5000000000,'MAC_DISK_RESERVE'
  index+=1;seq=4022+index;name=f'{seq:05d}-'+('forensic-'+group if is_b else 'editing-'+str(index))+f'-part{part:02d}';entries=[]
  for x in chunk:
   p=x['source_absolute'];bn=Path(p).name.lower();assert not any(t in p.lower() for t in ['/.codex/','/.claude/','/.ssh/','/.aws/','/.git/','/.config/']) and bn not in ['.env','credentials.json','token.json','tokens.json','id_rsa','id_ed25519'] and not bn.endswith(('.pem','.key')),'SENSITIVE_SOURCE_NOT_ELIGIBLE'
   s=snap(p);assert (s['st_size'],s['st_mtime_ns'],s['st_ino'])==(x['bytes'],x['mtime_ns'],x['inode']),'SOURCE_CHANGED_SINCE_PLAN';h=sha(p);assert snap(p)==s
   expected=x.get('sha256');assert not expected or len(expected)!=64 or h==expected,'HISTORICAL_SOURCE_HASH_MISMATCH'
   entries.append({'source_absolute':p,'restore_relative':x['restore_relative'],'bytes':s['st_size'],'sha256':h,'source_stat':s,'video_id':group if is_b and len(group)==11 else None,'role':priority,'original_plan_sequence':x['sequence']})
  prefix=str(Path(root)/group)+'/' if is_b and group!='_selected_root' else str(root)+'/'
  refs=[k for k in known if k['source'].startswith(prefix)]
  metadata_name='_recovery/'+name+'.members.json';manifest={'status':'LOCAL_PACKAGE_MEMBER_HASHES_VERIFIED_NOT_UPLOADED','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'members':entries,'existing_remote_companions':refs,'group':group,'part':part,'parts_in_selected_group':len(chunks),'source_scope':'Exact previously selected ordered-plan regular files only; related sources kept together where bounded. Other dependencies and later-created files not implied.','limitations':'Lossless archival packaging only; no inference of editing-project/analysis completion or independent-machine runtime recovery.'};mb=json.dumps(manifest,ensure_ascii=False,indent=2).encode();mp=D/(name+'.members.json');mp.write_bytes(mb);mp.chmod(0o400);archive=D/(name+'.tar.gz')
  with tarfile.open(archive,'x:gz',format=tarfile.PAX_FORMAT,compresslevel=3) as tf:
   for x in entries:
    p=x['source_absolute'];assert snap(p)==x['source_stat'];ti=tf.gettarinfo(p,arcname=x['restore_relative']);ti.uid=ti.gid=0;ti.uname=ti.gname=''
    with open(p,'rb') as f:tf.addfile(ti,f)
    assert snap(p)==x['source_stat']
   ti=tarfile.TarInfo(metadata_name);ti.size=len(mb);ti.mode=0o400;tf.addfile(ti,io.BytesIO(mb))
  expected={x['restore_relative']:x for x in entries};expected[metadata_name]={'bytes':len(mb),'sha256':hashlib.sha256(mb).hexdigest()};seen=set()
  with tarfile.open(archive,'r:gz') as tf:
   for ti in tf:
    assert ti.isfile() and ti.name in expected and ti.name not in seen;h=hashlib.sha256();n=0
    with tf.extractfile(ti) as f:
     for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
    assert n==expected[ti.name]['bytes'] and h.hexdigest()==expected[ti.name]['sha256'];seen.add(ti.name)
  assert seen==set(expected)
  for x in entries:assert snap(x['source_absolute'])==x['source_stat']
  archive.chmod(0o400);s=snap(archive)
  packages.append({'source_absolute':str(archive),'restore_relative':'recovery-packages/'+archive.name,'root':str(D),'kind':'regular','bytes':s['st_size'],'mtime_ns':s['st_mtime_ns'],'inode':s['st_ino'],'device':s['st_dev'],'sequence':seq,'proposed_destination_name':f'{seq:05d}__'+archive.name,'backup_priority':priority,'required_companions':'All selected group chunks and existing remote references in member manifest; external dependencies may remain missing','package_manifest':str(mp),'package_metadata_member':metadata_name,'package_metadata_sha256':hashlib.sha256(mb).hexdigest(),'package_metadata_bytes':len(mb),'package_member_count':len(entries),'package_member_bytes':logical,'video_id':group if is_b and len(group)==11 else None,'fresh_local_archive_sha256':sha(archive),'package_group':group,'package_part':part,'package_group_parts':len(chunks)})
  total_logical+=logical;total_packed+=s['st_size'];print(json.dumps({'sequence':seq,'priority':priority,'group':group,'part':part,'source_members':len(entries),'logical_bytes':logical,'archive_bytes':s['st_size']}),flush=True)
assert sum(x['package_member_count'] for x in packages)==len(selected)
old=plan['files'];new=[];inserted=False
for x in old:
 if x in selected:
  if not inserted:new.extend(packages);inserted=True
 else:new.append(x)
plan['files']=new;plan['package_rows']+=packages;plan['planned_files']=len(new);plan['planned_bytes']=sum(x['bytes'] for x in new);plan['ordering_revision']='V6: Original A and existing CT/Finance companion objects retained in order. Previously selected B/C sources replaced by lossless bounded related-source archives, each original with full path, bytes, source SHA and stability metadata, complete local decompression/hash readback; every member must also pass fresh remote decompression/hash verification before cloud status VERIFIED. No new global inventory.'
p=R/'ORDERED_PLAN_V6.json'
with p.open('x') as f:json.dump(plan,f,indent=2,ensure_ascii=False)
p.chmod(0o400);print(json.dumps({'status':'LOCAL_PACKAGING_COMPLETE_REMOTE_UPLOAD_NOT_STARTED','original_source_members':len(selected),'packages':len(packages),'logical_bytes':total_logical,'compressed_archive_bytes':total_packed,'plan_objects':len(new),'plan_payload_bytes':plan['planned_bytes']}),flush=True)
