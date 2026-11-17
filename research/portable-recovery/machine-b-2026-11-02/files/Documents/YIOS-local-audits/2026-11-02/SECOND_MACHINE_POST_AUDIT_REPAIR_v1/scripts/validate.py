from audit import *
def main():
 py=str(ROOT/'.venv/bin/python');fbase=ROOT/'research/finance-economics-intelligence'
 steps=[
 ('git-diff-check',['git','diff','--check'],ROOT,120),
 ('git-fsck',['git','fsck','--full','--no-dangling'],ROOT,300),
 ('tracked-secret-scan',[py,'scripts/scan_tracked_secrets.py'],ROOT,180),
 ('dataset-ledgers',[py,'-m','scripts.validate_dataset_ledgers'],ROOT,300),
 ('registry',[py,'-m','scripts.validate_youtube_channel_registry'],ROOT,300),
 ('finance-audit',[py,'/private/tmp/yios-sync-audit-v1/finance_validate.py',str(fbase),str(OUT/'validation/finance'),'validate_audit_966.py'],ROOT,300),
 ('finance-research',[py,'/private/tmp/yios-sync-audit-v1/finance_validate.py',str(fbase),str(OUT/'validation/finance'),'validate_research.py'],ROOT,300),
 ('finance-tests',[py,'-m','pytest','-q','-p','no:cacheprovider',str(fbase)],ROOT,300),
 ('finance-formatting',['node','--test','test_workbook_formatting.mjs'],fbase,120),
 ('repository-tests',[py,'-m','pytest','-q','-p','no:cacheprovider','tests'],ROOT,300),
 ('coordination-tests',[py,'-m','pytest','-q','-p','no:cacheprovider','tests/test_yios_coordination.py','tests/test_yios_checkpoints.py'],Path.home()/'.codex/worktrees/yios-dual-machine/youtube-intelligence-os',300),
 ]
 results=[]
 for name,args,cwd,timeout in steps:
  started=time.monotonic();r=run(args,cwd,timeout);r['elapsed_seconds']=round(time.monotonic()-started,3);r['name']=name
  write('validation/'+name+'.json',r);write('validation/'+name+'.log',r['stdout']+'\nSTDERR\n'+r['stderr']);results.append({'name':name,'code':r['code'],'elapsed_seconds':r['elapsed_seconds'],'log':'validation/'+name+'.log','result':'PASS' if not r['code'] else ('TIMEOUT' if r['code']==124 else 'FAIL')});write('validation_results.json',results)
  print(name,r['code'],r['stdout'][-700:],flush=True)
 # Record exact environment package availability without installing anything.
 write('validation/runtime.json',run([py,'-c','import sys,importlib.metadata as m,json; print(json.dumps({"python":sys.version,"packages":{p:m.version(p) for p in ["pytest","openpyxl","Pillow"]}},indent=2))']))
 write('validation/post-status.json',[{'path':d['path'],'status':git('status','--porcelain=v1','--untracked-files=all',cwd=Path(d['path']))} for d in read('before/checkouts.json')])
if __name__=='__main__':main()
