import os,json,csv,hashlib,subprocess,urllib.request,urllib.error,base64,time,shutil,sqlite3
from pathlib import Path
os.umask(0o077);O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
ps=list(csv.DictReader(open(A/'LFS_POINTER_PAYLOAD_CROSSWALK.csv')));token=subprocess.check_output(['gh','auth','token'],stderr=subprocess.PIPE).decode().strip();auth=base64.b64encode(('x-access-token:'+token).encode()).decode();req=urllib.request.Request('https://github.com/ghilmanITM360/youtube-intelligence-os.git/info/lfs/objects/batch',data=json.dumps({'operation':'download','transfers':['basic'],'objects':[{'oid':x['sha256'],'size':int(x['bytes'])} for x in ps]}).encode(),headers={'Authorization':'Basic '+auth,'Content-Type':'application/vnd.git-lfs+json','Accept':'application/vnd.git-lfs+json'},method='POST')
with urllib.request.urlopen(req,timeout=40) as r:data=json.load(r)
objects={x['oid']:x for x in data['objects']}; total=3012353 # prior audit sample counted conservatively against combined cap
ordered=[ps[0]]+sorted(ps[1:],key=lambda x:int(x['bytes']));results=[]
refs=subprocess.check_output(['git','ls-remote','--heads','origin'],cwd=P).decode();(O/'evidence/LIVE_REMOTE_REFS.txt').write_text(refs)
# Map pointer blobs to authoritative saved exact remote trees; unchanged refs noted separately.
trees=[]
for p in (A/'evidence').glob('REMOTE_TREE_*.txt'):
 try:trees.append((p.name,json.load(open(p))['tree']))
 except:pass
for p in ordered:
 oid=p['sha256'];size=int(p['bytes']);obj=objects.get(oid,{});act=obj.get('actions',{}).get('download');refmatches=[name for name,tree in trees if any(t.get('sha')==p['git_pointer_blob'] for t in tree)]
 row={'oid_sha256':oid,'expected_bytes':size,'pointer_blob_sha1':p['git_pointer_blob'],'path':p['path'],'git_ref_evidence':';'.join(refmatches) or 'Historical bounded local tree; see sealed GITHUB_AND_LFS_RECOVERY_STATUS.csv','remote_download_offered':bool(act),'bytes_retrieved':0,'actual_sha256':'','integrity':'NOT_TESTED','recovery_status':'REMOTE_LFS_PAYLOAD_NOT_VERIFIED','reason':'Combined 200MB cap; prioritize current catalog then smallest objects','drive_equivalent_ids':p['drive_remote_ids'],'independent_original_coverage':p['original_recovery'],'download_file':''}
 if act and total+size<=200000000 and shutil.disk_usage(O).free-size>=5000000000:
  dest=O/'scratch-private'/('lfs-'+oid);h=hashlib.sha256();n=0
  try:
   with urllib.request.urlopen(urllib.request.Request(act['href'],headers=act.get('header',{})),timeout=45) as response,open(dest,'xb') as f:
    length=response.headers.get('Content-Length')
    if length and int(length)!=size:raise ValueError('Unexpected content length')
    while True:
     b=response.read(min(1048576,size-n+1))
     if not b:break
     n+=len(b);total+=len(b)
     if n>size or total>200000000:raise ValueError('Download size limit exceeded')
     h.update(b);f.write(b)
   row.update(bytes_retrieved=n,actual_sha256=h.hexdigest(),download_file=str(dest),reason='Full authenticated LFS download; no signed URL/token retained')
   row['integrity']='PASS' if n==size and h.hexdigest()==oid else 'FAIL';row['recovery_status']='LFS_POINTER_REMOTE_OBJECT_VERIFIED' if row['integrity']=='PASS' else 'INTEGRITY_BLOCKER'
   if p is ps[0] and row['integrity']=='PASS':
    db=sqlite3.connect('file:'+str(dest)+'?mode=ro&immutable=1',uri=True);row['sqlite_quick_check']=db.execute('pragma quick_check').fetchall();db.close()
  except Exception as e:
   row.update(bytes_retrieved=n,reason='READ_FAILED: '+type(e).__name__,integrity='ERROR'); results.append(row);break
 results.append(row)
 fields=['oid_sha256','expected_bytes','pointer_blob_sha1','path','git_ref_evidence','remote_download_offered','bytes_retrieved','actual_sha256','integrity','recovery_status','reason','drive_equivalent_ids','independent_original_coverage','download_file','sqlite_quick_check']
 with open(O/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(results)
 (O/'evidence/LFS_PROGRESS.json').write_text(json.dumps({'objects':len(results),'new_bytes':total-3012353,'combined_test_bytes':total,'cap':200000000,'pass':sum(x['integrity']=='PASS' for x in results),'download_urls_retained':False},indent=2))
 print(oid[:12],row['integrity'],n if 'n' in locals() else 0,'combined',total,flush=True)
print('DONE',len(results),total)
