"""Hand-authored asset specs for Slot 07 (ids: FAMILY_NNN_NAME; FAMILY_000_SYSTEM rows are group containers).
Used only by build_manifest.py. Children are derived from `parent`; usage is derived from asset_usage.py + deps.

kind: group | illustration (Codex raster) | texture (Codex map, code-lit) | code (procedural, Claude) | model (python science) | rig (Claude)
evidence: SEEN (I opened the source) | SNIPPET (search summary only) | GAP | N/A (code, no real-world reference needed)
"""
ILRS = 'https://ilrs.gsfc.nasa.gov/missions/satellite_missions/current_missions/ap11_reflector.html'
LROC = 'https://lroc.im-ldi.com/images/22'
SVS = 'https://svs.gsfc.nasa.gov/5570'
ONSCOPE = 'https://tmurphy.physics.ucsd.edu/apollo/onscope.html'
LRRR = 'https://tmurphy.physics.ucsd.edu/apollo/lrrr.html'
APO = 'https://apo.nmsu.edu/'
FACT = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html'
EMU = 'https://www.nasa.gov/wp-content/uploads/static/history/alsj/tnD8093EMUDevelop.pdf'
AS11 = 'NASA photo AS11-40-5948 (cited on ' + LROC + ')'
ENV = '2160x3840 px (2x of 1080x1920)'
PNG = 'RGBA PNG, straight alpha, no matte fringe, no baked cast shadow'
OPQ = 'opaque RGB'
NONE = ''

# (id, parent, kind, owner, priority, evidence, description, extras)
# extras keys: sci, vis, cams, canvas, transp, anim, pivots, draw, deps, gen, rig
A = []


def a(id, parent, kind, owner, pri, ev, desc, **kw):
    A.append(dict(id=id, parent=parent, kind=kind, owner=owner, pri=pri, ev=ev, desc=desc, **kw))


# ------------------------------------------------------------------ EARTH
a('EARTH_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SEEN',
  'Reusable Earth (also for later films): independent surface, cloud, atmosphere, night-light and terminator layers, ONE film-wide sun direction shared with the Moon.',
  sci='C03 geometry only; Earth-Moon spacing is NOT TO SCALE (true ~30 Earth diameters)', vis=SVS, anim='spin, cloud drift, light direction, camera-relative orientation')
a('EARTH_001_SURFACE', 'EARTH_000_SYSTEM', 'texture', 'Codex', 'P0', 'SEEN',
  'Cloud-free Earth surface map: ocean, continents, polar ice. No light, shadow, atmosphere or clouds baked in. The only public cloud-free map (SVS 3615, 2048x1024) has a grey filler band at the north: the poles must be repainted clean.',
  sci='Earth radius 6,371.0 km (NASA fact sheet)', vis=SVS + ' (layer split); Blue Marble class texture (SNIPPET)',
  cams='globe; limb at bottom of frame; top-down orbit view (north pole up, pole regions must be clean)',
  canvas='4096x2048 equirectangular', transp=OPQ, anim='rotated by RIG_001; sun direction applied in code', pivots='spin axis = north-south, tilt 0 in schematic',
  draw='10', gen='PLANNED', rig='PLANNED')
a('EARTH_002_CLOUDS', 'EARTH_000_SYSTEM', 'texture', 'Codex', 'P0', 'SEEN',
  'Independent cloud layer: white cloud formations with soft alpha, no shadow, drifts slower than the surface. No transparent public cloud layer exists: it is authored from the cloud references.',
  vis=SVS, cams='globe; limb', canvas='4096x2048 equirectangular', transp='RGBA PNG, alpha = cloud density', anim='drift relative to surface',
  pivots='same spin axis as EARTH_001', draw='20', deps=['EARTH_001_SURFACE'], gen='PLANNED', rig='PLANNED')
a('EARTH_003_ATMOSPHERE', 'EARTH_000_SYSTEM', 'code', 'Claude', 'P0', 'SEEN',
  'Thin bright atmospheric rim and faint haze glow, drawn in code from the globe radius so it scales with any camera distance.',
  vis=SVS, cams='all globe views', canvas='radial gradient generated at runtime (no fixed canvas)', transp='additive/alpha ring', anim='rim brightens toward the sun side',
  pivots='globe centre', draw='30', gen='PLANNED', rig='N/A')
a('EARTH_004_NIGHT_LIGHTS', 'EARTH_000_SYSTEM', 'texture', 'Codex', 'P1', 'SEEN',
  'City-lights layer visible only on the night side (masked by the terminator). Used in the final pull-back.',
  vis=SVS, cams='wide space view (B37)', canvas='4096x2048 equirectangular', transp='RGBA PNG, emissive points on black alpha', anim='rotates with surface',
  pivots='same spin axis as EARTH_001', draw='15', deps=['EARTH_001_SURFACE'], gen='PLANNED', rig='PLANNED')
a('EARTH_005_TERMINATOR', 'EARTH_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A',
  'Day/night shading and soft terminator mask from the single sun direction; shared function with MOON_004.',
  cams='all globe views', canvas='generated at runtime', transp='multiply mask', anim='light direction constant for the film; variable for the reusable asset',
  pivots='globe centre', draw='25', gen='PLANNED', rig='N/A')
a('EARTH_006_ATMOS_SLICE', 'EARTH_000_SYSTEM', 'illustration', 'Codex', 'P1', 'GAP',
  'Side cross-section of the air over a ground limb, in layers with one turbulent band, for the atmosphere beat. Thickness is exaggerated and labelled magnified.',
  sci='C09 qualitative: air bends and slightly delays light', vis='GAP (no source opened yet)', cams='side view, beam passes through',
  canvas='2160x1200', transp=PNG, anim='turbulent band wobbles (driven by OPT_005)', pivots='none', draw='5', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ MOON
a('MOON_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SEEN',
  'One Moon that stays identical from globe to surface close-up: globe, shading, ground, horizon, props, dust.',
  sci='Moon radius 1,737.4 km; near-side fixed (tidally locked)', vis=FACT + '; ' + LROC)
a('MOON_001_GLOBE', 'MOON_000_SYSTEM', 'texture', 'Codex', 'P0', 'GAP',
  'Near-side-first Moon map: maria (incl. Tranquillitatis), highlands, major craters. The Apollo 11 site region must be locatable on it.',
  sci='Apollo 11 site in Mare Tranquillitatis (C05)', vis='GAP: LROC/SVS global Moon map not opened yet; ' + LROC + ' for the site',
  cams='globe (ground sky, schematic, top-down orbit view, closing pull-back)', canvas='4096x2048 equirectangular', transp=OPQ,
  anim='fixed near-side orientation, libration not modelled', pivots='globe centre; no spin in film', draw='10', gen='PLANNED', rig='PLANNED')
a('MOON_002_TERRAIN_SURFACE', 'MOON_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Grey fine regolith ground plane in perspective; low albedo (dark grey) but HARD-LIT: crisp black shadows from the single sun direction, no fill light, no atmosphere haze, sharp horizon (reference: Apollo 11/12 surface photographs).',
  sci='qualitative: regolith scatters light broadly (C06)', vis=AS11, cams='low lunar-surface 3/4 view, slow parallax',
  canvas=ENV, transp='RGBA PNG, soft alpha at far edge to meet the horizon', anim='parallax layer only', pivots='none', draw='40', gen='PLANNED', rig='N/A')
a('MOON_003_HORIZON', 'MOON_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Low lunar horizon, subdued hills, black sky (no stars required in the daylight surface view), no haze.',
  vis=AS11, cams='surface view background', canvas='4320x2160 (2x width for parallax pan)', transp=OPQ + ' (sky black)', anim='slow parallax', pivots='none', draw='10', gen='PLANNED', rig='N/A')
a('MOON_004_GLOBE_SHADE', 'MOON_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A',
  'Terminator and limb-darkening for the Moon globe, using the same sun direction function as EARTH_005.',
  cams='all globe views', canvas='generated at runtime', transp='multiply mask', anim='sun direction fixed for the film', pivots='globe centre', draw='20',
  deps=['MOON_001_GLOBE'], gen='PLANNED', rig='N/A')
a('MOON_005_PROPS', 'MOON_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Sprite sheet: rocks (3 sizes), small craters (oblique), boot prints (4), regolith clumps. Footprints give scale next to the reflector.',
  vis=AS11 + '; ' + ILRS + ' (boot prints)', cams='surface view', canvas='4096x4096 sheet, individual sprites <= 1024 px', transp=PNG, anim='static', pivots='base-centre of each sprite',
  draw='50', deps=['MOON_002_TERRAIN_SURFACE'], gen='PLANNED', rig='N/A')
a('MOON_006_SITE_DRESSING', 'MOON_000_SYSTEM', 'illustration', 'Codex', 'P2', 'SEEN',
  'OPTIONAL distant Apollo 11 site details seen in AS11-40-5948: flag, TV camera, seismometer silhouettes. Flag does NOT flutter (vacuum).',
  vis=AS11, cams='surface view, far midground', canvas='2048x1024', transp=PNG, anim='static', pivots='base-centre', draw='30', deps=['MOON_003_HORIZON'], gen='PLANNED', rig='N/A')
a('MOON_007_DUST', 'MOON_000_SYSTEM', 'code', 'Claude', 'P1', 'N/A',
  'Regolith particle emitter: ballistic arcs under 1.62 m/s2, no drag, no billowing.',
  sci='lunar surface gravity 1.62 m/s2 (NASA fact sheet)', cams='surface view', canvas='runtime particles', transp='alpha particles', anim='ballistic fall', pivots='emit at boot/hand contact points', draw='60', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ OBSERVATORY
a('OBS_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SEEN',
  'GENERIC observatory built from separate layers; labelled as an illustration, never captioned as Apache Point (enclosure form unresolved in sources).',
  vis=APO + ' (context only)', sci='station reality: same telescope sends and receives (' + ONSCOPE + ')')
a('OBS_001_EXTERIOR', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Observatory building body (no dome), doors, vents, a few lit windows; cool dim night light.',
  vis=APO + ' (context); generic by decision', cams='ground-level wide, vertical frame', canvas=ENV, transp=PNG, anim='static', pivots='ring where the dome sits', draw='30', gen='PLANNED', rig='N/A')
a('OBS_002_DOME', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P0', 'GAP',
  'Dome shell, closed state, with the slit region left as a clean cut-out; hidden overlap under the ring. DECIDED: generic hemispherical dome with two bi-parting leaves (the real 3.5 m enclosure form is unresolved; do not copy any specific building).',
  vis='generic; GAP on real enclosure form', cams='ground wide', canvas=ENV, transp=PNG + ' (slit region transparent)', anim='slit opens (OBS_006); optional slow dome rotation',
  pivots='dome rotation axis at ring centre', draw='40 (shell; telescope TEL_001/002 sit BEHIND it at 35/36 and show through the transparent slit)', deps=['OBS_001_EXTERIOR'], gen='PLANNED', rig='PLANNED')
a('OBS_003_INTERIOR', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Dome interior: ribs, floor, catwalk, shutter rails; separate foreground occlusion layer (structure that passes in front of the telescope).',
  cams='cutaway interior, 3/4 view', canvas=ENV, transp=PNG + '; background and occlusion layers delivered separately', anim='static; telescope placed by RIG_002', pivots='none', draw='10 (back) / 90 (occlusion)', gen='PLANNED', rig='N/A')
a('OBS_004_MOUNTAINS', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Three parallax ridge layers (far, mid, near) of a dry mountain-top site; distant landscape merges into the far layer.',
  vis=APO + ' (site overview)', cams='ground wide', canvas='4320x1400 per layer (x3)', transp=PNG, anim='tiny parallax with camera push', pivots='none', draw='15/17/19', gen='PLANNED', rig='N/A')
a('OBS_005_NIGHT_SKY', 'OBS_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A',
  'Night-sky gradient and star field (no named constellations), drifts at sidereal rate; also the sky behind the aperture.',
  cams='ground wide; aperture close', canvas='runtime, 2160x3840 render target', transp=OPQ, anim='barely visible drift', pivots='none', draw='5', gen='PLANNED', rig='N/A')
a('OBS_006_DOME_SLIT', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Shutter doors (two halves) and the opened slit, delivered as a slide-open pair with hidden overlap.',
  cams='ground wide; telescope visible through the slit', canvas=ENV, transp=PNG, anim='doors slide apart on "laser" (B01); motor sound cue', pivots='slide axis along the dome tangent; travel distance in rig JSON',
  draw='41', deps=['OBS_002_DOME'], gen='PLANNED', rig='PLANNED')
a('OBS_007_PROPS', 'OBS_000_SYSTEM', 'illustration', 'Codex', 'P1', 'GAP',
  'Foreground props: rocks, antenna mast, fence posts, utility box; sprite sheet.',
  cams='ground wide foreground', canvas='4096x4096 sheet', transp=PNG, anim='static', pivots='base-centre', draw='50', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ TELESCOPE
a('TEL_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SEEN',
  'Generic alt-azimuth 3.5 m class telescope: non-functional illustration; the same instrument sends the pulse and receives the return.',
  vis=ONSCOPE + '; ' + APO, sci='laser exits through the telescope aperture (ONSCOPE page); C07')
a('TEL_001_HOUSING', 'TEL_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Tube/truss, secondary-mirror cage and exterior instrument housings, side and 3/4 views, no mount.',
  vis=ONSCOPE + ' (laser bench on mirror cell); Ritchey-Chretien alt-az class (SNIPPET)', cams='side; 3/4; interior 3/4', canvas='3000x3000', transp=PNG,
  anim='tilts about the altitude axis', pivots='altitude axis at the bearing centre', draw='36 (behind the dome shell, seen through the slit)', deps=['TEL_002_MOUNT'], gen='PLANNED', rig='PLANNED')
a('TEL_002_MOUNT', 'TEL_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Azimuth base and two pylons (yoke) carrying the altitude bearings, 3/4 view; hidden overlap where the tube sits between them. Not a classic fork: follow the NTT/VLT-class references.',
  vis=APO + ' (alt-azimuth fork photo, telescope identity unconfirmed)', cams='side; 3/4', canvas='3000x3000', transp=PNG,
  anim='azimuth rotation (small), supports tilt', pivots='azimuth axis through base centre; altitude axis through bearings', draw='35 (behind the dome shell)', gen='PLANNED', rig='PLANNED')
a('TEL_003_APERTURE', 'TEL_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SNIPPET',
  'Head-on view of the open aperture: rim, secondary-mirror spider, primary mirror visible; clean area for the laser flash. NOTE: no photograph shows this exact view (the only front views hide the primary behind the centre box): a simplified illustration from the geometry.',
  vis=ONSCOPE, cams='front-on (B04), slow push-in (B24)', canvas='2160x2160', transp=PNG, anim='flash overlay from OPT_001; background dims in B24',
  pivots='aperture centre', draw='50', gen='PLANNED', rig='N/A')
a('TEL_004_PRIMARY_CUTAWAY', 'TEL_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Simplified educational cutaway: tube sliced, concave primary, return light path from sky to detector. Marked simplified; no fictional specs. The real return path folds sideways via a third mirror to a receiver at the axis, not through a hole behind the primary: label it simplified.',
  sci='C07 detector counts returned photons', vis=ONSCOPE, cams='cutaway side view', canvas='2160x3000', transp=PNG + '; shell/mirror/path layers separate',
  anim='light path animated by OPT_001', pivots='none', draw='55', deps=['TEL_001_HOUSING'], gen='PLANNED', rig='N/A')
a('TEL_005_DETECTOR_BOX', 'TEL_000_SYSTEM', 'illustration', 'Codex', 'P1', 'GAP',
  'Plain instrument housing on the telescope that receives the return; generic, no brand, no invented dials.',
  cams='interior 3/4; cutaway', canvas='1500x1500', transp=PNG, anim='highlight ring (MG_006)', pivots='none', draw='60', deps=['TEL_001_HOUSING'], gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ ASTRONAUT
a('ASTRO_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SNIPPET',
  'Apollo 11 astronaut in an A7L suit: complete poses plus replaceable component layers for limb offsets. Visor hides the face (no portrait of a real person).',
  vis=EMU + ' (SNIPPET); Smithsonian suit/helmet pages blocked by a verification wall, not opened',
  sci='vacuum + 1.62 m/s2: slow, bouncy, no cloth flutter', anim='whole-pose blends with limb offsets (playbook 7.2); NO wind-driven cloth (do not reuse skydiver cloth)')
for n, nm, d in [
    (1, 'HELMET', 'Polycarbonate helmet shell, neck ring, communication cap.'),
    (2, 'VISOR', 'Gold-coated outer visor and sun shade, separate from the shell.'),
    (3, 'VISOR_REFLECTION', 'Replaceable reflection plate for the visor (surface, sun glint, reflector).'),
    (4, 'TORSO', 'Suit torso with chest remote-control unit and hose connectors.'),
    (5, 'PLSS', 'Backpack life-support system, rigid.'),
    (6, 'ARMS', 'Upper arm and forearm, left and right, with hidden overlap at shoulder and elbow.'),
    (7, 'GLOVES', 'Gloves with wrist rings, left and right.'),
    (8, 'LEGS', 'Upper and lower legs, left and right, with hidden overlap at hip and knee.'),
    (9, 'BOOTS', 'Lunar boots with tread, left and right.')]:
    piv = {1: 'neck ring', 2: 'on helmet frame', 3: 'on visor', 4: 'torso centre', 5: 'mount on torso',
           6: 'shoulder, elbow', 7: 'wrist', 8: 'hip, knee', 9: 'ankle'}[n]
    a('ASTRO_%03d_%s' % (n, nm), 'ASTRO_000_SYSTEM', 'illustration', 'Codex', 'P0' if n not in (3,) else 'P1', 'SNIPPET', d,
      sci='A7L suit (Apollo 11 and 14)', vis=EMU + ' (SNIPPET); ' + AS11, cams='3/4 view (all poses); side view (step-back)',
      canvas='delivered per pose, 3000x3000 each, same scale and registration across poses', transp=PNG, anim='limb offsets inside the pose blend', pivots=piv,
      draw=str(40 + n * 2), deps=(['ASTRO_002_VISOR'] if n == 3 else []), gen='PLANNED', rig='PLANNED')
a('ASTRO_010_POSE_SET', 'ASTRO_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SNIPPET',
  'Registered complete poses: 3/4 standing rest, 3/4 kneel with equipment interaction (aligning the array; STYLISED: no photograph shows kneeling, name no astronaut), side step-back. Rear view, walking and top view are NOT PLANNED (no beat shows them).',
  sci='C05 (Apollo 11 deployed an array); naming the astronaut is blocked until a primary source is opened', vis=AS11 + '; ' + EMU, cams='3/4 stand; 3/4 kneel; side step',
  canvas='3000x3000 per pose, registered', transp=PNG, anim='RIG_003 blends poses; limb offsets a few degrees', pivots='ground contact point; same in every pose', draw='50',
  deps=['ASTRO_001_HELMET', 'ASTRO_002_VISOR', 'ASTRO_003_VISOR_REFLECTION', 'ASTRO_004_TORSO', 'ASTRO_005_PLSS', 'ASTRO_006_ARMS', 'ASTRO_007_GLOVES', 'ASTRO_008_LEGS', 'ASTRO_009_BOOTS'],
  gen='PLANNED', rig='PLANNED')
a('ASTRO_011_SHADOW', 'ASTRO_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A',
  'Contact/cast shadow from the single sun direction; hard-edged (no atmosphere), keyed to the pose ground point.',
  cams='surface view', canvas='runtime', transp='multiply', anim='follows the pose', pivots='ground contact point', draw='45', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ RETROREFLECTOR
a('RETRO_000_SYSTEM', '', 'group', 'Codex+Claude', 'P0', 'SEEN',
  'Apollo 11 laser ranging retroreflector: the same object from the lunar surface to the optical explanation, visually consistent.',
  sci='C05 100 cubes, 3.8 cm each, about 46 cm panel (ILRS; UCSD gives 0.45 m: say about half a metre if shown); C06 rule: the cube sends light back along its incoming direction', vis=ILRS + '; ' + LRRR + '; ' + LROC)
a('RETRO_001_ASSEMBLY', 'RETRO_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Hero composite on regolith, 3/4 view, tilted toward Earth: frame, support, 10x10 face grid and shadow. Assembled from RETRO_004, RETRO_002 and RETRO_006.',
  sci='Apollo 11 site, array and passive seismic package are a few tens of metres apart (ALSJ: array about 21 m, PSEP about 27 m from the LM); which one is nearer depends on viewpoint', vis=ILRS + '; ' + LROC + '; ' + AS11, cams='3/4 hero; low surface',
  canvas='3000x2000', transp=PNG, anim='pops in at B17 as the dashed ghost dissolves; astronaut aligns it at B18', pivots='bottom-centre of the support (ground contact)', draw='50',
  deps=['RETRO_002_CUBE_ARRAY', 'RETRO_004_FRAME_MOUNT', 'RETRO_006_SHADOW'], gen='RESEARCHED', rig='PLANNED')
a('RETRO_002_CUBE_ARRAY', 'RETRO_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Front and close-up view of the 10x10 grid of round glassy cube faces, dark glossy glass in a silver-aluminium frame (exactly 100 faces visible).',
  sci='100 cubes (ILRS)', vis=ILRS + ' (Apollo 11, 14, 15 photos)', cams='front; close-up macro for the push-in', canvas='4096x4096', transp=PNG,
  anim='macro push-in at B19; no animation inside', pivots='array centre', draw='55', gen='RESEARCHED', rig='N/A')
a('RETRO_003_CUBE_CUTAWAY', 'RETRO_000_SYSTEM', 'code', 'Claude', 'P0', 'SEEN',
  'Simplified side cross-section of ONE corner cube, geometry drawn exactly. The 2-D slice shows two of the three reflections; RETRO_005 insets the third face.',
  sci='C06: three mutually perpendicular faces (UCSD LRRR page)', vis=LRRR, cams='side cross-section, locked', canvas='2160x2160 vector', transp='RGBA',
  anim='appears as a transition from the real array at B19', pivots='cube apex', draw='60', deps=['RETRO_005_CUBE_3FACE', 'SCI_005_CORNER_CUBE'], gen='PLANNED', rig='N/A')
a('RETRO_004_FRAME_MOUNT', 'RETRO_000_SYSTEM', 'illustration', 'Codex', 'P0', 'SEEN',
  'Silver aluminium box frame with a white-bright base, mounting structure and tilt support as seen in the Apollo 11/14 photographs (AS11-40-5952, AS14-67-9385); faces left out (fit RETRO_002 by registration).',
  vis=ILRS, cams='3/4; top; side', canvas='3000x2000', transp=PNG, anim='static (rigid prop)', pivots='ground contact; face-plane corners listed for registration', draw='45', gen='RESEARCHED', rig='N/A')
a('RETRO_005_CUBE_3FACE', 'RETRO_000_SYSTEM', 'illustration', 'Codex', 'P1', 'SEEN',
  'One cube seen looking into its corner: three mutually perpendicular faces meeting at the apex; same glass look as RETRO_002.',
  sci='C06', vis=LRRR, cams='perspective into the corner', canvas='2160x2160', transp=PNG, anim='static; used as the bridge from the array and as the third-face inset',
  pivots='apex', draw='58', deps=['RETRO_002_CUBE_ARRAY'], gen='PLANNED', rig='N/A')
a('RETRO_006_SHADOW', 'RETRO_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A',
  'Hard cast shadow and regolith contact skirt for the assembly, from the single sun direction.',
  cams='surface view', canvas='runtime', transp='multiply', anim='static', pivots='ground contact', draw='44', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ OPTICS (code)
a('OPT_000_SYSTEM', '', 'group', 'Claude', 'P0', 'N/A',
  'Procedural light graphics: educational symbols only (light is invisible in vacuum). Colour grammar: outbound warm, return cool, whole film.',
  sci='SCI_004 declares which items are to scale')
for i, nm, d, an, dp, ev, sci in [
    (1, 'LIGHT_PULSE', 'Short pulse marker with a crisp head and fading tail; warm outbound, cool return; a 2-frame flash variant at the aperture. Never a continuous beam.', 'travels along the path on the beat time map, in step with the stopwatch (slow motion about 1.2-1.8x; the stopwatch ends on the true value)', ['SCI_001_LIGHT_TIME'], 'N/A', 'C01 C02'),
    (2, 'BEAM_SPREAD', 'Two-leg cone diagram: wide outbound cone, tiny array disc inside it, wide return cone, tiny telescope disc inside that. No numbers.', 'cones grow with the pulse; discs highlighted. Also a small footprint inset at B20 (km-wide beam, 46 cm array as a tiny marker), required by the C06 decision', ['SCI_004_SCALES'], 'N/A', 'C07 (~1 in 25 million photons finds the array)'),
    (3, 'PHOTON_MARKER', 'Single detected-photon marker: dot with a soft ring. Educational symbol, never a realistic photon.', 'lands, rings once', [], 'N/A', 'C08 (counts illustrative)'),
    (4, 'CORNER_PATHS', 'Rays at several incoming angles reflect from the faces of the cutaway and exit antiparallel to how they entered; includes the flat-mirror contrast variant.', 'rays animate in sequence, no absorption', ['SCI_005_CORNER_CUBE'], 'N/A', 'C06'),
    (5, 'ATMOS_DISTORT', 'Wavy distortion marker: footprint wobble and small arrival-time jitter, marked magnified.', 'wobble loop', [], 'N/A', 'C09'),
    (6, 'ACCUM', 'Pulse counter plus the feed that adds each pulse\'s few dots to the histogram.', 'counter increments; many pulses compressed in time (labelled)', ['SCI_003_STATS'], 'N/A', 'C08'),
    (7, 'SCATTER', 'Scatter arrows leaving a plain regolith patch in many directions (nothing returns toward the source).', 'arrows fan out', [], 'N/A', 'C06 qualitative')]:
    a('OPT_%03d_%s' % (i, nm), 'OPT_000_SYSTEM', 'code', 'Claude', 'P0', ev, d, sci=sci, cams='as the shot', canvas='runtime vector', transp='RGBA',
      anim=an, pivots='path start point / cone apex', draw='70', deps=dp, gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ MOTION GRAPHICS (code)
a('MG_000_SYSTEM', '', 'group', 'Claude', 'P0', 'N/A', 'Reusable scientific graphics driven by state(t) from SCI_001/002: stopwatch, ruler, formula, histogram, labels, highlight, path arrows.',
  sci='every shown number is in SCIENTIFIC_CLAIMS_LEDGER.csv')
for i, nm, d, dp in [
    (1, 'STOPWATCH', 'Phone-readable stopwatch driven by the beat time map (slowed together with the pulse; its final reading is the true 2.56 s); freezes, bracket and split variants.', ['SCI_001_LIGHT_TIME']),
    (2, 'RULER', 'Earth-Moon distance ruler with live value; km shown only where sourced.', ['SCI_001_LIGHT_TIME', 'SCI_002_ORBIT_GEOMETRY']),
    (3, 'FORMULA', 'Construction of t -> c x t -> divide by two; the bar folds at the Moon (visual, not just text).', ['SCI_001_LIGHT_TIME']),
    (4, 'HIST', 'Time axis, detection dots, histogram, peak marker and shrinking error bar; counts illustrative and labelled.', ['SCI_003_STATS']),
    (5, 'LABELS', 'Symbol set: question mark from dots, crossed-out lightbulb, dashed ghost mirror, question ring. Text only if the voice is ever muted.', []),
    (6, 'HIGHLIGHT', 'Pulsing ring/outline for the landing region, detector, A/B contrast.', []),
    (7, 'PATH_ARROWS', 'Path line between Earth and Moon, two-way arrows, outbound warm / return cool, bracket spans.', ['SCI_004_SCALES'])]:
    a('MG_%03d_%s' % (i, nm), 'MG_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A', d, sci='C01 C02 C11' if i in (1, 3) else '', cams='as the shot', canvas='runtime vector',
      transp='RGBA', anim='state-driven', pivots='anchor per element', draw='80', deps=dp, gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ SCIENTIFIC MODELS (code)
a('SCI_000_SYSTEM', '', 'group', 'Claude', 'P0', 'N/A', 'scientific_model/: one source of truth for timing, distance and scale; graphics are drawn from it.')
a('SCI_001_LIGHT_TIME', 'SCI_000_SYSTEM', 'model', 'Claude', 'P0', 'SEEN', 't = 2d/c; mean round trip 2.564 s; one way 1.282 s; 1 mm = 6.67 ps. Self-check recomputes the numbers.',
  sci='C01 C02 C11', vis=FACT, canvas='python module + check.py', gen='PLANNED', rig='N/A')
a('SCI_002_ORBIT_GEOMETRY', 'SCI_000_SYSTEM', 'model', 'Claude', 'P0', 'SEEN', 'Distance 357,000-407,000 km (round trip 2.38-2.71 s); orbit eccentricity exaggerated and disclosed.',
  sci='C03 C04', vis=FACT, canvas='python module + check.py', deps=['SCI_004_SCALES'], gen='PLANNED', rig='N/A')
a('SCI_003_STATS', 'SCI_000_SYSTEM', 'model', 'Claude', 'P0', 'N/A', 'Random background plus a stable peak that emerges over many pulses; seeded RNG, counts illustrative and labelled.',
  sci='C08 C10', canvas='python module + check.py', gen='PLANNED', rig='N/A')
a('SCI_004_SCALES', 'SCI_000_SYSTEM', 'model', 'Claude', 'P0', 'N/A', 'Declared scale/time registry: which items are real-time, which are not-to-scale, magnified or time-compressed; read by every graphic.',
  sci='SCIENTIFIC_CLAIMS_LEDGER.csv', canvas='SCALES.py + TIME_MAP.py', gen='PLANNED', rig='N/A')
a('SCI_005_CORNER_CUBE', 'SCI_000_SYSTEM', 'model', 'Claude', 'P0', 'SEEN', 'Vector reflection off three perpendicular faces; asserts every exit ray is antiparallel to its entry ray; also yields the 2-D slice rays and the flat-mirror contrast.',
  sci='C06', vis=LRRR, canvas='python module + check.py', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ BACKGROUNDS (code)
a('BG_000_SYSTEM', '', 'group', 'Claude', 'P0', 'N/A', 'Backgrounds shared across scenes.')
a('BG_001_SPACE', 'BG_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A', 'Deep-space star field for the schematic and space views; tiny parallax; no named constellations.',
  cams='space views', canvas='runtime, ' + ENV, transp=OPQ, anim='slow parallax', pivots='none', draw='1', gen='PLANNED', rig='N/A')
a('BG_002_DARK_FIELD', 'BG_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A', 'Dark graphic field for the histogram and detector close-ups.',
  cams='graphics', canvas='runtime, ' + ENV, transp=OPQ, anim='static', pivots='none', draw='1', gen='PLANNED', rig='N/A')
a('BG_003_NEUTRAL_CUTAWAY', 'BG_000_SYSTEM', 'code', 'Claude', 'P0', 'N/A', 'Neutral background for the corner-cube explanation; no scene context.',
  cams='cutaway', canvas='runtime, ' + ENV, transp=OPQ, anim='static', pivots='none', draw='1', gen='PLANNED', rig='N/A')

# ------------------------------------------------------------------ RIGS (code, built after art)
a('RIG_000_SYSTEM', '', 'group', 'Claude', 'P0', 'N/A', 'Reusable animation systems proven by clips P01-P13 before any editing.')
for i, nm, d, dp in [
    (1, 'GLOBE_LIGHTING', 'Earth and Moon globe shader: spin, cloud drift, one light direction, camera-relative orientation, orbit motion.',
     ['EARTH_001_SURFACE', 'EARTH_002_CLOUDS', 'EARTH_003_ATMOSPHERE', 'EARTH_004_NIGHT_LIGHTS', 'EARTH_005_TERMINATOR', 'MOON_001_GLOBE', 'MOON_004_GLOBE_SHADE', 'SCI_002_ORBIT_GEOMETRY']),
    (2, 'TELESCOPE_DOME', 'Parent-child rig: dome slit slide, telescope azimuth and altitude with pivots.',
     ['TEL_001_HOUSING', 'TEL_002_MOUNT', 'TEL_003_APERTURE', 'OBS_002_DOME', 'OBS_006_DOME_SLIT']),
    (3, 'ASTRONAUT_POSE', 'Whole-pose blend with limb offsets and 1/6 g timing; dust through MOON_007; no cloth flutter.',
     ['ASTRO_010_POSE_SET', 'ASTRO_011_SHADOW', 'MOON_007_DUST']),
    (4, 'CAMERA_MULTIPLANE', 'Multiplane camera: push-ins, parallax, match cuts, the ground-to-schematic transition (Moon stays at the same screen spot).', [])]:
    a('RIG_%03d_%s' % (i, nm), 'RIG_000_SYSTEM', 'rig', 'Claude', 'P0', 'N/A', d, anim='see description', deps=dp, gen='N/A', rig='PLANNED', canvas='code + rig JSON')

# proof clips (brief Phase 6). P13 is PROPOSED by me.
PROOFS = [
    ('P01', 'Earth rotation, clouds and consistent lighting', ['RIG_001_GLOBE_LIGHTING']),
    ('P02', 'Earth-Moon cinematic parallax', ['RIG_001_GLOBE_LIGHTING', 'RIG_004_CAMERA_MULTIPLANE', 'BG_001_SPACE']),
    ('P03', 'Observatory-to-Moon transition (B04 -> B05)', ['RIG_004_CAMERA_MULTIPLANE', 'TEL_003_APERTURE', 'MOON_001_GLOBE', 'OPT_001_LIGHT_PULSE']),
    ('P04', 'Telescope and observatory movement', ['RIG_002_TELESCOPE_DOME']),
    ('P05', 'Apollo astronaut movement', ['RIG_003_ASTRONAUT_POSE']),
    ('P06', 'Astronaut and retroreflector interaction', ['RIG_003_ASTRONAUT_POSE', 'RETRO_001_ASSEMBLY']),
    ('P07', 'Accurate simplified retroreflection', ['OPT_004_CORNER_PATHS', 'RETRO_003_CUBE_CUTAWAY', 'SCI_005_CORNER_CUBE']),
    ('P08', 'Outbound and return light journey', ['OPT_001_LIGHT_PULSE', 'MG_007_PATH_ARROWS', 'SCI_001_LIGHT_TIME']),
    ('P09', 'Faint photon detection', ['OPT_003_PHOTON_MARKER', 'MG_004_HIST']),
    ('P10', 'Repeated pulse accumulation', ['OPT_006_ACCUM', 'MG_004_HIST', 'SCI_003_STATS']),
    ('P11', 'Stopwatch synchronization', ['MG_001_STOPWATCH', 'SCI_001_LIGHT_TIME']),
    ('P12', 'Animated distance calculation', ['MG_003_FORMULA', 'MG_002_RULER']),
    ('P13', 'Narration-aligned sample sequence: PROPOSED B17-B21 (37.2-48.5 s) = hero reflector + astronaut + optics', ['RETRO_001_ASSEMBLY', 'ASTRO_010_POSE_SET', 'RETRO_003_CUBE_CUTAWAY', 'OPT_004_CORNER_PATHS']),
]
