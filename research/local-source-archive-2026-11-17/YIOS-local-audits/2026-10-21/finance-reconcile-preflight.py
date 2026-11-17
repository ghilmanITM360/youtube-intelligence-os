import pathlib,json,hashlib,subprocess,os,difflib,stat
R=pathlib.Path.cwd(); A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21'); D=A/'finance-reconciliation';D.mkdir(mode=0o700,exist_ok=True)
def g(*a):return subprocess.check_output(['git',*a])
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,d): (D/n).write_text(json.dumps(d,indent=2))
assert str(R)=='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
old=g('rev-parse','HEAD').decode().strip();assert old=='aea737320ad127e9783ab02912694c38c87b7c49'
assert g('branch','--show-current').decode().strip()=='research/finance-economics-intelligence'
assert not g('diff','--cached','--name-only')
m=json.loads((A/'AUDIT_SHA256_MANIFEST.json').read_text())
for n in ['INITIAL_INVENTORY.md','YIOS_MACHINE_A_AUDIT_AND_SYNC_2026-10-21.md','finance-conflicts.json','final-verification.json','worktree-0-files.json','worktree-0-diff.patch','worktree-0-staged.patch','stashes-before.txt','recovery-preservation.json']:
 assert sha((A/n).read_bytes())==m[n]['sha256'],n
assert g('diff','--binary')==(A/'worktree-0-diff.patch').read_bytes()
assert g('stash','list','--format=%gd %H %gs')==(A/'stashes-before.txt').read_bytes()
assert g('worktree','list','--porcelain')==(A/'worktrees-before.txt').read_bytes()
assert not list((R/'.git').rglob('*.lock'))
d=json.loads((A/'worktree-0-files.json').read_text());sets={}
for cat,args in [('modified',['diff','--name-only','-z']),('untracked',['ls-files','--others','--exclude-standard','-z']),('ignored',['ls-files','--others','--ignored','--exclude-standard','-z'])]:
 live=set(g(*args).decode().strip('\0').split('\0'));expected={str(pathlib.Path(x['path']).relative_to(R)) for x in d[cat]};assert live==expected,(cat,live^expected);sets[cat]=sorted(live)
 for x in d[cat]:
  p=pathlib.Path(x['path']);assert p.lstat().st_size==x['bytes'],str(p)
  if 'sha256' in x:assert sha(p.read_bytes())==x['sha256'],str(p)
save('before-paths.json',sets)
subprocess.run(['git','-c','fetch.prune=false','-c','gc.auto=0','fetch','--no-prune','--no-auto-maintenance','origin','refs/heads/research/finance-economics-intelligence:refs/remotes/origin/research/finance-economics-intelligence'],check=True)
remote=g('rev-parse','@{u}').decode().strip();subprocess.run(['git','merge-base','--is-ancestor',old,remote],check=True)
pr=json.loads(subprocess.check_output(['gh','pr','view','36','--repo','ghilmanITM360/youtube-intelligence-os','--json','headRefOid,headRefName,state,isDraft,url,updatedAt']));assert pr['headRefOid']==remote;save('pr-before.json',pr)
tree=set(g('ls-tree','-r','--name-only',remote).decode().splitlines())
c=json.loads((A/'finance-conflicts.json').read_text());t=c['modified_overlap_with_upstream'];u=c['untracked_paths_now_tracked_upstream'];assert not set(t)&set(u)
assert set(u)==set(sets['untracked'])&tree
# Git may overwrite ignored paths: require none newly materialized by target.
oldtree=set(g('ls-tree','-r','--name-only',old).decode().splitlines());assert not (set(sets['ignored'])&(tree-oldtree))
rows=[]
for p in t+u:
 b=(R/p).read_bytes();q=A/'preserved-files/worktree-0'/p;assert q.resolve()!= (R/p).resolve();assert not q.is_symlink();assert sha(q.read_bytes())==sha(b)
 assert sha(q.read_bytes())==m[str(q.relative_to(A))]['sha256']
 proc=subprocess.run(['git','show',f'{remote}:{p}'],capture_output=True);rb=proc.stdout if proc.returncode==0 else None
 proc=subprocess.run(['git','show',f'{old}:{p}'],capture_output=True);hb=proc.stdout if proc.returncode==0 else None
 same=rb==b
 row=dict(path=p,kind='tracked' if p in t else 'untracked',local_sha256=sha(b),local_bytes=len(b),archive=str(q),archive_sha256=sha(q.read_bytes()),head_sha256=sha(hb) if hb is not None else None,head_bytes=len(hb) if hb is not None else None,remote_sha256=sha(rb) if rb is not None else None,remote_bytes=len(rb) if rb is not None else None,classification='IDENTICAL_TO_REMOTE' if same else 'MIXED_OR_CONFLICTING_CONTENT',mode=stat.S_IMODE((R/p).stat().st_mode),mtime_ns=(R/p).stat().st_mtime_ns)
 if not same and p.endswith(('.csv','.json','.jsonl')) and rb:
  aa=b.decode().splitlines();bb=rb.decode().splitlines();diff=list(difflib.unified_diff(aa,bb,fromfile='local',tofile='remote',n=1));(D/(pathlib.Path(p).name+'.diff')).write_text('\n'.join(diff));row['difference']=dict(local_lines=len(aa),remote_lines=len(bb),diff_lines=len(diff))
 else:row['difference']='byte-identical' if same else 'binary differs or deleted upstream; retain historical bytes externally'
 rows.append(row)
save('collision-map.json',rows);save('gate.json',dict(old=old,remote=remote,tracked=len(t),untracked=len(u),overlap=0,all_affected_backups_verified=True,patch_exact_match=True,original_sets_unchanged=True,free_bytes=__import__('shutil').disk_usage(R).free))
print(json.dumps(dict(old=old,remote=remote,counts={k:len(v) for k,v in sets.items()},classifications=__import__('collections').Counter(x['classification'] for x in rows),gate='PASS'),indent=2))
