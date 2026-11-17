# Visual CT scan — YL2VNtus4xk "What if the wise men kept walking after Jesus’s birth?" (LONG_FORM)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /videos tab (snapshot 2026-11-04T01:43:22Z); published 2025-03-04T09:00:38-08:00; public views at census 1144906 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if the wise men kept walking after Jesus’s birth？ [YL2VNtus4xk].mp4` sha256 `d8e6ec5fc0f9f1c091df33872e92c9825f5b93c98c844d6b75ec813a667dedf9`, 1920x1080 h264, 24/1 (CHECK: 3966 distinct packet durations), time_base 1/12288, 3966 decoded frames, 165.326 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_YL2VNtus4xk` (Claude Code sonnet subagent; transcript audit: 14/14 sheets opened, 14 image results, validator errors 0); primary spot-check: 1 of 14 sheets re-viewed by primary (0.6 scale), 9 rows compared, 0 disagreements; long-activity undersampling noted.

## 1. Coverage (MEASURED)
All 3966 frames measured. 107 segments = 54 HOLD states (3376 frames, measured static; settled frame viewed) + 53 ACTIVITY events (590 frames; 112 viewed in tiles; 36 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 107. Unresolved segments: G0010, G0018, G0024, G0027, G0043, G0091, G0095.

## 2. Structure (OBSERVED, from ledgers)
- 22 shots (composition replacements incl. cuts back), 53 activity events: GRAPHIC/TEXT 37, CAMERA 4, CHARACTER 2, LIGHT/COLOR/EFFECT 0, SHOT_CUT 21, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_YL2VNtus4xk/observations.md`)


## 1. Premise (first ~10 s)
- G0001 (0-2.5s): question card "Q. The story of the three wise men... What path would you trace on the Earth?" (N. Murdoch), large stick figure holding paper, empty board. ASR 0-12s reads the same question.
- G0002 2.58s: horizon arc, three wise men, dot pop on in the board. G0004 5.67s: haloed baby figure pops on. G0006 8.08s: red arrow draws wise men to baby. G0008 11.17s: red dashed wandering loops. OBSERVED: the premise is bounded as a miniature diagram inside a board; the question card never changes until the title card at G0010 (12.79s).
- INFERRED: the dashed loops foreshadow the "path" the question asks for.

## 2. Reasoning steps and anchors
- Recurring anchors: three wise men (G0002, G0014, G0046, G0064, G0078, G0092, G0098); the whiteboard + teacher stick figure (G0001, G0019, G0024-G0027); JERUSALEM/BETHLEHEM dot pair (G0028, G0056); red path lines.
- Escalation: sky/Sirius (G0010) -> spiral on map (G0010 end 23.8s) -> globe spiral (G0018) -> board with conditions (G0024, 42.5s, ASR "only walk toward the star while it's in the sky") -> Jerusalem-Bethlehem path (G0030, 48.8s) -> Red Sea map (G0032) -> Africa globe (G0034, ASR "Botswana") -> software (G0036) -> candidate objects (G0048) -> dates (G0056-G0062) -> planets (G0066-G0076) -> hovercar (G0078-G0089) -> epilogue (G0098-G0105).
- Each step is a new shot with a persistent red path as the answer artifact; the black-sky wise-men scene returns at G0046, G0064, G0092 with prior red scribbles retained and new items added (cumulative state).

## 3. Labels vs objects
- Labels pop on after the object: BRACKET + "WALKING/HALF A DAY" at G0012 (25.6s) after the spiral; "#CAN WALK ON WATER" G0026; "DEC 25" G0058; "DEC X" typed during G0060/G0062; "MT. EVEREST" G0076 (99.54s, ASR "atop Mount Everest" 97.98s, onset about same time); "VENUS" G0082 (111.8s).
- Objects and labels appear together at G0020, G0048, G0066 (single-frame pop-on). Typed labels ("WRONG T" -> "WRONG TIME", "TOO F" -> "TOO FAST", G0052; "D" -> "DEC X", G0060) show letter-by-letter write-on.
- Numbers: "YEAR: 2025/250/~4BC" on screen (G0036-G0044); month labels on Mars path (G0070).

## 4. Reveal types
- Pop-on (single frame): objects/labels (G0002, G0004, G0012, G0020, G0026, G0048, G0066, G0076, G0080, G0082, G0096, G0102).
- Write-on lines: red paths (G0006, G0008, G0030, G0032, G0034, G0060, G0062, G0072, G0074, G0084, G0088), white dotted Mars path (G0070), red scribble strikes (G0022, G0050, G0052, G0094).
- Sequential pop-on: babies across the sky (G0104, 151.4-152.4s).
- Dissolve: none confirmed.

## 5. Jokes and callbacks
- G0014 (29.2s) wise men saying "AND I WOULD WALK 500 MILES / 500 MORE" (Proclaimers reference; ASR nearby "size of the spiral... half a day").
- G0022 (39.7-40.1s) red zigzag through Earth: ASR "wise men are hardly going to walk toward the star while it's behind the earth".
- G0026 (46.3s) "#CAN WALK ON WATER" (ASR "they can still walk on water").
- G0050-G0052 (67.5-70.4s) red scribbles with "WRONG TIME", "TOO FAST" (ASR "Chinese records don't show a supernova...").
- G0054 (72.1s) four period-dressed stick figures with different dates "112 BC!", "4AD!", "32AD", "7BC" (ASR "debate over Jesus' date and year of birth").
- G0078-G0080 (106-109.8s) hovercraft, "THOU SHALT TRAVEL THE WORLD BY HOVERCAR" (ASR "hover car... Gnostic Gospels").
- G0090 (126.6s) Christmas house, roof figure, tiny hovercraft (ASR "Santa Claus" at ~129s).
- G0096 (135.6s) "THAT'S A PLANET, SILLY." (ASR 133-141s, "Sir Patrick Moore").
- G0104 (151.4-152.4s) babies falling (ASR "statistics and birth rates are on your side").
- Callbacks: black sky re-used at G0064, G0092 with cumulative red scribbles.

## 6. Cuts vs camera vs drawing
- SHOT_CUT (hard cuts, single-frame onsets): about 21 segments: G0014, G0028, G0032, G0034, G0036, G0046, G0054, G0056, G0064, G0068, G0072, G0078, G0084, G0086, G0088, G0090, G0092, G0098, G0106 plus the multi-shot G0010 and G0018.
- Drawing animation (write-on lines/scribbles): about 20 segments (see 4).
- CAMERA: few and mostly INFERRED: panel shift G0074 (95.75s), slight reframes G0024, G0043, G0060, G0062, G0091, G0094/G0095. G0010 and G0018 contain moving sky/globe views but onsets UNRESOLVED.

## 7. Characters and objects
- Stick figures: round head, line limbs (teacher G0001, desk figure G0036, period figures G0054, babies G0104); wise men are small detailed robed figures with turban/crown/hat and staffs; hovercraft G0078, house G0090 and dunes G0098 are detailed line drawings.
- Colour: red used for paths, scribbles, "#CAN WALK ON WATER", "SIRIUS" (G0010), "DEC 25"/"DEC X", and as full-screen title/end cards (G0010, G0106). Grey fill for sea/globe/land. Black-sky shots use white lines.

## 8. Unusual
- Not a single persistent diagram: about 25 distinct shots, light and dark.
- Red is not only for marks: SIRIUS label (G0010), title card, end card.
- Stick figures also in explanation (teacher G0001, G0019-G0027; desk figure G0036-G0045), not only jokes.
- A recurring dark star-sky theme with white lines (G0046, G0064, G0068, G0098).
- Actual software UI mockup (PyEphem screen, G0036-G0045).
- Scribbled-out candidate items use red strikes over white items on black.

## 9. Unresolved segments
G0010 (multiple shots, 6 samples, cut times UNRESOLVED), G0018 (globe motion and exact cut to board UNRESOLVED), G0024 (layout shift vs text swap), G0027, G0043, G0091, G0094/G0095 (possible camera shifts), G0004 (wise-men shift), G0042, G0100, G0102 (identity of small circle).


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.6259, #101010 0.2874, #D0D0D0 0.0356, #D03030 0.015, #B0B0B0 0.014; mean settled dark-ink coverage 32.1% (max 99.4%); red accent present in 26/54 holds; any saturated colour in 26/54 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9682 (609/627 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
