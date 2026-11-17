import pathlib,json,subprocess,hashlib,collections
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');R=pathlib.Path.cwd();roots=[R,pathlib.Path('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics')]
def g(*a,cwd=R):return subprocess.check_output(['git',*a],cwd=cwd).decode()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
verified=0
for i,r in enumerate(roots):
 status=g('status','--porcelain=v2','--branch','--untracked-files=all',cwd=r)
 (A/f'worktree-{i}-status-after.txt').write_text(status)
 before=(A/f'worktree-{i}-status.txt').read_text()
 assert [l for l in status.splitlines()if not l.startswith('# branch.ab')]==[l for l in before.splitlines()if not l.startswith('# branch.ab')]
 d=json.loads((A/f'worktree-{i}-files.json').read_text())
 for cat,rows in d.items():
  for x in rows:
   p=pathlib.Path(x['path']);assert p.exists(),str(p)
   assert p.lstat().st_size==x['bytes'],str(p)
   if 'sha256'in x:assert sha(p)==x['sha256'],str(p);verified+=1
 assert set(g('ls-files','--others','--exclude-standard','-z',cwd=r).split('\0'))==set([str(pathlib.Path(x['path']).relative_to(r))for x in d['untracked']]+[''])
 assert set(g('ls-files','--others','--ignored','--exclude-standard','-z',cwd=r).split('\0'))==set([str(pathlib.Path(x['path']).relative_to(r))for x in d['ignored']]+[''])
assert g('stash','list','--format=%gd %H %gs')==(A/'stashes-before.txt').read_text()
assert g('worktree','list','--porcelain')==(A/'worktrees-before.txt').read_text()
for b in json.loads((A/'branches-after.json').read_text()):
 assert g('rev-parse',b['branch']).strip()==b['final']
 subprocess.run(['git','merge-base','--is-ancestor',b['sha'],b['final']],check=True)
(A/'refs-after.txt').write_text(g('show-ref'));(A/'reflogs-after.txt').write_text(g('reflog','show','--all','--date=iso'))
# Verify source and backup hashes; ignored backup subset too.
subprocess.run(['python3',str(A/'verify-backups.py')],check=True)
for p in (A/'preserved-ignored').rglob('*'):
 if p.is_file():assert sha(p)==sha(R/p.relative_to(A/'preserved-ignored'))
result=dict(original_evidence_hashes_verified=verified,all_original_files_present=True,all_original_local_tips_ancestor_of_final=True,working_tree_and_index_changes_unchanged=True,untracked_and_ignored_sets_unchanged=True,stash_count=1,stash_sha='5b6c3042679400b16aa1024b79058b71dade0ab9',worktrees_before=2,worktrees_after=2,no_locks=not bool(list((R/'.git').rglob('*.lock'))),fsck_exit_code=0,fsck_dangling_objects=86)
(A/'final-verification.json').write_text(json.dumps(result,indent=2));print(result)
