# Live remaining-work audit — 2026-10-11

This audit distinguishes the canonical main branch, the broader channel registry, the historical inventory catalog, branch-only research, and local source material. Evidence was recovered live from Git/GitHub, read-only SQLite queries, existing normalized evidence and targeted research artifacts. No raw evidence, catalog, snapshots or stage was modified. No Graphify, paid collection, background watcher or subagent was used.

Machine-readable evidence: [live evidence](remaining-work-2026-10-11/live-evidence.json), [packaging commit disposition](remaining-work-2026-10-11/packaging-unique-commits.csv), [identity candidates](remaining-work-2026-10-11/identity-candidates.json). Exact pending-registration implementation is isolated in [PR #17](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/17).

## Canonical Git and CI

- Local main and origin/main: `c2d88eb533465f790f44ff14f72e95d066e82b96`; default branch is main. The owner checkpoint is current main, not merely an ancestor. Main was clean and 0 ahead/0 behind at audit start.
- PR #16: MERGED, merge `c2d88eb`, head `a3c1fca`, base `06d374e`, merged 2026-10-10 00:45:39 UTC. Repository validation run `38010428097` on exact main SHA completed successfully: 438 passed, 1 skipped. Existing green tests were not rerun for reassurance.
- No open PR existed at audit start. PR #17 was created during this session; it changes registration behavior and has its own CI. No merge is authorized by this audit.
- Other worktrees preserved: thumbnail research local `ba3e734` (13 commits behind its own remote) has an untracked handoff; expansion `814a027` has a modified research script; integration `c1c3bb8` is clean. A `/private/tmp/wt-integration` entry is prunable because its path is absent; it was not deleted. One historical stash remains untouched.
- Before session branches, remote refs not contained in main were thumbnail research (48 unique commits, main has 21 commits absent from research), repository-health-remediation (one historical documentation commit), and `ui/v1` (historical UI handoff). Unique local backup/research branches were preserved; no claim that their names imply new canonical capability. The canonical integration/data branches are already ancestors of main. The old UI handoff does not authorize V2.

## PR #11–#16 reconciliation

All six merge commits are canonical ancestors. File lists and full head/base/merge SHAs are in live-evidence.json. Conclusions below come from source/tests and generated evidence, not titles.

| PR | Head / merge | Files and purpose | Capability / remaining gap | Relevance / supersession |
|---|---|---|---|---|
| 11 | aff815e / e43e2d9 | promote_what_if_forensics.py, orchestrator, stage/orchestrator tests, index/freshness | Deterministic, validated promotion and index linkage. This PR alone did not prove value consumption. | DONE; initial linkage supplemented by 13, not removed |
| 12 | 89ecee5 / 3c2fa06 | stage script/tests, completion plan | Durable ignored stage lifecycle with preserved creation timestamp and manifest checksum. | DONE; still active |
| 13 | 89e2acb / f79479a | query script/tests, orchestrator, dated JSON/Markdown plan, freshness | Actual eight-table consumption and source-backed Editing/Visual guidance; missing stage explicit, drift rejected. | DONE; supersedes index-only interpretation of 11 |
| 14 | 5afb803 / a084c57 | README, status, Architecture, DECISIONS, Phases, Security, contract/workflow, safety audit | Lifecycle, portability and privacy documentation. | DONE; current acquisition wording partially stale after 16 |
| 15 | 44f24a0 / 06d374e | provenance, staging/promotion, update, rollback, privacy entry points | Accessible update/rollback process; immutable source retention. | DONE; still active |
| 16 | a3c1fca / c2d88eb | status, crosswalk contract, two official identity evidence JSON files | Two exact owner/video identities independently verified; neither registered. | DONE; supersedes ownership/API uncertainty, not transcript gaps |

Promotion, durable provenance, consumption, lifecycle documentation, and rollback/update are implemented. They are not remaining implementation tasks.

## What If end-to-end trace

Current canonical identities: 83. Source contract: 14 sources, 10 eligible, 4 held. Existing durable lifecycle records 8,327 accepted and 3,258 held observations (11,585 total), zero rejected. Original 14/14 media hash verification is reused; media was not rehashed. Neither the accepted corpus nor snapshots were regenerated. The current query revalidated stage checksums, exact identities and index agreement without writing outputs.

Trace chosen: `SRC06`, slug `what_if_the_moon_were_made_of_protons`, exact canonical YouTube ID `mEUqVgGf4e0`. The MP4 remains external; the reviewed manifest records its relative path/hash. Crosswalk joins only exact approved ID. Eight source MASTER tables normalize through source_adapters/what_if_forensic_brain.py and stage_what_if_forensics.py into ignored JSONL with row IDs, CSV row numbers, timing, confidence, release, media hash and transformation version. promote_what_if_forensics.py validates and indexes that stage. query_what_if_forensics.py aggregates the values; run_youtube_intelligence.py attaches matching guidance to the existing Editing/Visual blueprint.

| Layer | Input / output keys | Consumer and coverage | Status |
|---|---|---|---|
| External source / manifest | relative_media_path, sha256; SRC06, slug, canonical_youtube_video_id | Source contract/adapter tests; existing 14/14 recorded verification reused | FULLY_CONSUMED; current external bytes not freshly rehashed |
| MASTER_SHOTS | START_SEC/END_SEC; shot_pacing.mean_duration_seconds | 9 shots, sampled mean 9.787 s; SHOT_PACING hypothesis; query pacing test | FULLY_CONSUMED |
| MASTER_STATES | VISUAL_FUNCTION/CAMERA_STATE and timing; visual_state_progression | 32 states; opening storyboard guidance; eight-table test | FULLY_CONSUMED |
| MASTER_MOTIONS | ACTION/RELATIONSHIP; motion_types/motion_relationships | 24 events; MOTION_SEQUENCE guidance with exact row citations | FULLY_CONSUMED |
| MASTER_ASSETS | TYPE; asset_types and recurrence | 27 assets; ASSET_PLANNING guidance with row citations | FULLY_CONSUMED |
| MASTER_AUDIO_EVENTS | TYPE and timing; audio_event_timing | 2 windows; AUDIO_EVENT_TIMING guidance | FULLY_CONSUMED |
| MASTER_AUDIO_VISUAL_SYNC | OFFSET_MS; narration_visual_sync | 80 events, signed median 39 ms; alignment hypothesis and signed-offset test | FULLY_CONSUMED |
| MASTER_WORDS/SENTENCES | timing; opening counts and references | 333 words / 18 sentences for this video; opening visual guidance | FULLY_CONSUMED |
| Production plan | editing.forensic_consumption / blueprint.forensic_guidance | Canonical dated OP-001 JSON/Markdown: 4 videos, 2,381 observations, 24 hypotheses; blueprint/missing-stage/drift tests | FULLY_CONSUMED |

The current single-video read-only query returned 525 observations and six hypothesis kinds. These are source-declared sampled records, not complete timelines, causal performance effects or additional channel samples. Older report_editing_visual_intelligence outputs are preserved; normalized enrichment happens in the unified production plan. The adapter is release/channel scoped; existing ordinary-channel fallback remains unchanged. Broader arbitrary-release ingestion is not claimed.

## Held identities and transcript contract

9VG0yqq_PHM and X97DDWvxaqQ: IDENTITY_VERIFIED, TRANSCRIPT_BLOCKED, NOT_REGISTERED. PR #16 evidence proves ownership independently of transcript availability. Official/public caption attempts in that evidence yielded empty bodies; official captions.download was not retried as a public transcript API.

The schema does **not** require a transcript for a video. Migration 002 separates both entities; the older structured importer accepts a workbook-only video. The complete loose-pack invariant exists in the supplied importer. Outcome B is therefore supported by repository architecture. [PR #17](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/17) adds explicit pending-ID semantics to that existing workflow, preserves strict defaults and provenance validation, and creates no fake transcript row. It does not change the canonical catalog or promote the held sources. A reviewed metadata packet is still required before registration. Null public metrics must not be fabricated to fit an export format.

Repository transcript filenames and ZIP member names were searched for both exact IDs: no matching acquired transcript package was found. Existing external MASTER_SENTENCES has 25 sentence rows for SRC03 and 38 for SRC11, but these remain derived forensic declarations, not accepted raw caption evidence. Existing registration parsing expects the supplied transcript header/body contract. No forensic words were relabeled as captions. Exhaustive alternate historical archives outside supplied roots are UNKNOWN.

SRC01 candidate U8F7UNK9jco and SRC02 candidate qu8nx1qUwEU now return official player metadata for the correct channel and independently matching question content. Official xkcd articles [42](https://what-if.xkcd.com/42/) and [141](https://what-if.xkcd.com/141/) corroborate the respective subjects. However, local durations are 129.980544 and 123.994558 seconds versus public 166 and 170 seconds. Exact edit/version and audiovisual correspondence remain unproved. Both stay HELD_UNRESOLVED; crosswalk unchanged. This is stronger candidate evidence, not a canonical identity decision.

## Packaging research reconciliation

Remote `research/thumbnail-forensics-complete-2026-10-04`: `aaa32b580131adfe8ab83bf3a46814d3aadee32d`. Local worktree is stale, dirty only through an untracked handoff, and was not switched or updated. No open integration PR existed. None of the 48 unique commits is canonical merely because it was pushed.

Recomputed from actual remote CSV/JSON rows: 2,303 analyst title rows; 518 unique verified thumbnail IDs (510 legacy plus eight channel additions); 518 unique package IDs; 121 unique package-image QA samples (110 legacy plus nine Genius and two Hypothetically reviews). Queue: 75 channels, 1 COMPLETE, 42 IN_PROGRESS, 3 PARTIAL_DATA, 29 IDENTITY_ONLY. Current channel Hypothetically: 5 complete / 39; next EvuEMhh7SSk. The dashboard folds partial-data channels into 45 in-progress; those labels must not be silently treated as equivalent.

Composite uses the existing dashboard's four-term arithmetic, not channel completion: (2303/2303 + 518/2698 + 518/2282 + 121/2282)/4 = 36.80028995412579%. Thumbnail denominator includes 414 unregistered identity images; this is not progress over canonical videos alone. Forty thumbnail drafts remain separately excluded; one is structurally invalid. Full visual QA is false.

Genius History: PUSHED_RESEARCH_ONLY, 10/10 complete, closure commit `73a7a45649ff42fb60f10be592326370f140f8ab` is a remote ancestor but not a main ancestor. Result has three best, three worst, three strongest analyst-rated, three weakest analyst-rated cases, two counterexamples and three matched comparisons. Ten source images match their recorded hashes in the research worktree; all ten are absent from the canonical checkout. Content promises remain NOT_CHECKED. Nine fresh QA records and one historical sample are disclosed.

Integration gate remains PARTIAL:

- The summary's source hash ledger matches 68/69 artifacts. `audit-batch-B002-03.json` has a stale expected hash (actual `4d7d487d...`). This does not establish corrupted raw source; it invalidates an unconditional dashboard source-unchanged claim.
- Legacy master-packages/package-forensics tables still cover 510; the channel overlays cover 518. They must be reconciled before canonical ingestion.
- The Genius qa.json channel_result still says IN_PROGRESS although final channel-results and progress say COMPLETE. Preserve historical review events; correct only current closure status.
- Workbook ZIP CRC and 11-sheet structure pass; dashboard formula caches exist. Some detail formulas have empty caches. Current visual QA, recalculation and workbook/queue/JSON equality were not rerun; old visual-review claims are historical evidence, not a fresh pass.
- The branch includes draft, partial and generated artifacts. Its public-thumbnail source assets are local only. Current cross-branch source dependency closure is incomplete.

Smallest safe integration: retain the branch; repair current summary/hash/closure wording there or in an isolated candidate; select validated title/thumbnail/package rows with explicit version and provenance; include a durable, owner-policy-compatible locator for each required thumbnail; exclude drafts and stale generated rollups; validate the selected subset and build registry-compatible availability rather than merging 286 files wholesale. Commit dispositions are conservative: validated Genius closure VALID_CURRENT, checkpoint rollups GENERATED_ONLY, mixed units PARTIAL until their dependency gates pass. PRIVATE/BROKEN/SUPERSEDED are not assigned without evidence.

## Global project matrix

Counts are verified at the canonical SHA unless explicitly marked branch/local. Last updated denotes source evidence time, not a fresh acquisition.

| Area / metric | Count | Source | Verified / last updated | Canonical? | Remaining gap |
|---|---:|---|---|---|---|
| Git / CI | 438 passed, 1 skipped | main run 38010428097 | Live GitHub / 2026-10-10 | Yes | PR #17 review/CI |
| Datasets | 33 registry; 26 inventory | separate SQLite datasets tables | Read-only query / 2026-09-28 | Yes, different populations | Historical partial rebuild remains |
| Channels | 75 registry; 10 inventory | separate channels tables | Read-only query / registry generation 2026-09-28 | Yes, different populations | 29 registry identity-only channels |
| Videos | 2,303 registry; 667 inventory | separate videos tables | Read-only query / 2026-09-28 | Yes | Two verified What If IDs unregistered |
| Transcripts | 2,291 real + 12 placeholders registry; 666 AVAILABLE + 2 UNAVAILABLE inventory rows | transcript tables | Read-only query / 2026-09-28 | Yes | No silent summation; unavailable/placeholder evidence distinct |
| Thumbnails | 1,907 registry URL references; 479 inventory thumbnail_evidence rows | videos/thumbnail_evidence | Read-only query / 2026-09-28 | Yes, metadata | Exact repo-wide local-thumbnail semantic count UNKNOWN; images/frames are not all thumbnails |
| Local thumbnail research | 2,282 primary references; Genius 10/10 local hashes | branch universe and channel source rows | Targeted branch query/hash / 2026-10-05 | No | Local source dependencies absent main |
| Title audits | 2,303 | branch analyst CSV | Row count / 2026-10-05 branch | No | Integrate validated subset |
| Package audits | 518 | legacy package JSON plus channel overlay | Unique Package_ID union / 2026-10-05 branch | No | Legacy rollups still 510 |
| Package QA | 121 sampled | legacy and channel review records | Unique mapped image union / 2026-10-05 branch | No | Full visual QA not complete |
| What If observations | 8,327 eligible; 3,258 held | durable stage/index | Current read-only query agreement / stage 2026-10-09 | Index yes; stage local | Four held sources |
| First-party Analytics | 0 formal normalized imports | ignored normalized first-party path; capability report | No populated import path / audit date | READY, not ingested | Real authorized exports; historical private-derived artifacts are separate |
| Knowledge corpora | 3 inventory class-A datasets; 17 document_records in DS-000011 | datasets/document_records | Read-only query / historical sources | Yes | Other corpus document-level registration/coverage UNKNOWN |
| Generated intelligence | 6 plan JSON artifacts; 600 registry layer/channel coverage rows | data/intelligence/plans; intelligence_coverage | File/table counts / plans through 2026-10-09 | Yes | 235 DATA_READY, 335 NOT_AVAILABLE, 7 PARTIAL, 23 VALIDATED are capability states, not independent analyses |
| Open research | 48 packaging unique commits; expansion local edit | Git refs/worktrees | Live / audit date | No | Preserve and isolate validation units |
| Privacy | 7 audio, 251 frames, 5 previously classified private-derived files | tracked file census and safety review | Media counts live; private-file classification reused / 2026-10-09 | Pre-existing | Private repository only; owner decision before broader sharing/history action |
| Historical artifacts | partial rebuilder, preserved inventory DB | catalog README, CI rebuilder | Canonical CI exercises partial rebuild | Yes | Not all historical inventory is source-rebuildable; do not replace DB with partial rebuild |

No tracked MP4, raw Studio-named export or newly introduced What If raw/private path was found. Secret-pattern scan found zero tracked matches. The scanner does not prove absence of every possible secret format or private content inside archives. Existing private-derived artifacts remain PRIVATE_REPO_ONLY; external MP4s/staging/public thumbnail recovery remain LOCAL_ONLY. New code/docs/contracts are PUBLIC_SAFE subject to the repository's existing access policy. No history rewrite, raw deletion or visibility change occurred.

## Remaining-work matrix

| ID | Area / issue | Evidence / status | Priority | Source-fixable? / external blocker | Risk / scope | Recommended action |
|---|---|---|---|---|---|---|
| RW-01 | Privacy retention/access | Existing 7 audio/251 frames/5 private-derived files; BLOCKED_OWNER_DECISION | P0 before public/broader sharing | No autonomous purge; owner/archive decision | High / separate migration | Keep private; preserve; decide access/archive before removal |
| RW-02 | Identity/transcript conflation | Schema independent; strict supplied importer; PARTIAL, fix in PR #17 | P1 | Yes; source packet still needed for real registration | Medium / bounded importer+validator+coverage | Review green PR #17; register only reviewed packets |
| RW-03 | Packaging research stranded | 48 branch-only commits; 10/10 Genius source hashes; PARTIAL | P1 | Yes; source dependencies local | Medium / selected integration | Isolate validated rows; reconcile rollups and locators |
| RW-04 | Packaging dashboard drift | 68/69 hashes, 510/518 rollups, stale Genius qa status; PARTIAL | P1 integration prerequisite | Yes; no paid blocker | Low-medium / generated/current sections | Correct generator/current state; validate workbook and equality |
| RW-05 | Two verified What If registrations | Identity proven; no reviewed registration workbook or raw transcript; BLOCKED_EVIDENCE | P1 | Partly; verified metadata packet required, no paid API necessary | Medium / data PR | Build reviewed packet with nullable missing observations; no invented metrics |
| RW-06 | SRC01/SRC02 exact source joins | Public content matches, duration differs; PARTIAL | P2 | Investigation possible; exact audiovisual corroboration missing | Medium / bounded research | Keep held; compare independent timing/visual content |
| RW-07 | Current documentation | API/ownership wording stale after 16; DONE in audit-doc branch | P2 | Yes | Low / current sections | Review documentation PR; preserve history |
| RW-08 | Formal first-party exports | Capability ready, no formal imports; BLOCKED_EXTERNAL_EVIDENCE | P2 | No without authorized owner exports | Private / ingestion | Obtain genuine exports; use existing file workflow |
| RW-09 | Historical reconstruction | Partial rebuilder intentionally incomplete; PARTIAL | P2 | Some sources unavailable | Medium / separate provenance recovery | Preserve DB; recover only evidence-backed missing registrations |
| RW-10 | Packaging channel expansion | Hypothetically 5/39; other queue channels incomplete; NOT_STARTED/PARTIAL | P3 | Yes where source data exists | Research scope | Continue next exact QA video; do not redo Genius |
| RW-11 | Robust cross-niche strategy claims | Only 2 channels/niche; BLOCKED_EVIDENCE | P3 | No code defect proved | Research / wider independent coverage | Expand evidence before upgrading robustness |
| RW-12 | Exhaustive local thumbnails and corpus coverage | Metadata/frame mix lacks semantic census; UNKNOWN | P2 | Yes, bounded provenance-safe inventory | Low / audit tooling | Count canonical thumbnail identities separately from image occurrences |

DONE: source contract, adapter, staging, promotion, actual downstream consumption, lifecycle/update/rollback, independent identity evidence, V1 intelligence within declared coverage. These must not be rebuilt.

## Work executed and continuation

Highest evidenced source-fixable core issue selected: RW-02. Commits `35c2ddb` and `c046c1f` were pushed to `codex/transcript-pending-registration`; PR #17 contains importer, versioned validator, coverage reporting, 12 regression tests and contract documentation. Sparse identity packets retain null metrics, subscriber counts and unclassified content format; populated values still require provenance. RED initially demonstrated the missing pending-ID interface. Final local full suite: 451 passed; focused registration/structured tests: 31 passed. Ruff, secret scan and whitespace checks passed. CI and owner review are required before merge. No canonical data was changed and neither held ID was promoted.

Audit and current documentation are a separate atomic unit, not bundled into the registration code PR. No packaging analysis or historical acquisition was repeated. Next actions: review PR #17; complete a nullable-metadata source packet before real held-ID registration; repair packaging rollup/hash/source dependency closure and prepare a selected integration PR. The owner has authorized execution and PR preparation, not an automatic merge.

Resource checks: start 0% short-term / 47% weekly; latest recorded 18% / 50%. No real context warning. Terminal-output truncation was not treated as exhaustion. Final status: READY_FOR_OWNER_REVIEW, canonical healthy with work remaining.

## Follow-up review and execution — 2026-10-11

This section updates current work without replacing the audit baseline above. Main remains `c2d88eb533465f790f44ff14f72e95d066e82b96`. PR #17 review found a hook/script inner-join gap: an identity without a transcript was dropped and then rejected as a corpus mismatch. Commit `842e2e36de7680ffa1633caa5e7204d2718bee6e` changes that join to retain identities, reports unavailable evidence and skips unsupported analysis. Two additional RED/GREEN regressions cover pending identity and pending-only report generation. Existing canonical rows are identical under both joins; only the affected freshness fingerprint was updated. Full local suite: 452 passed, 1 skipped. Exact-head CI run 38081398117 passed. PR #17 is merge-ready, with owner approval still required.

PR #18 baseline counts remain correct and distinct: registry/inventory datasets 33/26, channels 75/10, videos 2,303/667; registry transcripts 2,291 real plus 12 placeholders; formal first-party imports zero; knowledge datasets three and registered document rows 17. The 518 packaging and 121 QA counts remain research-only. Neither verified What If ID is registered. A reviewed metadata packet now preserves exact identity, source hashes, publish time and explicit pending/unknown transcript, metrics and format status. It is ready for source-workbook materialization after PR #17 becomes canonical. No catalog or source crosswalk changed.

Fresh packaging checkout exposed **67/69** matching dashboard hashes, versus the previous environment's 68/69: the current committed registry LFS bytes also differed from the dashboard's uncommitted historical hash. The audit wording above records the earlier environment, not a fresh clean-checkout guarantee. The two causes are now recorded explicitly. The B002-03 mismatch is a legitimate QA correction acknowledging tiny plaza figures in commit 3ae5c5e. The registry's current LFS pointer and validation provide the committed source truth. No DB was selected from the research branch for integration.

The 510/518 root cause is proven: legacy generators globbed only top-level wave audits, omitting eight Genius History channel-overlay packages. A shared QA-gated exact-ID union repairs master/package rollups and excludes unverified drafts. Rebuilt totals: 2,303 titles, 518 verified thumbnails, 518 packages and 121 sampled QA; hash registry 69/69. Repair is isolated on `codex/packaging-rollup-repair-2026-10-11`. Original research branch remains preserved.

The selected integration branch starts from current main: `integration/packaging-forensics-validated-subset-2026-10-11`. It contains only the completed Genius History packet: ten title/thumbnail/package records, nine sequential reviews and one historical sample, channel rankings/counterexamples/matched comparisons, exact original file/row provenance and a raw-image-independent validator. The other 508 packages, 2,293 title audits, partial drafts, raw images, old generated databases/dashboard checkpoints and unrelated private material are excluded. A whole-branch merge remains unsafe.

Current matrix: RW-02 SOURCE_FIX_RESOLVED_IN_PR17 / OWNER_MERGE_DECISION; RW-03 VALIDATED_GENIUS_SUBSET_PREPARED / REMAINING_RESEARCH_PARTIAL; RW-04 GENERATOR_AND_HASH_REPAIRED / WORKBOOK_VALIDATION_REQUIRED; RW-05 METADATA_PACKET_PREPARED / PR17_AND_IMPORT_WORKBOOK_PENDING; RW-06 EXTERNAL_EVIDENCE_BLOCKED, SRC01/SRC02 remain HELD_UNRESOLVED; RW-07 CURRENT_DOCS_UPDATED_IN_PR18. RW-01 remains OWNER_DECISION, without blocking safe source work.

Privacy decision scope remains the seven audio files and 251 frames enumerated in the existing safety review, plus these five private-derived files: Decode_Your_Heart_Analytical_Workbook.xlsx, Decode_Your_Heart_Forensic_Report.docx, Decode_Your_Heart_Research_Checkpoint.json, Decode_Your_Heart_Video_Evidence_Register.json and HANDOFF-2026-09-28.md under docs/research/decode-your-heart-2026-09-27/. Recommended options are restricted private retention or an owner-approved relocation/sanitization plan with an explicit separate history decision. No deletion, visibility change or history rewrite is proposed by this work.

Selected integration committed/pushed as `256104e` and opened in [PR #19](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/19). Local full suite: 444 passed, 1 skipped; six focused packet regressions. Registry/dataset validation, LFS fsck, compileall, Ruff and secret/whitespace checks passed. PR #18 local full suite: 439 passed. Official xkcd articles were rechecked for SRC01/SRC02: subject corroboration remains insufficient to prove exact local audiovisual correspondence; both stay held.
