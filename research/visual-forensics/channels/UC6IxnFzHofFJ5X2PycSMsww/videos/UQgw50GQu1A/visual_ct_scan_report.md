# Visual CT scan — UQgw50GQu1A "What if the moon turned into a black hole?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2025-07-08T09:00:50-07:00; public views at census 1610964 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if the moon turned into a black hole？ [UQgw50GQu1A].mp4` sha256 `5049f27c6312d3dc6f5b08522230ac717cbb038377e9fbaed9d880e008e7899d`, 1920x1080 h264, 24/1 (CHECK: 5301 distinct packet durations), time_base 1/12288, 5301 decoded frames, 220.938 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_UQgw50GQu1A` (Claude Code sonnet subagent; transcript audit: 15/15 sheets opened, 17 image results, validator errors 0); primary spot-check: 1 of 15 sheets re-viewed by primary (0.6 scale), 12 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 5301 frames measured. 131 segments = 66 HOLD states (4735 frames, measured static; settled frame viewed) + 65 ACTIVITY events (566 frames; 105 viewed in tiles; 48 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 92. Unresolved segments: G0010, G0022, G0030, G0046, G0078.

## 2. Structure (OBSERVED, from ledgers)
- 23 shots (composition replacements incl. cuts back), 65 activity events: GRAPHIC/TEXT 35, CAMERA 4, CHARACTER 11, LIGHT/COLOR/EFFECT 5, SHOT_CUT 22, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_UQgw50GQu1A/observations.md`)


1. **Premise (0-12 s).** G0001 (0-1.9s): grey Q-card 'What would happen if the Moon were replaced with an equivalently-massed black hole? ... -Matt', stick figure lower-left holding a paper, empty whiteboard. Moon + 'M_moon' pops on (G0002, 1.92s) as ASR says 'replaced with an equivalently-masked black hole'. G0004 (2.96-3.04s): ghosted trail shrinks the moon to a dot, second 'M_moon'. G0006 (5.42s, ASR 'lunar...eclipse') cut to black panel 'LUNAR ECLIPSE' vs '???'; G0008 (11.6s) '0.001°F' (ASR 'milli-degrees Fahrenheit'). Card and figure persist as frame until G0010. Red title card 'xkcd's what if? THE VIDEO SERIES' follows (G0010, 16.3-18.3s).

2. **Reasoning steps.** Each step is a new scene, not one persistent diagram. Anchors: whiteboard + figure (G0001-G0009, G0079-G0087); a central object/dot on dark field (G0048-G0057); Earth-moon pair (G0030, G0114-G0126); a graph with moon-phase axis (G0074) and a time graph (G0106). Escalation in G0048-G0066: dot, outward arrows (G0050), inward arrows (G0052), arrows removed (G0054), red sieve (G0056), full accretion disc (G0058), red emission/jets (G0060), '6% M→E' (G0062). Final escalation G0114-G0129: moon swapped for black disc (G0116, 197.2s), '600M_SUN' typed (G0118), Earth torn (G0120-G0124), 'BURP!' (G0128, 208.6s).

3. **Labels vs object.** Labels mostly arrive after or with the object: 'M_moon' with moon (G0002); 'EVENT HORIZON' after 'BLACK HOLE MOON' title and dot (G0012, 19.5s, ASR 'event horizon about the size of a sand grain'); 'SAND' with sandcastle (G0014); 'LIGHT LEVEL' meters after circles (G0084). Exceptions: titles ('BLACK HOLE MOON', 'WENTWORTH GRADE SCALE') are present at the cut. Numbers are typed after the diagram: '10X' (G0092), '±0.01°C' (G0094), unit lines G0096-G0104 (161-173s, ASR lists Rankine, Romer, Raimeer, kelvin), 'CO2 EMISSIONS' (G0108, 178.7s).

4. **Reveal types.** Pop-on (1-frame): most objects/labels/circles (G0002, G0012, G0014, G0018, G0020, G0050, G0052, G0062, G0084, G0092, G0094, G0128). Write-on: temperature curve G0074 (109.5s, 6 frames), red CO2 curve G0108, typed units G0096-G0104, typed '600M_SUN' G0118 (character-by-character appearance OBSERVED). Dissolve/fade: G0126 fade-out (205.8-206.0s), glow in G0120. Camera moves: G0026 (tilt/enlarge board), G0086 (zoom), G0122 (zoom-out/pan with Earth stream). Drawn animation: G0004, G0022 sieves, G0030 and G0078 orbit loops, G0010 title-card dinosaur.

5. **Jokes/callbacks.** G0026-G0028 (42.6-43.3s, ASR 'neither here nor there'): board tilted then crumpled to a paper ball. G0024 hourglass (40.8s, ASR 'point in time'). G0040 'R.I.P. HUMANS ... MAYBE WE SHOULDN'T HAVE TURNED THE SUN INTO A BLACK HOLE' (58.25s, ASR 'life on Earth might'). G0044 bats with '?' (59.8s, 'no moonlight'). G0072 figures gain hats/scarves (106.4s, 'colder'). G0076 moon red-scribbled (118.4s, ASR 'not due to moonlight'). G0086 'EXAMPLE 1/2' board. G0110-G0112 (187.7-192.2s, ASR 'famous quote... 1969'): 'THAT'S ONE SMALL STEP FOR -' then 'AAAAAAAAAAAHHHHHH!' falling astronaut. G0128 'BURP!' (ASR 'A total final lunar eclipse'). G0006 '???' callback to G0007 eclipse. Sieve callback: G0022 (31-36.9s) to red sieve G0056 (82.9s).

6. **Counts.** True/hard cuts about 22 (G0006, 0008, 0010, 0016, 0022, 0030, 0036, 0040, 0042, 0048, 0058, 0064, 0068, 0074, 0076, 0078, 0086, 0088, 0106, 0110, 0114, 0130). Partial scene swaps G0046, G0112. Camera motion 3 (G0026, G0086, G0122; G0030 framing shift UNRESOLVED). Drawing animation (multi-frame) about 12 (G0004, 0010, 0022, 0030, 0074, 0078, 0096-0104, 0108, 0118, 0120-0126). Remaining ~60 activities are 1-frame pop-on/off or pose swaps.

7. **Characters/objects/colour.** Stick figures: round head, line body, no face; in-board figure on whiteboard (G0001), small F_g figure (G0031), spacetime-diagram figures, hatted pair G0068-G0077, astronaut G0110. Objects: shaded grey cratered moon and Earth with continents, detailed Wentworth chart, spiky outline sun, sieves. Red ink is used for marks and annotations: circles G0018/G0020, red sieve G0056, emission arrows G0060, scribble G0076, unit lines, CO2 curve, '600M_SUN'. Red is also the title and credits background (G0010, G0130). Grey fills on dark scenes G0042-G0077, G0110-G0129.

8. **Unusual.** Several different scenes rather than one diagram (about 20 distinct canvases). Red used for continuing annotation text and curves, not only marks. Stick figures appear outside jokes: whiteboard narrator (G0001-G0009, G0079-G0087). Full dark-scene illustrations (street G0046, night trees G0042). Orbit loops G0030/G0078 do not use a pop-on idiom.

9. **UNRESOLVED:** G0010 (cut frame), G0022 (sieve removal onsets and final cut), G0030 (camera vs object motion, cut frame), G0046 (cut vs overlay), G0078 (cut frame). Low-confidence/MEDIUM: G0004, G0026, G0060, G0080, G0086, G0116, G0120, G0122, G0124. Small red text G0096-G0104 transcribed approximately.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.485, #303030 0.2447, #101010 0.2091, #D0D0D0 0.0145, #D03030 0.012; mean settled dark-ink coverage 48.7% (max 100.0%); red accent present in 23/66 holds; any saturated colour in 23/66 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9708 (865/887 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
