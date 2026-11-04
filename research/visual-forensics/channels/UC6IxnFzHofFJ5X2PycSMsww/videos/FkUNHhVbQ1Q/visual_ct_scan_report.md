# Visual CT scan — FkUNHhVbQ1Q "What if we teleported the oceans to Mars?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-08-13T09:00:12-07:00; public views at census 2550520 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if we teleported the oceans to Mars？ [FkUNHhVbQ1Q].mp4` sha256 `a2091cf27008390412516cb7770d43d4fbe5a8158d40c443e5cab51b7962180f`, 1920x1080 h264, 24/1 (CHECK: 6412 distinct packet durations), time_base 1/12288, 6412 decoded frames, 267.215 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_FkUNHhVbQ1Q` (Claude Code sonnet subagent; transcript audit: 22/22 sheets opened, 23 image results, validator errors 0); primary spot-check: 1 of 22 sheets re-viewed by primary (0.6 scale), 9 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 6412 frames measured. 183 segments = 92 HOLD states (6079 frames, measured static; settled frame viewed) + 91 ACTIVITY events (333 frames; 165 viewed in tiles; 58 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 260. Unresolved segments: G0010, G0056, G0078, G0080, G0132.

## 2. Structure (OBSERVED, from ledgers)
- 28 shots (composition replacements incl. cuts back), 91 activity events: GRAPHIC/TEXT 41, CAMERA 4, CHARACTER 8, LIGHT/COLOR/EFFECT 20, SHOT_CUT 27, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_FkUNHhVbQ1Q/observations.md`)


**1. Premise (first ~10 s).** G0001 (0-1.5s) shows a grey Q box ("Supposing you did drain earth's oceans ... Curiosity rover ... Mars change as the water accumulated?" - Iain), a stick figure holding paper, and an empty black-bordered frame. ASR 0-3.7: "This question comes from Ian, and many, many others". Comment cards pop on (G0002-G0005, 1.5-3.2s) and pile up into a wall, then a hard cut (G0006, 3.2s) to the figure with a black panel showing Earth and Mars; a water stream pops between them (G0008, 4.29s; ASR 4.3: "Suppose you did drain the Earth's oceans..."). Premise is bounded by the Q box staying on screen until 9.75s.

**2. Reasoning steps / anchors.** No single persistent diagram. Anchors are the stick-and-blackboard frame (G0011-G0021, G0170-G0181), the red-topped water column (G0020, G0052, G0064, G0156, G0181), the repeated Mars map (G0060, G0098, G0112, G0124, G0134) and the Curiosity-rover/rover-family close-ups. Escalation is shown by returning to the same Mars map after each close-up and a larger flood: sea at 137.7s (G0098), Valles at 155.6-157s (G0114-G0116), Hellas at 163.3s (G0126), islands at 183-195.9s (G0140-G0146). The water volume escalates over cuts; the map is the anchor. Scale is handled by a separate comparison scene (G0148, 203.7s, Olympus Mons vs Mt. Everest).

**3. Labels vs object.** Labels pop on after the object has settled in a hold: "POLAR ICE CAP" (G0026, 25.5s), "-65 C" (G0028, 28.1s), "~0.006xEARTH PRESSURE" (G0030, 28.96s), "TRIPLE POINT" (G0044, 46.4s), "HELLAS IMPACT CRATER" (G0128, 164.1s), "2% ICE" (G0152, 214.4s). Exceptions: names on the elevation map and temperature labels are present at the cut (G0056 "-30C - 0C" at 67.04s with the new scene). Graph axes arrive with the inset (G0034) and curves are written afterwards (G0036).

**4. Reveal types.** Pop-on (single-frame): arrows, labels, red annotations, inset panels, comment cards. Write-on: sine curves (G0036, 34.1-34.8s), dashed 0 C line (G0038), red scribble (G0172, 244.3-244.6s). Dissolve/fade: flood spreading on the map (G0114, G0126, G0140, G0144, G0146), ice formation (G0082, G0094, G0158-G0168), vapor lines (G0088, G0164), cutaway maps leaving (G0102). Camera: scroll up (G0016), slide/pan triptych (G0080), zoom out (G0170), scroll down (G0046).

**5. Jokes / callbacks.** Cutaway of four other xkcd maps (G0100, 141.4-141.7s) while ASR 141.56 "I'm a big fan of maps"; red "LAND" (G0104, 147.75s; ASR 147.88 "just this big empty swath of land") and "BORING COASTLINE" (G0106, 149.3s; ASR "I think this one's kind of boring"); "PRETTY COOL COAST" (G0118, 157.3s); "MANY CRINKLES" (G0136, 173.8s; ASR "crinkly coastline"); "PUT CASTLE HERE?" (G0138, 180.5s; ASR "where my kingdom would be"); red circled "A+" (G0142, 189.6s; ASR "plus excellent map"). Rovers: "OPPORTUNITY" surfing a wave (G0120, 159.7s) and "PERSEVERANCE" tumbling (G0130-G0132, 167.4-168.3s; ASR 167.6 "Perseverance is likely destroyed"). Red scribble striking out the final ice scene (G0172, 244.3s; ASR 243.7 "Except, maybe none of this would happen"). Brand callback: red title card and "PREVIOUSLY ON 'WHAT IF'" recap (G0010-G0013, 9.8-16.3s). Final shrug pose (G0180-G0181, 254s; ASR "There's only one way to find out").

**6. Cuts vs camera vs drawing.** Counted from annotations: about 36 SHOT_CUT rows (including G0006, G0010, G0022, G0032, G0040, G0052, G0056, G0060, G0064, G0076, G0084, G0090, G0092, G0098, G0108, G0112, G0120, G0124, G0130, G0132, G0134, G0148, G0150, G0156, G0174, G0178, G0182); camera moves only 5-6 (G0016, G0046, G0080, G0170 and parts of G0122/G0096, which are object moves with ghosting); write-ons 4 (G0036, G0038, G0172 and the circled/arrows are pop-ons); dissolves roughly 20. The video is cut-driven; true camera moves are rare.

**7. Characters/objects.** Stick figure: round head, single-line limbs, holds paper, poses by swap (G0014, G0016, G0170, G0180). A larger round head recurs at lower-left (G0011-G0021). Rovers and landers are detailed grey drawings with shading (G0032, G0092, G0108, G0120, G0130). Colour: beige sky and black ground in coloured scenes; blue only for water on top-down map (G0076-G0083) and the Mars planet (G0178); tan/brown for Gale Crater (G0022) and Mars/Earth planets; red for annotations and title/end cards.

**8. Unusual.** (a) Not a single persistent diagram: many distinct scenes. (b) Red is not only marks: it fills the title and end cards (G0010, G0182) and is used as the waterfall top edge (G0020, G0052). (c) Stick figure appears as an on-screen presenter in the recap and ending (G0012-G0021, G0170-G0181), not only in jokes. (d) Comment-card pile (G0002-G0005) and external map cutaways (G0100) are outside-the-diagram material. (e) A triptych strip (G0081) and split screen (G0056-G0059) are used for progression and comparison. (f) Long holds with narration only (G0137 6.6s, G0141, G0147, G0149).

**9. Unresolved.** G0010 (onset of second cut and why 49 activity frames), G0056 (whether left half changed), G0078 (channel write-on vs pop), G0080 (pan vs slide mechanics), G0132 (cut vs redraw). Lower-confidence: G0013, G0030, G0058, G0077, G0168.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.3281, #B0B090 0.3011, #101010 0.1814, #D0D0D0 0.0813, #B0B0B0 0.0187; mean settled dark-ink coverage 24.3% (max 94.3%); red accent present in 27/92 holds; any saturated colour in 75/92 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9762 (1024/1048 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
