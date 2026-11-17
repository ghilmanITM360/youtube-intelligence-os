# Individual Branch Audit

One section per branch (75). Evidence: `git log`, `git diff --name-only <merge-base>..<tip>`, `git diff --numstat` for code paths, containment via `git merge-base --is-ancestor`, PR and CI metadata from `gh`. Code on research branches is mostly evidence-builder scripts; branches that change shared code (`scripts/`, `tests/`, `.github/`) are flagged **[code]**.

Reading guide: *Purpose / completeness / unique value / risks* are reviewer judgements from the commits and file paths, marked as such. Counts are measured.


## Group: Baseline

### `main`

- **Tip** `e96f7f8f` · 2026-11-17 · ghilmanITM360 · LR · vs main +0/-0 · merge-base `e96f7f8f` · 0 files · PR none · CI success (2026-11-17)
- **Local vs origin**: local 0 ahead / 3 behind
- **Purpose**: Canonical baseline; CI runs on push.
- **Completeness**: V1 complete per AGENTS.md; CI green 2026-11-17.
- **Unique value**: All merged work (PRs #1-#19, #48, #51).
- **Risks**: Local `main` is 3 commits behind `origin/main`.
- **Recommendation**: Fast-forward local main (`git pull --ff-only`).


## Group: Casually Finance lineage

### `cleanup/yios-phase2-batch1`

- **Tip** `34a79e46` · 2026-11-10 · ghilmankhan · R · vs main +243/-6 · merge-base `08e71926` · 6947 files · PR none · CI no run
- **Stacked on** `research/casually-finance-consolidated` (+1 commits)
- **Areas changed**: `research/visual-forensics` (2229), `data/raw` (1223), `data/extracted` (1029), `research/casually-finance-editing-forensics` (992), `research/finance-economics-intelligence` (832), `research/casually-finance` (414), `research/casually-finance-success-playbook` (163), `knowledge` (30)
- **Commits** (237 non-merge since merge-base; latest first): docs: add YIOS start-here index and Phase 2 batch 1 consolidation maps; docs: add ASR proper-noun pilot note to Casually Finance hub; docs: add Casually Finance hub (index, ASR transcripts, script intelligence); Casual Finance visual CT_SCAN milestone 15/15: text-only artifacts for 15 videos
- **Purpose**: Phase 2 consolidation batch 1: START_HERE index + Casually Finance hub on top of the consolidated CF branch.
- **Completeness**: Leaf of the CF lineage (243 ahead, 73 exclusive per 2026-11-17 audit).
- **Unique value**: Casually Finance hub, ASR transcripts index, consolidation maps.
- **Risks**: Conflicts with main in README.md, docs/START_HERE.md, consolidation files (PR #48 already merged a draft of these).
- **Recommendation**: Integrate: rebase docs onto main, keep evidence on pinned branch.

### `codex/casually-finance-forensic-research` [code]

- **Tip** `043b85bf` · 2026-10-13 · ghilmankhan · LR · vs main +54/-6 · merge-base `08e71926` · 2257 files · PR #21 OPEN · CI no run
- **Contained by** `research/casually-finance-consolidated` (+188), `cleanup/yios-phase2-batch1` (+189)
- **Areas changed**: `data/raw` (1223), `data/extracted` (1029), `.gitattributes` (1), `"data` (1), `docs/CASUALLY-FINANCE-FORENSIC-RESEARCH-2026-10-12.md` (1), `scripts/validate_dataset_ledgers.py` (1), `tests` (1)
- **Commits** (54 non-merge since merge-base; latest first): research: document japan transmission and conditional mechanisms claim verification; research: document fiscal interviews and auction chronology claim verification; research: document crypto treasury and equity-return claim verification; research: document spacex index-exposure claim verification
- **Purpose**: Casual Finance corpus + production DNA + claim verifications.
- **Completeness**: Contained by consolidated branch.
- **Unique value**: None beyond descendants.
- **Risks**: Adds 1,223 data/raw files.
- **Recommendation**: Close #21 in favour of consolidated branch.

### `codex/casually-finance-knowledge-navigation`

- **Tip** `f4dc5d14` · 2026-10-28 · ghilmankhan · R · vs main +1/-6 · merge-base `08e71926` · 5 files · PR none · CI no run
- **Contained by** `research/casually-finance-consolidated` (+241), `cleanup/yios-phase2-batch1` (+242)
- **Areas changed**: `research/visual-forensics` (2), `README.md` (1), `docs/TWO_MAC_WORKFLOW.md` (1), `docs/intelligence` (1)
- **Commits** (1 non-merge since merge-base; latest first): docs: navigate Casually Finance forensic evidence across Macs
- **Purpose**: Two-Mac navigation doc for CF evidence.
- **Completeness**: Contained by consolidated branch.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete after consolidated lands.

### `research/casual-finance-inventory-scoped`

- **Tip** `4e7c4260` · 2026-11-06 · ghilmankhan · R · vs main +1/-6 · merge-base `08e71926` · 10 files · PR #47 OPEN · CI success (2026-11-06)
- **Contained by** `research/casually-finance-consolidated` (+241), `cleanup/yios-phase2-batch1` (+242)
- **Areas changed**: `research/casually-finance-video-inventory` (10)
- **Commits** (1 non-merge since merge-base; latest first): research: Casual Finance video inventory, scoped from PR #37
- **Purpose**: Scoped CF inventory (alternative to #37).
- **Completeness**: Contained by consolidated; CI green.
- **Unique value**: None beyond descendants.
- **Risks**: -
- **Recommendation**: Close #47 and #37 together.

### `research/casually-finance-consolidated`

- **Tip** `9a4023af` · 2026-11-09 · ghilmankhan · R · vs main +242/-6 · merge-base `08e71926` · 6736 files · PR none · CI no run
- **Stacked on** `research/casually-finance-video-inventory` (+156 commits)
- **Contained by** `cleanup/yios-phase2-batch1` (+1)
- **Areas changed**: `research/visual-forensics` (2027), `data/raw` (1223), `data/extracted` (1029), `research/casually-finance-editing-forensics` (992), `research/finance-economics-intelligence` (832), `research/casually-finance` (414), `research/casually-finance-success-playbook` (163), `knowledge` (30)
- **Commits** (236 non-merge since merge-base; latest first): docs: add ASR proper-noun pilot note to Casually Finance hub; docs: add Casually Finance hub (index, ASR transcripts, script intelligence); Casual Finance visual CT_SCAN milestone 15/15: text-only artifacts for 15 videos; Casual Finance Video006: close10timingrows, specifyG005/G006, publish priorreceipts
- **Purpose**: All CF branches consolidated + visual CT scans 15/15.
- **Completeness**: Contained by cleanup/yios-phase2-batch1; pinned by START_HERE.
- **Unique value**: Pinned evidence commit 9a4023af.
- **Risks**: -
- **Recommendation**: Keep as pinned evidence branch.

### `research/casually-finance-success-playbook` [code]

- **Tip** `fb1e56d0` · 2026-10-13 · ghilmankhan · LR · vs main +57/-6 · merge-base `08e71926` · 2420 files · PR #28 OPEN · CI no run
- **Contained by** `research/casually-finance-consolidated` (+185), `cleanup/yios-phase2-batch1` (+186)
- **Areas changed**: `data/raw` (1223), `data/extracted` (1029), `research/casually-finance-success-playbook` (163), `.gitattributes` (1), `"data` (1), `docs/CASUALLY-FINANCE-FORENSIC-RESEARCH-2026-10-12.md` (1), `scripts/validate_dataset_ledgers.py` (1), `tests` (1)
- **Commits** (57 non-merge since merge-base; latest first): research: render original finance pilot and document quality gaps; research: deliver Casually Finance analysis in Word and Excel; research: normalize generated CSV and preserve upstream runtime bytes; research: prove original SVG asset reuse with deterministic eight-second demo
- **Purpose**: CF success/production playbook, Remotion pilot, SVG asset factory.
- **Completeness**: Contained by consolidated; PR #28 targets a codex branch.
- **Unique value**: Remotion/HTML demo (only frontend-like code in repo).
- **Risks**: -
- **Recommendation**: Close #28 into consolidated.

### `research/casually-finance-video-inventory`

- **Tip** `1adfdeb9` · 2026-10-19 · ghilmankhan · LR · vs main +86/-6 · merge-base `08e71926` · 880 files · PR #37 OPEN · CI failure (2026-10-19)
- **Contained by** `research/casually-finance-consolidated` (+156), `cleanup/yios-phase2-batch1` (+157)
- **Areas changed**: `research/finance-economics-intelligence` (832), `knowledge` (30), `research/casually-finance-video-inventory` (10), `reports` (7), `docs/research` (1)
- **Commits** (86 non-merge since merge-base; latest first): research: Casual Finance complete video download inventory; chore(research): audit investing problem video; docs(research): checkpoint LDN source review; chore(research): audit two Nick Invests videos
- **Purpose**: CF complete download inventory (stacked on old finance audits).
- **Completeness**: Contained by consolidated; CI failed.
- **Unique value**: None beyond descendants.
- **Risks**: Drags 832 finance files.
- **Recommendation**: Close #37 (superseded by #47 + consolidated).


## Group: Data

### `data/ds-000011-supplement-2026-11-11`

- **Tip** `97eef476` · 2026-11-11 · ghilmankhan · LR · vs main +1/-3 · merge-base `fd029485` · 7 files · PR none · CI no run
- **Areas changed**: `data/raw` (7)
- **Commits** (1 non-merge since merge-base; latest first): data: preserve 5 unmatched files from training-data zip (DS-000011 supplement, unregistere
- **Purpose**: 5 unmatched files from a training-data zip (DS-000011 supplement, unregistered).
- **Completeness**: 1 commit.
- **Unique value**: Only copy of those 5 files on a remote.
- **Risks**: Unregistered raw data.
- **Recommendation**: Register via ledger, then merge.


## Group: Docs

### `recovery/local-research-reconciliation-2026-10-12`

- **Tip** `0fdf5a2d` · 2026-10-12 · ghilmankhan · LR · vs main +2/-6 · merge-base `08e71926` · 20 files · PR #22 OPEN · CI no run
- **Areas changed**: `docs/research` (18), `docs/audits` (2)
- **Commits** (2 non-merge since merge-base; latest first): docs: audit local preservation and verified repository synchronization; research: preserve recovered historical B002 checkpoint
- **Purpose**: Recovered B002 checkpoint + local sync audit.
- **Completeness**: 2 commits.
- **Unique value**: Historical B002 checkpoint.
- **Risks**: -
- **Recommendation**: Merge #22 (docs only).


## Group: Finance

### `data/finance-economics-complete-2026-11-11` [code]

- **Tip** `3a3f1aee` · 2026-11-16 · ghilmankhan · R · vs main +91/-3 · merge-base `fd029485` · 1219 files · PR none · CI no run
- **Areas changed**: `research/finance-economics-channel-forensics` (688), `research/finance-economics-master` (528), `.gitignore` (1), `data/catalog` (1), `scripts/build_finance_economics_complete_db.py` (1)
- **Commits** (91 non-merge since merge-base; latest first): research: finance PDF 21 full scripts for video 1 (Trump Accounts, facts flagged VERIFY) a; research: finance PDF 20 launch manual (videos 14/18-30 Trends+YouTube check, news shelf-l; research: finance PDF 19 bridge angles (Form 4 / budget interest / gold) checked on YouTub; research: finance trend + competitor recheck PDF 18 (Trends 4h/24h/7d/30d/3m, 5y seasonali
- **Purpose**: Complete finance/economics DB (69 channels, 3,634 videos) + owner PDF reports 16-21.
- **Completeness**: 91 commits; no PR.
- **Unique value**: `finance_economics_complete.db` (largest finance video table), owner launch manuals.
- **Risks**: 98 MB unapproved DB; `.gitignore` conflict in cumulative merge.
- **Recommendation**: Decide DB policy; open a PR.


## Group: Finance lineage

### `candidate/finance-integration-2026-11-02`

- **Tip** `f115285b` · 2026-11-02 · ghilmankhan · L · vs main +209/-6 · merge-base `08e71926` · 2249 files · PR none · CI no run
- **Stacked on** `codex/finance-machine-a-owner-directed` (+15 commits)
- **Contained by** `research/finance-economics-intelligence` (+4), `fix/finance-audit-validators` (+6), `research/senior-health-reports-2026-11-11` (+9)
- **Areas changed**: `research/finance-economics-intelligence` (1611), `research/portable-recovery` (360), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `.gitattributes` (1), `AGENTS.md` (1), `README.md` (1)
- **Commits** (208 non-merge since merge-base; latest first): chore(sync): portable Machine B sync manifest, CT006 UNAVAILABLE record and recovery packa; research(finance): reanalyse 4 more videos (26/558, all SEMANTIC_REVIEW_PENDING); cohort c; research(finance): reanalyse 6 more videos (22/558, all SEMANTIC_REVIEW_PENDING); persist ; research(finance): reanalyse 3 more videos (16/558, all SEMANTIC_REVIEW_PENDING); descript
- **Purpose**: Local integration candidate joining Machine A finance audits with Machine B repairs.
- **Completeness**: Contained by #36, #45 and the current branch.
- **Unique value**: None beyond its descendants.
- **Risks**: Local only; no upstream of its own.
- **Recommendation**: Delete after #36/#45 land (fully contained).

### `claude/finance-audits-machine-b-0044ae`

- **Tip** `223f4498` · 2026-10-30 · ghilmankhan · L · vs main +150/-6 · merge-base `08e71926` · 1401 files · PR none · CI no run
- **Contained by** `codex/yios-dual-machine-coordination` (+1), `repair/second-machine-post-audit-2026-11-02` (+1), `codex/finance-machine-a-owner-directed` (+44), `candidate/finance-integration-2026-11-02` (+59)
- **Areas changed**: `research/finance-economics-intelligence` (1130), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `.gitattributes` (1), `README.md` (1), `docs/research` (1), `research/README.md` (1)
- **Commits** (150 non-merge since merge-base; latest first): fix(finance): preserve audit projections and verify NICK_180 closeout; research(finance): complete NICK_185 deep audit and session closeout; research(finance): complete NICK_184 deep audit; research(finance): complete NICK_183 deep audit and session checkpoint
- **Purpose**: Machine B finance deep audits NICK_180-185.
- **Completeness**: Root of the finance lineage; contained by 3 descendants.
- **Unique value**: None beyond descendants.
- **Risks**: Local only; 63 behind its tracked upstream.
- **Recommendation**: Delete after #36/#45 land.

### `codex/finance-machine-a-owner-directed`

- **Tip** `9c6f42fb` · 2026-11-02 · ghilmankhan · R · vs main +194/-6 · merge-base `08e71926` · 1798 files · PR none · CI no run
- **Stacked on** `claude/finance-audits-machine-b-0044ae` (+44 commits)
- **Contained by** `candidate/finance-integration-2026-11-02` (+15), `research/finance-economics-intelligence` (+19), `fix/finance-audit-validators` (+21), `research/senior-health-reports-2026-11-11` (+24)
- **Areas changed**: `research/finance-economics-intelligence` (1527), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `.gitattributes` (1), `README.md` (1), `docs/research` (1), `research/README.md` (1)
- **Commits** (194 non-merge since merge-base; latest first): research(finance): accept NICK_277-278 (554/1,612); research(finance): accept NICK_275-276 (552/1,612); research(finance): accept NICK_273-274 (550/1,612); research(finance): accept NICK_271-272 (548/1,612)
- **Purpose**: Machine A owner-directed finance audits (to NICK_278, 554/1,612).
- **Completeness**: Contained by candidate, #36, #45.
- **Unique value**: None beyond descendants.
- **Risks**: -
- **Recommendation**: Delete after #36/#45 land.

### `fix/finance-audit-validators` [code]

- **Tip** `5d487623` · 2026-11-06 · ghilmankhan · R · vs main +215/-6 · merge-base `08e71926` · 2257 files · PR #45 OPEN · CI success (2026-11-06)
- **Stacked on** `candidate/finance-integration-2026-11-02` (+6 commits)
- **Areas changed**: `research/finance-economics-intelligence` (1612), `research/portable-recovery` (360), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `tests` (3), `.gitattributes` (1), `.github` (1)
- **Commits** (214 non-merge since merge-base; latest first): docs(audit): record frozen registry separation and trials; fix(finance): keep frozen audit on its pinned registry, validate live one apart; fix(ci,finance): close review findings in validators and guard; docs(coordination): both Macs eligible; add forensic identity crosswalk
- **Purpose**: Enforce finance/reference gates in CI; frozen registry separation.
- **Completeness**: Leaf; CI green (2026-11-06).
- **Unique value**: CI gates (closes debt D1), frozen-registry pinning, forensic crosswalk.
- **Risks**: Base is the research branch, not main; AGENTS.md conflict.
- **Recommendation**: Highest-value merge: land after #36 or retarget.

### `repair/second-machine-post-audit-2026-11-02`

- **Tip** `cd2160f9` · 2026-11-02 · ghilmankhan · L · vs main +151/-6 · merge-base `08e71926` · 1405 files · PR none · CI no run
- **Stacked on** `claude/finance-audits-machine-b-0044ae` (+1 commits)
- **Contained by** `candidate/finance-integration-2026-11-02` (+58), `research/finance-economics-intelligence` (+62), `fix/finance-audit-validators` (+64), `research/senior-health-reports-2026-11-11` (+67)
- **Areas changed**: `research/finance-economics-intelligence` (1132), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `.gitattributes` (1), `README.md` (1), `docs/research` (1), `research/README.md` (1)
- **Commits** (151 non-merge since merge-base; latest first): fix(provenance): pin DS-000028/30 .gitattributes rows to ingestion-time blob; freeze-label; fix(finance): preserve audit projections and verify NICK_180 closeout; research(finance): complete NICK_185 deep audit and session closeout; research(finance): complete NICK_184 deep audit
- **Purpose**: Provenance pin repair for DS-000028/30 on Machine B.
- **Completeness**: Contained by candidate/#36/#45.
- **Unique value**: None beyond descendants.
- **Risks**: -
- **Recommendation**: Delete after #36/#45 land.

### `research/finance-economics-intelligence`

- **Tip** `2b6ccea5` · 2026-11-11 · ghilmankhan · LR · vs main +210/-3 · merge-base `fd029485` · 2249 files · PR #36 OPEN · CI failure (2026-11-11)
- **Stacked on** `candidate/finance-integration-2026-11-02` (+4 commits)
- **Contained by** `research/senior-health-reports-2026-11-11` (+5)
- **Areas changed**: `research/finance-economics-intelligence` (1611), `research/portable-recovery` (360), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `.gitattributes` (1), `AGENTS.md` (1), `README.md` (1)
- **Commits** (208 non-merge since merge-base; latest first): chore(sync): portable Machine B sync manifest, CT006 UNAVAILABLE record and recovery packa; research(finance): reanalyse 4 more videos (26/558, all SEMANTIC_REVIEW_PENDING); cohort c; research(finance): reanalyse 6 more videos (22/558, all SEMANTIC_REVIEW_PENDING); persist ; research(finance): reanalyse 3 more videos (16/558, all SEMANTIC_REVIEW_PENDING); descript
- **Purpose**: 966/1,612 finance audit + reanalysis 26/558.
- **Completeness**: PR #36 open; CI fails on "unapproved databases".
- **Unique value**: The finance audit corpus.
- **Risks**: Fails CI DB allowlist; 210 ahead.
- **Recommendation**: Fix DB allowlist (take #45 approach), then merge #36.

### `research/senior-health-reports-2026-11-11`

- **Tip** `27987f2b` · 2026-11-11 · ghilmankhan · LR · vs main +215/-3 · merge-base `fd029485` · 2306 files · PR none · CI no run
- **Local vs origin**: local 1 ahead / 0 behind
- **Stacked on** `research/finance-economics-intelligence` (+5 commits)
- **Areas changed**: `research/finance-economics-intelligence` (1611), `research/portable-recovery` (360), `research/visual-forensics` (230), `knowledge` (30), `docs/research` (22), `data/extracted` (12), `docs/project-audit` (11), `data/manifests` (10)
- **Commits** (213 non-merge since merge-base; latest first): data(senior-health): Chrome refresh of 7 registry channels to 2026-11-11 (46 new videos, 4; data(senior-health): Chrome-based acquisition of Doctor Laura (67 videos, 63 transcripts) ; docs(audit): add selected-folders reconciliation and project audit docs; docs(senior-health): add Reports 1-6, build scripts and derived tables
- **Purpose**: CURRENT branch: Senior Health Reports 1-6 + Chrome acquisitions, stacked on the finance lineage.
- **Completeness**: Local is 1 ahead of remote (older slop-gate commit).
- **Unique value**: Reports 1-6, Doctor Laura/Neal K. Shah data, docs/project-audit.
- **Risks**: Unpushed commit 90f9cd22 duplicates PR #51 (older version).
- **Recommendation**: Drop 90f9cd22; split Senior Health commits onto main.


## Group: Merged

### `chore/full-local-data-sync-and-senior-health-acquisition`

- **Tip** `f3c56353` · 2026-09-25 · ghilmankhan · LR · vs main +0/-79 · merge-base `f3c56353` · 0 files · PR #4 MERGED #1 MERGED · CI no run
- **Purpose**: Early full local data sync + Senior Health acquisition.
- **Completeness**: Merged (#1, #4).
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete (fully in main).

### `claude/second-machine-audit-repair-ef17c5`

- **Tip** `08e71926` · 2026-10-11 · ghilmanITM360 · L · vs main +0/-6 · merge-base `08e71926` · 0 files · PR none · CI no run
- **Purpose**: Second-machine audit repair session.
- **Completeness**: Fully in main.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `claude/statins-senior-health-db38aa`

- **Tip** `fd029485` · 2026-11-10 · ghilmanITM360 · L · vs main +0/-3 · merge-base `fd029485` · 0 files · PR none · CI no run
- **Purpose**: Statins senior-health session worktree.
- **Completeness**: Tip equals old main (fd029485); no own commits.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete worktree + branch.

### `codex/remaining-work-audit-2026-10-11`

- **Tip** `6338efe2` · 2026-10-11 · ghilmankhan · R · vs main +0/-7 · merge-base `6338efe2` · 0 files · PR #18 MERGED · CI no run
- **Purpose**: Remaining-work reconciliation.
- **Completeness**: Merged #18.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `codex/transcript-pending-registration`

- **Tip** `ec171641` · 2026-10-11 · ghilmankhan · R · vs main +0/-17 · merge-base `ec171641` · 0 files · PR #17 MERGED · CI no run
- **Purpose**: Transcript-pending registration.
- **Completeness**: Merged #17.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `codex/what-if-normalized-staging`

- **Tip** `fe284619` · 2026-10-09 · ghilmankhan · LR · vs main +0/-37 · merge-base `fe284619` · 0 files · PR #10 MERGED · CI no run
- **Purpose**: What If staging (PR C).
- **Completeness**: Merged #10.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `codex/what-if-promotion`

- **Tip** `aff815ef` · 2026-10-09 · ghilmankhan · LR · vs main +0/-34 · merge-base `aff815ef` · 0 files · PR #11 MERGED · CI no run
- **Purpose**: What If promotion.
- **Completeness**: Merged #11.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `codex/what-if-readonly-adapter`

- **Tip** `58c7a12b` · 2026-10-09 · ghilmankhan · LR · vs main +0/-39 · merge-base `58c7a12b` · 0 files · PR #9 MERGED · CI no run
- **Purpose**: What If read-only adapter (PR B).
- **Completeness**: Merged #9.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `codex/what-if-source-contract`

- **Tip** `be4969c7` · 2026-10-09 · ghilmankhan · LR · vs main +0/-41 · merge-base `be4969c7` · 0 files · PR #8 MERGED · CI no run
- **Purpose**: What If source contract (PR A).
- **Completeness**: Merged #8.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `docs/yios-consolidation-index`

- **Tip** `efd3dc0a` · 2026-11-10 · ghilmankhan · R · vs main +0/-4 · merge-base `efd3dc0a` · 0 files · PR #48 MERGED · CI success (2026-11-09)
- **Purpose**: START_HERE index draft.
- **Completeness**: Merged #48.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `feat/ai-slop-gate`

- **Tip** `5b481bc9` · 2026-11-17 · ghilmankhan · LR · vs main +0/-1 · merge-base `5b481bc9` · 0 files · PR #51 MERGED · CI success (2026-11-17)
- **Purpose**: Pre-delivery AI-slop gate.
- **Completeness**: Merged #51.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `integration/packaging-forensics-validated-subset-2026-10-11`

- **Tip** `ce82c0a8` · 2026-10-11 · ghilmankhan · R · vs main +0/-19 · merge-base `ce82c0a8` · 0 files · PR #19 MERGED · CI no run
- **Purpose**: Genius History packaging subset.
- **Completeness**: Merged #19.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `integration/repository-consolidation-2026-09-25`

- **Tip** `73816f1e` · 2026-09-26 · ghilmankhan · R · vs main +0/-65 · merge-base `73816f1e` · 0 files · PR #5 MERGED · CI no run
- **Purpose**: PR#2/#3/#4 consolidation.
- **Completeness**: Merged #5.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `integration/repository-superset-2026-09-23`

- **Tip** `0930dfe3` · 2026-09-23 · ghilmankhan · R · vs main +0/-98 · merge-base `0930dfe3` · 0 files · PR none · CI no run
- **Purpose**: Repository superset integration.
- **Completeness**: Fully in main.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `integration/yios-current-canonical-2026-10-03`

- **Tip** `c1c3bb88` · 2026-10-04 · ghilmankhan · R · vs main +0/-43 · merge-base `c1c3bb88` · 0 files · PR #7 MERGED · CI no run
- **Purpose**: Canonical integration (phase 2 + DS-000034).
- **Completeness**: Merged #7.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `research/senior-health-acquisition-phase-2`

- **Tip** `373bf37e` · 2026-09-29 · ghilmankhan · R · vs main +0/-53 · merge-base `373bf37e` · 0 files · PR none · CI no run
- **Purpose**: Senior health acquisition phase 2.
- **Completeness**: Fully in main.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `research/senior-health-complete-local-sync`

- **Tip** `0cbabf50` · 2026-10-02 · ghilmankhan · LR · vs main +0/-77 · merge-base `0cbabf50` · 0 files · PR #3 MERGED · CI no run
- **Purpose**: Senior Health datasets preservation.
- **Completeness**: Merged #3.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete (stash@{0} was made on it).

### `research/senior-health-data-expansion-2026-09-28`

- **Tip** `814a0279` · 2026-09-28 · ghilmankhan · LR · vs main +0/-58 · merge-base `814a0279` · 0 files · PR #6 MERGED · CI no run
- **Purpose**: Senior Health data expansion.
- **Completeness**: Merged #6.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `research/senior-health-forensic-v2`

- **Tip** `206d67bc` · 2026-09-25 · ghilmankhan · R · vs main +0/-81 · merge-base `206d67bc` · 0 files · PR #2 MERGED · CI no run
- **Purpose**: Senior Health forensic V2.
- **Completeness**: Merged #2.
- **Unique value**: None.
- **Risks**: -
- **Recommendation**: Delete.

### `research/senior-health-metadata`

- **Tip** `fd029485` · 2026-11-10 · ghilmanITM360 · L · vs main +0/-3 · merge-base `fd029485` · 0 files · PR none · CI no run
- **Purpose**: Senior Health metadata worktree (~/Documents/yios-senior-health).
- **Completeness**: Tip = old main; work is UNTRACKED in its worktree (35 files, 10 MB).
- **Unique value**: Untracked files only.
- **Risks**: Uncommitted work at risk.
- **Recommendation**: Commit the untracked worktree files to a branch.


## Group: Metadata/forensics

### `codex/casual-economics-forensic-research` [code]

- **Tip** `fce81670` · 2026-10-14 · ghilmankhan · LR · vs main +20/-6 · merge-base `08e71926` · 477 files · PR #25 OPEN · CI success (2026-10-14)
- **Areas changed**: `data/extracted` (321), `research/casual-economics-deep-dive-2026-10` (140), `docs/research` (9), `data/manifests` (2), `tests` (2), `docs/YOUTUBE_CHANNEL_REGISTRY.md` (1), `scripts/apify_youtube_ingest.py` (1), `scripts/build_youtube_channel_registry.py` (1)
- **Commits** (20 non-merge since merge-base; latest first): research: performance, Trends and news study; final report and QA register; research: channel production DNA and original production blueprint; research: add Great Depression sampled forensic package (11/11 structural); research: add 2008 Financial Crisis sampled forensic package (10/11 structural)
- **Purpose**: Casual Economics acquisition and sampled audiovisual forensics.
- **Completeness**: Research complete for sampled set; excluded from CF milestones.
- **Unique value**: Only copy of Casual Economics research + registry script edits.
- **Risks**: Touches registry builder and Apify ingest script.
- **Recommendation**: Review code diff separately, then merge (#25).

### `research/barely-evolved-metadata`

- **Tip** `c4212c90` · 2026-10-20 · ghilmankhan · LR · vs main +1/-6 · merge-base `08e71926` · 24 files · PR #43 OPEN · CI failure (2026-10-20)
- **Areas changed**: `research/barely-evolved-metadata` (24)
- **Commits** (1 non-merge since merge-base; latest first): feat: add BarelyEvolved metadata snapshot
- **Purpose**: BarelyEvolved metadata snapshot.
- **Completeness**: 1 commit; CI failed before steps.
- **Unique value**: Channel snapshot.
- **Risks**: -
- **Recommendation**: Re-run CI, merge #43.

### `research/monkey-explains-1999-metadata`

- **Tip** `f176aa28` · 2026-10-20 · ghilmankhan · LR · vs main +1/-6 · merge-base `08e71926` · 18 files · PR #38 OPEN · CI failure (2026-10-20)
- **Areas changed**: `research/monkey-explains-1999` (18)
- **Commits** (1 non-merge since merge-base; latest first): feat(research): add MonkeyExplains metadata snapshot
- **Purpose**: MonkeyExplains1999 metadata snapshot.
- **Completeness**: 1 commit; CI failed before steps.
- **Unique value**: Channel snapshot.
- **Risks**: -
- **Recommendation**: Re-run CI, merge #38.

### `research/youtube-12-channel-metadata`

- **Tip** `967ea707` · 2026-10-20 · ghilmankhan · LR · vs main +2/-6 · merge-base `08e71926` · 262 files · PR #39 OPEN · CI failure (2026-10-20)
- **Areas changed**: `research/youtube-12-channel-metadata` (262)
- **Commits** (2 non-merge since merge-base; latest first): docs: record metadata delivery status; research: add 12-channel YouTube metadata snapshot
- **Purpose**: 12-channel metadata snapshot.
- **Completeness**: 2 commits; CI failed before steps.
- **Unique value**: 262 metadata files.
- **Risks**: -
- **Recommendation**: Re-run CI, merge #39.


## Group: Packaging

### `codex/packaging-rollup-repair-2026-10-11` [code]

- **Tip** `9ce62de2` · 2026-10-11 · ghilmankhan · R · vs main +50/-42 · merge-base `e43f97b1` · 295 files · PR none · CI no run
- **Contained by** `research/thumbnail-forensics-complete-2026-10-04` (+21)
- **Areas changed**: `docs/research` (293), `data/manifests` (1), `tests` (1)
- **Commits** (50 non-merge since merge-base; latest first): docs: preserve final green CI and packaging continuation handoff; packaging: repair audit rollup and dashboard hash reconciliation; packaging: record verified video push and resource checkpoint; packaging: complete Italian Mafia rank video QA
- **Purpose**: Packaging audit rollup and dashboard hash reconciliation.
- **Completeness**: Contained by thumbnail-forensics-complete.
- **Unique value**: None beyond descendant.
- **Risks**: 42 behind.
- **Recommendation**: Delete after descendant decision.

### `planning/deferred-legacy-thumbnail-research`

- **Tip** `9e7be191` · 2026-10-12 · ghilmankhan · LR · vs main +1/-6 · merge-base `08e71926` · 1 files · PR #24 OPEN · CI no run
- **Areas changed**: `docs/backlog` (1)
- **Commits** (1 non-merge since merge-base; latest first): docs: plan deferred legacy thumbnail evidence reuse
- **Purpose**: Plan for deferred legacy thumbnail evidence reuse.
- **Completeness**: 1 doc.
- **Unique value**: Backlog plan.
- **Risks**: -
- **Recommendation**: Merge #24 (docs only).

### `research/thumbnail-forensics-complete-2026-10-04` [code]

- **Tip** `6c6e8900` · 2026-10-11 · ghilmankhan · LR · vs main +71/-42 · merge-base `e43f97b1` · 304 files · PR none · CI no run
- **Stacked on** `codex/packaging-rollup-repair-2026-10-11` (+21 commits)
- **Areas changed**: `docs/research` (302), `data/manifests` (1), `tests` (1)
- **Commits** (71 non-merge since merge-base; latest first): packaging: QA Hypothetically HByY2gb1llw; packaging: QA Hypothetically GczRApVP5jo; packaging: QA Hypothetically A5mmQQiywfg; packaging: QA Hypothetically 81r4BT3Wm5E
- **Purpose**: Hypothetically packaging QA (thumbnail forensics).
- **Completeness**: 71 commits, no PR.
- **Unique value**: Thumbnail forensics QA corpus.
- **Risks**: Conflict with stash0 delta on completion-ledger.csv.
- **Recommendation**: Open PR after stash decision.


## Group: Preservation

### `preservation/stash0-tracked-delta-2026-11-11`

- **Tip** `ac51465b` · 2026-10-13 · ghilmankhan · L · vs main +3/-77 · merge-base `0cbabf50` · 1 files · PR none · CI no run
- **Stacked on** `preservation/stash0-untracked-LOCAL-ONLY-2026-11-11` (+133 commits)
- **Areas changed**: `docs/research` (1)
- **Commits** (2 non-merge since merge-base; latest first): index on research/senior-health-complete-local-sync: 0cbabf5 docs: preserve thumbnail inve; untracked files on research/senior-health-complete-local-sync: 0cbabf5 docs: preserve thum
- **Purpose**: stash@{0} tracked delta as a branch.
- **Completeness**: Local only.
- **Unique value**: Matches stash@{0}.
- **Risks**: Conflicts with thumbnail-forensics on completion-ledger.csv.
- **Recommendation**: Keep until owner reviews; then drop with stash.

### `preservation/stash0-untracked-LOCAL-ONLY-2026-11-11`

- **Tip** `2d0e6e97` · 2026-10-13 · ghilmankhan · L · vs main +1/-208 · merge-base `none` · 7309 files · PR none · CI no run
- **Contained by** `preservation/stash0-tracked-delta-2026-11-11` (+133)
- **Areas changed**: `docs/research` (2642), `data/raw` (2179), `research/finance-economics-intelligence` (1052), `research/portable-recovery` (360), `research/visual-forensics` (230), `data/extracted` (164), `"data` (124), `data/manifests` (117)
- **Commits** (1 non-merge since merge-base; latest first): untracked files on research/senior-health-complete-local-sync: 0cbabf5 docs: preserve thum
- **Purpose**: stash@{0} untracked files (~2,267 files, ~843 MB thumbnails).
- **Completeness**: Local only, no remote copy.
- **Unique value**: ONLY copy of thumbnail snapshots.
- **Risks**: Single point of loss.
- **Recommendation**: Owner decision: back up off-device before anything else.


## Group: Production

### `dr-rehan-test-videos`

- **Tip** `8daa1c83` · 2026-10-13 · ghilmankhan · R · vs main +1/-6 · merge-base `08e71926` · 62 files · PR #26 OPEN · CI no run
- **Areas changed**: `projects` (62)
- **Commits** (1 non-merge since merge-base; latest first): feat: add Dr Rehan Omar test video V1 V2 and editable production project
- **Purpose**: Dr Rehan Omar test video V1/V2 + editable production project.
- **Completeness**: 1 commit, 62 files under `projects/`.
- **Unique value**: Editable video project.
- **Risks**: Media in git.
- **Recommendation**: Owner decision: keep as production archive or move to media store (#26).

### `production/dr-rehan-diabetes-heart-warning-assets`

- **Tip** `c867af8e` · 2026-10-15 · ghilmankhan · R · vs main +12/-6 · merge-base `08e71926` · 473 files · PR #32 OPEN · CI success (2026-10-15)
- **Areas changed**: `productions` (473)
- **Commits** (12 non-merge since merge-base; latest first): production: V3 upload candidate without internal annotations, trimmed ending, thumbnails; production: V2 white-canvas visual redesign with audio-timed preview; production: audio-timed keyframe animation and muted provisional preview; production: finalize portable asset manifests QA and Claude handoff
- **Purpose**: Dr Rehan diabetes/heart warning storyboard, V1-V3 keyframe animation.
- **Completeness**: 12 commits; draft PR #32.
- **Unique value**: Production assets + renderer.
- **Risks**: Media in git.
- **Recommendation**: Archive as production record; merge only manifests.

### `production/finance-short-01-keyframe`

- **Tip** `315e76d5` · 2026-10-13 · ghilmankhan · LR · vs main +11/-6 · merge-base `08e71926` · 598 files · PR #29 CLOSED · CI success (2026-10-13)
- **Areas changed**: `productions` (598)
- **Commits** (11 non-merge since merge-base; latest first): test(finance-short): validate second-PC preview and checkpoint owner review; fix(finance-short): bound captions to shots and simulated phone safe zones; fix(finance-short): keep marker retreat continuous across shot cut; fix(finance-short): make asset renderer and frame QA portable
- **Purpose**: Finance Short 01 keyframe animation (21 shots).
- **Completeness**: 11 commits; PR #29 CLOSED.
- **Unique value**: Portable asset renderer + frame QA.
- **Risks**: Final export blocked on corrected APR MP3 (memory note).
- **Recommendation**: Keep branch; reopen when audio arrives.

### `production/finance-short-02-assets`

- **Tip** `30e0ef2f` · 2026-10-14 · ghilmankhan · R · vs main +14/-6 · merge-base `08e71926` · 504 files · PR #30 OPEN · CI success (2026-10-14)
- **Areas changed**: `finance-short-02-visual-calibration` (501), `"finance-short-02-visual-calibration` (3)
- **Commits** (14 non-merge since merge-base; latest first): polish Finance Short 02 into V3: retimed builds, original ducked soundtrack; animate Finance Short 02 from existing assets and render final video; verify remote asset recovery and prepare owner review handoff; checkpoint complete asset artwork and remaining remote validation
- **Purpose**: Finance Short 02 illustration package + V3 render.
- **Completeness**: 14 commits; draft PR #30.
- **Unique value**: Original asset package.
- **Risks**: Media in git; top-level non-standard folder.
- **Recommendation**: Archive as production record.

### `production/senior-health-casually-finance-three-videos`

- **Tip** `65caa889` · 2026-10-16 · ghilmankhan · R · vs main +15/-6 · merge-base `08e71926` · 1030 files · PR #34 OPEN · CI success (2026-10-15)
- **Areas changed**: `productions` (1030)
- **Commits** (15 non-merge since merge-base; latest first): production: Swimming After 60 V3 review (alternating crawl stroke, 6-beat kick, water cont; docs: RESUME_HERE V3 checkpoint (HIIT + Running done, Swimming next); production: Running After 60 V3 review (two-leg running gait, contralateral arms, red open; production: HIIT After 60 V3 review (two-leg gait rig, contralateral arms, red opening bar
- **Purpose**: HIIT/Running/Swimming After 60 V3 review videos.
- **Completeness**: 15 commits; draft PR #34.
- **Unique value**: Gait rigs, review packages.
- **Risks**: Media in git.
- **Recommendation**: Archive as production record.


## Group: Senior Health

### `claude/dr-rehan-seniors-health-data-5db7ab`

- **Tip** `05456d7a` · 2026-11-16 · ghilmankhan · LR · vs main +3/-3 · merge-base `fd029485` · 53 files · PR none · CI no run
- **Areas changed**: `data/raw` (44), `docs/research` (9)
- **Commits** (3 non-merge since merge-base; latest first): docs: add Dr Rehan review, Codex briefs, winning models and talking cards v2; docs: validate Dr Rehan scripts and clinical claims; research: validate Dr Rehan senior-health topics
- **Purpose**: Dr Rehan topic validation, clinical-claim validation, talking cards.
- **Completeness**: 3 commits; docs + 44 raw data files.
- **Unique value**: Clinical-claim validation docs not elsewhere.
- **Risks**: Adds files under `data/raw/` (immutability + privacy review needed).
- **Recommendation**: Review raw files, then merge via PR.

### `data/exercise-apify-2026-11-14` [code]

- **Tip** `23e6864d` · 2026-11-16 · ghilmankhan · R · vs main +64/-3 · merge-base `fd029485` · 174 files · PR none · CI no run
- **Stacked on** `research/senior-health-apify-2026-11-11` (+1 commits)
- **Areas changed**: `research/senior-health-forensics` (101), `research/senior-health-apify-2026-11-11` (29), `data/catalog` (17), `research/senior-health-master` (9), `research/senior-health-research` (8), `data/manifests` (3), `.gitignore` (1), `scripts/backfill_senior_health_transcripts.py` (1)
- **Commits** (64 non-merge since merge-base; latest first): data: exercise channels Apify pull (25 channels, 600 videos, top-8 transcripts for 169 vid; data: add local audits index 2026-11-14 (summary, gz manifest, readme); research: senior-health new-channel blueprint v1/v2 (PDF+HTML+builders) and Dr Rehan thumb; research: senior-health 44-channel synthesis (dawai-safety sub-niche, script-reuse cluster
- **Purpose**: Exercise-channel Apify pull (25 channels, 600 videos) on top of #50.
- **Completeness**: Leaf of Senior Health Apify lineage.
- **Unique value**: Exercise sub-niche data, 44-channel synthesis, new-channel blueprint HTML/PDF.
- **Risks**: Adds 7 SQLite DBs that CI rejects ("unapproved databases").
- **Recommendation**: Decide DB policy (LFS/allowlist or external), then merge with #50.

### `docs/dr-rehan-recording-pack-2026-11-17`

- **Tip** `8aac2523` · 2026-11-17 · ghilmankhan · R · vs main +1/-3 · merge-base `fd029485` · 11 files · PR none · CI no run
- **Areas changed**: `docs/research` (11)
- **Commits** (1 non-merge since merge-base; latest first): docs: Dr Rehan recording pack for 11 videos (single PDF, cue sheets, scripts, claim tables
- **Purpose**: Dr Rehan recording pack for 11 videos (PDF, cue sheets, scripts, claim tables).
- **Completeness**: 1 commit, today.
- **Unique value**: Production-ready recording pack.
- **Risks**: Scripts must pass the slop gate before delivery (AGENTS.md).
- **Recommendation**: Run slop gate, open PR.

### `research/senior-health-apify-2026-11-11` [code]

- **Tip** `9b23e061` · 2026-11-16 · ghilmankhan · R · vs main +63/-3 · merge-base `fd029485` · 163 files · PR #50 OPEN · CI failure (2026-11-15)
- **Contained by** `data/exercise-apify-2026-11-14` (+1)
- **Areas changed**: `research/senior-health-forensics` (101), `research/senior-health-apify-2026-11-11` (29), `research/senior-health-master` (9), `research/senior-health-research` (8), `data/catalog` (6), `data/manifests` (3), `.gitignore` (1), `scripts/backfill_senior_health_transcripts.py` (1)
- **Commits** (63 non-merge since merge-base; latest first): data: add local audits index 2026-11-14 (summary, gz manifest, readme); research: senior-health new-channel blueprint v1/v2 (PDF+HTML+builders) and Dr Rehan thumb; research: senior-health 44-channel synthesis (dawai-safety sub-niche, script-reuse cluster; research: senior-health forensics reports 43 Metabolic Unlocked (PARTIAL, constipation vid
- **Purpose**: Senior Health Apify metadata (21 channels/501 videos) + forensics reports 41-43 + senior_health_core DB.
- **Completeness**: PR #50 open; CI fails "unapproved databases".
- **Unique value**: senior_health_core.db (5,802 videos, 159 channels).
- **Risks**: Unapproved DBs.
- **Recommendation**: Decide DB policy; merge with exercise branch.


## Group: Senior Health/docs

### `consolidation/selected-folders-2026-11-11`

- **Tip** `89e3aa6d` · 2026-11-11 · ghilmankhan · LR · vs main +2/-3 · merge-base `fd029485` · 148 files · PR #49 OPEN · CI success (2026-11-11)
- **Areas changed**: `docs/audits` (131), `data/manifests` (10), `data/extracted` (7)
- **Commits** (2 non-merge since merge-base; latest first): docs: GitHub publication status for consolidation; docs/data: consolidate selected-folder research (indexes, provenance, Senior Health, audit
- **Purpose**: Selected-folder research consolidation: master index, provenance, Senior Health, audits.
- **Completeness**: 2 commits; CI green.
- **Unique value**: 131 audit docs + manifests.
- **Risks**: -
- **Recommendation**: Merge #49.


## Group: Stale

### `backup/decode-15cbe9f-original` [code]

- **Tip** `15cbe9f0` · 2026-09-28 · ghilmankhan · R · vs main +1/-59 · merge-base `31ea9a53` · 13 files · PR none · CI no run
- **Areas changed**: `docs/research` (5), `scripts/build_decode_your_heart_recovery.py` (1), `scripts/build_ds32_thumbnail_evidence.py` (1), `scripts/ingest_decode_retention_exports.py` (1), `scripts/inspect_decode_workbook.mjs` (1), `scripts/recover_ds32_thumbnails.sh` (1), `scripts/update_decode_report.py` (1), `scripts/update_decode_workbook.mjs` (1)
- **Commits** (1 non-merge since merge-base; latest first): research: recover Decode Your Heart (DS-000032) interrupted session
- **Purpose**: Backup of an interrupted Decode Your Heart (DS-000032) recovery session.
- **Completeness**: Snapshot only.
- **Unique value**: Original pre-rework versions of 8 Decode scripts.
- **Risks**: 59 behind; main reworked the same files on 2026-10-04.
- **Recommendation**: Archive (keep ref, do not merge).

### `fix/repository-health-remediation-2026-09-21` [code]

- **Tip** `11ad082b` · 2026-09-21 · ghilmankhan · R · vs main +4/-125 · merge-base `25110136` · 38 files · PR none · CI no run
- **Areas changed**: `tests` (11), `data/manifests` (2), `data/normalized` (2), `.github` (1), `.gitignore` (1), `.nvmrc` (1), `.python-version` (1), `AGENTS.md` (1)
- **Commits** (4 non-merge since merge-base; latest first): docs: record verified repository remediation; docs: reconcile registry status and bootstrap; build: make clean-clone validation reproducible; feat: integrate DS-000027 into canonical registry
- **Purpose**: Early repository health remediation.
- **Completeness**: Ported into main (811ad211, 73816f1e).
- **Unique value**: None verified.
- **Risks**: 125 behind.
- **Recommendation**: Archive.

### `ui/v1`

- **Tip** `0412932a` · 2026-09-11 · ghilmankhan · LR · vs main +1/-149 · merge-base `56296874` · 2 files · PR none · CI no run
- **Areas changed**: `docs/UI_BACKEND_HANDOFF_2026-09-11.md` (1), `docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md` (1)
- **Commits** (1 non-merge since merge-base; latest first): docs: add complete backend audit and UI handoff
- **Purpose**: UI backend handoff + complete audit docs (2026-09-11).
- **Completeness**: Docs preserved on main as HISTORICAL.
- **Unique value**: None (ported in 4335eff5).
- **Risks**: 149 behind.
- **Recommendation**: Archive; it is the prior UI plan this audit supersedes.


## Group: Test refs

### `yios-test/34df1220de934163b910f7d4c737bcf1/checkpoint`

- **Tip** `43aff9d3` · 2026-10-30 · ghilmankhan · R · vs main n/a (orphan) · merge-base `none` · 5603 files · PR none · CI no run
- **Areas changed**: `data/raw` (2179), `research/finance-economics-intelligence` (1611), `docs/research` (401), `research/portable-recovery` (360), `research/visual-forensics` (230), `data/extracted` (164), `"data` (124), `data/manifests` (117)
- **Commits** (2 non-merge since merge-base; latest first): research: checkpoint finance/TEST0000001 PARTIAL; test: non-production checkpoint seed
- **Purpose**: Orphan test refs from dual-machine claim tests.
- **Completeness**: No common ancestor with main (verified: `git merge-base` exit 1).
- **Unique value**: None.
- **Risks**: Ahead/behind numbers are meaningless (unrelated history).
- **Recommendation**: Delete after owner confirmation.

### `yios-test/34df1220de934163b910f7d4c737bcf1/claims/finance/TEST0000001`

- **Tip** `5ef9694a` · 2026-10-30 · ghilmankhan · R · vs main n/a (orphan) · merge-base `none` · 5602 files · PR none · CI no run
- **Areas changed**: `data/raw` (2179), `research/finance-economics-intelligence` (1611), `docs/research` (401), `research/portable-recovery` (360), `research/visual-forensics` (230), `data/extracted` (164), `"data` (124), `data/manifests` (117)
- **Commits** (5 non-merge since merge-base; latest first): YIOS finance/TEST0000001 RELEASED; YIOS finance/TEST0000001 ACTIVE; YIOS finance/TEST0000001 RELEASED; YIOS finance/TEST0000001 ACTIVE
- **Purpose**: Orphan test refs from dual-machine claim tests.
- **Completeness**: No common ancestor with main (verified: `git merge-base` exit 1).
- **Unique value**: None.
- **Risks**: Ahead/behind numbers are meaningless (unrelated history).
- **Recommendation**: Delete after owner confirmation.

### `yios-test/34df1220de934163b910f7d4c737bcf1/claims/finance/TEST0000002`

- **Tip** `abb9a7b4` · 2026-10-30 · ghilmankhan · R · vs main n/a (orphan) · merge-base `none` · 5602 files · PR none · CI no run
- **Areas changed**: `data/raw` (2179), `research/finance-economics-intelligence` (1611), `docs/research` (401), `research/portable-recovery` (360), `research/visual-forensics` (230), `data/extracted` (164), `"data` (124), `data/manifests` (117)
- **Commits** (2 non-merge since merge-base; latest first): YIOS finance/TEST0000002 RELEASED; YIOS finance/TEST0000002 ACTIVE
- **Purpose**: Orphan test refs from dual-machine claim tests.
- **Completeness**: No common ancestor with main (verified: `git merge-base` exit 1).
- **Unique value**: None.
- **Risks**: Ahead/behind numbers are meaningless (unrelated history).
- **Recommendation**: Delete after owner confirmation.


## Group: Tooling

### `codex/register-verified-transcript-pending-what-if` [code]

- **Tip** `e9b56960` · 2026-10-11 · ghilmankhan · R · vs main +1/-6 · merge-base `08e71926` · 17 files · PR #20 OPEN · CI no run
- **Areas changed**: `docs/evidence` (4), `data/manifests` (3), `data/catalog` (2), `data/normalized` (2), `tests` (2), `PROJECT_STATUS.md` (1), `data/raw` (1), `scripts/build_youtube_channel_registry.py` (1)
- **Commits** (1 non-merge since merge-base; latest first): Register verified What If identities with transcript-pending evidence
- **Purpose**: Register verified What If identities with transcript-pending state.
- **Completeness**: 1 commit; touches catalog DB + registry builder.
- **Unique value**: What If identity rows.
- **Risks**: Modifies committed `data/catalog` DBs: must be rebuilt, not merged blindly.
- **Recommendation**: Re-apply on current main via script, then close #20.

### `codex/yios-dual-machine-coordination` [code]

- **Tip** `205fc7eb` · 2026-10-30 · ghilmankhan · LR · vs main +151/-6 · merge-base `08e71926` · 1417 files · PR none · CI no run
- **Stacked on** `claude/finance-audits-machine-b-0044ae` (+1 commits)
- **Areas changed**: `research/finance-economics-intelligence` (1130), `research/visual-forensics` (230), `knowledge` (30), `reports` (7), `research/coordination` (3), `tests` (3), `.gitattributes` (1), `AGENTS.md` (1)
- **Commits** (151 non-merge since merge-base; latest first): feat: add verified per-video research coordination and checkpoint workflow; fix(finance): preserve audit projections and verify NICK_180 closeout; research(finance): complete NICK_185 deep audit and session closeout; research(finance): complete NICK_184 deep audit
- **Purpose**: Two-Mac task claims/checkpoints CLI (`scripts/yios.py`, coordination, integration, remote smoke).
- **Completeness**: 1 exclusive commit on top of the finance lineage; 518 test lines.
- **Unique value**: Only implementation of cooperative two-machine claims (git-ref based; produced the yios-test refs).
- **Risks**: Bundles 150 finance commits; conflicts on AGENTS.md.
- **Recommendation**: Extract the tooling commit onto main if two-Mac work continues; otherwise archive.

### `feat/registry-reviewed-workbooks` [code]

- **Tip** `264e9ebf` · 2026-11-06 · ghilmankhan · R · vs main +2/-6 · merge-base `08e71926` · 13 files · PR #46 OPEN · CI success (2026-11-06)
- **Areas changed**: `research/registry-ingestion` (10), `scripts/build_reviewed_channel_workbooks.py` (1), `scripts/source_adapters` (1), `tests` (1)
- **Commits** (2 non-merge since merge-base; latest first): docs(registry): record importer trial and its registry validator failure; feat(registry): reviewed importer workbooks for four channel gaps
- **Purpose**: Reviewed importer workbooks for four channel gaps.
- **Completeness**: 2 commits; CI green; doc records a registry validator failure in trial.
- **Unique value**: `build_reviewed_channel_workbooks.py` + test.
- **Risks**: Documented validator failure on import trial.
- **Recommendation**: Fix the recorded validator failure, then merge #46.

### `feat/slop-gate-alerts` [code]

- **Tip** `58f9b62c` · 2026-11-17 · ghilmankhan · LR · vs main +1/-0 · merge-base `e96f7f8f` · 5 files · PR #52 OPEN · CI success (2026-11-17)
- **Areas changed**: `.claude` (1), `AGENTS.md` (1), `docs/policies` (1), `scripts/check_slop_risk.py` (1), `tests` (1)
- **Commits** (1 non-merge since merge-base; latest first): feat(gate): activate AI-slop gate on every session and alert the user
- **Purpose**: Activate slop gate on every session + user alerts.
- **Completeness**: 1 commit; CI green; PR #52 open.
- **Unique value**: Session hook + alerting.
- **Risks**: -
- **Recommendation**: Merge #52.

### `research/local-channel-media-library` [code]

- **Tip** `78e8fd2d` · 2026-10-21 · ghilmankhan · LR · vs main +5/-6 · merge-base `08e71926` · 19 files · PR #41 OPEN · CI failure (2026-10-21)
- **Areas changed**: `research/media-library` (11), `.gitignore` (1), `AGENTS.md` (1), `README.md` (1), `docs/LOCAL_MEDIA_AVAILABILITY.md` (1), `scripts/build_local_media_library.py` (1), `scripts/media_cache.py` (1), `scripts/smoke_test_local_media_library.py` (1)
- **Commits** (5 non-merge since merge-base; latest first): docs: register local media availability; fix: normalize media manifest line endings; feat: add selective verified media cache workflow; chore: make local media root durable
- **Purpose**: Checksummed local media library + selective media cache.
- **Completeness**: 5 commits; CI failed before steps.
- **Unique value**: `build_local_media_library.py`, `media_cache.py`: the only media-availability layer.
- **Risks**: -
- **Recommendation**: Re-run CI, merge #41. Needed by any UI that shows media.


## Group: Visual forensics

### `claude/determined-darwin-v0gl6n`

- **Tip** `e0e2cbcc` · 2026-11-02 · Claude · R · vs main +1/-6 · merge-base `08e71926` · 5 files · PR none · CI no run
- **Contained by** `research/barely-evolved-visual-forensics` (+47)
- **Areas changed**: `research/visual-forensics` (5)
- **Commits** (1 non-merge since merge-base; latest first): research: Barely Evolved onboarding checkpoint (PARTIAL, blocked on media and network)
- **Purpose**: Barely Evolved onboarding checkpoint (PARTIAL, blocked on media/network).
- **Completeness**: Contained by research/barely-evolved-visual-forensics.
- **Unique value**: None beyond descendant.
- **Risks**: -
- **Recommendation**: Delete after Barely Evolved branch lands.

### `codex/what-if-archive-main-integration`

- **Tip** `f345abde` · 2026-10-28 · ghilmankhan · R · vs main +7/-6 · merge-base `08e71926` · 405 files · PR #44 OPEN · CI failure (2026-10-28)
- **Areas changed**: `research/visual-forensics` (316), `research/production-experiments` (82), `docs/intelligence` (2), `.claude` (1), `AGENTS.md` (1), `README.md` (1), `docs/AI_SESSION_CONTEXT.md` (1), `docs/YIOS_MASTER_PLAN.md` (1)
- **Commits** (7 non-merge since merge-base; latest first): docs: add source-backed What If visual navigation and storyboard skill; docs: pin historical authorities for main-based archive integration; docs: add canonical YIOS master plan and session context; research: preserve distinct What If reports and frozen metadata batch 4
- **Purpose**: Main-based What If archive integration + YIOS master plan + storyboard skill.
- **Completeness**: 7 commits; CI failed before any step ran (2026-10-28).
- **Unique value**: YIOS_MASTER_PLAN.md, AI_SESSION_CONTEXT.md, What If visual navigation.
- **Risks**: Conflicts with what-if-brain-preservation on the same two docs.
- **Recommendation**: Pick one master plan; merge #44 after re-running CI.

### `research/barely-evolved-visual-forensics`

- **Tip** `3e587c75` · 2026-11-06 · ghilmankhan · R · vs main +48/-6 · merge-base `08e71926` · 1000 files · PR none · CI no run
- **Stacked on** `claude/determined-darwin-v0gl6n` (+47 commits)
- **Areas changed**: `research/visual-forensics` (1000)
- **Commits** (48 non-merge since merge-base; latest first): research(barely-evolved): N20 N20 receipts and lock-release records; research(barely-evolved): N19 camera reconciliation, R20 dependency closure, N18 receipts; research(barely-evolved): N18 publish remaining receipts, lock and correction records; research(barely-evolved): N17 reconcile batch 2, method M3 log, audit matrix v3, R20 verif
- **Purpose**: Barely Evolved visual forensics N15-N20.
- **Completeness**: 48 commits, no PR.
- **Unique value**: Only copy of BE forensic records.
- **Risks**: 1,000 files; heavy media local only.
- **Recommendation**: Open PR or keep as pinned evidence branch.

### `research/casually-finance-editing-forensics`

- **Tip** `05e8635b` · 2026-11-15 · ghilmankhan · R · vs main +94/-6 · merge-base `08e71926` · 3073 files · PR none · CI no run
- **Areas changed**: `research/visual-forensics` (2081), `research/casually-finance-editing-forensics` (992)
- **Commits** (94 non-merge since merge-base; latest first): research: V006 AC1 SUB052 native verified (onset 2674, last 2682, cursor up); ledger v50/q; research: V006 AB1 EP0080 native verified (onset 2661, last 2665, multi-phase); ledger v49; research: V006 checkpoint AA1 SUB051 native verified (mid-stroke of red-stroke track, last; research: V006 checkpoint Z2 EP0079 native verify (card exit onset 2519 exact, last 2533; 
- **Purpose**: CF Video006 editing forensics ledger v50.
- **Completeness**: 94 ahead, 9 exclusive.
- **Unique value**: Latest V006 ledger.
- **Risks**: Shares history with CF lineage.
- **Recommendation**: Keep as evidence branch; merge after CF consolidation.

### `research/primitive-education-visual-forensics`

- **Tip** `ff2ff896` · 2026-11-06 · ghilmankhan · R · vs main +15/-6 · merge-base `08e71926` · 842 files · PR none · CI no run
- **Areas changed**: `research/visual-forensics` (842)
- **Commits** (15 non-merge since merge-base; latest first): research: Primitive Education visual forensics checkpoint N; research: Primitive Education visual forensics checkpoint M; research: Primitive Education visual forensics checkpoint L; research: Primitive Education visual forensics checkpoint K
- **Purpose**: Primitive Education visual forensics checkpoints J-N.
- **Completeness**: 15 commits; on hold.
- **Unique value**: Only copy.
- **Risks**: -
- **Recommendation**: Keep as evidence branch.

### `research/what-if-brain-preservation-batch1`

- **Tip** `abdcf8e0` · 2026-10-25 · ghilmankhan · R · vs main +139/-6 · merge-base `08e71926` · 1736 files · PR none · CI no run
- **Areas changed**: `research/finance-economics-intelligence` (1066), `research/visual-forensics` (545), `research/production-experiments` (82), `knowledge` (30), `reports` (7), `.gitattributes` (1), `README.md` (1), `docs/AI_SESSION_CONTEXT.md` (1)
- **Commits** (139 non-merge since merge-base; latest first): docs: add canonical YIOS master plan and session context; research: preserve distinct What If reports and frozen metadata batch 4; research: preserve What If production experiments batch 3; research: preserve What If per-video evidence batch 2
- **Purpose**: What If canonical brain batches 1-4 (stacked on older finance audits).
- **Completeness**: 139 ahead, 5 exclusive.
- **Unique value**: What If brain preservation.
- **Risks**: Conflicts with #44 on master plan docs.
- **Recommendation**: Reconcile with #44; merge one.

### `research/xkcd-whatif-visual-forensics`

- **Tip** `3c6145cc` · 2026-11-06 · ghilmankhan · R · vs main +19/-6 · merge-base `08e71926` · 1600 files · PR none · CI no run
- **Areas changed**: `research/visual-forensics` (1599), `data/intelligence` (1)
- **Commits** (19 non-merge since merge-base; latest first): research: xkcd What If visual forensics checkpoint R; research: xkcd What If visual forensics checkpoint Q; research: xkcd What If visual forensics checkpoint P; research: xkcd What If visual forensics checkpoint O
- **Purpose**: xkcd What If visual forensics checkpoints M-R.
- **Completeness**: 19 commits; pinned by START_HERE.
- **Unique value**: 29 closed videos of evidence.
- **Risks**: -
- **Recommendation**: Keep as pinned evidence branch.
