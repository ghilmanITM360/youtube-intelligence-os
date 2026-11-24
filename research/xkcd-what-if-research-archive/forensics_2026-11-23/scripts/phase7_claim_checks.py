"""Phase 7 independent physics check of 10 quantitative claims made in the xkcd What If? videos. Each claim: video ID, script paragraph locator, ASR time, quoted wording, the computation done here
(stdlib only), reference values with source, and a verdict. Verdict scale: CONSISTENT (recomputed within the claim's own rounding), CONSISTENT_WITH_CAVEAT, DISCREPANT, NOT_VERIFIED (no authoritative source reached).
REVISED 2026-11-23 (continuation): SC03 reopened; SC05 made relation-dependent; every row labelled same-model self-review. v1 kept as phase7_claim_checks_v1_2026-11-23.py.
Reference constants: CODATA 2018 / IAU / NASA values that are defined or standard (G, c, sigma, g0, Earth equatorial radius 6378.137 km, sidereal day 86164.1 s, solar mass/radius/Teff) are marked 'standard constant';
anything fetched this session is listed with its URL. Run: python3 -I scripts/phase7_claim_checks.py"""
import csv, json, math, re, os
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RS = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/what-if-scripts/'
V = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
inv = {i['id']: i for i in json.load(open(RS + 'analysis/inventory.json'))}
G, c, sig, g0 = 6.6743e-11, 299792458.0, 5.670374419e-8, 9.80665
Rearth_eq, Rearth, Dsid = 6378.137e3, 6371.0e3, 86164.0905
Msun, Rsun, Tsun, Mmoon, dMoon = 1.98847e30, 6.957e8, 5772.0, 7.346e22, 384400e3  # Moon mass 0.07346e24 kg: NASA NSSDC Moon fact sheet (fetched 2026-11-23); 384,400 km: NASA/JPL material (fetched)
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
    f'R/R0={g100:.3f}, so g={g100:.3f} g0; growth needed for exactly 6.00: {(6-1)*Rearth/1e3:.0f} km vs {0.01*100*365.25*86400/1e3:.0f} km computed ({(5*Rearth)/(0.01*100*365.25*86400)-1:+.1%}); with equatorial 6378 km: {(6378.137e3+0.01*100*365.25*86400)/6378.137e3:.3f}; with 26 km/month x1200 months: {(6371+26*1200)/6371:.2f}', 'standard; g ~ R at constant density (Newton shell theorem)', 'CONSISTENT_WITH_CAVEAT',
    'SBS "1G | 6G" with a figure lying down (t=216.5 s)', 'narration says "over 6" and the screen says 6G; recomputed 5.95 is 0.8% BELOW 6.00, so "over 6" is a rounding-up (exactly 6.00 needs 31,855 km of growth, 1.0094 cm/s, or about 100.9 years); 26 km/month x 1,200 months gives 5.9. If density changed as material was added g would differ; the video states no density assumption. The on-screen label "6G" matches the recomputation, "over 6" does not strictly')
# C2 lightning to power a house  (REOPENED 2026-11-23: see 07_SC03_LIGHTNING_REWORK.md; v1 verdict DISCREPANT withdrawn)
house_d = 899 * 12 / 365 * 3.6e6   # EIA FAQ id=97 as fetched 2026-11-23: 2022 average US residential customer 10,791 kWh/yr = 899 kWh/month; the earlier '865 kWh/month, 2024' was not reproduced on the fetched page
add('SC03', 'fs28lEq9smw', r'two days|house', "A typical lightning strike delivers enough energy to power a residential house for about two days (video context: 'the total amount of energy delivered isn't THAT extreme'; later lines: about a million bolts = about two Hiroshima bombs = US consumption for five minutes)",
    'quantity meant = energy DELIVERED by one strike (not stated whether total flash energy, ground-delivered share, or recoverable electricity); US house 899 kWh/month = 29.6 kWh/day = 106 MJ/day (EIA 2022); 1e6 bolts; Hiroshima 15 kt = 63 TJ',
    f"two days needs {2*house_d/1e6:.0f} MJ/bolt; the video's own lines imply 126 MJ (two bombs/1e6) and 132 MJ (US 5 min/1e6) = 1.2 house-days; sources (per FLASH): NatGeo/NOAA 100-30,000 MJ, typical 1,000-5,000 MJ = {1e9/house_d:.1f}-{5e9/house_d:.0f} house-days; Cooray 1997 model ~950 MJ dissipated per 4-stroke ground flash = {9.5e8/house_d:.1f} days",
    "National Geographic/NOAA (MacGorman) per-discharge energy (fetched 2026-11-23); Cooray 1997 per-flash dissipation 0.95 GJ and 0.2-7 GJ range (search summary, not read in full); EIA FAQ 97; Hiroshima 15 kt (Wikipedia/OSTI summary); EIA 2023 US sales 3,861 TWh. NO source found that gives the share delivered to ground or recoverable; What If #16 (Lightning) contains no energy figure, so the video's original source is UNKNOWN",
    'OPEN_DEFINITIONS_ORIGINAL_SOURCE_REQUIRED', 'LABEL/MAP frames of lightning (07 coding, t=36.8 s shot); schematic house-and-lightning comparison, proportions unmeasured',
    "NOT a proven error. The video's per-strike figure (about 0.13-0.2 GJ) is about 5-40x below the per-flash figures in the checked sources, but those sources estimate total flash/discharge energy, while the video says energy delivered; no checked source splits delivered vs dissipated or recoverable energy. Within the video the three statements agree to 5%. Resolving it needs the video authors' source or a paper with ground-delivered energy per stroke")
add('SC03B', 'fs28lEq9smw', r'million years', 'About two atomic bombs of energy is enough to power a game console and TV for several million years (a second line in the same video)', 'console + TV 100-500 W; two bombs = 1.26e14 J',
    f"100 W: {2*15*4.184e12/100/(365.25*86400):,.0f} yr; 300 W: {2*15*4.184e12/300/(365.25*86400):,.0f} yr; 500 W: {2*15*4.184e12/500/(365.25*86400):,.0f} yr; 3 million years needs 1.3 W",
    "arithmetic on the video's own two-bomb figure; the Catatumbo line in the same video (about a century for 1 flash/2 s x 10 h) scales by 1e6/18,000 = 56x to about 5,600 years, also not millions", 'NOT_VERIFIED',
    'text-only in the narration; frame not coded', "internal tension, not a source discrepancy: under ordinary appliance power the stated duration is 2-3 orders above the video's own energy; the original article/script may use different figures. Not counted among the 10 claims. The same SC03 wording is repeated in the Short _efsqO-4OoQ (V031, 'Could We Harvest Power From Lightning?'), so the open status applies to both videos")
# C3 key press energy
m = 1.5e-3 / (g0 * 300e-6); dT = 1.5e-3 / (0.05e-3 * 4186)
add('SC04', '0L44GEJ5pLE', r'squirrel', '1.5 mJ heats a drop of water by 1% of a degree and lifts a squirrel 300 microns', 'drop = 0.05 mL (0.05 g); c = 4.186 J/g/K; squirrel mass implied by E = m g h',
    f'implied squirrel mass {m:.2f} kg; dT for 0.05 g = {dT:.4f} K; for dT=0.01 K the drop is {1.5e-3/(0.01*4186)*1e3:.3f} g', 'standard constants (water specific heat, g0)', 'CONSISTENT_WITH_CAVEAT',
    'OBJ/LABEL: "1.5 MILLIJOULES", droplet "+0.01 C", squirrel "300 MICRONS" (shot at about t=57 s)', 'works for a 0.5 kg squirrel and a 0.036 g drop; typical drops are 0.03-0.05 mL, so "1%" is a fair rounding of 0.7%; four sheets of paper (about 0.4 mm) is a loose match for 300 microns')
# C4 magnitude 25
def E(M): return 10 ** (1.5 * M + 4.8)
Ebind_unif = 0.6 * G * Msun ** 2 / Rsun; Ebind_real = 5.7e41  # n=3 polytrope 1.5 GM^2/R from a UMD course coefficient (my own multiplication); a standard-solar-model value was not found; 6.9e41 used earlier was NOT supported by the fetched pages
add('SC05', 'e3uk7jU3RHo', r'magnitude 25', 'A magnitude 25 quake would explode the Sun', 'seismic energy E = 10^(1.5 M + 4.8) J (USGS energy-magnitude relation); Sun gravitational binding energy as the threshold',
    f'Gutenberg-Richter 10^(1.5M+4.8): E(M25)={E(25):.2e} J; USGS rough Mw relation 10^(1.44M+5.24): {10**(1.44*25+5.24):.2e} J; Sun binding: uniform sphere {Ebind_unif:.2e} J, n=3 polytrope about {Ebind_real:.1e} J; threshold magnitude (GR) {(math.log10(Ebind_real)-4.8)/1.5:.1f} to {(math.log10(Ebind_unif)-4.8)/1.5:.1f}; (USGS rough) {(math.log10(Ebind_real)-5.24)/1.44:.1f} to {(math.log10(Ebind_unif)-5.24)/1.44:.1f}',
    'Gutenberg-Richter joule form (Omni/Hawaii lecture/USGS OFR 01-0005, same relation in dyne-cm) and USGS page rough Mw relation log E = 5.24 + 1.44 Mw (fetched 2026-11-23); Sun binding energy: uniform sphere 2.3e41 J (PhysicsForums worked example), n=3 polytrope 5.7e41 J (own multiplication of a UMD coefficient); no standard-solar-model value found', 'QUALIFIED_RELATION_DEPENDENT', 'scale ladder drawn schematically (07 coding)',
    "RELATION-DEPENDENT: with the Gutenberg-Richter form M25 exceeds the Sun binding energy by about 3.5x to 9x, but with the USGS page's rough relation M25 gives about 1.7e41 J, BELOW both binding estimates, so the Sun would not be unbound. Either way the energy law is extrapolated far outside any measured range (no earthquake physics applies at those scales). The earlier threshold used 6.9e41 J, which the fetched pages did not support")
# C5 snow melt
add('SC06', 'WYf9-xfm6t8', r'335 joules', 'Melting a gram of snow takes about 335 joules', 'latent heat of fusion of ice at 0 C = 333.55 J/g', f'333.55 vs 335 J: +{(335/333.55-1)*100:.1f}%', 'CRC Handbook value 333.55 J/g (fetched via secondary tables 2026-11-23; thermochemical calorie 4.184 J)', 'CONSISTENT', 'MECH/LABEL', 'ignores warming from below 0 C, which for snow at -10 C adds about 21 J/g')
# C6 moon black hole
rs = 2 * G * Mmoon / c ** 2
add('SC07', 'UQgw50GQu1A', r'event horizon', 'A black hole with the Moon\'s mass has an event horizon about the size of a sand grain', 'Schwarzschild radius r = 2GM/c^2, Moon mass 7.342e22 kg',
    f'r_s={rs*1e3:.3f} mm, diameter {2*rs*1e3:.3f} mm (Wentworth fine sand 0.125-0.25 mm)', 'standard constants (G, c); Moon mass 7.346e22 kg NASA NSSDC (fetched); sand-size classes (Wentworth scale, not fetched)', 'CONSISTENT', 'OBJ/SCALEREF: "ELECTRON MOON" related frames; a grain-of-sand comparison', 'radius 0.11 mm or diameter 0.22 mm both fall in fine sand; "event horizon" size is a radius, so a 0.2 mm-wide sphere is the correct picture')
# C7 500 trillion calories
add('SC08', 'PUtI3xoaHx0', r'500 trillion', 'There are about 500 trillion calories of human in the world', 'about 8e9 people, mean mass 45 to 62 kg, 1,000 to 2,400 kcal per kg of body',
    f'range {8e9*45*1000/1e12:.0f} to {8e9*62*2400/1e12:.0f} trillion kcal', 'author back-of-envelope only: body energy density and mean mass were not fetched', 'NOT_VERIFIED', 'LABEL: "EARTH 500,000,000,000" with people ringing a globe (t=11.4 s)',
    'the claim is within the author\'s own range, so the order of magnitude is plausible, but no authoritative source was checked and "calories" here means kilocalories')
# C8 equatorial speed
v = 2 * math.pi * Rearth_eq / Dsid
add('SC09', 'gp5G1QG6cXc', r'thousand miles|470|1,000 miles', 'The surface moves about 1,000 mph relative to the axis; on screen "470 m/s (1040 mph)"', 'equatorial radius 6378.137 km, sidereal day 86164.09 s',
    f'v={v:.1f} m/s = {v/0.44704:.0f} mph', 'NASA NSSDC Earth Fact Sheet equatorial radius 6378.137 km (fetched); sidereal day 23.9345 h = 86164 s (Britannica/NASA archived sheet, fetched)', 'CONSISTENT_WITH_CAVEAT',
    'MAP/LABEL "470 m/s" band on the map (several Shorts)', 'the equatorial speed is 465 m/s; "470 m/s" is a rounding that does not equal 1,040 mph (470 m/s = 1,051 mph); "a thousand miles an hour" is 4% low. Speed falls with cos(latitude), which the map band shows only qualitatively')
# C9 geostationary
add('SC10', 'Z_xJ40QXu7Q', r'geostationary|tenth', 'Gravity and centrifugal effects equalise just over a tenth of the way to the Moon (geostationary height)', 'geostationary radius from Earth centre 42,164 km; Moon mean distance 384,400 km',
    f'42,164/384,400={42164/384400:.3f}', 'geostationary radius 42,164 km from Earth centre, altitude 35,786 km (fetched, Wikipedia-level source); Moon mean distance 384,400 km (NASA/JPL, fetched); the current NASA sheet lists 378,000 km at opposition, which changes only the 3rd digit', 'CONSISTENT', 'AXIS/SCALEREF (skyscraper on a distance axis)', 'distance is measured from the Earth centre; from the surface the figure is 35,786 km (9.3%)')
for r in rows: r['review_type'] = 'SAME_MODEL_SELF_REVIEW (not independent; constants fetched via web search summaries, not read in full)'
w = csv.DictWriter(open(A + '/07_SCIENCE_CLAIM_CHECKS.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r['claim_id'], r['verdict'], r['script_locator'], r['asr_time_s'], '|', r['recomputed'][:150])
