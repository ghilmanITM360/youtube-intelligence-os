# Visual CT scan — 2p305nzcVQE "What if we teleported the oceans to Mars?" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2025-12-23T10:00:08-08:00; public views at census 3677047 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if we teleported the oceans to Mars？ [2p305nzcVQE].mp4` sha256 `7ad232b09890be270b71e58af52ceb920996af6dd04e12c674209d933b2fc4bc`, 1080x1920 h264, 24/1 (CHECK: 2546 distinct packet durations), time_base 1/12288, 2546 decoded frames, 106.138 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_2p305nzcVQE` (Claude Code sonnet subagent; transcript audit: 10/10 sheets opened, 10 image results, validator errors 0); primary spot-check: 1 of 10 sheets re-viewed by primary (0.6 scale), 8 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 2546 frames measured. 85 segments = 43 HOLD states (2467 frames, measured static; settled frame viewed) + 42 ACTIVITY events (79 frames; 56 viewed in tiles; 35 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 16. Unresolved segments: G0016, G0017, G0054, G0068, G0074.

## 2. Structure (OBSERVED, from ledgers)
- 12 shots (composition replacements incl. cuts back), 42 activity events: GRAPHIC/TEXT 25, CAMERA 0, CHARACTER 3, LIGHT/COLOR/EFFECT 7, SHOT_CUT 11, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_2p305nzcVQE/observations.md`)


Sampling is sparse: most ACTIVITY segments are 1 frame, so onsets/durations are mostly UNRESOLVED.

## 1. Premise (first ~10 s)
- G0001 (0-0.83s): white canvas, boxed label "PREVIOUSLY ON 'WHAT IF'" upper-left, stick figure lower-left, hand on chin. G0002 (0.875s): chalkboard panel pops on with Mariana Trench ("MARIANA TRENCH"). ASR 0-5.8: "In the previous What If, we opened a portal at the bottom of the Mariana Trench...drained them to Mars."
- G0004 (3.0-3.2s): water level drops in the trench (ASR "let the oceans drain out"). G0006 (5.0s): panel swaps to red line over black strip "MARS"; G0008 (5.92s): rover with "!" pops on (ASR "Curiosity rover"). G0010 (8.96s): grey waterfall with splashes (ASR "make things easier for it"). Question is bounded by a framed panel plus the recurring figure. INFERRED: panel = recap frame.
- G0012 (11.0s): panel swaps to Earth/Mars with water stream, figure gets a paper; ASR "How would Mars change as the water accumulated?" (11.08).

## 2. Reasoning steps to visuals
- Persistent anchors: the stick figure and framed panel (G0001-G0013, G0052-G0063, G0072-G0083); the red-capped water column in cross-sections (G0022-G0043, G0064-G0066); the Mt. Sharp peak in cross-sections; the place-label map (G0052-G0063).
- Escalation is by staged states: labels added (G0018, G0020, G0024), water level rising (G0034, G0036, G0038), anchor ice (G0040), debris specks (G0042); then a zoomed-out top-down view with river extension (G0046), a lake (G0048), and freezing (G0050); then map-level flood (G0054) and ice-over (G0062). Ends with freeze-solid (G0066, G0070) then a red scribble (G0074 92.9s, ASR "Except maybe none of this would happen").

## 3. Labels relative to objects
- Labels usually arrive after the object, as separate events: temperature (G0018 18.54s, ASR "Liquid water doesn't last long there, because Mars is too cold"), pressure (G0020, ASR "too little air"), "-100 C - 0 C" (G0024). "HELLAS IMPACT CRATER" arrives after the blob (G0056, 70.08s, ASR "Hellas Impact Crater" 68.96-72). Exceptions: "ANCHOR ICE" fades in with its ice (G0040). Place labels exist at map arrival (G0052).
- Zoom callout: red dot plus inset "GALE CRATER" pops after the elevation map (G0030 32.75s, ASR "Currently Curiosity is sitting in Gale Crater").

## 4. Reveal types
- Pop-on (single frame): G0002, G0008, G0010, G0016, G0018, G0020, G0024, G0026, G0030, G0042, G0046, G0048, G0056, G0078.
- Panel-contents swap (frame retained): G0006, G0012, G0076, G0080, G0082.
- Dissolve/fade (6-8 frame): G0040, G0054, G0062, G0066, G0070 (G0068 LOW).
- Stepwise redraw of water level: G0004, G0034, G0036, G0038. No write-on is clearly visible; G0074 scribble onset UNRESOLVED.

## 5. Jokes / cutaways / callbacks
- Callback to opening: G0082 (102.5s) reuses G0010 waterfall panel; figure shrugs; ASR "There's only one way to find out" (102.62). G0084 (105.79s) blanks.
- Deadpan: G0012 figure holds a sheet; G0080 "EARTH (DEHYDRATED)" vs "MARS (JUST ADD WATER)" at 98.75s (ASR "Mars would warm up and the oceans would remain liquid").
- Rover damage: G0008 "!" (5.92s); G0060 tumbled rover (74.25s, ASR "perseverance is likely destroyed in the ensuing ice-rock waterfall").
- Place labels "MATT DAMON" and "TIANWEN" appear on map (G0052).
- Fish silhouettes in sea, G0026 (27.25s, ASR "oceans are saltwater").

## 6. Camera vs drawing vs cuts
- No CAMERA move observed. True shot cuts (composition replaced): G0014, G0022, G0028, G0032, G0044, G0052, G0058, G0062, G0064, G0072, G0084 = 11. Panel swaps = 5. Drawing/state animations = rest. INFERRED: many cuts alternate between panel-with-figure and full-bleed illustration.
- G0014 (13.25s) first full-bleed cut, G0058 wave, G0064 fully full-bleed ice layer.

## 7. Characters / objects / colour
- Stick figure: round head, single-line limbs, black ink; poses: hand on chin (default), holds paper (G0012-G0013), arms out (G0082-G0083). Rover is detailed (G0058, G0060). Colour is used heavily, beyond red: tan-grey sky, brown Mars, blue lake (G0044-G0050), grey water, brown Earth, blue Mars (G0080). Red used for the water-column cap line (G0006-G0082), small red dot at Curiosity (G0030, G0044) and scribble strike (G0074).

## 8. Unusual vs typical patterns
- Not a single persistent diagram: many distinct scenes (cross-section, elevation map, top-down map, place map, planet panel).
- Red is not only marks: also the recurring water-column cap and the Curiosity dot (marks nonetheless). Colour fills (blue, brown, tan) are unusual.
- Stick figure is not limited to jokes: it recurs in recap panels and map slides (G0052-G0063).
- Elevation-map image is greyscale raster with fine detail (G0028), unlike line drawing.
- Blank-end frame G0084-G0085 (105.79-106.04s).

## 9. Unresolved segments
G0016 (arrow count), G0017 (onset of patches/label), G0054 (which regions flip), G0068 (change unclear, LOW), G0074 (write-on timing). Also LOW/MEDIUM onsets for single-frame activities throughout; Water-level subtype labels (G0034-G0038) MEDIUM.


## 4. Art direction (MEASURED palette)
Background exact #F7F7F7; top quantised bins #F0F0F0 0.4114, #101010 0.2538, #B0B090 0.2355, #907070 0.0395, #D0D0D0 0.0219; mean settled dark-ink coverage 28.0% (max 65.9%); red accent present in 5/43 holds; any saturated colour in 29/43 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9795 (429/438 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
