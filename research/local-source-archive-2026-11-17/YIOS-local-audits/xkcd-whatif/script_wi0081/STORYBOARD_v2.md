# WI-0081 storyboard v2 (code-drawn SVG + HyperFrames, 1080x1920, 24 fps)

Replaces the Codex-PNG video v1. Timings are the real voiceover word times (`video/wordlist.json`), not the 68 s script estimate.

## What the real xkcd What If Shorts do (viewed: top 8 Shorts by views, frames 0-3 s, plus the repo's measured findings F1-F9)
- Frame 0 is already a finished picture of one concrete object or scene. No title card, no logo, no fade-in. (FKXV, aMsh, Uj10, wBLV, kNry, Ny9m)
- The question is spoken over that picture; the picture changes on the spoken words (a label pops on the noun, a thing appears on the verb). 1-frame pops, not fades.
- A persistent measuring anchor is common (FKXV: a ruler with a figure beside it), so every later number has something to sit on.
- A correction gag early: wBLV strikes "RICHTER SCALE" in red and writes the right name under it at ~1.8 s.
- 9:16 layout: board on top, narrator figure below, no end card. Line is thin, one weight, text is plain capitals. Labels are short (1-4 words).
- Density 20-30 events/min, median hold 1.4-2.8 s, no overshoot, no idle loops. Busy episodes accumulate labels on one persistent scene.
- Jokes are small: a reaction pose, a struck-through label, a "but" cut.

## Hook for this video (0-3.5 s)
| t | voice | picture |
|---|---|---|
| 0.0 | (frame 0) | Finished image: mug with a spoon already moving, thermometer at 20 C with a red "100 C" ceiling mark at the top of the tube. Narrator below holding a paper. The gap between 20 and 100 is the curiosity. |
| 0.6 | "boil" | "BOIL" pops (1 f) above the mug |
| 2.1 | "by stirring" | "BY STIRRING?" pops under it; swirl marks start |
| 4.3 | "no." | red strike across BOIL (1 f), narrator pose swap (palm up) |
| 5.6 | "spoon" | label "SPOON" + arrow |
| 6.2 | "try." | mercury rises 5 px, two red heat ticks pop |
Why it holds: the viewer sees a goal (100) and a start (20) before a word is spoken, then sees the verdict struck out on the exact word "no", then a hair of movement on "try": question, answer and a joke inside 6 s.

## Scenes
| # | time | voice | devices | physics note |
|---|---|---|---|---|
| S1 | 0-7.9 | hook above | pops, strike, stir swing | needle +hair only |
| S2 | 7.9-18.6 | energy, swirl rubs, friction -> heat, idea ok, amount | two opposite arrows (WATER/WATER), red friction ticks, check mark, circle on AMOUNT | viscous friction turns motion into heat |
| S3 | 18.6-27.8 | 1/4 L, 20 C, 100 C, 80 degrees, 84,000 J | jug, 20->100 scale, red bracket 80, big number pop | 0.25 kg x 4186 x 80 = 83.7 kJ |
| S4-S7 | 27.8-39.3 | 2 min, 700 W, 7 bulbs, microwave, horse | persistent watt ruler (0-1000 W, 1 px per W), stopwatch with 12 degree wedge, 7 bulbs stacked (100 W each), microwave at 700, horse at 746 | 84 kJ / 120 s = 700 W; 1 hp = 746 W |
| S8 | 39.3-45.7 | Niagara +0.1 C | tall fall, flat pool surface, cup, +0.1 C | g h / c = 0.12 C for 51 m |
| S9 | 45.7-54.6 | spoon under 1 W, 1/100 bulb, 700 needed vs under 1 | same ruler: dot at 0, one bulb, NEED 700 / GOT <1 | stirring power well under 1 W |
| S10 | 54.6-60.4 | warms a hair, cup leaks heat | SPOON IN small red arrow vs HEAT OUT wavy arrows, needle hair then stop | losses balance input |
| S11 | 60.4-66.1 | far faster, tens of thousands strokes/s | blurred spoon, speed marks, label | extreme case |
| S12 | 66.1-71.2 | cavitation, pressure drops, bubbles | label, bubbles pop one by one behind spoon | low pressure vapor, not heat |
| S13 | 71.2-75.0 | looks like boiling, but low pressure not heat | flame under mug struck in red, NOT HEAT | |
| S14 | 75.0-79.3 | splashing cools faster | droplets leave the cup, heat-out arrows widen | |
| S15 | 79.3-86.0 | tea: stir, dip, nothing | 3 mugs, 3 needles drop to nearly the same mark, tag ILLUSTRATIVE | |
| S16 | 86.0-93.1 | no, needle stays near room temperature | cut back to hook layout, red NO. pop on 88.3 | |
| S17 | 93.1-98.3 | sugar, job description | cube falls (gravity), sinks, dissolves; job card: DISSOLVE SUGAR checked, BOIL WATER struck | |

## Narrator
Original alien (mint head, black eyes, thin body), bottom-left on every scene, holding a paper. Pose swap on "no." and nowhere else.

## Verification plan
After each batch of scenes: HyperFrames snapshot at the key word times, review the contact sheet for overlap, readability at phone size, physics, and "AI slop" (floating objects, mismatched line weights, symmetric face-like marks, text overflow). Fix, re-snapshot, then render.
