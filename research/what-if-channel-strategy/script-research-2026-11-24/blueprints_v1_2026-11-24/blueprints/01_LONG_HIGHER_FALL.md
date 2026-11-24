# Blueprint 01 — LONG — Higher fall (Day 1)

**STATUS: BLUEPRINT READY FOR OWNER REVIEW** (research/blueprint status only, not permission to publish). The *equality* of landing speeds is robust to the drag value; the *numbers*, and everything above ~60 km, are model-only and need an aerodynamics reviewer (see I). SELF-REVIEW; no qualified reviewer has looked.

## A. IDENTITY
- **Calendar:** Day 1, Long (target 4–5 min).
- **Current working title:** "Would a Fall From Space Make You Hit the Ground Faster?"
- **Issue with it:** "faster" can mean *sooner* (a space fall takes ~6 min vs ~25 s) or *at a higher speed*. The calendar's audience question means speed at impact.
- **Proposed alternatives (calendar not edited):**
  1. "Do You Hit the Ground Any Faster If You Fall From Space Than From 1 km?" (keeps the question, names both heights)
  2. "1 km vs 100 km: Which Fall Hits Faster?" (shorter; does not state the answer)
  Avoid titles that print a km/h figure (V01-C03).
- **Central question:** If two people (hypothetically) start at rest — one 1 km up, one 100 km up — and nothing opens, which is moving faster just before the ground, and what happens in between?
- **One-sentence answer (qualified):** In our simplified model both land at nearly the same speed (within ~0.2 %; about 190 km/h with the Stratos-suit inputs, 164–204 km/h across drag assumptions) because air caps the speed — but the space fall spends minutes far faster (peak ≈ 3,500 km/h near 40 km, model-only) and slows down before landing; we say nothing about surviving it.
- **Viewer expects from the title:** a bigger speed from higher up.
- **Viewer actually learns:** why speed is capped by air; the difference between *peak speed* and *impact speed*; that "from space" changes the journey, not the landing speed (in this model); how real data (the 2012 Stratos jump) checks the idea.

## B. PRECISE SCENARIO
- **What changes (hypothetical, ASSUMPTION):** the person is released from rest at height H (1 m … 1 km … 100 km), zero horizontal speed, fixed belly-down posture, no parachute.
- **What stays normal:** a standard atmosphere, gravity decreasing slowly with height, windless air, sea-level ground.
- **Not this scenario:** a return from orbit (≈ 8 km/s sideways, V01-C12) — said on screen.
- **Model values (labelled):** CdA/m = 0.005891 m²/kg from the Stratos paper inputs (Cd 0.60, A 1.19 m², m 121.2 kg, V01-C14); other sets 164–204 km/h (V01-C03).
- **Known vs hypothetical:** known — drag law, density falls with height, the real Stratos peak 1,357.6 km/h at 28.8 km (V01-C14). Hypothetical — fixed posture, release at rest at 100 km, constant drag coefficient at Mach 3.

## C. DEPENDENCY MAP
| Needed | Source / calculation | Status / gap |
|---|---|---|
| Air density vs height | own USSA-1976 implementation; table above 86 km recalled | above 86 km LOW confidence (SRC-35) |
| Drag area per mass | Stratos paper (V01-C14) vs inherited fit (V01-C03) | posture/clothing/mass range needs reviewer |
| Equation of motion | `scripts/fall_model.py` (08 §1) | model, not observation |
| Real-data check | peak 377.1 m/s at 28,833 m, 50.0 s (V01-C05) | set B −3.3 %; set A fitted (not independent) |
| Slow-down threshold | V01-C10 (1.85 km, set B) | 5 % criterion is ours |
| Space edge | 100 km convention (V01-C11) | book + project note; re-check |

## D. CAUSE-AND-EFFECT STORY (beats)
| # | Cause / story question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook: two people, 1 km and 100 km, same rules — who hits harder? | rules of the hypothetical (rest, no chute, model) | viewer commits to a guess | "what does air do to a falling body?" | split frame, two altitude bars, a "guess" tally | V01-C11 |
| 2 | THEREFORE look at the simple case first: a 1 km fall | weight vs drag; speed stops growing at ~190 km/h | from 1 km: 191 km/h peak, 189 km/h landing (0.4 min); from 300 m: 177 km/h | "is that the limit for anyone?" | speed-vs-time curve flattening, a dashed "limit" line | V01-C02, C04, C16 |
| 3 | BUT start 10 km up — can you exceed the limit? | thinner air at height lets you go faster than the *ground* limit | peak ≈ 299 km/h at 8.8 km after ~20 s, then slows to 189 | "so the landing line is set by the ground air" | speed-vs-altitude curve with a hump, landing line marked | V01-C16, V01-C01, V01-C10 |
| 4 | THEREFORE test it on a real record: 39 km | model vs real peak | real peak 377.1 m/s (1,357.6 km/h) at 28.8 km; model 364.8 m/s (−3.3 %); landing ≈ 189 km/h after ~4.9 min | "what if we go to the edge of space?" | real-vs-model overlay; label which model number was fitted (A) and which was not (B) | V01-C05, C06, C14 |
| 5 | BUT from 100 km the air is almost absent for minutes | density ~2 million times lower at 100 km; speed builds until air thickens | model peak ≈ 3,585 km/h near 41 km after ~111 s, ~Mach 3; felt load ≈ 4.6 g; total ≈ 6 min — LOW confidence, extrapolated | "does the landing change?" | altitude strip with "air thickness" shading; "MODEL ONLY" tag on this segment | V01-C07, C08, C09 |
| 6 | THEREFORE compare the landing lines | all releases ≥ 3 km land within 0.5 km/h; 1 km within ~0.2 % | the landing line is flat across 1 m … 100 km in the model | "so did the title's 'faster' mean *speed* or *time*?" | all curves ending on one horizontal line; clock inset: 24 s vs 6 min | V01-C01, C02, C09 |
| 7 | BUT is that a real-world rule? Clarify what we did *not* model | released from rest; real return from orbit is ~8 km/s sideways; no heating, no survival claim | answer given with the range 164–204 km/h and the model/real labels | closing question (see F) | split card: "dropped from rest" vs "returning from orbit" | V01-C03, C12 |

*For a 3–5 min Long this is 7 beats of ~30–40 s. Do not repeat the ladder to stretch time.*

## E. NUMBERS INTO IMAGINABLE SCALE
| Number | Comparison (valid) | What the viewer sees | Qualification to show |
|---|---|---|---|
| ~190 km/h landing | "a fast racing car's speed" (~190 km/h; a plain car-speed comparison) | speed dial | value is a model range 164–204 km/h |
| 1,315 km/h peak (39 km) | "faster than sound" at that altitude (Mach 1.22 in the model; real Mach ≈ 1.25, V01-C14) | the speed dial passes a "speed of sound" mark | speed of sound depends on temperature (altitude) |
| ~3,585 km/h (100 km) | "about three times the speed of sound" (Mach 3.15) | dial and Mach tag | model-only; constant-Cd assumption |
| 6.0 min vs 0.4 min | length of a short song vs a short breath | two clocks | model times |
| density 265× thinner at 39 km | "like breathing through 265 times less air" is NOT used (misleading); show a density bar instead | bar chart | V02-C02 |

## F. HOOK, ESCALATION AND ENDING
- **Opening question and context (0–15 s):** "Two people let go from rest, one 1 km up, one 100 km up. Which one hits the ground harder?" State the rules in one breath.
- **First reason it isn't obvious:** energy suggests the high fall gains far more speed; air takes it back.
- **Escalation warranted?** Yes, in measured steps (1 km → 10 km → 39 km → 100 km), because each step changes the peak but not the landing line. Do not escalate beyond 100 km.
- **Direct answer:** "Within the model, no faster — the landing speed is set by the air near the ground, not by the height you fell from; the high fall just takes longer and has a scarier middle."
- **Possible dry-humor opportunity:** the ground "does not read the altimeter". (Original, not an xkcd line; keep optional.)
- **No-joke alternative:** end on the flat landing line: "Height changes the journey, not the last metre."

## G. VISUAL COMMUNICATION (text only)
- Beat 2: one speed-vs-time curve flattening; axes km/h and seconds; a labelled "drag = weight" line. Do not draw a person.
- Beat 3–5: speed-vs-altitude curves for 1, 10, 39, 100 km sharing one landing line; colour the model-only portion differently and tag it. Do not imply the 100 km curve is measured.
- Beat 4: overlay the real peak point (377.1 m/s, 28.8 km) as a marker, not a curve.
- Beat 6: clock inset 24 s vs 6 min so "faster" is not confused with "sooner".
- Must not depict: a fireball re-entry, injury, or survival; a spacesuit-brand lookalike; real footage.

## H. ORIGINALITY AND PRIOR ART
- **Closest prior art:** Munroe, *What If?* "Steak Drop" (printed pp.107-110): an object dropped from rest at 39 / 70 / 100 / 250 km slows to terminal speed; also "Free Fall" (p.195-196) and "Orbital Speed" (pp.187-190). The corresponding article number was not verified. No xkcd video with this premise among the 92 registry titles (title check only; no video watched).
- **Same in broad science:** drag caps speed; thin air lets speed overshoot.
- **Ours differs:** a person, a height ladder from 1 m to 100 km, peak-vs-impact as the central contrast, a real-data check from a peer-reviewed paper, a deliberate separation of "from rest" and "from orbit".
- **Do not copy:** the steak/food framing and jokes, the specific drop-height reveal sequence, the hypersonic-wind-tunnel aside, any drawings or phrasing.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- **Qualified/QUALIFIED:** equality of landing speeds (V01-C01/C02); Stratos inputs (V01-C14, SOURCE_READ_EXTRACT); real peak (V01-C05).
- **Open:** value of the landing speed (V01-C03); everything above ~60 km (V01-C07/C08); heating; Cd at Mach 3; posture stability; the 55 m/s book figure's source (V01-C13).
- **Highest-risk misunderstanding:** "you'd survive / it's safe" or "re-entry from orbit is the same". Mitigation: the "from rest vs from orbit" card and no survival claim.
- **Reviewer needed:** aerodynamics/atmospheric-flight expert (drag, atmosphere table, hypersonic extrapolation).
- **Publication blockers:** (1) reviewed drag range or an on-screen range; (2) check the density table above 86 km; (3) decide the number policy (title/thumbnail without a km/h figure); (4) re-open the Stratos paper PDF.
- **Confidence:** research 0.6 for the equality claim, 0.3 for the 100 km segment; story clarity high. (Subjective self-assessment, not audience data.)

## J. FORMAT AND DEPENDENCIES
- This is the parent of the Day-4 Short (blueprint 02). It must stand alone; it does not need the Short.
- If the Short is delayed nothing breaks; if this Long is delayed the Short can still publish (it repeats the terminal-speed idea) but loses the height ladder it points back to.
- No dependency on any other calendar video.
