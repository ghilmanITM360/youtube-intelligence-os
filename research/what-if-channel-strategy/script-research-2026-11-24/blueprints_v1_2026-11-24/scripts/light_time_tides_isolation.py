"""SHORT 2 / LONG 3 (Voyager light time), SHORT 4 (lunar laser), LONG 4 / SHORT 5 (Moon & tides), SHORT 6 (isolation geometry).
Stdlib only. Run: python3 scripts/light_time_tides_isolation.py  (reads scripts/data/noaa_harcon_summary.csv from fetch_noaa_harcon.py)
Constants: c=299792.458 km/s (exact, SI); AU=149597870.7 km (exact, IAU 2012); G=6.67430e-11 (CODATA 2018, recalled);
Moon mass/radius/perigee/apogee/semimajor axis from NASA NSSDC Moon fact sheet (read 2026-11-24): 0.07346e24 kg, 1737.4 km, 0.3633e6, 0.4055e6, 0.3844e6 km (MEAN perigee/apogee).
Sun mass 1.98847e30 kg and Earth mass 5.9722e24 kg, Earth radius 6371.0 km (mean) / 6378.137 km (eq): recalled, NOT re-sourced in this session.
"""
import math, csv, os, statistics
c=299792.458; AU=149597870.7; HERE=os.path.dirname(os.path.abspath(__file__))
def hms(s): return f"{int(s//3600)} h {int(s%3600//60)} min {s%60:04.1f} s"
print("== VOYAGER 1 (SHORT 2 / LONG 3)")
lightday=c*86400; print(f"1 light-day = c x 86,400 s = {lightday:,.0f} km = {lightday/AU:.2f} AU   (NASA: 'about 25.9 billion km')")
d0=25.9e9; print(f"one-way time at NASA's rounded 25.9e9 km: {d0/c:,.0f} s = {hms(d0/c)}  -> rounding of 25.9 changes it by up to +-{0.05e9/c:.0f} s")
v=16.9  # km/s  RECALLED (~17 km/s); NOT re-sourced
print(f"If Voyager recedes at ~{v} km/s (RECALLED, unsourced), one-way time grows {v*86400/c:.2f} s per day -> {(v*86400/c)*6:.0f} s after 6 days (24 Nov vs 18 Nov)")
print(f"Earth's own orbit changes the Earth-Voyager distance by up to +-1 AU over a year = +-{AU/c:.0f} s = +-{AU/c/60:.1f} min of one-way light time (geometry; approximate)")
rt=2*d0/c; print(f"round trip ~ 2 x one-way = {rt/3600:.2f} h (NASA: 'about 48 hours'); doesn't include onboard processing, antenna scheduling, or analysis time")
print("Light-travel times for comparison: Moon 384,400 km: %.2f s | Sun 1 AU: %.0f s (%.1f min) | Neptune ~30.07 AU (recalled): %.2f h | Voyager 1: 24 h | Proxima 4.2465 ly (recalled): %.2f yr"%(384400/c,AU/c,AU/c/60,30.07*AU/c/3600,4.2465))
print("Conversation arithmetic: 1 question+answer = 48 h; 5 exchanges = 10 days; 10 exchanges = 20 days (if every step were a one-sentence command and reply, no delays)")
print("Real precedent (NASA/JPL via news, snippet-level): April 2024 fix: ~22.5 h each way = ~45 h round trip; command 18 Apr, confirmation 20 Apr. Source quality: SECONDARY (news citing JPL); primary page not opened.")
print("\n== LUNAR LASER (SHORT 4)")
for lab,d in (("mean (semi-major axis)",384400.),("NSSDC mean perigee",363300.),("NSSDC mean apogee",405500.),("recalled extreme perigee 356,400",356400.),("recalled extreme apogee 406,700",406700.)):
    print(f"  {lab:34s} d={d:9,.0f} km  one-way {d/c:.4f} s  round trip {2*d/c:.4f} s")
RE=6378.137; RM=1737.4
print(f"  station-to-reflector (surface-to-surface, sub-Earth/sub-Moon geometry only) at mean: d-RE-RM = {384400-RE-RM:,.0f} km -> round trip {2*(384400-RE-RM)/c:.4f} s  (center-to-center is a MODEL; station geometry matters)")
print(f"  Moon moves ~1 km/s relative to Earth: in 2.56 s that is ~2.6 km = {2.6/c*1e6:.0f} us of light time (small, but ranging uses it)")
h=6.62607015e-34; cc=299792458.0; lam=532e-9; E=h*cc/lam; Np=0.100/E
print(f"  photon energy at 532 nm = {E:.3e} J ; 100 mJ pulse holds {Np:.2e} photons (Murphy review: ~3e17 -> consistent; his divergence loss factor ~1e16 [snippet level])")
print(f"  If ~1 photon returns per pulse (APOLLO-type best case: up to 0.6/pulse in short periods, snippet level), fraction returned ~ {1/Np:.1e}")
print("\n== TIDES (LONG 4 / SHORT 5)")
Ms=1.98847e30; Mm=7.346e22; Me=5.9722e24; dm=384400e3; ds=AU*1e3
ratio=(Ms/Mm)*(dm/ds)**3
print(f"  Sun/Moon mass = {Ms/Mm:.3e} ; (d_moon/d_sun)^3 = {(dm/ds)**3:.3e} ; tide-generating ratio Sun/Moon = {ratio:.3f} (NOAA page: about 1:2; Sun's direct pull on Earth {Ms/Mm*(dm/ds)**2:.0f}x the Moon's)")
for lab,d in (("lunar mean perigee",363300e3),("lunar mean apogee",405500e3)):
    print(f"  with {lab}: ratio = {(Ms/Mm)*(d/ds)**3:.3f}")
print(f"  equilibrium-theory crude bookkeeping: springs ~ (1+{ratio:.2f}) = {1+ratio:.2f}, neaps ~ (1-{ratio:.2f}) = {1-ratio:.2f}, Sun alone = {ratio:.2f}  -> Sun-alone / spring = {ratio/(1+ratio):.2f}; Sun-alone / neap = {ratio/(1-ratio):.2f}  [forcing ratios, NOT local heights]")
print(f"  Earth-Moon barycentre from Earth's centre = {dm/1000*Mm/(Me+Mm):,.0f} km (Earth radius 6,371 km => inside Earth)")
print(f"  lunar day 24 h 50.5 min -> tide ~ 12 h 25.2 min (M2 period ~12.42 h) vs solar tide 12.00 h: lunar high tide slips ~50 min/day; without the Moon only the 12.00 h solar rhythm of S2 stays")
print(f"  gravity-change and light delay from the Moon's distance: {dm/1000/c:.2f} s (if gravity changes propagate at c: constraint from GW170817 is RECALLED, not read)")
rows=list(csv.DictReader(open(os.path.join(HERE,"data","noaa_harcon_summary.csv"))))
r=[float(x["S2_over_M2"]) for x in rows if x["S2_over_M2"]]
print("  NOAA CO-OPS harmonic constituents (fetched 2026-11-24), S2/M2 amplitude ratio at 8 US stations:")
for x in rows: print(f"     {x['name']:34s} M2={x['M2_amp']:>7} ft  S2={x['S2_amp']:>6} ft  S2/M2={x['S2_over_M2']}  S2/(M2+S2)={float(x['S2_amp'])/(float(x['M2_amp'])+float(x['S2_amp'])):.2f}")
print(f"     range {min(r):.3f}-{max(r):.3f}, median {statistics.median(r):.3f}  vs equilibrium 0.46 -> NO single percentage; S2 alone is a LOWER bound for solar tide (P1, K1 part, T2, R2, K2 part also solar)")
print("\n== ISOLATION GEOMETRY (SHORT 6)")
RM=1737.4
for lab,alt in (("Munroe book-implied ~110 km",110.2),("Apollo 15 aposelene Wikipedia 120.8 km",120.8),("Apollo Flight Journal apocynthion 66.7 nmi",66.7*1.852),("altitude implied by Guinness 3,596.4 km",3596.4-2*RM)):
    print(f"  CM at altitude {alt:6.1f} km directly opposite a lander on the surface: distance = 2R+h = {2*RM+alt:7.1f} km  ({lab})")
print(f"  Munroe footnote (surface arc on Earth case): 3,585 km straight line ~ 3,619 km along surface (R_E=6371: chord->arc {2*6371*math.asin(3585/(2*6371)):.0f} km)")
print(f"  Artemis II: 252,756 mi x 1.609344 = {252756*1.609344:,.0f} km from Earth (NASA release / Guinness text); Guinness 'farthest separation between humans' 419,656 km (pair of crews) - a DIFFERENT quantity")
print(f"  Isolation definition test: Artemis II crew of 4 stayed together -> nearest other human is 0 m away -> isolation record unchanged by distance-from-Earth records")
