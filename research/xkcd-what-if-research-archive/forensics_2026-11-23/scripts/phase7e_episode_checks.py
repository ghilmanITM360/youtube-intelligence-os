"""Phase 7e: quantitative claim checks inside the directive's ten high-value episodes (2026-11-23 continuation). SAME-MODEL SELF-REVIEW, not expert review.
Every row: episode, video ID, claim id, script paragraph + ASR time, the spoken/captioned wording, assumptions, recomputation, constants status, verdict.
constants status codes: F = fetched this session (web search summary or page read); S = standard defined/CODATA constant not fetched; M = value from the author's memory, NOT fetched (a reviewer must confirm).
Verdicts: CONSISTENT | CONSISTENT_WITH_CAVEAT | QUALIFIED | OPEN | NOT_VERIFIED | DISCREPANT_AS_STATED | SUPPLEMENTARY (not a claim made by the video).
Run: python3 -I scripts/phase7e_episode_checks.py  -> 07e_EPISODE_CLAIM_CHECKS.csv"""
import csv, json, math, os, re
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RS = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/what-if-scripts/'
V = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
inv = {i['id']: i for i in json.load(open(RS + 'analysis/inventory.json'))}
G, c, sig, k, g0 = 6.6743e-11, 299792458.0, 5.670374419e-8, 1.380649e-23, 9.80665
yr = 365.25 * 86400
Re_eq, Re, Rm, Rsun_m = 6378.137e3, 6371.0e3, 1737.4e3, 6.957e8
Msun, Mearth, Mmoon, dMoon = 1.98847e30, 5.9722e24, 7.346e22, 384400e3
def segs(v):
    for f in (f'{A}/phase7b_asr/{v}.json', f'{A}/phase7c_asr/{v}.json'):
        if os.path.exists(f): return [(s['offsets']['from'] / 1000, s['text'].strip()) for s in json.load(open(f))['transcription']]
    d = json.load(open(f'{V}{v}/asr/asr_small_en.json')); return [(s['start'], s['text'].strip()) for s in d['segments']]
def when(v, pat):
    for t, x in segs(v):
        if re.search(pat, x, re.I): return round(t, 1), x
    return '', ''
def para(v, pat):
    t = open(RS + inv[v]['script']).read().split('## Script\n', 1)[1]; ps = [p for p in t.split('\n\n') if p.strip()]
    h = [n for n, p in enumerate(ps, 1) if re.search(pat, p, re.I)]; return ';'.join(f'para{n}' for n in h[:3]) if h else 'none (see ASR)'
EP = {'E01': ('gp5G1QG6cXc', 'Earth suddenly stops spinning'), 'E02': ('3EI08o-IGYk', 'Baseball at 0.9c'), 'E03': ('e3uk7jU3RHo', 'Magnitude 15 earthquake'), 'E04': ('Jpy55EgMQgY', 'Draining the oceans'),
      'E05': ('UXA-Af-JeCE', 'A nanosecond on the Sun'), 'E06': ('WH4g1ptJ-70', 'Earth rotated 90 degrees'), 'E07': ('UQgw50GQu1A', 'Moon as a black hole'), 'E08': ('EsUBRd1O2dU', 'Submarine as a spaceship'),
      'E09': ('JqFSGkFPipM', 'Everyone points a laser at the Moon'), 'E10': ('Z_xJ40QXu7Q', 'Billion-story building')}
rows = []
def add(ep, n, pat, claim, assum, calc, ref, cs, verdict, note):
    v, title = EP[ep]; t, q = when(v, pat)
    rows.append(dict(claim_id=f'{ep}{n}', episode=title, video_id=v, vid=inv[v]['vid'], script_locator=para(v, pat), asr_time_s=t, asr_quote=q[:150], claim=claim, assumptions=assum, recomputed=calc, reference=ref,
                     constants_status=cs, verdict=verdict, note=note, review_type='SAME_MODEL_SELF_REVIEW (not independent)'))
# ---------------- E01 Earth stops spinning
v_eq = 2 * math.pi * Re_eq / 86164.0905
add('E01', 'a', r'470 meters|470 m', 'Equatorial surface speed about 470 m/s, a little over a thousand mph; supersonic is 343 m/s', 'sidereal day 86164.09 s; equatorial radius 6378.137 km; sound 343 m/s at 20 C',
    f'{v_eq:.1f} m/s = {v_eq/0.44704:.0f} mph (stated 470, +{(470/v_eq-1)*100:.1f}%)', 'NASA NSSDC radius; sidereal day (F); speed of sound 343 m/s at 20 C (S, not fetched)', 'F+S', 'CONSISTENT', 'same quantity as SC09; 470 is a 1% rounding')
lat = math.degrees(math.acos(343 / v_eq)); vB = v_eq * math.cos(math.radians(42.36))
add('E01', 'b', r'42 degrees', 'Everyone between 42 N and 42 S would feel supersonic wind; Boston is just outside', 'wind = surface speed v_eq cos(lat); Mach 1 = 343 m/s; Boston 42.36 N (M)',
    f'cos(lat)=343/{v_eq:.1f} -> lat={lat:.2f} deg; Boston {vB:.1f} m/s = Mach {vB/343:.3f}', 'as above; Boston latitude (M)', 'F+S+M', 'CONSISTENT', 'Boston sits right at the boundary (Mach 1.00); at 0 C sound is 331 m/s and Boston would be supersonic')
add('E01', 'c', r'twice as strong', 'Boston winds would be twice as strong as the most powerful real tornadoes', 'strongest measured tornado wind about 135 m/s (Doppler on Wheels, 1999) (M); EF5 threshold 89 m/s (M)',
    f'{vB:.0f}/135 = {vB/135:.1f}x; {vB:.0f}/89 = {vB/89:.1f}x', 'tornado winds from the author\'s memory, not fetched', 'M', 'CONSISTENT_WITH_CAVEAT', 'ratio is 2.5x against the strongest measured wind and about 4x against the EF5 threshold, so "twice" is a low rounding')
add('E01', 'd', r'85', 'About 85% of the world population lives between 42 N and 42 S', 'needs population by latitude', 'not computed (no gridded population data available here)', 'none', '-', 'NOT_VERIFIED', 'data gap, not a contradiction')
Ratm = 5.15e18; Iatm = 2 / 3 * Ratm * Re ** 2; IE = 0.3307 * Mearth * Re ** 2; om0 = 7.292115e-5
omf = Iatm * om0 / IE
add('E01', 'e', r'three thousand|3,000|3000', 'After the stop, atmospheric momentum would start the Earth spinning again so slowly that one spin takes about three thousand years', 'atmosphere mass 5.15e18 kg (M) as a thin shell, whole atmosphere at the old rotation rate, full momentum transfer, I_Earth = 0.3307 M R^2 (M); oceans ignored',
    f'I_atm={Iatm:.2e}, I_E={IE:.2e} kg m2; omega={omf:.2e} rad/s; period {2*math.pi/omf/yr:,.0f} years (stated 3,000)', 'atmosphere mass and moment-of-inertia factor from memory, not fetched', 'M+S', 'QUALIFIED',
    'upper-bound style estimate gives about 1,600 years, a factor 1.9 from the stated 3,000; the result depends on how much atmospheric momentum is transferred, which the video does not state')
add('E01', 'f', r'six months|6 months', '6 months of daylight and 6 months of night on a non-rotating Earth', 'no rotation: the Sun circles once per orbit (365.25 d); axial tilt ignored', '365.25/2 = 182.6 days of day at the equator', 'geometry', 'S', 'CONSISTENT_WITH_CAVEAT', 'with the 23.4 degree tilt the day/night split differs away from the equator; the video draws it as a simple half-and-half')
# ---------------- E02 Baseball
add('E02', 'a', r'600 million', 'The ball moves at 600 million miles per hour (0.9c)', '0.9 x 299,792,458 m/s', f'{0.9*c/0.44704/1e6:.1f} million mph', 'c is exact (S)', 'S', 'CONSISTENT', '')
vN2 = math.sqrt(3 * k * 293 / (28.0134 * 1.66054e-27)); vmean = math.sqrt(8 * k * 293 / (math.pi * 28.0134 * 1.66054e-27))
add('E02', 'b', r'hundred miles', 'Air molecules vibrate back and forth at a few hundred miles per hour', 'N2 at 293 K, ideal gas', f'v_rms={vN2:.0f} m/s={vN2/0.44704:.0f} mph; mean speed {vmean/0.44704:.0f} mph', 'kinetic theory (S)', 'S', 'QUALIFIED',
    'thermal speeds are about 1,000 to 1,150 mph, 3 to 4 times "a few hundred"; the sentence says "vibrate back and forth", which is not a defined thermal speed. The same wording is in the original article (read by subagent)')
d = 60.5 * 0.3048; tb = d / (0.9 * c); tx = d / c
add('E02', 'c', r'60 nanosecond|nanosecond', 'X-ray shell reaches home plate after about 60 ns; the ball a handful of nanoseconds later', 'mound to plate 60 ft 6 in = 18.44 m (M); X-rays at c', f'x-ray {tx*1e9:.1f} ns; ball {tb*1e9:.1f} ns; gap {(tb-tx)*1e9:.1f} ns', 'MLB distance from memory; original article gives about 70 ns for the ball (F, page read)', 'M+S+F', 'CONSISTENT', '')
gam = 1 / math.sqrt(1 - 0.81); KE = (gam - 1) * 0.145 * c ** 2
add('E02', 'd', r'crater', 'SUPPLEMENTARY: the video gives no energy figure for the ball', 'mass 0.145 kg (M)', f'gamma={gam:.3f}; KE={KE:.2e} J = {KE/4.184e15:.1f} Mt TNT = {KE/(15*4.184e12):.0f} Hiroshima (15 kt); classical 0.5mv2 would be {0.5*0.145*(0.9*c)**2/4.184e15:.2f} Mt', 'Hiroshima 15 kt (F)', 'S+M+F', 'SUPPLEMENTARY', 'not a video claim; useful to scale the "crater" language')
add('E02', 'e', r'5\.05', 'MLB Rule 5.05(b)(2) would count it as hit by pitch', 'rulebook text', 'not checked', 'none', '-', 'NOT_VERIFIED', 'joke line; rulebook not read')
# ---------------- E03 Earthquake
E = lambda M: 10 ** (1.5 * M + 4.8)
add('E03', 'a', r'million times', 'A magnitude 15 quake is a million times more powerful than a magnitude 11', 'E = 10^(1.5M+4.8) J', f'E15/E11 = {E(15)/E(11):.1e}', 'Gutenberg-Richter joule form (F)', 'F', 'CONSISTENT', 'every result in this episode inherits the relation; with the USGS page\'s rough 1.44/5.24 form the ratios differ slightly (4 steps = 10^5.8)')
mw_ocean = 1.335e18 * 1000; Lv = 2.26e6; dT = 96; need = mw_ocean * (4186 * dT + Lv)
add('E03', 'b', r'evaporate all the water', 'M15 releases enough energy to evaporate all the water on Earth', 'ocean volume 1.335e18 m3 (M); heat from 4 C to 100 C plus vaporisation 2.26 MJ/kg (M); ignores ice and groundwater',
    f'E(M15)={E(15):.2e} J; needed {need:.2e} J; ratio {E(15)/need:.2f}', 'volume and latent heat from memory, not fetched', 'M+S', 'CONSISTENT_WITH_CAVEAT', 'within a factor of 2 (needs 1.8x more), so true only as "about"; no source fetched')
Eb_unif = 0.6 * G * Mearth ** 2 / Re
add('E03', 'c', r'ten to the thirty-two|binding energy of the earth', 'M18 releases nearly 1e32 J, roughly the Earth\'s gravitational binding energy', 'uniform-sphere 0.6 GM^2/R; a numerical profile value of 2.5e32 J was in a fetched forum summary',
    f'E(M18)={E(18):.2e} J; uniform-sphere binding {Eb_unif:.2e} J; ratio {E(18)/Eb_unif:.2f}; threshold M={(math.log10(Eb_unif)-4.8)/1.5:.1f}', 'binding energy: own computation (S) and a forum summary (F, low quality)', 'S+F', 'QUALIFIED', 'about 4x short of the binding energy: "roughly" holds only at order of magnitude')
add('E03', 'd', r'magnitude 24', 'The Sun could have up to a magnitude 24 quake', 'binding energy 2.3e41 (uniform) to 5.7e41 J (n=3 polytrope)', f'threshold M = {(math.log10(2.28e41)-4.8)/1.5:.1f} to {(math.log10(5.7e41)-4.8)/1.5:.1f}', 'see SC05 sources (F)', 'F', 'CONSISTENT', 'relation-dependent; same caveat as SC05')
add('E03', 'e', r'three and a half thousand', 'M10 needs a 3,500 km fault; M11 would need a fault half way round the world (about 20,000 km)', 'moment M0 = 10^(1.5 Mw + 9.1) N m; length L ~ M0^0.5 (width saturated) vs ^(1/3) (scale-invariant); anchors: Chile 1960 about 1,000 km (M), Sumatra 2004 about 1,300 km (M)',
    f'from 3,500 km at M10, M11 = {3500*10**0.75:,.0f} km (video: ~20,000); anchor Chile: L(M10) {1000*10**((10-9.5)*1.5/2):,.0f} km (exp 1/2), {1000*10**((10-9.5)*1.5/3):,.0f} km (exp 1/3); anchor Sumatra 2004 (M9.1): {1300*10**((10-9.1)*1.5/2):,.0f} km (exp 1/2)', 'rupture lengths from memory, not fetched', 'M+S', 'QUALIFIED', 'the video\'s step M10 to M11 equals the width-saturated scaling; the 3,500 km anchor is inside my 2,400 to 6,100 km spread; none of this is a tested seismological result')
add('E03', 'f', r'length of the day', 'M9+ quakes this century measurably changed the length of the day by a tiny fraction of a second', 'literature values about microseconds', 'not recomputed', 'none fetched', '-', 'NOT_VERIFIED', 'plausible; no source fetched')
mtruck = E(1) / (g0 * 10)
add('E03', 'g', r'cement truck', 'M1 equals a partially loaded cement truck dropped from 10 m', 'E=mgh', f'E(M1)={E(1):.2e} J -> m={mtruck:,.0f} kg', 'GR relation (F)', 'F+S', 'CONSISTENT', 'a mixer truck weighs about 13 to 30 t, so 20 t is a partial load')
KEp = lambda m, v: 0.5 * m * v ** 2
add('E03', 'h', r'Cowboys|football', 'M0 equals a whole football team hitting a garage; M-1 a single player', '110 kg players at 9 m/s (M); 11 or 53 players', f'E(M0)={E(0):.2e} J; 11 players {11*KEp(110,9):.2e} J; 53 players {53*KEp(110,9):.2e} J; E(M-1)={E(-1):.0f} J = one player at {math.sqrt(2*E(-1)/110):.1f} m/s', 'player mass and speed assumed', 'M', 'CONSISTENT_WITH_CAVEAT', 'matches an 11-player unit at 9 m/s; a full 53-man roster would be 4x more')
# ---------------- E04 Oceans
h = 10935; Torr = math.sqrt(2 * g0 * h); Q = math.pi * 10 ** 2 * Torr; Vo = 1.335e18; Ao = 3.61e14
add('E04', 'a', r'hundreds of thousands', 'It would take hundreds of thousands of years to drain the oceans through a 20 m portal at Challenger Deep', 'Torricelli outflow v=sqrt(2gh), h=10,935 m, portal area 314 m2, ocean volume 1.335e18 m3 (M); constant head (ideal)',
    f'v={Torr:.0f} m/s; Q={Q:.2e} m3/s; time {Vo/Q/yr:,.0f} years (head falls as it drains, friction ignored: longer)', 'volume and depth from memory (M); equation (S)', 'M+S', 'CONSISTENT', 'ideal outflow ignores compressibility, friction and the falling head; a discharge coefficient of 0.6 would lengthen it to about 480,000 years')
add('E04', 'b', r'centimeter per day', 'The water level drops by much less than a centimetre per day', 'ocean surface area 3.61e14 m2 (M)', f'{Q/Ao*86400*1000:.3f} mm per day', 'area from memory (M)', 'M', 'CONSISTENT', '')
add('E04', 'c', r'Black Sea', 'At -100 m the Black Sea stops shrinking because it is no longer connected', 'Bosphorus sill -32 to -40 m; Dardanelles sill -70 to -80 m (F, search summary)', 'sills 32 to 80 m below present level', 'search summary (F)', 'F', 'CONSISTENT_WITH_CAVEAT', 'true at -100 m, but the disconnection happens at about -35 to -80 m, so -100 m is not the threshold; the original article gives no figure')
add('E04', 'd', r'500 meters', 'At -500 m Japan becomes a causeway joining Korea and Russia', 'needs global bathymetry', 'not recomputed; the original article states the same -500 m (F, page read)', 'original article only', 'F', 'NOT_VERIFIED', 'no bathymetry data used')
add('E04', 'e', r'aircraft carrier', 'SUPPLEMENTARY: the video says pressure at the drain would fold an aircraft carrier', 'hydrostatic pressure rho g h, rho 1,025', f'p={1025*g0*h/1e6:.0f} MPa = {1025*g0*h/101325:.0f} atm', 'S+M', 'S+M', 'SUPPLEMENTARY', 'folding a hull at about 1,100 atm is plausible; not a quantified claim')
# ---------------- E05 Sun
q = sig * 5772 ** 4 / 1e4
add('E05', 'a', r'5,800', 'The Sun\'s surface is about 5,800 K', 'effective temperature 5772 K (IAU nominal)', f'sigma T^4 = {sig*5772**4:.3e} W/m2 = {q:.0f} W/cm2 (5,800 K: {sig*5800**4/1e4:.0f})', 'IAU nominal (S)', 'S', 'CONSISTENT', '')
add('E05', 'b', r'joules per', 'Skin absorbs about 1e-5 J/cm2 in a nanosecond at the surface', 'black-body flux, all absorbed, 1 ns', f'{q*1e-9:.2e} J/cm2 (stated 1e-5; factor {1e-5/(q*1e-9):.1f})', 'Stefan-Boltzmann (S)', 'S', 'CONSISTENT', 'stated "about 10^-5", computed 6.3e-6; skin absorptivity below 1 would lower it')
add('E05', 'c', r'butane|second-degree', 'Holding a finger in a butane flame for 1 s delivers about 5 J/cm2, roughly the threshold for a second-degree burn (IEEE 1584)', '1.2 cal/cm2 burn curve (M)', f'1.2 cal/cm2 = {1.2*4.184:.2f} J/cm2; time at the Sun surface to reach 5 J/cm2 = {5/q*1e3:.2f} ms', 'IEEE 1584 not fetched; conversion own', 'M+S', 'CONSISTENT_WITH_CAVEAT', 'conversion matches; the standard was not read')
T1fs = (5e4 / (sig * 1e-15)) ** 0.25
add('E05', 'd', r'femtosecond', 'You would exceed the second-degree burn standard after one femtosecond in the Sun (interior)', 'absorbed flux sigma T^4 in a black-body field of temperature T; threshold 5 J/cm2 = 5e4 J/m2',
    f'one femtosecond suffices only if T >= {T1fs/1e6:.1f} MK; at 15 MK (core) the threshold is reached in {5e4/(sig*1.5e7**4)*1e15:.3f} fs; at 3 MK it needs {5e4/(sig*3e6**4)*1e15:.0f} fs; at the surface 0.79 ms', 'Stefan-Boltzmann (S); core 15 MK (M)', 'S+M', 'CONSISTENT_WITH_CAVEAT', 'true for the deep interior (above about 5.5 MK), false for "a few million degrees" at the low end; the video places you inside after a "wrong coordinates" jump')
add('E05', 'e', r'30,000,000|thirty million', 'You spend 1 ns but your brain needs 30,000,000 ns to notice; 1 ns = 1,000,000 fs', 'arithmetic', '30,000,000 ns = 30 ms; 1 ns = 1e6 fs', 'arithmetic', 'S', 'CONSISTENT', 'the physiological 30 ms latency was not checked against a source')
# ---------------- E06 Earth rotated 90 degrees
add('E06', 'a', r'few hundred feet', 'Melting of the ice caps would push the ocean up by a few hundred feet', 'total land-ice sea-level potential about 65 to 70 m = 215 to 230 ft (M)', f'{65*3.281:.0f} to {70*3.281:.0f} ft', 'not fetched', 'M', 'NOT_VERIFIED', 'about 215 to 230 ft if all ice melted; "a few hundred" is a loose match')
add('E06', 'b', r'horse latitudes', 'Horse latitudes lie a bit poleward of 30 degrees', 'subtropical high-pressure belts at roughly 30 to 35 degrees', 'qualitative', 'not fetched', 'M', 'NOT_VERIFIED', 'qualitative climatology; no model run; the whole episode is a narrative counterfactual with no stated quantitative model')
# ---------------- E07 Moon black hole
rs = 2 * G * Mmoon / c ** 2
add('E07', 'a', r'sand grain', 'The event horizon would be about the size of a sand grain, passing an ASTM No. 70 or larger sieve', 'sieve No. 70 opening 212 um, No. 60 250 um (F); horizon diameter 2 r_s', f'r_s={rs*1e6:.0f} um, diameter {2*rs*1e6:.0f} um vs 212 um opening ({(2*rs*1e6/212-1)*100:+.0f}%)', 'ASTM E11 table (F, search summary); Moon mass NASA (F)', 'F+S', 'QUALIFIED',
    'the horizon diameter (218 um) is 3% above the No. 70 opening, so it would just be stopped by No. 70 and pass No. 60; the radius (109 um) passes easily. The sentence is the same in the original article (page read), so this is inherited and borderline, not a clear error')
Rm_mass = Rm * c ** 2 / (2 * G)
add('E07', 'b', r'600 times', 'A black hole the size of the Moon would have around 600 times the mass of the Sun', 'r_s = 2GM/c^2 solved for M with r_s = 1737.4 km', f'M = {Rm_mass/Msun:.0f} solar masses', 'constants (S); lunar radius NASA (S)', 'S', 'CONSISTENT', '')
add('E07', 'c', r'milli-degrees', 'Infrared moonlight warms Earth by about 1.2 milli-degrees Fahrenheit', 'Moon absorbs (1-0.12) S pi R^2, re-emits over the day hemisphere; Earth absorbs it fully, global mean = flux/4; no-feedback response dT/dF = 1/(4 sigma T^3), T=255 K; full Moon (maximum)',
    f'flux at Earth {0.88*1361*math.pi*Rm**2/(2*math.pi*dMoon**2):.4f} W/m2; mean forcing {0.88*1361*math.pi*Rm**2/(2*math.pi*dMoon**2)/4:.4f} W/m2; dT {0.88*1361*math.pi*Rm**2/(2*math.pi*dMoon**2)/4/(4*sig*255**3)*1000:.2f} mK = {0.88*1361*math.pi*Rm**2/(2*math.pi*dMoon**2)/4/(4*sig*255**3)*1000*1.8:.1f} m degF at full Moon; phase-averaged about half', 'Moon albedo 0.12, S=1361 (M)', 'M+S', 'CONSISTENT_WITH_CAVEAT', 'my crude estimate is 0.8 to 1.5 m degF, the same order as 1.2; the video\'s figure is credited to a calculation in the original article, not recomputed independently')
add('E07', 'd', r'Romer|Rankin', '1.2 m degF = 1.2 m degR = 0.35 m deg Romer = 0.53 m deg Reaumur = 2/3 mK', 'degree sizes: R=F; Romer 21/40 per C; Reaumur 4/5 per C; K=5/9 F', f'{1.2*5/9:.3f} mK; Romer {1.2*5/9*0.525:.3f}; Reaumur {1.2*5/9*0.8:.3f}', 'scale definitions (S)', 'S', 'CONSISTENT', 'the catalog caption garbles the unit names ("milligrees ranken"); ASR has the correct words')
# ---------------- E08 Submarine
Msub = 18750e3; csteel = 500
add('E08', 'a', r'half a degree|degree Celsius', 'A 200 MW reactor warms the whole sub by about half a degree Celsius every minute', 'sub 18,750 t (Ohio class submerged displacement, M), steel-like c=500 J/kg/K, all reactor heat retained',
    f'at 200 MW: {200e6*60/(Msub*csteel):.2f} K/min; at 100 MW: {100e6*60/(Msub*csteel):.2f} K/min; 0.5 K/min needs m*c = {200e6*60/0.5:.2e} J/K (200 MW)', 'displacement from memory (M)', 'M', 'QUALIFIED', 'the video\'s 0.5 K/min implies a heat capacity 2.6x above a steel-only estimate (water and air add some); order of magnitude agrees')
add('E08', 'b', r'4 meters per second|hundred meters per second', '24 Trident missiles at 4 m/s each give about 100 m/s, enough to de-orbit', 'momentum: dv = m_prop v_e / M_sub; Trident II about 59 t launch mass, about 50 t propellant, v_e 2.5 km/s (M)',
    f'24 x 4 = 96 m/s; one missile dv = {50e3*2500/Msub:.1f} m/s; de-orbit from 400 km (perigee 50 km): {(math.sqrt(3.986004418e14/(Re+400e3))-math.sqrt(3.986004418e14*(2*(Re+50e3)/((Re+400e3)*((Re+400e3)+(Re+50e3))))))/1:.0f} m/s', 'missile mass and exhaust speed from memory (M); mu_earth (S)', 'M+S', 'QUALIFIED', 'the 4 m/s per missile is the right order (about 6.7 m/s by my rough impulse); de-orbit delta-v about 120 m/s at 400 km, "in the neighbourhood of 100" holds')
# ---------------- E09 Laser
A_moon = math.pi * Rm ** 2; S = 1361.0
add('E09', 'a', r'6 petawatts', 'Sunlight on the Moon\'s bright half is about 6 petawatts (stated: about a kilowatt per m2 times 10 trillion m2)', 'cross-section 9.48e12 m2; S=1361 W/m2', f'S x A = {S*A_moon/1e15:.1f} PW; stated 6 PW is {6e15/(S*A_moon):.2f} of that', 'TSI standard (S, not fetched); original article gives about 1e16 W (F, page read)', 'S+F', 'QUALIFIED',
    'the video\'s own two numbers multiply to about 13 PW, not 6. The whiteboard shows 6,450,000,000,000,000 W, which is 0.5000 x S x pi R^2 (6.453e15), i.e. exactly half, not a visible-band share (about 45%). The cross-section already is the intercepted area of the bright side, so halving it again is unexplained; the original article says about 10 PW. Does not change the conclusion that the lasers are negligible (ratio 4e8 instead of 2e8)')
add('E09', 'b', r'30 megawatts', 'All 5 mW lasers add up to about 30 MW, 200 million times weaker', 'N people x 5 mW', f'30 MW / 5 mW = {30e6/5e-3:.1e} people; at 8.1e9 people: {8.1e9*5e-3/1e6:.1f} MW; 6e15/3e7 = {6e15/3e7:.1e}', 'population (M)', 'M', 'CONSISTENT_WITH_CAVEAT', 'internally consistent at 6e9 people; with 8.1e9 it would be 40 MW and 150 million times weaker')
lm = lambda W, Vl: W * Vl * 683
add('E09', 'c', r'half a lux', '1 W lasers for everyone light the Moon with about half a lux', 'N lasers each 1 W spread over the Moon\'s cross-section; luminous efficacy V(555 nm)=1.00, V(450 nm)=0.038 (S); N 7e9 and 8.1e9',
    f'green 555 nm: {lm(7e9,1.0)/A_moon:.2f} lux (7e9), {lm(8.1e9,1.0)/A_moon:.2f} lux (8.1e9); blue 450 nm: {lm(8.1e9,0.038)/A_moon:.3f} lux', 'photopic efficacy (S, not fetched)', 'S', 'CONSISTENT_WITH_CAVEAT', 'matches only for green light at peak efficacy; the script text says "blue flashlight" in the preceding paragraph but the original says green')
add('E09', 'd', r'half as bright', 'That is about half as bright as moonlight is to us on Earth', 'original article: full Moon about 1 lux (F, page read); common values 0.1 to 0.3 lux (M)', 'on screen: laser-lit Moon 0.5 LUX vs moonlight 1 LUX, so half within the video; literature full-Moon illuminance 0.1 to 0.3 lux (M, not fetched) would make 0.5 lux 2 to 5x brighter', 'mixed', 'F+M', 'OPEN', 'the compared quantities differ (laser-lit illuminance of the Moon\'s surface vs light the Moon sends to Earth) and the 1 lux full-Moon figure is higher than typical literature values; definitions and source needed')
add('E09', 'e', r'130,000', 'Sunlight gives 130,000 lux', '1361 W/m2 x about 93 lm/W (M)', f'{1361*93:,.0f} lux', 'efficacy of sunlight from memory', 'M', 'CONSISTENT', '')
add('E09', 'f', r'factor of 2', '20 lux outshines the ambient light on the Moon\'s night half by a factor of 2', 'earthshine on the Moon about 0.25 lux x (R_E/R_M)^2 x (Bond albedo 0.306/0.11) (M)', f'{0.25*(Re/Rm)**2*0.306/0.11:.1f} lux; 2 x that = {2*0.25*(Re/Rm)**2*0.306/0.11:.0f} lux', 'full-Moon lux 0.25 and albedos from memory', 'M', 'CONSISTENT_WITH_CAVEAT', 'my earthshine estimate is about 9 lux, so 20 lux is about 2x as stated; assumptions not fetched')
P_need = 130000 / 683 * A_moon
add('E09', 'g', r'petawatts of power', 'Matching sunlight draws 5 petawatts, which is double the world\'s average electricity consumption', 'optical power for 130,000 lux of 555 nm light over the cross-section; wall-plug efficiency 36%; world demand 29,471 TWh in 2023 (Ember, F)',
    f'optical {P_need/1e15:.2f} PW; at 36% efficiency {P_need/0.36/1e15:.1f} PW; world average electricity {29471e12*3600/(365*24*3600)/1e12:.2f} TW -> 5 PW is {5e15/(29471e12*3600/(365*24*3600)):,.0f}x it; 5 TW would be {5e12/(29471e12*3600/(365*24*3600)):.1f}x', 'Ember (F); the original article has the same wording (F, page read)', 'F+S', 'DISCREPANT_AS_STATED',
    'the 5 PW figure is plausible for matching sunlight, but it is about 1,500 times world average electricity, not double; "double" fits 5 terawatts. ASR and catalog both say petawatts and the original has the same wording, so listening cannot settle a transcript slip; the units need the authors\' confirmation')
add('E09', 'h', r'Asia|50 trillion', 'A megawatt laser on every square meter of Asia: 50 trillion lasers, which uses up Earth\'s oil reserves in about 2 minutes', 'Asia 44.6e12 m2 (M); 1 MW each; oil reserves about 1.7e12 bbl x 6.1e9 J (M)', f'{44.6e12*1e6:.1e} W; {44.6e12*1e6*120:.1e} J in 120 s vs reserves {1.7e12*6.1e9:.1e} J (ratio {44.6e12*1e6*120/(1.7e12*6.1e9):.2f})', 'values from memory, not fetched', 'M', 'CONSISTENT_WITH_CAVEAT', 'ASR writes "soil reserves", an apparent ASR error (catalog says oil); within a factor of 2')
add('E09', 'j', r'0 and 120', 'Most of the world\'s population lives between 0 and 120 degrees east (screen: 75% WORLD POPULATION)', 'needs population by longitude', 'not computed (no gridded population data)', 'none', '-', 'NOT_VERIFIED', 'the 75% label appears on screen only')
add('E09', 'i', r'quarter cup', 'NIF: 500 TW for a few ns equals a quarter cup of gasoline', 'about 1.85 MJ on target (LLNL, found earlier); gasoline 34 MJ/L (M); quarter cup 59 mL', f'quarter cup gasoline = {0.0591*34.2:.2f} MJ vs 1.85 MJ', 'LLNL page (F); gasoline energy density (M)', 'F+M', 'CONSISTENT', 'screen label "500 TW ~2 ns" multiplies to about 1 MJ, half of the quarter-cup figure (2 MJ), because the pulse is not a flat 500 TW')
# ---------------- E10 Billion-story
fl = 4.0
add('E10', 'a', r'halfway to space|ten thousand', 'Stacking 100 skyscrapers (100 floors each) reaches halfway to space; 1e4, 1e6, 1e8 floors; 10 more steps give 1e9', 'floor height about 4 m (M); space = 100 km (Karman line, M)', f'1e4 floors = {1e4*fl/1000:.0f} km (0.4 of 100 km); 1e6 = {1e6*fl/1000:,.0f} km; 1e8 = {1e8*fl/1000:,.0f} km (Moon at 384,400 km); 1e9 = {1e9*fl/1000:,.0f} km = {1e9*fl/1000/384400:.1f} Moon distances', 'floor height assumed', 'M', 'CONSISTENT', 'the floor counts are exact arithmetic; "halfway to space" is 0.4 at 4 m per floor (loose)')
gp, ge = 9.832186, 9.780327
add('E10', 'b', r'half a percent', 'Objects weigh about half a percent less at the equator than at the poles', 'WGS84 normal gravity', f'(g_pole-g_eq)/g_pole = {(gp-ge)/gp*100:.2f}%; centrifugal part alone = {om0**2*Re_eq/ge*100:.2f}%', 'WGS84 from memory (M); angular rate (S)', 'M+S', 'CONSISTENT', '')
add('E10', 'c', r'tenth of the way', 'Gravity and centrifugal effects balance just over a tenth of the way to the Moon, so a satellite could be launched by letting go', 'geostationary radius 42,164 km from the centre', f'{42164/384400:.3f} of the Moon distance from Earth\'s centre ({35786/384400:.3f} from the surface)', 'F (see SC10)', 'F', 'CONSISTENT', 'at that radius a corotating release has orbital speed, so the "let go" statement is physically right for an idealised rigid tower')
add('E10', 'd', r'2 or even 3 kilometers', 'Buildings 2 or 3 km tall could stand under their own weight', 'compressive stress limit height = sigma/(rho g); steel 250 MPa, 7,850 kg/m3; concrete 40 MPa, 2,400 kg/m3 (M); no buckling, wind or safety factor', f'steel {250e6/(7850*g0)/1000:.1f} km; concrete {40e6/(2400*g0)/1000:.1f} km', 'material properties from memory', 'M', 'CONSISTENT_WITH_CAVEAT', 'a uniform steel column tops out at about 3 km, concrete at 1.7 km; real buildings taper, so 2 to 3 km is plausible but not a tested design')
VIS = {
 'E01a': 'Screen 62.4 s: label "470 m/s (1040 mph)" on a bunker scene; schematic drawing, not a simulation. 14.9 s: a house and a figure before the wind (no number).',
 'E01b': 'Screen 33.8 s and 37.4 s: equirectangular map with a horizontal band marked 42 N / 42 S and arrows labelled 470 m/s; the band is a flat stripe although speed varies with cos(latitude); "85% OF POPULATION" appears as an overlay at 37.4 s.',
 'E01c': 'Screen 77.9 s: Boston skyline with "330 m/s" and "*NO LONGER SUPERSONIC :(" . The recomputed speed at 42.36 N is 344 m/s (Mach 1.002), so the on-screen 330 m/s is 4% lower than the geometry gives; narration says "twice as strong" as tornadoes, the screen gives no tornado comparison.',
 'E01f': 'Screen 221.9 s and 226.0 s: stick figure at a table with "6 MONTHS" in sunlight and "6 MONTHS" in the dark (grey side-by-side panel); axial tilt not drawn.',
 'E02a': 'Screen 40.0 s: ball labelled 604,000,000 mph (recomputed 603.6 million) with air molecules labelled ~1,000 mph; screen 44.3 s strikes the ~1,000 mph out and writes 0 mph (ball frame).',
 'E02b': 'The screen shows ~1,000 mph for the molecules (matches kinetic theory, 1,050 to 1,150 mph) while the narration says "a few hundred miles per hour": spoken and drawn values disagree by a factor of 3.',
 'E02c': 'Screen 79.7 s "T = 60 NANOSECONDS" with a ~1c arrow; 115.2 s and 132.9 s "T = 63 NANOSECONDS" with a 1c wave; recomputed X-ray arrival 61.5 ns and ball 68.3 ns.',
 'E02e': 'Screen 173.2 s: a rulebook page "OFFICIAL BASEBALL RULES RULE 5.05 (b)" with the hit-by-pitch wording visible; the text was not compared with the official rulebook.',
 'E03a': 'Screen: a vertical magnitude axis (marks from -15 to 30) with an arrow at the stated magnitude on every card; the axis is quantitative, the pictures on it (cracked Earth, Sun disc, Jupiter-like planet, hourglass) are schematic.',
 'E03c': 'Screen 71.0 s: "MAGNITUDE 18" with the label "10^32 JOULES = BYE BYE EARTH" and a shattered Earth; recomputed 6.3e31 J.',
 'E03e': 'Screen 41.3 s: globe with "MARCH 2011 9.0-9.1" and "9.1-9.3 DECEMBER 2004" labels (magnitudes of the two quakes).',
 'E03g': 'Screen 120.0 s: cement mixer truck above a house with "10m" and arrow, on the magnitude-1 card.',
 'E03h': 'Screen 126.9 s: a pile of helmeted football players against a garage wall on the magnitude-0 card.',
 'E04a': 'Screen 8.7 s and 15.7 s: cut-away of Challenger Deep with the portal; 35.6 s: globe with "MARIANA TRENCH PORTAL".',
 'E04c': 'Screen 90.0 s: world map "-100 m" with the Black Sea circled in red; maps for -50, -100, -200, -500 (116 to 122 s), -1000 and -5000 m use flat fills whose coastlines look contour-derived (provenance not checked).',
 'E04d': 'Screen 119.0 s and 122.0 s: "-500 m" map with Japan circled and joined to the mainland; the narration sentence starts at 113.4 s, so a frame at the ASR time shows the previous level (-200 m).',
 'E05a': 'Screen 21.7 s: dark gradient panel "~5,800 K" with a shovelling figure and "1 NANOSECOND" between two "HOURS" panels.',
 'E05b': 'Screen 98.7 s and 104.3 s: "0.00001 J/cm2" and "0.000000001 s" panels (computed 6.3e-6).',
 'E05c': 'Screen 98.7 s: "IEEE STANDARD 1584-2018 (GUIDE FOR PERFORMING ARC-FLASH HAZARD CALCULATIONS)", "5 J/cm2", "1s", "(DON\'T DO THIS)" with a lighter flame; the whiteboard at 136.4 s says "IEEE P1584B", so two designations appear.',
 'E05d': 'Screen 136.4 s: whiteboard with P/A = sigma T^4 (W/m2) and "1 FEMTOSECOND > IEEE P1584B"; 152.4 s: wavy "X-RAYS" arrows hitting a body drawing; 184 s: "TEMPERATURE != HEAT; HEAT = TEMPERATURE x TIME", an informal slide that is not dimensionally valid as written.',
 'E05e': 'Screen 72.2 s and 88.2 s: logarithmic time axis in nanoseconds (1 to 10^6 and 30x10^6) with eye, retina, nerve and brain icons; red arrows mark 1 ns and 30 ms.',
 'E06a': 'Screen 356.9 s: hill and sea line with "(THE NETHERLANDS FINALLY FLOODS)"; the maps in this episode are coloured (green, tan, light blue, grey) unlike the mostly achromatic other episodes.',
 'E06b': 'Screen 123.4 s and 130.7 s: rotated-world map with wind arrows and two orange bands labelled HORSE LATITUDES; 72.6 s: a three-cell circulation diagram (Hadley, Ferrel, Polar).',
 'E07a': 'Screen 27.6 s: a scanned "WENTWORTH GRADE SCALE" chart with red circles on two rows; 46.0 s: MOON vs BLACK HOLE MOON side by side, the black hole drawn as a dot.',
 'E07c': 'Screen 156.5 s to 174.9 s: IR arrows Moon to Earth, "10X" arrows and "+/-0.01 C" for the Sun-Moon effect; the list reads +0.0012 F, +0.0012 R, +0.00035 Romer, +0.00053 Reaumur, +0.00066 Kelvin.',
 'E07d': 'Screen 174.9 s shows +0.00066 K where 1.2 m degF = 0.000667 K (rounded down).',
 'E08a': 'Screen 140.7 s: "200 MEGAWATT" label on the reactor; 161.8 s: red heat marks on the reactor section; 122.0 s: "WHY SPACE IS WARM" with arrows leaving the hull.',
 'E08b': 'Screen 215.8 s: two panels "DELTA V ~ 100 m/s" and "24 x 4 m/s ~ 100 m/s"; 84.4 s: "T = 2/(3 k_B) x KE_average" (correct kinetic-theory relation); 103.2 s: sparks labelled "~2000 F (1100 C)" (2000 F = 1093 C).',
 'E09a': 'Screen 53.8 s: whiteboard with "~10^13 m2" and "~6,450,000,000,000,000 W" over a shaded half-disc of the Moon; narration says "about 6 petawatts".',
 'E09b': 'Screen 72.1 s: a figure aiming a "1 WATT" laser and a "5 MILLIWATT" pointer at a Moon poster.',
 'E09d': 'Screen 103.1 s to 109.5 s: red Moon "<- 0.5 LUX" versus a white Moon "1 LUX ->" with two figures on a hill, then a "130,000 LUX" glare panel.',
 'E09f': 'Screen 138.5 s: "NIGHTSUNS (WITH LENSES)" beams to the Moon and a "BEFORE" moon; 168.3 s "LUXOR SPOTLIGHTS".',
 'E09g': 'Screen 194.3 s: a grid of 747-style aircraft firing lasers versus two Earths plugged into a wall outlet, i.e. the picture itself shows the "double the world\'s electricity" comparison.',
 'E09h': 'Screen 216.4 s: a fuel-pump icon labelled "2 MIN" beside "GREAT ASIAN LASER ARRAY"; the pump supports the catalog word "oil" over the ASR word "soil".',
 'E09i': 'Screen 234.3 s: "NATIONAL IGNITION FACILITY" with "500 TW ~2 ns" next to a person for scale.',
 'E10a': 'Screen 99.7 s to 135.9 s: bar-and-arrow diagrams "FLOORS 100 / 10,000 / 1,000,000, GOAL: 1,000,000,000" with HOUSE, SKYSCRAPER, MOUNTAINS, AIRPLANES, SPACE, AIR, EARTH labels; schematic, not to scale.',
 'E10b': 'Screen 158.9 s: Earth with "WEIGHT MAXIMUM" and "WEIGHT MINIMUM" arrows and Fg / Fc vectors.',
 'E10c': 'Screen 167.5 s and 172.1 s: "GRAVITY WINS | CENTRIFUGAL WINS" bracket between Earth and Moon and "1/10th TO THE MOON" with a figure at a window dropping a satellite.',
 'E10d': 'Screen 45.3 s: a bar-style height chart with axis ticks 100 m, 1, 2 and 3 km and a collapsed pile at the right end; the axis is broken between 100 m and 1 km.'}
for r in rows: r['visual_vs_spoken'] = VIS.get(r['claim_id'], '')
w = csv.DictWriter(open(A + '/07e_EPISODE_CLAIM_CHECKS.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
import collections
print(len(rows), collections.Counter(r['verdict'] for r in rows))
for r in rows: print(r['claim_id'], r['verdict'], '|', r['recomputed'][:170])
