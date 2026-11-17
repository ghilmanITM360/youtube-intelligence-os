import csv,json,os,hashlib,collections,datetime
O='/Users/ghilmankhan/YIOS-targeted-ssd-cleanup-20261029T0010PKT';R='/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd';M='/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'
source=list(csv.DictReader(open(O+'/TARGET_FILE_HASH_CROSSWALK.csv')));versions={x['path']:x for x in csv.DictReader(open(O+'/CF_PR21_VERSION_CROSSWALK.csv'))};wi={x['downloads_path']:x for x in csv.DictReader(open(O+'/WHAT_IF_RELATIVE_SHA_COMPARISON.csv')) if x['downloads_path']};dr={x['id']:x for x in csv.DictReader(open(O+'/V7_CURRENT_DRIVE_METADATA.csv'))};vm=json.load(open(M));obs={x['source']:x for x in vm['objects']};members=collections.defaultdict(list)
for m in vm['members']:members[m['remote_archive_id']].append(m)
archive_check=json.load(open('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/evidence/REMOTE_METADATA_AND_ARCHIVE_RECEIPT_RECONCILIATION.json'));archives={x['archive_source']:x for x in archive_check['archives']}
W={x['workprojects_path']:x for x in csv.DictReader(open(O+'/WHAT_IF_RELATIVE_SHA_COMPARISON.csv')) if x['workprojects_path']}
rows=[]
for x in source:
 p=x['path'];g=x['group'];a=int(x['allocated'] or 0);v=versions.get(p,{});o=obs.get(p,{});w=wi.get(p,{});cat='KEEP';reason='original, active, historical, or no complete recovery proof';replacement='';rest='NOT_TESTED';dep='active source or historical references';eq='NOT_ESTABLISHED';pot=0;ref=O+'/TARGET_FILE_HASH_CROSSWALK.csv';remote='';required='';role=''
 if g=='V7':
  if x['relative'].startswith('selected-evidence-packages-20261026/') and p.endswith('.tar.gz'):
   role='derived V7 archive wrapper';remote=o.get('remote_id','');replacement='private Drive V7 object '+remote;dep='batch receipts/manifests reference historical path; no active V7 backup process found';eq='EXACT_REMOTE_BYTES' if x['remote_match']=='True' else 'NO_REMOTE_MATCH'
   batch=o.get('batch','');receipt=o.get('verification_receipt','');rj=json.load(open(receipt)) if receipt and os.path.exists(receipt) else {};mm=members.get(remote,[]);ar=archives.get(p,{});current=dr.get(remote,{}).get('metadata_current_ok')=='true';passed=(batch in ('batch-0033','batch-0034','batch-0036') and x['remote_match']=='True' and o.get('status')=='VERIFIED' and rj.get('status')=='VERIFIED' and rj.get('uploaded_bytes')==rj.get('independently_retrieved_bytes') and current and bool(mm) and all(z.get('verification_status')=='COMPLETE_REMOTE_DECOMPRESSION_MEMBER_SHA256_VERIFIED' for z in mm) and ar.get('status')=='PASS')
   if passed:
    cat='MANUAL_DELETE_REVIEW';reason='local generated wrapper; source members retained, exact Drive object retrieved and member-verified; current remote metadata passed';rest='FULL_REMOTE_BYTE_RETRIEVAL_VERIFIED; representative 04035 materialized restore PASS';pot=a;ref=receipt+'; '+M+'; '+O+'/V7_CURRENT_DRIVE_METADATA.csv';required='Owner final review; keep manifests/receipts; restore from Drive by object ID if needed; APFS clone savings uncertain'
   else:
    cat='BLOCKED';reason='Batch35 historical exception or incomplete direct recovery proof';pot=a;required='Resolve Batch35 exception and test exact restore/dependencies';ref=receipt or M
  else:role='V7 receipt, manifest, checkpoint, or protected CT/Finance package';dep='historical recovery record or active project reference';required='Do not delete original incident/receipt evidence'
 elif g=='SHORTS':
  role='38 Shorts local forensic source/derived evidence';remote=x['remote_id'];replacement='V7 private Drive object/member '+remote if remote else '';eq='EXACT_REMOTE_BYTES' if x['remote_match']=='True' else 'NOT_MAPPED';dep='protected forensic research, 38 Shorts evidence';rest='historical retrieval/member verification, no full production restore';required='Keep active evidence and confirm source-owner handoff before local retirement'
 elif g=='WI_D':
  role='What If original/derived research in Downloads';dep='possible source path and CapCut/Brain dependencies';ww=w.get('workprojects_path','');replacement=ww;eq=w.get('verdict','NOT_ESTABLISHED');remote=W.get(ww,{}).get('remote_id','') if ww else ''
  if eq=='EXACT_COMMON':cat='BLOCKED';reason='byte-identical workprojects copy, but path use/full original restore not certified';pot=a;required='Verify active path dependency, original media recovery, APFS clone extents';ref=O+'/WHAT_IF_RELATIVE_SHA_COMPARISON.csv'
  else:required='Unique file or changed .DS_Store: preserve until authority reviewed'
 elif g=='WI_W':
  role='What If working source/Brain and production';remote=x['remote_id'];replacement='PR44 selected navigation; V7 private Drive mapping where exact';eq='EXACT_REMOTE_BYTES' if x['remote_match']=='True' else 'UNMAPPED';dep='active authoritative workprojects source';required='Keep working source'
 elif g=='CF':
  role='Casually Finance derived research, staging, or historical source';eq=v.get('comparison','NOT_IN_PR21_PATH');remote='PR21 043b85bf58f84fb6a1c8981d54e3b233faa6a928' if eq!='NOT_IN_PR21_PATH' else '';replacement='PR21 '+v.get('relative','') if eq=='EXACT_PR21' else ''
  if x['relative'].startswith('_work/'):
   cat='BLOCKED';reason='staging/cache appears derived but exact regeneration and source dependencies unproven';pot=a;required='Pinned script+input hash+sample exact rebuild and owner dependency check'
  elif eq=='EXACT_PR21':cat='BLOCKED';reason='exact Git blob, but local corpus internal references and source history must be retained';pot=a;required='Prove no local pipeline dependency; preserve version/source manifest'
  elif eq=='DIFFERENT_VERSION':reason='local historical version differs from PR21; not redundant';required='Preserve and compare meaning before any consolidation'
  else:required='Unique _pipeline/snapshot or staging; prove derivation and recoverability'
 rows.append({'Machine':'A','Exact absolute path':p,'Parent folder':os.path.dirname(p),'File role':role,'Size':x['size'],'Allocated storage':x['allocated'],'SHA-256':x['sha256'],'Canonical replacement':replacement,'Exact remote object or Git commit':remote,'Independent byte restoration result':rest,'Current dependencies':dep,'Version equality':eq,'APFS/hardlink/clone consideration':f"nlink={x['nlink']}; inode={x['inode']}; clone extent sharing unmeasured",'Actual potential SSD saving':pot,'KEEP / MANUAL_DELETE_REVIEW / BLOCKED':cat,'Evidence reference':ref,'Remaining verification required':required,'Reason':reason})
with open(O+'/YIOS_VERIFIED_DELETION_CANDIDATES.csv','w',newline='') as f:
 w=csv.DictWriter(f,rows[0].keys());w.writeheader();w.writerows(rows)
count=collections.Counter(x['KEEP / MANUAL_DELETE_REVIEW / BLOCKED'] for x in rows);eligible=[x for x in rows if x['KEEP / MANUAL_DELETE_REVIEW / BLOCKED']=='MANUAL_DELETE_REVIEW'];total=sum(int(x['Allocated storage']) for x in eligible);batches=collections.Counter(obs[x['Exact absolute path']]['batch'] for x in eligible)
val={'created_at':datetime.datetime.now().astimezone().isoformat(),'files_classified':len(rows),'counts':count,'eligible_allocated_upper_bound_bytes':total,'eligible_batches':batches,'eligible_all_remote_sha_verified':all(x['Version equality']=='EXACT_REMOTE_BYTES' for x in eligible),'source_files_changed':False}
with open(O+'/VALIDATION.json','w') as f:json.dump(val,f,indent=2)
def gib(n):return f'{n/2**30:.3f} GiB'
cf=[x for x in rows if x['Exact absolute path'].startswith('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/')];v7=[x for x in rows if x['Exact absolute path'].startswith(R+'/')];whatif=[x for x in rows if x['Exact absolute path'].startswith('/Users/ghilmankhan/Downloads/video data of what if/')];shorts=[x for x in rows if x['Exact absolute path'].startswith('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence/')]
potential_cf=sum(int(x['Allocated storage']) for x in cf if '/_work/' in x['Exact absolute path']);potential_wi=sum(int(x['Allocated storage']) for x in whatif if x['Version equality']=='EXACT_COMMON');potential_35=sum(int(x['Allocated storage']) for x in v7 if 'selected-evidence-packages-20261026/' in x['Exact absolute path'] and x['Exact remote object or Git commit'] and obs.get(x['Exact absolute path'],{}).get('batch')=='batch-0035');protected_short=sum(int(x['Allocated storage']) for x in shorts)
report=f'''# YIOS actual SSD cleanup plan — Machine A, 2026-10-29

## Faisla

**CERTIFIED ELIGIBLE:** {len(eligible)} V7 ke generated archive wrappers, {gib(total)} allocated blocks. Owner in exact paths ko manual deletion ke liye review kar sakta hai. **Koi file delete nahi hui.** APFS clone sharing measure nahi hui; actual space saving 0 se {gib(total)} tak ho sakti hai, guarantee nahi. `df` ka free space investigation ke baad alag measure kiya gaya hai. Machine B access nahi; uska saving **unknown**.

**POTENTIAL, abhi blocked:** CF `_work` {gib(potential_cf)}; What If Downloads ki {sum(x['Version equality']=='EXACT_COMMON' for x in whatif):,} exact common files {gib(potential_wi)}; V7 Batch 35 wrappers {gib(potential_35)}. Inhein certified total mein shamil nahi kiya. **PROTECTED:** 38 Shorts evidence {gib(protected_short)}; current source aur active forensics ka hissa hai.

## 1. Verified manual deletion shortlist

Sirf `YIOS_VERIFIED_DELETION_CANDIDATES.csv` ki **MANUAL_DELETE_REVIEW** rows. Ye {dict(batches)} ke selected V7 `.tar.gz` wrappers hain. Har row mein absolute path, SHA-256, Drive object ID, batch receipt aur allocated bytes hain. 33/33 local SHA V7 map se match; 33/33 current Drive metadata ID, name, size, owner matched; 33/33 batch receipts `VERIFIED` aur uploaded = independently retrieved bytes; 2,290 members remote decompression SHA verified; archive reconciliation `PASS`. `04035-forensic-JsK53moCyZA-part01.tar.gz` ko alag scratch mein physically restore karke full SHA/member check bhi pehle pass hua. Baqi objects ki full remote byte retrieval documented hai, magar har object ka separate on-disk restore nahi kiya gaya.

Yeh **sirf local generated wrappers** ki review hai; original Shorts arrays, frames, audio, V7 manifests, batch receipts, exception records aur Drive objects ko delete na karein. Historical receipts mein local wrapper paths rahenge; agar future recovery script ko same path chahiye, pehle remote object ID se us wrapper ko restore karna hoga. Repo ke current docs/code mein selected wrapper path dependency nahi mili; V7 backup process active nahi dikha. Source owner/active session ka protected forensic work untouched raha.

## 2. Blocked high-value cleanup, savings rank

| Rank | Exact group | Occupied blocks | Evidence found | Missing smallest safe check |
|---|---|---:|---|---|
| 1 | `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/_work` | {gib(potential_cf)} | 1,267 staging files; two `gray.u8` alone ~0.88 GiB. PR21 excludes `_work`. | Pin script/input hashes; exact bounded regeneration of representative streams; owner confirms no active stage references. |
| 2 | `/Users/ghilmankhan/Downloads/video data of what if` exact common children | {gib(potential_wi)} | 2,467 same relative paths and exact SHA in workprojects. Four Downloads-only files and one changed `.DS_Store` remain. | Confirm CapCut/Brain/source path use; verify original video backup and restore for representative media; APFS clone sharing. No whole-folder deletion. |
| 3 | V7 `selected-evidence-packages-20261026` Batch 35 wrappers | {gib(potential_35)} | Local SHA/remote map match, but Batch 35 historical exceptions remain. | Reconcile exception/dedup identities and direct restore before any review. |

## 3. Four target folders: actual evidence

**Casually Finance derived folder:** {len(cf):,} files fully hashed. PR21 tree comparison: {sum(x['Version equality']=='EXACT_PR21' for x in cf)} exact blobs, {sum(x['Version equality']=='DIFFERENT_VERSION' for x in cf)} changed historical versions, {sum(x['Version equality']=='NOT_IN_PR21_PATH' for x in cf)} absent from matching PR21 path. Local deep report 6,538 characters versus PR21 report 29,404; same first five section headings, later PR21 adds QA/primary-source research; local text also differs inside old sections. Is liye older report ko disposable nahi kaha. Local-only `_pipeline` scripts, metadata snapshot aur `_work` ko provenance/derivation proof tak rakhein. Koi new small file is pass mein publish nahi ki gayi: 51 changed versions ko current PR21 se automatically overwrite ya merge karna evidence-safe nahi.

**V7 local audit folder:** {len(v7):,} files fully hashed. 57 direct remote objects match; 53 selected wrappers mein se 33 review eligible, 20 Batch 35 hold. 3 CT packages (Video 003 samet), Finance publication package, receipts, member manifests aur incident history protected. Batch 31/35 exceptions preserved.

**What If:** Downloads {len(whatif):,}, workprojects {sum(x['Machine']=='A' and x['Exact absolute path'].startswith('/Users/ghilmankhan/workprojects/video data of what if/') for x in rows):,} files. 2,467 exact common; 4 Downloads-only (3 generated PNG, workbook); 409 workprojects-only; `.DS_Store` differs. Workprojects Brain/source remains authority, PR44 selected navigation published, full originals ko PR44 coverage mat samjhein. Exact file list `WHAT_IF_RELATIVE_SHA_COMPARISON.csv` mein.

**38 Shorts:** {len(shorts)} files fully hashed; 392/393 V7 map exact, last `.DS_Store` unmapped. Full 4.15 GiB **protected**, even when remote backup matches: forensic pipeline/source-owner and full recovery obligations remain.

## 4. Single authority, Git, private originals

Current main YIOS repo/PR21/PR36/PR44 mein koi source change is investigation mein nahi hua. Casually Finance navigation pehle hi `f4dc5d14d6ad03c1edd92e48fac779e7a8555fc5` par publish hai. PR21 `043b85bf58f84fb6a1c8981d54e3b233faa6a928`, PR44 `f345abdef43d54ebde98251cfa4fafb6403c52be`. Finance PR36 ka writer Machine B hai; uske 1,612 records untouched. Original MP4, audio, frames, arrays, CapCut source aur active Video 003 external/private storage mein rakhein. Git pointers ya summary ko media recovery mat samjhein.

## 5. Owner ke liye next action

CSV mein `MANUAL_DELETE_REVIEW` filter karke exact 33 wrappers dekhein. Whole V7 folder delete na karein. Agar owner actual deletion choose kare, pehle corresponding Drive ID/receipt save rakhein; deleted wrapper restore karne ke liye same Drive bytes aur SHA compare karein. Batch 35, `_work`, What If copy, Shorts evidence, old research export/audit receipts aur Git recovery ko filhal na chhuyein. Machine B ko us Mac par alag verify karna zaroori hai.
'''
open(O+'/YIOS_ACTUAL_SSD_CLEANUP_PLAN_ROMAN_URDU.md','w').write(report)
print(json.dumps({'rows':len(rows),'eligible':len(eligible),'eligible_bytes':total,'batches':dict(batches),'potential_cf':potential_cf,'potential_whatif':potential_wi,'potential_batch35':potential_35},indent=2))
