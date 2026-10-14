# Casual Economics — Deep Research Report

Status: **FULL_RESEARCH_COMPLETE** within sampled-forensic scope. Full audiovisual sign-off: **0/11** (not claimed). Research date: 2026-10-14. Branch `codex/casual-economics-forensic-research`, draft PR #25. Exact commits and CI results are recorded in Git; this file does not track them.

## 1. Scope and evidence

- **Sources:** 11/11 original MP4s with verified SHA256 and size, read-only in `~/Downloads/casual_economics`. 11 English auto-caption tracks (DS-000036). Japan, 2008 and Great Depression were re-hashed in this session and matched.
- **Structural packages, 11/11 PASS:**
  - Six historical packages: `data/extracted/forensic-analysis/casual-economics/2026-10-12/02_VIDEO_FORENSICS/`, ten masters, 18,091 rows, unchanged.
  - Five research packages: `02_VIDEO_FORENSICS/`, five masters, 2,083 rows. Big Short 55 checks; Greece, Japan, 2008 and Great Depression 49 checks each.
  - The two master scopes are separate and do not duplicate each other.
- **Sampled coverage added this session:**

  | Video | Point samples | Temporal sequences | Sequence frame entries | Beats |
  |---|---|---|---|---|
  | Japan | 252 | 31 | 269 | 15 |
  | 2008 | 179 | 31 | 295 | 13 |
  | Great Depression | 181 | 31 | 275 | 14 |

  The maximum gap between point samples is 4 s, plus a final tail frame. These are point samples, not shots or an exhaustive state census.
- **Not done:**
  - Direct audio listening (all audio evidence is SIGNAL_MEASURED plus ASR_INFERRED).
  - Independent second-reviewer visual QA.
  - Frame-exact easing or timing.
  - A complete fact-check of every claim.

## 2. Per-video packages

| Video | ID | Package location | Key file |
|---|---|---|---|
| Singapore | kbPauzdHhcI | historical | VISUAL_RECONSTRUCTION.md |
| Dubai | N9GUfsfiM4M | historical | VISUAL_RECONSTRUCTION.md |
| Ancient Rome | rl6ggpS13ao | historical | VISUAL_RECONSTRUCTION.md |
| Norway | xVhMZPiIIGs | historical | VISUAL_RECONSTRUCTION.md |
| Great Depression Europe | VTx478EUybo | historical | VISUAL_RECONSTRUCTION.md |
| Switzerland | 3tVMjRRXQIg | historical | VISUAL_RECONSTRUCTION.md |
| Big Short | Iwz0fhJWN9Q | research | VIDEO_REPORT.md |
| Greece | nr5dcBPACH0 | research | VIDEO_REPORT.md |
| Japan's Lost Decade | x_MZu-QF-6o | research (new) | VIDEO_REPORT.md, PACKAGING_AND_CLAIMS.md |
| 2008 Financial Crisis | APlGPpM-nBo | research (new) | VIDEO_REPORT.md, PACKAGING_AND_CLAIMS.md |
| Great Depression | qF3ekm9Gx_E | research (new) | VIDEO_REPORT.md, PACKAGING_AND_CLAIMS.md |

## 3. Channel production DNA — summary

Full detail is in `03_CHANNEL_DNA/CHANNEL_PRODUCTION_DNA.md`.

- **Visual:** simple outlined round-head characters placed on detailed painted environments. Three "stage" fields alternate with scenes: cream for charts, black for years and concept cards, white for prop diagrams. One consistent chart style uses green for gains, red for losses and a yellow highlight band. Emphasis comes from blurring or dimming the background, not from 3D.
- **Characters:** a single body grammar throughout. Identity is carried by accessories (hats, glasses, facial hair, badges). The expression set is small. Dialogue is done with pose swaps, not rigs. The host character changes from video to video. Metaphors sometimes require custom reaction drawings.
- **Assets:** recurring families (money bags, certificates, bank and tower icons, seals, FOR SALE signs, zigzag arrows, chalkboards, maps) plus prepared state variants (intact/wrecked, cracked/repaired). Environment plates are reused heavily within a video. Some assets appear across videos: the Dow 1929 chart, the breadline storefront, the crash grid, and the shared thumbnail template used by the 2008 and Great Depression videos.
- **Motion:** almost everything can be reproduced with keyframes: cuts, type-on, pop-ins, numeric counters, chart line draws, bar and pie builds, staggered lists, strike-and-correct, character slides and swaps, prop swaps, drops and rises, accumulation of duplicates, opacity fades, recolours, split-panel slides, wipes and whips, and camera pushes. No lip-sync, rigs or 3D were observed. Easing was not measured.
- **Editing:** a new visual proposition roughly every 1–4 s, about one per sentence. The pattern is a statement followed by a proof chart. Black year cards mark chronology. Endings reuse earlier scenes.
- **Storytelling:** the opening (≤30 s) presents a contrast or a magnitude, then poses a question. The video then rewinds and follows a chronological spine. Mechanisms are laid out as lists of 2–4 causes or as feedback loops. Abstract finance is shown through literal metaphors (bubble, zombie loans, anvil of debt, dart-board stock picking). Dramatized skits carry part of the story. Videos end with lessons, a present-day parallel and a referral to another video.
- **Audio:** continuous non-silent soundtracks (measured). Music credits are mostly Kevin MacLeod. Narration, pauses and SFX are not verified.
- **Packaging:** four title formulas. The thumbnail system is a big outlined headline, a large distressed character, a central symbol and a small secondary group.

## 4. Production blueprint

`05_PRODUCTION_BLUEPRINT/ORIGINAL_PRODUCTION_BLUEPRINT.md` covers:

- originality guardrails;
- the 9-stage pipeline;
- script and act templates;
- the character system with pose and expression libraries;
- asset library folder structure and reuse estimates;
- eight layered scene templates;
- eighteen keyframe movement recipes with suggested durations;
- audio-sync and editing rules;
- a QA checklist;
- a thumbnail and title kit.

Custom drawing is required for poses, expressions, one-off metaphors and environment plates. Everything else can be animated from static layered originals.

## 5. Performance and virality — summary

Full detail is in `04_PERFORMANCE_RESEARCH/PERFORMANCE_AND_VIRALITY_RESEARCH.md`.

- **Tiers** (lifetime views/day vs. median): STRONG — Great Depression, Big Short, Singapore (provisional because the video is young). TYPICAL — Greece, 2008, Switzerland, Rome, Japan. WEAK — Dubai, Norway, Europe Depression.
- **SUPPORTED:**
  - One evergreen breakout (Great Depression, 3.1 M views, ≈57% of all channel views) dominates. It is still earning ≈1,300 views/day.
  - The production style is near-constant across videos, so style alone does not explain the 60× spread.
  - A visible source list in the description did not determine reach.
- **PLAUSIBLE:**
  - Canonical high-demand event titles help.
  - The April 2025 tariff crash and Smoot-Hawley news cycle amplified the Great Depression video. Trends peaked 2025-04-03/09.
  - Very low-search topics (Switzerland, Greece) relied on recommendations. Traffic source is not known.
- **WEAK_EVIDENCE:** question titles underperform.
- **UNKNOWN:**
  - The effect of the thumbnail template. It appears on both the best and the worst video.
  - CTR, retention, traffic sources, RPM and subscriber conversion.
- **Counterexample:** the Europe Depression video was uploaded while "great depression" interest was at its local peak, yet it is the weakest video.

## 6. Quality gaps

Status of the historical six:

- Their known gaps are already documented and partially supplemented in their own reports: Switzerland, Norway, Singapore and Big Short semantic-boundary misses, Europe's three failed targeted seeks, and Dubai's 1983/1985 caption-versus-screen discrepancy.
- No historical package was regenerated.
- Remaining limitations are in `06_VALIDATION_AND_HANDOFF/QA_LIMITATIONS_REGISTER.md`.

New factual issues found in this session:

- Japan: on-screen typo "TECHOLOGY" at 804 s.
- Great Depression: crash grid shows -90% while later chart labels show -70% and -68%.
- 2008: dramatized office dialogue.
- 2008 and Great Depression: no source notes in the descriptions.
