# Scientific visual QA — V11

## Model (unchanged, rerun)

The model is `tools/model.py`, unchanged since V9/V10:
- fixed posture, m = 80 kg, CdA = 0.5 m²
- NASA Glenn troposphere density fit

The self-check passes on the final render (`qa/render.log`):
- model time monotonic
- v ≥ 0 and altitude never rises
- the needle never rises after 47.7 s
- v > 0 once falling
- minimum altitude 445 m (no ground contact shown)

Key values:
- **peak:** 81.0 m/s at model 20 s
- **largest drag-to-weight ratio:** D/W = 1.035
- **near the end:** about 51 m/s

No numbers appear on screen. The V8 exaggerated drag-to-weight ratio is **not** used. The ×30 close-up is labelled as a zoom, not presented as the real ratio.

## Progression A–G (brief §11), as shown

| Step | Where | How |
|---|---|---|
| A. Weight exceeds upward drag | H1, K1 card (STATE 1) | Common scale on the body. On the card the drag tip sits below the "weight's length" line, with "net force: down". |
| B. Downward speed increases | H1 | Dashed "downward speed" arrow lengthens; wrist needle rises |
| C. Equal at peak speed | K1 card at 43.6 s | Drag tip on the line: "balanced: top speed". Wrist inset on the card at its highest. |
| D. Drag exceeds weight | K1 card after 43.6 s; Q2 card | Drag tip above the line: "drag bigger than weight" |
| E. Net force points up | K1/Q2 card, L1 | Violet double-shaft "NET FORCE: UP", always on a zoomed card or schematic, never beside the true-scale arrows |
| F. Velocity still downward | K2, L1, Q2 end | "still moving DOWN" dashed arrow back on the body; "MOVING: DOWN" with marching dashes |
| G. Downward speed decreases | L1 right column, M1, N1, Q1 | Gaps shrink, the speed arrow shortens, the needle falls, the graph declines |

Statements on screen stay inside the model: "MODEL · fixed posture · time compressed", "SIMPLIFIED MODEL", "not a prediction for a real person". Gravity is never shown switching off; the weight arrow is the same length throughout. The parachute stays closed and is labelled "still closed".

## Magnified force explanation (brief §12)

Both K1 (38.7–47.7 s) and Q2 (66.0–70.5 s) follow the same five steps, and **elements replace each other instead of piling up**:

1. Weight and drag from the centre of mass on **one common scale** (118 units = weight).
2. A ring on the two tips: "tiny difference here".
3. A circular reveal into a full-frame card: "CLOSE-UP OF THE ARROW TIPS · zoomed 30x" and "not the same scale as the body diagram". The gap is (D/W − 1) × 118 × 30 units, taken from the model.
4. The violet NET FORCE: UP arrow appears beside the drag tip.
5. Back to the body, showing only the dashed DOWN velocity arrow.

The V10 1:08 composition is gone. It had a speed card, lens inset, three arrows, multiple labels and gridded ground all at once (see `qa/before_after/1m08.png`).

## Equal-time positions (brief §13)

There are two columns of model positions:
- **"earlier: speeding up"** (model 0–20 s, a mark every 4 s): gaps grow.
- **"now: slowing down"** (30–150 s, every 15 s): gaps shrink by about 31%. They build one by one.

Every mark in both columns is lower than the one before. "MOVING: DOWN" and "NET FORCE: UP" sit beside the slowing column.

**Limitation:** each column uses its own vertical scale and its own time step (both labelled). One shared scale would make the early column too short to read. This is a deliberate, stated simplification.

## Speed graph

- The graph summarises the same story: speeding up, top speed, "slowing, still falling", and "never reaches zero before the ground". The label collisions are fixed: "speeding up" moved to the inside, and "slowing, still falling" moved below the curve.
- S1 alternative-input curves are labelled at their ends: "smaller drag area" above the faster curve, "larger drag area" below the slower one. Both come from `model.py` with CdA × 0.7 and × 1.6. They are illustrative and not tied to a specific posture.

## Airflow (brief §10)

**Research this round:**
- NASA Glenn Beginner's Guide: [definition of streamlines](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/definition-of-streamlines). A streamline is tangent to the flow velocity, and diagrams are drawn "moving with the object".
- NASA Glenn [relative velocity / reference frames](https://www.grc.nasa.gov/WWW/k-12/airplane/move.html). The forces are the same whether the object moves through still air or the air moves past the object.
- Found by search only, contents not read: NASA's ["short" page](https://www.grc.nasa.gov/WWW/k-12/airplane/short.html).

**Applied:**
1. The frame is stated first: "you: moving down".
2. Then the flow in the body's frame: "so the air rushes UP past you".
3. Lines are streamline-shaped, curving around the body (a potential-flow-around-an-ellipse sketch), with travelling chevrons pointing up.
4. Lines exist only near the body and fade at their ends, so they do not read as rain or background texture.
5. They are drawn behind the figure.
6. Colour is pale steel-blue at 1.3 px, distinct from the solid force arrows and the dashed velocity arrow.

It is labelled **"relative airflow · simplified sketch"**. **No aerodynamic simulation was performed.** The shape is a textbook potential-flow schematic, not a computed flow around a human body.

## xkcd What If / HumanCraft (brief §14)

I did **not** re-review the reference sequences in this round. V11 applies the principles already recorded in V10's `SCIENTIFIC_ILLUSTRATION_RESEARCH.md`:
- one idea per frame
- negative space
- restrained colour
- motion that carries meaning
- labels close to their objects
- no dashboard UI

No competitor characters or compositions were copied. The decluttered K1/Q2 and the cards follow these rules. The device inset and graph card are the most "interface-like" elements left.

## Muted reading test

From the contact sheet (`qa/V11_contact_1p5s.png`) with no audio, the sequence reads:

1. aircraft + "you"
2. closed pack
3. gravity
4. glance → wrist with SLOW/FAST dial
5. surprised face
6. same pull
7. you move down → air rushes up
8. model at rest, needle zero
9. thin air
10. weight > drag, speeding up
11. three densities
12. same air, twice the speed ≈ 4× drag
13. same-scale forces → tiny difference → zoom card: drag smaller → balanced → bigger, net UP
14. still moving DOWN
15. speeding up vs slowing down marks
16. speed decreasing → glance → own wrist, needle dropping → ground closer
17. still closed
18. graph
19. forces → zoom → still moving down
20. simplified model
21. other inputs

Speed (dashed blue, DOWN) and net force (violet double shaft, UP) are never the same glyph.

## Remaining scientific-visual issues

- The ×30 card shows the drag shaft very wide (magnified). That is correct for a zoom, but it could still be misread as "drag is huge". The on-card text addresses it.
- The two-scale equal-time diagram (above).
- Footnotes ("dots are marks, not molecules", "relative airflow · simplified sketch") are 9.5 units (28 px). They read on a phone, but only just.
