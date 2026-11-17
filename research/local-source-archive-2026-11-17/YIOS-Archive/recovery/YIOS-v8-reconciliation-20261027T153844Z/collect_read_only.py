import os,subprocess,json,hashlib,csv,time,re
from pathlib import Path
from datetime import datetime,timezone
os.umask(0o077)
O=Path(__file__).parent; E=O/'evidence'; P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os'); A=Path('/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z')
REF='refs/codex/turn-diffs/captures/1793071154306/f4029e0b-cceb-4bf2-8c8b-c56efc1ceeb1/base';OID='93dca940f88913968abf5ba9db1135c4a3027f69'
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def run(args,t=30):
 try:
  r=subprocess.run(args,cwd=P,env=env,capture_output=True,timeout=t);return {'exit':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')}
 except subprocess.TimeoutExpired:return {'exit':124,'stdout':'','stderr':'BOUNDED_TIMEOUT'}
def git(*a):return run(['git',*a])
def dump(n,x):(E/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def meta(p):
 if not p.exists():return {'path':str(p),'exists':False}
 s=p.stat();return {'path':str(p),'exists':True,'bytes':s.st_size,'sha256':sha(p),'mtime_ns':s.st_mtime_ns,'birthtime':s.st_birthtime,'ctime_ns':s.st_ctime_ns,'inode':s.st_ino,'mode':oct(s.st_mode)}
def snap():
 d={k:git(*v) for k,v in {'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'status':['status','--porcelain=v1','--untracked-files=all'],'refs':['show-ref'],'stashes':['stash','list','--format=%H %gd %s'],'worktrees':['worktree','list','--porcelain'],'index_entries':['ls-files','--stage'],'index_flags':['ls-files','-v'],'staged':['diff','--cached','--raw','--no-ext-diff','--no-textconv','HEAD'],'unstaged':['diff-files','--raw','--no-ext-diff'],'research_tracked_diff':['diff','--no-ext-diff','--no-textconv','--name-status','HEAD','--','research']}.items()}
 d['index_file']=meta(P/'.git/index');return d
S=snap();dump('GIT_CURRENT_BEFORE.json',S)
D={'ref':REF,'expected_oid':OID,'exact_ref':git('show-ref','--verify',REF),'object_type':git('cat-file','-t',OID),'object_size':git('cat-file','-s',OID),'head_tree':git('rev-parse','HEAD^{tree}'),'ref_reflog':git('reflog','show','--date=iso-strict',REF),'reflog_exists':git('reflog','exists',REF),'same_pattern':git('for-each-ref','--format=%(refname) %(objectname) %(objecttype)','refs/codex/turn-diffs'),'head_reflog_tail':git('reflog','show','-8','--date=iso-strict','HEAD'),'ref_file':meta(P/'.git'/REF),'ref_log_file':meta(P/'.git/logs'/REF),'head_file':meta(P/'.git/HEAD'),'packed_refs_file':meta(P/'.git/packed-refs'),'shallow':git('rev-parse','--is-shallow-repository'),'remotes':git('remote','-v')}
if D['ref_log_file']['exists']:D['ref_log_text']=(P/'.git/logs'/REF).read_text()[-8000:]
D['timestamp_component_utc']=datetime.fromtimestamp(1793071154306/1000,timezone.utc).isoformat();dump('EXACT_REF_INSPECTION.json',D)
# Existing local seal only: no iCloud/provider re-read, no new source census.
seal=[]
for l in (A/'SHA256SUMS').read_text().splitlines():
 h,n=l.split('  ',1);p=A/n
 seal.append({'path':n,'expected_sha256':h,'actual_sha256':sha(p),'pass':sha(p)==h})
dump('PRIOR_SEAL_CHECK.json',{'seal':meta(A/'SHA256SUMS'),'entries':seal,'passed':sum(r['pass'] for r in seal),'count':len(seal)})
eight=[]
for r in csv.DictReader((A/'EIGHT_FILE_PRESERVATION_VERIFICATION.csv').open()):
 p=Path(r['source_path']);a=p.stat();h=sha(p);b=p.stat();eight.append({'path':str(p),'bytes':b.st_size,'sha256':h,'expected_bytes':int(r['expected_bytes']),'expected_sha256':r['expected_sha256'],'stable_read':(a.st_ino,a.st_size,a.st_mtime_ns)==(b.st_ino,b.st_size,b.st_mtime_ns),'pass':h==r['expected_sha256'] and b.st_size==int(r['expected_bytes']),'independent_evidence':r['remote_copy_status'],'source_owner_record':r['source_owner']})
dump('EIGHT_SOURCE_REFRESH.json',eight)
auto=Path('/Users/ghilmankhan/.codex/automations/yios-verified-backup-continuation/automation.toml');dump('AUTOMATION_CURRENT.json',{'metadata':meta(auto),'paused':'status = "PAUSED"' in auto.read_text(),'historical_sha256':json.loads((A/'evidence/AUTOMATION_AFTER.json').read_text())['sha256']})
dump('RESOURCES_PREFLIGHT.json',{'utc':datetime.now(timezone.utc).isoformat(),'usage_five_hour_percent':2,'usage_weekly_percent':56,'context':'Prior task compacted; current task has sufficient capacity for bounded review; exact context meter unavailable','paid_balance':0,'reset_credits_available':2,'paid_or_reset_used':False,'disk':run(['df','-k',str(O)]),'free_bytes':os.statvfs(O).f_bavail*os.statvfs(O).f_frsize,'mac_reserve_bytes':5000000000,'memory':run(['memory_pressure']),'hostname':run(['hostname']),'processes':run(['ps','-axo','pid,ppid,etime,comm']),'ownership':'No writer takeover. Protected Claude session 873b9a27-ba03-4183-aa61-f82d01f65998 and Machine B Finance permissions preserved. Process existence is not current session-owner authentication. No distributed writer exclusivity claim.'})
print(json.dumps({'prior_seal':[sum(r['pass'] for r in seal),len(seal)],'eight':[sum(r['pass'] for r in eight),len(eight)],'head':S['head'],'branch':S['branch'],'ref_type':D['object_type'],'head_tree':D['head_tree'],'reflog':D['ref_reflog'],'reflog_exists':D['reflog_exists'],'ref_metadata':D['ref_file'],'staged':S['staged'],'unstaged':S['unstaged']},indent=2))
