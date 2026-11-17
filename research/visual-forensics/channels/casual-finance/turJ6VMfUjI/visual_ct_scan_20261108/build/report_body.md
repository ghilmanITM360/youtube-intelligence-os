## 2. Macro structure (OBSERVED, timings MEASURED)
| Act | Frames | Time | What happens |
|---|---|---|---|
| A. Bank and Earth hook | f0-f96 | 0.00-3.23 s | bank held on money bags, pile of briefcases and papers, Earth lowered on top and sweating |
| B. "Impossibly complex math" | f97-f211 | 3.23-7.03 s | collage with a whiteboard video clip |
| C. "Carved in stone / passed down" | f212-f335 | 7.07-11.2 s | stone tablet "2%", ancient-knowledge man, stick man |
| D. "Somebody chose it" / "Why 2%?" | f336-f418 | 11.2-13.93 s | pointing hand and red 2%, teacher and blackboard |
| E. Inflation icons | f419-f572 | 13.97-19.07 s | car, house, bag, oil barrel, price tags pop in, worried stick man |
| F. "0% sounds great, in reality it's not" | f573-f739 | 19.1-24.63 s | paper card, green 0%, laughing face, frowning stick man |
| G. Recession and the Fed | f740-f1040 | 24.67-34.67 s | bar-chart character, central bank, coin sliced, Earth with 0% inflation, coin sinks, stick man |
| H. One cut, maybe two, then zero | f1041-f1217 | 34.7-40.57 s | coin slices, "Can't cut any more!", US map trapped |
| I. Spiral into depression | f1218-f1342 | 40.6-44.73 s | chart character falls, close-up with fallen green critter |
| J. Don't aim too high | f1343-f1492 | 44.77-49.73 s | percent ladder to 4%, grocery bag = banknote, "18 years later" |
| K. Business can't forecast | f1493-f1655 | 49.77-55.17 s | building and boxes, cost question, contract and guessing |
| L. Goldilocks 2% | f1656-f1900 | 55.2-63.3 s | 2% turns yellow, cushion, money bags, flames, sunglasses man and "Ah, forgot that was there." |

Hard cuts (25, each verified on adjacent decoded frames; entry change MEASURED): f97, f212, f311, f336, f374, f419, f573, f684, f740, f779, f851, f903, f958, f1041, f1111, f1134, f1159, f1218, f1275, f1343, f1441, f1493, f1560, f1656, f1806. State length mean 1.02 s, median 0.82 s; longest S004 (115 frames, 3.83 s, the whiteboard-clip collage), then S002 (77 fr, bank/Earth stacking) and S043 (69 fr, close-up on the chart character).

## 3. Caption track (MEASURED)
- A burned-in caption line (black handwritten-style text, lower middle) changes 220 times in 63.4 s (about every 0.29 s), growing word by word and resetting between phrases; each change is a hard swap on the viewed frames. Measured as changed pixels in rows >= 1250 (`tables/caption_events.csv`, `caption_event_ledger.csv`).
- Against ASR word starts the caption changes have median lag 0.007 s (p10 -0.107, p90 +0.12; 209/220 within 0.2 s): captions appear on the spoken word. With words arriving every 0.3 s on average this closeness alone is weak evidence (see the control in section 5).
- Caption text read on all viewed frames matches the ASR wording on those frames (e.g. "the Fed gets one cut", "maybe two", "structurally trapped", "so 2% is that goldilocks number"); not read for every one of the 220 changes, so the text gate is PARTIAL.

## 4. Motion, camera and design
- **No camera moves:** the frame is locked; all motion is object-level. Camera = NOT_APPLICABLE; the only scroll is the percent ladder (f1394-f1415) and the coin drift (f903-f939).
- **Pop-ins dominate:** 26 of 62 states enter by a single-frame pop (price tags f440, f455, f478, f498; speech bubbles f252, f1521, f1849; text f353, f393, f605, f869, f1461, f1633; coin slices f811, f1063, f1083, f1093); no scale or opacity easing is visible on adjacent frames.
- **Eased/animated entries:** bank/Earth stack (f1-f77), hand slide-in (f336-f352), chart character slide-in (f980-f996), 2%-cushion reveal (f1712-f1805) sampled at 4-8 frame steps; easing curves not measured (UNAVAILABLE).
- **One embedded clip:** a short video clip of a bearded man at a whiteboard in S004 (f97-f211); every other scene is drawn.
- **Palette (MEASURED, k-means on 12 viewed frames, `tables/palette.json`):** canvas #fcfcfc covers 86-99 % of every sampled frame; accents are blackboard green #35853a, US-map green #46a44b, bar-chart blue #1d4fc1 / #2050c2, red handwriting and arrows, orange coin, yellow 2% with black outline, beige cushion #d8d5bb.
- **Typography (OBSERVED):** caption in a rounded handwritten-style sans (black); red handwritten percentages; chalk font on the blackboard ("Why 2%?"); tiny handwritten lines in bubbles; exact typefaces not identified.
- **Composition:** a single small cluster in the middle third of a 9:16 frame, one idea per state, large empty white above and below; the caption sits just under the cluster. Medium: flat 2D hand-drawn icons and stick figures; AI vs human origin cannot be determined.
- **Hierarchy (INFERRED salience hypothesis, not gaze data):** the isolated cluster and the changing caption word are the only high-contrast marks.

## 6. Story and editing (INFERRED, labelled)
- Structure: question in the hook ("what number is the whole system anchored to?"), myth rejection (not math, not stone), "somebody chose it", then a reasoning chain with a visual per step: why not 0% (recession, Fed has one or two cuts, hits zero, depression), why not 4% (prices double every 18 years, businesses cannot forecast, contracts need guessing), conclusion (2% is the Goldilocks cushion), and a closing gag.
- Cut rhythm: 25 hard cuts in 63.4 s (one per 2.5 s); the same stick-man plate returns four times as a neutral beat (f311, f684, f958, f1343).
- Counterexamples to the pop-in rule: the opening 96 frames and the recession-to-zero beat use continuous motion; there is no camera move anywhere.

## 7. Issues and optional improvements (all INFERRED, optional)
- The whiteboard clip is the only photographic element and appears for 3.8 s with no readable content; it reads as texture rather than evidence.
- A one-frame micro change at f1834 could not be resolved at tile scale (flagged, not guessed).
- Thumbnail/title not re-fetched; economic claims in narration not fact-checked.

## 8. Declared limitations
No listening; ASR unverified; quiet frames inside holds measured unchanged but not individually viewed; changes below about 150 changed full-res pixels in the content band (or 0.08 % of the 160 px content map) are not detected; the stack animation (f1-f77) and cushion reveal are sampled at 4-8 frame steps; the micro change at f1834 is unresolved; easing and typefaces not measured; captions measured but not read for all 220 changes.
