# Asset plan: Version A (16:9), story "Two Mornings"

**Story** (`01_script/STORYLINES.md`, A): Margaret, 72, is the viewer.
- It opens on her dizzy blue dawn and ends on the same bedroom and the same camera angle, on a warm morning when she stands up steady, then walks in the garden with her granddaughter Lily.
- Her daughter Claire (50) takes her to the check-up.
- The notebook explainers are drawn in Margaret's own notebook on her kitchen table, and she appears in them as a sketch.

**Audience:** 50+ in the USA, UK, NZ and Australia. The setting is a neutral suburban home: no plugs, cars, signs or text (see the WORLD LOCK in `asset_prompts.md`).

**Methods:**
- **T** typography;
- **C** code-drawn (SVG/canvas/Three.js). All anatomy (heart, arteries, kidneys) is C, never generated;
- **R** user reference/footage;
- **G** generated still (`asset_prompts.md`, IDs CH/L/S/T).

**Styles:**
- **CC** Clinical Calm is her daytime home.
- **MC** Midnight Clinic is only the dawn (H01) and the night hallway (B02).
- **NB** Notebook is her notebook.

The shared palette is red `#D64545`, navy `#14213D` and off-white `#F4F1EC`. Highlighter `#F5D547` is used in NB only.

| Beat | Slot | What the viewer must understand | Style | Method | Asset IDs | Animation idea |
|---|---|---|---|---|---|---|
| 1 | H01 | "BP is falling. Good news?" | MC | G + T + C | S01 (frame 0), S02 | push into the cuffed arm; code digits tick DOWN on the blank monitor screen; "72" lands |
| 2 | H01 | "…but standing up makes the room spin" | MC | G + C | S03, S04, S05 | S03 rise; S04 rotates 8° and rack-blurs for 0.4 s; hit and hold on S05 |
| 3 | H01 | "Lower? Or a second look?" | MC | G + T | S06 | the two questions over S06 |
| 4 | H01 | "Control matters, so does avoiding drops" | MC→CC | T + C + G | S07 | split card over the blurred window |
| 5 | I01 | Who Dr. Rehan is | CC | G + T + R | S08, S09, S10 | the sweep reveals S08; title card over S09; iris through the S10 doorway into the doctor |
| 6 | DR 1 | Hyperlipidemia / INTERHEART labels | CC | T + G | S12 | side-wall pops; the map behind INTERHEART |
| 7 | J01 | BP = #2 cause after cholesterol; treat it | NB | G + C + T | S13, S11 | dive into the S13 notebook page; code ranking and artery drawn on it; S11 fridge on "should be treated" |
| 8 | DR 2 | Standing up → BP drops → dizzy → fall | CC | G + C | S14 | split card: Margaret's sketch rises; the code line dips under her |
| 9 | J02 | HYPER ✗ → HYPO ✓ | NB | G + C + T | S14, S15 ⚠️, S16 | match cut S03 photo → S14 sketch (T07 brush matte); highlighter on HYPO; S16 on the last question |
| 10 | DR 3 | Old belief → treatment helps (< 150) | CC | G + T | S17, S18, S19 | stamp drop on S17 with T05 dust; S19 parallax on "trial" |
| 11 | B01 | The "high" line moved | CC | G + C | S20 | the pencil line on her notebook becomes the code number line, 150 → 140 |
| 12 | DR 4 | 140/90 + other conditions → treat | CC | G + T | S21 | numbers typeset on the blank monitor |
| 13 | B02 | Heart risk vs fall risk | MC→CC | G + C | S22, S23, S24, S25 | the code balance: S24 (heart, her family) on one pan, S23 (rug, falls) on the other; it levels on "PERSON" as the light warms to S25 |
| 14 | DR 5 | Condition → medicine map (his pairs only) | CC | G + C + T | S26, S27b, S28 | S26 in the top strip; the rows build beside the S27b tablet groups |
| 15 | U01 ⚠️ | No single target | NB | G + C + T | S29, S30, S31 | three different sketched people (S30) |
| 16 | DR 6 | Recap: treat · adjust dose · other illnesses | CC | G + T | S32, S33 | ticks drawn on S33 |
| 17 | O01 | Not lower. Safer. + 3 warning signs | NB→CC | G + T | S34 (the mirror), S35, S23, S36, S37, S38, S39 | S34 mirrors S03 exactly (cross-dissolve the two frames); three signs as small inset callbacks; S38 full screen on PROTECTION; S39 still in the pause |
| 18 | DR 7 | Subscribe | CC | C + G | S40 | T04 light leak from S40 into the doctor |
| 19 | END | Decode Your Heart with Dr. Rehan | CC | T + G | S41 | ECG line draws over S41 |

Code-drawn (no images needed): the BP/ECG line, monitor digits, artery and heart (C only), balance scale, number line, ranking list, medicine map, bars, ticks, subscribe pill and end card.

Generated stills: 6 cast sheets, 5 location masters, 41 story shots and 10 FX plates (62 prompts). Until they arrive, the edit keeps its code-drawn placeholders in the same slots.
