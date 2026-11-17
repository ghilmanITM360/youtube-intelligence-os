# YIOS Machine A — Phase 0 preservation audit

**Date:** 2026-10-25, Asia/Karachi. **Disposition:** HOLD FOR OWNER REVIEW. This audit authorizes no cleanup, migration, installation, commit, push, merge, branch change, worktree operation, spending, or acquisition. Only this external audit directory was created. Source folders and repository payload were read only.

## 1. Executive findings and resource gates

One canonical checkout exists among the seven inspected trees. Preserve it and the external evidence together: Git publication does not make the project fully portable. What If has valuable local production intelligence beyond its published adapter/index. Visual Videos 001/002 have published research but local-only external evidence. Video 003 is partial and must remain partial. Recovery archives contain preserved context and prerequisites, not demonstrated disposable backups.

Initial live usage: five-hour **15%**, weekly **2%**. Mid-audit: **21% / 3%**. Paid balance **0**; two reset credits were visible and untouched. Thresholds 90% / 95% were not approached. No precise context/compaction telemetry is exposed; no compaction occurred during this audit, and context pressure did not require an early stop. Initial disk: **8.1 GiB available**, Data volume 99% full. No large media decode, installation, acquisition, or all-media hash sweep was performed.

The metadata census found **60,123 regular files**, **17,234,877,804 logical bytes (16.051 GiB)**. Allocated path sum is 17,383,776,256 bytes; distinct-inode sum is 17,363,398,656 bytes. The 20,377,600-byte difference is repeated hard-link accounting, not recoverable space. APFS clone/snapshot/compression sharing cannot be attributed from st_blocks; allocated figures are upper bounds on exclusive physical storage. Symlinks are listed separately (70), never followed recursively. No stat errors occurred. Inventory is sequential, not a filesystem snapshot.

**Important boundary:** four offline-map recovery subtrees were excluded completely after their names were discovered. No unrelated project content was investigated. Root paths are real directories, not symlinks. Only the canonical root has a .git marker in the enumerated scope. External folders do not inherit Git protection from nearby repositories.

## 2. Folder inventory and classifications

A=canonical preserve; B=research integration candidate; C=private binary archive candidate; D=verified duplicate candidate; E=regenerable/OS candidate; F=historical recovery; G=unresolved protect. These labels never authorize deletion. Mixed folders retain multiple classes; a blanket folder deletion is unsafe.

| Exact path under /Users/ghilmankhan/ | Files | Logical GiB | Allocated GiB | Principal classes |
|---|---:|---:|---:|---|
| `workprojects/youtube-intelligence-os` | 8,266 | 7.070 | 7.088 | A; B/C/G untracked; E environment |
| `workprojects/video data of what if` | 2,876 | 0.657 | 0.662 | B/C; D selected release files; G dependencies outside tree |
| `workprojects/yios-recovery-status` | 2,132 | 0.067 | 0.071 | B/C/F; D four published matches |
| `workprojects/yio-cf-editing-forensics-local-evidence` | 393 | 4.153 | 4.154 | G arrays; B reports; C evidence |
| `workprojects/yios-visual-forensics-install-candidate-2026-10-24` | 45 | 0.000 | 0.000 | F/B; D matching snapshot files |
| `YIOS-local-audits` | 13,319 | 1.556 | 1.584 | B/C/F/G; D copies; E tooling |
| `yios-git-recovery` | 33,092 | 2.549 | 2.631 | F; E dependencies; D secondary duplicates |

Full extension/category counts, largest files/subfolders and Git states are in `INVENTORY_APPENDIX.md` and `inventory-summary.json`. `classified-files.csv.gz` gives every regular file an A–G disposition, reason, SHA status and matching live branch paths. G explicitly covers unexamined content; classification is not a claim of exhaustive semantic review. Only whole-file cryptographic matches establish exact duplicates. Nonmatching bytes can still be semantic derivatives or historical versions.

### Canonical checkout

`/Users/ghilmankhan/workprojects/youtube-intelligence-os` resolves to itself. Tracked: 4,615 files / 1,440,528,195 bytes; ignored: 2,777 / 158,884,035; untracked: 282 / 160,400,385; Git internals: 592 / 5,831,865,316. The untracked roots are `finance-short-02-visual-calibration/`, `productions/`, and `research/casually-finance-script-intelligence/`. These include editable source, owner reference images, narration WAVs, delivery ZIPs and research. They are not expendable merely because untracked. Several match production branches; the per-file comparison records which.

Git storage includes approximately 3,771 MiB under .git/lfs and 1,790 MiB under .git/objects. No LFS prune, repack or garbage collection is proposed now. There is one active LFS-tracked registry DB (pointer OID `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`); remote LFS payload retrieval was not tested. Local materialization does not establish remote recoverability. Partial-clone configuration `[blob:none]` makes lazy fetching a risk; tree reads used `GIT_NO_LAZY_FETCH=1` and no Git fetch was issued.

### External evidence trees

- **What If:** 672.55 MiB. 14 source MP4s total 165,316,917 bytes; all 14 hashes and sizes match the canonical source crosswalk. `video_forensics_output` has 2,276 files / 518,754,899 bytes, including frame evidence, word/audio timing, visual states, assets and retrospective reconstruction instructions. Do not count eight master tables and their per-video inputs as independent evidence.
- **yios-recovery-status:** 68.13 MiB, largely 2,070 frame/image files (65.24 MiB), motion-QA JSON, audio listening excerpts, original recovery inventories and scripts. Four hashed files match live branch-tip blobs; most files have not been fully hashed. No basis for deleting the folder as a historical status dump.
- **CF local evidence:** 4,252.83 MiB: 38 `gray.npy` arrays are 4,264,420,864 bytes (4,066.87 MiB), 38 `cells.npz` total 548,492 bytes, 38 WAVs total 84,429,792 bytes, plus 240 images and 38 ASR JSON files. **There are no MP4s in this tree.** Gray arrays are derived but reproduction recipes/source registration for every member are unverified; retain G. Naming and apparent derivability do not justify E. Older recovery scripts read other scratch layouts (`gray.u8`, `features.npz`), so they do not prove regeneration of these `.npy` files.
- **Skill candidate:** 45 files / 320,212 bytes; the 40-entry checksum manifest and handoff checksum validate. Preserve kit ZIP, installation proposal and original prompts. Do not run install.sh.
- **Local audits:** 1,592.83 MiB. Includes current Finance receipts/source PDFs, 001/002 evidence, partial 003, a 343.9 MiB tooling environment, preserved production files, a 562,372,703-byte local-commit bundle and a 46,780,829-byte unique-object pack. These are not all redundant audit reports.
- **Git recovery:** 2,609.82 MiB scoped to YIOS. `retired-local-files` ~1,012.5 MiB, `retirement-originals-2026-10-14` ~766.3 MiB and `blocked` ~762.5 MiB overlap by provenance, not yet by complete cryptographic comparison. Includes ~989.3 MiB dependencies/cache. Preserve F until archive restoration and local-only history coverage are proven.

A relevant symlink, `video data of what if/chair_test_v2_review/evidence/0921.mp4`, points outside scope to `/Users/ghilmankhan/Downloads/0921.mp4`. Its target is not included in size totals or assumed archived. Python environment links target Homebrew; workbook-runtime node_modules links target the shared Codex runtime. Their external dependencies are not portable folders and were not recursively scanned.

## 3. Current Git state and live publication

Remote: `https://github.com/ghilmanITM360/youtube-intelligence-os.git`.

- Local branch: `research/finance-economics-intelligence`.
- Local HEAD, upstream and independently advertised live branch: **`1adb8129f689207552f0838414e5823e4255bde1`**.
- Live main and PR base: **`08e719264e31ecd82de24f8eeb8f065c08359fe5`**.
- PR #36: OPEN, DRAFT, head **`1adb8129f689207552f0838414e5823e4255bde1`**, not merged. Its title/body still describe the old 966-video checkpoint; do not treat the body as the current ledger.
- Live protected forensic branch: **`090f84b3292a3b6c6e94653a6ef1867726e4ebdd`**. Protected sole writer remains Claude session `873b9a27-ba03-4183-aa61-f82d01f65998` under the supplied owner policy. No checkout, interrupt, retirement, ownership reassignment or write occurred.
- Git worktree list reports only the canonical checkout. This says nothing about unreported sessions, removed metadata, or Machine B's unpushed changes.
- Stash preserved: **`5b6c3042679400b16aa1024b79058b71dade0ab9`**, `On chore/full-local-data-sync-and-senior-health-acquisition: checkpoint doc wip`.

The GitHub connector returned 404 for PR metadata; authenticated read-only `gh` was the successful fallback. `git ls-remote` independently advertised 38 live branch tips. All 38 tip trees were readable locally without lazy fetch; Finance and main trees were independently retrieved through GitHub API and were not truncated. Current branch-tip exact-content comparisons do not prove absence from all historical commits, deleted refs, PR attachments or LFS. Full local/live ref SHAs and commands are retained in `refs.txt`, `live_refs.txt`, `live_pr_ref.txt`, `pr36.txt`, `branch-tree-coverage.json` and `all-live-branch-matches.json`.

**Ownership risk:** repository handoffs claim a later Machine A Finance takeover; the supplied owner policy still names Machine B as sole Finance/expansion/channel-metadata writer. This audit does not resolve that conflict or grant write ownership. Visible agent processes are not ownership proof. Obtain owner confirmation across both Macs before any future branch or production mutation.

| Artifact | Publication / completeness | Local-only dependency / disposition |
|---|---|---|
| Video 001 o3FQcd91MIs | Published on Finance branch; visual-only complete, 76 states / 47 inferred shots | 41 external manifest entries all SHA-valid; source MP4 freshly hash-valid at manifest path; human listening incomplete; B/C preserve |
| Video 002 Uumnx2Fo6cE | Published on Finance branch; visual-only complete, 507 states / 194 inferred shots | 968 external entries all SHA-valid; source MP4 freshly hash-valid; human listening incomplete; B/C preserve |
| Video 003 5umJ63d3rzQ | Absent from current published visual index; partial external checkpoint | Latest manifest 1,770/1,770 PASS; first pass 695 candidates/409 draft states/280 disputes in 8 shards; independent second pass, rebuild and completion gates pending; B/C/G |
| NICK_170 ULkTn-jHBBc | Packet, receipts, thumbnail published at current head; 58 external checksum entries PASS | Local PDFs, source texts, screenshots, calculation/verification evidence remain protected; six source files have exact live-tip matches, not the entire folder |
| Finance ledger/workbook | Fresh GitHub retrieval SHA matches both; local ledger has 966 original rows; current handoff reports 446/1,612 complete | Combined population includes 646 expansion records; limited-evidence statuses do not certify audio/visual editing; native Excel recalculation remains NOT_TESTED |
| What If source contract, promotion index, adapter/orchestrator | Code/contracts published; 10 sources / 8,327 promoted observations documented | External 14-source corpus is required; all 14 source MP4 hashes now checked; no exact hashed corpus file matches any of 38 live tips |
| What If full brain/experiments | 989 checked corpus files have no live-tip blob match; no complete raw brain publication established | B structured research; C media/frames; D individual release duplicates; G any remaining unhashed files |
| CF scratch evidence | 46 hashed files have no live-tip match; arrays not bulk-hashed | G arrays until reproducibility and source originals validated; C evidence archive candidates |
| Production workspaces | Some files match production branches, while current checkout roots remain untracked | Preserve editable/audio/reference/delivery sets; absence from current Finance branch alone is not proof of uniqueness |
| Recovery bundles / old copies | Partial exact matches only; 609 hashed recovery files match live tips | Bundle prerequisites and restoration unresolved; F preserve, not a verified independent backup |

Eight representative artifacts were actually retrieved from GitHub and SHA-256 compared to local bytes, all PASS: both principal visual reports, NICK_170 packet and receipts, current Finance JSONL/workbook, production orchestrator and What If source contract. See `remote-retrieval-verification.json` for exact paths, hashes and byte counts. This establishes recoverability of those exact Git artifacts at the checked SHA, not a full project backup. Source videos, external evidence and LFS were not remotely restored. No private object store was verified.

## 4. Integrity, duplicate evidence and uniqueness limits

The shared primary read budget was **1,073,741,797 bytes**, plus **8,090,929 bytes** for missing small research files; 11,288 paths have fresh SHA-256 receipts, with no in-read size/mtime changes recorded. The separate eight-artifact remote comparison reads ~13 MiB locally/remotely. No full-media decoding occurred. The existing manifest checks produced 8,070 PASS entries, four MISMATCH entries and 1,103 unresolved local-path entries across 35 checksum sources; counts repeat files across historical manifests and are not unique-file totals. JSON manifests were specifically validated for the two releases and two current external visual packages; other JSON hash manifests remain discoverable but are not all semantically revalidated. `manifest-catalog.csv` lists all candidate manifest/checksum names and explicitly marks unchecked ones.

The four mismatches are in older Video 003 checkpoints: three refer to the subsequently extended CONTINUATION_HANDOFF.md, and checkpoint1 also lists its own nonmatching hash. Latest checkpoint4 is fully valid. Preserve old manifests as historical records, not current integrity certificates; do not rewrite them to hide drift.

Most unresolved checksum paths are expected external references when copied checksum files are interpreted from the Git research subfolder: 1,067 occurrences across the two copied visual packages. The current external manifests independently verify all 1,009 external entries. Remaining unresolved entries include 28 installed-skill paths needing their original base directory, seven DS-000027 raw checksum paths requiring base-path resolution, and a missing What If release archive target. None is automatically a proven missing original. `manifest-checks.csv` contains every result; protect unresolved entries as G.

Both 50-entry What If release manifests validate separately. The active brain and release directory share **48 SHA-identical files**, but differ in **BRAIN_MANIFEST.json**, **RELEASE_MANIFEST.json**, and **PACKAGE_AUDIT.md**; one pycache was not hashed. They are not interchangeable directory backups. All eight master tables, DNA docs and recipes match their release counterparts. Preserve both metadata versions until reviewed.

There are **2,808 exact SHA duplicate groups** in the bounded hashed set, with 270,304,250 logical redundant bytes and a **277,671,936-byte (~264.81 MiB) allocated upper bound** after distinct-inode grouping and retaining one group member. Full paths and complete SHA-256 values are in `duplicate-groups.json`. Identical frame bytes at distinct source times may encode distinct evidence positions and must retain their separate provenance even if later stored once. Same name/size without a SHA match remains unresolved.

Example: MASTER_WORDS.csv (`7eb5c0bad045921e03df91f08aa1a5061edc7ab7cb4aec878d188a31ed89a190`, 820,972 bytes) appears in the active master table, legacy duplicate and frozen release. This proves exact bytes, not three independent observations. Likewise the copied published visual reports/ledgers match external counterparts. The largest verified duplicate group consists of the 2,014,758-byte FULL_FRAME_MEASUREMENTS.csv pair. See receipts before choosing any retained copy.

## 5. Channel DNA and production-intelligence preservation map

The future mission is original-video production from user script, voiceover and assets using an explicitly selected reference channel. Current V1 composes evidence-backed plans; it does not establish a general autonomous script-to-finished-video system. No V2 implementation is authorized by this audit.

| Existing evidence | Preserve for | Proposed structured representation |
|---|---|---|
| What If 01_master_data, source index/map and per-video 00_source/01_evidence/02_analysis | Measured state/shot/word/motion/asset/A-V relations | Evidence index keyed by canonical channel, video, source SHA, table/row and release; retain held identities |
| 02_production_dna (7 docs) + DNA_INDEX | Visual, pacing, asset, motion, editing and A-V grammar | Versioned channel-DNA rules with support/denominator, sample scope, confidence and exceptions |
| 03_reconstruction_system + 05_blueprints + 04_patterns | Layer composition, static vs I2V choice, asset transparency, narration-triggered operations | Production recipes with prerequisites, input/output types, operation sequence, timing basis and evidence refs |
| video_forensics_output/*/03_capcut and 04_image_to_video | Retrospective reconstruction specifications | Reference recipes marked retrospective; no automatic claim of unseen-script generalization |
| generalization_tests coffee/heart and revision_1 | Forward-planning experiment, storyboard, prompts, density and executability lessons | Experiment record separating estimated timing, corpus-derived rules, reviewer findings and unexecuted risks |
| chair_test_stage_a | Editable draft JSON, before-edit timeline, edit plan, build script | Historical experiment plus exact source project/media dependencies; preserve original timeline snapshots |
| chair_test_v2_review | Rejected prototype audit, reference fingerprint, frame study, asset/storyboard plans | Negative example / failure taxonomy with evidence refs; do not mark proposed V2 plan as an accepted render |
| releases | Frozen validated research package | Immutable version record + content manifest; differences preserved |
| Visual 001/002 and partial003 | Per-channel visual state grammars and original reconstruction methods | Separate Casual Finance evidence packages; partial003 cannot vote as accepted rules |
| Nick Invests channel-intelligence and Finance packets | Packaging/script/financial-review intelligence | Separate Nick Invests namespace; text completion never implies editing evidence |

Minimal shared record fields: `schema_version`, `channel_id`, canonical channel URL/aliases, `profile_version`, `evidence_video_ids`, source SHA/bytes, timebase/fps where measured, exact row/frame/time locators, `claim_kind` (fact/observation/interpretation/hypothesis), confidence, reviewer/pass, known limitations, completion gates, supersedes/derived_from, recipe inputs/operations/tool versions/asset rights, validation status and storage locator. Store generated-original assets separately from reference frames. For timing, retain both measured intervals and estimates; bind recipes to actual supplied voiceover before production. Counts and channel rules must aggregate unique videos, not repeated frames or duplicate CSV releases.

What If documents themselves disclose absent palette/typography measurements, uncontrolled visual-function vocabulary, mixed motion-confidence labels and no cross-video asset reuse tracking. Do not turn their prose into universal visual laws. The coffee/heart exercise uses estimated narration timing and has high-density opening/closing sections. The chair prototype was explicitly REJECTED; its audit is useful negative evidence, not disposable failure output.

### Skill installation comparison

Installed `/Users/ghilmankhan/.claude/skills/visual-ct-scan` contains 28 files. All 28 SHA-match candidate overlay files. Git's `research/visual-forensics/methodology/visual-ct-scan-skill-snapshot` contains 24 matching files; it omits exactly four `source-prompts/*_ORIGINAL.txt` files. The current project `.claude/skills/visual-ct-scan` and root `CLAUDE.md` do not exist. The candidate's old install instructions are historical proposals, not present authorization. Preserve originals and compare metadata before any future installation; do not overwrite the functioning personal skill. A Claude personal skill path is not, by itself, a Codex skill installation. No installation was performed.

## 6. Smallest canonical structure and documentation proposal

Retain existing data layers and research namespaces. Do not move the working What If source corpus or raw Finance records yet. Proposed additions only after owner review:

```text
youtube-intelligence-os/
  AGENTS.md                      # sole repository rules, unchanged for now
  README.md                      # link to mission + current handoff
  PROJECT_STATUS.md              # current implementation/evidence boundary
  docs/YIOS_MASTER_PLAN.md       # mission + architecture only; links to existing phase/docs
  docs/AI_SESSION_CONTEXT.md     # current writers, exact SHAs, evidence roots, next action
  research/visual-forensics/     # existing per-channel/video evidence packages
  data/intelligence/channels/<canonical-channel-id>/
    channel-dna-v1.json          # reviewed reusable rules, evidence refs and uncertainty
    production-recipes-v1.json   # original asset/animation/edit recipes
    evidence-index-v1.json      # content-addressed local/remote locators + verification
  productions/<project-id>/     # original user inputs + editable outputs, explicit manifest
```

Use existing channel IDs after registry reconciliation; do not guess a new ID for Casual Finance or Nick Invests. Existing `data/manifests`, CH-000004 promotion index, source contract, `docs/WHAT_IF_INTEGRATION_WORKFLOW.md`, `docs/PROVENANCE.md` and research indexes remain authorities for their scopes. Avoid adding competing mission documents under every folder.

`YIOS_MASTER_PLAN.md` should state the permanent original-production mission, facts vs inferred rules, the existing pipeline and future authorized production boundary, per-channel separation and binary storage contract. It should link rather than duplicate Architecture/Phases/Database documents. `AI_SESSION_CONTEXT.md` should be short and replace dated continuation prose as the top-level pointer, while retaining dated original handoffs. Include cross-Mac writer confirmation, open PR/ref SHAs, protected evidence roots, current operation and exact blocker. Do not copy obsolete instructions from historical reports.

Minimal existing-file edits: add two README links; refresh PROJECT_STATUS's current-state paragraph/date with dated evidence; add one research-index pointer for each newly approved package; adjust AGENTS only if the owner explicitly resolves ownership or production scope. Existing PROJECT_STATUS and README contain historical checkpoint paragraphs; label history clearly instead of silently replacing facts. No Markdown or agent instructions were changed in this phase.

## 7. Private binary storage and restore design (proposal only)

No verified shared store was found in the inspected manifests; the visual README explicitly says none is configured. Provider/account inventory and external backups outside scope remain UNVERIFIED. Do not purchase or configure a service yet.

Use an owner-approved private object store or existing private drive, with immutable object keys such as `yios/evidence/sha256/<first2>/<fullsha>/<originalname>` and separately versioned manifests. Preserve originals byte-for-byte; retain source filenames/paths as metadata even when the key is content-addressed. Keep channel/video/project/evidence-role references, SHA256, size, MIME, origin/rights, acquisition time, storage key/version, retention state and verification receipts in Git-safe manifests. Credentials never enter Git. Use portable root variables rather than hardcoded home directories. Raw video must never travel via GitHub.

Archive source videos, voiceovers, reference frames/sheets, source PDFs when unsuitable for Git, editable binary projects and accepted renders. Preserve rejected render/editable history where tied to QA findings. Large scratch arrays can be omitted only after exact regeneration is independently demonstrated and approved; until then archive/protect them too. Dependency binaries are a separate rebuild-environment issue.

Upload verification alone is insufficient. Future acceptance gate: stable pre-copy SHA, byte-preserving copy, destination checksum, independent retrieval to a new destination/device, recomputed SHA, manifest linkage and a report of failed/missing objects. Do not rely on provider ETag as SHA256. Preserve at least the original plus one independently restored copy; stronger redundancy can be chosen by the owner. A same-volume relocation frees no space. On this nearly full disk, use another device/approved storage for restore trials, not a second full local copy. No backup claim or cleanup until restore gates pass.

## 8. Space-recovery plan — cautious, non-additive bounds

| Candidate | Measured upper bound | Present action / realistic uncertainty |
|---|---:|---|
| D exact duplicate groups in bounded set | 264.81 MiB allocated | Actual reclaim 0–264.81 MiB; many frames/copies retain evidence roles; APFS sharing unknown; overlaps F |
| E dependencies + OS metadata across scope | 1,480.8 MiB allocated (about 1.446 GiB) | 0–1.446 GiB; active environments/cache portability and locks must be reviewed; recovered packages may preserve otherwise unavailable runtime versions |
| F historical recovery | yios-git-recovery 2.612 GiB unique-inode allocated, plus audit bundle/pack context | No independently additive approved recovery. Many files overlap E/D; unique originals and bundle prerequisites unresolved |
| G CF gray.npy arrays | 4,066.87 MiB logical | Zero approved reclaim. Potential later only after source+recipe+reproduction proof and archive policy |
| Git .git/lfs and objects | ~5,561.7 MiB logical | Zero approved reclaim; shared history/local-only objects and remote LFS must be validated first |

Do not add these rows. The hard-link path overcount is ~19.43 MiB and is already excluded from unique-inode estimates. No per-file APFS exclusive-extent accounting was available. The only defensible guaranteed reclaim now is **0 bytes**; these are future review bounds. Do not delete entire audit/recovery directories or strip frame chronology to gain small savings.

## 9. Ordered migration plan with validation and rollback gates

1. **Owner review / writer gate:** resolve Finance and forensic ownership across both Macs; record active session IDs and unpushed states. Recheck usage, free disk, full HEAD/upstream/live/PR SHAs and untouched stash. Do not switch branches during an active writer session.
2. **Close bounded evidence gaps:** resolve checksum base paths, original `0921.mp4`/CapCut media dependencies, source paths for all 38 CF scratch sets, and which recovery objects are uniquely local. Preserve manifest history and inspect semantic differences, not just filenames. No media decoding or expensive scans without a separate bounded plan.
3. **Storage selection gate:** owner chooses existing private storage or expressly approves provider/cost. Calculate upload+restore space. Preserve the current original trees until restore acceptance.
4. **Preservation copy gate:** copy immutable binaries and external research to approved durable storage; validate source/destination SHA and independent retrieval. Record failed checks and storage object versions. Never Git-transport raw MP4s.
5. **Controlled Git proposal:** after owner-approved writer access, integrate only reviewed small research/schema/index material, with provenance, canonical channel IDs, licensing/privacy review and explicit partial statuses. Keep original corpus unchanged. Do not bulk-merge research branches or overwrite Finance ledgers.
6. **Portability gate on Machine B:** restore approved evidence by manifest, configure root variables, read published recipes, then run existing validators in an approved environment. Keep 003 partial and all no-audio limits. Verify Git LFS independently if required for consumers.
7. **Documentation gate:** make only the two proposed entry-point documents and minimal links/status corrections; review with existing authorities. No V2 implementation is implied.
8. **Optional cleanup proposal:** produce exact per-path candidates, retained-copy/provenance links, exclusive-space uncertainty and restore receipts. Owner separately authorizes any removal. No deletion commands are supplied by this audit.

Rollback at every gate means stop on any mismatch and continue using untouched original roots; never reset shared refs. For future copied data, retain both old path and verified destination until explicit acceptance. For future reviewed Git changes, rollback through an owner-approved revert PR, not force push. Do not treat a failed test as permission to modify historical evidence.

## 10. Unresolved risks and exact next approved action

- Writer ownership conflict and cross-Mac unpushed work remain unresolved; read-only state cannot settle this.
- Full archival retrieval, remote LFS availability, bundle restore completeness and all historical Git publication are unverified.
- What If source media are hash-valid but SRC01/SRC02 identity joins remain unresolved; two verified identities remain held/unregistered in current contract. Preservation does not authorize registration.
- Video003 first-pass completion is not final review. Its latest checkpoint validates bytes, not analytical correctness.
- NICK170 is published as limited-evidence research, with recorded hosted CI billing blockage and a known pre-existing full-regression failure. This audit did not rerun or repair tests or spend credits; the old PR description must not conceal current limitations.
- The 562,372,703-byte bundle passes `git bundle verify` in the current repository but requires `e25dc63fc101390867ebf1495bba726ba9797fb6` and `31ea9a53a6b4c9a1b74a3478ce16e510fdf06e10`. It is not demonstrated standalone-restorable. Its large pack was not freshly SHA-hashed. Preserve bundle and prerequisite history together.
- All-file uniqueness is not established. Every unhashed file remains G or otherwise protected by its canonical/recovery role. 38 tip-tree comparison cannot rule out historical blobs, provider backups, or semantic overlap.

**Exact next action authorized now:** the owner reviews this external report and classification evidence. The audit stops here. A subsequent bounded preservation-copy/restore pilot for the What If brain and the 001/002 external manifests is recommended only after explicit owner storage/writer approval. Do not begin it automatically, create new worktrees, alter the skill or touch Finance records.

## 11. Continuation handoff

Read this report first, then `INVENTORY_APPENDIX.md`, `classified-files.csv.gz`, `manifest-summary.json`, `manifest-checks.csv`, `remote-retrieval-verification.json`, `all-live-branch-matches.json`, `duplicate-groups.json`, `skill-comparison.json`, `what-if-release-comparison.json`, and `scope.json`. All live/local ref SHAs and source evidence paths are preserved in this same directory. Source media paths for 001/002 are in their published portable manifests; 003's exact path/hash are in its external CONTINUATION_HANDOFF.md and this audit's manifest-checks.csv. Four original skill prompts remain in the personal skill and external candidate.

The original task is Phase 0 discovery/planning only; nothing in the proposed architecture or migration sequence is permission to execute it. Canonical root, external corpus, forensic evidence, stashes, ignored files and recovery history must remain protected. Do not restart completed Finance or visual research based on stale handoff sections. Recheck resources and the current owner policy before the next approved operation.

The audit scripts are retained for reproducibility, not automatic execution: `inventory.py`, `git_audit.py`, `verify.py`, `supplement.py`, `branch_compare.py`, `retrieval_check.py`, `report.py`. They create outputs only in this external report directory; source trees are read-only. Do not blindly rerun scripts that overwrite report artifacts; make a new dated audit directory if approved later. `SHA256SUMS` seals this audit's own outputs; it does not turn local source evidence into a remotely backed-up copy.

### Final preservation verification

Final HEAD, Git status, stash and advertised remote refs match the initial snapshot. Re-statting all 60,123 inventoried regular-file paths found 0 changes in size, mtime or inode. This is metadata stability evidence, not an atomic filesystem snapshot or a fresh checksum of every file.

Final live resource check: five-hour 24%, weekly 4%, paid credits 0; no reset/spend. Final disk receipt: resource-gates.json.
