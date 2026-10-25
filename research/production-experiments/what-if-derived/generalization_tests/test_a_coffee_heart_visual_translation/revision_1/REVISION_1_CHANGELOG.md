# Revision 1 Changelog

Blind first pass → forensic audit → keep/merge/remove/modify → this revision.

The first pass is experimental evidence and is preserved untouched in the parent
directory. All 18 of its locked SHA-256 hashes were verified before this review
began and again after it finished. Nothing in
`releases/production_intelligence_brain-v1.0.0/` was written to.

## Totals

| | First pass | Revision 1 | Δ |
|---|---|---|---|
| Shots | 5 | 5 | 0 |
| Base images | 5 | 5 | 0 |
| Visual states | 22 | 20 | −2 |
| Motions | 17 | 15 | −2 |
| Assets | 26 | 25 | −1 |
| Text overlays | 6 | 6 | 0 |
| Anchor words | 21 | 19 | −2 |
| Curved path-following draws | 2 | 0 | −2 |
| Multi-second strike draws | 2 | 0 | −2 |
| Operations with no deterministic build | 2 | 0 | −2 |
| I2V motions | 0 | 0 | 0 |
| Camera moves | 0 | 0 | 0 |
| Fades | 0 | 0 | 0 |
| Script words changed | 0 | 0 | 0 |

State decisions: KEEP 16 · MODIFY 3 · MERGE 2→1 · REMOVE 1.
Motion decisions: KEEP 10 · MODIFY 4 · MERGE 2→1 · REMOVE 1.

**No target count was set.** The counts above are what the per-item audit
produced. Two items were explicitly *kept against* the first pass's own
suggestion to cut them.

## Changes, largest first

### 1. REMOVED — the second red strike (state F03.2, motion A09)

The only outright removal. SH01 already teaches the viewer that a red strike
means *wrong*, on the same diagram. Repeating the identical gesture 54 words
later added no information, and it was superseded 7 words after that by the
total deletion of the diagram — so the beat ran strike, strike again, delete.

Removing it turns repetition into escalation: SH01 marks the model wrong, SH03
deletes it outright.

The corpus precedent that appeared to license the reuse does not: the ten
`Draw red strike for line N` rows in `Could you power your computer by typing?`
each strike a *different* line of a text block. That is enumeration, not
repetition of one mark on one object.

Knock-on: the deletion (now M09) inherits the `not` (w70) anchor instead of
`That's` (w77), which is the word that actually performs the rejection, and the
emptied frame's payoff hold grows from ~1.0s to ~2.6s ESTIMATED. Asset G03's
reuse count drops from 2 to 1.

### 2. MERGED — the left arrow and the left response arc (F04.1 + F04.2 → R04.1)

Two states two words apart carrying one idea: coffee reaches a body, the body
reads something. The corpus reveals coupled elements in one frame rather than
staggering them, and `respond` is the word that names the whole coupled idea.

The first-pass self-audit had proposed *cutting* A12 for density. That would
have deleted the left figure's reading and destroyed the two-figure comparison
the entire shot exists to make. Coupling keeps every visual element and removes
one unnecessary state boundary instead.

### 3. MODIFIED — both curved arrows now appear, they do not draw (M10, M11)

The first pass had both connector arrows tracing their own curves. Looking up
the brain's 34 arrow motions showed the corpus does not do this: the one
directly analogous row is *"Reveal the six red curved arrow strokes toward the
book pages"* at 0.292s / 7 frames — a group reveal — and two more curved-arrow
rows are one-frame changes at 0.042s.

This also eliminated the plan's only unbuildable operation. CapCut's masks are
linear and shape-based, not path-following, so a curved draw had no exact
implementation; the first pass flagged this and offered three fallbacks without
choosing one. The corpus-faithful answer and the buildable answer turned out to
be the same answer, and it was already among the fallbacks. It should have been
the primary choice.

Secondary benefit: with M10 and M11 both one-frame coupled pops, the left and
right readings are produced by identical mechanisms — which is what makes
"identical in every way except the number of arcs" true of the finished edit
and not only of the storyboard. M11's confidence rises from MEDIUM to HIGH.

### 4. MODIFIED — the strike stroke now draws in 4 frames, not across a phrase (M04)

Direction and mechanism were right; pacing was wrong. The first pass had the
stroke drawing from the word "wrong" through the word "question." Every one of
the corpus's ten drawn red strikes completes in **0.125–0.208s, i.e. 3–5
frames** (the SPEED column reads literally `3 frames / 0.125 s`). A 4-frame
draw reads as a decisive slash; a half-second draw reads as an animated
flourish. Measured off canonical rows, not a stylistic preference.

### 5. MODIFIED — the blood-pressure gauge icon is deleted (asset G10, motion M12)

Two independent problems. **Grammar:** a circular dial with a needle and a tick
mark is a stock infographic pictogram; nothing resembling an instrument dial
exists among the brain's 448 catalogued assets, so it was an import from
generic design rather than a grammar transfer. **Guardrail:** a needle resting
at a position on a dial reads as a *reading*, and a tick mark reads as a
*threshold*. The narration supplies neither — it says only that blood pressure
has something to do with it.

Directional alternatives were considered and rejected for the same reason: an
up-arrow beside BLOOD PRESSURE would assert that coffee raises it, which this
script never says. The top plate carries its text alone, set larger now that it
has the whole plate.

The heart and three-cup icons survive, because both are reuses of already
established shapes rather than new pictograms. Cost: the three plates are now
asymmetric. The symmetric alternative — drop all three icons — is recorded in
the self-audit and not applied.

### 6. MODIFIED — IMG04's two figures are one PNG duplicated, not a generated pair

The first-pass prompt asked an image model for "two stick figures that are
completely identical to each other". No image model reliably delivers that, and
the shot's argument collapses if the figures differ at all. The figures are
removed from the base plate; C03 is generated once as a transparent PNG and the
layer is duplicated with a changed X position. Identity is now structural.

### 7. KEPT AGAINST the first pass's own cut suggestion — the BAD? reveal (R01.2, M02)

The first-pass self-audit named A02 as a density cut. Merging it into R01.1
requires either revealing BAD? on the word "good" (a named concept fired four
words early) or holding GOOD? back to the word "bad" (four words late). Both
break word-onset anchoring, the single strongest measured rule in the brain
(581 STATE_CHANGE events, median offset 37 ms). Density is not a sufficient
reason to break the primary sync rule.

### 8. KEPT with its precedent status upgraded — the caution triangle (R02.3, M07)

This was the strongest MERGE candidate in the plan and the one the review
expected to cut. Direct lookup contradicted the first pass's claim that no
caution precedent exists:

- `if_all_humans_died` — asset G03 "warning markers and MAYDAY callout"; state
  F06.1 "Multiple black warning triangles appear over wall map".
- `weird_and_worrying_questions` — assets G08 and G10, radiation-triangle icons.
- `could_you_survive_nanosecond_sun` — asset O13 "Travel advice warning
  placard"; states F08.1/F08.3/F08.5 "red parenthetical warning near hand".

The corpus draws its warning triangles in black; the muted red here is a
deliberate, stated guardrail departure. "Dangerous" is also a distinct claim
from "stronger" with its own word onset nine words later, so merging would
attach caution to the wrong word.

### 9. Asset TYPE vocabulary conformed to the corpus

`BACKGROUND` → `ENVIRONMENT`, `MEDICAL_SYMBOL` → `GRAPHIC`,
`CAFFEINE_SYMBOL` → `GRAPHIC`, `CTA_ELEMENT` → `GRAPHIC`,
`TEXT_OVERLAY` → `TEXT_SYSTEM`. None of the five first-pass types exists among
the brain's 448 assets. The assets themselves are unchanged — only their
classification, so the plan reads consistently alongside the brain.

### 10. Two undocumented build problems written down

Neither shot SH03 nor SH05 can remove its diagram or plate column with a single
opacity switch, because the doctor shares the same base plate and would go with
it. The first pass never said how to build this. `REVISED_CAPCUT_BUILD.md` and
`EXECUTABILITY_CHECK.md` now specify splitting those two base images into a
base file plus a transparent removable-group file.

## Corrected claims from the first pass

| First pass said | Measurement says |
|---|---|
| "Density runs ~1.6–1.7× the corpus" | True against the aggregate portrait *mean* (0.402 / 0.307), misleading against the per-shot *distribution*: the first pass sat at the portrait p90 for states (0.665 vs 0.67) and just above it for motions (0.514 vs 0.45). High-normal, not anomalous. |
| "Corpus 25–37 words/shot" | Measured multi-shot portrait median is 25.5, IQR 15–45. Test A's 26.0 is on the median — the first pass's conclusion holds, its stated range was narrow. |
| "No medical or CTA visual precedent exists anywhere in the corpus" | Half right. No CTA precedent exists — confirmed, no corpus video ends on one. But warning/caution markers are directly precedented in three videos. |
| A02 and A12 named as candidate density cuts | Both rejected on evidence. Cutting A02 breaks word-onset anchoring; cutting A12 destroys the comparison the shot exists to make. |
| A13 "the closest I2V candidate, still rejected" | No longer applicable. It is now a plain one-frame group reveal. The closest candidate is M04, a straight wipe over a straight stroke — not close. |

## Unchanged and deliberately so

- The script, word for word.
- Five shots, five base images, five hard-cut boundaries, zero camera moves,
  zero fades, zero I2V.
- All five no-motion states, including SH03's 4.3-second ESTIMATED locked hold —
  the least motion-graphics-like moment in the plan, left completely alone.
- Every frame composition. Not one state's geometry, colour or layout changed.
  Every change in this revision is to *when* something happens, *whether* it
  happens as its own state, or *how* it is built — never to what a kept state
  looks like.
- All six text strings and their wording.
- The estimate basis: 3.93 words/sec, ESTIMATED, never mixed with measured
  values.
