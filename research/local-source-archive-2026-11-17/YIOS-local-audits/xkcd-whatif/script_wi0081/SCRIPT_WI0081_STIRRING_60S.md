# Can You Boil Water Just by Stirring It? — 60 s script (WI-0081)

Status: DRAFT for human read-through. Not a launch candidate until the originality flag in section 3 is resolved.
Labels: OBSERVED = read or measured this session. INFERRED = my reading. UNKNOWN = not checked.

## 1. Final voiceover (129 words)

| Time | Voiceover |
|---|---|
| 0–6 s | "Could you boil a mug of water just by stirring it?" (11 words) |
| 6–17 s | "Stirring really does add energy. The spoon drives the water into a swirl, and friction inside the swirl turns that motion into heat." (23) |
| 17–32 s | "A quarter liter of water, heated from twenty degrees to the boiling point, needs about eighty-four kilojoules. Do that in two minutes and you need roughly seven hundred watts. That's microwave territory." (32) |
| 32–49 s | "Your spoon adds well under a watt, while the open mug keeps leaking heat. Spin the spoon tens of thousands of times a second and the water cavitates: vapor bubbles from low pressure, not heat. Then the splashing cools it." (40) |
| 49–60 s | "So, an ordinary spoon and an open cup? No. The water stays near room temperature. As a heater, a spoon is decorative." (22) |

Read-aloud check (OBSERVED, machine only): macOS Samantha at 165 wpm speaks the five lines in 2.5 / 7.1 / 11.3 / 12.2 / 7.6 s = 40.6 s. Every line fits inside its window with 3–5 s spare for the visuals to land. A human at about 140 wpm would take about 55 s. A human read-through is still PENDING.

## 2. Visual cue table

| Beat | What physically changes on screen | What it teaches |
|---|---|---|
| 0–6 | Plain mug on a table, spoon beside it, thermometer standing in the water at 20 °C. The question appears as a text line. | The three objects the whole video uses. Starting temperature is on screen. |
| 6–17 | Spoon enters and circles. Water swirl drawn as 3–4 curved lines. Small red ticks leave the spoon and enter the water. The thermometer needle creeps up one hair, then stops. | Motion becomes heat, but the gain is visibly tiny. |
| 17–32 | Beside the mug a ruler shows 20 → 100 °C with the 80-degree gap in red. A label counter steps: 250 ml → 84 kJ → 2 min → ≈700 W. A small microwave drawing appears next to the 700 W label. | The target is a number. 700 W is a familiar object's power. |
| 32–49 | Same diagram, two arrows. A thin red arrow "spoon in" (nearly invisible) and a wide arrow "heat out" rising off the open top. Spoon blurs; bubbles appear along its path, labelled "vapor, low pressure". Splash droplets leave the mug, the heat-out arrow widens. | Two competing flows on one diagram. Bubbles are labelled so they are not confused with boiling. |
| 49–60 | Back to the opening mug and thermometer. Needle at about 20 °C. Final text line: "Open cup, ordinary spoon: no." Spoon rests across the rim. | The answer, shown by the same needle that started the video. |

Production notes for the editor: use one red colour for heat arrows. Keep the thermometer at one position in every shot. Show "illustrative" on any exaggerated bubble drawing.

## 3. Source and originality notes

### 3a. Source Notes — book WI-0081 "Stirring Tea" (my summary, not the book's text)
Pages: pdf 277–280 = printed 262–265. Checked against rendered page images (`pages/p-277…p-280.png` in this folder; I viewed 278 and 280). The OCR is unproofread; the images confirm the formula, the footnotes and the cavitation passage.
- **Setup (p. 262):** a reader asks whether stirring faster could boil a cup. The book answers "No". Temperature is molecular motion, so stirring does add energy, and that energy ends up as heat.
- **Power requirement (p. 263):** the book writes 1 cup × water heat capacity × (100 °C − 20 °C) / 2 min = 700 W. It says "nearly boiling". Footnote 2 says vaporizing needs a lot more energy on top. A microwave uses 700–1100 W.
- **Scale check (p. 263):** the book says water falling over Niagara warms by about 0.12 °C and a cup would have to fall from above the atmosphere to boil.
- **Stirring power (p. 264):** the book estimates vigorous stirring adds about a ten-millionth of a watt, based on industrial mixer reports. This is the book's estimate.
- **Cooling observations (p. 264):** the book cites a Stack Exchange user's measurements: stirring, dipping and leaving tea alone cool it at about the same rate, with dipping slightly faster. Stirring may bring hot water to the surface, disturb the air and warm the mug. Footnote 5 notes mixing can slow heat loss from the sea surface, so hurricanes weaken.
- **Limit (p. 265):** 700 W is about a horsepower. A longer heating time lowers the power but then cooling cancels the gain. At tens of thousands of stirs per second the tea would cavitate, stirring becomes ineffective, spray raises surface area and the tea cools to room temperature in seconds. Footnote 6: some enclosed blenders do warm their contents.

### 3b. Checked calculation (OBSERVED, python)
- Q = m·c·ΔT = 0.250 kg × 4186 J/(kg·K) × 80 K = 83,720 J ≈ 84 kJ.
- 83,720 J / 120 s = 698 W. With c = 4.18 the result is 83.6 kJ.
- With a US cup (236.6 ml) the result is 79 kJ and 660 W. The book's 700 W matches a metric 250 ml cup, so say "a quarter liter".
- 84 kJ only reaches the boiling point at 1 atm. Turning it to steam would need about 2.26 MJ per kg, about 27 times more (INFERRED from the book's footnote 2 plus standard latent heat; I did not source the latent-heat number this session). The script says "to the boiling point" for that reason.
- Water fall to heat 80 K: h = cΔT/g ≈ 34 km. Niagara (about 51 m, my figure) gives 0.12 °C, which reproduces the book's number.

### 3c. Where my check disagrees with the book — UNRESOLVED
The book's 10⁻⁷ W stirring power is NOT independently verified. A rough drag estimate of mine (spoon area 5 cm², 0.3 m/s, ½ρC_dAv³) gives about 7 mW, five orders of magnitude higher. Both are far below 700 W, so the conclusion does not change: even at 7 mW, 84 kJ would take about 138 days, and the cup would cool long before. Because the numbers disagree, **the narration says "well under a watt" and does not use the ten-millionth figure.** Treat the 7 mW as an order-of-magnitude guess.

### 3d. Independent science references
- Specific heat of water: 4.184 J/(g·°C) is the textbook value tied to the thermochemical calorie definition [Wikipedia: Calorie](https://en.wikipedia.org/wiki/Calorie), [LibreTexts calorimetry](https://chem.libretexts.org/Courses/University_of_Toronto/Chemistry:_Physical_Principles/05:_Thermochemistry/5.05:_Calorimetry). A listing of 4182 J/kg·K at 20 °C [amesweb](https://amesweb.info/Materials/Specific-Heat-Capacity-of-Water.aspx) and 4187 at 15 °C ([Wikipedia: Specific heat capacity](https://en.wikipedia.org/wiki/Specific_heat_capacity)) agree to 0.2 %. A NIST table value was NOT retrieved; the NIST search returned only the Osborne et al. measurement paper abstract ([NIST JRes](https://nvlpubs.nist.gov/nistpubs/jres/23/jresv23n2p197_A1b.pdf)).
- Cavitation = vapor bubbles forming when local pressure falls below vapor pressure, not from heating: [TU Delft chapter 2](https://ocw.tudelft.nl/wp-content/uploads/Chapter-2_01.pdf), [Caltech Engineering & Science](https://calteches.library.caltech.edu/699/2/Bubbles.pdf). The tens-of-thousands-of-stirs figure comes from the book only.

### 3e. Originality check (Chrome, YouTube, searched 2026-11-14)
Project index: WI-0081 `NOT_ON_CHANNEL` (title/script match only).

| Search | Closest results | Same question? | Same payoff? |
|---|---|---|---|
| "can you boil water by stirring" | [The Action Lab, "Can You Boil Water Just By Mixing it Really Fast?"](https://www.youtube.com/watch?v=GjcOobt9Ef8) — 8:50, published 2017-11-20, 2.6M views. Description: tests hand mixing, then a Blendtech blender, asks if friction can boil water. | Yes, nearly | UNKNOWN: I did not watch it. Experiment, not a calculation. |
| same | [Coffee & Chaos Short, "What if you stirred your coffee until it boiled?"](https://www.youtube.com/shorts/u8U5RTXGvfo) — published **2026-11-12**. Description (truncated by YouTube): stirring adds a little heat, the mug leaks it faster, a spoon spinning fast enough to … | Yes | LIKELY same (heat in vs heat out, extreme-speed limit). **CLOSE MATCH.** I did not watch it. |
| same | Shorts "Can you shake water to a boil?" ([m844wqFLiaA](https://www.youtube.com/shorts/m844wqFLiaA)); "Pick a Way to Boil Water Faster: Salt, Lid or Stirring?" ([nhYuLmNN2SE](https://www.youtube.com/shorts/nhYuLmNN2SE)) | Related | No |
| "stirring tea until it boils" | Same Coffee & Chaos Short; the rest are tea recipes or the leaves-in-the-middle effect | Only the Short | — |
| "can a spoon heat water to boiling" | Spoon heat-conduction and hot-spoon clips; no stirring-to-boil answer | No | — |

**Flag:** the question is already answered on YouTube twice (Action Lab long, 2017; Coffee & Chaos Short, 2 days before this check). Neither is an illustrated What-If answer, but the premise and the heat-in-vs-heat-out payoff overlap. Not cleared as a launch candidate. Possible differentiators: the 84 kJ → 700 W ladder, the "well under a watt" gap, and the cavitation-is-not-boiling point. Human decision needed. Also unresolved: the book's text is xkcd's; the script is in our own words, and visuals must not copy the book's horse drawing or its blender joke.

### 3f. Pending human checks
- Watch the Coffee & Chaos Short and the Action Lab video to confirm payoff overlap (I only read titles and descriptions).
- Human read-aloud of the 129 words at natural pace; voice not approved.
- Silent comprehension test of the cue table's beat 32–49 (two arrows plus bubbles in one frame is the densest).
- Proofread the page-278 formula once more before putting any number on screen; the OCR garbled it, the page image is correct.
