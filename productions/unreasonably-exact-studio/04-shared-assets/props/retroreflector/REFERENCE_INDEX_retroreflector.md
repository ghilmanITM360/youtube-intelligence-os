# retroreflector references (saved locally; reference use only, never in the film)

## REF-OPT-024  `optical_diffuse_scatter_reflection_wikimedia_diffuse-reflection1_render.png`
- source: https://commons.wikimedia.org/wiki/File:Diffuse_reflection1.svg (Wikimedia Commons / DnaX)
- licence: CC_BY_SA_4.0 DnaX (Wikimedia Commons), CC BY-SA 4.0
- perspective: 2-D schematic: incident ray from the upper left onto a grainy surface, rays scatter in all directions
- what is visible: 2-D schematic in white with a grey polygon-grain surface at the bottom: a thick black incident-light arrow runs from the upper left down onto the surface, several blue 'primary' rays and cyan 'secondary' rays with filled arrowheads leave the surface in many different directions (some back up-left, some up-right) and a small fan of five open arrows at the upper right is labelled 'Scattered light'; legend dots for primary and secondary rays. Crisp vector lines, no shading.
- influences: Confirms OPT_007 grammar: a black incident arrow, blue/cyan scattered rays leaving at many angles and a small fan of open arrows labelled Scattered light; surface drawn as grey polygon grains.
- assets: OPT_007_SCATTER

## REF-RETRO-014  `reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg`
- source: https://images.nasa.gov/details/NGLR Payload EDIT (NASA (Next Generation Lunar Retroreflector, NGLR-1))
- licence: PUBLIC_DOMAIN_NASA NASA
- perspective: close side/3-4 view at eye level, hardware on a bench or spacecraft deck, shallow depth of field
- what is visible: A cylindrical grey metal housing capped by a bright red plastic protective cover (covers the optical face), under which a downward-pointing conical/pyramidal lower body (the cube apex side) hangs; the housing is held by two grey aluminium A-frame side brackets with lightening cut-outs and a short pivot pin/knob on the left; the bracket sits on a dark deck with a gold polyimide foil edge; thin wires (one white, one fine black loop) run around it; blurred benches behind. The optical face itself is not visible.
- influences: Supports the depth of the cube in RETRO_003: the glass body is much deeper than the face and ends in an apex; a tilt pivot sits at the side of the mount (compare Apollo 14 tilt support).
- assets: RETRO_003_CUBE_CUTAWAY RETRO_004_FRAME_MOUNT

## REF-OPT-003  `optical_corner_cube_photo_gold_wikimedia_corner-cube.jpg`
- source: https://en.wikipedia.org/wiki/File:Corner-Cube.jpg (Wikimedia Commons / Kkmurray)
- licence: CC_BY_SA_3.0 Kkmurray / Wikimedia Commons, CC BY-SA 3.0
- perspective: 3/4 high angle looking into a black cylindrical mount, white background
- what is visible: A black anodised cylindrical housing with a square flange (two bolt holes at the bottom corners). Inside the round opening, a dark amber-gold interior with three thin bright seam lines meeting near the lower centre, and an irregular many-sided aperture edge at upper left. Glassy dark-gold look, speckle dust on the faces, no sharp reflections of the environment. Hollow, first-surface mirror type (per the file description), not a solid glass prism.
- influences: B19: the macro push into one cube should end on the apex with three seams meeting, not on a plain glass disc. Solid fused-silica Apollo cubes are glass (C05); this hollow gold one is a different construction, so use it for the seam geometry only.
- assets: OPT_004_CORNER_PATHS RETRO_000_SYSTEM RETRO_003_CUBE_CUTAWAY RETRO_005_CUBE_3FACE

## REF-OPT-004  `optical_corner_cube_three_reflections_animation_wikimedia_reflection-coin-cube-rot.gif`
- source: https://en.wikipedia.org/wiki/File:Reflection-coin-cube-rot.gif (Wikimedia Commons / V.pantaloni)
- licence: CC_BY_SA_4.0 V.pantaloni / Wikimedia Commons, CC BY-SA 4.0
- perspective: animated, camera orbits a transparent cube while a red marker travels along a ray
- what is visible: Frames sampled (every 1 s, 12 tiles, contact sheet in research/video_analysis/gif_corner_cube_wikimedia/). Black background, grey cube drawn as three visible faces with white edges, later turned semi-transparent. A thick yellow polyline ray enters from the top, kinks at three faces and leaves upward again; a red ball rides the head of the ray and leaves a yellow trail. Later frames add a second parallel entering ray and rotate the view to a side-on angle where the two rays are visibly parallel and the faces form a corner. 151 frames, 10.6 s.
- influences: B20: leading dot + persistent trail is the clearest way to show path order; rotate the view once to prove parallelism, or show two entering rays together (see sampled frames).
- assets: OPT_004_CORNER_PATHS

## REF-OPT-005  `optical_apollo_photon_histogram_apollo-collab_lunarphotons.png`
- source: https://en.wikipedia.org/wiki/File:LunarPhotons.png (APOLLO Collaboration (via Wikimedia Commons))
- licence: CC_BY_3.0 APOLLO Collaboration, CC BY 3.0 (via Wikimedia Commons)
- perspective: 2-D data plot: x = time (minutes), y = time into the detector gate (ns)
- what is visible: White background, small black dots. Title '8 December 2005'. X axis 'time (minutes)' 0 to about 12.5; Y axis 'time into gate (nanoseconds)' 0 to 120. Roughly 2,500 dots scattered uniformly over the whole area (background), plus a dense, perfectly horizontal heavy line of dots at about 46 ns running the whole width with two or three short gaps (around 4 min, 9.5 min). The signal is a flat band at constant arrival time; the background is evenly scattered.
- influences: B26-B27/B29b: build the 'signal emerges' scene as dots on a time-into-gate axis, one column per pulse, background uniform, signal at a constant offset. The horizontal band is the real look; the histogram is the projection of it. Counts stay labelled illustrative.
- assets: MG_004_HIST OPT_006_ACCUM SCI_003_STATS

## REF-OPT-006  `optical_beam_divergence_gaussian_wikimedia_divergenz-gauss-strahl.png`
- source: https://en.wikipedia.org/wiki/File:Divergenz.Gauss-Strahl.png (Wikimedia Commons / Bautsch)
- licence: CC0 Bautsch / Wikimedia Commons, CC0
- perspective: side view, beam axis horizontal (z), radius vertical (w)
- what is visible: White background. A blue hyperbola-like pair of curves pinching to a narrow waist at the centre, with straight dark-red dashed asymptotes crossing at the waist and opening outward to the left and right. Dimension arrows and symbols: w0 at the left, z0 (green) between centre and a vertical marker, sqrt(2) w0 at the right, small theta and large Theta as angle arcs in dark red. Axes: blue vertical 'w', green dash-dot horizontal 'z'.
- influences: B25: at lunar distance we are in the far field, so draw straight cone edges from an apex; do not draw a waist. Use the asymptote style (dashed edge lines) if a footprint inset needs an angle marker.
- assets: OPT_002_BEAM_SPREAD

## REF-OPT-007  `optical_beam_waist_divergence_wikimedia_gaussianbeamwaist.svg`
- source: https://en.wikipedia.org/wiki/File:GaussianBeamWaist.svg (Wikimedia Commons / DrBob (Gaussianbeam.png))
- licence: CC_BY_SA_3.0 DrBob / Wikimedia Commons, CC BY-SA 3.0
- perspective: side view, beam axis horizontal
- what is visible: Red hyperbola pair pinching at the centre, light-blue dashed asymptotes, black dimension arrows: w0 (waist radius), sqrt(2) w0, b (confocal parameter) across the top, zR (Rayleigh range) below, w(z) at the right, Theta as a curved double arrow between the asymptotes, grey axis z with arrow. Italic mathematical labels. The lower half of my render is blank because the SVG canvas is taller than the drawing.
- influences: Dimension-line style (thin black double arrows with end ticks) is a template for B09/B33 brackets as well.
- assets: OPT_002_BEAM_SPREAD

## REF-OPT-008  `optical_seeing_star_image_d2r0_wikimedia_ast-seeing-2r0.png`
- source: https://en.wikipedia.org/wiki/File:Ast_seeing_2r0.png (Wikimedia Commons (public domain))
- licence: PUBLIC_DOMAIN Wikimedia Commons, public domain (per file page)
- perspective: negative (dark-on-white) image of a point source
- what is visible: Square white field with a thin black border. A single compact dark core slightly left of centre, softly blurred, with a faint pale ring-like halo and two or three faint dark lobes (one upper left, one right) around it: a nearly clean diffraction pattern, slightly distorted.
- influences: B29: the mild case is a footprint that moves and distorts as one body.
- assets: OPT_005_ATMOS_DISTORT

## REF-OPT-009  `optical_seeing_star_image_d20r0_wikimedia_ast-seeing-20r0.png`
- source: https://en.wikipedia.org/wiki/File:Ast_seeing_20r0.png (Wikimedia Commons (public domain))
- licence: PUBLIC_DOMAIN Wikimedia Commons, public domain (per file page)
- perspective: negative image of a point source
- what is visible: Same framing as REF-OPT-008 but the single core is gone: a cloud of many tiny dark speckles filling a roughly round patch about a quarter of the frame wide, no bright centre, very low contrast.
- influences: B29: for the 'magnified' disturbance use a speckle breakup of the footprint, not a smooth sine wobble.
- assets: OPT_005_ATMOS_DISTORT

## REF-OPT-010  `optical_turbulence_wavefront_cells_wikimedia_atmos-struct-imaging.svg`
- source: https://en.wikipedia.org/wiki/File:Atmos_struct_imaging.svg (Wikimedia Commons / Gringer)
- licence: PUBLIC_DOMAIN Gringer / Wikimedia Commons, public domain (per file page)
- perspective: side view, light travelling downward
- what is visible: White canvas, black serif labels. At the top 'Plane waves from distant point source' above three straight horizontal grey lines. A pale cyan band with wavy upper and lower edges labelled 'Turbulent layer in atmosphere'. Below the band about ten stacked grey lines that are now wiggly, with local steps and bumps, labelled 'Perturbed wavefronts'. The lower part of my render is blank (canvas taller than drawing).
- influences: B29: show straight parallel lines becoming wiggly after the air band; that is also the visual reason for 'arrival time a little uncertain'.
- assets: OPT_005_ATMOS_DISTORT

## REF-OPT-011  `optical_seeing_moon_wobble_animation_wikimedia_seeing-moon.gif`
- source: https://en.wikipedia.org/wiki/File:Seeing_Moon.gif (Wikimedia Commons / Philipp Salzgeber)
- licence: CC_BY_SA_2.0 Philipp Salzgeber / Wikimedia Commons, CC BY-SA 2.0 AT
- perspective: telescopic close-up of lunar surface, 8 frames
- what is visible: Tiny 150x150 grey animation (8 frames at 5 fps, 1.6 s, three tiles viewed). A lunar crater field with a large dark shadow at right; between frames craters shift a few pixels and blur differently, edges wobble but the scene stays recognisable.
- influences: B29: wobble amplitude is a few percent of object size, random per frame, not periodic.
- assets: OPT_005_ATMOS_DISTORT

## REF-OPT-012  `optical_laser_beams_in_dark_sky_nasa-gsfc_gsfc_20171208_archive_e001973.jpg`
- source: https://images.nasa.gov/details/GSFC_20171208_Archive_e001973 (NASA / GSFC)
- licence: PUBLIC_DOMAIN_NASA NASA/GSFC
- perspective: ground-level, portrait; wide-angle looking up at a bright Moon
- what is visible: Portrait night photo (stored 1713x2400). Deep blue-navy sky with faint stars. A very bright Moon with starburst flare at upper left. Two thin, perfectly straight green beams: one climbs almost vertically from a small white dome at lower left; the other runs diagonally from a telescope on a platform at lower right up to the Moon. The beams are narrow, constant in width, slightly brighter near the source and fading higher up; the diagonal one reaches the bright Moon disc at the top. Telescope pad has railings and a person; red-lit foreground. No visible pulses, the beams look continuous.
- influences: B01-B04: the ground-view beam should be a thin straight green line with soft edges that fades with height; do not extend it visually past the atmosphere. Colour conflict with 'outbound warm' flagged in notes.
- assets: OBS_001_EXTERIOR OBS_002_DOME OBS_005_NIGHT_SKY OPT_000_SYSTEM OPT_001_LIGHT_PULSE

## REF-OPT-013  `optical_laser_beams_in_dark_sky_nasa-gsfc_gsfc_20171208_archive_e001957.jpg`
- source: https://images.nasa.gov/details/GSFC_20171208_Archive_e001957 (NASA / GSFC / Debbie McCallum)
- licence: PUBLIC_DOMAIN_NASA NASA/GSFC/Debbie McCallum
- perspective: ground-level, wide landscape, dome in lower centre
- what is visible: Dusk-blue sky with scattered stars. A white observatory dome with open slit at lower centre. From the slit a wide green fan-shaped beam rises to upper left, clearly broader at the top than at the dome (perspective plus spread) with brighter green edges inside the dome slit. A second, very thin straight green line runs from the lower right to the top right. Beams look soft-edged and continuous.
- influences: B25/B20 inset: a real beam is thin; the apparent fan is perspective and should not be read as the km-wide lunar footprint.
- assets: OBS_002_DOME OBS_006_DOME_SLIT OPT_001_LIGHT_PULSE OPT_002_BEAM_SPREAD

## REF-OPT-014  `optical_laser_beams_in_dark_sky_nasa-gsfc_gsfc_20171208_archive_e001974.jpg`
- source: https://images.nasa.gov/details/GSFC_20171208_Archive_e001974 (NASA / GSFC / Debbie McCallum)
- licence: PUBLIC_DOMAIN_NASA NASA/GSFC/Debbie McCallum
- perspective: ground-level, wide landscape, long exposure
- what is visible: Dark blue sky with faint short star trails. A bright Moon at upper right with halo. A thin green line runs from the top-left corner to the Moon; another thin line rises from a dome silhouette behind trees at lower centre to the Moon. Lines are straight, uniform and faint, brightest where thick. Tree line and building edge at the bottom right.
- influences: B02-B04: keep beam opacity low (about a quarter of the Moon's brightness); it should read as a faint line, matching 'faint scattered line' target (g).
- assets: OPT_000_SYSTEM

## REF-OPT-015  `optical_laser_guide_star_beam_night_wikimedia_photograph-of-laser-guide-star.png`
- source: https://en.wikipedia.org/wiki/File:Photograph_of_a_Laser_guide_star.png (Wikimedia Commons / Gunter Schuricht)
- licence: CC_BY_4.0 Gunter Schuricht / Wikimedia Commons, CC BY 4.0
- perspective: dark sky, vertical-ish beam rising from the bottom edge
- what is visible: Near-black star field with many fine white/blue stars. A single thin, sharply defined golden-yellow line rises from the bottom edge, leaning slightly right, and ends abruptly in a tiny bright dot about halfway up the frame, with nothing beyond. Thinner and tidier than the GSFC beams.
- influences: B04/B05: the beam line stops at the top of the atmosphere before the match cut to space; a pulse symbol then takes over. Yellow here is a sodium (589 nm) guide-star laser per the file title, not a ranging laser.
- assets: OPT_000_SYSTEM

## REF-RETRO-001  `reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg`
- source: https://commons.wikimedia.org/wiki/File:Apollo_11_Lunar_Laser_Ranging_Experiment.jpg (NASA / Apollo 11 (Armstrong, per ALSJ sequence AS11-40-5942-5953); Wikimedia Commons public-domain copy)
- licence: PUBLIC_DOMAIN_NASA NASA (Apollo 11)
- perspective: three-quarter view from the front, a few metres away (distance estimated by eye), array face tilted up toward the upper left
- what is visible: The deployed Apollo 11 array seen from the front-left and slightly above. The face is a flat rectangular panel made of a dark, glossy grid of cube faces; it reads as near-black with small bright glints, set in a silver-grey aluminium box. The panel is tilted so its face points up and to the left (toward the sky); the box edge facing the camera shows a thin lip and rivets. Below it is a white-bright base plate that rests on the soil, with angled struts and a tall bail-handle arch (a thin rectangular loop) at the right. Two thin rods lie on the ground at the left (gnomon/stowed legs). The surrounding soil is dark grey, rough, with chevron bootprints in the foreground. In the distance, upper left, the LM leg; upper right, the PSEP mast on its copper-coloured base. The base is much brighter than the panel face because it is sunlit white metal while the face is dark glass.
- influences: RETRO_001/RETRO_004: draw a silver-grey aluminium box with a white-bright base plate and bail handle; the cube faces read as a dark glossy grid (not round glassy bubbles). Tilt the face upward toward the camera's upper left.
- assets: RETRO_000_SYSTEM RETRO_001_ASSEMBLY RETRO_002_CUBE_ARRAY RETRO_004_FRAME_MOUNT RETRO_006_SHADOW

## REF-RETRO-003  `reflector_apollo11_lrrr_elevated_from_lm_window_nasa_as11-37-5551_crop.jpg`
- source: https://images.nasa.gov/details/as11-37-5551 (NASA / Apollo 11 (post-EVA photo through the LM window, cropped by this project))
- licence: PUBLIC_DOMAIN_NASA NASA
- perspective: elevated, from the LM window, long distance, front-left
- what is visible: A 1300x700 crop (offset x=1000, y=650 of the 4120x4120 frame). At the top centre the seismometer: a copper-coloured cylinder on a dark base with silver wing panels and a thin tilted mast. At lower right a bright white tilted frame with a plate (the retroreflector box and its stand), seen from above and from the side; a faint red-edged flat sheet (the thermal cover?) at lower left. The foreground is pale grey soil with small rocks and a dark dust-smeared band across the left edge (window glare).
- influences: Use only as layout reference (array in front of and closer than the PSEP from the window), not for detail.
- assets: RETRO_001_ASSEMBLY

## REF-RETRO-004  `reflector_apollo11_lrrr_preflight_hardware_nasa_sp214_fig7-6.png`
- source: https://an.rsl.wustl.edu/apollo/data/a11/stationLM/lrr/docs/lrr_psr.pdf (NASA (Apollo 11 Preliminary Science Report SP-214, ch. 7))
- licence: PUBLIC_DOMAIN_NASA NASA SP-214, Apollo 11 Preliminary Science Report, ch. 7, fig. 7-6
- perspective: three-quarter from above-front, on a test stand, face up
- what is visible: Grainy black and white print of the flight unit on a black test stand with a hand wheel on the left and a hand crank at the right. The panel is a square aluminium plate tilted on its frame with a grid of round cavities, about ten across, most of them dark; some cavities are shallow and some seem to hold the glass. A vertical gnomon rod rises from the front of the base; two pole arches (a bail handle at the back and a hinged arm at the left) rise from the frame. On the white base there is a pointer scale, a compass-like azimuth mark, a long black cylinder (the bubble level or pointing mount) and cable clips. A tag on the stand reads WARNING and 'THERMAL SURFACE'.
- influences: RETRO_004: include a gnomon rod, alignment scale and bail handle on the base; the cavities are visibly round and recessed.
- assets: RETRO_000_SYSTEM RETRO_001_ASSEMBLY RETRO_002_CUBE_ARRAY RETRO_003_CUBE_CUTAWAY RETRO_004_FRAME_MOUNT

## REF-RETRO-005  `reflector_apollo11_cube_mount_section_figure_nasa_sp214_fig7-1.png`
- source: https://an.rsl.wustl.edu/apollo/data/a11/stationLM/lrr/docs/lrr_psr.pdf (NASA (Apollo 11 Preliminary Science Report SP-214, ch. 7))
- licence: PUBLIC_DOMAIN_NASA NASA SP-214, Apollo 11 Preliminary Science Report, ch. 7, fig. 7-1
- perspective: cross-section drawing, side view, cube apex pointing down
- what is visible: A clean line cutaway of one cavity. A cylindrical hole in a hatched aluminium block holds a cylindrical glass cube whose rear end is cut to a pyramid apex pointing down into the cavity; labels: Aluminium retainer ring (threaded, with a lip), Upper Teflon mounting ring, Fused silica retroreflector, Lower Teflon mounting ring, Inside surface of cavity. The glass sits about half-way down the cavity (recessed by about half its diameter, as the text says), with a gap and an air space below it.
- influences: RETRO_003: draw the cutaway with these five labelled parts, apex down, and the glass front set back from the panel surface.
- assets: RETRO_003_CUBE_CUTAWAY RETRO_005_CUBE_3FACE RETRO_002_CUBE_ARRAY

## REF-RETRO-006  `reflector_apollo14_lrr_closeup_high_threequarter_tilt_support_nasa_as14-67-9385.jpg`
- source: https://ilrs.gsfc.nasa.gov/missions/lunar_missions/index.html (NASA / Apollo 14 (via ILRS))
- licence: PUBLIC_DOMAIN_NASA NASA / ILRS
- perspective: close three-quarter from above and in front, array face at lower left, support at right
- what is visible: A close, high view looking down at the panel: the face is a rectangular silver-grey aluminium plate with rows of round shallow dimples (the recessed cube faces), each showing a shiny curved glint; the plate is tilted down toward the lower left. At the right is a white box-shaped support with a hinged top plate, a thin vertical rod (gnomon) and a round fixture with a small circular lens or bubble-level window on top; behind it a rectangular bail-handle frame. Beneath, a white leg frame with angular struts rests on the soil. Dark shadow in the upper right; chevron bootprints at lower right.
- influences: RETRO_004: the support stands behind the array like a hinged easel with a round level fixture on top; gnomon is a thin vertical rod.
- assets: RETRO_001_ASSEMBLY RETRO_004_FRAME_MOUNT RETRO_002_CUBE_ARRAY

## REF-RETRO-007  `reflector_apollo14_lrr_medium_threequarter_sunlit_horizon_nasa_as14-67-9386.jpg`
- source: https://images.nasa.gov/details/as14-67-09386 (NASA / Apollo 14)
- licence: PUBLIC_DOMAIN_NASA NASA
- perspective: medium distance (a few metres, estimated by eye), three-quarter from the front-right, low, with a long horizon behind
- what is visible: The array sits at the lower right of the frame, tilted back like an open lid. Its face is light silver with a regular grid of round recessed circular cells, about ten by ten, each with a bright rim; the side wall of the aluminium box is a plain silver strip with rivets; a white metal support frame with angular bars sits at its left and a pair of short thin rods at the corners. Footprints in the soil around it; a dark shadow on the left; the horizon is flat and black above. A clear plastic bag-like sheet with red edging lies at the right background.
- influences: RETRO_002: faces are bright round rims in silver aluminium on the Apollo 14 unit, so cube count and spacing can be drawn exactly; box depth is shallow relative to its width.
- assets: RETRO_001_ASSEMBLY RETRO_002_CUBE_ARRAY RETRO_004_FRAME_MOUNT

## REF-RETRO-008  `reflector_apollo15_lrrr_topdown_hex_cubes_gnomon_nasa_as15-85-11468.jpg`
- source: https://ilrs.gsfc.nasa.gov/missions/lunar_missions/index.html (NASA / Apollo 15 (via ILRS))
- licence: PUBLIC_DOMAIN_NASA NASA / ILRS
- perspective: top-down looking over the array from the back, face toward the viewer's lower side
- what is visible: A black-and-white-looking high view of the large Apollo 15 panel: an aluminium plate dense with round recessed cells packed in staggered rows (a hex-like pattern), each cell dark with small triangular reflections; about a dozen rows are visible and the right edge of the panel is cropped. Most cells at the lower left are in shadow. At the top edge a white support hardware with a small round hinge and a tall thin gnomon rod, and a second hinge plate beside it. Dark shadow at left; grey soil.
- influences: The Apollo 15 array should only be shown as a comparison inset: far more cells in staggered rows, same cell size.
- assets: RETRO_002_CUBE_ARRAY

## REF-RETRO-009  `reflector_apollo15_lrrr_orbital_view_tiny_nasa_pia13037.jpg`
- source: https://images.nasa.gov/details/PIA13037 (NASA JPL (LRO/LROC imagery))
- licence: PUBLIC_DOMAIN_NASA NASA
- perspective: orbital top-down (LRO), array circled at left
- what is visible: A grey LROC strip with many small craters and labels: ALSEP, a circle labelled LRRR at the far left, the Falcon descent stage as a bright blob at centre and a track to LRV1 at lower right; a trail of tracks linking the sites. The array itself is a few pixels in the circle.
- influences: Use for the establishing shot sense of scale only: the array is a few pixels at LRO resolution.
- assets: RETRO_000_SYSTEM

## REF-RETRO-011  `reflector_corner_cube_ray_path_3d_diagram_wikimedia_corner-reflector.png`
- source: https://commons.wikimedia.org/wiki/File:Corner_reflector.svg (Wikimedia Commons (user Chetvorno))
- licence: CC0_1.0 Chetvorno (CC0), via Wikimedia Commons
- perspective: 3-D isometric of the open corner, rays entering from the upper right
- what is visible: A light-blue/lilac inner corner formed by three square planes meeting at a vertex at the left. Two incoming rays, one black and one red, enter from the right, each bounces off all three faces (arrowheads show direction) and leaves at the right back along a path parallel to its entry, displaced sideways from it. Faces are shaded in three tones.
- influences: RETRO_003/RETRO_005: use as the structural template (redrawn): three planes, three bounces, parallel but offset return; exit ray is not collinear with the entry ray.
- assets: OPT_004_CORNER_PATHS RETRO_003_CUBE_CUTAWAY RETRO_005_CUBE_3FACE SCI_005_CORNER_CUBE

## REF-RETRO-012  `reflector_corner_cube_ray_path_2d_comparison_wikimedia_comparison-of-retroreflectors.png`
- source: https://commons.wikimedia.org/wiki/File:Comparison_of_retroreflectors.svg (Wikimedia Commons (user Cmglee))
- licence: CC_BY_SA_3.0 Cmglee, CC BY-SA 3.0, via Wikimedia Commons
- perspective: 2-D side section diagrams
- what is visible: Two panels on white: (1) a corner reflector drawn as a blue V (two perpendicular mirrors) in a grey block, with a gold axis-parallel ray reflecting twice and returning parallel and offset, plus a red dashed and a green dotted off-axis ray each returning roughly back toward the source; (2) a cat's-eye sphere in pale cyan with a blue mirror cap behind it with the same colour code. Panel numbers 1 and 2 at left.
- influences: RETRO_003: the 2-D cutaway should show the V and two reflections only, with the third face as an inset (matches this drawing).
- assets: OPT_004_CORNER_PATHS RETRO_003_CUBE_CUTAWAY SCI_005_CORNER_CUBE

