# d5TD3r1nLqM: visual-only closure (contract v1; LOCAL ONLY)

## Source and evidence
- **Source:** sha re-computed = manifest (checks.json V1, 4d52a027…). 2045 frames. Every frame is measured and covered once (V2).
- **Reused:** the rv1 ledger (63 segments) and its measurements. rv1 had left 10 segments partly unviewed (343 frames).
- **New in closure_v1/:**
  - native frames;
  - holds_01..08.jpg, all 32 holds, viewed;
  - activity_grid.jpg, every frame of G0010 (201 f) and G0018 (110 f) at 1/8 scale, viewed;
  - strips of every frame of G0022, G0030, G0032, G0034, G0050, G0052, G0060 and G0062, viewed (stacked copies are in the session scratchpad);
  - crop_1572_1573.png;
  - a per-frame change series for every activity;
  - checks.json.
- **Disclosure:** the G0010 and G0018 grids are at 1/8 scale. Their content is low-detail drift and spiral growth, and the change curves are measured.
- **Parent:** not checked in this pass. This is dev-library evidence, not a held-out test.

## V4/V5 resolutions
| Seg | rv1 | Resolution |
|---|---|---|
| G0010 f307–507 | MEDIUM, 195 f unviewed | Hard cut at f307 to a stippled sky over the three travellers on a horizon. Over ~200 f the sky drifts right to left:<br>• the red-labelled star crosses the frame and exits (f307–405);<br>• a circled sun disc rises at the right and arcs across (f410–490);<br>• the star re-enters at the right (f483–506).<br>The travellers stay roughly in place. MEASURED change is steady at ~30k px/frame, i.e. a **constant-speed time-lapse drift**, not a camera move: the ground line is fixed and the hold shift is 0.19 px. Hard cut at f507 to the spiral map. |
| G0018 f744–853 | MEDIUM, 104 f unviewed | Hard cut at f744 to black space with a grey globe cap. A **red spiral grows** continuously around the travellers on the globe for ~108 f (steady ~2.7k px/frame). There is one spike at f781 (13.5k): a star twinkle or spiral-loop step, with no new object. Hard cut at f853 to the empty blackboard. |
| G0022 | — | Red zigzag scribble over the circle and the dashed line, written on in 5 f (f906–910). |
| G0030 | — | Red V path drawn from JERUSALEM to BETHLEHEM with an arrowhead, 4 f. |
| G0032 | MEDIUM | Hard cut at f1180 to a grey map close-up, then a red zigzag written on over 4 f. |
| G0034 | onset UNRESOLVED | **Hard cut at f1220** to the globe (648k px). The red route is then written on f1221–1230: down Africa, then horizontal loops at the south. **Resolved.** |
| G0050 | — | Red scribble over SUPERNOVA, 5 f. |
| G0052 | — | Red scribble over the comet head (f1624–1631). `WRONG TIME` is typed (f1632–1636), then `TOO FAST` (f1637–1641). The meteor scribble is drawn within the same run. |
| G0060 / G0062 | — | Second and third red dashed paths drawn on (13 f and 11 f). `DEC X` labels are typed at the end of each path (f1950–1953, f1978–1980). |

**Hold residue:** f1573 has 611 px with a largest component of 280 px but a max diff of only 22. The crop shows blocky low-amplitude change confined to the meteor's glow texture, with no visible drawn difference. I classify it as encoder residue on a textured glow, i.e. NOISE by viewing. There are no drawn changes inside holds.

## V6 creative (text read from native holds)
- **Text read:**
  - presenter frame: blank blackboard; travellers and arc; red arrow and dashed meander;
  - spiral map: `JERUSALEM`, `BETHLEHEM`, `DEAD SEA`, `To ANTARCTICA`, `WALKING/HALF A DAY`;
  - traveller captions: song-lyric quotes `AND I WOULD WALK 500 MILES` / `500 MORE`;
  - board diagram: sun, Earth, `SIRIUS`, struck through with red;
  - conditions board: `CONDITIONS:` / `IF: STAR IN SKY` / `IF: SUN HAS SET` / `THEN: WALK TOWARDS STAR`, with red `#CAN WALK ON WATER`;
  - planetarium logo text `PyEphem` (third-party software name) on a screen reading `YEAR: 2025` → rewind icon with streaks → `YEAR: 250` → rewind → `YEAR: ~4BC`, travellers shown on the screen;
  - night sky: `HALLEY'S COMET`, `SUPERNOVA`, `METEOR`, then red `WRONG TIME` / `TOO FAST`;
  - four scholars with date labels `112 BC!`, `4AD!`, `32AD`, `7BC`;
  - dashed routes with `DEC 25`, `DEC X`, `DEC X`.
- **Colour:** off-white canvas with black line art, used for most states.
  - **DARK_FIELD** night scenes use white line art plus grey GLOW plates: the comet tail and a supernova cross-flare.
  - The map and globe are flat grey (not MAP_FILL).
  - Red is used for marks only. There are no full-frame red frames and no photographs.
- **Continuity:** the traveller silhouettes are constant and invert to white on black. Placement of JERUSALEM/BETHLEHEM is constant across G0028–G0063.
- **INFERRED rv1 claims tested:**
  - "sky scroll" is confirmed as a content drift, not a camera move;
  - the G0034 "cut/zoom-out" is refuted as a zoom: it is a hard cut.
- **Originality flags:** the third-party software logo/name and the song-lyric captions must **never be reused**.

## V7
- `reconstruction_blueprint_v2.md`: per-state prompts, motion, continuity, QA and originality.
- **Format:** ORDINARY explainer Short with a presenter frame, a DARK_FIELD sequence and one long time-lapse drift.

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV are out of scope and remain unsigned.
