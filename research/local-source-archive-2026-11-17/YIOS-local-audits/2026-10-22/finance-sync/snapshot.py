import subprocess,json,hashlib,os,sys
from pathlib import Path
root=Path.cwd(); out=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-22/finance-sync')
def git(*a): return subprocess.check_output(['git',*a]).decode().strip()
def paths(*a): return subprocess.check_output(['git','ls-files','-z',*a]).decode().split('\0')[:-1]
def record(p):
 f=root/p
 if f.is_symlink(): return {'link':os.readlink(f)}
 return {'size':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
u=paths('--others','--exclude-standard'); i=paths('--others','--ignored','--exclude-standard')
d={'head':git('rev-parse','HEAD'),'branch':git('branch','--show-current'),'tracked':git('status','--porcelain','--untracked-files=no'),'refs':git('for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/stash'),'stash':git('stash','list','--format=%H %gd %s'),'worktrees':git('worktree','list','--porcelain'),'untracked':{p:record(p) for p in u},'ignored':{p:record(p) for p in i},'local_only':git('rev-list','--all','--not','--remotes')}
(out/(sys.argv[1]+'.json')).write_text(json.dumps(d,indent=2)); print({k:d[k] for k in ['head','branch','tracked','stash','worktrees']}); print('untracked',len(u),'ignored',len(i))
