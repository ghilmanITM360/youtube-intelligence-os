import sys,json,os,hashlib,datetime,urllib.request,stat
from pathlib import Path
BASE=Path(__file__).parent
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text())
def write(p,v):
    p=Path(p)
    with p.open('x') as f: json.dump(v,f,indent=2,ensure_ascii=False)
    p.chmod(0o600)
def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()
def snap(p):
    s=os.stat(p,follow_symlinks=False)
    assert stat.S_ISREG(s.st_mode),'SOURCE_TYPE_CHANGED'
    return {k:getattr(s,k) for k in ['st_size','st_mtime_ns','st_ctime_ns','st_ino','st_dev']}
def stable(x): assert snap(x['source_absolute'])==x['fresh_stat'],'SOURCE_MODIFIED'
cmd=sys.argv[1];arg=json.loads(sys.argv[2]) if len(sys.argv)>2 else {}
if cmd=='prepare':
    plan=read(BASE/'ORDERED_PLAN_V2.json');done=set();known={}
    pilot=read('/Users/ghilmankhan/YIOS-local-audits/YIOS-pilot-20261025T2120Z-chat-01a174dd/receipt.json')
    for x in pilot['files']:known[(x['refreshed_sha256'],x['bytes'])]={'remote_id':x['remote_id'],'remote_url':x['remote_url'],'verified':True}
    uploaded=95436174
    for d in sorted(BASE.glob('batch-*')):
        assert (d/'RECEIPT.json').exists(),'INCOMPLETE_PREVIOUS_BATCH'
        r=read(d/'RECEIPT.json');assert r['status']=='VERIFIED'
        for x in r['files']:
            done.add(x['source_absolute']);known[(x['fresh_sha256'],x['bytes'])]={'remote_id':x['remote_id'],'remote_url':x['remote_url'],'verified':True}
            if not x.get('duplicate_of_verified'):uploaded+=x['bytes']
    allowance=min(12000000000-uploaded,arg['conservative_free_bytes']-2000000000)
    assert allowance>0,'CAPACITY_STOP'
    batch=[];payload=0;batch_known={}
    for x in plan['files']:
        if x['source_absolute'] in done:continue
        if payload+x['bytes']>min(500000000,allowance):break
        s=snap(x['source_absolute']);assert s['st_size']==x['bytes'] and s['st_mtime_ns']==x['mtime_ns'] and s['st_ino']==x['inode'],'SOURCE_CHANGED_SINCE_MANIFEST'
        h=digest(x['source_absolute']);assert snap(x['source_absolute'])==s,'SOURCE_MODIFIED_DURING_HASH'
        x.update(fresh_stat=s,fresh_sha256=h,hash_refreshed_utc=now(),source_hash_status='FRESH_STABLE')
        key=(h,x['bytes'])
        if key in known:x.update(known[key],duplicate_of_verified=True)
        elif key in batch_known:x['duplicate_of_sequence']=batch_known[key]
        else:payload+=x['bytes'];batch_known[key]=x['sequence']
        batch.append(x)
        if len(batch)>=20:break
    assert batch,'NO_NEXT_BATCH'
    n=len(list(BASE.glob('batch-*')))+1;d=BASE/f'batch-{n:04d}';d.mkdir(mode=0o700)
    manifest={'batch':n,'created_utc':now(),'gate':arg,'payload_bytes':payload,'uploaded_before_including_pilot':uploaded,'safe_allowance_bytes':allowance,'files':batch}
    write(d/'MANIFEST.json',manifest)
    print(json.dumps({'batch_dir':str(d),'manifest':manifest},ensure_ascii=False))
elif cmd=='check':
    x=read(arg['batch_dir']+'/MANIFEST.json')['files'][arg['index']];stable(x);print('STABLE')
elif cmd=='upload':
    d=Path(arg['batch_dir']);x=read(d/'MANIFEST.json')['files'][arg['index']];stable(x)
    write(d/f"upload-{x['sequence']:05d}.json",dict(sequence=x['sequence'],remote_id=arg['remote_id'],remote_url=arg['remote_url'],upload_utc=now(),returned_metadata=arg.get('metadata')))
    print('UPLOAD_RECORDED')
elif cmd=='end':
    write(Path(arg['batch_dir'])/'UPLOAD_ENDED.json',{'utc':now(),'status':'UPLOAD_PHASE_ENDED_RETRIEVAL_PENDING'});print('UPLOAD_ENDED')
elif cmd=='verify':
    d=Path(arg['batch_dir']);assert (d/'UPLOAD_ENDED.json').exists()
    x=read(d/'MANIFEST.json')['files'][arg['index']];stable(x);h=hashlib.sha256();n=0
    with urllib.request.urlopen(arg['download_url'],timeout=120) as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b);n+=len(b)
    assert n==x['bytes'],'RETRIEVED_SIZE_MISMATCH'
    assert h.hexdigest()==x['fresh_sha256'],'RETRIEVED_SHA256_MISMATCH'
    stable(x)
    record={'sequence':x['sequence'],'remote_id':arg['remote_id'],'retrieval_file_id':arg['file_id'],'retrieved_bytes':n,'retrieved_sha256':h.hexdigest(),'retrieved_utc':now(),'method':'Fresh authenticated connector complete raw fetch by remote object identity, streamed URL response directly into SHA-256; no source substitution or local staging','source_stable_after_retrieval':True,'metadata':arg['metadata']}
    write(d/f"verify-{x['sequence']:05d}.json",record);print(json.dumps({'verified_bytes':n,'sha256':h.hexdigest()}))
elif cmd=='freeze':
    d=Path(arg['batch_dir']);m=read(d/'MANIFEST.json');files=[]
    for x in m['files']:
        stable(x);seq=x['sequence']
        if x.get('duplicate_of_verified'):x['verification_basis']='Existing complete authenticated hash-verified remote bytes; fresh local exact SHA-256 equality'
        elif x.get('duplicate_of_sequence'):
            other=next(y for y in files if y['sequence']==x['duplicate_of_sequence']);x.update(remote_id=other['remote_id'],remote_url=other['remote_url'],duplicate_of_verified=True,verification_basis='Same-batch exact SHA-256 and length; remote complete retrieval verified')
        else:
            x.update(read(d/f'upload-{seq:05d}.json'));x['retrieval']=read(d/f'verify-{seq:05d}.json')
        x['status']='VERIFIED'
        x['upload_status']='EXISTING_VERIFIED_EXACT_DUPLICATE_MAPPING' if x.get('duplicate_of_verified') else 'UPLOADED_AND_VERIFIED'
        x['binary_restore_status']='COMPLETE_REMOTE_BYTES_SHA256_VERIFIED'
        x['hash_status']='FRESH_STABLE_SOURCE_SHA256_VERIFIED'
        files.append(x)
    r={'status':'VERIFIED','batch':m['batch'],'completed_utc':now(),'preflight':m['gate'],'postflight':arg,'files':files,'uploaded_bytes':sum(x['bytes'] for x in files if not x.get('duplicate_of_verified')),'independently_retrieved_bytes':sum(x['retrieval']['retrieved_bytes'] for x in files if 'retrieval' in x),'mapped_source_files':len(files),'permissions':'Owner-only; inherited Restricted yios; no permission modifications','encryption':'Google provider managed; owner-held client key not established','retention':'Until explicit owner removal approval','coverage':'File-level cloud recovery only; no independent-machine disaster recovery assertion; external dependencies may remain missing'}
    write(d/'RECOVERY_MAPPING.json',{'files':[{k:x.get(k) for k in ['source_absolute','restore_relative','bytes','fresh_sha256','remote_id','remote_url','backup_priority','duplicate_of_verified','required_companions']} for x in files]})
    write(d/'RECEIPT.json',r)
    with (d/'SHA256SUMS').open('x') as f:
        for name in ['MANIFEST.json','RECOVERY_MAPPING.json','RECEIPT.json']:f.write(digest(d/name)+'  '+name+'\n')
    (d/'SHA256SUMS').chmod(0o600)
    print(json.dumps({k:r[k] for k in ['status','batch','uploaded_bytes','independently_retrieved_bytes','mapped_source_files']}))
