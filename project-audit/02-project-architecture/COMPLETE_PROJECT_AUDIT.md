# Complete Project Audit

Date 2026-11-17. Baseline `origin/main` @ `e96f7f8f`. Companion to `docs/project-audit/*` (2026-11-11, on the current branch). This audit re-checked those findings, kept the ones that still hold, and added the branch-wide and data-wide view.

## 1. What the project is

A private research workspace in which one owner (a multi-channel YouTube operator) and AI agents collect competitor evidence, record provenance, analyse it in five intelligence layers, and turn it into evidence-traceable content plans and production packages. Its core value is **traceability and honesty**: every claim points to evidence, and inference is labelled as inference.

## 2. Workstreams (from START_HERE + branches)

| Workstream | Scale | Where | State |
|---|---|---|---|
| V1 intelligence (5 channels) | 10 inventory channels / 667 videos; 75 registry channels / 2,303 videos | main | complete |
| Finance/Economics | 1,612 videos / 27 channels (audit); 69 channels / 3,634 videos (complete DB) | finance lineage, finance-complete branch | 558 accepted, 26/558 reanalysed |
| Casual Finance visual forensics | 206 catalog videos, 20-video target | CF lineage (pinned) | 19/20 visual-closed; 0 AV sign-off |
| xkcd What If | 91 census | xkcd branch (pinned) | 29 closed |
| Senior Health | 159 channels / 5,802 videos (core DB); 25 channels / 1,037 videos (Chrome merge) | SH branches, current branch | Reports 1-6; several PARTIAL |
| Production | Finance Shorts 01/02, Dr Rehan, three After-60 videos | production branches | 01 blocked on audio |
| Barely Evolved, Primitive Education | — | pinned branches | lower priority / on hold |

## 3. Health check (re-verified today)

| Check | Result | Source |
|---|---|---|
| CI on main | success 2026-11-17 | `gh run list` |
| DB integrity | inventory/registry/reference: readable read-only; prior audit `integrity_check ok` | sqlite read-only |
| Tests | 50 test files on main; CI green. 462 pass / 1 skip measured 2026-11-11 (current branch) | CI, prior audit |
| Open PRs | 23 open, many draft; 6 with CI failing before any step ran; #36/#50 fail the DB allowlist | `gh` |
| Prior debt D1 (finance gates not in CI) | **still open** on main; fixed on #45 | workflow file |
| Prior debt D2 (`python-docx` undeclared) | **still open** | `pyproject.toml` |
| Prior debt D5 (Apify no retry) | still open | code |

## 4. New findings in this audit

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| A1 | High | **Video data is split across 5 SQLite DBs with overlapping IDs** (10,553 unique video IDs: inventory 667, registry 2,303, finance-complete 3,634, senior-health-core 5,802, senior-health-apify 501; e.g. registry ∩ finance = 726, inventory ∩ senior-health = 425). Three DBs exist only on branches. | ID-overlap query, 03-data-architecture |
| A2 | High | No unified entity/read model or service boundary. A UI is blocked on this, not on intelligence coverage (this confirms the 2026-09-11 handoff). | code |
| A3 | Med | `video_type` not normalized: registry has `video` 1,150, `regular video` 890, NULL 159, `shorts` 90, `Short` 14; SH core adds `videos` 3,801 and `streams` 107. | group-by queries |
| A4 | Med | Three channel-ID schemes (`CH-0000NN`, registry `canonical_channel_id`, YouTube `UC…`). | schemas |
| A5 | Med | Inverted dependency `report_channel_strategy_intelligence → run_youtube_intelligence`. | AST scan |
| A6 | Med | Unrelated workstreams stacked on the finance lineage (Senior Health reports, CF inventory, What If brain). | containment |
| A7 | Med | Reference KB migration `011` exists only on the finance lineage; main's `AGENTS.md` mandates a framework gate main cannot run. | `git diff origin/main -- schemas` |
| A8 | High (data loss) | ~843 MB of thumbnail snapshots exist only in a local stash branch; ~15 GB of frames/audio and 454 MP4s are verified on one Mac only. | 2026-11-17 audit, START_HERE |
| A9 | Low | 3 orphan `yios-test/*` refs on origin. | merge-base |
| A10 | Info | The owner's real "UI" today is generated **PDF/HTML reports and simple guides** (finance PDF 16-21, SH blueprints, Dr Rehan recording pack). | branch files |

## 5. Workflow traces

1. **Competitor data → plan:** owner file → `data/raw` (hash) → `register_structured_source` → `youtube_inventory.db` → `build_youtube_channel_registry` → registry DB → `report_*` → `data/intelligence/channels/<CH>` → `run_youtube_intelligence --channel CH --opportunity …` → `data/intelligence/plans/<CH>-…json/.md` → owner reads MD.
2. **Finance audit:** registry (frozen copy on #45) → queue → per-video NICK audit (agent) → validators (`validate_audit_966`, `reference_comparison.check_coverage`) → accepted → reanalysis records (`SEMANTIC_REVIEW_PENDING`) → human review.
3. **Visual forensics:** local MP4 → frames/audio under `~/YIOS-local-audits` → per-video ledger + seals (SHA256SUMS) → `VISUAL_ANALYSIS_COMPLETE` → evidence map CSV → START_HERE.
4. **Production:** plan/script → slop gate (`check_slop_risk.py`) → assets/renderer → package → `production_pipeline validate` (`ready_for_capcut`).

## 6. Security and privacy (unchanged from 2026-11-11 unless noted)

- No secrets found by the scanner; Apify token is env-only.
- First-party analytics gitignored by design; any UI must stay local-first.
- Private media in git history (5.4 GB) awaits an owner decision.
- Medical content (Senior Health, Dr Rehan) carries `medical_validation_required`; a UI must show that flag, never hide it.

## 7. Verdict

The backend is a **mature, honest evidence engine with no presentation layer**. The best next investment is not more intelligence. It is (1) data-model consolidation into one read model and (2) a read-only Explorer that keeps the evidence-layer distinction. Both are V2 and need the owner's explicit go-ahead (AGENTS.md rule 12).
