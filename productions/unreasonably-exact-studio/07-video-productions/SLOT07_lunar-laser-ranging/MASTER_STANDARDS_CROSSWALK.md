# MASTER_STANDARDS_CROSSWALK — Unreasonably Exact (UE) x HumanCraft V4 (HC) -> concrete actions for Slot 07

Written 2026-11-26. Sources read in full or in the sections cited: `UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md` (UE; ToC, exec summary, §1, §7-§8, §14 read; §5, §9-§13, §17-§18 used via the gate table and the cited rows) and `HumanCraft_MASTER_Animation_Director_V4.md` (HC; Part I §1-§12 in full, Part II §6-§8, §12 read). Both documents' own statements about what is *verified* versus *proposed* are kept: **UE tags (PROPOSED / UNVERIFIED) are treated here as tests to run, not facts.**

Precedence used in this project: owner brief > actual files and observed evidence > UE (channel pipeline, science, Codex handoff, QA gates) > HC (creative direction, animation craft, shot judgement) > templates. Where UE and HC disagree, the stricter rule wins and the choice is written in `DECISIONS.md`-style lines in `PROGRESS_LOG.md`.

## 1. Who leads what

| Production area | Primary | What the other guide adds | Slot 07 action | Evidence file(s) |
|---|---|---|---|---|
| Scientific accuracy | UE §9 (claims ledger, `state(t)` model, six-way object taxonomy: calculated / simplified / magnified / time-compressed / artistic / assumed) | HC §10 truthful visualisation: annotate non-scale schematics | Every on-screen number traces to `SCIENTIFIC_CLAIMS_LEDGER.csv`; Earth-Moon spacing labelled not-to-scale; stopwatch final reading asserted in code (2.56 s) | `SCIENTIFIC_CLAIMS_LEDGER.csv`, `scientific_model/`, `renders/proofs/P11/` |
| Character asset specs | Both | UE §7.3 parts/pivots/overlap fields; HC §4.2 on-model sheet, pose extremes, contact plan | ASTRO briefs carry parts list, pivots, overlap unit, pose set, identity rules; kneel is *stylised* (no photo evidence) | `codex_handoff/individual_asset_briefs/ASTRO_*.md`, `CHARACTER_CONSISTENCY_GUIDE.md` |
| Claude-Codex handoff | UE §7.6 request template, §8.5 protocol, §8.6 tests | HC §6 asset-first (layers, clean plates, overscan) | One START_HERE, 34 briefs each with the 16 mandatory fields, hash-verified package, integration manifest | `codex_handoff/`, `qa/handoff_audit.txt` |
| Rigging verification | Both | UE §7.5 defects-as-tests (seam at extremes, identity, component test); HC §4.5 real constructed animation, §4.3 foot plant | Rest / seam / lift / identity / component tests via `tools/validate_asset.py` plus moving proof P05, P06 | `codex_handoff/ASSET_ACCEPTANCE_TESTS.md`, `renders/proofs/P05..P06/` |
| Scientific model architecture | UE §9, §6 (three clocks) | HC §7 timing | narration clock / animation clock / model clock kept separate in `animation/uemotion` | `animation/uemotion/clock.py` |
| Shot selection | HC §6 decision tree, Part II §5 shot spec | UE §10 motion-design system | Each beat gets purpose, focal hierarchy, medium, transition; no default flash/glitch/zoom | `storyboard/FULL_VISUAL_STORYBOARD.md`, `look_dev/VISION_CARD.md` |
| Art direction | HC §2 Vision contract + three candidates | UE gate G5 look-dev | Treatments A/B/C rendered as panels, one chosen with reasons | `look_dev/` |
| Animation principles | HC §3 (12 principles), §4 | UE §7.4 secondary-motion rules (delays 2-4 frames, damped spring defaults are **UNVERIFIED**, tune by eye) | Motion contract per hero shot; ambient motion on the real clock | `animation/uemotion/`, proof reports |
| 2D / 2.5D construction | HC §4.1, Part II §6 and the decisive 2.5D test | UE §6 renderer architecture | Layer compositor with per-layer parallax, overscan, occlusion; a one-image zoom is labelled Ken Burns, never 2.5D | `animation/uemotion/layers.py`, P02, P03 |
| Editorial judgement | HC §2D (editorial vs animation review as two passes), §8 transitions | UE §14 phase 9 sync map thresholds | Two separate review passes recorded per proof and per cut | `qa/REVIEW_*.md` |
| Narration sync | Both | UE §11 (alignment, offset policy), HC §7 (audio-first, global clock) | Master = 92.53 s recording; local frame = global frame - shot start; sync map auto-generated; no global stretch | `narration/`, `timeline/` |
| Audio and captions | Both | UE §12-§13 (separation in dB, SFX licence rows, caption lint, safe band); HC §10 contrast and truthful captions | Generated cues only until rights verified; caption safe band tested against a 9:16 UI mask | `audio/`, `captions/` |
| Production QA | Both | UE §17-§18 gates G0-G8 + HUMAN rows; HC §2F 12-category scorecard | Scorecard scored only on what was actually watched; human rows stay NOT PERFORMED | `qa/CREATIVE_SCORECARD.md`, `MASTER_PRODUCTION_DASHBOARD.md` |

## 2. UE gates mapped to files (status lives only in `MASTER_PRODUCTION_DASHBOARD.md`)

| Gate | Needs | Slot 07 file | Human step? |
|---|---|---|---|
| G0 Contract | claims ledger, brief | `SCIENTIFIC_CLAIMS_LEDGER.csv`, `ORIGINAL_BRIEF_COMPLIANCE_AUDIT.md` | owner approved assumptions (recorded) |
| G1 Narration | clean take, aligned words, human listen | `narration/` | **listen = NOT PERFORMED** |
| G2 Animatic | animatic watched at phone size, owner approves | `storyboard/animatic/ANIMATIC_V1_REFERENCE_INFORMED.mp4` | **owner approval = NOT PERFORMED** |
| G3 Asset tests | validator + acceptance tests on every Codex file | `codex_handoff/`, `qa/asset_tests/` | art approval = owner |
| G4 Rig proof | moving proof on real range of motion | `renders/proofs/P04..P06/` | watch = owner |
| G5 Look-dev | three treatments, choice | `look_dev/` | owner approval |
| G6 Science proof | P07-P12 and model assertions | `renders/proofs/P07..P12/` | comprehension check = human |
| G7 Audio proof | stems, separation dB, licence rows | `audio/` | **listen = NOT PERFORMED** |
| G8 Full render | decode, freeze, frame count, isolated rebuild | `renders/` | no |

## 3. HC craft rules turned into checkable actions

| HC rule | Action in this project | Test / evidence |
|---|---|---|
| §2A Vision card | `look_dev/VISION_CARD.md` (audience effect, thesis, anti-generic rules, hero moments, restraint moments) | file exists, referenced by briefs |
| §2B Three candidates | Treatments A (illustrated documentary), B (premium motion graphics), C (hybrid) as rendered panels for the same 6 representative beats | `look_dev/panels/` |
| §2C Motion contract | table per hero motion: subject, cause, meaning, poses, path, spacing, pivots, overlap, proof criterion | proof report front matter |
| §2D two reviews | separate `EDITORIAL` and `ANIMATION` sections in every proof report | `ANIMATION_PROOF_REGISTER.md` |
| §2E worst-three defects | after every moving proof list three defects with timecode, root cause, edit, re-test | proof reports |
| §2F scorecard | 12 categories, thresholds: critical >=4, supporting >=3, no blockers; **score only what was watched** | `qa/CREATIVE_SCORECARD.md` |
| §4.3 foot planting | astronaut stance feet constant in world space; contact shadow tied to contact | P05 frame strip + foot-world-position plot |
| §4.5 real constructed | each proof states mechanism (layers / pose swap / mesh / procedural) | `ANIMATION_PROOF_REGISTER.md` column `mechanism` |
| Part II §6 decisive 2.5D test | differential layer motion, occlusion, overscan measured | P02, P03 numeric parallax table |
| §8 transitions are relationships | every cut has a stated relationship (match, handoff, hard) | storyboard `transition_out` |

## 4. UE rules turned into checkable actions

| UE rule | Action | Test / evidence |
|---|---|---|
| §7.6 request template | brief sections 1-16 in this project's order (see `codex_handoff/START_HERE.md`) | `qa/handoff_audit.txt` |
| §7.2 rig decision tree | per-shot construction method chosen from: rigid layers, hierarchical rig, mesh deform, pose replacement, frame-by-frame, procedural, 3D-assisted camera | `ASSET_GENERATION_TRACKER.csv` column `construction_method` |
| §7.3 `pivot: null` blocks integration | pivots certified by test, not statement | `PIVOTS.json` + seam test |
| §7.7 validator | alpha >= 245 = opaque, RGB 0 where alpha 0, stray components | `tools/validate_asset.py` (UE Appendix B standard is **PROPOSED**; thresholds re-tested per generator) |
| §8.2 naming | `snake_case` ids, no overwrite, statuses candidate / reference_only / approved / not_used / blocked; only owner sets approved | tracker status column |
| §8.5 protocol | hash package, validate, integration manifest, moving proof, owner review | `CODEX_PROGRESS.csv` |
| §17 human rows | listening, watching, phone test, owner acceptance cannot be closed by an agent | dashboard "Requires human verification" |

## 5. Unverified or proposed standards: what we test instead of trusting

| Proposal | Why unverified | Test planned |
|---|---|---|
| Overlap 8-12 px on 640x400 canvas (UE §7.3) | unit was ambiguous in earlier versions | briefs state overlap as a % of canvas width and the unit used; validator measures it where overlap layers exist |
| Spring defaults, breathing 0.25-0.3 Hz (UE §7.4) | practitioner defaults | tuned by eye in proofs; recorded as tuned values |
| Baked 2-3 frame eye lead (UE §7.3) | V15 verified only glance and blink | not used for Slot 07 (no face visible in helmet) |
| Alpha >= 245 opaque threshold | derived from one generator | re-measured on first Codex batch (Batch 0 calibration) |
| HC "110 techniques" library | library, not a checklist | only those that change meaning are applied |
| HC / UE scorecard thresholds | "house gate, not an external benchmark" | used as stated, with disclosure |
| Caption position vs Shorts UI | UE §13 says untested in V15 | Slot 07 tests against an explicit safe-band mask and says it is *our* mask, not a platform specification |

## 6. What this crosswalk does **not** claim

No gate is passed by this file. It maps obligations to actions and evidence paths; whether an action happened is recorded only in `MASTER_PRODUCTION_DASHBOARD.md`, `ANIMATION_PROOF_REGISTER.md`, `ASSET_GENERATION_TRACKER.csv` and `CODEX_PROGRESS.csv`.
