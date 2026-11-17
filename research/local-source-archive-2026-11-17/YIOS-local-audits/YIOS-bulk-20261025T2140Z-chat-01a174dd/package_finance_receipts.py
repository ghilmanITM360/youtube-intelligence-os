from pathlib import Path
import json,hashlib,tarfile,io,datetime,os,stat
R=Path(__file__).parent;D=R/'finance-publication-evidence-20261026';D.mkdir(mode=0o700)
rows=json.loads((R/'FINANCE_EXTERNAL_AUDIT_EXISTING_ROWS.json').read_text())['files'];entries=[];excluded=[]
def snap(p):
 s=os.stat(p,follow_symlinks=False);assert stat.S_ISREG(s.st_mode)
 return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
for x in sorted(rows,key=lambda x:x['source_absolute']):
 p=x['source_absolute'];n=Path(p).name
 if n in ['preflight.json','final-usage.json'] or n.startswith('secret-scan'):
  excluded.append({'path':p,'reason':'Unnecessary machine/account resource observation or secret-scan output; local original preserved'});continue
 assert not any(t in p for t in ['/.codex/','/.claude/','/.ssh/','/.git/']) and n not in ['.env','credentials.json','token.json']
 s=snap(p);assert (s['st_size'],s['st_mtime_ns'],s['st_ino'])==(x['bytes'],x['mtime_ns'],x['inode']),'SOURCE_CHANGED_SINCE_MANIFEST';h=sha(p);assert snap(p)==s
 entries.append({'source_absolute':p,'restore_relative':x['restore_relative'],'bytes':s['st_size'],'sha256':h,'source_stat':s,'video_id':None,'role':'FINANCE_NICK_166_TO_170_EXTERNAL_RESEARCH_PUBLICATION_EVIDENCE'})
m={'status':'LOCAL_PACKAGE_MEMBER_HASHES_VERIFIED_NOT_UPLOADED','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'members':entries,'intentional_exclusions':excluded,'scope':'Exact existing manifest subset only. Source research, calculations, canonical transcripts, referenced public documents, publication/integrity receipts, scripts and workbook previews; no Finance source writes or writer transfer. Later-created files outside existing snapshot not claimed.'};mb=json.dumps(m,ensure_ascii=False,indent=2).encode();mp=D/'finance-publication.members.json';mp.write_bytes(mb);mp.chmod(0o400);archive=D/'NICK_166-170.publication-evidence.tar.gz'
with tarfile.open(archive,'x:gz',format=tarfile.PAX_FORMAT,compresslevel=3) as tf:
 for x in entries:
  p=x['source_absolute'];assert snap(p)==x['source_stat'];ti=tf.gettarinfo(p,arcname=x['restore_relative']);ti.uid=ti.gid=0;ti.uname=ti.gname=''
  with open(p,'rb') as f:tf.addfile(ti,f)
  assert snap(p)==x['source_stat']
 ti=tarfile.TarInfo('_recovery/finance-publication.members.json');ti.size=len(mb);ti.mode=0o400;tf.addfile(ti,io.BytesIO(mb))
expected={x['restore_relative']:x for x in entries};expected['_recovery/finance-publication.members.json']={'bytes':len(mb),'sha256':hashlib.sha256(mb).hexdigest()};seen=set()
with tarfile.open(archive,'r:gz') as tf:
 for ti in tf:
  assert ti.isfile() and ti.name in expected and ti.name not in seen;h=hashlib.sha256();n=0
  with tf.extractfile(ti) as f:
   for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
  assert n==expected[ti.name]['bytes'] and h.hexdigest()==expected[ti.name]['sha256'];seen.add(ti.name)
assert seen==set(expected)
for x in entries:assert snap(x['source_absolute'])==x['source_stat']
archive.chmod(0o400);s=snap(archive);row={'source_absolute':str(archive),'restore_relative':'recovery-packages/'+archive.name,'root':str(D),'kind':'regular','bytes':s['st_size'],'mtime_ns':s['st_mtime_ns'],'inode':s['st_ino'],'device':s['st_dev'],'sequence':4022,'proposed_destination_name':'04022__'+archive.name,'backup_priority':'D_FINANCE_PUBLICATION_EVIDENCE_HANDOFF_COMPANION','required_companions':'Exact published Finance Git head1adb8129f689207552f0838414e5823e4255bde1 and ledger/workbook; account/resource/secret-scan outputs intentionally excluded','package_manifest':str(mp),'package_metadata_member':'_recovery/finance-publication.members.json','package_metadata_sha256':hashlib.sha256(mb).hexdigest(),'package_metadata_bytes':len(mb),'package_member_count':len(entries),'package_member_bytes':sum(x['bytes'] for x in entries),'video_id':None,'fresh_local_archive_sha256':sha(archive)}
plan=json.loads((R/'ORDERED_PLAN_V4.json').read_text());a=plan['files'];last=max(i for i,x in enumerate(a) if x.get('package_manifest'));plan['files']=a[:last+1]+[row]+a[last+1:];plan['package_rows'].append(row);plan['planned_files']=len(plan['files']);plan['planned_bytes']=sum(x['bytes'] for x in plan['files']);plan['ordering_revision']='V5: existing order preserved; bounded Finance publication evidence companion placed next to CT handoff packages; original plan records retained. No new global inventory or source writes.'
p=R/'ORDERED_PLAN_V5.json'
with p.open('x') as f:json.dump(plan,f,indent=2,ensure_ascii=False)
p.chmod(0o400)
print(json.dumps({'archive_bytes':s['st_size'],'source_member_count':len(entries),'logical_source_member_bytes':sum(x['bytes'] for x in entries),'excluded_machine_resource_files':len(excluded)}))
