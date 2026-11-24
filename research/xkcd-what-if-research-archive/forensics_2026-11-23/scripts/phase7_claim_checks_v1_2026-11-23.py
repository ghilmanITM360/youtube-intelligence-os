"""Phase 7 independent physics check of 10 quantitative claims made in the xkcd What If? videos. Each claim: video ID, script paragraph locator, ASR time, quoted wording, the computation done here
(stdlib only), reference values with source, and a verdict. Verdict scale: CONSISTENT (recomputed within the claim's own rounding), CONSISTENT_WITH_CAVEAT, DISCREPANT, NOT_VERIFIED (no authoritative source reached).
Reference constants: CODATA 2018 / IAU / NASA values that are defined or standard (G, c, sigma, g0, Earth equatorial radius 6378.137 km, sidereal day 86164.1 s, solar mass/radius/Teff) are marked 'standard constant';
anything fetched this session is listed with its URL. Run: python3 -I scripts/phase7_claim_checks.py"""
import csv, json, math, re, os
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RS = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/what-if-scripts/'
V = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
inv = {i['id']: i for i in json.load(open(RS + 'analysis/inventory.json'))}
G, c, sig, g0 = 6.6743e-11, 299792458.0, 5.670374419e-8, 9.80665
Rearth_eq, Rearth, Dsid = 6378.137e3, 6371.0e3, 86164.0905
Msun, Rsun, Tsun, Mmoon, dMoon = 1.98847e30, 6.957e8, 5772.0, 7.342e22, 384400e3
def segs(vid):
    for f in (f'{A}/phase7b_asr/{vid}.json', f'{A}/phase7c_asr/{vid}.json'):
        if os.path.exists(f):
            return [(s['offsets']['from'] / 1000, s['text'].strip()) for s in json.load(open(f))['transcription']]
    d = json.load(open(f'{V}{vid}/asr/asr_small_en.json')); return [(s['start'], s['text'].strip()) for s in d['segments']]
def when(vid, pat):
    for t, x in segs(vid):
        if re.search(pat, x, re.I): return round(t, 1), x
    return '', ''
def para(vid, pat):
    t = open(RS + inv[vid]['script']).read().split('## Script\n', 1)[1]
    ps = [p for p in t.split('\n\n') if p.strip()]
    hits = [n for n, p in enumerate(ps, 1) if re.search(pat, p, re.I)]
    return ';'.join(f'para{n}' for n in hits[:3]) if hits else 'word-level only (caption block; see ASR time)'
rows = []
def add(cid, vid, pat, claim, assumptions, calc, ref, verdict, vis, note):
    t, q = when(vid, pat); rows.append(dict(claim_id=cid, video_id=vid, vid=inv[vid]['vid'], script_locator=para(vid, pat), asr_time_s=t, asr_quote=q[:160], claim=claim, assumptions=assumptions,
                                           recomputed=calc, reference=ref, verdict=verdict, visual_representation=vis, note=note))
# C1 Earth grows 1 cm/s
dR = 0.01 * 30 * 86400; g100 = (Rearth + 0.01 * 100 * 365.25 * 86400) / Rearth
add('SC01', '-1-ldW4kpLM', r'26 kilomet', 'After a month the Earth would have expanded by 26 km, +0.4 percent', 'radius grows 1 cm/s, 30-day month; mean radius 6371 km',
    f'dR={dR/1e3:.2f} km; {dR/Rearth*100:.2f}% of 6371 km', 'standard constants (IAU nominal mean radius)', 'CONSISTENT', 'MECH: "T = 1 MONTH" with a globe and a thin outer shell (t=109.2 s, coded 07)', 'arithmetic only')
add('SC02', '-1-ldW4kpLM', r'over 6 G', 'After 100 years we would experience over 6 g', 'radius grows 1 cm/s for 100 Julian years; constant density so g scales with R',
    f'R/R0={g100:.2f}, so g={g100:.2f} g0', 'standard; g ~ R at constant density (Newton shell theorem)', 'CONSISTENT_WITH_CAVEAT',
    'SBS "1G | 6G" with a figure lying down (t=216.5 s)', 'narration says "over 6" and the screen says 6G; recomputed 5.95 (about 6). If density fell as new material was added the number would change; the video does not state its density assumption')
# C2 lightning to power a house
eia = 865 * 3.6e6 / 30.4; l_lo, l_mid, l_hi = 1e9, 1.5e9, 5e9
add('SC03', 'fs28lEq9smw', r'two days|house', 'A typical lightning strike delivers enough energy to power a house for about two days', 'US residential use about 865 kWh/month (EIA, 2024) = 28.4 kWh/day',
    f'house/day={eia/1e6:.0f} MJ; two days={2*eia/1e6:.0f} MJ; 1 GJ flash = {l_lo/eia:.1f} days, 1.5 GJ = {l_mid/eia:.1f} days, 5 GJ = {l_hi/eia:.0f} days',
    'NOAA expert via National Geographic: typical flash 1,000 to 5,000 MJ, full range about 100 to 30,000 MJ (https://www.nationalgeographic.com/science/article/120308-energy-in-forces-of-nature); research value 1.5 GJ (https://arxiv.org/pdf/2101.12361); EIA household use (https://www.eia.gov/tools/faqs/faq.php?id=97&t=3)',
    'DISCREPANT', 'LABEL/MAP frames of lightning (07 coding, t=36.8 s shot)', '"two days" needs about 0.2 GJ, below the 1-5 GJ typical range and at the low end of the 0.1-30 GJ full range; 1-5 GJ would run an average house 10 to 50 days. The video may use energy delivered to ground or a different house load; its basis is not stated in the script. Needs the video authors\' source')
# C3 key press energy
m = 1.5e-3 / (g0 * 300e-6); dT = 1.5e-3 / (0.05e-3 * 4186)
add('SC04', '0L44GEJ5pLE', r'squirrel', '1.5 mJ heats a drop of water by 1% of a degree and lifts a squirrel 300 microns', 'drop = 0.05 mL (0.05 g); c = 4.186 J/g/K; squirrel mass implied by E = m g h',
    f'implied squirrel mass {m:.2f} kg; dT for 0.05 g = {dT:.4f} K; for dT=0.01 K the drop is {1.5e-3/(0.01*4186)*1e3:.3f} g', 'standard constants (water specific heat, g0)', 'CONSISTENT_WITH_CAVEAT',
    'OBJ/LABEL: "1.5 MILLIJOULES", droplet "+0.01 C", squirrel "300 MICRONS" (shot at about t=57 s)', 'works for a 0.5 kg squirrel and a 0.036 g drop; typical drops are 0.03-0.05 mL, so "1%" is a fair rounding of 0.7%; four sheets of paper (about 0.4 mm) is a loose match for 300 microns')
# C4 magnitude 25
def E(M): return 10 ** (1.5 * M + 4.8)
Ebind_unif = 0.6 * G * Msun ** 2 / Rsun; Ebind_real = 6.9e41
add('SC05', 'e3uk7jU3RHo', r'magnitude 25', 'A magnitude 25 quake would explode the Sun', 'seismic energy E = 10^(1.5 M + 4.8) J (USGS energy-magnitude relation); Sun gravitational binding energy as the threshold',
    f'E(M25)={E(25):.2e} J; Sun binding: uniform-density bound {Ebind_unif:.2e} J, realistic profile about {Ebind_real:.1e} J; threshold magnitude {(math.log10(Ebind_real)-4.8)/1.5:.1f} (realistic) or {(math.log10(Ebind_unif)-4.8)/1.5:.1f} (uniform)',
    'standard relation and constants; binding energy of the real Sun (about 7e41 J) is a literature value not fetched this session', 'CONSISTENT_WITH_CAVEAT', 'scale ladder drawn schematically (07 coding)',
    'M25 exceeds both thresholds by 3x to 9x; the statement is true only under the assumption that "magnitude" extrapolates the moment-magnitude energy law far outside any measured range (no earthquake physics applies at those scales)')
# C5 snow melt
add('SC06', 'WYf9-xfm6t8', r'335 joules', 'Melting a gram of snow takes about 335 joules', 'latent heat of fusion of ice at 0 C = 333.55 J/g', f'333.55 vs 335 J: +{(335/333.55-1)*100:.1f}%', 'standard value (IAPWS/CRC; not fetched)', 'CONSISTENT', 'MECH/LABEL', 'ignores warming from below 0 C, which for snow at -10 C adds about 21 J/g')
# C6 moon black hole
rs = 2 * G * Mmoon / c ** 2
add('SC07', 'UQgw50GQu1A', r'event horizon', 'A black hole with the Moon\'s mass has an event horizon about the size of a sand grain', 'Schwarzschild radius r = 2GM/c^2, Moon mass 7.342e22 kg',
    f'r_s={rs*1e3:.3f} mm, diameter {2*rs*1e3:.3f} mm (Wentworth fine sand 0.125-0.25 mm)', 'standard constants; sand-size classes (Wentworth scale, not fetched)', 'CONSISTENT', 'OBJ/SCALEREF: "ELECTRON MOON" related frames; a grain-of-sand comparison', 'radius 0.11 mm or diameter 0.22 mm both fall in fine sand; "event horizon" size is a radius, so a 0.2 mm-wide sphere is the correct picture')
# C7 500 trillion calories
add('SC08', 'PUtI3xoaHx0', r'500 trillion', 'There are about 500 trillion calories of human in the world', 'about 8e9 people, mean mass 45 to 62 kg, 1,000 to 2,400 kcal per kg of body',
    f'range {8e9*45*1000/1e12:.0f} to {8e9*62*2400/1e12:.0f} trillion kcal', 'author back-of-envelope only: body energy density and mean mass were not fetched', 'NOT_VERIFIED', 'LABEL: "EARTH 500,000,000,000" with people ringing a globe (t=11.4 s)',
    'the claim is within the author\'s own range, so the order of magnitude is plausible, but no authoritative source was checked and "calories" here means kilocalories')
# C8 equatorial speed
v = 2 * math.pi * Rearth_eq / Dsid
add('SC09', 'gp5G1QG6cXc', r'thousand miles|470|1,000 miles', 'The surface moves about 1,000 mph relative to the axis; on screen "470 m/s (1040 mph)"', 'equatorial radius 6378.137 km, sidereal day 86164.09 s',
    f'v={v:.1f} m/s = {v/0.44704:.0f} mph', 'NASA NSSDC Earth Fact Sheet radius (https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html); sidereal day standard', 'CONSISTENT_WITH_CAVEAT',
    'MAP/LABEL "470 m/s" band on the map (several Shorts)', 'the equatorial speed is 465 m/s; "470 m/s" is a rounding that does not equal 1,040 mph (470 m/s = 1,051 mph); "a thousand miles an hour" is 4% low. Speed falls with cos(latitude), which the map band shows only qualitatively')
# C9 geostationary
add('SC10', 'Z_xJ40QXu7Q', r'geostationary|tenth', 'Gravity and centrifugal effects equalise just over a tenth of the way to the Moon (geostationary height)', 'geostationary radius from Earth centre 42,164 km; Moon mean distance 384,400 km',
    f'42,164/384,400={42164/384400:.3f}', 'standard constants (geostationary orbit radius; not fetched)', 'CONSISTENT', 'AXIS/SCALEREF (skyscraper on a distance axis)', 'distance is measured from the Earth centre; from the surface the figure is 35,786 km (9.3%)')
w = csv.DictWriter(open(A + '/07_SCIENCE_CLAIM_CHECKS.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r['claim_id'], r['verdict'], r['script_locator'], r['asr_time_s'], '|', r['recomputed'][:150])
