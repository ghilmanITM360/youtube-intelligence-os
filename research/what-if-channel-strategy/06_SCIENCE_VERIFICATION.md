# 06 — Science verification: all 23 calendar items (2026-11-18)

**Scope:**
- 9 fixed longs
- 4 standalone Shorts
- 9 excerpt Shorts, each checked for its own angle
- headline check of the 4 Day-29 default topics

**What this pass is for:** a pre-script gate (05 §3.1). It decides whether each premise and number holds up. It does not replace the per-claim check that each script still needs once it exists.

**Recomputation:** `scripts/verify_science.py` reruns every derived number below from the cited constants (run time about 6 s).

**Status labels:**
- **VERIFIED:** matches a primary or official source.
- **COMPUTED:** our own calculation from sourced constants; the model limits are stated.
- **CORRECTED:** the calendar value was wrong and is fixed in 05.
- **REFRAME:** the premise or wording would mislead and is changed in 05.
- **OPEN:** needs a source before scripting.

**Source quality:**
- Primary or official: JPL, NASA NSSDC, FAI, Guinness, peer-reviewed papers.
- The model check for falls is a calibration. The 1-D drop model with US Standard Atmosphere 1976 reproduces Baumgartner's FAI speed record (1,357.6 km/h → model 1,358 km/h, Mach 1.26) with one fitted drag value. Every other fall number uses that same calibration.

## Summary

| Day | Item | Verdict | Change |
|---|---|---|---|
| 1 | WIB-36 Free fall (L) | VERIFIED + COMPUTED; title REFRAME | "to Orbit" → "to the Edge of Space": a drop from orbital height is not orbit |
| 2 | Excerpt: "the one altitude where falling gets slower" | REFRAME | Not one altitude. Every jump from above ~10 km peaks, then slows |
| 3 | WIB-55 Neutron bullet (S) | COMPUTED | "Billions of tonnes" holds (1.3–4.9 billion t). Use "≈ 1 km³ of rock", not "mountain-sized" |
| 4 | Excerpt: dropping the bullet | REFRAME | Only works with a stated "held together" assumption; real outcome is decompression ≈ 10¹¹ Mt |
| 5 | NEW-06 Moon vanishes (T) | VERIFIED; title REFRAME | "Hour by Hour" overpromises: little changes hourly. → "Night One to a Million Years" |
| 6 | T-01 Apophis 2029 | VERIFIED; title changed | Title → "What Will Apophis Look Like on 13 April 2029?" (real future event, so "What will" is accurate). 31,640 km above the surface (JPL CAD), 13 Apr 2029 21:46 UTC, no impact risk for ≥100 yr |
| 8 | WIB-22 Alien astronomers (L) | VERIFIED + COMPUTED | None |
| 9 | Excerpt: tides on night one | VERIFIED | None; state that solar tides remain at about 46% |
| 10 | Excerpt: what aliens see right now | VERIFIED | None |
| 11 | NEW-08 Light at 100 km/h (R) | COMPUTED; prior-art note | Must state the "only light slows" simplification; prior art: Gamow's *Mr Tompkins* (1940), MIT Game Lab's *A Slower Speed of Light* (2012) |
| 13 | WIB-18 Steak drop | COMPUTED (estimate, labelled) | Honest answer: **no height cooks it**. Thumbnail → "100 km: a seared crust, seconds long" (no temperature) |
| 15 | WIB-17 Little planet (S) | COMPUTED | "ORBIT: 1 JUMP" holds: radius 2.3–4.5 km |
| 16 | Excerpt: "a traffic jam of light" | **REFRAME (false premise)** | Light cannot jam. → "Why your headlights still outrun you" |
| 18 | WIB-11 Last human light (T) | VERIFIED (sourced rungs) + REWORDED (power plants) | Power-plant rungs are qualitative only; Cherenkov glow dropped; hydro has no number |
| 19 | Excerpt: why you can't walk there | VERIFIED + COMPUTED | None ("a few cm/s": walk-run switch ~3–4, hard ceiling ~4–6 cm/s) |
| 20 | WIB-53 Storm as one drop | COMPUTED | State the assumptions on screen (cell size, rain depth, drop height) |
| 22 | WIB-24 Plane on every planet (L) | VERIFIED + COMPUTED; **thumbnail CORRECTED** | "MARS: 0 LIFT?" is wrong → "MARS: 530 km/h JUST TO STAY UP" |
| 23 | Excerpt: light that lasts longest | Unblocked | Use only the sourced rungs |
| 25 | WIB-52 Loneliest human (Q) | VERIFIED; **thumbnail CORRECTED** | "3,500 km" → "3,596 km" (Guinness) |
| 26 | Excerpt: flying on Titan | VERIFIED + COMPUTED | None |
| 27 | NEW-07 Fall into Jupiter | VERIFIED | Stapp 46.2 g sourced (museum and magazine, not a USAF report) |
| 28 | Excerpt: "farther than the Moon?" | **REFRAME** | Worden was not farther than the Moon. → "Farthest from Earth ≠ loneliest" (Artemis II contrast) |
| 29 | 4 defaults | Headline-checked | NEW-05 must define *what* doubles; WIB-04 must state its reference frame |

**Bottom line:** no topic has to be dropped. The pass made these changes in 05:
- 2 thumbnails corrected (Days 22 and 25)
- 6 titles or angles reframed (Days 1, 2, 4, 5, 16, 28)
- 2 thumbnail labels sharpened (Days 3 and 13)

**Open items closed 2026-11-18** (owner request). Honest tally: 3 closed with sources (Stapp, Ingenuity, Gamow), 1 closed by dropping the claim (Cherenkov glow), 3 closed by rewording to qualitative or ranged claims (fossil, hydro, nuclear), 1 closed by labelling (Day 13 heating). Nothing below was reviewed by a domain expert. Several sources are search-confirmed, not fetched in full.

---

## Day 1 / Day 2 — WIB-36 Free fall (L ladder)

| Claim | Value | Source | Status |
|---|---|---|---|
| Fastest human freefall | 1,357.6 km/h (Mach 1.25), exit 38,969 m, 14 Oct 2012, Baumgartner, still standing | FAI: https://fai.org/node/193240 | VERIFIED |
| Highest exit altitude | 41,422 m, Eustace, 24 Oct 2014, with drogue | FAI via https://fai.org/node/155244; Guinness: https://www.guinnessworldrecords.com/news/2014/10/has-googles-alan-eustace-beaten-felix-baumgartners-skydive-record-61357 | VERIFIED |
| Sea-level belly-to-earth terminal speed | ~55 m/s (~200 km/h); the calibrated drag gives 205 km/h from 1 km | model (calibrated) | COMPUTED |
| Peak speed by drop height | 10 km → 320 km/h (peaks at 8.6 km); 20 km → 583; 30 km → 967; 39 km → 1,358 (peaks at 27.5 km); 60 km → 2,256 (Mach 2.05); 100 km → 3,620 (Mach 3.2, 4.7 g); 400 km dropped *standing still* → 8,947 km/h (Mach 8.7, 20 g, ~33 W/cm² stagnation heating) | `verify_science.py` | COMPUTED (±15%: body attitude, suit, 1-D) |
| "Orbit" | Orbit means moving sideways at ~7.66 km/s, not falling from a height. A 400 km drop with no sideways speed is a hard but different fall. Real re-entry from orbit is far worse | physics | **REFRAME** title |

**Thumbnail "39 km":** accurate as "the fastest-ever fall started at 39 km". Label it as a speed record, not a height record, because Eustace went higher.

**Excerpt (Day 2):** the slowdown is not a single altitude. From any start above ~10 km you reach peak speed high up, then slow down as the air thickens. → Reframed to "Why jumping from higher makes you slow down before landing".

## Day 3 / Day 4 — WIB-55 Neutron bullet (S scale)

| Claim | Value | Source | Status |
|---|---|---|---|
| Neutron-star density | Nuclear saturation 2.7×10¹⁷ kg/m³ (n₀ = 0.16 fm⁻³). Mean for 1.4 M☉ at R = 11–13 km is 3.0–5.0×10¹⁷. Core up to ~10¹⁸ | Lattimer & Prakash, *Phys. Rep.* 621:127–164 (2016), https://arxiv.org/abs/1512.07820 | VERIFIED (range; the 16 MeV/neutron energy is our order-of-magnitude reading of its pure-neutron-matter section) |
| Teaspoon (4.93 mL) mass | 1.3–4.9 billion tonnes ≈ 0.5–1.8 km³ of rock | computed | COMPUTED: thumbnail "billions of tonnes" holds; "mountain-sized" → "≈ 1 km³ of rock" |
| 9 mm bullet volume (8 g lead) of NS matter | 1.9–7.1×10¹¹ kg; its own gravity at 1 m = 13–47 m/s² (stronger than Earth's) | computed | COMPUTED |
| What actually happens | No gravity holds it, so it decompresses explosively. ~16 MeV per neutron (pure-neutron-matter energy near saturation) → ~3×10²⁶–1×10²⁷ J ≈ 10¹¹ Mt TNT, plus ~10²⁵ J from neutron β-decay (0.782 MeV) | Lattimer & Prakash 2016 (equation-of-state energetics); order-of-magnitude | COMPUTED (order of magnitude only) |

**Excerpt (Day 4):** "dropping it on the floor" only exists with an on-screen assumption ("suppose something magically holds it together"). With that, it sinks through the floor like a stone through water. → REFRAME: say the assumption out loud and label the segment SIMULATION.

## Day 5 / Day 9 — NEW-06 Moon vanishes (T timeline)

| Claim | Value | Source | Status |
|---|---|---|---|
| Sun's tide force vs the Moon's | 0.459 (computed from NSSDC masses and distances). NOAA: "about half" | NOAA: https://oceanservice.noaa.gov/education/tutorial_tides/tides02_cause.html; NSSDC fact sheet | VERIFIED |
| Tides after the Moon goes | Solar-only range ≈ 31% of today's spring range, 85% of neap (equilibrium-tide simplification; real ocean response is dynamic) | computed | COMPUTED + caveat |
| Earth's orbit | The barycentre is 4,671 km from Earth's centre (inside Earth). Earth stops a 12.4 m/s wobble; no dramatic orbital change | computed | COMPUTED |
| Axial tilt | Laskar et al. 1993 (*Nature* 361:615) predicted chaotic tilt without the Moon. Lissauer, Barnes & Chambers 2012 (*Icarus* 217:77) find larger variation, but bounded to a ~20–25° range over hundreds of millions of years | papers | VERIFIED; present as **contested**, and as a timescale of **100,000+ years** |

**Title "Hour by Hour" (REFRAME):** effects over the first hours are small: a dark sky and a next high tide about two-thirds lower than a spring tide. The big effects take 10⁵–10⁸ years. An hourly promise would fail FR-TITLE-03. → "What If the Moon Vanished Tonight? Night One to a Million Years" (still a T timeline).

**Excerpt (Day 9):** "tides on night one" is accurate as reframed above.

## Day 6 — T-01 Apophis 2029 (standalone)

| Claim | Value | Source | Status |
|---|---|---|---|
| Date and time | 2029-04-13 21:46 UTC (±<1 min) | JPL SBDB close-approach API: https://ssd-api.jpl.nasa.gov/cad.api?des=99942&date-min=2029-01-01&date-max=2029-12-31&dist-max=0.01 | VERIFIED |
| Distance | 0.000254091 au = 38,011 km from Earth's centre = **31,640 km above the surface**. Lower than geostationary satellites (35,786 km); the Moon is 10× farther | JPL CAD (computed from it) | VERIFIED. NASA's page gives both 32,000 and 36,000 km; use JPL |
| Size | Mean diameter 340 m, long axis ≥ 450 m | NASA: https://science.nasa.gov/solar-system/asteroids/apophis-facts/ | VERIFIED |
| Relative speed | 7.42 km/s | JPL CAD | VERIFIED |
| Risk | No impact risk for at least 100 years | NASA facts page | VERIFIED |
| Visibility | Naked eye from the Eastern Hemisphere | NASA facts page | VERIFIED |

**Date note:** 21:46 UTC is already 14 April in time zones east of UTC+2:14. Put "UTC" on screen. Do not reuse Tracer's city-and-date card style (04 §2).

## Day 8 / Day 10 — WIB-22 Alien astronomers (L ladder)

| Claim | Value | Source | Status |
|---|---|---|---|
| What each distance sees | Light from 10 ly away shows 2016; 100 ly → 1926; 10,000 ly → ~8000 BCE (early Holocene farming) | computed | COMPUTED |
| Resolving Earth | Making Earth even one resolved pixel at 550 nm needs a 5 km telescope at 10 ly, 50 km at 100 ly and ~5,000 km at 10,000 ly | Rayleigh criterion, computed | COMPUTED: no one sees continents or cities |
| Transit signal | Earth dims the Sun by 84 ppm | computed | COMPUTED |
| Who can see Earth transit | 1,715 stars in the last 5,000 years (+319 in the next 5,000); our radio has reached 75 of them | Kaltenegger & Faherty, *Nature* 594:505 (2021) | VERIFIED |
| Radio leakage | Mobile-tower leakage could **not** currently be detected within 10 ly with Green-Bank-class sensitivity | Saide, Garrett & Heeralall-Issur, *MNRAS* 522:2393 (2023), https://arxiv.org/abs/2304.13779 | VERIFIED; kills the "radio bubble = they hear us" myth |

**Excerpt (Day 10):** Proxima Centauri (4.25 ly) sees Earth as of 2022, and cannot hear our phones.

## Day 11 / Day 16 — NEW-08 Light at 100 km/h (R runaway)

| Claim | Value | Status |
|---|---|---|
| Time dilation (γ) | walking 5 km/h → 1.001; cycling 25 → 1.033; car 50 → 1.155; 90 → 2.29; 99 km/h → 7.1 | COMPUTED (special relativity) |
| Colour shift approaching (Doppler) | ×1.29 at 25 km/h; ×1.73 at 50; ×4.4 at 90 | COMPUTED |
| Delays | You see someone 100 m away 3.6 s late; moonlight takes 160 days; sunlight takes 171 years | COMPUTED |
| Consistency | The fine-structure constant scales with 1/c, giving α ≈ 8×10⁴ instead of 1/137, so atoms could not exist | COMPUTED: **must be stated on screen** as "only light's travel speed changes" |
| Prior art | Gamow, *Mr Tompkins in Wonderland* (1940): slow c with a cyclist. MIT Game Lab, *A Slower Speed of Light* (2012). Also the competitor WhatIfAnimations (03) | Collision note: credit Gamow by name, and use a different angle (cars and traffic) |

**Excerpt (Day 16) "traffic jam of light" is a false premise:**
- Photons do not block each other.
- Light leaves every car at c in that car's own frame.

→ REFRAME: "Why your headlights still outrun you, even at 99 km/h". That is correct relativity and counter-intuitive.

## Day 13 — WIB-18 Steak drop (standalone, L)

Model: 0.3 kg steak, 0.02 m² face, Cd 1.1, dropped from rest. Heating uses Sutton-Graves with a 7 cm nose radius, which is crude below Mach ~5.

| Drop | Peak speed | Peak Mach | Peak stagnation temp | Heat load |
|---|---|---|---|---|
| 39 km (Baumgartner height) | 180 m/s | 0.58 | subsonic, no heating | ~3 J/cm² |
| 70 km | 514 m/s | 1.56 | ~129 °C, for seconds | ~16 J/cm² |
| 100 km | 819 m/s | 2.6 | ~316 °C, for seconds | ~35 J/cm² |
| 400 km (from rest) | 2.4 km/s | 8.7 | ~2,800 °C, brief | ~240 J/cm² |

**Benchmark:** warming the outer 1 cm of steak by 40 K needs ~150 J/cm².

**Conclusion (COMPUTED, order of magnitude):**
- Below ~60 km the steak never goes supersonic.
- From 100 km it gets only a seconds-long sear.
- From 400 km the surface chars and ablates while the inside stays raw.
- It then falls for minutes through −56 °C stratosphere air and lands at ~25 m/s.

→ The title question's honest answer is **"no height cooks it"**. Thumbnail: see the decision below (no temperature shown).

**RESOLVED by labelling (decision, 2026-11-18):** no reviewer is available, so the script shows only "order of magnitude" figures, rounded to one significant figure, with the label "ESTIMATE" on screen. The headline "no height cooks it" rests on the Baumgartner-validated fall speeds plus a seconds-long heating window, not on the exact temperature. Thumbnail number "316 °C" is replaced by "100 km: a seared crust, seconds long" unless a reviewer later confirms it.

## Day 15 / Day 19 — WIB-17 Little planet (S scale)

| Claim | Value | Source | Status |
|---|---|---|---|
| Human jump take-off speed | 2.8–3.4 m/s (from a 0.4–0.6 m vertical jump) | computed | COMPUTED |
| Radius where a jump = orbit | Rock (5,514 kg/m³): 2.3–2.7 km. Rubble (2,000 kg/m³): 3.7–4.5 km | computed | COMPUTED: "ORBIT: 1 JUMP" holds |
| Orbit time | 84 min (dense) to 140 min (rubble), independent of size | computed | COMPUTED |
| Escape speed | 1.41× the jump speed. A slightly harder jump leaves for good | computed | COMPUTED |
| Real comparison | Deimos: escape speed ≈ 5.6 m/s (M ≈ 1.476×10¹⁵ kg, mean radius 6.2 km), so you cannot jump off it with ~3 m/s. The NSSDC Mars sheet still lists an older 2.4×10¹⁵ kg; do not use it | current mass search-confirmed from JPL-derived listings; NASA's own Deimos page not fetched | VERIFIED (5.6 m/s) |
| Walking (Day 19) | People switch from walking to running near Froude 0.5, and that holds in reduced gravity. The pendulum limit for any walk is Froude 1 (v = √(gL)). With g ≈ 2–4 mm/s² and a 0.9 m leg: a preferred walk-run switch at ~3–4 cm/s, and a hard ceiling of ~4–6 cm/s | Kram, Domingo & Ferris, *J. Exp. Biol.* 200:821–826 (1997), https://pubmed.ncbi.nlm.nih.gov/9076966/ . Caveat: at simulated 0.1–0.2 g the transition Froude rose above 0.5 | VERIFIED (source) + COMPUTED. Say "a few centimetres per second" |

**Caveat to state:** an orbit at head height only works over perfectly smooth ground. Any hill is in the way.

## Day 18 / Day 23 — WIB-11 Last human light (T timeline; the single remake)

| Claim | Value | Source | Status |
|---|---|---|---|
| Tritium exit signs | Half-life 12.32 ± 0.02 yr (4,500 ± 8 d) → 50% brightness after 12 yr, 24% after 25, 6% after 50 (decay only) | NIST, Lucas & Unterweger 2000: https://pmc.ncbi.nlm.nih.gov/articles/PMC4877155 | VERIFIED + COMPUTED |
| Promethium-147 dials | 2.62 yr → 7% after 10 yr | DOE Isotope Program sheet citing NNDC: https://isotopes.gov/sites/default/files/2025-10/Promethium-147%20Product%20Information.pdf | VERIFIED + COMPUTED |
| Radium dials | Radium lasts 1,600 yr, but the zinc-sulfide phosphor is wrecked by the radiation in years to decades, so the dial goes dark while still radioactive | ORAU Health Physics Museum: https://orau.org/health-physics-museum/collection/radioluminescent/index.html | VERIFIED: a strong counter-intuitive beat |
| Solar panels | Median degradation 0.5%/yr → ~78% output after 50 yr. Batteries and dirt fail first (uncertain) | Jordan & Kurtz, *Prog. Photovolt.* 21:12–29 (2013), ~2,000 measured rates: https://research-hub.nrel.gov/en/publications/photovoltaic-degradation-rates-an-analytical-review-2/ | VERIFIED (panel only) |
| Nuclear reactors on grid loss | Reactors scram automatically on loss of offsite power; emergency diesels then carry decay-heat removal. Station blackout (both fail) is the core-damage path | NRC: https://www.nrc.gov/reading-rm/doc-collections/nuregs/contract/cr6890/ ; NRC SBO history https://www.nrc.gov/sr0933/Section%202.%20Task%20Action%20Plan%20Items/a44r1.html (search-confirmed, not fully fetched) | CLOSED as a qualitative claim. Reactors do not keep lights on; they shut down |
| Spent-fuel pool, loss of cooling | At design heat load: >2 days to boiling, then ≥2 more days for the level to fall to the top of the fuel. Some plants/older fuel loads: hours to heat up. Source docs are 1996–2006 | NRC: https://www.nrc.gov/docs/ML1209/ML120970086.pdf and the NRC generic issue 82 page (search-confirmed, not fully fetched) | CLOSED as a range: "days to weeks". Do NOT script a years-long Cherenkov glow; see next row |
| Spent-fuel Cherenkov glow lifetime | No source found. A 1979 Los Alamos report says the glow is brightest on freshly exposed assemblies and fades with cooling time (INMM: https://resources.inmm.org/node/37451) | search result only | **DROPPED as a "last light" candidate.** The pool water boils off or drains within weeks once pumps stop, so the glow ends then regardless of fading. Mention only as "ends when the water does" |
| Grid fossil plants | No clean primary source for "hours to days". Reliable framing: plants need continuous fuel delivery and operators; automatic trips on grid loss | none | **REWORDED:** say "hours to days, our estimate, no source", or leave out of the on-screen timeline. Not a numeric claim |
| Unattended hydro | Hydro suits unmanned operation (ABB: https://library.e.abb.com/public/9c254798f2af4801a587a5721025c306/2020_HPP_Intelligent_Solutions.pdf) but needs a grid to follow and gates and trash-racks clear. Run-of-river plants often run manual because of level-control unreliability (MDPI: https://mdpi.com/1996-1073/10/11/1717/htm). No source gives a "months to years" figure | search-confirmed | **REWORDED:** no number. Say "the longest candidate, because water keeps coming; how long is not known". A dated claim needs an engineer, not a search |

**Day 18 decision:** the timeline's solid, sourced rungs are radioisotope and solar lights (rows above). Power-plant rungs are qualitative only. The title is already "which light goes out last", not "hour by hour", so the claim stays honest: it names a ranking with ranges, not exact times.

**Day 23 excerpt:** unblocked, with the same rule. Use only the sourced rungs (tritium, Pm-147, radium dial, solar) plus the qualitative hydro line.

## Day 20 — WIB-53 Storm as one raindrop (standalone, Q)

| Scenario (stated assumption) | Water | Single-drop diameter | Max impact speed (no drag) | Energy |
|---|---|---|---|---|
| Small cell: 5 km wide, 10 mm rain | 0.2 Mt | 72 m | 198 m/s from 2 km | 0.9 kt TNT (2.3 kt from 5 km) |
| Typical thunderstorm: 10 km, 25 mm | 2.0 Mt | 155 m | 198–313 m/s | 9–23 kt |
| Big storm: 20 km, 50 mm | 15.7 Mt | 311 m | 198–313 m/s | 74–184 kt |

**Reality check:** real drops break up above ~6 mm (Villermaux & Bossa, *Nature Physics* 5:697, 2009; the mechanism is disputed in a later *Nature Physics* comment, but the ~6 mm ceiling is not). A 155 m drop would shatter on the way down.

**Status:** COMPUTED. The on-screen numbers must show which scenario is used.

## Day 22 / Day 26 — WIB-24 Plane on every planet (L ladder)

Model: Cessna 172S stall speed, 53 KCAS flaps up at 2,550 lb (POH: https://www.befa.org/wp-content/uploads/2019/12/POH-Cessna-172S.pdf), scaled as v ∝ √(g/ρ).

| Body | Surface density | Gravity | C172 stall speed | Source |
|---|---|---|---|---|
| Earth | 1.225 kg/m³ | 9.81 | 98 km/h | POH |
| Venus surface | ~65 kg/m³ (92 bar, 464 °C) | 8.87 | 13 km/h, but the plane melts | NSSDC: https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html |
| Mars | ~0.016 ± 0.006 kg/m³ | 3.73 | **~530 km/h (Mach 0.6)**; range ~430–700 km/h given the density uncertainty | NSSDC: https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html |
| Titan | 5.3 kg/m³ (derived from the Huygens 1,467 hPa / 93.65 K reading) | 1.35 | 18 km/h | Fulchignoni et al., *Nature* 438:785 (2005) |

**Thumbnail "MARS: 0 LIFT?" (CORRECTED):**
- Lift is not zero. The plane needs ~530 km/h just to stay up.
- The piston engine also has no oxygen (95% CO₂).

→ "MARS: 530 km/h JUST TO STAY UP".

**Real-world anchor:** NASA's Ingenuity helicopter did fly on Mars, with rotors spinning very fast. **CLOSED (minor):** Ingenuity made 72 flights; the last was 18 Jan 2024 and NASA ended the mission on 25 Jan 2024 (rotor damage). Search-confirmed via NBC News (https://www.nbcnews.com/science/space/nasas-little-helicopter-mars-logged-last-flight-rcna135757); swap in the NASA page URL when scripting.

**Excerpt (Day 26):** Titan stall at 18 km/h is correct. Human-powered flight there is plausible, but the popular "flap your arms" claims come from student papers. Say "plausible", not "easy".

## Day 25 / Day 28 — WIB-52 Loneliest human (Q)

| Claim | Value | Source | Status |
|---|---|---|---|
| Most isolated human | Alfred Worden, Apollo 15 (1971): **3,596.4 km** from the nearest humans | Guinness: https://www.guinnessworldrecords.com/world-records/66111-most-isolated-human-being | VERIFIED: thumbnail **CORRECTED** from 3,500 |
| Geometry check | Lunar radius 1,737.4 km; CSM orbit ~110–120 km; surface crew on the far side → max 3,585–3,595 km | computed | COMPUTED: agrees with Guinness |
| Farthest from Earth | Artemis II, 6 Apr 2026: 252,756 mi = 406,771 km, beating Apollo 13's 400,171 km | NASA: https://www.nasa.gov/news-release/nasas-artemis-ii-crew-eclipses-record-for-farthest-human-spaceflight | VERIFIED |

**Excerpt (Day 28) "farther than the Moon?" (REFRAME):** Worden was never farther than the Moon. The true contrast is that the Artemis II crew went farther from Earth than anyone, but as four people together, so they were not lonely. → "Farthest from Earth ≠ loneliest".

## Day 27 — NEW-07 Fall into Jupiter (standalone, S)

| Claim | Value | Source | Status |
|---|---|---|---|
| No solid surface; "surface" = the 1-bar level | — | NSSDC Jupiter fact sheet | VERIFIED |
| Arrival speed from far away | ≥ escape velocity, 59.5 km/s | NSSDC: https://nssdc.gsfc.nasa.gov/planetary/factsheet/ | VERIFIED |
| Galileo probe | Entry 47.4 km/s (106,000 mph), peak deceleration 228 g, heat shield up to 16,000 °C, data for 58 min, lost at ~22.7 atm | NASA: https://science.nasa.gov/mission/galileo-jupiter-atmospheric-probe ; https://solarsystem.nasa.gov/missions/galileo-probe/in-depth | VERIFIED. NASA pages differ (228 vs 350 g); use 228 g |
| Survivability | 228 g ≈ 5× the highest human sled exposure (Stapp, 46.2 g, 10 Dec 1954, Holloman AFB; stop in 1.3–1.4 s; 228/46.2 = 4.9) | NM Space Museum: https://nmspacemuseum.org/inductee/john-p-stapp/ ; Air & Space Forces Magazine (Jan 2011 flashback PDF); Linda Hall: https://lindahall.org/john-paul-stapp | CLOSED (museum and magazine sources; no USAF primary report fetched). Say "46 g, measured on a rocket sled, for about a second", not "survivable in general" |
| Deep interior (metallic hydrogen, dilute core) | — | — | Leave out of the 60 s Short, or source it (Juno results) first |

## Day 29 — default topics (headline check only; a full check is due once Day 14 picks one)

| Default | Headline check |
|---|---|
| WIB-15 Lightning everywhere | ~44 ± 5 flashes/s worldwide (Christian et al., *JGR* 108, 2003, https://ntrs.nasa.gov/citations/20040050233). Top hotspot is Lake Maracaibo, ~233 flashes/km²/yr (Albrecht et al., *BAMS* 2016, https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/Where_are_the_lightning_hotspots_on_Earth.pdf). OK |
| NEW-10 Hollow Earth | Shell theorem: zero net gravity inside. But a self-supporting rock shell would carry ~94 GPa vs ~0.2 GPa rock strength, so it collapses. A strong two-act video. OK |
| WIB-04 Time machine on one spot | "Same spot" is meaningless without a reference frame (Earth's orbit is 29.78 km/s ≈ 30 km per second of jump). The script must pick the frame (Earth's surface) explicitly. OK with framing |
| NEW-05 Gravity doubles | Ambiguous: doubling G, doubling Earth's mass and doubling surface g give different results. Example (Earth's mass ×2): the Moon swings to a 128,000 km perigee. The script must define it first |

## Method limits (stated for honesty)

- Fall model:
  - 1-D, vertical, fixed drag area
  - US Standard Atmosphere 1976, with tabulated densities above 86 km
  - Validated against one real jump only
  - Expect ±15% on speeds; heating is order of magnitude.
- The neutron-matter energy (~16 MeV/neutron) is an order-of-magnitude figure from equation-of-state reviews. Do not show more than one significant figure on screen.
- **Provenance by tier:**
  - **Fetched directly this pass:**
    - JPL CAD API
    - NASA Apophis facts
    - NSSDC planetary, Mars and Venus fact sheets
  - **Confirmed through search results that quote the source:**
    - FAI and Guinness records
    - the NASA Artemis II release
    - Kaltenegger & Faherty; Saide et al.
    - Laskar; Lissauer et al.
    - ORAU (radium dials)
    - NASA Galileo pages
    - Fulchignoni et al. (Huygens)
    - Villermaux & Bossa
    - Christian et al.; Albrecht et al.
    - the C172S POH
    - NOAA tides
  - **Formerly domain-knowledge, now search-confirmed (2026-11-18, second pass):**
    - Lattimer & Prakash 2016
    - Kram et al. 1997
    - Jordan & Kurtz 2013
    - NIST tritium half-life; Pm-147 half-life
    - Deimos mass and escape speed
    - Gamow, *Mr Tompkins*: serialised 1938, book c. 1939–40; cite "c. 1940"
    - MIT Game Lab *A Slower Speed of Light* page (https://cms.mit.edu/slower-speed-of-light-teaching-relativity)
  - **Still unconfirmed (minor; doesn't block any script):**
    - the exact first-edition year of Gamow's book
    - the release year of the MIT game
    - the official NASA Ingenuity and Deimos pages; secondary sources were used
- Nothing here has been checked by a human domain expert. This is an AI pre-check, labelled as such.
