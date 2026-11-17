from audit import *
from data_audit import blob,tree,F
import gzip,plistlib,io,zipfile
def main():
 # Exact live re-observation does not fetch, push, claim or mutate any branch.
 br=run(['gh','api','--paginate','--slurp','repos/ghilmanITM360/youtube-intelligence-os/branches?per_page=100']);write('after/github-branches.json',br)
 live={x['name']:x['commit']['sha'] for page in json.loads(br['stdout']) for x in page} if not br['code'] else {}
 after=[];before=read('before/checkouts.json')
 for d in before:
  p=Path(d['path']);head=git('rev-parse','HEAD',cwd=p);up=git('rev-parse','--abbrev-ref','@{upstream}',cwd=p);ush=git('rev-parse',up,cwd=p)
  counts=git('rev-list','--left-right','--count','HEAD...'+up,cwd=p).split()
  row={'path':str(p),'branch':git('symbolic-ref','--short','HEAD',cwd=p),'head_before':d['head'],'head_after':head,'upstream':up,'upstream_sha':ush,'live_upstream_sha':live.get(up.removeprefix('origin/')),'ahead':int(counts[0]),'behind':int(counts[1]),'status':git('status','--porcelain=v1','--untracked-files=all',cwd=p),'operations':operations(p),'common_dir':d['common_dir'],'action':'ALREADY_CURRENT_NO_CHECKED_OUT_UPDATE_REQUIRED','tracked_tree_changed':bool(git('diff','--name-only',d['head'],'HEAD',cwd=p))}
  after.append(row)
 write('after/checkouts.json',after);csvout('after/checkouts.csv',after)
 write('after/refs.json',refs());write('after/stash-sha.txt',git('rev-parse','refs/stash')+'\n');write('after/disk-memory.json',[run(['df','-k',str(ROOT)]),run(['memory_pressure']),run(['sysctl','vm.swapusage'])])
 expected=read('remote/freshness.json')['remote_heads']
 moved=[{'branch':n,'fetched_sha':expected.get('refs/remotes/origin/'+n),'live_sha':s} for n,s in live.items() if expected.get('refs/remotes/origin/'+n)!=s]
 write('synchronization.json',{'initial_fetch_status':read('remote/freshness.json'),'final_live_observed_at':br['at'],'live_remote_heads_moved_since_fetch':moved,'local_branch_upstream_mismatches':[(r['name'],r['ahead_upstream'],r['behind_upstream']) for r in read('branch_matrix.json') if r['kind']=='local' and (r['ahead_upstream'] or r['behind_upstream'])],'checked_out_updates':0,'reason':'Every local branch was already at its configured fetched upstream. No fast-forward would change a ref. Main is a branch, not the primary checkout assignment. No research branch integration or writer transfer performed.','preserved_stash':git('rev-parse','refs/stash'),'after_checkouts':after})
 # Every changed/ignored path receives a disposition; no bulk deletion is inferred.
 cleanup=read('cleanup_ledger.json');removed={x['path']:x for x in cleanup};classifications=[]
 filemap={r['path']:r for r in csv.DictReader((OUT/'files.csv').open())}
 for d in before:
  for rel in d['ignored']+d['untracked']:
   p=Path(d['path'])/rel;record=filemap.get(str(p),{});classification='Unknown';reason='Local role not sufficiently established for deletion.'
   if str(p) in removed:classification=removed[str(p)]['classification'];reason=removed[str(p)]['reason']
   elif rel=='.env':reason='Private local configuration; values not read; preserve credential/service dependency.'
   elif rel.startswith('data/raw/'):classification='Unique incomplete research';reason='Raw source/evidence safety boundary; ignored status is not evidence of dispensability.'
   elif any(x in rel for x in ['__pycache__','.pytest_cache','.ruff_cache','.venv','egg-info','.cache']):classification='Active work';reason='Runtime/cache/dependency support; no need to remove for synchronization; preserve.'
   elif rel.endswith('.db'):reason='Legacy local catalog/index; not current frozen source; unknown consumers and retained for recovery.'
   elif Path(rel).name=='.DS_Store':classification='Unused local modification';reason='OS metadata; preserved because it does not block synchronization (only invalid Git-ref metadata was removed).'
   classifications.append({'path':str(p),'git_state_before':'ignored' if rel in d['ignored'] else 'untracked','classification':classification,'reason':reason,'action':'REMOVED_EXACT_FILE' if str(p) in removed else 'PRESERVED','bytes_before':record.get('bytes'),'recovery':removed.get(str(p),{}).get('recovery','Original remains in place')})
 csvout('local_path_classifications.csv',classifications)
 # Scheduler inspection is local only and read-only.
 sched=[]
 for base in [Path.home()/'Library/LaunchAgents',Path('/Library/LaunchAgents'),Path('/Library/LaunchDaemons')]:
  if not base.exists():continue
  for p in base.glob('*.plist'):
   try:d=plistlib.loads(p.read_bytes())
   except Exception:continue
   if any(k in json.dumps(d).lower() for k in ['yios','youtube-intelligence','forensics','finance-economics']):sched.append({'path':str(p),'fields':{k:v for k,v in d.items() if k in ['Label','StartCalendarInterval','StartInterval','RunAtLoad','WorkingDirectory']}})
 write('schedulers.json',{'local_codex_matching_automations':read('before/automations.json'),'cron':read('before/cron.json'),'matching_launch_agents':sched,'claude_top_level_schedule_entries':[str(p) for p in (Path.home()/'.claude').glob('*') if any(k in p.name.lower() for k in ['sched','cron','auto'])],'machine_a_scheduler':'UNKNOWN; historical Video005 handoff references yios-visual-forensics-machine-a, 7 */2 * * *, ~/YIOS-local-audits/vf_lock.sh. Those are not established on this Mac. No schedules modified.','codex_app_activity_observation':{'observed_date':'2026-11-02','source':'supported list_threads(limit=50)','active_yios_chats':['Audit and sync YIOS repository'],'other_yios_chats_seen_notLoaded':['Publish NICK_180 safely','Audit visual forensics research','Audit finance videos in batches','Resume Finance deep audits'],'limitation':'notLoaded/idle is not a writer release; other clients and Machine A remain outside visibility'}})
 # Latest existing CI job: never retrigger.
 jobs=run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/actions/runs/41053016403/jobs']);write('validation/latest-ci-jobs.json',jobs)
 annotations=run(['gh','api','repos/ghilmanITM360/youtube-intelligence-os/check-runs/124053485843/annotations']);write('validation/latest-ci-annotations.json',annotations)
 # Diagnose the two reproducible provenance mismatches, without rewriting evidence.
 issues=[]
 for ds,aid in [('DS-000028','DS-000028-F020'),('DS-000030','DS-000030-F019')]:
  f=ROOT/'data/manifests'/f'{ds}_FILES.csv';r=next(r for r in csv.DictReader(f.open()) if r['artifact_id']==aid);p=ROOT/r['repository_relative_path']
  issues.append({'dataset':ds,'artifact_id':aid,'path':str(p),'expected_bytes':int(r['size_bytes']),'actual_bytes':p.stat().st_size,'expected_sha256':r['sha256'],'actual_sha256':sha(p),'semantic_class':r['raw_or_derived_classification'],'latest_commit':git('log','-1','--format=%H %s','--',r['repository_relative_path']),'interpretation':'Historical ledger fingerprint of mutable shared .gitattributes drifted; not a demonstrated raw-data mismatch. Needs provenance-safe correction/ownership, not replacement of raw evidence.'})
 write('validation/provenance_mismatches.json',issues)
 # Archive-only recovery is available for the older published xtqb source.
 zpath=Path.home()/'Downloads/CasuallyFinance.zip';target='030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66';found=[]
 with zipfile.ZipFile(zpath) as z:
  for i in z.infolist():
   if i.file_size!=49993573:continue
   h=hashlib.sha256()
   with z.open(i) as f:
    for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
   if h.hexdigest()==target:found.append({'archive':str(zpath),'member':i.filename,'bytes':i.file_size,'sha256':target,'availability':'PRESENT_IN_ARCHIVE_HASH_VERIFIED_NOT_EXTRACTED'})
 v=read('video006_remote_search.json');v['legacy_published_package']={'ref':'origin/codex/casually-finance-forensic-research','root':'data/extracted/forensic-analysis/casually-finance/2026-10-12/02_VIDEO_FORENSICS/xtqbRt94TTw/','qa_status':'PASS_STRUCTURAL','states':489,'shots_reviewed':133,'source_sha256':target,'source_bytes':49993573,'source_original_machine_a':"/Users/ghilmankhan/Downloads/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4",'local_archive_matches':found,'limitation':'This older PR21 package is not the reported new Video006 Checkpoint B; new source fingerprint must be compared before assuming identical video encode.'};write('video006_remote_search.json',v)
 # Evaluate large stash archive matches only against exact size candidates; no new media copies.
 ss=read('stash_summary.json');matches=[]
 for r in csv.DictReader((OUT/'stash_contents.csv').open()):
  if r['matching_local_files']!='[]':continue
  for f in filemap.values():
   if int(f['bytes'])==int(r['bytes']) and f['kind']=='file':
    p=Path(f['path'])
    if p.exists() and sha(p)==r['sha256']:matches.append({'stash_path':r['path'],'matching_path':str(p),'sha256':r['sha256'],'bytes':int(r['bytes'])})
 ss['additional_unbounded_archive_matches']=matches;write('stash_summary.json',ss)
 # Refresh integrity/recovery proof after authorized cleanup.
 write('after/git-fsck.json',read('validation/git-fsck-after-cleanup.json'))
 assert all(sha(OUT/r['path'])==r['sha256'] for r in read('RECOVERY_MANIFEST.json'))
 for row in cleanup:
  with gzip.open(row['recovery'],'rb') as f:assert hashlib.sha256(f.read()).hexdigest()==row['sha256']
 assert all(not d['status'] and d['head_before']==d['head_after'] for d in after)
 print(json.dumps({'checkouts':len(after),'all_clean':all(not d['status'] for d in after),'remote_moved':moved,'stash_large_archive_matches':matches,'recovery_verified':True},indent=2))
if __name__=='__main__':main()
