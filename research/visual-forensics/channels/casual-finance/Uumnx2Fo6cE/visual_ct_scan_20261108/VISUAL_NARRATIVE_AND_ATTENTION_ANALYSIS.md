# VISUAL NARRATIVE AND ATTENTION ANALYSIS — Uumnx2Fo6cE

Narration references are ASR_ONLY_NOT_AUDIO_VERIFIED (local Whisper small.en; nobody has listened). Attention statements are PREDICTED SALIENCE HYPOTHESES from composition, not eye-tracking or retention data. No viewer metric is claimed.

## 1. Structure of the visual argument (INFERRED from ASR + states, per minute)
| Window | States | Dominant visual families | What the narration appears to be doing (ASR, unverified) |
|---|---|---|---|
| 0–60 s | 44 | F5 capture+presenter 16, F3 icon clusters 9, F11 5 | Hook: "58% more sellers than buyers", record buyer's-market claim; opens directly on a news-article capture with the presenter pointing |
| 60–180 s | 71 | F3/F2 doodles, F5, F6 charts | Mechanism #1: homeowners locked into low rates (Census and a working-paper capture); rate-lock visualised with house/tag/chain doodles |
| 180–300 s | 69 | F5, F3, F2, F10/F7 cards appear | Case study (Austin supply glut) then builders forced to cut prices; first title/text cards |
| 300–420 s | 51 | F5, F2, F4 | Builder earnings-call evidence: transcripts and a profile page; incentives/rate buydowns |
| 420–540 s | 74 | F2 19, F8 dark UI 7, F9 scene, sponsor props | Mid-roll sponsor block: handwritten offer, QR code, news-feed captures; yellow progress bar f10565–f12437 (440–518 s) |
| 540–720 s | 91 | F5, F4 documents, F8 | Policy experiments: mortgage-bond purchase, FHA premium cut (2015), cost figures in handwritten red |
| 720–900 s | 97 | F2, F5, F3, F6 | Property-tax cap example (2006 vs 2023 buyers), gift/inheritance down payments, working paper |
| 900–921 s | 10 | F5, F2, F1, F10 end card | Closing thesis, then a subscribe-style end card (OBSERVED end-card layout) |

## 2. How information is introduced (OBSERVED + INFERRED)
1. Source-first: the first frame is an article headline capture (identity evidence: a Sept-2026 news article); claims are shown on the page they come from before or while they are spoken.
2. Pointer + highlight: the presenter's pointer and drawn highlights/underlines direct reading inside long captures (≈ 90 state descriptions mention highlighting; 42 sub-threshold draw-on beats found).
3. Doodle metaphor for the abstract mechanism (rate lock, supply glut, subsidies) — generally placed after the evidence capture and kept on screen 1–3 s.
4. Numbers are re-typeset in big handwritten red next to the capture rather than left inside it (OBSERVED in states with "58%", "$3.1…", "4 in 10", "7%").
5. Comparisons are staged additively (counts of icons grow, two houses either side of a figure) rather than with split screens.

## 3. Escalation, callbacks and payoff (INFERRED)
- Recurring motifs: the pointer-holding presenter (60 states), house doodles (135 mentions), dollar bills (42), the documents icons (DEBT/TAX labels), the detective/magnifier (5) as a "check the claim" beat, the QR/progress bar as a single non-repeating block.
- Callbacks: the closing minutes reuse the house + figure composition from early states (continuity notes in VISUAL_STATES.csv). The final state is the end card held for the last frames.
- Payoff beats: scale-up of a doodle or a full-bleed drawn scene (F9: 6 states) tends to coincide with sentence starts (see ASR alignment: 58% of 174 large replacements start within 0.25 s of an ASR sentence start vs 10% chance).

## 4. Pacing and pattern interruption (MEASURED)
- 507 states, mean 1.59 s, median 1.25 s, 90th percentile 3.33 s; longest states: S0399 12.54 s (710.9–723.4 s), S0348 10.46 s, S0214 9.29 s — all dense article captures (F5) where the viewer is expected to read via highlights.
- 24.1 state-changing events per minute on average; windows range from 6 (final 60 s) to 33 per minute (a measured distribution; no claim is made about why the density varies).
- Pattern interruptions (INFERRED): a full-screen dark capture after many white-canvas states (F8 block at 420–480 s), a full-bleed drawn scene (F9), the sponsor block with a different layout, and the 12.5% of frames spent in zoom/scroll transitions.

## 5. Predicted salience (hypotheses)
- In doodle states the largest/most saturated item (gold/red/green prop or red handwritten number) is the first fixation candidate; the presenter face is second because of the high-contrast outline against white.
- In capture states, the highlighted/underlined region and the presenter pointer tip are the likely first targets because they are the only saturated elements on a grey/white text page.
- Attention competition: dense unreadable body text vs the highlight; resolved by the highlight draw-on animation (movement) which also marks the phrase the narration is expected to be on (INFERRED).
- NOT claimed: dwell times, retention, emotion, any biological response.

## 6. Narration relation (MEASURED timing, not intention)
Word-level offsets are not informative (speech is continuous and dense); sentence-level alignment is above chance for large changes. See ASR_VISUAL_ALIGNMENT.md.

## 7. Counterexamples and limits
- Some 12-s article captures change only via highlights; they are reading states, not cuts.
- Several additive entries come mid-sentence (e.g. icon additions), so "visual change = new sentence" is false for small changes (67% of boundary events are not within 0.25 s of a sentence start).
- Visual metaphors above are INFERRED from state descriptions; no creator-intent evidence exists.
