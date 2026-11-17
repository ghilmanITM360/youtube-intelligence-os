import os,stat,json,collections,gzip,csv,subprocess,time
from pathlib import Path
OUT=Path(__file__).parent
HOME=Path('/Users/ghilmankhan')
roots=[HOME/'workprojects'/x for x in ['youtube-intelligence-os','video data of what if','yios-recovery-status','yio-cf-editing-forensics-local-evidence','yios-visual-forensics-install-candidate-2026-10-24']]+[HOME/'YIOS-local-audits',HOME/'yios-git-recovery']
rows=[]; errors=[]; excluded=[]; links=[]; gitmarkers=[]
def cat(p):
 parts=p.parts; e=p.suffix.lower()
 if '.git' in parts:return 'git-internals'
 if any(x in parts for x in ['node_modules','__pycache__','.venv','site-packages','.pytest_cache','.mypy_cache']):return 'dependencies-cache'
 if p.name=='.DS_Store':return 'os-metadata'
 if e in ['.mp4','.mov','.mkv','.webm','.m4v','.mp3','.wav','.m4a','.aac']:return 'media'
 if e in ['.png','.jpg','.jpeg','.webp','.svg','.gif','.heic']:return 'image-frame-asset'
 if e in ['.zip','.gz','.tgz','.tar','.bundle','.bak']:return 'archive-recovery'
 if e in ['.db','.sqlite','.sqlite3']:return 'database'
 if e in ['.py','.sh','.js','.ts','.tsx','.jsx','.html','.css']:return 'code'
 if e in ['.json','.jsonl','.csv','.tsv','.yaml','.yml','.toml','.srt','.vtt']:return 'structured-data'
 if e in ['.md','.txt','.pdf','.docx']:return 'report-document'
 return 'other'
for root in roots:
 for d,ds,fs in os.walk(root,followlinks=False):
  for n in list(ds):
   p=Path(d)/n
   if 'offline-map' in n.lower() or p==OUT:
    excluded.append(str(p));ds.remove(n)
   elif p.is_symlink():
    links.append({'path':str(p),'target':os.readlink(p)});ds.remove(n)
   elif n=='.git':gitmarkers.append(str(p))
  for n in fs:
   p=Path(d)/n
   if 'offline-map' in n.lower():excluded.append(str(p));continue
   try:s=p.lstat()
   except OSError as ex:errors.append([str(p),str(ex)]);continue
   if stat.S_ISLNK(s.st_mode):links.append({'path':str(p),'target':os.readlink(p)});continue
   if not stat.S_ISREG(s.st_mode):continue
   if n=='.git':gitmarkers.append(str(p))
   rows.append({'root':str(root),'path':str(p),'relative':str(p.relative_to(root)),'bytes':s.st_size,'allocated':s.st_blocks*512,'dev':s.st_dev,'inode':s.st_ino,'nlink':s.st_nlink,'mtime_ns':s.st_mtime_ns,'extension':p.suffix.lower() or '[none]','category':cat(p)})
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
repo=roots[0]
tracked=set(subprocess.check_output(['git','ls-files','-z'],cwd=repo,env=env).decode().split('\0'))
inside=[r for r in rows if r['root']==str(repo) and r['category']!='git-internals']
raw='\0'.join(r['relative'] for r in inside)+'\0'
proc=subprocess.run(['git','check-ignore','--stdin','-z'],input=raw.encode(),stdout=subprocess.PIPE,cwd=repo,env=env)
ignored=set(proc.stdout.decode().split('\0'))
for r in rows:
 r['git_state']=('git-internals' if r['category']=='git-internals' else 'tracked' if r['relative'] in tracked else 'ignored' if r['relative'] in ignored else 'untracked') if r['root']==str(repo) else 'external-or-recovery'
 r['classification']=('A' if r['git_state'] in ['tracked','git-internals'] else 'E' if r['category'] in ['dependencies-cache','os-metadata'] else 'F' if r['root']==str(roots[-1]) else 'G')
with gzip.open(OUT/'files.csv.gz','wt') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def summ(rs):
 return {'files':len(rs),'logical_bytes':sum(r['bytes'] for r in rs),'allocated_path_bytes':sum(r['allocated'] for r in rs),'allocated_unique_inode_bytes':sum({(r['dev'],r['inode']):r['allocated'] for r in rs}.values())}
summary={}
for root in roots:
 rs=[r for r in rows if r['root']==str(root)];o=summ(rs)
 for key in ['extension','category','git_state','classification']:
  g=collections.defaultdict(list)
  for r in rs:g[r[key]].append(r)
  o[key]={k:summ(v) for k,v in sorted(g.items(),key=lambda x:-sum(r['bytes'] for r in x[1]))}
 g=collections.defaultdict(list)
 for r in rs:
  parts=Path(r['relative']).parts
  g['/'.join(parts[:2]) if len(parts)>2 else parts[0]].append(r)
 o['subfolders']={k:summ(v) for k,v in sorted(g.items(),key=lambda x:-sum(r['bytes'] for r in x[1]))}
 o['largest_files']=sorted(rs,key=lambda r:-r['bytes'])[:20]
 o['realpath']=os.path.realpath(root);o['symlink']=root.is_symlink()
 summary[str(root)]=o
(OUT/'inventory-summary.json').write_text(json.dumps(summary,indent=2))
(OUT/'scope.json').write_text(json.dumps({'excluded':excluded,'errors':errors,'symlinks':links,'gitmarkers':gitmarkers,'started_and_finished_non_atomic':True,'timestamp':time.time()},indent=2))
for root,o in summary.items():
 print(root, json.dumps({k:o[k] for k in ['files','logical_bytes','allocated_path_bytes','allocated_unique_inode_bytes']}))
 print('TOP',[(k,round(v['logical_bytes']/2**20,1),v['files']) for k,v in list(o['subfolders'].items())[:12]])
print('errors',len(errors),'symlinks',len(links),'gitmarkers',gitmarkers)
