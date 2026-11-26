# 08 — Calculations and assumptions (SELF-REVIEW; no qualified reviewer)

Everything below was computed on 2026-11-24 by the scripts in `scripts/` (Python 3.14, standard library only). Outputs are saved in `scripts/output/`. A calculation that reuses an input does not verify that input; each section says which inputs are independent.

## How to reproduce
```bash
cd ~/Documents/YIOS-local-audits/2026-11-24-what-if-10-story-blueprints
python3 scripts/fetch_noaa_harcon.py          # needs network; raw NOAA JSON -> scripts/data/
python3 scripts/fall_model.py                  # -> output/fall_results.csv, fall_stdout.txt
python3 scripts/atmosphere_check.py            # circular sanity check of the density table
python3 scripts/orbit_small_world.py           # -> output/orbit_stdout.txt, orbit_small_world.csv
python3 scripts/phobos_escape.py               # -> output/phobos_stdout.txt, phobos_hill_sim.csv  (seconds)
python3 scripts/light_time_tides_isolation.py  # -> output/light_tides_isolation_stdout.txt
python3 scripts/build_tables.py && python3 scripts/build_ledger.py && python3 scripts/validate_outputs.py
```
Constants: c, au, g0 are exact definitions (SRC-34). G (CODATA 2018), Earth/Sun mass, USSA-1976 constants and the >86 km density table were **recalled from memory** (SRC-35) and are flagged in every script header; none was re-read from a document.

---
## 1. Higher fall (slots 1 and 2) — `scripts/fall_model.py`
**Model (labelled):** one-dimensional vertical fall from rest; quadratic drag `dv/dt = g(h) − ½ρ(h)·(CdA/m)·v²`; `g(h)=g0(R/(R+h))²`; windless; fixed posture; **constant** drag coefficient; no parachute; ground at sea level. Atmosphere: own implementation of the US-Standard-Atmosphere-1976 layers to 86 km plus a log-interpolated recalled table 86–120 km. RK4, dt = 0.02 s.

**Drag parameter sets (CdA/m, m²/kg) and where each comes from**
| Set | CdA/m | Terminal speed at sea level | Provenance |
|---|---|---|---|
| A | 0.00505 | 202.7 km/h | **Inherited** from an earlier project fit to Baumgartner's peak speed. Not independent of that peak |
| B | 0.005891 (Cd 0.60 × A 1.19 m² / m 121.2 kg) | 187.7 km/h | Guerster & Walter 2017, PLoS ONE (SRC-27), values read by extraction; Cd was fitted from the same flight's subsonic part |
| C | 0.006111 (0.55 m² / 90 kg) | 184.3 km/h | assumed bracket (inherited from earlier review; unsourced) |
| D | 0.007778 (0.70 m² / 90 kg) | 163.3 km/h | assumed bracket (unsourced) |
| E | 0.002599 (0.60 × 0.525 m² / 121.2 kg) | 282.6 km/h | the paper's smallest cross-section as a **bound**; stability of that posture NOT established |

**Results (km/h; peak / landing)**
| Release | A | B | C | D |
|---|---|---|---|---|
| 300 m | 187 / 186.7 | 177 / 177.1 | 175 / 174.7 | 159 / 159.0 |
| 1 km | 205 / 204.0 | 191 / 188.8 | 188 / 185.4 | 167 / 164.2 |
| 5 km | 248 / 204.3 | 231 / 189.0 | 227 / 185.5 | 203 / 164.2 |
| 10 km | 320 / 204.3 | 299 / 189.0 | 294 / 185.5 | 264 / 164.2 |
| 39 km | 1,359 / 204.3 | 1,315 / 189.0 | 1,304 / 185.5 | 1,235 / 164.2 |
| 100 km | 3,620 / 204.3 | 3,585 / 189.0 | 3,577 / 185.5 | 3,521 / 164.2 |

Other outputs (set B): peak altitude 41.3 km and time 111 s from 100 km; 28.1 km and 50 s from 39 km; total fall 4.9 min (39 km), 6.0 min (100 km); net deceleration after the peak 0.66 g (39 km) and 3.59 g (100 km), i.e. felt load 1.65 g and 4.58 g; supersonic ~33 s from 39 km; max Mach 1.22 (39 km), 3.15 (100 km). Slow-down appears (peak ≥ 1.05 × landing speed) for releases above 1.85 km (B), 1.95 km (A), 1.7 km (D).

**What this does and does not show**
- Within each set, landing speed from ≥ 3 km is identical to < 0.5 km/h, and from 1 km differs by ≈ 0.2 % — this is robust to the drag value.
- The **value** of the landing speed is not: 164–204 km/h for sets A–D (head-down bound 287). Set A's "204" is the earlier project's calibrated number and is **not independent**. Using the paper's own inputs gives 189 km/h (182–197 km/h for Cd 0.65–0.55). **Do not lock "204 km/h vs 204 km/h".**
- Peak check against Stratos (measured 377.1 m/s at 28,833 m, t = 50.0 s, SRC-27): set B gives 364.8 m/s at 28,071 m, t = 50.0 s (−3.3 %); set A gives 377.1 m/s but A was fitted to it.
- Above ~60 km results are an extrapolation: constant Cd through Mach ~3, density table recalled, no heating, continuum assumption near 100 km. LOW CONFIDENCE. Release "from rest at 100 km" is a hypothetical (zero horizontal speed; a real return from orbit is ~8 km/s sideways, SRC-08 p.189).
- `atmosphere_check.py` compares the implementation with the same recalled values: it is a **circular** check (confirms code = recalled numbers, not that the numbers are right). Exception: at 39 km the implementation gives 0.004627 kg/m³ (ρ0/ρ = 265, matching the earlier fact-check's 1/264); my "recalled ref" of 0.004 there is rough.
- Not modelled: horizontal drift, spin, wind, terrain height, heating, survival (no survival claim planned).
- Discrepancy noted: the earlier FACT_CHECK quotes 4.7 g for 100 km; this model's net deceleration is 3.7 g and felt load 4.6 g — the same number, different definition.

## 2. Tiny world orbit (slot 4) — `scripts/orbit_small_world.py`
**Model (labelled):** uniform sphere, radius R, density ρ; `g = (4/3)πGρR`; `v_c = R√(4πGρ/3)`; `v_esc = √2·v_c`; `T = √(3π/(Gρ))` (independent of R). No rotation, no air, no terrain, no other bodies. Human launch speeds are **assumptions** (≈3 m/s standing jump from a 0.45 m jump height; unsourced).
- T = 198 / 144 / 140 / 120 / 84 min for ρ = 1,000 / 1,900 / 2,000 / 2,700 / 5,514 kg/m³.
- ρ = 2,000: v_c = 3 m/s needs R = 4.01 km (g = 2.24 mm/s² = 0.023 % of Earth). Worked world R = 3,000 m: g = 1.68 mm/s², v_c = 2.243 m/s, v_esc = 3.172 m/s.
- Horizontal launch from the surface of R = 3,000 m: 0.99 v_c → periapsis 117 m below the surface (hits ground); 1.00 v_c → circular, grazing; 1.01 v_c → apoapsis +123 m, period 144 min; 1.3 v_c → +13.4 km, 811 min; ≥ 1.414 v_c → escape.
- **Clearance:** only a (near-)horizontal launch keeps periapsis ≥ R. For 1.1 v_c: 0.5° upward → periapsis −0.7 m; 2° → −10.5 m; 5° → −63 m; 10° → −228 m. A jumper's centre of mass starts ~1 m above ground, so terrain taller than ~1 m on the path blocks a "grazing" orbit.
- RK4 cross-check at 1.1 v_c: analytic period 11,966.8 s, RK4 return 11,967.0 s.
- Sub-orbital hops (45° launch, R = 3,000 m): 0.2 v_c lands after 6.5 min, 0.12 km away; 0.5 v_c: 19.8 min, 0.85 km; 0.9 v_c: 68.6 min, 3.59 km.
- Rotation: if the equatorial speed equals v_c, the spin period equals the orbit period (140 min at ρ = 2,000). No statement about real asteroid spin limits is sourced.
- Bug history: my first "max clear-orbit elevation" table printed 0° for every case because any upward velocity puts the past periapsis below ground; it was replaced by the periapsis table above. A first suborbital-arc block was wrong (horizontal launch with v < v_c is at apoapsis) and was replaced by the RK4 hop table.

## 3. Phobos (slot 5) — `scripts/phobos_escape.py`
**Sourced inputs:** mass 10.6e15 kg, semi-axes 13.0/11.4/9.1 km, a = 9,378 km, T = 0.31891 d, Mars mass 0.64169e24 kg (NASA NSSDC, SRC-16); NASA 2012 slide: v_esc 11.3 m/s (40 km/h), synchronous rotation, mass 1.072e16 kg (SRC-18). G recalled.
- Volume-equivalent radius 11.05 km; point-mass v_circ 8.00 m/s, v_esc **11.32 m/s (40.7 km/h)** — agrees with the NASA slide's 11.3 m/s (not independent of the mass; independent in method). For spheres of 9.1 / 13.0 km: 12.5 / 10.4 m/s.
- Mean surface gravity (sphere) 5.80 mm/s². The NASA slide's own gravity entry is garbled in the text layer ("86Q-190 ~g") and contradicts its mass/size, so it is **not used**.
- Mars: Phobos's orbital speed 2.138 km/s; Mars's escape speed at that radius 3.022 km/s; **extra ≈ 884 m/s** to leave Mars from Phobos's orbit. Consistency: n²a³ vs G·M_Mars within 0.14 %.
- Hill radius of Phobos w.r.t. Mars: 16.56 km = 1.50 × 11.05 km = 1.27 × the 13.0 km semi-axis. Mars's pull therefore matters at the surface.
- **Hill-equation simulation** (sphere of 9.1 / 11.05 / 13.0 km; Phobos synchronous so the surface is at rest in the rotating frame; radial launches; 30 Phobos orbits ≈ 9.6 days; "far" = beyond 6 Hill radii; "impact" = returns to the surface):
  - 3 m/s: **impact in every direction and every radius**, after 12–155 min and 0.5–3.6 km of height depending on sphere radius and direction (volume-equivalent sphere: 17–31 min, 0.75–1.25 km; the longest cases are Mars-line launches from the 13.0 km sphere, which sits close to the Hill pass).
  - Threshold launch speed for no impact: along the Mars line 4 (R = 13.0) / 5 (R = 11.05) / 7 (R = 9.1) m/s; along the orbit 9 / 10 / >10 m/s; out of the orbit plane: still falls back at 11.4 m/s in this model (the point-mass escape speed is 11.3 m/s; the Coriolis term in the rotating frame keeps a polar launch bound for longer).
  - These sub-11 m/s thresholds are **HYPOTHESIS-grade**: the body is treated as a point-mass sphere, ignoring its shape, non-uniform gravity, Mars's oblateness and the orbit's eccentricity; "far" is not escape from Mars. They must not be shown as a result without an expert shape-model run.
- Bug history: a first run hung for >7 min because impact detection required the particle to pass 1.5 R, so small jumps fell through the point mass and the adaptive step shrank to zero; it was killed, fixed (impact = back to r ≤ R with inward velocity) and rerun (seconds).

## 4. Voyager light time (slots 3 and 6), laser (slot 7), tides (slots 8 and 9), isolation (slot 10) — `scripts/light_time_tides_isolation.py`
**Voyager:** 1 light-day = 25,902,068,371 km = 173.14 au (NASA: "about 25.9 billion km"); one-way at the rounded 25.9e9 km = 23 h 59 min 53 s (rounding of the 25.9 alone is ±167 s); round trip ≈ 48 h (NASA derived value). Growth ≈ 4.9 s/day uses a **recalled** speed of 16.9 km/s — not sourced; do not use on screen. Earth's orbital motion shifts the light time by up to ±499 s (±8.3 min). Comparisons: Moon 1.28 s, Sun 499 s, Neptune ≈ 4.17 h (30.07 au recalled), Proxima ≈ 4.25 yr (4.2465 ly recalled). Ten command–reply cycles = 20 days of light time alone. The 2024 fix (45 h round trip) is SNIPPET/SECONDARY level only.
**Laser:** round trip 2.564 s at 384,400 km; 2.424 s (mean perigee 363,300 km) to 2.705 s (mean apogee 405,500 km) (NASA NSSDC mean values); extreme values 2.378–2.713 s use recalled 356,400/406,700 km and are not used on screen; surface-to-surface geometry 2.510 s. A 100 mJ pulse at 532 nm holds 2.68e17 photons (matches the ~3e17 in the Murphy snippet); at ≈1 returned photon per pulse the returned fraction is ~4e-18 (return rate itself is SNIPPET level).
**Tides:** Sun/Moon mass 2.707e7; tide-generating ratio (M_s/M_m)(d_m/d_s)³ = **0.459** (NOAA: about 1:2; Sun's direct pull on Earth 179× the Moon's vs NOAA ">177"); 0.388 at mean lunar perigee, 0.539 at mean apogee. Bookkeeping in equilibrium-theory units: springs 1 + 0.46, neaps 1 − 0.46, Sun alone 0.46 → Sun alone ≈ 31 % of a spring forcing. These are **forcing ratios, not local heights**. Real station data (NOAA CO-OPS, 8 stations, fetched 2026-11-24): S2/M2 amplitude ratio 0.151 (Boston), 0.191 (Battery NY), 0.222 (Charlotte Amalie), 0.238 (San Francisco), 0.252 (Seattle), 0.279 (Anchorage), 0.328 (Honolulu), 0.536 (Grand Isle); median 0.245; S2/(M2+S2) 13–35 %. S2 is only one of several solar constituents, so using S2 alone is a **lower bound** and basins can respond differently to the new forcing. Tide periods from NOAA constants: M2 28.984°/h = 12.42 h; S2 30.0°/h = 12.00 h. Barycentre 4,671 km from Earth's centre (inside Earth, radius 6,371 km). Light delay of the Moon's removal 1.28 s (gravity speed = c is recalled, not read).
**Isolation:** 2R + h with R = 1,737.4 km: h = 110.2 km → 3,585.0 km (Munroe); 120.8 km → 3,595.6 km (Wikipedia aposelene, snippet); 123.5 km → 3,598.3 km (Flight Journal snippet); the altitude implied by Guinness's 3,596.4 km is 121.6 km. So Guinness and Munroe differ by ≈ 11.6 km purely from the assumed orbit altitude, and both assume a lander exactly opposite the command module at its highest point (an upper-bound geometry, not a measurement). Artemis II: 252,756 mi = 406,771 km (maximum was "expected" in NASA's release); Guinness separation 419,656 km (pair of crews). Munroe's footnote converting 3,585 km to 3,619 km "across the surface" gave 3,634 km in my chord→arc check (R = 6,371 km); the difference is unexplained and unused.

## Items NOT calculated
Survival or injury; air heating/temperatures; real-Phobos shape-model trajectory; ocean-basin response and decay time after the Moon's removal; obliquity evolution; Voyager's actual reply; link budget; neutron-star matter (on hold).
