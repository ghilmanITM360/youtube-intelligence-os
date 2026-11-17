import pathlib,json,hashlib,subprocess,datetime,os
base=pathlib.Path('/Users/ghilmankhan/workprojects');wt=base/'yio-cf-editing-forensics';area=wt/'research/casually-finance-editing-forensics';out=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/forensic-ownership-release');old=out.parent/'folder-consolidation'
def git(*args):return subprocess.check_output(['git','-C',str(wt),*args],text=True).strip()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4194304),b''):h.update(b)
 return h.hexdigest()
rows=[r for r in json.loads((old/'inventory.json').read_text())if r['folder']in['yio-cf-editing-forensics','yio-cf-editing-forensics-local-evidence']];fail=[]
for r in rows:
 p=base/r['folder']/r['path']
 if not p.is_file()or sha(p)!=r['sha256']:fail.append(str(p))
assert not fail,fail
s=json.loads((area/'STATUS.json').read_text());done=s['videos_complete'];qas=[]
for item in done:
 vid=item if isinstance(item,str) else item.get('video_id',item.get('id'))
 p=area/'videos'/vid/'QA.json';q=json.loads(p.read_text());assert q['all_checks_pass'];qas.append({'video_id':vid,'qa':str(p.relative_to(wt)),'sha256':sha(p),'status':q.get('status')})
assert len(qas)==38
head=git('rev-parse','HEAD');remote=git('ls-remote','origin','refs/heads/research/casually-finance-editing-forensics').split()[0];assert head==remote=='090f84b3292a3b6c6e94653a6ef1867726e4ebdd';assert git('status','--porcelain=v1','--untracked-files=all')==''
tracked=subprocess.check_output(['git','-C',str(wt),'ls-files','-z']).decode().rstrip('\0').split('\0');assert all((wt/p).exists()for p in tracked)
# Scan tracked text only for exact retirement-sensitive worktree references; evidence sibling references are excluded.
refs=[];needle=str(wt)
for rel in tracked:
 p=wt/rel
 if p.stat().st_size>5000000:continue
 try:lines=p.read_text().splitlines()
 except(UnicodeError,OSError):continue
 for n,line in enumerate(lines,1):
  if needle in line:
   import re
   if re.search(re.escape(needle)+r'(?!-local-evidence)',line):refs.append({'path':rel,'line':n,'text':line})
result={'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host':subprocess.check_output(['hostname'],text=True).strip(),'branch':git('branch','--show-current'),'head':head,'github_head':remote,'tracked_clean':True,'tracked_files':len(tracked),'verified_worktree_files':sum(r['folder']==wt.name for r in rows),'evidence_files':sum(r['folder']=='yio-cf-editing-forensics-local-evidence'for r in rows),'evidence_bytes':sum(r['size']for r in rows if r['folder']=='yio-cf-editing-forensics-local-evidence'),'baseline_manifest_sha256':sha(old/'inventory.json'),'qa':qas,'pending_longform':s['longform_procedure']['order'],'longform_status':s['longform_procedure']['status'],'retirement_sensitive_references':refs,'ignored':git('ls-files','--others','--ignored','--exclude-standard').splitlines(),'worktrees':git('worktree','list','--porcelain')}
(out/'verification.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items()if k not in['qa','worktrees','retirement_sensitive_references']},indent=2));print('retirement_sensitive_references',len(refs));print(json.dumps(refs,indent=2))
