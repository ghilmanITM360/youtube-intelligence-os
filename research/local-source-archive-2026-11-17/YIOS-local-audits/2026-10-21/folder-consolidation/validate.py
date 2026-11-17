import pathlib,json,hashlib,subprocess,ast,wave,zipfile,struct,collections,os,csv
out=pathlib.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/folder-consolidation');base=pathlib.Path('/Users/ghilmankhan/workprojects');repo=base/'youtube-intelligence-os';rr=json.loads((out/'inventory.json').read_text());checks=collections.Counter()
for r in rr:
 p=base/r['folder']/r['path']
 if r['folder']=='yio-cf-editing-forensics-local-evidence':
  ext=p.suffix
  if ext=='.json':
   x=json.loads(p.read_text());assert x.get('segments');checks['ASR_JSON']+=1
  elif ext=='.npy':
   with p.open('rb')as f:
    assert f.read(6)==b'\x93NUMPY';version=f.read(2);n=struct.unpack('<H'if version[0]==1 else '<I',f.read(2 if version[0]==1 else 4))[0];header=ast.literal_eval(f.read(n).decode().strip());assert header['shape'][0]>0
   checks['NPY_headers']+=1
  elif ext=='.npz':
   with zipfile.ZipFile(p)as z:assert z.testzip()is None
   checks['NPZ_archives']+=1
  elif ext=='.wav':
   with wave.open(str(p))as w:assert w.getnframes()>0 and w.getframerate()==16000
   checks['WAV_headers']+=1
  elif ext=='.png':
   with p.open('rb')as f:assert f.read(8)==b'\x89PNG\r\n\x1a\n'
   checks['PNG_headers']+=1
 elif r['folder']=='yios-recovery-status'and p.suffix=='.py':ast.parse(p.read_text());checks['recovery_script_parse']+=1
qas=json.loads((out/'forensic-qa.json').read_text());assert len(qas)==38 and all(q['qa']['all_checks_pass']for q in qas)
# Every inventoried source byte reverified, excluding symlinks themselves (targets not recursed).
for r in rr:
 p=base/r['folder']/r['path'];s=p.lstat();assert s.st_size==r['size'] and s.st_mtime_ns==r['mtime_ns'] and s.st_mode==r['mode'],str(p)
 if 'sha256'in r:
  h=hashlib.sha256()
  with p.open('rb')as f:
   for b in iter(lambda:f.read(4194304),b''):h.update(b)
  assert h.hexdigest()==r['sha256'],str(p);checks['unchanged_file_hashes']+=1
 else:assert os.readlink(p)==r['symlink'];checks['unchanged_symlinks']+=1
before=json.loads((out/'git-before.json').read_text());after={}
for k,args in {'refs':['for-each-ref','--format=%(refname) %(objectname)'],'stash':['stash','list','--format=%H'],'main_status':['status','--porcelain=v1','--untracked-files=all'],'ignored':['ls-files','--others','--ignored','--exclude-standard'],'worktrees':['worktree','list','--porcelain']}.items():after[k]=subprocess.check_output(['git','-C',str(repo),*args],text=True)
after['forensic_status']=subprocess.check_output(['git','-C',str(base/'yio-cf-editing-forensics'),'status','--porcelain=v1','--untracked-files=all'],text=True);assert before==after
assert len(after['main_status'].splitlines())==282 and all(x.startswith('?? ')for x in after['main_status'].splitlines());assert len(after['ignored'].splitlines())==2760
f=repo/'research/finance-economics-intelligence';book=f/'FINANCE_1612_COMBINED_INTELLIGENCE.xlsx';assert hashlib.sha256(book.read_bytes()).hexdigest()=='b87869124ec31a59b8d9e640ed370f72f303cd2902f1f0ef63b47998296002a9';assert len(list(f.rglob('*.xlsx')))==1
head=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip();assert head=='d41a5774f1381a21022b70f02d206303195be3a7'
ab=subprocess.check_output(['git','-C',str(repo),'rev-list','--left-right','--count','HEAD...@{upstream}'],text=True).strip();assert ab=='0\t0'
result={'checks':dict(checks),'all_source_bytes_unchanged':True,'git_state_unchanged':True,'head':head,'ahead_behind':ab,'untracked':282,'ignored':2760,'worktrees':2,'stash':after['stash'].strip(),'workbook_sha256':hashlib.sha256(book.read_bytes()).hexdigest(),'workbook_count':1,'forensic_qa_pass':38,'removed':0,'integrated':0,'reclaimed_bytes':0,'free_bytes_after':__import__('shutil').disk_usage(repo).free}
(out/'final-verification.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
