# ADDENDUM — Cost-Aware Representative Sampling and Parallel Channel Branches

**Status:** Mandatory standing rules for `YOUTUBE_VISUAL_INTELLIGENCE_MASTER_RULEBOOK.md` and `CLAUDE.md`.

**Scope:** Only channels with actual, local, decodable MP4 reference videos qualify. This addendum does not weaken evidence requirements, the same-video visual reconstruction test, novel-scene tests, or any GO gate. **It limits how many videos receive costly deep analysis and permits multiple channels to run independently in parallel.**

## R27 — NEVER DEEP-ANALYZE EVERY AVAILABLE VIDEO BY DEFAULT

A channel may contain dozens or hundreds of local MP4 files. **Inventorying all MP4s is required; deeply analyzing all of them is prohibited by default.** Stop spending model tokens on near-duplicate videos when the target production grammar is already adequately understood and validated. Study *unique visual families, new mechanics and unresolved uncertainty*, not a fixed percentage of the library.

For example, if an eligible channel has 216 MP4s, do **not** perform frame-level annotation on 216 videos. Perform a low-cost technical inventory of 216, select a diverse subset for deep analysis and hold back unstudied reference videos for out-of-sample checks.

### R27.1 — Cost tiers

| Tier | Breadth | Allowed work | Purpose |
|---|---|---|---|
| T0 | Every eligible MP4 | File identity/provenance, ffprobe metadata, size, duration, fps/resolution, existing-analysis lookup, duplicates; optionally limited thumbnails/contact sheets for grouping | Cheap complete inventory, not full semantic inspection |
| T1 | Candidate pool | Sparse screenshots/keyframes, coarse cut statistics, visual-era/style categorization, estimated novelty and difficulty | Rank what to deeply inspect next |
| T2 | Selected information-rich videos | Frame/event-accurate annotation, layer/asset/camera/motion reconstruction blueprints and full evidence | Deep understanding only where it adds value |
| T3 | Representative held-out videos | Small targeted spot checks for missed visual families and blind validation (retain some truly unseen footage) | Test generalization, not expand scope indiscriminately |
| T4 | A short reference segment + original concept(s) | Independent asset construction, animation, rendering, frame-comparison QA and novel-scene production | Actual reproduction gate |

Do not send every sampled frame to the language model. First use inexpensive programmatic extraction, grouping, and contact sheets; send focused frame windows only for ambiguous/new visual techniques or motion-critical sequences. Cache outputs, reuse validated prior analyses and do not regenerate unchanged work.

### R27.2 — Initial target and limit (heuristic, not scientific law)

- Start with 4–6 deliberately diverse representative MP4s, reusing any previously validated detailed analyses in this count.
- Expand to approximately 12–18 *total* deeply analyzed MP4s **only as needed**. A channel with a stable template may need fewer.
- Default initial ceiling is **24–30 total** deeply analyzed MP4s; it is **not a target to fill automatically**. Analyze beyond that only with explicit evidence of important unrepresented visual families or failed reconstruction tests, and log the reason/expected information gain.
- These counts apply *per channel* and refer to **distinct MP4s**, not the number of screenshots, frames, scenes or transcripts.
- Video count must never override missing critical techniques. One important unique video may outweigh 20 repetitive ones.
- Record actual count, selected duration, estimated processing cost/time *only when measurable*, token/tool usage *only when observable*, and why any further batch is worth analyzing. Do not invent token or time estimates.

### R27.3 — Sampling method (representative + active-learning)

1. Build a low-cost catalog of ALL eligible MP4s and cross-reference verified existing analyses.
2. Group videos by visual era, format, approximate style, character/environment family, scene/animation complexity, recurring template and length.
3. Choose the first 4–6 to cover the widest plausible diversity, not simply latest, longest or highest-viewed.
4. For every analyzed video maintain a technique ledger: `technique_id`, `visual_family`, `source_video`, `timecode`, `first_seen`, `repeated_in`, `full_blueprint?`, `reconstruction_test?`, `remaining_uncertainty`.
5. Rank additional candidate videos by *anticipated novel technique coverage*, rare visual forms, meaningful unanswered questions and expected effect on reconstruction; avoid redundant examples unless necessary to learn variation.
6. Add further deep-analysis videos in small batches of **3–5**; after each batch measure which *new material techniques* were discovered, which uncertainties resolved, which reproduction tests improved, and what the marginal gain was.
7. Reserve at least **2 distinct reference videos**, where available, for targeted out-of-sample visual checks. Do not use every video for training/analysis before validation.
8. Revisit sampling ONLY when a reconstruction/novel-scene test reveals missing evidence or a targeted spot check discovers a new important visual family.

### R27.4 — Objective stopping / saturation rule

Stop expanding the deep-analysis sample (not the overall project) when ALL conditions hold:

- All **known material** visual families found during the low-cost catalog pass have a detailed production blueprint and sufficient representative evidence (usually at least 2 examples per common family; a rare family may have 1 comprehensive example with appropriately limited confidence).
- The **two most recent 3–5-video batches** each discover **no new critical visual family** and at most one new minor technique, with no consequential unresolved ambiguity.
- At least two previously unstudied MP4s (when available) have undergone a targeted spot check without revealing an unrepresented critical production technique.
- Known asset, animation, layering, camera, editing and reconstruction blockers are resolved sufficiently for the defined production scope.
- The mandatory same-reference visual reconstruction and original-scene generalization tests have been completed and passed; all other GO rules remain in force.

If saturation conditions pass but render tests fail, **do not blindly analyze another 20 videos**: first diagnose implementation versus missing evidence, and select only specific videos/segments needed to resolve the failure.

If tests pass before reaching 12 videos, do not force reaching 12. If tests fail beyond 30 videos, report uncovered techniques and the most efficient next evidence targets. A fixed count or score never grants GO by itself.

### R27.5 — Deferred videos / parallel enrichment

Create `CHANNEL_VISUAL_AUDIT/<channel_id>/VIDEO_SELECTION_REGISTER.csv` with columns:

`video_id, path, eligible, duration, existing_analysis, visual_cluster, candidate_novelty, estimated_value, selection_status, selection_reason, identified_unique_techniques, deep_analysis_done, holdout, deferred_reason, next_trigger`

Statuses: `INVENTORIED`, `COARSE_SCREENED`, `SELECTED_FOR_DEEP`, `DEEP_VERIFIED`, `VALIDATION_HOLDOUT`, `DEFERRED`, `OUT_OF_SCOPE`.

Create `DEFERRED_VIDEO_QUEUE.md`; all remaining eligible MP4s stay available for a **later enrichment phase**. Future deep inspection may happen **in a separate lane or branch** after the core GO, but is not a prerequisite for the first production-ready milestone. Never mark unanalyzed files as inspected or verified.

---

## R28 — ONE CHANNEL PER BRANCH, PARALLEL ISOLATED WORKTREES

**A channel is sequential WITHIN its own dedicated branch, but independent channels MAY be analyzed concurrently by separate agents/accounts in distinct worktrees or clones.** This explicitly supersedes any prior phrasing that forbids starting another channel until the first has GO *globally*. The channel GO gate is **per branch**, not a global blocker. Never mix evidence, style rules, artifacts or progress ledgers between channels.

### R28.1 — Discover the real repository state first

Before creating or switching branches, inspect:

- `git status --short` (do not overwrite or auto-stash user changes)
- `git branch -a`
- `git worktree list`
- `git remote -v`
- Current tracked `CLAUDE.md`, master rulebook, channel folders and exact location of local MP4s

Determine the true common base branch/commit. Prefer an existing designated stable visual-audit base, or propose `visual-intelligence/base` **without silently resetting any existing branch**. Preserve user branches, worktrees, stashes and current uncommitted changes. Do not invent a remote or assume push rights.

### R28.2 — Branch convention and example

Use one branch per channel, for example:

- `visual-audit/casual-finance`
- `visual-audit/science-channel`
- `visual-audit/health-channel`

Use one independent working directory per active channel/agent. **Illustration only** (execute after verifying real base and paths):

```bash
# From the actual Git repository; assume a verified stable base exists:
git worktree add -b visual-audit/casual-finance ../visual-audit-worktrees/casual-finance visual-intelligence/base
# Another independent agent can use:
git worktree add -b visual-audit/science-channel ../visual-audit-worktrees/science-channel visual-intelligence/base
git worktree list
```

Do not use `-B`, force resets, forced checkout, forced pushes or destructive cleanup. If a channel branch/worktree already exists, **reuse or attach safely**; do not overwrite or recreate it. If separate Claude accounts run on different machines or containers, each needs its own authorized clone and access to the reference MP4 dataset; share changes via approved remote branches. Multiple agents should not simultaneously push unrelated changes to the same branch.

### R28.3 — Shared rulebook versus isolated channel intelligence

- Common base: universal `CLAUDE.md`, the master rulebook, this addendum, shared tooling and generic schemas.
- Channel branch: `CHANNEL_VISUAL_AUDIT/<channel_id>/`, evidence records, samples, visual DNA, assets/specs, reconstruction code/renders and channel progress ledger.
- Each branch must include `CHANNEL_AUDIT_PROGRESS.md` recording actual branch name, HEAD commit, worktree path, local MP4 source, verified sample counts, saturation status, tests and next action.
- Common-method changes should be proposed back to the base via a focused review/merge, and brought into channel branches by controlled merges/rebases. Never indiscriminately merge another channel's distinct assets and creative identity.
- Maintain a root-level cross-channel status index only if one designated coordinator owns it, to prevent concurrent edit conflicts.

### R28.4 — Large reference media and paths

`git worktree` shares Git history, **not untracked files from arbitrary working directories**. MP4s stored outside Git or in ignored folders may not appear in new worktrees. Verify that each agent has **read-only access** to the actual source MP4s; use a common approved local dataset path, safe mounts, or documented workspace-specific references. Avoid accidentally committing huge reference MP4s, proprietary raw files, temporary renders, API keys or credentials. Decide any Git LFS/external-media policy based on actual repository requirements and permissions.

### R28.5 — Cross-account handoff

At every checkpoint:

1. Save stable channel-scoped Markdown/CSV/JSON results and precise evidence references.
2. Record progress, sample decisions, outstanding gaps, failed experiments and exact next step.
3. Commit only appropriate tracked files in that channel branch; never create invented completion summaries.
4. Push the branch to the configured remote **only if authorized and configured**; verify the remote branch/commit. Otherwise provide the exact branch/commit and blocker.
5. The next Claude account must first read the project's `CLAUDE.md`, master rulebook, this addendum and its channel progress ledger; then verify current Git status and local MP4 access.

### R28.6 — Parallel execution and GO semantics

- Different agents/channels **CAN proceed in parallel** without waiting for another channel's GO.
- **Within a channel**, only promote its production grammar to ready when its own saturation, sample adequacy, recreation tests, novel-scene tests and GO gate pass.
- Do not let two agents produce contradictory canonical results for the same channel without an explicit owner/reconciliation process.
- A channel may be GO for the defined initial production scope while a later optional `ENRICHMENT` lane studies additional deferred videos.
- NO-GO / CONDITIONAL GO / GO state is local to each channel branch; one channel's verdict cannot be borrowed by another.

---

## R29 — FIRST ACTIONS ON RECEIVING THIS ADDENDUM

1. Read the existing master rulebook and `CLAUDE.md`; locate all previous analysis and progress files.
2. Reconcile these rules into standing instructions without losing existing requirements.
3. Inspect Git repository/worktree/branch state and the true MP4 storage paths.
4. Create a low-cost full MP4 inventory but **do not deep-analyze all videos**.
5. Record a justified per-channel sample plan and selected information-rich videos based on existing data.
6. Set up or reuse one safely isolated branch/worktree per eligible active channel, without destructive Git operations.
7. Immediately continue real scene/asset/motion analysis for the active channel, updating the technique ledger, saturation checks and progress ledger after every batch.
8. Run required render tests when supported by sufficient evidence. Only report GO on completed verified evidence and tests.
9. Preserve and defer remaining videos for optional later enrichment.

**Outcome:** Minimize token/time waste, maximize visual knowledge and early reconstruction proof, and support independently resumable parallel agents without mixing channel knowledge.
