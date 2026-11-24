# 14 Coverage plan: what the directive requires, what is a defensible scope, what stays unexamined (2026-11-23)

**Directive text reviewed:** `Pasted text(20261123-055514).txt` (973 lines, SHA-256 `e38230526627e27b49c0f09c44dcac2cdba63fbcfe773c0f7370607d72668dc7`), the user-attached copy of the XKCD WHAT IF master directive.

## What the directive literally says about visual coverage
- 6.1: a coverage matrix for **every available video** with an evidence tier. DONE (`03_CORPUS_COMPLETENESS_REPORT.md`, inventory tiers): DEEP_VISUAL 1, TARGETED 43, STRUCTURAL 44, UNAVAILABLE 4.
- 6.2: measure and document style with frame evidence for every major finding. DONE on a 125-frame purposive sample plus 160 frames; book-art comparison NOT done.
- 6.3: motion "for each **selected** scene". Selected scope: pilot video, 16 camera-move candidate shots (sequences viewed this pass), the ten directive episodes (sampled).
- 6.4: 14 storytelling questions "for **every** scene". Read literally this means every scene of every video; no sample can satisfy it. **Not met.** It is met only in a limited form (subject, setting, function, graphics text, humour type) for 156 shots; the full 14-question form exists for none of the 719 audit shots, except partial answers in the ten-episode studies.
- 6.5: quantitative editing metrics "where evidence supports it". DONE from machine ledgers; shot counts are inflated by false boundaries.
The directive also says "do not stop after listing"; it does not say every one of 2,160 events must be interpreted. It does say Phase 7 should study ten named episodes and Phase 10 should use holdouts.

## Unit definitions (so counts are not mixed)
| Unit | Count | Meaning |
|---|---|---|
| Logical videos | 92 (46 long, 46 Shorts) | live public tabs 2026-11-23; media for 88 |
| Audit shots (machine boundaries) | 719 in 44 videos | 675 have a boundary; 44 are first shots; not independent of each other (clustered by video) |
| Audit events | 2,160 | machine-detected visual changes, all UNCLASSIFIED; many belong to the same shot |
| Campaign layer | 718 shots, 2,708 events in 44 other videos | earlier detector; separate |
| Viewed shots | 156 | three stills each; 16 of them also viewed as 9-frame sequences |
| Viewed science frames | 125 + 160 | purposive, claim-time frames |
| Frame sequences viewed | 16 shots x 9 frames at 0.25 s | this pass |
| Listened items | 0 | no audio tool |

## Defensible plan for what remains (proposal, not executed)
1. **Do not interpret all 2,160 events one by one.** They are machine-detected changes inside shots already described, not independent observations. Instead estimate event classes from a stratified random sample of about 300 events (strata: format x event kind x strength) with a written codebook and a second coder (independent reviewer needed for any claim beyond description).
2. **Shots:** finish the ten directive episodes first (122 of 260 shots already touched; 138 left), applying all 14 questions; then extend the stratified shot review until each of the four strata (format x strength) has about 100 reviewed shots, drawn at random (not "fewest-sampled videos first"), to estimate boundary precision to about +-10 points. Recall needs a different sample: random timeline intervals drawn independently of the detector.
3. **Sequences for motion:** every claim about a technique (zoom, scroll, whoosh transition, typed text, pop-on) needs at least 10 dense sequences across at least 3 videos and both formats; achieved so far only for the map pan/zoom (8 shots, 1 video), diagram whoosh (3 shots, 1 video), scale-down zoom (2 shots, 1 video), horizontal slide (2 shots, 2 videos).
4. **Audio:** listening pack `09_LISTENING_PRIORITY_ITEMS.csv` (16 rows) plus `14_LISTENING_PACK_ADDITIONS.csv` (SC02 and 8 random speech-onset checks) for a human or an audio-capable tool.
5. **Owner decision needed:** whether 6.4 must be satisfied literally (every scene of 88 videos; thousands of coded scenes) or on the sampled and ten-episode scope above. Until decided, 6.4 is recorded as NOT MET, not as complete.

## Stays unexamined
563 of 719 audit shots; all 2,160 events individually; 1,585 + 204 faint-layer events and sub-15 px changes; 718 campaign shots beyond earlier labels; book illustrations; unlisted/private videos; audio.

## Owner decision recorded 2026-11-23: Phase 6.4 is to be met LITERALLY
Owner answer (chat): "Literal chahiye". Scope therefore = every ledger shot of every video that has a ledger: **1,437 shots** (719 audit layer in 44 videos + 718 campaign layer in 44 other videos; 88 videos with media). The 156 already-viewed shots also need re-coding because the earlier coding did not answer all 14 questions. Codebook: `phase15_scene_coding/CODEBOOK.md` (fields q2 to q14 plus boundary check, on-screen text, narration check, confidence; q1 narration comes from the ASR in the context CSV). Method: cells of 3 stills per shot (`scripts/phase15_cells.py`), coded by same-model subagents, one file per video (`phase15_scene_coding/out/`), validated by script, spot-checked by the main session. **This is self-review, not independent review; the ASR is provisional; motion is only what three stills show (q5), unless a dense sequence exists.** Tranches: A = the ten directive episodes (260 shots: 125 audit + 135 campaign layer); B = remaining audit-layer videos (594 shots); C = remaining campaign-layer videos (583 shots). Events (2,160) remain machine-detected inside shots; a shot-level answer covers them only descriptively. Progress and honest counts are in `phase15_scene_coding/PROGRESS.md`.
