# Visual DNA — how_long_could_you_drive_towards_the_sunset

Global, evidence-supported production characteristics. Scene-specific detail lives in `TIMELINE.csv`/`ASSET_MANIFEST.csv`; this file states only repeated rules and their exceptions.

## CHARACTER DNA
- Repeated rule: humans are rendered as minimal stick figures — a plain circle head with no facial features and thin line limbs (C01), used identically as a reader, desk-worker, and pedestrian.
- Exceptions or limits: the camera-crew pair (C02) is a distinct, more detailed silhouette design (visible hair, tripod camera prop) reserved only for the two photographic-style sunset shots (S03, S14); it never appears in the flat-diagram shots.

## ENVIRONMENT DNA
- Repeated rule: two visually distinct backdrop families recur — (1) a plain white canvas for schematic/diagram shots, and (2) painterly gradient-sky backdrops for "real-world" location shots (E02 polar dusk, E07 ocean sunset).
- Exceptions or limits: E01 (chalkboard) and E05 (office desk) and E06 (church) are unique single-shot environments that don't recur or blend with the two main families.

## OBJECT DNA
- Repeated rule: the sun/shadow relationship is always drawn as a small flat yellow circle (G01) paired with a small flat grey circle (G02), regardless of which larger diagram it appears in (horizon chains, mountain rolls, recap insets, map legends).
- Exceptions or limits: in the two full-scale "real" location shots (S07, S08) and the two photographic sunset shots (S03, S14), the sun is instead rendered as a larger illustrated/painterly disc, not the small flat schematic circle.

## COLOR PALETTE
- Repeated rule: diagram shots use a restricted grey/black/white/yellow palette (white canvas, black line art, yellow sun accents, grey shadow accents), with red reserved exclusively for rejection marks (X), directional arrows, and callout labels.
- Exceptions or limits: the two photographic sunset shots (S03, S14) and the two polar establishing shots (S07, S08) use a full painterly gradient palette (deep blue/purple night sky through red-orange-yellow sunset colors) that departs from the flat diagram palette.

## LIGHTING
- Repeated rule: diagram shots are flat and shadeless (no rendered light source other than labeled sun/shadow icons).
- Exceptions or limits: the photographic/painterly shots (S03, S07, S08, S14) simulate directional light via gradient skies and a glowing sun disc with a water/ice reflection.

## CAMERA / FRAMING
- Repeated rule: every shot in this video uses a static, locked camera — OBSERVED across all 14 shots; no pans, zooms, or tracking moves were detected anywhere in the source.
- Exceptions or limits: none observed. (The apparent "movement" in several shots — cars, sun circles, terminator arrows — is graphic-element motion within a fixed frame, not camera motion.)

## COMPOSITION
- Repeated rule: diagram shots are built around a single dominant horizontal reference line (a horizon line, a globe terminator, or a map's day/night band) with graphic elements arranged along or around it.
- Exceptions or limits: the chalkboard shot (S01) and photographic shots (S03/S14) are composed as full-bleed single-subject frames rather than around a horizontal reference line.

## TYPOGRAPHY
- Repeated rule: all on-screen text is a single consistent white, hand-lettered/rounded sans-serif caption style, used for location labels, data callouts, and dialogue.
- Exceptions or limits: none observed — caption styling is uniform across all shots that carry text (S03, S05-S14).

## GRAPHICS
- Repeated rule: rejection/confirmation is always communicated with a red hand-drawn X (wrong) or green check mark (right), never with color grading, sound stingers alone, or a spoken-only "no."
- Exceptions or limits: none observed.

## ILLUSTRATION / 3D STYLE
- Repeated rule: flat 2D vector/line-art illustration dominates (chalkboard, all circle/horizon diagrams, map shots, desk/church shots).
- Exceptions or limits: S06 uses a pseudo-3D wireframe/graticule globe render (grid lines suggesting a sphere in perspective) — the only shot with any implied 3D depth; S03/S07/S08/S14 use painterly/gradient rendering rather than flat vector fills.

## DEPTH
- Repeated rule: diagram shots are single-plane (foreground graphics directly on a flat background, no midground layer).
- Exceptions or limits: the photographic sunset and polar-location shots (S03, S07, S08, S14) use a simple foreground/background depth split (silhouette figures or vehicles in front of a gradient sky/horizon).

## MOTION LANGUAGE
- Repeated rule: nearly all motion in this video is graphic-element reveal/build (objects, arrows, and captions being progressively drawn onto an otherwise static frame) rather than continuous physical animation; OBSERVED across S02, S04-S06, S08-S14.
- Exceptions or limits: S01's globe spin, S04's mountain-roll gag, and S10/S12's car-advancing-along-a-path are the only cases of an element continuously translating/rotating rather than simply appearing.

## TRANSITION LANGUAGE
- Repeated rule: shot changes are hard cuts (OBSERVED via the `ffmpeg` scene-change filter for 11 of the 13 inter-shot boundaries).
- Exceptions or limits: two boundaries (S07→S08 and S13→S14) were not flagged by the automated scene-change detector despite a clear visual content change; these are labeled LIKELY DISSOLVE / LIKELY CUT respectively in `TIMELINE.csv` based on direct frame comparison rather than the detector.

## ASSET REUSE PATTERN
- Repeated rule: the small schematic sun/shadow circle pair (G01/G02) and the horizon-line motif (G03) are the throughline connecting nearly every diagram shot (S02, S04, S09, S10, S12, S13); the video's two "bookend" photographic sunset shots (S03, S14) reuse the exact same background plate (E07) and character pair (C02).
- Exceptions or limits: the North Pole (S07) and Longyearbyen (S08) establishing shots share a sky-gradient language (E02) but do NOT share foreground assets — each has its own unique vehicle and background silhouette.

## Evidence and measurement conventions
- All timing is expressed in frames at the source's true constant frame rate: 24fps, 3117 total frames, 129.875s video duration.
- Shot/state boundaries were established primarily from 130 source-resolution 1fps frame extractions, cross-checked against `ffmpeg` scene-change detection at thresholds 0.25 and 0.10. Two shot boundaries were not confirmed by the automated detector (see Transition Language above) and are marked LIKELY rather than OBSERVED for their exact frame-level cut point; all other boundaries are OBSERVED at 1-second precision.
- Long/continuous motions (A09 mountain roll, A24 car-and-legend advance) were confirmed smooth and single-direction via 1s interval sampling, not exhaustive native-frame verification; their internal easing/pacing is LIKELY steady rather than confirmed exact.
