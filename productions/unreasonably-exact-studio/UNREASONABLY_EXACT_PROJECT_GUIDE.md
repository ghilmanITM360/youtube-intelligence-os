# Unreasonably Exact: project guide

**For any new Claude or Codex session.** This guide explains the whole project without the earlier conversations. Written 2026-11-26.

- **Local workspace:** `~/workprojects/unreasonably-exact/` (Machine B).
- **Version-controlled copy:** GitHub `ghilmanITM360/youtube-intelligence-os`, branch `production/unreasonably-exact-studio`, folder `productions/unreasonably-exact-studio/` (§15).

**Recommended reading order (§20):**
1. `START_HERE.md` (final report of the 2026-11-26 consolidation: `FINAL_CONSOLIDATION_REPORT_ROMAN_URDU.md`)
2. this guide
3. the production playbooks
4. the Claude–Codex protocol
5. the production tracker
6. the selected video project

---

## 1. Channel identity and objectives

- **Name:** *Unreasonably Exact* (@unreasonablyexact), chosen by the owner on 2026-11-18. Source: repo `research/what-if-channel-strategy/07_CHANNEL_BRANDING.md`.
- **Position:** "ridiculous questions, answered with real physics, with the working shown". The brand is the gap between an absurd premise and a precise answer.
- **Differentiator:** accuracy you can see. Models are labelled and disclosed ("Not to scale", "Simulated data", "Slowed down"), numbers are sourced, and the math is shown.
- **Visual motif:** a ruler or ladder.
- **Naming rule:** "What if" is kept out of the channel name (a crowded term, and Marvel holds a WHAT IF... comics mark). It may be used in titles.
- **Formats:** vertical science Shorts (1080×1920) and long-form science explainers.
- **Objective:** build a reusable production system, so each new film reuses assets, engine and process and reaches finished quality in fewer revisions.

## 2. Selected Top 10 videos

The owner-selected V3 lineup (2026-11-25) has 4 Long and 6 Short videos. The source is repo `productions/unreasonably-exact-script-rewrite-v3/UNREASONABLY_EXACT_NEW_TOP_10_VIDEOS_V3.md`. The list with production status is [`11-production-management/TOP_10_PRODUCTION_TRACKER.md`](11-production-management/TOP_10_PRODUCTION_TRACKER.md).

| Slot | Video | Format |
|---|---|---|
| 01 | Does a Higher Fall Always Hit Harder? | Long |
| 02 | Why Can a Skydiver Slow Down Without a Parachute? | Short |
| 03 | Why Does a Radio Signal Take a Whole Day to Reach Voyager 1? | Short |
| 04 | Could One Sideways Jump Put You in Orbit Around a Tiny World? | Long |
| 05 | Could You Jump Off Phobos and Never Come Back? | Short |
| 06 | How Do You Repair Voyager 1 When Every Reply Takes Two Days? | Long |
| 07 | How Long Does a Laser Take to Reach the Moon and Back? | Short |
| 08 | What Would Happen to the Ocean If the Moon Vanished? | Long |
| 09 | Would Earth Still Have Tides Without the Moon? | Short |
| 10 | How Far Has a Human Been From Every Other Person? | Short |

## 3. Completed productions

| Slot | Final | Length | Folder |
|---|---|---|---|
| 02 | **V15, owner-approved production master** (2026-11-25) | 110.04 s, 24 fps, 2,641 frames, −16 LUFS, no music | [`07-video-productions/SLOT02_skydiver-slowdown/v15/`](07-video-productions/SLOT02_skydiver-slowdown/v15/START_HERE.md) |
| 07 | **V3, owner-selected final; visual quality accepted** (2026-11-26) | 96.000 s, 30 fps, 2,880 frames, −16.4 LUFS | [`07-video-productions/SLOT07_lunar-laser-ranging/`](07-video-productions/SLOT07_lunar-laser-ranging/START_HERE.md) |

## 4. Current production status

- **Nothing is uploaded.** Upload needs an explicit owner instruction.
- **Open human checks for both films:**
  - listening on phone and headphones;
  - a Shorts-UI caption test;
  - a muted-viewer test.
- **Slot 07 only:** the music licence (Small_Variables.mp3) is unverified, so publish the `*_RIGHTS_CLEAR*` master.
- **Next video:** Slot 03 (Voyager signal). The brief is prepared, and the project waits for narration and an owner directive ([NEXT_VIDEO_BRIEF_SLOT03.md](11-production-management/NEXT_VIDEO_BRIEF_SLOT03.md)).
- **Channel dashboard:** [`11-production-management/MASTER_PRODUCTION_DASHBOARD.md`](11-production-management/MASTER_PRODUCTION_DASHBOARD.md).

## 5. Project directory structure

```
unreasonably-exact/
├── README.md · START_HERE.md · PROJECT_INDEX.md · CHANGELOG.md · UNREASONABLY_EXACT_PROJECT_GUIDE.md · MIGRATION_MANIFEST.csv
├── FINAL_CAPTIONED_VIDEOS/          quick-access copies of both captioned finals (owner request 2026-11-26)
├── 01-channel-strategy/             pointers to the repo strategy + Top 10
├── 02-production-playbooks/         UE playbook 1.1 · HumanCraft 4.1 · Claude–Codex protocol · production standards
├── 03-script-library/               approved pointers · working drafts (repo) · historical scripts · DOCX build tools
├── 04-shared-assets/                reusable art by family (celestial, environments, characters, props, graphics, fonts, rigs) + ASSET_CARD.md each
├── 05-animation-engine/             uemotion snapshot · validators · captions · audio · codex · scientific models · Slot 02 reference tools · ENGINE_GUIDE.md
├── 06-audio-library/                music (unverified) · SFX library (unknown licence) · generated (original) SFX · licensing register
├── 07-video-productions/
│   ├── SLOT02_skydiver-slowdown/    v15/ (the project) + FINAL_MASTERS/
│   └── SLOT07_lunar-laser-ranging/  the project + FINAL_MASTERS/
├── 08-research-library/             index of research (kept inside productions) + script science reviews
├── 09-production-templates/         codex-handoff · storyboard · asset-manifest · narration-alignment · quality-assurance
├── 10-production-retrospectives/    SLOT07 deep retrospective · SLOT02 summary
├── 11-production-management/        TOP_10 tracker · master dashboard · REUSABLE_ASSET_INDEX.csv · next video brief
└── 99-archive/original-downloads/   original zips and the as-delivered narration WAV
```

## 6. Purpose of every major folder

| Folder | Purpose | Rule |
|---|---|---|
| `02-production-playbooks/` | How to make a film | Canonical. Edit here and add a revision-history row |
| `04-shared-assets/` | Art that a new film may start from | Clone into a project; never edit a project's copy from here |
| `05-animation-engine/` | Code a new film copies and pins | Changes need a regression rebuild of Slot 07 (`ENGINE_GUIDE.md` §5) |
| `06-audio-library/` | Sounds and their licence status | Nothing unlicensed in a publication master |
| `07-video-productions/<SLOT>/` | One self-contained project per film | Relative paths only; finished renders are locked |
| `09-production-templates/` | Starting files for a new film | Copy them; do not edit them in place for a single film |
| `11-production-management/` | Status across films | The tracker and dashboard are updated at every milestone |
| `99-archive/` | Original downloads | Keep them; do not use them in productions |

## 7. Canonical production playbooks

| Document | Use it for |
|---|---|
| [`UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md`](02-production-playbooks/UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md) (1.1) | The channel's method: architecture, gates G0–G8, sound, captions, the 14-phase workflow, Top 10 plans, and the §21 Slot 07 lessons |
| [`HumanCraft_MASTER_Animation_Director_V4.md`](02-production-playbooks/HumanCraft_MASTER_Animation_Director_V4.md) (4.1) | Creative and animation-direction judgement, the 110-technique library, and the Part VI verified lessons |
| [`CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`](02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md) | Commissioning and accepting Codex artwork from the CLI |
| [`PRODUCTION_STANDARDS.md`](02-production-playbooks/PRODUCTION_STANDARDS.md) | Numbers and naming at a glance |

**Precedence:**
1. The owner's instructions.
2. The evidence files of a production.
3. These playbooks.

## 8. Claude and Codex responsibilities

| Claude | Codex | Owner |
|---|---|---|
| Research, script science, shot design, references, briefs | Illustration: one image per run, by editing a master | Script, narration, art and film acceptance |
| All measurements, acceptance tests, layer cuts, registration, rigs, code-drawn graphics, animation, sound, captions, QA | Writes only in its run folder; never self-approves | Listening, viewing, licence evidence, upload decision |
| Starts Codex from the shell (no prompt relay by the owner) | | |

## 9. Asset-generation workflow

1. **Reference sprint:** 2–3 decisive photos per object, indexed with source and licence.
2. **Codex master run:** bundled CLI, `-c model_reasoning_effort="high"`, references attached with `-i`.
3. **Log check:** `grep view_image` in the log, then read NOTES.md.
4. **Claude acceptance:** `validate_asset.py`, a magenta check and measured tests.
5. **Layers:** layer-cut runs (edits of the master), with IoU ≥ 0.97.
6. **Rig:** Claude measures pivots and writes the rig JSON, then runs a moving rig test.
7. **Corrections:** one defect per edit; re-measure every earlier pass.

The full protocol is in [`CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`](02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md).

## 10. Scientific research requirements

- Every on-screen number and claim is a row in the production's `SCIENTIFIC_CLAIMS_LEDGER.csv`, with a primary source.
- The model code **asserts** each number. In Slot 07, the stopwatch reads 2.56 and d = c·t/2 rounds to 384,000 km.
- Time-sensitive claims (mission distances, records) are rechecked before release.
- Simplifications are disclosed once, in the disclosure table.
- No AI inference is presented as a fact (repo `AGENTS.md`).

## 11. Animation and rendering architecture

- A custom Python renderer. Scenes are pure functions of time on a supersampled canvas in design units.
- Three clocks: narration, animation and model.
- Proof scenes with asserts, then a cut table that keeps each proof's clocks.
- Parallel frame rendering into ffmpeg.
- Slot 07 uses `uemotion` (`05-animation-engine/ENGINE_GUIDE.md`). Slot 02 V15 uses its own Cairo/rig renderer with mesh warp (`v15/tools/`).

## 12. Audio and caption systems

- **Audio.**
  - Generated SFX with a cue sheet that gives a reason per cue.
  - Music edit with a spectral seam and story-driven automation.
  - Ducking plus a speech-band carve.
  - Separation is measured in voiced windows; output −16 LUFS.
  - A rights-clear master is always built.
  - Tools: `05-animation-engine/audio/`.
- **Captions.**
  - Word times from whisper.cpp; phrase-level cues with balanced lines and Comic Neue Bold.
  - Three deliverables: an SRT, a burned MP4 and a clean MP4.
  - Tools: `05-animation-engine/captions/`.

## 13. Reusable asset library

[`04-shared-assets/README.md`](04-shared-assets/README.md) and [`11-production-management/REUSABLE_ASSET_INDEX.csv`](11-production-management/REUSABLE_ASSET_INDEX.csv): 41 entries (25 APPROVED_IN_FILM, 11 CANDIDATE, 5 REJECTED).

The families are:
- Earth and Moon;
- celestial environments;
- lunar terrain;
- observatory with telescope rig;
- Apollo astronaut;
- retroreflector;
- stopwatch;
- scientific motion graphics;
- parallax;
- fonts.

## 14. Production quality standards

[`02-production-playbooks/PRODUCTION_STANDARDS.md`](02-production-playbooks/PRODUCTION_STANDARDS.md) and [`09-production-templates/quality-assurance/QA_CHECKLIST.md`](09-production-templates/quality-assurance/QA_CHECKLIST.md). Key gates:
- G0 science;
- narration lock;
- art acceptance;
- G-open (0–7 s activity);
- G-text (disclosure table);
- G-mix (separation plus a rights-clear master);
- three independent reviews.

Human gates stay open until a human performs them.

## 15. GitHub branch information

- **Repository:** `ghilmanITM360/youtube-intelligence-os`. Canonical checkout on this Mac: `~/Documents/youtube-intelligence-os`.
- **Branch:** **`production/unreasonably-exact-studio`**, created from `research/what-if-channel-strategy-2026-11-18` at commit `5ee988ce`.

**Why a new branch** (the owner's stated preference, checked against the repo rules):
1. The production system (engine source, tools, asset cards, playbooks) is a different kind of content from the strategy research on the channel branch.
2. A new branch has no competing writer.
3. The remote showed no claim or integration refs for this work when publishing.
4. A normal fast-forward push without force protects other work.

The channel branch is untouched and remains the home of the strategy and script packages.

**Folder in the repo:** `productions/unreasonably-exact-studio/`. It mirrors this workspace's documents and source.

**What is not committed:**
- MP4s, WAV stems, the 4096×2048 textures, raw research media, reference photos (several are CC BY-SA);
- the unlicensed music and SFX;
- Python environments.

Their checksums are listed in the repo folder's `EXTERNAL_MEDIA_MANIFEST.csv`. The bytes stay on this Mac, in `~/workprojects/unreasonably-exact/`.

## 16. How to start a new video

1. Confirm the slot and the owner directive. Narration is **recorded and locked** before shot design.
2. Create `07-video-productions/SLOT<NN>_<topic>/` with this layout:
   - `narration/`, `animation/` (copy `05-animation-engine/uemotion/`), `assets/`, `codex_handoff/` (runs, references, guides_construction), `renders/`, `qa/`, `tools/`;
   - copy `09-production-templates/*`.
3. Science ledger (G0), then the reference sprint, then the Codex masters (parallel runs), then layers and rigs.
4. One proof per mechanism, with asserts. Render the 0–10 s opening first.
5. Cut table plus disclosure table, then the full render, the mix (rights-clear alongside) and captions.
6. Three reviews. Then the owner review package: phone review page, report in Roman Urdu, and an honest pending list.
7. Update the tracker, the dashboard and `CHANGELOG.md`.

## 17. How to rebuild an existing video

- **Slot 07:** [`REBUILD_INSTRUCTIONS.md`](07-video-productions/SLOT07_lunar-laser-ranging/REBUILD_INSTRUCTIONS.md). The non-destructive check is `tools/rebuild_check.py`, and it passed on 2026-11-26.
- **Slot 02:** `v15/START_HERE.md`. The one-command rebuild is `zsh tools/build_v15.sh`; the self-check is `.venv/bin/python tools/v15.py --check`, which passed on 2026-11-26 from the new location.
- **Never re-render into a locked final folder** without an owner instruction. Render into a copy.

## 18. How to resume interrupted work

1. Read `START_HERE.md`, then the production's `START_HERE.md` and the **last entry of its `PROGRESS_LOG.md`** (append-only).
2. Check the production dashboard (Slot 07: `MASTER_PRODUCTION_DASHBOARD.md`, regenerated by `python3 tools/build_dashboard.py` from `qa/work_items.csv`).
3. Look for running jobs before starting renders: `ps aux | grep -E 'ffmpeg|uepipe|codex exec'`.
4. Read Codex run state in `codex_handoff/runs/<ID>/codex.log`. A missing PNG means the run is unfinished or failed; never assume.
5. Before writing to GitHub, follow the repo `AGENTS.md`: writer coordination, no force-push, and no new worktree without owner approval.

## 19. Known limitations

- Human listening, real-time viewing, muted-viewer and Shorts-UI tests are not performed for either film.
- The Slot 07 music licence is unverified. Both SFX library collections are of unknown licence.
- `uemotion/narration.py` is bound to one film, and the engine needs the macOS fonts Menlo and Arial Bold.
- Slot 07 `MASTER_ASSET_MANIFEST.csv` is stale and `scientific_model/` is empty (see the retrospective, §12).
- Machine A's state is not visible from this Mac. The local workspace is on Machine B only; its large media are not in git.
- Copies of the playbooks outside this workspace (`~/Downloads/`, other project folders) are older revisions.

## 20. Recommended reading order

```
START_HERE.md
  → UNREASONABLY_EXACT_PROJECT_GUIDE.md (this file)
    → 02-production-playbooks/ (UE playbook §1, §14, §18, §21; HumanCraft Part I + VI; PRODUCTION_STANDARDS)
      → 02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md
        → 11-production-management/TOP_10_PRODUCTION_TRACKER.md (+ MASTER_PRODUCTION_DASHBOARD.md)
          → 07-video-productions/<selected slot>/START_HERE.md (or NEXT_VIDEO_BRIEF_SLOT03.md for the next film)
```
