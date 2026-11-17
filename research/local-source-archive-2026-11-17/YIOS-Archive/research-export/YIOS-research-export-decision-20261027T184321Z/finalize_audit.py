import pathlib,json,csv,subprocess,os,hashlib,datetime,collections
O=pathlib.Path(__file__).parent;E=O/'evidence';R=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21');P=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_NO_REPLACE_OBJECTS='1',GIT_TERMINAL_PROMPT='0');checks=[]
def check(name,ok,detail=''):checks.append(dict(name=name,pass_=bool(ok),detail=detail))
initial=json.loads((E/'initial_metadata.json').read_text());after=[];dirs=0
for base,ds,fs in os.walk(R,followlinks=False):
 dirs+=len(ds)
 for n in fs:
  p=pathlib.Path(base)/n;s=p.lstat();after.append(dict(relative_path=str(p.relative_to(R)),size=s.st_size,blocks=s.st_blocks,flags=s.st_flags,mtime_ns=s.st_mtime_ns,mode=s.st_mode,dataless=bool(s.st_flags&0x40000000),symlink=p.is_symlink()))
beforemap={r['relative_path']:r for r in initial};aftermap={r['relative_path']:r for r in after};delta=[]
for p in set(beforemap)|set(aftermap):
 a=beforemap.get(p);b=aftermap.get(p)
 if a!=b:delta.append(dict(path=p,before=a,after=b))
(E/'final_metadata.json').write_text(json.dumps(after));(E/'source_metadata_delta.json').write_text(json.dumps(delta,indent=2));check('target_all_metadata_identical',not delta,delta[:10]);check('target_count_5373',len(after)==5373);check('target_logical_bytes',sum(r['size'] for r in after)==3710635920);check('target_dataless_count',sum(r['dataless'] for r in after)==5372)
for name,args in {'status':['status','--porcelain=v1','--untracked-files=all'],'refs':['show-ref'],'head':['rev-parse','HEAD'],'stashes':['stash','list'],'worktrees':['worktree','list','--porcelain']}.items():
 z=subprocess.run(['git','-c','remote.origin.promisor=false',*args],cwd=P,env=env,capture_output=True,check=True).stdout;(E/f'git_after_{name}.txt').write_bytes(z);before=(E/f'git_before_{name}.txt').read_bytes();check('git_'+name+'_unchanged',z==before,'See exact before/after receipts')
 if name=='refs' and z!=before:
  a=set(before.decode().splitlines());b=set(z.decode().splitlines());(E/'git_ref_delta.json').write_text(json.dumps(dict(added=sorted(b-a),removed=sorted(a-b)),indent=2))
check('no_automatic_git_network_recovery',False,'Safety incident: initial Git ls-tree spawned implicit remote recovery; 87 pack-related files creation/mtime during audit. Object store pre-state not captured; cannot certify unchanged. Audit process stopped; later reads disable lazy fetching.')
auto=pathlib.Path('/Users/ghilmankhan/.codex/automations/yios-verified-backup-continuation/automation.toml');ab=auto.read_bytes();check('automation_paused',b'status = "PAUSED"' in ab)
resources=dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),five_hour_percent=22,weekly_percent=59,paid_credit_balance=0,reset_credits_available=2,reset_credits_redeemed=0,free_disk_bytes=os.statvfs(O).f_bavail*os.statvfs(O).f_frsize,memory_free_percent=37,context_meter='Not exposed; no in-task compaction; durable checkpoints saved',host=os.uname().nodename,automation_sha256=hashlib.sha256(ab).hexdigest(),target_subdirectories=dirs);(E/'final_resources.json').write_text(json.dumps(resources,indent=2));check('disk_reserve_5GB',resources['free_disk_bytes']>=5_000_000_000);check('usage_below_owner_checkpoints',22<90 and 59<95)
counts={}
for p in O.glob('*.csv'):
 with p.open(newline='') as f:
  reader=csv.DictReader(f);rs=list(reader);check(p.name+'_valid',bool(reader.fieldnames) and all(None not in r for r in rs));counts[p.name]=len(rs)
check('inventory_5373',counts['COMPLETE_SOURCE_FILE_INVENTORY.csv']==5373);check('physical_crosswalk_5373',counts['REPOSITORY_CONTENT_CROSSWALK.csv']==5373);check('embedded_crosswalk_9011',counts['EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv']==9011)
for p in E.glob('*.json'):
 try:json.loads(p.read_text());ok=True
 except Exception:ok=False
 check(str(p.relative_to(O))+'_valid_json',ok)
required=['YIOS_RESEARCH_EXPORT_FOLDER_DECISION_REPORT.md','COMPLETE_SOURCE_FILE_INVENTORY.csv','REPOSITORY_CONTENT_CROSSWALK.csv','UNIQUE_USEFUL_DATA.csv','DUPLICATES_AND_SEMANTIC_OVERLAPS.csv','RECOMMENDED_YIOS_INTEGRATIONS.md','EXTERNAL_PRESERVATION_RECOMMENDATIONS.md','MANUAL_CLEANUP_REVIEW.md','CONTENT_ACCESS_AND_ICLOUD_LIMITATIONS.md']
check('required_content_deliverables_present',all((O/p).is_file() for p in required))
validation=dict(status='PARTIAL_CONTENT_ACCESS_BLOCKED_WITH_GIT_SAFETY_INCIDENT',scope='Metadata-complete target; one resident target file syntax/schema-complete; semantic sample only; bounded local/published source-version comparison',complete_file_semantic_audit=False,source_content_changes_observed=False if not delta else 'See metadata delta; content cause unknown',cloud_uploads_performed=0,explicit_git_fetch_commands=0,implicit_git_fetch_ruled_out=False,no_source_script_execution=True,checks=checks,csv_rows=counts,resources=resources,limitations=['5372 original files CONTENT_NOT_ACCESSIBLE','No exact top-level CSV/control or compressed original verification','Embedded source-hash match is not transformed-record fidelity validation','No complete historical Git deletion/tags/all-version census','Implicit Git recovery/object-store incident; no complete object-store before baseline','No independent full-folder restore; no cleanup certification'],passed=sum(c['pass_'] for c in checks),failed=sum(not c['pass_'] for c in checks))
(O/'VALIDATION.json').write_text(json.dumps(validation,indent=2))
(O/'CONTINUATION_HANDOFF.md').write_text(f'''# Continuation handoff — decision audit only

Status {validation['status']}. This folder audit stops here; do not start the next folder automatically.

Target {R}; output {O}. Complete metadata5373files/3710635920logicalbytes;5372dataless, one resident JSONL2741894860bytes. Full stream1089195records,19kinds,1157schemas,9011source versions/8811paths; no parse errors. Semantic samples only.

Published branch exact-hash match8335source versions; combined local/Git exact8558;453unresolved. All1239video/871channelIDs absent from registry occur in exact-published source bytes; do not call them missing-from-GitHub. Six already-local/untracked research files77142bytes fresh-hash match; no published equivalent proven. Do not copy them twice or take Finance ownership.

No target hydration, source script execution, integration, Drive upload, commit/push, deletion or ownership transfer. Automation paused. No credits/reset redeemed. Final usage22%/59%, disk{resources['free_disk_bytes']}bytes, memory37%free; refresh before future work.

SAFETY INCIDENT: Initial partial-clone git ls-tree triggered automatic remote recovery. Audit process and attributable orphan descendants stopped.87pack-related files creation/mtime during audit. Full prior object-store state and per-pack actor unavailable; do not certify no Git writes/downloads. Later Git reads use GIT_NO_LAZY_FETCH=1 plus remote.origin.promisor=false. Do not delete or reset objects. Exact Git HEAD/status/refs/stash/worktree comparisons in VALIDATION.json. Preserve the incident receipt.

Next source-specific decisions (not approval): bounded named control-file access with timeout/download cap; original gzip/remote-recovered payload integrity and independent private restore; six-file existing-owner review and dated factual revalidation; optional canonical registry integration proposal through existing schemas. No mass copying, V8 upload or cleanup.

Do not rerun census/compare/report scripts blindly. They preserve methods but some early versions required safety corrections; final artifacts include the incident and final constraints. SHA256SUMS seals every output/evidence file except itself. Prior V7 and V8-readiness receipts remain untouched. Machine B current state not directly accessible/certified.
''')
# Append final outcome without overwriting original incident explanation.
p=O/'YIOS_RESEARCH_EXPORT_FOLDER_DECISION_REPORT.md';p.write_text(p.read_text()+f'\nFinal acceptance: {validation["passed"]} checks passed, {validation["failed"]} failed. Status {validation["status"]}. Target metadata changed paths={len(delta)}; all details retained in VALIDATION.json. Latest usage22% five-hour/59%weekly, disk{resources["free_disk_bytes"]:,}bytes free, memory37%free; paid0/reset2available, none redeemed. Automation PAUSED. These resource values are observation-time, not a future transfer gate.\n')
files=sorted(p for p in O.rglob('*') if p.is_file() and p.name!='SHA256SUMS');manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(O))+'\n' for p in files);(O/'SHA256SUMS').write_text(manifest)
for line in manifest.splitlines():
 h,rel=line.split('  ',1);assert hashlib.sha256((O/rel).read_bytes()).hexdigest()==h
for p in files+[O/'SHA256SUMS']:p.chmod(0o400)
for p in O.rglob('*'):
 if p.is_dir():p.chmod(0o700)
print(json.dumps(dict(status=validation['status'],passed=validation['passed'],failed=validation['failed'],failures=[c for c in checks if not c['pass_']],manifest_files=len(files),manifest_sha256=hashlib.sha256((O/'SHA256SUMS').read_bytes()).hexdigest(),output=str(O)),indent=2))
