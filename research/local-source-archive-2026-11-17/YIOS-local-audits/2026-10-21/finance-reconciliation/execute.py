import pathlib,json,hashlib,subprocess,os,stat
R=pathlib.Path.cwd();A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');D=A/'finance-reconciliation'
def g(*a):return subprocess.check_output(['git',*a])
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
gate=json.loads((D/'gate.json').read_text());rows=json.loads((D/'collision-map.json').read_text());before=json.loads((D/'before-paths.json').read_text());old=gate['old'];remote=gate['remote']
assert g('rev-parse','HEAD').decode().strip()==old
assert g('rev-parse','@{u}').decode().strip()==remote
assert not g('diff','--cached','--name-only')
assert not list((R/'.git').rglob('*.lock'))
assert g('diff','--binary')==(A/'worktree-0-diff.patch').read_bytes()
for x in rows:
 p=R/x['path'];q=pathlib.Path(x['archive']);assert h(p)==h(q)==x['local_sha256'];assert p.stat().st_nlink==1 and q.stat().st_nlink==1
# Capture permissions/mtime of all 31 in manifest before any operation.
(D/'restoration-manifest.json').write_text(json.dumps(dict(root=str(R),historical_head=old,target_head=remote,files=rows),indent=2))
log=[]
for x in rows:
 if x['kind']!='untracked':continue
 p=R/x['path'];q=D/'relocated-untracked'/x['path'];q.parent.mkdir(parents=True,exist_ok=True);assert not q.exists();assert h(p)==x['local_sha256']
 os.rename(p,q);assert h(q)==x['local_sha256'];assert stat.S_IMODE(q.stat().st_mode)==x['mode'];assert q.stat().st_mtime_ns==x['mtime_ns'];assert not p.exists()
 x['relocated_path']=str(q);log.append(dict(path=x['path'],action='RELOCATED',sha256=h(q)));(D/'operations.json').write_text(json.dumps(log,indent=2))
t=[x['path'] for x in rows if x['kind']=='tracked']
assert not g('diff','--cached','--name-only');assert g('rev-parse','HEAD').decode().strip()==old
subprocess.run(['git','restore','--source='+old,'--worktree','--',*t],check=True)
assert not g('diff','--name-only');assert not g('diff','--cached','--name-only')
remaining=set(g('ls-files','--others','--exclude-standard','-z').decode().strip('\0').split('\0'))
assert remaining==set(before['untracked'])-{x['path'] for x in rows if x['kind']=='untracked'}
tree=set(g('ls-tree','-r','--name-only',remote).decode().splitlines());assert not remaining&tree
assert g('stash','list','--format=%gd %H %gs')==(A/'stashes-before.txt').read_bytes()
assert g('rev-parse','backup/decode-15cbe9f-original').decode().strip()=='15cbe9f0112596c1e07c1c1504302cce77bfd97a'
# Require server head still equals this verified target before ff-only.
live=g('ls-remote','origin','refs/heads/research/finance-economics-intelligence').decode().split()[0];assert live==remote
result=subprocess.run(['git','-c','gc.auto=0','merge','--ff-only','--no-autostash','origin/research/finance-economics-intelligence'],capture_output=True);(D/'fast-forward.log').write_bytes(result.stdout+result.stderr);assert result.returncode==0,result.stderr
assert g('rev-parse','HEAD').decode().strip()==remote
for x in rows:assert h(pathlib.Path(x['archive']))==x['local_sha256']
(D/'restoration-manifest.json').write_text(json.dumps(dict(root=str(R),historical_head=old,target_head=remote,files=rows),indent=2))
log.extend(dict(path=p,action='RESTORED_OLD_HEAD_THEN_FAST_FORWARDED') for p in t);(D/'operations.json').write_text(json.dumps(log,indent=2))
print('FAST_FORWARD_VERIFIED',old,remote,'tracked',len(t),'relocated',20)
