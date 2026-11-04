# Visual CT scan — rGZ6TsXvi8E "How long could you drive towards the sunset?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2026-08-18T10:00:21-07:00; public views at census 1705813 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4` sha256 `1e4498d55a84d0ec6d1bbd543a665ce4b47bdbff336b602d611047c63cf35189`, 1080x1920 h264, 24/1 (CHECK: 3117 distinct packet durations), time_base 1/12288, 3117 decoded frames, 129.939 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_rGZ6TsXvi8E` (Claude Code sonnet subagent; transcript audit: 15/15 sheets opened, 29 image results, validator errors 0); primary spot-check: 1 of 15 sheets re-viewed by primary (0.6 scale), 10 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 3117 frames measured. 109 segments = 55 HOLD states (2409 frames, measured static; settled frame viewed) + 54 ACTIVITY events (708 frames; 89 viewed in tiles; 43 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 9. Unresolved segments: G0040, G0052, G0054, G0078.

## 2. Structure (OBSERVED, from ledgers)
- 16 shots (composition replacements incl. cuts back), 54 activity events: GRAPHIC/TEXT 40, CAMERA 3, CHARACTER 4, LIGHT/COLOR/EFFECT 1, SHOT_CUT 15, FALSE_POSITIVE 1.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_rGZ6TsXvi8E/observations.md`)


1. Premise (0-11 s). G0001 (0-5.75s) holds a chalkboard drawing with globe and a stick figure with paper while ASR gives the question. Hard cut G0002 (5.79s) to a white canvas with horizon, a yellow sun and a red X. G0004 (6.75-11.1s) pops on sun copies stepping down past the horizon, with dashed red vertical lines, a green check and a second red X, bounding what counts (ASR "starts the instant the sun touches the horizon").

2. Reasoning as visual steps. Each ASR claim gets its own canvas: "not a sunset" examples (G0006-G0035, 11.75-31.3s) as sun-path diagrams, then a globe with "SUNSET ZONE" (G0036, 31.4s; G0048, 42.9s), place cards (G0056, 49.8s, North Pole; G0058, 53.2s, Longyearbyen), a V-shaped sun path (G0070-G0077), a DAY/NIGHT map (G0078, 74.25s), a laptop desk (G0081), and a car-over-map summary (G0090). Persistent anchors: the horizon line plus sun discs (G0002-G0035, G0070-G0077, G0090-G0095); the globe (G0036-G0055); the dark twilight gradient with sun at left (G0056-G0069). Escalation: arrows 1 to 3 to 5 (G0049-G0055), seals/vehicle to car to car with "355 mph" (G0056-G0069), "~95 min" over "~55 min" (G0092-G0095).

3. Labels vs objects. Labels arrive after their object, via separate 1-frame pop-ons: "NOT A SUNSET" (G0008, 12.29s) after the painting; "NOT TOUCHING THE HORIZON (YET)" (G0010); "~55 min" (G0062, 58.2s) after the sun-line (G0060); "355 mph" (G0068, 64.8s) after the map disc (G0066); "PyEphem" (G0082, 97.6s) after the figure; "~95 min" (G0092, 108.7s) after the suns. Exception: titles (G0056, G0078 labels) arrive with the cut.

4. Reveal types. Pop-on is dominant (about 45 single-frame segments): labels, X marks, check, arrows, sun copies, map frames. Write-on: Arctic circle dashed line and lettering (G0086-G0088, 102.9-103.1s), church/lower-half drawing (G0094, 111.3s, INFERRED write-on). Dissolve: G0058 (53.2-53.4s) title and scene morph. Camera/animation: G0078 and G0080 (74-95s) terminator line and map reframing. True cuts are the rest.

5. Jokes and callbacks. G0016 (16.25-16.4s, ASR "This is definitely not a sunset"): yellow square opens like a shutter on a hatted stick figure. G0018 (17.7-19.2s, "no matter what happens here"): cracked sun labelled "BRWAAK". Painted-sunset callback: G0006 (11.75s) returns as G0096 (113.4s). Ending gag: G0098 spinning figure (118.0s, ASR "spinning counterclockwise"), then "WHAT ARE YOU DOING?" (G0100) and four-line reply ending "HERE WITH YOU." (G0108, 126.96s, ASR "be worth it"). G0046 "OH NO!" (40.08s, "run out of fuel"). Red X marks repeat as deadpan crossings (G0020, G0026, G0032).

6. Counts (my reading). True cuts about 15: G0002, G0006, G0012, G0014, G0018, G0022, G0028, G0036, G0048, G0056, G0070, G0078, G0090, G0096, plus the end of G0080. Camera-like moves 3 (G0040 small, INFERRED; G0078, G0080). Dissolves 1 (G0058). Everything else is drawing animation: pop-on, write-on, state swaps. Note several cuts hide inside multi-frame ACTIVITY segments (G0012, G0018, G0078, G0080).

7. Characters/objects. Stick figures are plain black line drawings with circle heads (G0001, G0070, G0081, G0090 small). Detail rises sharply in scenic canvases: painted sunset gradient with dark figures and yellow rim (G0006, G0096), shaded gridded globe (G0048), photographic-style gradients with seals, tracked vehicle, car (G0056-G0069), grey maps with a glow band (G0078). Colour: yellow suns, grey for sub-horizon suns, red for X marks, dashed lines, arrows, NW/SW text and Arctic circle; green only for one check (G0004); white text on dark scenes.

8. Unusual. Not a single persistent diagram: about 14 distinct canvases. Red is not only for marks: red/orange dominates the painted sunset and the glow band. Stick figures appear in non-joke roles (observer G0070, programmer G0081). Dark scenes have painted gradients and white title text; this differs from the white line-art canvases. The final spinning figure is a character-based joke after a text-heavy technical stretch.

9. Unresolved: G0040 (zoom vs label add), G0052 (no visible change), G0054 (arrow count inconsistent between tiles). Partially resolved, internal order unseen at tile scale: G0004, G0012, G0030, G0078, G0080, G0094.


## 4. Art direction (MEASURED palette)
Background exact #FDFDFD; top quantised bins #F0F0F0 0.4827, #101010 0.0774, #303030 0.0738, #101030 0.0558, #909090 0.0415; mean settled dark-ink coverage 41.7% (max 97.9%); red accent present in 37/55 holds; any saturated colour in 50/55 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9659 (496/508 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
