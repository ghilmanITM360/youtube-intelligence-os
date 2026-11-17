import json,csv,hashlib,os,ast
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).parent;E=O/'evidence';A=Path('/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z');P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');os.umask(0o077)
def load(p):return json.loads(p.read_text())
def write(n,t):(O/n).write_text(t.strip()+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
d=load(O/'GIT_REF_DELTA_EVIDENCE.json');obj=load(E/'EXACT_REF_INSPECTION.json');src=load(E/'EIGHT_SOURCE_REFRESH.json');oldval=load(A/'VALIDATION.json');now=datetime.now(timezone.utc).isoformat();ref=obj['ref'];oid=obj['expected_oid'];s=load(E/'GIT_CURRENT_BEFORE.json')
q=load(E/'DRIVE_RESOURCE_STATUS.json');q['receipt_written_utc']=now;q.pop('observed_utc',None);(E/'DRIVE_RESOURCE_STATUS.json').write_text(json.dumps(q,indent=2)+'\n')
# Preserve exact saved strings plus decoded display for Git C-quoted path identity.
lf=list(csv.DictReader((A/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv').open()));remaining=[x for x in lf if x['integrity']!='PASS'];high=sorted([x for x in remaining if not x['drive_equivalent_ids']],key=lambda x:int(x['expected_bytes']));covered=[x for x in remaining if x['drive_equivalent_ids']]
fields=['priority','oid_sha256','expected_bytes','pointer_blob_sha1','path','path_raw_in_prior_receipt','lfs_payload_full_bytes','independent_drive_original','drive_equivalent_ids','existing_evidence_receipt','proposed_step','new_transfer_authorized']
with (O/'REMAINING_LFS_RECOVERY_GAPS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for x in high+covered:
  raw=x['path'];display=raw
  if raw.startswith('"'):
   try:display=ast.literal_eval(raw).encode('latin1').decode('utf-8')
   except (ValueError,SyntaxError,UnicodeError):pass
  risk=not bool(x['drive_equivalent_ids']);idx=high.index(x)+1 if risk else 0
  w.writerow({'priority':f'P0-{idx:02d}' if risk else 'P2_DRIVE_ORIGINAL_COVERED','oid_sha256':x['oid_sha256'],'expected_bytes':x['expected_bytes'],'pointer_blob_sha1':x['pointer_blob_sha1'],'path':display,'path_raw_in_prior_receipt':raw,'lfs_payload_full_bytes':'NOT_VERIFIED','independent_drive_original':'NO_COMPLETE_PROOF' if risk else 'PRIOR_FULL_BYTES_OR_MEMBERS_VERIFIED','drive_equivalent_ids':x['drive_equivalent_ids'],'existing_evidence_receipt':str(A/'LFS_REMOTE_PAYLOAD_VERIFICATION.csv'),'proposed_step':('Wave 1: one object at a time; 70,000,000-byte total payload cap for first three' if idx and idx<=3 else 'Wave 2: separately approved one historical catalog version at a time; do not substitute current catalog for old OID') if risk else 'Defer LFS transport test; preserve existing verified original mapping; fresh metadata before receipt reuse','new_transfer_authorized':'NO'})
# Formal evidence categories and deliberately non-passing current exact-ref acceptance.
checks=[]
def check(n,result,evidence,reason=''):checks.append({'criterion':n,'result':result,'evidence':evidence,'reason':reason})
check('Historical delta is one exact addition only','PASS','GIT_REF_DELTA_EVIDENCE.json#historical_delta')
check('Exact named ref currently resolves to expected OID','FAIL','evidence/EXACT_REF_INSPECTION.json#exact_ref','Ref is absent; exit 128. No reflog exists. It is not recreated.')
check('Recorded target exists and is tree','PASS','evidence/EXACT_REF_INSPECTION.json#object_type')
check('Same OID retained by pre-existing and current other refs','PASS','GIT_REF_DELTA_EVIDENCE.json#current_existing_target_refs','Five current refs retain the exact same immutable tree; historical prior baseline also retained it.')
check('Historical canonical Git state preserved','PASS','GIT_REF_DELTA_EVIDENCE.json#historical_core_equal')
check('Current HEAD branch status stash worktrees match prior final','PASS','GIT_REF_DELTA_EVIDENCE.json#fresh_core_equal')
check('Non-auxiliary local refs preserved','PASS','GIT_REF_DELTA_EVIDENCE.json#non_auxiliary_local_delta')
check('Live remote heads/tags match historical publication receipt','PASS','GIT_REF_DELTA_EVIDENCE.json#live_remote_delta','40 advertised heads/tags; ls-remote only, no fetch.')
check('Current tracked staged/unstaged and tracked research diff empty','PASS','evidence/GIT_CURRENT_BEFORE.json')
check('Six canonical research SHA256 and capture blobs match','PASS','evidence/RESEARCH_CAPTURE_BLOB_HASHES.json','Bounded six-file proof; no whole ignored/untracked census claim.')
check('Eight proposed local source identities match','PASS','evidence/EIGHT_SOURCE_REFRESH.json')
check('Original 84-entry seal and 286 historical V7 receipts match','PASS','evidence/PRIOR_SEAL_CHECK.json; evidence/V7_RECEIPTS_CURRENT_CHECK.json')
check('Automation still PAUSED and TOML unchanged','PASS','evidence/AUTOMATION_CURRENT.json')
validation={'written_utc':now,'status':'BLOCKED_CURRENT_EXACT_REF_ACCEPTANCE','original_result_preserved':{'path':str(A/'VALIDATION.json'),'sha256':sha(A/'VALIDATION.json'),'status':oldval['status'],'checks':108,'passed':107,'failed':1,'failed_check':'Git unchanged: refs','rewritten':False},'A_canonical_project_state_integrity':{'result':'NO_OBSERVED_PROTECTED_STATE_CHANGE_IN_CHECKED_SCOPE','head':s['head']['stdout'].strip(),'branch':s['branch']['stdout'].strip(),'local_publication_refs':'UNCHANGED','remote_publication_refs':'UNCHANGED_40','research':'6/6 full-byte hashes plus capture blobs match; tracked research diff empty','limits':['No historical raw index digest; compare historical staged/unstaged semantic state only','No new full ignored/untracked ecosystem content census','Machine B current source inventory unavailable']},'B_auxiliary_ref_changes':{'historical_event_classification':'DOCUMENTED_AUXILIARY_REF_EXCEPTION','current_delta_classification':'DOCUMENTED_AUXILIARY_REF_CHURN','exact_named_ref_current':'ABSENT','deltas':'GIT_REF_DELTA_EVIDENCE.json','current_target_retaining_refs':len(d['current_existing_target_refs']),'current_strict_ref_set_preservation':'FAIL'},'C_actor_attribution':{'status':'ACTOR_UNKNOWN','creation':'NOT_PROVEN','later_removal_checkpoint':'NOT_PROVEN','generic_codex_pattern':'CONSISTENT_NOT_ATTRIBUTION'},'D_data_loss_and_recovery':{'observed_delta_impact':'NO_OBSERVED_SOURCE_LOSS; same tree survives under five other refs; no publication ref moved','historical_addition':'Added another reachability root for an already retained tree, without changing HEAD/index/worktree objects','complete_restore_certification':False,'remaining_gaps':['16 known LFS OIDs not full-byte LFS verified; eight have verified Drive originals','Two selected local files lack proven independent recovery','Bundle external prerequisite closure not independently restore tested','iCloud current provider availability and immutable version retention unverified','Machine B current inventory unavailable']},'narrow_acceptance':{'criteria_file':'ACCEPTANCE_CRITERIA.md','criteria_sha256':sha(O/'ACCEPTANCE_CRITERIA.md'),'result':'BLOCKED','reason':'Predefined exact-ref presence criterion fails; it cannot be honestly reported present. Historical impact isolation supported, but original failure is not waived or converted.','checks':checks,'passed':sum(c['result']=='PASS' for c in checks),'failed':sum(c['result']=='FAIL' for c in checks),'count':len(checks)},'execution_readiness':{'result':'BLOCKED_NO_AUTHORIZATION_AND_RESOURCE_GATES','mac_disk_reserve':'FAIL_BELOW_5000000000_BYTES','Drive_owner_quota':'CURRENT_UNVERIFIED','writer_window':'NOT_RELEASED','V8_upload_authorization':False,'automation_restart_authorization':False},'preservation':{'new_cloud_objects':0,'uploads':0,'downloads':0,'git_write_operations':0,'source_content_writes':0,'automation_edits':0,'automation_paused':True,'credit_or_reset_use':False,'only_writes':'New external continuation directory'},'final_session_preservation_check':'Pending final bounded check; appended evidence and finalization record will be sealed.'}
(O/'FINAL_VALIDATION_ADDENDUM.json').write_text(json.dumps(validation,indent=2)+'\n')
ret='\n'.join('- `'+x+'`' for x in d['current_existing_target_refs'])
write('GIT_AUXILIARY_REF_INVESTIGATION.md',f'''# Git auxiliary-ref investigation — 27 October 2026

**Historical classification: documented auxiliary-ref exception. Actor: ACTOR_UNKNOWN. Current exact-ref acceptance: BLOCKED. No observed canonical project-integrity loss in the checked scope.**

This is a read-only reconciliation of `{A}`. Its original `VALIDATION.json` remains **107 PASS / 1 FAIL / 108**, status INCOMPLETE_BLOCKED. No prior report, ref or receipt was changed.

## A. Canonical project-state integrity

Historical before/after and fresh checkout agree on HEAD `{s['head']['stdout'].strip()}`, branch `{s['branch']['stdout'].strip()}`, complete saved porcelain status, stash and worktree list. Existing untracked evidence remains present in the same status listing; a dirty source tree was preserved, not cleaned. Stash OID remains `5b6c3042679400b16aa1024b79058b71dade0ab9`. Only one registered YIOS worktree is shown: `{P}`. All non-auxiliary local refs agree. A fresh bounded `git ls-remote --heads --tags origin` returns the same **40** publication entries as the historical receipt; this is not a fetch or proof of Machine B's unpushed work.

Current staged diff, unstaged tracked diff and tracked research diff are empty. Current raw index bytes, entries and flags were captured for end-of-review comparison. The original audit did not save a raw index digest, so byte-for-byte historical index preservation is not claimed. Historical porcelain status supports semantic staged/unstaged preservation.

The six selected Casually Finance documents all match their original canonical SHA-256 receipts, totalling **77,142 bytes**. Their Git blob bytes in the captured tree also match all six current and historical hashes. This establishes the relevant canonical research content within that bounded scope. It does not certify every ignored/untracked research artifact or Machine B data.

## B. Exact auxiliary event and fresh ref delta

Original failed check: `Git unchanged: refs`. The original exact delta is only this addition:

`{ref}`

Recorded OID: `{oid}`.

The timestamp-like name component decodes to **{obj['timestamp_component_utc']}**; it is a naming observation, not a trusted creation timestamp or actor ID.

**Fresh result differs from the prompt's expected existence:** `git show-ref --verify` exits 128; the exact ref is absent. The loose ref file and its reflog file are absent, and `git reflog exists` exits 1. `git cat-file -t {oid}` succeeds with type **tree**. HEAD's tree is `{obj['head_tree']['stdout'].strip()}`; the captured tree is not falsely treated as HEAD.

Since the prior final receipt, the saved comparison shows **one auxiliary checkpoint added and two auxiliary refs removed**, no retargeting. Exact full names and OIDs are in `GIT_REF_DELTA_EVIDENCE.json`. Every changed name is under `refs/codex/turn-diffs`; every changed entry concerns the same tree OID. No canonical branch, tag, stash or remote-tracking ref moved.

Other capture names share the structure `refs/codex/turn-diffs/captures/<milliseconds>/<UUID>/base` and resolve to trees. Checkpoint names share the same namespace family and tree type. The target already existed under older refs before the original addition. Five current refs still retain it:

{ret}

Tree-to-HEAD metadata comparison reports **282 extra capture entries**, and no modifications to HEAD entries in that comparison. The reverse diff's `D` markers mean entries are present in the capture tree but absent from HEAD; they are not a deletion operation and do not establish source loss. The six research documents are among the captured entries.

## C. Attribution and bounded log review

**ACTOR_UNKNOWN** applies to both original creation and later auxiliary churn. No reflog identity or contemporaneous create/delete command was found for the exact ref. The prior authorized readiness rollout contains observations and report-writing commands mentioning this ref; those are not independent creation evidence. Seven local desktop log files for 27 October (about 5.2 MB) contain no exact event token or matching turn-diff logging. Absence of a log entry is not evidence that no tool acted.

The naming/structure and tree targets are consistent with the owner's stated Codex bookkeeping explanation. Public explanations and generic OpenAI documentation cannot identify the actor of this exact local event. A bounded official-documentation check did not establish this namespace's precise implementation. No creator attribution is inferred from generic tool behaviour. Official reference inspected: https://learn.chatgpt.com/docs/reference/troubleshooting . This reference is not used as evidence of attribution.

No tool was restarted, no ref recreated, and no Git mutation, checkout, reset, prune, garbage collection, fetch or cleanup was run. Git reads used `GIT_OPTIONAL_LOCKS=0` and `GIT_NO_LAZY_FETCH=1`.

## D. Recovery implications and acceptance

The original addition created another name retaining an already retained immutable tree. Its isolated historical impact is a documented auxiliary-ref exception. The later missing names do not remove the target tree's current reachability because five other refs retain it. No source loss or publication-history change was observed from this delta. This conclusion does not prove complete tree/blob closure, all-history LFS coverage or clean-machine recovery.

`ACCEPTANCE_CRITERIA.md` was written before the narrow checks ran. The resulting **13-check** narrow assessment is **12 PASS / 1 FAIL / BLOCKED** because the exact named ref does not currently exist. This is a distinct present-state failure, not a rewrite of the original 107/108 result. There is no silent waiver. A future owner decision may accept the documented historical exception and current auxiliary churn for planning; neither decision authorizes ref deletion/recreation or transfer.

All **84/84** prior sealed entries and **286/286** V7 historical control receipts match. V7 accepted verified bytes remain **6,332,524,432** (physical **6,332,929,262**, including the approved 404,830-byte duplicate). V8 uploads remain zero in this reconciliation; the backup automation remains PAUSED. Disk is below the 5 GB reserve and current authorized Drive quota could not be reauthenticated, so execution is separately blocked even if the owner accepts the documented exception.

Exact commands, captured outputs, source identities and log-review boundaries are under `evidence/`; consult the JSON addendum and handoff. No complete disaster-recovery certification is issued.
''')
table='\n'.join(f"| `{x['path']}` | {x['bytes']:,} | `{x['sha256']}` | {'Observation-time iCloud full-byte match; current provider availability/retention unverified' if '/research/' in x['path'] else 'No proven independent recovery copy'} |" for x in src)
pack=load(A/'evidence/BUNDLE_PACK_VERIFICATION.json');prereq='\n'.join('- `'+x+'`' for x in pack['external_delta_prerequisites'])
priority='\n'.join(f"| {i} | `{x['oid_sha256']}` | {int(x['expected_bytes']):,} | `{x['path']}` |" for i,x in enumerate(high,1))
write('V8_OPTION_A_VS_B_RECOMMENDATION.md',f'''# V8 Option A versus B — proposal only

**Recommend Option B, conditional on explicit owner approval, the source writer's read window and fresh resource/privacy gates. No transfer is authorized or executed.**

| Alternative | Files | Payload bytes | 100,000-byte control allowance ceiling | Benefit |
| --- | ---: | ---: | ---: | --- |
| A minimum | 2 | 1,033,903 | 1,133,903 | Addresses the two selected identities with no proven independent copy |
| B durable set | 8 | 1,111,045 | 1,211,045 | A plus a dedicated independently verified private recovery copy of six authored documents |

B adds only **77,142 bytes** (about 75.33 KiB, 7.46% over A). It adds a separate recovery copy beyond the observation-time iCloud receipts. A is reasonable only if the owner intentionally defers durable preservation of those six documents. These alternatives are not additive. Neither is complete YIOS recovery coverage.

## Exact refreshed scope

All eight canonical local files were read once with before/after stable inode/size/mtime checks; **8/8 SHA-256 and size matches**, **1,111,045 bytes**. This refresh did not read iCloud providers, edit the sources, or release ownership. Evidence: `evidence/EIGHT_SOURCE_REFRESH.json`.

| Exact local source | Bytes | SHA-256 | Independent recovery evidence |
| --- | ---: | --- | --- |
{table}

The six iCloud full-byte observations are preserved at `{A}/evidence/ICLOUD_SIX_SCRIPT_COPIES.json` and covered by the immutable prior seal. Their current on-demand accessibility and immutable version retention remain **UNVERIFIED** after the earlier provider stall. No additional iCloud read was attempted. Local copies on this same Mac do not establish independent-machine disaster recovery.

## Bundle prerequisites — not standalone

The unchanged bundle's recorded 28-object pack checksum and claimed local commit/stash objects passed the prior bounded verification. Its two declared base commits are:

- `e25dc63fc101390867ebf1495bba726ba9797fb6`
- `31ea9a53a6b4c9a1b74a3478ce16e510fdf06e10`

Eight external delta prerequisites were required by the prior pack decoder:

{prereq}

Prior remote API commit metadata existed for both base commits, and the local decoder could read the prerequisite objects. That does not prove independent full closure after this Mac is lost. Preserve the bundle now if approved; separately authorize a bounded clean independent restore experiment with verified prerequisite closure, storage ceiling and no writes to the production object database. No clone, fetch, test restore or new bundle was made in this task. Bundle preservation benefits local commit/stash recovery but must not be described as standalone recovery.

## Future transfer decision, still blocked

Proposed destination: a new distinct private V8 child under existing owner-only `yios` folder `1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr`, using authenticated **kgk2930@gmail.com**. Suggested child name `V8-selected-recovery-2026-10-27` is a proposal, not an existing object or authorization. Owner must approve this exact child/scope and source-read window; Finance and protected Visual Forensics ownership remain unchanged.

If separately approved and gates pass, recheck eight source hashes/stability; prove exact destination owner/Restricted privacy; reconcile existing exact identities before any upload; upload only the selected scope and bounded controls; independently retrieve each full raw remote file and compare length/SHA-256; preserve actual IDs/parent/privacy/readback receipts. Archive/wrapper checks do not substitute for raw bytes. Do not upload a current catalog or the discovery candidate list. Any changed source hash or destination/account mismatch stops execution.

V7's 12,000,000,000-byte physical ceiling has historical headroom **5,667,070,738 bytes** before V8. B plus the 100,000-byte allowance would add at most **1,211,045 bytes**, making prospective physical bytes **6,334,140,307**, if nothing else changed. The owner account's fresh quota remains unavailable; historical rounded quota supported a conservative 7.6 GB free floor and 5.6 GB after its 2 GB reserve, but these are not current measurements. Local disk is currently below the 5 GB reserve. No execution should start under these resource conditions.

## Remaining LFS proposal — separate authorization

Thirteen full-byte verified LFS receipts remain sealed (**192,210,838 bytes**). Remaining **16 OIDs / 976,973,901 bytes** are listed exactly in `REMAINING_LFS_RECOVERY_GAPS.csv`. Eight have prior independently verified Drive originals (**223,141,535 bytes**) but their LFS transport bytes were not read. Eight lack complete independent recovery proof (**753,832,366 bytes**); an offer or pointer is not a full-byte recovery proof.

| Priority | High-risk exact LFS SHA-256 OID | Bytes | Saved path |
| --- | --- | ---: | --- |
{priority}

**Proposed Wave 1:** retrieve only priorities 1–3, sequentially, **69,857,710 payload bytes**, under a newly explicit **70,000,000-byte payload ceiling**. This is a new budget request; the old 200,000,000-byte budget has only **4,608,869 bytes** remaining after its 195,391,131-byte conservative upper bound and cannot fund even the smallest remaining object. Require ≥5 GB Mac reserve throughout, fresh usage/credits checks and an owner-approved durable evidence destination; preserve prior scratch originals and never delete them for space.

**Proposed Wave 2:** only after owner review of Machine B/prerequisite evidence, approve one of the five exact historical catalog OIDs at a time, smallest first, under an explicit per-object **160,000,000-byte payload ceiling** and stop/checkpoint after each full size/hash comparison. Further versions need separately confirmed scope/budget; no bulk command. A verified newer catalog is not a substitute for an older OID. Prefer already independently covered Drive originals for the other eight and defer redundant LFS transport tests.

No LFS or other recovery payload was downloaded in this reconciliation. Known 29 identities are not a complete all-history census: the historical missing Git blob `793ee3c02688ed7f3275b3f1026d9fd5f683d714` limitation remains unresolved. No fetch/repair was attempted.
''')
write('MACHINE_B_READ_ONLY_INVENTORY_PROMPT.md',f'''# Request for Machine B's existing operator — NOT DISPATCHED

Owner authorization requested: have the **existing Machine B operator** perform only a current, bounded READ-ONLY recovery inventory. This request does not appoint a new operator, transfer Finance ownership, authorize Finance research/audits, resume any automation, or disturb protected Visual Forensics/Claude session `873b9a27-ba03-4183-aa61-f82d01f65998`.

1. Check five-hour usage first, weekly second, then context, disk/memory, paid/reset credits and active operators. Stop costly work at 90% five-hour, 95% weekly, or below 5 GB Mac reserve. Spend/redeem no credits. Record actual Machine B identity, authenticated operator, observation UTC/PKT time and canonical source paths. Confirm who is writing what; do not infer exclusivity from remote refs or a PID.
2. Reuse current manifests and authoritative handoffs. Create small dated external inventory evidence only; never change source data, raw media, ignored/untracked files, ownership, permissions, branches, refs, stash, LFS stores, remotes or automation. No fetch, clone, checkout, reset, clean, push, upload, bulk cloud hydration or new backup copies. Do not print credentials/signed URLs. Do not open new Finance investigations or revise research judgments.
3. Locate the **original Creator Intelligence Master Guide** and its original supporting ledgers/registers, not merely derivative reports or summaries. Provide exact canonical path, source authority/provenance, size, stable full SHA-256, readable/original/derived status, existing remote ID/receipt/member mapping and any missing dependency. If unavailable, report exact search boundary and missing locator; do not fabricate.
4. Inventory current Finance ignored/untracked data, canonical research inputs/outputs, source ledgers, current workbook/JSONL/CSV identities, original media/thumbnails/transcripts, source archive identities and member manifests, and current media-library indexes. Respect privacy and active-writer windows; prefer existing stable hashes for large media and label their date. Do not repeatedly hash huge media or copy whole libraries.
5. Preserve and inventory protected stash OIDs, local unpublished commits, uncommitted/ignored/untracked evidence and source-only work. Record full current HEAD/branch, all relevant local/remote-tracking/publication refs, `git status`, stash OIDs and worktree identities using read-only optional-locks-disabled commands. Bounded authenticated `ls-remote` may observe current publication without fetching. Include current full remote/PR head evidence when accessible; distinguish local unpushed work, handoff claims and live publication. Do not merge/close PRs, switch branches, reclaim a protected writer or infer source release from a published SHA.
6. Produce a source manifest with one row per selected logical identity: machine/operator/UTC, absolute path, size, SHA-256 or explicitly dated hash evidence, source/derived status, stable-read result, Git/LFS/ignored/untracked/stash/publication identity, archive member identity, independent recovery location/actual remote ID and full-byte hash receipt, prerequisites, owner and uncertainty. Mark **exact files with no independent recovery proof**. A filename match, sync marker, remote metadata or LFS pointer alone is insufficient. Unknown sizes remain unknown, never zero.
7. Specifically reconcile Machine A's remaining exact LFS identities using `{O}/REMAINING_LFS_RECOVERY_GAPS.csv` if that evidence is already made available by the owner/operator. No download is authorized by this request. Confirm whether original `sfx.wav`, the two Calf Pain video versions and the five historical catalog OIDs have independent full-byte evidence on B or elsewhere. Do not replace older catalog versions with current bytes.
8. Return a dated small external Markdown handoff, CSV/JSON source manifests and SHA256SUMS through the owner's established handoff channel. Include observations versus claims, missing locators, exact independent-copy gaps, resources, current publication SHAs, and all remaining unverified boundaries. Do not upload or send messages without separate explicit authorization.

Historical Finance release `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff` remains a publication checkpoint, not proof of today's source inventory. Machine A observed that remote branch SHA unchanged during this reconciliation; that does not establish Machine B's current unpushed state. Machine B remains NOT_DIRECTLY_VERIFIED here.
''')
write('EXACT_OWNER_DECISIONS_REQUIRED.md',f'''# Exact owner decisions — proposal ready, execution unauthorized

No yes/no response is inferred from silence. These are separate decisions; accepting this review is not blanket authority for later transfers, restore tests, cleanup or ownership changes.

1. **Historical Git exception:** acknowledge original 107 PASS / 1 FAIL unchanged. Decide whether to accept the documented isolated historical capture-ref addition and later same-tree auxiliary churn as a planning exception with **ACTOR_UNKNOWN**. Current exact-ref presence acceptance remains BLOCKED; do not authorize removing/recreating refs to make a check pass. No canonical damage was observed in the checked scope, but no whole-ecosystem integrity or complete disaster-recovery certificate is claimed.
2. **V8 scope:** recommend **Option B**, exactly the eight paths/hashes in `V8_OPTION_A_VS_B_RECOMMENDATION.md`, **1,111,045 payload bytes**, plus at most **100,000 control bytes** (total ceiling **1,211,045**). Option A is the explicit alternative: two paths, **1,033,903 payload**, ceiling **1,133,903**. Do not combine both. Any hash/path change requires reapproval/reconciliation.
3. **Destination and source window:** approve or reject the proposed new distinct owner-only private child `V8-selected-recovery-2026-10-27` under `1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr`, using `kgk2930@gmail.com`. Confirm the existing source owner allows a stable read window for the selected research files. This is no Finance/Visual production ownership transfer. No folder exists by virtue of this proposal.
4. **Resource gate:** before any future execution, independently restore/verify ≥**5,000,000,000 local free bytes** without authorizing this agent to delete anything. Reauthenticate actual owner Drive quota and retain ≥**2,000,000,000 free bytes**, the 12 GB physical ceiling and the established safety buffer. Current Mac disk fails the reserve. Current owner Drive quota is unverified: a different-account UI result was rejected, then the Mac locked. Historical quota is not current permission to proceed. Usage must remain below 90% five-hour /95% weekly; never spend/reset credits.
5. **LFS Wave 1:** separately approve or defer exactly the first three high-risk OIDs in the CSV, **69,857,710 payload bytes**, under a new **70,000,000-byte** payload ceiling, one at a time. Old budget remaining is only **4,608,869 bytes**. Preserve the thirteen verified receipts; no bulk LFS fetch/pull. Larger catalog versions require separately confirmed per-OID scope; proposed per-object ceiling 160,000,000 bytes. No new retrieval is currently authorized.
6. **Independent bundle restore:** separately authorize a bounded isolated recovery experiment proving the two base commits and eight external delta prerequisites from independent sources. Require a concrete independent environment, storage/network ceiling and unchanged production Git state. The current bundle is not standalone; a restore test is not executed or approved by preserving the file.
7. **Machine B:** approve forwarding the exact `MACHINE_B_READ_ONLY_INVENTORY_PROMPT.md` to B's existing operator, or deliver it yourself. It requests inventory/hashes/source originals and missing independent copies only. This task has not sent it and does not authorize new Finance audits, branch changes or writer takeover.
8. **Automation:** keep **PAUSED**. A possible future manual V8 transfer does not authorize resuming the completed V7 automation. Any restart needs a separate scope/policy review and explicit instruction.

Preserve Batch31's permanently unresolved duplicate actor, Batch35's corrected-destination history, all prior receipts, stashes, ignored/untracked evidence, originals, and the exact current refs. Nothing should be deleted or rewritten to improve a validation count.
''')
write('CONTINUATION_HANDOFF.md',f'''# V8 readiness reconciliation handoff — 27 October 2026

Continuation directory: `{O}`. Predecessor `{A}` is immutable: **84/84** seal entries match; **286/286** historical V7 control receipts match. New report seal is `SHA256SUMS`. Read the investigation and `FINAL_VALIDATION_ADDENDUM.json` before any future action.

**Resolved evidence question:** historical strict ref-set preservation failed on one added auxiliary capture ref. Exact original ref `{ref}` recorded OID `{oid}`. Freshly, the named ref is absent, one new checkpoint ref appeared and one old checkpoint ref also disappeared. Full delta is saved; every changed entry uses the same tree OID under `refs/codex/turn-diffs`. The target survives under **five other refs**. The original addition is a documented auxiliary exception; original result **107 PASS /1 FAIL** is unchanged. The separately predefined narrow current-ref check is **12 PASS /1 FAIL /BLOCKED**, because current exact presence is false. Both creation and later churn remain **ACTOR_UNKNOWN**.

Current HEAD `badec432bbf5610748123b3f0e0bcb9cdb25fa10`, branch `codex/what-if-archive-main-integration`, stash `5b6c3042679400b16aa1024b79058b71dade0ab9`, single registered canonical checkout `{P}`. Historical and fresh status/stash/worktree lists match; existing untracked evidence preserved. Tracked staged/unstaged/research diffs empty. All non-auxiliary local refs and **40 live remote heads/tags** match prior receipts, including main `08e719264e31ecd82de24f8eeb8f065c08359fe5`, Finance `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff` and protected Visual Forensics `090f84b3292a3b6c6e94653a6ef1867726e4ebdd`. No branch/ref/index mutation. Raw historical index digest was unavailable; current digest/entries/flags establish this review's baseline and final comparison.

V7 accepted verified **6,332,524,432**, physical **6,332,929,262**, approved duplicate **404,830**, pending **0** remain preserved historical verified totals. No new cloud census, cloud object or transfer. V8 uploads **0**; automation **PAUSED** and its TOML unchanged.

Eight current local identities match **1,111,045 bytes**; six authored docs also match capture-tree Git blob bytes. Two selected gaps remain original audio `/Users/ghilmankhan/workprojects/youtube-intelligence-os/output/chair-stand-safety/source/source.mp3` (275,181) and `/Users/ghilmankhan/yios-git-recovery/cleanup-2026-10-13/local-only-history.bundle` (758,722). Recommend B over A for only **77,142 extra bytes**. Six iCloud matches remain observation-time proof only; no provider reread attempted. Bundle pack/prerequisites preserved, independent closure restore untested.

Thirteen verified LFS payload receipts **192,210,838 bytes** preserved; remaining **16 /976,973,901 bytes** listed in CSV: eight prior Drive-original covered, eight high-risk without complete recovery proof. Proposed separate Wave1 is first three high-risk objects **69,857,710 bytes**, new 70 MB cap. Old sample conservative upper **195,391,131 /200,000,000** leaves only 4,608,869. No further downloads authorized. Historical missing Git blob/all-history limitation retained.

**Resources:** initial usage2% five-hour/56% weekly; exact final usage/disk are appended in `evidence/FINAL_RESOURCES.json`. Disk starts around3.94 GB and **fails 5 GB reserve**; no expensive operation started. Memory pressure reports33% system-wide free. Paid balance0, two reset credits untouched. Exact context meter unavailable; existing prior task compaction noted, current bounded task completed using durable evidence. Owner Drive current quota **UNVERIFIED**: different-account UI quota rejected; UI locked before owner account could be verified. Historical owner conservative free floor7.6 GB /5.6 GB after2 GB reserve is stale, not a current gate pass. Historical physical cap headroom5,667,070,738 bytes.

Ownership remains per owner instructions: no takeover, no Machine B direct inventory, no protected-session interruption, no new Finance work. Local Claude PID existence/cwd was recorded only as an observation, not identity/exclusivity proof. Machine B prompt is prepared **not dispatched**.

**Exact next action:** owner reviews `EXACT_OWNER_DECISIONS_REQUIRED.md`, chooses whether to acknowledge the documented ref exception/churn, chooses A/B and exact private destination/read window, and requests the existing Machine B operator's bounded inventory. Before any separately authorized execution, fresh resource/account/ownership/hash/privacy gates must pass. Keep V8 and automation paused; no fetch/push/ref deletion/recreation/cleanup/commits. Do not certify complete disaster recovery. No prior report or historical validation is to be rewritten.
''')
print(json.dumps({'deliverables_written':8,'lfsgaps':len(remaining),'narrow_checks':len(checks),'narrow_pass':sum(c['result']=='PASS' for c in checks),'narrow_fail':sum(c['result']=='FAIL' for c in checks),'output':str(O)},indent=2))
