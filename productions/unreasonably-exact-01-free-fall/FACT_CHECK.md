# Fact check — Day 1 "What If You Fell From Every Height — 1 Metre to the Edge of Space?"

Per-claim table required before scripting (05 §3.1). Builds on `research/what-if-channel-strategy/06_SCIENCE_VERIFICATION.md` (Day 1 section).

**Computed values:** re-run with `python3 research/what-if-channel-strategy/scripts/verify_science.py` (section "Day 1 script").

**Model:**
- 1-D vertical drop from rest.
- Belly-down suited body; drag area per mass is 0.00505 m²/kg, calibrated once so the peak speed equals Baumgartner's 1,357.6 km/h.
- US Standard Atmosphere 1976, with tabulated densities above 86 km.
- Gravity varies with altitude.

**Model validation against independent data it was not fitted to:**
- Peak altitude: 27.5 km vs 27.8 km reported.
- Time to peak: 51 s vs 50 s.
- Supersonic duration: 36 s vs 30 s reported. The model runs slightly fast, and the script says so.

**Status labels:**
- VERIFIED: source read or confirmed through search results quoting it.
- COMPUTED: our model.
- ESTIMATE: order of magnitude only.

| ID | Script claim | Value used | Source / derivation | Status |
|---|---|---|---|---|
| D1-01 | 400 km drop: >8,000 km/h at the top of the atmosphere | 8,405 km/h at 100 km | model | COMPUTED |
| D1-02 | "For four minutes nothing touches you" | 4.3 min to reach 100 km | model | COMPUTED |
| D1-03 | 1 m: under half a second, ~16 km/h | 0.45 s, 16 km/h | model (equals vacuum at this height) | COMPUTED |
| D1-04 | 10 m ≈ three-storey building; <1.5 s; 50 km/h; same as with no air | 1.43 s; 50 km/h (vacuum 50) | model; storey ≈ 3 m (approximate, said "roughly") | COMPUTED |
| D1-05 | 100 m: vacuum ~160 vs with air ~138 km/h | 159 / 138 km/h | model | COMPUTED |
| D1-06 | Terminal velocity ~200 km/h; 95% in 7 s after ~220 m | 204 km/h; 7 s; 218 m | model. Belly-down terminal ~55 m/s is the standard skydiving figure (06) | COMPUTED |
| D1-07 | From 1, 3 or 5 km you land at ~200 km/h | 204 km/h | model | COMPUTED |
| D1-08 | 10 km air ≈ −50 °C | −50 °C | USSA 1976 | COMPUTED (standard model) |
| D1-09 | Peak ~320 km/h ~20 s in; ~265 at 5 km; ~200 near ground | 320 at 8.6 km after 21 s; 265; 204 | model | COMPUTED |
| D1-10 | ~19 km: pressure ≈ the point where water boils at 37 °C; saliva and lung moisture boil, blood is protected by heart pressure | USSA 6.5 kPa at 19 km; water vapour pressure at 37 °C ≈ 6.3 kPa | Armstrong limit (https://en.wikipedia.org/wiki/Armstrong_limit, secondary); USSA | VERIFIED (secondary) + COMPUTED. Script says "roughly" |
| D1-11 | 14 Oct 2012, exit 38,969 m | 38,969.4 m | FAI https://fai.org/node/193240 | VERIFIED |
| D1-12 | Air ~260× thinner at 39 km | 1/264 | USSA | COMPUTED |
| D1-13 | Peak ~50 s, ~28 km, 1,357.6 km/h, Mach 1.25 | 50 s, 27,833 m | FAI (speed); Red Bull final data via NBC https://www.nbcnews.com/id/wbna50700999 and CSM | VERIFIED (time/altitude search-confirmed; Red Bull's own page did not load) |
| D1-14 | Flat spin ~13 s; ~4 min 20 s freefall | 13 s at ~60 rpm; 4:20 | Red Bull final data (as above) | VERIFIED (search-confirmed) |
| D1-15 | Model: 27.5 km after 51 s; supersonic ~6 s too long | 27.5 km, 51 s; 36 vs 30 s | model vs D1-13/14 | COMPUTED |
| D1-16 | Eustace, Oct 2014, 41,422 m, drogue, speed record stayed with Baumgartner | 41,422 m, 24 Oct 2014 | FAI https://fai.org/node/155244; Guinness 2014 | VERIFIED |
| D1-17 | 60 km: ~2,250 km/h, ~Mach 2, ~2.5 g | 2,256 km/h, Mach 2.05, 2.6 g | model | COMPUTED |
| D1-18 | 100 km = FAI boundary convention, not universal | FAI 100 km; the US often uses 80 km | https://www.space.com/karman-line-where-does-space-begin | VERIFIED (secondary) |
| D1-19 | 100 km: ~3,600 km/h, >3× sound, ~5 g, ~5.5 min, ~200 km/h at the ground | 3,620 km/h, Mach 3.19, 4.7 g, 5.6 min, 204 | model | COMPUTED |
| D1-20 | Gravity at 400 km ≈ 89% | 89% | (R/(R+h))² | COMPUTED |
| D1-21 | Peak ~20 g; >10 g for ~11 s | 20 g; 11 s | model | COMPUTED (±15%) |
| D1-22 | Air ahead heated to "thousands of degrees" | stagnation estimate ~2,800 °C at Mach 8.7 | ideal-gas stagnation; real-gas effects lower it | ESTIMATE (labelled on screen) |
| D1-23 | Stapp 46.2 g, 1954, about a second | 46.2 g, 10 Dec 1954, stop in 1.3–1.4 s | AFTC history page; NM Space Museum (06) | VERIFIED |
| D1-24 | "Eleven seconds above ten g, in this kind of fall, is far beyond what anyone is put through on purpose" | — | v1 said "never been tested on a person", which was too strong because sustained-g centrifuge research exists. Narrowed in v1.1; no outcome is predicted | FIXED (v1.1) |
| D1-25 | ISS at about this height; ~5 miles (8 km) per second; ~90 min per orbit | NASA "five miles per second", 16 orbits/day, ~90 min; altitude ~400 km (secondary) | NASA https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ | VERIFIED |
| D1-26 | Answer: start above ~35 km to break the sound barrier | model threshold 32.5 km; the model runs fast, so "about 35" | model | COMPUTED |

## Notes and decisions

**D1-24 (owner or reviewer):**
- Centrifuge studies have exposed people to sustained g. The script's line is "never been tested on a person", which is too strong unqualified.
- Safer replacement, recommended before recording: "That's far beyond what people are exposed to on purpose, and we're not going to guess how it ends."
- This is not changed in v1, so that the owner sees the choice. *(Applied in v1.1 below.)*

**Footage:**
- No real footage is used. The Stratos and Stapp moments are original illustrations labelled REAL DATA with dates.
- Collision check, 2026-11-18: xkcd's RSS has no falling-from-height video. Their 2026-10-20 "floated upwards 1ft per second" is an adjacent altitude ladder, so the breathing and pressure rungs are kept to one short beat (Rung 6).
- No title in our 03/04 competitor lists matches ours.

**Packaging check (FR-TITLE-03 / FR-TITLE-04):**
- The title asks "what happens from every height". The answer is given on screen at 7:50 (three-bracket summary).
- The thumbnail number, 1,358 km/h, is VERIFIED (D1-13).
