import os,json,csv,hashlib,subprocess,collections,re,time
from pathlib import Path
O=Path(__file__).parent; A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z'); P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
os.umask(0o077);(O/'evidence').mkdir(exist_ok=True);(O/'scratch-private').mkdir(exist_ok=True)
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def sh(c,t=60,cwd=P):
 r=subprocess.run(c,cwd=cwd,env=env,capture_output=True,timeout=t);return {'exit':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')}
def dump(n,d): (O/'evidence'/n).write_text(json.dumps(d,indent=2))
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def snap():
 return {k:sh(['git']+v) for k,v in {'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'status':['status','--porcelain=v1','--untracked-files=all'],'refs':['show-ref'],'stashes':['stash','list','--format=%H %gd %s'],'worktrees':['worktree','list','--porcelain']}.items()}
dump('GIT_BEFORE.json',snap());auto=Path('/Users/ghilmankhan/.codex/automations/yios-verified-backup-continuation/automation.toml');dump('AUTOMATION_BEFORE.json',{'path':str(auto),'sha256':sha(auto),'paused':'status = "PAUSED"' in auto.read_text()})
dump('PREFLIGHT.json',{'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'five_hour_percent':67,'weekly_percent':43,'paid_balance':0,'reset_credits':2,'context':'Prior audit summarized; exact context meter unavailable; durable checkpoints used','hostname':sh(['hostname']),'disk':sh(['df','-k',str(O)]),'memory':sh(['memory_pressure']),'writers':sh(['pgrep','-fl','continue_backup|rclone|upload|claude']),'claude_cwd':sh(['lsof','-a','-p','28898','-d','cwd','-Fn']),'ownership':'Protected Claude 873b9a27 and Machine B Finance unchanged; no distributed exclusivity claim; no writes to sources'})
checks=[]
for line in (A/'SHA256SUMS').read_text().splitlines():
 h,n=line.split('  ',1);p=A/n;checks.append({'path':n,'pass':p.is_file() and sha(p)==h})
dump('PREVIOUS_AUDIT_SEAL_CHECK.json',{'entries':len(checks),'all_pass':all(x['pass'] for x in checks),'checks':checks})
# Read required saved artifacts, no filesystem census
names=['YIOS_FULL_BACKUP_COVERAGE_AND_RECOVERY_READINESS_REPORT.md','ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv','FOLDER_BY_FOLDER_COVERAGE.csv','MACHINE_A_B_SOURCE_CROSSWALK.csv','GITHUB_AND_LFS_RECOVERY_STATUS.csv','LFS_POINTER_PAYLOAD_CROSSWALK.csv','MISSING_CRITICAL_ASSETS.csv','NEXT_BACKUP_SCOPE_CANDIDATES.csv','NEXT_BACKUP_SCOPE_PROPOSAL.md','COVERAGE_AUDIT_VALIDATION.json','SHA256SUMS','CONTINUATION_HANDOFF.md']
dump('INPUT_ARTIFACTS.json',[{'path':str(A/n),'bytes':(A/n).stat().st_size,'sha256':sha(A/n)} for n in names])
rows=list(csv.DictReader(open(A/'ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));local=[r for r in rows if r['absolute_path']];important=[r for r in local if r['coverage_status']!='NOT REQUIRED' and r['classification']!='SYMLINK']
# authoritative exact important classification is taken from prior validation and independently count status populations
summary={'local_rows':len(local),'coverage_counts':dict(collections.Counter(r['coverage_status'] for r in local)),'important_path_status_counts':dict(collections.Counter(r['coverage_status'] for r in important)),'dataless':sum(r['dataless']=='True' for r in local),'regular_files_expected':72076,'roots':len(set(r['root_directory'] for r in local)),'prior_validation_checks':len(json.load(open(A/'COVERAGE_AUDIT_VALIDATION.json'))['checks'])}
dump('BASELINE_RECONCILIATION.json',summary)
proposal=(A/'NEXT_BACKUP_SCOPE_PROPOSAL.md').read_text();matches=re.findall(r'^\| (/[^|]+) \| (\d+) \| ([a-f0-9]{64}) \|',proposal,re.M)[:8]
verified=[]
for path,size,h in matches:
 p=Path(path.strip());before=p.stat();actual=sha(p);after=p.stat();equiv=[{'path':r['absolute_path'],'status':r['coverage_status'],'drive':r['drive_remote_id'],'receipt':r['drive_receipt_reference'],'git':r['git_commit_ref']} for r in rows if r['machine_a_sha256']==h]
 parsing=sh(['ffprobe','-v','error','-show_entries','format=format_name,duration','-of','json',str(p)]) if p.suffix=='.mp3' else {'utf8':'PASS','lines':len(p.read_text().splitlines())} if p.suffix in ['.md','.csv'] else sh(['git','bundle','verify',str(p)])
 if p.suffix=='.csv': parsing['csv_rows']=len(list(csv.DictReader(open(p))))
 if p.suffix=='.bundle':dump('BUNDLE_HEADS.json',sh(['git','bundle','list-heads',str(p)]))
 v={'source_path':str(p),'expected_bytes':int(size),'actual_bytes':before.st_size,'expected_sha256':h,'actual_sha256':actual,'integrity':'PASS' if actual==h and before.st_size==int(size) and (before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns) else 'FAIL','source_owner':'Machine B Finance/protected research ownership; no transfer' if '/research/' in str(p) else 'Machine A owner; preserve existing source authority','active_open_handles':sh(['lsof','-Fpc',str(p)])['stdout'],'remote_copy_status':'NO_INDEPENDENT_COPY_PROVEN_IN_SEALED_SCOPE; fresh publication recheck pending','equivalents':json.dumps(equiv),'parsing':json.dumps(parsing),'classification':'Unique authorship/evidence, rebuild not proven' if p.suffix in ['.md','.csv'] else 'Original narration, regenerate-exact not proven' if p.suffix=='.mp3' else 'Recovery container for local commit/stash; prerequisites needed','destination':'Existing owner-only YIOS private namespace, future explicitly approved V8 scope','approval':'REQUIRED_BEFORE_UPLOAD; source writer window unresolved'};verified.append(v)
with open(O/'EIGHT_FILE_PRESERVATION_VERIFICATION.csv','w') as f:
 w=csv.DictWriter(f,fieldnames=verified[0]);w.writeheader();w.writerows(verified)
dump('EIGHT_FILE_CHECKPOINT.json',{'count':len(verified),'bytes':sum(v['actual_bytes'] for v in verified),'all_integrity_pass':all(v['integrity']=='PASS' for v in verified)})
# Preserve selected high-value rows from previous census; no re-enumeration
selected=[r for r in rows if r['source_group'] in ['yios-recovery-status','CasuallyFinance-Forensic-Research'] or '.gray.u8' in r['absolute_path'] or 'casually-finance-script-intelligence' in r['absolute_path'] or ('forensic' in r['absolute_path'].lower() and r['file_type']=='.zip' and r['coverage_status'] not in ['SAFE','NOT REQUIRED'])]
with open(O/'evidence/SELECTED_PRIOR_GAP_ROWS.csv','w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(selected)
print(json.dumps({'output':str(O),'seal_pass':all(x['pass'] for x in checks),'baseline':summary,'eight':len(verified),'bytes':sum(v['actual_bytes'] for v in verified),'selected':len(selected)},indent=2))
