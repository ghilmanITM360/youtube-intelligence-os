# Fact check — Day 1 "Does a Higher Fall Always Hit Harder? 1 Metre to the Edge of Space" (script v3)

Per-claim table required before scripting (05 §3.1). Builds on `research/what-if-channel-strategy/06_SCIENCE_VERIFICATION.md` (Day 1 section). Rewritten 2026-11-19 for script v2 after the critical review; v1.1 claims that changed are listed at the end.

**Computed values:** re-run with `python3 research/what-if-channel-strategy/scripts/verify_science.py` (section "Day 1 script"). v2 added the "landing speed from …" lines.

**Model:**
- 1-D vertical drop from rest.
- Belly-down suited body; drag area per mass is 0.00505 m²/kg, calibrated once so the peak speed equals Baumgartner's 1,357.6 km/h.
- The drag coefficient is held constant across Mach 0 to about 9 and across the continuum-to-thin-air transition above ~100 km. This is a real limitation.
- US Standard Atmosphere 1976, with tabulated densities above 86 km.
- Gravity varies with altitude. Earth's rotation and wind are ignored (stated on screen).

**Model check (honest status):**
- One number was fitted: the peak speed.
- Peak altitude (27.5 km vs 27.8 km) and time to peak (51 s vs 50 s) come out of the same fit. They are a **consistency check, not independent validation**.
- The one clear miss is supersonic duration: 36 s vs 30 s reported (20% off). The script says so.
- Uncertainty is ±15% (06). v2 says this on screen. Above 60 km the model is extrapolation.

**v3 length cut (2026-11-19):** ~1,230 → ~890 words. Claims **no longer in the script** (kept for reference): D1-04 (10 m), D1-10 (19 km pressure), D1-14 (spin and freefall duration), D1-16 (Eustace), D1-29 (Alkemade), D1-17 (60 km, already cut in v2). Every remaining claim is unchanged from v2.
- No domain expert has reviewed any of this.

**Status labels:**
- VERIFIED: source read or confirmed through search results quoting it.
- COMPUTED: our model.
- ESTIMATE: order of magnitude only.
- SECONDARY: sourced to Wikipedia or a news/history site, not a primary document.

| ID | Script claim | Value used | Source / derivation | Status |
|---|---|---|---|---|
| D1-01 | 400 km drop: more than 8,000 km/h at the top of the atmosphere | 8,405 km/h at 100 km | model | COMPUTED |
| D1-02 | "For four minutes, nothing happens" | 4.3 min to reach 100 km | model | COMPUTED |
| D1-03 | 1 m: ~16 km/h | 16 km/h, 0.45 s | model (equals vacuum at this height) | COMPUTED |
| D1-04 | 10 m ≈ three-storey building; 50 km/h; same as with no air | 50 km/h (vacuum 50) | model; storey ≈ 3 m ("roughly") | COMPUTED |
| D1-05 | 100 m: 138 km/h, vs 159 with no air | 138 / 159 km/h | model | COMPUTED |
| D1-06 | Top speed ~200 km/h | 204 km/h (belly-down, sea level) | model. FAI skydiving commission: ~200 km/h belly-to-earth, https://fai.org/node/24646 | COMPUTED + VERIFIED (secondary agreement) |
| D1-07 | From 300 m you land at 187; from 1 km, 204; from 3 or 5 km, about the same | 187 / 204 / 204 / 204 km/h | model (`verify_science.py`, "landing speed from …"). **Replaces v1's "95% after 220 m", which was measured from a 5 km drop and does not apply to a drop starting at 220 m (that lands at 175 km/h)** | COMPUTED |
| D1-08 | 10 km air ≈ −50 °C | −50 °C | USSA 1976 | COMPUTED (standard model) |
| D1-09 | From 10 km: peak ~320 km/h ~20 s in; ~265 at 5 km; back to ~200 near the ground | 320 km/h at 8.6 km after 21 s; 265; 204 | model | COMPUTED |
| D1-10 | ~19 km: pressure low enough that water boils at body temperature; blood stays liquid because it is sealed in vessels under its own pressure and skin contains the body; tongue and lung moisture are not | USSA 6.5 kPa at 19 km; water vapour pressure at 37 °C ≈ 6.3 kPa | Armstrong limit https://en.wikipedia.org/wiki/Armstrong_limit; Ebullism https://en.wikipedia.org/wiki/Ebullism (blood pressure adds to ambient pressure; skin contains the body) | VERIFIED (secondary) + COMPUTED. v1.1 said "your heart keeps it there", which was loose |
| D1-11 | 14 Oct 2012, exit ~39 km (38,969 m) | 38,969.4 m | FAI https://fai.org/node/193240 | VERIFIED |
| D1-12 | Air ~260× thinner at 39 km | 1/264 | USSA | COMPUTED |
| D1-13 | ~50 s later, near 28 km, 1,358 km/h, faster than sound | 1,357.6 km/h; 50 s; 27,833 m | FAI (speed); Red Bull final data via NBC https://www.nbcnews.com/id/wbna50700999 and CSM | VERIFIED |
| D1-14 | Flat spin ~13 s; freefall 4 min 20 s | 13 s at ~60 rpm; 4:20 | Red Bull final data https://www.redbull.com/us-en/red-bull-stratos-release-mission-data (search-confirmed 2026-11-19; AVweb reports 4:18, so the script says "four minutes and twenty seconds" per Red Bull) | VERIFIED |
| D1-15 | Model test: tuned one number; peak height/timing within about a second; a consistency check, not proof; 36 s vs 30 s supersonic; trust ±15%, less the higher | 27.5 km, 51 s; 36 vs 30 s; ±15% (06) | model vs D1-13/14 | COMPUTED. Wording corrected in v2 to say it is not independent proof |
| D1-16 | Eustace, two years later, ~41 km, small stabilising chute, fell slower on purpose | 41,422 m, 24 Oct 2014 | FAI https://fai.org/node/155244; Guinness 2014 | VERIFIED |
| D1-17 | **Not in script v2 (60 km height cut for pacing; kept for reference).** 60 km: peak ~2,250 km/h, ~twice the speed of sound, ~2.5 g | 2,256 km/h, Mach 2.05, 2.6 g | model | COMPUTED |
| D1-18 | 100 km = FAI boundary convention, not universal | FAI 100 km; the US often uses 80 km | https://www.space.com/karman-line-where-does-space-begin | VERIFIED (secondary) |
| D1-19 | 100 km: peak ~3,600 km/h, ~5 g, ~5.5 min, lands at ~200 | 3,620 km/h, 4.7 g, 5.6 min, 204 | model | COMPUTED |
| D1-20 | Gravity at 400 km ≈ 89% | 89% | (R/(R+h))² | COMPUTED |
| D1-21 | 400 km: >8,400 km/h at 100 km; peak ~20 g; >10 g for ~11 s; script says the 20 g and 11 s are shaky because the air is so thin | 8,405 km/h; 20 g; 11 s | model with constant drag coefficient. Above ~100 km the flow is in the transition to free-molecular regime where real drag differs; the true uncertainty is **larger than ±15%** | COMPUTED, low confidence for g and duration (flagged on screen: ESTIMATE) |
| D1-22 | Air ahead heated to "thousands of degrees" | stagnation estimate ~2,800 °C at Mach 8.7 | ideal-gas stagnation; real-gas effects lower it | ESTIMATE (labelled on screen) |
| D1-23 | "Rocket-sled riders have taken forty g and more, but only for a second or less" (reworded 2026-11-19 review: the ~83 g figure lasted ~0.04 s, so "a second or so" overstated it) | NASA history gives ~40 g peak for Stapp (1954) and ~83 g on Beeding's chest for about 0.04 s (1958) | https://www.nasa.gov/wp-content/uploads/static/history/afspbio/part5-5.htm; Guinness lists Beeding 82.6 g (voluntary record); Wikipedia disputes that value (sled ~40.4 g). Sources also differ on Stapp (40 vs 46.2 g) | VERIFIED (range). **v1.1's "hardest deceleration anyone has deliberately ridden was Stapp, 46.2 g" is removed: contradicted by Beeding and sources disagree** |
| D1-24 | "Twenty g for seconds, with that heat, is outside any test we know of. We can't tell you how it ends" | — | No outcome predicted. "Any test we know of" is a statement about our own search, not a universal claim | NARROWED |
| D1-25 | ISS at about this height; ~8 km per second; ~90 min per orbit | NASA "five miles per second", ~90 min; altitude ~400 km (secondary) | https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ | VERIFIED |
| D1-26 | Answer: from about 35 km up, the danger moves into the sky (faster than sound, crushing g, heat) | model threshold for supersonic: 32.5 km; model runs fast, so "about 35" | model | COMPUTED |
| D1-27 | The model's landing speed from 3 km, 5 km, 10 km, 39 km, 60 km, 100 km and 400 km is 204 km/h in every case ("the landing line stays flat") | 204 km/h each | `verify_science.py` "landing speed from …". For 400 km this assumes the fall is survived, which the script says in so many words ("the word 'if' is doing a lot of work") | COMPUTED |
| D1-28 | Alan Magee: ~22,000 ft, 1943, no parachute, through the glass roof of a railway station, survived | 22,000 ft (one source says 20,000) | https://en.wikipedia.org/wiki/Alan_Magee | SECONDARY (height varies by source; script says "about") |
| D1-29 | Nicholas Alkemade: ~18,000 ft, 1944, no parachute, into pine trees and snow, survived | 18,000 ft | https://en.wikipedia.org/wiki/Nicholas_Alkemade; RAF Museum https://www.rafmuseum.org.uk/blog/the-indestructible-alkemade/; German investigators checked the wreck | SECONDARY |
| D1-30 | "By then the air had capped their speed. The floor did the rest." | speed capped by terminal velocity; tumbling and body position change the exact figure | physics (D1-07); no source gives their measured speed | INTERPRETATION. Wording is qualitative on purpose |

## Notes and decisions

**Survival claims (changed from v1.1):**
- The script makes **no** claim about which height is lethal. The search on 2026-11-19 found fall-height studies that disagree (some find mortality rises with height; others find height adds little once injury severity or intent is accounted for), and no accepted lethal-height threshold.
- Instead, the script says the landing speed is capped and uses two documented survivors to show the floor matters. It states "luck, not a plan" and "nothing here is safety advice".
- **Vesna Vulović (10,160 m, 1972) is deliberately left out.** Guinness lists the record, but a 2009 journalistic inquiry argues the plane may have broken up much lower. Not worth the dispute for one beat.

**Footage:**
- No real footage is used. The Stratos moments are original illustrations labelled REAL DATA with dates.
- Collision check, 2026-11-18: xkcd's RSS has no falling-from-height video. Their 2026-10-20 "floated upwards 1ft per second" is an adjacent altitude ladder, so the breathing and pressure heights stay to one short beat (Height 6).
- No title in our 03/04 competitor lists matches ours.

**Packaging check (FR-TITLE-03 / FR-TITLE-04):**
- The title asks "does a higher fall always hit harder?". The answer is given on screen at 0:56 (landing line freezes at 204) and summarised at 4:24.
- Thumbnail numbers: "1 KM: 204 km/h" and "100 KM: 204 km/h", both COMPUTED (D1-07, D1-19).

**Changes from v1.1:**

| v1.1 claim | v2 |
|---|---|
| D1-06 "95% of terminal after ~220 m" | Replaced by D1-07 (landing speeds from 300 m and 1 km). The v1.1 number came from a 5 km drop |
| D1-10 "your heart keeps it there" | Reworded (sealed vessels, own pressure, skin) |
| D1-15 "This is the check we promised … within about a second" | Reworded as a consistency check, with the ±15% limit stated |
| D1-23 Stapp "hardest ever" | Removed; replaced by a ranged claim |
| D1-24 narrowed in v1.1 | Narrowed further (D1-24) |
| Eustace height (v1.1 Height 8) | One sentence |
| Ground rules block | One paragraph |
