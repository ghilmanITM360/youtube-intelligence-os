import json,gzip,csv,hashlib,collections,os
from pathlib import Path
O=Path(__file__).parent;R=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');H=Path('/Users/ghilmankhan')
cache=json.loads((O/'hashes.json').read_text());rows=list(csv.DictReader(gzip.open(O/'files.csv.gz','rt')));read=0;budget=64*1024**2
for x in rows:
 p=Path(x['path']);size=int(x['bytes'])
 if str(p) in cache or x['category'] not in ['report-document','structured-data','code'] or size>4*1024**2 or read+size>budget:continue
 if Path(x['root']).name not in ['video data of what if','yio-cf-editing-forensics-local-evidence','yios-recovery-status'] and 'NICK_170' not in str(p):continue
 a=p.stat();data=p.read_bytes();b=p.stat();read+=len(data)
 cache[str(p)]={'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha1':hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest(),'bytes':len(data),'stable_during_read':(a.st_size,a.st_mtime_ns)==(b.st_size,b.st_mtime_ns)}
(O/'hashes.json').write_text(json.dumps(cache,indent=2))
# Check known What If media against canonical crosswalk using already computed SHA256.
j=json.loads((R/'data/manifests/what-if-forensic-source-v1.json').read_text());base=H/'workprojects/video data of what if';media=[]
for x in j['sources']:
 p=base/x['relative_media_path'];v=cache.get(str(p));media.append({'source_video_id':x['source_video_id'],'path':str(p),'expected_sha256':x['sha256'],'actual_sha256':v['sha256'] if v else None,'size_matches':p.stat().st_size==x['size_bytes'],'status':'PASS' if v and v['sha256']==x['sha256'] and p.stat().st_size==x['size_bytes'] else 'UNVERIFIED_OR_MISMATCH'})
(O/'what-if-source-verification.json').write_text(json.dumps(media,indent=2))
# Compare active and released canonical tables; keep drift explicit.
a=base/'production_intelligence_brain';b=base/'releases/production_intelligence_brain-v1.0.0';pairs=[]
for p in b.rglob('*'):
 if not p.is_file() or p.name=='.DS_Store':continue
 q=a/p.relative_to(b);va=cache.get(str(q));vb=cache.get(str(p))
 pairs.append({'relative':str(p.relative_to(b)),'status':'IDENTICAL_SHA256' if va and vb and va['sha256']==vb['sha256'] else 'DIFFERENT_SHA256' if va and vb else 'NOT_HASHED','working_sha256':va['sha256'] if va else None,'release_sha256':vb['sha256'] if vb else None})
(O/'what-if-release-comparison.json').write_text(json.dumps(pairs,indent=2))
print('supplement bytes',read,'hashes',len(cache),'source media',collections.Counter(x['status'] for x in media),'release compare',collections.Counter(x['status'] for x in pairs))
