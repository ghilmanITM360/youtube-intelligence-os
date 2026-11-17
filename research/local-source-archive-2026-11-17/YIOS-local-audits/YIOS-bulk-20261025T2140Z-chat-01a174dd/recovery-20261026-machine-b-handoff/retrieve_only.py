import sys,json,os,stat,hashlib,datetime,urllib.request
from pathlib import Path
base=Path(__file__).parent
a=json.loads(sys.argv[1]);seq=a['sequence']
x=next(x for x in json.loads((base.parent/'batch-0009/MANIFEST.json').read_text())['files'] if x['sequence']==seq)
x['upload']=json.loads((base.parent/'batch-0009'/f'upload-{seq:05d}.json').read_text())
def snap():
 s=os.stat(x['source_absolute'],follow_symlinks=False)
 assert stat.S_ISREG(s.st_mode),'SOURCE_TYPE_CHANGED'
 return {k:getattr(s,k) for k in x['fresh_stat']}
def localhash():
 h=hashlib.sha256()
 with open(x['source_absolute'],'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
r={'sequence':seq,'attempt':a['attempt'],'remote_id':x['upload']['remote_id'],'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'metadata':a['metadata'],'retrieval_file_id':a['file_id'],'retrieved_bytes':0,'status':'UNVERIFIED','method':'Fresh authenticated connector raw fetch by remote identity; complete response streamed into SHA-256 without local source substitution or staging'}
h=hashlib.sha256()
try:
 assert snap()==x['fresh_stat'],'SOURCE_CHANGED_SINCE_UPLOAD'
 assert localhash()==x['fresh_sha256'],'SOURCE_HASH_CHANGED'
 assert snap()==x['fresh_stat'],'SOURCE_CHANGED_DURING_HASH'
 with urllib.request.urlopen(a['download_url'],timeout=45) as f:
  r['http_status']=f.status
  r['response_content_length']=f.headers.get('Content-Length')
  for b in iter(lambda:f.read(1048576),b''):
   h.update(b);r['retrieved_bytes']+=len(b)
 r['retrieved_sha256']=h.hexdigest()
 assert r['retrieved_bytes']==x['bytes'],'RETRIEVED_SIZE_MISMATCH'
 assert h.hexdigest()==x['fresh_sha256'],'RETRIEVED_SHA256_MISMATCH'
 assert snap()==x['fresh_stat'],'SOURCE_CHANGED_AFTER_RETRIEVAL'
 r.update(status='VERIFIED',source_stable=True,verified_bytes=r['retrieved_bytes'])
except Exception as e:
 r.update(error_type=type(e).__name__,error=str(e) if isinstance(e,AssertionError) else type(e).__name__,partial_sha256=h.hexdigest(),verified_bytes=0)
 if hasattr(e,'code'):r['http_error_code']=e.code
r['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=base/f"object-{seq:05d}-attempt-{a['attempt']}.json"
with p.open('x') as f:json.dump(r,f,indent=2)
p.chmod(0o600)
print(json.dumps({k:r.get(k) for k in ['sequence','attempt','status','retrieved_bytes','verified_bytes','error_type','error']}))
