# 07 Science and physics visual layer: how the xkcd What If? videos put a quantity on screen

Status: **self-review, one coder (me), small sample, still frames only.** New perception was done in this phase: 47 frames viewed on contact sheets. Nothing here is a performance claim, and nothing here copies artwork: it describes devices (how a quantity is drawn), not the drawings.

## 1. Question and design

Question: when the narration states a number or a scale comparison, what does the screen show at that moment?

- **Sample (coding set):** the 24 long videos with ledgers, sorted by ID, every 2nd (12 videos). In each, ASR segments matching a quantity regex (digits, units, "times", "bigger", etc.); the 2 hits closest to 1/3 and 2/3 of the runtime. Still frame at the segment midpoint. `scripts/phase7_sample.py` -> `07_SAMPLE_FRAMES.csv`, 24 frames.
- **Holdout:** the other 12 videos (odd positions), same rule, `scripts/phase7_holdout.py` -> `07_HOLDOUT_FRAMES.csv`, 23 frames (one video had one hit). **The scheme below was frozen before the holdout was viewed.**
- **Coding scheme (frozen):**
  - `device` (primary way the frame carries the quantity): `LABEL` numeral/unit text on or beside the drawing; `AXIS` a scaled line, depth axis or ordinal axis; `SBS` side-by-side comparison with numerals; `SCALEREF` a figure or object drawn to give size; `MAP`; `MECH` mechanism or process diagram; `TALLY` data tally; `OBJ` a labelled object with no quantity.
  - `spoken_qty_restated`: `YES` the spoken number or ratio is on screen (unit conversion counted if the arithmetic holds); `PARTIAL`; `NO` not on screen at that instant; `UNCLEAR` cannot tell from the frame; `NA` the spoken segment has no quantity (only a date, a name or a qualitative statement).
  - `human_role`: `SCALE` a person drawn to size something; `PRESENTER` a person at a board or desk; `NONE`.
  - `red_accent`: any red or crimson on the frame.

## 2. Results (counts, not percentages of anything larger)

| | Sample (24) | Holdout (23) | Combined (47) |
|---|---|---|---|
| Device: LABEL | 6 | 9 | **15** |
| MECH | 5 | 4 | 9 |
| MAP | 3 | 3 | 6 |
| AXIS | 4 | 1 | 5 |
| OBJ | 2 | 3 | 5 |
| SCALEREF | 1 | 3 | 4 |
| SBS | 2 | 0 | 2 |
| TALLY | 1 | 0 | 1 |
| Frames with a spoken quantity | 18 | 19 | 37 |
| ...restated YES | 9 | 9 | **18** |
| ...PARTIAL | 4 | 3 | 7 |
| ...NO | 3 | 6 | 9 |
| ...UNCLEAR | 2 | 1 | 3 |
| Human as SCALE / PRESENTER | 3 / 3 | 2 / 3 | 5 / 6 |
| Red accent present | 10 | 7 | 17 |

**Replication:** the headline held on the unseen holdout: the quantity is on screen in about half of the quantity moments (9 of 18, 9 of 19), and a direct numeral or unit label is the most common device in both sets. The holdout moved the device mix (SBS and TALLY did not recur; SCALEREF and LABEL did), so treat the minor categories as unstable.

## 3. What the frames show (OBSERVED, n small)

1. **The number is usually written on the drawing, not spoken alone.** Labels such as a speed arrow with its unit, a multiplier, a power or mass figure sit beside the object. A restated quantity often arrives as a numeral in a different form from the narration: miles drawn as a metre axis; "one sixteenth" gravity drawn as 0.61 m/s2 (9.81/16 = 0.613, consistent); a 40-degree change drawn on a Kelvin, Celsius and Fahrenheit line where it looks tiny.
2. **Comparison is carried by layout.** Side-by-side panels with numerals (1G against 6G; 130,000 lux against 1 lux), a scaled depth or time axis with the objects positioned on it (a falling-sphere race with times under each), and a number line with named landmarks.
3. **Size is given by a tiny drawn person** next to a large object (a building, a mountain range with a climber at the 8 km mark) or by a bracket labelled with a length. 5 of 47 frames use a person this way; 6 more use a person as a presenter at a board.
4. **When the number is huge or abstract, the frame often shows the context and not the number.** The 9 NO frames: 26 km, 500 terawatts, 12 billion footfalls, "thousands of degrees", 200 megawatts, a 50-year recurrence, 0.5 percent, billions of dollars, a single square metre. The number may be on screen a few seconds earlier or later (the ASR timing is uncertified), so NO means "not on screen at that instant", not "never shown".
5. **Red is a highlight colour:** it marks the key number, a flow or heat path, a route, or the object under study (17 of 47 frames); the rest is black line on white or grey. This is a style observation, not a rule.
6. **Mismatch seen once:** a frame labelled 15 lbs while the narration said "5 extra pounds beyond its own weight". Plausibly total against surplus; not reconciled. A fact-check is not in scope here.
7. **Format conventions:** attributed viewer question shown as a card with the asker's name; title cards that are a label only; equation cards (T = 2/3kB KE). These did not fit the scheme cleanly (see 4).

## 4. Limits (do not skip)

- **One coder.** No second reviewer; inter-coder agreement is unknown. All coding is self-review.
- **Selection bias by design.** Frames were drawn at quantity moments found by a regex over ASR text, so this says nothing about the rest of the runtime, and a regex misses written-out quantities.
- **Still frames only.** Whether a label appears with the word, before it or after it is not measured; animation (write-on) is invisible in a stills pass.
- **Frame-to-speech offset** is uncertain (campaign lead/lag column is `ASR_UNCERTIFIED`); midpoint sampling can miss a number shown a few seconds off.
- **Scheme gaps found in holdout:** no TITLE, EQUATION or SCENE class; 4 of 23 holdout frames were forced to the nearest class (noted in the coding CSV). A v2 scheme should add them.
- **Coverage:** 12 + 12 of 24 long videos with ledgers; 0 Shorts; 0 of the 44 long videos without ledgers. This is **TARGETED_VISUAL**, not DEEP_VISUAL.
- **No performance link:** nothing connects any device to retention or views.

## 5. Use for an original channel (descriptive, OWNER class)

- Treat "number on screen at the moment it is spoken, drawn in a different representation" as a **checklist item for a storyboard**, not a rule: for each quantity in a script, decide label, axis, side-by-side or scale reference, and decide deliberately when the number is *not* shown.
- Add a scale-reference figure only where a size is being claimed.
- Do not copy xkcd's drawings, layouts or jokes; the study is of mechanism.

## 6. Recompute

`python3 -I scripts/phase7_sample.py`, `scripts/phase7_holdout.py` (regenerates frames), then view `phase7_frames/sheet1-4.jpg` and `holdout7/sheet1-4.jpg` (frame order = row order in the two CSVs), `scripts/phase7_tally.py` for counts. The coding itself is manual; the CSVs hold it.
