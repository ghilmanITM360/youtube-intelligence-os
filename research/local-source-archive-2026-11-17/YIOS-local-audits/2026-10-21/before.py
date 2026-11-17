import pathlib,json,subprocess,shutil
A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21');R=pathlib.Path.cwd()
remote={l.split()[1]:l.split()[0] for l in (A/'github-before.txt').read_text().splitlines()}
rows=['# Machine A pre-fetch inventory','', '| Branch / worktree | Local SHA | GitHub SHA | Ahead/behind (cached) | Dirty/unique data | Owner | Safe update |','|---|---|---|---|---|---|---|']
for b in json.loads((A/'branches-before.json').read_text()):
 u=b['upstream']; r=remote.get('refs/heads/'+u.removeprefix('origin/'),'MISSING') if u else 'NO_UPSTREAM'
 ab=subprocess.run(['git','rev-list','--left-right','--count',b['branch']+'...'+u],capture_output=True,text=True).stdout.strip() if u else 'N/A'
 finance=b['branch']=='research/finance-economics-intelligence'; cf=b['branch']=='research/casually-finance-editing-forensics'
 rows.append('| '+' | '.join([b['branch'],b['sha'],r,ab,'11 modified; 302 untracked; ignored inventory' if finance else ('clean; ignored .DS_Store' if cf else 'no checkout'), 'Machine B Finance' if finance else ('Claude 873b9a27-ba03-4183-aa61-f82d01f65998' if cf else 'no local active checkout; cross-Mac ownership not yet confirmed'), 'BLOCKED_DIRTY' if finance else ('PROTECTED_ACTIVE_OWNER' if cf else 'pending fetch/ancestry verification')])+' |')
(A/'INITIAL_INVENTORY.md').write_text('\n'.join(rows)+'\n')
# External exact backups for all modified files plus all untracked research/production evidence; no dependencies.
for k in [0,1]:
 d=json.loads((A/f'worktree-{k}-files.json').read_text())
 root=R if k==0 else pathlib.Path('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics')
 for cat in ['modified','untracked']:
  for row in d[cat]:
   src=pathlib.Path(row['path']); dst=A/'preserved-files'/f'worktree-{k}'/src.relative_to(root)
   dst.parent.mkdir(parents=True,exist_ok=True)
   if not dst.exists():shutil.copy2(src,dst,follow_symlinks=False)
# refs/reflogs/stash metadata copied, retain original object database unchanged.
shutil.copytree(R/'.git/logs',A/'git-logs',dirs_exist_ok=True)
print((A/'INITIAL_INVENTORY.md').read_text())
