# Visual CT scan — BnGqPxnQh9A "Could you power a house with the radioactivity from bananas?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2026-05-05T10:00:13-07:00; public views at census 856381 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Could you power a house with the radioactivity from bananas？ [BnGqPxnQh9A].mp4` sha256 `04ce628fd63b51cccac643f815f16eba340b59dc54ae04a1e97d5279135906ca`, 1920x1080 h264, 24/1 (CHECK: 4315 distinct packet durations), time_base 1/12288, 4315 decoded frames, 179.839 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_BnGqPxnQh9A` (Claude Code sonnet subagent; transcript audit: 16/16 sheets opened, 32 image results, validator errors 0); primary spot-check: 1 of 16 sheets re-viewed by primary (0.6 scale), 10 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 4315 frames measured. 137 segments = 69 HOLD states (4077 frames, measured static; settled frame viewed) + 68 ACTIVITY events (238 frames; 116 viewed in tiles; 43 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 137. Unresolved segments: G0008, G0014, G0028, G0066, G0082, G0092, G0100, G0104, G0134.

## 2. Structure (OBSERVED, from ledgers)
- 19 shots (composition replacements incl. cuts back), 68 activity events: GRAPHIC/TEXT 43, CAMERA 4, CHARACTER 7, LIGHT/COLOR/EFFECT 1, SHOT_CUT 18, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_BnGqPxnQh9A/observations.md`)


1. Premise (0-14s). G0001 (0-1.9s) opens on a grey question card "Q. I heard that bananas are radioactive... power a house? - Kang Ji", a paper-holding stick figure left, empty blackboard right. Banana pops on (G0002, 1.9s), trefoil (G0004, 2.6s), squiggles write on (G0006, 4.3-4.5s), banana becomes a bunch (G0008, 5.6s). ASR: "I heard bananas are radioactive" near 2-3s. The card and board stay persistent through G0015 (14s); the figure swaps paper for banana (G0010, 8.2s) then a burning banana (G0014, 11.9s; ASR "safe until you use them to power a house"). Bounded by a hard cut to a red title card (G0016, 14-16s). INFERRED: the burning banana jokes at the house-power escalation.

2. Reasoning steps. Each step is a new self-contained scene via hard cut, not a persistent diagram: banana quantities (G0017-G0021), figures (G0022+), CRC table (G0032+), comparison columns (G0040+), K-40 nucleus (G0044+), flowchart (G0050-G0063), decay chain (G0064-G0077), rover (G0078+), banana machine and house (G0090+). Persistent anchors exist only within a scene: the Q-board and figure (G0001-G0015); the banana (G0064-G0077, shifting in the frame as sub-elements add); the rover (G0078-G0089); the blackboard graph (G0112-G0117). Escalation of scale: 0.00005 g (G0021), 15 vs 45 vs 3500 decays (G0041-G0043), plutonium ~2e15 vs 15 decays (G0083-G0089), house (G0092), Manhattan map (G0096).

3. Labels vs objects. Labels mostly arrive after the object: banana then text (G0017 -> G0018, 16.9s); book then table (G0032 -> G0034); columns with labels on arrival (G0040); nucleus then half-life caption (G0045 -> G0046); rover then "238 Pu" (G0078 -> G0080, 94s); radiation arrows and "~2,000,000,000,000,000 DECAYS/SECOND" (G0082) after the rover, then "~2000 W" (G0084). Numbers are typed in lines (G0084, G0088). The "YOU" column is added third (G0042, 48.7s, ASR "your own body").

4. Reveal types. Pop-on (single-frame): banana, trefoil, table, columns, dice, branch nuclei, banana mound, explosions. Write-on type (left-to-right clip): G0018, G0020, G0024, G0036, G0038, G0046, G0084, G0088, G0120, G0124. Write-on line: zigzag arrow (G0074), graph lines (G0114, G0116), flames (G0128), NO loop (G0062). Fade-in/dissolve: squiggles fade out (G0012), thought bubble (G0026), "238 Pu" (G0080). Camera: pan with motion blur (G0112); zoom-out (G0092, G0104, INFERRED, onset UNRESOLVED).

5. Jokes/callbacks. Burning banana in hand at G0014/G0015 (11.9-14s). "IT'S OKAY, IT'S NO MORE RADIATION..." with thought bubble "DON'T STAND NEXT TO BANANAS. GOT IT." (G0026, 27.75-28.0s) and red scribble over the dropped peel (G0030, 34.8s; ASR "they're really not"). "YOU" 3500 column (G0042, 48.7s). Large figure bonking the nucleus (G0076-G0077, 87.4-89.8s; ASR "bonk into other atoms"). Figure on ladder dumping bananas into a radioactive machine (G0090, 106.4s; ASR "even if you capture..."). House with banana pile above (G0094, 110.8s). Manhattan buried (G0096, 112.6s) and its callback with skyline and shrugging figure (G0106-G0111, 132.4-138s; ASR "which we buried in bananas"). Burning banana callback (G0134, 165.9s; ASR "real threat").

6. Counts. True cuts (SHOT_CUT or SHOT_CUT-mixed): about 25 (e.g. G0016, G0022, G0032, G0040, G0044, G0050, G0064, G0078, G0090, G0096, G0098, G0102, G0106, G0112, G0118, G0126, G0132, G0136). Camera: 1 clear pan with blur (G0112) and 2-3 probable zoom-outs (G0092, G0104) plus small frame shifts within diagrams (G0054, G0066, G0068, G0072). Drawing animation (write-on, pop-on, fade) accounts for the rest, ~80 events.

7. Characters/objects. Stick figures: round-headed, thin limbs, two lines; dark-haired figure with black hair (G0022, G0132); knit-cap "YOU" figure (G0042). Objects are detailed outlines with shading (banana, Mars rover G0078, house G0092, CRC book). Colour: red title and end cards (G0016, G0136-G0137); red scribble (G0030); small red oval and dice pips (G0056, G0058); grey fill for book cover, banana piles, methanogens background; otherwise black ink on near-white.

8. Unusual. Red is used in marks inside the story (G0030, G0056, G0058), not only on title and end cards. The nominal single-diagram pattern does not hold: scenes change roughly every 2-5 seconds with hard cuts. Stick figures appear in explainer scenes (blackboard, G0098, G0112) as well as jokes. A repeating deadpan "banana mound" appears in three different graphics (G0094, G0096, G0108). A title card interrupts the opening at 14-16s (G0016), after a cold-open with the question. The end card ASR is "So, don't worry about the radioactivity in bananas" repeated at 170-180s while the end card is held (G0136-G0137).

9. Unresolved segments: G0002, G0008, G0010, G0014, G0028, G0034, G0052, G0054, G0056, G0058, G0060, G0062, G0066, G0068, G0070, G0072, G0076, G0082, G0086, G0092, G0094, G0100, G0104, G0106, G0108, G0110, G0122, G0130, G0134. Reason: single-frame activity, only the settled state is visible; onset and exact reveal type cannot be seen. Several single-frame events also change the view framing slightly (INFERRED camera drift or layout re-centre).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.8288, #B0B0B0 0.077, #101010 0.0352, #D0D0D0 0.03, #D03030 0.0113; mean settled dark-ink coverage 6.2% (max 94.2%); red accent present in 4/69 holds; any saturated colour in 5/69 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9783 (630/642 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
