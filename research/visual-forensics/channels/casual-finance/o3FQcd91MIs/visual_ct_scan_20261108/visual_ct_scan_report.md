# Visual CT Scan report — Casual Finance · `o3FQcd91MIs` · "Why The Dumbest Investors Win (it's not why you think)"

Mode: `DEEP + CT_SCAN + RECONSTRUCTION` · Date: 2026-10-24 · Machine A · sha256 prefix `82ab2b63` · 1280×720, CFR 30 fps, 277.93 s, 8,338 frames, H.264 + AAC.
Evidence folder (outside Git): `/Users/ghilmankhan/YIOS-local-audits/2026-10-24-o3FQcd91MIs-deep-ct-scan/`.
Status vocabulary: `MEASURED` (computed from frames) · `OBSERVED` (seen in viewed native frames) · `ESTIMATED` · `INFERRED` (interpretation) · `UNAVAILABLE`.

## 0. Verdict (see `quality_gate.json`)

`final_video_status = VISUAL_ANALYSIS_COMPLETE_WITHIN_DECLARED_COVERAGE` for the visual domain; **`CT_SCAN_COMPLETE` is NOT claimed** (see §9: the 8,338-frame measurement is exhaustive, but native-frame *viewing* covered 76 state frames + 12 transition windows, not every frame; and the audio gate is pending human listening). `FULL_AV_SIGNOFF_COMPLETE` = **NO**.

## 1. Source identity and what was independently checked

| Check | Result | Label |
|---|---|---|
| SHA-256 of the local MP4 equals the registered hash | match | MEASURED |
| Title, duration (277.93 vs public 278 s), 16:9 long-form | consistent | MEASURED |
| On-screen content matches the title question and the "Casual Finance" end card | S003.0, S011.0, S021.4 | OBSERVED |
| Registered thumbnail (`62fc9699…`) viewed: same lead character + "Dave vs Warren Buffett" line chart, no headline words | consistent with the video's own S005.3 chart | OBSERVED |
| Live YouTube page/thumbnail equivalence | not fetched (no acquisition) | UNAVAILABLE |
| Frame timebase | CFR, PTS delta 0.033333 s for all 8,337 intervals; first PTS = 1/30 s so frame *i* has PTS (*i*+1)/30 | MEASURED |

Prior evidence (Oct 12 `02_VIDEO_FORENSICS/o3FQcd91MIs`, `PASS_STRUCTURAL`) was treated as a historical input, **independently re-measured**, and spot-verified against viewed frames. It was not copied as truth.

## 2. Temporal coverage

- **Whole video, every frame**: 8,338/8,338 frames decoded and diffed (320×180 gray, changed-pixel fraction at threshold 10, plus mean-abs-diff). `tables/frame_metrics.csv`. MEASURED.
- **89 change episodes** found (threshold ≥0.06% pixels, ≤3-frame gap merge). **All 75 prior state boundaries are independently reproduced** (0 missed). 12 extra episodes are ≤0.31% of pixels and fall on I-frames/GOP positions (periodic every 120 frames ≈ 4.0 s, plus a further 36 micro-groups at the same spacing) → classed `CODEC_REFRESH_ARTIFACT`, **not** content events. MEASURED.
- 87 of 89 episodes are **one frame** long; one is 2 frames (36.03–36.07 s, a codec-refresh episode); one is 3 frames (the 2-frame black dip at 241.13–241.17 s + the arrival frame). See §6.
- PySceneDetect (`scenedetect-headless 0.7.2`) was validated on a synthetic clip only; per skill rule it is a *candidate* detector and was not substituted for the frame-diff measurement or the visual confirmation.
- **Visual review of native frames** (viewed by the analyst): all 76 state representative frames (13 labelled sheets) + 12 frame-by-frame transition windows (3–6 consecutive native frames each) + thumbnail + a contrast-stretched crop. Frames between are measured but not individually viewed (no change > threshold means identical content; MEASURED).

Blind spots: changes smaller than ~35 px of a 320×180 grid (≈0.06%) are below the floor (a blinking sparkle, e.g., on the trophy, could hide here); on-screen text below ~8 px in a 1280×720 frame (small captions, UI micro-text) was read by vision only where legible and is flagged unverified where not.

## 3. Shot and state structure (MEASURED)

- **47 shots**, **76 visual states**; median state 3.35 s, mean 3.63 s, p10 1.57 s, p90 5.63 s, min 0.67 s, max 10.83 s. Median shot 5.20 s.
- Change cadence (new states per minute): 0–15 s **24**, 15–30 s **20**, 30–60 s **18**, 60–120 s **15**, 120–180 s **19**, 180–240 s **14**, 240–278 s **12.6**. The cold-open is the densest.
- Background class by duration: near-white canvas 233.6 s (84%); hard-black beats 8.07 s (3 holds); dark UI cards (search/quote/AI overview); 4 full-field coloured cards/scenes.
- 66 of 76 states carry on-screen text.
- **Shots ≠ states ≠ pose changes ≠ typographic events** (skill rule): here a "state" is any stable composition; a shot groups states with one narrative purpose. Pose changes occur only inside shots at hard replaces. No camera movement exists.

Full ledgers: `shot_ledger.csv` (47), `visual_states.csv` (76), `visual_event_ledger.csv` (75 events, with before/after state, frame index, PTS, changed-region bbox).

## 4. Art direction, illustration and colour

- **Style (OBSERVED):** flat 2D marker-doodle. Stick figures with oversized round heads, irregular thick black outline, flat fills, no shading or perspective; third-party material (photos, UI captures, logos) is placed as rectangular cut-outs on the same canvas. The mix of crude drawn characters with real screenshots/photos *is* the comedic contrast engine (INFERRED function).
- **Palette (MEASURED, k-means on 10 frames):** canvas `#FCFCFC` (90–94% of pixels in character states); skin `#F2D5B6`/`#EED1B7`; black beat `#110F10`; dark UI `#1E2021`; definition-card blue `#90B7F9`; beach scene tan `#DEBA9B`/`#EFD2B2` with sky `#CBE9F9`; chain-restaurant beige `#E1D4B3`; accents gold `#EAAD2B`, green `#4FAE57`, red `#E53A2D`. Palette discipline: neutral field + 1–2 saturated accents per state.
- **Negative space (MEASURED):** median non-canvas content only **4.05%** of pixels on white-canvas states. Focal subject sits low/centre-left; text and props to the right (centroids in `visual_states.csv`).
- **Typography (OBSERVED; font names INFERRED, not asserted):** two voices — handwritten script (name tags, "When Market is ↑/↓", asides, wordmark value "Beta: 1.33", "33% More Volatile") and a rounded comic-style sans for typed statements/questions. Hierarchy by size only (large pose + tag, small caption asides at ≈8–10 px). A second line appears under the first on a later cut rather than animating in.
- **Annotation grammar (OBSERVED):** hand-drawn arrows (pointer to head/subject), red circle (emphasis on a chart peak/ratio), red box (cash-balance bars), red X (cancel), jagged zig-zag divider (split-screen), thick brush arrow + caption (time skip), equals-sign pairs (bull vs bear contrast).
- **Production artefact observed with contrast stretch:** an inserted image (the later TESLA logo card region at f1141) carries a background ≈1 level brighter than the canvas (`#FDFDFD` vs `#FCFCFC`), visible only at 16× contrast; a similar faint matte appears near the Buffett photo in S005.0/S005.2. Cause INFERRED: matted raster with non-identical white. Irrelevant to viewers; useful for reconstruction (match canvas exactly or key it out).

## 5. Composition and cinematography

- **Camera:** none. No pan, tilt, push-in, rack focus, shake, or parallax (MEASURED: zero continuous change). The "zoom" at S001.0→S001.1 is a one-frame swap: frame f40 (small figure) → f41 (large figure + trophy + banner) (OBSERVED, frames viewed).
- **Framing:** static medium-wide on empty canvas; characters never touch the frame edge except in full-bleed scenes (S018, S020), where the lead sits dead-centre in a tableau (INFERRED: a payoff "money shot" for the A/B contrast).
- **Scale as emphasis (OBSERVED):** lead character appears at three scales: tiny at opening/evidence cards (≈25% frame height), medium with props, and very large with a long name tag (S005.7, S017.6) to stress the "outperformer" label.
- **Rhythm devices:** (a) cold-open rapid prop pops; (b) repeated callbacks (the same chart/pose reused: "Yes! Yes! Yes!" doodle appears at 192.8 s and 232.1 s; the coin blob at 13.3 s and 266.4 s; the "Market is Rigged" pair at 179.97 s and 246.8 s) → recurrence as structure; (c) three black holds (3.3 s, 2.1 s, 2.7 s) bracketing the central question card.

## 6. Motion and animation (CT-scan finding)

| Class | Count / duration | Evidence |
|---|---|---|
| One-frame hard replace (pose/prop/text/card swap) | 74 of the 75 state-to-state events | MEASURED peak pixel fraction per event in `visual_event_ledger.csv` |
| Two-frame black dip, then new full-bleed scene | 1 (frames 7233–7234; 241.133–241.167 s) | MEASURED + viewed (`frames/trans_sheet_2.jpg`) |
| Eased / tweened / continuous motion | **0 detected** | MEASURED (no multi-frame ramp anywhere) |
| Codec refresh blips | ≈48 (every 120 frames) | MEASURED |

Therefore the video's "motion" is **stepped stop-motion-like composition replacement locked to narration**, not animation in the keyframed-tween sense. This is the single most important reproducible trait: it makes the style cheap to build (no rigging) and highly rhythmic. Easing could not exist between consecutive frames at this granularity; sub-frame tweening is indistinguishable from a hard cut at 30 fps (alternative interpretation recorded in the ledger).

Facial/object motion: **none** inside any state (faces are fixed poses; expression changes are separate asset swaps). Object lifecycle: props enter on the cut frame and persist until the state ends (e.g., the poster persists S001.7–S001.9; the quote caption persists across three states).

## 7. Text, graphics and data (OBSERVED; accuracy status)

- 66 states carry text; visible text is transcribed in `visual_states.csv` (`visible_text`). On-screen wording was cross-read against the viewed frames: the quoted-word cards, the Dunning–Kruger chart labels, the Amazon beta example (Beta 1.33; spreadsheet 2%→2.66%, −2%→−2.66%, formulas `=B5*B2`, `=B11*B14`), the S&P 500 cards, and the closing line "Everone's a Genius in a Bull Market" (typo in source, preserved).
- Third-party images are shown in the video (quote card, film poster, product tin, news article, forum post, portraits). Identities are taken **only** from on-screen captions/attribution (e.g., "Mr. Buffett" label; Soros portrait shown beside an equals sign is not captioned in the frame viewed → not asserted here). No person is identified from a face.
- Numbers shown on cards (S&P 500 index quotes, +715%, P/E ratio) are as-displayed and **not fact-checked** here; `FINANCE_CLAIMS.csv` from the prior pass remains the claim ledger (not re-verified).
- Tesseract OCR is deferred by owner decision (`OPTIONAL_DEFERRED`); text was read by native-frame vision. Items too small to read reliably are flagged unverified: small asides inside S001.4/S001.5 (read as "Its no big deal" and the pitch text), S001.12 phone-call captions, and the forum-post body in S021.1.

## 8. Story and visual–script mapping

16 semantic beats (prior pass, re-read against this scan): HOOK → ESCALATION → TWIST → CENTRAL QUESTION (64 s) → EXPLANATION (Dunning–Kruger as "Darwinism of markets") → EVIDENCE (S&P 2020–25) → COUNTERARGUMENT → EVIDENCE/STAKES (17-year chart) → CENTRAL QUESTION 2 (154 s) → Option 1 / Option 2 → PAYOFF (answer card at 188.4 s after black) → definition + worked example (Amazon beta) → bull/bear contrast scenes → TAKEAWAY + end card.
- **Visual story logic (INFERRED):** a character-led parable (Dave) is the vehicle; evidence cards deliver the "adult" claims; gags are the retention scaffolding; the central question is asked twice and answered late (≈ 69% of runtime) with black beats as a "drum-roll".
- **Question/answer visual scaffolding (OBSERVED):** the title question appears alone on white twice (S003.0, S011.0), the definition question (S015.0) and "why does this matter?" (S017.3) likewise → "single-line question card" is a recurring section header.
- **Dave's arc as visual escalation:** grin → flex → smug → distressed (−67% chart) → "rigged" scowl → "outperformer" large pose → full-bleed restaurant (up market) vs counter (down market).

## 9. Attention hypotheses (labelled INFERRED — no retention data used)

H1 The cold-open cadence (24 changes/min) plus a visible prop on nearly every state front-loads novelty. H2 Extreme negative space makes each new element the sole focal point (single-focus composition). H3 Callbacks (coin, "Yes! Yes! Yes!", "rigged" pair) reward attention through recognition. H4 Black beats around the central question carry spoken setup ("…the answer to the question of today's video", "And the answer is simple") over a blank screen, which may focus attention on the voice and create anticipation. H5 Mixing crude art with real screenshots creates a credibility/comedy contrast. **No gaze map, dopamine, retention, CTR, or viewer-response claim is made.** Public performance in the prior packaging doc (≈237k views, below long-form median in n=33) is context only and is **not** evidence that these visuals caused or prevented retention.

## 10. Audio–visual alignment (`audio_visual_alignment.csv`, 75 events) — ASR timing only

Method: visual PTS (frame-exact, MEASURED) minus the nearest ASR word start (local `openai-whisper small.en`, word timestamps). Lag < 0 means the picture changes *before* the word.
- Median lag **−0.073 s** (≈ 2 frames early); p10 −0.207 s; p90 +0.120 s.
- 29 of 75 events within ±0.10 s of a word start; 60 of 75 within ±0.20 s; 10 events lead the word by more than 0.2 s (visual-before-word cues, e.g., a prop appearing just ahead of its spoken name).
- Reliability: ASR word timing is ±~0.1–0.2 s, so only the *pattern* (cuts land on or just before the key word) is supportable, not frame-exact sync. (INFERRED reading: the edit was cut to the voice track.)
- Cross-check of two independent ASR runs (prior `base` vs this `small.en`): 774 vs 777 words; median word-start difference **0.02 s**, p90 0.08 s. This validates the timing track's stability, **not** the wording (see ASR limits).
- **Black beats are not silent (MEASURED via ASR timestamps):** narration runs over each hold — 185.1–188.4 s "All this brings us to the answer to the question of today's video.", 188.4–190.7 s (white question card) "Why do the dumbest investors win?", 190.7–192.8 s (black) "And the answer is simple.", 196.8–199.5 s (black) "Let's get a little more technical real quick." So the holds are *spoken setup over a blank screen*, not a pause. Whether music/SFX accompany them is `UNAVAILABLE` (no listening).
- Pace: 774 words over 271.9 s voiced span ≈ 171 words/min; 75 pauses > 0.4 s; longest 1.22 s (at 190.28 s, just before "And the answer is simple.").

## 11. Audio status and limits

- `audio_human_listening = BLOCKED / PENDING`. The agent cannot listen. All audio statements rest on ASR timestamps; nothing is claimed about music, SFX, mix, voice quality or emotion.
- ASR text is `ASR_UNCERTIFIED`. Known divergences against on-screen text: the spoken product name is transcribed by small.en as "zinning" while the screen shows the tin brand text; the "Co*ai*n*" certificate title is censored on screen. On-screen text outranks ASR wherever both exist.
- Audio-visual sync tables from the prior pass (`AUDIO_VISUAL_SYNC.csv`, 122 rows) are historical; this run re-derives 75 event-level rows only.

## 12. Validation summary and gates

See `quality_gate.json` and `coverage.json`. Open items for `CT_SCAN_COMPLETE`: (a) native-frame *viewing* (not measurement) is sampled, not exhaustive; (b) human listening pending; (c) OCR deferred. Therefore the honest label is **`VISUAL_ANALYSIS_COMPLETE_WITHIN_DECLARED_COVERAGE`, CT_SCAN gate = PARTIAL**.
