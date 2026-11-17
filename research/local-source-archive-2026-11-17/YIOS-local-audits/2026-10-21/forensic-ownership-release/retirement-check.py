import pathlib as P,subprocess as S,json,hashlib,os,shutil,socket
base=P.Path('/Users/ghilmankhan/workprojects');repo=base/'youtube-intelligence-os';wt=base/'yio-cf-editing-forensics';out=P.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/forensic-ownership-release');sha='090f84b3292a3b6c6e94653a6ef1867726e4ebdd';branch='research/casually-finance-editing-forensics'
def git(*a,cwd=repo):return S.check_output(['git','-C',str(cwd),*a],text=True).strip()
def h(p):
 x=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(4194304),b''):x.update(b)
 return x.hexdigest()
def state():return {k:git(*a) for k,a in {'refs':['for-each-ref','--format=%(refname) %(objectname)'],'stash':['stash','list','--format=%H'],'status':['status','--porcelain=v1','--untracked-files=all'],'ignored':['ls-files','--others','--ignored','--exclude-standard'],'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'ab':['rev-list','--left-right','--count','HEAD...@{upstream}']}.items()}
assert socket.gethostname()=='Ghilmans-Laptop.local';assert git('rev-parse','--show-toplevel')==str(repo)
assert 'FORENSIC_WORKTREE_RELEASED_FOR_RETIREMENT' in (out/'FORENSIC_CONTINUATION_AND_RELEASE_2026-10-21.md').read_text()
assert git('worktree','list','--porcelain').count('worktree ')==2
assert git('branch','--show-current',cwd=wt)==branch
assert git('rev-parse','HEAD',cwd=wt)==sha==git('rev-parse',branch)
assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==sha
assert git('status','--porcelain=v1','--untracked-files=all',cwd=wt)==''
assert git('ls-files','--others','--ignored','--exclude-standard',cwd=wt)=='.DS_Store'
assert h(wt/'.DS_Store')==h(out/'worktree.DS_Store')
rows=json.loads((out.parent/'folder-consolidation/inventory.json').read_text());assert h(out.parent/'folder-consolidation/inventory.json')=='5d3640b88040f3af022ceae4ce4e58a1dcbbaa17e2ca6f104f4614ee7f8a82e1'
# All retiring checkout bytes checked; external media metadata plus bounded deterministic hash sample.
checks={};ev=[]
for folder in [wt.name,'yio-cf-editing-forensics-local-evidence']:
 rr=[r for r in rows if r['folder']==folder];root=base/folder;actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() or p.is_symlink()};assert actual=={r['path']for r in rr}
 for r in rr:
  p=root/r['path'];st=p.lstat();assert (st.st_size,st.st_mtime_ns,st.st_mode)==(r['size'],r['mtime_ns'],r['mode']),str(p)
  if folder==wt.name:assert h(p)==r['sha256'],str(p)
 if folder!=wt.name:
  ev=sorted(rr,key=lambda r:r['path'])[::19]
  for r in ev:assert h(root/r['path'])==r['sha256']
 checks[folder]={'files':len(rr),'bytes':sum(r['size']for r in rr)}
common=P.Path(git('rev-parse','--git-common-dir'));common=common if common.is_absolute() else repo/common
assert not list(common.rglob('*.lock'))
ls=S.run(['lsof','-n','-P','+D',str(wt)],capture_output=True,text=True);assert ls.returncode==1 and not ls.stdout and not ls.stderr,(ls.stdout,ls.stderr)
ps=S.check_output(['ps','-axo','pid=,command='],text=True);(out/'retirement-processes.txt').write_text(ps)
assert not any(('claude ' in l.lower() or 'ffmpeg ' in l.lower()) and ('native-host' not in l) for l in ps.splitlines()),'Inspect possible active worker'
s=state();assert s['head']=='d41a5774f1381a21022b70f02d206303195be3a7';assert s['branch']=='research/finance-economics-intelligence';assert s['ab']=='0\t0'
book=repo/'research/finance-economics-intelligence/FINANCE_1612_COMBINED_INTELLIGENCE.xlsx';assert h(book)=='b87869124ec31a59b8d9e640ed370f72f303cd2902f1f0ef63b47998296002a9'
assert P.Path('/Users/ghilmankhan/Downloads/CasuallyFinance').is_dir()
rec={'state':s,'registrations':git('worktree','list','--porcelain'),'checks':checks,'evidence_spot_hashes':len(ev),'free_bytes':shutil.disk_usage(repo).free,'worktree_allocated_bytes':sum(p.stat().st_blocks*512 for p in wt.rglob('*') if p.is_file()),'forensic_sha':sha}
(out/'retirement-before.json').write_text(json.dumps(rec,indent=2));print(json.dumps({k:v for k,v in rec.items() if k!='state'},indent=2));print('PRE_REMOVAL_GATES_PASS')
