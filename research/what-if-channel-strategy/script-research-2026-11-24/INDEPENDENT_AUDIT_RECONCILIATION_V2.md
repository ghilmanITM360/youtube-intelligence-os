# Independent audit reconciliation V2 (2026-11-24)

Status vocabulary requested: CONFIRMED / QUALIFIED / DISAGREED WITH EVIDENCE / STILL OPEN. None is DISAGREED; none is wholly STILL OPEN as a finding, but residual open items are listed per row. 'Evidence checked' states reading depth: WebFetch extracts and sub-agent reads are summaries, not full verbatim reading by the lead; Horizons tables and model reruns were read/run in full.

| # | Slot | Finding | Status | Fix | Still open |
|---|---|---|---|---|---|
| F1 | 08 | Moon Long overstates ocean timing (12-h solar beach clock, 'lose most of their size', 'would not flood') | CONFIRMED | FIXED | Physical oceanographer still needed |
| F2 | 09 | Solar-tides Short final paragraph implies a specific smaller tide at many coasts | CONFIRMED | FIXED | Oceanographer to confirm |
| F3 | 03 | 'Delay keeps growing by about five seconds every day' ignores Earth's orbital motion | CONFIRMED | FIXED | Optional navigation reader |
| F4 | 05 | Phobos ending 'not with a jump' categorical despite stated model limits | CONFIRMED | FIXED (status CONDITIONAL_DRAFT) | Planetary dynamicist; primary escape-speed paper |
| F5 | 01 | Higher Fall Long: peak vs arrival vs time; model assumptions; not re-entry; duration metadata; compare with Day 1 v3 | QUALIFIED | FIXED / owner choice open | Aerodynamics reviewer |
| F6 | 02 | Skydiver Short: 1.85 km/5% criterion; 10 km example; safety | CONFIRMED (already corrected, rechecked) | FIXED | Aerodynamics reviewer |
| F7 | 04 | Tiny-world orbit: orbit as trajectory, toy world, 140 min tie, launch geometry, jump speed | QUALIFIED | FIXED | Physicist; biomechanics source |
| F8 | 06 | Voyager Long: preserve 2024 repair; separate historical vs current; replace process language; qualify two days; recheck NASA | CONFIRMED | FIXED (time-sensitive) | Production-day recheck |
| F9 | 07 | Lunar laser Short: instrument specifics, photon figures, mm meaning, mirrors-only implication | CONFIRMED | FIXED | LLR expert |
| F10 | 10 | Farthest human: Guinness record and definition; geometry; Munroe overlap; keep slot and offer distinct angle | CONFIRMED | FIXED (owner decision on overlap open) | Mission-report check; owner |

## Detail

### F1 (slot 08): Moon Long overstates ocean timing (12-h solar beach clock, 'lose most of their size', 'would not flood')
- **Status:** CONFIRMED
- **Evidence checked:** v1 spoken text contained: 'the sea does not drain, and it does not flood'; 'solar rhythm repeats exactly every twelve hours'; 'beach clock would lock to the Sun'; 'lose … most of their size'. NOAA tides07_cycles (read 2026-11-24): continents block the bulges, coasts differ (diurnal/semidiurnal/mixed); the page does not mention the Sun. No ocean model of a Moonless Earth found (searches 2026-11-24).
- **Change:** Rewrote narration into four separated parts: immediate removal, transient existing motion (decay time unknown), solar forcing (a little under half the Moon's), local response (basin, Bay of Fundy example). Removed flood/no-flood, 12-hour clock, size-loss and 'beach clock'.
- **Files updated or checked:** 08 SCRIPT/TITLE/BEATS/FACT/LENS/STATUS; 09 (same issue checked); ledger V08-C05..C09
- **Still open:** Physical oceanographer still needed

### F2 (slot 09): Solar-tides Short final paragraph implies a specific smaller tide at many coasts
- **Status:** CONFIRMED
- **Evidence checked:** v1 last paragraph: 'many coasts would still have two high tides and two low tides a day … smaller, by an amount that depends on the coast'. That implies two daily solar tides and a smaller tide at many coasts. NASA: Sun's force 'a little less than half' the Moon's; NOAA: 'about half'; Hendershott 0.4605 (potential ratio).
- **Change:** New last paragraph: the Sun's push would remain, but that is a force statement, not water level; local tide could differ a lot. '46%' removed; NASA wording used; no fraction remaining.
- **Files updated or checked:** 09 all files; 08 checked for the same phrase
- **Still open:** Oceanographer to confirm

### F3 (slot 03): 'Delay keeps growing by about five seconds every day' ignores Earth's orbital motion
- **Status:** CONFIRMED
- **Evidence checked:** JPL Horizons (Earth-centred, queried 2026-11-24): +6.7 s/day on 2026-11-24, +3.1 s/day May 2026/2027, about −2 s/day Feb–Mar 2027, up to +11.7 s/day Sep 2027. Sun-relative growth is 4.87 s/day, which is where 'about five' came from. NASA release 2026-11-19 and blog 2026-11-18/20 reread: one light-day = 25.9 billion km, ~24 h each way.
- **Change:** Daily-growth statement removed; replaced by 'changes a little each day … stays close to a day each way'. Ledger records the Horizons numbers.
- **Files updated or checked:** 03 all files; 06 checked
- **Still open:** Optional navigation reader

### F4 (slot 05): Phobos ending 'not with a jump' categorical despite stated model limits
- **Status:** CONFIRMED
- **Evidence checked:** Ball model: 11.3 m/s vs jump 2–3 m/s (fall back in ~12–17 min). Real escape speed varies with shape, spin and Mars's tide (Herreros & Charnoz 2026, appendix read by sub-agent); secondary sources give conflicting local ranges (≈1.4–10 m/s; 4–10 m/s); no primary numeric range found. Mass 1.0659e16 kg from v1 not found in any source.
- **Change:** Ending now conditional: ball model says you fall back; real moon varies by place; reported values differ; only a real shape model could say; leaving Phobos is not leaving Mars. Mass replaced by 1.0637e16 kg (secondary).
- **Files updated or checked:** 05 all files
- **Still open:** Planetary dynamicist; primary escape-speed paper

### F5 (slot 01): Higher Fall Long: peak vs arrival vs time; model assumptions; not re-entry; duration metadata; compare with Day 1 v3
- **Status:** QUALIFIED
- **Evidence checked:** Model rerun 2026-11-24: 1 km arrival 188.8 km/h, 21–22 s; 100 km arrival 189.0, 5.6–6.0 min, peak 3,585–3,620 km/h at 40–41 km (Mach 3.1–3.2); arrival difference 0.1–0.15% (belly-down); 2.8% head-down bound. v1 text already separated these but mixed them in the recap, said 'first minute and a half' and gave two runtimes (4:45 vs 3.5–4 min). Day 1 v3 (approved) prints 204 km/h and 'about five g' from a calibrated fit.
- **Change:** Added three-numbers recap; stated 41 km as highest jump on record and that higher values are calculation; arrival 'about 190, range 160–205'; 'first minute or so'; one runtime range; re-entry paragraph kept. Both V2 and Day 1 v3 preserved; differences documented in STATUS.
- **Files updated or checked:** 01 all files; 02 checked
- **Still open:** Aerodynamics reviewer

### F6 (slot 02): Skydiver Short: 1.85 km/5% criterion; 10 km example; safety
- **Status:** CONFIRMED (already corrected, rechecked)
- **Evidence checked:** Searched v1 and V2 for '1.85' and '5%': none in the spoken text. 10 km, set B: peak 299 km/h at 20.4 s, ground 189.0, total 154 s (slowing 134 s); '1 km' arrival 188.8 (0.1% difference, computed not chosen).
- **Change:** Kept 10 km example; added 'in a simple model', no-advice sentence; arrival comparison stated as computed equality.
- **Files updated or checked:** 02 all files
- **Still open:** Aerodynamics reviewer

### F7 (slot 04): Tiny-world orbit: orbit as trajectory, toy world, 140 min tie, launch geometry, jump speed
- **Status:** QUALIFIED
- **Evidence checked:** orbit_checks.py: g=1.7e-4 g; v_circ 2.24 m/s; lap 140.0 min (ρ=2000), 84.3 min (ρ=5514); tilt 0.5° → 26.2 m, 5° → 261.5 m; 110% → +1,595 m; escape 3.17 m/s; friction-limited sprint 22 min (μ=1).
- **Change:** 'Orbit is a speed' → 'a path made by sideways speed'; lap time attached to 'circular orbit that just skims a smooth ball'; take-off speed marked as assumption twice; 1.5 km → 1.6 km; 'couple of coins' → 'few coins'.
- **Files updated or checked:** 04 all files; 05 checked
- **Still open:** Physicist; biomechanics source

### F8 (slot 06): Voyager Long: preserve 2024 repair; separate historical vs current; replace process language; qualify two days; recheck NASA
- **Status:** CONFIRMED
- **Evidence checked:** NASA blog 2024-04-22 reread (via fetch extract): 22.5 h one way, 45 h cycle; sent 18 April, reply 20 April; chip failure; code split and relocated. 2026: release 2026-11-19, blog 2026-11-18 (updated 2026-11-20); mission page updated 2026-11-23; newest narrative statement 2026-11-20.
- **Change:** Kept the 2024 story; separated 22.5 h (2024) from the 2026 light-day; 'I could not find a later update' removed; 'each test costs two days' → 'about forty-five hours per command and reply'; 2026 paragraph dated and attributed; link to 2023 stated as not claimed by NASA.
- **Files updated or checked:** 06 all files; 03 checked
- **Still open:** Production-day recheck

### F9 (slot 07): Lunar laser Short: instrument specifics, photon figures, mm meaning, mirrors-only implication
- **Status:** CONFIRMED
- **Evidence checked:** Murphy 2013 (targeted sections): APOLLO 115 mJ, 100 ps, 532 nm (~3e17 photons); record 5000-shot runs 0.96/1.52/3.15 detected photons per shot (Apollo 11/14/15); older stations ~0.002–0.01 per pulse; millimetre = statistical precision per normal point (<3 mm median); accuracy limited by modelling/reflectors; 2.56 s mean round trip, 2.38–2.71 s range. No average per-pulse figure found.
- **Change:** Instrument-specific numbers; record-run language; 'a few millimetres, approaching one'; explicit precision-not-accuracy sentence; removed 'most pulses bring back nothing' and first-echo date; no claim that mirrors are the only possible return.
- **Files updated or checked:** 07 all files
- **Still open:** LLR expert

### F10 (slot 10): Farthest human: Guinness record and definition; geometry; Munroe overlap; keep slot and offer distinct angle
- **Status:** CONFIRMED
- **Evidence checked:** Guinness page (read via fetch extract): 3,596.4 km from nearest living fellow human; Worden; 30 Jul–1 Aug 1971; no method given. Guinness April 2026 item is a different record (separation 419,656 km, Artemis II vs Tiangong crew). NASA: Artemis II passed Apollo 13's distance-from-Earth record on 6 April 2026. Apollo Flight Journal mirror: orbit ~110 km (95–122 km at times). 2R+h geometry appears in no source.
- **Change:** Record-holder, definition, our calculation and the Artemis II contrast are separate; geometry spoken as 'our own arithmetic' and conditional; Munroe overlap disclosed in packaging and status; slot kept; distinct-angle option (ISS vs Point Nemo) listed unresearched and not substituted.
- **Files updated or checked:** 10 all files
- **Still open:** Mission-report check; owner

## Check that the same issue is not left elsewhere
Searched all V2 files for: `five seconds`, `forty-six percent`, `46%`, `twelve hours exactly`, `lock to the Sun`, `does not flood`, `not with a jump`, `1.85`, `could not find a later update`, `I could not`, `two million times`: see `work/residual_phrase_scan.txt`.
