## 2. Macro structure (OBSERVED, timings MEASURED)
| Act | Frames | Time | What happens |
|---|---|---|---|
| A. Hook: "pattern repeated" | f0-f153 | 0.00-5.13 s | "?" circles scroll in, chart icon and money bag, more "?" circles pop |
| B. Bubble gag | f154-f253 | 5.13-8.43 s | dollar sign, bubble inflates, bursts |
| C. "Right in front of their eyes" | f254-f365 | 8.47-12.17 s | stick man and a sweating Earth |
| D. Back to June 2007 | f366-f439 | 12.2-14.63 s | year timeline scroll, calendar icon |
| E. Wall Street booming | f440-f540 | 14.67-18.0 s | Wall St sign with clips, "The market:" fire clip, stick man |
| F. Blackstone founders cash in | f541-f729 | 18.03-24.3 s | logo, two portraits, stick man, yacht clip, stick man |
| G. Peter Peterson joke | f730-f849 | 24.33-28.3 s | baby-bed cartoon, name bubble, newborn close-up |
| H. $2.6 billion | f850-f1046 | 28.33-34.87 s | article page, logo and portraits pop in, banknotes fall, text highlighted |
| I. Crisis a year later | f1047-f1191 | 34.9-39.7 s | timeline, burning Earth, red news tiles |
| J. Stock -90% | f1192-f1288 | 39.73-42.93 s | candlestick chart, arrow, "90%", worried face |
| K. "Knew it was time to exit" | f1289-f1460 | 42.97-48.67 s | search card, red ellipse, logo tilts out with "bye-bye" |
| L. IPO data | f1461-f1659 | 48.7-55.3 s | table page, stick man leans in, column highlight, check, skyscrapers and bubble with crowd clip |

Hard cuts (verified on adjacent decoded frames; entry change MEASURED): f99, f154, f254, f366, f440, f477, f511, f541, f631, f664, f707, f730, f780, f825, f850, f1047, f1105, f1160, f1192, f1289, f1461 (21; f477 is BOUND(476-477)). State length mean 0.907 s, median 0.833 s; longest 81 frames (S039, banknotes fall over the article, 2.7 s), then S010 (75 fr, bubble inflating) and S061 (72 fr, crowd clip in bubble); the longest pure hold is 23 frames (S054).

## 3. Caption track (MEASURED)
- A burned-in caption line (black handwritten-style text, lower middle) changes 190 times in 55.3 s (mean 0.29 s apart), growing word by word and resetting between phrases. Each change is a hard text swap (no fade seen on viewed frames). Measured as changed pixels in rows >= 1250 (`tables/caption_events.csv`, `caption_event_ledger.csv`).
- Against ASR word starts the caption changes have median lag 0.013 s (p10 -0.12, p90 +0.12; 179/190 within 0.2 s), i.e. captions appear on the spoken word. Because words arrive every 0.3 s on average, closeness is weak evidence by itself (see the control in section 5).
- Caption text was read on all viewed frames and matches the ASR text on those frames (examples: "it's a pattern that's repeated", "every major financial bubble pops", "Steven Schwartzman and Peter Peterson", "walked away with about $2.6 billion"); it was not read for every one of the 190 changes, so the text gate is PARTIAL.

## 4. Motion, camera and design
- **No camera moves:** the frame is locked; all motion is object-level. Camera = NOT_APPLICABLE except the timeline scroller (object scroll, f366-f399 and f1065-f1086).
- **Pop-ins dominate:** 21 of 61 states enter by a single-frame pop (portraits, logos, bubble, "?" circles, check mark, "90%"); there is no scale/opacity easing visible on adjacent frames.
- **Eased/animated entries:** Earth slides in (f303-f319), logo tilts and slides out (f1391-f1437), stick man leans in (f1470), highlight sweeps a table column (f1534-f1561), bubble inflates (f155-f229). Easing curves not measured (UNAVAILABLE).
- **Embedded clips:** five scenes carry looping clips (Wall St traders, fire puppet, yacht, red tiles, crowd); these are third-party-looking clips inside a flat canvas.
- **Palette (MEASURED, k-means on 13 viewed frames, `tables/palette.json`):** canvas #fcfcfc covers 68-97 % of every sampled frame; accents are teal bubble #7cbfbd, green dollar and Earth #4a7d42/#4f7a45, flame orange #ce771f, news-tile red #5b0b14, dark search card #212227 and Wall St sign #2b303c; red hand-drawn arrows and "90%" are the only saturated annotation colour.
- **Typography (OBSERVED):** caption in a rounded handwritten-style sans (black), "Wall St" sign lettering, handwritten red "90%", serif "Blackstone" logo; article/table text is tiny and unreadable at phone size. Exact typefaces not identified.
- **Composition:** content is a small cluster in the middle third of a 9:16 frame with large empty white above and below (the canvas colour covers 68-97 % of the pixels of every sampled frame); the caption sits just below the cluster. Medium: flat 2D hand-drawn icons and one-line stick figures plus small screenshots and clips; AI vs human origin of drawings cannot be determined.
- **Hierarchy (INFERRED salience hypothesis, not gaze data):** the isolated centre cluster and the moving caption word are the only high-contrast marks, so they likely take the first look.

## 6. Story and editing (INFERRED, labelled)
- Structure: curiosity hook (question marks), a thesis in 8 s ("pattern before every bubble pops"), then a single worked example (Blackstone 2007) told as a chain: boom, founders cash out ($2.6 bn), crisis, stock -90%, "knew it was time to exit", then the generalisation from IPO data (booming markets -> companies go public and sell shares). Gags (bubble, Peter Peterson baby, bye-bye logo) sit between factual beats.
- Cut rhythm: 21 hard cuts in 55.3 s (one per 2.6 s); the same stick-man plate recurs 5 times as a reset between evidence cards (cuts at f254, f511, f631, f707, f825).
- Counterexamples: the first 99 frames have no cut (continuous "?" scroll), and the last scene (f1461-f1659, 6.6 s) holds one table page while annotations pile up, the longest single-plate scene.

## 7. Issues and optional improvements (all INFERRED, optional)
- Article, table, search-card and chart-axis text are unreadable at phone width; the evidence shown cannot be read, so the claim rests on narration.
- Between 68 % and 97 % of every sampled frame is empty white canvas; an optional test would enlarge the content cluster to the frame width.
- Thumbnail/title not re-fetched; figures ($2.6 billion, -90 %) not fact-checked against the sources shown.

## 8. Declared limitations
No listening; ASR unverified; quiet frames inside holds measured unchanged but not individually viewed; changes below about 150 changed full-res pixels in the content band (or 0.08 % of the 160 px content map) are not detected; the yellow highlight onset on the article (f970-f990) and the pop frames of overlapping red tiles (f1161-f1176) are inside animated intervals and were not isolated; embedded clip contents are not analysed beyond their presence; easing and typefaces not measured; captions measured but not read for all 190 changes.
