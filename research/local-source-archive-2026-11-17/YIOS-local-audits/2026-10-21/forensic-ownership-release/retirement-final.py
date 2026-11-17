import pathlib as P,subprocess as S,json,hashlib,shutil,csv,datetime
repo=P.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');out=P.Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-21/forensic-ownership-release');before=json.loads((out/'retirement-before.json').read_text());v=json.loads((out/'verification.json').read_text());branch='research/casually-finance-editing-forensics';sha=v['head']
def git(*a):return S.check_output(['git','-C',str(repo),*a],text=True).strip()
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s={k:git(*a) for k,a in {'refs':['for-each-ref','--format=%(refname) %(objectname)'],'stash':['stash','list','--format=%H'],'status':['status','--porcelain=v1','--untracked-files=all'],'ignored':['ls-files','--others','--ignored','--exclude-standard'],'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'ab':['rev-list','--left-right','--count','HEAD...@{upstream}']}.items()};assert s==before['state']
wt=git('worktree','list','--porcelain');assert wt.count('worktree ')==1 and 'worktree '+str(repo) in wt;assert not (repo.parent/'yio-cf-editing-forensics').exists()
assert git('rev-parse',branch)==sha==git('ls-remote','origin','refs/heads/'+branch).split()[0]
assert git('ls-remote','origin','refs/heads/research/finance-economics-intelligence').split()[0]==s['head']
for q in v['qa']:
 data=S.check_output(['git','-C',str(repo),'show',branch+':'+q['qa']]);assert hashlib.sha256(data).hexdigest()==q['sha256'];assert json.loads(data)['all_checks_pass']
status=json.loads(git('show',branch+':research/casually-finance-editing-forensics/STATUS.json'));assert len(v['pending_longform'])==10 and 'WRITTEN_NOT_STARTED' in json.dumps(status)
evroot=repo.parent/'yio-cf-editing-forensics-local-evidence';rows=[r for r in json.loads((out.parent/'folder-consolidation/inventory.json').read_text()) if r['folder']==evroot.name];assert len(rows)==392
assert {str(p.relative_to(evroot))for p in evroot.rglob('*')if p.is_file()}=={r['path']for r in rows}
for r in rows:
 st=(evroot/r['path']).stat();assert st.st_size==r['size'] and st.st_mtime_ns==r['mtime_ns']
for r in sorted(rows,key=lambda r:r['path'])[::19]:assert h(evroot/r['path'])==r['sha256']
f=repo/'research/finance-economics-intelligence';audits=[json.loads(l)for l in (f/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()];universe=list(csv.DictReader((f/'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv').open()));assert len(universe)==len({r['video_id']for r in universe})==1612;assert len(audits)==966
complete={'COMPLETE_EVIDENCE_BACKED','COMPLETE_LIMITED_EVIDENCE'};done=sum(all(s in complete for s in r['statuses'].values())for r in audits);nxt=next(r['Video_ID']for r in audits if any(s in {'NOT_STARTED','IN_PROGRESS'}for s in r['statuses'].values()));assert done==437 and nxt=='S_8SLGjLrBM'
books=list(f.rglob('*.xlsx'));assert len(books)==1;assert h(books[0])=='b87869124ec31a59b8d9e640ed370f72f303cd2902f1f0ef63b47998296002a9'
fs=S.run(['git','-C',str(repo),'fsck','--full'],capture_output=True,text=True);(out/'retirement-fsck.txt').write_text(fs.stdout+fs.stderr);assert fs.returncode==0
free=shutil.disk_usage(repo).free;delta=free-before['free_bytes'];result={'verified_local_date':'2026-10-22','before_count':2,'after_count':1,'registrations':wt,'state_unchanged':True,'head':s['head'],'forensic_head':sha,'qa_records_accessible':38,'longform_pending':10,'evidence_files':392,'evidence_bytes':sum(r['size']for r in rows),'evidence_spot_hashes':21,'finance_total':1612,'original':966,'expansion':646,'audited':done,'remaining':1612-done,'next':nxt,'workbooks':1,'untracked':len(s['status'].splitlines()),'ignored':len(s['ignored'].splitlines()),'fsck_exit':fs.returncode,'free_bytes_before':before['free_bytes'],'free_bytes_after':free,'measured_free_space_delta':delta,'retired_file_allocated_bytes':before['worktree_allocated_bytes']}
(out/'retirement-after.json').write_text(json.dumps(result,indent=2))
refs='\n'.join('- '+r['path']+':'+str(r['line'])for r in v['retirement_sensitive_references'])
report=f'''# Forensic worktree retirement result — 2026-10-22 (Asia/Karachi)

MACHINE_A_ONE_WORKTREE_COMPLETE

Owner-authorized release was read and final safety gates passed. Normal `git worktree remove` succeeded without force.
Removed: /Users/ghilmankhan/workprojects/yio-cf-editing-forensics
Registrations: 2 before; 1 after. Retained: {repo}

Retained forensic branch: {branch}
Local and live GitHub SHA: {sha}
All refs and stash IDs identical before/after (retirement-before.json). All 38 published QA records accessible and hash matched; 10 long-form videos remain WRITTEN_NOT_STARTED. Visual QA does not claim audio listening completion. Full history remains reachable from retained branch; git fsck --full exit 0 (retirement-fsck.txt).

Finance branch unchanged: {s['branch']}
HEAD/live origin: {s['head']}; upstream ahead/behind 0/0.
Tracked clean; {result['untracked']} untracked and {result['ignored']} ignored entries unchanged exactly.
Read-only source check: 1,612 unique videos, 966 originals + 646 expansion, 437 audited, 1,175 remaining; next S_8SLGjLrBM. Exactly one workbook, original SHA-256 unchanged. No Excel regeneration or native recalculation performed.

External evidence retained in place: {evroot}
392 files, 4,459,400,272 bytes; complete file/size/mtime census unchanged and 21 deterministic SHA-256 spot checks matched the recently fully verified inventory. Retiring checkout's 4,274 files all hash checked before removal; sole ignored .DS_Store independently preserved as worktree.DS_Store. Source media /Users/ghilmankhan/Downloads/CasuallyFinance retained. No recovery archives, other projects, source media or evidence edited/relocated.

Four stale references, retained on forensic branch for future authorized repair:
{refs}

Do not run prep_banded.sh/prep_full.sh until their hardcoded cd paths are fixed on the forensic branch. Future research should use the existing branch in canonical checkout only after Finance ownership permits a safe switch. Read the release handoff and branch STATUS.json/RESUME_HERE.md first; external evidence paths remain valid. No new checkout/branch needed or authorized here. Pending long-form work remains unfinished.

Measured free bytes: {before['free_bytes']} before; {free} after; observed increase {delta} bytes ({delta/1024**3:.3f} GiB). This filesystem-wide measurement can include concurrent system activity; retired file allocation measured {before['worktree_allocated_bytes']} bytes, not a claim of exclusive physical APFS reclamation.

No retirement blockers remain. Four stale references require repair before future script execution. Usage at preflight: 12% five-hour, 46% weekly; no paid credits/reset used, no context pressure (exact percentage unavailable).
'''
(out/'FORENSIC_WORKTREE_RETIREMENT_RESULT.md').write_text(report)
print(json.dumps(result,indent=2))
