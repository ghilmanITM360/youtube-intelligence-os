import os,stat,json,pathlib,collections,subprocess,time
H=pathlib.Path('/Users/ghilmankhan');D=H/'YIOS-local-audits/2026-10-25-machine-a-phase1b';start=time.time()
roots=[H/'workprojects'/n for n in ['youtube-intelligence-os','video data of what if','yios-recovery-status','yio-cf-editing-forensics-local-evidence','yios-visual-forensics-install-candidate-2026-10-24']]+[H/'YIOS-local-audits',H/'yios-git-recovery',H/'Downloads/videos in mp3',H/'Movies/CapCut/User Data/Projects/com.lveditor.draft/0921']
R={'timestamp':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'roots':[],'exclusions':[],'gitmarkers':[],'errors':[],'global_hardlinks':[]};seen_global={};visited=0
for root in roots:
 row={'path':str(root),'exists':root.exists(),'symlink':root.is_symlink(),'logical_bytes':0,'allocated_path_bytes':0,'unique_inode_allocated_bytes':0,'files':0,'directories':0,'symlinks':[],'top_children':{},'categories':{},'largest':[]};seen=set();child=collections.defaultdict(lambda:[0,0,0]);cats=collections.defaultdict(lambda:[0,0,0]);large=[]
 if not root.exists():R['roots'].append(row);continue
 for parent,dirs,files in os.walk(root,followlinks=False):
  for n in list(dirs):
   p=pathlib.Path(parent)/n
   if root.name=='yios-git-recovery' and parent==str(root) and n.startswith('offline-map'):
    dirs.remove(n);R['exclusions'].append(str(p));continue
   if n=='.git':R['gitmarkers'].append(str(p))
  for n in ['.']+dirs+files:
   if n=='.' and parent!=str(root):continue
   p=pathlib.Path(parent) if n=='.' else pathlib.Path(parent)/n
   try:s=p.lstat()
   except OSError as e:R['errors'].append([str(p),str(e)]);continue
   visited+=1
   if visited>300000:raise RuntimeError('bounded entry limit reached')
   if stat.S_ISLNK(s.st_mode):row['symlinks'].append({'path':str(p),'target':os.readlink(p),'target_exists':p.exists()});continue
   if stat.S_ISDIR(s.st_mode):row['directories']+=1;continue
   if not stat.S_ISREG(s.st_mode):continue
   rel=p.relative_to(root);size=s.st_size;alloc=s.st_blocks*512;key=(s.st_dev,s.st_ino);row['files']+=1;row['logical_bytes']+=size;row['allocated_path_bytes']+=alloc
   if key not in seen:row['unique_inode_allocated_bytes']+=alloc;seen.add(key)
   if key in seen_global:R['global_hardlinks'].append([str(p),seen_global[key],size,alloc])
   else:seen_global[key]=str(p)
   parts=rel.parts;c='/'.join(parts[:2]) if len(parts)>2 else parts[0];child[c][0]+=size;child[c][1]+=alloc;child[c][2]+=1
   ext=p.suffix.lower();text=str(rel)
   if text.startswith('.git/lfs/'):cat='Git LFS'
   elif text.startswith('.git/objects/'):cat='Git objects'
   elif '.git' in parts:cat='Git other'
   elif n=='gray.npy':cat='gray.npy evidence'
   elif any(x in parts for x in ['node_modules','.venv','visual-ct-scan-venv']):cat='dependencies/runtime'
   elif any(x in parts for x in ['__pycache__','.pytest_cache','.cache']):cat='cache candidate'
   elif ext in ['.mp4','.mp3','.wav','.aac','.m4a','.mov','.webm']:cat='media'
   elif ext in ['.jpg','.jpeg','.png','.webp']:cat='frames/images'
   elif ext in ['.bundle','.zip','.tar','.gz','.7z']:cat='archive/recovery'
   elif ext in ['.md','.csv','.json','.jsonl','.txt','.py','.html','.log','.sha256']:cat='research/code/metadata'
   else:cat='other'
   cats[cat][0]+=size;cats[cat][1]+=alloc;cats[cat][2]+=1;large.append([size,alloc,str(p)])
   if n=='.git':R['gitmarkers'].append(str(p))
 row['top_children']=dict(sorted(child.items(),key=lambda x:x[1][0],reverse=True)[:25]);row['categories']=dict(cats);row['largest']=sorted(large,reverse=True)[:12];R['roots'].append(row)
 print(root,'files',row['files'],'logical',row['logical_bytes'],'allocated',row['allocated_path_bytes'],flush=True)
# canonical subroots are nested, not additional space totals
R['canonical_untracked_subroots']=[]
for name in ['finance-short-02-visual-calibration','productions','research/casually-finance-script-intelligence']:
 p=roots[0]/name;files=list(p.rglob('*'));ss=[x.lstat() for x in files if x.is_file() and not x.is_symlink()];R['canonical_untracked_subroots'].append({'path':str(p),'exists':p.exists(),'files':len(ss),'logical_bytes':sum(x.st_size for x in ss),'allocated_bytes':sum(x.st_blocks*512 for x in ss)})
R['df']=subprocess.check_output(['df','-k',str(H)]).decode();R['seconds']=time.time()-start;R['visited']=visited
(D/'STORAGE_READINESS_MEASUREMENTS.json').write_text(json.dumps(R,indent=2));print('finished',visited,'entries',R['seconds'],'seconds','markers',R['gitmarkers'])
