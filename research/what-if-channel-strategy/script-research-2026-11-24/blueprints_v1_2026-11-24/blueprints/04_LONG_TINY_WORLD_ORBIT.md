# Blueprint 04 — LONG — One sideways jump into orbit (Day 10)

**STATUS: BLUEPRINT READY FOR OWNER REVIEW** (research/blueprint status only). It is a labelled toy model (uniform airless sphere); no real-world trajectory claim is made. SELF-REVIEW.

## A. IDENTITY
- **Calendar:** Day 10, Long (3–5 min).
- **Current working title:** "Could One Sideways Jump Put You in Orbit?"
- **Issue:** "a small world" and "sideways" are undefined; and a jump that starts on the ground has a ground-clearance problem.
- **Proposed alternatives:**
  1. "Could You Jump Into Orbit Around a Tiny Planet?" (Claude review's title; clear)
  2. "How Small Must a World Be for a Jump to Reach Orbit?" (puts the radius in the question)
- **Central question:** On a small, airless, uniform rocky world, could a single horizontal jump at the right speed put you in orbit — and what has to be true of the ground?
- **One-sentence answer (qualified):** Yes in the toy model: on a world about 4 km in radius (density 2,000 kg/m³) a horizontal jump at about 3 m/s is already orbital speed, but only a level, horizontal launch with a clear path works — any upward lean puts the orbit through the ground — and one lap (≈ 140 min) brings you back to where you started.
- **Viewer expects:** a Little-Prince-style tiny planet or a yes/no.
- **Viewer actually learns:** orbit is sideways speed, not height; how three speeds (grazing, orbit, escape) differ; the lap time depends only on density; why the ground matters.

## B. PRECISE SCENARIO
- **Changes (ASSUMPTIONS, labelled):** a uniform sphere of density 2,000 kg/m³, no rotation, no air, no other bodies, no terrain; a human can launch at about 3 m/s (V04-C09, unsourced).
- **Normal:** Newtonian gravity of a uniform sphere.
- **Exact conditions:** worked world R = 3,000 m (v_c = 2.243 m/s, v_esc = 3.172 m/s) and the 3 m/s world R = 4.01 km (V04-C01/C03).
- **Known vs hypothetical:** formulas are textbook (calculation); the world and the human launch speed are hypothetical.

## C. DEPENDENCY MAP
| Needed | Source | Gap |
|---|---|---|
| g = (4/3)πGρR; v_c = R√(4πGρ/3) | textbook formula, own calculation (V04-C01) | G recalled |
| Lap time T = √(3π/(Gρ)) | V04-C02 | none |
| Radius for a 3 m/s orbit | V04-C03 | 3 m/s is an assumption |
| Outcome ladder (lands / grazes / orbits / escapes) | V04-C04 | none |
| Upward-lean penalty | V04-C05 | none |
| Prior art on tiny dense asteroids | V04-C08 | — |

## D. CAUSE-AND-EFFECT STORY (beats)
| # | Cause / story question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook + rules: "a rocky ball a few km across, no air — a jump?" | define the toy world and say it is a model | rules card: size, density, no rotation, no air | "how weak is the gravity?" | the toy world next to a human silhouette, radius label in km | V04-C01 |
| 2 | THEREFORE feel the gravity | on the worked 3 km world g = 1.68 mm/s² = 0.017 % of Earth's (V04-C01) | a jump becomes a long hop: at 0.9 v_c, 45°, you land after ~69 min, 3.6 km away | "what if the hop never lands?" | hop arc with a clock and distance marker | V04-C03, C06 |
| 3 | BUT what does "orbit" mean? sideways speed so the ground curves away as fast as you fall | v_c = 2.24 m/s on the 3 km world — a brisk jog | circular speed in plain terms | "what happens just below / above that?" | falling-around-the-curve diagram, labels in m/s | V04-C01 |
| 4 | THEREFORE the speed ladder | 0.99 v_c lands; 1.00 grazes; 1.01 orbits (apoapsis +123 m); 1.3 v_c reaches 13 km high; 1.414 v_c escapes (3.17 m/s) | three outcomes from tiny changes in speed | "does direction matter?" | one picture with the paths for 0.99, 1.01, 1.3, 1.414 v_c | V04-C04 |
| 5 | BUT the ground is in the way | periapsis: 0.5° upward → 0.7 m below the surface; 5° → 63 m; any lean ploughs through the ground; ~1 m of clearance is all a bump can take | only a level horizontal launch works; terrain matters | "so what does one lap look like?" | the orbit ellipse dipping under the surface line, shaded below ground | V04-C05 |
| 6 | THEREFORE the lap | T depends only on density: 140 min at 2,000 kg/m³ (198 to 84 min across 1,000–5,514 kg/m³); size doesn't matter | you return to the launch spot ~2 h 20 min later | "what's the limit of this idea?" | stopwatch with the same lap time for two different-sized worlds | V04-C02, C07 |
| 7 | BUT limits & answer | rotation, tides, lumpy shape and other bodies change it; spin equal to v_c would shed material | qualified yes | closing | "model" card listing what was left out | V04-C10 |

## E. NUMBERS INTO IMAGINABLE SCALE
- 2.24 m/s ≈ 8 km/h — "a slow jog" (exact conversion 8.07 km/h).
- 140 min ≈ "a feature-length film" (comparison approximate).
- R = 4 km: ~8 km across — "a long walk across a small town" (approximate).
- g = 0.017 % of Earth (3 km world): a 70 kg person would "weigh" the equivalent of about 12 g (0.00017 × 70 kg ≈ 12 g) — arithmetic, label it as weight-equivalent, not mass.
Qualification to narrate: all values assume a uniform airless sphere.

## F. HOOK, ESCALATION AND ENDING
- Hook (0–20 s): "Could one jump put you in orbit?" Show the toy world and say the three rules.
- First reason it isn't obvious: orbit sounds like height; it is speed.
- Escalation: warranted in speed steps (0.99 → 1.414 v_c) only.
- Direct answer: "Yes on a world this small — if you jump level, fast enough, and the ground stays out of the way."
- Dry humor option: "orbit: the only trip where you come back from behind to find yourself standing where you left." (original; optional)
- No-joke alternative: finish on the equal lap times for two worlds.

## G. VISUAL COMMUNICATION (text only)
- Draw all paths in one frame in the same scale; label m/s, km, min.
- The sub-surface part of the ellipse must be visibly *under the ground line*.
- Must not depict: a real asteroid or moon as if it were this uniform ball; air or clouds; a person jumping upward at an angle for the orbit case.

## H. ORIGINALITY AND PRIOR ART
- **Closest prior art:** Munroe, *What If?* "Little Planet" (printed pp.102-106) and what-if.xkcd.com/68 (opened): a tiny superdense asteroid (1.75 m radius), escape ~5 m/s, orbital ~3 m/s, the "can you dunk" rule of thumb, running off a ramp, chaotic tidal orbit. No registry video title matches (titles only).
- **Same broad science:** circular and escape speed on a tiny body.
- **Ours differs:** realistic density, a radius ladder, the three-trajectory ladder, ground clearance (periapsis vs surface), lap time depending on density alone, and the "level launch" rule.
- **Do not copy:** the Little Prince framing, the basketball rule, the ramp idea, the Sonic aside, the rotating-merry-go-round comparison.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- Qualified: formulas; RK4 cross-check agreed to 0.2 s of a 12,000 s period (V04-C04).
- Open: the 3 m/s launch speed (assumption); real shape/rotation/tides.
- Highest-risk misunderstanding: that it would work on a real small asteroid or on any hop. Mitigation: model labels, "level launch" rule.
- Reviewer: a physicist for the model statement; biomechanics source for jump speeds.
- Blockers: label the model on screen; source human speed or present it as a variable.
- Confidence: research 0.8; story clarity medium-high (overlap with "Little Planet" needs a distinct opening).

## J. FORMAT AND DEPENDENCIES
- Parent of the Day-13 Phobos Short (blueprint 05). Must stand alone.
- If this Long is delayed, the Phobos Short can still publish (it repeats the idea of escape speed); if the Phobos Short is delayed, no effect.
- No other dependency.
