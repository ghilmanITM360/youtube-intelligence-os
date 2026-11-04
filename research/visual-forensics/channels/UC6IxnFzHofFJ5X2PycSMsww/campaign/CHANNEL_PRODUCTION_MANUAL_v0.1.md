# xkcd's What If? — observable production system, manual v0.1 (development evidence only)

Status: DRAFT v0.1, 2026-11-04. Built from development-set videos reviewed so far (long: 2LSyizrk8-0, EsUBRd1O2dU, 8fADp43wJwU, FkUNHhVbQ1Q, -1-ldW4kpLM, YL2VNtus4xk; Shorts: wBLVmEZV2Oc, _efsqO-4OoQ, sFTRRdHqZIQ, kNry0bf7eC0, 5k8ciEx__5w, i6e4NnFnQi0, Uj10jGq2O8o, aMshLs0YCTQ, 2p305nzcVQE, d5TD3r1nLqM, oLoxdLfB6Gs). Held-out videos (JcXpCyPc2Xw, BnGqPxnQh9A, Ny9m2l6h478, jVy3qd70AqU, rGZ6TsXvi8E) were NOT used. Every rule cites `video_id seg/PTS`; per-segment evidence lives in `videos/<id>/tables/state_ledger.csv`. Labels: MEASURED (tool), OBSERVED (seen in tiles by reviewer and/or primary), INFERRED (interpretation). Audio rules are ASR-only (no listening). This manual describes the creator's output for study; it does not license their characters, artwork, scripts, voice or branding. Section 9 converts it into an ORIGINAL production spec.

## 1. Format facts (MEASURED, campaign/aggregate_interim1.csv)
- All sources 24 fps CFR; long-form 1920x1080, Shorts 1080x1920. Loudness integrated −16.2…−16.8 LUFS across 10 measured sources (levels only).
- Long-form (n=4 at aggregation): 20.4–22.2 visual events/min; 4.9–6.1 hard cuts/min; median hold 2.15–2.33 s.
- Shorts (n=9): 17.9–28.2 events/min; 3.6–8.7 cuts/min; median hold 1.44–2.84 s.
- Change is concentrated in single-frame swaps: most ACTIVITY segments are 1 frame (pop-on, state swap or cut); multi-frame events are write-ons (≈5–12 frames), dissolves/fades (≈6 frames), pans/slides (≈7–10 frames) and rare long continuous moves (scroll 140 frames wBLVmEZV2Oc G0060; sky rotation inside YL2VNtus4xk G0010).
- 38 of 40 caption-available Shorts reuse ≥90 % of their narration from one long video (campaign/short_long_text_reuse_population.csv). Primary visual comparison of pairs (2p305nzcVQE↔FkUNHhVbQ1Q; d5TD3r1nLqM↔YL2VNtus4xk; i6e4NnFnQi0↔2LSyizrk8-0) shows the same drawings recomposed for 9:16, not new art. Standalone Shorts: oLoxdLfB6Gs, SLd4hnmeW_g.

## 2. Canvas, palette, line and type
- Default canvas is flat off-white `#F7F7F7` (MEASURED, wBLVmEZV2Oc frame 0) with black hand-drawn line art; mean settled ink coverage ≈3 % of pixels in diagram scenes (MEASURED wBLVmEZV2Oc). Light grey fills (bin #D0D0D0) for globes/water/land.
- Counterexamples (OBSERVED, common, so they are part of the system): inverted black space scenes with white line art (sFTRRdHqZIQ throughout; EsUBRd1O2dU SHEET_12; 2LSyizrk8-0 G0016–G0025); grey night scenes with soft radial light cones, rain overlay and vignettes (kNry0bf7eC0 G0011–G0017; 8fADp43wJwU G0132–G0134); flat colour fields — beige Mars with blue water (FkUNHhVbQ1Q G0072–G0080), blue sky gradient + yellow sun (oLoxdLfB6Gs G0004); photographic or photo-like inserts (2LSyizrk8-0 G0036, G0050; i6e4NnFnQi0; Uj10jGq2O8o G0066–G0073).
- Red is the accent: correction strikes, circles, hatching, paths, rays, highlighted quantities (wBLVmEZV2Oc G0002/G0010/G0024; -1-ldW4kpLM G0130 '+5 DAYS'; d5TD3r1nLqM red coil path; i6e4NnFnQi0 red wedge). Full-frame red is used for the series title and end cards in long-form (2LSyizrk8-0 G0010; FkUNHhVbQ1Q G0010/G0182; EsUBRd1O2dU G0194). Counterexample: no red at all in sFTRRdHqZIQ and kNry0bf7eC0.
- Lettering: hand-lettered all-caps labels and headings; question boxes and footnotes use a small serif typeset face (2LSyizrk8-0 G0002 'Q. If the Hubble…'; wBLVmEZV2Oc G0018 footnote). Exact fonts UNAVAILABLE.
- Characters: stick figures — circle head, single-line body/limbs, no facial features by default; identity via hair/hat/props (bob hair 5k8ciEx__5w G0004; ponytail operator 2LSyizrk8-0 G0012; helmet sFTRRdHqZIQ G0016; wise-men robes/crowns d5TD3r1nLqM G0014). Objects and machines are drawn with much higher detail than figures (seismograph wBLVmEZV2Oc G0001; submarine cutaway EsUBRd1O2dU G0114; Hubble 2LSyizrk8-0 G0006).

## 3. Opening grammar (how the absurd question is introduced and bounded)
- Long-form opens on a "lecture" frame: stick figure holding a paper beside an empty framed board; the reader's question appears in a grey rounded box typed on letter-by-letter with attribution, before the narrator finishes reading it (2LSyizrk8-0 G0002–G0004 text 0.42–1.46 s vs ASR 3.06–6.42 s; FkUNHhVbQ1Q G0001 'Q…—Iain'). The board then receives the subject object as a pop-on (2LSyizrk8-0 G0006 Hubble at 2.79 s). A red series title card follows within ~6–10 s (2LSyizrk8-0 G0010 at 6.38 s).
- Shorts drop the title card and usually the typed question; they open directly on the subject drawing or lecture board (wBLVmEZV2Oc G0001; 5k8ciEx__5w G0001; aMshLs0YCTQ G0001; d5TD3r1nLqM G0001). Some open on an object only, no character, no text (kNry0bf7eC0 G0001).
- Bounding device: the question is restated as one concrete visual with a scale or limit marker — a ruler running off frame (wBLVmEZV2Oc G0018), a dashed algorithm limit line (i6e4NnFnQi0 G0016), a rope around a globe (5k8ciEx__5w G0002).

## 4. Reasoning → visual steps (escalation)
- Dominant pattern: hard cut to a new canvas per reasoning step, often with a typed step heading ('1) RESOLUTION', '2) MOTION' 2LSyizrk8-0 G0040/G0064). A single persistent diagram is the minority case (wBLVmEZV2Oc ruler G0012–G0057), so "one diagram per video" is NOT a channel rule.
- Persistent anchors carry a quantity across cuts: magnitude ruler + arrow (wBLVmEZV2Oc), black top banner 'T = 1 YEAR'/'T = 5 YEARS' (-1-ldW4kpLM G0125–G0134), elapsed-time labels 'T = 30 NANOSECONDS' (Uj10jGq2O8o G0030), depth label on a world-map band '0 m'→'DRAINED' (aMshLs0YCTQ G0030–G0072), 'PART 1/PART 2' sub-labels (sFTRRdHqZIQ G0010/G0034).
- Escalation by state swap of the same drawing: damage/fracture swaps (wBLVmEZV2Oc G0046, G0062), grime and corrosion swaps (kNry0bf7eC0 G0004–G0006), freezing swap (2p305nzcVQE G0050), dam speckle damage (8fADp43wJwU G0130).
- Comparison layouts: split screens and triptychs (FkUNHhVbQ1Q G0080; 2LSyizrk8-0 G0110 EXPECTATION/REALITY), equation-panel jokes ('PROBLEM + PROBLEM = BIGGER PROBLEM' 2LSyizrk8-0 G0070–G0072).
- Intra-state change exists inside measured holds: slow drift (water level) in aMshLs0YCTQ G0027 (D4 flag) — long holds are not automatically static.

## 5. Labels, numbers, diagrams
- Labels arrive with or just after the object they label, as single-frame pops (wBLVmEZV2Oc G0038 '3500 Km' after G0036 fault block; FkUNHhVbQ1Q G0076 map labels). Exception: number typed first, arrow second (2LSyizrk8-0 G0056 '535 km').
- Numbers on screen equal narrated numbers in the reviewed cases (wBLVmEZV2Oc 9.0–9.1/9.1–9.3/3500 km/10^32 J vs ASR). Formula build-ups are written on in steps (5k8ciEx__5w G0012–G0018 'C = 2πr' → '~6.28' in red; sFTRRdHqZIQ G0012).
- Time-passing is labelled, often by cross-fading labels ('OOPS!' → '~4 YEARS' 8fADp43wJwU G0128–G0130).

## 6. Reveal and motion vocabulary (measured frame counts)
| Device | Typical duration | Used for | Evidence |
|---|---|---|---|
| Pop-on (1 frame) | 1 frame | objects, labels, annotations, figures, jokes | most ACTIVITY rows in every ledger |
| Write-on type | 5–12 frames | question boxes, headings, titles, formulas | 2LSyizrk8-0 G0002; wBLVmEZV2Oc G0004 (9 f) |
| Write-on stroke | 7–9 frames | red strikes, hatching, paths | wBLVmEZV2Oc G0002 (9 f), G0024 (7 f) |
| Cross-dissolve/fade | ≈6 frames | zoom-out reveal, time passing, flood, fade to dark | wBLVmEZV2Oc G0018; 8fADp43wJwU G0134; 2p305nzcVQE G0054 |
| Slide/pan with motion blur | 7–10 frames | entering a new panel, re-laying out | i6e4NnFnQi0 G0018; 2LSyizrk8-0 G0110; FkUNHhVbQ1Q G0080 |
| Scroll of an anchor | 8–140 frames | advancing a scale | wBLVmEZV2Oc G0034/G0060 |
| State swap | 1 frame | damage, pose, clothing, lighting | EsUBRd1O2dU G0112 beanie removed; kNry0bf7eC0 G0016 |
Easing/interpolation curves are UNAVAILABLE (sampled tiles only).

## 7. Humour and narration relations (ASR_UNCERTIFIED timing)
- Deadpan stick-figure asides with literal speech: 'PHEW!' (wBLVmEZV2Oc G0050), 'YUP, THE EARTH IS DEFINITELY EXPANDING' (-1-ldW4kpLM G0128), 'THIS IS THE HOTTEST PLACE I'VE EVER GOTTEN FROSTBITE' (sFTRRdHqZIQ G0016), 'WAS THIS TAKEN OUT OF A MOVING CAR?' (2LSyizrk8-0 G0074).
- Visual literalisation of a phrase at the moment it is spoken: chair rolling (2LSyizrk8-0 G0134 vs ASR 178.5 s), capsule wearing a beanie (EsUBRd1O2dU G0110), 'TO DO: ADD DRAINS / ADD WHALE FILTER' (aMshLs0YCTQ G0028).
- Pop-culture and pedantry gags (Death-Star-like sphere wBLVmEZV2Oc G0058; 'UHM, ACTUALLY…' G0008; song-lyric wise men d5TD3r1nLqM G0014); REDACTED bars (EsUBRd1O2dU G0118; 2LSyizrk8-0 G0136).
- Callbacks: long-form returns to the opening board and red end card (EsUBRd1O2dU G0140/G0190/G0194).

## 8. Shorts vs long-form
- Shorts: no series title card, no end card observed, narration excerpted from a long video, same drawings re-laid out vertically (stacked panels, crops, re-composed rivers/maps), equal or higher event density. INFERRED: the Short starts at the excerpt's own visual premise rather than the long video's reader-question frame.

## 9. Original-production specification (transfer, not copy)
Use the mechanics above with a NEW visual identity: different character design (e.g., a rounded pebble-shaped narrator with dot eyes, not a stick figure), different accent colour (e.g., teal `#1F8A8A` instead of red), different lettering (a rounded monoline sans), original topics and scripts.
1. Script → beat list: question, bound, 3–6 escalation steps, deadpan aside per 20–40 s, payoff.
2. For each beat define: canvas (light/dark/colour field), persistent anchor (scale, timer banner, map band), one new object, ≤1 label, ≤1 accent mark.
3. Timing defaults (from measured source ranges, to be validated by test): hold 1.5–2.5 s median; pops on the narration word that names the element; write-ons 6–10 frames at 24 fps; dissolves 6 frames; panel slides 8 frames.
4. Shorts: cut the long script into 45–120 s excerpts and re-lay each beat for 9:16 (stack panels vertically, keep the anchor on screen).
5. Image prompt template: "<aspect>, <canvas>, hand-drawn monoline ink illustration in <original style>, subject: <object> at <position>, persistent anchor: <anchor>, label '<text>' near <object>, accent colour only on <mark>, generous empty space, no shading unless lighting scene, no extra text".
6. Animation prompt template: "<object> appears in one frame at t=<word onset>; everything else static; <write-on> strokes left-to-right over 8 frames; camera locked except <slide/scroll> over 8 frames with slight motion blur".

## 10. Open questions / to verify
- Sound design, music, delivery: UNAVAILABLE (no listening).
- Long activities sampled with ≤6 tiles leave internal cut times unresolved (e.g., YL2VNtus4xk G0010; 2LSyizrk8-0 G0022): dense-strip pass needed.
- Era change: early (2023–24) vs recent (2026) long-form not yet compared (BO8rOs05v48, 9VG0yqq_PHM, lLlwvmu1ZeA, WH4g1ptJ-70 pending).
