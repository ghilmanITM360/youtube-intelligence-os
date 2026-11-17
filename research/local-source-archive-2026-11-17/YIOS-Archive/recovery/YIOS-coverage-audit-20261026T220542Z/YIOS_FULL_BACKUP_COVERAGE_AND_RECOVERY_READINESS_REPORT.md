# YIOS full backup coverage aur recovery readiness — 27 October 2026 Pakistan time

Audit UTC start: 2026-10-26T22:05:42Z. Machine A: `Ghilmans-Laptop.local`. Output: `/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z`.

**Faisla: selected V7 backup complete aur verified hai; poore dono Macs ko abhi disaster-recovery ready kehna durust nahin.** Machine A ke 14 authorized roots ka complete metadata census hua. Machine B ka filesystem accessible nahin tha, is liye us ka current poora count ya unpublished data verify nahin hua. Is report ka status **MACHINE_A_METADATA_CENSUS_COMPLETE / TWO_MACHINE_READINESS_LIMITED_BY_ACCESS_AND_RESTORE_GAPS** hai.

Koi naya upload, cloud move, delete, rename, permission change, Git fetch/pull/checkout/commit/push ya production install nahin hua. Backup automation **PAUSED** aur unchanged hai. Yeh independent audit hai; Finance ya backup ki nayi canonical authority nahin.

## 1. Hamare paas total kitne important YIOS files aur GB hain?

Machine A par **72,076 regular file paths**, **6,375 directories**, aur **70 symlinks** enumerate hue. In ka logical path total **33,392,613,422 bytes / 33.393 GB** hai. Is mein Git internals, dependency caches, preservation copies aur original ZIP wrappers shamil hain; yeh unique content total nahin.

Git internals, dependencies/cache, Finder metadata aur symlinks alag karne ke baad **34,015 important source/evidence/export paths, 26,085,270,508 bytes / 26.085 GB** hain. In mein **24,266,769,320 bytes** resident source/evidence paths hain; **7,359 dataless placeholders / 1,818,501,188 logical bytes** ko local bytes nahin gina gaya. Resident path bytes bhi same-content copies ko shamil karte hain.

| Coverage | Important path count | Logical path bytes | Matlab |
| --- | --- | --- | --- |
| SAFE | 8300 | 11839582137 | Independent exact bytes/member/Git blob retrieval receipt matches |
| PROVISIONALLY COVERED | 4254 | 5523845749 | Evidence hai; exact wrapper, full retrieval ya dependency test baqi |
| LOCAL ONLY | 14102 | 6903341434 | Proven independent recovery copy nahin mili |
| BLOCKED | 7359 | 1818501188 | Mostly iCloud placeholder bytes; source access/recovery unverified |


Machine B ke available dated manifests mein **1,009 path representations / 1,000 SHA-256 identities** mili. **630 identities** ka Machine A resident hash overlap hai. **370 additional identities** A census se hash-match nahin hue: un mein known-size population **21,910,612 bytes**, aur **36 identities ka size unknown** hai. Yeh B ki complete inventory nahin. Unknown-size/source populations ko zero bytes samajh kar total nahin banaya gaya. Primary matrix mein har local file/link aur har additional B-only fingerprint identity ki row hai; B ke historical alternate paths supplemental manifest CSV mein hain.

## 2. Kitna actual data GitHub par verified hai?

Fresh authenticated tree/ref checks mein main, Finance, What If candidate, original What If archive aur protected Visual branch mila kar **5,989 unique normal Git blob IDs / 1,314,226,210 blob bytes** referenced hain. Yeh content-addressed publication/tree proof hai; har blob ko is audit mein dobara download nahin kiya gaya. **416 distinct Git blobs / 22,574,122 bytes** ke full independent retrieval/hash receipts available aur reconciled hain; yeh usi population ka subset hai, extra bytes nahin. Is mein What If ke **397 files / 8,221,384 bytes** ke four preserved publication batches shamil hain.

- Main: `08e719264e31ecd82de24f8eeb8f065c08359fe5`.
- Current A branch: `codex/what-if-archive-main-integration`, HEAD `badec432bbf5610748123b3f0e0bcb9cdb25fa10`; live remote same; PR44 OPEN/DRAFT, unmerged.
- Live Finance/PR36: `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff`; OPEN/DRAFT, unmerged. A ka cached local Finance ref purana hai; update/fetch nahin kiya.
- Local-only branch commit relative to cached refs; authenticated remote commit lookup returned Not Found: `15cbe9f0112596c1e07c1c1504302cce77bfd97a`.
- A stash (authenticated remote commit lookup also Not Found): `5b6c3042679400b16aa1024b79058b71dade0ab9`; ek modified checkpoint document. Existing **758,722-byte** local bundle in dono refs ko list karta hai. Same SSD copy independent backup nahin.

**29 LFS pointer identities** bounded available trees mein pehchani gayin. Provider ne read-only `operation=download` metadata request par **29/29 download actions** offer kiye; kisi LFS payload ke remote bytes download/hash nahin hue. Current catalog ke local **141,373,440 bytes** frozen SHA `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654` se match hain. Pointer, provider link, aur local payload teen alag evidence levels hain. Full all-ref LFS CLI scan missing Git blob `793ee3c02688ed7f3275b3f1026d9fd5f683d714` par fail hua; is liye complete historical LFS census claim nahin.

## 3. Kitna Google Drive par verified hai?

| Measure | Exact value |
| --- | --- |
| Accepted verified transfer bytes including controls | 6,332,524,432 |
| Physical remotely verified bytes including extra copy | 6,332,929,262 |
| Accepted payload object IDs | 551 |
| Verified control object IDs | 27 |
| Extra Batch31 physical object IDs | 1 |
| Current approved private physical objects | 579 |
| Remaining V7 objects / bytes | 0 / 0 |
| V7 packages / verified original members / explicit pilot aliases | 53 / 3,524 / 3 |
| All recorded archive packages / member representations | 57 / 6,825 |
| All archive member logical bytes; never added to physical total | 5,294,152,556 |


Fresh read-only listings of **24 approved private folders** exactly reconcile **579 physical files / 6,332,929,262 bytes**; no unmapped IDs, missing mapped IDs, or objects created after audit start appeared. **579/579 object owner-only privacy metadata** and **24 parent privacy checks** passed. **552 selected source mapping metadata checks** match preserved name/size/time/parent evidence. The 552 path mappings point to 551 accepted payload IDs because one earlier proven 3,999,999-byte Japan source alias reuses an ID. Physical totals deduplicate IDs; source path counts do not.

552 direct source path mappings + 6,825 archive member representations + 3 explicit pilot aliases = **7,380 original mapping representations**. Controls and checksum documents recover evidence, but do not create new original media coverage. Original archive members have actual byte hashes, not only filename indexes. Current A clone/alias matches are separate from unique recovery coverage.

**Batch31** remains `CLOSED_WITH_APPROVED_EXCEPTION_UNATTRIBUTED_DUPLICATE`: selected `1_I0MqlstrAynSWTsPnOTuZOzr5eueJtv`, extra `127DXG7Ih9tw61aFNGL0tGzwt4dc0no_A`, each404,830bytes, common SHA `e99f5577c066109a03da5d71fd6e4cb23f79f5c45d3eb6a3991a4aaf8dff2953`. Owner actor established historically; exact client/session/mechanism **UNRESOLVED** permanently. Extra copy adds zero unique coverage.

**Batch35** remains `PASS_VERIFIED_AFTER_APPROVED_DESTINATION_CORRECTION`: exact20 same IDs are in intended private folder; original wrong-root event and BLOCKED receipts remain preserved. **Batch36** remains9/9 verified. No completed batch reopened or uploaded again. Earlier recovered Batch9 object receipts and its original source-stat MANIFEST were reused correctly, rather than treating its absent conventional RECEIPT.json as a missing backup.

## 4. Screenshot wale folders ka kya status hai?

Table ke logical GB mein duplicates/wrappers ho sakte hain. “Metadata complete” ka matlab har file ka plaintext/current full hash read nahin. Folder rows ke subtrees overlap karte hain; CSV subtree totals ko jama na karein.

| Exact absolute root | Regular files | Directories | Logical GB | Dataless files | SAFE path rows | Status |
| --- | --- | --- | --- | --- | --- | --- |
| /Users/ghilmankhan/YIOS-local-audits | 15291 | 1269 | 3.504 | 0 | 3672 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/yios-git-recovery | 33092 | 2926 | 2.737 | 0 | 176 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/Documents/YIOS-Media-Library | 57 | 2 | 0.394 | 57 | 0 | PLACEHOLDERS / byte recovery unverified |
| /Users/ghilmankhan/Documents/YIOS-Production-Library | 1098 | 64 | 0.201 | 1097 | 0 | PLACEHOLDERS / byte recovery unverified |
| /Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21 | 5373 | 3 | 3.711 | 5354 | 0 | PLACEHOLDERS / byte recovery unverified |
| /Users/ghilmankhan/Documents/yios-private-backups | 851 | 128 | 0.277 | 851 | 0 | PLACEHOLDERS / byte recovery unverified |
| /Users/ghilmankhan/Downloads/videos in mp3 | 498 | 16 | 8.571 | 0 | 456 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/workprojects/video data of what if | 2876 | 190 | 0.705 | 0 | 2868 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence | 393 | 77 | 4.459 | 0 | 392 | 392 important files SAFE; 1 Finder metadata excluded |
| /Users/ghilmankhan/workprojects/yios-recovery-status | 2132 | 15 | 0.071 | 0 | 2 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/workprojects/yios-visual-forensics-install-candidate-2026-10-24 | 45 | 11 | 0.000 | 0 | 0 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/workprojects/youtube-intelligence-os | 7929 | 1380 | 7.457 | 0 | 683 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/Movies/CapCut/User Data/Projects/com.lveditor.draft | 408 | 218 | 0.072 | 0 | 42 | PARTIAL / recovery proof baqi |
| /Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research | 2033 | 76 | 1.234 | 0 | 9 | PARTIAL / recovery proof baqi |


Requested screenshot ke sab9 named roots exact spelling ke saath inspect hue. `yio-cf-editing-forensics-local-evidence` ka spelling isi tarah hai. Historical `workprojects/yio-cf-editing-forensics` current path nahin; source export ka historical locator hai, active worktree nahin. `yios-git-recovery` mein4 unrelated offline-map subtrees exclude hue; doosre personal folders scan nahin hue. Symlinks follow nahin hue.

## 5. Agar aaj Machine A ka SSD fail ho jaye?

Verified Drive originals/packages aur exact retrieved Git blobs recover ho sakte hain. Normal published Git blobs strong publication evidence rakhte hain, lekin clean independent install/restore test poora nahin. Important-path classification mein **8,300 SAFE rows / 11,839,582,137 logical path bytes** hain; yeh unique bytes ya full working production ka certificate nahin.

Risk mein six unpublished script-intelligence documents, source narration, local-only Git commit/stash, kuch forensic scratch, derived exports aur local recovery evidence hain. **14,102 important LOCAL ONLY paths / 6,903,341,434 logical bytes** ka raw total deduplicated upload requirement nahin. Bada2.742GB research JSONL derived export hai; many recovery packs and duplicates are same-SSD convenience copies. Unhashed files ko sirf name/size ki wajah se duplicates nahin kaha gaya.

7,359 iCloud placeholders ko lost nahin kaha: un ke current remote original bytes is audit mein verify nahin hue. Owner account/recovery credentials aur cloud original access ko separately prove karna hoga; secrets is audit output mein collect nahin hue.

## 6. Agar Machine B ka SSD fail ho jaye?

B ke dated registry ke **456 media path entries / 4,363,111,708 logical bytes** A ke current hash evidence aur existing verified Drive originals se **456/456** match hue. Do same-content media path representations ko unique content mein dobara nahin gina gaya. Yeh registry2026-10-21 commit aur2026-10-23 handoff ka proof hai, B ki aaj ki disk ka scan nahin.

Published Finance branch ke code/research/registered transcripts/thumbnails GitHub par content-addressed hain. B source handoff333 fingerprints,180 registered images,26 immutable baseline inputs, published Finance release records aur37-file supplementary package map preserve karta hai. Eleven external-only support files exact hashes/sizes ke saath crosswalk mein hain. Latest authenticated Finance closeout2026-10-26 hai;455 completions is handoff ka statement hai, naya Finance deep audit nahin.

B ke current ignored files, unpublished work, media additions, exact local library state aur stash `ac51465b33be2d25d1a18749b1301cda778e33e5` ka independent backup unverified hai. Original-source **Creator Intelligence Master Guide** ka exact original locator/hash available authorities mein establish nahin hua; derived guides ko original ka replacement nahin maana. B owner se bounded current manifest/access chahiye. **MACHINE_B_DIRECTLY_VERIFIED count zero** hai.

## 7. Original videos, transcripts, editing projects, audio aur forensics restore ho sakte hain?

- **Registered media:**456 historical B media path entries ke original bytes verified Drive coverage se match. Seven large source ZIP containers ke456 nonOS media members ko full streaming SHA256 se match kiya; un ka4,207,413,265-byte ZIP wrapper separately exact-backed-up nahin. Originals recoverable hain; exact ZIP-byte restoration unproven. ZIP wrappers dobara upload karne se extra unique original coverage zero ho sakti hai.
- **Transcripts and research:** Normal Git/archived source bytes available by ref/blob. Nick canonical transcript ZIP source hash is in26-file baseline; current catalog isLFS. No blanket claim that every transcript archive member was revalidated in this audit. Published research completion is separate from backup coverage.
- **Editing:** selected CapCut/What If JSON/assets recovered by source-to-member mappings, but full rendering/editability unproven. Fresh exact checks found11 referenced dependencies unavailable at recorded A paths: `0921.mp4`,9PNGs, and one narrationMP3. Broken symlink remains. Fonts, licensed assets, platform/runtime and other projects require separate tests.
- **Forensics:** V7 original member hashes and full remote decompression receipts reconcile. Downloaded sample archive restores all7 original members; three small members materialized, WAV parsed. Forensic completion, human listening, and regeneration equivalence remain separate.
- **Audio:** source m4a full SHA256/length and ffprobe parsing passed in isolated scratch. Original chair narration `output/chair-stand-safety/source/source.mp3` has two matching local copies but no proven remote copy in this scope.

[RESTORE_TEST_RESULTS.md](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/RESTORE_TEST_RESULTS.md) records exact sample IDs/hashes. A3MB sample does not certify every application or both Macs.

## 8. Agle backup mein exactly kya chahiye aur storage kitna lagega?

**Pehla minimum source-preservation candidate:8 distinct files / 1,111,045 bytes (~1.11MB)**: six script-intelligence documents, one source narration, one existing compact Git recovery bundle. No upload authorized by this audit. Source owner and stable read/hash must refresh before a future operation.

Current catalog adds141,373,440bytes only **conditionally**: verify existing remoteLFS full bytes first. Provider action offered hai; agar exactSHA retrieval pass ho, nayi Drive copy required nahin. Conservative P0 gross upper bound including this conditional catalog is **142,484,485bytes**,9files. Small forensic kitZIP95,862bytes and source/scratch gaps require next-priority review. Original guide locator and B stash scope remain unknown-size discovery tasks.

[NEXT_BACKUP_SCOPE_CANDIDATES.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/NEXT_BACKUP_SCOPE_CANDIDATES.csv) has exact sources, hashes/hash-needed flags, duplicate groups, privacy, ownership, byte upper bounds and restore requirements. It is a review queue, not approved transfer selection. 19,015 candidate rows remain after strict hash-based merging and explicit agent-configuration exclusion;12537initial path-only candidates could not be cryptographically deduplicated. Do not upload this entire queue blindly.

Resident candidate upper bound before per-owner/rebuild review is about6.65GB. It exceeds current12GB physical-cap headroom5,667,070,738bytes and conservative Drive after-reserve budget5,705,929,779bytes. Provisional Git blobs, fully covered seven mediaZIP wrappers, known SAFE hash equivalents, caches/Git internals and excluded machine-agent settings are not an automatic upload proposal. Compression is lossless-only when appropriate; no compression estimate is counted as guaranteed savings and none was performed.

## 9. Existing automation restart honi chahiye?

**Nahin. PAUSED rahe.** V7 pending zero hai. Separate owner-approved V8 may be justified for confirmed small unique sources and later owner-confirmed gaps. Existing schedule must not select these candidates itself. No new batches, controls or cloud destinations were created by this audit.

## 10. Genuinely disaster-recovery ready kehne ke liye kya baqi hai?

1. Machine B owner runs a bounded current metadata/hash inventory and matches current unpublished/ignored/stash/media assets; record date, root, refs and exact hashes without changing writer ownership.
2. Fully retrieve/check criticalLFS catalog and any needed historical/media payload; repair missing-object recovery only under separate authorization. No pointer-only acceptance.
3. Preserve confirmed unique8file minimum and any source-owner-confirmed additional gaps into a separately approved private scope; independently retrieve exact bytes.
4. Verify iCloud originals/account access, or prove identical independent recoverable copies. Keep placeholders distinguished from resident data.
5. In an independently authorized clean machine/environment, reconstruct a pinned repo/runtime from normal Git and verifiedLFS/Drive packages. Restore safe paths, file hashes, member locators, manifest ordering and source ownership.
6. Open recovered SQLite read-only, validate schema/representative queries and all required source references; validate full transcript/member retrieval. Do not run production/audits against protected canonical sources.
7. Resolve chair/CapCut missing original media, images, voice, fonts and runtime. Open/render a representative editing project in isolated authorized environment and compare expected outputs. No unknown recovered scripts/installers execute automatically.
8. Demonstrate recovery without A's SSD or hidden local cache, with authenticated private provider access and owner-controlled account/key recovery. Record recovery time and verified omissions. Until then full two-machine readiness remains **NOT_CERTIFIED**.

## Technical evidence and counting rules

Primary baseline: `/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/checkpoint-20261026T213404Z/CONTINUATION.json` SHA256 `72a99f3661265336e94889cdc6c608b2eb7b9933dd6c1586efe5a2e5ee559829`.

The baseline independently sums551accepted payload IDs6,305,546,478bytes +27controls26,977,954bytes =6,332,524,432bytes. Add one404,830-byte extra physical copy =6,332,929,262bytes. An inherited183,330-byte initial handoff control was absent from the later self-excluding control inventory; its original HANDOFF_DRIVE_RECEIPT.json closes that accounting step. Stage2initial diagnostic is retained; FINAL reconciliation is authoritative for this audit. No historical source receipt was edited.

All1,084 checksum-manifest entries selected for evidence verification passed. Fifty-seven package manifest member counts/bytes match full remote retrieval receipts; V7 subset53packages/3524members/4,933,487,806logical member bytes. Large original hashes reused only with exact recorded inode/device/size/mtime/ctime identity or documented phase0stable identity. First source hashing stage had1.5GBread cap; focused critical checks and justified per-ZIP member passes were separately checkpointed. Files lacking a current supported hash remain labelled, never silently promoted.

`recorded_source_sha256` can describe a historical B source fingerprint; `machine_a_sha256` is blank for B-only rows. `machine_b_source_paths`, `machine_b_size`, authority and evidence date preserve original locators without inventing A paths. `MACHINE_B_HANDOFF_VERIFIED` means documentary hash evidence, not current direct access. No row is labelled BOTH_MACHINES_VERIFIED merely on a past handoff. UNKNOWN bytes remain blank/UNKNOWN.

Primary inventory has72,146A file/link rows +370additional B-only identities =**72,516 rows**. Directories are separately represented in census and folder CSV. `SAFE` applies to a specific byte identity or Git blob; not a complete project/environment. File/path logical bytes, deduplicated hashes, Git blobs, LFS pointers, archive logical members, compressed physical objects and capacity totals stay separate. APFSallocated bytes are measured path/inode allocation, not guaranteed exclusive/reclaimable space; clone sharing, OScompression and iCloud make `du`/logical comparisons non-additive.

### Safety and limitations

Start usage22%five-hour/36%weekly; final63%/42%, paid0, resetcredits2untouched. Disk at final resource reading about8.916GBfree; initial12.246GB. Memory pressure read37%free of16GiB. Exact context meter unavailable; earlier conversation was summarized before this audit, and bounded durable checkpoints preserve progress. No new costly work starts near90%/95% gates.

GoogleOne fresh authenticated reload:6.7GBof15GBused, rounded UI. Conservative free7,705,929,779bytes; required reserve2,000,000,000; after-reserve5,705,929,779. Physical upload ceiling headroom5,667,070,738. Final resource JSON records latest reading; no paid/reset credits consumed.

Git branch/HEAD/full refs/stashes/worktrees/status were identical in initial and final snapshots. No original media/content writes, permission changes or protected-session interruption were issued. One SOURCE_INDEX.json ctime-only change was observed during filesystem reads; inode/size/mtime/allocation unchanged and freshSHA256 equals preserved export manifest (`677a875cadcbcca5409bc3613d1071ee7f7f0cbef18090730c68335a9b53e4ec`). Filesystem/iCloud metadata mechanism is not attributed; **not all filesystem metadata is claimed unchanged**. This qualification is preserved in SOURCE_INDEX_METADATA_CHANGE_RECONCILIATION.json.

Visible Claude cwd check was outside YIOS; protectedClaude873b9a27 remains reserved. No current B disk or distributed writer lock was inspected, and process absence is not ownership release. Original-Mac/Finance/Visual sessions and PRs were not modified. Separate local test scratch remains mode700 with mode600 recovered files; no cleanup/delete performed.

### Evidence package entry points

- [ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv)
- [FOLDER_BY_FOLDER_COVERAGE.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/FOLDER_BY_FOLDER_COVERAGE.csv)
- [MACHINE_A_B_SOURCE_CROSSWALK.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/MACHINE_A_B_SOURCE_CROSSWALK.csv)
- [MACHINE_B_MANIFEST_SOURCE_IDENTITIES.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/MACHINE_B_MANIFEST_SOURCE_IDENTITIES.csv)
- [GITHUB_AND_LFS_RECOVERY_STATUS.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/GITHUB_AND_LFS_RECOVERY_STATUS.csv), [LFS_POINTER_PAYLOAD_CROSSWALK.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/LFS_POINTER_PAYLOAD_CROSSWALK.csv)
- [DRIVE_BACKUP_COVERAGE_MATRIX.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/DRIVE_BACKUP_COVERAGE_MATRIX.csv), [MEDIA_ZIP_MEMBER_COVERAGE.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/MEDIA_ZIP_MEMBER_COVERAGE.csv)
- [DUPLICATES_ALIASES_AND_OVERLAPS.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/DUPLICATES_ALIASES_AND_OVERLAPS.csv), [MISSING_CRITICAL_ASSETS.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/MISSING_CRITICAL_ASSETS.csv)
- [NEXT_BACKUP_SCOPE_PROPOSAL.md](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/NEXT_BACKUP_SCOPE_PROPOSAL.md), [RESTORE_TEST_RESULTS.md](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/RESTORE_TEST_RESULTS.md)
- [COVERAGE_AUDIT_VALIDATION.json](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/COVERAGE_AUDIT_VALIDATION.json), [SHA256SUMS](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/SHA256SUMS), [CONTINUATION_HANDOFF.md](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/CONTINUATION_HANDOFF.md)

Git ref/stash statuses: [GITHUB_REF_AND_STASH_RECOVERY_STATUS.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/GITHUB_REF_AND_STASH_RECOVERY_STATUS.csv). Physical objects: [DRIVE_PHYSICAL_OBJECTS_RECONCILIATION.csv](/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/DRIVE_PHYSICAL_OBJECTS_RECONCILIATION.csv).

All consequential statements trace to artifacts under evidence/ or immutable prior receipts. This package is local and deliberately **not uploaded**, so its own independent recovery copy is not established.
