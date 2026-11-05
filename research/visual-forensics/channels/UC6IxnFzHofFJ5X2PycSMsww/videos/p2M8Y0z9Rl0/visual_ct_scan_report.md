# Visual CT scan — p2M8Y0z9Rl0 "What if everyone jumped at once?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2024-04-16T09:00:40-07:00; public views at census 2604066 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if everyone jumped at once？ [p2M8Y0z9Rl0].mp4` sha256 `c949504fd017d7ec201e250abae580cbf58667c8275e2beb8138f56689a92cb4`, 1920x1080 h264, 24/1 (CHECK: 5559 distinct packet durations), time_base 1/12288, 5559 decoded frames, 231.689 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_p2M8Y0z9Rl0` (Claude Code sonnet subagent; transcript audit: 17/17 sheets opened, 17 image results, validator errors 0); primary spot-check: 1 sheet re-viewed by primary, 11 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 5559 frames measured. 177 segments = 89 HOLD states (5363 frames, measured static; settled frame viewed) + 88 ACTIVITY events (196 frames; 115 viewed in tiles; 77 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 167. Unresolved segments: G0018, G0114, G0124, G0126, G0128.

## 2. Structure (OBSERVED, from ledgers)
- 29 shots (composition replacements incl. cuts back), 88 activity events: GRAPHIC/TEXT 49, CAMERA 2, CHARACTER 9, LIGHT/COLOR/EFFECT 3, SHOT_CUT 28, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_p2M8Y0z9Rl0/observations.md`)


Facts are OBSERVED from tiles; reasons are INFERRED. ASR is machine text, not audio.

## 1. Premise and bounding (first ~10 s)
- G0001 (0-1.67 s): a persistent grey Q box (top) reads "What would happen if everyone on earth stood as close to each other as they could, jumped, and landed ... at the same instant?" with attribution; a paper-holding stick figure sits lower-left beside an empty framed panel. G0002 (1.71 s) edits the attribution to "-Thomas Bennett (and many others)" (ASR: "Thomas and many other people").
- G0004 (4.21 s) pops "ALL HUMANS ON EARTH" plus a tiny crowd on an Earth arc into the panel; G0006 (7.42 s) crowd jumps; G0008 (8.13 s) landing with ripples. The first 10 s therefore define the scenario as a three-state crowd-on-Earth diagram, using the persistent Q box as boundary. INFERRED: the panel is a presentation surface and the narrator figure stays as host.

## 2. Reasoning steps as visual steps; persistent anchors
- Anchors: Q box + narrator + panel (0-20 s, G0001-G0017); crowd row on ground line (re-entered at G0026 30.3 s, G0062 78.5 s, G0070, G0093, G0150); the framed south-New-England map with hatched "CROWD" outline (G0052 59.6 s, G0060, G0146 172.8 s, G0160 193.6 s).
- Escalation is by cutting between the same anchors: mass labels (G0038 39.7 s, G0040 40.4 s) -> red 0.5 m dashed line (G0042 42.1 s) -> energy "2,000,000,000,000 JOULES" (G0050 57.5 s) -> map ripples (G0054 63.9 s) -> seismograph (G0056 68.3 s) -> contour map "VRAMPAMPAM" (G0058 71 s). The disaster chain later uses pops of objects on a blank canvas (mower, plane, pan, ball, G0078-G0084, 97.6-106 s) and maps with growing red overlays (pins G0112, routes G0114, car inset G0122, arrows G0142, gravestones G0162).

## 3. Diagrams and labels relative to objects
- Labels arrive after the object they label, usually one sample (>=0.04 s) to seconds later: "THE EARTH" fades in (G0036 37.96 s) then the mass (G0038 39.67 s); "ALL HUMANS" mass at G0040; "BOSTON"/"NEW YORK" labels with dots (G0140 161.5 s) then arrows (G0142 167.7 s); "YOU"/"ME" after gravestones (G0162 -> G0164 198.5 s). Exceptions: "ALL HUMANS ON EARTH" arrives with the crowd (G0004); "THE REAL STORY" replaces panel contents in one step (G0016).
- Numbers: "~6,000,000,000,000,000,000,000,000 KG", "~500,000,000,000 KG", "2,000,000,000,000 JOULES", "1% IN 100 YEARS" (G0108 134.5 s), "X 1,000,000" (G0122 148 s), "20 Km" scale bar (G0024 27.75 s).

## 4. Reveal types
- Hard pop-on: the vast majority (e.g., G0004, G0012, G0014, G0028, G0030, G0072, G0074, G0082, G0084, G0140, G0142, G0148, G0156, G0158, G0162, G0164, G0170, G0172).
- Write-on: red dashed 0.5 m line and its label drawn over 42.1-42.4 s (G0042); red scribble on restroom sign (G0102 126.5 s, sample only, MEDIUM); red road lines G0114/G0124-G0128 are UNRESOLVED (single-frame).
- Fade in/out: "THE EARTH" (G0036), restroom sign in (G0100 123 s), sign out (G0104), whole annotation set out (G0046 54.8-55 s).
- Wipe: population shading wiped east-to-west (G0022 26.25-26.75 s).
- Cross-dissolve: close-up to wide crowd (G0092 113.5-113.7 s); title card has internal dinosaur motion (G0018).
- Object motion: car exits right (G0134 157.6-158.3 s).

## 5. Jokes, cutaways, callbacks (ASR nearby)
- Speech "HOW DID WE GET HERE?" (G0026 30.29 s; ASR "let's assume they, I mean we, are actually in Rhode Island"); red ME/THOMAS (G0028 31.83 s) and "THIS IS RHODE ISLAND?" (G0030 32.96 s) all popped off (G0032).
- Crowd close-ups with beards/hair (G0064-G0068, 81.9-83.9 s; ASR "Seconds pass. Everyone looks around").
- Restroom sign scribbled out (G0100-G0104, 123-128 s; ASR "nicest bathrooms ... Very impressive. This is not part of the recording").
- "WHO BROUGHT SNACKS?" on container ship (G0118 144.3 s; ASR "container ships ... stocking sufficient food").
- City placards with question marks (G0094 115.7 s; ASR "how do we get everyone home?").
- Multilingual bubbles (G0150 176.2 s). Outhouse and bent figure (G0156-G0158 190-191.6 s; ASR "Sanitation is a disaster").
- Gravestones with red YOU/ME (G0162-G0164 194.8-198.5 s; ASR "probably you and me too"); wasteland vehicles (G0166 199.6 s); carved boulder "THOU SHALT NOT JUMP IN RHODE ISLAND" (G0174 216.5 s; ASR "Let's not try that again").

## 6. Camera vs animation vs cuts
- Counting my SHOT_CUT-class rows: about 50 hard cuts (e.g., G0026, G0052, G0056, G0058, G0060, G0062, G0070, G0076, G0078, G0086, G0090, G0096, G0110, G0116, G0120, G0132, G0136, G0138, G0146, G0150, G0152, G0160, G0166, G0168, G0174, G0176).
- Camera-like: only G0064 and G0066 (zoom-in jump to close-ups at 81.9 s and 82.4 s); no continuous pan seen. Jump cuts, not eased moves (single sampled frame each).
- Drawing animation (write-on/fade/wipe/dissolve): about 10 segments.
- Everything else is pop-on or pose swap.

## 7. Characters and objects
- Stick figures: round head, thin limbs, varied hair/beards (solid black fill for beards), sometimes caps/beanies; crowd arcs above heads (INFERRED: sweat or compression marks). Objects are line drawings with hatching (airport, seismograph, cell tower, cars grey-filled).
- Colour: red is used for annotations (0.5 m line, ME/THOMAS, pins, routes, arrows, YOU/ME, orbit/spin arrows), but also fills (red phones G0072, red title/end cards G0018/G0176, pink Rhode Island inset G0024, red-outlined no-signal and no-car signs). Grey fills for Earth ground, sea, maps, cars; black background only for the globe scene (G0168-G0173).

## 8. Unusual vs typical patterns
- Not a single persistent diagram: many distinct scenes, with the Q box persisting only in the first 20 s.
- Red is not only for marks: whole red title and end cards and red phone fills.
- Stick figures appear in narrative scenes, not only jokes; non-stick content includes a wizard (G0020), a hatted-figure round inset (G0144), and a video-thumbnail bearded face (G0010).
- Scale-zoom close-ups (G0064, G0066) are used for emphasis, apparently a jump rather than a camera move.
- A black globe scene (G0168-G0173) with a red rotation/orbit overlay is the only dark-ground shot.

## 9. Unresolved
- G0018 (exact frame of title-card to map cut within f530-f539).
- G0114, G0124, G0126, G0128 (red route/road line draw-on vs pop-on; very small deltas, tiny detectors).
- G0102 (scribble draw timing, one sample).
- G0142 internal order of arrows (single frame).
- G0177 small credit text unreadable at tile scale.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.732, #D0D0D0 0.1533, #101010 0.0735, #707070 0.0094, #D03030 0.009; mean settled dark-ink coverage 10.1% (max 94.3%); red accent present in 24/89 holds; any saturated colour in 23/89 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9748 (792/818 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
