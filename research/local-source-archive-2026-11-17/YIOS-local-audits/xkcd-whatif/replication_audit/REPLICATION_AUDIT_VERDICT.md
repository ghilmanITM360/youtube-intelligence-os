# REPLICATION_AUDIT_VERDICT — xkcd's What If? (2026-11-14)
Consolidated answer for Phases 3-12 of the master prompt. Phases 1-2 are in DATA_INVENTORY, SOURCE_COVERAGE_REPORT, EXISTING_RESEARCH_AUDIT, CHANNEL_MASTER_ANALYSIS, REFERENCE_VIDEO_DATABASE.csv. Not separately written: per-phase files such as SHOT_BY_SHOT_BREAKDOWN.csv (the equivalents already exist: `videos/<id>/tables/state_ledger.csv`, 5,458 states, and `asset_library/_channel/motion_windows/`), and nothing new was rendered today.

## Premise check
The master prompt assumes 3D-style craft (rigs, 3D camera, Blender). The measured evidence says this channel is **flat 2D**: off-white canvas (~#F9F9F9), ~8 px stroke at 1080p, single-stroke stick figures, pop-on in 1 frame (38% of entries) or hard cut (23%), linear 6-frame dissolves, locked camera by default (moves are <=4% of events, 9-12 frames, blurred, eased), 24 fps, 1920x1080 and 1080x1920. So Blender/3D rigging is NOT required; the difficulty is editorial (consequence-led drawing), original art, and audio. Authoring software of the source is UNKNOWN.
Also note: the channel is the official adaptation of Randall Munroe's book, produced by Neptune Studios LLC. A "very close" clone of look and scripts has brand/IP risk. Repo policy already says learn the system, build an original character, no 1:1 copy. Book text must not be reused.

## Phase 3-8 findings (labels: OBSERVED / INFERRED / UNKNOWN)
- Camera: OBSERVED locked default, blurred eased pans/zooms 9-12 f. INFERRED 2D transforms. UNKNOWN true curves.
- Entries: OBSERVED pop-on, cut, draw-on, type-on, pose swap. Dissolves exactly linear 6 f (13 windows, 0 overshoot).
- Template reuse: OBSERVED narrator lecture frame pixel-identical in 18/24 long openings, layer-level not whole-frame.
- Opening: OBSERVED 2.0 s opening card (48 f) + 10 s red end screen (240 f), 288 f in 40/44.
- Character: single-stroke unfilled round head, angular joints, pose-led expression (from the chair-test audit and model sheets). Needed for an original character: model sheet, turnaround, expression and pose library, modifier kit (hats, props). A rig is optional because the source uses pose swaps.
- Storytelling: titles are extreme-scale hypotheticals; Shorts re-use long-video narration (38/40 Shorts are excerpts). The deeper hook/payoff structure was NOT re-studied today. ASR-based timing is uncertified.
- Physics/science: book-derived answers are real science; original assets would need real references per object. Not tested.
- Sound: UNKNOWN entirely. No listening, no SFX/music inventory, no licensed library.

## Phase 9 scorecard
| Category | Weight | Score 0-5 | Weighted | Evidence |
|---|--:|--:|--:|---|
| Reference video coverage | 10% | 3 | 6.0 | 88/91 local, 70 ingested, 29 visual-closed, 0 full; independent ~24L+11S |
| Shot-level motion analysis | 15% | 3 | 9.0 | every decoded frame measured for 44 gated videos; only 13 motion windows, easing UNAVAILABLE; 6.7% frames unverified |
| Animation technique understanding | 15% | 3 | 9.0 | pop/cut/dissolve/draw-on grammar measured and held-out tested; authoring software UNKNOWN; v3/v4 rule changes untested |
| Character rigging feasibility | 10% | 2 | 4.0 | style is single-stroke stick figure with pose swaps (simple), but no original character or pose set exists |
| Storytelling understanding | 10% | 2 | 4.0 | transcripts + 91-question book extraction exist; no verified structural study; ASR uncertified |
| Asset construction capability | 10% | 1 | 2.0 | no asset generated, no image model chosen, no asset QC |
| Camera and compositing capability | 10% | 3 | 6.0 | PIL+ffmpeg composites pass machine checks in two layouts; no Remotion/Blender (not needed for flat 2D) |
| Sound design capability | 5% | 0 | 0.0 | no listening, no library, no music or SFX study |
| Rendering and reproducibility | 10% | 3 | 6.0 | timeline JSON + sha256 + ffprobe; 8 s only; no long-form render |
| Quality-control evidence | 5% | 3 | 3.0 | held-out protocols and validators; human review pending; chair-test failure shows QC is needed |

**Readiness = 49%** (project heuristic, not a measure of the creator's quality). Band: 40-59% = major knowledge and implementation gaps.

## Phase 10 gaps (severity, blocks pilot?)
| Gap | Sev | Blocks 10-20 s pilot | How to close |
|---|---|---|---|
| Original character art (model sheet, poses, expressions) | Critical | yes | choose image model (owner), generate CHR-001, check consistency over 10+ poses |
| Human playback review of existing proofs (P8/P9) | Critical | yes | owner or reviewer watches both MP4s, scorecard |
| Narration + sync (no listening capability) | Critical for full video | no for silent pilot | owner narration file + human listener |
| Sound design / music / SFX library | High | no for silent pilot | licensed or original set, document licences |
| Consequence-led drawing skill (chair test failed) | High | yes | storyboard test against reference fingerprint, redo chair test |
| Easing curves of pans/zooms | Medium | no | more motion windows, fit curves |
| 2026 long journey format untested; alkJ7xScBiw no source (yt-dlp absent) | Medium | no | owner supplies file |
| Long-form full render (3 min) never done | High | no for pilot, yes for production | scale compositor, render 60 s then 3 min |
| Source authoring pipeline unknown | Low | no | not needed |
| Per-video "viewed" claims not re-audited after today's decode-failure finding in another channel | Medium | no | spot-check 5 xkcd review sheets |

## Phase 11 status
No new proof built today. Existing proof (8 s, silent, 16:9 + 9:16, machine PASS) uses the source-style layout and a placeholder pop-on set; it is not our original character and has no audio, so it does NOT count as replication proof. Next pilot spec: 12 s, original narrator + one object interaction + one dissolve + one eased pan, original narration line, rendered at 1080p24, compared against 3 reference windows with a 10-point scorecard.

## Phase 12 answers
1. Enough data about the channel? **For visual style: yes (about 35 independent videos, 91/91 census). For audio and narration timing: no.**
2. Fully analysed videos: **0** CT-scan complete; **29** visual-only closed; 44 partial gates; 70 ingested.
3. Demonstrably learned: canvas/line/palette, state rhythm, pop/cut/dissolve grammar, template reuse, 9:16 re-layout, export spec.
4. Only theoretical: easing curves, typography match, character motion library, busy/calm drivers beyond correlation, story structure.
5. Reproducible with working code now: 1-frame pops, linear dissolves, red-circle pop, 16:9 and 9:16 layouts (8 s silent proof, machine checks only).
6. Missing: original character art, audio listening/sound, long-form render, human QC, narration sync.
7. Original character with comparable sophistication? Plausible because the style is simple; **UNPROVEN**, nothing exists.
8. Pacing, camera language, editing: rhythm and grammar yes (silent animatics RT2-RT4 pass); storytelling and audio quality no; chair-test failure shows editorial quality is not automatic.
9. Full-length video today: **no**.
10. Remaining: owner picks image model, generate and approve character set, human review of proofs, pilot above, audio plan, then 60 s and 3 min renders, then rerun this scorecard.

## Verdict: CONDITIONAL GO for a silent 12 s original-character pilot only. NO-GO for full-length production.
Readiness 49% (major gaps). Verified strengths: measured visual system, reproducible machine-checked renderer. Biggest risks: character art, sound, editorial quality, and brand closeness.
