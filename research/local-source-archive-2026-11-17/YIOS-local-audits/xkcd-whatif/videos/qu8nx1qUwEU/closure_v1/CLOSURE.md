# qu8nx1qUwEU: visual-only closure (contract v1; LOCAL ONLY) — first LONG closure

## Evidence base
- **Source:** sha re-computed = manifest (checks.json V1, 4aa23ce0…), 4084 frames (170.2 s, CFR 24). Every frame measured and covered once (V2).
- **Reused:** rv1 ledger (129 segments: 65 holds, 64 activities), shot_ledger (16 shots), measurements. rv1 left 5 segments unviewed (55 frames): G0002, G0004, G0010, G0094, G0126.
- **New in closure_v1/ (all viewed by me this pass, 2026-11-09):**
  - holds_01..17.jpg — all 65 holds at 1/2 scale (settled end frame);
  - strip_G0002, G0004, G0010_01..05, G0022, G0052, G0054, G0076, G0094, G0126 — every frame start-1..end+1, native crops (scale ≤1);
  - cuts_01..02.jpg — before/after of all 15 shot cuts at 1/4 scale;
  - residue_crops_01..03.png — every non-noise hold residue frame pair at native scale plus ×6 diff;
  - extra_checks.json (all 41 hold residue frames classified), palette_closure.json, activity_curves.csv, checks.json.

## V3 cuts
All 15 shot_ledger cuts (f349, 448, 648, 1073, 1524, 1749, 1818, 2581, 2753, 2942, 3295, 3341, 3468, 3701, 3844) viewed before/after: hard cuts, no transition frames.
**Correction (not an rv1 edit):** an additional hard cut at **f396|f397** (title card → space scene VS006) lies inside rv1 activity G0010 / shot SH002, so SH002 is really two shots (title card f349–396, space f397–447). Viewed in strip_G0010_05.

## V4/V5 resolutions
| Seg | rv1 | Resolution (native view) |
|---|---|---|
| G0002 f53–58 | 3/6 viewed | 6-f cross-fade: background greys, SUN + rays and UN-SUN-SPECTING EARTH + arrow + globe fade in; head shading appears. Curve flat ~16k px/frame (linear fade). |
| G0004 f96–101 | 3/6 viewed | 6-f cross-fade: looped field lines and beam fade in; label cross-dissolves UN-SUN-SPECTING → UNINHABITABLE. ~7.6–8.1k px/frame. |
| G0010 f349–397 | 6/49 viewed | Hard cut to the red series title card (f349); type static; only the mascot animates (head/jaw loop, debris specks) f350–396 at 1–14k px/frame; hard cut f397 to VS006. All 49 frames viewed. |
| G0022 f667 | MEDIUM | 1-frame pop of `~1.5·10^22 J/day` (next frame 0). |
| G0052 f1643 | LOW "Earth re-positioned higher" | **Refuted.** Change bbox is only the label (1280–1423 × 144–259): 1-frame pop of red `NOT` above SAFE and a red scribble over `?`. Earth unchanged (hold sheets VS026/VS027 identical framing). |
| G0054 f1674 | LOW "UNRESOLVED glyphs" | **Resolved:** 1-frame pop of three tiny white outline tombstones stacked on Earth's right limb. |
| G0076 f2431 | MEDIUM "Earth smaller/shifted" | **Refuted:** f2430→f2432 phase-correlation shift 0.003 px; only the ring tips and their sparks redraw. |
| G0094 f2912–2917 | 3/6 viewed | 6-f fade-out of ~25 white wavy arrows; moon, glow wall and figure unchanged (~19–20k px/frame). |
| G0126 f3750–3755 | 3/6 viewed, "FADE_IN+ZOOM_IN" | **Zoom refuted:** tombstone edge x at row 800 = 602/1362 in f3751, f3753 and f3756 (no scale change). 6-f opacity fade-in; red Earth greys under the stone. |

All other 59 activities are 1-frame events, each seen in its before/after natives and rv1 tile view (rv1 frames_viewed = frames). Hold stillness: 41 hold frames >50 px; 20 NOISE by component size, 21 viewed in residue crops:
- **f2283–f2288 (inside VS036/G0071): sub-threshold tint fade** of the outward arrows red → grey (components 105–1450 px, max diff ≤69). Matches rv1 G0070 note "arrows start turning grey". Recorded as a hold sub-event (COLOR_FADE), not a ledger miss.
- f0/1/3, f90, f960 (scribble edges), f1774, f1830, f2081, f2670, f3136, f3390/3391, f3630/3631, f3764, f3990: edge/grain/glow shimmer, no visible drawn change in crops → NOISE by viewing.

## V6 creative (text read from native/half-scale holds)
- **Text:** `Q. What if all of the sun's output of visible light were bundled up into a laser-like beam that had a diameter of around one meter once it reached Earth?` `— Max Schäfer`; `SUN`, `UN-SUN-SPECTING EARTH` → `UNINHABITABLE EARTH`, `1m` (white, later red); `DNA`, `FATTY ACIDS`, `BLOOD`, `MITOSIS`, `CELLULOSE`; scattered letters; particle symbols (`e`, `γ`, `ν`, `W⁻`, `Z⁰`, `μ⁺`); `~1.5·10^22 J/day`, `~3.8·10^26 J/second`; top note (VS013, see blueprint); red `~2,000,000,000x`; `MILLIONS OF DEGREES (FAHRENHEIT, CELSIUS, RANKINE, OR KELVIN – IT DOESN'T REALLY MATTER)`; `PLASMA`, `X-RAYS`, `MORE PLASMA`, `IR`; `RIP`, `SAFE?` → red `NOT` + scribbled `?`; tombstones `RIP / CAUSE OF DEATH: TWILIGHT`, `… MOONLIGHT`, broken `TWILI…`, `MOO…IGHT`; `TWILIGHT`; `?`; red `↑ ? ↑`; `RIP` / `WE SHOULDN'T HAVE TURNED THE SUN INTO A LASER`; series title card and end-card credits (source branding: not transferable).
- **Palette (palette_closure.json):** near-black space canvas, greys, white line art and glows; red/pink glow family for heat; purple→pink dusk gradient (VS029/030); red-washed VS057 (debris) and red title/end cards. White whiteboard scenes at open and VS058/059. No photographs.
- **Continuity checked across consecutive holds** (sheets): objects persist and upgrade in place; camera static (hold-to-hold shift max 1.03 px).
- **INFERRED claims tested:** G0052 re-position (refuted), G0076 shrink/shift (refuted), G0126 zoom (refuted), G0054 unresolved (resolved).
- **Originality:** series title card, mascot silhouette, end card, book covers and credit names are source branding — replace entirely in transfer.

## V7
`reconstruction_blueprint_v2.md`: per-state prompts (65), motion/timing per event, continuity, QA, originality.

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV out of scope, unsigned. Reviewer: single model, no human second review.
