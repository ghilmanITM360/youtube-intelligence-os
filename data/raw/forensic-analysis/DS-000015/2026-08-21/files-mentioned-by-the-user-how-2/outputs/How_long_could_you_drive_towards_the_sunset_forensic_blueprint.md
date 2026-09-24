# “How long could you drive towards the sunset?” — forensic reconstruction blueprint

**Source:** `How long could you drive towards the sunset_.mp4`  
**Analysis date:** 2026-08-21  
**Method:** direct source-file inspection; 3,119 decoded source frames sampled at the native 24 fps cadence; 34 full-resolution keyframes; local Whisper transcription with word/segment timing; Apple Vision OCR; 50 ms audio-envelope and spectrogram analysis.  
**Timing convention:** frame-verified transitions are shown to the nearest decoded source frame. State boundaries inside continuous animation are approximate where the change is gradual.  
**Confidence language:** “High” means directly visible/measured; “Medium” means strongly inferred from adjacent frames or audio; “Low/Speculative” is used where the original production method or intent cannot be verified.

## Executive finding

The video is engineered as a compact causal explainer: define the exact problem, eliminate seductive loopholes, introduce the correct moving-boundary model, demonstrate the route, reveal a measured answer, then return to the opening sunset image for a human joke. Its repeatable production grammar is:

> Establish a stable coordinate frame, introduce one information-bearing variable, animate only that variable, label the consequence, hold long enough to understand it, and cut only when the coordinate system or argumentative job changes.

The visible system is mostly deterministic hand-drawn motion graphics—not generative video. White fields, black outlines, gray context, yellow suns, and scarce red/green accents make the information hierarchy self-explanatory. The richly colored sunset appears only as a pattern interrupt and emotional callback.

---

# Pass 0 — media inspection

| Property | Measured value | Confidence |
|---|---:|---|
| Duration | 129.932653 s | High |
| Display size | 720 × 1280 px | High |
| Aspect/orientation | 9:16 vertical | High |
| Frame rate | 24.000 fps | High |
| Video codec | H.264 / `avc1` | High |
| Video color metadata | Rec. 709 primaries/transfer/matrix | High |
| Video bitrate | ~156 kb/s | High |
| Audio | Present, AAC stereo, 44.1 kHz | High |
| Audio bitrate | ~128 kb/s | High |
| Speech | English narration, 44 recognized segments | High, with two context-corrected tokens |

### Audio evidence

- Overall RMS: **−19.14 dBFS**; absolute peak: **0.795** (about −2.0 dBFS).
- Mid RMS: **−19.14 dBFS**; side RMS: **−35.39 dBFS**. The mix is strongly center-dominant, consistent with narration.
- The spectrogram is speech-dominant: voiced harmonic bands and consonant transients recur throughout. No separate music or SFX layer can be verified from the mixed track. Treat “narration only” as **Medium confidence**, not a stem-level fact.
- Only one measured low-level interval longer than 150 ms crossed −42 dBFS: **02:08.15–02:09.89**, the ending fade/hold.
- Most large energy rises align with new spoken clauses. Correlation with a visual cut is common but not universal; no claim is made that every edit was audio-triggered.

### Transcript corrections

The local recognizer produced “ideal ice horizon” and “PIFM code.” Context and the visible `PyEphem` label support **“idealized horizon”** and **“PyEphem code.”** Those two corrections are used below. All other quoted wording follows the recognized narration.

---

# Passes 1–4 — shots, states, and persistent assets

## Shot/edit decision list

| Shot | In | Out | Dur. | States | Visual type | Entry / exit | Cut motivation | Motion hero | Static anchor |
|---|---:|---:|---:|---:|---|---|---|---|---|
| S01 | 00:00.000 | 00:05.833 | 5.833 | 1 | Whiteboard presenter | Start / hard cut | Hook → formal definition | None; narration carries | Board and figure |
| S02 | 00:05.833 | 00:11.792 | 5.958 | 2 | Horizon rule diagram | Hard cut / hard cut | Define valid sunset interval | Repeated sun positions | Horizontal horizon |
| S03 | 00:11.792 | 00:13.833 | 2.042 | 1 | Painterly sunset | Hard cut / hard cut | Visual contradiction/pattern break | Text reveal only | Landscape |
| S04 | 00:13.833 | 00:15.708 | 1.875 | 1 | White invalid-sunset diagram | Hard cut / replacement | Comic exclusion | Yellow/gray discs | Horizon |
| S05 | 00:15.708 | 00:17.750 | 2.042 | 2 | Square → doorway gag | Replacement/morph / cut | Escalate absurd exclusions | Door opening | White canvas/horizon |
| S06 | 00:17.750 | 00:21.083 | 3.333 | 1 | “Bru-WAAK” sun gag | Hard cut / replacement | Close loophole humorously | Disc chain/cracking | Horizon |
| S07 | 00:21.083 | 00:25.417 | 4.333 | 1 | Touch-then-rise diagram | Replacement / replacement | State disqualification rule | Sun trajectory | Horizon |
| S08 | 00:25.417 | 00:31.417 | 6.000 | 1 | Hill vs ideal horizon | Replacement / hard cut | Clarify obstruction rule | Sun path | Mountains/horizon |
| S09 | 00:31.417 | 00:42.917 | 11.500 | 2 | Dark globe/airliner diagram | Hard cut / hard cut | Establish rotation loophole and fuel caveat | Arrows and airplane | Globe |
| S10 | 00:42.917 | 00:49.875 | 6.958 | 1 | Polar wireframe globe | Hard cut / hard cut | Explain why poles help | Aircraft/poleward paths | Wire globe |
| S11 | 00:49.875 | 00:53.292 | 3.417 | 1 | North Pole twilight | Hard cut / animated location replacement | Eliminate unroaded poles | None | Horizon and title |
| S12 | 00:53.292 | 01:08.417 | 15.125 | 3 | Longyearbyen benchmark | Text/location replacement / hard cut | Set 55-min benchmark, reject westward driving | Car, map inset, numeric labels | Polar horizon |
| S13 | 01:08.417 | 01:14.292 | 5.875 | 1 | Presenter + symmetric sun path | Hard cut / hard cut | “Better approach” reset | Sun sequence | Horizon/presenter |
| S14 | 01:14.292 | 01:35.583 | 21.292 | 5 | Scandinavia terminator strategy | Hard cut / hard cut | Explain the winning route | Boundary, car, inset sun | Map |
| S15 | 01:35.583 | 01:44.500 | 8.917 | 3 | Research/computation proof | Hard cut / hard cut | Earn result with method/evidence | Callout, map, Arctic line | Researcher/desk |
| S16 | 01:44.500 | 01:51.500 | 7.000 | 2 | Route/result comparison top panel | Hard cut / additive reveal | Reveal 95-minute result | Arrow/bracket/text | Map strip |
| S17 | 01:51.500 | 01:53.458 | 1.958 | 1 | 95 vs 55 split comparison | Additive reveal / hard cut | Quantify payoff delta | Lower panel reveal | Upper 95-min panel |
| S18 | 01:53.458 | 02:09.933 | 16.474 | 5 | Painterly callback and joke | Hard cut / end hold | Emotional callback + humor coda | Spinning figure/text | Sunset landscape |

**Measured shot statistics:** 18 major shots; average 7.218 s; median 5.917 s; shortest S04 at 1.875 s; longest S14 at 21.292 s. The apparent slowness of S14 is offset by continuous map reframing, car motion, terminator motion, labels, and an inset sun sequence.

## Visual-state index

| Visual | Time | Shot | Narrative/visual function |
|---|---|---|---|
| V01 | 00:00.000–00:05.833 | S01 | Hook: presenter, Earth, sun, road/vehicle question |
| V02 | 00:05.833–00:08.000 | S02 | Define sunset start; single yellow sun and invalid marker |
| V03 | 00:08.000–00:11.792 | S02 | Complete valid interval and end condition |
| V04 | 00:11.792–00:13.833 | S03 | Painterly “NOT A SUNSET” contradiction |
| V05 | 00:13.833–00:15.708 | S04 | First diagrammatic non-sunset gag |
| V06 | 00:15.708–00:16.458 | S05 | Yellow square absurd example |
| V07 | 00:16.458–00:17.750 | S05 | Square opens to a person in a doorway; still invalid |
| V08 | 00:17.750–00:21.083 | S06 | Sun evolves/cracks; “no matter what happens” gag |
| V09 | 00:21.083–00:25.417 | S07 | Touching horizon then rising disqualifies sunset |
| V10 | 00:25.417–00:31.417 | S08 | Nearby hill is invalid; idealized horizon is required |
| V11 | 00:31.417–00:35.800 | S09 | Earth rotation and London-latitude speed |
| V12 | 00:35.800–00:42.917 | S09 | Westbound airliner can prolong sunset until fuel ends |
| V13 | 00:42.917–00:49.875 | S10 | Poleward latitude reduces required chasing speed |
| V14 | 00:49.875–00:53.292 | S11 | North Pole has no qualifying paved road |
| V15 | 00:53.292–00:59.750 | S12 | Longyearbyen qualifies; benchmark just under an hour |
| V16 | 00:59.750–01:02.875 | S12 | Westward driving strategy introduced and rejected |
| V17 | 01:02.875–01:08.417 | S12 | Norway inset and `355 mph` proof |
| V18 | 01:08.417–01:14.292 | S13 | Pattern reset: there is a better approach |
| V19 | 01:14.292–01:20.125 | S14 | Day-night line moves NW, slows, reverses SW |
| V20 | 01:20.125–01:22.125 | S14 | Strategy coordinate frame: map, boundary, car |
| V21 | 01:22.125–01:26.875 | S14 | Wait until first horizon contact |
| V22 | 01:26.875–01:32.000 | S14 | Drive north just ahead of the terminator |
| V23 | 01:32.000–01:35.583 | S14 | Turn south across the line into night |
| V24 | 01:35.583–01:38.875 | S15 | Researcher and PyEphem method |
| V25 | 01:38.875–01:43.000 | S15 | Norway map added as search domain |
| V26 | 01:43.000–01:44.500 | S15 | Arctic Circle dashed line/label completes proof scope |
| V27 | 01:44.500–01:48.708 | S16 | Car/sun route over Scandinavia |
| V28 | 01:48.708–01:51.500 | S16 | `~95 min` bracket reveals result |
| V29 | 01:51.500–01:53.458 | S17 | Split `~95 min` vs `~55 min` comparison |
| V30 | 01:53.458–01:58.083 | S18 | Painterly sunset callback |
| V31 | 01:58.083–02:01.167 | S18 | Figure spins counterclockwise |
| V32 | 02:01.167–02:02.917 | S18 | `WHAT ARE YOU DOING?` appears |
| V33 | 02:02.917–02:05.083 | S18 | `LENGTHENING THE SUNSET / PUSHING BACK THE NIGHT` |
| V34 | 02:05.083–02:09.933 | S18 | `GIVING ME A LITTLE MORE TIME / HERE WITH YOU.`; audio fades |

## Persistent asset manifest

### Characters

- **C01 — anonymous explainer/researcher:** thin irregular black stick limbs, unfilled oval head, no facial features; pose changes by scene. High continuity in line weight; identity is generic rather than portrait-specific.
- **C02 — black-haired sunset companion:** small stick figure with black filled hair/head mass, positioned left in the painterly sunset.
- **C03 — gray-headed spinner:** small stick figure with a flat gray circular head, positioned right in the painterly sunset; later surrounded by white elliptical spin trails.
- **C04 — doorway figure:** small black-haired/capped stick bust inside a yellow open door. Treat as a gag-specific figure, not necessarily C01.

### Environments

- **E01 — white diagram field:** pure/near-white 9:16 canvas, irregular black horizon around y≈50%, abundant negative space.
- **E02 — painterly sunset:** deep indigo sky, dense horizontal red/orange/yellow strokes, white-yellow sun at the horizon, nearly black olive foreground.
- **E03 — dark globe field:** charcoal gradient background with intense white light clipping at a side edge; centered gray Earth.
- **E04 — polar twilight:** navy/purple sky, orange-white sun at left horizon, black mountainous silhouette, minimal white stars.
- **E05 — Scandinavia map:** light gray land, darker gray water/night region, thin roads/coastlines, curved day/sunset/night bands.
- **E06 — research canvas:** white field, seated stick researcher, chair/desk/laptop, framed gray Scandinavia map.

### Objects and graphics

- **O01 yellow sun disc:** flat saturated yellow fill, irregular black outline; primary moving variable.
- **O02 gray sun disc:** flat medium/dark gray below-horizon state; exact size follows O01.
- **O03 Earth/globe:** gray continents/oceans, hand-drawn black edge/grid; orientation changes when argument changes.
- **O04 vehicle family:** rough truck at the North Pole; gray hatchback in Longyearbyen; small white/black car icon on maps. This is intentional functional variation, not one exact model.
- **O05 aircraft icons:** tiny black/gray commercial jets following red/orange latitude paths.
- **O06 seals:** two outlined gray seals in the North Pole foreground.
- **O07 mountains/hill:** thin black mountain contour used as obstruction.
- **O08 research desk set:** black-outline chair, desk, laptop, satellite-dish-like PyEphem callout.
- **O09 Longyearbyen church:** black-outline white church used only in the comparison panel.
- **G01 verdict marks:** red X for invalid, single green check for valid.
- **G02 motion grammar:** black arrows for object direction; red arrows/lines for terminator, danger, direction, or emphasized geometry.
- **G03 sunset-sequence inset:** boxed mini-diagram of yellow-to-gray sun positions, reused in the long route sequence.
- **T01 white-field lettering:** hand-drawn uppercase, black or red, irregular baseline.
- **T02 dark-field lettering:** hand-drawn uppercase white, large location title or compact annotation.

### Audio

- **A01 narration:** center-dominant English voice, continuous intellectual pacing with short phrase gaps.
- **A02 final fade:** narration ends near 02:07.92; level drops below −42 dBFS by 02:08.15 and remains low through export.
- **Music/SFX:** unavailable as verified separate elements. Do not add them in a strict reconstruction unless intentionally redesigning.

---

# Engine A — Script Intelligence

## Packaging promise

- **Title promise (Medium confidence; derived from filename):** “How long could you drive towards the sunset?”
- **Thumbnail promise:** unavailable; no separate thumbnail supplied.
- **Combined click question:** What is the longest sunset obtainable while obeying road and speed constraints?
- **Opening validation:** immediate. The first sentence restates the question and supplies the governing constraints by 00:05.30.
- **Delivery:** **MATCH**. The result is stated and visually compared at 01:44.48–01:53.08.

## Script beats and loop status

| Beat | Time | Spoken content (condensed) | Function | Active viewer question | Loop status |
|---|---|---|---|---|---|
| A01 | 00:00.00–00:05.30 | Longest possible sunset while driving legally on paved roads? | Hook + constraints | What is the maximum? | Main loop opened |
| A02 | 00:05.76–00:13.28 | Sunset begins at first horizon contact and ends at full disappearance; painterly scene does not qualify. | Definition + pattern break | What exactly counts? | Rules loop escalating |
| A03 | 00:13.82–00:20.42 | Several increasingly absurd cases still are not sunsets. | Comic reinforcement | Are there loopholes in the definition? | Partially answered |
| A04 | 00:21.06–00:31.18 | Rising again disqualifies it; nearby hills do not count; use the idealized horizon. | Rule closure | What boundary is physically valid? | Rules loop answered |
| A05 | 00:31.54–00:42.52 | At London latitude Earth moves ~1000 km/h; flying west can extend sunset until fuel ends. | Principle + counterexample + caveat | Can motion cancel Earth’s rotation? | New loop opened/limited |
| A06 | 00:42.96–00:49.40 | Go far north/south; nearer a pole, keeping up is easier. | Directional inference | Where is chasing the sun feasible? | Location loop opened |
| A07 | 00:49.92–00:59.40 | No paved roads near poles; Longyearbyen is closest and gives just under an hour. | Constraint + benchmark | Is ~55 minutes the answer? | Partial payoff; larger loop remains |
| A08 | 00:59.74–01:07.92 | Driving west fails; even far north requires ~half the speed of sound. | Failed strategy + quantified proof | Is there any legal driving solution? | Stakes escalate |
| A09 | 01:08.44–01:19.48 | Better approach: near a barely-setting sun, the day-night line moves NW, slows, reverses SW. | Reversal/mechanism | How can reversal be exploited? | Winning loop opened |
| A10 | 01:20.12–01:26.64 | Wait in the car until first contact and the line is about to pass. | Step 1 | When should the drive begin? | Answered |
| A11 | 01:26.90–01:34.96 | Drive north ahead of the line, then turn south across it into night. | Steps 2–3 | What exact route maximizes duration? | Strategy answered |
| A12 | 01:35.62–01:44.20 | Search with PyEphem and Norwegian-highway GPS traces; works across the Arctic Circle. | Evidence/method | Is the strategy computationally supported? | Proof supplied |
| A13 | 01:44.48–01:53.08 | Best result is consistently ~95 minutes, ~40 longer than Longyearbyen. | Major payoff | What is the maximum? | Main loop answered |
| A14 | 01:53.08–02:07.92 | Spin counterclockwise to slow Earth by an imperceptible fraction; “might be worth it.” | Joke coda + emotional closure | Can one gain even more time? | Comic micro-loop answered |

## Hook architecture

- **Context:** “sunset,” “driving,” “speed limit,” and “paved roads” are understandable immediately.
- **Relevance:** a universal natural event is turned into a constrained optimization puzzle.
- **Pattern break:** the video refuses familiar-looking sunsets unless the geometric definition is satisfied.
- **Open question:** maximum duration and route remain unknown until the final third.
- **Value preview:** a counterintuitive but calculable answer is promised.
- **Click validation:** strong; the exact question is restated without preamble.

## Causal narrative spine

**Setup:** Find the longest legal road sunset.  
**But:** “Sunset” needs strict geometric rules.  
**Therefore:** common visual and local-obstruction loopholes are excluded.  
**But:** flying west can cancel rotation only until fuel runs out.  
**Therefore:** move toward a pole where rotational ground speed is lower.  
**But:** no paved roads reach the poles, and due-west driving still needs ~355 mph.  
**Therefore:** exploit a reversing day-night boundary, wait, drive north, then cross south.  
**Payoff:** route search returns ~95 minutes, roughly 40 minutes beyond the Longyearbyen benchmark.  
**Coda:** a physically real but infinitesimal spinning “improvement” restores human warmth.

No major “and then” chain dominates. Each section either establishes a necessary premise, kills a tempting strategy, or unlocks the next strategy.

## Curiosity and payoff architecture

- **Main loop:** maximum duration (00:00 → 01:44–01:53).
- **Nested loops:** definition (00:05–00:31); latitude (00:42–00:59); failed west strategy (00:59–01:08); reversing-boundary strategy (01:08–01:35); computational evidence (01:35–01:44).
- **Micro-payoffs:** precise definition; airliner loophole; ~55-minute benchmark; 355 mph impossibility; three-step route.
- **Major payoff:** `~95 min`.
- **Comparative payoff:** `~95 min` versus `~55 min`, converting an abstract number into gain.
- **Emotional/humor payoff:** “a little more time here with you,” built on the returned painterly sunset.
- **Curiosity trajectory:** expanding through 01:08, focused through 01:35, answered in 01:44–01:53, then replaced by a short joke loop. It is not artificially prolonged.

## Logic and evidence order

The dominant pattern is **claim → geometric reason → constraint → consequence**. The strongest ordering choice is introducing the 55-minute Longyearbyen benchmark before rejecting due-west driving; this gives the final 95-minute result a meaningful comparator. The PyEphem/GPS method arrives immediately before the numerical reveal, so the payoff is earned.

Limitations: the video does not expose the route-search code, objective function, full road dataset, date range, terrain visibility, acceleration/turn constraints, or sensitivity analysis. The claim is therefore well-motivated within the explainer but not independently reproducible from the video alone. This is an evidence-depth limitation, not an internal contradiction.

## Emotional, pacing, retention, shareability

- Intended movement: curiosity → amusement → analytical surprise → apparent dead end → renewed hope → proof/payoff → warmth/humor.
- Opening risk: low; context is immediate.
- Early-body risk: the 00:13–00:21 exclusion gags could feel indulgent, but their rapid replacement edits and escalating absurdity keep them short.
- Midpoint risk: low; `~55 min`, `WEST`, and `355 mph` are concrete resets.
- Pre-payoff risk: S14 is the longest shot, but the car, line, map, labels, and inset change continually.
- CTA risk: none. There is no subscribe/product/next-video interruption.
- Shareable/replay moments: “arbitrarily long sunset” in an airliner; `355 mph`; the reversing terminator; `~95 min`; counterclockwise spinning. Replay is predominantly **positive**, though the fast NW→SW map transition around 01:14–01:20 may produce **confusion replay** for viewers unfamiliar with the terminator.

## CTA and next-video bridge

No explicit CTA is present. The ending deliberately favors closure over conversion. A seamless next-video bridge, if needed, would be: **“What changes if the vehicle is not restricted to roads—or if the target is a sunrise, eclipse shadow, or twilight rather than the solar disc?”** Place it after the final two-second hold, not over the emotional line.

## Seven-lens consensus

**Strong agreement:** immediate hook; causally connected failed strategies; benchmark before final payoff; high clarity of the moving-boundary explanation; clean callback ending.  
**Tradeoff:** the strict definition sequence is longer than the minimum, but it simultaneously prevents objections and creates comedy.  
**Critical problems:** none observed.  
**High-priority problem:** the computational proof is asserted rather than reproducible; a link/brief route specification would strengthen intellectual confidence.  
**Medium-priority problems:** explain the NW→SW reversal one beat more slowly; label `355 mph` as approximate and tie it explicitly to the shown latitude; clarify whether road speed limits and route feasibility are globally or locally constrained.  
**Highest-leverage fixes:** add a two-line methodology card before `~95 min`; hold the terminator reversal for ~0.5 s; surface the 55→95 gain in narration and text simultaneously.

| Dimension | Rating |
|---|---|
| Hook | Exceptional |
| Curiosity | Strong |
| Narrative spine | Strong |
| Logic | Strong, with reproducibility limitation |
| Pacing | Strong |
| Payoffs | Strong |
| Emotional engagement | Strong for a technical short |
| Intellectual clarity | Strong |
| CTA | Not applicable/absent by design |
| Title alignment | Exceptional |
| Thumbnail alignment | Unavailable |

---

# Engine B — Visual Intelligence

## Ground-truth visual summary

The video alternates among six coordinate systems: whiteboard/presenter, white horizon diagram, richly colored sunset, dark rotating globe, polar twilight landscape, and gray Scandinavia map. Each system is introduced by a hard cut or unmistakable replacement. Within a system, change is additive and rule-based: one disc, arrow, line, label, car, or inset moves while the reference frame remains fixed.

## Composition, attention, and dominance

- **Dominant composition:** large negative space with one diagram centered around a single horizon or map boundary. Most subjects occupy 15–45% of frame area.
- **Dominant attention order:** moving yellow sun/car → red directional mark or verdict → black/white label → gray context.
- **Primary attention device:** motion plus scarce saturation. Yellow is usually the only saturated object; red is reserved for verdicts, boundaries, and direction.
- **Secondary device:** handwritten labels placed adjacent to the exact variable they name.
- **Attention competition:** low. The painterly sunset is the only dense background, and its high-detail texture is intentionally used for emotional/pattern-interrupt shots rather than technical diagrams.
- **Eye flow:** typically left-to-right along a horizon; then top-to-bottom in split comparisons; along a curved terminator on maps.

## Color system

| Color family | Visible job |
|---|---|
| Near-white | Neutral reasoning field and negative space |
| Black | Outlines, baseline geometry, arrows, primary diagram text |
| Mid-gray | Context, past/below-horizon sun states, land/water, secondary structure |
| Yellow | Sun/current target; highest saliency on white diagrams |
| Red/coral | Invalid X, emphasized path, terminator/sunset band, direction, Arctic Circle |
| Green | Used once for “valid,” making approval unambiguous |
| Indigo/red/orange | Emotional sunset bookends and dark polar atmosphere |

## Typography and graphics

Text is manually drawn, mostly uppercase, slightly irregular, and aligned to nearby geometry rather than a rigid grid. Exact numerical text is safest as an editor overlay. The core graphic vocabulary is: thin horizon lines, small black arrows, red verdict Xs, one green check, red dashed meridians/circles, curved map bands, simple braces, and boxed miniature sun sequences.

## Motion and edit grammar

- **Usually moves:** the sun disc, car, day-night line, airplane, route arrow, spin trails, and newly introduced label.
- **Usually static:** horizon, globe/map, background, lighting, already-explained labels, and camera.
- **Camera:** locked for most shots. S14 uses controlled map reframing/translation to follow the car and boundary. Other perceived movement is object/layer motion, not camera motion.
- **Reveals:** additive drawing, replacement, or transform; exact geometry is best built with vector/shape layers.
- **Cuts:** used when the coordinate system or argumentative role changes. Animation is used when only a variable inside the same model changes.
- **Motion economy:** one hero at a time; surrounding anchors remain still so motion has explanatory meaning.

## Visual information value and fatigue

Essential/evidential visuals: V03, V10–V13, V17, V19–V29. Explanatory/reinforcing visuals: V01–V09 and V18. Emotional visuals: V04 and V30–V34. Decorative-only content is minimal. The highest fatigue risk is the 21.3-second map shot S14, but it avoids stasis through a changing boundary, moving car, map reframe, labels, and an inset progress diagram. The weakest information moment is V06 by itself; it only works as a rapid absurdist bridge into V07.

## Object lifecycles and callbacks

- **Sun O01/O02:** introduced on the board → formalized as yellow/gray horizon states → used in invalid examples → converted into polar/map inset data → quantified as 55/95 minutes → returns as a painterly sun.
- **Car O04:** constraint in the hook → absent during pure geometry → benchmark vehicle in Longyearbyen → map cursor for the winning strategy → result icon in the comparison.
- **Day-night boundary G02:** first implicit in horizon diagrams → explicit on globe → becomes labeled `DAY / SUNSET / NIGHT` map band → drives the final route.
- **Painterly sunset E02:** first appears as “NOT A SUNSET” at 00:11.792; returns without that verdict at 01:53.458, converting a rejected visual into emotional closure.

## Cross-frame consistency/drift audit

- **Characters:** C02/C03 maintain left/right identity across the painterly callback. High confidence.
- **Vehicles:** the North Pole truck, Longyearbyen hatchback, and map icon differ. Likely intentional functional simplification; preserve per-shot designs rather than forcing one exact car.
- **Maps:** Scandinavia changes crop, rotation, and scale as required by the argument. This is intentional reframe, not accidental geometry drift.
- **Sun:** outline thickness and diameter vary slightly between diagrams. Preserve the local relative scale, but standardize fill/outline within any rebuilt shot.
- **Lighting:** white diagram scenes are flat by design; dark scenes use a left-edge solar glow. No unintended lighting drift is evident.
- **Typography:** hand variation is intentional. Preserve family, hierarchy, and placement; exact glyph duplication is unnecessary unless matching pixel-for-pixel.

## Visual consensus

- **Dominant composition strategy:** one geometric model per frame with large negative space.
- **Dominant attention strategy:** scarce yellow/red accents plus motion.
- **Dominant motion strategy:** animate the variable, lock the coordinate frame.
- **Dominant editing strategy:** cut on model/argument change; add or replace within a model.
- **Strongest pattern interrupt:** S03 painterly sunset at 00:11.792.
- **Strongest callback:** S18 painterly sunset return at 01:53.458.
- **Strongest visual payoff:** S17 split 95-vs-55 comparison.
- **Weakest moment:** isolated yellow-square V06, meaningful only in its rapid gag chain.
- **Highest fatigue risk:** S14 map strategy, mitigated by layered motion.
- **Reusable visual rule:** **Keep context gray and static; give the new causal variable color, motion, and the nearest label.**

| Evidence category | Confidence |
|---|---|
| Visible objects / subjects / pose | High |
| Composition / spatial relationships | High |
| Camera framing | High |
| Lighting/color | High |
| Object/subject motion | High (24 fps pass) |
| Camera motion | Medium–High |
| Transition classification | High for hard cuts; Medium for gradual replacements |
| Text | High where OCR/source frame is readable |
| Reconstruction | High for vector scenes; Medium for painterly texture |

---

# Engine C — Reconstruction Intelligence

## Global production locks

These apply to every card unless the card explicitly overrides them:

1. Canvas is 720×1280, vertical 9:16.
2. White-diagram scenes use irregular black ink outlines, flat fills, no shadows, and abundant white negative space.
3. Yellow sun = current/visible solar state; gray sun = below-horizon/previous state; red = verdict/direction/boundary; green = valid.
4. Hand lettering is uppercase, irregular, and subordinate to the diagram. Bake text only when exact source imitation is required; otherwise overlay in the editor.
5. Camera remains locked unless a map card explicitly calls for reframe/track.
6. Do not introduce photorealism, gradients, lens effects, extra icons, extra people, decorative texture, or autonomous background motion into white-diagram scenes.
7. “Recreation method” below does **not** claim the original software.

## V01 — 00:00.000–00:05.833

**SHOT:** S01  
**SOURCE REFERENCE:** 00:02.500 — [keyframe](keyframes/V01_0002500ms.jpg)  
**DURATION:** 5.833 s

### C1. What the viewer actually sees

If you paused the video here, you would see a white 9:16 frame. A wide hand-drawn classroom board occupies almost the full upper half. On it, a large partial sun intrudes from far left, a gray Earth floats center-right, and a tiny car curves along the Earth’s upper-right edge. Below the board, an anonymous stick figure stands left-of-center reading a sheet of paper. The lower-right two-thirds remain empty. Literal grounding: **a stick presenter reads beneath a board showing the sun, Earth, and a tiny moving vehicle.**

### C2. Script ↔ visual synchronization

**Spoken words:** “What’s the longest possible sunset you can experience while driving, assuming you’re obeying the speed limit and driving on paved roads?”  
**Visual appears:** during the full hook.  
**Trigger idea:** “sunset … driving.”  
**Motion synchronized with:** no major visible motion; the visual holds while narration supplies constraints.  
**Likely communication function:** compress the entire question into one instantly readable visual proposition.

### C3. Change from previous visual

**Added:** all elements from black/start. **Removed:** none. **Moved/resized/recolored/reframed/replaced/text changed:** none observed. **Remained static:** board, sun, Earth, car, figure, paper, camera.

### C4. Visual purpose

**ORIENTING / ESSENTIAL / REINFORCING.** Without it, the opening would lose its immediate sun–Earth–vehicle relationship and feel like unsupported narration.

### C5. Construction map

**Background:** white. **Main subject:** upper board. **Secondary:** lower-left stick presenter/paper. **Graphics/text:** sun rays, Earth continents, tiny car and curved arrow; no readable title. **Static coordinate frame:** board rectangle. **Visual hero:** sun–Earth–car triad.  
**Layers:** 1 white field; 2 board frame/gray board fill; 3 sun/Earth/car; 4 presenter; 5 paper.

### C6. Exact composition/layout map

**Canvas:** 720×1280. **Approximate visual map—not pixel measurement:** board x≈2–98%, y≈10–48%; sun edge x≈3–26%, y≈14–34%; Earth x≈40–72%, y≈21–43%; presenter x≈9–34%, y≈55–91%. Large negative space x≈38–100%, y≈50–100%. Board is roughly three times the presenter's visual mass. Eye path: board sun → Earth/car → presenter/paper.

### C7. Attention order

**First:** board/Earth because of scale and centrality. **Second:** partial sun and tiny car because their relationship creates the puzzle. **Third:** reading presenter. **Competition:** low. **Flow:** controlled.

### C8. Image reuse status

**IMAGE SOURCE:** NEW BASE IMAGE. **BASE VISUAL:** N/A. **BASE ASSETS:** C01, O01/O03/O04, E01. **Changes from base:** N/A.

### C9. Forensic image DNA

**Output:** flat hand-drawn explainer frame. **Subject:** featureless stick presenter holding paper. **Pose:** standing, one bent arm at waist, one holding sheet. **Environment/geometry:** outlined board over open white field. **Camera:** orthographic/front-on, no depth. **Lighting:** none/flat. **Color:** black, white, gray with implied white sun. **Style:** irregular ink line and flat gray fill. **Typography:** none. **Graphic DNA:** curved arrow and simple icons.

### C10. Exact reconstruction image prompt

Create a 720×1280 vertical hand-drawn explainer frame on a clean white field. Across the upper 38% place a wide, slightly irregular black-outlined classroom board with pale-to-medium gray fill. On the board, crop a large outlined sun at far left with long triangular rays pointing inward; place a gray globe slightly right of center with light gray continents; add a tiny black car riding over the globe’s upper-right curve with a short curved directional arrow. Below the board at lower-left, draw a featureless stick figure with an empty white oval head, thin black limbs, one hand on its hip and the other holding a white sheet. Preserve the large empty lower-right area, flat orthographic perspective, uneven ink line, no shadows, no extra text, and the exact vertical hierarchy board → presenter → negative space.

### C11. Text bake/overlay decision

**BAKE EXACT TEXT:** NO. **Clean plate:** board and character only. **Overlay:** none required.

### C12. Fidelity/do-not-change lock

**Character:** one anonymous presenter. **Pose:** standing/reading. **Object count:** one board, one sun crop, one globe, one tiny car, one paper. **Relationships:** board above; presenter lower-left. **Background/camera:** white, front-on, locked. **Color:** gray board/Earth, black outlines. **Negative space:** preserve lower-right. **Prohibited additions:** title, road photo, facial features, scenery, shadows.

### C13. Image prompt QC

Subject High; pose High; composition High; scale High; perspective High; lighting High; color Medium–High; text N/A; negative space High; continuity High; unsupported-addition risk Low.

### C14. What exactly animates?

No verified information-bearing animation. Minor line shimmer, if present, is not analytically necessary.

### C15. What must remain still?

Board, presenter, paper, sun, Earth, car, background, and camera remain still to let the spoken constraints land.

### C16. Why move / why not more?

**Motion hero:** none. **Static anchor:** entire diagram. **Why:** the hook is already dense in language; added motion would compete with constraint comprehension. **Over-animation risk:** high. **Motion purpose:** static visual orientation under verbal setup.

### C17. Motion-cue conflict check

Source image implies motion: **NO**, except the drawn curved arrow. Requested motion agrees: **YES—no physical movement.**

### C18. Temporal animation sequence

Start full composition → hold through question → cut at 00:05.833. **Source state duration:** 5.833 s. **Recommended generated clip:** 5.8 s. **Editorial trim:** cut on the end of “roads.”

### C19. Best reconstruction method

**A — STATIC IMAGE** with optional editor hold. **Why:** no required temporal geometry.

### C20. AI motion suitability

**LOW.** Generative motion adds no information and risks drifting the board, globe, or character.

### C21. Editor/motion-design build

**Layers:** white background; board/frame; sun/Earth/car; presenter; paper. **Build:** draw base → place board icons → position presenter → hold. **After Effects/CapCut/Premiere:** still image or nested vector comp. **Recreation method—original software not verified.**

### C22. First/last-frame decision

**NO.** No transformation destination is needed.

### C23. Final AI image-to-video prompt

**ANIMATION PROMPT:** “Locked camera. Hold the entire hand-drawn board, sun, Earth, tiny car, presenter, paper and white background completely still for the spoken hook.”  
**CHARACTER COUNT:** 146 / 500  
**STATUS:** PASS

### C24. Tool-specific adapter

Tool-neutral. For Runway, use the source image and the same locked-camera instruction; suppress autonomous character movement through positive stillness language.

### C25. Edit out / next visual

**Edit out:** hard cut at 00:05.833. **Trigger:** narration finishes the road constraint. **Next:** V02. **Continuity:** sun concept persists; the board becomes a direct horizon diagram.

### C26. One-line reconstruction rule

**RECONSTRUCTION RULE:** Visualize the whole question once, then hold absolutely still while the verbal constraints establish the puzzle.

---

## V02 — 00:05.833–00:08.000

**SHOT:** S02  
**SOURCE REFERENCE:** 00:06.250 — [keyframe](keyframes/V02_0006250ms.jpg)  
**DURATION:** ~2.167 s

### C1. What the viewer actually sees

If you paused here, you would see a white vertical field split by a thin irregular black horizon at mid-height. A yellow sun disc sits at the far-left edge just above the line. A red hand-drawn X floats above it. Everything else is empty. Literal grounding: **one yellow sun and one red X sit against a white horizon diagram.**

### C2. Script ↔ visual synchronization

**Words:** “For the purpose of our question, sunset starts the instant the sun touches the horizon…” **Appears:** during the phrase. **Trigger:** “starts” / “touches the horizon.” **Motion sync:** the first sun position appears before later positions are copied. **Function:** establish coordinate frame and initial condition.

### C3. Change from previous visual

**Added:** horizon, yellow sun, red X. **Removed:** board/presenter/Earth. **Reframed/replaced:** full visual system becomes E01. **Static:** horizon/camera.

### C4. Visual purpose

**ESSENTIAL / ORIENTING.** Removing it would eliminate the physical definition of first contact.

### C5. Construction map

Background white; hero O01 at left; G01 X above; horizon fixed at y≈50%. Layers: white → horizon → sun → red X.

### C6. Exact composition/layout map

Sun x≈0–18%, y≈38–51%; horizon y≈50%; X x≈5–15%, y≈25–33%. Negative space exceeds 80% of frame. Eye path: red X → yellow sun → horizon contact.

### C7. Attention order

First yellow sun, second red X, third horizon. Color and isolation drive the hierarchy; competition is clean.

### C8. Image reuse status

**NEW BASE IMAGE** for the horizon sequence. Base assets E01, O01, G01.

### C9. Forensic image DNA

Flat vector-like ink, perfect conceptual front view, saturated yellow disc with uneven outline, thin black horizon, muted coral-red X, no lighting/depth/text.

### C10. Exact reconstruction image prompt

Create a 720×1280 vertical minimalist hand-drawn diagram on pure white. Draw one thin, slightly wavy black horizontal line across the complete frame at exactly mid-height. At the far-left edge, place one flat saturated-yellow circle with an irregular black outline, diameter about 17% of frame width, resting just above and touching the line. Center a loose coral-red handwritten X above that disc. Leave the remaining frame empty. Use no shadows, gradients, texture, labels, people, scenery, or extra objects. Preserve the extreme left placement, midline contact, large negative space, and simple black/yellow/red palette.

### C11. Text bake/overlay decision

No text. Bake the red X as a graphic, not typography.

### C12. Fidelity lock

One sun; one X; one horizon; left placement; camera locked; pure white; no extra sun positions yet.

### C13. Image prompt QC

Subject High; pose/state High; composition High; scale High; perspective High; lighting N/A; color High; text N/A; negative space High; continuity High; risk Low.

### C14. What animates?

The first yellow disc enters/appears at the left and settles to first-contact height. Camera/horizon stay locked.

### C15. What remains still?

Horizon, X, background, camera. Their stability defines the coordinate system.

### C16. Why this motion?

Motion hero O01. The sun is the variable being defined; moving the horizon would invert the model. No other motion improves comprehension.

### C17. Motion-cue conflict

No blur/speed lines. The disc’s clean edge permits controlled keyframe translation. Requested direction agrees with the following left-to-right sequence.

### C18. Temporal sequence

Blank horizon → yellow sun appears at far left above line → holds at first-contact reference → later copies begin in V03. Recommended clip ~2.2 s.

### C19. Best method

**C — VECTOR MOTION GRAPHICS / B — EDITOR KEYFRAMES.** Deterministic geometry is required.

### C20. AI suitability

**LOW.** Exact circle, horizon contact, and verdict placement are easier with shape layers.

### C21. Editor build

White solid; horizon shape; yellow ellipse; red X strokes. Keyframe ellipse position/opacity only. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Simple position/opacity is sufficient.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Reveal one yellow sun disc at the far-left horizon and let it settle into first contact with the black line. Keep the red X, horizon and white field fixed.”  
**CHARACTER COUNT:** 170 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; for AI video use the source image and request only the short settling motion. Prefer vectors.

### C25. Edit out

Continue without a cut into V03 as new sun positions are added. Continuity device: same horizon and disc geometry.

### C26. Rule

**RECONSTRUCTION RULE:** Establish the invariant horizon before animating the changing solar state.

---

## V03 — 00:08.000–00:11.792

**SHOT:** S02  
**SOURCE:** 00:10.750 — [keyframe](keyframes/V03_0010750ms.jpg)  
**DURATION:** ~3.792 s

### C1. What the viewer actually sees

The white horizon now carries a left-to-right chain of five sun states: two yellow discs above the line, one half-yellow/half-gray at contact, then two gray discs below it. Small black arrows link the positions. Red dashed vertical limits stand near the first and last valid moments; a green check sits above the middle interval, with red Xs outside both limits. Literal grounding: **a color-coded sun sequence crosses a horizon between two dashed timing boundaries.**

### C2. Script sync

**Words:** “…and ends when it disappears completely…” **Appears:** during/after phrase. **Trigger:** “ends” / “disappears completely.” **Motion:** successive disc copies and arrows reveal left-to-right. **Function:** encode the valid interval and exclude before/after states.

### C3. Previous change

Added four sun states, arrows, dashed boundaries, green check, right X; original left sun/X remain. Gray replaces yellow as discs pass below the line.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** Without it, the operational definition would remain verbal rather than measurable.

### C5. Construction map

Static frame: horizon. Hero: yellow→gray sequence. Layers: white; horizon; five discs; arrows; dashed coral limits; verdict marks.

### C6. Layout

Sequence spans x≈0–100%, y≈39–62%; dashed lines at x≈25% and x≈80%; green check x≈50%, y≈25–33%; outer Xs at x≈7% and x≈90%. Discs are equal size. Eye path is strictly left-to-right.

### C7. Attention

First yellow disc chain, second green check, third red boundaries/Xs. Slight competition is intentional but controlled by the horizontal narrative.

### C8. Reuse

**MODIFIED REUSE** of V02. Base V02; added repeated O01/O02, arrows, limits, green check, right X. Complete prompt follows.

### C9. DNA

Same flat white diagram; equal sun modules; yellow current/above, gray below/past; verdict color scarcity; orthographic view; no environmental detail.

### C10. Exact image prompt

Create a 720×1280 vertical minimalist hand-drawn horizon diagram on pure white. Draw a thin uneven black horizontal line across the full frame at mid-height. Arrange five equal black-outlined sun circles along a descending left-to-right trajectory: yellow above the line at far left; yellow slightly lower near x=29%; a half-yellow, half-dark-gray disc straddling the line at x=51%; a fully gray disc below the line near x=70%; and a fully gray disc farther below near x=88%. Connect consecutive states with small black curved arrows. Add thin coral-red dashed vertical guide lines near x=25% and x=80%. Place a green hand-drawn check above the valid middle interval and coral-red Xs above the outer invalid regions. Keep the rest empty; preserve equal disc size, exact color coding, flat fills, irregular ink, no shadows or extra labels.

### C11. Text decision

No words. Verdict marks and dashed guides may be baked as vector graphics.

### C12. Lock

Five discs only; equal diameter; left-to-right descent; two dashed lines; one green check; two red Xs; fixed horizon/camera; no labels.

### C13. QC

Subject/state High; composition High; scale High; perspective High; color High; text N/A; negative space High; continuity High; risk Low.

### C14. Animation

Discs appear sequentially left-to-right; arrows reveal after each new state; fill transitions yellow→half gray→gray; limits and verdicts reveal after the sequence.

### C15. Static

Horizon, camera, background, and already revealed states remain locked to provide temporal comparison.

### C16. Why

Motion communicates passage through a threshold. Camera motion would destroy positional comparison; background motion adds nothing. Motion hero is the newest disc.

### C17. Conflict

Source arrows imply left-to-right/downward progress; requested animation agrees.

### C18. Sequence

V02 state → add second yellow disc/arrow → add half-gray contact state → add gray below states → draw dashed limits → reveal check/X verdicts → hold → hard cut.

### C19. Method

**C — VECTOR MOTION GRAPHICS.** Shape layers, trim paths, opacity, fill swaps.

### C20. AI suitability

**LOW.** Exact counts, fill geometry, equal sizes, and guide positions should be deterministic.

### C21. Build

Precompose one sun symbol; duplicate five times; use position/fill keyframes; draw arrow strokes with trim paths; dash red guides; reveal verdict marks. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Editor keyframes are more faithful than a generated transformation.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Add equal sun states left-to-right along the fixed horizon: yellow above, half gray at contact, then gray below. Reveal each linking arrow, then the two dashed limits, green check and outer red Xs. Keep prior states fixed.”  
**CHARACTER COUNT:** 237 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; AI alternative only. For Runway, use the completed diagram as first frame and request restrained additive reveals, but expect geometry drift.

### C25. Edit out

Hard cut at 00:11.792 to V04. Conceptual continuity: the source says “this is not a sunset” as the formal diagram becomes a visually beautiful but invalid scene.

### C26. Rule

**RECONSTRUCTION RULE:** Use repeated equal symbols to turn continuous motion into a readable sequence of threshold states.

---

## V04 — 00:11.792–00:13.833

**SHOT:** S03  
**SOURCE:** 00:13.500 — [keyframe](keyframes/V04_0013500ms.jpg)  
**DURATION:** 2.042 s

### C1. What the viewer sees

The frame becomes a dense painterly sunset: indigo sky, red/orange/yellow horizontal strokes, a bright white-yellow sun just above the horizon, and a black-olive foreground. Two thin stick figures stand at lower-left facing the sun. White text near upper-center reads `NOT A SUNSET`; a small black arrow near the sun reads `NOT TOUCHING THE HORIZON (YET)`. Literal grounding: **two figures watch a vivid sun that has not yet reached the horizon, while text rejects it as a sunset.**

### C2. Script sync

**Words:** “…which means that for us, this is not a sunset.” **Appears:** during the punchline. **Trigger:** “not a sunset.” **Motion:** text/callout finish revealing over the static landscape. **Function:** pattern break and counterexample.

### C3. Change

White diagram is fully replaced by E02; two characters and exact labels added; palette, density, lighting, and depth all change.

### C4. Purpose

**EXPLANATORY / EMOTIONAL / PATTERN INTERRUPT.** It proves that familiar appearance is not sufficient and resets attention through a radical palette change.

### C5. Construction map

Background painted sky; midground sun/horizon; foreground dark land and C02/C03; text overlays. Hero: bright sun plus `NOT A SUNSET`. Layers: indigo base; red cloud strokes; orange/yellow glow; sun/reflection; dark land; figures; labels/arrows.

### C6. Layout

Sun x≈45–67%, y≈45–61%; figures x≈4–31%, y≈55–80%; headline x≈45–93%, y≈40–47%; lower callout x≈57–98%, y≈55–59%. First look sun, second headline, third figures/callout.

### C7. Attention

Sun wins through luminance; headline through white-on-red contrast; figures through silhouette. Eye flow is controlled despite high background texture.

### C8. Reuse

**NEW BASE IMAGE** E02; later compositionally reused by V30–V34.

### C9. DNA

Painterly horizontal scribble strokes; small anonymous stick figures; frontal wide landscape compressed into 9:16; no camera blur; indigo/red/orange/yellow/black; hand-lettered white/black annotations.

### C10. Exact image prompt

Create a 720×1280 vertical hand-drawn painterly sunset illustration. Fill the upper half with a deep indigo night sky and dense irregular horizontal strokes that transition through dark crimson, bright red, orange and yellow toward the horizon. Place a large brilliant white-yellow sun slightly right of center, still visibly above and not touching the flat distant horizon, with a short broken reflection below it. Use a nearly black olive foreground with a curved shoreline/road sweeping from lower-right toward center. At lower-left, draw two small thin stick figures facing the sun: left figure with a black hair-filled head, right figure with a flat gray circular head. Preserve their left/right identity and scale. Leave text-safe space above and beside the sun. Maintain rough energetic strokes, high luminance contrast, no photorealism, no extra people or objects.

### C11. Text decision

**BAKE:** NO. **Clean plate:** painterly landscape/figures. **Overlay:** `NOT A SUNSET` in small white uppercase above the sun; `NOT TOUCHING THE HORIZON (YET)` in tiny black uppercase to the lower-right of the sun with a thin arrow pointing to its bottom edge.

### C12. Lock

Two figures at lower-left; sun right-of-center and above horizon; dark foreground; horizontal warm strokes; exact text and arrow positions; no extra stars beyond sparse white points; no sun contact.

### C13. QC

Subject High; pose High; composition High; scale High; perspective Medium–High; lighting High; color High; text High as overlay; negative space Medium; continuity High; unsupported risk Medium for painterly texture.

### C14. Animation

Only the labels/arrows need reveal; optional very subtle stroke flicker is nonessential. No camera movement.

### C15. Static

Sun, horizon, figures, shoreline, sky structure, and camera remain fixed so the geometrical objection is readable.

### C16. Why

Text is the information hero; moving the beautiful sun would imply a different state and weaken the joke. Extra atmospheric motion would compete with the verdict.

### C17. Conflict

No directional motion cues except annotation arrow. Source does not require physical sun movement.

### C18. Sequence

Hard cut to full sunset → reveal `NOT A SUNSET` → reveal lower arrow/callout → brief hold → cut.

### C19. Method

**K — HYBRID:** painted static plate plus deterministic text/arrow overlays.

### C20. AI suitability

**MEDIUM** for subtle organic texture; **LOW** for exact text and sun geometry.

### C21. Build

Background painting; separated sun glow; land; two character layers; white headline; black callout/arrow. Use opacity/trim path only. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Text overlay reveal suffices.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the vivid sunset, sun, shoreline and both stick figures still. Reveal ‘NOT A SUNSET’ above the sun, then draw the small arrow and ‘NOT TOUCHING THE HORIZON (YET)’ callout. Hold.”  
**CHARACTER COUNT:** 197 / 500  
**STATUS:** PASS

### C24. Adapter

For Runway, animate only faint hand-painted shimmer if desired; composite exact text in the editor.

### C25. Edit out

Hard cut at 00:13.833 to V05 on the repeated verbal phrase “not a sunset.” Continuity is conceptual, not visual.

### C26. Rule

**RECONSTRUCTION RULE:** Use the richest image as a contradiction, then let a precise label overturn the viewer’s first impression.

---

## V05 — 00:13.833–00:15.708

**SHOT:** S04  
**SOURCE:** 00:15.250 — [keyframe](keyframes/V05_0015250ms.jpg)  
**DURATION:** 1.875 s

### C1. Viewer sees

On the white horizon field, a yellow half-disc rises above the center of the line while its lower half is gray. Two full gray discs sit below the line at left and right, with small black arrows pointing toward/from the center state. A red X floats above. Literal: **an impossible yellow/gray sun transition is rejected with a red X.**

### C2. Sync

**Words:** “This is also not a sunset.” **Appears:** during phrase. **Trigger:** “also not.” **Motion:** side gray states and arrows build around center. **Function:** fast comic escalation.

### C3. Change

Painterly scene removed; white coordinate frame restored; three-disc state and red X added.

### C4. Purpose

**REINFORCING / HUMOR / PATTERN INTERRUPT.** By itself it is not new evidence; it demonstrates that visual tricks do not evade the definition.

### C5. Map

White background; horizon; center half yellow/gray disc; gray side discs; two arrows; red X. Hero: invalid center state.

### C6. Layout

Center disc x≈39–61%, y≈42–57%; gray discs x≈5–26% and 73–95%, y≈50–66%; X x≈43–56%, y≈25–34%. Symmetric visual weight.

### C7. Attention

Center yellow disc first, red X second, side discs/arrows third. Clean symmetric flow.

### C8. Reuse

**COMPOSITIONAL REUSE** of E01/O01/O02/G01; new symmetric arrangement.

### C9. DNA

Flat circle modules, white space, central symmetry, black arrows, coral X, no text or depth.

### C10. Prompt

Create a 720×1280 vertical white hand-drawn explainer diagram. Draw a thin uneven black horizon across mid-frame. Center one equal-sized sun circle straddling the line, with its upper half saturated yellow and its lower half medium gray, outlined in irregular black. Place one full medium-gray circle below the horizon near the far-left and one near the far-right at the same vertical level. Draw a short black arrow from the left gray circle toward the center and another from the center toward the right gray circle. Add one loose coral-red X above the center sun. Preserve near symmetry, large blank upper/lower space, flat fills, no shadows, no labels, no scenery, and exactly three discs.

### C11. Text

No text; bake X/arrows as editable graphics.

### C12. Lock

Three equal discs; center half yellow/gray; side discs gray; one horizon; two arrows; one X; locked camera.

### C13. QC

Subject/state High; composition High; scale High; perspective High; color High; text N/A; negative space High; continuity High; risk Low.

### C14. Animation

Side states and arrows appear around the center; the red X reveals last.

### C15. Static

Horizon and center reference remain fixed; after reveal all discs hold.

### C16. Why

Additive symmetry makes the absurd transition legible quickly. Camera/background motion would dilute the gag.

### C17. Conflict

Arrows imply left→center→right; requested reveal order agrees.

### C18. Sequence

Center state → left/right gray discs → arrows → red X → brief hold → replacement.

### C19. Method

**C — VECTOR MOTION GRAPHICS.** Shape duplication and opacity/trim paths.

### C20. AI suitability

**LOW** because disc count/fill symmetry are exact.

### C21. Build

Reuse sun precomp; duplicate/gray-fill; place symmetrically; trim arrow paths; draw X. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Deterministic additive reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the center half-yellow, half-gray sun on the horizon. Add equal gray discs below left and right, draw arrows left-to-center-to-right, then reveal the red X. Keep all geometry fixed after entry.”  
**CHARACTER COUNT:** 213 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors strongly preferred over AI.

### C25. Edit out

Replacement at 00:15.708 to V06, motivated by the next repeated “not a sunset.” White field/horizon continue.

### C26. Rule

**RECONSTRUCTION RULE:** For rapid rule reinforcement, reuse the same coordinate frame and change only the impossible state.

---

## V06 — 00:15.708–00:16.458

**SHOT:** S05  
**SOURCE:** 00:15.917 — [keyframe](keyframes/V06_0015917ms.jpg)  
**DURATION:** 0.750 s

### C1. Viewer sees

A single flat yellow square with irregular black outline floats in the upper-left quadrant of the white horizon frame. No red X is visible yet. Literal: **one yellow square replaces the circular sun.**

### C2. Sync

**Words:** start of “This is definitely not a sunset.” **Appears:** before/during “definitely.” **Trigger:** escalating negation. **Motion:** square appears, then begins transforming in V07. **Function:** absurd pattern break.

### C3. Change

Three discs/arrows/X removed; one yellow square added; horizon retained.

### C4. Purpose

**REINFORCING / HUMOR.** Its loss would reduce the escalating absurdity but not the core explanation.

### C5. Map

White field; mid-horizon; yellow square at x≈10–31%, y≈28–44%. Hero square. Layers: white, line, square.

### C6. Layout

Square occupies ~20% frame width; strong upper-left isolation; >85% negative space. Eye path is immediate and singular.

### C7. Attention

Square first, horizon second; no competition.

### C8. Reuse

**GRAPHIC-ONLY MODIFICATION** of E01; O01 circle replaced by yellow square.

### C9. DNA

Flat yellow fill, hand-wobbled black perimeter, orthographic, no shadow/text/depth.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn diagram on pure white. Draw a thin slightly wavy black horizon across the full frame at mid-height. Place one isolated flat saturated-yellow square with a loose irregular black outline in the upper-left quadrant, spanning about 20% of the frame width and sitting clearly above the horizon. Leave every other area blank. Use no text, red marks, people, scenery, shadows, gradients, or extra shapes. Preserve the extreme simplicity and the square’s slight hand-drawn imperfection.

### C11. Text

None.

### C12. Lock

Exactly one yellow square and one horizon; no X yet; no sun discs; locked camera.

### C13. QC

All visual matching dimensions High; text N/A; unsupported risk Low.

### C14. Animation

Square appears as a replacement and holds briefly.

### C15. Static

Horizon/background/camera remain fixed.

### C16. Why

The shape substitution is the joke; movement would delay recognition. Motion purpose: instantaneous category violation.

### C17. Conflict

No implied motion.

### C18. Sequence

Hard replacement → square hold → square begins folding/opening into V07.

### C19. Method

**C — VECTOR MOTION GRAPHICS**, with a square shape prepared for a hinged transform.

### C20. AI suitability

**LOW.** Exact simple geometry needs no generation.

### C21. Build

White solid; horizon; yellow quadrilateral precomp. Hold, then pass to V07. Recreation method—original software not verified.

### C22. First/last frame

**YES** only if using AI for the square→door transformation; deterministic vector/2.5D is preferred. Start: isolated square. End: open door with figure.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the isolated yellow square above the fixed black horizon for a brief beat. Keep the white field completely empty and still.”  
**CHARACTER COUNT:** 143 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; no AI needed.

### C25. Edit out

Transform continues into V07 at ~00:16.458. Continuity: the yellow square becomes the door panel.

### C26. Rule

**RECONSTRUCTION RULE:** A single impossible object can function as a visual punchline when the surrounding grammar stays unchanged.

---

## V07 — 00:16.458–00:17.750

**SHOT:** S05  
**SOURCE:** 00:17.250 — [keyframe](keyframes/V07_0017250ms.jpg)  
**DURATION:** ~1.292 s

### C1. Viewer sees

The yellow square has become an open yellow door angled toward the viewer at upper-left. Behind it, a small black-haired/capped stick bust appears inside a thin black rectangular frame. A large red X floats upper-right. The horizon remains centered. Literal: **a person appears behind an open yellow door, and the scene is rejected.**

### C2. Sync

**Words:** “…definitely not a sunset.” **Appears:** on the stressed rejection. **Trigger:** “definitely.” **Motion:** square hinges open; figure is revealed; X appears. **Function:** payoff to V06’s absurd setup.

### C3. Change

Square rotates/folds into door; black frame/person added; red X added. Horizon remains.

### C4. Purpose

**HUMOR / REINFORCING / REVEAL.** Removing it would break the square setup/payoff pair.

### C5. Map

White background; horizon; yellow door panel x≈8–17%; black doorway/person x≈14–35%; X x≈59–75%, y≈22–35%. Motion hero: door.

### C6. Layout

Left visual mass counterbalanced by isolated red X on right; large negative space elsewhere. Eye path door → person → X.

### C7. Attention

Yellow door first, face/head second, red X third. Controlled.

### C8. Reuse

**MODIFIED REUSE** of V06. Base square becomes hinged door; C04 and G01 added.

### C9. DNA

Cartoon hinge/perspective, flat yellow, black stick bust/hair, no shading except yellow side plane, red verdict.

### C10. Prompt

Create a 720×1280 vertical hand-drawn explainer frame on pure white with a thin uneven black horizon at mid-height. In the upper-left, draw an open saturated-yellow door: a narrow yellow side edge at far left and a larger yellow panel angled outward toward the viewer, outlined in irregular black. Behind it, place a simple thin black rectangular doorway containing a small anonymous stick-figure bust with a white circular head and a solid black cap or hair wedge. Place one loose coral-red X in the upper-right quadrant. Keep all elements flat, sparse and front-facing except the door angle. Preserve the door/person scale, left-heavy composition, empty lower half, and absence of scenery or shadows.

### C11. Text

No text; red X remains a separate vector layer.

### C12. Lock

One open yellow door, one small figure, one black doorway, one X, fixed horizon; do not add a room or facial features.

### C13. QC

Subject High; pose/state High; composition High; scale High; perspective Medium–High; color High; text N/A; negative space High; continuity High.

### C14. Animation

Door panel rotates outward around a vertical left hinge; doorway/person reveal behind; red X draws last.

### C15. Static

Horizon, background, doorway position, camera; person can remain completely still.

### C16. Why

The hinged reveal explains what the square was. Moving the person would add a second joke beat and compete with the transformation.

### C17. Conflict

Door perspective implies outward opening; requested hinge motion agrees.

### C18. Sequence

Yellow square → left edge becomes hinge → panel swings open → doorway/person revealed → red X appears → hold.

### C19. Method

**K — HYBRID 2.5D/vector.** Parent door panel to hinge null; reveal back layer; draw X.

### C20. AI suitability

**MEDIUM–LOW.** Organic hinge motion is possible, but exact geometry/identity is safer with layers.

### C21. Build

Door panel; hinge edge; doorway; C04; X; horizon. Rotation/scale skew + opacity/mask. Recreation method—original software not verified.

### C22. First/last frame

**YES** if AI is used. Start prompt: V06 exact square. End prompt: V07 exact open door/figure/X. Transition: one clean hinge opening, no camera move or morphing background.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. The yellow square becomes a door panel and swings outward on its left hinge, revealing the small black-haired stick figure in the doorway. Draw the red X last. Keep the horizon and white field fixed.”  
**CHARACTER COUNT:** 214 / 500  
**STATUS:** PASS

### C24. Adapter

For first/last-frame AI, supply V06 and V07 plates; otherwise use editor layers.

### C25. Edit out

Hard replacement at 00:17.750 to V08. Continuity: yellow shape/color persists as a sun disc.

### C26. Rule

**RECONSTRUCTION RULE:** Pay off an abstract shape by transforming it into one readable object while every anchor remains fixed.

---

## V08 — 00:17.750–00:21.083

**SHOT:** S06  
**SOURCE:** 00:20.250 — [keyframe](keyframes/V08_0020250ms.jpg)  
**DURATION:** 3.333 s

### C1. Viewer sees

Four equal yellow sun discs form a left-to-right chain along the horizon, connected by black arrows. The first is above/left, the second descends, the third shakes at the line, and the rightmost is cracked with jagged black fissures. A small black handwritten sound label `BRU-WAAK` sits above the cracked disc; a red X floats above the sequence. Literal: **a sun undergoes escalating transformations and breaks, but is still rejected.**

### C2. Sync

**Words:** “And no matter what happens here, this will not be a sunset.” **Appears:** throughout the line. **Trigger:** “no matter what happens.” **Motion:** discs enter in stages, shake, crack, and receive the verdict. **Function:** close fanciful loopholes through exaggeration.

### C3. Change

Door/person removed; four yellow disc states, arrows, shake marks, cracks, sound label and X added.

### C4. Purpose

**REINFORCING / HUMOR / PATTERN INTERRUPT.** It keeps the definition sequence entertaining.

### C5. Map

Horizon fixed; disc chain x≈0–100%, y≈40–57%; X x≈70%, y≈24%; sound label at upper-right of final disc. Hero: cracked final disc.

### C6. Layout

Equal-sized discs occupy a horizontal band; first two are above, final two touch the line. Negative space dominates above/below. Eye path left→right→X/sound label.

### C7. Attention

Cracked disc first through internal detail, red X second, earlier discs/arrows third. Slightly competitive but linear.

### C8. Reuse

**COMPOSITIONAL REUSE** of O01/E01; new state chain and gag-specific cracks/text.

### C9. DNA

Flat yellow modules, black directional arrows, sparse shake marks, hand-written onomatopoeia, coral verdict X.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn sequence on a pure white field with a thin uneven black horizon at mid-height. Arrange exactly four equal saturated-yellow circles from far left to far right: first above-left, second descending toward the line, third resting on the line with two small black vibration marks, and fourth resting at far right with several jagged black cracks across its face. Connect each state with a small black arrow pointing right. Add a loose coral-red X above the right half and the tiny irregular black handwritten sound label `BRU-WAAK` just above the cracked disc. Preserve equal circle size, flat fills, no gray discs, no scenery, no shadows, and abundant negative space.

### C11. Text

**BAKE:** NO preferred. Overlay exact `BRU-WAAK` above final disc; uppercase/irregular black. Red X/vector separate.

### C12. Lock

Four yellow discs; final cracked; arrows rightward; one X; exact sound label; horizon fixed; no fragments leaving frame.

### C13. QC

Subject/state High; composition High; scale High; perspective High; color High; text Medium–High overlay; negative space High; continuity High; risk Low.

### C14. Animation

Disc states reveal left-to-right; third shakes with small amplitude; final develops cracks; sound label/X appear after crack.

### C15. Static

Horizon, camera, background, earlier disc states after reveal.

### C16. Why

Only the current state moves, keeping causality readable. Camera or background motion would make the gag noisy.

### C17. Conflict

Arrows and shake marks support the requested direction/motion.

### C18. Sequence

First disc → second → third reaches line/shakes → fourth appears/cracks → `BRU-WAAK` → red X → hold.

### C19. Method

**C/E — VECTOR MOTION plus replacement drawings.** Use shape duplication and crack stroke reveals.

### C20. AI suitability

**LOW–MEDIUM.** Cracking can be organic, but exact count/text/arrows are deterministic.

### C21. Build

Sun symbol duplicates; arrow trim paths; wiggle limited to third/fourth; crack strokes; label; X. Recreation method—original software not verified.

### C22. First/last frame

**NO** for preferred vector workflow; optional for an AI crack morph.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Reveal four equal yellow sun states left-to-right with arrows. Let the third shake briefly; crack the fourth with jagged black lines, then reveal ‘BRU-WAAK’ and the red X. Keep earlier states and the horizon fixed.”  
**CHARACTER COUNT:** 229 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; composite exact label/X in editor.

### C25. Edit out

Replacement at 00:21.083 to V09. Continuity: yellow disc and horizon remain as the explanatory vocabulary.

### C26. Rule

**RECONSTRUCTION RULE:** Escalate a gag through discrete state copies, not chaotic full-scene animation.

---

## V09 — 00:21.083–00:25.417

**SHOT:** S07  
**SOURCE:** 00:24.750 — [keyframe](keyframes/V09_0024750ms.jpg)  
**DURATION:** 4.333 s

### C1. Viewer sees

Three equal sun states cross the horizon: yellow above-left, a half-yellow/half-gray disc touching the line at center, and a yellow disc rising above-right with a large coral X drawn over it. Small arrows show down then up. Literal: **the sun touches the horizon and rises again, so the final state is crossed out.**

### C2. Sync

**Words:** “If the sun touches the horizon and then it lifts back up, the sunset is disqualified.” **Appears:** exactly across the trajectory. **Trigger:** “touches,” “lifts back up,” “disqualified.” **Motion:** down to contact, then up; X lands on “disqualified.”

### C3. Change

Four-disc crack gag replaced by a three-state down/up trajectory; gray contact fill and crossed final disc added.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** Removes the “graze and rise” loophole.

### C5. Map

Horizon; three discs x≈8%, 48%, 86%; arrows down/right and up/right; X over final. Static frame: horizon. Hero: rising final sun/X.

### C6. Layout

Trajectory creates a shallow V. Discs equal size; center straddles line. Eye path left → center → crossed right.

### C7. Attention

Crossed yellow disc first, center half-gray state second, left start/arrows third. Controlled.

### C8. Reuse

**COMPOSITIONAL REUSE** of horizon/sun modules; new V-shaped path.

### C9. DNA

Flat symbols, black arrows, red verdict, orthographic geometry, no text.

### C10. Prompt

Create a 720×1280 vertical hand-drawn explainer diagram on pure white. Draw one thin uneven black horizon across mid-frame. Place exactly three equal black-outlined sun circles in a shallow V-shaped sequence: a fully yellow disc above the line at far left; a disc at center straddling the horizon with yellow upper half and medium-gray lower half; and a fully yellow disc rising above the line at far right. Draw a small black arrow down-right from the first to the center and another up-right from the center to the final disc. Draw a large loose coral-red X directly over the final right disc. Preserve equal size, flat fills, empty background, and no labels or scenery.

### C11. Text

None.

### C12. Lock

Three discs only; V path; center half gray; right disc yellow and crossed; horizon/camera fixed.

### C13. QC

All match dimensions High; text N/A; risk Low.

### C14. Animation

One conceptual sun moves down/right to contact, then up/right; motion may leave frozen state copies; X draws last.

### C15. Static

Horizon, background, camera, earlier state copies after they appear.

### C16. Why

The reversal itself is the rule violation. Moving the horizon would obscure that the sun reversed relative to a fixed boundary.

### C17. Conflict

Arrows support down-then-up motion; no conflict.

### C18. Sequence

Left sun → descend to center contact → rise to right → red X → hold → replacement.

### C19. Method

**C — VECTOR MOTION GRAPHICS.** Position path, optional state duplication, fill split, trim X.

### C20. AI suitability

**LOW.** Deterministic path and color state are critical.

### C21. Build

Horizon; sun symbol; motion path; duplicate state holds; arrows; X. Recreation method—original software not verified.

### C22. First/last frame

**NO.** One vector path is sufficient.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Move the yellow sun down-right until it touches the fixed horizon, then lift it up-right. Leave equal state copies at start and contact; draw the final red X over the risen sun. Keep all anchors still.”  
**CHARACTER COUNT:** 216 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors preferred.

### C25. Edit out

Replacement at 00:25.417 to V10 on “nearby hill.” Continuity: left sun and horizon persist; mountain is introduced.

### C26. Rule

**RECONSTRUCTION RULE:** When the rule concerns direction reversal, visualize the complete path and freeze its critical states.

---

## V10 — 00:25.417–00:31.417

**SHOT:** S08  
**SOURCE:** 00:30.750 — [keyframe](keyframes/V10_0030750ms.jpg)  
**DURATION:** 6.000 s

### C1. Viewer sees

A jagged black mountain/hill contour spans the middle of the white frame. A yellow sun remains above-left. A gray disc sits partly behind/below the mountain center; a yellow sun reappears above-right but is crossed with a coral X. A final gray disc below the baseline at lower-right is reached by a black arrow, representing the idealized horizon end state. Literal: **a mountain can hide and reveal the sun, but only the later below-horizon state counts.**

### C2. Sync

**Words:** “For a sunset to count, the sun also can’t just disappear behind a nearby hill. It needs to set behind the idealized horizon.” **Appears:** across two clauses. **Triggers:** “hill” introduces contour; “idealized horizon” adds final below-line gray state. **Function:** distinguish obstruction from geometric setting.

### C3. Change

V-shaped sun path replaced by mountain system; hill contour and final ideal-horizon arrow/state added; invalid reappearance crossed.

### C4. Purpose

**ESSENTIAL / EXPLANATORY / COMPARISON.** Without it, a key measurement ambiguity remains.

### C5. Map

White field; baseline y≈50%; mountain x≈20–80%; sun states left/center/right/lower-right; hero is contrast between crossed reappearance and final gray below-horizon state.

### C6. Layout

Left yellow x≈5–25%, y≈31–48%; mountain band x≈20–82%, y≈39–53%; center gray x≈39–61%, y≈45–61%; right crossed yellow x≈75–95%, y≈32–49%; final gray x≈73–94%, y≈56–73%. Eye path left→behind hill→crossed right→final gray.

### C7. Attention

Crossed yellow first, mountain/center gray second, final arrow/gray third. Moderate but controlled competition.

### C8. Reuse

**COMPOSITIONAL REUSE** of E01/O01/O02/G01; O07 mountain and final state added.

### C9. DNA

Simple black contour, flat discs, one red verdict, black causal arrows, no geographic detail or perspective.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn diagram on pure white. Draw a thin uneven black horizon at mid-height and a simple jagged mountain range rising across the central 60% of the frame. Arrange four equal sun states: a full saturated-yellow disc above-left before the mountains; a medium-gray disc partially hidden behind the central peaks and extending below the horizon; a full yellow disc reappearing above-right with a large coral-red X drawn over it; and a full medium-gray disc below the horizon at lower-right. Connect the states with small black directional arrows, including a final down-right arrow from the crossed reappearance toward the below-horizon gray disc. Preserve exact count, equal scale, sparse flat style, no landscape fill, no text, shadows, or extra objects.

### C11. Text

No text in frame; optional editor label “idealized horizon” would be a redesign, not source-faithful.

### C12. Lock

Mountain is outline-only; four states; right yellow crossed; final gray below line; arrows; locked camera; no filled terrain.

### C13. QC

Subject/state High; composition High; scale High; perspective High; color High; text N/A; negative space High; continuity High; risk Low.

### C14. Animation

Sun travels behind mountain, is occluded, reappears and gets crossed, then path continues to final below-horizon state.

### C15. Static

Mountain, horizon, camera, background, and previously revealed state copies stay fixed.

### C16. Why

Occlusion is the concept. A static mountain provides the comparison reference; camera motion would make disappearance ambiguous.

### C17. Conflict

Mountain occlusion and arrows imply the requested left-to-right/downward trajectory; no conflict.

### C18. Sequence

Left sun → moves behind mountain/gray occluded state → reappears yellow right → red X → descends to final gray below ideal horizon → hold → cut.

### C19. Method

**C — VECTOR MOTION GRAPHICS** with mask/track matte for mountain occlusion.

### C20. AI suitability

**LOW.** Exact occlusion and state preservation require deterministic masks.

### C21. Build

Mountain/horizon paths; sun symbol; mountain matte; state duplicates; arrows; X. Use position, fill switch, mask, trim paths. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Masked editor path is more accurate.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Move the yellow sun left-to-right behind the fixed mountain mask. Show a gray hidden state, let it reappear yellow and draw a red X, then continue down to a final gray state below the horizon. Keep prior states fixed.”  
**CHARACTER COUNT:** 232 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; use AI only as a rough alternative and composite exact arrows/X separately.

### C25. Edit out

Hard cut at 00:31.417 to V11 on the new claim about Earth’s surface speed. Conceptual continuity: horizon mechanics scale up to a globe.

### C26. Rule

**RECONSTRUCTION RULE:** Use a static occluder and state copies to distinguish apparent disappearance from true threshold crossing.

---

## V11 — 00:31.417–00:35.800

**SHOT:** S09  
**SOURCE:** 00:34.500 — [keyframe](keyframes/V11_0034500ms.jpg)  
**DURATION:** ~4.383 s

### C1. Viewer sees

A gray Earth floats centered on a charcoal vertical gradient. Bright white sunlight clips the far-left edge. The globe shows gray continents, `W` and `E`, a narrow bright vertical band bordered by coral dashed lines, and a white callout `SUNSET ZONE`. A coral arrow and `1000 km/h` label run eastward around the globe. Literal: **a globe diagram marks a narrow sunset band and eastward surface speed.**

### C2. Sync

**Words:** “At London’s latitude, the Earth’s surface is moving from west to east at about a thousand kilometers per hour.” **Trigger:** “west to east” / “thousand.” **Motion:** band, arrow and label draw during the phrase. **Function:** establish the velocity to cancel.

### C3. Change

White hill diagram removed; dark E03, O03 globe, side light, cardinal labels, sunset band and speed annotation added.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** It scales the horizon model to planetary motion.

### C5. Map

Charcoal background; left-edge light; globe x≈35–78%, y≈30–57%; W/E flank globe; sunset band near x≈58%; speed arrow across lower globe. Hero: coral speed arrow/band; anchor: globe.

### C6. Layout

Globe occupies ~43% width; generous dark space above/below. Eye path white edge light → globe → sunset zone → 1000 km/h arrow.

### C7. Attention

Globe/bright band first, red arrow second, label third. Clean.

### C8. Reuse

**NEW BASE IMAGE** E03/O03/G02; later modified in V12.

### C9. DNA

Hand-drawn gray globe, soft charcoal vignette, side-clipped white sun, narrow warm boundary, white/coral handwriting, orthographic conceptual camera.

### C10. Prompt

Create a 720×1280 vertical hand-drawn planetary explainer. Use a charcoal-gray background with a soft vertical light gradient and a bright white solar glow clipped at the far-left edge. Center a medium gray Earth slightly above mid-frame, outlined in irregular black, with simplified light/dark gray continents. Mark `W` left of the globe and `E` right in small white hand lettering. Draw a narrow vertical sunset band down the globe, bordered by two thin coral dashed lines with a warm center, and label it `SUNSET ZONE` in white above with a curved pointer. Across the lower-middle latitude, add a coral eastward curved arrow labeled `1000 km/h`. Preserve the small centered globe, dark negative space, flat drawn geography, and no stars, vehicles, or extra labels.

### C11. Text

**BAKE:** NO. Overlay exact `W`, `E`, `SUNSET ZONE`, `1000 km/h`; white except coral speed label/arrow.

### C12. Lock

One globe; light left; W left/E right; vertical sunset band; one eastward speed arrow; fixed camera/background.

### C13. QC

Subject High; composition High; scale High; perspective Medium–High; lighting High; color High; text High overlay; negative space High; continuity High.

### C14. Animation

Sunset band brightens; dashed borders and eastward arrow draw; `1000 km/h` appears. Optional slow globe rotation only if directly matching adjacent frames.

### C15. Static

Camera, background gradient, left solar glow, globe position, cardinal labels.

### C16. Why

Arrow/band carry new information. Spinning the whole globe aggressively would compete with the numerical relationship.

### C17. Conflict

Arrow implies eastward motion; request agrees.

### C18. Sequence

Globe/light → sunset band/dashes → W/E → eastward arrow → `1000 km/h` → hold.

### C19. Method

**C/F — VECTOR MOTION GRAPHICS with 2.5D globe texture.**

### C20. AI suitability

**LOW–MEDIUM.** Subtle globe motion is possible; exact labels/band need deterministic layers.

### C21. Build

Gradient; globe precomp; continent mattes; band/dashes; labels; trim-path arrow. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive vector reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Brighten the narrow sunset band on the fixed globe, draw its dashed coral borders, then draw one eastward coral arrow and reveal ‘1000 km/h’. Keep the globe position, W/E labels, side light and background fixed.”  
**CHARACTER COUNT:** 226 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; composite all exact labels after any generated globe motion.

### C25. Edit out

Continue into V12 without cut as the airplane solution is added. Same globe is the continuity device.

### C26. Rule

**RECONSTRUCTION RULE:** When scaling up an explanation, keep the globe small and animate only the measured band and velocity vector.

---

## V12 — 00:35.800–00:42.917

**SHOT:** S09  
**SOURCE:** 00:41.750 — [keyframe](keyframes/V12_0041750ms.jpg)  
**DURATION:** ~7.117 s

### C1. Viewer sees

The same dark globe now carries small airplane icons and coral looping/latitude paths. A plane follows a westward route near the sunset band; curved red arrows wrap around the upper/lower hemispheres. White `OH NO!` appears near the plane, while `1000 km/h` remains. Literal: **an airliner chases the sunset around the globe until a constraint interrupts it.**

### C2. Sync

**Words:** “So if you fly west… arbitrarily long sunset. Or at least… until you run out of fuel 15 or 20 hours in.” **Triggers:** “fly west,” then “run out of fuel.” **Motion:** plane travels path; `OH NO!`/caveat appears at the reversal. **Function:** prove principle, then cap it.

### C3. Change

Airplane(s), wraparound route arrows and caveat label added to V11; globe/band persist.

### C4. Purpose

**EXPLANATORY / MICRO-PAYOFF / REVERSAL.** It gives the intuitive solution and immediately shows why it is outside the road problem.

### C5. Map

Globe anchor; route arcs wrap across right/upper regions; small aircraft near upper hemisphere; `OH NO!` near center. Motion hero: plane; static anchor: globe/band.

### C6. Layout

Globe x≈35–78%, y≈30–57%; plane/icons <8% width; route arrows hug globe curves. Eye path plane → route → sunset band → caveat.

### C7. Attention

Moving plane first; coral routes second; `OH NO!` third. Controlled despite multiple arcs because globe contains them.

### C8. Reuse

**MODIFIED REUSE** V11. Added O05, route paths and caveat text.

### C9. DNA

Same E03; tiny repeated transport icons; coral geographic arcs; white hand notes; left-edge solar glow.

### C10. Prompt

Create a 720×1280 vertical hand-drawn globe explainer on a charcoal gradient with a bright white sun glow clipped at the left edge. Center the same small gray Earth with simplified continents, W/E labels, narrow vertical coral-dashed `SUNSET ZONE`, and the existing `1000 km/h` annotation. Add several tiny black-and-gray commercial airplane icons at different latitudes on the globe’s left-to-upper arc. Draw thin coral curved arrows wrapping westward around the globe, converging toward the sunset band and continuing across visible latitudes. Place the small white handwritten caveat `OH NO!` near the upper-center aircraft. Preserve exact globe position/scale, sparse dark negative space, flat diagram style, and do not add clouds, photorealism, contrails, or extra text.

### C11. Text

Overlay `SUNSET ZONE`, `1000 km/h`, `OH NO!`; if `15–20 h` is added, match the exact source frame where visible rather than inventing placement.

### C12. Lock

Globe/band/side light fixed; tiny aircraft only; coral paths follow globe; no camera orbit; no fuel explosion.

### C13. QC

Objects High; composition High; scale High; perspective Medium; lighting/color High; text High overlay; continuity High; risk Medium for globe geometry.

### C14. Animation

Aircraft travels westward along a curved path; route strokes draw; caveat appears at stop/limit. Other paths may reveal sequentially.

### C15. Static

Globe, band, W/E, background, side light, already drawn routes.

### C16. Why

Plane is the causal variable. Globe motion is unnecessary because the route already shows relative travel; extra motion would obscure speed comparison.

### C17. Conflict

Curved arrows imply wraparound westward travel; requested motion agrees.

### C18. Sequence

V11 → plane enters route → westward path draws → additional arcs reinforce arbitrary duration → caveat/`OH NO!` → hold → cut.

### C19. Method

**C/F — vector paths on 2.5D globe.** Motion-path parenting and trim paths.

### C20. AI suitability

**LOW.** Precise route/label geometry matters.

### C21. Build

Reuse V11 comp; add plane precomp, motion path, route strokes, caveat label. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Motion path is deterministic.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Move the small airliner westward along the globe’s curved sunset path while coral route arrows draw behind it. Stop near the band and reveal ‘OH NO!’ for the fuel limit. Keep the globe, band, W/E labels and side light fixed.”  
**CHARACTER COUNT:** 239 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; AI only for a subtle plane glide, with exact routes/text composited separately.

### C25. Edit out

Hard cut at 00:42.917 to V13 on “as far north… as possible.” Continuity: globe remains, but expands and shifts to a polar grid.

### C26. Rule

**RECONSTRUCTION RULE:** Let a moving icon demonstrate the tempting solution, then stop it with one visible constraint label.

---

## V13 — 00:42.917–00:49.875

**SHOT:** S10  
**SOURCE:** 00:48.750 — [keyframe](keyframes/V13_0048750ms.jpg)  
**DURATION:** 6.958 s

### C1. Viewer sees

A large gray wireframe globe fills most of the white frame. Longitudes/latitudes converge toward the upper pole. Several tiny airplanes sit on a diagonal poleward line, with red horizontal arrows of decreasing circumference leading toward a small orange-red `SUNSET ZONE` near the top-right of the globe. Literal: **aircraft at progressively higher latitudes traverse shorter circles toward a polar sunset zone.**

### C2. Sync

**Words:** “The closer we are to the pole, the easier it is to keep up with the sun.” **Trigger:** “closer… pole.” **Motion:** aircraft/path copies progress upward; shorter red arrows demonstrate reduced distance/speed. **Function:** geometric intuition.

### C3. Change

Dark background removed; globe enlarged/regridded on white; multiple poleward aircraft and shrinking latitude arrows added.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** Makes the latitude argument visible without equations.

### C5. Map

White field; globe x≈1–99%, y≈22–88%; pole/sunset zone upper-right; diagonal aircraft chain lower-left→upper-center; red horizontal arrows. Hero: shrinking path lengths.

### C6. Layout

Globe dominates; aircraft remain tiny; red paths are longest near equator and shortest near pole. Eye path lower-left plane → successive planes → sunset zone.

### C7. Attention

Red arrows/plane chain first, label second, gray grid third. Clean.

### C8. Reuse

**NEW BASE/COMPOSITIONAL REUSE** of O03/O05 concept; geometry is rebuilt as a wireframe globe.

### C9. DNA

Dense gray grid kept subordinate, black outline, tiny black vehicles, red/orange route accents, white background, no shadows.

### C10. Prompt

Create a 720×1280 vertical hand-drawn scientific explainer on white. Draw one very large gray wireframe globe occupying almost the full width and central two-thirds of the frame, with irregular black outer edge, dark gray longitude and latitude grid lines, and a view tilted so meridians converge near an upper-right pole. Along a diagonal path from lower-left toward that pole, place five tiny black-and-gray commercial airplane icons at progressively higher latitudes. At each latitude draw a thin coral-red eastward curved arrow, longest near the bottom and progressively shorter toward the pole. Mark a small orange-red cap/path near the upper pole and label it `SUNSET ZONE` in black handwritten uppercase with a pointer. Preserve white negative space outside the globe, exact decreasing path hierarchy, and no extra geography or labels.

### C11. Text

Overlay exact `SUNSET ZONE` above upper-right globe.

### C12. Lock

One large grid globe; five small aircraft; decreasing red arrows; polar zone upper-right; camera locked; no globe spin.

### C13. QC

Objects High; composition High; scale High; perspective Medium–High; color High; text High overlay; continuity High; risk Medium in grid fidelity.

### C14. Animation

Aircraft/arrow pairs reveal from low to high latitude; red arrows shorten with each step; final sunset-zone callout appears.

### C15. Static

Globe/grid/camera/background; previously revealed planes/arrows.

### C16. Why

Progressive path shortening communicates the proposition directly. Rotating the globe would make length comparison harder.

### C17. Conflict

Aircraft orientation/arrows support poleward reveal and eastward paths; no conflict.

### C18. Sequence

Globe → lowest plane/long arrow → successive higher planes/shorter arrows → polar sunset zone label → hold.

### C19. Method

**C/G — vector motion on a simple 3D or 2.5D globe.**

### C20. AI suitability

**LOW.** Exact grid, icon count and comparative path lengths matter.

### C21. Build

Globe grid precomp; five plane icons; five trim-path arrows; pole highlight; label. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive reveal is safer.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Reveal airplane-and-arrow pairs from low to high latitude on the fixed wireframe globe. Each new coral path is shorter than the one below. End by highlighting and labeling the upper ‘SUNSET ZONE’. Keep prior pairs still.”  
**CHARACTER COUNT:** 235 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; composite grid and exact labels deterministically.

### C25. Edit out

Hard cut at 00:49.875 to V14 on “no paved roads anywhere near either pole.” Continuity: polar concept becomes a literal polar landscape.

### C26. Rule

**RECONSTRUCTION RULE:** Explain a quantitative trend with repeated icons and visibly shrinking paths, not extra narration alone.

---

## V14 — 00:49.875–00:53.292

**SHOT:** S11  
**SOURCE:** 00:52.500 — [keyframe](keyframes/V14_0052500ms.jpg)  
**DURATION:** 3.417 s

### C1. Viewer sees

A navy polar-twilight landscape fills the frame. `NORTH POLE, 90°N` appears large in white across the top. An orange-white sun sits at the far-left horizon; two seals lie in the dark foreground; a small boxy road vehicle is stranded far-right on rough ice. Literal: **the North Pole is shown as a dark roadless landscape with seals and a distant vehicle.**

### C2. Sync

**Words:** “Unfortunately, there are no paved roads anywhere near either pole.” **Trigger:** “no paved roads.” **Motion:** mostly static; the cut itself is the emphasis. **Function:** eliminate the intuitive polar solution.

### C3. Change

White globe replaced by E04; location title, seals, terrain, left sun and truck added.

### C4. Purpose

**ESSENTIAL / EVIDENTIAL-ILLUSTRATIVE / PATTERN INTERRUPT.** Converts an abstract constraint into a concrete scene.

### C5. Map

Navy sky; title top; sun left horizon; seals lower-left/center; terrain/vehicle right. Hero: title and roadless separation.

### C6. Layout

Title x≈10–90%, y≈8–18%; sun x≈0–12%, y≈54–62%; vehicle x≈68–95%, y≈48–58%; seals x≈8–48%, y≈58–78%. Eye path title → sun/empty span → vehicle/seals.

### C7. Attention

Title first, bright sun second, vehicle/seals third. Controlled.

### C8. Reuse

**NEW BASE IMAGE** E04; later modified into V15–V17.

### C9. DNA

Deep indigo/navy sky, low orange glow, thin black contour silhouettes, sparse stars, large white hand title, restrained detail.

### C10. Prompt

Create a 720×1280 vertical hand-drawn polar twilight illustration. Use a deep navy and violet sky with a soft blue vertical glow near the left horizon and only a few tiny white stars. Draw a thin black horizon across the lower-middle. Place a small bright white-yellow setting sun at the far-left edge with a restrained orange-red halo. In the lower-left foreground, draw two simple gray seals outlined in black, one larger and closer, both lying on dark ice. At far-right, place a tiny boxy gray snow/road vehicle on a rough black ice contour, separated from the sun by a large empty span. Leave clear space across the top for the location title. Preserve the flat hand-drawn style, dark palette, no paved road markings, no people, and no photorealistic snow.

### C11. Text

**BAKE:** NO. Overlay `NORTH POLE, 90°N` in large white hand-drawn uppercase across upper frame.

### C12. Lock

Two seals; one boxy vehicle far-right; one sun far-left; no paved road; title exact; camera/background fixed.

### C13. QC

Subject High; composition High; scale High; perspective Medium; lighting/color High; text High overlay; negative space High; continuity High.

### C14. Animation

No necessary motion; optional tiny vehicle idle or star shimmer is not source-critical.

### C15. Static

Entire landscape/title/camera remain still to emphasize geographic impossibility.

### C16. Why

The spatial emptiness is the message. Environmental motion would romanticize rather than clarify the road constraint.

### C17. Conflict

No motion cues; requested stillness agrees.

### C18. Sequence

Hard cut to full North Pole plate → title holds → gradual location replacement begins near 00:53.292.

### C19. Method

**A/K — static illustration with deterministic title.**

### C20. AI suitability

**MEDIUM** for the painted plate; low for exact title/object count.

### C21. Build

Sky/glow; sun; horizon/terrain; seals; vehicle; title. Recreation method—original software not verified.

### C22. First/last frame

**NO** for this state; location transition into V15 can use cross-replacement layers.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the North Pole title, left-edge sun, two seals, distant boxy vehicle, ice horizon and navy sky completely still.”  
**CHARACTER COUNT:** 132 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; composite title after plate generation.

### C25. Edit out

Animated location replacement at ~00:53.292 to V15: title morphs, seals/ice simplify, hatchback and mountain line replace polar objects. Twilight palette persists.

### C26. Rule

**RECONSTRUCTION RULE:** Let geographic emptiness—not extra explanatory clutter—communicate an infrastructure constraint.

---

## V15 — 00:53.292–00:59.750

**SHOT:** S12  
**SOURCE:** 00:58.750 — [keyframe](keyframes/V15_0058750ms.jpg)  
**DURATION:** ~6.458 s

### C1. Viewer sees

The same twilight palette now reads `LONGYEARBYEN, 78°N` at top. The sun remains at far-left horizon; a gray hatchback sits right-of-center before a black mountain outline. Near the sun, a small black brace/curved mark and `~55 min` label quantify the benchmark. Literal: **a car in Longyearbyen faces a left-edge sunset lasting about 55 minutes.**

### C2. Sync

**Words:** “The closest road that qualifies is probably in Longyearbyen… The longest sunset there lasts just under an hour.” **Triggers:** location name and duration. **Motion:** title/location objects replace North Pole; `~55 min` appears near the end. **Function:** establish achievable benchmark.

### C3. Change

Title changes; seals/truck removed; road/hatchback/mountain added; `~55 min` appears. Twilight/sun/camera persist.

### C4. Purpose

**ESSENTIAL / EVIDENTIAL / MICRO-PAYOFF.** Supplies the comparator for the final result.

### C5. Map

Title top; sun far-left; car x≈62–94%, y≈52–61%; mountain right; duration near x≈4–25%, y≈50%. Hero: `~55 min`; anchor: horizon.

### C6. Layout

Large empty space between sun and car; location title spans upper width. Eye path title → sun/55 → car.

### C7. Attention

Title first, sun/duration second, car third. Controlled.

### C8. Reuse

**MODIFIED REUSE** of V14; palette/horizon/sun retained, location assets replaced.

### C9. DNA

E04 twilight, white hand location title, gray outlined hatchback, thin mountain silhouette, black duration label.

### C10. Prompt

Create a 720×1280 vertical hand-drawn Longyearbyen twilight illustration. Use the same deep navy-violet sky, sparse stars, soft blue/orange glow and thin black horizon as the North Pole frame. Place one small white-yellow sun at the far-left horizon with an orange-red halo. Draw a compact gray hatchback with irregular black outline on the road at right-of-center, facing left, with a low black mountain contour behind it. Leave a wide empty dark interval between sun and car. Near the sun, reserve space for a small black `~55 min` duration annotation and curved measuring mark. Keep the lower half dark navy, the upper title area clear, and do not add seals, snow truck, streetlights, buildings, photorealism, or extra vehicles.

### C11. Text

Overlay `LONGYEARBYEN, 78°N` large in white at top; `~55 min` small black near left horizon.

### C12. Lock

One hatchback; one left sun; one mountain outline; exact title/duration; fixed horizon/camera; no visible road detail beyond line.

### C13. QC

Subject High; composition High; scale High; perspective Medium; lighting/color High; text High overlay; negative space High; continuity High.

### C14. Animation

Location title/assets replace V14; `~55 min` draws/reveals after car/road settle. Car itself mostly static.

### C15. Static

Sun, horizon, sky, car after replacement, camera.

### C16. Why

The number is the information hero; keeping car/sun fixed turns duration into the new variable.

### C17. Conflict

Car may have subtle motion lines later, but this benchmark frame implies a parked/held car; stillness agrees.

### C18. Sequence

North Pole elements replace → Longyearbyen title → car/mountain settle → `~55 min` appears → hold.

### C19. Method

**K — static illustration + editor replacement/text.**

### C20. AI suitability

**MEDIUM** for location plate; low for exact title/number.

### C21. Build

Reuse sky/sun; swap foreground assets; add title and duration overlay. Recreation method—original software not verified.

### C22. First/last frame

**YES** only for V14→V15 location morph; preferred method is layered cross-replacement.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Replace the North Pole foreground with the Longyearbyen road, right-side hatchback and mountain line while keeping the twilight sky and left sun fixed. Change the title, then reveal ‘~55 min’ by the sun.”  
**CHARACTER COUNT:** 218 / 500  
**STATUS:** PASS

### C24. Adapter

For first/last-frame AI, supply V14/V15 clean plates without text; add exact titles in editor.

### C25. Edit out

Continue into V16; `~55 min` is replaced by `WEST` as the strategy changes, while car/sun remain.

### C26. Rule

**RECONSTRUCTION RULE:** Preserve the atmosphere and coordinate frame when replacing a failed location with the best qualifying benchmark.

---

## V16 — 00:59.750–01:02.875

**SHOT:** S12  
**SOURCE:** 01:01.750 — [keyframe](keyframes/V16_0061750ms.jpg)  
**DURATION:** ~3.125 s

### C1. Viewer sees

The Longyearbyen title has disappeared. `WEST` appears in black near the left sun. The hatchback remains on the right with black speed lines behind it, pointing left/west across the fixed horizon. Literal: **a car attempts to chase the sunset westward.**

### C2. Sync

**Words:** “In general, driving west to keep up with the sun isn’t a viable strategy.” **Trigger:** “driving west.” **Motion:** speed lines/car imply westward travel; `WEST` replaces duration. **Function:** introduce failed strategy.

### C3. Change

Location title and `~55 min` removed; `WEST` and car speed lines added; car/sun/horizon persist.

### C4. Purpose

**EXPLANATORY / TRANSITION.** Converts benchmark scene into a velocity test.

### C5. Map

Sun/`WEST` left; moving car right; mountain/horizon anchor; large gap emphasizes chase distance.

### C6. Layout

`WEST` x≈5–24%, y≈48%; sun x≈0–12%, y≈54%; car x≈62–95%, y≈51–61%. Eye path WEST/sun → car/speed lines.

### C7. Attention

Moving car first, `WEST`/sun second, mountain third. Clean.

### C8. Reuse

**TEXT/GRAPHIC MODIFICATION** of V15.

### C9. DNA

Same twilight plate; black hand label; restrained speed lines; no camera move.

### C10. Prompt

Create a 720×1280 vertical hand-drawn twilight chase diagram. Use a deep navy-violet sky with sparse stars, a small white-yellow sun glowing at the far-left horizon, a thin black road/horizon line, and a low black mountain silhouette at right. Place one compact gray hatchback at right-of-center facing left, with several short thin black horizontal speed lines trailing behind its right side. Leave a wide empty span between car and sun. Reserve space immediately above the sun for the black handwritten uppercase label `WEST`. Preserve the flat outlined car, dark lower field, fixed front-on camera, and no location title, duration label, extra vehicles, road markings, or scenery.

### C11. Text

Overlay `WEST` in black hand uppercase above/left of sun.

### C12. Lock

One left sun; one left-facing hatchback right; speed lines only behind car; one WEST label; fixed sky/horizon.

### C13. QC

Subject High; composition High; scale High; perspective Medium; lighting/color High; text High; continuity High.

### C14. Animation

Car translates slightly left or holds with looping speed lines; `WEST` appears. Camera and sun remain fixed.

### C15. Static

Sun/horizon/mountain/sky/camera.

### C16. Why

Relative car motion tests the strategy; moving the sun or camera would obscure the failed speed comparison.

### C17. Conflict

Speed lines support west/leftward motion; request agrees.

### C18. Sequence

`~55 min` disappears → `WEST` appears → car speed lines activate → map/speed proof enters V17.

### C19. Method

**B/C — editor keyframes/vector speed lines.**

### C20. AI suitability

**MEDIUM–LOW.** Car glide is simple; exact label/layout deterministic.

### C21. Build

Reuse V15; animate car x-position a few percent; loop speed lines; replace text. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Simple keyframes.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. The right-side hatchback drives slightly left toward the fixed sunset with short speed lines trailing behind it. Reveal ‘WEST’ above the sun. Keep the horizon, mountain silhouette, sky and sun stationary.”  
**CHARACTER COUNT:** 219 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; text in editor.

### C25. Edit out

Additive transition to V17 near 01:02.875 as a circular Scandinavia inset appears above and `355 mph` later labels the car.

### C26. Rule

**RECONSTRUCTION RULE:** Show chasing speed as vehicle motion against an absolutely fixed sun/horizon reference.

---

## V17 — 01:02.875–01:08.417

**SHOT:** S12  
**SOURCE:** 01:07.750 — [keyframe](keyframes/V17_0067750ms.jpg)  
**DURATION:** ~5.542 s

### C1. Viewer sees

The westward car/sun scene remains below. A large circular gray Scandinavia map inset appears in the upper half with a small coral point near northern mainland Norway. `WEST` remains left; `355 mph` appears in white near the car at right. Literal: **a northern-Norway map and 355 mph label prove westward driving is impractical.**

### C2. Sync

**Words:** “Even at the northernmost tip of mainland Norway, you’d have to travel at about half the speed of sound…” **Triggers:** location → map inset; speed claim → `355 mph`. **Function:** quantified failure/proof.

### C3. Change

Circular map inset, coral point and `355 mph` label added; V16 anchors persist.

### C4. Purpose

**EVIDENTIAL / EXPLANATORY / MICRO-PAYOFF.** The number closes the due-west strategy loop.

### C5. Map

Inset x≈20–80%, y≈5–39%; lower car/sun scene y≈45–63%; speed text near car. Hero: `355 mph`; anchor: inset/map and horizon.

### C6. Layout

Top/bottom hierarchy: geography above, physical chase below. Eye path map point → WEST/sun → 355/car.

### C7. Attention

Map point/title-less inset first by scale, `355 mph` second by contrast, moving car third. Controlled.

### C8. Reuse

**ADDITIVE MODIFICATION** of V16; introduces map asset used later.

### C9. DNA

Circular gray map, coral locator dot, white speed text on navy, same hatchback/horizon.

### C10. Prompt

Create a 720×1280 vertical hand-drawn infographic in a deep navy polar-twilight palette. In the lower half, keep a small white-yellow sun at the far-left horizon, black `WEST` label above it, a thin black road line, a low mountain silhouette, and one gray left-facing hatchback at right with short speed lines. Place the exact white handwritten label `355 mph` immediately above/right of the car. In the upper half, add a large black-outlined circular inset containing a simplified light-gray map of Scandinavia on medium-gray water, with one small coral-red dot near the northernmost tip of mainland Norway. Preserve the large gap between inset and road, flat fills, sparse stars, fixed camera, and no extra labels, routes, or vehicles.

### C11. Text

Overlay `WEST` black; `355 mph` white. Keep number exact.

### C12. Lock

Circular map only; one coral dot; one car; one sun; exact speed; no `~55 min`; camera locked.

### C13. QC

Objects High; composition High; scale High; perspective Medium; color High; text High; continuity High; risk Low–Medium.

### C14. Animation

Map inset scales/reveals; coral point pops in; `355 mph` appears; car/speed lines continue subtly.

### C15. Static

Sun, horizon, sky, final inset position, camera.

### C16. Why

Geography and number are added only when spoken; car motion remains secondary. No map rotation is needed.

### C17. Conflict

Car speed lines agree with leftward travel; inset has no motion cue.

### C18. Sequence

V16 chase → inset appears → coral point → `355 mph` → hold → hard cut.

### C19. Method

**C/B — vector/map graphic plus editor keyframes.**

### C20. AI suitability

**LOW** for map/number; medium only for subtle car motion.

### C21. Build

Reuse V16; circular map matte; gray land; coral point; speed overlay. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive layers.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Scale in the circular Scandinavia inset above the chase scene, pop a coral dot onto northern mainland Norway, then reveal ‘355 mph’ beside the car. Keep the sun, horizon, map orientation and final labels fixed.”  
**CHARACTER COUNT:** 225 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; never ask AI to render the exact map/number if deterministic layers are available.

### C25. Edit out

Hard cut at 01:08.417 to V18 on “Luckily, there’s a better approach.” Visual reset to white restores cognitive space.

### C26. Rule

**RECONSTRUCTION RULE:** Close a failed-strategy loop with one locator and one unmistakable number.

---

## V18 — 01:08.417–01:14.292

**SHOT:** S13  
**SOURCE:** 01:13.750 — [keyframe](keyframes/V18_0073750ms.jpg)  
**DURATION:** 5.875 s

### C1. Viewer sees

The white horizon diagram returns. Above the line, five yellow/gray sun states form a symmetric dip: yellow high-left, lower yellow, half-gray at contact, gray below center, then mirrored rising states to yellow high-right. Black arrows connect them; a small coral downward arrow marks the lowest center. C01 stands below-left looking up. Literal: **a presenter watches the sun barely set and rise again around a marked midpoint.**

### C2. Sync

**Words:** “Luckily, there’s a better approach. If you’re in Northern Scandinavia on a day when the sun just barely sets and then rises again…” **Triggers:** “better approach” resets; “sets… rises” builds symmetric path. **Function:** reversal and new model.

### C3. Change

Dark chase scene/map removed; white diagram, presenter, symmetric sun path and center arrow added.

### C4. Purpose

**ORIENTING / ESSENTIAL / PATTERN INTERRUPT.** Reopens solution space after the 355 mph dead end.

### C5. Map

Horizon y≈50%; sun sequence spans full width y≈35–58%; coral midpoint arrow x≈57%; presenter x≈10–28%, y≈56–80%. Hero: center dip; anchor: horizon.

### C6. Layout

Top-half diagram, lower-left presenter, empty lower-right. Eye path left sun chain → center arrow → right rise → presenter.

### C7. Attention

Yellow chain first, gray center/coral arrow second, presenter third. Clean.

### C8. Reuse

**COMPOSITIONAL REUSE** of V03 sun modules and C01/E01; new symmetric trajectory.

### C9. DNA

White flat field; equal circles; yellow/gray threshold coding; thin arrows; anonymous presenter; no labels.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn explainer on pure white. Draw a thin uneven black horizon at mid-height. Above and across it, arrange a symmetric left-to-right sequence of seven equal sun states connected by small black arrows: yellow high-left, yellow lower-left, half-yellow/half-gray at first contact, one fully gray disc centered below the line, then mirrored half-gray and yellow states rising to a yellow disc high-right. Add one small coral-red arrow pointing downward at the lowest center state. Below the horizon at lower-left, draw one featureless black stick presenter with a white oval head looking upward. Preserve equal disc sizes, fixed horizon, empty lower-right, flat fills, no text, shadows, scenery, or extra people.

### C11. Text

None.

### C12. Lock

Symmetric dip; one gray center below horizon; one presenter lower-left; midpoint arrow; camera/horizon locked.

### C13. QC

All dimensions High; text N/A; risk Low.

### C14. Animation

Sun states reveal left-to-right through a dip and rise; midpoint arrow appears at lowest state. Presenter remains still.

### C15. Static

Horizon, camera, presenter, prior sun copies.

### C16. Why

The solar path is the new mechanism. Presenter is a scale/orientation anchor and must not compete.

### C17. Conflict

Arrows imply the correct down-then-up direction.

### C18. Sequence

Presenter/horizon → left descending states → gray midpoint/arrow → rising right states → hold → cut.

### C19. Method

**C — VECTOR MOTION GRAPHICS.**

### C20. AI suitability

**LOW** due exact count/symmetry.

### C21. Build

Sun symbol duplicates; position/fill; arrows; midpoint arrow; presenter layer. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive states.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Reveal equal sun states left-to-right: descend from yellow above the horizon to one gray center state below, then rise symmetrically back to yellow. Add the coral midpoint arrow. Keep the presenter and prior states still.”  
**CHARACTER COUNT:** 236 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors preferred.

### C25. Edit out

Hard cut at 01:14.292 to V19. Conceptual continuity: the solar dip becomes movement of the day-night boundary on a map.

### C26. Rule

**RECONSTRUCTION RULE:** Announce a reversal with a clean symmetric diagram before showing geographic complexity.

---

## V19 — 01:14.292–01:20.125

**SHOT:** S14  
**SOURCE:** 01:19.750 — [keyframe](keyframes/V19_0079750ms.jpg)  
**DURATION:** ~5.833 s

### C1. Viewer sees

A large grayscale Scandinavia map fills the frame. A curved boundary divides light `DAY` above from dark `NIGHT` below. Coral arrows initially point `NW`; after slowing, their direction reverses and the visible final state reads `SW` with three downward coral arrows. Literal: **a curved day-night boundary over Scandinavia reverses from northwest to southwest.**

### C2. Sync

**Words:** “…the day-night line moves northwest, then slows, reverses, and heads back to the southwest.” **Triggers:** each direction word changes the arrow/label. **Function:** explain the exploitable reversal.

### C3. Change

White sun diagram replaced by E05; day/night fills, curved line, direction arrows/labels added.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** This is the core physical mechanism.

### C5. Map

Scandinavia land light gray; lower night region dark gray; curved line across lower-middle; `DAY/NIGHT` near left-center; direction label/arrows near center-right. Hero: coral direction change; anchor: map.

### C6. Layout

Map fills nearly 100%; boundary arcs y≈47–68%; labels sit adjacent. Eye path boundary → NW/SW arrows → DAY/NIGHT regions.

### C7. Attention

Coral arrows first, high-contrast boundary second, gray geography third. Clean.

### C8. Reuse

**NEW BASE MAP** E05, reused V20–V23.

### C9. DNA

Simplified Norway/Sweden/Finland silhouette; two-tone day/night; coral arrows; hand labels; no roads yet.

### C10. Prompt

Create a 720×1280 vertical hand-drawn map of Scandinavia. Use a pale gray background with a simplified medium-gray silhouette of Norway, Sweden and Finland occupying most of the frame. Across the lower-middle draw one broad curved day-night boundary: light gray `DAY` region above, dark charcoal `NIGHT` region below, separated by a clean black arc. Place the small gray handwritten labels `DAY` and `NIGHT` beside the boundary. Near center-right, add three coral-red arrows pointing down-left/southwest and the large coral label `SW`. Preserve the exact map orientation, restrained grayscale hierarchy, flat fills, no car, sunset band, inset, roads, title, or decorative texture.

### C11. Text

Overlay `DAY`, `NIGHT`, and direction state (`NW` then `SW`) as editor layers.

### C12. Lock

Map/orientation fixed; one curved boundary; correct light/dark sides; exact direction label; no car yet.

### C13. QC

Map High; composition High; perspective High; color High; text High overlay; continuity High; risk Low–Medium.

### C14. Animation

Boundary translates/rotates subtly NW, slows to near stop, reverses SW; arrows/label swap accordingly.

### C15. Static

Map geography, camera, light/dark region style, labels after each state.

### C16. Why

The line is the moving information. Moving the map would obscure its direction; surrounding geography must anchor the reversal.

### C17. Conflict

Direction arrows explicitly support the motion; ensure NW first, SW last.

### C18. Sequence

Map/boundary → `NW` arrows/motion → decelerate → reverse → `SW` arrows/motion → hold.

### C19. Method

**C — VECTOR MAP/MOTION GRAPHICS** using a masked curved band and keyframed transform.

### C20. AI suitability

**LOW.** Geography, labels and directional reversal require deterministic control.

### C21. Build

Map land/water layers; boundary path/mattes; DAY/NIGHT labels; direction arrows/text; speed graph easing. Recreation method—original software not verified.

### C22. First/last frame

**YES** only as a planning aid: start NW state, end SW state. Preferred build remains vector.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked map and camera. Move the curved day-night boundary northwest, decelerate to a brief stop, then reverse and move southwest. Change the coral direction arrows and label from NW to SW. Keep Scandinavia and DAY/NIGHT labels fixed.”  
**CHARACTER COUNT:** 233 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; do not rely on generative video for the exact reversal.

### C25. Edit out

No cut: at ~01:20.125 the map reframes and a car becomes the route variable in V20.

### C26. Rule

**RECONSTRUCTION RULE:** When the solution depends on reversal, visibly slow before reversing so the causal change cannot be missed.

---

## V20 — 01:20.125–01:22.125

**SHOT:** S14  
**SOURCE:** 01:21.750 — [keyframe](keyframes/V20_0081750ms.jpg)  
**DURATION:** ~2.000 s

### C1. Viewer sees

The Scandinavia map reframes so a small black/white car icon sits near center. A diagonal curved band enters from lower-right, now explicitly labeled `DAY / SUNSET / NIGHT`; the sunset strip glows muted coral between day and night. Literal: **a car is positioned beside a labeled moving sunset band on the map.**

### C2. Sync

**Words:** “To get a long sunset, the strategy is simple.” **Trigger:** “strategy.” **Motion:** map settles into the actionable coordinate frame; car appears. **Function:** orient the three-step demonstration.

### C3. Change

Map reframed; car, coral sunset strip and three labels added; SW arrows removed.

### C4. Purpose

**ORIENTING / ESSENTIAL / TRANSITION.** Establishes objects before instructions begin.

### C5. Map

Map full frame; boundary band enters lower-right diagonal; car near x≈52%, y≈55%; labels along band right. Hero: car/band; anchor: geography.

### C6. Layout

Car small (~5% width) at center; band spans x≈45–100%, y≈65–100%; ample map field above. Eye path car → sunset label → day/night sides.

### C7. Attention

Car first through isolation, coral band second, labels third. Clean.

### C8. Reuse

**MODIFIED REUSE** V19. Adds O04 and labeled sunset band.

### C9. DNA

Gray map, small white/black car icon, muted coral glow, angled hand labels, front-on map.

### C10. Prompt

Create a 720×1280 vertical hand-drawn grayscale map of Scandinavia with pale-gray background and medium-gray land shapes. Reframe the map so central Norway/Sweden occupies the middle. Place one tiny white car icon with black outline near the center on a faint north-south road. Across the lower-right, draw a broad curved diagonal boundary band: light-gray `DAY` above, a narrow muted-coral glowing `SUNSET` strip in the middle, and dark-charcoal `NIGHT` below. Set the three uppercase labels directly along the band on the right. Preserve the exact car-to-band relationship, map orientation, flat diagram style, and no inset sun sequence, route arrows, extra cars, or direction labels.

### C11. Text

Overlay `DAY`, `SUNSET`, `NIGHT`; align to band angle, gray/white hierarchy.

### C12. Lock

One car; one band; correct layer order day/sunset/night; fixed map orientation; no inset yet.

### C13. QC

Objects High; composition High; perspective High; color High; text High; continuity High.

### C14. Animation

Controlled digital reframe/track settles map; car and band labels appear.

### C15. Static

After settle, map and camera hold briefly; car waits.

### C16. Why

Reframing creates room for the route. Car should not move until the instruction begins.

### C17. Conflict

No motion cues conflict; car is a neutral cursor.

### C18. Sequence

V19 map → smooth reframe → sunset band/labels → car appears → brief hold.

### C19. Method

**B/C — digital map reframe plus vector overlays.**

### C20. AI suitability

**LOW.** Exact map/band/car registration matters.

### C21. Build

Reuse map comp; camera/null reframe; car icon; band mattes; labels. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Deterministic reframe.

### C23. Animation prompt

**ANIMATION PROMPT:** “Smoothly reframe the fixed Scandinavia map until the small car sits near center and the DAY–SUNSET–NIGHT band enters from lower-right. Then lock the camera and hold the car still.”  
**CHARACTER COUNT:** 179 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; editor keyframes preferred.

### C25. Edit out

Continue to V21. Same map/car/band; inset appears when first contact is discussed.

### C26. Rule

**RECONSTRUCTION RULE:** Settle the map and cursor before issuing route instructions.

---

## V21 — 01:22.125–01:26.875

**SHOT:** S14  
**SOURCE:** 01:26.500 — [keyframe](keyframes/V21_0086500ms.jpg)  
**DURATION:** ~4.750 s

### C1. Viewer sees

The map/car/band remain. A small white rectangular inset appears near the upper-right, showing two yellow sun positions descending toward a black mini-horizon. The car waits near the approaching sunset band. Literal: **the driver waits while an inset sun approaches first horizon contact.**

### C2. Sync

**Words:** “Sit in your car until the sun first touches the horizon, which means the day-night line is about to pass you.” **Triggers:** “sit” keeps car static; “first touches” builds inset. **Function:** step 1/timing cue.

### C3. Change

Inset G03 added and begins extending; car/band/map retained.

### C4. Purpose

**ESSENTIAL / EXPLANATORY.** Links local sun appearance to map-boundary position.

### C5. Map

Map/band anchor; car center-lower; inset x≈70–95%, y≈12–31%; two sun states. Hero: inset descent; static anchor: car.

### C6. Layout

Inset occupies <25% width; does not cover car/band. Eye path inset → car → band label.

### C7. Attention

Yellow inset suns first, car second, coral band third. Controlled.

### C8. Reuse

**ADDITIVE MODIFICATION** of V20; inset reuses O01/horizon grammar.

### C9. DNA

Map plus boxed white mini-diagram; same yellow sun modules; black inset outline; sparse layering.

### C10. Prompt

Create a 720×1280 vertical hand-drawn Scandinavia route map with pale-gray field, medium-gray land, one tiny white/black car near center, and the curved diagonal `DAY / SUNSET / NIGHT` band across lower-right with a muted-coral sunset strip. In the upper-right, add a small black-outlined white rectangular inset occupying about one-quarter of the frame width. Inside it, draw a thin black mini-horizon and exactly two equal yellow sun circles descending left-to-right toward the line, connected by one small black arrow. Keep the car stationary just ahead of the band. Preserve map orientation, band labels, empty spacing around the inset, flat fills, and no extra sun states or route arrow yet.

### C11. Text

Overlay band labels only; no inset words.

### C12. Lock

Car still; inset upper-right; two sun states; map/band fixed except measured boundary approach; no route arrow.

### C13. QC

Objects High; composition High; scale High; perspective High; color High; text High; continuity High.

### C14. Animation

Inset frame appears; second sun state reveals; boundary approaches car slowly; car remains still.

### C15. Static

Car, geography, camera, existing labels, previously revealed inset state.

### C16. Why

Boundary and inset sun are synchronized variables; parked car is the reference. Moving it would violate step 1.

### C17. Conflict

Inset arrow supports descent; car has no speed lines, agreeing with stillness.

### C18. Sequence

Inset frame → first/second sun states → boundary nears parked car → hold at imminent contact.

### C19. Method

**C/B — vector inset and keyframed boundary; static car.**

### C20. AI suitability

**LOW.** Cross-diagram synchronization requires deterministic control.

### C21. Build

Reuse V20; inset precomp; two sun modules; boundary transform; car locked. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Layered reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked map and camera. Keep the car parked while the sunset band approaches. In the upper-right inset, reveal two equal yellow sun states descending toward first horizon contact. Keep all labels, geography and prior inset states fixed.”  
**CHARACTER COUNT:** 235 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; editor motion only.

### C25. Edit out

Continue at ~01:26.875 into V22 when narration says “Then drive north.” Inset expands and car begins moving.

### C26. Rule

**RECONSTRUCTION RULE:** Synchronize a small local-view inset with the large map while keeping the driver static until the trigger moment.

---

## V22 — 01:26.875–01:32.000

**SHOT:** S14  
**SOURCE:** 01:31.500 — [keyframe](keyframes/V22_0091500ms.jpg)  
**DURATION:** ~5.125 s

### C1. Viewer sees

The car moves north along the curved sunset band while the map reframes to follow. The upper inset widens and accumulates yellow-to-gray sun states, showing the sun held in a prolonged setting phase. Literal: **a car tracks north just ahead of the sunset boundary as the inset sunset stretches.**

### C2. Sync

**Words:** “Then drive north to stay a little ahead of the line as long as you can…” **Triggers:** “drive north” starts car; “stay ahead” keeps it on day side; “as long as” lengthens inset. **Function:** step 2.

### C3. Change

Car starts; map/camera track; inset widens and gains multiple states; sunset band slides under/behind car.

### C4. Purpose

**ESSENTIAL / EXPLANATORY / ESCALATION.** Demonstrates the winning action.

### C5. Map

Map anchor with controlled reframe; car near center; band under car; inset top spans x≈28–96%, y≈10–28%. Motion hero: car; secondary: newest inset sun.

### C6. Layout

Car kept near center by map tracking; band diagonal; inset horizontal progress strip. Eye path car → band → inset chronology.

### C7. Attention

Moving car first, yellow inset sequence second, coral band third. Controlled.

### C8. Reuse

**MODIFIED REUSE** V21; same assets with longer inset and tracked motion.

### C9. DNA

Map tracking, tiny car cursor, coral band, growing boxed state history, muted gray geography.

### C10. Prompt

Create a 720×1280 vertical hand-drawn Scandinavia route map with pale-gray field, medium-gray land, one tiny white car with black outline near center, and a curved diagonal `DAY / SUNSET / NIGHT` band passing immediately below it. Position the car just on the day-side edge of the muted-coral sunset strip, oriented northward along a faint road. Across the upper frame, add a wide black-outlined white inset containing a left-to-right chain of six equal sun states: yellow above the mini-horizon, yellow descending, half-yellow/half-gray at contact, then gray portions increasing while the disc remains near the line. Link states with small black arrows. Preserve the car-centered map crop, exact band hierarchy, flat gray palette with yellow/coral accents, and no extra vehicles or labels.

### C11. Text

Overlay `DAY`, `SUNSET`, `NIGHT` along band; inset has no wording.

### C12. Lock

One car; remain ahead/day side; inset chronology left→right; map orientation changes only through controlled tracking; no autonomous globe motion.

### C13. QC

Objects High; composition High; scale High; perspective High; color High; text High; continuity High.

### C14. Animation

Car travels north; map layer pans/rotates subtly to hold car near center; boundary follows just behind; inset adds states sequentially.

### C15. Static

Car relative hierarchy to band, inset frame position after expansion, labels, previously added inset states.

### C16. Why

Car is the route variable; map reframe serves tracking, not spectacle. Boundary and inset move only to explain “staying ahead.”

### C17. Conflict

Car orientation/road support northward travel; inset arrows agree left-to-right.

### C18. Sequence

Car starts north → map tracks → boundary remains just behind → inset accumulates prolonged-setting states → approach turn point.

### C19. Method

**C/B — vector map with car motion path and controlled camera/null tracking.**

### C20. AI suitability

**LOW.** Registration and inset counts are exact.

### C21. Build

Map precomp on transform null; car motion path; band matte; inset precomp; labels. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Use keyframes and path constraints.

### C23. Animation prompt

**ANIMATION PROMPT:** “Track the small car north along the map while keeping it near center and just ahead of the moving sunset band. Extend the upper inset left-to-right with new yellow-to-gray sunset states. Keep prior states and band labels stable.”  
**CHARACTER COUNT:** 228 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; deterministic map animation required.

### C25. Edit out

Continue to V23 at ~01:32.000 when narration says “Then you turn.” Car orientation/path changes; same map/inset persist.

### C26. Rule

**RECONSTRUCTION RULE:** Track the map only to keep the moving decision variable centered; let the inset record accumulated time.

---

## V23 — 01:32.000–01:35.583

**SHOT:** S14  
**SOURCE:** 01:35.250 — [keyframe](keyframes/V23_0095250ms.jpg)  
**DURATION:** ~3.583 s

### C1. Viewer sees

The car turns and moves south/down across the coral sunset band into the dark night side. The upper inset is nearly full, extending through multiple gray below-horizon states. Literal: **the route ends by crossing the terminator into night after the prolonged sunset.**

### C2. Sync

**Words:** “Then you turn and drive south across the line into nighttime.” **Triggers:** “turn,” “south,” “across,” “nighttime.” **Motion:** car rotates and crosses the labeled band. **Function:** step 3 and strategy closure.

### C3. Change

Car direction reverses toward south; crosses from day/sunset to night; inset completes with final gray states.

### C4. Purpose

**ESSENTIAL / PAYOFF / TRANSITION.** Completes the route and prepares proof.

### C5. Map

Map/band anchor; car lower/right of band on night side; wide inset top; hero car crossing; end state dark side.

### C6. Layout

Car x≈51–58%, y≈67–73%; band arcs y≈54–70%; inset x≈6–95%, y≈7–26%. Eye path car crossing → NIGHT label → completed inset.

### C7. Attention

Car first, sunset/night boundary second, final inset state third. Clean.

### C8. Reuse

**MODIFIED REUSE** V22; route direction and final state change.

### C9. DNA

Same E05/G03; one decisive car turn; dark lower region; completed progress strip.

### C10. Prompt

Create a 720×1280 vertical hand-drawn Scandinavia route map with pale-gray land, dark-gray night region, and a curved muted-coral `SUNSET` band separating labeled `DAY` above from `NIGHT` below. Place one tiny white car with black outline just below the band on the night side near center-right, angled south/downward as if it has crossed the line. Across the top, place a wide black-outlined white inset showing a complete left-to-right sunset sequence of equal circles: yellow descending, half-yellow/half-gray at contact, then several progressively gray states below the mini-horizon. Link states with small arrows. Preserve the exact final car-to-band relationship, map crop, flat palette, and no second car, route trail, or extra annotations.

### C11. Text

Overlay `DAY`, `SUNSET`, `NIGHT` along band; no inset words.

### C12. Lock

Car ends on NIGHT side; single turn; inset complete; fixed labels/map at end; no bounce back.

### C13. QC

Objects High; composition High; state High; perspective High; color/text High; continuity High.

### C14. Animation

Car rotates toward south and crosses the band; inset adds final gray states; camera/map tracking eases to stop.

### C15. Static

Band labels, geography, prior inset states; camera locks after crossing.

### C16. Why

Crossing is the terminal action. Additional motion after it would weaken closure; the end hold confirms night entry.

### C17. Conflict

Car angle and band crossing support southward motion; no conflict.

### C18. Sequence

V22 northward state → car turns → crosses sunset strip → reaches night → final inset gray state → camera settles → hard cut.

### C19. Method

**C/B — path/rotation keyframes and map tracking.**

### C20. AI suitability

**LOW.** Exact line crossing and state history are deterministic.

### C21. Build

Reuse V22; add turn rotation; keyframe car path through band matte; finish inset; ease map null to stop. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Path animation is precise.

### C23. Animation prompt

**ANIMATION PROMPT:** “Keep the map readable as the small car turns south, crosses the coral sunset band once, and stops on the dark NIGHT side. Add the final gray sunset states to the upper inset, then settle the camera and hold.”  
**CHARACTER COUNT:** 207 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors/editor keyframes preferred.

### C25. Edit out

Hard cut at 01:35.583 to V24 on “I ran a search.” Conceptual continuity: route animation becomes research/proof.

### C26. Rule

**RECONSTRUCTION RULE:** End a procedural animation with one irreversible crossing and a clear static end state.

---

## V24 — 01:35.583–01:38.875

**SHOT:** S15  
**SOURCE:** 01:38.500 — [keyframe](keyframes/V24_0098500ms.jpg)  
**DURATION:** ~3.292 s

### C1. Viewer sees

On a white field, C01 sits at a black-outline chair and desk in the lower-left/center, hands at an open laptop. A small gray satellite-dish-like icon and hand label `PyEphem` float above the laptop with a curved pointer. Upper half remains empty. Literal: **a stick researcher uses a laptop and PyEphem.**

### C2. Sync

**Words:** “I ran a search for long sunset driving paths using some PyEphem code…” **Triggers:** “ran a search” shows researcher; “PyEphem” reveals callout. **Function:** methodology/proof layer.

### C3. Change

Map strategy removed; research desk, laptop, seated character and PyEphem callout added.

### C4. Purpose

**EVIDENTIAL / ORIENTING.** Signals computation rather than intuition.

### C5. Map

White field; researcher/desk x≈6–58%, y≈54–89%; callout x≈47–72%, y≈47–57%; upper/right negative space reserved for V25 map. Hero: PyEphem label; anchor: desk.

### C6. Layout

Lower-left mass with >55% empty upper-right. Eye path head/laptop → PyEphem → empty proof space.

### C7. Attention

Researcher/laptop first, PyEphem second. Clean.

### C8. Reuse

**NEW BASE IMAGE** E06/C01/O08; later modified V25/V26.

### C9. DNA

Thin black irregular office line art, empty oval head, no fills except gray callout icon, orthographic white field.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn research explainer on a pure white background. In the lower-left half, draw one featureless stick researcher seated side-on in a simple black-outline swivel chair at a rectangular black-outline desk. Place an open thin laptop on the desk facing the researcher; show both hands near the keyboard. Keep the oval head empty white and limbs thin black. Above and slightly right of the laptop, draw a small gray satellite-dish-like icon, the exact hand-lettered word `PyEphem`, and a short curved black pointer toward the laptop. Leave the entire upper-right half empty for a later map. Use no shadows, room walls, floor, facial features, extra furniture, or color accents.

### C11. Text

Overlay `PyEphem` in small black hand lettering beside gray icon.

### C12. Lock

One researcher, chair, desk, laptop, one PyEphem callout; pose seated/typing; upper-right empty; locked camera.

### C13. QC

Subject High; pose High; composition High; scale High; perspective Medium–High; color High; text High; negative space High; continuity High.

### C14. Animation

Researcher/desk appear; PyEphem icon/label reveals. No necessary typing motion.

### C15. Static

Researcher pose, desk/laptop, background, camera.

### C16. Why

The callout—not hand motion—is the evidence hero. Keeping the researcher still avoids anthropomorphic distraction.

### C17. Conflict

No motion cues; stillness agrees.

### C18. Sequence

Hard cut to researcher → PyEphem icon/word → hold → map begins V25.

### C19. Method

**A/C — static line illustration plus callout reveal.**

### C20. AI suitability

**LOW–MEDIUM.** Character can be generated, but exact laptop/negative space/text are safer as drawn layers.

### C21. Build

White solid; chair/researcher; desk/laptop; callout icon/text/pointer. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the seated researcher, chair, desk and laptop still. Reveal the small gray dish icon, draw its curved pointer, then add the ‘PyEphem’ label above the laptop. Keep the upper-right empty.”  
**CHARACTER COUNT:** 205 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; exact label in editor.

### C25. Edit out

No cut; V25 adds the Norway map in the reserved upper-right.

### C26. Rule

**RECONSTRUCTION RULE:** Reserve negative space before introducing the evidence object that will occupy it.

---

## V25 — 01:38.875–01:43.000

**SHOT:** S15  
**SOURCE:** 01:41.500 — [keyframe](keyframes/V25_0101500ms.jpg)  
**DURATION:** ~4.125 s

### C1. Viewer sees

The researcher/desk/PyEphem remain below-left. A large black-framed grayscale Scandinavia map now occupies the upper-right/upper-center. Land is medium gray on light gray. Literal: **the researcher works below a framed Scandinavian search map.**

### C2. Sync

**Words:** “…and GPS traces of Norwegian highways…” **Trigger:** “Norwegian highways.” **Motion:** map scales/reveals in the reserved space. **Function:** identify search domain/data.

### C3. Change

Framed map added; base research scene remains static.

### C4. Purpose

**EVIDENTIAL / EXPLANATORY.** Makes the geographic data scope concrete.

### C5. Map

Map x≈34–94%, y≈10–52%; researcher x≈4–57%, y≈54–90%; PyEphem between. Hero: map; anchor: desk.

### C6. Layout

Diagonal balance: map upper-right vs researcher lower-left. Minimal overlap. Eye path map → PyEphem → laptop/researcher.

### C7. Attention

Map first by scale, researcher second, callout third. Controlled.

### C8. Reuse

**ADDITIVE MODIFICATION** V24; introduces framed E05 map.

### C9. DNA

White field, black frame, flat gray map, persistent line-art researcher, no roads visibly over-detailed.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn research explainer on white. Keep one featureless stick researcher seated at a black-outline chair and desk with an open laptop in the lower-left half. Preserve the small gray `PyEphem` dish callout above the laptop. In the upper-right/upper-center, add a large portrait-oriented rectangular map with a slightly irregular black frame, light-gray background and a simplified medium-gray silhouette of Scandinavia, including recognizable Norway, Sweden, Finland and nearby Arctic land. Balance the map diagonally against the researcher without overlap. Use flat fills, thin irregular black lines, no route, no Arctic Circle, no road labels, no room detail, shadows, or extra objects.

### C11. Text

Only `PyEphem` overlay remains; no map title.

### C12. Lock

Map orientation/crop; researcher lower-left; map upper-right; callout between; no red route yet.

### C13. QC

Objects High; composition High; scale High; perspective High; color High; text High; continuity High.

### C14. Animation

Map frame and land reveal/scale in; researcher remains fixed.

### C15. Static

Researcher/desk/laptop/PyEphem, camera, background.

### C16. Why

Map is the new evidence layer. Moving the researcher would split attention.

### C17. Conflict

No motion cue; additive reveal agrees.

### C18. Sequence

V24 → map frame → gray land → hold for “GPS traces” → V26 route.

### C19. Method

**C — vector/map layer reveal.**

### C20. AI suitability

**LOW** for exact geography; deterministic map preferred.

### C21. Build

Reuse V24; add frame; land silhouette/matte; scale/opacity. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive layer.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Scale in the black-framed grayscale Scandinavia map above the researcher. Reveal the frame first, then the gray land silhouette. Keep the researcher, desk, laptop and PyEphem callout completely still.”  
**CHARACTER COUNT:** 215 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; use an exact vector/map asset.

### C25. Edit out

Continue to V26; same map becomes a coordinate frame for the Arctic Circle.

### C26. Rule

**RECONSTRUCTION RULE:** Add proof in the negative space without disturbing the established researcher–tool relationship.

---

## V26 — 01:43.000–01:44.500

**SHOT:** S15  
**SOURCE:** 01:44.375 — [keyframe](keyframes/V26_0104375ms.jpg)  
**DURATION:** ~1.500 s

### C1. Viewer sees

On the framed Scandinavia map, a coral-red dashed arc crosses the northern region. Bold coral hand text `ARCTIC CIRCLE` sits along the path with a curved pointer. Researcher and PyEphem remain below. Literal: **the Arctic Circle is drawn across the researcher’s Scandinavian map.**

### C2. Sync

**Words:** “…works about equally well anywhere inside the Arctic Circle.” **Trigger:** “Arctic Circle.” **Motion:** dashed path draws; label follows. **Function:** delimit result scope.

### C3. Change

Red dashed circle segment, label and pointer added; all base assets persist.

### C4. Purpose

**EVIDENTIAL / EXPLANATORY / PROOF COMPLETION.** Defines the domain of the search claim.

### C5. Map

Static framed map upper-right; coral arc across its upper third; label near center-right; researcher below-left. Motion hero: arc.

### C6. Layout

Arc x≈34–96%, y≈18–37%; label x≈56–92%, y≈27–34%. Eye path coral arc/label → map → PyEphem/researcher.

### C7. Attention

Coral path first, label second, map/researcher third. Clean.

### C8. Reuse

**GRAPHIC-ONLY MODIFICATION** V25.

### C9. DNA

Scarce coral accent, dashed hand path, uppercase hand label, gray map anchor, flat white canvas.

### C10. Prompt

Create a 720×1280 vertical minimalist hand-drawn research explainer. Keep the seated featureless researcher, chair, desk, laptop and gray `PyEphem` callout in the lower-left, and the large black-framed grayscale Scandinavia map in the upper-right. Across the northern third of that map, draw one thin coral-red dashed curved path representing the Arctic Circle, entering from the left frame edge and rising toward the upper-right. Place the exact coral-red uppercase hand label `ARCTIC CIRCLE` along the path near center-right with a small curved pointer. Preserve the map orientation, researcher pose, layer spacing, flat palette, and do not add routes, roads, extra labels, pins, or animation marks.

### C11. Text

Overlay exact `ARCTIC CIRCLE` in coral red; PyEphem remains black.

### C12. Lock

One dashed arc; exact label; map orientation; researcher/desk/callout fixed; no route line.

### C13. QC

Objects High; composition High; geometry High; color/text High; continuity High; risk Low.

### C14. Animation

Dashed Arctic Circle draws left-to-right; label/pointer reveal after completion.

### C15. Static

Researcher, map, frame, desk, laptop, PyEphem, camera/background.

### C16. Why

The path is the new scope boundary; map must stay still for geography. No added character motion improves comprehension.

### C17. Conflict

Dashed arc implies drawing direction; requested left-to-right agrees with source reveal.

### C18. Sequence

V25 → draw dashed coral arc → reveal `ARCTIC CIRCLE`/pointer → hold → cut.

### C19. Method

**C — VECTOR MOTION GRAPHICS** with dashed stroke/trim path.

### C20. AI suitability

**LOW.** Exact dashed geography/text should be deterministic.

### C21. Build

Map precomp; dashed shape stroke; trim path; label/pointer overlays. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Stroke reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Draw one coral-red dashed Arctic Circle left-to-right across the fixed Scandinavia map, then reveal the ‘ARCTIC CIRCLE’ label and pointer. Keep the researcher, desk, laptop, PyEphem callout and map frame still.”  
**CHARACTER COUNT:** 225 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors required for fidelity.

### C25. Edit out

Hard cut at 01:44.500 to V27 as the method becomes the result. Continuity: Scandinavia map persists but reconfigures into a horizontal result panel.

### C26. Rule

**RECONSTRUCTION RULE:** Draw the geographic scope only after method and domain are visible.

---

## V27 — 01:44.500–01:48.708

**SHOT:** S16  
**SOURCE:** 01:47.000 — [keyframe](keyframes/V27_0107000ms.jpg)  
**DURATION:** ~4.208 s

### C1. Viewer sees

The frame becomes a wide top result strip over a large gray Scandinavia map. At upper-left a gray hatchback with black speed lines faces right. Beside it, a yellow sun sits on a black horizon; a black route arrow slopes down-right toward a gray end-state disc. The lower third is blank white. Literal: **a car and sun traverse a route over Scandinavia toward a gray sunset end state.**

### C2. Sync

**Words:** “Over a wide range of routes and driving speeds…” **Trigger:** “routes/driving speeds.” **Motion:** car/sun/arrow relationship builds across map. **Function:** summarize explored route family before number.

### C3. Change

Researcher removed; map enlarged into middle panel; car, sun, arrow, gray end disc added; lower comparison space reserved.

### C4. Purpose

**EVIDENTIAL / ORIENTING / PRE-PAYOFF.** Shows result mechanism and creates space for number/comparison.

### C5. Map

Top strip y≈7–31%; car x≈5–43%; yellow sun x≈43–52%; arrow to gray disc x≈52–88%; map y≈31–67%; blank lower third. Hero: car/sun/arrow.

### C6. Layout

Strong horizontal action above geographic proof; white lower area anticipates V29. Eye path car → yellow sun → arrow/gray disc → map.

### C7. Attention

Car/yellow sun first, arrow/gray disc second, map third. Controlled.

### C8. Reuse

**COMPOSITIONAL REUSE** of O04/O01/O02/E05; new result layout.

### C9. DNA

Black-outline car, yellow/gray sun coding, gray map, black arrow, white panel architecture.

### C10. Prompt

Create a 720×1280 vertical hand-drawn result infographic on white. Across the upper quarter, draw a thin black horizon line. At upper-left place one compact gray hatchback facing right with several short black speed lines behind it. Immediately to its right place one saturated-yellow sun disc resting at the line. From the sun, draw a long thin black arrow sloping gently down-right to a medium-gray end-state disc near the upper-right edge. Fill the middle third with a large simplified medium-gray map of Scandinavia on a light-gray rectangle, aligned beneath the car/sun strip. Leave the entire lower third pure white and empty for a later comparison. Preserve flat fills, irregular black outlines, exact left-to-right hierarchy, no number/bracket yet, no church, no extra vehicles, and no decorative detail.

### C11. Text

None yet; keep clean plate for V28 number.

### C12. Lock

One car, one yellow sun, one gray end disc, one arrow, one map panel, blank lower third; camera locked.

### C13. QC

Objects High; composition High; scale High; perspective High; color High; text N/A; negative space High; continuity High.

### C14. Animation

Car/speed lines enter; sun/arrow/end disc reveal; map holds. The car need not traverse the full route.

### C15. Static

Map, horizon, lower blank area, camera; final icon positions after reveal.

### C16. Why

The arrow compresses many tested routes into one causal summary. A full map-drive replay would duplicate S14.

### C17. Conflict

Car speed lines/right-facing pose and arrow support rightward motion.

### C18. Sequence

Hard cut to panel → car/sun → arrow/end state → map proof holds → number enters V28.

### C19. Method

**C — VECTOR/EDITOR MOTION GRAPHICS.**

### C20. AI suitability

**LOW.** Exact panel geometry and icons matter.

### C21. Build

White background; top horizon; car precomp; sun/end disc; arrow trim; map block; lower blank matte. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Bring in the right-facing car with short speed lines, reveal the yellow sun, then draw the black arrow to the gray end-state disc above the fixed Scandinavia map. Keep the lower third blank and all final icons still.”  
**CHARACTER COUNT:** 231 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; vectors preferred.

### C25. Edit out

No cut; V28 adds the result bracket/number above the route.

### C26. Rule

**RECONSTRUCTION RULE:** Before revealing a number, compress the tested mechanism into one clean route strip.

---

## V28 — 01:48.708–01:51.500

**SHOT:** S16  
**SOURCE:** 01:50.750 — [keyframe](keyframes/V28_0110750ms.jpg)  
**DURATION:** ~2.792 s

### C1. Viewer sees

V27 remains. Above the sun-to-end-state route, a black hand-drawn bracket spans the interval and the exact label `~95 min` appears above it. Literal: **the route strip is quantified as approximately 95 minutes.**

### C2. Sync

**Words:** “…the longest sunset I could come up with was consistently about 95 minutes…” **Trigger:** “95 minutes.” **Motion:** bracket draws, number writes/reveals. **Function:** major payoff.

### C3. Change

Bracket and `~95 min` added; all V27 assets persist.

### C4. Purpose

**ESSENTIAL / REVEAL / PAYOFF.** Removing it eliminates the answer.

### C5. Map

Bracket x≈54–95%, y≈13–21%; number centered above. Motion hero: number; static anchor: route/map.

### C6. Layout

Number sits top-right above relevant interval; no competing lower content yet. Eye path number/bracket → sun/end states → map.

### C7. Attention

`~95 min` first, yellow sun second, car/map third. Clean.

### C8. Reuse

**TEXT/GRAPHIC MODIFICATION** V27.

### C9. DNA

Handwritten black number/brace, no typographic box, exact proximity to measured path.

### C10. Prompt

Create a 720×1280 vertical hand-drawn result infographic on white. In the upper strip, place a right-facing gray hatchback with black speed lines at left, a yellow sun on the horizon beside it, and a black arrow sloping down-right to a gray end-state disc. Beneath the strip fill the middle third with a simplified gray Scandinavia map; leave the lower third blank. Above the sun-to-gray-disc interval, draw a long loose black horizontal bracket with short downturned ends and center the exact hand-lettered text `~95 min` above it. Preserve the original icon positions, map crop, flat black/yellow/gray palette, open lower space, and do not add a comparison panel or any other numbers.

### C11. Text

**BAKE:** NO. Overlay exact `~95 min` in black hand lettering, centered over bracket.

### C12. Lock

Number exact; bracket spans sun→gray end; V27 unchanged; lower third blank.

### C13. QC

All geometry High; text High overlay; continuity High; risk Low.

### C14. Animation

Bracket draws left-to-right; `~95 min` writes/reveals after completion.

### C15. Static

Car, sun, arrow, gray disc, map, lower white field, camera.

### C16. Why

The answer deserves the only motion. Moving existing icons at the reveal would split attention.

### C17. Conflict

Bracket direction is neutral; left-to-right drawing matches reading order.

### C18. Sequence

V27 hold → draw bracket → reveal `~95 min` → hold → lower comparison appears.

### C19. Method

**C — VECTOR/TEXT MOTION GRAPHICS.**

### C20. AI suitability

**LOW.** Exact number must be deterministic.

### C21. Build

Reuse V27; bracket trim path; text animator/opacity. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Stroke/text reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Draw the black bracket across the yellow-sun-to-gray-disc interval, then reveal the exact label ‘~95 min’ above it. Keep the car, route arrow, map and blank lower third completely still.”  
**CHARACTER COUNT:** 201 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; exact text in editor.

### C25. Edit out

Additive transition at 01:51.500 to V29. Upper 95-minute panel stays fixed as the Longyearbyen comparator fills the lower third.

### C26. Rule

**RECONSTRUCTION RULE:** Reveal the measured answer only after its visual interval is already visible and stable.

---

## V29 — 01:51.500–01:53.458

**SHOT:** S17  
**SOURCE:** 01:53.000 — [keyframe](keyframes/V29_0113000ms.jpg)  
**DURATION:** 1.958 s

### C1. Viewer sees

The upper two-thirds preserve the `~95 min` car/map route. The lower third now contains a black-outline Longyearbyen church at far-left, a tiny stick figure, a yellow sun on a horizon, a short path to a gray disc, and `~55 min` above. Beneath/behind them is a small gray Svalbard map labeled `LONGYEARBYEN` with a pointer. Literal: **a stacked comparison shows the 95-minute route above a 55-minute Longyearbyen benchmark.**

### C2. Sync

**Words:** “…about 40 minutes longer than the longest sunset you can get in Longyearbyen.” **Trigger:** “40 minutes longer” / “Longyearbyen.” **Motion:** lower comparator reveals under fixed upper result. **Function:** comparative payoff.

### C3. Change

Lower white field filled with church, figure, sun path, `~55 min`, Svalbard map/label; upper panel unchanged.

### C4. Purpose

**ESSENTIAL / COMPARISON / PAYOFF.** Converts 95 into a meaningful improvement.

### C5. Map

Upper: V28. Lower: church x≈0–35%, figure/sun x≈45–67%, bracket x≈66–94%; Svalbard map lower-center. Hero: 95-vs-55 vertical comparison.

### C6. Layout

Top-to-bottom reading: 95 route → 55 benchmark → Longyearbyen locator. Comparable sun/path geometry reinforces the numerical delta.

### C7. Attention

`~95 min` first, `~55 min` second, church/map context third. Slightly dense but controlled.

### C8. Reuse

**ADDITIVE/COMPOSITIONAL REUSE** of V28 plus V15 benchmark assets.

### C9. DNA

Stacked panels, identical yellow/gray sun code, black hand brackets, grayscale geography, simple church/figure icons.

### C10. Prompt

Create a 720×1280 vertical hand-drawn split comparison on white. Preserve the upper two-thirds exactly: right-facing gray car with speed lines, yellow sun, black arrow to gray end disc, `~95 min` bracket above, and a large gray Scandinavia map below. In the lower third, draw a thin black horizon; place a simple black-outline white Longyearbyen church at far-left, one tiny featureless stick figure near center-left, one yellow sun on the line, a short black arrow to a gray end disc, and the exact black label `~55 min` above a shorter bracket. Beneath the lower scene, include a small simplified gray map of Svalbard with the hand label `LONGYEARBYEN` and a pointer. Preserve the stacked hierarchy, comparable sun scales, flat black/yellow/gray palette, no extra buildings, vehicles, numbers, or decorative detail.

### C11. Text

Overlay exact `~95 min`, `~55 min`, `LONGYEARBYEN`; black hand lettering.

### C12. Lock

Upper panel unchanged; lower has one church, one figure, one sun, one gray disc, one short arrow, one Svalbard map; numbers exact.

### C13. QC

Objects High; composition High; scale High; perspective High; color/text High; continuity High; risk Medium due density.

### C14. Animation

Lower comparison panel reveals bottom-up or additively; `~55 min` appears after icons; upper panel stays still.

### C15. Static

Entire 95-minute upper panel; camera/background; lower icons after reveal.

### C16. Why

Only the comparator is new. Holding 95 fixed makes the gain cognitively immediate; animating both would reduce comparison accuracy.

### C17. Conflict

No conflicting motion cues; vertical reveal supports hierarchy.

### C18. Sequence

V28 hold → lower church/figure/sun path → `~55 min` → Svalbard map/Longyearbyen → brief comparison hold → cut.

### C19. Method

**C — VECTOR/EDITOR ADDITIVE REVEAL.**

### C20. AI suitability

**LOW.** Exact stacked layout/numbers/maps need deterministic construction.

### C21. Build

Reuse V28; lower-panel precomp; church/figure/sun icons; map matte; labels/bracket. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive panel reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Keep the complete ‘~95 min’ upper panel still. Reveal the lower Longyearbyen church, figure, yellow-to-gray sun path, then ‘~55 min’ and the Svalbard locator. Hold both panels for comparison.”  
**CHARACTER COUNT:** 206 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; build in vectors and editor text.

### C25. Edit out

Hard cut at 01:53.458 to V30. Continuity: the abstract yellow sun becomes the painterly sunset; the numerical payoff yields to emotional closure.

### C26. Rule

**RECONSTRUCTION RULE:** Make the payoff comparative by holding the winning result fixed while the baseline appears beneath it.

---

## V30 — 01:53.458–01:58.083

**SHOT:** S18  
**SOURCE:** 01:56.500 — [keyframe](keyframes/V30_0116500ms.jpg)  
**DURATION:** ~4.625 s

### C1. Viewer sees

The painterly sunset E02 returns without the earlier “NOT A SUNSET” verdict. C02 (black-haired) stands at lower-left beside C03 (gray-headed), both facing the bright sun near center-right. No text yet. Literal: **the same two figures quietly watch the same vivid sunset.**

### C2. Sync

**Words:** “But if you are stuck on Svalbard and you want to make the sunset or sunrise last a little longer…” **Trigger:** “sunset… longer.” **Motion:** none yet; callback establishes emotional scene. **Function:** callback, decompression, joke setup.

### C3. Change

Split infographic removed; E02/C02/C03 return; all labels initially removed.

### C4. Purpose

**EMOTIONAL / CALLBACK / TRANSITION.** Re-humanizes the numerical answer and sets up the coda.

### C5. Map

Indigo/red/orange sky; white-yellow sun x≈47–67%, y≈48–61%; figures x≈5–29%, y≈58–80%; dark curved foreground. Hero: sun; anchor: figures/land.

### C6. Layout

Same diagonal balance as V04, but no verdict text. Eye path sun → figures → empty sky for dialogue.

### C7. Attention

Sun first, figures second, textured sky third. Clean for a dense plate.

### C8. Reuse

**EXACT/COMPOSITIONAL REUSE** of V04 base plate, with text removed and possibly slightly different stroke state.

### C9. DNA

Painterly horizontal scribbles, indigo-to-yellow gradient, tiny anonymous pair, black-olive foreground, sparse stars.

### C10. Prompt

Create a 720×1280 vertical hand-drawn painterly sunset illustration matching the established callback plate. Use a deep indigo sky with dense irregular horizontal crimson, red, orange and yellow strokes concentrated around the horizon. Place a brilliant white-yellow sun slightly right of center at the horizon with a short broken reflection. Use a nearly black olive foreground with a curved shoreline/road sweeping from lower-right toward center. At lower-left, draw exactly two small stick figures facing the sun: C02 on the left with a solid black hair/head mass and C03 on the right with a flat gray circular head. Preserve their scale, spacing and left/right identity. Leave text-safe sky above them; include no verdict, callout, spin trails, extra people, objects, or photorealism.

### C11. Text

No text in this state; use clean plate for later dialogue overlays.

### C12. Lock

Two figures only; C02 left/C03 right; sun center-right; no `NOT A SUNSET`; no spin trails; camera locked.

### C13. QC

Subject High; pose High; composition High; scale High; perspective Medium–High; lighting/color High; text N/A; continuity High; painterly risk Medium.

### C14. Animation

No required motion; hold callback plate.

### C15. Static

Figures, sun, sky strokes, foreground, camera, lighting.

### C16. Why

Stillness creates contrast after dense infographics and gives the coda emotional space. Additional movement would preempt the spinning gag.

### C17. Conflict

No motion cues; stillness agrees.

### C18. Sequence

Hard cut to clean sunset → quiet hold → C03 begins spinning in V31.

### C19. Method

**A/K — static painted plate; later vector character trails.**

### C20. AI suitability

**MEDIUM** for subtle organic shimmer, but static plate is more faithful.

### C21. Build

Reuse V04 clean plate; separate C02/C03 layers for later animation. Recreation method—original software not verified.

### C22. First/last frame

**NO** for this state.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Hold the painterly sunset, bright sun, dark foreground and both stick figures completely still for a quiet callback beat. Preserve their left-right identities and spacing.”  
**CHARACTER COUNT:** 186 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; if generated, keep motion near zero.

### C25. Edit out

No cut; V31 begins when narration says “try spinning counterclockwise.”

### C26. Rule

**RECONSTRUCTION RULE:** After the numerical payoff, return to the richest earlier image and remove its old verdict to change its emotional meaning.

---

## V31 — 01:58.083–02:01.167

**SHOT:** S18  
**SOURCE:** 02:00.750 — [keyframe](keyframes/V31_0120750ms.jpg)  
**DURATION:** ~3.084 s

### C1. Viewer sees

E02 and C02 remain. C03 spins in place at lower-left/center: thin white elliptical loops encircle its waist and legs, with a vertical scribble/axis extending below. The body blurs into a simple rotating stick form while the gray head stays readable. Literal: **the gray-headed figure spins counterclockwise while the companion watches.**

### C2. Sync

**Words:** “…you can always try spinning counterclockwise, so your angular momentum slows the Earth’s rotation.” **Triggers:** “spinning counterclockwise.” **Motion:** C03 rotates; white loops appear. **Function:** physical joke/demonstration.

### C3. Change

White rotation trails and C03 body rotation added; C02/sunset remain static.

### C4. Purpose

**HUMOR / EXPLANATORY / PATTERN INTERRUPT.** Visualizes a technically real but absurdly tiny intervention.

### C5. Map

Sun/land anchor; C02 x≈5–16%; spinning C03 x≈18–38%; white loops x≈13–42%, y≈63–87%. Hero: spin trails.

### C6. Layout

Motion confined to lower-left so the bright sun still balances frame. Eye path spin → watching figure → sun.

### C7. Attention

Motion makes spinner first; sun second; companion third. Controlled.

### C8. Reuse

**MODIFIED REUSE** V30; only C03/trails change.

### C9. DNA

Painterly plate plus simple white scribble motion graphic; small-amplitude character rig/replacement drawings; no camera movement.

### C10. Prompt

Create a 720×1280 vertical painterly sunset frame matching the established indigo/red/orange/yellow landscape. Keep the bright white-yellow sun near the center-right horizon and the black-haired stick companion C02 standing still at lower-left. Place the gray-headed stick figure C03 immediately to C02’s right, centered at lower-left/center. Around C03’s torso, hips and legs, draw several thin irregular white elliptical loops viewed in perspective, widening around the waist and narrowing toward a vertical white scribble beneath the feet, clearly indicating rapid counterclockwise spinning. Keep the gray circular head recognizable and all motion trails confined to C03. Preserve the dark foreground, camera, lighting and background; add no text yet, dust, duplicated bodies, extra people, or camera blur.

### C11. Text

None yet; dialogue comes V32–V34.

### C12. Lock

C02 still; C03 spins in place only; white elliptical trails; sun/background/camera fixed; counterclockwise direction; no translation.

### C13. QC

Subject High; pose Medium–High; composition High; scale High; perspective Medium; lighting/color High; continuity High; risk Medium for generative anatomy.

### C14. Animation

C03 body rotates rapidly counterclockwise with small amplitude; white elliptical trails loop; head stays centered. C02 remains still.

### C15. Static

C02, sun, horizon, shoreline, sky, lighting, camera.

### C16. Why

C03 is the sole motion hero and joke. Moving C02, sun or camera would dilute the absurd action and remove the reference frame.

### C17. Conflict

White loops imply circular motion; ensure counterclockwise direction matches narration.

### C18. Sequence

C03 initiates turn → accelerates → trails build → steady spin/hold into dialogue.

### C19. Method

**D/E/C — simple character rig or replacement drawings plus vector loop trails.**

### C20. AI suitability

**MEDIUM.** Organic spinning can work, but identity/limb integrity and exact direction may drift.

### C21. Build

Separate C03 head/body; rotate body around vertical pivot; use 3–5 replacement poses; animate white ellipse strokes; keep head stabilized. Recreation method—original software not verified.

### C22. First/last frame

**NO** for rigged build; optional AI start/end does not guarantee a sustained spin.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Spin only the gray-headed right stick figure rapidly counterclockwise in place; keep its head centered and draw tight white elliptical trails around torso and legs. The black-haired companion, sun and landscape remain still.”  
**CHARACTER COUNT:** 239 / 500  
**STATUS:** PASS

### C24. Adapter

For Runway, isolate motion to C03 and use positive stillness language for all anchors; composite loop trails deterministically if needed.

### C25. Edit out

Continue into V32 without cut; spin persists as the companion’s question appears.

### C26. Rule

**RECONSTRUCTION RULE:** Confine comic motion to one character and stabilize every environmental reference.

---

## V32 — 02:01.167–02:02.917

**SHOT:** S18  
**SOURCE:** 02:03.500 — [keyframe](keyframes/V32_0123500ms.jpg)  
**DURATION:** ~1.750 s

### C1. Viewer sees

C03 continues spinning. White uppercase `WHAT ARE YOU DOING?` appears at left-center above C02, with a thin curved white speech pointer toward the black-haired figure. Literal: **the still companion asks the spinning figure what it is doing.**

### C2. Sync

On-screen dialogue, not narration quote: `WHAT ARE YOU DOING?` appears as the spinning gag becomes interpersonal. Narration continues explaining angular momentum. **Function:** open comic dialogue loop.

### C3. Change

Question text and pointer added; spin/background unchanged.

### C4. Purpose

**HUMOR / EMOTIONAL / OPEN LOOP.** Gives the audience’s likely reaction to C02.

### C5. Map

Question x≈1–36%, y≈54–59%; pointer toward C02; spinner lower-center; sun center-right. Motion hero spinner; attention hero text.

### C6. Layout

Text uses left sky negative space and avoids the sun. Eye path question → C02 → spinner.

### C7. Attention

Moving spinner and bright text compete slightly; speech pointer resolves reading order. Controlled.

### C8. Reuse

**TEXT-ONLY MODIFICATION** V31.

### C9. DNA

Small white hand uppercase, thin curved pointer, high contrast on red/orange sky, no bubble outline.

### C10. Prompt

Create a 720×1280 vertical painterly sunset frame matching V31: indigo/red/orange/yellow sky, bright sun center-right, dark foreground, black-haired C02 still at lower-left, and gray-headed C03 spinning counterclockwise beside it with thin white elliptical trails. In the open left-center sky above C02, reserve a compact two-dimensional text area for the exact white uppercase hand lettering `WHAT ARE YOU DOING?`. Add one thin curved white pointer descending from the text toward C02’s head. Preserve all figure positions, spin-trail geometry, sun and landscape; do not add a speech bubble, response text, extra motion, people, or objects.

### C11. Text

**BAKE:** NO. Overlay exact `WHAT ARE YOU DOING?`, white, uppercase, left-center; thin pointer to C02.

### C12. Lock

Question exact; pointer to C02; C03 spin unchanged; no response text yet; sun/background fixed.

### C13. QC

Subject High; composition High; motion continuity High; color High; text High overlay; risk Medium for spinner.

### C14. Animation

Spinner continues; question/pointer write on. No new body motion.

### C15. Static

C02, sun, landscape, camera, already established spin center.

### C16. Why

Text opens the loop while ongoing spin maintains the gag. Extra gesture from C02 is unnecessary; the pointer assigns speech.

### C17. Conflict

Spin trails agree; text does not imply direction.

### C18. Sequence

V31 spin → write question → draw pointer → hold → answer enters.

### C19. Method

**C/D — existing rig plus deterministic text/pointer.**

### C20. AI suitability

**MEDIUM** for continuing spin, **LOW** for exact dialogue.

### C21. Build

Reuse V31 comp; text animator; pointer trim path. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Text reveal.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Continue the gray-headed figure’s counterclockwise spin at constant speed. Write ‘WHAT ARE YOU DOING?’ in the left sky and draw its pointer to the still black-haired companion. Keep the sun and landscape fixed.”  
**CHARACTER COUNT:** 225 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; composite dialogue in editor.

### C25. Edit out

Continue to V33; response appears in the upper-right/center sky with pointer to C03.

### C26. Rule

**RECONSTRUCTION RULE:** Use existing negative space for dialogue so the visual gag can continue uninterrupted.

---

## V33 — 02:02.917–02:05.083

**SHOT:** S18  
**SOURCE:** 02:05.000 — [keyframe](keyframes/V33_0125000ms.jpg)  
**DURATION:** ~2.166 s

### C1. Viewer sees

The question remains at left. Above the sun/right figure, white uppercase response text appears in two lines: `LENGTHENING THE SUNSET` / `PUSHING BACK THE NIGHT`, with a long curved white pointer down to C03. C03 keeps spinning. Literal: **the spinner claims it is lengthening sunset and pushing back night.**

### C2. Sync

Narration: “It’s true that it will only add an imperceptibly small fraction of a nanosecond…” The on-screen response visually states the grandiose intention while narration undercuts its magnitude. **Function:** irony and partial answer.

### C3. Change

Two-line response and pointer added; question/spin/background persist.

### C4. Purpose

**HUMOR / REINFORCING / PARTIAL PAYOFF.** Converts physics into character motive.

### C5. Map

Response x≈43–96%, y≈43–54%; pointer curves to C03; question left; spinner lower-center. Hero: response text; anchor: characters/sun.

### C6. Layout

Dialogue balances both sides of the sun without covering it. Eye path question → response → spinner → sun.

### C7. Attention

Response and spinning figure compete slightly; white pointer organizes them. Controlled.

### C8. Reuse

**TEXT-ONLY MODIFICATION** V32.

### C9. DNA

White compact uppercase, two-line hierarchy, curved pointer, painterly high-contrast background.

### C10. Prompt

Create a 720×1280 vertical painterly sunset frame matching V32. Keep C02 still at lower-left, C03 spinning counterclockwise beside it with white elliptical trails, the bright sun at center-right, and the existing left-side question `WHAT ARE YOU DOING?` with pointer to C02. In the open sky above the sun and C03, reserve a right-centered two-line response area for exact white uppercase hand text: `LENGTHENING THE SUNSET` on line one and `PUSHING BACK THE NIGHT` on line two. Draw one long thin curved white pointer from this response down toward C03. Preserve all prior composition, color, motion trails and text; do not add the final “more time” lines yet.

### C11. Text

Overlay exact two lines in white uppercase, centered/right; pointer to C03. Preserve left question.

### C12. Lock

Both speakers assigned correctly; exact wording/line breaks; no final line yet; spinner/background unchanged.

### C13. QC

Subject High; composition High; motion continuity High; color High; text High; risk Medium.

### C14. Animation

Spinner continues; response types/writes in line 1 then line 2; pointer draws.

### C15. Static

C02, sun, background, camera, left question.

### C16. Why

Text is the new semantic information; constant spin keeps physical cause present. More movement would compete with reading.

### C17. Conflict

No conflict; pointer attaches response to spinner.

### C18. Sequence

V32 → line 1 → line 2 → response pointer → brief hold → final emotional line.

### C19. Method

**C/D — deterministic text over existing spin rig.**

### C20. AI suitability

**MEDIUM** for spin, **LOW** for text.

### C21. Build

Reuse V32; two text layers; pointer trim; maintain spin loop. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive text.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Continue the same counterclockwise spin. Reveal ‘LENGTHENING THE SUNSET’, then ‘PUSHING BACK THE NIGHT’, and draw the response pointer to the spinner. Keep the question, companion, sun and landscape fixed.”  
**CHARACTER COUNT:** 220 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; exact dialogue in editor.

### C25. Edit out

Continue to V34 as one more response line appears beneath/right of the first answer.

### C26. Rule

**RECONSTRUCTION RULE:** Let text carry the escalation while physical motion holds at a constant readable loop.

---

## V34 — 02:05.083–02:09.933

**SHOT:** S18  
**SOURCE:** 02:07.500 — [keyframe](keyframes/V34_0127500ms.jpg)  
**DURATION:** ~4.850 s

### C1. Viewer sees

All prior dialogue and spin remain. A final two-line white response appears below the first answer: `GIVING ME A LITTLE MORE TIME` / `HERE WITH YOU.` The sunset glows behind it. The visual holds after narration ends. Literal: **the spinning figure reframes the tiny physical effect as wanting more time with its companion.**

### C2. Sync

**Words:** “…but it might be worth it.” The on-screen line supplies the emotional reason. **Trigger:** final clause. **Motion:** final text reveals; spinner continues briefly; audio fades to low level after 02:08.15. **Function:** ultimate emotional/humor payoff and closure.

### C3. Change

Final two response lines added; all prior elements persist. Audio enters ending fade/near-silence.

### C4. Purpose

**EMOTIONAL / PAYOFF / END HOLD.** It transforms an infinitesimal technical fact into a relational joke.

### C5. Map

Final text x≈50–97%, y≈52–60%; first answer above; question left; figures lower-left; sun center-right. Hero: final line; anchor: sunset/companions.

### C6. Layout

Text forms a conversational triangle around the sun/figures. Eye path final line → figures → sun → retained question/first answer.

### C7. Attention

Final bright text first, spinner second, sun third. Slight density is acceptable because it is a held end card.

### C8. Reuse

**TEXT-ONLY MODIFICATION** V33; final state of E02 callback.

### C9. DNA

Same painterly plate, looping white trails, clustered white handwritten dialogue, long end hold, audio fade.

### C10. Prompt

Create a 720×1280 vertical painterly sunset end frame matching V33 exactly. Keep the indigo/red/orange/yellow sky, brilliant sun at center-right, dark foreground, black-haired C02 still at lower-left, and gray-headed C03 spinning counterclockwise beside it with white elliptical trails. Preserve the left white question `WHAT ARE YOU DOING?`, the upper response `LENGTHENING THE SUNSET` / `PUSHING BACK THE NIGHT`, and their curved pointers to the correct speakers. Beneath the upper response, add the exact final white uppercase hand text on two lines: `GIVING ME A LITTLE MORE TIME` and `HERE WITH YOU.` Preserve all line breaks, spacing, character identities, spin center and open lower field. Add no credits, CTA, logo, extra people, objects, camera movement, or new effects.

### C11. Text

**BAKE:** NO. Overlay all exact dialogue; final line white, two lines, right-center, period after `YOU.`

### C12. Lock

All wording exact; C02/C03 identity; counterclockwise spin; sun/landscape/camera fixed; no CTA/logo; final hold through export.

### C13. QC

Subject High; composition High; motion continuity High; lighting/color High; text High overlay; continuity High; unsupported risk Medium only for painterly regeneration.

### C14. Animation

Final two lines write/reveal; spin continues then may ease subtly; no camera motion; visual holds to end.

### C15. Static

C02, sun, horizon, sky, foreground, camera, previously revealed text/pointers.

### C16. Why

The final words are the payoff. The continuing spin keeps the joke alive, but every other element stays still to protect readability and tenderness.

### C17. Conflict

Spin trails continue to imply counterclockwise rotation; final text adds no conflicting cue.

### C18. Sequence

V33 → line `GIVING ME A LITTLE MORE TIME` → line `HERE WITH YOU.` → hold; narration ends ~02:07.92 → audio falls below −42 dBFS by 02:08.15 → visual persists to 02:09.933.

### C19. Method

**K — painted plate + rig/replacement spin + deterministic typography.**

### C20. AI suitability

**MEDIUM** for spin/paint texture; **LOW** for exact text and continuity.

### C21. Build

Reuse V33; final text layers; maintain spin; optionally ease trail opacity near end; keep full composition through export. Recreation method—original software not verified.

### C22. First/last frame

**NO.** Additive text and hold.

### C23. Animation prompt

**ANIMATION PROMPT:** “Locked camera. Continue the spinner’s counterclockwise loop. Reveal ‘GIVING ME A LITTLE MORE TIME’, then ‘HERE WITH YOU.’ Keep all prior dialogue, pointers, the companion, sun and landscape fixed; hold the completed frame to the end.”  
**CHARACTER COUNT:** 233 / 500  
**STATUS:** PASS

### C24. Adapter

Tool-neutral; render dialogue in editor. For Runway, feed a text-free plate and composite text afterward.

### C25. Edit out

No outgoing cut. Hold completed frame to 02:09.933 with measured audio fade/near-silence.

### C26. Rule

**RECONSTRUCTION RULE:** End by adding one human meaning to the established mechanism, then stop changing the frame.

---

# Editing + audio integration

## Cut logic

Hard cuts occur when one of three things changes: the coordinate system (white horizon → globe → map), the argumentative job (rule → counterexample → proof → result), or the emotional register (diagram → painterly sunset). Within a coordinate system, the editor prefers additive reveals, object replacement, masking, or a short transform.

Key motivations:

- 00:05.833: question ends; formal definition begins.
- 00:11.792: diagram completion becomes a vivid counterexample.
- 00:13.833–00:25.417: repeated “not a sunset” phrases drive rapid replacement/gag states.
- 00:31.417: definition closes; scale jumps to planetary mechanism.
- 00:42.917: airliner limitation produces poleward reframe.
- 00:49.875: abstract pole geometry becomes a real location constraint.
- 01:08.417: `355 mph` dead end triggers a white-field “better approach” reset.
- 01:14.292: symmetric solar path becomes geographic terminator motion.
- 01:35.583: completed strategy cuts to evidence/method.
- 01:44.500: proof scope cuts to result panel.
- 01:51.500: baseline comparator is added rather than cutting away, preserving the 95-minute anchor.
- 01:53.458: numerical argument resolves; painterly callback begins the coda.

## Fast and slow zones

- **Fastest cluster:** 00:11.792–00:25.417, where S03–S07 average roughly 2–4 s and repeated rejection phrases motivate replacements.
- **Slowest explanatory cluster:** S14, 01:14.292–01:35.583 (21.292 s), but internal state change is continuous.
- **Slowest emotional hold:** S18, 01:53.458–02:09.933 (16.474 s), justified by one character loop, progressive dialogue, and final silence.

## Audio engine

- **Narration behavior:** nearly continuous, brisk, center-dominant, clause-based; pauses commonly precede a new visual claim.
- **Music behavior:** no separate music bed is confidently verifiable from the mixed-track spectrogram. If present, it is subordinate enough not to form an independent measurable layer.
- **SFX behavior:** no isolated SFX can be semantically verified. `BRU-WAAK` is visibly written, but the mixed track does not permit a confident claim that a synchronized sound effect is present.
- **Audio–visual sync:** strong at nouns/numbers/directions (`sunset`, `WEST`, `355 mph`, `NW`, `SW`, `PyEphem`, `ARCTIC CIRCLE`, `95 minutes`). This is semantic synchronization, not merely beat cutting.
- **Silence/ending:** narration ends about 02:07.92; the mix falls below −42 dBFS at about 02:08.15 and remains low through 02:09.89 while the final text holds.

---

# Thumbnail and Shorts extraction

## Thumbnail candidates

### Candidate T01 — 01:53.000 split comparison

- **Why strong:** contains the answer and comparator in one frame.
- **Dominant object:** `~95 min` over car/sun route.
- **Mobile readability:** Medium in the source; numbers are too small without a custom crop.
- **Contradiction/question:** Why is the legal road result longer than the northernmost-road benchmark?
- **Remove:** most map detail, PyEphem-style context, tiny stick figure.
- **Enlarge:** `95 min`, `55 min`, yellow sun, car.
- **Thumbnail question:** `95 MINUTES?!`
- **Title relationship:** directly fulfills “How long?”

### Candidate T02 — 01:07.750 `WEST / 355 mph`

- **Why strong:** one vivid number makes the intuitive strategy absurd.
- **Dominant object:** car and `355 mph`.
- **Mobile readability:** High after a modest crop; dark background gives text contrast.
- **Contradiction/question:** Why does chasing a slow-looking sunset require near-supersonic road speed?
- **Remove:** small stars and nonessential map detail.
- **Enlarge:** car, sun, `355 mph`.
- **Thumbnail question:** `YOU’D NEED 355 MPH`
- **Title relationship:** previews the failed approach, not the answer; strongest curiosity packaging.

### Candidate T03 — 00:13.500 `NOT A SUNSET`

- **Why strong:** richly colored pattern break and explicit contradiction.
- **Dominant object:** bright sun plus white verdict.
- **Mobile readability:** High if cropped around sun/text/figures.
- **Contradiction/question:** How can this visibly beautiful sunset “not” be a sunset?
- **Remove:** tiny lower callout if it becomes illegible.
- **Enlarge:** `NOT A SUNSET`, sun, two figures.
- **Thumbnail question:** `THIS DOESN’T COUNT?`
- **Title relationship:** supports the definition puzzle but hides the final duration.

**Recommended packaging:** T02 for curiosity-led discovery; a redesigned T01 for answer-led search intent.

## Shorts candidates

| Candidate | Source | Hook | Core/payoff | Context needed | Suggested length | Visuals/prompts | End CTA |
|---|---|---|---|---|---:|---|---|
| SH01 — What counts as sunset? | 00:00–00:31 | “A beautiful sunset might not count.” | First contact → full disappearance → hill is invalid | None beyond one-sentence question | 28–32 s | V02–V10 cards | “Now find the longest legal one.” |
| SH02 — Why west fails | 00:31–01:08 | “Even northern Norway needs 355 mph.” | Globe speed → poles → roads → `355 mph` | Define road/speed constraint | 32–38 s | V11–V17 | Bridge to “the route that beats it” |
| SH03 — The winning route | 01:08–01:53 | “Don’t chase west—wait for the boundary to reverse.” | NW→SW terminator, wait/north/south, `~95 min` | One sentence defining sunset | 42–48 s | V18–V29 | “That’s ~40 minutes beyond Longyearbyen.” |
| SH04 — Nanosecond romance | 01:53–02:08 | “Can spinning make sunset longer?” | Counterclockwise spin → imperceptible fraction → “more time here with you” | State that angular momentum effect is tiny | 15–18 s | V30–V34 | None; let final line land |

Do not force SH04 to sell a product or subscription; its value is the tonal surprise.

---

# Engine D — Master synthesis

## D1. Story engine

**Hook:** constrained optimization question.  
**Escalation:** stricter definition, failed apparent sunsets, airliner loophole, pole/road conflict, impossible westward speed.  
**Reversal:** stop chasing west; exploit a reversing day-night line.  
**Payoff:** wait → drive north → turn south → ~95 minutes → 40-minute gain.  
**Closure:** a technically real nanosecond trick becomes a relational joke.

## D2. Script engine

- **Main hook:** longest legal paved-road sunset.
- **Open loops:** what counts; where to drive; how fast; whether west fails; how reversal works; measured maximum.
- **Mini-hooks:** “not a sunset,” arbitrarily long airliner, no polar roads, 355 mph, “better approach,” PyEphem search.
- **But/therefore chain:** every intuitive solution creates its own constraint and points to the next model.
- **Midpoint:** 355 mph closes the obvious strategy at 01:08.
- **Payoff ladder:** definition → airliner principle → 55-min benchmark → 355-mph rejection → route steps → 95-min answer → 55/95 comparison → emotional coda.
- **CTA:** absent.
- **Next-video bridge:** extend the same constrained-optimization method to non-road vehicles, sunrise, twilight, or an eclipse shadow.

## D3. Visual engine

- **Visual grammar:** whiteboard question → white rule diagrams → high-color contradiction → globe mechanics → real location → map strategy → research proof → result comparison → high-color callback.
- **Composition habits:** one model per frame, one saturated hero, large negative space, front-on explanatory camera.
- **Camera habits:** locked; one controlled map-tracking sequence.
- **Object system:** repeated sun, car, globe/map, arrows, labels.
- **B-roll system:** none in the conventional live-action sense; illustrative scene replacement performs the same reset job.
- **Illustration system:** irregular black ink, flat gray context, yellow/red/green semantics, painterly bookends.
- **Graphic system:** horizons, state copies, arrows, dashed boundaries, inset progress strip, brackets.
- **Text system:** exact hand labels adjacent to variables; no decorative headlines.
- **Color system:** gray context, yellow target, coral verdict/boundary, green valid, full-spectrum warm palette only for emotional/pattern-break scenes.

## D4. Motion engine

- **Usually moves:** the newest information-bearing object—sun, plane, car, terminator, path, label, spinner.
- **Usually still:** the coordinate frame—horizon, map, globe, landscape, camera—and previously explained state copies.
- **Static coordinate frame:** one horizon line, globe surface, or geographic map.
- **Triggers:** a spoken direction, threshold, number, location, or new step.
- **Motion amount:** small and legible; mostly translation, stroke reveal, opacity, and replacement.
- **Reveals:** add variable → draw direction → reveal label → hold.
- **Camera moves:** only when the map must keep the car/boundary readable.
- **Camera locks:** all rule diagrams, globe comparisons, proof panels, and the coda.
- **Cut vs animation:** cut for new coordinate system/argument; animate for changed state within the same system.
- **Replacement drawings:** absurd gags, door, cracked sun, spinning stick body.
- **Scale/color/text change:** scale for map inset/proof; yellow→gray at horizon crossing; labels appear on the narrated keyword.

**CREATOR MOTION FORMULA:** Fix the world, move one variable through a visible threshold, freeze the evidence it leaves behind, label the result, then hold.

## D5. Editing engine

The edit alternates conceptual “chapters” rather than arbitrary tempo changes. Fast white replacements handle objections; slower globe/map shots build causal models; painterly shots reset attention and change emotional register. Continuity is usually carried by one object or relation: sun → horizon → globe band → map band → sun comparison → painterly sun.

## D6. Audio engine

Narration provides nearly all pacing and semantic triggers. The waveform is dense but not brick-walled; short clause gaps create visual entry points. Separate music/SFX are unverified. The final dialogue stays on-screen after the spoken ending while the mix fades into a measured low-level hold.

## D7. Attention engine

**Typical eye flow:** moving yellow sun/car → red direction/verdict → adjacent label/number → gray geographic context.  
**Primary device:** scarce saturation plus motion.  
**Secondary device:** scale/centrality and exact handwritten labels.  
**Common competition:** painterly background versus small white text; resolved through luminance contrast and held frames.  
**Motion redirection:** a new path or object appears only when narration names it.

## D8. Object/visual lifecycle engine

The sun is the strongest lifecycle: question icon → measured threshold → invalid variants → planetary velocity → polar benchmark → map inset/progress → 55/95 result → emotional callback. The car evolves from title constraint to failed chaser to route cursor to result icon. The sunset image evolves from invalid visual at 00:11.792 to accepted emotional space at 01:53.458.

## D9. Creator image philosophy and master locks

- **Ideas per frame:** one primary claim, sometimes supported by one inset/comparator.
- **Density:** low on technical scenes, high only for painterly emotional scenes.
- **Negative space:** functional staging area for upcoming proof/text.
- **Subject scale:** large enough to read on mobile; variable remains most saturated.
- **Realism vs abstraction:** abstraction dominates; painterly realism is still stylized.
- **Text integration:** adjacent to its referent; exact numbers never separated from measurement geometry.
- **Asset/composition reuse:** extensive and intentional.

**MASTER CHARACTER LOCK:** featureless oval heads, thin irregular black limbs, no facial acting; preserve C02/C03 left-right identity.  
**MASTER OBJECT LOCK:** yellow/gray sun modules remain equal within a sequence; car design may simplify by context.  
**MASTER ENVIRONMENT LOCK:** white diagrams are textureless; dark/painterly scenes retain fixed palette and horizon.  
**MASTER GRAPHIC LOCK:** black arrows for object motion; coral for boundaries/verdict/direction; green only for valid.  
**MASTER TYPOGRAPHY LOCK:** hand-drawn uppercase; exact words/numbers as editor overlays.  
**MASTER COLOR LOCK:** near-white/black/gray base, saturated yellow hero, scarce coral/green semantics.  
**MASTER IMAGE STYLE LOCK:** irregular ink line, flat orthographic diagrams, no photorealistic depth unless rebuilding the painterly sunset plate.

## D10. Reusable creator formula

1. Ask one constrained question in the first sentence.
2. Define the measurable threshold before offering solutions.
3. Eliminate loopholes with rapid state replacements.
4. Scale from a local line to a globe/map only when causality demands it.
5. Introduce a benchmark before the final result.
6. Make the obvious strategy fail with one visible number.
7. Reset the palette and explain the winning mechanism in three steps.
8. Show method immediately before payoff.
9. Compare winner to benchmark in the same frame.
10. Return to an earlier image and change its emotional meaning for closure.

## D11. Ranked improvement system

### HIGH — Computational result is not independently reproducible

- **Works:** PyEphem + GPS traces arrive before the number.
- **Friction:** no date range, road constraints, route objective, terrain visibility, or search output is shown.
- **Why it may hurt:** technically demanding viewers cannot test `~95 min` from the video.
- **Minimal fix:** add a 2–3 line method card or pinned source link.
- **Aggressive alternative:** publish an interactive route map with date/speed inputs.

### HIGH — Terminator reversal is visually fast

- **Works:** NW and SW are both labeled.
- **Friction:** the slow/stop/reverse moment passes quickly and may require replay.
- **Why:** this is the least intuitive causal step.
- **Minimal fix:** hold the stopped boundary for ~0.5 s and highlight the pivot.
- **Aggressive alternative:** split V19 into two labeled panels: `BEFORE TURN` / `AFTER TURN`.

### MEDIUM — 355 mph claim needs local context

- **Works:** number is memorable.
- **Friction:** the derivation/latitude is not shown in the same state.
- **Why:** viewers may confuse it with a universal requirement.
- **Minimal fix:** add “northern mainland Norway” beneath the map point.
- **Aggressive alternative:** show a tiny speed-vs-latitude curve.

### MEDIUM — Early gag chain is longer than minimum

- **Works:** closes objections and builds voice.
- **Friction:** V06 alone contributes little explanatory value.
- **Why:** a highly impatient viewer may perceive repetition.
- **Minimal fix:** trim square hold by ~0.2–0.3 s.
- **Aggressive alternative:** combine V06/V07 into one faster transform.

### OPTIONAL — Final comparison could foreground “+40 min”

- **Works:** 95 and 55 are both visible.
- **Friction:** viewer performs subtraction.
- **Minimal fix:** add a small `+~40 min` brace between panels.
- **Aggressive alternative:** animate the 55-minute bracket stretching to 95.

## D12. New-topic translation

The safe translation is structural, not literal. Example new topic: **“How long could you stay inside a solar-eclipse totality shadow while driving on legal roads?”** The facts below are placeholders requiring fresh astronomical/road verification.

| Original production function | Original mechanism | New-topic equivalent |
|---|---|---|
| Constrained hook | sunset + legal road/speed | totality + legal road/speed |
| Define threshold | first horizon contact → full disappearance | full photosphere covered → first reappearance |
| Reject loopholes | hills/clouds/apparent sunset | cloud obstruction/partial eclipse does not count |
| Tempting solution | chase west by aircraft | chase umbra by aircraft |
| Geography principle | rotation speed falls toward poles | umbra ground speed/direction varies by path geometry |
| Road benchmark | Longyearbyen ~55 min | best single roadside totality duration |
| Obvious strategy fails | `355 mph` | local umbra speed exceeds road limit |
| Better mechanism | reversing terminator; wait/north/south | exploit a road nearly tangent to the shadow path or a slower path segment—only if verified |
| Proof | PyEphem + Norwegian GPS traces | eclipse ephemeris + legal-road graph + speed limits |
| Payoff | `~95 min` vs `~55 min` | computed route duration vs stationary benchmark |
| Emotional coda | spin for a nanosecond | a tiny verified physical trick or human reason to stay |

**Keep:** question→definition→failed strategies→benchmark→reversal→method→number→comparison→callback; white/gray/yellow/red grammar; one moving variable; exact map overlays.  
**Change:** every fact, path, location, number, character/object surface, and physical mechanism.  
**Rule:** copy the production grammar, not the sunset content or an unverified reversal.

## D13. Zero-to-final rebuild workflow

1. Confirm title promise and road/speed constraints.
2. Transcribe narration and split it into the 14 causal beats above.
3. Storyboard one visual claim per beat; reserve high-color scenes for two pattern interrupts and the ending callback.
4. Build master assets: sun symbol, gray end state, verdict marks, C01/C02/C03, car family, globe, Scandinavia map, PyEphem research set, E02 sunset plate.
5. Lock 720×1280 canvas, palette, line weight, text family, and sun diameter.
6. Build clean static plates first; keep text separate.
7. Construct white horizon sequences using duplicated sun precomps and arrows.
8. Build globe/map scenes with deterministic vectors, masks, and path constraints.
9. Animate one information hero per state; freeze prior evidence.
10. Add exact labels/numbers only at their spoken trigger words.
11. Assemble the 18-shot EDL using frame-verified boundaries as timing references, then retime only if redesigning.
12. Integrate narration; do not assume music/SFX from the source mix.
13. Add the 55-minute benchmark before the 355-mph failure and 95-minute payoff.
14. Preserve the 95-minute panel when revealing the 55-minute comparator.
15. Reuse the painterly sunset plate for the coda; separate C03 for spin animation.
16. Add dialogue as editor text, preserve line breaks, and hold through the final audio fade.
17. QC: object counts, yellow/gray semantics, car/map registration, text accuracy, NW→SW order, counterclockwise direction, final silence.
18. Export H.264 Rec.709, 720×1280, 24 fps; verify duration and audio tail after encoding.

---

# Completeness audit

| Requirement | Result |
|---|---|
| Media inspection | Complete |
| Total major shots | 18 |
| Total visual states | 34 |
| Script beats analyzed | 14/14 |
| Packaging promise | Title analyzed; thumbnail unavailable |
| Script consensus | Complete |
| Visual states grounded | 34/34 |
| Spatial maps | 34/34 |
| Attention analysis | 34/34 |
| Visual information value | 34/34 |
| Object lifecycles | 3/3 principal applicable systems |
| Cross-frame drift audit | Complete |
| Reconstruction cards | 34/34 |
| Standalone image prompts | 34/34 |
| Text bake/overlay decisions | 34/34 |
| Fidelity locks | 34/34 |
| Moving visual states | 30; four intentional static holds |
| Motion forensics | 34/34, including stillness decisions |
| Why-move/why-static | 34/34 |
| Motion-cue checks | 34/34 |
| Best production method | 34/34 |
| AI suitability | 34/34 |
| Animation prompts | 34/34 |
| Animation prompts ≤500 | 34/34 after programmatic count |
| First/last-frame decisions | 34/34 |
| Visual-state transitions | 33/33 |
| Edit decision list | Complete |
| Audio | Complete with limitation: mixed track, no stems |
| Thumbnail candidates | 3 |
| Shorts candidates | 4 |
| Next-video bridge | Complete |
| Zero-to-final workflow | Complete |
| New-topic translation | Complete |

## Evidence limitations

1. The supplied file contains no separate thumbnail, description, source project, layer files, route data, or code; those cannot be reconstructed as facts.
2. Music/SFX cannot be separated from the stereo mix; only the narration-dominant mixed audio was measured.
3. Original software, brushes, easing curves, exact color values, and creator intent are unverified. Recommended methods are reconstruction choices.
4. The 95-minute claim is analyzed as presented; independent scientific validation would require the underlying search inputs and code.

## Final quality gate

The report identifies the hook, causal spine, loops, payoff ladder, title fulfillment, all major visible states, spatial relationships, attention hierarchy, callbacks, lifecycles, continuity issues, standalone image prompts, exact moving/static channels, temporal order, deterministic production methods, edit logic, audio timing, extraction candidates, reusable grammar, and a new-topic translation. A competent scriptwriter, storyboard artist, illustrator, motion designer, and editor can rebuild the production logic without inventing a new visual system.
