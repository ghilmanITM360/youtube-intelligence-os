# Visual CT scan report - CFrVTZBYa3Q (Casual Finance) - visual-only scope
Reader: Claude Sonnet 5.5, Machine A, 2026-11-08. Mode CT_SCAN (visual). Audio: ASR only, never heard. See `quality_gate.json` (visual-only, declared coverage; AV sign-off BLOCKED).

## 1. Source and coverage (MEASURED, generated)
- File `You_re Celebrating Stocks, They_re Heading For The Exits. [CFrVTZBYa3Q].mp4`; SHA-256 `933c909aa3e58b66ad58d9b759acd852f2d3f69f915ca2d1598d11b5db528a5e`; 6,709,178 bytes. Identity: filename `[ID]` and roster/queue EXACT_ID_MATCH where stated; live YouTube not re-checked.
- h264 1080x1920 yuv420p, 24/1 fps, CFR: 1189 frames, delta [0.04167] s, PTS = frame/24, last PTS 49.500; 18 I-frames.
- Pass 1 (MEASURED): all 1189 frames decoded once; 320 px changed-fraction, mean abs difference, luma, 4x4 grid, full-res changed pixels -> `tables/frame_metrics.csv`; 37 candidate episodes -> `tables/episodes.csv`.
- Pass 2 (OBSERVED): 1 fps overview, all 37 episodes viewed (decoded frames start-1/start/mid/end/end+1), 23 native consecutive-frame windows, 12 stepped sheets, one representative decoded frame per state (70) compared with the ledger. No interpolated frames.
- Result: 70 states contiguous f0-f1188; 18 shots; 17 hard cuts + start; 70 events; onset precision 43 EXACT, 7 BOUND (<= 6-frame windows), rest MEAS (activity edge).

## 2. Macro structure (OBSERVED, timings MEASURED)
| Act | Frames | Time | What happens |
|---|---|---|---|
| A. Five bond-yield chart scenes | f0-f483 | 0.00-20.17 s | US 30y (2007 high), UK 30y (1998), Germany 30y (2011), Japan 10y (1999), Japan 30y (all-time high); each = screenshot chart panned right, then overlays |
| B. Flag recap grid | f484-f555 | 20.17-23.13 s | four flag icons + four chart thumbnails pop in one by one (US f484, UK f488, Germany f492, Japan f494) |
| C. Doge analogy | f556-f643 | 23.17-26.79 s | Doge coins fade over the flags; Dogecoin/Bitcoin chart; Elon tweet screenshot and a peeking head |
| D. Blackboard question | f644-f703 | 26.83-29.29 s | teacher at a blackboard; "One VERY important question:" |
| E. Meme and sleepy bonds | f704-f800 | 29.33-33.33 s | reaction-meme video with two "???", blank, two bond drawings, sleeping armchair figure |
| F. Blackboard "Predictable / Uneventful" | f801-f861 | 33.375-35.88 s | stern teacher, two chalk bullets typed on with pointer pops |
| G. Old man falls asleep | f862-f922 | 35.92-38.42 s | old man says a line, then dozes, three z marks added one by one |
| H. Party | f923-f1004 | 38.46-41.83 s | confetti party scene; thought bubble "These people are mad" |
| I. "But right now," | f1005-f1019 | 41.875-42.46 s | stick man, text typed on character by character |
| J. S&P 500 | f1020-f1088 | 42.5-45.33 s | dark finance screenshot, two characters hop in, chart pans right, green ellipse |
| K. AI chatter | f1089-f1116 | 45.375-46.50 s | chart grid, robot rises with thumbs up |
| L. Plug pulled | f1117-f1188 | 46.54-49.54 s | Treasury character unplugged at f1157; black from f1167 (0.917 s) |

Hard-cut frames (each verified on adjacent decoded frames, entry change MEASURED in `shot_ledger.csv`): f99, f203, f296, f423, f484, f585, f644, f704, f746, f801, f862, f923, f1005, f1020, f1089, f1117, f1167.
State length: mean 0.708 s, median 0.583 s; longest S030 (62 frames = 2.58 s, the four-flag grid hold). Of 70 states, 12 are pure holds.

## 3. Motion and camera findings
- **Recurring chart module (OBSERVED, n=4 full cycles + US variant):** hard cut to a wide chart screenshot already panned to its left end -> camera pans right across it for 3.46 s (UK, f99-f181), 3.25 s (Germany, f203-f280), 3.33 s (Japan 10y, f296-f375), 2.12 s (Japan 30y, f423-f473), 2.04 s for the US opener (f1-f49, where the yield line also draws on) -> a red arrow slides in at the right edge -> a handwritten "since YEAR" label pops in -> a country-map character rises from the bottom edge.
- **Overlay cadence (MEASURED from onsets):** UK cut f99, arrow f135 (+36 fr), label f164 (+65), character f165; Germany cut f203, arrow f227 (+24), label f268 (+65), character f269; Japan 10y cut f296, arrow f326 (+30), circle f339 (+43), label f375 (+79), character f386 (+90). Label comes about 65 frames (2.7 s) after the cut in both UK and Germany; n=2 so this is a pattern, not a rule.
- Pop-ins are single-frame (no scale/opacity easing visible on adjacent frames): "since" labels, speech/thought text, chalk bullets, flag rows, "???", armchair, z marks. Text that is *typed on* (one character per frame) appears only for "But right now," (f1006-f1012).
- Camera type: all pans are horizontal digital pans of a screenshot wider than the 1080 px frame (content moves left); easing curve not measured (ease-in/out vs linear would need per-frame offset tracking; marked UNAVAILABLE). The Doge/tweet scene uses a vertical scroll-up (f612-f627). The S&P scene pans right (f1048-f1067) while two characters stay fixed in screen space.
- Character motion: slides/rises from frame edges over 10-18 frames (UK/Germany/Japan maps, robot f1092-f1101, S&P pair f1022-f1034), a looping dancing Doge sprite (f556-f584), one idle bob (f1117-f1153), pose swaps (teacher pointer up/down at f816, f824, f838, f845; old man doze f889).
- Shot cuts: all 17 cuts are hard cuts (no dissolves or wipes); fade-to-black is a hard cut to black at f1167.

## 4. Art direction and design
- **Medium (OBSERVED):** flat 2D hand-drawn explainer on a near-white canvas (#fcfcfc covers 52-95 % of sampled frames) mixing (a) news-outlet and data-vendor chart screenshots, (b) a reaction-meme video clip, social-post screenshot, and a dark finance-app screenshot, (c) original-looking flat characters with thick uneven black outlines. Whether characters are hand-drawn or AI-assisted cannot be determined from frames.
- **Palette (MEASURED, k-means on 12 viewed frames, `tables/palette.json`):** canvas #fcfcfc; chart hues pink #c69aa1 (UK), orange #eeab53 (Germany, Japan 30y), purple (US), black line (Japan 10y); characters' country-map green #4d9953 / #509355; blackboard green #37843e with brown frame #6a5046; skin #efd2b8 / #f5d2b7; old-man beige #cdd0b1; armchair red #b14f4d; dark app panel #212228 (42 % of f1020). Red handwritten year labels and arrows are the single saturated accent that repeats in every chart scene.
- **Typography (OBSERVED):** three registers: (1) tiny grey/black sans in screenshots, unreadable at phone size beyond headlines; (2) handwritten display for "since" (black, small) over the year (red, large); (3) chalk-style white font on the blackboard and a handwritten black type-on font for "But right now,". Exact typefaces not identified.
- **Composition:** vertical 9:16 with a full-width screenshot in the upper two thirds and characters/overlays in the lower third; characters are cropped by the frame edge, which keeps the chart readable. Static anchors: the white canvas, the chart image position (between pans) and the lower-third character slot.
- **Hierarchy (INFERRED salience hypothesis, not gaze data):** large red year label and red arrow on white are the highest-contrast marks in each chart scene, so they likely draw the eye before the chart line.

## 6. Story and editing (INFERRED, labelled)
- The video states a thesis in 20 s with five identical-format chart "proofs", then switches visual grammar (blackboard, memes, characters) at the first rhetorical question, returns to a screenshot-plus-character grammar for the S&P/AI context, and ends on a visual pun (the Treasury character being unplugged) timed to the final clause, followed by 0.92 s of black.
- Cut rhythm: 17 hard cuts in 49.5 s (one per 2.9 s on average); chart scenes run 3.3-4.2 s each, character gag scenes 1.5-3.4 s.
- Counterexamples to the chart module: Japan 30y has no "since" label (it is "all-time high"), and its character is a different dizzy variant; the S&P scene pans but has no arrow/label; the AI chart scene has no pan.

## 7. Issues and optional improvements (all INFERRED, optional)
- Tweet screenshot, chart axes and S&P footer text are below readable size at phone width (OBSERVED unreadable); an optional fix is to crop to the one figure that matters.
- Two stills with no state change for 2.6 s (flag grid hold f494-f555) are the longest static interval; a test would be to add the Doge fade earlier or shorten the hold.
- Thumbnail/title not re-fetched; chart figures on screen not fact-checked.

## 8. Declared limitations
No listening; ASR text unverified; quiet frames inside holds were measured unchanged within threshold but not individually viewed; changes below about 0.06 % of pixels at 320 px (about 35 px) and below 300 changed full-res pixels are not detected; pan easing and exact typefaces not measured; seven overlay onsets carry a window of up to 6 frames (BOUND); shot count is exact here because every cut was a hard cut.


## Audio alignment (generated; ASR_UNCERTIFIED - nobody listened)
- Whisper small.en text: The 30-year Treasury yield just hit the highest level since 2007. The UK's 30-year just climbed to its highest level since 1998, while Germany's 30-year reached its highest level since 2011. And not only did Japan's 10-year rise to levels it hadn't seen since 1999, but Japan's 30-year is now sitting at an all-time high. So when four of the largest sovereign bond markets in the world start doing their best impression of Dogecoin after an Elon Musk tweet, it raises one very important question. What the f**k is happening? Because the bond market's supposed to be boring, it's supposed to be predictable, uneventful, and something your grandpa falls asleep watching. And that's why it often gets labeled as the adult in the room. But right now, while everyone's distracted watching stocks go vertical and the AI hype, the adult in the room quietly just pulled the plug on the party.
- Phrase-level pairs (31, `audio_visual_alignment_phrase.csv`): median visual-minus-word lag -0.040 s, p10 -0.135, p90 0.075; 24/31 within 0.1 s, 31/31 within 0.3 s; visual leads in 21, trails in 10. Control: random times lie within 0.1 s of some word start 57% and within 0.3 s 90% of the time, so closeness alone is weak evidence; the pairing of the right word is the evidence.
- Nearest-word table for all non-hold events: `audio_visual_alignment.csv` (58 rows, median lag -0.014 s). Music, SFX, tone: UNAVAILABLE.
