# SC03 lightning: definitions, original source, and verdict (rework, 2026-11-23)

Verdict: **OPEN: definitions / original source required.** v1 said DISCREPANT; that is withdrawn (history kept in `07_SCIENCE_CLAIM_CHECKS_v1_2026-11-23.*`). Review type: same-model self-review; constants fetched via web search and one subagent page read; not an expert assessment. Code: `scripts/phase7_sc03_rework.py` -> `07_SC03_LIGHTNING_REWORK.json`.

## 1. What the video's sentence refers to
- Video `fs28lEq9smw` (V010, 2024-05-07), script paragraph 5 and ASR 36.9 s: "A typical lightning strike delivers enough energy to power a residential house for about two days." The preceding sentence (ASR ~28-32 s): "a lightning strike is over so fast that the total amount of energy delivered isn't THAT extreme". The same wording is repeated in the Short `_efsqO-4OoQ` (V031).
- So the quantity is **energy delivered by one strike**. The narration does not say whether that is the total flash energy, the share delivered to the ground, or electricity that could be captured and stored. The video also says harvesting is impractical, so it is not a claim about recoverable electricity.
- Its household assumption is not stated.

## 2. What the checked sources estimate
| Source | Quantity | Value | Defines ground share? |
|---|---|---|---|
| National Geographic quoting NOAA's MacGorman (page loaded) | energy per atmospheric discharge (flash) | 100 to 30,000 MJ; typical 1,000 to 5,000 MJ; 1,000 MJ = about 280 kWh | No. It says the return stroke is "responsible for most of the energy transferred to ground" but gives no share |
| Cooray (1997) via a search summary (not read in full) | energy dissipated by a four-stroke ground flash | about 950 MJ; range 200 to 7,000 MJ per flash in a charge-transfer summary | It is dissipation, not ground-delivered or recoverable energy |
| arXiv 2101.12361 | unknown | text could not be extracted | not used |
| What If #16 "Lightning" (original article page, loaded) | none | no energy figure at all (currents and timing only) | n/a, so this is not the source of the video's number |

## 3. Recomputation (all in `07_SC03_LIGHTNING_REWORK.json`)
- Household: EIA 2022 899 kWh/month = 29.6 kWh/day = 106 MJ/day (assumption: US average residential customer; a different household basis moves the answer proportionally; NatGeo's own 280 kWh = about 9 days implies about 31 kWh/day).
- "Two days" needs 213 MJ per strike.
- The video's own lines: about a million bolts = "about two atomic bombs" (2 x 63 TJ = 125.5 TJ, so 125.5 MJ per bolt) and = US consumption for five minutes (3,861 TWh/yr, so 132 TJ, 132 MJ per bolt). These two agree to 5%, and give 1.2 house-days per bolt at 106 MJ/day. "About two days" is 1.7x that. Within the video the three numbers are mutually consistent to a factor of 1.7.
- The sources' per-flash typical range 1,000 to 5,000 MJ is 9 to 47 house-days. The video's 126 to 213 MJ per strike is about 5 to 40 times below it.

## 4. Why this is not a proven error
1. A flash (several strokes, up to about half a second) is not the same as a "strike" in the video's phrasing, and total energy in a flash is not the same as energy delivered to the ground.
2. No checked source gives the delivered or recoverable share, so the 5 to 40x gap cannot be attributed to an error in the video rather than to a different definition.
3. The original source of the video's figure is unknown (What If #16 has none). The video authors' reference is needed.
4. The household load, the strikes-per-day count (about a million vs 45 flashes/s = 3.9 million per day, assuming roughly a quarter are cloud-to-ground, unchecked) and the "bolt" definition all enter.

## 5. Sub-check SC03B (not among the 10)
ASR 106.0 s and the script say two bombs "power a game console and TV for several million years". At 100 to 500 W, 125.5 TJ lasts about 8,000 to 40,000 years; "3 million years" needs 1.3 W. The Catatumbo line in the same video (about a century for 1 flash/2 s over a 10 h night) scales by 1e6/18,000 = 56x to about 5,600 years. So this is an internal tension of 2 to 3 orders of magnitude, **NOT_VERIFIED**: the original may use other power figures, and the captions and ASR agree, so it is not a transcription slip.

## 6. What is needed to close it
The video authors' source for "a typical strike delivers ... two days"; a paper giving energy delivered to ground per return stroke; and the household basis. Until then do not present the two-day figure as an error, and do not reuse it as a fact in a new script.

## 7. Visual representation
The viewed frame is a schematic house-and-lightning label comparison (07 coding, about t = 36.8 s); proportions are not measured against the numbers.
