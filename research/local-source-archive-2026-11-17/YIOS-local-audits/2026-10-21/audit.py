import subprocess,json,pathlib,os,hashlib,time
R=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os'); A=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21')
def g(*args,cwd=R):
 p=subprocess.run(['git',*args],cwd=cwd,capture_output=True); return p.stdout.decode(errors='replace')
def save(n,s): (A/n).write_text(s)
save('refs-before.txt',g('show-ref')); save('reflogs-before.txt',g('reflog','show','--all','--date=iso'));save('stashes-before.txt',g('stash','list','--format=%gd %H %gs'));save('worktrees-before.txt',g('worktree','list','--porcelain'));save('config.txt',g('config','--local','--list'))
branches=[]
for l in g('for-each-ref','--format=%(refname:short)\t%(objectname)\t%(upstream:short)','refs/heads').splitlines():
 b,s,u=l.split('\t'); branches.append(dict(branch=b,sha=s,upstream=u))
save('branches-before.json',json.dumps(branches,indent=2))
for i,p in enumerate([R,pathlib.Path('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics')]):
 save(f'worktree-{i}-status.txt',g('status','--porcelain=v2','--branch','--untracked-files=all',cwd=p)); save(f'worktree-{i}-diff.patch',g('diff','--binary',cwd=p));save(f'worktree-{i}-staged.patch',g('diff','--cached','--binary',cwd=p))
 cats={}
 for label,args in [('modified',('ls-files','-m','-z')),('untracked',('ls-files','--others','--exclude-standard','-z')),('ignored',('ls-files','--others','--ignored','--exclude-standard','-z'))]:
  rows=[]
  for f in g(*args,cwd=p).split('\0'):
   if not f: continue
   q=p/f
   try:
    st=q.lstat(); row=dict(path=str(q),bytes=st.st_size,mtime_ns=st.st_mtime_ns,symlink=q.is_symlink())
    # Hash evidence; avoid dependency/cache trees, retaining inventory for all.
    if q.is_file() and not any(x in q.parts for x in ['node_modules','.venv','venv','__pycache__','.cache']):
     h=hashlib.sha256()
     with q.open('rb') as fh:
      for c in iter(lambda:fh.read(1024*1024),b''):h.update(c)
     row['sha256']=h.hexdigest()
    rows.append(row)
   except OSError as e: rows.append(dict(path=str(q),error=str(e)))
  cats[label]=rows
 save(f'worktree-{i}-files.json',json.dumps(cats,indent=2))
 print(str(p),{k:{'files':len(v),'bytes':sum(x.get('bytes',0) for x in v),'hashed':sum('sha256'in x for x in v)} for k,v in cats.items()})
locks=list((R/'.git').rglob('*.lock'));save('locks.txt','\n'.join(map(str,locks)))
print(json.dumps(branches,indent=2))
