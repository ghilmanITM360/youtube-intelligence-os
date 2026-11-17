# Visual CT scan — 4ZVtHknKuvg "What if Earth’s Water Suddenly Disappeared?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2026-08-25T10:00:12-07:00; public views at census 1042020 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4` sha256 `fd96c7878fd8713e45ce1e29784fde7e42d6ba4374844844c7482edda703f1c8`, 1920x1080 h264, 24/1 (CHECK: 4411 distinct packet durations), time_base 1/12288, 4411 decoded frames, 183.856 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_4ZVtHknKuvg` (Claude Code sonnet subagent; transcript audit: 22/22 sheets opened, 43 image results, validator errors 0); primary spot-check: 1 sheet re-viewed by primary, 10 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 4411 frames measured. 179 segments = 90 HOLD states (3649 frames, measured static; settled frame viewed) + 89 ACTIVITY events (762 frames; 163 viewed in tiles; 60 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 300. Unresolved segments: G0010, G0036, G0038, G0044, G0046, G0070, G0092, G0140, G0164, G0166, G0170, G0176.

## 2. Structure (OBSERVED, from ledgers)
- 15 shots (composition replacements incl. cuts back), 89 activity events: GRAPHIC/TEXT 30, CAMERA 4, CHARACTER 25, LIGHT/COLOR/EFFECT 29, SHOT_CUT 14, FALSE_POSITIVE 3.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_4ZVtHknKuvg/observations.md`)


## 1. Premise intro (first ~10 s)
- G0001 (0-2.0s): grey panel top: "Q. What would happen if all the bodies of water on Earth magically disappeared? —Joanna Xu"; stick figure with paper left; empty board right. ASR 0.0-4.7: "This question comes from Joanna... What would happen if all the bodies of water on Earth magically disappeared?"
- G0002 (2.0s) sailboat on grey water pops on inside the board; G0004 (3.8-4.0s) water fades to dashed line; G0006 (5.17s) boat crashed. G0008 (7.08s) label "NOT AGAIN" and head swap; ASR 5.1-8.1 "everyone would die".
- G0010 (8.29-10.29s) red title card "xkcd's what if? THE VIDEO SERIES"; beach scene at ~10.29s (G0011). The premise is bounded by one reusable board frame: Q panel stays through G0009.

## 2. Reasoning steps / anchors
- Each step is a new scene, not one persistent diagram. Recurring anchors: the beach slope with palm tree (G0011, G0030, G0034), the lecturing stick figure plus board (G0001, G0120, G0146, G0172), and a drawn horizon/waterline (solid grey fill to dashed line).
- Escalation by scale: beach (5m, "1 SECOND", G0034) to shelf ("~6 SECONDS", G0036) to deep sea (-1000 to -3000m, G0038) to "~600 SECONDS" and "~30 SECONDS" (G0042, G0044) to Mariana trench "~60 SECONDS" (G0048). The depth axis is redrawn with new tick values each time (G0036 ticks read -60m -40m -20m -80m -100m in drawn order, odd).
- Later steps: tank-pair animal diagrams (G0072-G0093), dry land/rain/forest/fire (G0100-G0119), tombstone (G0120), carbon-silicate cycle (G0126-G0145), sun/Earth board (G0146-G0171).

## 3. Labels relative to object
- Labels generally pop on after the object is on canvas: depth labels at 59.58s (G0040) after ships at 58.75s; "~600 SECONDS" bracket at 61.88s (G0042) after labels; "~30 SECONDS" at 67.3s (G0044); "O2" at 97.1s (G0086) and "GASP!/WHEEZE!" at 99.6s/101.9s (G0088, G0090) after tanks. Year label "~1,000,000,000 YEARS FROM NOW" at 155.6s (G0148) then "BYE!" 156.8s (G0150). Exception: the time bracket and 5m scale bar arrive together with the zoom-out in G0034.
- ASR near G0044: "Titanic... five and fifteen minutes... thirty seconds".

## 4. Reveal types
- Pop-on (single frame): sailboat G0002, labels G0040/G0042/G0086/G0088/G0090, tanks G0074/G0076/G0078, fire G0112/G0114, CO2 clouds G0116.
- Fade/dissolve (6 frames): water and fills fading to dashed outlines (G0004, G0012, G0016, G0020, G0022, G0024, G0064, G0102-G0106, G0128-G0138); stipple VACUUM fade (G0014); red gradient (G0144, 152.1-152.3s).
- Slide-in with blur: note box G0118 (133.8s). Zoom-in inset: G0060 (73.25-73.67s).
- Write-on/stroke-by-stroke drawing: none seen at tile scale (INFERRED not used; sampling could miss it).

## 5. Jokes / callbacks
- G0008 7.08s "NOT AGAIN" (ASR "everyone would die" nearby).
- G0060 73.25s sailor text "THERE'S NOTHING IN HERE ABOUT HOW TO TRIM THE SAILS FOR A WIND FROM BELOW THE SHIP!" (ASR 72.5-77.9 "final boat... small sailboat or life raft... deep ocean trench").
- G0120 136.79s tombstone "RIP ALL LIFE ON EARTH / THANKS JOANNA" (ASR "virtually all life dying out pretty fast"); G0124 142.33s "WORSE? FOR WHO?" (ASR "things get even worse").
- G0118 133.8s climate-model note (ASR 132.3-136.3 greenhouse gas).
- G0150 156.8s "BYE!" on Earth, repeated G0162 (163.8s) and removed G0168 (ASR 157-164 oceans lost anyway).
- G0174 170.17s long-haired character "HI!" (ASR "Unless Joanna ruins everything"), a callback to the questioner.
- G0098 111.3s drinker replaced by tank-top figure and collapsed paddler (ASR dehydrate and die in days).

## 6. Counts (from annotations)
- True hard cuts (SHOT_CUT incl. combos): G0010, G0018, G0030, G0038 (end), G0048, G0062, G0072, G0094, G0100, G0120, G0126, G0146, G0172, G0178 = 14 (G0038 start and G0044 onset UNRESOLVED).
- Camera moves: G0034 zoom-out/pan with blur (32.7-33.3s), G0036 blurred horizontal pan (39.6s), G0068 and G0070 scroll/glide with the seaplane = 4.
- Drawing animation/state swaps (CHARACTER, fades, pop-ons): the remaining ~60 ACTIVITY segs. Many 1-frame ACTIVITY segs are pop-on or state swaps at roughly 2-frame cadence (stepped, low frame-rate motion, e.g. G0050-G0058).
- FALSE_POSITIVE: G0046, G0140, G0170 (LOW).

## 7. Characters / objects / colour
- Lecturer: round-head, line-body stick figure with paper, redrawn pose to pose (G0008, G0122, G0124). Secondary characters are also stick figures: swimmers, kayaker, diver, tank-top figure, paddler; long-haired girl G0174.
- Objects have higher detail than figures: sailboat, seaplane (G0062-G0071), whales/fish in tanks, water tower, volcano diagram, Earth (grey shaded).
- Colour: mostly black ink plus grey fills (water, clouds, ice). Non-grey: red title/end cards (G0010, G0178, G0179); pink magma in G0126; red/orange fire G0112-G0115; red gradient G0144-G0145; red tick marks around Earth G0158-G0159. So red is NOT only for marks; it is also used for fire and heat effects.

## 8. Contradictions to typical patterns
- No single persistent diagram: the video uses 14+ scenes.
- Stick figures appear outside jokes (swimmers, divers, tank figures); they are scene participants.
- Frame-level step animation (stepped falling) and heavy fade-to-dashed-outline vocabulary: water removed = grey fill fades to dashed line, recurring across G0004, G0012, G0020-G0026, G0064, G0102, G0128, G0176.
- Full-frame colour (red gradient G0144, fire G0114) is escalation signalling, INFERRED.
- Detector D4 drift in G0039-G0045 is likely bubble/spray animation; INFERRED.

## 9. UNRESOLVED
G0010 (exact cut frame), G0036 (cut vs pan), G0038 (f1211 cut vs zoom; f1410 onset), G0044 (white panel onset), G0046, G0070 (transition boundaries), G0092 (tiny object identity), G0140, G0164, G0166, G0170, G0176 (dolphin redraw).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.7544, #101010 0.0963, #B0B0B0 0.0797, #707070 0.02, #D0D0D0 0.0141; mean settled dark-ink coverage 13.6% (max 94.3%); red accent present in 16/90 holds; any saturated colour in 16/90 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.973 (667/684 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
