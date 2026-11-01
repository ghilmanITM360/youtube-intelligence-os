# Video 004 — Production DNA and Original Reconstruction Blueprint (v3 text, checkpoint L, PARTIAL; numbers from integrated_v4)

Video `0ll9rEtoRrs` "The World's Safest Market Is Breaking", 1280×720, 24 fps, 24,298 frames (16.87 min). Source SHA-256 `8fd0c2bfd7b89d46e49280b7329626b7656dca7f5f2fd98c8046998af0c95b73`.
Built from `integrated_v4/` (v3 plus the boundary rule below; see also `PER_STATE` v4 files `per_state_specs_v4.csv`, `dna_statistics_v4.json`, `composition_family_specs_v4.csv`, which supersede the v3 files) (supersedes the v2-based `PRODUCTION_DNA_AND_BLUEPRINT.md`, which is kept as history). Status: `PARTIAL_STRUCTURE_RECONCILED`, NOT `CT_SCAN_COMPLETE`, audio `AUDIO_NOT_VERIFIED`.
Labels: MEASURED (computed from ledgers/frames), OBSERVED (seen in frames), INFERRED, UNKNOWN, CREATIVE_INSTRUCTION (guidance for new original work).

## 0. What changed vs v2 (evidence-backed only)
- 161 merge flags reviewed on before/after frame pairs: 158 MERGE_CONFIRMED, 3 UNCERTAIN (S0022, S0035, S0056, left separate). Blind control: 6/6 flagged pairs judged same-composition, 10/12 unflagged pairs judged different, 2/12 unflagged judged same (S0080, S0212: possible missed merges, NOT applied).
- 530 states are grouped into 370 compositions (158 confirmed merges + 2 split-sibling groupings). States and their events are preserved; compositions are a grouping layer only.
- Split children (S0089.*, S0097.*, S0116.*, S0475.*, S0466P/S0466, S0033) re-described from their own frames (`integrated_v3/split_child_corrections_v3.csv`). S0466 hard replace at f21628 is observed in sequential decode, so the earlier "inferred 21628" caveat is closed. S0033 has no visible infographic cut-in through f1294.
- All 143 unowned intervals (3,012 frames) re-reviewed with dense sheets (up to 12 frames each) plus per-frame diffs: 99 motion-in-composition, 13 continuous animation, 13 static/near-static, 6 hard-cut-ending, 6 third-party playback, 6 fade; 29 flagged limited by sampling; 13 end on a new composition in their last sampled frame (possible boundary corrections, NOT applied). Gaps are still not absorbed into states. For the first 48 priority gaps: Only 6 of the 35 earlier EMBEDDED_VIDEO intervals are third-party playback (221 frames); 24 are PDF/browser/screen scroll inside a composition. The 658-frame embedded-video figure in v2 was an over-label for those intervals.
- All 807 first-pass CONFIRMED candidates are now independently viewed (before/after frames at 560×315, one reviewer per row): 749 type OK (92.8%), 33 wrong type (4.1%), 25 no visible change (3.1%; 15 LOW, 10 MEDIUM confidence, mostly tiny highlight extensions). 25 types corrected (HIGH/MEDIUM confidence only). This is single-reviewer second pass at reduced resolution, not native-resolution frame-by-frame.

## 0b. Boundary rule (checkpoint L)
Rule: if the last frame of an unowned gap is an isolated one-frame jump (≥10% of pixels changed vs the previous frame and ≥3× the largest change in the 4 frames before), that frame is the first frame of the next composition and is reassigned to the next state (same convention as the 225 states that already start on a visible cut). Applied to 15 gaps (U010 U024 U031 U035 U044 U045 U074 U077 U088 U096 U099 U120 U123 U131 U141): each next state starts 1 frame earlier, each gap loses 1 frame. NOT applied to U059, U069, U073, U083 (steady converging motion, not a cut). Result: states 21,301 frames, unowned 2,997 frames (12.3%), tiling still 24,298. Rule is a measured heuristic; 1-frame boundary ±1 caveat stays. Gaps are still not absorbed into states.

## 1. Editing DNA (MEASURED)
| Metric | Value |
|---|---|
| States | 530 (31.4/min); median 1.12 s, mean 1.67 s, p10 0.29 s, p90 3.79 s, max 13.12 s |
| Compositions | 370 (21.9/min); span median 1.77 s, mean 2.47 s, p90 5.42 s |
| Edit events (excl. not-a-change/codec) | 996 (59/min); 853 in states, 143 in unowned gaps |
| Additive entry | 268 (26.9%) |
| Full replace | 252 (25.3%) |
| Highlight add | 118 (11.8%) |
| Draw-on / reveal | 94 (9.4%) |
| Text change | 52 |
| Pan/scroll | 32; zoom/scale 23; object motion 21; character animation 25 |
Type labels carry about ±4% uncertainty (second-pass wrong-type rate); 25 rows have no visible change at review resolution and are kept but flagged.
INFERRED: rhythm = hard cut to a new drawn composition, then build it up piece by piece (typical state 1 s, composition about 1.8 s), with highlights/draw-on for emphasis.

## 2. Visual DNA (MEASURED families, OBSERVED look)
State-frame share: F5 screenshot+character 26.9%, F2 character+prop 16.4%, F4 full-bleed screenshot/document 14.9%, F3 object/icon cluster 12.7%, F1 character-only 11.5%, F6 chart 7.0%, F11 composite 5.4%, F9 drawn scene 2.8%, F10 title/end 1.1%, F8 dark-UI 0.6%, F7 text card 0.3%.
OBSERVED: white canvas, flat marker-outline stick-figure presenters (skin-tone heads; brown-haired glasses man with green tie recurs; black-haired figure), green country characters with faces, globe, money bags, bond/cheque/debt-paper doodles, red handwritten emphasis text and arrows, third-party charts/PDFs/web pages inside the frame.
UNAVAILABLE: palette hex codes, typeface names, line widths (not sampled). Do not import values from other videos.

## 3. Motion DNA
- MEASURED (all 143 gaps, frames by class): motion-in-composition 1,668, continuous animation 517, hard-cut-ending 274, static/near-static 251, third-party playback 221, fade/transition 81. Hard cuts (>50% pixels changed in one frame) measured at f1056, 2718, 5877, 18221, 21983, 23669, all on the last frame of their interval, so the cut frame itself sits in the unowned interval; boundary ownership is NOT corrected.
- OBSERVED: laptop/PDF scrolling, red arrow travelling along a chart (S0466P), timeline bar growing with Year labels (S0097.2/S0116.2), money bags hopping (S0475.2), typed-in text.
- UNKNOWN: easing curves and layer coordinates (not measured).
- Three low-contrast fades (U042, U075, U080) show 0 frames above the 24-grey-level threshold: slow fades are invisible to the cut threshold.

## 4. Pacing, story, narrative-to-visual
MEASURED: 192 ASR sentences (Whisper base, historical 2026-10-12 pass, not listened to) map to states by time overlap (`phaseB/asr_sentence_to_state.csv`). 74% of sentence starts fall within 0.25 s of a state start vs 25% for shuffled timing (95th pct 30%): visual changes are tied to narration timing. Median 2 states per sentence; 61 numeric sentences identify where on-screen number evidence is expected (`has_number`). Wording/timing are ASR-grade and unverified by listening.
Story function per state is the first-pass reviewers' INFERRED note (field `visual_purpose`). A hook/claim-by-claim map and quality scorecard of the video are NOT produced; only the evidence-confidence scorecard in section 7.

## 5. Original reconstruction blueprint (CREATIVE_INSTRUCTION; build new assets)
1. Canvas: white 1280×720 (or 1920×1080), one composition per beat. Create an original presenter kit (2–3 poses/expressions each) and original icon/character set in a new hand-drawn style. Do not trace the source characters, mascots or doodles.
2. Beat grammar: cut to a clean composition; add 2–5 elements at 0.3–1.5 s spacing; one emphasis (underline/box/highlight or red handwritten number). Target composition median ~1.8 s with 3–6 s holds for data/punchline beats; ~22 compositions per minute.
3. Align visual changes to narration sentence starts (target: most within 0.25 s).
4. Data scenes: original charts from cited public data, source named on screen; zoom/pan into the region, then draw highlight.
5. Embedded footage: replace third-party clips with original drawings, licensed stock or documented-basis short clips.
6. Motion kit: pop-in (scale+fade ~4–6 frames), draw-on stroke, slide-in, in-frame scroll, arrow travel, pose swap, typed text, growing timeline bar.
7. QA: composition rate 22 ± 5/min; every composition has a focal element; every number has a source line; licence record per third-party asset.
Per-state guidance: `per_state_specs_v3.csv` (530 rows; layers, measured event frames, original prompt template, UNAVAILABLE for colour/typeface/easing). Family summary: `composition_family_specs_v3.csv`.

## 6. Source-to-claim map
Limited to the ASR numeric-sentence index above. Factual claim checking of the video's finance claims is out of scope here (see Finance Intelligence, untouched).

## 7. Evidence scorecard (of this package, not of the video)
| Area | Status |
|---|---|
| Frame tiling (states + gaps = 24,298) | MEASURED, validator PASS |
| Merge/composition grouping | 161/161 reviewed; 3 UNCERTAIN |
| Split children | frame-reviewed |
| Unowned gaps | 143/143 re-reviewed (single reviewer, 29 limited by sampling); 15 boundaries moved by rule; not absorbed |
| CONFIRMED candidates | 807/807 independently viewed (single reviewer, reduced resolution); 25 no-visible-change flags |
| ASR alignment | time-overlap only; not listened |
| Audio / AV | AUDIO_NOT_VERIFIED, AV_CERTIFICATION_BLOCKED |

## 8. Still not done
Native-resolution check of the 25 no-visible-change and 33 corrected rows; ruling on absorbing gaps; 29 sampling-limited gaps; ruling on possible missed merges (S0080, S0212); 6 gap-cut boundary ownership; colour/type sampling; listening/AV sign-off; live YouTube identity check; claim map and video scorecard.
