# Can You Boil Water Just by Stirring It? — 60 s Short, v2 (rebuilt on the channel's winning-Shorts model)

Supersedes `SCRIPT_WI0081_STIRRING_60S.md` (v1 kept, not deleted). Labels: OBSERVED = measured or viewed this session. INFERRED = my reading. UNKNOWN = not checked.
Status: DRAFT. Originality flag from v1 section 3e still stands (two close YouTube matches); not a cleared launch candidate.

## 0. What the winning Shorts do (OBSERVED, local ASR + ledgers)

Pool: 46 Shorts in `census/census.csv`, ranked by player views. Six top Shorts have local ASR: FKXVs4UteSc (7.8M, 67 s), wBLVmEZV2Oc (3.6M, 66 s), aMshLs0YCTQ (5.0M, 109 s), 19gun1mffWs (2.1M, 76 s), Uj10jGq2O8o (2.7M, 114 s), 2p305nzcVQE (3.7M, 106 s).

| Feature | Measured in the winners | v1 script | v2 script |
|---|---|---|---|
| Speech starts at | 0.0 s in all six; the question is the first sentence | 0.0 s | 0.0 s |
| Speech pace | 3.80, 4.06, 3.90, 3.81, 3.91, 4.09 words/s, nearly continuous | **2.15 w/s (129 words) — half speed, FAIL** | 3.9 w/s (230 words) |
| Words in first 60 s | 233 / 251 / 251 / 239 / 249 / 262 | 129 | 230 |
| Verdict early | "Yes! In fact…" (2.6 s); "In fact, there is no top or bottom" (12 s); "Not much." (17 s); "first nearly everyone would die. Then things would get interesting." (5.8 s) | at 49 s, **FAIL** | "Short answer: no." at 3 s |
| Body | a ladder: one number plus one familiar comparison per rung (cement truck → football team → cat → penny on a dog → feather → dust). wBLV is a magnitude 9 → 10 → 11 → 15 → 18 ladder on one ruler | one calculation chain, no ladder, **FAIL** | power ladder: bulb → microwave/horsepower → spoon |
| Anchor on screen | wBLV keeps a vertical ruler ("spine") on screen and swaps the drawing on it (globe → fractured globe → vapor ring) | none | vertical watt ruler stays all 60 s |
| Visual event rate | wBLV: 32 states in 66 s, one event about every 2 s; Shorts all-segments average about 24 events/min | 5 beats in 60 s, **FAIL** | 24 events (table below) |
| Title treatment | wBLV: all-caps title on the opening frame, wrong term struck in red at ~2 s | text line | chip "BOIL BY STIRRING?" at f ≤ 6 |
| Ending | FKXV: dry joke ("Sometimes it's nice not to destroy the world for a change"); wBLV, Uj10: final escalation, held; no end card in any Short | dry line | dry line, final hold, no end card |
| Length | winners 66–124 s; the Mars Short 106 s | 60 s | 60 s (about 6 s shorter than the shortest winner; keep for the test) |
| Format | 1080×1920 portrait, 24 fps, no opening card, no end card, narrator in lower third (SHT-002) | not stated | stated |

Limits: "winning" = top views, not a controlled retention measure. Six of the top 20 Shorts checked, not all twenty. Pace comes from machine ASR; nobody has listened. At least 38 of 40 Shorts in the earlier audit are re-sequenced excerpts of long videos, so these narrations are Randall Munroe's text. This model borrows structure and pace only; the wording below is ours.

## 1. Final voiceover (230 words, windows are my estimate from the machine read)

| Time | Voiceover |
|---|---|
| 0–4.5 s | "Could you boil a cup of water just by stirring it? Short answer: no. But the spoon does try." |
| 4.5–12 s | "Stirring really does add energy. The swirl rubs the water against itself, and that friction turns motion into heat. So the idea is sound. The problem is the amount." |
| 12–26.5 s | "Take a quarter liter of water at twenty degrees. Boiling is a hundred. Lifting it those eighty degrees takes about eighty-four thousand joules. Do that in two minutes, and you need seven hundred watts going in. That's seven old hundred-watt light bulbs, or about what a microwave draws to heat a mug. In horse terms, about one horsepower." |
| 26.5–36 s | "Now the spoon. A hard stir adds well under one watt: less than a hundredth of one of those bulbs. Seven hundred needed, under one delivered. The water warms a hair, until the cup leaks that heat away as fast as the spoon adds it." |
| 36–49 s | "So stir faster, far faster than any hand: tens of thousands of strokes a second, and the water cavitates. Pressure drops behind the spoon and vapor bubbles form. That looks like boiling, but it's low pressure, not heat. And the splashing spreads the water out, so it cools even faster." |
| 49–59 s | "So, ordinary spoon, open cup? No. The needle stays near room temperature, however hard you stir. A spoon is for dissolving sugar. Boiling is not in its job description." |

Read-aloud check (machine only, macOS Samantha): 230 words take 58.8 s at 235 wpm (3.9 w/s, inside the winners' 3.80–4.09), 61.5 s at 225 wpm. A human read and a voice decision are PENDING. The 125–140 word target in the first brief is dropped here on purpose: it would run at half the winners' pace.

## 2. Visual cue table (9:16, 1080×1920, 24 fps, 24 events)

Style per the project's style bible: black monoline on #F7F7F7, flat fills, faceless stick figure in the lower third, one red (#D7263D) only on heat or the answer, 1-frame pops, hard cuts only between scene classes, every label popping on the same frame as the state it names, no opening card, no end card.

| # | Time | What physically changes (event) | What it teaches |
|---|---|---|---|
| 1 | 0.00 | Chip "BOIL BY STIRRING?" pops at f ≤ 6 above a detailed mug, spoon and thermometer; needle at 20 °C | The three objects and the starting temperature |
| 2 | 2.0 | Red strike write-on across "BOIL" only, leaving "STIR"; stays | The answer is delivered early, as in wBLV |
| 3 | 3.0 | Spoon enters; 3 curved swirl lines pop | The spoon moves water |
| 4 | 5.0 | Two small red ticks leave the swirl and enter the water | Motion becomes heat |
| 5 | 8.0 | Needle moves one hair then holds | The gain is tiny |
| 6 | 10.5 | Vertical watt ruler pops at left ("W") and stays to the end | The anchor for every following number |
| 7 | 12.0 | Cut to a quarter-liter jug beside the 20 → 100 °C ruler, gap in red | The 80-degree gap |
| 8 | 14.5 | Label "84 kJ" pops in the gap | The energy, as one number |
| 9 | 17.5 | Clock "2 min" pops beside it | The time |
| 10 | 19.5 | Red circle pops on the ruler at 700 | The needed power |
| 11 | 21.0 | Seven bulb drawings pop one per tick, ruler mark "100" under the first | 7 × 100 W = 700 |
| 12 | 23.5 | A microwave drawing replaces the bulbs, same height on the ruler | Same power, familiar object |
| 13 | 25.5 | Horse silhouette (our own drawing) pops at the same height | "about one horsepower" |
| 14 | 26.5 | Cut back to the mug; spoon blur | Return to the actual tool |
| 15 | 28.0 | On the ruler a tiny dot appears near 0, a long way under 700 | "well under one watt" |
| 16 | 30.5 | Dot is circled, bulb pops beside it (the dot is under 1/100 of it) | The size gap |
| 17 | 33.5 | Two arrows on the mug: tiny red arrow "spoon in", equal arrow "heat out" from the open top; needle rises a hair, stops | The competing effects balance |
| 18 | 36.0 | Spoon blurs and doubles speed marks; label "tens of thousands / s" | The extreme-speed case |
| 19 | 39.0 | Bubbles pop along the spoon's trailing edge; label "low pressure" (the bubbles appear on this frame) | Cavitation is a pressure effect |
| 20 | 42.5 | Label "NOT BOILING" on the bubbles, a crossed-out flame under them | Bubbles are not heating |
| 21 | 44.5 | Splash droplets leave the mug; the "heat out" arrow widens | Splashing cools faster |
| 22 | 49.0 | Cut to the opening mug; needle at about 20 °C | The answer on the same needle |
| 23 | 52.5 | Sugar cubes pop and dissolve at the spoon (state change) | What the spoon is actually for |
| 24 | 56.0–59.0 | Hold; no card, no CTA; last frame is the held mug | Winner pattern: held final state, no end card |

Legibility: numbers on screen equal the narrated numbers (84 kJ, 2 min, 700, 100). Check at 320 px width. Keep the "illustrative" tag on any exaggerated bubble drawing. The horse drawing must be our own and must not copy the book's horse panel or its blender joke.

## 3. Match checklist against the model (self-check; not a 100% guarantee)

PASS (measured above): speech at 0.0 s, question first, pace 3.9 w/s, 230 words in 59 s, verdict by 3 s, ladder body, persistent ruler, 24 events, chip at f ≤ 6, no cards, held final state, dry last line, 9:16.
NOT MATCHED, by decision: length is 60 s, shorter than every checked winner (66–124 s).
UNKNOWN: whether the winners are winners because of this structure (no retention data); whether the ladder reads at phone size without a human watch; whether the pace sounds natural to a listener.

## 4. Checked numbers and sources (carried from v1, one change)

- Q = mcΔT = 0.250 kg × 4186 J/(kg·K) × 80 K = 83,720 J ≈ 84 kJ; over 120 s = 698 W. Book p. 263 (page image viewed) gives 700 W and a microwave at 700–1100 W.
- 7 bulbs × 100 W = 700 W (arithmetic; bulb wattage is the nominal rating).
- 1 mechanical horsepower = 745.7 W ([Wikipedia: Horsepower / Power](https://en.wikipedia.org/wiki/Horsepower)). 700 W is "about" one horsepower, as the book says on p. 265.
- Specific heat of water 4.184 J/(g·°C): [Wikipedia: Calorie](https://en.wikipedia.org/wiki/Calorie), [LibreTexts](https://chem.libretexts.org/Courses/University_of_Toronto/Chemistry:_Physical_Principles/05:_Thermochemistry/5.05:_Calorimetry). No NIST table value retrieved.
- "Well under one watt": the book's 10⁻⁷ W (its own estimate, unverified) and my 7 mW drag estimate (rough) both sit far under 1 W, so the narration uses neither number.
- "The water warms a hair, until the cup leaks that heat away": steady-state balance, INFERRED from the book's p. 265 statement that over-slow heating is cancelled by cooling.
- "Less than a hundredth of one of those bulbs": under 1 W vs 100 W; true for both estimates.
- Cavitation = vapor forms where pressure drops below vapor pressure, not from heat: [TU Delft](https://ocw.tudelft.nl/wp-content/uploads/Chapter-2_01.pdf), [Caltech](https://calteches.library.caltech.edu/699/2/Bubbles.pdf). "Tens of thousands of strokes a second" is from the book (p. 265) only.
- Book pages: pdf 277–280 = printed 262–265. Page images 278 and 280 viewed; formula, footnotes and cavitation passage match.

## 5. Originality (unchanged from v1)

Searched 2026-11-14. Close matches: [The Action Lab, 2017, 2.6M views](https://www.youtube.com/watch?v=GjcOobt9Ef8) and [Coffee & Chaos Short, 2026-11-12](https://www.youtube.com/shorts/u8U5RTXGvfo). I read titles and descriptions only. v2 differences: the watt ladder with bulbs and horsepower, the early verdict, and "cavitation is not boiling". Human decision needed.

## 6. Pending human checks

- Silent watch of the Short at phone size: do events 15–17 and 19–21 read without sound?
- Listen to the 230-word read at natural pace; approve or replace the voice.
- Watch the two matched videos for payoff overlap.
- Proofread the page-278 formula against the image before any figure goes on screen.
