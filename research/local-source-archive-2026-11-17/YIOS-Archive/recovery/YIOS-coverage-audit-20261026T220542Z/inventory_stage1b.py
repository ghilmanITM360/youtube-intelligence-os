import os,stat,json,csv,hashlib,collections,time,subprocess
from pathlib import Path
O=Path(__file__).parent; H=Path('/Users/ghilmankhan'); R=H/'YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd'
roots=[H/'Downloads/CasuallyFinance-Forensic-Research']
# Root overlap removed using lexical paths; symlinks not followed.
unique=[]
for r in sorted(set(roots),key=lambda p:(len(p.parts),str(p))):
 if not any(str(r).startswith(str(a)+'/') for a in unique):unique.append(r)
roots=unique
errors=[];excluded=[];rootresults=[];cnt=0
fields=['root','path','relative','kind','bytes','allocated_bytes','device','inode','nlink','mtime_ns','ctime_ns','flags','dataless','extension','category','symlink_target']
def cat(p):
 if '.git' in p.parts:return 'git-internals'
 if any(x in p.parts for x in ['node_modules','__pycache__','.venv','site-packages','.pytest_cache','.mypy_cache']):return 'dependency-cache'
 if p.name=='.DS_Store':return 'os-metadata'
 e=p.suffix.lower()
 if e in ['.mp4','.mov','.mkv','.webm','.m4v','.mp3','.wav','.m4a','.aac']:return 'media'
 if e in ['.png','.jpg','.jpeg','.webp','.svg','.gif','.heic']:return 'image'
 if e in ['.zip','.gz','.tgz','.tar','.bundle','.bak']:return 'archive'
 if e in ['.db','.sqlite','.sqlite3']:return 'database'
 if e in ['.py','.sh','.js','.ts','.tsx','.jsx','.html','.css']:return 'code'
 if e in ['.json','.jsonl','.csv','.tsv','.yaml','.yml','.toml','.srt','.vtt']:return 'structured-data'
 return 'document-or-other'
def row(root,p):
 try:s=p.lstat()
 except OSError as e:errors.append({'path':str(p),'error':str(e)});return
 kind='symlink' if stat.S_ISLNK(s.st_mode) else 'directory' if stat.S_ISDIR(s.st_mode) else 'regular' if stat.S_ISREG(s.st_mode) else 'special'
 return dict(root=str(root),path=str(p),relative=str(p.relative_to(root)) if p!=root else '.',kind=kind,bytes=s.st_size,allocated_bytes=s.st_blocks*512,device=s.st_dev,inode=s.st_ino,nlink=s.st_nlink,mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns,flags=hex(s.st_flags),dataless=bool(s.st_flags&0x40000000),extension=p.suffix.lower(),category=cat(p),symlink_target=os.readlink(p) if kind=='symlink' else '')
with open(O/'checkpoints/STAGE1B_REFERENCED_CENSUS.csv','x') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for root in roots:
  a=row(root,root)
  if a is None:rootresults.append({'root':str(root),'status':'UNAVAILABLE'});continue
  st={'root':str(root),'status':'FULL_METADATA_CENSUS','files':0,'directories':0,'symlinks':0,'logical_bytes':0,'dataless_files':0,'dataless_bytes':0,'errors_at_start':len(errors)}
  def emit(a):
   if not a:return
   w.writerow(a)
   if a['kind']=='regular':
    st['files']+=1;st['logical_bytes']+=a['bytes']
    if a['dataless']:st['dataless_files']+=1;st['dataless_bytes']+=a['bytes']
   elif a['kind']=='directory':st['directories']+=1
   elif a['kind']=='symlink':st['symlinks']+=1
  emit(a)
  if a['kind']=='directory':
   for d,ds,fs in os.walk(root,followlinks=False,onerror=lambda e:errors.append({'path':e.filename,'error':str(e)})):
    for n in list(ds):
     p=Path(d)/n
     if root==H/'yios-git-recovery' and 'offline-map' in n.lower():excluded.append(str(p));ds.remove(n);continue
     b=row(root,p);emit(b)
     if b and b['kind']=='symlink':ds.remove(n)
    for n in fs:
     p=Path(d)/n
     if root==H/'yios-git-recovery' and 'offline-map' in n.lower():excluded.append(str(p));continue
     emit(row(root,p))
  st['errors']=len(errors)-st.pop('errors_at_start')
  if st['errors']:st['status']='PARTIAL_METADATA_CENSUS'
  rootresults.append(st);f.flush();os.fsync(f.fileno());print(json.dumps(st),flush=True)
  (O/'checkpoints/STAGE1B_PROGRESS.json').write_text(json.dumps(rootresults,indent=2))
(O/'evidence/ROOT_SCOPE_ADDITIONS.json').write_text(json.dumps({'roots':rootresults,'errors':errors,'excluded_unrelated':excluded,'symlinks_followed':False,'read_source_bytes':False,'non_atomic_live_census':True,'purpose':'Metadata census; dataless placeholders not hydrated; caches and Git internals separately classified'},indent=2))
