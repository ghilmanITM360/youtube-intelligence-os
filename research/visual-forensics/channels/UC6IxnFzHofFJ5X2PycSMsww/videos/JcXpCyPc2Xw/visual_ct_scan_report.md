# Visual CT scan — JcXpCyPc2Xw "What if NASCAR had no rules?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2023-12-19T09:00:13-08:00; public views at census 3284701 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4` sha256 `a8aa9dbcd4cf3510e31d11b6c38e4106a5d6d103c55388ec480a0e3b06245d5e`, 1920x1080 h264, 24/1 (CHECK: 6463 distinct packet durations), time_base 1/12288, 6463 decoded frames, 269.351 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_JcXpCyPc2Xw` (Claude Code sonnet subagent; transcript audit: 26/26 sheets opened, 27 image results, validator errors 0); primary spot-check: 1 of 26 sheets re-viewed by primary (0.6 scale), 8 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 6463 frames measured. 213 segments = 107 HOLD states (4992 frames, measured static; settled frame viewed) + 106 ACTIVITY events (1471 frames; 200 viewed in tiles; 76 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 179. Unresolved segments: G0010, G0022, G0078, G0090, G0096, G0110, G0198, G0210.

## 2. Structure (OBSERVED, from ledgers)
- 20 shots (composition replacements incl. cuts back), 106 activity events: GRAPHIC/TEXT 79, CAMERA 9, CHARACTER 18, LIGHT/COLOR/EFFECT 2, SHOT_CUT 19, FALSE_POSITIVE 1.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_JcXpCyPc2Xw/observations.md`)


1. **Premise.** G0001 (0.0s) shows a stick figure with magazine and paper beside an empty rectangle. G0002 (0.42-0.71s) pops on a grey card quoting Hunter Freyer's question (ASR "This is a question from Hunter"). G0004 (2.42-2.71s) pans right; a trash bin with flies enters. G0006 (5.42s) pops a rocket/human drawing into the rectangle (ASR "simply to get a human being around a track 200 times"). G0008 (10.4-10.67s) types "Let's say the racer has to survive." into the card with a red underline. G0010 (12.04-14.04s) is a red "xkcd's what if? THE VIDEO SERIES" title card during ASR silence. The question is bounded by the card, then a caveat line.

2. **Reasoning steps.** Each step is a new canvas or a new annotation on the last one. Escalation: ID.R car, rocket sled, Slinky Dog Dash (G0014-G0018, 19.8-21.2s) lead to a "POINT OF FAILURE" circle (G0020, 26.25s), then the human is crushed (G0022). The Daytona track is the main persistent anchor (G0023-G0090 and G0104-G0110): labels and red arrows are added, then "LIMIT: 4 Gs", an equation and a time (G0066-G0077). It is cleared (G0078, 83.0s), then a speed graph fades in (G0082). The limit is struck and rewritten 4 to 6 to 10 Gs with times 1:45, 1:20, 1:00 (G0110, 138.7-150.1s). A blackboard figure with a G-graph (G0046-G0056) is a second anchor. Later anchors are the chute (G0146-G0168), the LHC ring (G0170-G0181) and the track grid (G0188-G0211). The opening scene returns at G0114 (159.08s).

3. **Labels vs objects.** Almost always the object is drawn first and the label follows in a later segment: G0014 car then G0016/G0018 sled and dog; G0172 ring then labels; G0134 arm then "KEVLAR"; G0136 "MAX: ~1.5km/s". Exceptions: G0014 and G0016 appear together with their labels, and G0118/G0120/G0122 add COUNTERBALANCE, "VEHICLE" and TRACK one at a time. Numbers arrive after their equation: G0072 equation, G0074 red 2:05:00, G0076 "2:48:55 CURRENT RECORD". The same pattern holds at G0138/G0140 and G0178/G0180.

4. **Reveal types.** Pop-on (instant, one frame) is dominant, about 90 segments, for labels, arrows, numbers, stars (G0098, G0100), and charts (G0062). Write-on and type-on: G0008, G0052, G0056, G0094, G0116, G0128-G0132, G0190-G0204; red scribble strikes G0112, G0116, G0142, G0144, G0154. Fades: G0002, G0080, G0082 graph, G0138 and G0178 figures, G0188 page dissolve. Camera/slide: G0004, G0046, G0138, G0178, G0186, G0188.

5. **Jokes and callbacks (ASR nearby).**
   - G0004 bin with flies, a gag against the premise.
   - G0022 (28-29.6s) figure collapses in the circle ("The problem is acceleration").
   - G0032 (36.9s) "RIP" portrait ("drivers will die").
   - G0034-G0040 (39.5-44.7s) Beetle crash, squirrel, 100 Gs ("car accidents... hundreds of Gs").
   - G0098/G0100 (116-120s) star ratings ("best if... chest" and "least capable... downward").
   - G0102 (124.67s) "I DIDN'T SIGN UP FOR THIS!" ("swivel them around").
   - G0106-G0108 (134.6-136.2s) podium with cars ("fastest modern Daytona race cars").
   - G0111/G0112 (150-155s) "NOT FDA APPROVED" sphere with red scribble ("liquid breathing").
   - G0114/G0116 (159-160s) callback: red scribble over "Let's say the racer has to survive." ("what if we dropped the survive requirement").
   - G0142 (188.3s) figure scribbled out ("not with a living driver").
   - G0162 (219.25s) "DIAMONDS: ACTUALLY FLAMMABLE" ("our diamond might catch fire").
   - G0168 (227.4s) "THIS IS CONCERNING" ("Oops, we've accidentally built a particle accelerator").
   - G0208 (253.6s) thumbnails of earlier vehicles ("before the drivers had made it to the first turn"; INFERRED recap callback).

6. **Camera vs drawing vs cuts.** Hard cuts, about 23 (12.04, 14.04, 19.83, ~29.6, 39.5, 48.04, 62.38, 70.92, 98.54, 105.25, ~111.5, 124.67, 129.04, 133.92, 138.71, ~150.0, 159.08, 163.96, 169.6, ~192.1, 230.25, 243.29, 259.29s). Camera moves, about 6 (pans G0004, G0138, G0178, G0186; zoom-out to blackboard G0046; snap rescale G0048). Pure drawing animation covers the rest. Object animation (spin G0126, ball rolls G0148, capsule G0158/G0166, Beetle G0034) is a fourth class, not camera.

7. **Characters/objects.** Stick figures have a plain oval head, or dark hair from G0090 on. Vehicles and machines are detailed, hatched line art (Beetle, jet, ID.R, gimbal sphere). Colour: red for arrows, numeric results, circles, scribbles and the title/end cards (G0010, G0212); grey for tracks, panels and the Q card; black fill for ball bearing and capsule; a grey half-shell sphere; black box with white digits at G0076.

8. **Departures from typical patterns.** Not a single persistent diagram: about 20 distinct scenes. Red is not only for marks: it is also the answer-number colour (1:30:00, 2:05:00, 0:08:57) and full-frame title/end cards. Stick figures are used as scale anchors (G0138, G0178, G0206 result label) and in the main reasoning (G0046-G0056 blackboard host), not only jokes. Scribble-out is a repeated negation device (G0112, G0116, G0142, G0144, G0154). Three-frame step cadence at G0190-G0204 (~0.04s per trace) is much faster than elsewhere. A Wikipedia-table screenshot dissolves into the track grid (G0188).

9. **Unresolved segments.** G0010 (cut-out frame), G0022 (cut frame), G0078 (title blink), G0090 (cut-out frame), G0096 (false positive or strike-through change), G0110 (cut-in frame), G0198 (count of tracks traced), G0210 (tiny marks). Single-frame segments elsewhere were inferred from adjacent holds, so the exact onset frame may be one frame off.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.9136, #D0D0D0 0.0311, #101010 0.0289, #D03030 0.0076, #B0B0B0 0.0063; mean settled dark-ink coverage 4.4% (max 94.3%); red accent present in 36/107 holds; any saturated colour in 36/107 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9702 (994/1026 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
