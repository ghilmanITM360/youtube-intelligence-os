import pathlib,json,csv,hashlib,os,subprocess,datetime,collections
O=pathlib.Path('/Users/ghilmankhan/YIOS-research-export-targeted-20261028'); B=pathlib.Path('/Users/ghilmankhan/YIOS-research-export-decision-20261027T184321Z'); T=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21'); R=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
names=['YOUTUBE_RESEARCH_MASTER_REPORT.md','SUMMARY.json','SOURCE_INDEX.json','SHA256_MANIFEST.json','MISSING_DATA_AND_CONFLICTS.md','ALL_VIDEOS.csv','ALL_CHANNELS.csv','RESEARCH_FILES_INVENTORY.csv','VERIFIED_PROJECT_CHECKPOINTS.json','LFS_DATABASE_RECOVERY.json']
prior={r['relative_path']:r for r in csv.DictReader((B/'COMPLETE_SOURCE_FILE_INVENTORY.csv').open())}
rows=[]
for n in names:
 p=T/n;s=p.stat();rows.append(dict(source_path=str(p),name=n,expected_size=s.st_size,allocated_bytes=s.st_blocks*512,flags=s.st_flags,mtime_ns=s.st_mtime_ns,status='CONTENT_NOT_ACCESSIBLE_DATALESS',new_download_bytes=0,current_sha256='',historical_sha256=prior[n]['sha256_evidence'],historical_hash_authority=prior[n]['hash_authority'],reason='Combined selected set exceeds 30 MB; no partial oversized transfer initiated',metadata_matches_prior=str(s.st_size)==prior[n]['size'] and str(s.st_mtime_ns)==prior[n]['mtime_ns'] and str(s.st_flags)==prior[n]['flags']))
def csvout(n,rs):
 with (O/n).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
csvout('TARGETED_RECOVERY_STATUS.csv',rows)
total=sum(r['expected_size'] for r in rows); controls=[r for r in rows if r['name'] not in ['ALL_VIDEOS.csv','ALL_CHANNELS.csv','RESEARCH_FILES_INVENTORY.csv']];controltotal=sum(r['expected_size'] for r in controls)
checks=[]
for line in (B/'SHA256SUMS').read_text().splitlines():
 h,n=line.split('  ',1);p=B/n;checks.append({'file':n,'pass':hashlib.sha256(p.read_bytes()).hexdigest()==h})
(O/'PRIOR_EVIDENCE_CHECKSUM_VALIDATION.json').write_text(json.dumps(checks,indent=2))
rs=list(csv.DictReader((O/'UNRESOLVED_SOURCE_VERSION_RECHECK.csv').open()));six=json.loads((O/'SIX_DOCUMENT_VERIFICATION.json').read_text());summary=json.loads((O/'RECHECK_SUMMARY.json').read_text())
cap=json.loads((O/'GIT_CAPABILITY.json').read_text());cap['object_reads_permitted']=True;cap['verification']='xcrun resolved real Xcode Git binary; strings contains GIT_NO_LAZY_FETCH twice; no object lookup used this continuation';(O/'GIT_CAPABILITY.json').write_text(json.dumps(cap,indent=2))
# Compare current status, HEAD, worktrees and stash listings to this continuation preflight.
env=os.environ.copy();env.update(GIT_NO_LAZY_FETCH='1',GIT_NO_REPLACE_OBJECTS='1',GIT_TERMINAL_PROMPT='0',GIT_OPTIONAL_LOCKS='0');before=json.loads((O/'PREFLIGHT_GIT.json').read_text());after=[]
for r in before:
 z=subprocess.run(r['command'],cwd=R,env=env,capture_output=True,text=True,timeout=30);after.append({'command':r['command'],'rc':z.returncode,'stdout':z.stdout,'stderr':z.stderr,'matches_before':z.returncode==r['rc'] and z.stdout==r['stdout']})
(O/'FINAL_GIT.json').write_text(json.dumps(after,indent=2))
autom=pathlib.Path('/Users/ghilmankhan/.codex/automations/yios-verified-backup-continuation/automation.toml');atext=autom.read_text();paused='status = "PAUSED"' in atext
resources={'host':subprocess.run(['hostname'],capture_output=True,text=True).stdout.strip(),'free_disk_bytes':os.statvfs('/Users/ghilmankhan').f_bavail*os.statvfs('/Users/ghilmankhan').f_frsize,'usage_five_hour_percent':28,'usage_weekly_percent':60,'paid_credit_balance':0,'reset_credits_available':2,'credits_redeemed_by_audit':0,'automation_paused':paused,'automation_config_sha256':hashlib.sha256(autom.read_bytes()).hexdigest(),'context':'Exact meter unavailable; no compaction within continuation so far','memory_pressure':subprocess.run(['memory_pressure'],capture_output=True,text=True).stdout}
(O/'FINAL_RESOURCES.json').write_text(json.dumps(resources,indent=2))
uses={'TRANSCRIPT_COVERAGE.md':('Historical coverage/provenance, 16/206 usable transcripts; two source-missing Shorts at the time','High: defines evidence limits; preserve historical counts, no current Finance overwrite','Future owner-reviewed private tracking at existing exact path; keep date and ASR limitations'), 'SCRIPT_DNA.md':('16 ASR transcripts, 248 semantic beats and description proxies; hypotheses/associations separated','High: script planning and original writing guidance; not causal performance proof','Future owner-reviewed private tracking at existing exact path; verify dependencies and retain labels'), 'TITLE_DNA.md':('206-title historical exploratory regex features and dated performance ratios','High: packaging hypotheses with positive/negative examples; no CTR proof','Future owner-reviewed private tracking at existing exact path; preserve snapshot/denominator'), 'SOURCE_REGISTER.csv':('52 source records, 11 columns, primary/secondary/local dependencies and dates','High: traceable claim and dependency ledger','Future owner-reviewed private tracking at existing exact path; validate links and remove unsafe private paths only in later approved transformed copy'), 'TOPIC_RESEARCH.md':('2026-10-14 editorial hypotheses and financial claims; not creator unpublished plans','Useful historical draft; time-sensitive facts unvalidated today','Keep historical draft; future tracking only after owner/source-rights review; production use requires fresh claim verification'), 'FINAL_SHORT_SCRIPT.md':('Owner-approval draft, dated Oct 8 financial inputs and Oct 28 forward cue','Useful writing example; not publish-ready on current date','Keep as historical draft; future private Git tracking after owner review, no production publication until revalidated')}
dec=[]
for d in six:
 n=pathlib.Path(d['path']).name;u=uses[n];dec.append({'source_path':d['path'],'proposed_destination':d['path'],'bytes':d['current_size'],'sha256':d['current_sha256'],'purpose':u[0],'usefulness':u[1],'local_yios':'YES_FRESH_EXACT','main_publication':'NOT_PROVEN_IN_PRIOR_COMPARISON','other_branch_publication':'NOT_PROVEN_IN_PRIOR_COMPARISON','primary_recommendation':'ADD_TO_YIOS_REPO_RECOMMENDED_AFTER_SEPARATE_APPROVAL','conditions':u[2],'rights':'No redistribution grant established for third-party transcripts/quotes; private storage does not establish permission; retain short attributed excerpts and require owner review','owner':'Existing Finance/research ownership protected; no integration authority assumed'})
csvout('EXACT_INTEGRATION_DECISIONS.csv',dec)
readme=f'''# YIOS Research Export — targeted revised decision report

Observation date: 2026-10-28 (Asia/Karachi). Status: **PARTIAL — TARGETED RECOVERY BLOCKED BY SELECTED-SET DOWNLOAD BUDGET**.

## Owner ke liye seedhi baat

Is dafa **10 mein se zero named original files recover ya read hue**. Sab iCloud dataless hain. In ka combined expected size **{total:,} bytes ({total/1e6:.2f} MB)** hai; ijazat 30,000,000 bytes ki hai. Aap ne oversized set ka partial transfer mana kiya tha, is liye koi hydration/download shuru nahi hua. Naya downloaded content **0 bytes**. Disk ki kami blocker nahi: latest free {resources['free_disk_bytes']:,} bytes, 5 GB reserve se upar.

Purana 5,373-file census repeat nahi kiya. Pichli report aur us ke 55 sealed artifacts ke checksums dobara verify kiye. Pichla Git lazy-fetch incident aur original FAIL result bilkul preserve hain; yeh revision usay replace ya clean PASS mein tabdeel nahi karti.

**Useful nayi tasdeeq:** 453 unresolved source versions ke current local paths par bounded recheck hua. **18 exact source versions** fresh full SHA-256 se locally mil gaye. **7** ke current paths par mukhtalif versions hain; historical export versions abhi unproven hain. **428** baqi unresolved hain. Is tarah **435 exported versions ab bhi unresolved** hain. Yeh missing original files ki ginti nahi. Current source hashing {summary['hashed_bytes']:,} bytes tak bounded thi; large/cap-excluded files ko missing nahi kaha.

Six existing research documents **77,142 bytes** ke hain, fresh hashes purane evidence se match hue. In ki duplicate copy nahi banayi. Five Markdown documents ke key sections aur complete bytes inspect hue; SOURCE_REGISTER ke tamam 52 records parse hue, selected source claims semantically inspect hue. Current financial facts ko web par revalidate nahi kiya; dates/VERIFIED labels historical author assertions hain.

## Yeh export kis liye hai aur YIOS mein kya already hai?

Pichlay accessible JSONL census ke mutabiq yeh multi-ref research, datasets aur recovery representations ka historical collection hai. Yeh ek clean new competitor dataset ya nayi canonical database nahi. Original master report/SUMMARY abhi unreadable hain, is liye exact export-generation intent/content independently certify nahi hua.

Pichlay audit ne 9,011 source versions mein **8,335** exact-published Git blob matches aur **8,558** combined local/Git matches establish kiye the. Unki observation/evidence authority purani hi hai; is run mein bulk object comparison repeat nahi hua. Aaj read-only ls-remote se 40 published branch tips refresh hue. Main `08e719264e31ecd82de24f8eeb8f065c08359fe5`, Finance `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff`, aur What If `badec432bbf5610748123b3f0e0bcb9cdb25fa10` par hain. Main aur branch publication alag cheezen hain. Individual old matches ke liye prior crosswalk ka remote_ref/remote_commit dekhein; old branch tip reachability ko universal current main integration na samjhein.

Registry se absent 1,239 video IDs aur 871 channel IDs ki published source-byte occurrence pehle prove thi. Is run mein woh record/semantic comparison repeat nahi hua. Unhen nayi missing-from-repository knowledge na kahen.

18 naye local matches channel-data DS-000020/21/23/24/25/27/28/30 combined CSV/JSON/XLSX, DS-000022 NickInvests transcript ZIP, DS-000021/24 raw actor JSON, aur DS-000003 screenshot mein hain. Exact paths/hashes `UNRESOLVED_SOURCE_VERSION_RECHECK.csv` mein hain. Local match se GitHub ya independent private backup prove nahi hota; archive ZIP ka hash member validation nahi hai.

## Original named files: exact access aur download decision

| Original file | Expected bytes | Actual original read? | Primary decision |
|---|---:|---|---|
'''
for r in rows:readme+=f"| `{r['name']}` | {r['expected_size']:,} | NO — dataless | NEEDS_FURTHER_VERIFICATION; preserve |\n"
readme+=f'''
In sab ke exact paths, historical hash authority aur current metadata `TARGETED_RECOVERY_STATUS.csv` mein hain. Historical SHA-256 ko current recovered-byte SHA-256 nahi kaha. Existing inventory mein named-file candidates target ki historical observations the; unrelated SUMMARY/manifests ko equivalent nahi maana. Koi independently verified resident equivalent establish nahi hua.

**Agli targeted request ki priority recommendation:** sirf seven controls (master report, SUMMARY, SOURCE_INDEX, SHA256_MANIFEST, conflicts, checkpoints, LFS recovery) ko explicitly select karein: **{controltotal:,} bytes ({controltotal/1e6:.2f} MB)**. Yeh 30 MB ke andar hain, magar is oversized ten-file request ka partial transfer is run mein nahi kiya. RESEARCH_FILES_INVENTORY alag {next(r['expected_size'] for r in rows if r['name']=='RESEARCH_FILES_INVENTORY.csv'):,} bytes hai; seven controls ke saath budget cross hota hai. ALL_VIDEOS aur ALL_CHANNELS har ek akelay bhi 30 MB se baray hain. Unke liye existing verified resident equivalent, owner-created bounded export, ya separately approved larger selective budget chahiye. No recursive hydration.

## Six existing documents: exact future integration decision

Source/destination parent: `{R}/research/casually-finance-script-intelligence/`. Proposed Git destination har file ka **existing exact relative path** hai; dobara copy nahi karni.

| File | Actual bytes | Usefulness and historical limit | Future decision |
|---|---:|---|---|
'''
for d in dec:readme+=f"| `{pathlib.Path(d['source_path']).name}` | {d['bytes']:,} | {d['purpose']}. {d['usefulness']} | {d['conditions']} |\n"
readme+='''
Five Markdown research documents use snapshot dates Oct 11–14, 2026. TRANSCRIPT_COVERAGE's 16/206 and six-Short scope is historical, not today's authoritative Finance coverage. SCRIPT_DNA's short excerpt/paraphrase practice and originality claim are documented practices, not an independently proven licence. SOURCE_REGISTER records sources and claims, not redistribution permission. External URLs were not fetched/revalidated here. Retain attribution; do not copy competitor narration/media into new scripts or claim an open licence. Review any third-party excerpts, source access rights and sensitive local paths before later publication. The repository is private according to prior authenticated evidence; no access/permission change was made.

Recommendation: preserve all six at current paths and consider future tracking in the existing private repository after the existing owner review. Prior comparison did not prove an exact published equivalent; no fresh remote blob absence census occurred here. Main vs unmerged publication evidence remains explicitly limited. TOPIC_RESEARCH and FINAL_SHORT_SCRIPT can be tracked as dated research/drafts, but their current-news claims and forward cue must be rechecked before production. Do not convert editorial scores into a trained virality model or performance associations into causal rules.

YIOS use: coverage document gates confidence; SOURCE_REGISTER links claims and dependencies; TITLE_DNA supplies packaging hypotheses; SCRIPT_DNA supplies original hook/story structures; TOPIC_RESEARCH preserves dated editorial reasoning; FINAL_SHORT_SCRIPT is a draft example awaiting approval. No new database/authority or automatic channel automation is recommended by this task.

## Kya genuinely missing hai, kya separate rehna chahiye?

Abhi koi new unique useful original population establish nahi hua. Six documents already local hain; unki proven independent publication/recovery coverage is audit mein establish nahi hui. 435 unresolved historical versions ko missing/lost nahi kaha ja sakta. Manifest/source-index access ke baghair source-version lineage, complete top-level CSV schemas, historical row conflicts aur exact newly unique findings resolve nahi hue.

Large JSONL export, original gzip containers, recovered objects, large CSV exports aur private binary/source material private external preservation mein rakhein. Repo mein later approved small dated research/indexes fit ho sakte hain; huge exports ka second canonical copy na banayein. Neither a source-hash label nor metadata-only cloud entry proves original bytes recoverable. Private Drive copies were not queried/downloaded/reverified in this continuation; no new backup coverage credit awarded.

**Cleanup: zero files certified safe for manual removal.** Original content, dependency closure and independent recovery proof abhi incomplete hain. No destructive commands supplied.

## Safety, Git capability aur protected ownership

Installed Git: 2.50.1 (Apple Git-155). `/usr/bin/git` launcher mein env string absent thi; `xcrun --find git` resolved `/Applications/Xcode.app/Contents/Developer/usr/bin/git`, jis binary mein `GIT_NO_LAZY_FETCH` do martaba present hai. Har Git subprocess mein GIT_NO_LAZY_FETCH=1, GIT_NO_REPLACE_OBJECTS=1, GIT_TERMINAL_PROMPT=0, GIT_OPTIONAL_LOCKS=0 aur remote.origin.promisor=false use hua. Is run mein object-reading commands nahi hue; status/ref metadata aur explicit read-only ls-remote hua. Missing object fetch fallback nahi use hua.

Pichlay incident mein implicit Git downloads/object-store writes rule-out nahi ho sakte; original incident receipt aur validation FAIL unchanged hain. Is run mein Git checkout/status/HEAD/worktree/stash snapshots compare hue; result validation mein hai. These checks do not certify all other owners' concurrent activity or global object-store immutability. Active session process-name evidence captured; no protected session interrupted, no production/Finance ownership assumed. Machine B Finance and designated forensic session remain protected. No repo writes/staging/commit/push, no Drive operations, no source script execution or deletion. Only external audit artifacts written.

Latest usage 28% five-hour / 60% weekly; paid balance 0, two reset credits available, none redeemed. Memory pressure and disk evidence `FINAL_RESOURCES.json`; exact context meter unavailable. Backup config observed PAUSED; not restarted. No selected-file hydration/metadata change observed relative to prior metadata; automatic unrelated OS cloud activity is not globally certified.

## Evidence / owner decisions

- Prior audit: `/Users/ghilmankhan/YIOS-research-export-decision-20261027T184321Z` — unchanged, sealed checksum revalidation supplied.
- `TARGETED_RECOVERY_STATUS.csv`: ten original paths, current metadata, historical hashes and zero-download status.
- `UNRESOLVED_SOURCE_VERSION_RECHECK.csv`: all 453 source-version rows, exact current hashes, bounded exclusions and lineage uncertainty.
- `EXACT_INTEGRATION_DECISIONS.csv` / `SIX_DOCUMENT_VERIFICATION.json`: six existing paths, current SHA-256, purpose, rights/ownership conditions.
- `LIVE_REMOTE_HEADS.txt`: fresh published tips only; no fetch or main integration inference.
- `VALIDATION.json` and `SHA256SUMS`: this revision's validation and seal.

Owner ki next choice: seven named controls ka narrower <=30 MB selective recovery scope, ya large CSVs ke liye separate budget/equivalent request; phir exact unique-content decision. Six documents ki future private Git tracking separately approve karein, existing writers se coordinate karke. Production financial claims require a separately scoped revalidation. No integration approval inferred. Task stops here; no next folder, backup or Finance audit.
'''
(O/'YIOS_RESEARCH_EXPORT_FOLDER_DECISION_REPORT_REVISED.md').write_text(readme)
(O/'CONTINUATION_HANDOFF.md').write_text(f'''# Targeted recovery handoff — 2026-10-28
Status PARTIAL_DOWNLOAD_SCOPE_EXCEEDS_BUDGET. No selected original recovered/read. Ten files {total} bytes >30000000; no partial transfer. Proposed future explicit seven-control scope {controltotal} bytes. No uploads/integration/deletion authorized. 453 unresolved versions rechecked:18 fresh local exact;7 current differing;428 unresolved. Remaining unresolved exported versions435; not missing-file count. Six existing documents77142bytes unchanged hashes; no duplicate copy, current claims unvalidated. Prior audit55checksums retained; prior lazy-fetch incident and FAIL preserved. All Git commands NO_LAZY_FETCH=1; resolved Xcode Git2.50.1 binary contains support; promisor=false defense; no object operations or fetch. Fresh40remote head metadata. See revised report, decision CSV and VALIDATION. Do not automatically hydrate proposed subset or start any next scope.\n''')
validation={'status':'PARTIAL_DOWNLOAD_SCOPE_EXCEEDS_BUDGET','date':'2026-10-28','selected_files':10,'selected_expected_bytes':total,'download_cap_bytes':30_000_000,'new_download_bytes':0,'recovered_originals':0,'proposed_seven_controls_bytes':controltotal,'prior_files_checksum_verified':len(checks),'prior_checksum_all_pass':all(x['pass'] for x in checks),'prior_validation_preserved':True,'prior_git_incident_preserved':True,'git_before_after_same':all(x['matches_before'] for x in after),'selected_metadata_matches_prior':all(r['metadata_matches_prior'] for r in rows),'six_complete_hashes_match_prior':all(x['matches_prior'] and x['stable'] for x in six),'unresolved_recheck':summary,'remaining_unresolved_exported_versions':435,'automation_observed_paused':paused,'disk_reserve_pass':resources['free_disk_bytes']>=5_000_000_000,'no_download_initiated':True,'no_cloud_mutation':True,'no_integration_or_source_write':True,'scope_limitations':['No originals in ten-file selection read','No new manifests recovered','No global remote absence or private backup verification','No full folder census repeated','No full Git object database pre/post comparison','Current financial claims and source rights not independently validated']}
(O/'VALIDATION.json').write_text(json.dumps(validation,indent=2));print(json.dumps(validation,indent=2))
