# Visual DNA — what_if_the_moon_were_made_of_protons

Global, evidence-supported production patterns. Scene-specific detail lives in `TIMELINE.csv`; this file records only what repeats across shots. IDs reference `ASSET_MANIFEST.csv` / `MOTION_EVENTS.csv`.

## CHARACTER DNA
- Repeated rule: a single plain white-outline stick figure (C01) — round bald head, no facial features beyond simple eyes/mouth marks, thin limb lines — represents the narrator/reactor throughout the diagram-heavy first two-thirds of the video (S01, S02, S04).
- Exceptions or limits: a second, visually distinct stick figure (C02, wavy/curly hair) appears once, only in S08, for a single joke aside. No other characters appear.

## ENVIRONMENT DNA
- Repeated rule: two background families alternate — (a) a flat white "whiteboard" canvas (E01) for scientific-diagram shots, and (b) a black background (E03 explosion / E05 starfield) for the more dramatic/cosmic beats. A third, one-off grey palette (E04) marks the single "real-world consequence" cutaway (S07).
- Exceptions or limits: E02 (ground/horizon line) appears only once, layered onto E01 for S04.

## OBJECT / GRAPHIC DNA
- Repeated rule: every concept is illustrated with a self-contained hand-drawn-style vector icon (circles, dashed orbit rings, arrows, funnels) labeled with small black text; icons are rarely reused verbatim but repeat a consistent "circle + label" visual grammar (G02/G03/G08/G11 all use a circle-plus-caption pattern; G05/G12/G16 all use an arrow-or-funnel-plus-label pattern).
- Exceptions or limits: G08 ("ELECTRON MOON") is the only icon drawn twice at different scales (full-size in S05, miniature in S06) — a deliberate callback rather than a new design.

## COLOR PALETTE
- Repeated rule: near-monochrome black/white/grey linework throughout, with a single reserved accent color — red — used exclusively for two purposes: (1) rejection/annotation marks (G04) and (2) all "aside" caption text (T01: "200,000 MOLES OF MOLES", "DARK ENERGY", "WHAT A BEAUTIFUL DAY", "HO HUM", "LA LA LA").
- Exceptions or limits: none observed; red never appears on any core diagram label (T03) or dialogue caption (T02).

## LIGHTING
- Not applicable in the photographic sense — all content is flat vector/sketch illustration. "Lighting" is simulated only via background value: bright/white diagram shots vs. a bright radial flash (S02) vs. solid black (S08/S09).

## CAMERA / FRAMING
- Repeated rule: every shot uses a static, locked camera — no pans, zooms, or parallax were observed anywhere in the video. All apparent scale change is achieved by redrawing/regenerating graphic elements at a new size (e.g., the growing cloud in S04, the growing circle in S09), never by moving a virtual camera.
- Exceptions or limits: none. This holds for all 9 shots without exception.

## COMPOSITION
- Repeated rule: diagram shots are typically composed with the primary graphic in the upper-to-middle portion of the tall 9:16 frame and any caption/character content below it, leaving generous white/black negative space around the edges.
- Exceptions or limits: S07's collapse illustration and S09's growing circle both intentionally break this by using more of the full frame as the shot progresses.

## TYPOGRAPHY
- Repeated rule: three consistent text roles are held throughout — red hand-drawn-style captions (T01) for narrator asides/jokes, black plain captions (T02) for character dialogue, and small black label text (T03) integrated directly into each diagram. No other font families or colors are used for text anywhere in the video.
- Exceptions or limits: none.

## GRAPHICS
- Repeated rule: every major concept gets one dedicated icon (see Object/Graphic DNA); icons are additive within a shot (new elements appear alongside old ones) rather than being redrawn from scratch, except at hard shot cuts.
- Exceptions or limits: none beyond the G08 reuse noted above.

## ILLUSTRATION / STYLE
- Repeated rule: loose, hand-drawn/sketch vector illustration style throughout (visible line waver, no photographic or 3D-rendered elements) — consistent with a "science explainer" whiteboard-doodle aesthetic.
- Exceptions or limits: none.

## DEPTH
- Repeated rule: all content is flat 2D with no simulated depth-of-field, parallax, or perspective camera; the "stretched fabric" graphic (G10) and "funnel" graphic (G12) simulate depth *within* a flat illustration (a drawn 3D-looking well), not via any camera or layering technique.

## MOTION LANGUAGE
- Repeated rule: motion is almost always either (a) a graphic element being drawn on/revealed (text pop-ins, rejection scribbles, new icons appearing) or (b) a single icon growing/expanding/radiating in place (field lines, cloud growth, starburst, circle growth). No independent camera motion, parallax, or multi-object choreography was observed anywhere.
- Exceptions or limits: A02 (S02) is the only shot with any character-body motion (a small recoil/crouch), and even that is a minor, brief gesture rather than sustained movement.

## TRANSITION LANGUAGE
- Repeated rule: every shot boundary in this video is a hard CUT; no dissolves, wipes, or other transition effects were observed or detected by the scene-cut filter at either threshold.
- Exceptions or limits: none — all 8 shot boundaries are confirmed hard cuts (see `TIMELINE.csv` TRANSITION_IN/OUT columns).

## ASSET REUSE PATTERN
- Repeated rule: most graphics (G01–G07, G09–G15) are single-use, purpose-built for one shot's specific beat; only the character (C01), the three text systems (T01–T03), the "ELECTRON MOON" icon (G08), and the background families (E01, E05) recur across multiple shots.
- Exceptions or limits: this is a lower-reuse video than a typical talking-head or recurring-set explainer — nearly every shot introduces at least one new bespoke diagram, reflecting its fast-moving, joke-a-beat comedic-explainer structure.

## Evidence and measurement conventions
- All 8 shot boundaries are OBSERVED via `ffmpeg` scene-cut detection (5 at threshold 0.25, 3 additional at threshold 0.10); see `00_source/SOURCE_MANIFEST.md`.
- All internal visual-state boundaries and all motion timings were derived from 1-second-interval frame sampling (not exhaustive per-frame verification) and are labeled LIKELY in `TIMELINE.csv` / `MOTION_EVENTS.csv` accordingly.
- No camera movement, easing curve, exact font, exact music/SFX, or original authoring tool is claimed anywhere in this analysis.
