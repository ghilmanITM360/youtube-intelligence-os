# PRODUCTION ASSET AND EDITING PLAN — original production using the learned system

All numbers are MEASURED counts from this source's review tables (VISUAL_STATES.csv etc.); the plan is for an ORIGINAL production, ~15 minutes, 24 fps CFR, 1280×720 (or 1920×1080 with the same ratios).

## A. Asset inventory (categories and approximate quantities needed)
| Category | Source evidence (states mentioning) | Original asset target |
|---|---|---|
| Presenter body/head parts | presenter ≈186 mentions, 8 variants | 1 lead + 2 foils; 8 heads × 6 poses × 2 prop variants, SVG/PNG layers |
| House/building doodles | house ≈135, building ≈42, mansion 17 | 3 house styles, 2 tower styles, 1 mansion, 1 chain/ice modifier |
| Money/labels | dollar ≈42 | bills, coins, price tag, % badge |
| Documents/icons | DEBT/TAX papers, newspaper 14, laptop 17 | 6 labelled document icons, newspaper, laptop frame |
| Capture frames (you author) | F4 47 + F5 144 + F8 15 states | 12–20 authored article/transcript/table mock-ups with fictional text, plus dark-mode variant |
| Charts | F6 20 states, chart ≈81 mentions | 6 authored line/bar charts + stroke-overlay assets |
| Draw-on strokes | 42 sub-threshold + ≥91 highlight mentions | highlight, underline, box, curve strokes in red/yellow/blue/purple with write-on masks |
| Handwritten numbers/text | handwritten red numerals | one marker font + 20 prerendered number reveals (glyph-by-glyph) |
| Text/title/end cards | F7 4, F10 7 | title card, 3 text cards, end card (CTA layout) |
| Sponsor/CTA block | 440–518 s | only if you have a real sponsor: your own QR/offer layout and progress bar |
| Cursor | 20+ micro-events | arrow cursor sprite |

## B. Editing timeline model
1. Build the A/V script, mark sentence starts (use forced alignment on your own recording, not copied timing).
2. Place a "scene card" at each sentence start where the idea changes (large replace); within sentences, add additive beats at phrase points.
3. Per hour of runtime expect ~1,450 state changes (24/min), ~530 of them motion transitions per hour (136 in 15.3 min ≈ 8.9/min) — budget animation time accordingly.
4. Provide a 3-tier edit list: T1 hard cuts (≈73%), T2 motion transitions (scroll/zoom/object, ≈27%), T3 micro-beats (draw-on/highlight/cursor, ≈14 per minute measured).

## C. Per-minute budget (derived from this source; adjust to your script)
- State changes 24 ±8/min; motion intervals 11/min (169/15.3 min); intra-state micro-events 14/min.
- Doodle states (F1+F2+F3) = 319 s of 921 s ≈ 35% (MEASURED sum of state durations); capture-bearing states (F4+F5+F6+F8) ≈ 449 s ≈ 49%; cards/scenes ≈ 37 s ≈ 4%.

## D. Quality-control checklist
1. Frame ledger: export your timeline's change frames and compare against the plan (every planned event present, no extras).
2. Run the same measurement pass (frame diffs ≥ 30 px at contrast ≥ 150) on the export; list unplanned changes.
3. Legibility: every must-read text ≥ 3% frame height, contrast ≥ 4.5:1 against its background.
4. Continuity: same hex for canvas/ink; recurring props byte-identical.
5. Rights: all captures authored; fonts licensed; no source characters or text.
6. Audio sign-off: a human listens to the final mix end-to-end (separate gate).

## E. Suggested 8-step implementation sequence
Character/prop kit → capture mock-up kit → stroke/write-on kit → master timeline template (24 fps, layer order from the blueprint) → rough cut with hard cuts → motion pass (scroll/zoom) → micro-beat pass → QC diff + legibility + rights pass.
