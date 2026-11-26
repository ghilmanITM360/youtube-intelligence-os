# Scientific illustration research — V10

**Method.** A research subagent used web search and opened the pages in the built-in browser. WebFetch returned only alt text for the NASA pages and a 403 for Physics Classroom, so the full-size figure files were opened and looked at directly. The xkcd What If frame sheets and the HumanCraft rules come from the V9 study (`../v9/research/REFERENCE_STUDY_V9.md`, `../v9/research/xkcd_sheets/`); that study was re-read for V10 rather than repeated. **Not examined:** BBC Bitesize (blocked), the Save My Exams figure (only navigation loaded), HyperPhysics, OpenStax, PhET. No source artwork was copied; every V10 diagram is drawn from `tools/model.py` in our own grammar.

## What each source actually shows

| Source | Figure as seen | Convention | What V10 took from it |
|---|---|---|---|
| [NASA Glenn: Falling Object with Air Resistance](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/falling-object-with-air-resistance/) | Beach ball, Drag arrow up from the top, Weight arrow down from the bottom, roughly equal; W = mg, D = Cd·ρ·V²·A/2, a = (W − D)/m; "When Drag is equal to Weight, acceleration is zero." | One object, arrows from the surface, equations alongside | STATE 2 (balanced at top speed: acceleration zero, still moving down) and the sign flip of a = (W − D)/m as STATE 3 |
| [NASA Glenn: Drag Equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) | Airliner; the equation with a word version underneath, with "density × velocity squared" underlined | Words under the symbols | Density and speed each get their own dedicated composition (I1 and J1), not a footnote |
| [NASA Glenn: What is Drag?](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-drag/) | Four forces on an aircraft; drag is the only red arrow | One colour per force | Fixed colours: weight rust, drag teal, velocity dashed blue, net force violet double shaft, airflow pale-blue dashes |
| [Physics Classroom: Free Fall and Air Resistance](https://www.physicsclassroom.com/class/newtlaws/u2l3e) | Skydiver diagrams A–D: Fgrav 833 N constant; Fair 0 → 350 → 700 → 833 N; D = terminal velocity | Row of free-body snapshots, weight arrow fixed | V10 extends this row with **STATE 3, drag > weight**, which the textbook row does not include. Weight length is constant throughout. |
| [Physics Classroom: Ticker Tape Diagrams](https://www.physicsclassroom.com/class/1DKin/U1L2b) | Strips: constant speed has even gaps; accelerating has widening gaps; the text says slowing shows shrinking gaps | Equal-time dots; spacing encodes speed | L1 equal-time positions: model positions every 15 s, gaps shrink, every mark is lower than the last |
| [NASA Glenn: Earth Atmosphere Model](https://www.grc.nasa.gov/WWW/k-12/airplane/atmosmet.html) | Sky gradient by altitude, troposphere equations, ρ = p / (0.2869·(T + 273.1)) | Altitude bands | The same troposphere fit is the one in `model.py`. Density boxes use ρ(h) from it. |
| [NASA Glenn: Shape Effects on Drag](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/shape-effects-on-drag/) | One "Flow" arrow plus silhouettes with Cd values, "same frontal area" | A single relative-flow arrow; shape is the variable | Posture held fixed through the model section ("body position held fixed"), so the slowdown cannot be credited to a shape change |
| [Red Bull Stratos (Wikipedia)](https://en.wikipedia.org/wiki/Red_Bull_Stratos), [Guerster & Walter, PLOS ONE 2017](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0187798) | Timeline: after the speed peak, air resistance slows the jumper "as the atmosphere becomes denser"; Fig 1 plots velocity, altitude and density over time | Real measured trajectory | Confirms the phenomenon is real. It is **not quoted on screen**, because that jump (39 km) is a different regime from our 10 km model. |

**Misconception noted** (Save My Exams search snippets): the standard school speed–time graph has a sharp drop when the parachute opens, and students sometimes think the skydiver moves upward. V10's graph has no parachute event. It labels "slowing, still falling" and keeps speed positive.

## Design principles applied in V10

1. **One fixed weight length.** Only drag changes, and both arrows use one scale (118 units = weight).
2. **Magnification is a zoom, not a second arrow.** The difference between drag and weight is 0–3.5%, so a lens circle zooms 10× onto the arrow tips. Inside the lens are the weight-length reference, the drag tip and the gap (net force), labelled "zoomed in 10x". This replaces V9's net-force box, which sat beside the arrows as if it shared their scale.
3. **Show density and the speed dependence on their own full-frame compositions,** at a readable size, instead of small boxes inside the force scene.
4. **Keep the controlled comparison (same air, same body, two speeds) separate from the main descent,** where density changes. The comparison is labelled as such and drawn on a paper card, not over the falling world.
5. **Show motion and net force as separate quantities in separate places:** "MOVING: DOWN" with marching dashes, and "NET FORCE: UP".
6. **The graph only summarises what was already shown,** and has no decorative dashed lines. The alternative curves appear only at the end, labelled as other model inputs.
