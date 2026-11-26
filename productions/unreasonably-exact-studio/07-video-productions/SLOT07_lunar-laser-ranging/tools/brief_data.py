"""Per-asset production detail for the 34 Codex briefs (read by build_handoff.py).

Keys per asset id:
  real      real-world object identification (one sentence, what it is and what it is NOT)
  geom      required geometry / proportions (numbers where a source gives them)
  state     pose or object-state requirement
  layers    list of (layer_file_stem, contents, parent, pivot_px_note, draw_order)
  overlap   hidden-overlap requirement specific to this asset
  method    construction method chosen for the shot (UE 7.2 / HC 4.1 vocabulary)
  motion    intended motion in the film
  proof     proof clips that must pass
  limits    scientific or historical limitation (what the art must NOT claim)
  out       expected deliverable filename pattern
Units: all pixel numbers refer to the canvas stated in the brief. Overlap is stated as % of canvas width.
"""
P = 'Painterly-clean cinematic illustration'

D = {}


def d(k, **kw):
    D[k] = kw


# ---------------------------------------------------------------- EARTH
d('EARTH_001_SURFACE',
  real='Cloud-free Earth surface map (equirectangular). Not a photograph of a particular day; not a political map.',
  geom='4096x2048, 2:1. Equator at row 1024, antimeridian at the left/right edge: left and right columns must tile (wrap-safe). North/south 8% bands are polar ice, painted clean (no grey filler band, no pinching artefact).',
  state='Opaque. Daylight-neutral colour: ocean #1C5AA8-#2C6CC4 shallow-to-deep, land muted greens/ochres, ice #E9EEF5. NO clouds, light, shadow, terminator, atmosphere, graticule or labels.',
  layers=[('earth_surface_4096x2048', 'surface colour map (Claude assembles from the public-domain base map)', 'EARTH_000_SYSTEM', 'spin axis = vertical centre line of the globe; texture u=0 at antimeridian', 10), ('earth_pole_north_native', 'BATCH 1 CODEX DELIVERABLE: clean top-down north polar cap disc (ice, ocean edge), square canvas, transparent outside the disc, no clouds/light/atmosphere', 'EARTH_001_SURFACE', 'pole at canvas centre', 11), ('earth_pole_south_native', 'BATCH 1 CODEX DELIVERABLE: clean top-down south polar cap (Antarctica) disc, same rules', 'EARTH_001_SURFACE', 'pole at canvas centre', 11)],
  overlap='Wrap-safe: the leftmost 64 px column must continue the rightmost 64 px column (state the measured seam difference in ARTWORK_QA.md).',
  method='BASE = public-domain NASA map (SVS / Blue Marble class, licence verified by Claude); Codex repaints only what is wrong (poles, filler band) at native size; Claude assembles/upscales to 4096x2048 (labelled resampled); sphere mapping in code',
  motion='rotated by the Earth rig (spin) under a fixed sun direction; no baked motion',
  proof='P01', limits='The Pacific/Atlantic arrangement shown to the camera is a design choice, not a claim about which side faces the Moon at transmit time (C03). No Earth-Moon distance is implied by the map.',
  out='earth_surface_4096x2048.png (+ earth_surface_preview_1024.png)')
d('EARTH_002_CLOUDS',
  real='Independent cloud layer for Earth (alpha-only formations: frontal bands, a tropical convective belt, cyclonic swirls). Authored from the cloud references; NOT cut from a satellite composite.',
  geom='4096x2048 equirectangular; same wrap-safe seam rule; ~55-65% of pixels fully transparent; cloud alpha 0.35-0.95 with soft edges; polar regions thinner.',
  state='RGBA. Cloud colour #F0F4FA (bright side) - shading is added in code from the sun direction, so paint clouds flat-lit with only internal density variation.',
  layers=[('earth_clouds_4096x2048', 'cloud density as alpha', 'EARTH_000_SYSTEM', 'same spin axis as surface', 20)],
  overlap='Wrap-safe seam (as the surface).', method='Codex generates cloud tiles at native size (<= ~1500 px, flat-lit, alpha); Claude tiles/blends them into the 4096x2048 wrap-safe layer; clouds drift at ~0.1-0.3 deg/s in code',
  motion='drifts independently of the surface', proof='P01',
  limits='Not weather; must not create a recognisable single storm that would date the picture.',
  out='earth_clouds_4096x2048.png')
d('EARTH_004_NIGHT_LIGHTS',
  real='City-light emissive layer for the night side (points of light, denser in coastal and populated regions). Qualitative; not a data layer.',
  geom='4096x2048 equirectangular on black alpha; points 1-3 px, warm white #FFD9A0 (not the reserved warm/cool pair as areas); no oceans lit; wrap-safe.',
  state='RGBA emissive points only. No glow halos baked (glow is added in code, only on the unlit side).',
  layers=[('earth_night_lights_4096x2048', 'emissive points', 'EARTH_000_SYSTEM', 'same spin axis', 15)],
  overlap='Wrap-safe.', method='procedural sphere mapping; masked by the terminator in code', motion='rotates with the surface', proof='P01',
  limits='Decorative realism only; no light pollution claim.', out='earth_night_lights_4096x2048.png')
d('EARTH_006_ATMOS_SLICE',
  real='Educational side cross-section of air above a ground limb (thin layered air with one turbulent band). Magnified in thickness and labelled magnified by Claude (not in the art).',
  geom='2160x1200 landscape; ground at the bottom 12%, 5 horizontal air layers fading upward, one turbulent band at ~40% height with soft vertical eddies; no sun disc.',
  state='RGBA. Transparent above the last air layer; the beam never appears in the art.',
  layers=[('atmos_slice_ground', 'ground strip', 'EARTH_006_ATMOS_SLICE', 'none', 4), ('atmos_slice_air_layers', 'stacked translucent layers', 'EARTH_006_ATMOS_SLICE', 'none', 5), ('atmos_slice_turbulent_band', 'separate turbulent band', 'EARTH_006_ATMOS_SLICE', 'band centre', 6)],
  overlap='Band extends 4% of canvas width beyond both side edges of the air layers.', method='rigid layers; band wobble driven in code (OPT_005)',
  motion='turbulent band wobbles (code)', proof='none (checked in the shot)', limits='Qualitative only (C09): air bends and slightly delays light; thickness exaggerated; no refractive-index numbers.',
  out='atmos_slice_{ground,air_layers,turbulent_band}_2160x1200.png')

# ---------------------------------------------------------------- MOON
d('MOON_001_GLOBE',
  real='Full-disc Moon near-side-first texture map (equirectangular) showing maria and highlands; the Mare Tranquillitatis region (Apollo 11 site) must be locatable.',
  geom='4096x2048. Near side centred at u=0.5 (lon 0), Mare Imbrium upper-left, Mare Serenitatis/Tranquillitatis centre-right, Oceanus Procellarum left, Tycho (south) bright rayed crater. Maria #55555D-#6A6A72, highlands #8A8A90-#ACACB0.',
  state='Opaque, no baked phase or terminator, no baked limb darkening (code adds both). No labels.',
  layers=[('moon_globe_4096x2048', 'surface albedo map', 'MOON_000_SYSTEM', 'globe centre; no spin in the film', 10)],
  overlap='Wrap-safe seam (far-side edge columns continue).', method='BASE = public-domain LRO/SVS Moon map (licence verified by Claude); Codex repaints/cleans only if needed at native size; Claude upscales (labelled resampled); sphere mapping in code', motion='none (fixed near side)', proof='P02',
  limits='Apollo 11 site position is approximate on the map (C05); libration not modelled; far side is a plausible fill and is never shown.',
  out='moon_globe_4096x2048.png')
d('MOON_002_TERRAIN_SURFACE',
  real='Lunar regolith ground plane in perspective as seen from a standing astronaut eye level (about 1.7 m). Low albedo, HARD-lit grey regolith, not sand.',
  geom='2160x3840 portrait; camera 1.7 m high, looking slightly down; horizon at 36% from the top (its position is fixed by MOON_003); ground fills below with perspective foreshortening; fine texture scale 3 mm near to 3 cm far; a few shallow craters, oblique.',
  state='RGBA, top edge soft alpha (~64 px) to blend into the horizon layer. Crisp, long shadows from the left sun fall to the right; no fill light, no haze.',
  layers=[('moon_terrain_near', 'near regolith strip with foot-scale texture', 'MOON_000_SYSTEM', 'none', 42), ('moon_terrain_mid', 'mid plane with craters', 'MOON_000_SYSTEM', 'none', 41), ('moon_terrain_far', 'far plane flattening to the horizon', 'MOON_000_SYSTEM', 'none', 40)],
  overlap='Each strip overlaps the next by 6% of canvas height with matched texture so parallax never exposes a gap.', method='2.5D rigid layers with real parallax factors (near 1.0, mid 0.6, far 0.3)',
  motion='parallax layer only', proof='P05', limits='No atmospheric perspective: distant ground stays sharp (vacuum). Terrain is generic, not the real Apollo 11 landscape.',
  out='moon_terrain_{near,mid,far}_2160x3840.png')
d('MOON_003_HORIZON',
  real='Lunar horizon line with low subdued hills against a black sky, as in the Apollo 11 surface photographs.',
  geom='4320x2160 (2x width for pan). Horizon curvature visible only as a very slight arc (camera 1.7 m: horizon distance ~2.4 km); hills peak at <= 6% of image height; sky pure #000000 to #05070D; no stars required.',
  state='Opaque. Sunlit slopes on the left faces, black shadow on the right faces.',
  layers=[('moon_horizon_far_hills', 'far low hills', 'MOON_000_SYSTEM', 'none', 10), ('moon_horizon_sky', 'black sky plate', 'MOON_000_SYSTEM', 'none', 5)],
  overlap='Hills extend 5% of canvas height below the horizon line under the terrain top edge.', method='2.5D layers', motion='slow parallax pan', proof='P05',
  limits='Sky is black in daytime on the Moon: no gradient glow at the horizon.', out='moon_horizon_far_hills_4320x2160.png, moon_horizon_sky_4320x2160.png')
d('MOON_005_PROPS',
  real='Sprite sheet of regolith props: rocks, small oblique craters, boot prints, clumps. Boot prints give scale beside the reflector.',
  geom='4096x4096 sheet, individual sprites <= 1024 px, 6 rocks (3 sizes x 2 shapes, angular not round), 4 boot prints (~30 cm long, chevron tread, left/right pairs), 4 small craters (oblique), 4 clump piles; gutter 32 px; sprite base-centre registered.',
  state='RGBA, shadows NOT baked (code adds them from the sun vector).',
  layers=[('moon_props_sheet', 'all sprites on one sheet', 'MOON_005_PROPS', 'base-centre of each sprite (listed in PIVOTS.json)', 50)],
  overlap='Not applicable (static); 8 px alpha padding around every sprite.', method='sprite replacement (static)', motion='static', proof='P05',
  limits='Boot-print size ~30 cm is a design size (qualitative scale cue only).', out='moon_props_sheet_4096x4096.png + PIVOTS.json')
d('MOON_006_SITE_DRESSING',
  real='OPTIONAL distant Apollo 11 site details: a flag silhouette, TV camera on a tripod, seismometer package, foil-covered descent stage fragment. Generic silhouettes.',
  geom='2048x1024 strip, items at 2-5% of image height (far midground), flag static and unfurled-by-wire (horizontal rod), TV camera tripod 3 legs.',
  state='RGBA. Flag hangs in a fixed folded shape (vacuum, no flutter).',
  layers=[('moon_site_flag', 'flag + pole', 'MOON_006_SITE_DRESSING', 'pole base', 30), ('moon_site_tv', 'TV camera tripod', 'MOON_006_SITE_DRESSING', 'tripod base', 31), ('moon_site_seismo', 'seismometer silhouette', 'MOON_006_SITE_DRESSING', 'base', 32)],
  overlap='n/a (static silhouettes)', method='sprite (static)', motion='static', proof='none', limits='No named patch or insignia; the flag has no readable stripes at this size; optional asset.',
  out='moon_site_{flag,tv,seismo}.png')

# ---------------------------------------------------------------- OBSERVATORY
d('OBS_001_EXTERIOR',
  real='A generic observatory building body at night (no dome): concrete base, lit windows, vents, doors. Never a real named site, no signage.',
  geom='2160x3840 portrait; building width 62% of canvas, height 16%; dome ring (circle seen as ellipse, 0.7 ratio) at the roof centre; 3 lit windows (warm-dim #C9A877 at 30% value); door at left.',
  state='RGBA. Cool night light #16223F-#2A3558; the building is lit only by starlight, a small work-light and the windows.',
  layers=[('obs_exterior_body', 'building without dome', 'OBS_000_SYSTEM', 'dome ring centre', 30), ('obs_exterior_window_light', 'window glow as separate layer', 'OBS_000_SYSTEM', 'none', 31)],
  overlap='Roof ring extends 4% of canvas width under where the dome shell sits.', method='rigid layers', motion='static; window glow may flicker once (code opacity)', proof='P03', limits='Generic: do not copy Apache Point or any building; unnamed.', out='obs_exterior_{body,window_light}_2160x3840.png')
d('OBS_002_DOME',
  real='Dome shell, closed, with a vertical slit region cut out as clean alpha; generic hemispherical dome with two bi-parting leaves.',
  geom='Dome diameter = 52% of canvas width; hemispherical with a flattened top; slit width 9% of dome diameter, centred on the dome front; ribs subtle; dome rim ring height 2.5% of canvas height.',
  state='RGBA, slit region transparent (telescope seen through it), dome shell lit only by starlight (no sun). Slit edges thick (about 0.8% canvas width) so the opening reads.',
  layers=[('obs_dome_shell', 'shell with slit cut-out', 'OBS_000_SYSTEM', 'dome rotation axis = ring centre', 40), ('obs_dome_rim_front', 'rim in front of telescope', 'OBS_000_SYSTEM', 'ring centre', 92)],
  overlap='Shell extends 3% of canvas width past the slit edges (under the shutter doors) and under the building roof ring.', method='hierarchical rig: dome rotates about the vertical axis (2D approximation: horizontal shell slide + rim ellipse), slit doors child of dome',
  motion='slow dome rotation (small), slit opens on B01', proof='P04', limits='The real 3.5 m telescope enclosure form is unresolved; generic by decision.', out='obs_dome_{shell,rim_front}_2160x3840.png')
d('OBS_003_INTERIOR',
  real='Dome interior seen as a cutaway: ribs, catwalk, shutter rails; separate foreground occlusion layer that passes in front of the telescope.',
  geom='2160x3840; interior ribs converge to the slit; floor ellipse; catwalk as horizontal band at 62% height; occlusion layer = 3 ribs + a rail running in front of the telescope tube.',
  state='RGBA two files: back (opaque interior) and front occlusion (partial).', layers=[('obs_interior_back', 'ribs, floor, catwalk', 'OBS_000_SYSTEM', 'none', 10), ('obs_interior_occluder', 'ribs/rail in front of telescope', 'OBS_000_SYSTEM', 'none', 90)],
  overlap='Occluder extends 2% of canvas width onto the back plate at every join.', method='rigid layers', motion='static', proof='P04', limits='Illustrative interior; no real instrument layout.', out='obs_interior_{back,occluder}_2160x3840.png')
d('OBS_004_MOUNTAINS',
  real='Three parallax ridge layers of a dry mountain-top site seen from the observatory at night.',
  geom='Each 4320x1400 (2x width): far ridge value #1B2744 (lightest, near the horizon sky glow), mid #12203C, near #0B1530 (darkest); silhouette edges slightly different in each layer; no snow.',
  state='RGBA, three separate files.', layers=[('obs_ridge_far', 'far ridge', 'OBS_004_MOUNTAINS', 'none', 15), ('obs_ridge_mid', 'mid ridge', 'OBS_004_MOUNTAINS', 'none', 17), ('obs_ridge_near', 'near ridge', 'OBS_004_MOUNTAINS', 'none', 19)],
  overlap='Each ridge extends 8% of canvas height below its visible base.', method='2.5D rigid layers (parallax factors far 0.15, mid 0.35, near 0.6)', motion='tiny parallax with camera push', proof='P03',
  limits='Generic dry-mountain silhouette; no real range.', out='obs_ridge_{far,mid,near}_4320x1400.png')
d('OBS_006_DOME_SLIT',
  real='Two shutter door leaves that slide apart along the dome tangent to open the slit.',
  geom='Each leaf 4.5% of dome diameter wide when closed (together they cover the 9% slit), travel 100% of leaf width outward, curved to follow the dome (slight arc), slightly lighter edge strip where they meet.',
  state='Two files: leaf_L and leaf_R, closed state on the dome canvas; opened state is produced by translation in code.',
  layers=[('obs_slit_leaf_L', 'left shutter leaf', 'OBS_002_DOME', 'slide axis start at closed centre seam', 41), ('obs_slit_leaf_R', 'right shutter leaf', 'OBS_002_DOME', 'slide axis start at closed centre seam', 41)],
  overlap='Each leaf extends 1.5% of canvas width onto the dome shell on its outer edge and 0.6% past the centre seam.', method='rigid layers with a slide constraint (hierarchical child of dome)',
  motion='slides apart on B01 (anticipation: 3-frame hold, ease-out, tiny settle)', proof='P03', limits='Motor sound is added by Claude (generated), not by this art.', out='obs_slit_leaf_{L,R}_2160x3840.png')
d('OBS_007_PROPS',
  real='Foreground ground props around an observatory: rocks, antenna mast, fence posts, utility box.',
  geom='4096x4096 sheet, sprites <= 1024 px: 5 rocks, 1 lattice mast (tall, 1:8), 4 fence posts, 1 grey utility box, 2 shrubs (dry); base-centre registered; gutter 32 px.',
  state='RGBA, shadows not baked.', layers=[('obs_props_sheet', 'sprite sheet', 'OBS_007_PROPS', 'base-centre per sprite (PIVOTS.json)', 50)],
  overlap='n/a', method='sprite replacement (static)', motion='static (mast light blink by code optional)', proof='none', limits='No signs, text or logos; no real-site hardware.', out='obs_props_sheet_4096x4096.png + PIVOTS.json')

# ---------------------------------------------------------------- TELESCOPE
d('TEL_001_HOUSING',
  real='A generic alt-azimuth Ritchey-Chretien-class telescope tube (3.5 m class) with open-truss secondary cage and instrument housings. Non-functional illustration; not any named telescope.',
  geom='Tube length 1.7x aperture diameter; secondary cage = 1/3 of aperture diameter; centre section box (primary cell) 1.15x aperture wide; three views on separate 3000x3000 canvases: side, 3/4, interior 3/4; aperture diameter = 52% of canvas width in side view.',
  state='RGBA. Telescope pointed ~45 degrees up in the "side" master; the altitude axis is at the tube balance point.',
  layers=[('tel_tube', 'tube/truss + secondary cage', 'TEL_000_SYSTEM', 'altitude axis (bearing centre)', 36), ('tel_cell_box', 'primary mirror cell box', 'tel_tube', 'rigid with tube', 37), ('tel_instrument_housing', 'exterior instrument housings', 'tel_tube', 'rigid with tube', 38)],
  overlap='Tube extends 2% of canvas width into the pylon bearing sockets (hidden), cell box extends 1.5% under truss.', method='hierarchical rig (rotation about altitude axis only; rigid child parts)',
  motion='tilts about the altitude axis from ~15 to ~65 degrees on B02-B03', proof='P03, P04', limits='Illustration of the class of instrument; same telescope sends and receives (ONSCOPE); do not show a laser beam or laser hardware in the art.',
  out='tel_{tube,cell_box,instrument_housing}_{side,34}_3000x3000.png')
d('TEL_002_MOUNT',
  real='Azimuth base with two pylons (yoke) carrying altitude bearings (NTT/VLT-class alt-az mount). Not a classic fork.',
  geom='Base disc width 78% of canvas; pylon spacing = 1.3x tube width; bearing circles Ø 9% of canvas width; pylon height 1.1x tube; 3000x3000 for side and 3/4.',
  state='RGBA. Bearing sockets open toward the tube, neutral grey/white #AEB4C2/#E6E9F0.',
  layers=[('tel_base', 'azimuth base', 'TEL_000_SYSTEM', 'azimuth axis through base centre', 35), ('tel_pylon_near', 'near pylon', 'tel_base', 'rigid; bearing centre listed', 36), ('tel_pylon_far', 'far pylon (behind tube)', 'tel_base', 'rigid', 34)],
  overlap='Pylons extend 2% of canvas width into the base; the far pylon extends 2% behind the tube footprint.', method='hierarchical rig (azimuth rotation small)',
  motion='azimuth rotation <= 6 degrees; supports tilt', proof='P04', limits='Generic mount; no specific telescope identity; no text.', out='tel_{base,pylon_near,pylon_far}_{side,34}_3000x3000.png')
d('TEL_003_APERTURE',
  real='Head-on simplified view of the open aperture: rim, secondary mirror with 4-vane spider, primary mirror visible around it. No photograph shows this exact view (centre box hides the primary), so it is built from the geometry.',
  geom='2160x2160; outer rim circle Ø 92% of canvas; secondary mirror Ø 31% of aperture with 4 spider vanes at 45/135/225/315 degrees; primary mirror dark glass with a faint ring of mounting pads; perfect circles.',
  state='RGBA, black sky visible through the aperture is NOT painted (transparent where the sky shows); no flash drawn (code adds the pulse).',
  layers=[('tel_aperture_rim', 'rim + housing front face', 'TEL_000_SYSTEM', 'aperture centre', 50), ('tel_aperture_secondary', 'secondary + spider', 'tel_aperture_rim', 'aperture centre', 51), ('tel_aperture_primary', 'primary mirror face', 'tel_aperture_rim', 'aperture centre', 49)],
  overlap='Spider vanes extend 1% of canvas width into the rim; primary extends 1% under the rim.', method='rigid layers (push-in by camera)', motion='slow push-in on B24; background dims in code', proof='P03',
  limits='Simplified: the real optical path is folded (third mirror) - label as simplified in the shot.', out='tel_aperture_{rim,secondary,primary}_2160x2160.png')
d('TEL_004_PRIMARY_CUTAWAY',
  real='Educational cutaway of the telescope tube: sliced tube, concave primary mirror, secondary, and an indicated receiver position. Marked simplified; no fictional specs.',
  geom='2160x3000 portrait; tube cut along its axis, near half removed; primary concave surface drawn in section (gentle curve); secondary near the top; receiver housing at the side at the primary level; return path as empty space (Claude draws the path).',
  state='RGBA, shell / mirror / interior as separate layers.', layers=[('tel_cutaway_shell', 'cut tube shell', 'TEL_000_SYSTEM', 'none', 55), ('tel_cutaway_primary', 'primary in section', 'tel_cutaway_shell', 'none', 56), ('tel_cutaway_secondary', 'secondary in section', 'tel_cutaway_shell', 'none', 57), ('tel_cutaway_receiver', 'receiver housing', 'tel_cutaway_shell', 'none', 58)],
  overlap='All inner layers extend 1.5% of canvas width under the shell edge.', method='rigid layers + procedural light path (Claude)', motion='light path drawn by code', proof='P08',
  limits='The real return path folds sideways via a third mirror to the receiver at the axis, not through a hole behind the primary: simplified, labelled so.', out='tel_cutaway_{shell,primary,secondary,receiver}_2160x3000.png')
d('TEL_005_DETECTOR_BOX',
  real='Generic plain instrument housing on the telescope that receives the return light.',
  geom='1500x1500; a plain rectangular box 1:1.3 with rounded corners, one round port, two mounting flanges; no dials, brand marks or text.',
  state='RGBA; neutral grey/white.', layers=[('tel_detector_box', 'box', 'TEL_001_HOUSING', 'port centre', 60)],
  overlap='Flanges extend 1.5% of canvas width into the telescope body.', method='rigid sprite', motion='highlight ring by code', proof='P09', limits='Illustrative box; no internal detail claimed.', out='tel_detector_box_1500x1500.png')

# ---------------------------------------------------------------- RETRO
d('RETRO_001_ASSEMBLY',
  real='Apollo 11 Laser Ranging Retroreflector Array hero composite on regolith: silver aluminium frame, dark glossy glass faces in a 10x10 grid, support legs, shadow. Not the Apollo 14/15 array (those carry 100 and 300 cubes).',
  geom='3000x2000; panel 46 cm square (0.45 m by UCSD, say about half a metre), tilted toward Earth about 30 degrees back from vertical; legs ~25 cm; 10x10 round cube faces, cube diameter 3.8 cm = 1/12 of panel width; boot-print scale cue 30 cm.',
  state='Hero state: panel tilted, resting on regolith; shadow added in code. Second state: ghost (code) - the astronaut aligns it at B18; art is the settled state only.',
  layers=[('retro_assembly_frame', 'frame + support (from RETRO_004)', 'RETRO_000_SYSTEM', 'ground contact bottom-centre', 45), ('retro_assembly_faces', '10x10 faces (from RETRO_002)', 'retro_assembly_frame', 'array centre', 55)],
  overlap='Faces layer extends 1.2% of canvas width under the frame lip.', method='rigid prop (frame + faces)', motion='pops in at B17 (scale/alpha), tiny settle at B18', proof='P06',
  limits='C05/C06: the array is a passive prop; its distance from the lander is tens of metres; which of array/PSEP appears nearer is viewpoint-dependent; do not name an astronaut.',
  out='retro_assembly_frame_3000x2000.png, retro_assembly_faces_3000x2000.png, retro_assembly_master_3000x2000.png')
d('RETRO_002_CUBE_ARRAY',
  real='The 10x10 grid of round glassy cube faces of the Apollo 11 retroreflector in its silver frame (exactly 100 faces). Built from TWO generated parts that Claude assembles in code: an empty frame plate with 100 recesses, and one face-disc sprite (plus variants).',
  geom='NATIVE generation (about 1254-1500 px per image; label anything larger resampled). Plate: square 1:1, panel fills 92% of the canvas with a transparent margin, 10x10 round recesses on a uniform pitch (recess diameter 0.083 of panel width = 3.8/46 cm, pitch 0.086), recesses EMPTY (flat dark floor). Face sprite: ONE round fused-silica face, square canvas, centred, transparent outside the disc, subtle 3-facet interior, no perfect sphere highlight, matte-clean. Variants: 3 faces with slightly different reflection (so the grid does not look stamped).',
  state='Front orthographic view (inferred projection; no photograph is exactly front-on: the Apollo 11 photograph AS11-40-5952 shows the panel tilted, dark glass, matte silver box). Keep the surface MATTE aluminium, not mirror-polished. Light from the upper left, about 30 degrees up, hard.',
  layers=[('retro_array_plate_empty', 'frame plate with 100 empty recesses', 'RETRO_000_SYSTEM', 'plate centre; recess (1,1) and (10,10) centres listed in PIVOTS.json', 54), ('retro_face_disc_a', 'one face disc sprite', 'retro_array_plate_empty', 'disc centre', 55), ('retro_face_disc_b', 'face variant b', 'retro_array_plate_empty', 'disc centre', 55), ('retro_face_disc_c', 'face variant c', 'retro_array_plate_empty', 'disc centre', 55), ('retro_array_macro3x3_native', 'independently generated 3x3 close-up at native size', 'RETRO_000_SYSTEM', 'centre face centre', 55)],
  overlap='Face discs are placed 0.5% of canvas width inside the recess edge in code (hidden bezel overlap lives in the plate).', method='sprite instancing in code: Claude places 100 copies of the face disc on the measured recess grid (exact count and registration); macro is its own generation', motion='macro push-in B19; no motion inside the art', proof='P06, P07',
  limits='100 faces exact (B7 is checked in code from the instance list, not by eye); registration point shared with RETRO_005 cube centre (B9); appearance of the glass varies with viewing angle in the photographs, so the dark-glass look is an illustration choice.', out='retro_array_plate_empty.png, retro_face_disc_{a,b,c}.png, retro_array_macro3x3_native.png (native sizes stated in ASSET_MANIFEST.csv)')
d('RETRO_004_FRAME_MOUNT',
  real='Apollo 11/14-style frame and mount: silver aluminium box frame, white-bright base, tilt support (faces left out).',
  geom='3000x2000; 3/4 view, top view and side view as three separate masters; frame depth 6% of panel width; face-plane corners listed in PIVOTS.json for registration with RETRO_002.',
  state='RGBA, no faces, no cast shadow.', layers=[('retro_frame_34', '3/4 frame + support', 'RETRO_000_SYSTEM', 'ground contact bottom-centre', 45), ('retro_frame_top', 'top view', 'RETRO_000_SYSTEM', 'panel centre', 45), ('retro_frame_side', 'side view', 'RETRO_000_SYSTEM', 'ground contact', 45)],
  overlap='n/a (rigid)', method='rigid prop', motion='static', proof='P06', limits='Silver aluminium box, dark glass faces, white base per the Apollo photographs; no dark frame; no invented markings.', out='retro_frame_{34,top,side}_3000x2000.png + PIVOTS.json')
d('RETRO_005_CUBE_3FACE',
  real='One corner cube seen looking into its corner: three mutually perpendicular faces meeting at the apex, same glass look as RETRO_002.',
  geom='2160x2160; apex at the exact canvas centre pixel (1080,1080), three faces as 120-degree-apart rhombi in perspective; circular front aperture Ø 86% of canvas.',
  state='RGBA, clear glass with faint edge lines; no rays.', layers=[('retro_cube_3face', 'cube interior view', 'RETRO_000_SYSTEM', 'apex = (1080,1080)', 58)],
  overlap='n/a', method='rigid sprite (bridge/inset)', motion='static', proof='P07', limits='C06: three faces mutually perpendicular; return travels back along the incoming direction.', out='retro_cube_3face_2160x2160.png')

# ---------------------------------------------------------------- ASTRONAUT
POSES = 'three poses on separate registered 3000x3000 canvases: `stand34` (3/4 standing rest, facing left-front), `kneel34` (stylised kneeling alignment), `side_step` (side-on step-back)'
ASTRO_COMMON = dict(
    method='pose replacement for large changes (stand -> kneel -> step-back) + hierarchical rigid FK for small limb offsets (<= +-8 degrees) with deliberately drawn suit joint rings (hard-shell suit: UE 7.2 step 3)',
    proof='P05, P06',
    limits='Apollo 11 A7L suit; no face, no name, no patch text; kneel is STYLISED (no photograph shows it); rear view, walking, top view are not planned; no cloth flutter in vacuum.')
ASTRO_LAYER = lambda part, contents, parent, pivot, order: [(('astro_%s_%s' % (part, p)), contents, parent, pivot, order) for p in ('stand34', 'kneel34', 'side_step')]
d('ASTRO_001_HELMET', real='Apollo A7L helmet: white outer shell with neck ring (blue/red/silver disc rings), communication cap hidden under the helmet cover; face hidden by the gold visor.',
  geom='Helmet height = 1/8 of figure height; neck ring Ø 0.7x helmet width; viewed 3/4: helmet width 1.0, depth 1.05 (slightly deeper); side view: helmet silhouette with the PLSS top directly behind.',
  state='Same helmet in every pose; neck angle follows the torso (kneel: head down ~20 degrees).', layers=ASTRO_LAYER('helmet', 'helmet shell + neck ring', 'astro_torso_<pose>', 'neck ring centre', 42), overlap='Neck ring extends 1.2% of canvas width into the torso collar.', motion='head rotation <= 4 degrees; no face motion', out='astro_helmet_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_002_VISOR', real='Gold-coated outer sun visor over the helmet face opening (mirror-like, gold #D6AA46).',
  geom='Visor covers 78% of helmet height x 74% width; curved; reflective: shows an inverted surface/horizon plate (ASTRO_003) with a sun glint at upper left; no face behind it.',
  state='Same gold hue and edge rim in every pose; the visor is lowered in all poses.', layers=ASTRO_LAYER('visor', 'visor with gold coating (reflection removed to its own plate)', 'astro_helmet_<pose>', 'helmet frame hinge (top)', 44), overlap='Visor rim overlaps the helmet frame by 1.0% of canvas width on all sides.', motion='none (rigid on the helmet)', out='astro_visor_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_003_VISOR_REFLECTION', real='Replaceable reflection plate for the visor: lunar surface and horizon in the lower half, black sky above, one sun glint, a tiny silhouette of the retroreflector only in the kneel pose.',
  geom='Plate sized to the visor outline; inverted perspective; sun glint 3% of visor width at upper-left; contains no photographer or lander unless the brief for that pose says so.',
  state='Per pose; the kneel plate shows the reflector small near centre.', layers=ASTRO_LAYER('visor_reflection', 'reflection plate', 'astro_visor_<pose>', 'visor centre', 45), overlap='Plate extends 0.5% beyond the visor outline and is masked to it.', motion='plate cross-fades when the pose changes', out='astro_visor_reflection_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_004_TORSO', real='A7L suit torso: white outer layer, chest remote-control unit box with small switches, hose connector cluster (blue/red/silver rings), harness lines, waist convolute.',
  geom='Torso height 3/8 of figure height; shoulder width 0.30 of height; RCU box 0.07 of height wide on the chest; waist ring at 0.55 of height; arms hang slightly away from the torso.',
  state='Stand: upright. Kneel: torso leans 25 degrees forward. Side step: torso leans back 6 degrees.', layers=ASTRO_LAYER('torso', 'torso + chest RCU + hose cluster', 'astro_master', 'torso centre (hip line)', 46), overlap='Torso extends 1.5% of canvas width under shoulder rings, the neck collar and the waist ring.', motion='torso breathing is not needed; rotation +-3 degrees', out='astro_torso_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_005_PLSS', real='Portable life-support backpack: rigid white box with a flat antenna stowed on top, two small connectors, grey strap hardware.',
  geom='PLSS width 0.78 of torso width, height 0.9 of torso height; rigid rectangle with rounded edges; in the side view it extends 0.2 of figure height behind the torso; antenna folded.',
  state='Rigid, same in all poses; visible edge behind the helmet in the 3/4 views.', layers=ASTRO_LAYER('plss', 'backpack', 'astro_torso_<pose>', 'mount on torso upper-back', 43), overlap='Backpack extends 2% of canvas width into the torso silhouette (hidden).', motion='rigid (moves with the torso)', out='astro_plss_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_006_ARMS', real='Upper arm + forearm, left and right, white fabric suit with elbow convolute rings.',
  geom='Upper arm 0.17 of figure height, forearm 0.15; elbow ring Ø 0.045 of height; shoulder ring Ø 0.06 of height; arms bagged, loose folds at the elbow; both arms present in every pose (near and far).',
  state='Stand: arms relaxed, elbows 20 degrees flexed. Kneel: near arm reaches forward-down to the reflector; far arm braces on the knee. Side step: arms slightly out.',
  layers=[('astro_upper_arm_near_<pose>', 'upper arm near', 'astro_torso_<pose>', 'shoulder', 48), ('astro_forearm_near_<pose>', 'forearm near', 'astro_upper_arm_near_<pose>', 'elbow', 49), ('astro_upper_arm_far_<pose>', 'upper arm far (behind torso)', 'astro_torso_<pose>', 'shoulder', 40), ('astro_forearm_far_<pose>', 'forearm far', 'astro_upper_arm_far_<pose>', 'elbow', 41)],
  overlap='Each child extends 1.5% of canvas width under its parent as bagged fabric with a drawn joint ring, never a generic round cap.', motion='shoulder +-30, elbow 0-100 degrees (extremes tested in P05)', out='astro_{upper_arm,forearm}_{near,far}_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_007_GLOVES', real='Apollo gloves: grey outer glove with fingers, blue-white-grey wrist ring (quick-disconnect), no bare hands.',
  geom='Glove length 0.1 of figure height; four fingers + thumb, fingers slightly curled; wrist ring Ø 0.04 of height; five fingers on each glove (count test).',
  state='Stand: relaxed half-open. Kneel: near hand open flat reaching the panel; far hand clenched on the knee.', layers=[('astro_glove_near_<pose>', 'near glove', 'astro_forearm_near_<pose>', 'wrist', 50), ('astro_glove_far_<pose>', 'far glove', 'astro_forearm_far_<pose>', 'wrist', 42)],
  overlap='Glove cuff extends 1% of canvas width under the sleeve (hidden).', motion='wrist +-15 degrees', out='astro_glove_{near,far}_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_008_LEGS', real='Upper and lower legs, left and right, white fabric with knee and hip convolutes.',
  geom='Thigh 0.22 of figure height, shin 0.22; knee ring Ø 0.06; hip joint at 0.50 of figure height; weight on one leg in stand.',
  state='Stand: one foot slightly ahead, weight on the far leg. Kneel: near knee on the regolith, far knee up at ~90 degrees. Side step: one step back, heel lifted.',
  layers=[('astro_thigh_near_<pose>', 'near thigh', 'astro_torso_<pose>', 'hip', 47), ('astro_shin_near_<pose>', 'near shin', 'astro_thigh_near_<pose>', 'knee', 48), ('astro_thigh_far_<pose>', 'far thigh', 'astro_torso_<pose>', 'hip', 39), ('astro_shin_far_<pose>', 'far shin', 'astro_thigh_far_<pose>', 'knee', 40)],
  overlap='Each child extends 1.5% of canvas width under its parent with a drawn convolute, not a round disc.', motion='hips 0-80, knees 0-120 degrees extremes in the seam test', out='astro_{thigh,shin}_{near,far}_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_009_BOOTS', real='Apollo lunar overshoes: grey-silver boot with ribbed tread pattern, dirt-darkened toe and heel.',
  geom='Boot length 0.17 of figure height, height 0.06; tread pattern ribs 8-10 per sole; left and right differ by mirror, not by redesign; ankle ring Ø 0.04 of height.',
  state='Stand: feet 0.5 stance width apart, one ahead. Kneel: near boot sole facing up behind the knee. Side step: toe-off.', layers=[('astro_boot_near_<pose>', 'near boot', 'astro_shin_near_<pose>', 'ankle', 49), ('astro_boot_far_<pose>', 'far boot', 'astro_shin_far_<pose>', 'ankle', 41)],
  overlap='Boot cuff extends 1% of canvas width under the shin.', motion='ankle +-20 degrees; contact shadow by code', out='astro_boot_{near,far}_{stand34,kneel34,side_step}_3000x3000.png', **ASTRO_COMMON)
d('ASTRO_010_POSE_SET', real='Registered complete poses of one Apollo astronaut as the master art of the character: 3/4 standing rest, 3/4 kneel (stylised), side step-back.',
  geom='Figure height = 1.75 m reference; canvas 3000x3000 each; ground contact point at (1500, 2700) in every pose; figure height 78% of canvas; reflector panel 46 cm = 0.263x figure height wide when shown with it.',
  state=POSES + '. Each pose is a composite of the 9 component layers (see the assembly diagram), delivered also as one flat master.',
  layers=[('astro_master_stand34', 'flat master pose', 'ASTRO_000_SYSTEM', 'ground contact (1500,2700)', 50), ('astro_master_kneel34', 'flat master pose', 'ASTRO_000_SYSTEM', 'ground contact (1500,2700)', 50), ('astro_master_side_step', 'flat master pose', 'ASTRO_000_SYSTEM', 'ground contact (1500,2700)', 50)],
  overlap='Master poses are flat composites; overlap is carried by the component layers.', motion='blend between poses + limb offsets a few degrees (B17-B18)', out='astro_master_{stand34,kneel34,side_step}_3000x3000.png + PIVOTS.json', **ASTRO_COMMON)


def get(asset_id):
    return D.get(asset_id)
