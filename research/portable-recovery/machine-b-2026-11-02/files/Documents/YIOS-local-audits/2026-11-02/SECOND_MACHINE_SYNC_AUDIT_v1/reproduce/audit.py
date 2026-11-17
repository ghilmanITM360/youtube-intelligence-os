#!/usr/bin/env python3
"""Read-only YIOS audit collector. All output is external to the checkout."""
import os, sys, re, json, csv, subprocess, hashlib, shutil, time, socket, platform
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT=Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os')
OUT=Path('/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-02/SECOND_MACHINE_SYNC_AUDIT_v1')
def now(): return datetime.now(timezone.utc).isoformat()
def redact(s):
 s=re.sub(r'(https?://)[^/@\s]+:[^/@\s]+@',r'\1[REDACTED]@',s)
 s=re.sub(r'(?i)((?:token|password|api[_-]?key|authorization)[=: ]+)[^\s,;]+',r'\1[REDACTED]',s)
 s=re.sub(r'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,})\b','[REDACTED]',s)
 return s
def run(args,cwd=ROOT,timeout=120,raw=False):
 try:
  p=subprocess.run(args,cwd=cwd,capture_output=True,timeout=timeout,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0','PYTHONDONTWRITEBYTECODE':'1','GIT_TERMINAL_PROMPT':'0'})
  return {'argv':args,'cwd':str(cwd),'at':now(),'code':p.returncode,'stdout':p.stdout if raw else redact(p.stdout.decode(errors='replace')),'stderr':p.stderr if raw else redact(p.stderr.decode(errors='replace'))}
 except subprocess.TimeoutExpired: return {'argv':args,'cwd':str(cwd),'at':now(),'code':124,'stdout':'','stderr':'TIMEOUT'}
def git(*args,cwd=ROOT):
 # Repository blobs must remain byte-exact for comparisons; sanitize command metadata separately.
 if args and args[0] in ['show','cat-file']:
  return run(['git','-c','core.quotepath=false',*args],cwd,raw=True)['stdout'].decode(errors='replace').strip()
 return run(['git','-c','core.quotepath=false',*args],cwd)['stdout'].strip()
def write(name,obj):
 p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=str)+'\n' if not isinstance(obj,str) else obj)
def read(name):return json.loads((OUT/name).read_text())
def csvout(name,rows,keys=None):
 rows=list(rows);p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
 keys=keys or list(dict.fromkeys(k for row in rows for k in row))
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
  for row in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
def worktrees():
 blocks=git('worktree','list','--porcelain').split('\n\n');out=[]
 for block in blocks:
  d={}
  for line in block.splitlines():
   k,_,v=line.partition(' ');d[k]=v
  if d:out.append(d)
 return out
def refs():
 fmt='%(refname)\t%(objectname)\t%(upstream)\t%(upstream:track)\t%(committerdate:iso-strict)\t%(subject)'
 return [dict(zip(['ref','sha','upstream','track','date','subject'],line.split('\t',5))) for line in git('for-each-ref','--format='+fmt).splitlines()]
def pathlist(args,cwd):
 p=run(['git',*args],cwd,raw=True)
 return [x.decode(errors='surrogateescape') for x in p['stdout'].split(b'\0') if x]
def discover():
 home=Path.home();found=set([str(ROOT)]);searched=[]
 for base in [home/'Documents',home/'Desktop',home/'Downloads',home/'GhilmanProjects',home/'workprojects',home/'Projects',home/'.codex/worktrees',home/'.claude/worktrees']:
  if not base.is_dir():continue
  searched.append(str(base))
  for d,dirs,files in os.walk(base):
   p=Path(d);depth=len(p.relative_to(base).parts)
   if '.git' in dirs or '.git' in files:
    remote=git('config','--get','remote.origin.url',cwd=p)
    if 'youtube-intelligence-os' in remote:found.add(str(p))
    dirs[:]=[];continue
   dirs[:]=[x for x in dirs if x not in ['node_modules','.venv','Library','.git','.cache','data','research'] and (depth<3 or 'yios' in str(p).lower() or 'youtube-intelligence' in str(p).lower())]
   if depth>=6:dirs[:]=[]
 for w in worktrees():found.add(w['worktree'])
 return {'searched_roots':searched,'limit':'directory metadata to depth 4; known YIOS paths to depth 6; repositories stop traversal; no unrelated file content','repositories':sorted(found),'outside_scope':'other volumes and arbitrary unrelated folders not searched'}
def operations(p):
 gd=Path(git('rev-parse','--absolute-git-dir',cwd=p));names=['MERGE_HEAD','REBASE_HEAD','CHERRY_PICK_HEAD','REVERT_HEAD','BISECT_START','rebase-merge','rebase-apply','sequencer','index.lock','HEAD.lock','shallow.lock']
 return {n:str(gd/n) for n in names if (gd/n).exists()}
def checkpoint():
 OUT.mkdir(parents=True,exist_ok=True)
 write('discovery.json',discover())
 write('before/refs.json',refs());write('before/worktrees.json',worktrees())
 write('before/git-config-safe.json',{k:git('config','--get-all',k) for k in ['remote.origin.url','remote.origin.fetch','core.hooksPath','core.sparseCheckout','extensions.worktreeConfig','lfs.storage']})
 snapshots=[]
 for i,path in enumerate(read('discovery.json')['repositories']):
  p=Path(path)
  d={'id':i,'path':path,'head':git('rev-parse','HEAD',cwd=p),'branch':git('symbolic-ref','--short','HEAD',cwd=p),'upstream':git('rev-parse','--abbrev-ref','@{upstream}',cwd=p),'common_dir':str((p/git('rev-parse','--git-common-dir',cwd=p)).resolve()),'status':git('status','--porcelain=v1','--untracked-files=all',cwd=p),'operations':operations(p)}
  for typ,args in [('unstaged',['diff','--binary','--full-index']),('staged',['diff','--cached','--binary','--full-index'])]:
   rr=run(['git',*args],p,raw=True);dest=OUT/f'before/checkout-{i}-{typ}.patch';dest.write_bytes(rr['stdout']);d[typ+'_patch']=str(dest)
  d['untracked']=pathlist(['ls-files','--others','--exclude-standard','-z'],p)
  d['ignored']=pathlist(['ls-files','--others','--ignored','--exclude-standard','-z'],p)
  d['local_only_commits']=git('log','--format=%H %s','HEAD','--not','--remotes',cwd=p).splitlines()
  copied=[]
  for rel in d['untracked']:
   f=p/rel
   if not f.is_file():continue
   record={'path':str(f),'size':f.stat().st_size,'sha256':sha(f)}
   if f.stat().st_size<=20*1024*1024 and not any(x in rel.lower() for x in ['.env','.pem','.key']):
    dst=OUT/f'before/untracked-{i}'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dst);record['copy']=str(dst)
   else:record['copy']='ORIGINAL_PRESERVED_NO_DELETION'
   copied.append(record)
  d['untracked_recovery']=copied;snapshots.append(d)
 write('before/checkouts.json',snapshots)
 stashes=[]
 for line in git('stash','list','--format=%gd%x09%H%x09%gs').splitlines():
  ref,commit,subject=line.split('\t',2);i=len(stashes)
  rr=run(['git','stash','show','--include-untracked','--binary','--full-index','-p',commit],raw=True)
  dest=OUT/f'before/stash-{i}.patch';dest.write_bytes(rr['stdout'])
  stashes.append({'ref':ref,'sha':commit,'subject':subject,'paths':git('stash','show','--include-untracked','--name-status',commit),'patch':str(dest),'parents':git('show','-s','--format=%P',commit)})
 write('before/stashes.json',stashes)
 write('before/reflogs.txt',git('reflog','show','--all','--format=%H %gD %gs'))
 write('before/machine.json',{'host':socket.gethostname(),'user':os.environ.get('USER'),'cwd':str(ROOT),'platform':platform.platform(),'time_utc':now(),'commands':[run(x) for x in [['sw_vers'],['uname','-a'],['df','-k',str(ROOT)],['memory_pressure'],['sysctl','hw.memsize','hw.physicalcpu','hw.logicalcpu'],['sysctl','vm.swapusage']]]})
 proc=run(['ps','-axo','pid,ppid,lstart,command'])
 proc['stdout']='\n'.join(x for x in proc['stdout'].splitlines() if re.search(r'yios|youtube-intelligence|finance|forensic|codex|claude|ffmpeg|pytest|git |python|node',x,re.I))
 write('before/processes.json',proc)
 write('before/cron.json',run(['crontab','-l']))
 lc=run(['launchctl','list']);lc['stdout']='\n'.join(x for x in lc['stdout'].splitlines() if re.search(r'yios|youtube|finance|forensic|codex|claude|cron',x,re.I));write('before/launchctl.json',lc)
 locks=[]
 for d in snapshots:
  gd=Path(d['common_dir'])
  for f in gd.rglob('*.lock'):
   locks.append({'path':str(f),'bytes':f.stat().st_size,'mtime':f.stat().st_mtime})
  for f in Path(d['path']).glob('**/*lock*'):
   if any(x in f.parts for x in ['.git','.venv','node_modules','.cache','.claude']):continue
   if f.is_file() and not f.name.endswith(('.py','.json','.md','.csv','.jsonl')):locks.append({'path':str(f),'bytes':f.stat().st_size})
 write('before/locks.json',locks)
 import tomllib
 autos=[]
 for f in (Path.home()/'.codex/automations').glob('*/automation.toml'):
  try:d=tomllib.loads(f.read_text())
  except Exception:continue
  if any(x in json.dumps(d).lower() for x in ['yios','youtube-intelligence','finance','forensic']):autos.append({'path':str(f),'config':d})
 write('before/automations.json',autos)
 write('before/instructions-and-handoffs.txt','\n\n'.join('FILE '+str(p)+'\n'+p.read_text() for p in [ROOT/'AGENTS.md',ROOT/'research/finance-economics-intelligence/FINANCE_WRITER_OWNERSHIP.md',ROOT/'research/finance-economics-intelligence/RESUME_HERE.md'] if p.exists()))
 manifest=[{'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in (OUT/'before').rglob('*') if p.is_file()]
 write('RECOVERY_MANIFEST.json',manifest)
 assert all(sha(OUT/r['path'])==r['sha256'] for r in manifest)
 write('RECOVERY_VERIFIED.json',{'at':now(),'files':len(manifest),'verified':True,'strategy':'Exact binary patches; all refs, reflogs, stash patch and identities; unique small untracked copies. No commit rewrite or branch deletion authorized; refs/objects retained in original Git common directory. Large evidence originals preserved in place.'})
 print(json.dumps({'out':str(OUT),'checkouts':[(d['path'],d['head'],len(d['untracked']),len(d['ignored']),d['status']) for d in snapshots],'stashes':len(stashes),'locks':len(locks),'automations':len(autos),'recovery_files':len(manifest)},indent=2))

def fetch():
 auth=run(['gh','api','user','--jq','.login']);write('remote/auth.json',auth)
 repo=run(['gh','repo','view','ghilmanITM360/youtube-intelligence-os','--json','nameWithOwner,isPrivate,defaultBranchRef,url']);write('remote/repository.json',repo)
 if auth['code'] or repo['code']:
  write('remote/freshness.json',{'status':'UNKNOWN','reason':'Authenticated GitHub read failed','at':now()});print('Authenticated repository read failed; remote freshness UNKNOWN');return
 info=json.loads(repo['stdout']);assert info['nameWithOwner'].lower()=='ghilmanitm360/youtube-intelligence-os'
 rr=run(['git','fetch','origin','--no-prune','--tags','--no-recurse-submodules','--no-auto-gc'],timeout=300);write('remote/fetch.json',rr)
 write('remote/refs-after-fetch.json',refs())
 branches=run(['gh','api','--paginate','--slurp','repos/ghilmanITM360/youtube-intelligence-os/branches?per_page=100']);write('remote/github-branches-response.json',branches)
 tags=run(['git','ls-remote','--tags','origin']);write('remote/live-tags.json',tags)
 prs=run(['gh','api','--paginate','--slurp','repos/ghilmanITM360/youtube-intelligence-os/pulls?state=all&per_page=100']);write('remote/github-pr-response.json',prs)
 runs=run(['gh','run','list','--repo','ghilmanITM360/youtube-intelligence-os','--limit','20','--json','databaseId,headSha,headBranch,status,conclusion,createdAt,url']);write('remote/actions.json',runs)
 status='VERIFIED' if rr['code']==0 and branches['code']==0 else 'UNKNOWN'
 write('remote/freshness.json',{'status':status,'observed_at':now(),'default_branch':info['defaultBranchRef']['name'],'fetch_code':rr['code'],'authenticated_login':auth['stdout'].strip(),'remote_heads':{x['ref']:x['sha'] for x in refs() if x['ref'].startswith('refs/remotes/origin/')}})
 print(json.dumps(read('remote/freshness.json'),indent=2))

def matrix():
 fresh=read('remote/freshness.json');default='refs/remotes/origin/'+fresh['default_branch']
 allrefs=refs();wts=worktrees();live={}
 br=read('remote/github-branches-response.json')
 if br['code']==0:live={x['name']:x['commit']['sha'] for page in json.loads(br['stdout']) for x in page}
 prr=read('remote/github-pr-response.json');prs=[]
 if prr['code']==0:prs=[x for page in json.loads(prr['stdout']) for x in page]
 write('remote/pr-summary.json',[{'number':p['number'],'state':p['state'],'draft':p['draft'],'merged_at':p['merged_at'],'head':p['head']['ref'],'head_sha':p['head']['sha'],'base':p['base']['ref'],'url':p['html_url'],'title':p['title']} for p in prs])
 rows=[];cache={}
 for ref in allrefs:
  full=ref['ref']
  if not (full.startswith('refs/heads/') or full.startswith('refs/remotes/origin/')) or full.endswith('/HEAD'):continue
  name=full.removeprefix('refs/heads/').removeprefix('refs/remotes/origin/')
  sh=ref['sha'];local=full.startswith('refs/heads/')
  if sh not in cache:
   slug=sh[:12];base=git('merge-base',default,full)
   counts=git('rev-list','--left-right','--count',default+'...'+full).split()
   cherry=git('rev-list','--left-right','--cherry-pick','--count',default+'...'+full).split()
   changes=[]
   for ln in git('diff','--numstat',base,full).splitlines():
    vals=ln.split('\t',2)
    if len(vals)==3:changes.append({'additions':vals[0],'deletions':vals[1],'path':vals[2]})
   tree=[]
   for ln in git('ls-tree','-rl',full).splitlines():
    meta,_,path=ln.partition('\t');v=meta.split()
    if len(v)==4:tree.append({'path':path,'mode':v[0],'type':v[1],'blob':v[2],'git_blob_bytes':int(v[3]) if v[3].isdigit() else 0})
   csvout('branches/trees/'+slug+'.csv',tree)
   csvout('branches/diffs/'+slug+'.csv',changes,['additions','deletions','path'])
   commits=git('log','--format=%H%x09%aI%x09%s',default+'..'+full).splitlines();write('branches/commits/'+slug+'.txt','\n'.join(commits)+'\n')
   write('branches/cherry/'+slug+'.txt',git('cherry','-v',default,full))
   mainblobs=set(git('ls-tree','-r',default).splitlines()) if not cache else cache.get('_main_lines',set())
   if '_main_lines' not in cache:cache['_main_lines']=mainblobs
   mainpaths={ln.partition('\t')[2]:ln.partition('\t')[0].split()[-1] for ln in mainblobs}
   unique=[t for t in tree if mainpaths.get(t['path'])!=t['blob']]
   docs=[x for x in unique if x['path'].endswith(('.md','.json')) and x['git_blob_bytes']<200000 and re.search(r'README|HANDOFF|RESUME|STATUS|CHECKPOINT|ACCEPT|OWNERSHIP|MANIFEST|SUMMARY|VALIDATION|DISCOVERY',x['path'],re.I)]
   docs=sorted(docs,key=lambda x:(0 if re.search('RESUME|OWNERSHIP|HANDOFF|CHECKPOINT|ACCEPT|STATUS',x['path'],re.I) else 1, len(x['path'])))[:16]
   excerpts=[]
   for d in docs:
    excerpts.append({'path':d['path'],'blob':d['blob'],'text':git('show',full+':'+d['path'])[:14000]})
   write('branches/evidence/'+slug+'.json',excerpts)
   jsonl=[x for x in tree if x['path'].endswith('.jsonl') and x['git_blob_bytes']<40_000_000]
   datasets=[]
   for d in jsonl:
    s=git('show',full+':'+d['path']);ids=[];statuses=Counter();bad=0
    for line in s.splitlines():
     if not line.strip():continue
     try:
      obj=json.loads(line)
      if isinstance(obj,dict):
       vid=obj.get('video_id') or obj.get('Video_ID') or obj.get('id')
       if vid:ids.append(str(vid))
       status=obj.get('status') or obj.get('audit_status') or obj.get('overall_status')
       if isinstance(status,str):statuses[status]+=1
     except Exception:bad+=1
    datasets.append({'path':d['path'],'records':len(s.splitlines()),'unique_ids':len(set(ids)),'duplicate_ids':len(ids)-len(set(ids)),'statuses':dict(statuses),'invalid_lines':bad})
   write('branches/datasets/'+slug+'.json',datasets)
   cache[sh]={'merge_base':base,'behind_default':int(counts[0]),'ahead_default':int(counts[1]),'patch_unique_behind_default':int(cherry[0]),'patch_unique_ahead_default':int(cherry[1]),'changed_files_since_merge_base':len(changes),'additions_since_merge_base':sum(int(x['additions']) for x in changes if x['additions'].isdigit()),'deletions_since_merge_base':sum(int(x['deletions']) for x in changes if x['deletions'].isdigit()),'tree_file_count':len(tree),'tree_git_blob_bytes':sum(x['git_blob_bytes'] for x in tree),'different_paths_vs_default':len(unique),'different_top_areas':Counter('/'.join(x['path'].split('/')[:2]) for x in unique).most_common(8),'deliverable_examples':[x['path'] for x in unique if not x['path'].startswith(('data/raw/','data/extracted/'))][:15],'doc_evidence':'branches/evidence/'+slug+'.json','tree_index':'branches/trees/'+slug+'.csv','commit_index':'branches/commits/'+slug+'.txt','datasets':datasets}
  up=ref['upstream'];upcounts=git('rev-list','--left-right','--count',full+'...'+up).split() if up else []
  localonly=git('log','--format=%H %s',full,'--not','--remotes').splitlines() if local else []
  same=next((w['worktree'] for w in wts if w.get('branch')==full),'')
  associated=[{'number':p['number'],'state':p['state'],'draft':p['draft'],'merged':bool(p['merged_at']),'base':p['base']['ref'],'url':p['html_url']} for p in prs if p['head']['ref']==name]
  d={**ref,'name':name,'kind':'local' if local else 'remote','github_sha':live.get(name),'github_head_matches':live.get(name)==sh if name in live else None,'ahead_upstream':int(upcounts[0]) if upcounts else None,'behind_upstream':int(upcounts[1]) if upcounts else None,'local_only_commits':localonly,'worktree':same,'prs':associated,**cache[sh]}
  d['contained_in_default']=d['ahead_default']==0
  d['integration_assessment']='CONTAINED' if d['contained_in_default'] else ('PATCH_EQUIVALENT_CANDIDATE' if d['patch_unique_ahead_default']==0 else 'DISTINCT_HISTORY_REVIEW_REQUIRED')
  d['reuse_assessment']='PRESERVE_ACTIVE_ASSIGNMENT' if same else ('CONSOLIDATION_CANDIDATE_REVIEW_IGNORED_DEPENDENCIES' if d['contained_in_default'] else 'KEEP_DISTINCT_ROLE_NO_AUTOMATIC_INTEGRATION')
  rows.append(d)
 write('branch_matrix.json',rows);csvout('branch_matrix.csv',rows)
 write('remote/branch-coverage.json',{'api_heads':len(live),'matrix_rows':len(rows),'local_branches':sum(x['kind']=='local' for x in rows),'remote_rows':sum(x['kind']=='remote' for x in rows),'missing_api_branches':[n for n in live if not any(r['kind']=='remote' and r['name']==n and r['sha']==live[n] for r in rows)],'stale_remote_tracking_refs':[r['name'] for r in rows if r['kind']=='remote' and r['name'] not in live]})
 print(json.dumps({'coverage':read('remote/branch-coverage.json'),'local_not_equal_upstream':[(r['name'],r['ahead_upstream'],r['behind_upstream']) for r in rows if r['kind']=='local' and (r['ahead_upstream'] or r['behind_upstream'])],'not_in_default':sum(not r['contained_in_default'] for r in rows if r['kind']=='remote')},indent=2))

if __name__=='__main__':
 assert redact('https://user:pass@example.org/a')=='https://[REDACTED]@example.org/a'
 globals()[sys.argv[1]]()
