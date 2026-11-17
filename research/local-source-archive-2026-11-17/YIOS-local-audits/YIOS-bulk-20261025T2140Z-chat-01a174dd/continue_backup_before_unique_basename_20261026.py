"""Preservation-only bookkeeping and streamed retrieval. No API credentials or uploads here."""
import json,sys,os,stat,hashlib,datetime,urllib.request,shutil,tarfile
from pathlib import Path
BASE=Path(__file__).parent
CHECKPOINT=BASE/'recovery-20261026-machine-b-handoff'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text())
def save(p,x):
 p=Path(p)
 with p.open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False)
 p.chmod(0o600)
def digest(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def snap(p):
 s=os.stat(p,follow_symlinks=False);assert stat.S_ISREG(s.st_mode),'NOT_REGULAR_SOURCE'
 return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
def stable(x):
 assert snap(x['source_absolute'])==x['fresh_stat'],'SOURCE_MODIFIED'
 if x.get('package_manifest'):
  for m in read(x['package_manifest'])['members']+read(x['package_manifest']).get('duplicate_aliases',[]):assert snap(m['source_absolute'])==m['source_stat'],'PACKAGE_SOURCE_MODIFIED'
def plan():
 versions=list(BASE.glob('ORDERED_PLAN_V[0-9]*.json'));p=max(versions,key=lambda p:int(p.stem.rsplit('_V',1)[1]));return read(p)
def state():
 inv=read(CHECKPOINT/'SOURCE_TO_DRIVE_INVENTORY.json')['files'];done={x['source'] for x in inv};known={(x['sha256'],x['bytes']):x for x in inv};total=read(CHECKPOINT/'HANDOFF_DRIVE_RECEIPT.json')['total_uploaded_bytes_including_source_backup'];verified=total
 for cp in sorted(BASE.glob('CONTROL-UPLOAD-*.json')):
  control=read(cp);cv=read(BASE/('CONTROL-VERIFY-'+cp.name[len('CONTROL-UPLOAD-'):]))
  assert cv['status']=='VERIFIED' and cv['remote_id']==control['remote_id'] and cv['retrieved_bytes']==control['uploaded_bytes'] and cv['sha256']==control['sha256'],'CONTROL_NOT_VERIFIED'
  total+=control['uploaded_bytes'];verified+=cv['retrieved_bytes']
 for d in sorted(BASE.glob('batch-*')):
  if int(d.name.split('-')[1])<10:continue
  assert (d/'RECEIPT.json').exists(),'INCOMPLETE_BATCH_'+d.name
  r=read(d/'RECEIPT.json');assert r['status']=='VERIFIED'
  total+=r['uploaded_bytes'];verified+=r['independently_retrieved_bytes']
  for x in r['files']:done.add(x['source_absolute']);known[(x['fresh_sha256'],x['bytes'])]=x
 return done,known,total,verified
cmd=sys.argv[1];a=json.loads(sys.argv[2]) if len(sys.argv)>2 else {}
if cmd=='prepare':
 done,known,total,verified=state();assert total==verified
 assert a['five_hour_used']<85 and a['weekly_used']<93,'RESOURCE_CHECKPOINT'
 assert a['account']=='kgk2930@gmail.com' and a['privacy']=='OWNER_ONLY','GATE'
 assert shutil.disk_usage(str(BASE)).free>5000000000,'MAC_DISK_LOW'
 allowance=min(12000000000-total-10000000,a['conservative_free_bytes']-2000000000);assert allowance>0,'CAPACITY'
 rows=[];payload=0;batch_known={}
 for original in plan()['files']:
  if original['source_absolute'] in done:continue
  x=dict(original);p=x['source_absolute'];name=Path(p).name.lower()
  assert not any(t in p.lower() for t in ['/.codex/','/.claude/','/.ssh/','/.aws/','/.config/','/.git/']),'SENSITIVE_PATH'
  assert name not in ['.env','credentials.json','token.json','tokens.json','id_rsa','id_ed25519'] and not name.endswith(('.pem','.key')),'SENSITIVE_FILENAME'
  if payload+x['bytes']>min(500000000,allowance):break
  s=snap(p);assert (s['st_size'],s['st_mtime_ns'],s['st_ino'])==(x['bytes'],x['mtime_ns'],x['inode']),'SOURCE_CHANGED_SINCE_PLAN'
  h=digest(p);assert snap(p)==s,'SOURCE_CHANGED_DURING_HASH';expected=x.get('sha256') or x.get('fresh_local_archive_sha256');assert not expected or len(expected)!=64 or h==expected,'HISTORICAL_SOURCE_HASH_MISMATCH';x.update(fresh_stat=s,fresh_sha256=h,hash_refreshed_utc=now(),status='PREPARED')
  stable(x);key=(h,x['bytes'])
  if key in known:x.update(duplicate_of_verified=True,remote_id=known[key]['remote_id'],remote_url=known[key]['remote_url'])
  elif key in batch_known:x['duplicate_of_sequence']=batch_known[key]
  else:payload+=x['bytes'];batch_known[key]=x['sequence']
  rows.append(x)
  if len(rows)>=20:break
 assert rows,'NO_NEXT_BATCH_WITHIN_CAP'
 n=max([int(p.name.split('-')[1]) for p in BASE.glob('batch-*')])+1;d=BASE/f'batch-{n:04d}';d.mkdir(mode=0o700)
 m={'batch':n,'created_utc':now(),'files':rows,'payload_bytes':payload,'uploaded_before_including_control_files':total,'safe_allowance_bytes':allowance,'final_control_document_reserve_bytes':10000000,'preflight':a}
 save(d/'MANIFEST.json',m);print(json.dumps({'batch_dir':str(d),'batch':n,'payload_bytes':payload,'files':[{k:x.get(k) for k in ['sequence','source_absolute','bytes','fresh_sha256','proposed_destination_name','duplicate_of_verified','duplicate_of_sequence','remote_id','remote_url']} for x in rows]},ensure_ascii=False))
elif cmd in ['check','upload','verify']:
 d=Path(a['batch_dir']);x=next(x for x in read(d/'MANIFEST.json')['files'] if x['sequence']==a['sequence']);seq=x['sequence']
 if cmd=='check':stable(x);print('STABLE')
 elif cmd=='upload':
  save(d/f'upload-{seq:05d}.json',{'sequence':seq,'remote_id':a['remote_id'],'remote_url':a['remote_url'],'upload_utc':now(),'upload_response':a['upload_response']});stable(x);print('UPLOAD_RECORDED')
 else:
  assert (d/'UPLOAD_ENDED.json').exists();u=read(d/f'upload-{seq:05d}.json');assert any(read(p)['utc']>=u['upload_utc'] for p in d.glob('UPLOAD*ENDED*.json')),'UPLOAD_PHASE_NOT_ENDED';stable(x);h=hashlib.sha256();n=0
  v={'sequence':seq,'remote_id':a['remote_id'],'retrieval_file_id':a['file_id'],'metadata':a['metadata'],'started_utc':now(),'retrieved_bytes':0,'status':'UNVERIFIED','method':'Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging'}
  try:
   with urllib.request.urlopen(a['download_url'],timeout=90) as f:
    v['http_status']=f.status;v['response_content_length']=f.headers.get('Content-Length')
    if x.get('package_manifest'):
     class HashReader:
      def __init__(self,stream):self.stream=stream;self.h=hashlib.sha256();self.n=0
      def read(self,size=-1):
       b=self.stream.read(size);self.h.update(b);self.n+=len(b);return b
     hr=HashReader(f);members=read(x['package_manifest'])['members'];expected={m['restore_relative']:m for m in members};expected[x['package_metadata_member']]={'bytes':x['package_metadata_bytes'],'sha256':x['package_metadata_sha256']};seen=set();logical=0
     with tarfile.open(fileobj=hr,mode='r|gz') as tf:
      for ti in tf:
       assert ti.isfile() and ti.name in expected and ti.name not in seen,'UNEXPECTED_ARCHIVE_MEMBER'
       mh=hashlib.sha256();mn=0
       with tf.extractfile(ti) as mf:
        for b in iter(lambda:mf.read(1048576),b''):mh.update(b);mn+=len(b)
       assert mn==expected[ti.name]['bytes'] and mh.hexdigest()==expected[ti.name]['sha256'],'REMOTE_MEMBER_MISMATCH'
       seen.add(ti.name)
       if ti.name!=x['package_metadata_member']:logical+=mn
     while hr.read(1048576):pass
     assert seen==set(expected),'INCOMPLETE_ARCHIVE_MEMBERS'
     h=hr.h;n=hr.n;v.update(package_source_members_verified=len(members),package_uncompressed_member_bytes_verified=logical,package_member_provenance=x['package_manifest'],package_exact_duplicate_aliases_reused=len(read(x['package_manifest']).get('duplicate_aliases',[])))
    else:
     for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
   v.update(retrieved_bytes=n,retrieved_sha256=h.hexdigest());assert n==x['bytes'],'RETRIEVED_SIZE_MISMATCH';assert h.hexdigest()==x['fresh_sha256'],'SHA256_MISMATCH';stable(x);v.update(status='VERIFIED',source_stable_after_retrieval=True)
  except Exception as e:
   if 'hr' in locals():n=hr.n;h=hr.h
   v.update(retrieved_bytes=n,error_type=type(e).__name__,error=str(e) if isinstance(e,AssertionError) else type(e).__name__)
   if hasattr(e,'code'):v['http_error_code']=e.code
  v['finished_utc']=now();save(d/f'verify-{seq:05d}-attempt-{a["attempt"]}.json',v)
  print(json.dumps({k:v.get(k) for k in ['sequence','status','retrieved_bytes','retrieved_sha256','error','http_error_code']}))
elif cmd=='end':
 d=Path(a['batch_dir']);p=d/'UPLOAD_ENDED.json'
 if p.exists():p=d/f'UPLOAD_PHASE_{len(list(d.glob("UPLOAD*ENDED*.json")))+1}_ENDED.json'
 save(p,{'utc':now(),'status':'UPLOAD_PHASE_ENDED'});print(str(p.name))
elif cmd=='freeze':
 d=Path(a['batch_dir']);m=read(d/'MANIFEST.json');rows=[]
 for original in m['files']:
  x=dict(original);stable(x);seq=x['sequence']
  if x.get('duplicate_of_sequence'):
   prev=next(y for y in rows if y['sequence']==x['duplicate_of_sequence']);x.update(duplicate_of_verified=True,remote_id=prev['remote_id'],remote_url=prev['remote_url'])
  if x.get('duplicate_of_verified'):x['verification_basis']='Fresh exact source SHA-256/length equals prior complete remote verification; no additional remote upload or retrieved byte count'
  else:
   x.update(read(d/f'upload-{seq:05d}.json'));vs=[read(p) for p in d.glob(f'verify-{seq:05d}-attempt-*.json')];v=next(v for v in vs if v['status']=='VERIFIED' and v['retrieved_bytes']==x['bytes'] and v['retrieved_sha256']==x['fresh_sha256'] and v['remote_id']==x['remote_id']);x['retrieval']=v
  x['status']='VERIFIED';x['upload_status']='EXACT_DUPLICATE_MAPPING' if x.get('duplicate_of_verified') else 'UPLOADED_AND_VERIFIED';x['binary_restore_status']='COMPLETE_REMOTE_BYTES_SHA256_VERIFIED';rows.append(x)
 r={'status':'VERIFIED','batch':m['batch'],'completed_utc':now(),'files':rows,'uploaded_bytes':sum(x['bytes'] for x in rows if not x.get('duplicate_of_verified')),'independently_retrieved_bytes':sum(x['retrieval']['retrieved_bytes'] for x in rows if 'retrieval' in x),'mapped_source_files':len(rows),'preflight':m['preflight'],'postflight':a,'permissions':'Owner-only Restricted; no changes','encryption':'Google provider managed; owner-held client key not established','retention':'Until explicit owner removal approval','coverage':'File-level verified recovery only; no complete-package or independent-machine recovery claim'}
 save(d/'RECOVERY_MAPPING.json',{'files':[{k:x.get(k) for k in ['source_absolute','restore_relative','bytes','fresh_sha256','remote_id','remote_url','backup_priority','required_companions','status','duplicate_of_verified']} for x in rows]});save(d/'RECEIPT.json',r)
 files=sorted(p for p in d.iterdir() if p.is_file())
 with (d/'SHA256SUMS').open('x') as f:
  for p in files:f.write(digest(p)+'  '+p.name+'\n')
 for p in files+[d/'SHA256SUMS']:p.chmod(0o400)
 print(json.dumps({'batch':m['batch'],'status':'VERIFIED','uploaded_bytes':r['uploaded_bytes'],'independently_retrieved_bytes':r['independently_retrieved_bytes']}))
elif cmd=='resume':
 d=Path(a['batch_dir']);m=read(d/'MANIFEST.json');rows=[]
 for x in m['files']:
  stable(x);z={k:x.get(k) for k in ['sequence','source_absolute','bytes','fresh_sha256','proposed_destination_name','duplicate_of_verified','duplicate_of_sequence','remote_id','remote_url']};seq=x['sequence'];up=d/f'upload-{seq:05d}.json'
  if up.exists():u=read(up);z.update(remote_id=u['remote_id'],remote_url=u['remote_url'])
  attempts=list(d.glob(f'verify-{seq:05d}-attempt-*.json'));z['next_attempt']=1+max([int(p.stem.rsplit('-',1)[1]) for p in attempts] or [0])
  for p in attempts:
   v=read(p)
   if v.get('status')=='VERIFIED' and v.get('retrieved_bytes')==x['bytes'] and v.get('retrieved_sha256')==x['fresh_sha256'] and v.get('remote_id')==z.get('remote_id'):z.update(verified_before=True,verified_modified_time=v['metadata'].get('modified_time'),verification_receipt=str(p))
  rows.append(z)
 dest=read(d/'DESTINATION.json')['folder'] if (d/'DESTINATION.json').exists() else {'id':'12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf','url':'https://drive.google.com/drive/folders/12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf'}
 print(json.dumps({'batch_dir':str(d),'batch':m['batch'],'payload_bytes':m['payload_bytes'],'destination_folder_id':dest['id'],'destination_url':dest['url'],'files':rows},ensure_ascii=False))
elif cmd=='event':
 assert Path(a['name']).name==a['name'],'INVALID_EVENT_NAME'
 save(Path(a['batch_dir'])/a['name'],{'observed_utc':now(),**a['data']});print('EVENT_RECORDED')
elif cmd=='state':
 done,known,total,verified=state();print(json.dumps({'mapped_source_paths':len(done),'uploaded_bytes_including_controls':total,'verified_bytes_including_controls':verified,'remaining_payload_bytes':12000000000-total,'remaining_plan_files':sum(x['source_absolute'] not in done for x in plan()['files'])}))
