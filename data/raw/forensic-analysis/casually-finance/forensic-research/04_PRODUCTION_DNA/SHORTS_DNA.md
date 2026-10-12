# SHORTS DNA — 9:16 production patterns (6 of 8 selected Shorts)

_Status: **PARTIAL**. Built from the six selected Shorts with local media (`2EZzwupIa80, YGC3ao005as, PxgCsLSf-w4, 6S3PzAUFnXQ, rSa2aziEsAI, JsK53moCyZA`); `turJ6VMfUjI` and `Qof71Ef-3EU` are MISSING_LOCAL and not covered. Evidence: `03_MASTER_DATA/MASTER_*.csv` (308 motion rows, 353 measured sync offsets, 389 asset rows across videos). Labels: OBSERVED = read from frames/tables; MEASURED = computed; INTERPRETATION = reviewer judgement. No claim about CTR, retention or causality is made._

## 1. Format and timing (MEASURED, every frame decoded)
| Video | Title | Dur s | fps | First word s | Shots/min | Median shot s | States/min | Median state s | Words/min |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2EZzwupIa80 | Nothing Forces the Government to Fix The $ | 75 | 24 | 0.00 | 8.0 | 6.46 | 42.3 | 0.5 | 190.9 |
| YGC3ao005as | We're Fighting A Battle Against the Market | 63 | 24 | 0.00 | 3.8 | 16.25 | 45.7 | 0.46 | 188.2 |
| PxgCsLSf-w4 | Somebody Is Quietly Repricing America | 65 | 24 | 0.00 | 6.5 | 8.75 | 49.0 | 0.46 | 190.9 |
| 6S3PzAUFnXQ | America's Debt Hasn't Broken... Yet | 69 | 24 | 0.00 | 7.8 | 5.92 | 50.5 | 0.52 | 200.0 |
| rSa2aziEsAI | Why Japan's Economy Is Awful | 60 | 30 | 0.00 | 11.9 | 4.07 | 44.6 | 0.77 | 212.5 |
| JsK53moCyZA | The SpaceX IPO Nobody Can (Actually) Expla | 43 | 30 | 0.00 | 4.2 | 8.53 | 79.5 | 0.37 | 186.5 |

- All six are 720×1280, 24 fps (30 fps for `rSa2aziEsAI` and `JsK53moCyZA`) and 43–75 s long; narration is continuous (first word at ≈0 s in each) at ≈187–213 words/min.
- A new visual *state* (caption word-chunk, pop-in, highlight step) arrives about every 0.4–0.8 s (median); a new *shot* (new composition) every 4–16 s. The pace is carried by small in-shot state changes, not by cuts.

## 2. Hook pattern (OBSERVED)
- Narration starts on frame 0 with the thesis or a dated fact; no logo, intro or greeting.
- First visual is a single concrete object on white: a sunglasses-wearing map character (`2EZzwupIa80`), a plain canvas with a dated-fact caption (`YGC3ao005as`), hand-lettered "30 years" (`PxgCsLSf-w4`), a debt-clock screenshot with a dollar figure (`6S3PzAUFnXQ`), a joke bubble from a Japan character (`rSa2aziEsAI`), a presenter figure then a comparison bar chart at ~1.3 s (`JsK53moCyZA`).
- Evidence objects (screenshots, charts, documents) enter within the first 10 s in 5 of 6 Shorts (see `VISUAL_RECONSTRUCTION.md` §1b of each video).

## 3. Caption system (OBSERVED)
- A burned-in hand-lettered caption shows 1–4 words at a time and is replaced as the narrator speaks (`TEXT_SWAP` is 71 of 308 motion rows, 23%; `CAPTION_CHUNK` appears in 5 of 6 Shorts). Key words are occasionally recoloured red or enlarged (`TXT_RED_BIG`, 3 Shorts).
- In `2EZzwupIa80` captions also *accumulate* into a stacked key phrase ("the investor / who broke the Bank / of England") instead of swapping.

## 4. Motion vocabulary (OBSERVED labels, 308 rows; easing NOT_ASSESSED)
`CUT` 86 (28%) · `TEXT_SWAP` 71 (23%) · `POP_IN` 55 (18%) · `TEXT_REVEAL` 15 · `DRAW_ON` 14 · `ZOOM_IN` 8 · `LOOP_ANIM` 8 · `HIGHLIGHT` 7 · `SLIDE` 7 · `HOLD` 6 · `REPOSITION` 5 · `SCROLL` 5 · `POSE_CHANGE` 4 · `EXIT` 4.
- Objects appear by pop-in or cut, rarely by tweened movement. Highlighting is a marker sweep that follows the words being read (word-synced), typically over a screenshot of the source text (`2EZzwupIa80`, `YGC3ao005as`).

## 5. Recurring asset kit (OBSERVED)
- In 6/6: hand-lettered text (`TXT_HANDLETTER`) and a stick-figure host. In 5/6: pointer, speech bubble, caption chunk. 4/6: percent icon, red box. Country/map characters with eyes and stick legs (USA in 3 Shorts, Japan in 2) carry the "character" role; the same USA character wears pixel sunglasses in `2EZzwupIa80`.
- Sources are screenshots (CNBC/Reuters/WSJ/CRFB/Treasury/Hustle Fund/Genius pages), press photos, and original drawings on a white canvas — technique classes: ORIGINAL_DRAWING + SCREEN_CAPTURE + COMPOSITED_STILLS + MOTION_GRAPHICS. Press-photo stills appear in 2 Shorts (`2EZzwupIa80`, `YGC3ao005as`); no embedded video-footage clips were identified in the reviewed states.

## 6. Audio–visual alignment (MEASURED, ASR timing ±~100 ms)
- 353 visual events matched to the nearest spoken word: 170 fall *during* a word (48%), 138 *on* the word start (39%), 30 before it (8%), 15 after it (4%); median offset +85 ms (visual just after the word onset). Visuals therefore follow the narration closely rather than leading it.
- Audio: narration-only on the signal evidence — pauses drop to very low noise floor or near-digital silence in 5 of 6 Shorts (`JsK53moCyZA` has non-speech sound in 2 of 3 pauses); no SFX/music events were detected beyond speech transients. **Not an auditory listen**; do not read this as proof that no music exists.
- `2EZzwupIa80` uses ~0.5 s pauses around the payoff sentence ("It is an invoice.", pauses at 68.3–68.9 s and 69.6–70.1 s).

## 7. Structure and ending (OBSERVED / INTERPRETATION)
- 4–9 semantic beats per Short; the usual order is HOOK → EXPLANATION/EVIDENCE → CONFLICT/TWIST → PAYOFF/TAKEAWAY (see `MASTER_SEMANTIC_BEATS.csv`).
- Endings: no end card, subscribe prompt or loop device in the five Shorts annotated as such (`2EZzwupIa80`, `YGC3ao005as`, `PxgCsLSf-w4`, `6S3PzAUFnXQ`, `JsK53moCyZA`); `rSa2aziEsAI` ends on its closing red-X graphic (no CTA noted). `JsK53moCyZA` stops mid-reveal (the Nasdaq rule is introduced but not explained).

## 8. Packaging link (OBSERVED)
- Every Short's public thumbnail carries its own two-line headline in bold black rounded sans on white with one recurring character; headline wording differs from the title in 6/6. ASR check: title/thumbnail keywords such as "battle", "quietly", "yet", "collapse", "explain" never occur in the narration (see each `PACKAGING.md`). Packaging copy is written separately from the script.

## 9. Original-content principles derived (INTERPRETATION; not a copy of any video)
1. Start narration on frame 0 with one claim and one concrete object on screen.
2. Carry pace with small state changes (word-chunk captions, pop-ins, highlight steps) and reserve cuts for new evidence objects.
3. Show the source (screenshot + marker sweep synchronised to the read-out words) so claims are visibly attributed.
4. Use one reusable character kit of your own design for jokes and metaphors; keep the canvas white and sparse.
5. Put a short pause (~0.5 s) before and after the payoff line; end on the thesis graphic without an outro.
6. Write the thumbnail headline and the title as two different promises; do not let packaging promise more than the script shows (e.g. "collapse").

## 10. Gaps
Two Shorts not analysed (media missing); ASR is Whisper-base (proper nouns/numbers unverified); audio not listened to; easing not assessed; thumbnails not tested at mobile scale; no retention/CTR data exists in public metadata.
