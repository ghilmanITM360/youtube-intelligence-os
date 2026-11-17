"""Bounded durable CT evidence archives from existing inventory; originals never modified."""
import json,gzip,tarfile,hashlib,datetime,os,stat,io
from pathlib import Path
BASE=Path(__file__).parent;AUDITS=BASE.parent;OUT=BASE/'ct-evidence-packages-20261026'
OUT.mkdir(mode=0o700,exist_ok=False)
names=['2026-10-24-o3FQcd91MIs-deep-ct-scan','2026-10-24-Uumnx2Fo6cE-deep-ct-scan','2026-10-24-5umJ63d3rzQ-deep-ct-scan'];groups={n:[] for n in names}
checkpoint=BASE/'recovery-20261026-machine-b-handoff'
already={x['source']:x for x in json.loads((checkpoint/'SOURCE_TO_DRIVE_INVENTORY.json').read_text())['files']}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def snap(p):
 s=os.stat(p,follow_symlinks=False);assert stat.S_ISREG(s.st_mode)
 return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
with gzip.open(AUDITS/'2026-10-25-machine-a-phase1b/PRIVATE_BACKUP_OBJECT_MANIFEST.jsonl.gz','rt') as f:
 for line in f:
  x=json.loads(line)
  for name in names:
   if x['source_absolute'].startswith(str(AUDITS/name)+'/') and x['kind']=='regular' and Path(x['source_absolute']).name!='.DS_Store':groups[name].append(x)
rows=[]
for i,name in enumerate(names):
 video=name.split('-')[3];entries=[];refs=[]
 for x in sorted(groups[name],key=lambda x:x['source_absolute']):
  p=x['source_absolute'];s=snap(p)
  assert (s['st_size'],s['st_mtime_ns'],s['st_ino'])==(x['bytes'],x['mtime_ns'],x['inode']),'SOURCE_CHANGED_SINCE_INVENTORY'
  if p in already:refs.append(already[p]);continue
  h=sha(p);assert snap(p)==s
  entries.append({'source_absolute':p,'restore_relative':x['restore_relative'],'bytes':s['st_size'],'sha256':h,'source_stat':s,'video_id':video,'role':'CT_VISUAL_EVIDENCE_DECLARED_COVERAGE'})
 for f in ['SOURCE.json','SENTENCES.csv','evidence/thumbnail_maxresdefault.jpg']:
  p=Path('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS')/video/f
  assert p.exists(),'MISSING_REQUIRED_COMPANION'
  s=snap(p);h=sha(p);assert snap(p)==s
  entries.append({'source_absolute':str(p),'restore_relative':'machine-a/'+str(p.relative_to('/Users/ghilmankhan')),'bytes':s['st_size'],'sha256':h,'source_stat':s,'video_id':video,'role':'HISTORICAL_IDENTITY_ASR_OR_THUMBNAIL_UNCERTIFIED'})
 manifest={'status':'LOCAL_PACKAGE_MEMBER_HASHES_VERIFIED_NOT_UPLOADED','video_id':video,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'members':entries,'existing_remote_companions':refs,'source_scope':'Exact existing audit inventory excluding .DS_Store, plus three explicit registered companion files; not a new directory census. Files created after original inventory are not included.','limitations':'Visual-only declared states unchanged; no independent-machine runtime or AV certification.'}
 mb=json.dumps(manifest,ensure_ascii=False,indent=2).encode();mp=OUT/f'{video}.members.json';mp.write_bytes(mb);mp.chmod(0o400)
 archive=OUT/f'{video}.ct-evidence.tar.gz'
 with tarfile.open(archive,'x:gz',format=tarfile.PAX_FORMAT,compresslevel=3) as tf:
  for x in entries:
   p=Path(x['source_absolute']);assert snap(p)==x['source_stat'];ti=tf.gettarinfo(str(p),arcname=x['restore_relative']);ti.uid=ti.gid=0;ti.uname=ti.gname=''
   with p.open('rb') as f:tf.addfile(ti,f)
   assert snap(p)==x['source_stat']
  ti=tarfile.TarInfo('_recovery/'+video+'.members.json');ti.size=len(mb);ti.mode=0o400;tf.addfile(ti,io.BytesIO(mb))
 # Complete local decompression/hash readback qualifies archive members before any upload.
 expected={x['restore_relative']:x for x in entries};expected['_recovery/'+video+'.members.json']={'bytes':len(mb),'sha256':hashlib.sha256(mb).hexdigest()};seen=set()
 with tarfile.open(archive,'r:gz') as tf:
  for ti in tf:
   assert ti.isfile() and ti.name in expected and ti.name not in seen
   h=hashlib.sha256();n=0
   with tf.extractfile(ti) as f:
    for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
   assert n==expected[ti.name]['bytes'] and h.hexdigest()==expected[ti.name]['sha256'];seen.add(ti.name)
 assert seen==set(expected)
 for x in entries:assert snap(x['source_absolute'])==x['source_stat']
 archive.chmod(0o400);s=snap(archive);seq=4019+i
 rows.append({'source_absolute':str(archive),'restore_relative':'recovery-packages/'+archive.name,'root':str(OUT),'kind':'regular','bytes':s['st_size'],'mtime_ns':s['st_mtime_ns'],'inode':s['st_ino'],'device':s['st_dev'],'sequence':seq,'proposed_destination_name':f'{seq:05d}__'+archive.name,'backup_priority':'B_IRREPLACEABLE_CT_REVIEW_PACKAGES','required_companions':'Original MP4 and existing verified checkpoint manifest refs in package member manifest; declared scope only','package_manifest':str(mp),'package_metadata_member':'_recovery/'+video+'.members.json','package_metadata_sha256':hashlib.sha256(mb).hexdigest(),'package_metadata_bytes':len(mb),'package_member_count':len(entries),'package_member_bytes':sum(x['bytes'] for x in entries),'video_id':video,'fresh_local_archive_sha256':sha(archive)})
 print(json.dumps({'video_id':video,'archive_bytes':s['st_size'],'member_count':len(entries),'logical_member_bytes':sum(x['bytes'] for x in entries)}),flush=True)
old=json.loads((BASE/'ORDERED_PLAN_V2.json').read_text());a=old['files'];old['files']=[x for x in a if x['backup_priority']=='A_ORIGINAL_MEDIA']+rows+[x for x in a if x['backup_priority']!='A_ORIGINAL_MEDIA'];old['ordering_revision']='V3: preserve original A order, then three bounded CT evidence archives (existing inventory + explicit companions), then original B/C order. Original rows/sequence IDs unchanged. No repeated global inventory.';old['planned_files']=len(old['files']);old['planned_bytes']=sum(x['bytes'] for x in old['files']);old['package_rows']=rows
p=BASE/'ORDERED_PLAN_V3.json'
with p.open('x') as f:json.dump(old,f,ensure_ascii=False,indent=2)
p.chmod(0o400)
