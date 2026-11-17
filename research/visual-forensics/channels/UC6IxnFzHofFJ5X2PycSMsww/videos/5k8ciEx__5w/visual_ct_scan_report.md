# Visual CT scan — 5k8ciEx__5w "Circumference pop quiz!" (SHORT)

- Channel xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww`; format evidence: listed on channel /shorts tab (snapshot 2026-11-04T01:43:22Z); published 2025-08-05T10:00:04-07:00; public views at census 674672 (single snapshot; no CTR/retention).
- Source `/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Circumference pop quiz! [5k8ciEx__5w].mp4` sha256 `05fce38976a32594cc613ce3e6b88fe00fe3b62c7a38d090f287ae0d074fddd3`, 1080x1920 h264, 24/1 (CHECK: 501 distinct packet durations), time_base 1/12288, 501 decoded frames, 20.944 s.
- Mode DEEP with frame-precise onsets. Status **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED_CAPABILITY). Segment classification by fresh reviewer `rv1_5k8ciEx__5w` (Claude Code sonnet subagent; transcript audit: 2/2 sheets opened, 2 image results, validator errors 0); primary spot-check: 1 of 2 sheets re-viewed by primary, 10 rows compared, 0 disagreements.

## 1. Coverage (MEASURED)
All 501 frames measured. 19 segments = 10 HOLD states (492 frames, measured static; settled frame viewed) + 9 ACTIVITY events (9 frames; 9 viewed in tiles; 9 activities viewed at every frame). Encoder-refresh frames absorbed by rule: 1. Unresolved segments: G0011, G0012, G0016.

## 2. Structure (OBSERVED, from ledgers)
- 4 shots (composition replacements incl. cuts back), 9 activity events: GRAPHIC/TEXT 6, CAMERA 0, CHARACTER 0, LIGHT/COLOR/EFFECT 0, SHOT_CUT 3, FALSE_POSITIVE 0.
- Full per-segment descriptions: `tables/state_ledger.csv`; shots: `shot_ledger.csv`; events: `visual_event_ledger.csv`.

## 3. Reviewer observations (OBSERVED from tiles unless marked INFERRED; verbatim from `review/rv1_5k8ciEx__5w/observations.md`)


Note: each ACTIVITY segment is one frame, so only before/after states are visible; transition style (pop vs fade vs write-on) is mostly UNRESOLVED.

1. Premise. G0001 (0-1.4 s) opens on a lone black stick figure, arm raised, empty canvas. G0002 (1.42 s) a grey globe with a rope tied in a bow appears; held to 5.4 s (G0003). ASR: "tied a rope tightly around the earth" (0-3.7 s). INFERRED: the figure is a narrator presenting the puzzle. Question is bounded by the globe+rope image; ASR "raise the rope one meter" (6.96-10.96 s) is shown as the rope scene, not as text.

2. Steps. Visual order: globe+rope (G0003) -> cut to rope on posts with two figures (G0004, 5.46 s) -> cut to rope raised/straight with figures (G0006, 8.29 s) -> label '6.28m' (G0008, 12.46 s) -> cut to abstract diagram (G0010, 14.5 s) -> formula built in steps (G0012 'C = 2πr' 15.1 s, G0014 'C = 2π(r+1)' 16.3 s, G0016 '= 2πr + 2π' 18.2 s, G0018 red '~6.28' 19.3 s). Persistent anchor from G0010 on: globe with 'C' arrow ring at left (G0010-G0019); formula column at right grows downward. In the rope scenes the hair-bob figure and rope persist G0004-G0009.

3. Labels vs object. '6.28m' with leader arrow appears (12.46 s) after its figure is already on screen (since 8.29 s); ASR "answer is about six meters" at 11.56-16.18 s is near it. Diagram: ring 'C' present at the cut (G0010); radius arrow 'r' appears with 'C = 2πr' (G0012), ASR "Circumference is proportional to radius" nearby. Final number '~6.28' appears at 19.29 s, ASR "two pi units" (16.3-20.3 s).

4. Reveal types. OBSERVED: full-composition replacements (G0004, G0006, G0010); object appearance (globe G0002); label additions (G0008, G0018); text edits (G0012, G0014, G0016). Write-on vs pop-on is UNRESOLVED because single-frame activity; no dissolve or camera move observed.

5. Jokes/callbacks. None clearly visible. INFERRED mild deadpan: figure with hand on hip at the rope (G0006-G0009) near ASR "Miles? Hundreds of miles?". Callback: globe from G0002 reappears as the diagram in G0010 (new style, light grey, with arrow ring).

6. Counts. True cuts: 3 (G0004, G0006, G0010). Camera motion: 0 observed. Drawing/text updates: 6 (G0008, G0012, G0014, G0016, G0018) plus object pop-on G0002 = 6 total graphic events. False positives: 0 (G0011's possible shift UNRESOLVED).

7. Characters/objects. Stick figures: round blank head, line body; one has a black filled bob hairstyle with small motion marks (G0004). Globe: grey fill with lighter grey continents, black outline, small rope bow. Rope scenes: line rope with short vertical posts. Colour: black ink, greys; red appears only in '~6.28' (G0018). The '6.28m' label in G0008 is black.

8. Unusual. Not a single persistent diagram: scenes change three times, with the formula diagram only in the last third (14.5-20.8 s). Stick figures appear in the opening and rope scenes (not only jokes); they disappear from the explanatory diagram. Red used for the result number, not for marks/strikes. Two different Earth renderings across cuts.

9. Unresolved. G0011 (possible slight layout/size shift vs G0010; LOW). Reveal method (write-on vs pop-on vs fade) for G0002, G0012, G0016 (MEDIUM). No segment fully unreadable.


## 4. Art direction (MEASURED palette)
Background exact #FDFDFD; top quantised bins #F0F0F0 0.9774, #101010 0.0095, #D0D0D0 0.0077, #707070 0.0025, #505050 0.0014; mean settled dark-ink coverage 1.4% (max 2.1%); red accent present in 1/10 holds; any saturated colour in 1/10 holds. Typeface, software and layer structure UNAVAILABLE.

## 5. Audio
ASR faster-whisper small.en (PROVISIONAL_ASR_NOT_LISTENING); word-sequence agreement with catalog plaintext captions ratio 0.9202 (75/80 caption words). Listening, music/SFX, delivery: UNAVAILABLE. AV relations in `audio_visual_alignment.csv` are ASR_UNCERTIFIED nearest-word lags.

## 6. Limits
Hold interiors verified by measurement, not by viewing every frame; activity in-between frames sampled where noted in coverage.json; tile scale 1/4 (small text partly unreadable); reviewer is same model family as orchestrator (not independent human review).
