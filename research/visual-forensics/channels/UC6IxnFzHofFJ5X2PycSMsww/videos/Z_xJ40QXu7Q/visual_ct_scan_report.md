# Visual CT scan — Z_xJ40QXu7Q "What if you built a billion-story building?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2025-02-11T07:07:03-08:00; public views at census 2505166 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you built a billion-story building？ [Z_xJ40QXu7Q].mp4` sha256 `6384c44ce09ce40ed82936ea4248ee47807db3ff2624eef5694d8b7413bf733e`, 1920x1080 h264, 24/1 (CHECK: 5652 distinct packet durations), time_base 1/12288, 5652 decoded frames, 235.566 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_Z_xJ40QXu7Q` (Claude Code sonnet subagent; transcript audit: 15/15 sheets opened, 15 image results, validator errors 0); primary spot-check: 1 sheet re-viewed by primary, 5 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 5652 frames measured. 133 segments = 67 HOLD states (5445 frames, measured static; settled frame viewed) + 66 ACTIVITY events (207 frames; 103 viewed in tiles; 55 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 194. Unresolved segments: G0018, G0044, G0065, G0128.

## 2. Structure (OBSERVED, from ledgers)
- 24 shots (composition replacements incl. cuts back), 66 activity events: GRAPHIC/TEXT 30, CAMERA 7, CHARACTER 12, LIGHT/COLOR/EFFECT 2, SHOT_CUT 24, FALSE_POSITIVE 1.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_Z_xJ40QXu7Q/observations.md`)


Facts are OBSERVED from tiles; reasons are marked INFERRED. ASR is provisional text, not audio.

## 1. Premise (first ~10 s)
G0001 (0-0.67s): grey box with the reader question ("Q. My daughter-age 4.5-maintains she wants a billion-story building...", "-Keira, via Steve Brodovicz"), a stick figure holding paper at left, and an empty board. G0002 (0.71s) a seated marker figure pops on at the board corner; G0004 (2.67-2.88s) red doodles "YAY!" "BILLION!" "BIG!" "THIS IS A MILLION!" fade in; G0006 (5.08s) hard-hat figure; G0008 (6.58s) lattice tower; G0010 (10.2s) first drawing inside the board. ASR: "wanted to build a billion-story building" (0-4.8s), "top part will tear itself off and go into orbit" (14-18s). The board is bounded as a stage; the answer's first spoiler is the G0010-G0017 sequence (tower, rubble G0012 12.54s, tilting rod G0016) at 10-20s. INFERRED: board = the 'answer frame'.

## 2. Reasoning steps / escalation
The escalation is a counter: header "GOAL : 1,000,000,000" (G0066, 97.17s) plus "FLOORS" counter (G0068 98.4s: 100; G0070 102s: 10,000; G0076 113s: 1,000,000; G0086 139s: 100,000,000). Persistent anchors: the header, a thin reference line ("HOUSE", then "100 SKYSCRAPERS", "100 MEGA-SKYSCRAPERS", "100 MEGA-MEGA SKYSCRAPERS"), and one skyscraper drawing that is redrawn taller each step. Each step is a blurred camera zoom-out/scroll (G0070, G0076, G0086) followed by new labels. Earlier, a vertical log axis (10m to 100m to 1 km to 3 km) anchors the height comparison (G0030-G0035, 36-45s). After 183s the axis becomes Earth/Moon on black (G0110, G0116) and a galaxy/solar-system close-ups (G0120-G0130).

## 3. Labels relative to objects
Labels mostly arrive AFTER the object, as separate pop-ons: MEGA-SKYSCRAPER (G0072, 104.25s), MEGA-MEGA SKYSCRAPER (G0078, 115.2s), SPACE STATION (G0082, 121.3s), SPACE JUNK (G0084, 124.75s), MEGA-MEGA-MEGA SKYSCRAPER (G0088, 141.8s), MOON (G0090, 148.1s), KEIRA-SKYSCRAPER (G0118, 198.4s). Exception: labels arrive with a zoom (G0070, G0076). ELEVATORS/ROOMS arrive after the building (G0060 74.75s). ASR near these: "stack 100 mega skyscrapers" (112s), "International Space Station" (121s), "broken satellites... junk" (124-128s).

## 4. Reveal types
- Pop-on (hard, 1 frame): most labels, objects, characters (e.g. G0002, G0006, G0112, G0122).
- Write-on: red ellipse around WIND (G0040, 51.9-52.1s); red dashed circle with "1/10TH TO THE MOON" (G0102, 168.25-168.46s).
- Fade-in: red doodles (G0004), faint METEORS (G0074, 106.96-107.17s).
- State swap (whole object replaced): intact to collapsed (G0012, G0024, G0028, G0036, G0048, G0114).
- Camera: blurred zoom/scroll (G0032, G0034, G0070, G0076, G0086).
- Cut: all scene changes.

## 5. Jokes / callbacks
- Jell-O: castle labelled "BARAD-DUR-LICIOUS!" (G0022, 29.67s; ASR "fancy Jell-O") then collapse G0024 (32.1s; "smushes down on itself").
- Chance-gag: "I WISH I COULD BE CATAPULTED UP THE BUILDING INSTEAD..." / "YEEESSSS!!" with balloon and catapult (G0054-G0055, 61-64.8s; ASR "no one wants to climb hundreds of flights of stairs").
- "ARE YOU WAITING FOR THE TOP FLOOR TOO?" (G0058, 69.5s; ASR "floors purely dedicated to letting people change").
- "WE COULD BUILD A SWIMMING POOL ON THE MOON FOR THIS AMOUNT OF MONEY..." (G0062, 79.8s; ASR "Another big problem is money").
- "1 FLOOR DONE, ONLY 999,999,999 TO GO." (G0064, 90.2s; ASR "A billion stories is just too many").
- Stick figures with spinning scribbles then carousel (G0092-G0094, 151-152.7s; ASR "swing carousel").
- Callback: a "WIND" list item circled (G0040) then cut to tower bending and snapping (G0046-G0048, 55-56.5s).
- Callback to the opening: "KEIRA-SKYSCRAPER" (G0118, 198.4s).
- Throw-away listing "GETTING ELEVATOR MUSIC THAT'S LONG ENOUGH" (G0038, 49.7s) - deadpan list.

## 6. Camera vs animation vs cuts
Counted from tile annotations: about 40 SHOT_CUT rows (every scene change, plus the title card and credits card); 5 clear CAMERA events with blur (G0032, G0034, G0070, G0076, G0086) plus 2 small reframings (G0098, G0108, MEDIUM); write-ons: 2 (G0040, G0102); fades: 2 (G0004, G0074); the remaining activity is pop-on or state swap. Note: the story is NOT one continuous ascent shown by long uninterrupted camera moves. It is a sequence of static comparison scenes, with one recurring diagram (GOAL/FLOORS counter plus tower) re-zoomed in 5 short blurred transitions (each 0.3-0.7s) between long holds (4-14 s).

## 7. Characters / objects / colour
Stick figures: round head, line limbs; hard hat (G0006), hair bun (G0002), cap (G0092), hat (G0052). Buildings are detailed hatched ink drawings; the planet/galaxy/moon are grey-shaded. Red is used for marks (arrows, circles, "1/10TH TO THE MOON") and for red building doodles (G0004). Dark scenes: from G0110 (183.2s) to G0130 background is black with white lines, grey shading for the cratered sphere (G0130) and the spiral galaxy (G0124). Red full-screen cards at open (G0018) and credits (G0132).

## 8. Unusual
- Black-background sequence (183-225s) is a style shift from white canvas.
- Title card is inserted at 20.46-22.4s, after a cold open that already shows the answer; not at 0s.
- Red also used for decorative doodles (G0004), not only marks.
- Figures appear in non-joke explanatory beats too (hard-hat figure with board G0038; two figures G0050).
- Diagram is NOT single and persistent across the whole video: persistent only for 97-150s.

## 9. Unresolved
- G0018: exact onset of the second cut (title card to Jell-O scene) between 22.04s and 22.46s.
- G0044: tiny change, unreadable at tile scale (LOW).
- G0065 / G0095 (slight reframing), G0098 / G0108 (partial camera), G0128 (faint particles): MEDIUM/LOW.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.7561, #101010 0.1862, #D0D0D0 0.0231, #D03030 0.0121, #303030 0.0046; mean settled dark-ink coverage 21.4% (max 99.5%); red accent present in 21/67 holds; any saturated colour in 21/67 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9603 (835/867 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
