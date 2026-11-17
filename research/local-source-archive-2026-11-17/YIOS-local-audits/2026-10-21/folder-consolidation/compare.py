import pathlib,os,json,hashlib,collections,subprocess
out=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/folder-consolidation');base=pathlib.Path('/Users/ghilmankhan/workprojects');repo=base/'youtube-intelligence-os';rows=json.loads((out/'inventory.json').read_text());targets=collections.defaultdict(list)
for r in rows:
 if 'sha256'in r:targets[r['size']].append(r)
wanted={r['sha256']for r in rows if 'sha256'in r}; matches=collections.defaultdict(list); canonicalfiles=0
for d,dirs,files in os.walk(repo):
 dirs[:]=[x for x in dirs if x not in ['.git','.venv','node_modules','__pycache__','.pytest_cache']]
 for f in files:
  p=pathlib.Path(d)/f
  if p.is_symlink()or not p.is_file()or p.stat().st_size not in targets:continue
  h=hashlib.sha256(p.read_bytes()).hexdigest();canonicalfiles+=1
  if h in wanted:matches[h].append(str(p))
index={}
for r in rows:
 if 'sha256'in r:index.setdefault(r['sha256'],[]).append(r['folder']+'/'+r['path'])
result=[]
for r in rows:
 h=r.get('sha256');r=dict(r);r['canonical_matches']=matches.get(h,[]);r['sibling_matches']=[x for x in index.get(h,[])if x!=r['folder']+'/'+r['path']];result.append(r)
(out/'comparisons.json').write_text(json.dumps(result,indent=2))
for name in sorted(set(r['folder']for r in result)):
 rr=[r for r in result if r['folder']==name];print(name,'canonical identical',sum(bool(r['canonical_matches'])for r in rr),'no canonical identical',sum(not r['canonical_matches']for r in rr),'sibling identical',sum(bool(r['sibling_matches'])for r in rr))
print('canonical hash candidates',canonicalfiles)
# Snapshot refs and working statuses, no branch mutation.
state={}
for k,args in {'refs':['for-each-ref','--format=%(refname) %(objectname)'],'stash':['stash','list','--format=%H'],'main_status':['status','--porcelain=v1','--untracked-files=all'],'ignored':['ls-files','--others','--ignored','--exclude-standard'],'worktrees':['worktree','list','--porcelain']}.items():state[k]=subprocess.check_output(['git','-C',str(repo),*args],text=True)
state['forensic_status']=subprocess.check_output(['git','-C',str(base/'yio-cf-editing-forensics'),'status','--porcelain=v1','--untracked-files=all'],text=True)
(out/'git-before.json').write_text(json.dumps(state,indent=2))
