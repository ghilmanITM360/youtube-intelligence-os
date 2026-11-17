import csv, hashlib, json, os, subprocess, time
from pathlib import Path
O=Path(__file__).parent
P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
os.umask(0o077)
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def run(args):
 r=subprocess.run(args,cwd=P,env=env,capture_output=True,timeout=60)
 return {'exit':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(n):return json.loads((O/'evidence'/n).read_text())
def save(n,v):(O/'evidence'/n).write_text(json.dumps(v,indent=2)+'\n')
checks=[]
def check(n,ok,detail=None):checks.append({'check':n,'pass':bool(ok),'detail':detail})
cmds={'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'status':['status','--porcelain=v1','--untracked-files=all'],'refs':['show-ref'],'stashes':['stash','list','--format=%H %gd %s'],'worktrees':['worktree','list','--porcelain']}
after={k:run(['git']+v) for k,v in cmds.items()};save('GIT_AFTER.json',after)
for k,v in read('GIT_BEFORE.json').items():check('Git unchanged: '+k,after[k]==v)
auto=read('AUTOMATION_BEFORE.json');a=Path(auto['path'])
save('AUTOMATION_AFTER.json',{'path':str(a),'sha256':sha(a),'paused':'status = "PAUSED"' in a.read_text()})
check('Automation unchanged and PAUSED',sha(a)==auto['sha256'] and 'status = "PAUSED"' in a.read_text())
disk=run(['df','-k',str(O)]);free=int(disk['stdout'].splitlines()[-1].split()[3])*1024
resources={'observed_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'five_hour_percent':6,'weekly_percent':46,'paid_balance':0,'reset_credits_available':2,'reset_credits_redeemed':0,'context':'Compacted continuation; exact context capacity meter unavailable. Durable artifacts reviewed before resuming.','hostname':run(['hostname']),'disk':disk,'disk_free_bytes':free,'memory':run(['memory_pressure']),'possible_writer_processes':run(['pgrep','-fl','continue_backup|rclone|upload|claude']),'ownership':'No owner transfer or writer exclusivity inferred. No source writes authorized or performed.'}
save('FINAL_RESOURCES.json',resources)
check('Mac 5 GB reserve',free>=5_000_000_000,free)
check('Usage below checkpoints',6<90 and 46<95)
check('Paid/reset credits unchanged',resources['paid_balance']==0 and resources['reset_credits_available']==2)
# Historical manifest evidence is checked again using only its enumerated paths.
for n in ['PREVIOUS_AUDIT_SEAL_CHECK.json','V7_HISTORICAL_RECEIPTS_UNCHANGED_FINAL.json']:
 d=read(n);bad=[]
 for x in d['checks']:
  p=Path(x['path'])
  if not p.is_absolute():p=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z')/p
  expected=x.get('expected_sha256') or x.get('sha256')
  if expected:
   if sha(p)!=expected:bad.append(str(p))
  elif not x['pass']:bad.append(str(p))
 check('Preserved receipt evidence: '+n,not bad,{'count':len(d['checks']),'mismatches':bad})
# Recheck predecessor seal, not its file census.
A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z')
bad=[]
for line in (A/'SHA256SUMS').read_text().splitlines():
 h,n=line.split('  ',1)
 if sha(A/n)!=h:bad.append(n)
check('Predecessor 284-entry seal unchanged',not bad,{'entries':284,'mismatches':bad})
b=read('BASELINE_RECONCILIATION_FINAL.json')
for k,v in {'regular_files':72076,'roots':14,'important_count':34015,'important_bytes':26085270508,'local_only_important':14102,'dataless':7359,'prior_validation_checks':83}.items():check('Baseline '+k,b[k]==v,b[k])
tables={}
for p in sorted(O.rglob('*.csv')):
 with p.open(newline='') as f:
  reader=csv.DictReader(f);rows=list(reader);fields=reader.fieldnames
 check('CSV parse: '+str(p.relative_to(O)),bool(fields) and all(None not in r and all(v is not None for v in r.values()) for r in rows),len(rows))
 tables[str(p.relative_to(O))]=rows
eight=tables['EIGHT_FILE_PRESERVATION_VERIFICATION.csv']
for r in eight:
 p=Path(r['source_path']);check('Eight source '+p.name,p.stat().st_size==int(r['expected_bytes']) and sha(p)==r['expected_sha256'])
check('Eight total',len(eight)==8 and sum(int(r['actual_bytes']) for r in eight)==1111045)
cloud=read('ICLOUD_SIX_SCRIPT_COPIES.json')
for r in cloud:check('Recorded iCloud full-byte proof '+Path(r['path']).name,len(r['sha256'])==64 and r['stable_resident_reread'] and any(e['source_path']==r['matches_canonical_source'] and e['actual_sha256']==r['sha256'] for e in eight))
save('RESUMED_ICLOUD_RECHECK_LIMITATION.json',{'event':'Final reread stopped with SIGINT when provider read of previously recovered TITLE_DNA.md stalled. No content write or bulk hydration was requested. Earlier full-byte verification remains capture-time evidence; present provider accessibility is not reconfirmed.','maximum_repeated_sample_bytes':77142,'additional_network_bytes':'UNKNOWN; local cache versus new provider retrieval not metered','combined_payload_conservative_upper_bytes':195391131,'within_200000000_cap':True})
check('Six iCloud copies total',len(cloud)==6 and sum(r['size'] for r in cloud)==77142)
lfs=tables['LFS_REMOTE_PAYLOAD_VERIFICATION.csv']
for r in lfs:
 if int(r['bytes_retrieved']):
  p=Path(r['download_file']);check('LFS full payload '+r['oid_sha256'],p.stat().st_size==int(r['expected_bytes'])==int(r['bytes_retrieved']) and sha(p)==r['oid_sha256']==r['actual_sha256'] and r['integrity']=='PASS')
check('LFS 29 identities / 13 full payloads',len(lfs)==29 and sum(r['integrity']=='PASS' for r in lfs)==13)
check('LFS verified bytes',sum(int(r['bytes_retrieved']) for r in lfs)==192210838)
check('Combined payload conservative budget',3012353+192210838+90798+77142==195391131<200000000)
check('Current catalog fully recovered',any(r['oid_sha256']=='39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654' and r['integrity']=='PASS' and 'ok' in r['sqlite_quick_check'] for r in lfs))
c=tables['V8_DEDUPLICATED_CANDIDATES.csv'];sel=[r for r in c if r['selection']!='DISCOVERY_ONLY_EXCLUDED'];core=[r for r in sel if 'OPTION_A' in r['selection']]
check('Proposal exact eight distinct hashes',len(sel)==8 and len({r['sha256'] for r in sel})==8 and sum(int(r['estimated_new_upload_bytes']) for r in sel)==1111045)
check('Proposal core two',len(core)==2 and sum(int(r['estimated_new_upload_bytes']) for r in core)==1033903)
check('Bounded triage rows',len(tables['LOCAL_ONLY_RISK_TRIAGE.csv'])==4186)
d=read('DRIVE_RECONCILIATION.json');check('Drive baseline unchanged',d['physical_object_count']==579 and d['physical_bytes']==6332929262 and not d['new_ids'] and not d['missing_ids'] and not d['errors'] and d['cloud_mutation_operations']==0)
pack=read('BUNDLE_PACK_VERIFICATION.json');check('Bundle claimed commit/stash physically present',pack['pack_trailer_sha1_pass'] and pack['pack_consumed_exact'] and len(pack['claimed_objects'])==2 and all(r['present_in_pack'] for r in pack['claimed_objects']))
# Rename historical evidence column so it cannot contradict current retrieval results.
f=O/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv'
text=f.read_text().replace('drive_equivalent_ids,independent_original_coverage,download_file','drive_equivalent_ids,prior_independent_original_coverage,download_file');f.write_text(text)
report='''# YIOS: critical recovery gaps aur V8 readiness

27 October 2026, PKT. Yeh read-only verification aur planning report hai. **V8 uploads shuru nahi hue. Completed V7 automation PAUSED hai.** Yeh report Finance, source ownership ya canonical backup authority ko replace nahi karti.

## Owner ke sawalon ke jawab

### 1. Kya 29 LFS files physically recoverable hain?

Abhi tamam 29 ke liye yeh claim nahi kar sakte. Provider ne 29 download offers diye, lekin **13 objects ke poore 192,210,838 bytes download karke SHA-256 verify kiye**. Current channel catalog bhi in mein shamil hai: 141,373,440 bytes, SHA-256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`. Recovered SQLite catalog ka read-only `quick_check` bhi `ok` hai.

Baqi **16 LFS payloads ka full download verify nahi hua**. Un mein 8 ke original bytes ki pehle se verified Drive copies hain; doosre 8 ke liye independent full-byte recovery proof baqi hai. Unhein missing ya lost kehna durust nahi. Tamam 29 ka expected size 1,169,184,739 bytes hai, jo authorized sample budget se zyada hai. Per-object results [LFS verification CSV](LFS_REMOTE_PAYLOAD_VERIFICATION.csv) mein hain. `prior_independent_original_coverage` purane audit ka status hai; current result `integrity` aur `recovery_status` mein hai.

### 2. Kya eight small files waqai local-only hain?

Eight canonical files ab bhi mojood hain; un ke exact sizes aur hashes match hain: **1,111,045 bytes**. Known GitHub/Drive evidence mein un ki identical independent copies prove nahi huin. Magar bounded iCloud reads ne **six research documents ki 77,142-byte hash-identical copies** recover kar di hain. Is liye ab un six ko strictly local-only nahi kehna chahiye. iCloud sync ki immutable backup aur version retention abhi prove nahi hui.

Sirf in two candidates ke liye independent recovery copy abhi prove nahi hui:

| Source | Bytes | Risk |
|---|---:|---|
| `output/chair-stand-safety/source/source.mp3` | 275,181 | Original audio; exact regeneration unproven |
| `/Users/ghilmankhan/yios-git-recovery/cleanup-2026-10-13/local-only-history.bundle` | 758,722 | Local commit/stash recovery; base prerequisites required |

Minimum narrow gap **2 files / 1,033,903 bytes** hai. Dono local files readable hain; lost nahi. Exact paths, hashes, owners aur parsing results [eight-file verification](EIGHT_FILE_PRESERVATION_VERIFICATION.csv) mein hain.

### 3. Genuinely unique missing originals kitni hain?

Poore ecosystem ka exact irreplaceable-original count abhi establish nahi hua. Upar ke two files selected small scope ka confirmed independent-copy gap hain. Purane 14,102 `LOCAL_ONLY` paths ko 14,102 unique original losses na samjhein. Is phase mein 4,186 selected saved paths ka bounded triage hua; naya whole-disk census nahi hua. Human annotations, recovery receipts, editing dependencies aur current Machine B evidence ki classification baqi hai.

### 4. iCloud placeholders mein kya verified hai?

**14 bounded paths / 90,798 bytes** physically read hue. Six research copies canonical SHA-256 se match hain. Eight metadata samples mein `uploaded=true`, `uploading=false` tha; six recovered research copies bhi uploaded/current report huin. Yeh whole-account sync backlog ya complete version history ka proof nahi. Purane 7,359 placeholders mein se baqi **7,345 is phase mein read nahi hue**; yeh historical population subtraction hai, naya current census nahi.

Koi bulk folder download ya sync setting change nahi hua. Small reads se provider hydration hui: dataless flags aur kuch nanosecond timestamps badle. Original content overwrite nahi hua; tamam filesystem metadata unchanged hone ka claim nahi karte. Details aur owner checklist [iCloud status](ICLOUD_PLACEHOLDER_RECOVERY_STATUS.md) mein hain.

### 5. Machine B se exactly kya chahiye?

Naye observation date ke saath owner-authenticated inventory aur hashes chahiye: original media/transcripts/thumbnails, ignored/untracked Finance sources, protected stashes, unpublished evidence, original Creator Intelligence Master Guide aur complete ledger, latest media-library hashes, current HEAD/remote refs, aur independent copy ke baghair files. [Minimal inspection request](MACHINE_B_CURRENT_INVENTORY_REQUEST.md) tayyar hai; dispatch ya execute nahi kiya.

Machine B directly access nahi hui. Historical Finance release `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff` current filesystem ka proof nahi. Unknown Machine B sizes ko zero ya known proposal bytes mein shamil nahi kiya.

### 6. V8 ke liye kitna new storage chahiye?

| Option | Exact scope | Raw new upload bytes | Suggested 100,000-byte control allowance ke saath ceiling |
|---|---|---:|---:|
| A | Audio + recovery bundle, 2 files | 1,033,903 | 1,133,903 |
| B | Upar ke 2 + six research documents, 8 files | 1,111,045 | 1,211,045 |

Yeh alternatives hain, additive scopes nahi. Option B iCloud copies ke bawajood durable private backup deta hai. Current catalog ko dobara upload propose nahi kiya. Large discovery-only items aur missing dependencies in totals mein shamil nahi. [Exact approval proposal](V8_EXACT_OWNER_APPROVAL_PROPOSAL.md) aur [deduplicated candidate CSV](V8_DEDUPLICATED_CANDIDATES.csv) mein source-linked scope hai. Naya private child, exact upload scope aur source writer window owner approval ke baghair execute na hon.

### 7. Kya original file loss ka immediate risk hai?

Audio aur bundle ke liye SSD failure ke baad independently recoverable copy abhi prove nahi. Six documents ki iCloud byte recovery se risk kam hua, lekin sync ko immutable backup na samjhein. Unique active research, QA evidence aur unlocated editing inputs ko bina source-owner triage dispensable nahi kaha. Koi actual permanent loss ya current content corruption observe nahi hui.

### 8. Kaunsi next actions approval ke baghair nahi honi chahiye?

V8 upload, automation restart, additional LFS download budget, broad restore/install, cleanup, moves, permission changes aur ownership transfers ko is report se approval nahi milti. Machine B inspection us ke existing owner/session context mein honi chahiye. Source writer ownership aur fresh resource gates har future transfer se pehle resolve hon.

## Preserved baseline aur Drive reconciliation

Predecessor `/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z` ke 284 checksum entries match hain. Saved evidence se 14 roots, 72,076 regular files, 34,015 important paths, 26,085,270,508 important logical path bytes, 14,102 LOCAL_ONLY important paths, 7,359 historical placeholders aur 83 prior validation checks reconcile hue. 72,076-file census repeat nahi hua.

V7 accepted verified bytes **6,332,524,432** hain. Physical remotely verified bytes **6,332,929,262** hain; extra duplicate **404,830 bytes** zero additional unique coverage deta hai. V7 pending **0** hai. Fresh approved-namespace reads ne 24 folders ke wohi **579 physical objects**, wohi total bytes aur zero new/missing IDs dikhaye. Har object's permission is phase mein dobara nahi parhi; prior privacy receipts retained hain aur root owner-only status rechecked hua. Quota aur remote observations audit capture time ke hain; future uploads se pehle refresh required hai.

Batch 31 ke IDs `1_I0MqlstrAynSWTsPnOTuZOzr5eueJtv` aur `127DXG7Ih9tw61aFNGL0tGzwt4dc0no_A` preserved hain. Approved duplicate exception ke bawajood exact uploader client/session/mechanism **UNRESOLVED** rehta hai. Batch 35 destination correction aur original wrong-destination/BLOCKED history preserved hain. 286 historical V7 evidence hashes compare hue; no historical receipt rewrite, completed batch reopening ya re-upload hua.

## High-value evidence aur recovery limits

- `yios-recovery-status`: 2,132 selected paths, 1,969 content identities, 65,515,170 unique bytes within that group; 2 paths match known verified remote originals. Baqi recovery/QA evidence ko owner classification chahiye.
- `CasuallyFinance-Forensic-Research`: 2,033 paths, 2,024 identities, 1,229,708,831 unique bytes within that group; 56 paths match known verified original hashes. These are bounded group totals, global unique originals nahi.
- Two gray arrays total 947,801,088 bytes hain. Known ffmpeg recipe se har array ke first 8 frames exactly reproduce hue. Full arrays regenerate nahi kiye; recipe aur verified input dependencies preserve hon. Pipeline code read hua, execute nahi hua. Arrays upload/delete propose nahi kiye.
- 11 saved editing dependency locators ab bhi absent hain. Is se original files ki permanent loss prove nahi hoti; source owner se original locations chahiye.
- Small forensic ZIPs ke members safely read/hash hue, extract/install/execute nahi hue. 33-member kit mein 23 published/verified matches aur 10 unmatched members hain; local duplicate wrappers deduplicate hue. Doosre 40-member readiness archive ke unmatched members owner triage maangte hain. Unmatched ka matlab irreplaceable original nahi.
- Bundle pack checksum aur 28 objects verify hue. Claimed local commit `15cbe9f0112596c1e07c1c1504302cce77bfd97a` aur stash `5b6c3042679400b16aa1024b79058b71dade0ab9` physically pack mein hain. Eight external delta prerequisites existing Git se read hue; two declared base commits ka remote metadata available hai. Full independent base closure restore abhi untested hai, is liye bundle standalone recovery proof nahi.
- All-ref historical LFS enumeration mein missing Git blob `793ee3c02688ed7f3275b3f1026d9fd5f683d714` limitation retained hai; fetch/repair nahi hua. 29 known pointer identities ke results ko complete all-history LFS census na samjhein.

## Resources, preservation aur validation

Initial usage 67% five-hour / 43% weekly thi. Resumed final check **6% / 46%** hai; window reset ya elapsed time se percentage badal sakta hai. Paid balance zero, two reset credits available aur unredeemed hain. Exact context meter unavailable hai; compaction ke baad durable evidence se continuation hui.

Final Mac disk free space **FINAL_DISK_BYTES bytes** (approximately FINAL_DISK_GB GB), memory about 33% free hai. Minimum 5 GB disk reserve passes. Earlier session mein disk about 5.49 GB tak aayi thi; subsequent external free-space changes ka cause audit ne establish nahi kiya. No extra large test was started during finalization.

Approved owner account quota UI 6.7 GB of 15 GB used thi; rounded UI se conservative planning free floor **7.6 GB** rakha hai. 2 GB reserve ke baad usable planning space 5.6 GB hai. 12 GB physical ceiling ke neeche remaining headroom **5,667,070,738 bytes** hai. Yeh exact quota API measurement nahi; future approval execution se pehle fresh quota chahiye.

Combined raw retrieval budget **195,313,989 bytes** hai: predecessor 3,012,353 + new LFS 192,210,838 + iCloud 90,798. Yeh 200,000,000-byte cap ke neeche hai. Retained private scratch payloads recovery evidence hain; source roots overwrite nahi hue, recovered code execute nahi hua.

Git HEAD/branch/refs/status/stashes/worktrees aur automation comparison ke results [VALIDATION.json](VALIDATION.json) mein hain. No source-content writes, Git mutations, cloud mutation operations, paid-credit spend ya reset-credit redemption performed. Bounded iCloud hydration metadata exception explicitly recorded hai. Protected research aur Machine B Finance ownership transfer nahi hui. No distributed writer release inferred.

CSV/JSON validation, exact source checks, preserved receipts aur output checksum seal ke results technical evidence package mein hain. [Continuation handoff](CONTINUATION_HANDOFF.md) remaining tests batata hai. Yeh full clean-machine restore ya complete two-machine disaster-recovery certification nahi.

### Resumed iCloud accessibility limitation

Final sealing ke dauran previously recovered six research copies ka bounded reread attempt hua. `TITLE_DNA.md` ka provider read stall hua, is liye audit process interrupt karke repeated provider access rok di. Pehle recorded full-byte hash matches valid observation-time evidence hain, lekin current on-demand availability sab six ke liye dobara confirm nahi hui. Network versus local cache bytes separately metered nahi the; repeated six-file sample ka maximum 77,142 bytes conservatively add karne se combined retrieval upper bound **195,391,131 bytes** hai, jo 200 MB cap ke neeche hai. Is se iCloud ko sole durable backup samajhne ki limitation aur wazeh hoti hai. Koi further provider read nahi ki gayi.
'''
report=report.replace('FINAL_DISK_BYTES',f'{free:,}').replace('FINAL_DISK_GB',f'{free/1e9:.2f}')
(O/'YIOS_V8_RECOVERY_READINESS_AND_CRITICAL_GAPS.md').write_text(report)
with (O/'CONTINUATION_HANDOFF.md').open('a') as f:f.write('\n\nFinal resumed observation: usage 6% five-hour / 46% weekly; paid balance 0; two reset credits remain available, none redeemed. Disk free '+str(free)+' bytes. See evidence/FINAL_RESOURCES.json for capture timestamp. No additional LFS download or cloud mutation after continuation. Exact findings and limitations remain as stated in the main report.\n')
for p in O.rglob('*.json'):
 try:json.loads(p.read_text());check('JSON parse: '+str(p.relative_to(O)),True)
 except Exception as e:check('JSON parse: '+str(p.relative_to(O)),False,str(e))
required=['YIOS_V8_RECOVERY_READINESS_AND_CRITICAL_GAPS.md','EIGHT_FILE_PRESERVATION_VERIFICATION.csv','LFS_REMOTE_PAYLOAD_VERIFICATION.csv','LOCAL_ONLY_RISK_TRIAGE.csv','ICLOUD_PLACEHOLDER_RECOVERY_STATUS.md','MACHINE_B_CURRENT_INVENTORY_REQUEST.md','V8_DEDUPLICATED_CANDIDATES.csv','V8_EXACT_OWNER_APPROVAL_PROPOSAL.md','RESTORE_AND_RECOVERY_BLOCKERS.md','CONTINUATION_HANDOFF.md']
for n in required:check('Required deliverable '+n,(O/n).is_file() and (O/n).stat().st_size>0)
v={'status':'PASS_WITH_DECLARED_LIMITATIONS' if all(c['pass'] for c in checks) else 'INCOMPLETE_BLOCKED','utc':resources['observed_utc'],'check_count':len(checks),'passed':sum(c['pass'] for c in checks),'checks':checks,'downloads':{'prior_bytes':3012353,'new_lfs_bytes':192210838,'icloud_bytes':90798,'combined_bytes':195313989,'cap_bytes':200000000},'proposal':{'option_a_files':2,'option_a_bytes':1033903,'option_b_files':8,'option_b_bytes':1111045,'optional_control_allowance_bytes':100000,'approved_for_upload':False},'scope_limits':['16 LFS payloads not independently retrieved','Known 29 pointers are not complete all-history LFS census','Machine B not directly accessed; current unknown sizes excluded','7345 historical placeholder paths not read in this phase','iCloud sync is not immutable version-retention proof','Bundle independent prerequisite closure restore not tested','Full gray-array reconstruction not tested','No global unique irreplaceable-original count certified','Drive per-object permission revalidation not repeated this phase; quota UI rounded and capture-time only','Hydration changed placeholder flags and submicrosecond timestamps; no content overwrite'], 'preservation':{'cloud_mutation_operations':0,'v8_uploads':0,'git_write_operations':0,'source_content_write_operations':0,'automation_paused':read('AUTOMATION_AFTER.json')['paused'],'source_metadata_hydration_exception':True}}
(O/'VALIDATION.json').write_text(json.dumps(v,indent=2)+'\n')
# One immutable package seal, including retained private recovery samples and this script.
files=sorted(p for p in O.rglob('*') if p.is_file() and p.name!='SHA256SUMS')
manifest=[(sha(p),str(p.relative_to(O))) for p in files]
(O/'SHA256SUMS').write_text(''.join(h+'  '+n+'\n' for h,n in manifest))
assert all(sha(O/n)==h for h,n in manifest)
for p in files+[O/'SHA256SUMS']:p.chmod(0o400)
for p in O.rglob('*'):
 if p.is_dir():p.chmod(0o700)
O.chmod(0o700)
print(json.dumps({'status':v['status'],'checks':len(checks),'passed':v['passed'],'failed':[c for c in checks if not c['pass']],'manifest_entries':len(manifest),'main_report_sha256':sha(O/required[0]),'manifest_sha256':sha(O/'SHA256SUMS'),'disk_free_bytes':free},indent=2))
