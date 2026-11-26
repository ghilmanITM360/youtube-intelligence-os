# UNREASONABLY EXACT: Master Animation Production Playbook

**Primary production reference for Claude and Codex sessions.** Built from a reverse-engineering audit of the V15 "Skydiver slowdown" production and the V8 to V14 history behind it. Audit date: **2026-11-25**. Location: project root, outside the version folders. **V15 was not modified.**

> **Status.** This is a reference, not an acceptance record. Every V15 automated gate is closed; **no human listening, no continuous phone playback and no owner acceptance of V15 are on record** (§17). Items tagged **PROPOSED**, **UNVERIFIED**, **ESTIMATE** or **NOT PERFORMED** are the playbook's own or are unresolved (legend in §1.2; register in §20.3).

## Revision history

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-11-25 | 1.0 | First edition: a reverse-engineering audit of Slot 02 V15 (Skydiver) and its V8–V14 history | Claude |
| 2026-11-26 | 1.1 | Added §21, the sixteen verified Slot 07 V1–V3 lessons, kept apart from proposed standards. Status block updated: V15 is the owner-approved production master and Slot 07 V3 is owner-selected. New canonical location `unreasonably-exact/02-production-playbooks/`. Sections 1–20 and the appendices are unchanged | Claude |

**Canonical copy.** `unreasonably-exact/02-production-playbooks/UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md`, published to GitHub branch `production/unreasonably-exact-studio`. Before this revision, the copies in `~/Downloads/` (three files) and in `S07/codex_handoff/guides/` were byte-identical (sha256 `b0641d826151b229…`). They are left untouched as historical 1.0 mirrors.

> **Status update (2026-11-26).** The owner approved Slot 02 V15 as the final production master on 2026-11-25. The owner selected Slot 07 V3 as its final production version and accepted its visual quality on 2026-11-26. For both films the human listening and publication checks are still open, and nothing has been uploaded. The status block below is the 2026-11-25 original and is kept for history.

## Table of contents

- [Executive summary: the ten facts that matter most](#executive-summary-the-ten-facts-that-matter-most)
- [1. Purpose, scope and status legend](#1-purpose-scope-and-status-legend)
  - [1.1 What this document is](#11-what-this-document-is)
  - [1.2 Status legend (used throughout)](#12-status-legend-used-throughout)
  - [1.3 Who reads what](#13-who-reads-what)
  - [1.4 Precedence](#14-precedence)
- [2. Evidence base and audit method](#2-evidence-base-and-audit-method)
  - [2.1 Where the project actually is](#21-where-the-project-actually-is)
  - [2.2 What was inspected](#22-what-was-inspected)
  - [2.3 What was measured or re-verified independently in this audit](#23-what-was-measured-or-re-verified-independently-in-this-audit)
  - [2.4 What was **not** done (read this before relying on the document)](#24-what-was-not-done-read-this-before-relying-on-the-document)
  - [2.5 Evidence rules used](#25-evidence-rules-used)
- [3. How V15 was created: the production lifecycle](#3-how-v15-was-created-the-production-lifecycle)
  - [3.1 Stage 1: Question and research](#31-stage-1-question-and-research)
  - [3.2 Stage 2: Script and human narration](#32-stage-2-script-and-human-narration)
  - [3.3 Stage 3: Storyboard and visual beats](#33-stage-3-storyboard-and-visual-beats)
  - [3.4 Stage 4: Asset creation and rigging](#34-stage-4-asset-creation-and-rigging)
  - [3.5 Stage 5: Animation and scientific models](#35-stage-5-animation-and-scientific-models)
  - [3.6 Stage 6: Audio, captions and editing](#36-stage-6-audio-captions-and-editing)
  - [3.7 Stage 7: Rendering and quality review](#37-stage-7-rendering-and-quality-review)
  - [3.8 Stage 8: Final production master](#38-stage-8-final-production-master)
- [4. Version-by-version production history (V8 → V15)](#4-version-by-version-production-history-v8--v15)
  - [4.1 What is verified and what is not](#41-what-is-verified-and-what-is-not)
  - [4.2 Timeline](#42-timeline)
  - [4.3 Defect lifecycle (the lessons behind the table in the brief)](#43-defect-lifecycle-the-lessons-behind-the-table-in-the-brief)
- [5. Professional animation research and tool review](#5-professional-animation-research-and-tool-review)
  - [5.1 What V15 actually used, in one table](#51-what-v15-actually-used-in-one-table)
  - [5.2 The nine tools named in the brief](#52-the-nine-tools-named-in-the-brief)
  - [5.3 Other tools, one line each (all RECOMMENDED FUTURE or REVIEWED; none in V15)](#53-other-tools-one-line-each-all-recommended-future-or-reviewed-none-in-v15)
  - [5.4 Local reference material](#54-local-reference-material)
  - [5.5 The professional-technique findings, applied to this channel](#55-the-professional-technique-findings-applied-to-this-channel)
  - [5.6 Research defaults for the next films](#56-research-defaults-for-the-next-films)
  - [5.7 Decision for the next films](#57-decision-for-the-next-films)
- [6. V15 technical architecture (as implemented)](#6-v15-technical-architecture-as-implemented)
  - [6.1 One-page map](#61-one-page-map)
  - [6.2 Rendering engine](#62-rendering-engine)
  - [6.3 Coordinate systems and the three clocks](#63-coordinate-systems-and-the-three-clocks)
  - [6.4 Layer hierarchy (back to front)](#64-layer-hierarchy-back-to-front)
  - [6.5 Camera transformations](#65-camera-transformations)
  - [6.6 Easing and interpolation](#66-easing-and-interpolation)
  - [6.7 Character deformation](#67-character-deformation)
  - [6.8 Scientific state management](#68-scientific-state-management)
  - [6.9 Audio, subtitles and encoding](#69-audio-subtitles-and-encoding)
  - [6.10 Reusable modules vs. debt](#610-reusable-modules-vs-debt)
- [7. Character animation system and the Claude → Codex asset request](#7-character-animation-system-and-the-claude--codex-asset-request)
  - [7.1 What V15 actually has (verified in the tree)](#71-what-v15-actually-has-verified-in-the-tree)
  - [7.2 Rig decision tree for a new character (PROPOSED, derived from the V8–V15 failures)](#72-rig-decision-tree-for-a-new-character-proposed-derived-from-the-v8v15-failures)
  - [7.3 Standard character package (PROPOSED standard; every field is checkable)](#73-standard-character-package-proposed-standard-every-field-is-checkable)
  - [7.4 Secondary motion rules (verified where marked)](#74-secondary-motion-rules-verified-where-marked)
  - [7.5 What the owner rejected or QA found, as acceptance criteria](#75-what-the-owner-rejected-or-qa-found-as-acceptance-criteria)
  - [7.6 The standard Claude → Codex asset request (copy this; fill every `<…>`)](#76-the-standard-claude--codex-asset-request-copy-this-fill-every-)
  - [7.7 Asset validation](#77-asset-validation)
  - [7.8 What to ask Codex for in the next nine films](#78-what-to-ask-codex-for-in-the-next-nine-films)
- [8. Codex and Claude: responsibilities, naming, folders and asset standards](#8-codex-and-claude-responsibilities-naming-folders-and-asset-standards)
  - [8.1 Who does what](#81-who-does-what)
  - [8.2 Naming rules](#82-naming-rules)
  - [8.3 Transparency and resolution standards](#83-transparency-and-resolution-standards)
  - [8.4 Manifest schemas](#84-manifest-schemas)
  - [8.5 The handoff protocol (the order in which things happen)](#85-the-handoff-protocol-the-order-in-which-things-happen)
  - [8.6 Acceptance tests Claude runs before using any art](#86-acceptance-tests-claude-runs-before-using-any-art)
  - [8.7 Failure modes observed in handoffs (one line each, with the version)](#87-failure-modes-observed-in-handoffs-one-line-each-with-the-version)
- [9. Scientific visualization engine](#9-scientific-visualization-engine)
  - [9.1 What V15 built (verified; code excerpts are in §6.8)](#91-what-v15-built-verified-code-excerpts-are-in-68)
  - [9.2 The generalised engine (PROPOSED structure; the V15 files are the template)](#92-the-generalised-engine-proposed-structure-the-v15-files-are-the-template)
  - [9.3 The six-way taxonomy (every number and every drawing falls in exactly one primary class)](#93-the-six-way-taxonomy-every-number-and-every-drawing-falls-in-exactly-one-primary-class)
  - [9.4 The verification checklist (run for every film; each row needs a result and an evidence path)](#94-the-verification-checklist-run-for-every-film-each-row-needs-a-result-and-an-evidence-path)
  - [9.5 Generalising the engine to the remaining scripts](#95-generalising-the-engine-to-the-remaining-scripts)
  - [9.6 What would make a visual scientifically wrong even when the numbers are right](#96-what-would-make-a-visual-scientifically-wrong-even-when-the-numbers-are-right)
- [10. Motion-design system](#10-motion-design-system)
  - [10.1 Primitive library (all verified in `v15.py` / `v15_shots.py`; function names are real)](#101-primitive-library-all-verified-in-v15py--v15_shotspy-function-names-are-real)
  - [10.2 Reveal rules (how things appear)](#102-reveal-rules-how-things-appear)
  - [10.3 The text budget (the single biggest cause of cluttered frames)](#103-the-text-budget-the-single-biggest-cause-of-cluttered-frames)
  - [10.4 Reusable scene recipes (all from V15; each lists its shot IDs)](#104-reusable-scene-recipes-all-from-v15-each-lists-its-shot-ids)
  - [10.5 Colour, contrast and accessibility](#105-colour-contrast-and-accessibility)
  - [10.6 Checks that belong to the motion layer](#106-checks-that-belong-to-the-motion-layer)
- [11. Human narration-first production](#11-human-narration-first-production)
  - [11.1 What actually happened in V15 (verified)](#111-what-actually-happened-in-v15-verified)
  - [11.2 The reusable process: build every video around the final human narration](#112-the-reusable-process-build-every-video-around-the-final-human-narration)
- [12. Professional sound-design system](#12-professional-sound-design-system)
  - [12.1 V15 audio, in one table](#121-v15-audio-in-one-table)
  - [12.2 Dialogue-first mixing: ducking, carving, masking](#122-dialogue-first-mixing-ducking-carving-masking)
  - [12.3 Mastering](#123-mastering)
  - [12.4 The V14 → V15 improvement, and why it matters](#124-the-v14--v15-improvement-and-why-it-matters)
  - [12.5 Reusable sound categories](#125-reusable-sound-categories)
  - [12.6 SFX library audit](#126-sfx-library-audit)
  - [12.7 Standard sound workflow for future films](#127-standard-sound-workflow-for-future-films)
- [13. Caption production system](#13-caption-production-system)
  - [13.1 What V15 does (verified; measured on the shipped files in this audit)](#131-what-v15-does-verified-measured-on-the-shipped-files-in-this-audit)
  - [13.2 The reusable caption system (PROPOSED standard built on the above)](#132-the-reusable-caption-system-proposed-standard-built-on-the-above)
- [14. The 14-phase production workflow](#14-the-14-phase-production-workflow)
  - [Phase 1: Topic validation](#phase-1-topic-validation)
  - [Phase 2: Scientific research](#phase-2-scientific-research)
  - [Phase 3: Scriptwriting](#phase-3-scriptwriting)
  - [Phase 4: Human recording](#phase-4-human-recording)
  - [Phase 5: Visual planning](#phase-5-visual-planning)
  - [Phase 6: Asset generation](#phase-6-asset-generation)
  - [Phase 7: Animation](#phase-7-animation)
  - [Phase 8: Scientific graphics](#phase-8-scientific-graphics)
  - [Phase 9: Editing](#phase-9-editing)
  - [Phase 10: Audio](#phase-10-audio)
  - [Phase 11: Captions](#phase-11-captions)
  - [Phase 12: Rendering](#phase-12-rendering)
  - [Phase 13: QA](#phase-13-qa)
  - [Phase 14: Delivery](#phase-14-delivery)
- [15. Applying the playbook to the Top 10 V3 script package](#15-applying-the-playbook-to-the-top-10-v3-script-package)
  - [15.1 Status and authority (read this before planning)](#151-status-and-authority-read-this-before-planning)
  - [15.2 What carries over from V15 (reusable inventory)](#152-what-carries-over-from-v15-reusable-inventory)
  - [15.3 Production card per video](#153-production-card-per-video)
  - [15.4 Cross-video findings](#154-cross-video-findings)
  - [15.5 Recommended production order (cheapest reusable-first; **differs from the owner's slot order, so confirm it first**)](#155-recommended-production-order-cheapest-reusable-first-differs-from-the-owners-slot-order-so-confirm-it-first)
  - [15.6 Strategy: Shorts versus long-form](#156-strategy-shorts-versus-long-form)
- [16. Reusable production project template](#16-reusable-production-project-template)
  - [16.1 The directory structure (the brief's tree, with what goes in each folder)](#161-the-directory-structure-the-briefs-tree-with-what-goes-in-each-folder)
  - [16.2 Where V15 differs (so a session can map the old folder to the template)](#162-where-v15-differs-so-a-session-can-map-the-old-folder-to-the-template)
  - [16.3 What is shared globally and what stays project-specific](#163-what-is-shared-globally-and-what-stays-project-specific)
  - [16.4 `START_HERE.md` standard (the file a new session reads first)](#164-start_heremd-standard-the-file-a-new-session-reads-first)
- [17. Quality assurance framework](#17-quality-assurance-framework)
  - [17.1 The two rules that govern every row](#171-the-two-rules-that-govern-every-row)
  - [17.2 What V15's QA did and did not establish (state this in every handoff)](#172-what-v15s-qa-did-and-did-not-establish-state-this-in-every-handoff)
  - [17.3 The QA checklist (16 areas; A = automated, H = human; every H item leaves a record in `qa/human/`)](#173-the-qa-checklist-16-areas-a--automated-h--human-every-h-item-leaves-a-record-in-qahuman)
  - [17.4 The acceptance gate (what must be true before a film is called final)](#174-the-acceptance-gate-what-must-be-true-before-a-film-is-called-final)
  - [17.5 Review records (templates)](#175-review-records-templates)
  - [17.6 Why this framework looks the way it does](#176-why-this-framework-looks-the-way-it-does)
- [18. Root-cause analysis and the workflow that removes repetitive revisions](#18-root-cause-analysis-and-the-workflow-that-removes-repetitive-revisions)
  - [18.1 What the version count really measures](#181-what-the-version-count-really-measures)
  - [18.2 The nine causes the brief names, with the evidence and the gate that catches each](#182-the-nine-causes-the-brief-names-with-the-evidence-and-the-gate-that-catches-each)
  - [18.3 Defect lifecycle in one table (from the brief's problem → lesson list)](#183-defect-lifecycle-in-one-table-from-the-briefs-problem--lesson-list)
  - [18.4 The pre-render gates G0–G8 (each blocks the next expensive step)](#184-the-pre-render-gates-g0g8-each-blocks-the-next-expensive-step)
  - [18.5 Regression checks (re-run at every build, because these recurred)](#185-regression-checks-re-run-at-every-build-because-these-recurred)
  - [18.6 Expected effect (ESTIMATES, not measurements)](#186-expected-effect-estimates-not-measurements)
- [19. Production efficiency and automation](#19-production-efficiency-and-automation)
  - [19.1 Automation opportunities (the 13 the brief lists)](#191-automation-opportunities-the-13-the-brief-lists)
  - [19.2 What must stay human (creative and approval judgement)](#192-what-must-stay-human-creative-and-approval-judgement)
  - [19.3 Estimated production time and effort for future films (ESTIMATES)](#193-estimated-production-time-and-effort-for-future-films-estimates)
  - [19.4 Risks to the estimates](#194-risks-to-the-estimates)
- [20. Source references, checklists and appendices](#20-source-references-checklists-and-appendices)
  - [20.1 Sources](#201-sources)
  - [20.2 Practical production checklists](#202-practical-production-checklists)
  - [20.3 Open-items register (everything this audit could not close)](#203-open-items-register-everything-this-audit-could-not-close)
  - [20.4 V15 key numbers (quick reference; each is in the section noted)](#204-v15-key-numbers-quick-reference-each-is-in-the-section-noted)
- [21. Slot 07 V1–V3 lessons (added 2026-11-26)](#21-slot-07-v1v3-lessons-added-2026-11-26)
  - [21.1 The sixteen lessons](#211-the-sixteen-lessons)
  - [21.2 Workflow changes that follow (PROPOSED for Slot 03 onward)](#212-workflow-changes-that-follow-proposed-for-slot-03-onward)
  - [21.3 What Slot 07 did not prove](#213-what-slot-07-did-not-prove)
- [Appendix B: reference asset validator (PROPOSED standard; tested in this audit)](#appendix-b-reference-asset-validator-proposed-standard-tested-in-this-audit)

---

## Executive summary: the ten facts that matter most

1. **V15 is a custom Python/Cairo renderer** (design space 360×640 rendered at 1080×1920, 24 fps, 2,641 frames, 25 shots, 110.04 s) driven by **three clocks** (film time, design time via a monotone warp, model time via `MODEL_MAP`) and **one scientific state function** that the model-section shots read (§6, §9).
2. **The character is one continuous Codex drawing deformed by a mesh warp** (32 px grid; knees ±2.6°, wrists ±4°; cloth amplitude `1 + 4.2·load^1.3` with `load = drag/weight`), after four architecture changes forced by failed art (§7, §3.4).
3. **The recurring cause of revisions was art without acceptance tests** and a narration that changed late; the fix is a set of nine pre-render gates, G0–G8 (§18).
4. **Narration comes first.** V9–V13 were built on a 78.2 s narration that was never confirmed; V14 swapped in Hamza's 110 s recording and needed a 0.26–1.40× warp. The reusable process records first and designs on real word timing (§11).
5. **Audio is proved by separation, not loudness.** V14 and V15 are both −16 LUFS; the median voice-minus-background gap went from 10.5 dB to 20.7 dB (§12.4).
6. **Captions are separate from the picture** (clean MP4, burned MP4, SRT). V15's check protects only four graphic colours and its position has **not** been tested against the Shorts UI (§13).
7. **Every automated V15 gate is closed; the human gates are not.** No listening, no owner acceptance, and only sampled playback are recorded. The playbook makes these explicit rows that no agent can close (§17).
8. **Nothing is rights-cleared in the SFX libraries** (83 library clips in the licence manifest are `UNKNOWN`; a second zip is unverified); V15's publication master uses only generated cues and the owner's own recording (§12.6).
9. **Tool verdict:** keep Cairo + whisper.cpp + ffmpeg; pilot HyperFrames once in isolation; skip Remotion (licence watch), EffectCraft, Claude Animated Shorts, WhisperX, aeneas (§5).
10. **Nine films remain.** Build order by reuse: 07, 03, 09, 05, 10, 06, 04, 08, 01; the shot-level beat maps do not exist yet and are the real gap before production (§15).

---

## 1. Purpose, scope and status legend

### 1.1 What this document is

This is the **master production playbook for the Unreasonably Exact channel** (vertical 1080×1920 science animations and long-form science documentaries). It is the result of a reverse-engineering audit of the **V15 "Skydiver slowdown" film** and of the V8–V14 history that led to it, converted into a reusable system for the nine remaining Top-10 videos and for later films. It is written so that **a Claude or Codex session that has never seen the original conversation can use it**: every claim names the file, number or source it came from, and every proposal is labelled as a proposal.

It is **not a generic animation guide.** Each major recommendation is grounded in one of four things, and says which: V15 *implementation* (code or files that exist), *documented production evidence* (QA reports, histories), *verified research* (a source was read), or an *explicitly identified future improvement* (labelled **PROPOSED**).

### 1.2 Status legend (used throughout)

| Tag | Meaning |
|---|---|
| **VERIFIED** | Read from the V15 source or files in this audit, or reproduced by a command run in this audit |
| **MEASURED** | A number computed in this audit from the actual files (SRT statistics, audio separation, checksums, recomputed physics) |
| **INFERRED** | A conclusion drawn from evidence but not directly stated by it; the inference is shown |
| **UNAVAILABLE** | The evidence no longer exists (V1–V7; V8–V12 renders; the owner's briefs and screenshots) |
| **PROPOSED** | A recommendation, standard or estimate that is **not** in V15 and has not been tested; it is the playbook's own |
| **UNVERIFIED** | A claim from a source that could not be confirmed, or a practitioner default |
| **NOT PERFORMED** | A human step (listening, watching, phone test, owner acceptance) that has **not** happened. An agent cannot close it |
| **ESTIMATE** | A time or effort figure reasoned from the record, never measured (§19) |
| **V / V-2nd** | (research) verified from a primary page / from a secondary source quoting a primary one |

Tools used in V15 are always distinguished from tools merely recommended: the three labels **USED IN V15**, **REVIEWED** and **RECOMMENDED FUTURE** appear in §5.

### 1.3 Who reads what

| Reader | Start with | Then |
|---|---|---|
| A **new Claude session** about to build a film | §1–§2, §14 (workflow), §18 (gates), §6 (architecture), §20 checklists | §9 (science), §11–§13 (narration, sound, captions) |
| A **Codex session** asked for art | §7 (request template, validation), §8 (responsibilities, naming, manifests) | §10 (what the art will be used for), §15 (which characters and environments are needed) |
| The **owner** deciding what to approve | §17 (what only a human can do), §18.4 (gates), §15 (production order) | §5 (tool decisions), §19 (estimates) |
| Anyone auditing this document | §2 (method and limits), §20 (open-items register, sources) | |

### 1.4 Precedence

If this playbook disagrees with a V15 file, **the V15 file governs** (it is the evidence). If it disagrees with the owner's instructions, the owner governs. The owner's brief for this audit (20 sections plus a final directive) is the source of this document's structure; each of its 20 sections has the same number here.

---

## 2. Evidence base and audit method

### 2.1 Where the project actually is

The brief names `~/workprojects/unreasonably-exact/skydiver-slowdown/v15/`. **On this Mac the V15 folder is `/Users/ghilmankhan/workprojects/unreasonably-exact/v15/`** (no `skydiver-slowdown` level). Earlier records refer to another path on the build machine (`/Users/ghilmanislam360/GhilmanProjects/skydiver-slowdown/`); that machine's files are not here. V15 is 1.1 GB, 3,452 files. This document is saved at the project root, **outside** the version folders, as the brief requires.

### 2.2 What was inspected

- **Final videos and exports:** `SKYDIVER_SLOWDOWN_FINAL_V15.mp4`, `…_CAPTIONS.mp4`, `…_picture.mp4`, the `.srt`; probed with ffprobe (both finals: h264 1080×1920, 24 fps, 110.04 s; AAC audio).
- **Source code, read in full:** `tools/v15.py` (renderer, camera, captions), `v15_shots.py` (25 shots, state function, graphics), `model.py` (physics), `build_v15.sh`, `rig_renderer.py`, `cloth_warp.py`, `build_rig.py`, `instrument11.py`, `mix_v15.py`, `align_v14.py`, `prepare_voice.py`, `audio_qa.py`, `caption_qa.py`, `sync_map_v15.py`, `timeline_v15.py`, `frame_strips.py`, `review_sheet.py`, `sheet.py`, `strip.py` (about 2,577 lines in 19 files).
- **V15 documents:** `START_HERE.md`, `FINAL_PRODUCTION_QA.md`, `AUDIO_MIX_QA.md`, `CHARACTER_ANIMATION_QA.md`, `SCIENTIFIC_VISUAL_QA.md`, `PROJECT_CLEANUP_REPORT.md`, `research/V15_RESEARCH_NOTES.md`, `HUMAN_VOICE_TRANSCRIPT.md`.
- **Data and evidence:** `qa/*` (decode, freeze, caption, audio, sync, isolated rebuild, checksums, model check), `NARRATION_VISUAL_SYNC_MAP.csv`, `SOUND_DESIGN_CUE_SHEET.csv`, `SFX_LICENCE_MANIFEST.csv`, `WORD_LEVEL_TIMESTAMPS.json`, rig data (`rigs/side/rig.json`, `assets/v12rig/RIG.json`), the Codex art packages and their manifests, the Codex briefs in `codex_request/`.
- **History (V8–V14), documents and manifests only:** `history/v8` … `history/v14` (briefs, ledgers, QA, manifests, tools). The deleted V8–V12 folders were **not** restored.
- **Other project material:** `HumanCraft_MASTER_Animation_Director_V4.md` (read in full by a research pass), the xkcd *What If?* research folders (`what if book/`, `video data of what if/`), `SOUND EFFECT.zip` (listing only; nothing opened or used).
- **The Top-10 V3 script package** (`youtube-intelligence-os/productions/unreasonably-exact-script-rewrite-v3/` and the earlier extract), read-only.

### 2.3 What was measured or re-verified independently in this audit

| Item | Result |
|---|---|
| V15 integrity | `shasum -a 256 -c qa/checksums_v15.txt`: **8/8 OK** at the end of the audit; all 3,452 V15 content files are dated no later than 2026-11-25 18:06:35 (the V15 build); none was created or changed by this audit. macOS Finder created **11 `.DS_Store` metadata files** inside `v15/` at 21:31:23 during the audit session (OS folder-view metadata, not an action of this audit; left in place because V15 must not be touched) |
| Raw narration | `HAMZA_VOICEOVER_RAW.mp3` SHA-256 `edd24139…c82f`, matches the recorded checksum |
| Final MP4 | SHA-256 `2cb6ece9…0346`, matches |
| Final loudness and the **V15 voice-vs-background separation** | Re-measured from the shipped files (median 20.7 dB, p10 17.1 dB, §12.4); V14 values are *as recorded* in V15's documents because the V14 audio is not in this tree |
| Shipped SRT | 46 cues; max 17.4 chars/s, median 13.2; no cue above 20 chars/s; 0 overlaps; one-line cues, longest 51 chars (§13.1) |
| Caption geometry | from `qa/caption_qa.csv`: box 1,506–1,626 px, 294 px bottom margin |
| Warp rate | Evaluated at all 2,641 frames: instantaneous **0.26–1.40, median 0.68** (the script's *segment-average* limit is 0.34–1.6; §11.2) |
| Physics numbers for the nine scripts | Recomputed from G, c and standard constants (§9.5); all reproduced the research pass |
| Asset validator | **Written and run on four real V15 files** (§7.7, Appendix B) |
| Voice chain claims | Double compression (2:1 at −24 dB in `prepare_voice.py`, then 2:1 at −22 dB in `mix_v15.py`) read from source |

### 2.4 What was **not** done (read this before relying on the document)

1. **V15 was not rebuilt here.** Its `.venv` points at another user's Python 3.14 that is absent on this Mac, so the "isolated rebuild 8/8 byte-identical" result (which holds only downstream of narration editing and ASR (those were not re-run: the build uses the committed `qa/asr/clean_words.json`, and the clean voice WAV was a copied input)) is **proven on the build machine and unverified here**. A scratch environment (Python 3.12, numpy, Pillow, scipy) in the session scratchpad was used only for the validator and for re-measuring audio.
2. **No human watched or listened to V15 in this audit**, and an agent cannot. All audio statements are measurements. The V15 author also had no audio output (`HUMAN_VOICE_TRANSCRIPT.md`, `FINAL_PRODUCTION_QA.md` §3). **No owner acceptance of V15 is recorded.** See §17.
3. **V1–V7 are UNAVAILABLE** and V8–V12 renders no longer exist; their history is second-hand, from QA and audit documents written by Claude and Codex. The owner's briefs and screenshots are known only through those documents (except `history/v8/BRIEF.md`).
4. **Four parallel research passes** (history digest, Top-10 package, tools and licensing, technique research) produced second-hand material that is integrated here. Where it matters I recomputed or re-read the key facts; the rest is marked with the research confidence tags (**V**, **V-2nd**, **UNVERIFIED**). The web facts are a **2026-11-25 snapshot**; licences and versions change.
5. **No part of this audit uploaded, published or modified anything outside this playbook.** In particular, nothing under `v15/` was changed, no folder was restored, no script was rewritten, no packages were installed into the project, and no Graphify activity was run. The playbook file and the scratch validator are the only things created (the validator lives in the session scratchpad and is reproduced in Appendix B).
6. **Dates and effort.** All V8–V15 records are dated 2026-11-25; the one-version-per-hour cadence in §18.1 is an *inference from file times*.

### 2.5 Evidence rules used

Source code over summary documents wherever both exist; a number from a QA document is repeated here only if it was seen in a source file, a log, or re-measured, and is otherwise tagged "as recorded". Where a document disagreed with code, the code is followed and the discrepancy is noted (for example: CHARACTER_ANIMATION_QA.md says a 12-frame lift sequence; the code uses frames 00–09, i.e. **10**, with files 10 and 11 unused).

## 3. How V15 was created: the production lifecycle

Each stage lists what was done, the tools, the files, who did it, what went wrong, how it was corrected, and what to reuse or avoid. Evidence tags: **[V]** stated in a file and cited, **[M]** measured by this audit on 2026-11-25, **[I]** inferred. Paths are relative to `v15/` unless noted.

> **Who "Claude" and "Codex" are in these records.** Claude (Claude Code sessions) wrote the renderer, rigs, physics, audio, alignment, QA and reports. Codex (OpenAI's coding agent, using its built-in `image_gen` tool) produced illustrated artwork packages (`CODEX_V11_ART_REPAIR_PACKAGE/`, `CODEX_V12_ART_PACKAGE/`, `CODEX_V13_ART_PACKAGE/`, `assets/codex/`). The owner (Hamza; reports are written in Roman Urdu for the owner, `FINAL_REPORT_ROMAN_URDU.md`) briefs, reviews screenshots, records the narration and accepts the film. Owner feedback survives only second-hand in Claude's audit files; the owner's own briefs and screenshots are not in the tree.

### 3.1 Stage 1: Question and research

| Item | Detail |
|---|---|
| **Done** | Framed the single physical question (why can a skydiver slow down without opening the parachute?) and reduced it to ten ideas that the film must show (`SCIENTIFIC_VISUAL_QA.md` table). Built a fixed-posture model (`tools/model.py`) from the NASA Glenn drag equation and troposphere fit. Collected references: NASA Glenn drag equation and drag coefficient pages, USPA neutral-body-position pages and FAQ, saved free-body-diagram and ticker-tape references (`research/V15_RESEARCH_NOTES.md`, `research/screens/`). V8 also kept a research folder (`history/v8/research/`). |
| **Tools** | Web reading, saved screenshots, Python physics script. |
| **Claude / Codex** | Claude only. Codex supplied no science. |
| **What went wrong** | V8 drew drag at 91 against weight 60 (1.5×) where the model gives ≤ 1.035, a ≈ 17× overstatement of the net force, and an invented net-force arrow (`history/v9/V8_DEEP_AUDIT.md`) **[V]**. The model's inputs (80 kg, CdA 0.50 m²) are assumptions, flagged on the end card, not measurements of a person. V15's research notes admit that real skydiving footage was **not** watched; the figure's flutter relies on the USPA description and general knowledge. |
| **Corrected by** | V9 introduced `tools/model.py` and made every arrow, needle, density dot and camera read it. V15 added the cloth/airflow load from the same equation. |
| **Reuse** | One physical model per film that every visual reads; a research table that pairs each source with *what it changed in the film*; an assumptions line on screen. |
| **Avoid** | Drawing a force "because it looks right"; magnitudes not traceable to the model; citing footage that was not watched. |

### 3.2 Stage 2: Script and human narration

| Item | Detail |
|---|---|
| **Done** | The spoken text was designated the **final script** by the owner (`history/v8/FINAL_SCRIPT_OWNER_APPROVED.md`) after V8 found that the then-current 78.2 s recording did not match the 130-word, ≈ 58 s reference script (≈ 200 words, ≈ 20 s longer: a 78.2 s recording against a ≈ 58 s storyboard assumption; `history/v8/AUDIO_TRANSCRIPT_AND_ANALYSIS.md`) **[V]**. Hamza's own recording replaced that narration at V14: raw take 125.16 s, 10.14 s of setup talk removed, 202 words, 108.70 s clean (§11). |
| **Tools** | whisper.cpp (`ggml-small.en`), ffmpeg, numpy voice-activity detection. |
| **Claude / Codex** | Claude analysed and edited the audio. The owner recorded. Codex: none. |
| **What went wrong** | V9–V13 were tuned to a recording that was "unconfirmed" in every QA file; V14 then replaced it and the film grew by 41 % (78.2 → 110.04 s). The V9–V13 documents call the 78.2 s file "the owner's recording"; whether it was a real take could not be verified, and it was never confirmed as the final narration **[I]**. |
| **Corrected by** | Anchor-based time warp (no global stretch), 44 anchors, ambient motion on the real clock (§6.3, §11). |
| **Reuse** | Record before designing; word-level beat map (§11.2). |
| **Avoid** | Designing 13 versions on a provisional voice. |

### 3.3 Stage 3: Storyboard and visual beats

| Item | Detail |
|---|---|
| **Done** | Each version carried a `SHOT_MANIFEST.csv` and a "full-screen visual storyboard" document: V9 22 shots / 68 panels, V10 26 / 82, V11 26 / 90, V12 25 / 75, V13 25 / 75, V15 25 shots (`SHOTS` list in `tools/v15_shots.py:500-526`). V12 audited every piece of on-screen text (39 items: 13 REMOVE, 8 TEMPORARY, 6 REDUNDANT; `history/v12/TEXT_REDUCTION_AUDIT.csv`) and set the rule "mostly calm holds, one new visual event every ≈ 2 s". The V15 shot list states a *purpose* for each shot ("Cause and effect: you move down through still air → camera holds you → drag arrow grows"). I read the V15 shot list and the V12/V13 manifests; I did **not** open the per-version storyboard panel documents. |
| **Tools** | Markdown/CSV; contact sheets (`tools/review_sheet.py`, `tools/sheet.py`, `tools/frame_strips.py`). |
| **Claude / Codex** | Claude. |
| **What went wrong** | Text accumulated shot by shot (V9→V11 overlays); V10's frames at 0:41 and 1:08 showed everything at once; V8's two-line headline on every shot read as a slide deck. A "foreground cloud crosses the lens" tip was applied with no size limit and produced a full-frame white wipe in V12. |
| **Corrected by** | Text budget and audit (V12); one idea per shot; clouds kept at mid scale below the subjects (V13). |
| **Reuse** | A shot list with a purpose sentence per shot; a text-element audit with REMOVE / TEMPORARY / REDUNDANT / KEEP classes (§10.6). |
| **Avoid** | Adding overlays without removing older ones; importing a technique tip without a size limit. |

### 3.4 Stage 4: Asset creation and rigging

| Item | Detail |
|---|---|
| **Done** | V1–V8 characters were procedural (Pillow PNGs, then Bézier SVGs); **no AI-illustrated character asset existed until V10** (V9 still used procedural placeholders) (`history/v9/V8_DEEP_AUDIT.md`) **[V]**. Codex then delivered 73 image-generated layers (13 `image_gen` calls, `history/v10/assets/codex/README.md`), and three later repair/partition packages (V11 repair, V12, V13). The architecture then changed four times because of art limits: FK limb rig (V9–V10) → whole-pose drawings (V11) → constrained sprite-sequence rig (V12) → one continuous drawing deformed by a mesh (V15) (§4, §7). |
| **Tools** | Codex `image_gen` (+ local registration, masking, cropping); Pillow, numpy, cairocffi in Claude's repair scripts (`work/legacy_v11/fix_boots.py`, `work/legacy_v11/recolour.py`, `hands.py`, `folds.py`, `neck.py`, `finish.py`, `tools/build_rig.py`, `tools/cloth_warp.py`). |
| **Claude / Codex** | Codex: illustrated layers and poses, transparent PNGs, manifests, previews. Claude: repair in code, registration, rig construction, the wrist-instrument face (drawn in code: `tools/instrument11.py`), aircraft cleanup. |
| **What went wrong** | Generated joint caps and boot ovals (rejected by the owner on screenshots at V10); no hidden overlap art; `PIVOTS.json` all `null` (V12) and "seam test failed" (V13); gloves and faces inconsistent between views; a stray 2,754 px grey blob under the aircraft tail shipped in V14; the Codex V12 and V13 packages **failed their own motion tests** ("NOT READY TO ANIMATE… Motion FAIL"; "P0 acceptance criteria are not met") **[V]**. |
| **Corrected by** | Claude stopped relying on jointed parts: warp a continuous drawing instead (V15), keep head ≤ 1°, use sprite sequences for the one big arm motion, patch art in code, remove the blob (`assets/codex/aircraft_side_v15.png`, pixel diff equals the blob size). |
| **Reuse** | Whole continuous poses + deformation; executable acceptance tests in every art brief (§7.8, §8); registration to a shared canvas with alpha-bounds checks. |
| **Avoid** | Accepting `candidate` / `pivot: null` art as a baseline; asking a generator for jointed parts without testable overlap; naming packages after the wrong version. |

### 3.5 Stage 5: Animation and scientific models

| Item | Detail |
|---|---|
| **Done** | Procedural shot code (`tools/v15_shots.py`) reads `state(tm)` from the physics model; camera, terrain and cloud parallax from a pinhole camera; motion graphics (arrows, bars, lens, trail, graph) in code (§6, §9, §10). |
| **Tools** | Python + Cairo; Pillow MESH transform; numpy. |
| **Claude / Codex** | Claude. |
| **What went wrong** | V8: 9 of 22 shots froze the rig; clouds scrolled at one speed regardless of velocity; V9: drag crossed weight at 40.2 s, *before* the word "stronger"; V11: no limb motion at all; V14: "legs, boots, hands and clothing never moved". The honest net force is **0.9–3.6 % of weight (≈ 4 design units, about 13 px at 1080 wide, at true scale)**, so repeated designs tried to show it (10× inset, 10× lens, 30× card, 30× lens, push-in bars, ×8 lens) (§4.3). |
| **Corrected by** | Retiming reveals to words (V9 and V14 event anchors); model-driven cloth and airflow (V15); one disclosed ×8 lens (V15). |
| **Reuse** | State-function pattern, invariants asserted in `--check`, colour grammar, magnification disclosure. |
| **Avoid** | Redesigning the same diagram every version because the first design had no scale rule. |

### 3.6 Stage 6: Audio, captions and editing

| Item | Detail |
|---|---|
| **Done** | V8 had zero SFX; V9 added library SFX (10 cues); V13 had 18 library placements; V14 rebuilt the sound fully generated (35 cues); V15 reduced it to 24 generated cues + 2 beds in 5 stems with dialogue-first ducking (§12). Captions: whisper.cpp word timing (V13), raised and collision-checked (V15) (§13). Editing was code: shot list plus warp; HyperFrames was used only for a V8 timeline of baked-picture trims **[V]**. |
| **Tools** | numpy synthesis, ffmpeg filters (`loudnorm`, `alimiter`, `acompressor`, `deesser`, `highpass`, `equalizer`, `apulsator`, `tremolo`, `anoisesrc`), whisper.cpp. |
| **Claude / Codex** | Claude. |
| **What went wrong** | Library SFX had **unknown licences** from V9 through V13 (83 of the 110 manifest rows are library clips with an `UNKNOWN` licence; the other 27 are generated cues or the owner's recording); the loudness number (−16 LUFS) hid a bed that competed with speech in V14; captions sat at 1,752 px (box bottom), too low; one cue was 131 characters held 7.63 s (V12) **[V]**. |
| **Corrected by** | All-generated publication mix; separation metrics; ducking and carve; caption baseline raised 126 px and an automated collision check. |
| **Reuse** | Stems per function; separation measurement; cue sheet with rights column. |
| **Avoid** | Using integrated LUFS as evidence the voice is clear; library clips without a licence record; mixing last. |

### 3.7 Stage 7: Rendering and quality review

| Item | Detail |
|---|---|
| **Done** | Parallel render (9 workers), picture self-check (`--check`), frame-by-frame review strips (35 six-frame strips at every cut and key animation, `qa/frames_critical/`), caption collision check (46 cues × 3 samples = 138), sync map (34 events), decode test, muted contact sheets, phone-size review page, isolated rebuild with hash equality (§17). |
| **Tools** | ffmpeg/ffprobe, Python scripts in `tools/`, local `http.server` review page `qa/review/index.html`, the built-in browser. |
| **What went wrong** | V11's first render crashed (divide by zero) and freezes were fixed at 50.75 s and 67.96 s (V11) and 21.9 s (V12); V9's 21.9–22.7 s and V10's 50.63–52.04 s hits were judged deliberate holds; arrows and bars slid under captions (V14 ≈ 65 s; V15 regression at 68–74 s caught by the new collision check); glyphs missing; V8–V10 had only short or sampled browser playback, V11–V14 had none, and no version was ever listened to. |
| **Corrected by** | Automated checks per defect class (§17); V15 was the first version with a documented full-length playback at normal speed (V9 and V10 were sampled), still with the caveat "sampled, not watched continuously". **Nobody has listened to V15.** |
| **Reuse** | Every defect class gets a script; every script's result is stored in `qa/`. |
| **Avoid** | Claiming review that was not performed. |

### 3.8 Stage 8: Final production master

| Item | Detail |
|---|---|
| **Done** | Clean MP4, captioned MP4, SRT, review MP4 with the library-SFX comparison mix, stems, cue sheet, sync map, timeline JSON, checksums, one-command rebuild, isolated rebuild (8 of 8 files byte-identical, downstream of narration editing and ASR only), cleanup report, owner report. |
| **Files** | `SKYDIVER_SLOWDOWN_FINAL_V15.mp4` (SHA-256 `2cb6ece9…0346`, re-verified by this audit), `…_CAPTIONS.mp4`, `.srt`, `audio/stems/`, `timeline/V15_TIMELINE.json`, `qa/checksums_v15.txt`, `START_HERE.md`. |
| **Open at the time of this audit** | No recorded owner acceptance or listening; V13/V14 folders (≈ 2.1 GB) untouched "pending owner acceptance"; the V15 venv is not runnable on this Mac (§6.10). Nothing was uploaded or published. |

---

## 4. Version-by-version production history (V8 → V15)

### 4.1 What is verified and what is not

| Status | Items |
|---|---|
| **Unavailable** | **V1–V7**: only second-hand audit statements survive (V1/V3–V6 Pillow PNG characters; V7/V8 Bézier SVGs; V7 had 75 SVGs, 7 rigs, 12 motion clips). **V8–V12 renders and per-version folders**: permanently deleted at V13 with owner permission (4.81 GiB → ≈ 1.0 GiB); only docs, manifests, JSON and some tools survive in `history/`. The owner's briefs and screenshots. The original Codex assignment ("never found", `history/v8/research/TOOL_AUDIT.md`). |
| **Verified** | Everything cited to a file below. |
| **Inferred** | **Calendar time**: every dated statement from V8 to V15 is 2026-11-25; render mtimes run 11:19 (V9), 12:41 (V10), 13:50 (V11), 14:49 (V12), and V15 files 15:44–18:06 (final MP4 17:57). So the eight versions were probably built in a **single working day, roughly one per hour** **[I]**. "15 versions" is therefore fast iteration against owner review, not weeks of calendar effort. |

### 4.2 Timeline

| Ver | What it was | Key change | Defect that forced the next version | Evidence |
|---|---|---|---|---|
| **V1–V7** | Earlier builds | Pillow PNG then Bézier SVG characters; 75 SVGs, 7 rigs, 12 clips at V7 | No AI-illustrated asset existed; requirement unmet | `history/v9/V8_DEEP_AUDIT.md` (second-hand) |
| **V8** | Continuation of V7, native Python/Cairo/SVG renderer kept to avoid migration risk | 78.208 s, 1,877 frames, 22 shots; aircraft opening, pale-blue sky, staged forces, velocity lane; HyperFrames only for a timeline of 22 baked trims | 9/22 shots froze the rig; clouds one speed; drag 1.5× weight vs model ≤ 1.035; a two-line headline on every shot; zero SFX; dial at 4 sizes | `history/v8/START_HERE.md`, `history/v9/V8_DEEP_AUDIT.md` |
| **V9** | Physics-driven review cut ("not publishable") | `tools/model.py`; pinhole camera and perspective terrain; five force grammars; 10 library SFX + generated wind; 68 panels; first Codex request (9 asset families) | Placeholder procedural art ("clean but geometric", the owner's stated objection); SFX unlicensed; narration unconfirmed | `history/v9/START_HERE.md`, `CODEX_MISSING_ASSET_REQUEST_V9.md` |
| **V10** | First film with Codex art (73 layers; 65 integrated) | Wrist device; painted landscapes; force states with a 10× lens; 26 shots / 82 panels | **Nine owner screenshots**: floating pack, round joint discs, "different person" face, airflow like rain, limbs "bolted on", dial fills the screen like a clock, everything on screen at once | `history/v10/START_HERE.md`, `history/v11/V10_SCREENSHOT_DEFECT_AUDIT.md` |
| **V11** | **Architecture pivot**: abandon limb rigs (45 layers retired), animate whole-pose drawings | Boots and colours repaired in code; wrist device always on a wrist with a code-drawn SLOW…FAST face; irregular jittered field mesh; streamline airflow | No arm/hand motion; gloves inconsistent; four renders needed (div-by-zero crash, freezes at 50.75 and 67.96 s, black strip) | `history/v11/CHARACTER_ANATOMY_QA.md` |
| **V12** | **Motion-design re-edit** | 39-item text audit; pinhole camera over metre-scale terrain; constrained side rig (forearm lift 0→22° + dissolve, glance swap, code blink); in-scene ×30 lens; equal-time trail | Codex V12 package "NOT READY TO ANIMATE"; opening: figure 15–20 px tall at lower right, 55 % ground, whole-frame cloud wipe (owner at 0:00/0:01/0:03) | `history/v12/START_HERE.md`, `history/v13/OPENING_V10_V11_V12_V13_COMPARISON.md` |
| **V13** | Opening restored and layered; caption/sync rebuild | 4-layer parallax opening; "you move through still air → air streams up" causal sequence; two equal density boxes; two bars + ×2.25 push; whisper.cpp captions (48 cues, 0 overlaps vs V12's 29 cues with one 131-char cue held 7.63 s); self-contained isolated rebuild (6/6 hashes) and cleanup | Codex V13 elbow/neck repairs rejected (P0 not met); only the bare-hands back pose used | `history/v13/START_HERE.md`, `CODEX_V13_INTEGRATION_MANIFEST.csv` |
| **V14** | **Narration replaced by Hamza's recording** | 78.2 → 110.04 s, 2,641 frames; per-phrase monotone warp; sound rebuilt fully generated (35 cues, rights-clear); 33 sync rows | Owner-reported audio defect: bed competed with the voice | `history/v14/START_HERE.md`, `FINAL_SYNC_QA.md` |
| **V15** | Final production | Mix rebuilt (bed −15 dB × envelope, 10 dB lower than V14; ducking −12/−9 dB, speech-band carve, 5 reveal sounds); captions raised and collision-checked; **mesh-deformed continuous character**; ×8 net-force lens + arrow; weight → orange; farmsteads and tree crowns; foreground motes; one-command and isolated rebuild | None recorded; **no human listening or owner acceptance recorded** | `FINAL_PRODUCTION_QA.md`, `START_HERE.md` |

### 4.3 Defect lifecycle (the lessons behind the table in the brief)

| Problem | First seen | Fixed in | Root cause | Technique that finally worked | Final lesson |
|---|---|---|---|---|---|
| Mechanical-looking joints | V8 audit; discs on owner screenshots at V10 | V11 (discs gone), V15 (motion without cutting) | Generated limb parts carried baked round overlap ends; the requested 8–12 px hidden overlap was never tested or certified | Whole poses (V11) → continuous drawing + mesh deformation (V15) | Natural deformation and continuous anatomy |
| Static character | V8 audit (joints moved 1–3°) | V12 (lift, glance, blink), V15 (knees, hands, cloth) | Rigid sprites; V11 regressed to no limb motion | Sprite-sequence lift, then model-driven mesh ripple, two incommensurate frequencies per joint | Independent movement and secondary animation |
| Detached speedometer | V8 audit (4 sizes, floating) | V11–V12 | Instrument designed as a stand-alone object; V10's dial read as a clock | Wrist art with blank face; scale, needle in code; dial only on a wrist | Contextual, wrist-mounted instrument |
| Excess screen text | V8 audit | V9 → V12 audit → V15 | Text used as the explanation; no text budget | 39-item audit; captions as an optional overlay; labels only where a mark needs a name | Visual-first scientific storytelling |
| Confusing force diagrams | V8 (1.5× drag, invented net) | six designs: V9 → V15 | True net force is 0.9–3.6 % of weight; no standing scale rule | One scale from the centre of mass; one disclosed ×8 lens | Progressive, consistently scaled visualization |
| Oversized foreground clouds | V12 (owner 0:03) | V13 | A "cloud crosses the lens" tip applied without a size limit | Mid-scale clouds below subjects; no wipe | Controlled camera composition |
| Unnatural terrain | V9 (checkerboard) | V11 → V13 → V15 | Regular parcels; painted layers clashed with flat characters | Jittered irregular mesh, merged fields, palette sampled from the painted study; farmsteads, crowns | Detailed illustrated environments |
| Poor narration sync | V8 (phrase times ± 0.3 s estimates) | V13 words, V14 voice, V15 34/34 | Estimated boundaries; overlapping cues | whisper.cpp DTW + voice-activity snap + per-phrase warp + sync map | Word-level and phrase-level alignment |
| Loud background effects | V12 ("wind dips with graphics"), V14 (owner) | V13, V15 | V14 bed at −5 dB with −7/−4.5 dB ducking over the consonant band; −16 LUFS hid it | −15 dB × envelope bed (10 dB lower than V14), −12/−9 dB duck, 1–4.5 kHz carve | Dialogue-first mixing |
| Low captions | V14 (box bottom 1,752 px) | V15 (1,626 px) | No numeric safe zone | Baseline 578 → 536 units; automated collision check | Mobile-safe placement (see the caveat in §13.1, limit 3) |
| Repeated rendering defects | V9 onward | every version | Fixes re-broke earlier fixes; only stills caught them | `--check`, strips, caption QA, sync map, decode test | Systematic production QA |

Other recurring defects the history shows: costume and identity mismatches across views (smiling three-quarter face, grey vs bare gloves, V10–V13); "candidate / not approved" art status repeated V10–V13 (and in V14's report) and then absent from V15's root documents **[I: a documentation lapse]**; unlicensed library SFX V9–V13; narration "unconfirmed" V9–V13; label collisions V9, V12, V13, V15; the same missing `→` glyph in V9 and V13.

## 5. Professional animation research and tool review

**Reading rule for this section.** Three things are kept apart everywhere below:

- **USED IN V15**: the tool or idea is in the V15 build, with a file that proves it.
- **REVIEWED**: someone read about it, ran it or looked for it, and decided; it is not in the V15 build.
- **RECOMMENDED FUTURE**: proposed here for later films. Nothing in V15 depends on it.

Web facts were fetched on **2026-11-25** by a research pass; where a primary page was blocked the entry says so. Confidence tags: **V** = verified from a primary page, **V-2nd** = a secondary source quoting a primary one, **UNVERIFIED** = could not confirm, or a practitioner default of this playbook.

### 5.1 What V15 actually used, in one table

| Tool / idea | Status | Proof in the tree |
|---|---|---|
| Python 3 + `cairocffi` (immediate-mode 2D), `numpy`, `Pillow` | **USED IN V15** (the renderer) | `tools/v15.py`, `cloth_warp.py`; §6 |
| `ffmpeg` (libx264 encode, `loudnorm`, `alimiter`, `acompressor`, `deesser`, `highpass`, overlay, null-decode) | **USED IN V15** | `tools/build_v15.sh`, `prepare_voice.py`, `mix_v15.py` |
| `whisper.cpp` (`whisper-cli`, `ggml-small.en`, `-ml 1 -sow -ojf -dtw small.en`) | **USED IN V15** | `tools/build_v15.sh` (`--from-voice` branch), `tools/whisper_models/` |
| HyperFrames **technique** (voice-over carve of the bed) | **USED IN V15 as an idea only** | `tools/mix_v15.py` `carve()`; `research/V15_RESEARCH_NOTES.md` ("Used the technique, not the renderer") |
| HyperFrames **renderer / HTML timeline** | Used once, in **V8**, only to trim 22 baked pictures into an editorial timeline; reviewed and rejected for V12, V13, V15 | `history/v8/editorial/meta.json`; `history/v12/TOOL_AND_LIBRARY_USAGE.md` |
| HumanCraft written guidance | **USED IN V15 as principles** (mesh deformation instead of cut-out joints, secondary motion, layers at different rates) | `research/V15_RESEARCH_NOTES.md` |
| Anidoodle (Apache-2.0, 32 styles) | **REVIEWED, not used** (its look would replace the approved Codex character) | `research/V15_RESEARCH_NOTES.md` |
| Claude Animated Shorts, EffectCraft, Three.js Skills, Hand-Drawn Explainer, "FFmpeg Skill" | **REVIEWED only by absence**: V15's author searched `~` to depth 4 and the skills folder and found none of them | `research/V15_RESEARCH_NOTES.md` |
| Remotion | **Not evaluated in the V15 files.** Reviewed for this playbook (§5.2) | — |
| NASA Glenn drag pages, USPA body-position pages | **USED IN V15** as science sources | `research/V15_RESEARCH_NOTES.md` |

**Local installation facts (this Mac, 2026-11-25, read-only check):** `ffmpeg` 9.0.1 at `/opt/homebrew/bin/ffmpeg` (a GPL build: `--enable-gpl --enable-version3 --enable-libx264`), all of `sidechaincompress`, `loudnorm`, `deesser`, `acompressor`, `zoompan`, `equalizer`, `alimiter`, `amix`, `afade` present, plus VideoToolbox encoders; `whisper-cli` from Homebrew `whisper-cpp` 1.9.5_2 (upstream is 1.9.6); `node` 24.14.0; `python3.12` and `uv`-managed 3.10/3.11/3.13; **no Python 3.14** and no `ggml-*.bin` model was found in the places searched first (V15 ships its own copy under `v15/tools/whisper_models/`; a later check found `ggml-large-v3-turbo-q5_0.bin` under `~/Downloads/YIOS-Channel-Forensics/_tools/whisper-models/`, which V15 does not use); the `hyperframes` CLI is **not installed** (the `hyperframes`, `hyperframes-cli`, `hyperframes-registry` and `media-use` *skills* are). None of motion-skills, anidoodle, claude-animated-shorts or threejs-skills is installed here. This is why V15's `.venv` cannot be run on this machine (§2, §6.10).

### 5.2 The nine tools named in the brief

Each entry: what it is, licence, status relative to V15, verdict for the next films.

**1. Remotion.** React framework that renders each frame in headless Chrome and encodes it. Version 4.0.547 (2026-11-24). **Licence: custom, source-available, not open source.** Free tier: an individual, a for-profit company with up to 3 employees, a non-profit, or evaluation; commercial video creation is allowed. Company licences start at $25/seat/month ("Creators"), $0.01/render with a $100/month minimum ("Automators"), Enterprise from $500/month. **The 5.0 licence change** (PR #3750, Terms page; **pending: it takes effect with the 5.0 release, and npm latest is 4.0.547, so it is not in force yet**) counts *all personnel regardless of whether they use the software*, with a Company Licence needed at a combined headcount of 4 or more, contractors included. The repo says "3 employees", the pricing page says "3 people"; use the stricter reading. Output videos are yours. Status: not used and not evaluated in V15. Verdict: **SKIP for the core pipeline.** It would replace a deterministic Python renderer with a Node + Chrome stack and add a headcount watch item. **PILOT only** if a future film wants React-authored scenes. Official skills exist (`npx remotion skills add`). Limits not confirmed: Node/Apple-Silicon requirements (docs page 404), audio-mix and concurrency docs. **V**

**2. "Motion Skills".** No single product has this name. Best match: `iart-ai/motion-skills`, 56 skills in 19 packs, **MIT**, created 2026-06-22, last push 2026-11-18, about 2.2k stars; video packs render through **Remotion or Manim**, not HyperFrames. It is promoted by a paid service (iart.ai) and carries unverified cost claims; its optional MCP needs a paid plan. Other things called motion skills: a `motion-graphics` skill inside the HyperFrames repo, community skills for the *Motion* web-animation library (licences differ: one MIT, one AGPL-3.0, per listings), Remotion's own skills pack. Status: not used. Verdict: **PILOT (read only)**: skim the Manim and explainer packs for prompt structure; they are prompt files, not a renderer; read each `SKILL.md` before installing; do not install the paid MCP. **V** (repo), **UNVERIFIED** (the cost claims)

**3. HyperFrames.** HeyGen's open-source framework that renders HTML/CSS/JS to MP4 by seeking a paused GSAP (or CSS, Lottie, Three.js, Anime.js, WAAPI) timeline frame by frame in headless Chrome and encoding with FFmpeg. Version 0.9.94 (2026-11-25), pre-1.0, daily releases, about 90k stars. **Licence: Apache-2.0**, "no per-render fees or commercial-use thresholds". Needs Node 22+, FFmpeg, Chrome via Puppeteer. Its skill contract forbids `Date.now()`, unseeded `Math.random()`, network fetches and `repeat: -1`, so every frame is a function of timeline time, which matches V15's determinism rule (crc32-seeded RNG, §6.2). Default 1920×1080 at 30 fps; vertical is possible. Captions are in its registry; audio is placed with `<audio>` tags. Status: see §5.1 (V8 editorial only; carve idea in V15). Verdict: **PILOT**: one 30-second Short in an *isolated* project, compared against the Cairo renderer on frame determinism and render time. Cost of adopting it: scenes would move from Python to HTML + GSAP. Warnings: the browser editor is "evolving"; installing its skills into a checkout can overwrite uncommitted edits (the YIOS preservation policy applies: install only into a throwaway project). **V**

**4. EffectCraft.** Open-source Rust After-Effects-style compositor. Latest release v0.25.1 (2026-11-23); **MIT or Apache-2.0**; the README mentions "ArtCraft" trademarks (unreconciled). macOS is "the most tested platform". Has a headless CLI render, an MCP server and versioned JSON projects. The README calls it alpha, "about 45% of the way" to professional use, "not yet recommended for production client work". Determinism not addressed. Status: not used (absent from the V15 author's machine). Verdict: **SKIP; revisit after 1.0.** A GUI compositor does not fit a scripted, repeatable channel. **V**; the version number conflicts with a third-party review (v0.9.2) and is unexplained.

**5. Anidoodle.** A Claude Code / Codex / Grok skill and code-drawn art engine (`alexgreensh/anidoodle`), 32 styles, deterministic per-frame functions, 9:16 supported, exports MP4/WebM/GIF/APNG/PNG/HTML, composes music and SFX in code. **Apache-2.0** with a NOTICE file; an optional acoustic sample library's licence is **UNVERIFIED**. Not the unrelated iOS app of the same name. Created 2026-09-22, about 2k stars, little track record. Status: **reviewed and not used in V15** because its style would replace the approved character and painted environment. Verdict: **PILOT as a style or music reference only.** It is style-led, not physics-led. Check licence provenance before using any bundled sample. **V** (repo, licence), **UNVERIFIED** (version, samples)

**6. Claude Animated Shorts.** Free **MIT** skill (`mromidev/claude-animated-shorts`, created 2026-11-01) for 55–70 s vertical stories with ink-outlined 2D characters in a painted 3D town, using three.js and Remotion. Rendering copies a ~1.3 GB `public/` folder per bundle. Its "viral/proven" claims have no linked output; reference frames are "style study only". Status: not used. Verdict: **SKIP**: wrong genre for a science channel, and Remotion-locked (so the headcount rule above applies). **V**

**7. Three.js skills.** Several unrelated packs; the verified one is `cloudai-x/threejs-skills` (13 skills, **MIT**, targets three.js r186 while npm `three` is 0.187.0, no deterministic-capture material). Status: not used. Verdict: **PILOT only if a film needs 3D** (none of the nine remaining scripts require it; §15). For deterministic 3D frames the real routes are HyperFrames' Three.js adapter or Remotion's `@remotion/three`. **V**

**8. Whisper and word-timing tools.**

| Tool | Licence | Status / verdict |
|---|---|---|
| **whisper.cpp** (`ggml-org/whisper.cpp`, v1.9.6) | MIT; models declared MIT on Hugging Face (**V-2nd**: the README itself says nothing about model licences) | **USED IN V15.** Metal on Apple Silicon. `-ml 1 -sow` gives one word per segment (README marks `-ml` experimental); `-ojf` adds per-token data; `-dtw <model>` needs the model name to pick alignment heads. Keep. |
| OpenAI Whisper (Python) | MIT code and weights | Reviewed. Not needed while whisper.cpp works. |
| **WhisperX** | BSD-2-Clause | **Not installable on Python 3.14** (requires `>=3.10,<3.14`); CPU-only on Mac; pyannote diarization needs a gated token. SKIP. |
| **Montreal Forced Aligner** | MIT toolkit; pretrained-model licence **UNVERIFIED** (believed CC BY 4.0) | RECOMMENDED FUTURE only if the script text must be force-aligned; needs a transcript and a pronunciation dictionary; conda-distributed. |
| **aeneas** | **AGPL-3.0**, last release 2017 | AVOID for a closed pipeline. |
| **ctc-forced-aligner** | Code BSD-2; default model **CC-BY-NC-4.0** | AVOID the default model on a monetized channel. |

Note the V15 lesson (§11.1): two ASR decodes agreeing is not a listening check; and ASR is not alignment to a trusted script.

**9. FFmpeg.** **USED IN V15.** Licence LGPL-2.1+ by default; the Homebrew build enables GPL parts, which is fine for personal rendering but means **do not redistribute that binary** without GPL compliance. Rendered videos are not covered. The legal page notes patent uncertainty for H.264/HEVC and does not discuss running ffmpeg as a separate program. Filter options verified against the official docs and the local build: `sidechaincompress` (threshold 0.001–1, ratio 1–20, attack 0.01–2000 ms, release 0.01–9000 ms), `loudnorm` (I −70…−5, LRA 1–50, TP −9…0, use two passes for accuracy), `deesser` (`i`, `m`, `f`, `s`), `zoompan` (set `s=1080x1920` and `fps` explicitly; default is 720p at 25). **V**

### 5.3 Other tools, one line each (all RECOMMENDED FUTURE or REVIEWED; none in V15)

| Tool | Licence / cost | Note |
|---|---|---|
| Rive | Runtimes MIT; editor is paid SaaS (price **UNVERIFIED**) | Skeletal + mesh + IK runtime. |
| Lottie / dotLottie | `lottie-web` MIT, `dotlottie-web` MIT | Vector playback; for web, not for this renderer. |
| Spine | Proprietary; per-person editor licence, tiers tied to <$500k revenue; runtime licence separate | Source of the rigging conventions in §5.5. Costly lock-in. |
| DragonBones | Runtimes MIT; editor maintenance **UNVERIFIED** | Mesh + FFD + IK. |
| Blender Grease Pencil | GPL; output is yours | 2D-in-3D; Grease Pencil specifics **UNVERIFIED**. |
| Manim (ManimCE 0.22.1) | MIT; needs Python ≥3.11 | Best fit for equation- and graph-led scenes; Python, so it can join the pipeline. |
| Motion Canvas | MIT; low activity | |
| Theatre.js | `core` Apache-2.0, **`studio` AGPL-3.0**; development moved private | Avoid studio. |
| Cavalry / Moho | Free-for-individuals (terms **UNVERIFIED**) / ~$400 one-time (**UNVERIFIED**) | GUI tools; do not fit a scripted pipeline. |

### 5.4 Local reference material

**HumanCraft_MASTER_Animation_Director_V4.md** (1,519 lines, at the project root; also a PDF). It is *a method document*, not code. Its own precedence rule: the real brief and supplied media first, then V4, then V3, then templates; all numbers inside templates are illustrative. The 22 most operationally useful rules are listed below (**section numbers in this list are HumanCraft's own, not this playbook's**):

1. **Eight-link chain** (§1): claim → viewer interpretation → shot/staging → approved assets → editable motion → audio time → rendered proof → critique. A missing link is labelled UNVERIFIED / PROVISIONAL / BLOCKED.
2. **VISION_CARD** (§2A): audience effect, creative thesis, visual identity, scope, reference grammar, 3–8 anti-generic rules, 2–5 hero moments, planned restraint moments, approval evidence.
3. **Three candidates, one decision** (§2B): simplest clear, expressive character/space, graphic/metaphor/data; only for important shots.
4. **Motion contract** (§2C): subject, cause, meaning, initial and final pose, path, velocity/spacing, start/end time, contact, pivot/hierarchy, secondary overlap, camera relationship, hold, proof criterion. No communicative or physical reason means no movement.
5. **Two separate reviews** (§2D): editorial (comprehension, focus, arc, pacing) and animation (silhouette, volume, contacts, arcs, overlap, on-model).
6. **Reject/repair loop** (§2E, §12): after the first moving proof, list the worst three defects, each with timecode, severity, root cause, exact source edit, expected evidence; re-render the same interval and compare.
7. **Blocking defects and house gate**: misleading science visual, unreadable essential label, broken sync, severe continuity break, bad contact in a hero action, failed decode. House gate 0–5 per dimension, critical ≥4, supporting ≥3; self-described as house policy, not an external benchmark.
8. **12-principles table** (§3) with the common AI/preset failure and a verification method for each.
9. **Frame rate is not exposure** (§3): do not claim "hand-drawn" if only whole-PNG transforms were used.
10. **Character spec** (§4.2): part list with pivots (pelvis, torso, neck, head, shoulders, upper arm, forearm, hand, thigh, shin, foot, eyes/brows, props), drawing order, phase lists (walk: contact→down→passing→up→contact; jump: anticipation→push→flight→landing→compression→settle).
11. **Foot planting** (§4.3): a planted foot is constant in world space during stance; shadows change with elevation.
12. **Robotic-animation inspection list** (§4.4) and **anti-generic symptom→cause→fix table** (§12): every shot slow-zooms, everything pops in, one easing everywhere, PNGs that bob.
13. **Real-construction test** (§4.5, §6): 2.5D needs differential layer motion plus valid occlusion; otherwise call it a Ken Burns move.
14. **Meaning-first shot decision table** (§6): suspense, mechanism, personality, scale, statistic, impact, sequence each have a first method and a reject condition ("icons only label rather than explain").
15. **Audio-first clock** (§7, V3 §4): narration master immutable and hashed; word timing from an aligner (silence detection is not alignment); one global frame clock.
16. **Caption rules** (V3 §4): SRT/VTT sidecar separate from kinetic type; captions follow what is spoken; highlight only meaningful words; respect reading time; keep faces and diagrams clear.
17. **10-step shot decision order** (V3 §5) and **visual-density rhythm**: alternate high, medium, low energy; there is no "new shot every 3 s" formula.
18. **Transition grammar** (V3 §8): hard cut, match cut, movement handoff, foreground wipe, L/J cut, freeze; do not default to flash, glitch, shake, zoom or spin.
19. **Pass pipeline** (V3 §11): 0 reality inspection, 1 story spine, 2 style contract, 3 audio/fact verification, 4 shot list, 5 art proof, 6 **mandatory 5–12 s moving proof**, 7 full rough, 8 polish, 9 render, 10 independent review. (§14 of this playbook is built on this shape.)
20. **Truthful science visuals** (§10, §13C): annotate stylised scale, one cause per step, arrows mathematically meaningful, comparisons built stepwise, hold for comprehension, never bounce every digit.
21. **QA vocabulary** (§15): PASS / FAIL / NOT VERIFIED / N/A. `ffprobe` plus `ffmpeg -v error -i f -f null -` proves decode only.
22. **Trade-off order when short of time** (§9): factual/legal/narration integrity → story clarity and acting → pose/contact/timing → legible text/composition → continuity → embellishment.

Its schemas are the best existing templates: project brief (YAML, III.A; defaults to 1920×1080 at 30 fps, so change to 1080×1920 / 24 for this channel), **shot contract** (III.B), **cue sheet** (III.C), **QA report** (III.E, 13 gates, with a revision-log table), and a 110-technique library in six groups (camera/depth, mask/track/comp, keyframe/editorial, character, type/graphics, light/colour/audio). **Gaps it does not fill** (these are the places §7–§13 of this playbook add numbers): mesh and weight conventions, spring and wind numbers, vertical safe areas, caption reading-speed numbers, loudness and ducking targets, vertical delivery specs.

**xkcd *What If?* research folders** (outside this project; paths under `/Users/ghilmankhan/workprojects/`). Used as analysis input only: the book PDF is copyrighted and its figures are **not** assets (redraw originals).

- `what if book/WhatIf_Complete_Extraction/`: OCR database of the 2014 book, 321/321 pages, 91 questions (57 main, 27 Weird, 7 Short-Answer); `figure_index.csv` lists 330 extracted figures with page, size, format, SHA-256. The README warns the OCR is machine output and unproofed. Coverage audit: answer summaries 59/91, science explanations 52/91, 32 early records pending. A channel-vs-book comparison (snapshot 2026-11-04) counts **91 channel videos (45 long, 46 Shorts)**, 39 overlapping the book, 52 not.
- `video data of what if/`: forensic analysis of **14** channel videos (8 portrait, 6 landscape, 24 fps except one at 30). Its own audit says **channel provenance is unresolved** (the attribution is inferred; no thumbnails, descriptions or analytics) and that no caption style, style bible or character bible exists. Corpus counts: 7,864 words, 604 sentences, 200 shots, 581 states, 438 motions, 448 assets.

| Measured finding (corpus) | Value |
|---|---|
| Locked or static camera | 89.8% of states; change comes from hard cuts and illustration replacement |
| Transitions | all 186 internal boundaries are exact 0.0 s hard cuts; zero fades or dissolves |
| Shot length | mean 10.54 s, median 7.77 s, range 1.54–78.9 s (the 78.9 s outlier is one continuous map pan) |
| **State** length (n=581, computed in the research pass) | mean 3.61 s, **median 3.0 s**, p10 0.75, p25 1.75, p75 4.5, p90 7.0 |
| Motion type | state replacement 53% (230/438) at about 1.6 s; sequential 131 at 3.5 s; persistent loops rare (7) |
| Sync to speech | 99.5% of motion starts and 98.8% of ends land during or adjacent to a word; only 66.8% of state changes do (193 of 581 have no speech); median offset 33–56 ms after word start |
| Narration pace | mean sentence 3.04 s, 13.0 words; about 256 wpm by arithmetic, well above subtitle norms |
| Silence | 15 non-speech regions across 14 videos (8 silences averaging 1.41 s, 7 pauses averaging 0.73 s) |
| Visual style | mostly diagrammatic, no recurring illustrated characters |

Two caveats that must travel with these numbers: (1) the audit's claim that red is reserved for rejection marks is **UNVERIFIED** (the current `VISUAL_DNA.md` says palette and typography were never measured); (2) caption style was never captured. **Consequence for this channel (a design decision of ours, not a reproduction of the corpus):** Unreasonably Exact uses a rigged character, which the corpus does not; so the corpus rules on cuts, camera and state pacing apply, and the character rules come from §7.

**xkcd's own visual traits (analysis only, no copying):** stick-figure drawings with a casual look; rough estimates and simplifying assumptions drive the answers; footnotes carry extra information or jokes; wit mixed with dramatic-disaster seriousness; landscapes, graphs and charts. "Deadpan" is **not** supported by the page checked; treat it as an observation to test against the owner's own viewing. **V-2nd**

### 5.5 The professional-technique findings, applied to this channel

**Character and the 12 principles** (Thomas & Johnston, *The Illusion of Life*, 1981; **V-2nd**, Wikipedia). Loose parts keep moving after the body stops and settle with damped oscillation; the torso is the core; a "moving hold" (breathing) keeps a still character alive; limbs rotate about joints and so travel on arcs; realistic squash and stretch conserves volume. For cut-out rigs: FK gives arcs for free; use IK only for contacts such as feet and a held prop (Spine: FK/IK mixing is "often needed only briefly"; **V**). Delay child parts 2–4 frames behind the parent plus a damped spring rather than a sine (the 2–4 frame figure is a **practitioner default, UNVERIFIED**). Do not scale child parts independently (it breaks joints). *How V15 applied it:* the continuous mesh warp makes follow-through emerge from the cloth weight map (§6.7); knees ±2.6° and wrists ±4° keep the posture and therefore the CdA unchanged.

**Skeletal and mesh conventions** (Spine docs, **V**; Rive, Toon Boom, Moho, DragonBones, **V-2nd**).

- Keep mesh vertex counts minimal; each bone influence adds a vertex transform. "Most or all deformation should be done using weights."
- Keep the hull tight (pixels outside it are not drawn; meshes cannot have holes). Auto-weights then **Prune** with a bone cap and threshold.
- IK is one- or two-bone only; Mix, Bend, Softness (slows the limb as it straightens, avoiding a snap), Stretch/Compress. Useful to keep feet from penetrating the floor.
- Physics constraints (Inertia, Strength, Damping, Mass, Wind, Gravity, Mix) update at **30–60 FPS**; warm up before looping exports.
- Toon Boom: a master peg at the root and a parent peg per drawing; set pivots on pegs, not drawings. Moho: "flexible" (every bone influences every point) versus "region" binding; frame 0 is the rest pose.
- **ARAP** (Igarashi, Moscovich & Hughes, *As-Rigid-As-Possible Shape Manipulation*, ACM TOG 24(3):1134–1141, SIGGRAPH 2005; **V**): drag handle vertices on a triangle mesh and the rest move so each triangle distorts as little as possible; closed-form two-step solve factorised once per drag. Triangle fold-over at extreme handle moves is a known limitation from background knowledge, **UNVERIFIED in-session**. **FFD** (Sederberg & Parry, SIGGRAPH '86, 20(4):151–160; **V-2nd**) deforms through a lattice. V15's `cloth_warp.py` is a displacement-field warp on a 32 px grid, i.e. in the FFD family, not ARAP; no solver is involved (§6.7).
- Rule for our rigs: rigid FK parts by default; meshes only for hair, cloth, faces, soft shapes, with ≤2 bones per vertex; add joint-cap overlap art at elbows and knees so rigid segments hide their seams (the V10 owner objection was exactly the *visible* caps; §3.4, §7.5); ARAP-style pinning for cartoon blobs, weights and IK for limbs.

**Multiplane and parallax camera.** Disney's multiplane camera (Garity, completed early 1937, tested on *The Old Mill*, used on *Snow White*; up to 7 glass layers; "the further from the camera, the slower the speed"; **V-2nd**). **Derived rule (geometry, not a source):** for a pinhole camera translated sideways by *t*, a layer at depth *z* shifts by about *t/z* and scales by about *1/z* on a push-in; so put layers at real *z* and drive one virtual camera, instead of hand-keying per-layer speeds. This is what V15's `Cam.proj` does (§6.5). Starting multipliers (practitioner, **UNVERIFIED**): sky 0.05–0.15, far 0.3, mid 0.6, subject 1.0, near foreground 1.4–2.0; pad every layer's overscan by the maximum shift. The corpus is 89.8% locked camera, so use parallax for 1–2 reveals per film and a moving hold (breathing, drifting dust) elsewhere.

**Secondary motion and cloth.** Verlet integration (Jakobsen, GDC 2001: `x += x − oldx + a·dt²`, constraints relaxed by projection, "for most cloth one iteration is necessary"; **V**). Damped spring: Remotion's `spring()` defaults (mass 1, damping 10, stiffness 100) give ζ = c/(2√(km)) = 0.5, about 16% overshoot, natural period about 0.63 s (**derived**, standard second-order dynamics); critical damping would be c = 20. Starting ζ (**UNVERIFIED, tune by eye**): hair or sleeve 0.3–0.5; heavy cloth or tail 0.6–0.8; UI and text ≈ 1. Wind: sum 2–3 incommensurate sines (e.g. 0.7, 1.9, 4.3 s) as a force, scaled by distance from the root and **gated by cause** (V15's version: the amplitude is `1 + 4.2·load^1.3` with `load = drag/weight`, so with no air the ripple would fall to its base amplitude; a vacuum scene must not reuse the flutter driver unchanged; §6.7, §15). The HumanCraft test: cloth waving as an independent sine is a fail.

**Camera, punch-ins, shot size, vertical safe area.** Shot-size ladder: extreme long, long, full, medium long, medium, medium close-up, close-up, extreme close-up (**V-2nd**). A cut to a tighter crop beats a slow zoom for this channel (100% hard cuts in the corpus; the HumanCraft anti-pattern "every shot has a slow zoom"); start at 115–135% (**UNVERIFIED**). Shorts: up to 3 minutes, square or vertical, 9:16 recommended (**V-2nd**); the Shorts editor shows non-safe-area guides and Google Ads says to keep key elements inside a red safe area with a right-hand column of like/comment/share (**V**). **No official pixel margins in text were found** (**UNVERIFIED**); third-party tools disagree (Socialync: top 288, bottom 672, left 48, right 192; others use centred boxes about 888×1500 or 900×1160). **Working rule until verified on a phone: keep content inside x 48–888, y 288–1248.** Verify by overlaying Google's PNG (`services.google.com/fh/files/misc/youtubesafezoneoverlay_vertical_final.png`, not downloaded here) and by an unlisted test upload.

**Animated science diagrams.** Manim structures a video as a `Scene` of `Create`/`Transform`/`FadeOut` with `wait()` holds (**V**). Kurzgesagt's own page: a per-video source sheet, about a dozen script drafts, visual metaphors sketched per scene, and narration whose recording "sets the timing for the animators" (**V**); about 1,200 hours per video (**V-2nd**). Direct labelling beats legends (EU data-visualisation guide, **V**); Tufte's data-ink ratio and small multiples (**V-2nd**); the Okabe–Ito / Wong colour-blind-safe palette `#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000` (Wong, *Nature Methods* 8:441, 2011; **V-2nd**). Claims about 3Blue1Brown colour/pacing practice and Vox practice were **not verified**. House rules adopted (§10): one cause per beat, label appears with the spoken noun, one unit and one scale bar per sequence, a concept keeps its colour for the whole film, direct-label everything.

**Captions.** Netflix English style guide (**V**): 42 characters per line, 2 lines, 20 characters/second for adults (17 for children), minimum duration 5/6 s (20 frames at 24 fps), maximum 7 s; break after punctuation and before conjunctions and prepositions, keep names together, bottom-heavy pyramid. BBC via Clevercast (**V-2nd**): 160–180 wpm, minimum about 0.3 s/word, 2 lines (3 if no key picture is covered); the "1.5 s minimum gap" in that source looks wrong (**UNVERIFIED**); the primary BBC page was blocked. A 2024 replication reports comprehension holding at 12 and 20 cps and dropping at 28 cps (Szarkowska et al.; **V-2nd**). **Tension to carry forward:** the reference corpus narrates at about 256 wpm, far above these norms; Hamza's V15 narration is 202 words in 108.7 s ≈ 112 wpm. See §13 for what V15 did and the caption rules proposed from it.

**Audio.** EBU R128: −23.0 LUFS ±0.5 LU, true peak ≤ −1 dBTP (**V**). **YouTube: no official figure found**; one blog says playback is normalised to −14 LUFS since 2019 and Frame.io says "−12 to −14" (**V-2nd**); treat −14 as a working target and read "Stats for nerds → Content loudness" on a test upload. Netflix dialogue-gated −27 LKFS ±2 LU, TP −2 dBTP (**V-2nd**; an older page says ±3 and −1 dBTP). Ducking (Sound On Sound, **V**): ratio about 2:1, attack 15–20 ms, release 600–700 ms; ducking works best on long phrases, frequent pauses cause pumping and call for automation. Speech intelligibility sits in 1–4 kHz, consonants 2–8 kHz, sibilance 3–6 kHz (male) and 6–8 kHz (female) (**V-2nd**). Small cuts of even about 1 dB in a few bands help (IOA papers; a dissenting view says the 2–4 kHz link is weaker than assumed). **No credible source found** for Foley/ambience/hit layering or for voice-compression ratios; those parts of §12 are practitioner defaults and V15 evidence, labelled as such. **V15 differs from these defaults on purpose** (bed −15 dB × envelope, 10 dB below V14, and 12/9 dB ducking, no music, −16 LUFS master); §12.4 shows the measured separation that justified it.

**Narrative editing.** Murch's Rule of Six (emotion 51%, story 23%, rhythm 10%, eye-trace 7%, 2D plane 5%, 3D space 4%; the 51% figure is debated; **V-2nd**). J/L cuts: with fixed narration the picture moves and the voice does not, so cut pictures on the beat of the spoken noun or verb. Cut on the beat: corpus state median 3.0 s (p25–p75 1.75–4.5 s), and 40% of state changes occur with no covering word. "Pattern interrupts" as a retention mechanism: **no credible source**; the practitioner use is to change one visual variable every 2–4 s, which matches the corpus median and is **UNVERIFIED as a retention claim**.

### 5.6 Research defaults for the next films

| Area | Default | Basis | Confidence |
|---|---|---|---|
| Camera | Locked frame; hard cuts; 1–2 parallax or push-ins per film | Corpus (89.8% locked, 100% hard cut) + V15 | measured (corpus); V15 verified |
| State length | Median ~3 s; fast swaps ~1.6 s | Corpus | measured |
| Cue timing | Motion starts at the word onset, ±1 frame at the film frame rate | Corpus median 33–56 ms after word | measured |
| Rig | Rigid FK parts, IK on contacts only, ≤2 bone weights, 2–4 frame follow-through delay | Spine, Toon Boom | V + practitioner |
| Spring | ζ 0.3–0.5 for hair/sleeves | Derived from a spring model | derived, tune by eye |
| Captions | 2 balanced lines ≤27 characters, cue = one phrase (V15); full text also as sidecar SRT | V15 + Netflix | V15 verified; Netflix V |
| Safe area | Content in x 48–888, y 288–1248 until verified on a phone | single third-party source | **UNVERIFIED** |
| Loudness | −14 LUFS integrated, ≤ −1 dBTP for the YouTube master (V15 is −16 LUFS) | blogs, Frame.io | **UNVERIFIED** |
| Bed vs voice | V15: bed −15 dB × envelope (10 dB below V14; background stems 15.4 LU under the voice, integrated), ducks 12/9 dB, carve 1–4.5 kHz; literature: static 12–15 dB under, light sidechain 3–6 dB | V15 measured; SOS | V15 measured; others partly **UNVERIFIED** |
| QA | HumanCraft gates + V15 gates (§17) | A1 | — |

### 5.7 Decision for the next films

1. **Keep the Cairo + whisper.cpp + ffmpeg core.** It is reproducible (isolated rebuild 8/8 byte-identical downstream of narration/ASR, §6.10, §17) and V15 shows it can carry a 110 s film with a mesh-deformed character.
2. **Pilot HyperFrames once, in isolation**, on a Short with no character (Slot 07 or 09, §15), purely as a determinism and render-time comparison. Decide after, not before. Preservation note: do not install its skills into the V15 tree or any tree with uncommitted work.
3. **Skip** Remotion (licence watch item), EffectCraft (alpha), Claude Animated Shorts (genre), WhisperX, aeneas, ctc-forced-aligner's default model.
4. **Read-only** use of Motion Skills, Anidoodle and Three.js skills for prompt structure and ideas.
5. **Re-verify** every licence and version row above before relying on it; this table is a 2026-11-25 snapshot.

## 6. V15 technical architecture (as implemented)

Everything in this section was read from source in `v15/tools/` (2,577 lines in 19 files) and cross-checked against the shipped files. Line numbers are for the files as they exist on 2026-11-25. Nothing here is theory.

### 6.1 One-page map

```
 HAMZA_VOICEOVER_RAW.mp3 ──prepare_voice.py──► HAMZA_VOICEOVER_CLEAN.wav + audio/voice_edit.csv
        │                                              │
        │                           whisper-cli (ggml-small.en, DTW) ──► qa/asr/clean_words.json
        │                                              │
        │                                  align_v14.py ──► WORD_LEVEL_TIMESTAMPS.json
        │                                              ├─► audio/narration_v14.json   (sentences, caption cues, pauses)
        │                                              ├─► audio/warp.json            (44 anchors: film time → design time)
        │                                              └─► SKYDIVER_SLOWDOWN_FINAL_V15.srt
        │
 tools/model.py (physics) ─┐
 tools/v15_shots.py (25 shots, drawn in design time) ─┐
 tools/cloth_warp.py (mesh deformation) ─────────────┼─► tools/v15.py ──► SKYDIVER_SLOWDOWN_V15_picture.mp4 (no audio)
 tools/rig_renderer.py + instrument11.py (art loader, wrist dial) ─┘          └► qa/caption_overlay.mov (transparent captions)
                                                                  
 tools/mix_v15.py ──► audio/stems/*.wav ──► audio/V15_mix.wav (−16 LUFS) + SOUND_DESIGN_CUE_SHEET.csv
 ffmpeg mux  ──► SKYDIVER_SLOWDOWN_FINAL_V15.mp4 (clean)  ──overlay──► SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4
 sync_map_v15.py · timeline_v15.py · caption_qa.py · audio_qa.py · frame_strips.py · review_sheet.py ──► qa/ , timeline/
```

`tools/build_v15.sh` (27 lines) is the single entry point. It stops on the first error (`set -euo pipefail`), and its order is the order of the pipeline above. On the original build machine a full rebuild took 3 min 02 s–3 min 04 s (`qa/build.log`, `qa/build_isolated.log`); the picture render alone took 1 min 22 s on 9 worker processes (`qa/render_picture.time`).

### 6.2 Rendering engine

| Item | V15 fact | Evidence |
|---|---|---|
| Engine | **Custom Python immediate-mode 2D renderer on Cairo.** Every frame is drawn from scratch by calling `draw(c, t)`; there is no scene graph, no retained timeline object, no GPU. | `tools/v15.py:415-421` (`frame_surface`) |
| Not used | Remotion, HyperFrames, Three.js, Blender, After Effects, any NLE. HyperFrames' *audio technique* (speech-band carve) was borrowed; its renderer was not. | `research/V15_RESEARCH_NOTES.md` |
| Languages | Python 3.14.7 (venv) for everything; zsh for the build script; JSON/CSV for data; Markdown for reports; a small static HTML page for review. | `.venv/pyvenv.cfg`, `tools/build_v15.sh`, `qa/review/index.html` |
| Python deps | `cairocffi==1.7.1`, `CairoSVG==2.9.1`, `numpy==2.5.5`, `pillow==13.0.0` (+ cffi, cssselect2, tinycss2, defusedxml, webencodings, pycparser) | `requirements.txt` |
| System deps | Homebrew `libcairo` (the code patches `ctypes.util.find_library` to load `/opt/homebrew/lib/libcairo.2.dylib`, `tools/rig_renderer.py:5-8`), Homebrew `ffmpeg`, `whisper-cli` (whisper.cpp) and `tools/whisper_models/ggml-small.en.bin` (487,614,201 bytes). | files listed |
| Fonts | `Helvetica Neue` through Cairo's "toy" font API. **macOS-only**; on Linux this silently substitutes a different font. | `tools/v15.py:81,88,112` |
| Frame size | Design space **360 × 640 units**, rendered with `c.scale(W/360, H/640)` to **1080 × 1920** (×3). 24 fps. 2,641 frames = 110.0417 s. | `tools/v15.py:31,418` |
| Frame → video | Raw BGRA frames are piped into `ffmpeg … -f rawvideo -pix_fmt bgra … -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p`. No intermediate PNG files. | `tools/v15.py:436-441` |
| Parallelism | `multiprocessing.Pool(9)`; frames split into `ceil(N/(2×workers))`-frame chunks, each chunk encoded to its own MP4, then joined with `ffmpeg -f concat -c copy`. | `tools/v15.py:444-455` |
| Determinism | Random scenery uses `hrand()`: a `random.Random` seeded by `zlib.crc32(repr(key))`. Python's built-in `hash()` is salted per process and would differ between pool workers (the code comment says so). Every other RNG has a fixed seed. | `tools/v15.py:155-157` |
| Captions | Not baked into the picture. A second render pass (`--out qa/caption_overlay.mov`) writes transparent frames as PNG-in-MOV; ffmpeg `overlay` composites them. That gives a clean MP4, a captioned MP4 and an SRT from one source. | `tools/v15.py:429-435`, `tools/build_v15.sh:19,22` |
| Final audio | AAC 192 kbps, 48 kHz, `-movflags +faststart`. | `tools/build_v15.sh:21` |

**Why Cairo was the right choice for V15 (and when it would not be).** Cairo gave exact, scriptable control of arrows, dashed lines, clips, gradients and transforms, rendered fast enough (≈ 1.5 min for 2,641 frames on 9 workers) to re-render after every change, and was byte-deterministic. It is the wrong tool for: 3-D (orbits viewed from changing angles, lit spheres), heavy particle systems, or text with rich typography. Those cases are covered by the tool review in §5.2–§5.7 and the per-video notes in §15.

### 6.3 Coordinate systems and the three clocks

V15 uses several coordinate systems at once. Mixing them up is the commonest source of bugs, so each is named here.

| Space | Units | Origin / axes | Where |
|---|---|---|---|
| **Pixel** | 1080 × 1920 px | top-left, y down | output; caption QA reports boxes in this space |
| **Design (screen)** | 360 × 640 units (1 unit = 3 px) | top-left, y down | all drawing code (`text`, `arrow`, `chip`, UI) |
| **World** | metres: X right, Y up (altitude), Z forward | camera at altitude `h` | `Cam.proj(X,Y,Z)` → screen units; terrain, clouds, houses |
| **Rig canvas** | source pixels: side rig 1920 × 819; legacy FK rigs 640 × 400 (art delivered 4× = 2560 × 1600); three-quarter 1774 wide; back 1586 wide | top-left | `BODIES`, `RIG.json`, `rig.json`, `PIVOTS.json` |
| **Physics** | seconds, metres, m/s, kg | `t = 0` at rest at 10 km | `tools/model.py` |

There are **three time axes**, and each frame converts between them (`tools/v15.py:415-421`, `tools/v15_shots.py:488-497`):

| Clock | Symbol in code | Meaning | Converted by |
|---|---|---|---|
| **Film time** | `T`, `_TR` | Real seconds in the final MP4 (0 … 110.04). Captions, SRT, audio cues and ambient motion use it. | — |
| **Design time** | `t`, `_TO = warp(T)` | The 78.2 s timeline the shots were *designed* on (V13 timings). All shot code (`k == 'lift'`, `ramp(t, 8.4, …)`) is written in this time. | `warp(T)` (monotone cubic through 44 anchors, `audio/warp.json`) and `unwarp(t)` (bisection) |
| **Model time** | `tm = model_t(t)` | Seconds into the physics run (0 … 150) | `MODEL_MAP` piecewise-linear table (`v15_shots.py:489-495`) |

The ambient clock is the clever part. `amb(t)` returns **real film time** whenever it is called with the current frame's design time, so wobble, wind streaks, flow markers, cloth ripples and the propeller keep moving at constant real speed even when a stretched narration beat slows the *story* clock (`tools/v15.py:50-53`). The picture never freezes when Hamza pauses.

### 6.4 Layer hierarchy (back to front)

From `draw()` and the helpers it calls (`tools/v15_shots.py:544-651`, `tools/v15.py:232-387`). A typical side-tracking shot (`tracking_bg` + `side_rig` + `forces`) is composed in this order:

1. **Sky gradient** (`sky`) – top colour mixes with altitude (`#86B6DA → #A9CDE6`), haze at the horizon.
2. **Ground** (`ground`) – irregular field mesh (near mesh ±9 km on 520 m cells; far bands widening to 240 km), forest clumps with shaded crowns, houses, roads, river, distant hills, horizon haze band. Every colour is mixed toward `HAZE` by `haze_k = 1 − exp(−d/40000)`.
3. **Cloud deck** (`cloud_deck`) – 240 world-space clouds from 9 Codex PNG sprites, depth-sorted, alpha reduced by haze and by closeness.
4. **Passing wisps** (`passing_wisps`) – 4 fast, large, translucent wisps (the "something goes by" depth cue).
5. **Air streaks** (`air_streaks`) – count `8 + 30·ρ/1.226` (thins out high up), speed and length from model speed, alpha from aerodynamic load.
6. **Airflow back layer** (`airflow`, layer `'back'`) – potential-flow streamlines with travelling markers (only in model scenes).
7. **Character** (`side_rig`) – continuous mesh-deformed body image, neck underlay, head / glance head, optional blink overlay.
8. **Force marks** (`forces`, `vel_arrow`, net-force arrow with white halo, `label`/`chip`).
9. **Instruments and lenses** (`alt_ruler`, `density_box`, `bar_lens`, `speed_graph`).
10. **Foreground air motes** (`fg_air`) – soft blurred streaks *in front of* the faller for depth.
11. **Captions** – only if `CAPTIONS` is true; the default is the separate overlay pass.

### 6.5 Camera transformations

Two cameras coexist.

**(a) Pinhole world camera** for terrain and clouds (`class Cam`, `tools/v15.py:142-153`):

```python
class Cam:
    """Pinhole camera at height h (m) above flat ground, pitch p (deg, + = look down), focal F (units)."""
    def proj(s, X, Y, Z):
        dy, Zr, Xr = Y - s.h, Z - s.z, X - s.x
        zc = -dy * s.sp + Zr * s.cp          # depth along the optical axis
        yc =  dy * s.cp + Zr * s.sp
        if zc <= 1.0: return None            # behind / too close: culled
        return s.cx + s.F * Xr / zc, s.cy - s.F * yc / zc, zc
```

Perspective foreshortening, haze-by-distance and size-by-depth all follow from this one function, which is why the parallax between clouds, ground and faller is physically consistent rather than hand-tuned. Pitch and focal length are animated per shot (e.g. `Cam(9990 - 20*lt, 62, 520, cy=300)` for the rear reveal; `pullback` interpolates `h`, `pitch`, `F`, `cy` and `z`).

**(b) 2-D "push" camera** for the screen layer (`push(c, fx, fy, z)`, `tools/v15_shots.py:297-298`): translate to the focus point, scale by `z`, translate back. All close-ups (wrist, face) are `push` with an `ease_io` zoom. V15 deliberately removed full-screen pushes onto the force bars (they covered the figure and the captions) and replaced them with an in-scene lens (§10).

**(c) Opening multiplane.** The opening (`opening()`, `v15_shots.py:342-374`) splits one painted landscape at its horizon into a `far` and a `near` part and zooms each by a different fraction of the dolly (`1+(Z-1)*.06`, `.12`, `.45`, `1.0` for far / near / mid clouds / subjects). That is a manual multiplane camera: depth comes from ratios of zoom, not from a 3-D engine.

### 6.6 Easing and interpolation

All easing is closed-form and lives in `tools/v15.py:68-77`:

| Function | Definition | Used for |
|---|---|---|
| `smooth(u)` | `u²(3−2u)` smoothstep | fades, `ramp` |
| `ease_out(u)` | `1−(1−u)³` | arrows and lenses growing on ("trim path" reveal) |
| `ease_io(u)` | cubic in-out | camera moves, lifts, trail camera |
| `ramp(t,a,b)` | `smooth((t−a)/(b−a))` | every on-screen element's appearance, e.g. `ramp(t, 43.75, 44.1)` |
| `wobble(t,f,seed,amp)` | two sines at `f` and `2.71 f`, amplitudes 0.6/0.4 | non-repeating ambient secondary motion; runs on the ambient clock |

There are no keyframe files for V15's shots: timing is **procedural**, written as `ramp(t, start, end)` calls inside each shot. The legacy FK renderer (`rig_renderer.value()`) uses keyframe lists with smoothstep between them, but it is unused by the V15 film (only `drawing`/`draw` from that module are used, to load art).

**Time warp.** `audio/warp.json` stores 44 anchor pairs `(film time, design time)` plus Fritsch–Carlson (PCHIP) slopes, so the cubic Hermite evaluation in `warp()` (`tools/v15.py:37-41`) is monotone by construction. `align_v14.py` also enforces a per-segment rate window `RATE = (0.34, 1.6)` design-seconds per film-second by dropping the weakest anchor until every segment fits (`tools/align_v14.py:172-182`). The limit applies to each segment's average rate; evaluating `warp()` at every frame (this audit) gives an instantaneous rate of 0.26–1.40 design-seconds per film-second, median 0.68, and confirms the warp is monotone over all 2,641 frames.

### 6.7 Character deformation

The side rig is **not** a cut-out skeleton any more. `tools/cloth_warp.py` (113 lines) applies one smooth displacement field `D(x,y)` on a 32-px grid to a single continuous 1920 × 819 image using Pillow's `Image.MESH` transform with bicubic resampling (the inverse map: each destination vertex samples the source at `v − D(v)`):

```python
def field(t, load, hands=1.0, seed=0):
    """Displacement (dx, dy) on the grid. load = aerodynamic drag/weight (0 at rest .. ~1 at speed)."""
    load = max(0.0, min(1.2, load));  calm = .35 + .65 * load
    for i, (k, tip) in enumerate(LEGS):         # knees: independent, slow, small
        ex, ey = _limb(k, tip, osc(.21 + .06 * i, seed + 1.7 * i, 2.6 * calm))
    for i, (w, tip) in enumerate(WRISTS):       # wrists: hand trims in the airflow
        ex, ey = _limb(w, tip, osc(.37 + .05 * i, seed + 3.1 + i, 4.0 * calm) * hands, sigma=70)
    if load > .02:                              # cloth: ripples travel tail-ward
        amp = 1.0 + 4.2 * load ** 1.3; om = 2.0 + 5.5 * load
        ph = _gx / 95.0 + t * om + .6 * np.sin(_gy / 70.0 + t * 1.3)
        dy += CW * amp * (np.sin(ph) * .7 + np.sin(ph * 2.13 + 1.1) * .3)
```

- `_limb()` rotates the shin-and-boot about the knee with a weight that ramps 0 → 1 along the limb, so the boot follows its shin without a joint cut.
- `CW` is a **cloth weight map**: soft boxes over trousers (1.0), sleeves (0.8) and shirt (0.45), multiplied by 0 near rigid regions (pack, head/neck, boot soles, watch) and the pack box. The pack therefore never ripples.
- Amplitude is driven by the physics: `load = ½ρv²·CdA/(m g)` (`aero()` in `v15_shots.py:34`), so cloth reacts to density *and* speed.
- Self-test (`python tools/cloth_warp.py`) asserts: zero angle = identity; pack moves < 0.35 px at maximum load; head/neck region < 1 px; whole field < 16 px (< 1 % of body length).

On top of the mesh, `side_rig()` (`v15_shots.py:55-83`) layers: a **10-frame forearm-lift sprite sequence** (`assets/v12rig/side_lift_00..09.png`, built by `tools/build_rig.py`: rest + 7 rotation steps to 22° + 2 dissolve frames; `RIG.json` says `lift_frames: 10` and `NLIFT` reads it. Two more files, `side_lift_10/11.png`, exist on disk but are never indexed, and `CHARACTER_ANIMATION_QA.md` says "12-frame": a documentation/housekeeping mismatch found by this audit), a fixed **neck underlay**, a **head** layer that nods ≤ 1° about the neck pivot `(1352, 452)`, a registered **glance head** cross-fade, and a code-drawn **blink** (skin ellipse + ink arc at eye `(1472, 291)`). Whole-body roll ≤ 0.8° and bob ≤ 1.2 units come from `wobble`.

**Known limits (documented, not hidden):** fingers do not articulate; no new facial art; the three-quarter and back views are whole-pose drawings with bob/roll only (`CHARACTER_ANIMATION_QA.md`).

### 6.8 Scientific state management

`tools/model.py` (32 lines) is the single source of physical truth: a vertical fall from rest at 10 km with fixed posture.

```python
M, G, CDA = 80.0, 9.8, 0.50          # kg, m/s^2, m^2  (assumed fixed belly-down posture)
def rho(h):                           # NASA Glenn troposphere fit
    T = 15.04 - 0.00649*h;  p = 101.29*((T+273.1)/288.08)**5.256
    return p/(0.2869*(T+273.1))
def simulate(h0=10000.0, dt=0.01):    # semi-implicit Euler, 10 ms steps
    d = 0.5*rho(h)*v*v*CDA;  a = G - d/M;  v += a*dt;  h -= v*dt
```

Verified output (`qa/model_check.txt`): peak 81.0 m/s at t = 20.0 s and 8,809 m where drag/weight = 1.000; afterwards D/W stays about 1.01–1.036 (`SCIENTIFIC_VISUAL_QA.md`: 1.009–1.036; the `model_check.txt` samples: 1.013–1.035); ground reached at 158.6 s at 50.9 m/s. `model.py` asserts: speed never negative; D/W ≥ 0.999 after the peak; ground speed < peak.

Every quantity in the model-section shots (F1, H1, I2, K1–S1) is a function of **one** model state per frame; the hook (A1–E1) and the J1 and I1 comparisons use fixed illustrative values, some through `PHYS.rho`:

```python
def state(tm):  t, h, v, dw, rho = PHYS.at_time(tm or 0.0);  return h, v, dw, rho
```

and `MODEL_MAP` (film design time → model seconds, e.g. `(47.71, 30), (55.57, 60), (57.16, 90), …, (78.2, 150)`) is the **declared time compression**: 150 model seconds are shown in 57 design seconds. Altitude marker, density-dot count, arrow lengths, bar heights, needle angle, cloth load, airflow intensity and graph cursor all read the same `state()` (§9 generalises this). `v15.py --check` asserts the invariants the *picture* must keep: monotone model time, speed never negative, altitude never rising, needle never rising after the crossing, every shot present, and a minimum altitude shown above 300 m (`min(hs) > 300`; the build log prints 445 m) (`tools/v15.py:463-481`).

### 6.9 Audio, subtitles and encoding

Covered in detail in §11–§13. In brief: `prepare_voice.py` edits the raw voice; `align_v14.py` produces word/phrase timing, captions and the warp; `mix_v15.py` synthesises and ducks five stems with numpy + ffmpeg and masters to −16 LUFS with a limiter; `build_v15.sh` muxes AAC 192k and overlays captions. Independent re-measurement on 2026-11-25 of the final MP4: integrated −16.0 LUFS, LRA 3.4 LU, true peak −1.5 dBFS, 2,641 frames, 0 decode errors on a full decode pass (this audit; `ffmpeg -af ebur128=peak=true`).

### 6.10 Reusable modules vs. debt

| Module | Reusable as is? | Needed to generalise |
|---|---|---|
| `model.py` pattern (state function + checks) | Pattern yes | Replace with a per-video `model/` package exposing `state(model_time)` and `invariants()` (§9) |
| Easing / ramp / wobble helpers | Yes | Move into `lib/motion.py` |
| `Cam` pinhole + haze | Yes for any ground/space-view scene | Add 3-D camera path presets; add star/planet primitives |
| Arrow, chip, label, lens, bars, graph primitives | Mostly | Parameterise palette and scale; remove skydiver constants (`L_W`, `BAR_BASE`, `SPEED_MAX`) |
| `align_v14.py` word matching + PCHIP warp | Yes, but only needed when re-timing an existing design; **for new films design on the final narration instead** (§11) | Split into `transcribe.py`, `phrases.py`, `captions.py`, `warp.py` |
| `prepare_voice.py` | Yes | Make `PRE_END`, `CAP`, `TARGET` config; detect pre-roll automatically from a transcript |
| `mix_v15.py` | Generators, `carve`, `speech_curve`, `master` yes; `CUES` table no (per film) | Move cue table to JSON; keep generators in `lib/sfx_synth.py` |
| `cloth_warp.py` | Method yes; geometry constants are per-character | Read `LEGS/WRISTS/CLOTH/RIGID` from the character's rig JSON |
| `caption_qa.py`, `audio_qa.py`, `sync_map_v15.py`, `frame_strips.py` | Yes after parameterisation | Take a project config instead of `exec`-ing `v15.py` |

**Structural debt to fix before the next film** (observed, not speculative):

1. `v15.py` loads shot code with `exec(open('v15_shots.py').read())` into its own namespace, and six QA/mix scripts (`mix_v15.py`, `caption_qa.py`, `sync_map_v15.py`, `timeline_v15.py`, `frame_strips.py`, `review_sheet.py`) `exec` `v15.py` the same way. It works, but the dependencies are implicit and invisible to linters and to a new Claude/Codex session. Replace with real imports and an explicit `Project` object.
2. Shot code is written in **V13 design seconds** and warped to V14/V15 film time. That was the right *recovery* for a late narration swap (§11) but a poor *default*: future shots should be written in film time on the final narration.
3. Hard-coded constants that must become config: `V13_DUR = 78.2`, `D=110.0417` (in `build_v15.sh`), `MODEL_MAP`, `EVENTS`, `SPEED_MAX`, caption baseline.
4. The venv records an absolute path from another user account in `pyvenv.cfg` (`/Users/ghilmanislam360/…/v13/.venv`) and its interpreter link targets `/opt/homebrew/opt/python@3.14`, which is **not installed on the Mac this audit ran on** (only Python 3.12 is). The isolated rebuild was verified on the original machine (`qa/isolated_rebuild.txt`); it has **not** been re-run here. Treat "reproducible" as *proven on the build machine, unverified on this one* until Python 3.14 and the venv are re-created and the 8 hashes in `qa/checksums_v15.txt` are re-checked.
5. Stale references remain: `mix_v15.py`'s docstring names `tools/v14_shots.py`, and `tools/strip.py` calls `tools/v13.py`, which does not exist in `v15/tools/` (a dead script). `align_v14.py` and `prepare_voice.py` keep V14 names although V15 uses them.

## 7. Character animation system and the Claude → Codex asset request

**Scope of the evidence.** V15 animates **one** character doing **one** action (a belly-to-earth freefall) in a handful of views. Everything V15 proves is marked *verified*. Walking, running, sitting, a spacesuit and a cast of several people are **PROPOSED**: they are needed for the nine remaining films (§15) and are built here from the rig conventions in §5.5 and the HumanCraft rules, not from anything V15 did.

### 7.1 What V15 actually has (verified in the tree)

| Item | Where | Fact |
|---|---|---|
| Rig folders | `v15/rigs/{side,back,three_quarter,closeup,instrument,pov,wrist}/` | Seven views; `rigs/side/rig.json` has `canvas [640,400]` and a `parts[]` list with `id, file, parent, pivot, limits` (e.g. `far_upper_arm`, parent `torso`, pivot `[396,195]`, limits `±32°`) |
| Original Codex layered parts | `assets/codex/{side,back,…}/` | 73 PNG layers (67 at 2560×1600, 4 instrument layers at 1120×828, 2 POV layers at 1440×960), produced by Codex's `image_gen` (13 calls); the **V10-era FK parts**. `manifest.csv` columns `view,part,file,source,width,height,sha256` |
| What is on screen in V15 | `tools/v15_shots.py` `side_rig()`, `body()` | The **side** view is a *single continuous drawing* `assets/v11reg/side_body.png` mesh-warped by `cloth_warp.py`, plus a 10-frame forearm-lift sprite sequence (`side_lift_00…09.png`), a neck underlay, a head layer (≤1°), a glance head cross-fade and a code-drawn blink. The **back** (and, in V11–V12, three-quarter) views are whole-pose drawings. The V13 manifest records the three-quarter pose as no longer on screen |
| Rig data actually read at render time | `assets/v12rig/RIG.json` (`lift_frames`, `neck_pivot`) | Constants such as `EYE = (1472, 291)` and per-view centres of mass `COM = {'side': (325,210), 'three_quarter': (327,214), 'back': (321,212), 'front': (320,216)}` are in `v15.py` / `v15_shots.py` |
| Character design reference | `history/v8/CHARACTER_DESIGN_BIBLE.md` | The identity rules (costume, bare hands, neutral face) that every view had to match |

**The honest summary of the rig history** (details in §3.4 and §4): FK limb rig from generated parts (V8–V10) → rejected by the owner for visible round joint caps → whole-pose swaps with no limb motion (V11) → constrained sprite rig for one forearm and the head (V12) → a Codex package that failed its own tests twice (V12, V13) → **mesh deformation of one continuous drawing (V15)**. The architecture was changed four times *because of the art*, never because of a design decision. This is the root cause the next section is built to remove.

### 7.2 Rig decision tree for a new character (PROPOSED, derived from the V8–V15 failures)

1. **Does the character have a body part that must bend or rotate visibly in the film?** If no, use a **whole-pose drawing** plus breathing, bob and roll (V11). Cheapest; zero seam risk.
2. **Is the character made of soft cloth and the motion is small (< about ±5°) or secondary?** Use **mesh deformation of one continuous drawing** (V15). Needs a *clean continuous drawing*, a weight map and a rigid-zone mask. No joint can ever show a seam; the price is that large rotations stretch the art.
3. **Does a limb need a large rotation (> about ±20°)?** Use **layered rigid parts with FK**, and demand hidden overlap art as *cloth or a purposely drawn joint*, never a generic circular cap. For hard-shell characters (a spacesuit, §7.3) a visible joint ring is *correct* and can be drawn deliberately; the V10 owner objection was to round caps on a soft-cloth skydiver.
4. **Does a limb need to hit a contact (a hand on a console, a foot on ground)?** Add **two-bone IK for that limb only** (§5.5: Spine says IK is one- or two-bone, useful for feet not penetrating the floor). A planted foot is constant in world space during stance (HumanCraft §4.3).
5. **Is a big pose change needed (arm lifting to the face)?** Use a **sprite sequence** of generated in-between drawings (V12/V15's 10-frame lift), cross-faded or stepped, with a rest-pose pixel-match test.

Never combine two techniques on the same body part in the same shot unless a proof clip passes the seam test (§7.7).

### 7.3 Standard character package (PROPOSED standard; every field is checkable)

**View set.** A character needs, at minimum, the views the storyboard uses, decided *before* the request: `side`, `three_quarter`, `back`, `front`, `closeup` (face), plus props. Identity rules (costume, hands, face, proportions) are written once in a `CHARACTER_BIBLE.md` and every view is tested against it (the "identity test").

**Parts and layer order** (back to front; names follow HumanCraft §4.2 and Toon Boom's master→pelvis→torso hierarchy; **V-2nd**):

```
master (root, no art)
└─ pelvis                       far_thigh → far_shin → far_foot       (behind)
   └─ torso  (pack/backpack child; harness; far_upper_arm → far_forearm → far_hand behind torso)
      ├─ neck → head (helmet, face, eyes, brows, mouth, mouth_open, lids)
      └─ near_upper_arm → near_forearm → near_hand                    (in front)
   └─ near_thigh → near_shin → near_foot                              (in front)
contact_shadow (child of master, scaled by elevation)
props (own parent; hand-held props re-parent to a hand)
```

**Pivots.** Each part carries `pivot [x,y]` in canvas pixels, `parent`, `draw_order`, and `limits [min,max]` in degrees. **`null` means unknown and blocks integration**: the V12 `PIVOTS.json` was all `null` and Claude chose pivots by visual test (the first elbow pivot opened a gap; head ±4° failed and was cut to ±1°). Pivots are *certified by a test*, not by a statement.

**Overlap.** Every child extends under its parent by a hidden overlap. **State the unit**: the V9 request asked for 8–12 px on the 640×400 rig canvas (delivered at 2560×1600, never converted), V13 asked for ≥ 25 px on 1920×819; it was never *tested* (§7.7).

**Mesh.** For soft parts only: grid size (V15: 32 px on 1920×819), a weight map (`CW`) that is 1 where cloth moves and 0 in rigid zones (pack, helmet, device), a maximum displacement in px (V15: under 16 px; pack under 0.35 px), bicubic resampling.

**Faces.** Neutral mouth in all views (the three-quarter V10 face was smiling); blink drawn in code as an eyelid shape; glance as a head cross-fade; **a face may not change identity between views**.

**Hands.** One decision, recorded: **bare hands in every view** for the skydiver (the V13 "gloves vs bare hands" mismatch lasted V10–V13). Hands are the first thing an identity test checks.

**Clothing and cloth.** Cloth weight (heavy/light), which zones are rigid, and what drives the ripple (V15: `load = drag/weight`; ripple amplitude `1 + 4.2·load^1.3` px). If the cause is absent (no air) the driver must be absent.

**Motion phase lists** (the V15 film needs none of these; the next nine do, §15):

| Action | Phases | Status |
|---|---|---|
| Belly-to-earth freefall (USPA neutral position) | arch from the hips, hands about shoulder level, elbows slightly below, knees shoulder-width, toes pointed; relaxed oscillation of lower legs and hands, a still head | **Verified** (V15, `research/V15_RESEARCH_NOTES.md`) |
| Walk | contact → down → passing → up → contact (HumanCraft §4.2) | PROPOSED |
| Run | contact → flight → contact; both feet off the ground in flight; torso lean; arms counter-swing | PROPOSED, no source in the tree beyond the walk list |
| Jump (hop on a small body, Slots 04–05) | anticipation → push → flight → landing → compression → settle (HumanCraft §4.2); in low gravity the flight arc is a long, slow parabola | PROPOSED |
| Sit down (control room, Slot 06) | weight shift forward → hips lower along an arc → contact with the seat → settle | PROPOSED |
| Look down at a wrist, glance at the viewer | head turn leads, eyes lead the head by 2–3 frames, blink on the head turn | V15 verified for the glance and blink (cross-fade + code blink) |

### 7.4 Secondary motion rules (verified where marked)

- Delay a child 2–4 frames behind the parent and add a damped spring (§5.5; defaults **UNVERIFIED**, tune by eye).
- Ambient motion is on the **real clock** (`amb(t)`), not the warped design clock, so stretched beats do not freeze (**verified**, §6.3).
- No always-moving decorative loops: every secondary motion has a cause (HumanCraft rule 12; V15's cloth is driven by `load`).
- Idle body motion for a "moving hold": breathing about 0.25–0.3 Hz amplitude under 1% scale (practitioner default, **UNVERIFIED**; V15 uses `wobble()` = two incommensurate sines, §6.6).

### 7.5 What the owner rejected or QA found, as acceptance criteria

These are the observed failures, turned into pass/fail tests (sources: `history/v11/V10_SCREENSHOT_DEFECT_AUDIT.md`, `history/v13/…COMPARISON.md`, history digest in §4):

| Observed in | Defect | Test that would have caught it |
|---|---|---|
| V10 (0:13, 0:16, 0:22) | Round joint discs, "bolted on" limbs, oval boot tops | **Seam test at extremes**: render every joint at both limits on sky blue and look for any disc, gap or double outline |
| V10 (0:16) | "Different person" face | **Identity test**: side, three-quarter, back and close-up shown side by side |
| V10–V13 | Smiling three-quarter face; grey gloves vs bare hands | Identity test, plus a single `CHARACTER_BIBLE.md` |
| V10 (0:55) | Instrument read as a clock with a long strap, no wrist | **Wrist test**: the device sits on the same wrist in every view |
| V11 | No limb motion at all | **Motion-contract check**: every body part that the script mentions must have a keyed event |
| V12 | A ~4 px elbow notch for ~0.3 s; head limited to ±1° | Seam test at the *shot's actual* range, not 60% of it (V10's QA tested "60% of limits" and missed the discs) |
| V14 | Stray grey fragment under the aircraft tail (2,754 px detached blob) | **Component test** in the validator (§7.7) |

### 7.6 The standard Claude → Codex asset request (copy this; fill every `<…>`)

This is the structure that worked best in the surviving briefs (`codex_request/v11/CODEX_V12_ART_BRIEF.md`, `codex_request/v12/CODEX_V13_ART_BRIEF.md`), with the V9 request's priority table and the missing acceptance numbers added. **Package names use the version that will consume them** (a V11 request that produced `CODEX_V12_ART_PACKAGE` caused a persistent off-by-one).

```markdown
# <CHANNEL> — Codex art brief for <FILM_ID>   (from Claude, <date>)
Request ID: <FILM_ID>-ART-<n>     Deliver into: CODEX_<FILM_ID>_ART_PACKAGE_<n>/   (+ zip, + SHA256SUMS.txt)

## 0. Why this exists (3 sentences)
What the previous package got right, what failed, and which shot needs this art. Cite the shot IDs.

## 1. Do not / Do
Do not: change the character design; redraw poses that already work; add text, scales, numbers,
arrows or diagrams (Claude draws those in code); add a circular cap or disc at any joint.
Do: preserve every earlier file; deliver only into the folder above; use the master named in §2.

## 2. Reference files (in this folder) and the MASTER
- master_<view>.png  <- "Use this as the master." Exact canvas <W>x<H> px, RGBA.
- pivots_target.png  <- numbered approximate pivots (Claude's estimate; certify or correct).
- bible.md           <- identity rules: costume, hands (bare/gloved), face (neutral), proportions.

## 3. Priority table (every asset on one line)
| Asset ID | Shot IDs | Purpose (what must move / be seen) | View | Components | Expected path | Priority |
|---|---|---|---|---|---|---|

## 4. Layer spec (one table per pose)
| Layer | Contents | Parent | Pivot | Draw order | Limits (deg) |
Requirements:
- Same canvas as the master, same pixel position as the master (no cropping, no trimming).
- Hidden overlap art under each parent: <8-12> px, CLOTH or a purposely drawn joint, never a generic round cap.
- Fill behind every limb that moves: the body layer must contain what a lifted arm uncovers.
- Clean alpha: no haze; no thresholded hard edges; nothing touching the canvas edge unless the master does;
  RGB must be 0 where alpha is 0 (see validator); no detached stray components.
- PIVOTS.json: {layer: {pivot:[x,y], parent:name, draw_order:n, limits:[min,max]}} in canvas pixels.
  Unknown = null, never guess. A null pivot makes that layer "candidate".

## 5. Joint extremes Claude will render (so you can test first)
| Joint | Extremes (deg) |

## 6. Acceptance tests (Claude runs these BEFORE using any file; any FAIL = candidate)
- Rest test: assembled layers at rest == master within anti-aliasing (report max abs diff and # px > 8).
- Seam test: every listed extreme on sky blue; no gap, disc, double outline.
- Lift/occlusion test: lifting the arm reveals jacket/harness, not empty background.
- Identity test: same person in every delivered view; same hands; neutral face.
- Component test: validate_asset.py reports no stray component and RGB-under-zero-alpha == 0.
- Native-resolution test: state the true generation size; 4x exports that are resampled must be labelled "resampled".

## 7. Status labels
Anything that fails a test or is unverified is `candidate`. Never label it `approved`. Codex's OWN failed
test = package status BLOCKED (Claude does not integrate it).

## 8. Required package contents
ARTWORK_QA.md (what you checked, what FAILED), ASSET_MANIFEST.csv (schema in §8.4), PIVOTS.json,
IMAGE_GENERATION_PROMPTS.md (exact prompts and which are rejected), previews/, SHA256SUMS.txt.

## 9. Return path
Claude replies with <FILM_ID>_INTEGRATION_MANIFEST.csv (file, decision, use, evidence, status, sha256).
```

**Why each clause exists** (evidence): the *Do not* list and master file are from the V12 brief; the **priority table** is the V9 request (`Asset ID | Shot IDs | Purpose | Viewpoint | Components | Pivots | Expected path | Priority`); the **acceptance tests** were first written in the V11→V12 brief *after* the V9–V11 requests, which contained none; "RGB must be 0 where alpha is 0", "no stray components" and "native-resolution" come from defects recorded in V9, V12 and V13 (§8.3); "Codex's own failed test = BLOCKED" comes from Codex shipping a package labelled "NOT READY TO ANIMATE… Motion FAIL" (V12) and "P0 not met" (V13) that Claude still had to read and reject.

### 7.7 Asset validation

**What V15 had.** `assets/codex/validation.json` records `png_count: 73`, `all_dimensions_and_alpha_pass: true`, and a mode/size/alpha-range row per file, with the note "These are review evidence, not automatic seam approval." That check is *necessary but not sufficient*: it passed while the owner found the round discs on screenshots.

**What the next pipeline should run (PROPOSED).** The reference check below was **written and run during this audit** on four real V15 files in a scratch environment (numpy, Pillow, scipy). It is not part of V15 and is not stored in the project tree; it is reproduced in full in Appendix B so that another session can create it. Results on V15 assets:

| File | Result |
|---|---|
| `assets/v12rig/side_lift_00.png` | clean, no warnings |
| `assets/v11reg/side_body.png` | **707 px of non-zero RGB under zero alpha** (warning) |
| `assets/codex/aircraft_side.png` | **flags a 2,754 px detached component** (the stray grey fragment that stayed in V14 and was removed in V15) |
| `assets/codex/aircraft_side_v15.png` | stray blob gone, but **3,250 px of non-zero RGB under zero alpha** (warning) |

A note on a tuning decision: the first version of the "semi-transparent" metric flagged ~99.7% of pixels because generated art has body alpha 253–254, not 255; the check therefore treats alpha ≥ 245 as opaque. This is the kind of threshold that must be re-tested against each generator.

**Full acceptance procedure (what is automated, what is not):**

| # | Check | How | Automated? |
|---|---|---|---|
| 1 | Mode, canvas size, alpha range | `validate_asset.py --canvas WxH` | yes |
| 2 | Alpha bounding box vs the manifest's `alpha_bounds` | compare | yes (to build) |
| 3 | RGB under zero alpha | validator | yes |
| 4 | Detached stray components | validator | yes |
| 5 | Fringe / haze share | validator (`semi_transparent_share`) | yes |
| 6 | Rest test (assembled == master) | per-pixel diff | to build |
| 7 | **Seam test at extremes** | render joints at limits on sky blue → contact sheet | to build; **a human must look** |
| 8 | **Identity / hands / face** | side-by-side sheet | human |
| 9 | Wrist / instrument registration | overlay `WRIST_FACES.json` circle | to build + human |
| 10 | Native resolution | read the generator's report; test a 2× downsample/upsample for blur | human + script |
| 11 | SHA-256 of every file recorded in the manifest | `shasum -a 256` | yes |

**Do not claim** a check passed that was not run. A contact sheet that nobody looked at is *evidence prepared for review*, not review (§17).

### 7.8 What to ask Codex for in the next nine films

Derived from the production cards in §15 (which characters appear where): one **spacesuit** character (Slots 01, 04, 05, 10; side view plus a front view for 01; mesh-deform not needed in vacuum, so rigid FK with deliberate suit joint rings is correct), one **generic engineering team** of 2–3 people (Slot 06; three-quarter and back views; sit/turn), one **beach figure** in back view (Slot 08), and **environment** art (Phobos with Mars, a control room, a beach, the Moon from above). Shorts 03, 07 and 09 need **no character at all**. Request nothing until the beat maps exist (§15, §18 G0).

## 8. Codex and Claude: responsibilities, naming, folders and asset standards

### 8.1 Who does what

**Definition (as used in the V15 files).** *Codex* = the OpenAI image-generation agent that delivered illustrated art packages through its built-in `image_gen` tool ("no image API key or paid external API workflow", `assets/codex/README.md`). *Claude* = the Claude Code sessions that wrote every line of code, every audio file, every QA document and every brief. The V9 request states the split in one sentence: *"Claude does the procedural animation, airflow, forces, camera, terrain and editing. Codex supplies the complex illustrated artwork"* (`history/v9/CODEX_MISSING_ASSET_REQUEST_V9.md`).

| Work item | Owner (observed V9–V15) | Proposed rule for the next films |
|---|---|---|
| Script, narration recording, final wording, all approvals | **Owner (Hamza)** | Unchanged. No agent edits an approved script (§15). |
| Research and claim ledger | Claude | Claude drafts `CLAIMS.csv`; owner approves; every on-screen number traces to a row (§9.4). |
| Illustrated characters, props, painted environments | **Codex** (image generation) | Codex, against the request template in §7.6. Whole continuous poses are preferred over jointed parts (§7.2). |
| Splitting art into layers, pivots, overlap art | Codex *requested*, but delivered failing packages twice (V12 "NOT READY TO ANIMATE… Motion FAIL", V13 "P0 not met"); in practice **Claude** repaired in code | Codex delivers layers *with* certified pivots and passes its own tests first. If it cannot, Claude does the registration **before** any animation (never integrate `pivot: null`). |
| Art repair in code (boot caps, recolour, hand/neck/fold finishing, stray-blob removal) | Claude (`work/legacy_v11/fix_boots.py`, `recolour.py`, `work/hands.py`, `folds.py`, `neck.py`, `finish.py`) | Allowed, but recorded in the integration manifest as "repaired by Claude" with before/after hashes. |
| Rigs, mesh deformation, renderer, camera, parallax | Claude | Unchanged (§6). |
| Scientific model, force/graph/lens drawing, labels, instruments (dial face and needle) | Claude (code-drawn; Codex is told *never* to draw text, numbers, arrows, scales) | Unchanged. |
| Terrain and environment mesh | Claude, painted references from Codex | Unchanged. |
| Narration cleanup, transcription, alignment, phrase cues | Claude | §11. |
| Sound design, mix, master | Claude (numpy-synthesised stems, §12) | §12. Rights-clear by construction. |
| Captions | Claude | §13. |
| Automated QA | Claude | §17. |
| **Human review: watching real-time playback, listening, accepting** | **Owner**; a human reviewer | **No agent may mark a human step done** (§17). V15 has no recorded owner acceptance. |
| Package naming and the integration decision | Claude | §8.2, §8.5. |

**What Claude may not assume from Codex:** that an asset is on-model, that its pivots are right, that its alpha is clean, that a 4× export is native resolution, or that an image service will perform every edit (one shoulder edit was refused by the image service's safety system in the V10 supplement, `assets/v10supp/ASSET_QA.md`).

### 8.2 Naming rules

1. **Packages are named after the film version that consumes them**, e.g. a package built for V12 is `CODEX_V12_ART_PACKAGE`, *not* the version that issued the request. In V11–V13 the reverse convention (request-version naming) produced a persistent off-by-one (history digest, §3 "Naming and format").
2. **One film = one folder named for the film**, never "v15" as a standing project name: for the next films, `<slot>_<slug>/` (e.g. `07_laser_moon_round_trip/`), with versions as sub-folders only if more than one render exists (§16).
3. **Asset IDs** are lowercase `snake_case`: `<view>_<part>` for character layers (`side_near_forearm`), `<noun>_<variant>` for everything else (`aircraft_side_v15`). Variants and repairs get a suffix; originals are never overwritten.
4. **Statuses are one of** `candidate`, `reference_only`, `approved`, `not_used`, `blocked`. `approved` may only be set by the owner (art) or by a passing acceptance test plus owner sign-off. V10–V13 root documents (and V14's Roman-Urdu report) carried "candidate / not approved art", while V9 and most V14 documents did not; **V15's root documents dropped that line** (a lapse recorded here so it is not repeated).
5. **SFX and music** files keep their source filename in a `source_name` column of the ledger (§12.6); never rename a licensed file without recording the original.

### 8.3 Transparency and resolution standards

| Property | Standard (PROPOSED unless marked) | Evidence |
|---|---|---|
| Format | RGBA PNG, straight alpha | Verified V15 files are RGBA |
| Canvas | **Every layer of one pose on the same canvas as the master, same pixel positions** (no cropping) | V12/V13 briefs; the V12 package used 1920×819, 1774×887, 1586×992 and 1536×1024 canvases (the V13 manifest has about 14 distinct canvases) in different views, and a 1585 vs 1586 px generation had to be padded |
| Generation size | State the true generation size; exports larger than that are labelled `resampled` | V9: 2560×1600 exports; "4× exports were resampled, not native 4×" (V13) |
| Alpha | Body alpha may be 253–254 rather than 255 in generated art: treat ≥ 245 as opaque. No haze, no thresholded hard edges, no low-alpha fringes (found in V10 supplement, V12) | validator measurement, §7.7 |
| RGB under zero alpha | **0**; if not, the loader must crop by alpha, not RGB | V9 README; validator: 707 px in `side_body.png`, 3,250 px in `aircraft_side_v15.png` |
| Stray components | None above a size threshold | `aircraft_side.png` has a 2,754 px stray blob |
| Edge touching | Nothing touches the canvas edge except where the master does | V12 brief |
| Overlap art | 8–12 px hidden cloth overlap under each parent | V9 request |
| Safety margin for transforms | Author art at no less than the largest on-screen size it will be drawn at, so it is only ever downsampled (V15 renders a 360×640-unit design space at 1080×1920, i.e. 3 px per unit; the render-time scale of each asset was not audited here) | §6.3 |
| Colour | One colour space (sRGB); no embedded profiles surprises | **UNVERIFIED** (not checked in V15) |

### 8.4 Manifest schemas

**V12 package** (`CODEX_V12_ART_PACKAGE/ASSET_MANIFEST.csv`):

```
asset_id,path,canvas_px,pivot_px,parent,draw_order,alpha_bounds_geometry,channels,status,method_or_purpose
side_head,character/side/side_head.png,1920x819,null,side_body,1,328x359+1210+108,4.0,candidate,split from source or image-generated local edit; see QA
```

**V13 package** (`CODEX_V13_ART_PACKAGE/ASSET_MANIFEST.csv`; `pivot` now filled in; "pose already applied, do not rotate again" is noted where relevant):

```
file,canvas_px,pivot_px,parent,draw_order,alpha_bounds_ltrb_exclusive,method,status
character/side/side_head.png,1920x819,"[1352, 452]",side_body,30,"[1210, 108, 1538, 467]",generated then locally registered/masked,candidate
```

**Claude's integration manifest** (`history/v13/CODEX_V13_INTEGRATION_MANIFEST.csv`):

```
file,decision,v13_use,evidence,status,sha256
ARTWORK_QA.md,REFERENCE ONLY,-,preview / source / document,candidate (not approved),612918ae…
```

Its V13 outcome was **38 REFERENCE ONLY, 6 NOT USED, 2 USED** out of the whole package: integration decisions are data, not memory.

**Original V10 manifest** (`assets/codex/manifest.csv`, sha256 per file): `view,part,file,source,width,height,sha256`.

**Proposed single schema** (superset, PROPOSED; every column exists in at least one of the manifests above):

```
asset_id, path, view, part, canvas_px, pivot_px, parent, draw_order, limits_deg,
alpha_bounds_ltrb_exclusive, generation_px, resampled(y/n), rgb_hidden_px, stray_components,
method (generated | split | repaired-by-claude | drawn-in-code), prompt_ref, status, decision,
used_in (shot ids), evidence (path), sha256
```

### 8.5 The handoff protocol (the order in which things happen)

1. Claude writes the request (§7.6), including the master and the acceptance tests, **before** Codex draws anything.
2. Codex delivers into `CODEX_<FILM>_ART_PACKAGE_<n>/` with `ARTWORK_QA.md` listing **what failed**, not only what passed.
3. Claude hashes the package (`SHA256SUMS.txt`), runs the validator and the five acceptance tests, and writes the integration manifest. Any fail ⇒ `candidate`; a failed test that Codex itself reported ⇒ `blocked` and the package is not integrated (V12 and V13 were integrated in part *despite* Codex's own failing QA, costing a version each).
4. Claude proves the rig in a 5–12 s moving proof on the **shot's actual range of motion** (HumanCraft's "mandatory moving proof"; V10's QA tested only 60% of the limits and missed the discs).
5. The owner reviews the proof on a phone. Only then is the asset `approved`.
6. Nothing in an earlier package is overwritten or deleted without the owner's explicit permission (V8–V12 were deleted with permission at V13 and are now unrecoverable beyond docs; §4.1).

### 8.6 Acceptance tests Claude runs before using any art

| Test | Pass condition | Source |
|---|---|---|
| Rest | assembled layers at rest equal the master within anti-aliasing (report max abs diff, count of pixels > 8) | V12 brief; Codex V13 failed it with 11,936 differing RGBA px |
| Seam | at every listed extreme, no gap, no disc, no double outline | V12 brief |
| Lift / occlusion | lifting the arm reveals jacket and harness, not background | V12 brief |
| Identity | same person (hands, face, costume) in every view | V12 brief |
| Wrist / instrument | the device sits on the same wrist in every view; face centre matches `WRIST_FACES.json` | V12 brief; Codex's fits (88/80, 75/74) disagreed with Claude's (84/81, 76/85) |
| Component / alpha hygiene | validator clean (§7.7) | this audit (PROPOSED) |
| Provenance | prompt, tool and date recorded; not an image of a real person or a copyrighted work | V9 README ("no image API key"), §12.6 for audio |

### 8.7 Failure modes observed in handoffs (one line each, with the version)

The V9 torso arrived with a baked-in pack, a grey head and bent upper arms. Rear forearm/hand registration was wrong. Round joint caps and oval boot tops (V10). Smiling three-quarter face and glove mismatch (V10–V13). No true side or oblique device view; buckle and ticks baked in (V10). The V11 package had no layered rig at all. The V12 partition had no hidden torso or sleeve overlap; its underlay experiments were "large haze". Nonzero RGB under zero alpha (V9), thresholded alpha (V10), low-alpha fringes (V12), hard internal cuts in wrist layers (V12). `PIVOTS.json` all `null` (V12). Rig channel names changed between versions (`plate/pointer` → `housing/dial_face/needle/cap`). `layered.svg` was a raster carrier, not vector. Canvases varied from package to package. Every item above maps to a clause in §7.6 or a test in §8.6.

## 9. Scientific visualization engine

### 9.1 What V15 built (verified; code excerpts are in §6.8)

One function, `state(tm)`, returns every physical quantity for a model time `tm`; the picture never invents a number. `tools/model.py` is an semi-implicit-Euler integrator (dt 0.01 s) of `m·dv/dt = m·g − ½ρ(h)·v²·CdA` with **m = 80 kg, CdA = 0.50 m² (assumed), starting at rest at 10 km, ρ from the NASA Glenn troposphere fit**. Its `qa/model_check.txt` output is:

```
peak speed 81.0 m/s at t=20.0s h=8809 m; drag/weight there 1.000
t=  30.0s  h= 8009  v= 78.5  D/W=1.035  rho=0.526
t= 158.6s  h=    3  v= 50.9  D/W=1.013  rho=1.226
model checks pass; ground reached at 158.6 s
```

Every on-screen quantity in the model-section shots reads that one state (the hook and the J1/I1 comparisons use fixed illustrative values): altitude marker, density dots (count ∝ ρ), arrow lengths, bar heights, dial needle, cloth and airflow load (`drag/weight`), the graph point. Invariants asserted in `--check` (2,641 frames): speed ≥ 0; after the peak D/W ≥ 0.999; ground speed < peak; model time never runs backwards; altitude never rises; the needle never rises after the crossing; minimum altitude shown above 300 m (the build log prints 445 m); warp monotone; all 25 shots appear. The V9 audit found that V8 had drawn drag at 91 against weight at 60 (1.5×) where the model gives ≤ 1.035, an overstatement of about 17× in the excess: **that is the defect this engine exists to prevent**.

**The idea→shot→mark→check ledger** (`SCIENTIFIC_VISUAL_QA.md`) is the pattern to copy: for each of the ten ideas in the script, the film time it appears, exactly how it is drawn, and the numeric check that guards it ("Drag length = 24·k²", "Bar heights = 250 × (1, D/W)", "Arrow length = (D/W − 1)·118·8"). **Colour grammar, one meaning per colour:** weight orange `#DB7224` (solid, down), drag teal `#2F7F7A` (solid, up), downward velocity blue `#2F5D8C` (*dashed*, its own lane, never a solid force arrow), net force violet `#7A4CC2` (double shaft), relative air light blue `#5E8FB3` (dots and streamlines, no arrowheads). V14 used rust `#9A4F2C` for weight; V15 changed it to orange.

### 9.2 The generalised engine (PROPOSED structure; the V15 files are the template)

```
science/
  model_<film>.py        # state(tm) -> dict of SI quantities; integrator or closed form; self-check at __main__
  CLAIMS.csv             # one row per number said or shown (schema in 9.4)
  TIME_MAP.py            # MODEL_MAP: [(film_s, model_s), ...]  (V15: 150 model s -> ~57 design s)
  SCALES.py              # every magnification / not-to-scale decision, once (V15: ZOOM = 8)
  check.py               # asserts every invariant below; run before every render
```

Rules the engine enforces (each is observed in V15 or required to avoid a recorded V8–V14 defect):

1. **One state, one source.** No drawing function receives a hand-typed magnitude. Hand-typed numbers are allowed only as *labels* that are also in `CLAIMS.csv`.
2. **One scale per diagram, chosen once.** V15's weight arrow is 118 units on the common scale; drag = `118·D/W`.
3. **One disclosed magnification.** The net force is 0.9–3.6% of the weight (about 4 design units, about 13 px at 1080 wide, at true scale); it is shown at ×8 in **one place and one way**, with a "×8" badge on the lens rim and "net force ×8" on the arrow. The V9–V13 history shows repeated redesigns of the same problem (10× inset, 10× lens, 30× card, 30× lens, bars plus push-in, ×8 lens); the lesson is to decide once (`SCALES.py`).
4. **Time compression is a mapped function, not a speed-up knob.** `MODEL_MAP` is monotone; the check asserts model time never runs backwards. Visible compression is disclosed ("time compressed") whenever it exceeds what a viewer would assume.
5. **Invariants are asserted, not eyeballed.** Write the physical limits (conservation, signs, monotonicity, limiting cases) as `assert`s in `check.py`.
6. **Idealisation is drawn, not hidden.** V15 keeps a "MODEL" frame with an assumptions line, labels streamlines "schematic" (they are potential flow past an ellipse, not CFD), and keeps limb motion within ±2.6°/±4° so the picture never implies a posture change the model does not have.

### 9.3 The six-way taxonomy (every number and every drawing falls in exactly one primary class)

| Class | Definition | On-screen treatment (PROPOSED) | V15 example (verified) | Where recorded |
|---|---|---|---|---|
| **Calculated** | Computed from the model or a cited formula with stated inputs | Plain label; live readout allowed | Drag arrow length, bar heights, needle, graph point, density dot count (`state(tm)`) | `CLAIMS.csv` + model self-check |
| **Simplified** | A real mechanism drawn with fewer terms than reality | "MODEL" frame / "schematic" tag | Fixed posture (constant CdA); streamlines as potential flow, labelled "schematic" | `SCALES.py` + assumptions line |
| **Magnified** | A true quantity drawn larger than true scale so it can be seen | Visible badge "×N" on the object, once | Net force ×8 (lens rim badge and arrow label) | `SCALES.py` |
| **Time-compressed** | Real duration shown shorter | "time compressed" tag, or a live clock | 150 model s shown in about 57 design s; equal-time trail "one mark every 10 s, one scale" | `TIME_MAP.py` |
| **Artistic** | Not a measured value: decoration or staging | No tag if it carries no claim; never place a number on it | Terrain, farmsteads, tree crowns, clouds, character | `CLAIMS.csv` "artistic: no claim" |
| **Assumed** | A value *chosen* because the real one is unknown or variable | Said aloud or on the MODEL line; never presented as measured | m = 80 kg, CdA = 0.50 m², start from rest at 10 km | `CLAIMS.csv` + model header |

Two rules: (a) **a drawing may carry only one class at a time per object**; a magnified *and* time-compressed arrow has two disclosures and probably wants splitting; (b) **artistic content must not carry data**: a cloud's speed must not encode wind speed unless it is calculated.

### 9.4 The verification checklist (run for every film; each row needs a result and an evidence path)

`CLAIMS.csv` columns (PROPOSED): `claim_id, where (script phrase / shot), value, unit, class (calculated|simplified|magnified|time-compressed|artistic|assumed), source (URL + access date, or derivation), recomputed (y/n, by what), tolerance, time_sensitive (y/n + recheck date), status (open|checked|owner-approved), notes`.

| # | Check | How |
|---|---|---|
| 1 | Every number **said** is in the ledger with a source | Script → ledger diff |
| 2 | Every number **shown** is in the ledger | Frame OCR/grep of labels vs ledger |
| 3 | Units stated and consistent (SI in the model, conventional units for the viewer) | Read the model header |
| 4 | **Independently recomputed** by a second route (closed form vs integration; or a second person) | Script |
| 5 | Limiting cases and sign checks pass (v ≥ 0, ρ > 0, energy sense) | `check.py` |
| 6 | Source date and **time-sensitivity** (current-event claims) rechecked on release day | Ledger column |
| 7 | To-scale vs not-to-scale declared for every diagram; "not to scale" badge where needed | `SCALES.py` |
| 8 | Magnification declared once; no stacked magnification | `SCALES.py` |
| 9 | Caption/voice wording equals the ledger wording (no "twice as" when the model says 1.4×) | Diff |
| 10 | **Assumed** values said aloud or shown; no assumed value presented as measured | Ledger class column |
| 11 | Colour meaning consistent across the whole film | Grep for hex |
| 12 | A viewer who sees only the picture would draw the same conclusion as one who hears only the voice | Human review (§17) |

**Status of this audit's own number checks.** In this audit I recomputed, from the constants G = 6.674×10⁻¹¹, c = 299,792,458 m/s, standard planetary and lunar parameters and the script assumptions, the headline numbers of the nine remaining scripts; every one reproduced the figures given in the research pass (listed in §9.5). I did **not** independently re-verify the *inputs* (e.g. Phobos GM and radius, lunar distances, Guinness's 3,596 km) against their primary sources, nor the time-sensitive NASA statements; those stay `open` in the ledger until checked.

### 9.5 Generalising the engine to the remaining scripts

Each domain below lists the state variables, the formula, the visual primitive, the **scale trap**, and the numbers recomputed in this audit. *Script risk* flags are from the research pass (§15).

**Atmosphere and falling bodies (Slots 01, 02).** State: `h, v, ρ(h), g(h), M(h)`. Model: `m·dv/dt = m·g(h) − ½ρ(h)v²CdA`; US Standard Atmosphere 1976 for ρ(h) beyond the troposphere fit used in V15; Mach from a(T(h)). Primitive: V15's force bars, lens, speed graph, altitude ruler. Trap: a 5.6-decade height ladder (1 m to 400 km) needs a log ruler; peak speed and landing speed are different quantities on one HUD. Recomputed: g at 400 km is 88.5% of surface g (an 11.5% drop); a vacuum fall from 400 km to 100 km takes about **4.35 min** and reaches about **8,404 km/h** (the script says "for four minutes" (recomputed 4.35 min) and 8,400 km/h). Script risk: constant drag to about Mach 3 is an assumption; "twenty g, thousands of degrees" is flagged by the script itself, but "about five g" at 100 km is stated flatly; 204 vs ~190 km/h differ across drafts.

**Light-time (Slots 03, 06, 07).** `t = d/c`. Recomputed: light-day = **2.590×10¹⁰ km = 173.1 AU**; the Moon is **1.282 s** one way; round trip **2.564 s** mean (perigee 356,400 km → **2.378 s**, apogee 406,700 km → **2.713 s**); **1 mm of range ≈ 6.7 ps** of round-trip time. Primitive: a pulse riding a ruler; a clock; a two-leg arrow with a processing block. Trap: Moon-to-Voyager is about **67,000:1**; use a light-time ruler (1.3 s, 8.3 min, about 4 h, 24 h), not kilometres, and no literal to-scale trail. Script risk: NASA's "one light-day" wording and date, whether the spacecraft is returning data, the 2026 issue (time-sensitive; recheck on release day); "remarkable precision" must not become a single-shot precision claim.

**Orbits on a small body (Slots 04, 05, 10).** Uniform sphere: circular surface speed `v_c = R·√(4πGρ/3)`, period `T = 2π/√(4πGρ/3)` (independent of R), `v_esc = √2·v_c`, `g = G·M/R²`. Recomputed for R = 3 km, ρ = 2,000 kg/m³: `v_c = 2.243 m/s` (8.08 km/h), `T = 8,403 s ≈ 140.0 min`, `v_esc = 3.172 m/s`, `g = 1.68×10⁻³ m/s²`. For Phobos (GM = 0.0007087 km³/s², R = 11.08 km): `v_esc = 11.31 m/s`, `v_c = 8.00 m/s`, `g = 5.77×10⁻³ m/s²`. For Slot 10: 2R_moon = 3,474.8 km, and Guinness's 3,596 km implies an orbital altitude about **121 km**. Primitive: orbit renderer, inset with a magnified contact point, range circle. Trap: a person is 1:1,760 of a 3 km radius, about 0.5 px on a 900-px world, so use a two-view scheme; the lap is 140 min, compressed with a clock. Script risk: an isolated-sphere escape speed overstates escape at the tidally weak sub-/anti-Mars points on Phobos; the launch is granted, never shown; Guinness's method is unexplained; the Artemis II record needs a release-day check.

**Tides (Slots 08, 09).** Differential acceleration `a ≈ 2GMR/d³`. Recomputed: Sun **5.05×10⁻⁷ m/s²**, Moon **1.10×10⁻⁶ m/s²**, ratio **0.459** (NASA's "a little under half"); direct pull ratio **179**; Sun's pull at Earth **5.93 mm/s²**, Moon's **0.0332 mm/s²**. Primitive: near/far arrows, "subtract the shared part", a basin and a wave, spring-neap from lunar phase. Trap: the two arrows differ by about 10⁻⁴ (Sun) to 3×10⁻² (Moon) of their length, so draw it as an animation of subtraction, not to scale, with a "not to scale" badge; a 0.5 m tide on a 12,742 km Earth means a bulge exaggerated by about 10⁷. **A force ratio is not a tide-height ratio.** Script risk: the transient adjustment time after the Moon vanishes is unknown; the two-bulge picture is something the script itself calls oversimplified.

**Scale (all).** Three scale tools: a **log ladder** (a ruler whose ticks are decades), a **broken-scale ruler** (one label per beat), and a **two-view inset** (overview plus a magnified contact area). Rules: one unit and one scale bar per sequence; if the scale is stylised, say so on screen; never combine a broken scale with a trail that implies true distance.

### 9.6 What would make a visual scientifically wrong even when the numbers are right

Colour reused for two meanings; an arrow whose length encodes two different things in two shots; a magnification applied to one object but not its comparison partner; time compression that changes the *order* of events; a label that appears before the voice says the noun; artistic detail that carries a number; a "model" panel that is hidden for the one shot where the assumption matters. Each is a human-review item in §17 as well as a code check.

## 10. Motion-design system

The picture is built from a small vocabulary of code-drawn primitives, each with one job, driven by the model state (§9) and timed to words (§11). This section lists the primitives that exist in V15, the rules that make them behave, and the rules for *removing* things, which is where V8–V11 failed hardest.

### 10.1 Primitive library (all verified in `v15.py` / `v15_shots.py`; function names are real)

| Primitive | Function(s) | What it does | Reuse note |
|---|---|---|---|
| Arrow | `arrow(c,x,y,dx,dy,h,w,head,dashed,double,dash_off)` | Solid, dashed (animated `dash_off = -t·18`) or double-shaft; head length capped at 60% of length | The one arrow for every force and velocity |
| Arrow reveal | `grow_arrow(c,x,y,L,h,g,…)` | Draws an arrow on like a pen stroke: length `L·ease_out(g)`, `g` in 0..1. The docstring says "trim path"; it is a length growth, not a true path trim | Use for every first appearance of a force |
| Force pair | `forces(c,cx,cy,dw,gw,gd,a,lab)` | Weight (constant length `L_W = 118` units) and drag (`L_W·D/W`) from the centre of mass, with chips labelled after the arrows exist | Generalise to any pair of opposed quantities |
| Velocity arrow | `vel_arrow(c,x,y,v,…)` | Dashed blue, own lane, length `8 + 0.75·v` | Velocity is never a solid force arrow |
| Lens (magnifier) | `magnifier(c,t,cx,cy,dw,open_,lx,ly,r=86,…)` | A circular lens with a leader to the real object, clipped content drawn at `ZOOM×`, a rim badge "×8" and an in-lens difference arrow | One lens per film, one magnification (§9.2) |
| Bars | `force_bars`, `bar_lens`, `compare_scene` | Two bars on one scale from one baseline, a "weight line" the second bar crosses; compare two figures at equal speed in different air | Comparison = same scale, one variable changes |
| Ruler | `alt_ruler(c,h,…)` | A vertical altitude ruler with a marker and ghost marks | Becomes the log ladder / light-time ruler (§9.5) |
| Graph | `speed_graph(c,t,t0,upto,…,axes,marks)` | Builds axes, zero line, curve to a time, labelled marks; "not zero" annotation | Draws on at the pace of the voice |
| Equal-time trail | `positions_demo`, `TRAIL_T = [10·i …]`, `TRAIL_SCALE = .085` units/m | One mark per 10 model seconds, one scale for every gap | The honest way to show changing speed |
| Air | `air_cause`, `air_lens`, `density_box`, `density_scene`, `air_streaks`, `passing_wisps`, `fg_air`, `airflow` | Marks whose **count ∝ ρ**, streamlines (potential flow past an ellipse), foreground motes | Density = dot count, not tint |
| Camera push | `push(c,fx,fy,z)` and `Cam` | A 2D push-in and a pinhole camera for parallax (§6.5) | Hard cuts by default; 1–2 pushes per film |
| Text | `text`, `chip`, `label`, `caption` | Helvetica Neue bold; `chip` = small quiet label (default 8.5 units); `label` = chip on a 82% white pill (10.5 units) | **System font dependency**: Helvetica Neue is a macOS font; a build on another OS needs a bundled font (§16, debt in §6.10) |
| Easing | `smooth`, `ease_out`, `ease_io`, `ramp(t,a,b)`, `wobble(t,f,seed,amp)` | Cubic and smoothstep ramps; `ramp` is the **window function**: 0 before `a`, 1 after `b` | Every reveal is `ramp()` between two film times taken from `beats.csv` |

**Size in pixels.** The design space is 360×640 units at **3 px per unit** (1080×1920). `chip` default 8.5 units ≈ **25.5 px**; `label` 10–10.5 units ≈ **30–31.5 px**; caption text 15 units = **45 px**. The V8 audit counted footers of about 30 px as a defect and V10's 22–25 px footnotes as an open issue; V15's smallest default (25.5 px) is below the former. **PROPOSED:** essential labels ≥ 30 px, secondary chips ≥ 24 px, verified on a phone (§17); V15 did not run that phone-size test on its chips.

### 10.2 Reveal rules (how things appear)

1. **Cause first, label second.** The object appears (a `ramp`), then its label (V15 `lab` argument reveals chips after the arrows exist). A label never precedes the thing it names.
2. **The word is the cue.** A reveal starts when the voice starts the noun or verb that names it (`NARRATION_VISUAL_SYNC_MAP.csv`: e.g. "stronger" → the drag bar passes the weight line; sentence end after "think" → the lens closes). Two **event anchors** pin reveals in V15's warp (§11.1). Corpus median: motion starts 33–56 ms after the word (§5.4); strict sync-map threshold PROPOSED: event within **−0.10 s / +0.30 s** of the word onset (V15 used the looser −0.30 s / +1.0 s after the key word ends).
3. **Easing is chosen by meaning.** `ease_out` for things that arrive and settle (arrows, lens opening); `ease_io` for camera and between-state moves; `smooth` for fades; **never linear and never one easing everywhere** (HumanCraft anti-generic table).
4. **One new idea per beat.** A beat adds one thing or replaces one thing. The V11 frames at 0:41 and 1:08 had everything on screen at once and drew the owner's complaint.
5. **Hard cuts over decorative transitions** (corpus: 100% hard cuts; HumanCraft: no default flash, glitch, shake, zoom or spin). V15's cuts are direct cuts and pushes tied to a motivation ("motivated close-up of the attached device").
6. **Hold for comprehension.** After a reveal, hold at least as long as it takes to read the label (about 0.3 s per word; §5.5) before the next change. V15's `P1` "pack still closed (held beat)" is the pattern.
7. **Replacement, not accumulation.** If something new needs the space, the old thing is removed by a stated rule, not left to fade. This is the text-budget rule below.

### 10.3 The text budget (the single biggest cause of cluttered frames)

V12 audited all **39 text items** in the V11 film and classified each: **REMOVE 13, TEMPORARY 8, REDUNDANT 6, ESSENTIAL 8 (3 as-is, 3 compressed, 2 reworded), REDUCED 2, OPTIONAL CAPTION 2** (`history/v12/TEXT_REDUCTION_AUDIT.csv`, columns `v11_text, where, class, v12_treatment`). Examples: the "UNREASONABLY EXACT" top-left on every shot → **REMOVE** (a small end mark only); the "MODEL · starts at rest · fixed posture" banner → **TEMPORARY** (shown once for 2 s); "speed: zero" → **REMOVE** because the absent speed arrow plus the still world already says it.

**Rules for the next films (derived from that audit and the V8 defect list):**

| Rule | Detail |
|---|---|
| Text is a last resort | If motion, position, scale or colour can say it, it must |
| **Class every text item** | Each label is `ESSENTIAL`, `TEMPORARY` (with a stated duration), `REDUNDANT` or `REMOVE`; only the first two ship. The audit file is a gate (§18 G5) |
| One number per beat | Matches the Shorts strategy (§15); V3's beat maps are label-heavy and need splitting |
| No headline on every shot | The V8 "slide deck" look: a two-line headline per shot |
| Assumptions as icons, not lists | A boxed list of assumptions is a text wall on a phone |
| Corner tags | One small category tag (SIMULATION / REAL DATA / THE MATH, proposed for Slot 01) rather than a banner |
| Captions are separate | Burned captions live in a separate overlay pass and a clean version without them is also exported (§13) |

### 10.4 Reusable scene recipes (all from V15; each lists its shot IDs)

| Recipe | What happens | V15 shot |
|---|---|---|
| **Cause and effect** | You move through still air → the camera locks onto you → the air streams past → the drag arrow grows. Drag appears *only after* the airflow is shown | `E1` |
| **Same-size comparison box** | Two equal boxes, thin vs dense air; then the same speed under each; dot count ∝ ρ | `G1`, `I1` |
| **One-variable compare** | Same air, same posture, speed ×2 → drag ×4 (live labels) with a ghost of the ×1 arrow | `J1` |
| **Crossing reveal** | Bars side by side on one scale from one baseline; the drag bar passes the weight line on the word "stronger" | `K1` |
| **Lens** | Magnify the small difference once, with a disclosed badge | `K1`–`Q2` |
| **Equal-time trail** | One mark every 10 s on one scale: gaps grow, then shrink, while every mark is lower | `L1` |
| **Graph that builds** | Axes, zero, rise, top speed, a fall that stays above zero ("not zero") | `Q1`, `S1` |
| **Motivated close-up** | The forearm lifts, the head turns to the wrist, the camera pushes toward the device; needle eases down | `B2`–`B3` |
| **Reaction** | "Wait, what?": head snaps up, blink, arm returns, quick push on the face | `C1` |
| **Reset / model frame** | The world freezes, a MODEL frame draws in, the altitude ruler appears | `F1`, `R1` |
| **Four-layer opening** | Aircraft upper-middle, figure below, parallax layers; no cloud wipe | `A1` |

**Shot tempo in V15:** 25 shots in 110.04 s, mean 4.4 s; in the V13 design timing (before the warp) shot lengths run from 1.11 s (`K2`) to 7.88 s (`K1`), computed from `SHOTS`. The corpus median *state* length is 3.0 s (§5.4); a V15 shot contains several states.

### 10.5 Colour, contrast and accessibility

- **One meaning per colour** (§9.1). The V15 palette is **not** the Okabe–Ito colour-blind-safe set (§5.5); whether orange `#DB7224`, teal `#2F7F7A`, blue `#2F5D8C` and violet `#7A4CC2` stay distinguishable under common colour-vision deficiencies **has not been tested** (**UNVERIFIED**). Mitigations already in the design: the velocity arrow is *dashed* (shape, not just colour) and the net-force arrow is *double-shafted*. PROPOSED test: render the arrow set through a deuteranopia/protanopia simulation and confirm dash/shaft cues survive.
- **Text contrast** target 4.5:1 for ordinary text, 3:1 for large text (WCAG, cited by HumanCraft); captions sit on an 88% white pill so they hold on any background.
- **Direct labelling** beats legends (§5.5).

### 10.6 Checks that belong to the motion layer

`tools/v15.py --check` asserts structural invariants (warp monotone, all shots appear, minimum altitude); `frame_strips.py` builds six-frame strips per shot (35 strips in V15); `caption_qa.py` counts science-graphic pixels under every caption box (§13); a *muted* contact sheet (`qa/muted_sheet_1.png`, `_2.png`) proves the picture works without sound. None of them substitutes for watching it at phone size (§17).

## 11. Human narration-first production

### 11.1 What actually happened in V15 (verified)

Hamza recorded the script himself. The earlier film versions (up to V13) had been timed to a **different narration** (`history/v13/narration16k.wav`, `history/v13/narration_words.json`; see §4 for what it was). V14 swapped in Hamza's recording; V15 kept that timing. The swap was done **without time-stretching the video as a whole**: shot code written in V13's 78.2 s "design time" is replayed through a time warp built from word matches (§6.3, `tools/align_v14.py`). This was a recovery technique for a late narration change. The reusable lesson is the opposite: **record first, then design on the real timing.**

Pipeline, with the file that does each step:

| # | Step | Tool / file | Verified detail |
|---|---|---|---|
| 1 | **Inspect the raw take** | `HAMZA_VOICEOVER_RAW.mp3` (125.16 s, 48 kHz mono, 320 kb/s, kept untouched) | SHA-256 `edd24139…c82f` (re-verified 2026-11-25) |
| 2 | **Find recording-setup material** | whisper.cpp on the first seconds, written to `qa/asr/preroll.txt` | 0.33–7.97 s is setup talk ("I will do a video recording here … Start the video."); 7.97–10.24 s is digital silence (≈ −134 dB RMS); first script word "You're" at **10.24 s** |
| 3 | **Cut to the true onset** | `tools/prepare_voice.py`: energy voice-activity (10 ms hop, −60 dBFS threshold, gaps < 0.25 s stay inside a run), `PRE_END = 9.0 s`, `LEAD = 0.10 s` | cut at **10.14 s** raw; `PRE_END` is a safe parameter inside the silence, *chosen after* the transcript showed where the setup talk ended |
| 4 | **Natural pause editing** | same script: each pause longer than `CAP = 1.5 s` loses the middle of its silence | 8 pauses shortened, **3.56 s** removed; pauses ≤ 1.5 s untouched ("Wait, what?" and "Think about that." keep Hamza's own beats); longest (about 2.5–2.6 s between voiced runs after "…start to decrease."; `HUMAN_VOICE_TRANSCRIPT.md` says 2.67 s) capped to 1.5 s. No time-stretch, no pitch change, no word removed. Edit list: `audio/voice_edit.csv` (9 keep-segments) |
| 5 | **Voice cleanup** | ffmpeg chain in `prepare_voice.py`: `highpass=f=70, deesser=i=0.25, acompressor=threshold=-24dB:ratio=2:attack=10:release=120`, one linear gain to **−18 LUFS**, `alimiter=limit=0.708` (−3 dBFS) | No noise reduction (gaps are digital silence). Clean file: 108.70 s, 48 kHz, 24-bit, −18.5 LUFS, TP −2.1 dBFS |
| 6 | **Transcription** | `whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/clean16k.wav -ml 1 -sow -ojf -of qa/asr/clean_words --dtw small.en -l en -np` (in `tools/build_v15.sh`, `--from-voice` branch) | Decoded twice (greedy and beam 5): word-for-word identical. **202 words.** Two ASR decodes agreeing is not a listening check. |
| 7 | **Word-level alignment** | `tools/align_v14.py` `load_words()` + `vad()` + `snap()` | whisper.cpp DTW word spans are snapped to voiced audio: a word's start moves to a voiced run that begins inside its span (DTW spans absorb the pause before them); its end is clipped to the voiced run. Output `WORD_LEVEL_TIMESTAMPS.json`: film / clean / raw time for every word, plus `loud_db`, `stretch` and an **emphasis estimate** (35 of 202 words flagged; an estimate, not a listening judgement) |
| 8 | **Phrase segmentation** | `split()` in `align_v14.py` | Sentences split at `, . ?`, then any phrase > 40 chars is split near its middle, penalising a split after a weak word (`a, the, your, to, …`); a one-word fragment merges with the next phrase if ≤ 40 chars and < 0.5 s apart; `NO_SPLIT` protects "Slowing down doesn't mean you have stopped falling." → **46 caption cues, 28 sentences, 45 pauses ≥ 0.25 s** (`audio/narration_v14.json`) |
| 9 | **Retiming the picture** | `align_v14.py` anchors | `difflib.SequenceMatcher` aligns Hamza's words to the V13 narration; one anchor per phrase (first-word onset); two **event anchors** pin reveals to the word that names them (`stronger` → drag bar passes weight line; sentence end after `think` → lens closes); PCHIP monotone cubic; rate window 0.34–1.6; **44 anchors**. No global stretch. |
| 10 | **Captions** | cues from step 8; display lead 0.05 s, hold 0.25 s after speech, min 0.9 s, never overlapping | 46 cues → SRT + burned overlay (§13) |
| 11 | **Narration-driven reactions and sound** | `SHOTS` + `ramp()` windows in `v15_shots.py`; `CUES` in `mix_v15.py` via `unwarp()` | e.g. forearm lift 0.39 s before "somehow"; wrist cut 0.56 s after "slowing" starts; head snap on "Wait, what?" (`NARRATION_VISUAL_SYNC_MAP.csv`) |
| 12 | **Verify** | `tools/sync_map_v15.py` | 34 narration→visual events checked; status `ok` unless the event is > 0.30 s before the phrase starts or > 1.0 s after the key word ends. **All 34 `ok`.** Event times come from `unwarp(design_time)` in `sync_map_v15.py`; nothing is detected in rendered frames, so `ok` is a loose scheduling check (offsets up to −0.88 s inside the window). The 3 ms figure compares MP4 audio with the voice stem (audio against audio). |

**Honest limits.** (a) Nobody has *listened* to the transcript against the recording (the V15 author had no audio output; `HUMAN_VOICE_TRANSCRIPT.md` says so). (b) The `ok` thresholds are deliberately loose: a row can be `ok` with the event 1.45 s before its key word, as long as it is inside the phrase (see row "ground." in the sync map). Tighten them per project (§17). (c) The voice receives **two** compression stages (2:1 at −24 dB in `prepare_voice.py`, then 2:1 at −22 dB in `mix_v15.py`) and the 70 Hz high-pass twice. Probably harmless at 2:1, but it is an accident of history, not a design; the next pipeline should have one voice chain.

### 11.2 The reusable process: build every video around the final human narration

**Principle.** The narration is the master clock. Picture, captions and sound are *derived* from word-level timing; nothing is stretched to catch up with the voice.

| Phase | Output | Gate to leave the phase |
|---|---|---|
| N0 Script lock | `script/SCRIPT_FINAL.md` with **beat markers** (`[B07: drag arrow grows]`) at every moment that needs a picture event | Owner approval; every number in the script traced to `research/CLAIMS.csv` |
| N1 Record | Raw take(s), unedited, in `narration/raw/` (never overwritten). Record **room tone for 10 s** and a **clap or tone** at the start for sync. Read the script once, in order; re-record a sentence rather than fix it later | Raw file SHA-256 recorded in `narration/MANIFEST.md` |
| N2 Inspect | `narration/INSPECTION.md`: duration, sample rate, peak, noise floor, clipping count, pre-roll transcript, true onset, pauses > 1.5 s, mouth-click / plosive spots noted *by listening* | A **human listens** to the whole take once with the script and marks retakes (this is the step V15 could not do) |
| N3 Edit | `narration/clean.wav` + `voice_edit.csv` (raw→clean map) using the V15 rules: remove setup, cap long pauses at a configurable length, never remove words, never time-stretch | Edit list reviewed; listening pass on every cut point |
| N4 Transcribe & align | `words.json` (film/clean/raw time per word), `phrases.json`, `sentences.json`, `pauses.json` | Two ASR decodes agree; any disagreement resolved against the script and by ear; homophone fixes recorded in a `SPELL` table |
| N5 **Beat map** | `timeline/beats.csv`: for every beat marker: key word, word start/end, planned visual event, **event offset policy** (on-word, 0.1 s before, after pause…) | Every beat has a word anchor; no beat shorter than one reveal |
| N6 Design | Storyboard and shot code written **in film time on this timing** (frame = round(t × fps)) | Storyboard reviewed against `beats.csv` before any animation |
| N7 Animate / mix / caption | As §14 | Sync map generated automatically (`sync_map`) with strict thresholds |
| N8 Late change protocol | If the narration is re-recorded: re-run N3–N5, then **re-time with anchors**, not global stretch (V15's `warp.json` method), and re-run the sync map | Rate window respected (`0.6–1.5` recommended for tighter shots); ambient motion on real time |

**Why avoid global stretching.** A uniform stretch changes everything at once (motion speeds, ease durations, sound pitch if audio follows), and drifts against the words. Anchor-based warping keeps every shot on its word; ambient motion on the real clock keeps stretched beats alive. The cost is a rate window: V15's script limits each segment's *average* rate to 0.34–1.6 design-seconds per film-second, and the measured result (this audit, evaluating `warp()` at all 2,641 frames) is an instantaneous rate of **0.26–1.40, median 0.68**, i.e. the picture was designed for a narration about 41 % faster than Hamza's (78.2 s design → 110.04 s film). That is wide. A narration-first design never needs the warp.

**Pause policy.** Cap pauses (V15: 1.5 s) only after the owner has agreed a rhythm; keep dramatic pauses ("Wait, what?") by using the cap as a ceiling rather than a rule. Where the picture needs time to land a reveal, ask the narrator for a pause at **record** time (a beat marker `[PAUSE 1.0]`) instead of inserting silence later.

**Narration-driven character reactions.** Put reaction onsets on the *end* of the triggering word or the following breath (V15: head snap on "Wait, what?" start; forearm lift on "somehow"). Reactions should lead slightly rather than follow: viewers perceive visual-before-audio as natural (§5, sync note on A/V offsets).

## 12. Professional sound-design system

### 12.1 V15 audio, in one table

All values read from `tools/mix_v15.py` and `tools/prepare_voice.py`. The mix is numpy + ffmpeg at 48 kHz, 24-bit PCM stems.

| Layer | What it is | Processing | Level |
|---|---|---|---|
| **VOICEOVER** | Hamza's clean narration (`HAMZA_VOICEOVER_CLEAN.wav`) | Prep: 70 Hz high-pass, de-esser `i=0.25`, 2:1 compressor above −24 dB (10 ms / 120 ms), gain to −18 LUFS, −3 dBFS limiter. Mix: 70 Hz high-pass, 2:1 above −22 dB (15 ms / 250 ms) "gentle levelling". No EQ, no noise reduction (gaps are digital silence) | 0 dB reference; −24.3 LUFS as a stem |
| **AMBIENCE** | Generated wind bed + distant aircraft + three gusts | Brown noise 90 Hz–700 Hz (+6 dB) mixed with pink noise 700 Hz–3.5 kHz (−18 dB, tremolo 0.17 Hz depth 0.35); `apulsator` 0.07 Hz; **−6 dB dip at 2.5 kHz** (`equalizer`) to stay out of the consonant region; intensity keyed by `WIND_KEYS` to the *fall* (near-silent at the model "rest" frame); aircraft hum = brown noise low-passed 320 Hz + 88 Hz and 176.5 Hz sines | wind −15 dB × envelope; aircraft −14 dB |
| **FOLEY** | Suit flutter, sleeve + strap, wrist ticks, needle ratchet, head snap, pack flutter (9 cues) | Band-limited noise × irregular flapping envelope; 3 ms noise touch on ticks | −31 to −36 dB peak |
| **TRANSITIONS** | Camera tilts and moves (7 cues) | STFT noise-sweep "whoosh": band centre glides f0 → f1 → f2 | −30 to −36 dB peak |
| **SCIENCE_FX** | 5 soft reveal accents: weight (G4), drag (C5), net force (E5), graph (D5), ending (G3) | Mallet-style partial tones with exponential decay | −31 to −35 dB peak |
| *(review only)* **LIBRARY_REVIEW** | 4 library clips | Same ducking | −30 to −38 dB; never in the publication master |

**Cue sheet.** `SOUND_DESIGN_CUE_SHEET.csv` lists every sound: stem, cue, start/end, V13 design time, picture event, level, pan, source, rights. 31 rows: 1 voice, 24 generated cues, 2 beds, 4 library-review. Each cue is tied to a **picture event** and placed at the frame where that event is drawn (`unwarp(design_time)`), so sound follows picture whatever the narration timing.

**No music.** The V15 film has no music stem (verified in `START_HERE.md` and the stem list).

### 12.2 Dialogue-first mixing: ducking, carving, masking

**Frequency masking.** Voice intelligibility lives in roughly 1–4 kHz; a bed with energy there competes with consonants even when it is quiet. V15 treats this twice:

1. *Static:* the wind bed is high-passed, low-passed and given a −6 dB dip at 2.5 kHz.
2. *Dynamic:* `carve(x, depth_db, carve_db=-6, lo=1000, hi=4500)` splits each non-voice stem into a speech band (FFT band-pass 1–4.5 kHz) and the rest, then multiplies the *rest* by the duck gain `g` and the *speech band* by `g × carve`.

```python
def carve(x, depth_db, carve_db=-6.0, lo=1000.0, hi=4500.0):
    """Duck a stem under speech by depth_db and cut its speech band (lo..hi) a further carve_db while Hamza talks."""
    ...
    g  = 1 - (1 - db(depth_db)) * SPEECH            # SPEECH = 1 inside phrases, 0 in pauses
    gb = g * (1 - (1 - db(carve_db)) * SPEECH)
    return rest * g[:, None] + bandp * gb[:, None]
```

Depths: **ambience −12 dB, effects −9 dB**, plus the −6 dB speech-band carve.

**"Sidechain" without a compressor.** `speech_curve()` builds the ducking envelope from the *known phrase times* (`audio/narration_v14.json`), not from the audio. It is 1 inside each phrase and 0 in pauses, with raised-cosine ramps (0.22 s lead-in **before** the first word, 0.38 s release **after** the last). Advantages: deterministic, look-ahead for free (the duck starts before the voice does), intended to avoid pumping on breaths (not measured: 20 of the 45 inter-cue gaps are under 0.6 s, so the bed reopens only partly there). Limitation: it depends on correct phrase timing; if the voice changes, rebuild alignment first. A conventional sidechain compressor (`ffmpeg sidechaincompress`: `threshold`, `ratio`, `attack`, `release`, `makeup`, `knee`) is the alternative when timing data is not available.

**Why the release matters.** V14 used linear 0.18 s ramps and returned the bed quickly; the longer release is intended to keep rising noise from covering word endings (not measured, and no one has listened). V15's slower raised-cosine release (0.38 s) protects trailing consonants ("net force", "decrease" were on the owner's listening list).

**Foley, ambience, transitions, reveals: roles.**

| Layer | Purpose | Rule used in V15 |
|---|---|---|
| Ambience | Place and speed (relative air follows the fall) | Continuous, ducked hardest; near-silent at the "rest" model reset so silence signals the model world |
| Foley | Material truth for visible objects (cloth, strap, dial) | One sound per *visible* action; tick on the cut to the wrist, ratchet as the needle moves |
| Transitions | Make a camera move feel physical | Whoosh length = move length (1.1 s tilt = 1.1 s whoosh) |
| Science reveals | Mark the 5 ideas that matter | Reduced from 11 plucks (V14: almost every arrow) to 5 (weight, drag, net force, graph, ending). A reveal sound on everything means none is a reveal |

### 12.3 Mastering

```python
def master(stems, out_path):
    mix = sum(stems.values()); write(tmp, mix)
    g = -16.0 - lufs(tmp)                                   # loudnorm measurement, then one linear gain
    ffmpeg -af "volume={g}dB,alimiter=limit=0.84:level=false:attack=3:release=80"  -c:a pcm_s24le
```

Result, independently re-measured on the final MP4 on 2026-11-25 (`ffmpeg -af ebur128=peak=true`): **−16.0 LUFS integrated, LRA 3.4 LU, true peak −1.5 dBFS** [M]. The AAC encode is 192 kbps, 48 kHz.

*Open question for the owner:* −16 LUFS was chosen in the V9 brief and is common for mobile-first delivery, but YouTube's own normalisation reference should be confirmed against its current help page before standardising (§12.7).

### 12.4 The V14 → V15 improvement, and why it matters

| Measurement (voiced 0.4 s windows, 50 % overlap, n = 302) | V14 | V15 |
|---|---|---|
| Voice − background, broadband, **median** | 10.5 dB | **20.7 dB** |
| Same, weakest 10 % (p10) | 5.2 dB | **17.1 dB** |
| Worst single window | −6.8 dB | +5.8 dB |
| Speech band (300 Hz–4 kHz) median / p10 | 14.1 / 6.5 dB | **24.8 / 19.0 dB** |
| Voice stem − summed background (integrated) | 8.6 LU | 15.4 LU |
| Master integrated loudness | −16.0 LUFS | −16.0 LUFS |

*Provenance of the numbers:* V14 values are as recorded in `AUDIO_MIX_QA.md` and `qa/audio_qa.json` (V14 stems no longer exist, so they cannot be re-measured). **V15 values were re-computed by this audit** by running a scratch copy of `tools/audio_qa.py` against `audio/stems/` and `audio/V15_mix.wav`, giving median 20.7, p10 17.1, min 5.8, speech-band median 24.8 and p10 19.0 dB (identical to the recorded values) [M]. V14 and V15 both measure −16.0 LUFS.

**Why the numbers matter.** (1) They show the mechanism behind the owner's complaint: V14's wind bed was set at −5 dB × envelope (V15: −15 dB) with only 4.5–7 dB of ducking and no speech-band treatment, so in the weakest 10 % of windows the voice was only ≈ 5 dB above the summed background. A small speech-to-background ratio is where listening effort rises sharply (a general finding in the speech-in-noise literature; not tested on this film), and phone speakers tend to lose low-level consonants first **[I]**. (2) Integrated loudness alone cannot reveal this: both versions are −16 LUFS. (3) The weakest-window list is a *work list for listening*, not a verdict: V15's two weakest speech-band windows (93.1 s and 76.2 s, ≈ 0 dB) are breaths where the voice itself is at −52/−48 dBFS, and the weakest window containing real speech energy is +6.3 dB at 62.8 s.

**What the numbers cannot tell you.** They measure level ratios on isolated stems. They do not capture perceptual masking by the *shape* of the bed, intelligibility on a phone speaker, the voice's naturalness after processing, or whether a sound is *annoying*. **No human has listened to V15.** The measurement proves the V14 defect's mechanism was addressed; it does not prove the owner will accept the mix. Treat the target ("median ≥ 20 dB, p10 ≥ 15 dB") as a *screening threshold* (§17) and keep the listening gate.

### 12.5 Reusable sound categories

A single taxonomy for generated and library sounds (use it in the SFX ledger, filenames and cue sheets):

| Code | Category | Examples in V15 | Role | V15 level (PROPOSED where V15 has no such cue) |
|---|---|---|---|---|
| `AMB` | Ambience / beds | wind bed, aircraft | Place, speed | −35 to −40 LUFS stem; ducked 12 dB |
| `FOL` | Foley (object / body) | cloth flutter, strap, tick, ratchet | Material truth | −31 to −36 dB peak |
| `TRN` | Transitions / camera | whoosh, swell, air gust | Camera physics | −30 to −36 dB peak |
| `SCI` | Science reveals / accents | weight, drag, net-force tones | Mark a concept | −31 to −35 dB peak; ≤ 5 per Short |
| `IMP` | Impacts, hits | none in V15 | Emphasis (use sparingly) | −30 dB peak (PROPOSED) |
| `RIS` | Risers / reverses | `reset swell` | Anticipation | −33 dB peak (PROPOSED) |
| `MUS` | Music | none | Mood (needs a licence record) | ≤ −24 dB under voice (PROPOSED, UNVERIFIED) |
| `VOX` | Vocals / memes | none | — | avoid |

**Naming:** `<CAT>_<object>_<variant>_<source>_<ID>.wav`, e.g. `FOL_suit-flutter_a_gen_0004.wav`. **Generated vs library:** generated sounds carry rights `Generated (tools/…)`; library sounds carry a licence-ledger row (§12.6).

### 12.6 SFX library audit

Two separate collections exist, and **neither is cleared for a monetized channel**.

**A. "SFX Library" (83 clips used in V9–V13 review mixes).** Listed in `SFX_LICENCE_MANIFEST.csv` (111 lines: header + 83 library + 26 generated + 1 owner recording). All 83 library rows read `UNKNOWN: library README states licensing/ownership was not established`; each clip's origin is "Extracted from supplied video AQMEykx9… (time range)", i.e. cut from supplied third-party videos (the README says 83 clips from 16 videos; ownership not established). Categories: Cinematic Hits and Impacts 15, Foley and Objects 14, Risers and Reverses 14, Bells Rhythms and Music 12, Whooshes and Transitions 11, Nature and Ambience 6, Magic and Sparkles 4, Glitches Drones and Textures 4, Vocals and Memes 3. A copy of the library exists as `~/Downloads/SFX Library.zip` (47 MB); four clips used in the V15 *review* mix are copied to `audio/library_review/`. **Decision (already enforced in V15): none in the publication master.**

**B. `SOUND EFFECT.zip` / `~/workprojects/SOUND EFFECT/` (234 zip entries, 106 audio/video files, 342 MB).** Contents (listing only; no clip was used or opened for this audit): "00-TENET Inspired Free Giveaway", "BLADE RUNNER 2049 FREE SOUNDS" (incl. "From Solaris SFX Library"), "CinePacks Sfx SAMPLE", two complete music tracks ("Death of a Bluebird – Rorschach Roy", "Synthwave goose – Blade Runner 2049"), and "personal sfx" containing files named `ES_… – SFX Producer.mp3` and "…[No Copyright Music]…". There is **no licence file**; the only text file is a reseller promo ("Explore more FREE Resources… Telegram … WhatsApp") that points to freebie channels. My assessment **[I]**: this is a bundle of freebies re-uploaded by third parties with unknown or non-transferable terms, and the `ES_` prefix suggests Epidemic Sound downloads, whose licence is tied to a subscription and a connected channel. **Treat the whole bundle as unusable for publication until each file's origin and licence are documented.** Reference-listening only.

**Rights-clear alternatives (verified 2026-11-25 by the tooling research; links in §20):**

| Source | Terms | Monetized YouTube | Attribution |
|---|---|---|---|
| **Generated in code** (`tools/mix_v15.py`) | Own work | Safe | None |
| Freesound **CC0** | No restrictions | Safe | None |
| Freesound **CC-BY** | Commercial use with credit | Safe with credit | Title, author, URL, licence, "changed" note |
| Freesound **CC-BY-NC** / Sampling+ | Non-commercial | **Do not use** | n/a |
| YouTube Audio Library | For YouTube use, Partner Program allowed; CC tracks need description credit | Safe on YouTube | Only for CC-tagged tracks |
| Pixabay (licence page; the 20 Oct 2026 update date is UNVERIFIED) | Free use incl. commercial, no attribution; no standalone redistribution | Allowed (Content ID not addressed) | Not required |
| Sonniss GameAudioGDC | Royalty-free, commercial, "YouTube videos you monetize"; no standalone redistribution; no AI/ML training | Safe | Not required |
| ZapSplat | Primary page unreachable (403): **UNVERIFIED**; secondary sources say commercial use allowed with attribution on free accounts | Probably, with credit | Credit if free tier |
| BBC Sound Effects (RemArc) | **UNVERIFIED** primary text; secondary quotes say non-commercial only | **Do not use** for monetized videos without a paid licence | — |
| Unlabelled "free sample packs" | Unknown | **Do not use** | — |

**Licence ledger (required for every non-generated asset):** `asset_id, file, sha256, source_url, author, licence_name_and_version, licence_page_saved_as, download_date, attribution_text, used_in_video, notes`. Reject anything marked NC at intake. None of this is legal advice.

### 12.7 Standard sound workflow for future films

1. **Spotting session** (after storyboard, before animation): list which visible actions get Foley, which camera moves get a transition, which ≤ 5 ideas get a science accent, and where silence is deliberate. Output: `audio/SPOTTING.csv` (event id, picture event, category code, planned level, source plan).
2. **Narration first**: voice processing chain defined once (HPF, de-ess, 2:1 levelling, target stem loudness) in `audio/voice_chain.json` and not re-applied downstream.
3. **Generate or source** sounds against the ledger; generated first.
4. **Rough mix with the animatic** (G2 in §18), not at the end: this is the "late audio integration" fix.
5. **Measure** with `audio_qa` (target: median voice-minus-background ≥ 20 dB, p10 ≥ 15 dB, no voiced window below +5 dB broadband, and every window under +6 dB listed with its cause; V15's minimum is +5.8 dB, and its two speech-band windows near 0 dB are breaths), loudness (−16 LUFS ±0.5 unless the owner sets another target; true peak ≤ −1.5 dBFS), A/V sync (cross-correlation ≤ 20 ms).
6. **Human listening gate** on three playbacks: headphones at normal level; a phone speaker; the phone at 20 % volume. The reviewer fills `qa/LISTENING_REVIEW.md`. **Automated measurements never close this gate.**
7. **Remove** any reveal sound that does not mark one of the five ideas.

## 13. Caption production system

### 13.1 What V15 does (verified; measured on the shipped files in this audit)

| Stage | Implementation | Evidence |
|---|---|---|
| Human narration transcription | whisper.cpp `ggml-small.en`, decoded twice (greedy and beam 5), **word-for-word identical**; 202 words | `qa/asr/`, §11.1 |
| Word-accurate timing | DTW word spans **snapped to voiced audio** (voice-activity detection on a 10 ms hop; threshold 30 dB below the 95th-percentile frame level in `vad()`) | `tools/align_v14.py` `snap()`, `WORD_LEVEL_TIMESTAMPS.json` |
| Natural phrase segmentation | `split()`: split at `, . ?`; any phrase > 40 chars is split near its middle, penalising a split after a weak word (`a, the, your, to…`); a one-word fragment merges with its neighbour if ≤ 40 chars and < 0.5 s apart; `NO_SPLIT` protects "Slowing down doesn't mean you have stopped falling." | **46 cues**, 28 sentences |
| Cue timing | display lead 0.05 s, hold 0.25 s after speech, minimum 0.9 s, **never overlapping** | **Measured on the shipped SRT:** min cue 0.90 s, max 3.00 s, 0 overlaps (min gap 0.0 s) |
| Line layout (burned) | `caption()` in `v15.py`: one cue = one phrase; if > 24 chars, **two balanced lines** chosen to minimise the longer line (≤ 27 chars each) instead of greedy wrapping | `tools/v15.py` lines 101–119 |
| Styling | Helvetica Neue bold 15 design units = **45 px** at 1080×1920; ink `#2A2B27` on a **white pill at 88% opacity**, corner radius 5 units, 0.08 s fade-in/out | `caption()` |
| Position | `CAPTION_Y = 536` units (baseline of a one-line caption; two lines go up by 19 units per extra line). Raised **126 px (42 units)** from V14's 578. Resulting **box bottom 1,626 px, 294 px clear** at the bottom; V14's was 1,752 px (168 px clear) | `qa/caption_qa.csv`, `FINAL_PRODUCTION_QA.md` |
| Collision check | `tools/caption_qa.py`: for every cue it samples **start / middle / end** (46 × 3 = 138), renders the picture and the caption overlay, dilates the caption boxes by 6 px, and counts picture pixels inside that zone that are **weight orange, drag teal, net-force violet or velocity blue** (colour distance < 38); `FLAG` if more than 40 | **0 flags / 138 samples**; min bottom margin 294 px |
| Exports | clean `SKYDIVER_SLOWDOWN_FINAL_V15.mp4` (no captions); burned `…_CAPTIONS.mp4`; sidecar `.srt`; caption overlay rendered as a separate transparent MOV (`qa/caption_overlay.mov`) | files present; both MP4s 1080×1920, 24 fps, 110.04 s |
| SRT | 46 cues, one line each | **Measured:** max **17.4 chars/s** (median 13.2), **0 cues above 20 chars/s**; longest cue **51 chars** (the protected sentence; above Netflix's 42 per line, which is why the burned version wraps it in two lines of ≤ 27) |

**Honest limits of V15's caption system** (these matter more than the successes):

1. **"Dynamic" collision avoidance is not dynamic.** The caption sits at a fixed baseline. A `CAPTION_TOP` set exists so that named shot kinds could move the caption to the top (y = 70 units), but it is **empty** in V15: nothing ever moves. What exists is a *static* raised position plus a *post-hoc* check.
2. **The check protects only four colours.** It does not look for faces, the wrist dial, the text labels, graph axes or the aircraft. "Scientific diagram protection" is therefore partial: it protects the force arrows and bars, the things that collided in V14 (about 65 s) and V15 defect #15.
3. **No Shorts-UI check.** V8's ledger only said "keep UI regions clear"; the 294 px figure was chosen, not derived. The working safe area in §5.5 (x 48–888, **y 288–1248**) would put V15's captions (box 1,506–1,626 px) **outside** the conservative area; the third-party numbers are **UNVERIFIED**, but the right move is a phone test on an unlisted upload (§17), not an assumption either way.
4. **No colour-contrast or legibility measurement** beyond the 88% white pill.
5. **No human read-through of every cue against the recording** (§11.1 limit (a)).
6. The check runs `exec()` over `v15.py` (§6.10 debt): it is only as portable as the build.

### 13.2 The reusable caption system (PROPOSED standard built on the above)

**Inputs:** `narration/words.json` (film time per word, §11.2 N4), `phrases.json`.

**Cue construction rules.**

| Rule | Value | Basis |
|---|---|---|
| Cue unit | One phrase (≤ ~40 chars), never cross a sentence end without a break | V15 `split()` |
| Burned line length | **≤ 27 characters per line**, **2 lines maximum**, balanced (minimise the longer line) | V15; works with 45 px type in 1080 px |
| Sidecar line length | ≤ 42 characters per line, ≤ 2 lines (the protected sentence is the one exception to record) | Netflix (**V**) |
| Reading speed | ≤ 20 chars/s (V15 max 17.4); ≤ 17 for any child-directed film | Netflix (**V**) |
| Minimum / maximum duration | ≥ 0.9 s (V15) / ≤ 7 s (Netflix) | V15; Netflix (**V**) |
| Display lead / hold | start 0.05 s before the first word; end 0.25 s after the last | V15 |
| Overlap | none; cue *n+1* may start at the instant cue *n* ends | V15 |
| Break points | after punctuation; before conjunctions and prepositions; keep names and numbers with their units; avoid a 1–2 word top line | Netflix line-break rules (**V**) |
| Emphasis | highlight only meaningful words (the film has an emphasis estimate for 35/202 words; an estimate, not a listening judgement) | HumanCraft V3 §4; `WORD_LEVEL_TIMESTAMPS.json` |
| Spelling | every homophone fix recorded in a `SPELL` table | §11.2 N4 |
| Word chunks | for very fast narration, 2–4 word chunks follow speech (the corpus narrates at ~256 wpm; Hamza at ~112 wpm does not need it) | §5.5 |

**Safe-area rule.** Until verified on a phone, treat the caption box as needing to be **at or above y = 1248 px** (conservative) *and* run the V15 collision check. Where the V15 position (box bottom 1,626 px) is kept, the owner must accept the risk after a phone test. Decide **once per channel**, record it in `START_HERE.md`, and never change it per film without a test.

**Diagram protection (PROPOSED extension of `caption_qa.py`).** Replace the four-colour test with a **protection mask** that each shot declares: a list of regions or tagged draw calls that must stay clear (force arrows, bars, dial, face, labels, graph). The check renders the mask per sample and fails on any overlap, instead of guessing from colours. Add a *top position* fallback (`CAPTION_TOP` populated) for shots whose mask intersects the default box.

**Automatic checks (all PROPOSED unless stated):**

| Check | Pass condition |
|---|---|
| No overlapping cues; min 0.9 s; max ≤ 7 s | SRT lint (V15's cue stats were measured by hand in this audit) |
| chars/s ≤ 20; chars per line ≤ 27 burned / ≤ 42 sidecar | lint |
| Every cue's words equal the transcript words in that span | diff against `words.json` |
| Cue start within ±0.1 s of the first word's onset | against `words.json` |
| Box top/bottom inside the declared safe band | from the overlay's bounding box (**implemented** in V15's `caption_qa.csv`: `box_top_px, box_bottom_px, bottom_margin_px`) |
| Protection-mask overlap = 0 at start / middle / end of every cue | extended `caption_qa.py` |
| Clean export is byte-identical in picture to the burned export minus the overlay | frame diff |

**Exports (standard, three):** `…_FINAL.mp4` (clean, **no burned captions**: the master for platforms that take sidecar captions and for any re-edit), `…_FINAL_CAPTIONS.mp4` (burned), `…_FINAL.srt`. Also keep the overlay (`caption_overlay.mov`, transparent) so the burned version can be re-composited without re-rendering the picture. The V15 build does exactly this and verified it by rebuild (§17).

## 14. The 14-phase production workflow

**How to read this section.** The 14 phases are the brief's; each is defined with an **Output**, a **Done when** list (every item is checkable), the **Owner**, whether a **human gate** applies, and the **V15 evidence** or the V8–V15 failure the phase exists to prevent. Phases are grouped under the nine pre-render gates **G0–G8** of §18: a gate is a hard stop that must pass before the next expensive phase begins. `[H]` = a human must perform it; no script may mark it done (§17). Anything not in the V15 tree is **PROPOSED**.

| Phase | Gate it feeds |
|---|---|
| 1 Topic validation, 2 Research, 3 Script | **G0 Contract** |
| 4 Human recording | **G1 Narration** |
| 5 Visual planning | **G2 Animatic** |
| 6 Asset generation | **G3 Asset tests** |
| 7 Animation | **G4 Rig proof**, **G5 Look-dev** |
| 8 Scientific graphics | **G6 Science proof** |
| 9 Editing | G2/G5 refreshed on the real timing |
| 10 Audio | **G7 Audio proof** |
| 11 Captions | checks in G7/G8 |
| 12 Rendering | **G8 Full render** |
| 13 QA | final human acceptance |
| 14 Delivery | self-contained master |

### Phase 1: Topic validation
- **Output:** `research/TOPIC.md`: the selected question, the title, the format (Short or long), the one-sentence answer, and the "why a viewer will care" line.
- **Done when:** the question is bounded (one answer, one chain of reasoning); the format is chosen and the target runtime is **planned at the owner's real pace (~110 wpm, not 150)** (§15); prior art is checked (Slot 10 overlaps Munroe's "Loneliest Human"); the owner has selected it.
- **Owner:** owner decides; Claude drafts. **Human gate:** yes (selection).
- **V15 evidence / failure prevented:** V8's scope had to be *reconstructed* because the original assignment was lost (`history/v8/research/TOOL_AUDIT.md`); a written topic card is the cure.

### Phase 2: Scientific research
- **Output:** `research/CLAIMS.csv` (schema in §9.4), `research/SOURCES.md` (URL + access date), `research/ASSUMPTIONS.md`.
- **Done when:** every number in the script has a row with a source or a derivation; every row is classed (calculated / simplified / magnified / time-compressed / artistic / assumed); each calculated value has been **independently recomputed**; time-sensitive claims carry a recheck date; open items are listed and none is hidden inside the script.
- **Owner:** Claude drafts; owner approves the assumptions. **Human gate:** yes (assumptions).
- **V15 evidence:** `research/V15_RESEARCH_NOTES.md` (NASA Glenn drag, USPA position), `qa/model_check.txt`; V9's physics ledger caught the 17× drag overstatement.

### Phase 3: Scriptwriting
- **Output:** `script/SCRIPT_FINAL.md` with **beat markers** (`[B07: drag arrow grows]`) at each moment that needs a picture event.
- **Done when:** the owner has approved the text; the script and the recording script are the **same text** (V8 found a 130-word / 58 s reference script against a ~200-word / 78 s recording); every number matches `CLAIMS.csv`; no agent edits an approved script (§15).
- **Owner:** owner / script agent; Claude only flags. **Human gate:** yes.
- **V15 evidence:** the script/recording mismatch discovered at V8 and the "owner-designated final" script resolution (`FINAL_SCRIPT_OWNER_APPROVED.md`).

### Phase 4: Human recording
- **Output:** `narration/raw/` (untouched take, SHA-256 in `MANIFEST.md`), `narration/clean.wav`, `voice_edit.csv`, `words.json`, `phrases.json`, `pauses.json`, `INSPECTION.md` (§11.2 N1–N4).
- **Done when:** two ASR decodes agree; homophones resolved against the script *and by ear*; the **owner or a human has listened to the whole take against the script** (this is the step V15 could not do); pauses > 1.5 s handled by policy; the clean file follows one voice chain (§11.1 step 5; V15 compressed twice by accident); the transcript is `HUMAN_VOICE_TRANSCRIPT.md`-style, with unresolved doubts listed.
- **Owner:** owner records; Claude cleans, transcribes, aligns. **Human gate:** yes (listening).
- **V15 evidence:** `tools/prepare_voice.py`, `align_v14.py`; 202 words, 46 cues, 34/34 sync events. **Failure prevented:** V9–V13 were tuned to a 78.2 s narration that was never confirmed; V14 replaced it and forced a 0.26–1.40× warp (§11).

### Phase 5: Visual planning
- **Output:** `storyboard/` (a panel or a still per beat), `timeline/beats.csv` (key word, word start/end, planned visual event, offset policy), `storyboard/SHOT_LIST.csv` (HumanCraft shot spec keys: `shot_id, start, end, narration, narrative_job, viewer_focus, visual_medium, camera, transition_out, rejected_choices`).
- **Done when:** every beat has a word anchor from `words.json`; the **animatic** (stills + narration + captions, 8 fps is enough) has been **watched at phone size**; text budget classed per item (§10.3); each shot states why it exists (the motion contract); the owner approves the animatic.
- **Owner:** Claude drafts; owner approves. **Human gate:** yes (animatic).
- **V15 evidence:** V9's 68 panels, V10's 82, V11's 90, V12's 75 and V15's `timeline/V15_TIMELINE.json` (25 shots; `SHOT_MANIFEST.csv` exists only for V8–V13); **but** V8–V11 storyboards were drawn in design time on a different narration and accumulated overlays (§4). **Failure prevented:** accumulation of on-screen elements; reveals firing before their words ("starts at rest" fired 1.9 s early when the V13 timeline was first mapped onto the V14 narration; fixed in V14).

### Phase 6: Asset generation
- **Output:** a package per §7.6 plus the integration manifest per §8.4.
- **Done when:** the request used the template; the package passed the validator and all five acceptance tests (§7.7, §8.6); statuses are honest (`candidate` until proven); pivots are certified; hashes recorded; **no asset with `pivot: null` or a self-reported FAIL is integrated**.
- **Owner:** Codex draws; Claude tests and integrates; owner approves art. **Human gate:** yes (identity and seam contact sheet).
- **V15 evidence:** 73 Codex layers (V9–V10), the V12/V13 packages that failed their own QA, and the V15 repair (stray 2,754 px blob removed). **Failure prevented:** eight versions of procedural art against an illustrated-art requirement; discs and cut-out joints (V10); architecture pivoted four times.

### Phase 7: Animation
- **Output:** `animation/` rigs and clips; a **5–12 s moving proof** per distinct motion (HumanCraft pass 6) on the shot's *real* range of motion; shot code in film time on the real narration timing.
- **Done when:** the proof passes the seam, rest and lift tests; every body part the script mentions has a keyed event; secondary motion has a cause; ambient motion is on the real clock; the motion contract is filled in for each hero shot; an editorial review and an animation review (separate) have happened (HumanCraft §2D).
- **Owner:** Claude; owner reviews the proof. **Human gate:** yes (watch the proof).
- **V15 evidence:** `cloth_warp.py` self-check (identity at 0°, pack rigid, head/neck < 1 px, deformation < 16 px), `qa/rig_v15/`, 35 strips. **Failure prevented:** a static character (V8 audit: 1–3° of motion, 9/22 shots held), V11's "no arm motion at all".

### Phase 8: Scientific graphics
- **Output:** `scientific_model/model_<film>.py`, `check.py`, `SCALES.py`, `TIME_MAP.py`, the graphics drawn from `state(tm)`.
- **Done when:** the `check.py` invariants pass; every shown number is in `CLAIMS.csv`; magnification and not-to-scale are declared once; colour grammar consistent; the six-way taxonomy has no unclassified object; a human has checked that picture-only and voice-only lead to the same conclusion.
- **Owner:** Claude; owner reviews. **Human gate:** yes (comprehension).
- **V15 evidence:** `SCIENTIFIC_VISUAL_QA.md` ledger, `model_check.txt`. **Failure prevented:** repeated force-diagram redesigns (V9–V15).

### Phase 9: Editing
- **Output:** `timeline/timeline.json` / `V15_TIMELINE.json`; cuts and pushes tied to words; the sync map.
- **Done when:** the **sync map** is generated automatically with the strict thresholds of §10.2 and shows no row beyond them; every cut or push has a stated motivation; rhythm alternates high/medium/low density; no uniform cadence; holds exist after reveals.
- **Owner:** Claude; owner reviews. **Human gate:** yes (watch).
- **V15 evidence:** `tools/sync_map_v15.py` (34/34 `ok`, with loose thresholds).

### Phase 10: Audio
- **Output:** the stems (voice, ambience, effects, accents, optional music), `SOUND_DESIGN_CUE_SHEET.csv`, `SFX_LICENCE_MANIFEST.csv` / ledger, `AUDIO_MIX_QA.md`.
- **Done when:** every SFX has a rights row; the mix has a **separation number** (voice minus background per 0.4 s window; V15 median 20.7 dB, p10 17.1 dB), not only LUFS; the speech-band carve and ducking are applied and measured; the master is at the channel loudness target with true peak under the limit; **a human has listened to the full mix on headphones and on a phone speaker** (§12.7).
- **Owner:** Claude; owner listens. **Human gate:** yes (listening).
- **V15 evidence:** `mix_v15.py`, `audio_qa.py`; V14 vs V15 table in §12.4. **Failure prevented:** SFX only arrived in V9, library SFX unlicensed to V13, and "−16 LUFS proved nothing" for six versions.

### Phase 11: Captions
- **Output:** `captions/…srt`, `caption_overlay.mov`, `qa/caption_qa.csv`.
- **Done when:** §13.2 lint passes; the protection-mask check shows 0; the caption box lies inside the declared safe band; the owner has read every cue against the recording on a phone.
- **Owner:** Claude; owner reads. **Human gate:** yes (read).
- **V15 evidence:** §13.1. **Failure prevented:** low captions (V14 box bottom 1,752 px), overlapping cues (V12), 131-character cue held 7.63 s (V12).

### Phase 12: Rendering
- **Output:** `renders/…_picture.mp4`, clean master, burned master, SRT.
- **Done when:** full decode with no errors (`ffmpeg -v error -i f -f null -`); `freezedetect` clean (V15 had **0 freezes**); frame count equals `round(duration × fps)`; audio duration matches video within one frame; one-command rebuild works; **an isolated rebuild** produces byte-identical files (V15: 8/8, 3 min 04 s, downstream of narration/ASR).
- **Owner:** Claude. **Human gate:** no (but see Phase 13).
- **V15 evidence:** `build_v15.sh`, `qa/decode_check.txt`, `qa/isolated_rebuild.txt`.

### Phase 13: QA
- **Output:** `qa/FINAL_PRODUCTION_QA.md` with **separate sections for automated checks and for human review**, each human item with a name, a date and a verdict (§17).
- **Done when:** every row of the §17 framework is `PASS`, or `FAIL` with a fix, or `NOT PERFORMED (human)`; **browser playback in real time** has happened; **human listening** has happened; the owner has accepted.
- **Owner:** Claude runs automation; **owner and a human reviewer perform the review**. **Human gate:** yes, mandatory.
- **V15 evidence / honesty:** V15 played the film in the built-in browser (sampled, "not watched continuously"); **no listening and no owner acceptance are recorded** (§17).

### Phase 14: Delivery
- **Output:** a **self-contained production master**: the three exports, `START_HERE.md`, the sources needed to rebuild, hashes (`qa/checksums_v15.txt`-style), the handoff doc with full SHAs, and a record of owner decisions (art approved, narration chosen, what was deleted).
- **Done when:** a clean machine can rebuild from the folder (the V15 venv is *not* portable: `pyvenv.cfg` points at another user's Python 3.14; see §6.10, so declare the interpreter and a `requirements.txt` lock); milestone renders are archived (V8–V12 were deleted with permission and left no before/after evidence beyond 24 frames); nothing is uploaded or published without the owner's explicit say-so.
- **Owner:** Claude packages; owner publishes. **Human gate:** yes (publish decision).

## 15. Applying the playbook to the Top 10 V3 script package

**Scope and rule.** This section inspects the latest V3 script package and says what each of the **nine remaining videos** needs. **It does not rewrite, edit or approve any script.** Slot 02 is the finished skydiver film (V15). Source note: the research pass read the V3 package read-only; this audit independently recomputed the headline numbers (§9.5) but did not re-read every V3 file.

Paths: **V3** = `/Users/ghilmankhan/workprojects/youtube-intelligence-os/productions/unreasonably-exact-script-rewrite-v3/` (scripts `V3/revised_scripts_v3/SCRIPT_##_*.md`, "S##"); **X** = `/Users/ghilmankhan/workprojects/what-if-scripts-extract-2026-11-24/` (earlier drafting generation); **V15** = `…/unreasonably-exact/v15/`.

### 15.1 Status and authority (read this before planning)

- **V3 is the latest** (dated 2026-11-25; its header says it "supersedes previous planning selections"). X is the earlier generation (2026-11-24: Codex, Claude V1 and V2 versions per slot). **The two sets differ in wording and in numbers** (V3 03–10 are new rewrites; V3 drops figures X carries, e.g. 04's tilt numbers, 05's 3 m/s jump, 07's 3×10¹⁷ photons, 08/09's "a little under half" tide ratio, 06's exact April dates, 10's 3,475 km arithmetic).
- **Approval status.** Only **Slot 01's reference script** (`V3/reference/SLOT_01_APPROVED_SCRIPT.md`, ~880 words, a 1 m → 400 km ladder) and **Slot 02** are owner-approved. The V3 alternative for Slot 01 (`S01`, 518 words) is explicitly **not approved**. **Slots 03–10 are "working drafts, not research-cleared or production-approved"** (`V3/V3_RESEARCH_AND_PRODUCTION_STATUS.md`). `V3/VISUAL_BEAT_MAPS.md` is "preliminary"; **shot-level beat maps do not exist**. They are the real gap before production starts (G0, §18).
- **Pace.** V3's "150 wpm" planning figure does not match the owner's real narration: V15 runs **110.04 s for ~201–202 words (≈ 110 wpm over the whole film, ≈ 112 over the speech span)**, and V3 lists Slot 02 as "78.2 seconds measured" while the real film is 110 s. **Plan at ~110 wpm**: Shorts 159 words ≈ 87 s, 171 ≈ 93 s, 174 ≈ 95 s, 177 ≈ 97 s, 186 ≈ 101 s; long-form 518–552 words ≈ 4:45–5:00. V15 used 25 shots in 110 s (~4.4 s each).

### 15.2 What carries over from V15 (reusable inventory)

| V15 asset / system | Where | Reusable for |
|---|---|---|
| Side rig, mesh-deformed (`cloth_warp.py`), back/three-quarter/closeup/wrist/instrument/pov rigs | `v15/rigs/`, `tools/` | 01, plus method for new characters (but a **spacesuit** is a *new* character) |
| Environment art: far/near ridge, river plain, two cloud layers, aircraft | `assets/environment/` | 01, 08 (clouds, sky) |
| Physics driver pattern (`model.py` → `state(tm)`) | `tools/model.py` | every film (§9.2) |
| Colour grammar, MODEL frame with assumptions line, ×N lens, speed-time graph | `v15_shots.py` | 01, 04, 05, 08, 09 |
| Whisper alignment, sync map, caption QA, audio carve and separation metric | `tools/` | all |
| **Constraint:** the cloth-flutter driver must **not** be reused in vacuum (drag/weight ≈ 0 ⇒ cloth stays still) | §9, §7.2 | 04, 05, 10 |
| **Constraint:** SFX library clips are not rights-cleared; synthesise | `SFX_LICENCE_MANIFEST.csv`, §12.6 | all |

### 15.3 Production card per video

Complexity classes: **S** small (no character, one idea), **M** medium, **L** large, **XL** extra large. Reuse tags: **[V15]** reusable from the skydiver production, **[B]** reusable inside this batch, **[NEW]** unique to the video. **"Script risk"** lines are claims to verify before production, not criticism of the script.

#### 01 · Does a Higher Fall Always Hit Harder? (Long; approved reference script, ~880 words)
- **Runtime:** about 8 min at 110 wpm unless cut (the reference script header says about 890 spoken words, about 4.1 min at xkcd pace and about 5.4 min with pauses; 5:16 is the end-screen timestamp). The unapproved V3 alternative is 518 words / 3:27.
- **Chain:** higher means harder → holds to a few hundred metres → terminal speed about 200 km/h from ~1 km → from 10 km peak about 320 km/h but landing speed is flat → Baumgartner check at 39 km → 100 km is a convention → 400 km is all model → the ISS: same height, but sideways speed.
- **Models:** drag `D = ½ρv²C_dA`, integration `m·dv/dt = m·g(h) − ½ρ(h)v²C_dA`; US Standard Atmosphere 1976 for ρ(h); g(h) falls about 11.5% by 400 km (recomputed); Mach from a(T(h)); calibration to Baumgartner (1,357.6 km/h, exit 38,969 m, peak at about 27.8 km after about 50 s).
- **Characters:** suited figure at 400 km [NEW]; a skydiver [V15 side rig]; no real likeness. **Environments:** thin blue limb, sky and cloud parallax [V15], capsule platform, ISS silhouette, a railway-station glass-roof card.
- **Unique assets [NEW]:** 1 m–400 km ladder ruler, HUD with PEAK/LANDING lines, record-vs-model split panel, capsule, ISS. **Reusable:** side rig, force arrows, model driver, altitude marker, parallax [V15].
- **Techniques:** sim-driven HUD; camera tracking down the ruler; three small illustrated cards. **Motion graphics:** corner tags (SIMULATION / REAL DATA / THE MATH), speed and g readouts, flat landing line, dashed 100 km line.
- **Sound:** wind bed following ρ(h); **silence** in the 400 km opening; atmosphere-entry roar; sonic-boom cue **synthesised** (not from the unlicensed library).
- **Complexity: XL.** Seven or more segments, a 5.6-decade scale, heavy data-driven HUD. **Challenges:** a log ladder; ~6 min of fall time-compressed; peak vs landing speed on one HUD. **Phone-first risk:** two readouts + corner tag + ruler on one 9:16 frame; show one number at a time.
- **Script risk:** constant drag to about Mach 3 is an assumption; "twenty g, thousands of degrees" is flagged by the script, but "about five g" at 100 km is stated flatly; 204 vs ~190 km/h differ across drafts; "260 times thinner" at 39 km; Magee 1943 rests on a secondary source.

#### 03 · Why Does a Radio Signal Take a Whole Day to Reach Voyager 1? (Short, 177 words ≈ 97 s)
- **Chain:** the signal is not slowed → radio and light are the same kind of wave with the same speed → Moon about 1 s → Voyager reached one light-day → a reply doubles it → the exact delay changes.
- **Models:** `t = d/c`; light-day = 2.590×10¹⁰ km = 173.1 AU (recomputed); Moon 1.282 s; delay grows about 4.9 s/day at a radial speed of about 17 km/s; Earth's orbit adds about ±7 min seasonally (the research pass's estimate).
- **Characters:** none required (optional operator hand). **Environments:** Earth with a Deep Space Network dish, a light-time ruler, Voyager in black space.
- **Unique [NEW]:** Voyager art (dish + boom), vertical light-time ruler, 24 h clock. **Reusable [B]:** Earth, Moon (from 07), pulse, clock (shared with 06).
- **Techniques:** code-driven 2D; a pulse that rides the ruler. **Motion graphics:** clock sweep, two-leg arrow plus processing block, broken-scale ruler.
- **Sound:** pulse blip, soft ticking, low radio carrier; no music (V15 precedent). **Complexity: S.**
- **Challenge:** the Moon-to-Voyager ratio is about 67,000:1 → a light-time ruler (1.3 s, 8.3 min, ~4 h, 24 h), no literal trail. **Phone-first conflict:** the "nested ruler with broken scale" beat is label-heavy → one vertical ruler, one label per beat.
- **Script risk:** NASA's light-day date (the URL in `V3/SCIENTIFIC_CLAIMS_AND_SOURCES.md` row 06 is dated 2026/11/18, while one X draft says 19 November); whether the spacecraft is currently returning data. Recheck on release day.

#### 04 · Could One Sideways Jump Put You in Orbit Around a Tiny World? (Long, 552 words ≈ 5:00)
- **Chain:** toy world R = 3 km, ρ = 2,000 kg/m³, smooth, no spin/air/other body → surface circular speed ≈ 2.2 m/s, lap ≈ 2 h 20 → it touches the ground everywhere (zero clearance) → launching is a separate problem → an upward jump returns → altitude gives clearance → escape ≈ 3.2 m/s.
- **Models (recomputed):** `v_c = 2.243 m/s` (8.08 km/h), `T = 8,403 s ≈ 140.0 min` (independent of R), `v_esc = 3.172 m/s`, `g = 1.68×10⁻³ m/s²`; vis-viva for the elliptic arc; outside the surface `v = v_c√(R/r)`, `T ∝ r^1.5`; a 0.5° tilt puts perigee about 26 m below the surface, 5° about 261 m (research pass).
- **Characters:** one jumper in side view (stand, crouch, level launch, tilted launch, drift): **decide spacesuit or a labelled "pretend"** (the script says "shoes" with no atmosphere). **Environments:** smooth asteroid surface, star field, top-down orbit diagram, magnified contact-point inset.
- **Unique [NEW]:** the ball world, trajectory/ellipse renderer, perigee-under-the-surface graphic. **Reusable:** spacesuit rig [B from 05], trajectory renderer [B shared with 05], MODEL frame, ×N lens, force-arrow grammar [V15].
- **Techniques:** 2D side rig with orbital paths computed in code. **Motion graphics:** dashed path, the "mathematical" continuation inside the rock, speed arrow, lap clock.
- **Sound:** very sparse: soft footfall thud, suit breath if suited, rising tone for speed. **Complexity: L.**
- **Challenges:** the person is 1:1,760 of the radius (~0.5 px on a 900 px world) → **two-view scheme with an inset**; a 140-min lap compressed about ×500 with a clock; zero clearance needs a magnified inset (cf. V15's ×8 lens). **Phone-first conflict:** "diagram R=3 km, density label, no atmosphere/spin…" is text-heavy → show the assumptions as icons.
- **Script risk:** the launch speed is assumed, never shown; the "jogging pace" analogy (8.1 km/h is a slow jog).

#### 05 · Could You Jump Off Phobos and Never Come Back? (Short, 186 words ≈ 101 s)
- **Chain:** weak gravity means a longer jump → isolated-sphere escape speed about 11 m/s (≈ 40 km/h) → that is a speed, not a promise → the real moon is irregular and spinning, and Mars matters → leaving Phobos is not leaving Mars.
- **Models (recomputed):** `v_esc = √(2GM/R) = 11.31 m/s` (GM = 0.0007087 km³/s², R = 11.08 km); circular 8.00 m/s; surface g ≈ 5.8×10⁻³ m/s²; Mars tide about 1.15×10⁻³ m/s² at 9,376 km and a centrifugal term of about 5.8×10⁻⁴ m/s² (≈ 30% of g at the sub-/anti-Mars points); Mars spans about 42° in Phobos's sky; Phobos's orbital speed ≈ 2.14 km/s, Mars escape needs ≈ 0.89 km/s more.
- **Characters:** suited jumper, side view (stand, crouch, push-off, rise, arc) [B same suit rig as 04]. **Environments:** Phobos surface (Stickney crater, grooves), Mars filling the sky, a not-to-scale orbit diagram.
- **Unique [NEW]:** Phobos shape, Mars disk, hop trajectory. **Reusable [B]:** trajectory renderer, MODEL frame, speed readout.
- **Techniques:** low-gravity slow-motion hop (a ~17 min flight compressed to about 10 s). **Motion graphics:** a smooth-sphere overlay on the real shape, a speed meter against 11 m/s, Mars's pull as qualitative arrows.
- **Sound:** muffled suit sounds, soft landing thump, a low rumble from Mars; **no wind or air**. **Complexity: M** (the first suited-rig build and an irregular body).
- **Challenges:** Mars is 42° wide, so scale it correctly; irregular shape vs sphere overlay; the jump arrow cannot be measured, label it "assumed". **Phone-first conflict:** "overlay smooth sphere with model speed" needs one number and one overlay at a time.
- **Script risk:** the ball model overstates escape at the tidally weak points; reported escape values conflict across drafts; V3 gives **no jump speed** so viewers will want one (X used 3 m/s; not carried over). The ~17 min and ~780 m figures come from the 3 m/s case.

#### 06 · How Do You Repair Voyager 1 When Every Reply Takes Two Days? (Long, 545 words ≈ 5:00)
- **Chain:** late 2023 readable data is lost → the flight data subsystem packages data for the radio → March 2024 a command returns a memory readout → about 3% of that memory is corrupted (cause uncertain) → the code is split and relocated → April the first fix is sent and engineering data returns → science returns in stages → two days of delay at one light-day → a 2026 issue has no established shared cause.
- **Models:** light time 22.5 h each way in 2024 (≈ 2.43×10¹⁰ km, 162 AU), round trip 45 h; at a light-day the round trip is 48 h; ≈ 84 sequential 45 h round trips fit in 158 days (the research pass's calculation); a **schematic** memory map (never invent addresses).
- **Characters:** a generic engineering team of two to three (three-quarter and back views), a "you" at a console; no real people. **Environments:** mission control, a DSN dish at night, Voyager in space, the abstract memory map.
- **Unique [NEW]:** control room, memory-relocation diagram, timeline strip, the team. **Reusable [B]:** Voyager, dish, Earth, clock, pulse (from 03); back/three-quarter rig method and the caption pipeline [V15].
- **Techniques:** diagram animation with blocks that move and re-point; a "carrier vs content" wave. **Motion graphics:** timeline strip, two-leg delay clock with a processing block, health packets before science.
- **Sound:** console ticks, low radio carrier, a "data unreadable" noise burst; no music. **Complexity: L** (a human cast and many abstract diagrams over ~5 min).
- **Challenges:** 45 h delay compressed to a few seconds; abstract memory relocation; a 2.5-year timeline (2023 → 2026) must stay legible. **Phone-first conflict:** "highlight corrupted region and label suspected chip", "label 22.5 h each direction; add processing time" are label-heavy → one at a time.
- **Script risk:** "NASA confirmed" and the 2026 data issue are **time-sensitive**; the 3% figure, "three computers" (X drafts only; V3 says "several computers") and exact March/April dates need re-checking.

#### 07 · How Long Does a Laser Take to Reach the Moon and Back? (Short, 174 words ≈ 95 s)
- **Chain:** about 2.5 s round trip, not each way → Apollo reflectors send a small fraction of light back → most light does not return → scientists combine photons from many pulses and apply corrections → `d = cΔt/2`.
- **Models (recomputed):** `Δt = 2d/c`: mean **2.564 s**, perigee 356,400 km → **2.378 s**, apogee 406,700 km → **2.713 s**; ~1.28 s each way; 1 mm of range ≈ **6.7 ps**; corner-cube retroreflector geometry; a beam spot of a few km on the Moon at 1–2 arcsec; photon budget ≈ 3×10¹⁷ per pulse with 1–3 detected (X draft; V3 omits it).
- **Characters:** none. **Environments:** night observatory dome and telescope; Earth to Moon; the Apollo reflector close-up.
- **Unique [NEW]:** corner-cube ray diagram, laser beam, photon counter. **Reusable [B]:** Earth, Moon, pulse, clock (shared with 03, 09). **Build this first** (§15.5).
- **Techniques:** a real-time countdown (2.5 s is watchable as it is). **Motion graphics:** outbound/return arrows, a clock, accumulating photon dots.
- **Sound:** laser zap, tick, a faint "ping" on each detected return. **Complexity: S.**
- **Challenges:** ~30 Earth diameters to the Moon; the reflector is tiny against the beam spot; light covers ~7.5 laps of Earth's circumference per second (a good scale hook); 10¹⁷ photons vs 1–3 returns. **Phone-first conflict:** none significant.
- **Script risk:** "remarkable precision" is not quantified in V3 and the beat map warns against a "single-shot precision" claim; the atmospheric delay size needs verification.

#### 08 · What Would Happen to the Ocean If the Moon Vanished? (Long, 522 words ≈ 4:45)
- **Chain:** stipulated removal of lunar forcing → water already in motion keeps moving → the Moon's effect is a *difference* in pull that drives long waves → two bulges are a simplification → basins and coasts decide each tide → the motion fades with friction (no height or time given) → the Sun's tide remains → the spring–neap cycle disappears → wind and storms still move the sea → neither an instantly still sea nor a flood.
- **Models (recomputed):** `a ≈ 2GMR/d³`: Moon 1.10×10⁻⁶, Sun 5.05×10⁻⁷ m/s², **ratio 0.459**; direct pull ratio 179; equilibrium range (notional) Moon ≈ 0.53 m, Sun ≈ 0.25 m (research pass); M2 period 12 h 25 min; lunar day 24 h 50 min; shallow-water wave speed √(gh) ≈ 713 km/h at 4 km depth.
- **Characters:** a beach figure (back or three-quarter) watching the tide. **Environments:** beach and sky [V15 cloud parallax], Earth cross-section, basin outlines, coastline.
- **Unique [NEW]:** the beach, the 2D wave/basin animation, the Earth ocean cross-section. **Reusable [B]:** Moon, Sun, Earth (from 09, 07), arrow grammar [V15], "not to scale" badge.
- **Techniques:** a simple shallow-wave animation in code; water level against a fixed pole. **Motion graphics:** lunar arrows switch off while water keeps moving; the Sun arrow persists; spring–neap fades.
- **Sound:** surf and wind bed, soft swell, a pulse for the Moon's disappearance. **Complexity: L** (XL if a basin wave is truly simulated).
- **Challenges:** a 0.5 m tide on a 12,742 km Earth means the bulge is exaggerated by ~10⁷ and **must be labelled**; the unknown adjustment time **cannot be shown numerically**; 12.4 h cycles compressed to seconds. **Phone-first conflict:** the "compare forces across Earth" arrows and a bulge picture the script itself calls oversimplified → one arrow pair, then fade into the basin.
- **Script risk:** V3 declines to compare solar and lunar tide sizes; **a graphic must not show 0.46 as a height ratio**; transient decay time "not known".

#### 09 · Would Earth Still Have Tides Without the Moon? (Short, 171 words ≈ 93 s)
- **Chain:** yes, the Sun makes tides → tides come from the near–far difference in pull → the Sun pulls harder overall but the Moon's pull changes more across Earth → Sun and Moon reinforce or oppose each other today → without the Moon that cycle disappears → coasts respond differently.
- **Models (recomputed):** Sun's pull at Earth 5.93 mm/s², Moon's 0.0332 mm/s² (Sun pulls ~179× harder); tidal difference Sun 0.50 µm/s², Moon 1.10 µm/s², ratio 0.46; distance ratio ≈ 389; differential = `2GMR/d³`, subtracting the shared acceleration.
- **Characters:** none. **Environments:** Earth–Sun–Moon diagram (not to scale), two basin outlines with waves.
- **Unique [NEW]:** the Sun and the "subtract the average" arrow animation. **Reusable [B]:** Earth, Moon (from 07), arrows [V15], basin outlines (shared with 08). **Build before 08.**
- **Techniques:** pure code-driven diagram. **Sound:** a soft tone per reveal, a swell for the wave, no music. **Complexity: S.**
- **Challenges:** the two arrows differ by ~10⁻⁴ (Sun) to 3×10⁻² (Moon) of their length, so animate the subtraction, not a to-scale drawing, with a "not to scale" badge. **Phone-first conflict:** two arrow sets at once → one at a time.
- **Script risk:** NASA's "little under half" was dropped in V3; a force ratio is not a tide-height ratio (row 09).

#### 10 · How Far Has a Human Been From Every Other Person? (Short, 159 words ≈ 87 s)
- **Chain:** the farthest from every other human is not the farthest from Earth → Apollo 15: Worden orbited alone while Scott and Irwin were on the surface → a world stood between them → Guinness gives about 3,600 km → Artemis II went farther from Earth, but together → a different record.
- **Models (recomputed):** separation ≈ `2·R_moon + h` through the Moon = 3,474.8 km + h; Guinness's 3,596 km implies h ≈ 121 km (arithmetic); orbit `v = √(GM/r) ≈ 1.63 km/s` at ~110 km, period ≈ 2 h; Artemis II 252,756 mi ≈ 406,771 km vs Apollo 13's 400,171 km (**verify**); the range circle is ~28% of Earth's diameter.
- **Characters:** a generic astronaut silhouette alone in a command module; two small figures on the surface; a group of four in Orion; **no real likeness** (real people are named in the narration, so keep the art generic). **Environments:** the Moon from above (polar view) with the far side, an orbit diagram, Earth far off-frame.
- **Unique [NEW]:** Apollo CSM/LM and Orion silhouettes, a range circle. **Reusable [B]:** Moon, Earth (from 07), suit (from 05), ruler (from 03).
- **Techniques:** 2D top-down geometry with an occlusion beat as the Moon passes between the figures. **Motion graphics:** a range circle around one person, others outside; a distance label; a contrast beat (grouped crew, distant Earth).
- **Sound:** quiet cabin tone, a faint radio crackle that drops out behind the Moon. **Complexity: M.**
- **Challenges:** drawing the Moon's diameter against a 3.5% altitude; 3D occlusion on a 2D phone frame; Earth (384,400 km) stays off-frame. **Phone-first conflict:** none significant.
- **Script risk:** Guinness's method is unexplained (V3 uses "about 3,600 km", illustrative); the Apollo 15 orbit altitude and alignment; the Artemis II record and distance (time-sensitive); overlap with Munroe's "Loneliest Human".

### 15.4 Cross-video findings

**Shared asset library (build once):** Earth (globe + cross-section + night + dish) → 03, 07, 08, 09, 10; Moon (near face, far side, polar view) → 07, 08, 09, 10; Sun → 08, 09; light pulse + clock → 03, 06, 07; Voyager + DSN dish → 03, 06; **spacesuit character** (rigid FK, mesh deform not needed in vacuum) → 01, 04, 05, 10; trajectory/orbit renderer → 04, 05, 10; force-arrow and MODEL frame [V15] → 01, 04, 05, 08, 09; ×N lens [V15] → 04, 06, 09; cloud and sky parallax [V15] → 01, 08; basin/wave animation → 08, 09; caption and sound pipeline [V15] → all.

**Consolidated script risks** (verify at G0): (1) 03/06/10 time-sensitive NASA/Guinness/Artemis claims; (2) 01 constant-drag assumption and g/heating figures; (3) 04 assumed launch speed; (4) 05 isolated-sphere escape speed and conflicting values; (5) 08 inferred transient adjustment and the bulge picture; (6) 09 force ratio vs height ratio; (7) 10 Guinness method and Artemis II record.

### 15.5 Recommended production order (cheapest reusable-first; **differs from the owner's slot order, so confirm it first**)

| # | Slot | Class | Why here |
|---|---|---|---|
| 1 | **07** | S | Builds Earth, Moon, pulse, clock; no character; ideal for the HyperFrames-vs-Cairo pilot (§5.7) |
| 2 | **03** | S | Adds Voyager, light-time ruler, dish |
| 3 | **09** | S | Adds the Sun and the differential-arrow animation; shares basin art with 08 |
| 4 | **05** | M | Builds the suit rig and trajectory renderer |
| 5 | **10** | M | Reuses Moon, Earth, suit |
| 6 | **06** | L | Reuses Voyager, dish, clock; adds the team and control room |
| 7 | **04** | L | Reuses suit, trajectory renderer, MODEL frame |
| 8 | **08** | L | Reuses Earth, Moon, Sun, basin art; adds beach and water |
| 9 | **01** | XL | Largest script; reuses the most from V15. If the fall pair should stay close to 02, move it after 05 once the suit exists |

**Pairs** (`X/START_HERE.md`): 03 with 06, 04 with 05, 08 with 09, 01 with 02. **Build the Short first and reuse its assets in the long film.**

### 15.6 Strategy: Shorts versus long-form

| | **Shorts (03, 05, 07, 09, 10)** | **Long-form (01, 04, 06, 08)** |
|---|---|---|
| Structure | One bounded question, one chain, one closing caveat. V15 order: hook → model frame → mechanism → answer → limits | An investigation with several consequences: 4–9 beats with a visual "reset" between each |
| Runtime and shots | ~87–101 s at 110 wpm; about 20 shots at 4–5 s | ~4:45–5:00 (01 about 8 min); about 55–70 shots; chapter markers planned |
| Characters | Mostly none; one new asset per Short | Each long film adds a human or environment build; budget separately |
| Captions | Burned + clean + SRT; two lines ≤ 27 chars; collision check | Same pipeline; longer silent diagram holds |
| Text | One number per beat; assumptions as icons | Same; stricter because beats are denser |
| Asset reuse | High; aim for one new asset per Short | The Short's assets first; reserve new work for the environment (beach, control room, ladder) |
| Sound | No music; synthesised cues; wind/ambience follow the model | Same; plan silence as an effect (01's 400 km opening) |
| Main risk | Label overload on a 9:16 frame; the one-number rule | Scope creep; the XL ladder in 01; the time-sensitive claims in 06 |
| Gating (PROPOSED) | G0–G8 in full | G0–G8, with G4 and G6 run per chapter so a long film never reaches G8 with an unproven segment |

## 16. Reusable production project template

### 16.1 The directory structure (the brief's tree, with what goes in each folder)

```
VIDEO_PROJECT/                       # one folder per film, named <slot>_<slug>, e.g. 07_laser_moon_round_trip/
├── START_HERE.md                    # status, how to rebuild, owner decisions, open items, full SHAs, what is NOT verified
├── research/                        # TOPIC.md, CLAIMS.csv, SOURCES.md, ASSUMPTIONS.md, notes on tools
├── script/                          # SCRIPT_FINAL.md (owner-approved, beat markers), SCRIPT_APPROVAL.md (who/when)
├── narration/
│   ├── raw/                         # untouched takes; SHA-256 in MANIFEST.md; never overwritten
│   ├── clean.wav, voice_edit.csv    # cleaned voice and the raw->clean edit list
│   └── words.json, phrases.json, pauses.json, INSPECTION.md, TRANSCRIPT.md
├── storyboard/                      # panels/stills, SHOT_LIST.csv, animatic, text-budget audit (REMOVE/TEMPORARY/...)
├── assets/
│   ├── characters/                  # layered or whole-pose art, rig.json/PIVOTS.json, CHARACTER_BIBLE.md
│   ├── environments/                # backgrounds, parallax layers, terrain sprites
│   ├── objects/                     # props, instruments, vehicles
│   ├── graphics/                    # code-drawn component notes, icon art
│   └── _packages/                   # CODEX_<FILM>_ART_PACKAGE_<n>/ as received + integration manifest (never edited in place)
├── animation/                       # shot code, rig renderer, moving proofs (5-12 s), SHOT_CONTRACTS
├── scientific_model/                # model_<film>.py, check.py, SCALES.py, TIME_MAP.py
├── audio/
│   ├── voiceover/                   # voice stem (the cleaned narration as mixed)
│   ├── ambience/                    # beds
│   ├── foley/                       # cloth, strap, touch, device
│   └── sfx/                         # accents, hits, transitions; SFX_LEDGER.csv (rights) beside them
├── captions/                        # .srt, caption_overlay.mov, cue stats
├── timeline/                        # beats.csv, timeline.json, warp.json (if any), NARRATION_VISUAL_SYNC_MAP.csv
├── tools/                           # pinned snapshot of the shared library + project scripts + build_<film>.sh + requirements lock
├── renders/                         # picture, clean master, burned master, SRT; checksums
└── qa/                              # automated evidence, human-review records (qa/human/), contact sheets, decode/freeze logs
```

**Additions to the brief's tree that this playbook recommends** (each fixes an observed V8–V15 problem): `assets/_packages/` (so received Codex packages stay untouched and named after the consuming film, §8.2); `narration/raw/` (the raw take hashed and never overwritten, §11); `qa/human/` (a place where a human review must leave a signed record, §17); `animation/` moving proofs; `renders/` for the exports instead of the V15 habit of leaving deliverables at the folder root.

### 16.2 Where V15 differs (so a session can map the old folder to the template)

| V15 location | Template location |
|---|---|
| `SKYDIVER_SLOWDOWN_FINAL_V15.mp4`, `_CAPTIONS.mp4`, `.srt`, `_picture.mp4` (folder root) | `renders/`, `captions/` |
| `HAMZA_VOICEOVER_RAW.mp3`, `HAMZA_VOICEOVER_CLEAN.wav`, `HUMAN_VOICE_TRANSCRIPT.md`, `WORD_LEVEL_TIMESTAMPS.json` (root) | `narration/` |
| `audio/` (stems, `voice_edit.csv`, `narration_v14.json`) | `audio/` and `narration/` |
| `assets/codex/`, `assets/v10reg|v10supp|v11reg|v12rig|v13reg`, `CODEX_V11|V12|V13_*` (root) | `assets/characters|environments|objects` and `assets/_packages/` |
| `rigs/` (7 views) | `assets/characters/<view>/rig.json` |
| `tools/model.py` | `scientific_model/` |
| `tools/*` (build, align, prepare_voice, mix, QA, rig, shots) | split: shared → library; project-specific shot code → `animation/` |
| `timeline/`, `NARRATION_VISUAL_SYNC_MAP.csv` | `timeline/` |
| `qa/`, `FINAL_PRODUCTION_QA.md`, `*_QA.md` | `qa/` |
| `research/` | `research/` |
| `codex_request/` | `assets/_packages/` requests (or `research/requests/`) |
| `history/v8…v14`, `work/` | `history/` (archive; keep milestone renders and hashes, §14 Phase 14) |
| `SFX_LICENCE_MANIFEST.csv`, `SOUND_DESIGN_CUE_SHEET.csv` | `audio/sfx/` |

### 16.3 What is shared globally and what stays project-specific

**Principle (from V13/V15):** a build must be reproducible *from inside the project folder*. V13 was made self-contained and rebuilt bit-identically in an isolated folder (6/6 SHA-256 equal); V15's isolated rebuild was 8/8 byte-identical in 3 min 04 s (downstream of narration/ASR only). Therefore the **global library is the source; each project vendors a pinned snapshot** (`tools/LIBRARY_PIN.md` records the library version and SHA-256 of every file copied) and never imports from outside its own folder at build time.

| Shared globally (one canonical copy, pinned into each project) | Project-specific (never shared) |
|---|---|
| **Render engine modules**: camera (`Cam`), easing (`smooth/ease_out/ease_io/ramp/wobble`), arrow/label/lens primitives, caption renderer, mesh warp (`cloth_warp.py`), chunked parallel renderer + ffmpeg pipe | The script, the owner's narration (raw and clean), word timings, transcripts |
| **Audio tools**: `prepare_voice.py`, `mix_v15.py` skeleton with `carve()` and `speech_curve()`, `audio_qa.py`, the separation metric, mastering chain | The shot code and shot list, the beat map, the cue sheet |
| **Alignment tools**: `align_v14.py` core (`load_words`, `vad`, `snap`, `split`), `sync_map` | The scientific model and the claim ledger for that film |
| **QA tools**: `caption_qa.py`, `frame_strips.py`, `review_sheet.py`, `sheet.py`, validator (§7.7), decode/freeze scripts, human-review record template | The renders, the checksums, the QA evidence |
| **Style system**: colour grammar (hex values and meanings), type sizes, caption standard, motion-design recipes (§10), safe-area decision | Film-specific labels and the text-budget audit |
| **Characters that recur** (the skydiver, the suit, a generic team) with their `CHARACTER_BIBLE.md`, rigs and certified pivots | One-off props, environments, special diagrams |
| **Environment kit that recurs** (Earth, Moon, Sun, clouds, sky, voyager-class spacecraft) | Hero shots built for a single film |
| **Sound kit**: synthesis recipes, the rights-clear ledger schema, the SFX categories (§12.5), wind/ambience generators | Cue timing, mix levels tuned to that voice |
| **Request templates**: the Codex brief (§7.6), manifests (§8.4), acceptance tests (§8.6) | The actual requests and received packages |
| **Research defaults and the licence ledger** (§5, §12.6) | Claim sources and assumptions |

**Rules for the shared library.** (1) Version it (a changelog and a tag per change); (2) a project may *fork* a library file but must record the divergence in `LIBRARY_PIN.md`; (3) library changes are tested by rebuilding one old project and confirming the hash does not change (V15 is the regression film); (4) nothing in the library hard-codes a film's constants (V15's `v15.py` and `v15_shots.py` hard-code palette, caption position and shot data and are loaded by `exec()`, §6.10 debt); (5) the library never contains rights-unclear audio (the 83 library clips in the V15 licence manifest are `UNKNOWN`-licence, §12.6, and must not be copied into the shared kit).

### 16.4 `START_HERE.md` standard (the file a new session reads first)

A 1-page file with: film ID and one-sentence answer; **status per phase** (done / in progress / blocked / NOT PERFORMED (human)); the **one-command rebuild** and how long it takes; Python and ffmpeg versions and how to create the environment; where each deliverable is and its SHA-256; **owner decisions on file** (art approved? narration chosen? what was deleted and when); **what has not been verified** (listening, phone playback, safe-area test); open claims in `CLAIMS.csv`; the local/remote/PR SHAs where a repository is involved. V15's `START_HERE.md` is the starting point for this file, but it predates this list; its "owner decisions" and "not verified" content is spread across other documents (§17 records that the V15 root documents lost the "candidate / not approved art" line).

## 17. Quality assurance framework

### 17.1 The two rules that govern every row

1. **Automated checks are never proof that a human review happened.** A script, a contact sheet or a measurement is *evidence prepared for a human*. Every QA record has two sections: **Automated (A)** and **Human (H)**. An (H) item is `PASS` or `FAIL` only when a named human performed it and signed it with a date; otherwise it is **`NOT PERFORMED`**. An agent may not write `PASS` in an (H) row. Agents state what they could not do (V15's own wording: "I have no audio output").
2. **Final production acceptance requires two human acts that no tool can replace: (a) real-time playback in a browser or phone, watched, and (b) listening to the full mix.** Both are listed in the acceptance gate at §17.4.

Status vocabulary (HumanCraft §15): `PASS`, `FAIL`, `NOT VERIFIED`, `N/A`; this playbook adds `NOT PERFORMED (human)` to mark an (H) item still owed. `ffprobe` and a null decode prove that the file decodes; they do not prove quality.

### 17.2 What V15's QA did and did not establish (state this in every handoff)

| Claim | Status for V15 | Evidence / limit |
|---|---|---|
| Full decode, no errors | **Done (A)** | `qa/decode_check.txt`: 0 errors |
| No frozen picture | **Done (A)** | 0 freezes |
| Caption collision | **Done (A)** | 138 samples, 0 flags (four graphic colours only, §13.1) |
| 34 narration→visual events inside the loose sync window (times computed from design time, not detected in rendered frames) | **Done (A)** | `qa/sync_map.log`; the 3 ms figure is MP4 audio against the voice stem (audio against audio, not picture sync) |
| Voice vs background separation | **Done (A)** | median 20.7 dB, p10 17.1 dB, speech band 24.8 dB (§12.4; re-measured in this audit) |
| Loudness | **Done (A)** | −16 LUFS, true peak under limit; V15 and V14 are *both* −16, which is why LUFS was not accepted as proof |
| Isolated rebuild | **Done (A)** | 8/8 byte-identical, 3 min 04 s (`qa/isolated_rebuild.txt`), downstream of narration editing and ASR (those were not re-run: the build uses the committed `qa/asr/clean_words.json`, and the clean voice WAV was a copied input) |
| Real-time playback in a browser | **A (agent-sampled); H NOT PERFORMED** | The captioned film played start to end in the built-in browser (110.04 s, 0 dropped frames, 0 stalls) via `qa/review/` on localhost, but "I sampled its state during playback, not by watching continuously" (`FINAL_PRODUCTION_QA.md` §3). Google Chrome: not used |
| **Human listening** | **NOT PERFORMED** | "Listening: No. No audio output available. Replaced by measurements; owner check required." |
| **Owner acceptance of V15** | **NOT RECORDED** | No acceptance in the tree. V13/V14 folders are retained pending it |
| Transcript vs recording by a listener | **NOT PERFORMED** | `HUMAN_VOICE_TRANSCRIPT.md` says so |
| Phone-size visual review | **Partly done** | Reviewed at 375×812 in the browser and in 216–360 px sheets, by the agent |
| Shorts safe-area on a real phone | **NOT PERFORMED** | §13.1 limit 3 |
| Colour-blind simulation | **NOT PERFORMED** | §10.5 |
| Rights clearance of the *library* SFX | **NOT CLEARED** | 83 library clips `UNKNOWN` (of 110 manifest rows); V15's publication master uses only generated cues and the owner's recording; a review-only mix with four library clips exists and must not be published (§12.6) |

### 17.3 The QA checklist (16 areas; A = automated, H = human; every H item leaves a record in `qa/human/`)

| # | Area | Automated checks (A) | Human review (H) | Pass criteria | V15 evidence / tool |
|---|---|---|---|---|---|
| 1 | **Scientific correctness** | `check.py` invariants; every on-screen number in `CLAIMS.csv`; recompute by a second route; assertions on limits | A second person (or the owner) reads the claims ledger against sources; verifies assumptions are said aloud | All ledger rows `checked`; no unclassed object (§9.3); time-sensitive claims rechecked on release day | `qa/model_check.txt`, `SCIENTIFIC_VISUAL_QA.md` |
| 2 | **Character anatomy** | Validator (alpha, strays); seam/rest renders at limits | Look at the seam contact sheet and the moving proof; confirm no disc, gap, double outline, wrong-length limb | Seam test passes at the shot's **real** range; identity test passes | `cloth_warp.py` self-check; `frame_strips.py`; `CHARACTER_ANIMATION_QA.md` |
| 3 | **Equipment continuity** | Overlay `WRIST_FACES.json`; same device geometry per view | Confirm the device, strap, pack, gloves/hands, helmet match in every shot | Same object on the same body part in every view | V13 "wrist test"; V10 owner screenshot audit |
| 4 | **Realistic object movement** | Motion contract fields present (cause, path, contact); ambient motion on real clock | Does each secondary motion have a visible cause; no always-on decorative loops | No motion without a cause; cloth/hair settle with damping | `perf_flutter`, `load` driver |
| 5 | **Motion design** | Text-budget audit complete (REMOVE/TEMPORARY/...); one-idea-per-beat lint (count of simultaneous new objects) | Watch: does anything appear before its word; does anything accumulate; is anything unreadable | No item classed REMOVE ships; no beat adds more than one new idea | `TEXT_REDUCTION_AUDIT.csv`, sync map |
| 6 | **Camera composition** | Subject bounding boxes inside the declared safe band at every cut; push-in scale ≤ declared | Is the subject readable at the first frame (V12: figure 15–20 px tall at 0:00); is any wipe/bloom covering the frame | Subject ≥ a stated fraction of frame height at every cut | V12 opening comparison; stills |
| 7 | **Parallax** | Layer speeds follow `1/z` from one camera (not hand-keyed); overscan covers max shift | Does depth read (differential motion plus occlusion) rather than a flat card pan | Real-construction test (HumanCraft's own §4.5) | `Cam.proj`, `PARALLAX_LAYER_MAP.md` |
| 8 | **Visual comprehension** | Muted contact sheet generated | **Watch muted**: can a viewer state the conclusion from the picture alone? Then voice alone? Same answer? | Picture-only and voice-only lead to the same conclusion | `qa/muted_sheet_1.png`, `_2.png` |
| 9 | **Narration alignment** | Sync map (strict thresholds, §10.2); cue-to-word diff | A human listens to the take against the transcript; checks 10 random reveals by eye | All rows within window; listener finds no mis-heard word | `sync_map_v15.py` (34/34, loose window) |
| 10 | **Caption readability** | SRT lint (§13.2); protection-mask collision at start/middle/end; box inside safe band | Read every cue on a phone at arm's length | 0 flags; ≤ 20 chars/s; no overlap | `caption_qa.py`, `qa/caption_qa.csv` |
| 11 | **Sound-effect timing** | Cue times derived from beat anchors, not typed; offset to the visual event within ±50 ms | Listen with picture; each sound has a visible cause; none on every zoom/arrow | No sound without a cause; none masks consonants | `CUES` + `unwarp()` in `mix_v15.py` |
| 12 | **Voice intelligibility** | Separation metric (voice − background per 0.4 s window): median ≥ 15 dB, p10 ≥ 10 dB *(PROPOSED thresholds; V15 is 20.7 / 17.1)*; speech-band separation; loudness and TP | **Listen on headphones and on a phone speaker** to the full mix; mark any word that is hard to hear | No word lost; owner agrees | `audio_qa.py`, `AUDIO_MIX_QA.md` |
| 13 | **Mobile playback** | Resolution/fps/codec correct (1080×1920, 24 fps, h264/aac); safe-area geometry computed | **Play on a real phone** (unlisted upload or local file): readable, UI not covering captions/labels | No important element under platform UI | Browser at 375×812 only (§17.2) |
| 14 | **Rendering errors** | Full decode; `freezedetect`; black-frame detect; frame count = `round(duration·fps)`; A/V duration within one frame; glyph check (missing `→`/`−` rendered as boxes in V9 and V13) | Watch the whole film once at normal speed for glitches the detectors miss | 0 errors, 0 freezes, 0 black strips | `decode_check.txt`, `build.log` |
| 15 | **Copyright and licensing** | SFX ledger complete (one row per asset, source URL, licence, date, screenshot); no NC licences; no rights-unclear files in the mix; image provenance recorded (§8.6) | Owner reviews the ledger; confirms no real person's likeness, no copyrighted figure reproduced (e.g. the xkcd book figures) | Every file in the final mix traces to a cleared row | `SFX_LICENCE_MANIFEST.csv`, `assets/codex/README.md` |
| 16 | **Independent rebuild verification** | Copy the folder to a new empty location, rebuild with the one command, compare SHA-256 of every deliverable | A human confirms the rebuilt film is the one they reviewed | All deliverables byte-identical; interpreter and tool versions declared | `qa/isolated_rebuild.txt` (8/8) |

**Defect-recording standard** (HumanCraft §2E, matches the V15 defect table): every defect gets `shot_id | timecode | defect | severity | root cause | exact source edit | expected evidence | result`, then the same interval is re-rendered and compared (before/after). V15's 19-row audit (`FINAL_PRODUCTION_QA.md` §1) is the model. It also shows QA working: row 15 is "V15 regression, caught by QA".

**Blocking defects** (any one blocks release): misleading science visual; unreadable essential label; broken sync; severe continuity break; bad contact in a hero action; failed decode; unlicensed audio in the mix. House gate (HumanCraft): score 0–5 per dimension, critical dimensions ≥ 4, supporting ≥ 3; this is a house policy, not an external benchmark.

### 17.4 The acceptance gate (what must be true before a film is called final)

| # | Requirement | Who | Recorded in |
|---|---|---|---|
| 1 | All (A) rows `PASS` | automation | `qa/AUTOMATED.md` |
| 2 | Real-time playback **watched** start to end on a real phone and in a browser | **a human** (owner or reviewer) | `qa/human/PLAYBACK.md` (name, date, device, verdict) |
| 3 | The full mix **listened to** on headphones and on a phone speaker | **a human** | `qa/human/LISTENING.md` |
| 4 | The transcript read against the recording | **a human** | `qa/human/TRANSCRIPT_REVIEW.md` |
| 5 | Claims ledger approved | owner | `research/CLAIMS.csv` status |
| 6 | Art approved (identity + seam sheet) | owner | `assets/_packages/…/INTEGRATION_MANIFEST.csv` |
| 7 | Rights ledger approved | owner | `audio/sfx/SFX_LEDGER.csv` |
| 8 | Isolated rebuild matches | automation + human confirm | `qa/isolated_rebuild.txt` |
| 9 | The owner accepts the film | **owner** | `START_HERE.md` "owner decisions" |

If (2), (3) or (4) is `NOT PERFORMED`, the film's status is **"review cut, pending human acceptance"**, never "final". V15 is in exactly that state: every automated gate is closed, and the human gates (3), (4) and (9) are open; (2) is only partly met.

### 17.5 Review records (templates)

```markdown
# qa/human/LISTENING.md
Film: <id>     Reviewer: <name>     Date: <YYYY-MM-DD>     Device(s): <headphones model> / <phone model, speaker>
Played: full film, once, with picture / audio-only
Hard-to-hear words (timecode, word): <list or "none">
Effects that distract (timecode, which): <list or "none">
Voice: clear / mostly clear / not clear         Bed level: right / too loud / too quiet
Verdict: PASS / FAIL          Signed: <name>
```

The same shape serves `PLAYBACK.md` (device, orientation, caption position vs platform UI, any stutter) and `TRANSCRIPT_REVIEW.md` (each cue read against the recording; mis-heard words).

### 17.6 Why this framework looks the way it does

V8–V13 were accepted on frames; V11 says "the owner's own review is the acceptance test"; the owner's nine V10 screenshots, eight V11 screenshots and the V12 opening frames *were* the real test loop. No one listened until at least V15. V14 and V15 both measured −16 LUFS yet differed by 10 dB in separation; LUFS passed while the owner heard a defect. The framework therefore does three things V8–V15 did not: it makes the human steps **explicit rows that cannot be closed by an agent**; it gives every check a **numeric pass condition**; and it requires a **record** from the person who did the review.

## 18. Root-cause analysis and the workflow that removes repetitive revisions

### 18.1 What the version count really measures

V15 is the **eighth reconstructed version** (V8–V15; V1–V7 are unavailable). All dated records are 2026-11-25; render and file modification times (V9 11:19, V10 12:41, V11 13:50, V12 14:49; V15 files 15:44–18:06) suggest V8 through V15 were built in **about one working day, roughly one version an hour** (an *inference* from mtimes; the first-hand calendar is not recorded). "Fifteen versions" is therefore not fifteen weeks. It is **eight fast review loops**, in which the owner's screenshots and complaints were the main test. The aim of this section is to move those complaints to *before* the render. Every cause below is evidenced in the V8–V15 record (§4); inferences are marked.

### 18.2 The nine causes the brief names, with the evidence and the gate that catches each

| # | Cause (brief's list) | What happened (evidence) | Cost | Caught by |
|---|---|---|---|---|
| 1 | **Missing requirements** | The original Codex assignment was lost; V8 reconstructed a 22-phase ledger (`history/v8/research/TOOL_AUDIT.md`, `CONTINUATION_LEDGER.csv`). The owner's illustrated-asset requirement was unmet for **eight versions** (V1–V8 characters were Pillow or Bézier-drawn). The script conflicted with the recording (130 words / 58 s vs ~200 / 78 s) | Rework of the whole character system at V9; script "owner-designated" retroactively | **G0 Contract** |
| 2 | **Incomplete asset specifications** | The V9 request asked for 8–12 px hidden overlap but defined **no test**; pivots were `null` (V12); canvases varied; 4× exports were resampled; no gloves/hands/face rule for the body views | Round discs (V10), "bolted-on" limbs, different face; V12 and V13 packages unusable | **G3 Asset tests** |
| 3 | **Poor initial planning** | V9–V13 tuned to a 78.2 s narration that was never confirmed; V14 replaced it and forced a 0.26–1.40× warp; the text-heavy storyboard of V8 ("headline on every shot") | A narration change *after* 13 versions of timing; overlays that accumulated V9→V12 | **G1 Narration**, **G2 Animatic** |
| 4 | **Unverified artwork** | The V10 integration QA tested joints "at 60% of limits" and found no gaps; the owner found discs on screenshots within minutes. The Codex V10 supplement said "INCOMPLETE — candidates only"; V12 "NOT READY TO ANIMATE… Motion FAIL"; V13 "P0 not met" | Three art-driven architecture changes | **G3**, **G4 Rig proof** |
| 5 | **Incorrect animation architecture** | FK vector rigs (V8) → PNG parts in FK rigs (V10) → whole-pose, no limb motion (V11) → constrained sprite rig (V12) → mesh deformation (V15). Each swap was forced by the art, not chosen for the film. HyperFrames was reviewed and rejected three times | Four pivots; ~one version each | **G4 Rig proof** + the decision tree (§7.2) |
| 6 | **Insufficient production checkpoints** | No gates; the owner's screenshots were the test. Four versions shipped on decode and stills only; browser playback only sampled in V9–V10, none in V11–V14, and a first sampled full-length playback in V15; defects re-introduced after fixes and caught only by stills (freezes fixed at 21.9 s in V12 and at 50.75/67.96 s in V11; V9's 21.9 s and V10's 50.63 s hits were judged deliberate holds; missing `→` glyph V9 and V13; label collisions V9, V12, V13, V15) | The same defect classes recurred | **G5–G8** + the regression list (§18.5) |
| 7 | **Communication gaps between Claude and Codex** | Package named for the wrong version (off-by-one); rig channel names changed between versions; Codex's own FAIL notes shipped *with* the package and the package was still integrated in part; Claude's measurements disagreed with Codex's (`WRIST_FACES.json` 88/80 vs 84/81); no shared acceptance tests until V12 | Mix-ups; wasted integrations | §7.6 template; §8.5 protocol |
| 8 | **Late audio integration** | The first SFX arrived in V9; ducking, carve and the voice/bed ratio were first *measured* at V15; library SFX were unlicensed to V13 (83 library clips `UNKNOWN` in the manifest); LUFS was the proof for six versions; no listening at all | V14 owner-reported defect (bed vs voice); a rebuilt, fully generated sound design (V14) and re-mix (V15) | **G7 Audio proof**; audio spikes at G2 |
| 9 | **Weak visual acceptance criteria** | QA "judged from frames"; no numbers for subject size at frame 0 (V12 opening: figure 15–20 px tall), caption position (V14 box bottom 1,752 px), text size; the 30× lens, 30× card and ×8 lens were each judged "OK" until the next screenshot | Repeated force-diagram redesigns; a regression of V11's best opening at V12 | **G5 Look-dev** with numeric criteria |

**Cross-cutting causes** (not in the brief's nine, but evidenced): *fix-then-regress* (V11's opening was best, V12 broke it, V13 restored it); *tips imported without a limit* (the "foreground cloud crosses the lens" idea produced a full-frame wipe at V12); *deleted evidence* (V8–V12 folders were permanently deleted with owner permission at V13, leaving 24 frames and documents, so before/after is no longer reproducible); *a decision not recorded* (art approval, narration choice, V13/V14 trashing all pending in prose).

### 18.3 Defect lifecycle in one table (from the brief's problem → lesson list)

| Problem | First reported | Fixed in | Lesson now encoded as |
|---|---|---|---|
| Mechanical-looking joints | V8 audit; V10 owner screenshots | V11 (discs gone), V15 (motion without cutting) | Whole poses + mesh deformation; seam test (§7.5, §7.7) |
| Static character | V8 audit (1–3°, 9/22 shots held) | V12, V15 | Motion contract: every mentioned body part has a keyed event (§14 Phase 7) |
| Detached speedometer | V8 audit (4 sizes, floating) | V11, V12 | Instrument lives on the wrist; face and needle drawn in code |
| Excessive screen text | V8 audit | V9, V12, V13/V15 | Text-budget audit as a gate (§10.3) |
| Confusing force diagrams | V8 (1.5× drag) | repeated redesigns | One scale, one disclosed magnification, decided once (§9.2) |
| Oversized foreground clouds | V12 (owner, 0:03) | V13 | Numeric subject-size criteria at every cut (§17.3 #6) |
| Unnatural terrain | V9 checkerboard | V11, V13, V15 | Look-dev on one finished 5–10 s shot (G5) |
| Poor narration sync | V8–V12 | V13, V14, V15 | Record first; word-level anchors; sync map (§11) |
| Loud background effects | V14 (owner) | V15 | Separation metric + carve; listen (§12.4, §17) |
| Low captions | V14 | V15 | Numeric safe band; collision check (§13) |
| Repeated rendering defects | every version | each | Regression list and G8 (§18.5) |

### 18.4 The pre-render gates G0–G8 (each blocks the next expensive step)

| Gate | Name | Stop-and-fix condition (pass = all true) | What it prevents |
|---|---|---|---|
| **G0** | **Contract** | Topic card; owner-approved script with **beat markers**; `CLAIMS.csv` with all numbers sourced or derived; asset list with a **decision per character** (whole-pose / mesh / FK, §7.2); format (Short or long), runtime at 110 wpm; safe-area and caption decisions recorded; **shot-level beat map exists** (V3's does not yet) | Missing requirements; lost assignment; script/recording mismatch |
| **G1** | **Narration** | Raw take hashed; cleaned; ASR twice agreeing; **a human has listened to the take**; `words.json` exists | Late narration change; the 0.26–1.40× warp |
| **G2** | **Animatic** | Stills + real narration + captions at phone size, **watched by the owner**; text budget classed per item; one audio spike (voice + bed + 3 key cues) tested for separation | Text accumulation; unwatched timing; late audio |
| **G3** | **Asset tests** | Package passed validator and the five acceptance tests; statuses honest; no `pivot: null`, no self-reported FAIL; hashes recorded | Unverified art; round discs; wrong-version packages |
| **G4** | **Rig proof** | A 5–12 s moving proof on the shot's **real** range of motion passes seam/rest/lift; owner has watched it | Architecture swaps late; static character |
| **G5** | **Look-dev** | One **finished** 5–10 s shot (art + motion + caption + graphics + sound) approved on a phone: subject size, text size, colour grammar, safe area all meet **numeric** criteria | Weak visual criteria; clouds, terrain and caption defects found at V12–V14 |
| **G6** | **Science proof** | `check.py` passes; every shown number is in the ledger; magnification/scale declared once; second-route recomputation done | Overstated forces; repeated force redesigns |
| **G7** | **Audio proof** | Stems built; separation numbers meet thresholds; SFX ledger complete; carve applied; **a human has listened** | Loud background; unlicensed SFX |
| **G8** | **Full render** | Build from clean state; decode, freeze, black-frame, glyph checks; captions pass; **isolated rebuild byte-identical**; human playback and listening records exist (§17.4) | Recurring render defects; unreproducible builds |

### 18.5 Regression checks (re-run at every build, because these recurred)

- Frame-by-frame `freezedetect` (freezes fixed in V11 and V12; deliberate holds flagged in V9 and V10).
- Glyph presence for every character used in labels (`→`, `−`, `×`; V9 and V13).
- Caption collision at start/middle/end of every cue (V12, V13, V14, V15).
- Label clipping at frame edges (V9, V12, V13, V15 `"one scale"` at 59 s).
- Opening-frame subject size (V12 regression).
- Any change to a previously approved shot triggers a re-run of *that shot's* strip and the caption check (the V15 regression at 68–74 s was caught this way).
- Build twice in different locations and diff the hashes.

### 18.6 Expected effect (ESTIMATES, not measurements)

The aim is V15-level quality earlier. **ESTIMATE:** with G0–G5 passed before any full-length render, a Short of class S or M should need about **2–3 owner review rounds** instead of V8–V15's eight, and a long film about **3–4**; the reasoning is that every V8–V14 owner complaint (discs, face, instrument, text clutter, force diagram, clouds, terrain, captions, audio) maps to a gate before the full render (table in §18.2/§18.3). No data supports a more precise number; **record actual rounds in `qa/TIME_LOG.csv` on the first film and replace this estimate with a measurement.**

## 19. Production efficiency and automation

**Rule for this section.** Everything marked **EXISTS** is in the V15 tree and was read. Everything marked **BUILD** is a proposal. **Every time or effort figure below is an ESTIMATE**, produced by reasoning from the V15 record (§19.3 says exactly from what); none was measured. The only *measured* timings available are the ones in the V15 logs: a full build **about 3 min**, picture render **1 min 22 s** (9 workers), isolated rebuild **3 min 04 s**, and the version cadence inferred from file times (~one version per hour, §18.1).

### 19.1 Automation opportunities (the 13 the brief lists)

| # | Opportunity | State | What to build | Effort (ESTIMATE) | Human judgement still needed |
|---|---|---|---|---|---|
| 1 | **Automatic storyboard generation** | BUILD. V15 has `V15_TIMELINE.json` (25 shots; `SHOT_MANIFEST.csv` exists only for V8–V13) and `timeline_v15.py`, but panels were authored by hand | A script that reads `beats.csv` + `words.json` and emits a contact sheet of one still per beat (stills from the shot code at the beat's time) and a draft `SHOT_LIST.csv` with the HumanCraft shot-spec keys | 1–2 days | Choosing what each beat *shows* (the creative decision); approving the animatic |
| 2 | **Asset manifests** | PARTLY EXISTS (`assets/codex/manifest.csv` with sha256; `ASSET_MANIFEST.csv` per package) | Generate the §8.4 superset manifest from the folder by running the validator and hashing | 0.5–1 day | Deciding `approved` vs `candidate` |
| 3 | **Reusable character rigs** | PARTLY EXISTS (`rig_renderer.py`, `build_rig.py`, `rigs/*/rig.json`, `cloth_warp.py`) | Extract a rig loader that takes `rig.json` and a weight map, with the V15 self-checks (identity at 0°, rigid zones, displacement bound) as a library test | 3–5 days | Whether a new character reads as alive; art direction |
| 4 | **Narration alignment** | EXISTS (`prepare_voice.py`, `align_v14.py`, whisper.cpp) | Parameterise (no hard-coded V13 paths), merge the two compression stages into one voice chain, add the `SPELL` table and the two-decode agreement check as a script | 1–2 days | Listening to the take; resolving homophones; the pause rhythm |
| 5 | **Scientific simulation interfaces** | EXISTS as a pattern (`model.py` → `state(tm)`) | A thin interface: `state(tm) → dict`, `check()`, `TIME_MAP`, `SCALES`, and a `CLAIMS.csv` linter that verifies every labelled number matches a row | 2–3 days (interface); 0.5–2 days per new model | Choosing the model, the assumptions, the idealisation |
| 6 | **Camera presets** | BUILD (V15 has `Cam`, `push()`, hand-set per shot) | Named presets: `locked`, `punch_in(115–135%)`, `push(z)`, `parallax_reveal`, `pull_back`, `track_down`, each with a motivation string | 1–2 days | When a move is motivated; restraint (the corpus is 89.8% locked) |
| 7 | **Motion-graphics components** | EXISTS as functions (`arrow`, `grow_arrow`, `forces`, `magnifier`, `speed_graph`, `alt_ruler`, `positions_demo`, `density_box`) | Move into the shared library with a gallery render per component and per-component parameters (no film constants); add a log ladder and a light-time ruler | 3–5 days | Composition on a 9:16 frame; the one-number-per-beat rule |
| 8 | **SFX classification** | EXISTS in part (V15 cue-sheet categories; `SFX_LICENCE_MANIFEST.csv` has 110 rows: 83 library clips `UNKNOWN`, 26 generated, 1 owner recording) | Classify by §12.5 category, tag rights status, reject NC at intake, build the ledger linter (§12.6) | 1–2 days | The licence decision and approving the sounds |
| 9 | **Caption collision detection** | EXISTS (`caption_qa.py`, four graphic colours) | Replace the colour test with the per-shot protection mask, add top-position fallback, add SRT lint (§13.2) | 1–2 days | Reading every cue on a phone |
| 10 | **Contact sheets** | EXISTS (`frame_strips.py`: 35 six-frame strips; `review_sheet.py`, `sheet.py`, `strip.py`) | One command that builds the seam sheet, identity sheet, shot strips and muted sheet from a build | 1 day | *Looking* at them |
| 11 | **Mobile previews** | EXISTS (`qa/review/` page played on localhost at 375×812) | Add the Shorts-UI overlay (from Google's PNG, once verified) and a QR/URL for opening on a real phone | 0.5–1 day | Watching on a phone |
| 12 | **Automated render checks** | EXISTS (`decode_check`, freeze, `--check`, caption QA, sync map, `audio_qa`, `isolated_rebuild`) | A single `qa_all.sh` that runs every automated check, writes `qa/AUTOMATED.md`, and refuses to write any (H) row | 1 day | All (H) rows (§17) |
| 13 | **Reproducible project builds** | EXISTS (`build_v15.sh`, isolated rebuild 8/8 (downstream of narration/ASR); **but** the venv is not portable and `exec`-loading is brittle, §6.10) | A `requirements.lock`, an interpreter pin, a bundled font, replace `exec()` with imports, a `bootstrap.sh` that creates a project from the §16 template | 2–3 days | — |

**Implementation order (ESTIMATE of total ≈ 3–4 working weeks for one person, but a first useful slice in about 1 week):** items 13, 12, 5, 4 first (they remove V15's portability debt and make the next film's gates enforceable); then 2, 9, 10; then 6, 7; then 1, 3, 8, 11.

### 19.2 What must stay human (creative and approval judgement)

The topic and the question; the final script; the **performance** (the voice, the pauses); art direction and approving identity; what each beat shows and what to leave out; restraint (silence, hold, no move); comprehension (does a viewer who sees only the picture reach the answer); **watching** the film and **listening** to it; licence decisions; accepting and publishing. Automation can prepare evidence for each of these and can refuse to proceed without a record; it cannot do them.

### 19.3 Estimated production time and effort for future films (ESTIMATES)

**Basis, stated plainly.** There is **no measured baseline** for human time: V8–V15 took roughly one working day of agent time at about one version per hour (inferred), with an unknown amount of owner review time. The numbers below come from (a) that cadence, (b) the V15 computation times above (renders are cheap: ~3 min), (c) the complexity classes of §15 and (d) the assumption that the shared library of §16 exists and the gates are used. They are **planning figures to be replaced by measurements**: log actual hours per phase in `qa/TIME_LOG.csv` from the first film.

| Class | Examples (§15) | Agent work, estimated | Owner review time, estimated | Review rounds (§18.6) | New-asset load |
|---|---|---|---|---|---|
| **Short, S** | 07, 03, 09 | about 1–2 working days | about 1–2 hours across 2 rounds | 2 | 1 new asset (Voyager, Sun, ruler) |
| **Short, M** | 05, 10 | about 2–3 working days (the first suit rig is the cost) | about 2–3 hours across 2–3 rounds | 2–3 | suit + irregular body |
| **Long, L** | 04, 06, 08 | about 4–6 working days | about 4–6 hours across 3–4 rounds | 3–4 | a human or environment build |
| **Long, XL** | 01 | about 8–12 working days | about 8–10 hours across 3–4 rounds | 3–4 | ladder, HUD, capsule, ISS |
| **Library build before film 1** | the §16 shared library and gates | about 3–4 working weeks (ESTIMATE, §19.1) | the owner decides the standards (colour grammar, safe area, caption position) | — | one-time |

**ESTIMATE of the whole batch** (nine films, in the §15.5 order, library built first): on the order of **8–12 weeks of agent time for one operator** if films are built sequentially, falling as reuse rises (the first three Shorts build the shared kit). This is a planning range, **not a forecast**: the largest unknown is Codex art turnaround, which V9–V13 show to be failure-prone and which the §7.6 template is designed to shorten.

**Where the time is expected to go** (ESTIMATE, from the V8–V15 pattern): asset acceptance and rig proof (largest, historically eight versions), the science model and its checks, then audio; **rendering is not the bottleneck** (picture render 1 min 22 s; full build ~3 min).

### 19.4 Risks to the estimates

Codex package failures (V12, V13); time-sensitive claims changing before release (03, 06, 10); a licence or version change in a tool (§5 snapshot is dated 2026-11-25); the pending Remotion 5.0 headcount rule if collaborators are added; the V15 venv not being portable (needs 13 first); owner availability for the human gates (§17.4), which cannot be parallelised away.

## 20. Source references, checklists and appendices

### 20.1 Sources

**A. V15 and project files (all under `/Users/ghilmankhan/workprojects/unreasonably-exact/`)**

| Area | Files |
|---|---|
| Finals | `v15/SKYDIVER_SLOWDOWN_FINAL_V15.mp4`, `…_CAPTIONS.mp4`, `…_picture.mp4`, `….srt` |
| Renderer and shots | `v15/tools/v15.py`, `v15_shots.py`, `rig_renderer.py`, `build_rig.py`, `instrument11.py`, `cloth_warp.py` |
| Science | `v15/tools/model.py`, `v15/qa/model_check.txt`, `v15/SCIENTIFIC_VISUAL_QA.md` |
| Narration and alignment | `v15/tools/prepare_voice.py`, `align_v14.py`, `v15/HAMZA_VOICEOVER_RAW.mp3`, `HAMZA_VOICEOVER_CLEAN.wav`, `HUMAN_VOICE_TRANSCRIPT.md`, `WORD_LEVEL_TIMESTAMPS.json`, `audio/narration_v14.json`, `audio/warp.json`, `audio/voice_edit.csv`, `qa/asr/` |
| Audio | `v15/tools/mix_v15.py`, `audio_qa.py`, `AUDIO_MIX_QA.md`, `SOUND_DESIGN_CUE_SHEET.csv`, `SFX_LICENCE_MANIFEST.csv`, `audio/V15_mix.wav`, `audio/stems/` |
| Captions | `v15/tools/caption_qa.py`, `qa/caption_qa.csv`, `qa/caption_overlay.mov` |
| Timeline and sync | `v15/tools/timeline_v15.py`, `sync_map_v15.py`, `timeline/V15_TIMELINE.json`, `NARRATION_VISUAL_SYNC_MAP.csv` |
| QA | `v15/FINAL_PRODUCTION_QA.md`, `CHARACTER_ANIMATION_QA.md`, `PROJECT_CLEANUP_REPORT.md`, `qa/decode_check.txt`, `qa/isolated_rebuild.txt`, `qa/checksums_v15.txt`, `qa/build.log`, `qa/build_isolated.log`, `qa/render_picture.time`, `qa/review/`, `qa/muted_sheet_*.png`, `frame_strips.py`, `review_sheet.py`, `sheet.py`, `strip.py` |
| Art and rigs | `v15/assets/codex/` (73 layers, `manifest.csv`, `validation.json`, `PROMPTS.md`, `README.md`), `assets/v11reg/`, `assets/v12rig/` (`RIG.json`, `side_lift_00…11.png`), `assets/environment/`, `rigs/{side,back,three_quarter,closeup,instrument,pov,wrist}/`, `CODEX_V11_ART_REPAIR_PACKAGE/`, `CODEX_V12_ART_PACKAGE/`, `CODEX_V13_ART_PACKAGE/` |
| Codex briefs | `v15/codex_request/v11/CODEX_V12_ART_BRIEF.md`, `codex_request/v12/CODEX_V13_ART_BRIEF.md`; `v15/history/v9/CODEX_MISSING_ASSET_REQUEST_V9.md` |
| Research | `v15/research/V15_RESEARCH_NOTES.md`; `v15/history/v12/TOOL_AND_LIBRARY_USAGE.md`, `MOTION_DESIGN_RESEARCH.md`, `TEXT_REDUCTION_AUDIT.csv`, `PARALLAX_LAYER_MAP.md` |
| History | `v15/history/v8` (BRIEF, CHARACTER_DESIGN_BIBLE, CONTINUATION_LEDGER, AUDIO_TRANSCRIPT_AND_ANALYSIS, FINAL_SCRIPT_OWNER_APPROVED, SCRIPT_REFERENCE) through `v14`; key audits: `history/v9/V8_DEEP_AUDIT.md`, `history/v11/V10_SCREENSHOT_DEFECT_AUDIT.md`, `history/v13/CLEANUP_AND_CONSOLIDATION_REPORT.md`, `OPENING_V10_V11_V12_V13_COMPARISON.md`, `CODEX_V13_INTEGRATION_MANIFEST.csv` |
| Method document | `HumanCraft_MASTER_Animation_Director_V4.md` (and `.pdf`) at the project root |
| Sound archives | `SOUND EFFECT.zip` (listing only; not rights-cleared) |
| xkcd research (outside the project) | `/Users/ghilmankhan/workprojects/what if book/WhatIf_Complete_Extraction/`; `/Users/ghilmankhan/workprojects/video data of what if/` |
| Top-10 scripts (outside the project) | `/Users/ghilmankhan/workprojects/youtube-intelligence-os/productions/unreasonably-exact-script-rewrite-v3/`; `/Users/ghilmankhan/workprojects/what-if-scripts-extract-2026-11-24/` |

**B. External sources (read by the research pass on 2026-11-25; re-verify before relying on a licence or a number)**

*Tools and licences*
- Remotion: <https://www.remotion.dev/docs/> · licence <https://github.com/remotion-dev/remotion/blob/main/LICENSE.md> · pricing <https://www.remotion.dev/docs/license/pricing> · FAQ <https://www.remotion.dev/docs/license/faq> · terms <https://www.remotion.dev/docs/terms> · `spring()` <https://www.remotion.dev/docs/spring> · skills <https://www.remotion.dev/docs/ai/skills>
- Motion Skills (iart-ai): <https://github.com/iart-ai/motion-skills>
- HyperFrames: <https://github.com/heygen-com/hyperframes> · <https://www.npmjs.com/package/hyperframes> · <https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen>
- EffectCraft: <https://github.com/storytold/effectcraft>
- Anidoodle: <https://github.com/alexgreensh/anidoodle>
- Claude Animated Shorts: <https://github.com/mromidev/claude-animated-shorts>
- Three.js skills: <https://github.com/cloudai-x/threejs-skills>
- whisper.cpp: <https://github.com/ggml-org/whisper.cpp> · models <https://huggingface.co/ggerganov/whisper.cpp> · OpenAI Whisper <https://github.com/openai/whisper> · WhisperX <https://github.com/m-bain/whisperX> · Montreal Forced Aligner <https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner> · aeneas <https://github.com/readbeyond/aeneas> · ctc-forced-aligner <https://github.com/MahmoudAshraf97/ctc-forced-aligner>
- FFmpeg legal <https://ffmpeg.org/legal.html>
- Manim <https://docs.manim.community/en/stable/tutorials/quickstart.html> · <https://github.com/3b1b/manim>
- SFX sources: Freesound licences, YouTube Audio Library, Pixabay licence, Sonniss GameAudioGDC, ZapSplat, BBC Sound Effects (site-level; the exact page URLs were not captured in the research report: re-open each official licence page and save a copy for the ledger, §12.6)

*Rigging, deformation, camera, secondary motion*
- Twelve basic principles of animation <https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation>
- Spine: <https://esotericsoftware.com/spine-meshes> · <https://esotericsoftware.com/spine-weights> · <https://esotericsoftware.com/spine-ik-constraints> · <https://esotericsoftware.com/spine-physics-constraints>
- Rive IK <https://help.rive.app/editor/constraints/ik-constraint> · Toon Boom <https://docs.toonboom.com/help/harmony-22/premium/getting-started/character-building.html> · Moho <https://www.lostmarble.com/moho/manual/bone_layers.html> · DragonBones <https://dragonbones.github.io/en/animation.html>
- ARAP: Igarashi, Moscovich & Hughes, ACM TOG 24(3):1134–1141 (SIGGRAPH 2005) <https://dblp.org/rec/journals/tog/IgarashiMH05> · <https://history.siggraph.org/?p=113958> · Igarashi & Igarashi 2009 <https://www-ui.is.s.u-tokyo.ac.jp/~takeo/papers/takeo_jgt09_arapFlattening.pdf>
- FFD: Sederberg & Parry, SIGGRAPH '86, DOI 10.1145/15886.15903 <https://history.siggraph.org/?p=116034>
- Multiplane camera <https://en.wikipedia.org/wiki/Multiplane_camera> · parallax scrolling <https://en.wikipedia.org/wiki/Parallax_scrolling> · shot size <https://en.wikipedia.org/wiki/Shot_(filmmaking)>
- Verlet: Jakobsen, "Advanced Character Physics", GDC 2001 <https://gamedeveloper.com/programming/advanced-character-physics>

*Captions, safe area, loudness, audio*
- Netflix English timed-text style guide <https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-Timed-Text-Style-Guide> · general requirements <https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements>
- BBC subtitling summary (secondary) <https://clevercast.com/bbc-subtitling-guidelines> · Szarkowska et al. (2024) <https://ueaeprints.uea.ac.uk/id/eprint/100082/1/6_Szarkowska_et_al.pdf>
- YouTube Shorts: <https://support.google.com/youtube/answer/12779649?hl=en> · <https://blog.youtube/creator-and-artist-stories/your-guide-to-getting-started-with-youtube-shorts/> · <https://support.google.com/youtube/answer/16215842?hl=en> · Google Ads <https://support.google.com/google-ads/answer/13547298?hl=en> · <https://support.google.com/google-ads/answer/16041697?hl=en> · safe-zone overlay PNG <https://services.google.com/fh/files/misc/youtubesafezoneoverlay_vertical_final.png> (**not downloaded**) · third-party margins <https://www.socialync.io/tools/safe-zones/youtube-shorts> (**UNVERIFIED**)
- EBU R128 <https://tech.ebu.ch/docs/r/r128.pdf> · YouTube loudness (blog) <https://productionadvice.co.uk/youtube-loudness/> · Frame.io <https://workflow.frame.io/guide/loudness-for-youtube> · Netflix sound mix <https://backlothelp.netflix.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-5>
- Sound On Sound ducking <https://www.soundonsound.com/techniques/duck-tales> · de-essing <https://www.soundonsound.com/techniques/techniques-vocal-de-essing> · <https://en.wikipedia.org/wiki/De-essing> · speech intelligibility <https://www.tvtechnology.com/miscellaneous/the-importance-of-speech-intelligibility> · IOA <https://www.ioa.org.uk/system/files/proceedings/g_leembruggen_a_stacey_should_the_matrix_be_reloaded.pdf>

*Scientific communication and editing*
- Kurzgesagt process <https://kurzgesagt.org/youtube/> · <https://kottke.org/20/02/how-to-make-a-kurzgesagt-video-in-just-1200-hours>
- EU direct labelling <https://data.europa.eu/apps/data-visualisation-guide/direct-labelling> · Tufte notes <https://faculty.cc.gatech.edu/~stasko/7450/12/Notes/tufte.pdf> · Cairo/Cornell notes <https://info3312.infosci.cornell.edu/notes/great-viz.html> · Okabe–Ito/Wong palette <https://siegal.bio.nyu.edu/color-palette/> · AMS Notices (Sanderson) <https://www.ams.org/notices/202210/rnoti-p1789.pdf>
- Murch Rule of Six <https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch> · critique <https://nofilmschool.com/2018/08/editing-eye-trace-mind-rule-six-incorrect> · split edits <https://en.wikipedia.org/wiki/Split_edit>
- xkcd *What If?* <https://en.wikipedia.org/wiki/What_If%3F_(book)> · <https://en.wikipedia.org/wiki/Xkcd>

*Science sources used by V15*
- NASA Glenn drag equation <https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/> · drag coefficient <https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-coefficient/> · USPA neutral body position <https://www.uspa.org/foundations-of-flight-neutral-body-position> · USPA FAQ <http://www.uspa.org/discover/faqs/learning> · USPA SIM A <https://uspa.org/skydiveschool/A>

### 20.2 Practical production checklists

Copy a checklist into the project's `START_HERE.md` and tick it; an unticked human item (marked **[H]**) is a blocker, not a formality.

**G0 Contract**
- [ ] `research/TOPIC.md`: one bounded question, one answer, format, title
- [ ] `script/SCRIPT_FINAL.md` owner-approved, with beat markers; approval recorded
- [ ] `research/CLAIMS.csv`: every number sourced or derived; classed (calculated / simplified / magnified / time-compressed / artistic / assumed); recomputed by a second route
- [ ] Time-sensitive claims flagged with a release-day recheck date
- [ ] Asset list with a rig decision per character (§7.2); character bible written
- [ ] Runtime planned at ~110 wpm; shot-level beat map exists
- [ ] Safe area and caption position decided (and phone-tested [H])
- [ ] **[H]** Owner approves the contract

**G1 Narration**
- [ ] Raw take untouched, SHA-256 in `narration/MANIFEST.md`; room tone and a sync clap recorded
- [ ] Setup talk removed; pauses > 1.5 s capped by policy; no words removed; no time-stretch
- [ ] ASR decoded twice, outputs identical; homophones fixed in the `SPELL` table
- [ ] `words.json`, `phrases.json`, `pauses.json` generated; one voice chain (not two compressions)
- [ ] **[H]** A human listened to the whole take against the script; retakes marked

**G2 Animatic**
- [ ] One still per beat; text budget classed (ESSENTIAL / TEMPORARY / REDUNDANT / REMOVE)
- [ ] Stills + real narration + captions playable at phone size
- [ ] One audio spike: voice + bed + three key cues, separation measured
- [ ] **[H]** Owner watched the animatic

**G3 Asset tests**
- [ ] Request used the §7.6 template; package named after the consuming film
- [ ] Hash recorded for every file; manifest in the §8.4 schema
- [ ] Validator: mode, canvas, alpha range, RGB under zero alpha = 0, no stray components, no haze
- [ ] Rest, seam, lift, identity, wrist tests run; no `pivot: null`; no self-reported FAIL integrated
- [ ] Statuses honest (`candidate` until proven); repairs by Claude recorded with before/after hashes
- [ ] **[H]** Owner looked at the seam and identity contact sheets

**G4 Rig proof**
- [ ] 5–12 s moving proof on the shot's real range of motion
- [ ] Every body part the script mentions has a keyed event; every secondary motion has a cause
- [ ] Ambient motion on the real clock
- [ ] **[H]** Owner watched the proof

**G5 Look-dev**
- [ ] One finished 5–10 s shot (art + motion + captions + graphics + sound)
- [ ] Subject size at frame 0 and every cut meets the numeric criterion
- [ ] Essential labels ≥ 30 px, secondary ≥ 24 px; contrast ≥ 4.5:1 (3:1 large)
- [ ] Colour grammar consistent; colour-blind simulation run
- [ ] **[H]** Reviewed on a phone

**G6 Science proof**
- [ ] `check.py` passes (limits, signs, monotone time)
- [ ] Every shown number is in `CLAIMS.csv`; every magnification and not-to-scale declared once
- [ ] Picture-only and voice-only lead to the same conclusion **[H]**

**G7 Audio proof**
- [ ] Every SFX has a ledger row (source URL, licence, date, saved licence page); no NC; generated cues recorded as own work
- [ ] Bed well under the voice (V15: −15 dB × envelope, 10 dB below V14; measure the separation), ducking and speech-band carve applied
- [ ] Separation: median ≥ 15 dB, p10 ≥ 10 dB (PROPOSED thresholds; V15 = 20.7 / 17.1); loudness at channel target; true peak under limit
- [ ] **[H]** A human listened (headphones and phone speaker)

**G8 Full render and delivery**
- [ ] Clean build from empty state with one command
- [ ] Full decode; freeze, black-frame and glyph checks; frame count = `round(duration × fps)`; audio within one frame
- [ ] Caption lint and protection-mask check pass; box inside the safe band
- [ ] Three exports: clean MP4, burned MP4, SRT; caption overlay kept
- [ ] Isolated rebuild in a new empty folder, SHA-256 equal on every deliverable
- [ ] `qa/AUTOMATED.md` complete; `qa/human/{PLAYBACK,LISTENING,TRANSCRIPT_REVIEW}.md` each signed by a named person
- [ ] Owner decisions recorded (art approved, narration chosen, rights ledger approved, deletions)
- [ ] `START_HERE.md` says what is **not** verified
- [ ] **[H]** Owner accepts; owner decides whether to publish (nothing is uploaded by an agent)

### 20.3 Open-items register (everything this audit could not close)

| # | Item | Why open | Who can close it |
|---|---|---|---|
| 1 | V15 owner acceptance | None recorded | Owner |
| 2 | Listening to the V15 mix and the narration against the transcript | No human has; agent has no audio output | Owner / a human reviewer |
| 3 | Continuous real-time playback of V15 on a real phone | Only sampled playback in a browser | Owner |
| 4 | Shorts safe area (x 48–888, y 288–1248 is a third-party working rule; V15's box bottom is 1,626 px) | No official pixel margins found | Owner, with an unlisted test upload |
| 5 | V15 rebuild on this Mac | `.venv` points to an absent Python 3.14 and another user's path | A session that creates a pinned environment |
| 6 | V15 art status | "candidate / not approved" line dropped from V15 root documents; no art approval recorded | Owner |
| 7 | `SOUND EFFECT.zip` provenance and rights | 234 entries / 106 audio-video files, listing only; free-giveaway and film-inspired names | Owner; do not use until read |
| 8 | The 83 SFX-library clips in `SFX_LICENCE_MANIFEST.csv` (`UNKNOWN` licence), including the four used in the review-only mix `audio/V15_mix_library_review.wav` and `qa/review/review_library_mix.mp4` | Library README says ownership was not established | Owner; keep out of every publication mix and do not publish the review render |
| 9 | Colour-blind legibility of the force colours | Not tested | A session with a simulator |
| 10 | Remotion 5.0 final terms; ZapSplat and BBC licence text; Anidoodle sample licence; official YouTube loudness | Primary sources blocked or absent | Re-check before use |
| 11 | Beat maps for Slots 03–10; research clearance of those drafts | V3's maps are preliminary; drafts are "not research-cleared" | Owner + research pass |
| 12 | Time-sensitive claims in Slots 03, 06, 10 (NASA light-day statement, Voyager 2026 issue, Artemis II record) | Change over time | Release-day recheck |
| 13 | Slot order | Recommended build order differs from slot order | Owner |
| 14 | Original V8–V12 evidence, V1–V7, the owner's briefs and screenshots | Deleted or never in this tree | Not recoverable here |
| 15 | Status of the original 78.2 s narration (V9–V13 documents call it the owner's recording; never confirmed as final) | Not verifiable | Owner |
| 16 | Which tools V15's author actually found on the build machine | Only the V15 notes exist | — |
| 17 | Voice chain: two 2:1 compressors in series (`prepare_voice.py` at −24 dB, then `mix_v15.py` at −22 dB); the second explains the drop from the clean file (−18.5 LUFS) to the voice stem | Read from source and measured, never listened to | Owner decides the single chain (§11.1 step 5) |
| 18 | Isolated rebuild (8/8) covers only the build downstream of narration editing and ASR; the cleaned voice WAV was a copied input | Narration cleaning and ASR were not re-run | A session that runs `build_v15.sh --from-voice` on the build machine |
| 19 | V15 speech-band separation: two windows near 0 dB (breaths at 76.2 s and 93.1 s) and the broadband minimum of +5.8 dB | Below the +6 dB working floor; judged breaths by level only, not by listening | Listening gate (§12.7) |
| 20 | The §15 complexity classes (S/M/L/XL), shot counts and sound lists | PROPOSED planning figures, not measured | Replace with measurements from the first film |
| 21 | A reviewer could not confirm: Remotion `LICENSE.md` (HTTP 503), Netflix −27 LKFS figures, WhisperX CPU-only and pyannote terms, Hugging Face model licences, Anidoodle date and samples | Primary pages blocked or absent | Re-check before relying on them |
| 22 | The Appendix B validator: no try/except around image loading, small components are counted but not warned on, and 4-connectivity inflates component counts | Known weaknesses of a scratch tool | Harden before reuse |

### 20.4 V15 key numbers (quick reference; each is in the section noted)

110.0417 s · 2,641 frames · 24 fps · 1080×1920 · 25 shots · 202 words · 46 caption cues · 44 warp anchors (§6, §11, §13) | model m 80 kg, CdA 0.5 m², peak 81.0 m/s at 20 s and 8,809 m, D/W 1.000 → 1.035 → 1.013, ground 50.9 m/s at 158.6 s (§9.1) | net force 0.9–3.6% of weight shown at ×8 (§9.2) | mesh grid 32 px, knees ±2.6°, wrists ±4°, deformation < 16 px, pack < 0.35 px, ripple `1 + 4.2·load^1.3` (§6.7) | bed −15 dB × envelope, ducks 12/9 dB, carve 1–4.5 kHz −6 dB, master −16 LUFS, separation median 20.7 dB (§12) | captions box 1,506–1,626 px, 294 px clear, ≤ 27 chars/line, max 17.4 chars/s (§13) | full build ≈ 3 min, picture render 1 min 22 s on 9 workers, isolated rebuild 3 min 04 s, 8/8 byte-identical (§14, §17).

---

---

## 21. Slot 07 V1–V3 lessons (added 2026-11-26)

**Source.** The Slot 07 production of *How Long Does a Laser Take to Reach the Moon and Back?*. The owner selected V3 as the final version on 2026-11-26 and accepted its visual quality; listening and the music licence are still open. The evidence is in `07-video-productions/SLOT07_lunar-laser-ranging/`, shortened here to `S07/`. The retrospective is `10-production-retrospectives/SLOT07_PRODUCTION_RETROSPECTIVE_AND_LESSONS.md`, and the Codex method is `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`.

**How to read the Status column.**
- **VERIFIED (S07)**: the lesson is backed by measured Slot 07 evidence.
- **PROPOSED**: a future standard derived from that evidence that no film has yet run end to end.

Section 1.4's precedence still applies.

### 21.1 The sixteen lessons

| # | Area | Lesson to preserve | Slot 07 evidence | Status | Standard from now on |
|---|---|---|---|---|---|
| L1 | Research | **Collect real visual evidence before generating any artwork** | 173 references saved and indexed with source, licence and influence (`S07/research/REFERENCE_MANIFEST.csv`, `codex_handoff/references/*/REFERENCE_INDEX.md`). Brief error R10, a retroreflector tilt of 30° where the real value is about 23°, was caught only because the AS11-40-5952 photo had been inspected | VERIFIED (S07) | Gate G0-art: no Codex brief until each object has 2–3 decisive photos viewed and indexed |
| L2 | Codex coordination | **Claude can assign focused artwork tasks to Codex through the Codex CLI**, without the owner relaying prompts | 16 runs launched from Claude's shell with the bundled CLI 0.171 (`tools/codex_run.sh`, run logs `codex_handoff/runs/*/codex.log`) | VERIFIED (S07) | Use the protocol document. The PATH `codex` 0.153 cannot use the configured model |
| L3 | Asset references | **Verify that references were inspected before generation** | Batches 0–2: no image ever reached the generator (R1). After `-i` attachment plus a required `view_image`, every log shows 2–5 `view_image` calls before `image_gen` | VERIFIED (S07) | `grep -c view_image codex.log` > 0, or the run is rejected unread |
| L4 | Art consistency | **Master artwork first, derived perspectives afterwards** | Independent text-only views disagreed (R2). Masters B4M, B5M, B3M and B5P, with every layer cut by editing the master, gave IoU 0.978–0.992 | VERIFIED (S07) | One approved master per object; every other view is an edit of it |
| L5 | Asset generation | **One focused deliverable per run** | Multi-asset batches 0–2 at effort `low`: 0 approved images. 16 single-deliverable runs at effort `high`: 13 usable, 3 rejected, 7 in the final film | VERIFIED (S07) | One deliverable per run (plus a NOTES.md of at most 12 lines), `-c model_reasoning_effort="high"` |
| L6 | Asset correction | **Repair the individual defect instead of regenerating the family** | B4L2 (open the slit) passed first time at IoU 0.992. R2b and B5PR2 show the limit: an edit that triggers a redraw is rejected, and the detail is composited in code from an approved part (R16) | VERIFIED (S07) | One defect per edit; after one failed edit, change strategy (code composite or rig fix) rather than repeat |
| L7 | Rigging | **Measure pivots, overlaps and registration independently**, never from Codex's report | RIG_002 pivots measured by Claude (`assets/rigs/observatory/RIG_002_observatory.json`). The P05 shoulder gap was measured at worst 86 px of 15,361 after rig v2. The fix was skinning, not new art (R17) | VERIFIED (S07) | Claude writes the rig JSON; ±25° rotation test in a moving proof before use |
| L8 | Small components | **Generate small parts on tightly cropped canvases** | B5L2: a small shoulder cap on a full canvas came back with no alpha 0 anywhere (R11). B5C on its own canvas came back clean | VERIFIED (S07) | Small parts fill their own canvas; Claude registers them by measured offset and scale |
| L9 | Validation | **Re-run all earlier tests after every artwork correction** | R2b fixed the base and broke the tilt (23.6° to 14.7°) (R13) | VERIFIED (S07) | The acceptance script re-runs the whole test list, not only the named defect |
| L10 | Opening | **No visually inactive period in the first seven seconds** | V2 had 30 of 60 frames frozen at 2–4 s. V3 has 0 of 60, from an aim-line trace, a continuous tilt and a charge glow. A self-check gives the minimum screen speed as 38 u/s (`S07/renders/roughcut_v3/OPENING_RETENTION_AUDIT.md`) | VERIFIED (S07) as motion. Effect on retention is **NOT MEASURED** | Gate G-open: an automated frame-difference check over 0–7 s, with no hold longer than 0.5 s unless it is motivated |
| L11 | Scientific visualization | **Explain relationships, not merely display objects** | The V2 0:59 triangle showed "light spreads wide" only as the width of a shape. V3 shows a rain of photons that miss the telescope and a single one detected on the word "detector" (D06). A self-check confirms no other photon enters the telescope | VERIFIED (S07) for the design. Comprehension is **NOT MEASURED** (no muted-viewer test) | Every model beat names the relationship it shows (cause, ratio, miss/hit) in its shot contract |
| L12 | Typography | **Minimal, readable scientific disclosures** | V2 had 8 kinds of pill and about 78 s of persistent badges. V3 has no pills: 11 timed sentence-case notes, 31.5 s in total, shown once per model entry (`roughcut.DISCLOSURES`, `ON_SCREEN_TEXT_AUDIT.csv`) | VERIFIED (S07). Phone legibility at about 12 pt is **NOT TESTED** | One disclosure table per film; a disclosure is shown once when its model begins, attached to the object it qualifies |
| L13 | Captions | **Consistent handwritten-inspired typography with verified licensing** | Comic Neue (SIL OFL, `assets/fonts/comicneue/OFL.txt`) for captions and every label. The formula keeps a geometric maths face because Comic Neue's "t" reads as "†" (D12) | VERIFIED (S07) | One caption face for captions and labels; maths and numbers get their own faces; the font licence is on file before use |
| L14 | Sound design | **Selective, meaningful sound cues** | 115 cues cut to 51, with 14 removals logged with reasons. 65 stopwatch ticks cut to two runs on the beat. Accents retuned into the music's key (`SOUND_DESIGN_CUE_SHEET.csv`) | VERIFIED (S07) as a mix. **Listening NOT PERFORMED** | Every cue has a reason in the cue sheet; tonal cues are tuned to the music's measured key |
| L15 | Music | **Narration-first mixing and emotionally motivated automation** | Music 21.0 dB under the voice (K-weighted, voiced windows; per-section 19–23 dB). Ducking −6 dB, plus −4 dB at 1–4 kHz. 29 automation points tied to story beats (`MUSIC_AUTOMATION_MAP.csv`) | VERIFIED (S07) as measurement. **Listening NOT PERFORMED**; **licence UNVERIFIED** | Target 18–24 dB under the voice; every automation point names its story reason; always build a rights-clear master alongside |
| L16 | Final editing | **Independent visual, scientific and technical reviews** | Decoded-frame review found five defects that the automated checks had passed: an opening rest at 2.19 s, a schematic box, the Moon overlapping Earth, the formula glyphs, an undersized beat. Scene self-checks guard the science. ffprobe and loudness guard the technical side | VERIFIED (S07) | Three separate review passes, each with its own evidence file; a passed automated gate never replaces a decoded-frame review |

### 21.2 Workflow changes that follow (PROPOSED for Slot 03 onward)

1. **Reference sprint before art.** At least 2–3 inspected photos per object (L1, L3).
2. **Masters, then layers, then rig.** Run the Codex master runs in parallel, four at a time, on the first day. Claude cuts, registers and rigs them while Codex is drawing (L2, L4–L8).
3. **Moving proof per mechanism** before the cut. Keep each proof's clocks inside the cut so its checks stay valid (S07 `roughcut.py`).
4. **Gates added to G0–G8 (§18):**
   - **G-open:** an automated check of 0–7 s (L10).
   - **G-text:** the disclosure table (L12).
   - **G-mix:** the separation measurement plus the rights-clear master (L15).
   - **G-review:** three named reviews (L16).
5. **Library first.** Start from `04-shared-assets/` and `05-animation-engine/`, and record pinned versions in the project's `LIBRARY_PIN.md` (§16).

### 21.3 What Slot 07 did not prove

- No human has listened to Slot 07, and no muted-viewer or comprehension test exists.
- Retention and click-through effects are unknown; the film is unpublished.
- Two disclosure notes overlap at 13.75–15.2 s.
- The engine's `narration.py` is bound to one film: it loads the narration files at import.
- `S07/MASTER_ASSET_MANIFEST.csv` was never updated after planning.

These are tracked in `11-production-management/MASTER_PRODUCTION_DASHBOARD.md`.


## Appendix B: reference asset validator (PROPOSED standard; tested in this audit)

Written and run in a scratch environment during this audit; **not part of V15 and not stored in the project tree**. To use it: create a Python environment with `numpy`, `Pillow`, `scipy`; save the code as `validate_asset.py`; run `python validate_asset.py FILE [--canvas WxH] [--min-blob 400]`. It prints one JSON line per file and exits 1 on `FAIL`. Warnings do not fail a file; a human decides (§7.7).

```python
"""Asset acceptance check for layered PNG art (PROPOSED standard; tested on V15 assets in the scratchpad).
usage: python validate_asset.py FILE [--canvas WxH] [--min-blob 400]
Reports: mode, size, alpha range, alpha bbox, RGB-under-zero-alpha pixels, semi-transparent fringe share,
and connected opaque components (stray blobs). Exit 1 on FAIL."""
import sys, json
import numpy as np
from PIL import Image
from scipy import ndimage
def check(path, canvas=None, min_blob=400):
    im = Image.open(path); res = dict(file=str(path), mode=im.mode, size=list(im.size), fail=[], warn=[])
    if im.mode != 'RGBA': res['fail'].append('not RGBA')
    a = np.asarray(im.convert('RGBA')); al = a[..., 3]
    res['alpha_range'] = [int(al.min()), int(al.max())]
    if al.max() == 0: res['fail'].append('fully transparent'); return res
    ys, xs = np.nonzero(al > 8); res['alpha_bbox_ltrb'] = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    if canvas and list(im.size) != list(canvas): res['fail'].append(f'canvas {im.size} != {canvas}')
    hidden = int(((al == 0) & (a[..., :3].max(-1) > 0)).sum()); res['rgb_under_zero_alpha_px'] = hidden
    if hidden: res['warn'].append('non-zero RGB under zero alpha (loaders must crop by alpha, not RGB)')
    # NOTE: body alpha in generated art is often 253-254, not 255, so 'opaque' means >= 245
    semi = ((al > 8) & (al < 245)).sum() / max(1, (al > 8).sum());  res['semi_transparent_share'] = round(float(semi), 4)
    if semi > .25: res['warn'].append('large semi-transparent share: haze or soft fringe')
    lab, n = ndimage.label(al > 8); sizes = ndimage.sum(np.ones_like(al), lab, range(1, n + 1)) if n else []
    big = sorted((int(s) for s in sizes if s >= min_blob), reverse=True); small = [int(s) for s in sizes if 20 <= s < min_blob]
    res['components'] = dict(total=int(n), large=big[:6], small_20_to_min=len(small))
    if len(big) > 1 and big[-1] < .02 * big[0]: res['warn'].append(f'tiny detached component(s) {big[1:]} vs main {big[0]}: possible stray blob')
    return res
if __name__ == '__main__':
    args = sys.argv[1:]; canvas = None; mb = 400
    if '--canvas' in args: i = args.index('--canvas'); canvas = [int(x) for x in args[i + 1].split('x')]; del args[i:i + 2]
    if '--min-blob' in args: i = args.index('--min-blob'); mb = int(args[i + 1]); del args[i:i + 2]
    bad = 0
    for f in args:
        r = check(f, canvas, mb); print(json.dumps(r)); bad += bool(r['fail'])
    sys.exit(1 if bad else 0)
```

**Results on real V15 files** (re-run at the end of this audit; the project tree was not modified): `assets/v12rig/side_lift_00.png` clean; `assets/v11reg/side_body.png` 707 px of RGB under zero alpha; `assets/codex/aircraft_side.png` a 2,754 px detached component beside the 1,054,701 px main body; `assets/codex/aircraft_side_v15.png` no stray component but 3,250 px of RGB under zero alpha. **Calibration note:** generated art has body alpha 253–254, so "opaque" is defined as alpha ≥ 245; re-tune per generator. The validator checks hygiene only; it cannot see a visible disc, a seam or a different face, which need the human review of §7.7 and §17.
