# Visual CT scan report - SYSUh-oow6M (Casual Finance) - visual-only scope
Reader: Claude Sonnet 5.5, Machine A, 2026-11-08. Mode CT_SCAN (visual). Audio: ASR only, never heard. See `quality_gate.json` (visual-only, declared coverage; AV sign-off BLOCKED).

## 1. Source and coverage (MEASURED, generated)
- File `Why Being a Millionaire Doesn_t Impress Anyone... [SYSUh-oow6M].mp4`; SHA-256 `bdd68c91f25f935f3adbb15e3b5e151708ed67872e9985c134b797227465a88e`; 4,202,276 bytes. Identity: filename `[ID]` and roster/queue EXACT_ID_MATCH where stated; live YouTube not re-checked.
- h264 1080x1920 yuv420p, 30/1 fps, CFR: 2616 frames, delta [0.03333] s, PTS = frame/30, last PTS 87.167; 30 I-frames.
- Pass 1 (MEASURED): all 2616 frames decoded once; 320 px changed-fraction, mean abs difference, luma, 4x4 grid, full-res changed pixels -> `tables/frame_metrics.csv`; 75 candidate episodes -> `tables/episodes.csv`.
- Pass 2 (OBSERVED): 1 fps overview, all 75 episodes viewed (decoded frames start-1/start/mid/end/end+1), 1 native consecutive-frame windows, 2 stepped sheets, one representative decoded frame per state (79) compared with the ledger. No interpolated frames.
- Result: 79 states contiguous f0-f2615; 30 shots; 29 hard cuts + start; 79 events; onset precision 74 EXACT, 1 BOUND (<= 6-frame windows), rest MEAS (activity edge).

## 2. Macro structure (OBSERVED, timings MEASURED)
| Act | Frames | Time | What happens |
|---|---|---|---|
| A. Rich man and cash | f0-f95 | 0.00-3.17 s | glasses man slides right as banknote piles multiply |
| B. Mansion, cigars, yacht | f96-f195 | 3.2-6.5 s | stick man then three props pop in |
| C. Name weight like a villain | f196-f300 | 6.53-10.0 s | man at counter, boast bubble, pale figure |
| D. "How to win at capitalism" | f301-f409 | 10.03-13.63 s | three-step list |
| E. The finish line and the dream | f410-f518 | 13.67-17.27 s | laughing figure with thought cloud; rich man with car, house, money bags |
| F. Almost nobody reached it | f519-f587 | 17.3-19.57 s | cash man and three small figures |
| G. 1848 chart | f588-f781 | 19.6-26.03 s | stick man, historic bar chart, stick man |
| H. 1 in 84,000 and Chicago | f782-f1052 | 26.07-35.07 s | text, houses, Chicago map, 13 millionaires |
| I. Two categories | f1053-f1479 | 35.1-49.3 s | MILLIONAIRES splits, slope with east-coast elites and a farm owner, stick man |
| J. Black pause | f1480-f1526 | 49.33-50.87 s | 47 frames of full black |
| K. Industrialization | f1527-f1669 | 50.9-55.63 s | stick man, US map with factories added one by one |
| L. 5,000 millionaires and decades | f1670-f1934 | 55.67-64.47 s | green infographic, decade timeline scroll |
| M. Today it's the norm | f1935-f2472 | 64.5-82.4 s | stick man, man with banknote, Millionaire Mirage card with ellipse, Fed report, UBS paragraph |
| N. 1 in 6 households | f2473-f2615 | 82.43-87.17 s | green infographic and a red ellipse |

Hard cuts (29, each verified on adjacent decoded frames; entry change MEASURED): f96, f114, f196, f301, f410, f447, f519, f588, f667, f765, f782, f857, f989, f1053, f1141, f1371, f1480, f1527, f1582, f1670, f1829, f1935, f1991, f2023, f2160, f2249, f2338, f2381, f2473. State length mean 1.12 s, median 1.02 s; longest S063 (116 frames, 3.87 s, the households infographic), then S030 (98 fr, historic chart), S078 (95 fr) and S077 (92 fr).

## 3. Caption track (MEASURED)
- A burned-in caption line (black handwritten-style text, lower middle) changes 238 times in 87.2 s (about every 0.37 s), growing word by word and resetting between phrases; each change is a hard swap on the viewed frames. Measured as changed pixels in rows >= 1250 (`tables/caption_events.csv`, `caption_event_ledger.csv`).
- Against ASR word starts the caption changes have median lag 0.013 s (p10 -0.127, p90 +0.10; 233/238 within 0.2 s). With words arriving every 0.3 s on average this closeness alone is weak evidence (control in section 5).
- Caption text read on all viewed frames matches the ASR wording on those frames (e.g. "there was a time when being a millionaire actually meant", "one in every six households in", "has a million dollar net worth"); not read for every one of the 238 changes, so the text gate is PARTIAL.

## 4. Motion, camera and design
- **No camera moves:** the frame is locked; all motion is object-level (man slide f1-f30, word split f1093-f1104, timeline scroll f1829-f1912).
- **Pop-ins dominate:** 35 of 79 states enter by a single-frame pop; no scale or opacity easing is visible on adjacent frames. Characters change by pose swaps (8 POSE states), not by animation.
- **Black beat:** f1480-f1526 is a fully black frame run aligned with an ASR gap (last word ends about 49.0 s, next starts 50.96 s), i.e. the cut hides a pause.
- **Palette (MEASURED, k-means on 13 viewed frames, `tables/palette.json`):** canvas #fcfcfc covers 88-98 % of every sampled frame; accents are US-map green #47a14e, Chicago teal #47a2af, infographic mint #9cecb5, counter brown #463226, dark card #13181b, banknote green #82ae68, red annotations.
- **Typography (OBSERVED):** caption in a rounded handwritten-style sans (black); bold handwritten "ONE in" and "84,000" in red; "MILLIONAIRES" in a hand-lettered caps style; small embedded article/report/chart text is unreadable at phone size; exact typefaces not identified.
- **Composition:** one small cluster in the middle third of a 9:16 frame, one idea per state, large empty white above and below; the caption sits just under the cluster. Medium: flat 2D hand-drawn icons and stick figures plus small embedded charts and screenshots; AI vs human origin cannot be determined.
- **Hierarchy (INFERRED salience hypothesis, not gaze data):** the isolated cluster and the changing caption word are the only high-contrast marks.

## 6. Story and editing (INFERRED, labelled)
- Structure: nostalgic hook (being a millionaire used to mean mansion, cigars, yacht), joke about the "final boss of the American dream", historical evidence (about 50 millionaires in 1848, one in 84,000 households, 13 in a Chicago-sized city), who they were (east-coast elites, southern farm owners), black pause, industrialization (factories added one by one), then the modern reversal (average household net worth just over $1 million; one in six households).
- Cut rhythm: 29 hard cuts in 87.2 s (one per 3.0 s); the stick-man plate returns 7 times plus a pointer variant as a neutral beat.
- Counterexamples to the pop-in rule: slide at the start, the word split, the timeline scroll and the black pause are the only non-pop timing devices.

## 7. Issues and optional improvements (all INFERRED, optional)
- Infographics, the report cover, the Millionaire Mirage card and the UBS paragraph are unreadable at phone size; the evidence is audible but not legible.
- A 1.57 s black frame mid-video could read as a playback glitch to some viewers; optional test: a held neutral plate instead.
- Thumbnail/title not re-fetched; figures (84,000, 13, 22 million, one in six) not fact-checked against the sources shown.

## 8. Declared limitations
No listening; ASR unverified; quiet frames inside holds measured unchanged but not individually viewed; changes below about 150 changed full-res pixels in the content band (or 0.08 % of the 160 px content map) are not detected; the man's slide (f1-f30) and the prop piles at f43 are sampled, not per-frame; one micro change at f283 is unresolved; the first banknote stack onset is BOUND(17-31); easing and typefaces not measured; captions measured but not read for all 238 changes.


## Audio alignment (generated; ASR_UNCERTIFIED - nobody listened)
- Whisper small.en text: There was a time when being a millionaire actually meant something. It meant you had the mansion, the cigars, and the yacht. And it meant your name carried the same weight as Lord Voldemort's. Because for most of American history being a millionaire wasn't a milestone, it was the finish line. It was the final boss of the American dream. And almost nobody reached that status. Because if you rewind back to 1848, there were about 50 millionaires in the entire United States, which is roughly one in every 84,000 households. That means if you gathered every household in a city the size of modern-day Chicago, you'd find about 13 millionaires. And the millionaires at the time were split into two categories. About half of them lived on the east coast in New York or Philly, where they were industrial elites, bankers, or port owners. And the other half, uh, well, they were farm owners in the south. Anyways, then something happened. Industrialization took off and America scaled. And by the early 1900s, the number of millionaires grew from 50 to roughly 5,000. And if you keep fast forwarding through time to where we are today, being a millionaire is not rare anymore. It's just the norm. Because today, the average American household has a net worth of just over one million. That's the average. And that's not an exaggeration. That's data coming directly from the Federal Reserve. And according to UBS, the United States now has roughly 22 millionaires, which means roughly one in every six households in America has a million-dollar net worth.
- Phrase-level pairs (48, `audio_visual_alignment_phrase.csv`): median visual-minus-word lag -0.104 s, p10 -0.213, p90 0.007; 21/48 within 0.1 s, 48/48 within 0.3 s; visual leads in 41, trails in 6. Control: random times lie within 0.1 s of some word start 55% and within 0.3 s 88% of the time, so closeness alone is weak evidence; the pairing of the right word is the evidence.
- Nearest-word table for all non-hold events: `audio_visual_alignment.csv` (76 rows, median lag -0.087 s). Music, SFX, tone: UNAVAILABLE.
