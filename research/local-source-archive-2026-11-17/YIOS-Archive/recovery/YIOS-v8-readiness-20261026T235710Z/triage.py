import os,csv,json,hashlib,subprocess,collections,zipfile,io,re
from pathlib import Path
O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1');rows=list(csv.DictReader(open(A/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')))
def run(c,t=40):
 r=subprocess.run(c,cwd=P,env=env,capture_output=True,timeout=t);return {'exit':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')[:1000]}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def dump(n,d):(O/'evidence'/n).write_text(json.dumps(d,indent=2))
def stable(p,r):
 s=p.stat();return s.st_size==int(r['machine_a_size']) and s.st_mtime_ns==int(r['mtime_ns']) and s.st_ino==int(r['inode'])
# Fresh exact-blob lookup for eight candidates; no file data upload; 404 means lookup not found, not exhaustive other-provider absence.
eight=list(csv.DictReader(open(O/'EIGHT_FILE_PRESERVATION_VERIFICATION.csv')));lookups=[]
for v in eight:
 p=Path(v['source_path']);b=p.read_bytes();oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();r=run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/blobs/'+oid]);lookups.append({'source':str(p),'git_blob_sha1':oid,'http_api_result':r['exit'],'provider_not_found':'Not Found' in r['stderr'] or 'Not Found' in r['stdout'],'remote_match':r['exit']==0});v['remote_copy_status']='EXACT_GITHUB_BLOB_FOUND_REQUIRES_HASH_READBACK' if r['exit']==0 else 'NO_INDEPENDENT_COPY_PROVEN; exact GitHub blob lookup NOT_FOUND; sealed Drive mappings absent; other undiscovered copies unknown'
with open(O/'EIGHT_FILE_PRESERVATION_VERIFICATION.csv','w') as f:w=csv.DictWriter(f,fieldnames=eight[0]);w.writeheader();w.writerows(eight)
dump('EIGHT_GITHUB_BLOB_LOOKUPS.json',lookups)
# Bounded fresh checks, no new census
selected=list(csv.DictReader(open(O/'evidence/SELECTED_PRIOR_GAP_ROWS.csv')));tri=[];gray=[]
for r in selected:
 p=Path(r['absolute_path']);s=p.lstat();ok=stable(p,r);h=r['machine_a_sha256'];kind='NOT_YET_CLASSIFIABLE';reason='Existing local-only evidence; no full rebuild or independent original copy proof';priority='P2_REVIEW'
 if r['coverage_status']=='SAFE':kind='HASH_IDENTICAL_VERIFIED_REMOTE_ORIGINAL';priority='NO_UPLOAD';reason=r['drive_receipt_reference'] or r['git_commit_ref']
 elif p.name=='gray.u8':
  before=p.stat();h=sha(p);after=p.stat();vid=p.parent.name;F=Path('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research');src=json.load(open(F/'02_VIDEO_FORENSICS'/vid/'SOURCE.json'));sources=[x for x in rows if x['machine_a_sha256']==src['sha256'] and x['local_machine_a_presence']=='MACHINE_A_VERIFIED' and x['drive_remote_id']];source=next((x for x in sources if Path(x['absolute_path']).is_file() and stable(Path(x['absolute_path']),x)),None)
  test={'path':str(p),'size':s.st_size,'sha256':h,'stable':(before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns),'recipe':str(F/'_pipeline/stage_visual.py'),'recipe_sha256':sha(F/'_pipeline/stage_visual.py'),'source_sha256':src['sha256'],'source':source['absolute_path'] if source else None,'source_receipt':source['drive_receipt_reference'] if source else None,'full_regeneration':'NOT_PERFORMED'}
  if source:
   c=['ffmpeg','-v','error','-i',source['absolute_path'],'-an','-vf','scale=192:108:flags=area,format=gray','-fps_mode','passthrough','-frames:v','8','-f','rawvideo','-'];z=subprocess.run(c,capture_output=True,timeout=30)
   with open(p,'rb') as f:orig=f.read(192*108*8)
   test.update(sample_frames=8,sample_bytes=len(z.stdout),sample_regeneration_matches=z.returncode==0 and z.stdout==orig,ffmpeg_version=run(['ffmpeg','-version'])['stdout'].splitlines()[0],method='Direct known ffmpeg command; project Python not executed')
  gray.append(test);kind='DERIVED_RECIPE_IDENTIFIED_SAMPLE_TESTED';priority='P3_CONDITIONAL_NOT_APPROVED';reason='Original MP4 independently Drive verified; 8-frame sample tested; full stream bit-for-bit rebuild and independent recipe preservation remain required before dispensability'
 elif '/_pipeline/' in str(p):kind='REPRODUCTION_PROCEDURE_OR_HUMAN_ANNOTATION';priority='P1_REVIEW';reason='Procedure/source annotations can recreate outputs; not automatically covered by media backup'
 elif '/yios-recovery-status/' in str(p):kind='RECOVERY_OR_QA_EVIDENCE_UNIQUE_STATUS_UNPROVEN';reason='May include human QA and receipts; same-SSD copies not independent; compare preserved hashes before selection'
 elif '/casually-finance-script-intelligence/' in str(p):kind='UNPUBLISHED_AUTHORSHIP';priority='P0_EXACT_EIGHT';reason='One of six hash-confirmed unpublished documents; source ownership must be respected'
 elif p.suffix=='.zip':kind='FORENSIC_ARCHIVE_MEMBER_COMPARISON_REQUIRED';priority='P2_REVIEW';reason='Wrapper hash alone insufficient; compare each member with published skill and Drive originals'
 tri.append({'source_path':str(p),'size':s.st_size,'sha256':h,'hash_evidence':'FRESH_SHA256' if p.name=='gray.u8' else r['machine_a_hash_evidence'] if h else 'HASH_NEEDED','saved_identity_stable':ok,'classification':kind,'priority':priority,'reason':reason,'existing_remote_ids':r['drive_remote_id'],'receipt':r['drive_receipt_reference'],'source_owner':'Existing Finance/Visual session owner; no ownership release inferred','safe_to_read':'Read-only stable-stat inspection; active writer globally not provable','recommended_action':'Preserve; proposed review only; no upload/deletion'} )
with open(O/'LOCAL_ONLY_RISK_TRIAGE.csv','w') as f:w=csv.DictWriter(f,fieldnames=tri[0]);w.writeheader();w.writerows(tri)
dump('GRAY_ARRAY_REBUILD_EVIDENCE.json',gray)
# Check eleven exact missing dependencies again, never search unrelated Downloads.
missing=[]
for r in json.load(open(A/'evidence/REFERENCED_UNAVAILABLE_AND_UNLOCATED_SCOPE.json')):
 if r['status']=='REFERENCED_PATH_UNAVAILABLE_ON_MACHINE_A':
  p=Path(r['path']);r['current_exists']=p.exists();r['current_lstat']=str(p.lstat()) if p.exists() else None;missing.append(r)
dump('EDITING_DEPENDENCY_RECHECK.json',missing)
# Small forensic kits: read-only safe member/hash comparison with known Git blob IDs and Drive original mappings.
blobset=set()
for q in (A/'evidence').glob('REMOTE_TREE_*.txt'):
 try:blobset.update(x['sha'] for x in json.load(open(q))['tree'] if x['type']=='blob')
 except:pass
verifiedhashes={r['machine_a_sha256'] for r in rows if r['machine_a_sha256'] and r['coverage_status']=='SAFE'};kits=[]
for r in rows:
 p=Path(r['absolute_path'])
 if p.suffix!='.zip' or not ('forensic' in str(p).lower()) or not p.is_file() or int(r['machine_a_size'] or 0)>500000:continue
 try:
  with zipfile.ZipFile(p) as z:
   members=[]
   for n in z.infolist():
    if n.is_dir():continue
    if n.file_size>5000000:members.append({'name':n.filename,'status':'SKIP_LARGE'});continue
    b=z.read(n);hh=hashlib.sha256(b).hexdigest();oid=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();members.append({'name':n.filename,'size':len(b),'sha256':hh,'git_published_blob_match':oid in blobset,'verified_original_sha_match':hh in verifiedhashes,'path_safe':not Path(n.filename).is_absolute() and '..' not in Path(n.filename).parts})
   kits.append({'path':str(p),'archive_sha256':sha(p),'members':members,'unmatched_members':sum(not m.get('git_published_blob_match',False) and not m.get('verified_original_sha_match',False) for m in members)})
 except Exception as e:kits.append({'path':str(p),'error':type(e).__name__})
dump('SMALL_FORENSIC_KITS_MEMBER_CHECK.json',kits)
# Missing LFS historical objects are not automatically new original source gaps.
lf=list(csv.DictReader(open(O/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv')));dump('TRIAGE_SUMMARY.json',{'rows':len(tri),'classification':dict(collections.Counter(x['classification'] for x in tri)),'unstable_saved_identities':sum(not x['saved_identity_stable'] for x in tri),'gray_count':len(gray),'gray_bytes':sum(x['size'] for x in gray),'exact_github_found':sum(x['remote_match'] for x in lookups),'missing_editing_paths':sum(not x['current_exists'] for x in missing),'unverified_lfs_with_no_drive':[{k:x[k] for k in ['oid_sha256','expected_bytes','path']} for x in lf if x['integrity']!='PASS' and not x['drive_equivalent_ids']]})
print(json.dumps({'triage':len(tri),'gray':[(x['size'],x.get('sample_regeneration_matches')) for x in gray],'kits':[(x['path'],x.get('unmatched_members')) for x in kits],'eight_git_remote_found':sum(x['remote_match'] for x in lookups)},indent=2))
