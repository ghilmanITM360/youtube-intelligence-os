# Fact check — Day 3 "What If a Bullet Were Made of Neutron Star?"

Per-claim table (05 §3.1). Builds on `06_SCIENCE_VERIFICATION.md` (Day 3/4 section).

**Computed values:** run `python3 research/what-if-channel-strategy/scripts/verify_science.py` (section "Day 3 script").

**Inputs:**
- **Bullet volume:** 8 g of lead (11,340 kg/m³), which is 0.71 cm³. A typical 9 mm bullet weighs ~7.5–8 g.
- **Density range:** nuclear saturation 2.7×10¹⁷ kg/m³ up to a core value of ~10¹⁸ (Lattimer & Prakash 2016).
- **Every result is shown as a range.**

| ID | Script claim | Value used | Source / derivation | Status |
|---|---|---|---|---|
| D3-01 | Released energy ≈ the Sun's total output for about a second (cold open) / 1–3 s (body) | 2.9×10²⁶–1.1×10²⁷ J vs L☉ 3.828×10²⁶ W → 0.8–2.8 s | ~16 MeV per neutron (pure neutron matter near saturation, Lattimer & Prakash 2016); IAU 2015 B3 | ESTIMATE (order of magnitude; labelled on screen) |
| D3-02 | Neutron star: core collapse plus supernova; typically ~1.5 solar masses; ~25 km across | ~1.3–1.4 M☉, 25–26 km (2019); R ≈ 12.4 km (2024 reanalysis) | NICER PSR J0030+0451: Astronomy Now summary; arXiv 2403.14105 | VERIFIED (search-confirmed) |
| D3-03 | NICER is on the Space Station | — | NASA NICER mission (an ISS payload) | VERIFIED (general knowledge; NASA page not fetched) |
| D3-04 | Teaspoon (4.93 mL): 1–5 billion t ≈ 0.5–1.8 km³ of rock | 1.3–4.9 billion t | computed (rock 2,700 kg/m³) | COMPUTED |
| D3-05 | Earth at this density: ball ~225–350 m across; walk around it in ~10 min | 225–349 m; circumference 0.7–1.1 km at 5 km/h = 8–13 min | NSSDC Earth mass; computed | COMPUTED |
| D3-06 | Bullet ~0.7 cm³; ≥190 million t, >700 million t at the dense end | 189–705 million t | computed | COMPUTED |
| D3-07 | Balances a rock cube ~400 m a side | 412–639 m | computed | COMPUTED |
| D3-08 | Pull at 1 m: 1.3 to almost 5 g | 1.3–4.8 g | Newton's gravity | COMPUTED |
| D3-09 | Dust orbit at 1 m: 13–25 km/h, 1–2 s per lap | 3.6–6.9 m/s; 0.9–1.8 s | computed | COMPUTED |
| D3-10 | Surface pull: tens of thousands to >100,000 g | 42,000–157,000 g (5.5 mm equivalent sphere) | computed | COMPUTED |
| D3-11 | Same push as a normal bullet at ~speed of sound gives ~10⁻¹¹ m/s; < 0.5 mm per year | 8 g × 343 m/s → 1.5×10⁻¹¹–3.9×10⁻¹² m/s; 0.46–0.12 mm/yr | momentum conservation. "Roughly the speed of sound": 9 mm muzzle speeds are commonly ~350–400 m/s (not sourced; worded "roughly") | COMPUTED |
| D3-12 | Pressure under it ~100 million × what granite takes | 1.9–7.2×10¹⁶ Pa vs ~0.2 GPa | computed; granite strength order of magnitude (06) | COMPUTED |
| D3-13 | Contact area ≈ a fingernail | cross-section ~95 mm² | computed | COMPUTED |
| D3-14 | Sinks toward Earth's centre | stress ≫ any rock strength | follows from D3-12 (inside the stated magic-container assumption) | SIMULATION (labelled) |
| D3-15 | Held together only by the star's gravity; springs apart when removed | — | standard neutron-star physics (Lattimer & Prakash 2016) | VERIFIED (qualitative) |
| D3-16 | Free neutron lasts ~15 min on average; decays to proton + electron + antineutrino | mean life 878.4 ± 0.5 s | PDG 2024 https://pdglive.lbl.gov/view/S017T | VERIFIED |
| D3-17 | Decay adds "a few percent" | 0.782 MeV vs ~16 MeV ≈ 5% | computed | COMPUTED |
| D3-18 | Ends as a hot cloud of ordinary hydrogen | protons + electrons → hydrogen | follows from D3-16 | COMPUTED (qualitative) |

**v2 length cut (2026-11-19):** claims **no longer in the script** (kept for reference): D3-03 (NICER on ISS), D3-05 (Earth at this density), D3-09 (dust orbit), D3-10 (surface pull), D3-17 (decay adds a few percent). All remaining claims are unchanged from v1.1.

## Notes

**Self-review fixes in v1.1:**
- The cold open had implied power equals the Sun's. It now says total energy equals about one second of the Sun's output.
- Surface-g range corrected.
- "Smaller than a fingernail" → "about the size of a fingernail".
- Removed "a very large hole", which understated the energy and has no sourced comparison.
- Two new lines corrected: walk time 5 → ~10 min; "walking" → "jogging" speed.

**Collision check, 2026-11-18:**
- xkcd's RSS has no neutron-bullet video, and our bank lists the topic as UNUSED by xkcd.
- An older "What If" channel video on neutron stars exists (2.58M views, ~7 years old; 03 M4 scan). Our title and angle (a bullet as a scale reference) differ.

**Firearm framing:**
- The bullet is a size reference only.
- The "launcher" is a featureless outline, and nothing is aimed at anyone.
- The firing beat only shows that it can't be fired.

**Packaging (FR-TITLE-03/04):**
- The title question is answered at ~4:02.
- The thumbnail claim "AT LEAST 190 MILLION TONNES" is D3-06 (the low end, labelled THE MATH).
