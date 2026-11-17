import json,hashlib,csv,zipfile,os,collections,time
from pathlib import Path,PurePosixPath
O=Path(__file__).parent;root=Path('/Users/ghilmankhan/Downloads/videos in mp3');D=json.load(open(O/'checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'));known=collections.defaultdict(set)
for x in D['objects']:known[(x['sha256'],x['bytes'])].add(x['remote_id'])
for x in D['members']+D['aliases']:known[(x['sha256'],x['bytes'])].add(x.get('remote_archive_id') or x.get('remote_id'))
# Justified bounded hash pass over eight explicitly inventoried ZIPs: prove whether large source containers add any unique recoverable payload; no extraction, no recompression, no writes to originals.
summ=[]
for p in sorted(root.glob('*.zip')):
 before=p.stat();entries=[];total=0
 with zipfile.ZipFile(p) as z:
  for a in z.infolist():
   pp=PurePosixPath(a.filename);safe=not pp.is_absolute() and '..' not in pp.parts and '\\' not in a.filename
   if a.is_dir():continue
   if a.file_size>2_000_000_000:raise RuntimeError('Unexpected member bound')
   total+=a.file_size
   if total>12_000_000_000:raise RuntimeError('Archive logical bound')
   h=hashlib.sha256();n=0
   with z.open(a) as f:
    for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
   assert n==a.file_size
   sha=h.hexdigest();ids=sorted(known.get((sha,n),[]));osmeta=pp.name=='.DS_Store' or '__MACOSX' in pp.parts
   entries.append({'archive':str(p),'member':a.filename,'bytes':n,'sha256':sha,'path_safe_for_future_restore':safe,'drive_ids':'|'.join(ids),'coverage':'DRIVE_ORIGINAL_BYTES_SHA256_VERIFIED' if ids else 'OS_METADATA' if osmeta else 'MEMBER_BACKUP_GAP'})
 after=p.stat();assert all(getattr(before,k)==getattr(after,k) for k in ['st_ino','st_size','st_mtime_ns','st_ctime_ns'])
 out={'archive':str(p),'physical_local_bytes':before.st_size,'member_files':len(entries),'member_logical_bytes':total,'drive_covered_members':sum(bool(x['drive_ids']) for x in entries),'gap_members':sum(x['coverage']=='MEMBER_BACKUP_GAP' for x in entries),'gap_bytes':sum(x['bytes'] for x in entries if x['coverage']=='MEMBER_BACKUP_GAP'),'source_stat_stable':True,'archive_container_byte_recovery':'NOT_INDEPENDENTLY_BACKED_UP_UNLESS_SEPARATE_RECEIPT; member recovery is separate','member_results':entries}
 (O/'checkpoints'/('MEDIA_ZIP_'+hashlib.sha256(str(p).encode()).hexdigest()[:12]+'.json')).write_text(json.dumps(out,indent=2));summ.append(out);print(json.dumps({k:v for k,v in out.items() if k!='member_results'}),flush=True)
(O/'evidence/MEDIA_ZIP_COVERAGE_SUMMARY.json').write_text(json.dumps(summ,indent=2))
with open(O/'MEDIA_ZIP_MEMBER_COVERAGE.csv','x') as f:
 w=csv.DictWriter(f,fieldnames=list(summ[0]['member_results'][0]));w.writeheader();w.writerows(x for a in summ for x in a['member_results'])
