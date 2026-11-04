# Visual CT scan — JqFSGkFPipM "What if everyone pointed a laser at the moon?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-11-05T09:51:51-08:00; public views at census 6086476 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if everyone pointed a laser at the moon？ [JqFSGkFPipM].mp4` sha256 `a25cece84e9e0aa9929bd9dbed4d718335fcc0a2ee9bd81049a8dceaed5e8c6d`, 1920x1080 h264, 24/1 (CHECK: 8078 distinct packet durations), time_base 1/12288, 8078 decoded frames, 336.643 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_JqFSGkFPipM` (Claude Code sonnet subagent; transcript audit: 19/19 sheets opened, 37 image results, validator errors 0); primary spot-check: 1 of 19 sheets re-viewed by primary (0.6 scale), 8 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 8078 frames measured. 209 segments = 105 HOLD states (7885 frames, measured static; settled frame viewed) + 104 ACTIVITY events (193 frames; 123 viewed in tiles; 94 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 187. Unresolved segments: G0008, G0012, G0060, G0180, G0186, G0188.

## 2. Structure (OBSERVED, from ledgers)
- 38 shots (composition replacements incl. cuts back), 104 activity events: GRAPHIC/TEXT 54, CAMERA 3, CHARACTER 6, LIGHT/COLOR/EFFECT 16, SHOT_CUT 37, FALSE_POSITIVE 1.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_JqFSGkFPipM/observations.md`)


1. **Premise (0-12 s).** G0001 (0-1.8s): grey Q box "If every person on Earth aimed a laser pointer at the Moon..." (-Peter Lipowicz), stick figure with paper, empty blackboard. G0002 (1.875s) Moon and crowd arc pop on; G0004-G0006 (2.9-7.5s) red lines fan to the Moon, then red scribble is written across the beams (ASR 6.46s: "not if we used regular laser pointers"). G0008 (9.4-11.4s) hard cut to red "xkcd's what if? THE VIDEO SERIES" card, then Earth/Moon with two bubbles (G0010, 12.4s) and an "ALL HUMANS / THE EARTH" panel (G0014, 15.6s). Bounding by constraint: 75% of population on a map (G0018 18.8s, circle G0020 23-23.25s) then a night scene (G0022 25.3s).

2. **Escalation.** The same device recurs: "What if we tried more power?" ASR at 64.9, 113.1, 143.3, 170.7, 198.3, 216.9s. Each step is a new power source: 5 mW (G0030 32.5s), 1 W (G0062 67.5s), helicopter 50,000 lumens (G0094 121.6s), IMAX (G0106 145s), Luxor (G0112 155.5s), YAL-1 (G0124 175.5s, G0132 193.4s), Asia array/fuel pump (G0140 203.6s), NIF (G0154 223.2s). Persistent anchors: the night-sky frame (half-lit Moon top, crowd arc bottom) recurs at G0034, G0072, G0100, G0108, G0118, G0128, and the beam fan re-appears each time with new colour/glow (white G0102/G0110, red G0120/G0130). A hat figure plus bare figure pair is the recurring "dialogue" anchor between steps (G0088, G0104, G0122, G0134, G0150, G0206). Maps are used twice (G0016, G0136).

3. **Labels vs objects.** Labels usually follow the object: Moon icon first, then "5 mW LASER POINTER" (G0028), "~10^13 m^2" after disc (G0048), "~6,450,... W" after arrows (G0052), "0.5 LUX" after glow (G0080), "1 LUX" (G0082), "130,000 LUX" arrives with the white flood (G0084), "500 TW" then ". ~2 ns" then "= ENERGY OF 60 mL PETROL" (G0158, G0160, G0162; ASR 231.1s "pulses lasting a few nanoseconds"). Numbers appear about 1-3 s after the ASR utters them (e.g. G0074 97s equation vs ASR 96.4s).

4. **Reveal types.** Pop-on: most labels, objects, beam fans (about 40 GRAPHIC/TEXT rows, many 1-frame). Write-on: red scribbles (G0006, G0176), circle (G0020), numbers typed (G0052, G0058, G0074), laser line (G0024). Dissolve/flash: G0084, G0172, glow swaps G0146/G0148. Slide: G0014 (INFERRED slide from left). Cross-dissolves are not clearly seen; transitions between scenes are hard cuts.

5. **Jokes/callbacks.** G0068 (79.9s) phone figure with "200$" ("suspicious $200 listings"); G0070 (93.1s) goggles ("safety glasses that cost more than the laser"); G0092 (119s) "TRUST ME, THIS COUNTS AS AN EMERGENCY"; G0112 (155.5s) "I NEED THIS FOR A SCIENCE PROJECT" (ASR "Luxor Hotel"); G0150/G0152 (216.8-218.8s) bin with toy plane then wizard with sparkles (ASR "outside the realm of plausibility"); G0170 (251.9s) "UNHARMED" corrected to "HARMED ATMOSPHERE" (ASR "Earth still catches fire"); G0176 (258s) Earth scribbled out (ASR "forget the Earth"); G0204/G0206 (317.5-318.8s) moon meets flaming Earth (ASR "we'd deserve it").

6. **Counts.** True hard cuts (SHOT_CUT rows): 36 plus 1 SHOT_CUT+CAMERA (G0060). Camera-only rows: 2 (G0186 ZOOM_OUT, objects shrink; G0196 INFERRED recede). Drawing/graphic events about 52 plus 6 character rows. Holds: 105. Cut count is high; camera moves are rare compared with 1-frame pop-ons.

7. **Characters/objects.** Stick figures are plain black-ink circles with line limbs; hat figure has a flat black hat; ponytail figure; a detailed wizard, helicopter, 747, IMAX unit, Luxor pyramid are far more detailed than the figures. Colour: red for beams, scribbles, circles, "BEFORE" box, title card, Asia fill and NIF starburst; grey for maps and bands; white-on-black for night scenes with glow effects.

8. **Unusual.** Not a single persistent diagram: the video re-cuts to fresh scenes each step. Red is also used for large fills and glows (beam fans, map region, title/end cards), not only marks. Stick figures appear in main content, not only jokes. Heavy glow/flash effects (G0084, G0146, G0172) are unlike the plain line style. G0060 (64.7s) rearranges characters/board and may be a recompose rather than a cut.

9. **Unresolved:** G0008 (onset of second cut 11.0-11.4s), G0012 (no visible change), G0180 (exact spark/glow change), G0186 (cut vs zoom), G0188 (what moved).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.4422, #101010 0.4198, #D0D0D0 0.0422, #707070 0.0153, #909090 0.0132; mean settled dark-ink coverage 48.3% (max 98.7%); red accent present in 57/105 holds; any saturated colour in 58/105 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9669 (1227/1269 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
