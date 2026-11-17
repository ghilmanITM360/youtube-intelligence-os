import json,hashlib,subprocess,base64,tarfile,os,io,wave,shutil
from pathlib import Path,PurePosixPath
O=Path(__file__).parent;S=O/'restore-scratch-private';R=Path('/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');results=[]
# Recover one tracked research/provenance artifact through exact authenticated GitHub blob, without checkout.
T=json.load(open(O/'evidence/REMOTE_TREE_WHATIF.txt'));path='docs/WHAT_IF_FORENSIC_SOURCE_CONTRACT.md';a=next(x for x in T['tree'] if x['path']==path);r=subprocess.run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/blobs/'+a['sha']],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True);b=base64.b64decode(json.loads(r.stdout)['content']);g=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();assert g==a['sha'];local=P/path;assert hashlib.sha256(local.read_bytes()).hexdigest()==hashlib.sha256(b).hexdigest();f=S/'tracked-research-artifact.md';f.open('xb').write(b);os.chmod(f,0o600);b.decode('utf-8');results.append({'category':'TRACKED_GIT_RESEARCH_ARTIFACT','source_path':str(local),'remote_commit':T['sha'],'git_blob_sha1':g,'sha256':hashlib.sha256(b).hexdigest(),'recovered_bytes':len(b),'result':'PASS','validation':'Authenticated complete GitHub blob, exact Git SHA1, SHA256 local match, UTF8 parse','restored_path':str(f)})
raw=json.load(open(O/'evidence/RESTORE_RAW_RECEIPTS.json'));assert all(x['result']['pass'] for x in raw)
for a in raw:results.append({'category':'DRIVE_RAW_ORIGINAL','source_path':a['target']['source'],'remote_id':a['target']['remote_id'],'sha256':a['result']['sha256'],'recovered_bytes':a['result']['bytes'],'result':'PASS','restored_path':a['result']['path'],'validation':'Fresh authenticated full bytes; exact recorded length and SHA256'})
# No extractall; validate every path/type/size/hash and materialize only selected small members into fresh isolated subdirectory.
mp=R/'selected-evidence-packages-20261026/04035-forensic-JsK53moCyZA-part01.members.json';md=json.load(open(mp));members={x['restore_relative']:x for x in md['members']};ar=S/'04035-forensic-JsK53moCyZA-part01.tar.gz';sub=S/'safe-members';sub.mkdir(mode=0o700);checked=[];total=0;seen=set()
with tarfile.open(ar,'r|gz') as tf:
 for m in tf:
  pp=PurePosixPath(m.name);assert not pp.is_absolute() and '..' not in pp.parts and '\\' not in m.name and m.name not in seen;seen.add(m.name);assert m.isfile(),'No links/devices/executable execution';assert m.size<=100_000_000;total+=m.size;assert total<=200_000_000
  body=tf.extractfile(m);h=hashlib.sha256();buf=bytearray()
  for chunk in iter(lambda:body.read(1048576),b''):h.update(chunk);buf.extend(chunk)
  if m.name in members:
   ex=members[m.name];assert len(buf)==ex['bytes'] and h.hexdigest()==ex['sha256'];checked.append({'member':m.name,'sha256':h.hexdigest(),'bytes':len(buf),'result':'PASS'})
   # Actual selected originals restored: WAV plus image/structured companions, all new files.
   if len(checked)<=3:
    dest=sub/('%02d-'%len(checked)+pp.name);dest.open('xb').write(buf);os.chmod(dest,0o600)
    if pp.suffix=='.wav':
     with wave.open(str(dest),'rb') as w:assert w.getnframes()>0
    if pp.suffix=='.json':json.loads(buf)
  else:
   assert m.name.startswith('_recovery/'),'Unexpected unmanifested member';emb=json.loads(buf);assert emb['members']==md['members']
assert len(checked)==len(members)
results.append({'category':'DRIVE_FORENSIC_ARCHIVE_AND_ORIGINAL_MEMBERS','source_path':str(mp),'remote_id':'1TDZDudFFyZXVfZc3jKPgX-05re9smAaO','result':'PASS','all_original_members':len(checked),'all_original_member_bytes':sum(x['bytes'] for x in checked),'checked':checked,'validation':'All archive members fully hashed; exact manifest agreement; path traversal/absolute paths/links rejected; three small originals materialized; WAV header parsed; no code execution','archive_total_decompressed_bytes':total})
# Read-only parser validation of recovered source audio; no playback or script/application execution.
ff=shutil.which('ffprobe')
if ff:
 x=subprocess.run([ff,'-v','error','-show_entries','format=format_name,duration:stream=codec_type,codec_name','-of','json',str(S/'original_audio.m4a')],stdout=subprocess.PIPE,stderr=subprocess.PIPE);assert x.returncode==0;results.append({'category':'SOURCE_AUDIO_FORMAT','result':'PASS','parsed':json.loads(x.stdout)})
else:results.append({'category':'SOURCE_AUDIO_FORMAT','result':'NOT_TESTED','reason':'ffprobe unavailable; SHA256 bytes still verified'})
(S/'YIOS_MACHINE_B_HANDOFF_20261026.md').read_text(encoding='utf-8');download=sum(x['result']['bytes'] for x in raw)+len(b);assert download<100_000_000
out={'status':'SMALL_SAMPLE_PASS_NOT_FULL_DISASTER_RECOVERY','scratch':str(S),'raw_downloaded_bytes':download,'hard_cap':200_000_000,'target':100_000_000,'source_files_overwritten':0,'code_executed_from_restored_content':False,'results':results,'not_proven':['MachineB filesystem census','independent machine bootstrap','full CapCut media/font/runtime dependencies','remote LFS payload availability','full archive package set restore','iCloud placeholder hydration/recovery']};(O/'evidence/RESTORE_TEST_DETAILS.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2));print('checked archive originals',len(checked))
