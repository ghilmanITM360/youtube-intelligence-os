# Visual DNA — what_would_a_magnitude_15_earthquake_be

Global, evidence-supported production characteristics. Scene-specific detail lives in `TIMELINE.csv`; do not repeat it here.

## CHARACTER DNA
Stick figures throughout: plain circle head (no facial features except in a couple of speech-bubble reaction beats), thin single-stroke limbs, no color fill. Identical drawing convention to the host character in every other video already reconstructed in this project. Secondary animals (cat, dog, mouse) use the same simple single-stroke line-art convention, no shading. — OBSERVED

## ENVIRONMENT DNA
Backgrounds are almost always a flat off-white/light-gray canvas with no horizon or setting except where the gag specifically requires one (the newspaper's cornfield inset, the outdoor tree scenes). No parallax layers, no depth-of-field. — OBSERVED

## OBJECT DNA
All illustrated objects (globe, sun, seismograph, truck, furniture) are simple black-outline line art on the same flat canvas, redrawn/modified in place rather than replaced with a differently-styled asset when their state changes (e.g. the globe gains cracks and a debris ring but keeps the same base silhouette). — OBSERVED

## COLOR PALETTE
Overwhelmingly black-line-on-off-white, matching the rest of the project's "xkcd what if" videos. Two deliberate color accents: red, used exclusively for (a) the "xkcd's what if?" bumper/credits card background and (b) hand-scribbled emphasis marks (Richter Scale strikethrough, ruler tick marks, quake epicenter rings). No other color appears. — OBSERVED

## LIGHTING
Flat, shadowless line-art throughout; no rendered lighting model. — OBSERVED

## CAMERA / FRAMING
Every shot is a locked, static 2D camera — no pans, zooms, or parallax were measured anywhere in the video. All apparent "movement" is the illustrated subject changing (label swaps, object animation, particle motion), not camera motion. — OBSERVED

## COMPOSITION
Consistent single-focal-point compositions: one dominant illustration per state, usually paired with a large "MAGNITUDE ##" headline directly above it, and a persistent vertical reference ruler at frame-left for most of the ascending/descending sequence (S05–S12). — OBSERVED

## TYPOGRAPHY
Two font treatments: (1) a bold, slightly hand-drawn-style sans-serif for the "MAGNITUDE ##" headlines and most captions; (2) a looser, more hand-lettered style for onomatopoeia/sound-effect text (WHUMP, CRASH, PLINK, CLICK, KERTHUMP). Intro question text and LIVE-TV captions sit in light-gray rounded rectangles / black-bordered boxes respectively. — OBSERVED

## GRAPHICS
Recurring motifs: the vertical "Moment Magnitude" ruler (present from S05 through S12, growing then implicitly continuing off-frame during the descending scale), red hand-scribble emphasis marks, cloud-shaped thought bubbles, small radiating shake-line clusters for impacts, and a reusable explosion-burst graphic (appears 3 times: NYC example, Earth breakup, sun/Magnitude 25). — OBSERVED

## ILLUSTRATION / 3D STYLE
Pure 2D hand-drawn vector/line-art style; no 3D rendering anywhere, including the "3500 km" tectonic block diagram, which is drawn in a flat isometric-style illustration rather than true 3D. — OBSERVED

## DEPTH
No true depth layering; foreground/background separation is implied only by relative scale and left/right placement, not by parallax or blur. — OBSERVED

## MOTION LANGUAGE
Two motion categories only were measured: (1) instantaneous full-composition swaps between magnitude values (the dominant pattern — see `MOTION_EVENTS.csv` RELATIONSHIP=STATE_REPLACEMENT rows), and (2) genuine continuous motion reserved for specific illustrated physics — falling objects (leaf, feather, cat), particle flow (hourglass sand, debris cascade), and explosive/fracturing expansion (Earth breakup, sun burst, magnetar field-line pulse). No decorative camera motion, parallax, glow, or idle-loop animation was found anywhere; none should be added in reconstruction. — OBSERVED

## TRANSITION LANGUAGE
All 16 shots are joined by hard cuts (`ffmpeg scdet` score ≥5.4 at every shot boundary) except the final shot change into the ending vignette, which uses a brief (~1s) full black-screen wipe (S14→S15 via S15/F15.0). No cross-fades or dissolves were measured. — OBSERVED

## ASSET REUSE PATTERN
Heavy reuse of a small set of recurring assets across otherwise distinct states: the host stick figure (C01), the vertical ruler (O05), the globe (E03, reused with escalating damage states), the sun (O07, reused with escalating states), the explosion-burst graphic (G03), and the debris/fragment graphic (G04). The "MAGNITUDE ##" text system (T01) is the single most-repeated element in the entire video, appearing in nearly every state. See `ASSET_MANIFEST.csv` OTHER_APPEARANCES column for the full reuse map. — OBSERVED
