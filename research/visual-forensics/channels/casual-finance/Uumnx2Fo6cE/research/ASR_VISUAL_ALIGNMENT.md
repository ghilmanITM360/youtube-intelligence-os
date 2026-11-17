# ASR ↔ VISUAL ALIGNMENT — Uumnx2Fo6cE

**Status: PROVISIONAL_ASR_ONLY. ASR_ONLY_NOT_AUDIO_VERIFIED. Nobody has listened to the audio; wording and word timing are automated (openai-whisper small.en, local). Human listening NOT_COMPLETED; full audiovisual sign-off BLOCKED.**

## Method
- Transcript: local Whisper small.en with word timestamps (3,027 words, 196 segments). Cross-check against the registered earlier base-model transcript: 2,964 words matched in sequence, median word-start difference 0.02 s (asr/asr_crosscheck.json).
- Visual event time = PTS of the first changed frame of each of the 370 state-boundary events (MEASURED). Offset = visual time − nearest ASR word onset (negative = visual changes before the word).
- A timing relationship is MEASURED; any claim about editorial intention is NOT made.

## Result 1 — word-level alignment is not informative (honest null)
Speech is dense (~3.3 words/s), so some word onset is always near. Median |offset| 0.068 s; 246/370 (66.5%) events lie within 0.10 s of a word onset, versus 60.1% for random times (chance baseline, 5,000 draws). That is barely above chance, so word-level offsets must NOT be read as deliberate word-sync.
Offset distribution: median -0.037 s, p10 -0.15 s, p90 0.095 s; 181 events precede the nearest word onset by >0.04 s, 68 follow it.

## Result 2 — sentence-level alignment is real (MEASURED)
Using ASR sentence starts (195): across all state-boundary events 33.0% fall within 0.25 s of a sentence start (chance 10.3%). For the 174 full/large composition replacements, 58.0% fall within 0.25 s of a sentence start versus 10.3% chance. Large scene changes therefore cluster at ASR sentence starts; small additive changes are spread through sentences (they follow phrases/words).

## Numerical-claim contexts
48 state-boundary events have a digit/percent/dollar/million token within ±3 ASR words (median |offset| 0.065 s). Closest examples (ASR wording UNVERIFIED):

- EP0261 @ 325.500 s, offset +0.000 s, ASR "…% this summer, while the market rate…" — visual: A spiky-haired presenter appears at the right edge beside the transcript page.
- EP0533 @ 670.042 s, offset +0.002 s, ASR "…,000 new homeowners. That's a trade so…" — visual: Worried head, small house, money bags and red $3.1 BILLION text all removed; replaced by an empty canvas with a full-height green-tie presenter at right-centre.
- EP0259 @ 323.333 s, offset -0.007 s, ASR "…its pipeline at 4 .9 % this…" — visual: Right-hand page pane of the PDF viewer swaps to a different page of transcript text; thumbnails stay.
- EP0214 @ 255.250 s, offset -0.010 s, ASR "…homes since 2009. This month, 38 %…" — visual: Chart replaced by a small article-text screenshot with a presenter holding a pointer at lower right.
- EP0110 @ 130.750 s, offset -0.010 s, ASR "…out 1 .7 million home sales that…" — visual: A third house/tower/for-sale-sign cluster appears at far right, giving three clusters across the abstract.
- EP0108 @ 129.750 s, offset +0.010 s, ASR "…that wiped out 1 .7 million home…" — visual: A doodle cluster (small house, grey tower block, red for-sale sign) appears at left over the abstract text.
- EP0158 @ 192.208 s, offset -0.012 s, ASR "…added about 9%, so what happened is…" — visual: The article is removed and a smaller smiling stick figure stands alone at centre on blank white.
- EP0151 @ 184.292 s, offset +0.012 s, ASR "…its 2022 peak, but it's not because…" — visual: Chart and presenter are replaced by a yellow price-tag doodle with red dollar signs and a curved string.
- EP0012 @ 10.625 s, offset -0.015 s, ASR "…this in 2013. By their measure, it's…" — visual: Presenter jumps from large centre position with frown to smaller right position with flat neutral face and pointer; both red arrows vanish; chart re-laid out sl
- EP0055 @ 55.583 s, offset -0.017 s, ASR "…Mortgage rates just hit 7%. Higher rates…" — visual: Third dark news-card appears below-left, overlapping the stack.
- EP0567 @ 723.417 s, offset +0.017 s, ASR "…than $14 ,000. The only difference is…" — visual: Article page and pointer figure replaced by two small houses flanking a smiling spiky-haired figure's head, lower centre.
- EP0053 @ 55.042 s, offset -0.018 s, ASR "…is cheap. Mortgage rates just hit 7%.…" — visual: First dark-mode news-card (headline, thumbnail at right) appears at upper right of the mortgage papers.

## Silence and pacing
- No ASR pause longer than 1 s exists (asr_pauses_gt_1s = 0): narration is continuous over the whole 913.8 s speech span; visuals change underneath continuous speech.

## What is NOT claimed
- No human-verified wording, no audible-beat, music or sound-effect analysis (audio not listened to), no editorial-intention claim.
- Per-event rows: audio_visual_alignment.csv (370 rows); per-state ASR text: VISUAL_STATES.csv (asr_text_unverified).