# 07e Ten physics episode studies (continuation, 2026-11-23)

**Review kind: SAMPLED_AND_VIEWED + same-model recomputation. Not DEEP_VISUAL, not independent, not expert review.** The ten episodes come from the directive's list of "high-value deep-study episodes" (listed in the request). For each, 16 native-resolution frames were extracted at the ASR time of each checked claim (+0.8 s) plus evenly spaced fill, assembled into one contact sheet, and **viewed by the main session** (`phase7e_frames/SHEET_<id>.jpg`, frame list with times, file names and media hash prefix in `07e_EPISODE_SHEET_FRAMES.csv`). 160 frames over 10 videos touched 122 of the 260 machine-detected shots (one frame per shot at most; "touched" is not "reviewed"), and none of the 719/2,160 numbers of the wider ledger campaign changes because of this pass. Audio was not listened to. Claim data: `07e_EPISODE_CLAIM_CHECKS.csv` (51 rows). Code: `scripts/phase7e_episode_checks.py`, `scripts/phase7e_sheets.py`. Constants: F = fetched this session, S = standard constant, M = author's memory, not fetched (the CSV carries the code on every row).

## Episode map (directive topic -> video ID)
| # | Directive topic | Video ID (long form) | Other videos on the topic (not studied) | Tier before | Shots / events | Frames viewed (shots touched) |
|---|---|---|---|---|---|---|
| 1 | Earth suddenly stops spinning | `gp5G1QG6cXc` (V004) | `19gun1mffWs`, `ERieN5pee7A` (Shorts) | STRUCTURAL | 36 / 86 | 16 (14) |
| 2 | Baseball approaching light speed | `3EI08o-IGYk` (V005) | `Uj10jGq2O8o` | STRUCTURAL | 23 / 69 | 16 (12) |
| 3 | Massive earthquake (the directive gives no number; the magnitude-15 video was chosen) | `e3uk7jU3RHo` (V002) | `wBLVmEZV2Oc`, `FKXVs4UteSc` | STRUCTURAL | 25 / 80 | 16 (12) |
| 4 | Draining the oceans | `Jpy55EgMQgY` (V012) | `aMshLs0YCTQ`, `FkUNHhVbQ1Q` (teleport to Mars) | STRUCTURAL | 21 / 72 | 16 (14) |
| 5 | Nanosecond on the Sun | `UXA-Af-JeCE` (V015) | none | STRUCTURAL | 20 / 63 | 16 (10) |
| 6 | Earth rotating 90 degrees | `WH4g1ptJ-70` (V023) | four Shorts | TARGETED | 25 / 125 | 16 (8) |
| 7 | Moon as a black hole | `UQgw50GQu1A` (V030) | `n2XRulD_IVs` | TARGETED | 23 / 65 | 16 (13) |
| 8 | Submarine in space | `EsUBRd1O2dU` (V007) | none | TARGETED | 25 / 97 | 16 (14) |
| 9 | Laser pointer to the Moon | `JqFSGkFPipM` (V018, "everyone pointed a laser at the moon") | `zgBTwtg7H8E` is a different topic (laser umbrella) | TARGETED | 38 / 104 | 16 (13) |
| 10 | Billion-story building | `Z_xJ40QXu7Q` (V021) | two Shorts | TARGETED | 24 / 66 | 16 (12) |

All ten source videos are available locally (hashes in `03_CHANNEL_MASTER_INVENTORY.csv`). Gap: none. The original article of each topic exists on what-if.xkcd.com (#1, #13, #53, #94, #129 were read by a subagent for the numbers listed per episode; the Earth-stops-spinning, magnitude-15, nanosecond, rotated-world and submarine videos have no matching title in the 162-title archive list, so their originals were not compared).

## Counts
51 rows: 19 consistent, 13 consistent with a caveat, 8 qualified, 7 not verified, 2 supplementary (not claims), 1 open, 1 **discrepant as stated** (E09g). Per episode: E01 6 rows, E02 5, E03 8, E04 5, E05 5, E06 2, E07 4, E08 2, E09 10, E10 4. These are the claims that could be recomputed, chosen by the reviewer; they say nothing about the error rate of the channel. Episode 6 is a qualitative climate counterfactual with no quantitative model: only two rows exist and both are NOT_VERIFIED.

## Episode studies
Each entry: scenario and model, what the picture shows over time (OBSERVED in the viewed frames, times in seconds), simplifications and likely misreadings, and which original method could carry the idea (a proposal, not tested). Claim IDs refer to the CSV.

### 1. Earth stops spinning (`gp5G1QG6cXc`)
- **Model:** the ground stops, the atmosphere and oceans keep their eastward speed v = 2 pi R / T = 465 m/s at the equator, scaled by cos(latitude). Supersonic (343 m/s) for latitudes below 42.5 degrees (E01a, b: consistent). Later a non-rotating Earth has a one-year solar day (E01f, caveat: axial tilt ignored), and atmospheric momentum slowly restarts rotation (E01e: my thin-shell upper-bound estimate is 1,600 years against the stated 3,000, qualified).
- **Visuals:** 14.9 house and clothesline; 33.8 and 37.4 a world map with a 42 N / 42 S band and "470 m/s" arrows, then a "85% OF POPULATION" overlay; 62.4 "470 m/s (1040 mph)" over a bunker; 77.9 Boston skyline with "330 m/s *NO LONGER SUPERSONIC :(" (recomputed 344 m/s at 42.36 N, Mach 1.002, so the label is 4% low and the "no longer supersonic" depends on the sound speed used); 137.2 and 162.1 ocean scenes, the second with a red-orange gradient and lightning (colour used for heat; an exception to an achromatic look); 187.1 cloud map; 211.8 Earth half lit on a black starfield; 221.9 and 226.0 "6 MONTHS" day and night panels; 237 to 261.9 a Moon with a chain and a hat-wearing stick figure "WHAT IF...".
- **Misreading risks:** the band is a flat stripe although speed falls with cos(latitude); the 85% figure is unchecked (E01d); "twice the strongest tornado" is 2.5x to 4x depending on the tornado reference (memory values).
- **Original methods:** 2D vector map with a parametric latitude band and speed gradient; animated arrows; split day/night panel; no 3D needed.

### 2. Baseball at 0.9c (`3EI08o-IGYk`)
- **Model:** relativistic speed 6.04e8 mph (E02a), a gas that is effectively stationary, X-rays arriving at 61.5 ns and the ball at 68.3 ns over 18.44 m (E02c, consistent; the original article says about 70 ns). Kinetic energy (not stated in the video) would be 4.0 Mt TNT, 270 Hiroshima (E02d, supplementary).
- **Visuals:** 8.9 thought bubble; 36.9 to 44.3 ball with speed lines and molecule dots, labels "604,000,000 mph" and "~1,000 mph", the latter struck to "0 mph" at 44.3; 62.0 compression and partial-vacuum diagram; 79.7 "T = 60 NANOSECONDS" with a "~1c" arrow; 115.2 and 132.9 "T = 63 NANOSECONDS" and a "1c" wave; 150.6 white flash; 160.5 mushroom cloud; 168.2 and 172.0 a street map with a crater; 173.2 the rulebook page "RULE 5.05 (b)"; 186.1 the red end card with named credits.
- **Mismatch (OBSERVED):** the screen says ~1,000 mph for the molecules (kinetic theory gives 1,050 to 1,150 mph), the narration says "a few hundred" (E02b, qualified).
- **Original methods:** nanosecond timeline with expanding rings (parametric), particle field (procedural), static document page.

### 3. Magnitude 15 earthquake (`e3uk7jU3RHo`)
- **Model:** E = 10^(1.5 M + 4.8) J (Gutenberg-Richter joule form; the USGS page quotes a different rough relation, 1.44 / 5.24, which changes the Sun result, see SC05). M11 to M15 is a factor 1e6 (E03a); M15 is 2.0e27 J against 3.5e27 J to evaporate the oceans (E03b, within 2x); M18 is 6.3e31 J against an Earth binding energy near 2.2e32 J (E03c, qualified); the Sun threshold is M24.4 to M24.6 (E03d). M1 is a 20 t truck dropped from 10 m (E03g), M0 is an 11-player team at 9 m/s (E03h).
- **Visuals:** a persistent vertical magnitude axis (marks from -15 to 30) with an arrow at the card's magnitude: 30.9 scale; 41.3 globe with 2004 and 2011 labels; 55.8 and 59.6 cracked Earth; 71.0 "10^32 JOULES = BYE BYE EARTH"; 86.0 Sun disc; 92.7 a banded planet; 120.0 cement truck and "10m"; 126.9 football pile; 133.9 to 163.5 tiny events (tree, typing, hourglass); 175.0 figure under a tree.
- **Scientific status:** the axis is a quantitative device (arrows sit at the stated value); the pictures are schematic. M10/M11 fault lengths are anchor-dependent (E03e: 1,800 to 6,100 km for M10; the video's 3,500 km and half-way-round for M11 fit the width-saturated scaling).
- **Original methods:** a reusable vertical ladder component with an animated pointer; one drawing per rung; counters for energy.

### 4. Draining the oceans (`Jpy55EgMQgY`)
- **Model:** ideal Torricelli outflow at 463 m/s through 314 m2 gives 2.9e5 years and 0.035 mm per day (E04a, b, consistent, idealised); the Black Sea is cut off by sills at -32 to -80 m, so -100 m is not the threshold (E04c, caveat); the -500 m "Japan connects to Korea and Russia" claim equals the original article but was not checked against bathymetry (E04d).
- **Visuals:** 8.7 and 15.7 cut-away of Challenger Deep with the portal; 35.6 globe "MARIANA TRENCH PORTAL"; 43.7 a whale pulled in; maps labelled -50 (61.2), -100 (90.0, Black Sea circled), -200 (114.2, "THE NETHERLANDS"), -500 (116 to 122 s, Japan circled and joined), -1000 (125 to 131 s) and -5000 m (166.2); 148.7 "MID-OCEAN RIDGE" profile; 185.3 news gag; 201.2 end card. The -500 m map appears about 3 s after the sentence starts (the ASR-time frame shows -200 m).
- **Caveat:** the map coastlines look contour-derived but their data source is unknown here.
- **Original methods:** bathymetry-threshold maps built procedurally from an open elevation dataset; side-profile silhouettes.

### 5. A nanosecond on the Sun (`UXA-Af-JeCE`)
- **Model:** Stefan-Boltzmann flux 6.3e7 W/m2 at 5,772 K gives 6.3e-6 J/cm2 per nanosecond, "about 1e-5" (E05b); the burn threshold 5 J/cm2 equals 1.2 cal/cm2 (E05c) and would take 0.79 ms at the surface; "one femtosecond" only works if the temperature exceeds 5.4 MK, true in the deep interior, false at "a few million" degrees (E05d).
- **Visuals:** 21.7 split panel "HOOOURS | 1 NANOSECOND | HOURS" with "~5,800 K"; 40.1 eye with "~0.000001 J"; 72.2 and 88.2 log time axis (1 ns to 30x10^6 ns) with eye, retina, nerve, brain; 98.7 and 104.3 "0.00001 J/cm2", "0.000000001 s", "IEEE STANDARD 1584-2018", "5 J/cm2"; 120.3 teleporter phone gag; 136.4 whiteboard P/A = sigma T^4 and "1 FEMTOSECOND > IEEE P1584B"; 152.4 X-rays; 184 "TEMPERATURE != HEAT, HEAT = TEMPERATURE x TIME".
- **Misreading risk:** the last slide is an informal statement, not a valid equation; two designations of the IEEE standard appear (1584-2018 and P1584B).
- **Original methods:** log time axis component; equation board with animated substitution; gradient hot/cold panels.

### 6. Earth rotated 90 degrees (`WH4g1ptJ-70`)
- **Model:** none quantitative. A narrative climate counterfactual (land rotated, axis fixed). Only two rows: the sea-level range if all ice melted (about 215 to 230 ft, memory) and the horse-latitude statement, both NOT_VERIFIED. No model run was available; the claims are qualitative climatology.
- **Visuals:** 43.6 feedback-loop whiteboard (Sun, clouds, rain, wind, CO2, mountains, biosphere); 72.6 three-cell circulation; 101.7 wind cells over a globe; 123.4 and 130.7 coloured rotated-world map with wind arrows and orange HORSE LATITUDES bands; 159.8 hurricane; 188.8 to 334.1 coloured regional maps with circular vignettes (Amazon, Antarctica, Asia city dots, London); 356.9 and 363.1 flood and rain scenes; 392.1 film-strip gag with fire ants.
- **Style note (OBSERVED):** this episode uses green, tan, light-blue and grey flat fills, unlike the mostly achromatic episodes, so the "achromatic palette" statement must stay a sample statement.
- **Original methods:** data-driven rotated map (sphere rotation of real land polygons), simple climate-zone fills, vignette circles; needs a real geography source.

### 7. Moon as a black hole (`UQgw50GQu1A`)
- **Model:** r_s = 0.109 mm, diameter 0.218 mm; the same-size case needs 588 solar masses (E07b); the sieve statement is borderline: 218 um against the 212 um opening of ASTM No. 70, so it passes No. 60, not No. 70 (E07a, qualified, inherited from the original); the infrared warming of 1.2 m degF is the right order in my crude model (0.8 to 1.5 m degF, E07c); the unit conversions are exact (E07d).
- **Visuals:** 9.7 eclipse versus "???"; 18.9 "BLACK HOLE MOON" with a dot; 27.6 a scanned Wentworth grade chart with two red circles; 46.0 side-by-side Moon / black hole Moon; 64.4 to 119.7 dark night scenes; 138.1 whiteboard of phases; 156.5 to 174.9 IR flow diagram with "10X" and the unit list (+0.0012 F, +0.0012 R, +0.00035 Romer, +0.00053 Reaumur, +0.00066 K); 193.3 "THAT'S ONE SMALL STEP FOR -" "AAAAH"; 201.3 black circle on the Moon's orbit.
- **Rights note:** the Wentworth chart on screen looks like a reproduced scan; any original production needs its own redraw.
- **Original methods:** scale comparison (sphere versus sand grain), animated unit-conversion list, energy-flow arrows.

### 8. Submarine in space (`EsUBRd1O2dU`)
- **Model:** reactor heat of 100 to 200 MW warms a steel-like 18,750 t hull by 0.6 to 1.3 K per minute against the video's 0.5 K (E08a, qualified: needs a 2.6x larger heat capacity); 24 Trident missiles at about 4 m/s give 96 m/s (E08b, arithmetic exact; my rough impulse estimate is 6.7 m/s per missile, same order); a 400 km de-orbit burn is about 102 m/s.
- **Visuals:** 28.1 "WATER-FREE ZONE" with pressure arrows; 46.9 electrolysis diagram; 65.7 figure in "SPACE"; 84.4 "WHY SPACE IS WARM, PART 1" with T = 2/(3 k_B) KE; 103.2 sparks "~2000 F (1100 C)"; 122.0 heat leaving the hull; 140.7 "200 MEGAWATT"; 161.8 red heat on the reactor; 178.3 deorbit arc; 197.0 and 203.6 missile launch from the cut-away; 215.8 "DELTA V ~ 100 m/s" and "24 x 4 m/s ~ 100 m/s"; 231.8 and 234.5 a figure on a rail gag.
- **Original methods:** flat 2D cut-away with labelled layers; equation card; delta-v comparison panels.

### 9. Everyone points a laser at the Moon (`JqFSGkFPipM`)
- **Model:** S x pi R^2 = 12.9 PW; **the board shows 6.45e15 W, exactly half**, with no stated reason, and narration says "about 6 petawatts" (E09a, qualified; the original page gives about 10 PW). 5 mW x 6e9 people = 30 MW, 200 million times weaker (E09b); half a lux needs green light at peak efficacy (E09c); "half as bright as moonlight" compares different quantities and the screen's 1 LUX full-Moon value is above typical 0.1 to 0.3 lux (E09d, open); 20 lux is 2x an earthshine estimate of 9 lux (E09f); the quarter cup of gasoline matches the 1.85 MJ NIF shot (E09i). **E09g: "5 petawatts, double the world's average electricity consumption" is about 1,500 times world demand (3.36 TW from Ember's 29,471 TWh); 5 petawatts is plausible for matching sunlight (1.8 PW of green light at 36% efficiency), so the comparison is what is wrong, and the original article has the same wording.** The ASR word "soil reserves" is an ASR error: the pump icon at 216.4 supports "oil" (E09h).
- **Visuals:** 24.0 map "75% WORLD POPULATION"; 53.8 and 57.3 whiteboard "~10^13 m2", "~6,450,000,000,000,000 W"; 72.1 "1 WATT" and "5 MILLIWATT" pointers; 103.1 to 109.5 "0.5 LUX" versus "1 LUX" Moons and "130,000 LUX"; 138.5 "NIGHTSUNS (WITH LENSES)"; 168.3 "LUXOR SPOTLIGHTS"; 194.3 aircraft firing lasers versus two Earths on a plug; 216.4 pump "2 MIN"; 234.3 "NATIONAL IGNITION FACILITY, 500 TW ~2 ns"; 264.5 Moon struck by a beam.
- **Original methods:** a quantity-chain board (area x flux = power), procedural beam fans and glow, a scale gag for the NIF.

### 10. Billion-story building (`Z_xJ40QXu7Q`)
- **Model:** floor counts are exact (1e4, 1e6, 1e8, 1e9); with 4 m per floor 1e8 floors is 400,000 km, about the Moon's distance, and 1e9 floors is 10 Moon distances (E10a); weight is 0.53% lower at the equator (E10b); geostationary radius is 0.110 of the Moon distance from the centre, 0.093 from the surface (E10c); a uniform steel column tops out near 3.2 km, concrete near 1.7 km (E10d).
- **Visuals:** 9.1 question card and a child in red ink; 45.3 a height chart with a collapsed pile; 63.4 a lattice tower and a catapult gag; 99.7 to 135.9 floor ladders ("FLOORS 100 / 10,000 / 1,000,000, GOAL: 1,000,000,000"); 154.0 a swing ride; 158.9 "WEIGHT MAXIMUM / MINIMUM"; 167.5 and 172.1 "GRAVITY WINS | CENTRIFUGAL WINS", "1/10th TO THE MOON"; 190.3 a tower toward the Moon; 208.4 "~220 km/s" arrow with a satellite (not recomputed).
- **Original methods:** parametric height bars on a broken axis; Earth-Moon distance bar with a bracket; no 3D needed.

## What this adds and what it does not
- Adds: 51 recomputed rows with assumptions and constants status, 10 contact sheets viewed, and visual-versus-spoken mismatches (E01c 330 versus 344 m/s, E02b 1,000 versus a few hundred mph, E09a 6.45 PW, E07d 0.00066 versus 0.000667 K, E05 slides).
- Does not: view every frame or all 260 shots, hear the audio, use an independent reviewer, fetch the constants coded M, or establish the accuracy of the drawn maps or the physics of Episode 6.
- Hand-offs for a human: listen to the E09g sentence (petawatt versus terawatt), compare the on-screen rule text with the MLB rulebook, check the Earth-stops-spinning, magnitude-15, nanosecond, rotated-world and submarine originals if they exist, and confirm every M-coded constant.
