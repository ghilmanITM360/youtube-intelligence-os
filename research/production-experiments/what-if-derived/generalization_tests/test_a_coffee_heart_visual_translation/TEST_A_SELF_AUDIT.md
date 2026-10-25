# Test A — Self Audit (blind first pass)

Verdicts are PASS / CONCERN / FAIL. No numerical scores. This is a
self-assessment of a blind first pass, not a test result.

---

### Did I over-animate?
**CONCERN.**
17 motions across 33.1s ESTIMATED = 0.51 motions/sec. The frozen corpus's 8
portrait videos measure 230 motions across 748s = 0.31 motions/sec. This plan
is **~1.6× the corpus motion density**.

Mitigating facts: every motion is the cheapest kind the corpus has (14 of 17
are one-frame pop-ons or one-frame replacements; only 3 are drawn strokes),
and every motion is a narration-anchored reveal that carries a distinct
spoken concept. There is no decorative motion, no camera movement, no
continuous animation, no loop, and no fade anywhere.

Unmitigated fact: the density is above the corpus and I chose it. If the
reviewer wants corpus-exact density, the honest cuts are A02 (fold `BAD?`
into F01.1, revealing the whole binary at once) and A12 (fold the left
figure's arc into A11), taking it to 15 motions / 0.45 per sec.

### Did I over-reveal? (states)
**CONCERN.**
22 states across 33.1s = 0.67 states/sec against a corpus portrait figure of
301 states / 748s = 0.40 states/sec — **~1.7× corpus density**.

The shot-level numbers, by contrast, sit right on the corpus: 5 shots for 130
words = 26 words/shot against a corpus range of 25–37, and a per-shot median
of 6.6s against a corpus portrait median of 6.45s. So the shot grammar
matches and the within-shot reveal grammar runs hot. Both facts are stated
rather than averaged away.

### Did I invent visual techniques absent from the brain?
**PASS.**
Every technique used appears in the corpus: one-frame pop-on reveal
(`MASTER_MOTIONS` SPEED=INSTANT, 69 rows — the single most common value),
progressive stroke draw (`ACTION`="ADD/DRAW", 5 rows; "Draw red strike for
line 1/2", 5 rows), grouped simultaneous reveal ("Droplet and temperature text
appear together"), whole-group removal/replacement (`STATE_REPLACEMENT`,
230/438), red as a rejection/annotation accent (real in corpus), hard cuts only
(186/186 boundaries at 0.0s), locked camera (89.8% of states).

Nothing here uses a fade, dissolve, wipe transition, scale-in, slide-in,
rotation, pulse, glow, parallax, speed ramp or camera move — all of which are
either absent from the corpus or explicitly ruled out by
`CAPCUT_PRODUCTION_SYSTEM.md`.

### Did I create unnecessary base images?
**CONCERN.**
5 base images for 5 shots. Each supports 4–5 states, which is the economy the
protocol asks for *within* a shot — but **no base image is reused across
shots**, so cross-shot base reuse is zero.

I considered and rejected two reuses: IMG01 for SH03 (rejected — SH03 needs
two facing figures and a smaller diagram; it is a different composition, not a
variant) and IMG02 for SH04 (rejected — no shared elements). The one genuine
reuse opportunity I *did* take is at the asset level, not the plate level:
O01 (mug) appears in 4 of 5 shots, C01 (Dr. Rehan) in 3, G01 (heart) in 2, G03
(red strike) in 2, T01/T02 in 2. That matches `ASSET_DNA.md`, where reuse is
tracked per asset and runs roughly 150/448 rows.

A reviewer could reasonably argue SH01 and SH03 should share one plate. I do
not think so, but the disagreement is legitimate and I am flagging it rather
than burying it.

### Did I map the narration concepts clearly?
**PASS.**
All 13 concepts named in the protocol have an explicit visual treatment:
coffee (O01, 4 shots) · heart (G01, SH01 + SH05) · good/bad binary (SH01, SH03)
· energy-drink comparison (SH02) · stronger stimulant (stroke counts, SH02) ·
caution (G05, SH02) · patient question (C02, SH03) · body response (SH04) ·
individual response (two figures, SH04) · blood pressure (SH05) · heart
response (SH05) · quantity (SH05) · CTA (SH05 F05.4).

None of them was given a redundant scene of its own — 13 concepts fit into 5
shots.

### Did I visually overstate any medical claim?
**PASS.**
No skull, death icon, flatline, exploding heart, heart attack, poison symbol,
emergency-red frame, ECG or arrhythmia trace appears anywhere. No blood-pressure
number, no caffeine milligram figure, no dose threshold, no diagnosis, no
disease label. The gauge dial has no numbers; the quantity icon has no count.
The energy-drink beat gets exactly one outline caution triangle, over one
object, with nothing above the mug — the asymmetry carries "higher caution",
which is as far as "a bit more dangerous" goes. Neither figure in SH04 is
marked as healthy or unwell; one simply reads higher than the other. Coffee is
never shown as universally good or universally bad — the video's own
conclusion is that the label is the wrong tool.

### Did I accidentally use external reference material?
**PASS.**
No xkcd or What If video, thumbnail, screenshot or storyboard was viewed,
searched for or referenced. All visual grammar came from the frozen release's
own files, listed in `TEST_A_MANIFEST.json`. One web search was performed, for
medical guardrails only, restricted to heart.org / fda.gov / nih.gov /
ncbi.nlm.nih.gov. Its output is used only to check that no visual overstates a
claim, is labelled as a guardrail rather than a production decision wherever it
appears, and changed no visual decision in this plan.

### Did I force I2V?
**PASS.**
`I2V_REQUIRED = 0`. All 17 motions are CapCut. The one motion with a plausible
case (A13, a coupled arrow-then-arcs progression) was evaluated and rejected
on stated grounds in `I2V_DECISIONS.md`, not waved away. No AI-video use case
was manufactured.

### Can every image actually be generated?
**CONCERN.**
Two real risks:

1. **IMG04's two identical figures.** Image models will not reliably produce
   two figures that are pixel-identical, and the entire argument of SH04 rests
   on them differing *only* in arc count. **Mitigation:** generate one figure
   on transparent background, then duplicate and place it twice in the editor.
   This is the safer build and should probably be the default.
2. **Exact x/y percentage placement.** Every frame description in this plan
   specifies bounding boxes to the percent, in the corpus's own convention.
   Generators will approximate these. **Mitigation:** treat the percentages as
   the compositing spec, not the generation spec — generate each element loose,
   then place it to spec in the editor. All 13 overlay assets already work this
   way; only the 5 full-frame plates depend on the generator's own layout, and
   each of those has ≤4 elements with large empty space, which is the easiest
   case for a generator to get roughly right.

Everything else is low-risk: simple black line art on white, few elements,
large negative space, no text requested anywhere.

### Can every animation actually be executed?
**CONCERN.**
14 of 17 are layer visibility switches at a marked frame — trivially
executable in any editor.

The 3 drawn strokes (A04, A09, A11 and the first half of A13) need a
progressive reveal along the stroke's own path. A04 and A09 are near-straight
diagonals and a standard linear mask animated across the frame will do it
correctly. **A11 and A13's arrows are curves, and CapCut's masks are linear
and shape-based, not path-following** — a linear wipe across a curved arrow
reveals it in a straight-edged sweep rather than along its length. Three
fallbacks, in order of preference:
1. Supply each arrow pre-split into 3–4 short segment PNGs and switch them on
   in consecutive frames — reads as a draw-on, stays fully deterministic.
2. Accept the linear wipe; on a ~0.4s reveal at phone size the difference is
   close to invisible.
3. Drop the draw entirely and pop the arrow on in one frame, matching the
   other 14 motions. This is the most corpus-faithful option of the three.

No animation in this plan requires a feature CapCut does not have.

### Overall
**FIRST_PASS_COMPLETE — AWAITING HUMAN REVIEW.**
Shot grammar, transition grammar, camera grammar, motion-type grammar, asset
grammar and text grammar all track the frozen corpus. Within-shot reveal and
motion density run ~1.6–1.7× the corpus and cross-shot base-image reuse is
zero — those are the two places a reviewer should push first. No claim is made
here that the brain generalises; that is the reviewer's call after comparison.
