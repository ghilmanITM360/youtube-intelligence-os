# Corpus Density Baseline

Recomputed directly from frozen Production Intelligence Brain v1.0.0
`01_master_data/` canonical rows. Prose DNA summaries were **not** used as the
source for any number here.

Brain unmodified. Read-only access only.

## Orientation split

Derived from `SOURCE_VIDEO_INDEX.csv` `ASPECT_RATIO` / `WIDTH`x`HEIGHT`.

| Class | Videos | Slugs |
|---|---|---|
| PORTRAIT | 8 | `how_long_could_you_drive_towards_the_sunset` (240:427), `what_if_all_visible_light_was_a_single_beam`, `Could you power your computer by typing?`, `earthquake-magnitude-shorts-wBLVmEZV2Oc`, `weird_and_worrying_questions`, `what_if_the_moon_were_made_of_protons`, `drained_oceans`, `worlds-largest-cities-what-if` |
| LANDSCAPE | 6 | `could_you_survive_nanosecond_sun`, `if_all_humans_died`, `if_toaster_in_freezer`, `what-if-earth-grew-1cm-every-second`, `what_if_earths_water_suddenly_disappear`, `what_would_a_magnitude_15_earthquake_be` |

Test A is 9:16, so **PORTRAIT is the governing baseline**. The all-14 figures
are recorded for context only.

## Aggregate ratios (the numbers the first pass used)

| Class | Shots | States | Motions | Shot-time | states/sec | motions/sec |
|---|---|---|---|---|---|---|
| ALL 14 | 200 | 581 | 438 | 2108.1s | 0.276 | 0.208 |
| PORTRAIT 8 | 72 | 301 | 230 | 748.7s | 0.402 | 0.307 |
| LANDSCAPE 6 | 128 | 280 | 208 | 1359.4s | 0.206 | 0.153 |

## Distribution — this is what the aggregate hides

Per-shot, portrait only (n=72):

| Metric | mean | median | p25 | p75 | **p90** | min | max |
|---|---|---|---|---|---|---|---|
| states/shot | 4.18 | 3.00 | 2.00 | 4.00 | 6.00 | 1 | 43 |
| motions/shot | 3.19 | 2.00 | 1.00 | 3.00 | 5.00 | 0 | 25 |
| shot duration (s) | 10.40 | 6.45 | 3.93 | 11.50 | 17.58 | 1.54 | 78.91 |
| **per-shot states/sec** | 0.48 | 0.38 | 0.26 | 0.50 | **0.67** | 0.07 | 5.58 |
| **per-shot motions/sec** | 0.31 | 0.27 | 0.19 | 0.35 | **0.45** | 0.00 | 3.11 |

State duration (portrait, n=301): mean 2.45s, median 2.00s, p25 1.00s, p90 4.79s, min 0.04s.
Motion duration (portrait, n=230): mean 1.93s, median 0.96s, p25 0.25s, p90 4.38s, min 0.04s.

Excluding the three single-shot portrait videos (which put an entire video in
one shot and so carry no shot-level signal), the multi-shot portrait subset
(n=68 shots) is nearly identical: states/shot median 3.00, motions/shot median
2.00, shot duration median 6.23s, per-shot states/sec median 0.38, per-shot
motions/sec median 0.27.

Per-video portrait:

| Video | Shots | States | Motions | Shot-time | st/shot | mo/shot | st/s | mo/s |
|---|---|---|---|---|---|---|---|---|
| Could you power your computer by typing? | 13 | 97 | 59 | 100.8 | 7.46 | 4.54 | 0.962 | 0.585 |
| drained_oceans | 17 | 30 | 29 | 109.2 | 1.76 | 1.71 | 0.275 | 0.266 |
| earthquake-magnitude-shorts | 1 | 23 | 25 | 66.0 | 23.00 | 25.00 | 0.349 | 0.379 |
| how_long_could_you_drive_towards_the_sunset | 14 | 48 | 34 | 129.9 | 3.43 | 2.43 | 0.370 | 0.262 |
| weird_and_worrying_questions | 1 | 27 | 25 | 47.5 | 27.00 | 25.00 | 0.569 | 0.527 |
| what_if_all_visible_light_was_a_single_beam | 15 | 33 | 18 | 123.9 | 2.20 | 1.20 | 0.266 | 0.145 |
| what_if_the_moon_were_made_of_protons | 9 | 32 | 24 | 88.1 | 3.56 | 2.67 | 0.363 | 0.272 |
| worlds-largest-cities-what-if | 2 | 11 | 16 | 83.3 | 5.50 | 8.00 | 0.132 | 0.192 |

Portrait state-density spans 0.132 → 0.962 states/sec **at video level**. This
is not a tight distribution with one correct value. It is a wide band, and the
densest member of it (`Could you power your computer by typing?`, 0.962 st/s)
is 3.5× the sparsest.

## Words per shot (measured, not assumed)

Counted by intersecting `MASTER_WORDS.START_SEC` with `MASTER_SHOTS`
start/end, multi-shot portrait subset (n=68 shots):

mean 32.3, **median 25.5**, p25 15, p75 45, min 7, max 118.

The first pass quoted "corpus 25–37 words/shot". The measured median is 25.5
and the interquartile range is 15–45. Test A's 26.0 words/shot sits essentially
**on the median**. That part of the first pass holds.

## Where the first-pass Test A actually sat

| Metric | Test A first pass | Portrait median | Portrait p75 | Portrait p90 | Verdict |
|---|---|---|---|---|---|
| words/shot | 26.0 | 25.5 | 45 | — | at median |
| shot duration (est) | 6.6s median | 6.45s | 11.50s | — | at median |
| states/sec | 0.665 | 0.38 | 0.50 | 0.67 | **at p90 — inside range** |
| motions/sec | 0.514 | 0.27 | 0.35 | 0.45 | **above p90 — outside the top decile** |

**Correction to the first-pass self-audit.** It reported density as "~1.6–1.7×
the corpus" against the aggregate portrait *mean* (0.402 / 0.307). Against the
per-shot *distribution*, state density sat exactly at the portrait 90th
percentile and motion density just above it. That is high-normal for a portrait
Short, not anomalous, and it is well inside the range set by the corpus's own
densest portrait video (0.962 st/s).

## Consequence for this revision

Density alone does not justify a single cut. Per §8, no target count was set.
Every change in `STATE_REVIEW.csv` and `MOTION_REVIEW.csv` is justified by a
function argument or a grammar-conformance argument, and the resulting counts
are an output, not a goal.

The one metric that *was* genuinely outside the corpus — motion density — is
reduced as a side effect of three motion findings (§ MOTION_REVIEW: M04 strike
duration, the A11/A12 coupling, the A13 draw→pop conversion), each of which
stands on its own evidence.

## Grammar distributions used in the review

Camera (`MASTER_STATES.CAMERA_STATE`, all 581): every well-formed value is
LOCKED/STATIC family (STATIC 105, "LOCKED; no observed pan/zoom/roll" 97,
LOCKED 79, LOCKED WIDE 70, LOCKED FULL FRAME 66, "STATIC, LOCKED" 48, "STATIC
LOCKED FRAME" 47, LOCKED CLOSE 6, LOCKED MEDIUM 3). Two rows mention PAN, both
in landscape map sequences. **Zero camera motion remains correct for Test A.**

Transitions (`MASTER_SHOTS`): TRANSITION_IN is hard-cut family in 80+37+8+4+2 =
131 of 200 rows. Two FADE rows exist, both video-open. **Hard-cut-only remains
correct.**

Motion relationship (`MASTER_MOTIONS.RELATIONSHIP`, 438): STATE_REPLACEMENT
230, SEQUENTIAL 131, SIMULTANEOUS_COUPLED 36, SIMULTANEOUS_INDEPENDENT 28,
PERSISTENT_LOOP 7, CAMERA_SUBJECT_COUPLED 3.

Speed, **portrait only** (230 motions): the single most common value is
`ONE-FRAME CHANGE` (28), then `FAST` (27), `INSTANT` (21), `QUICK, ~1S` (13),
`MODERATE REVEAL` (12), `FAST, ~1S` (9), `FAST, <1S` (8), plus 30 rows giving
an explicit frame count of 3–15 frames (0.125–0.625s). **In portrait, a change
is normally one frame or a handful of frames.** This is the single most
consequential distribution for the motion review.

Asset TYPE vocabulary (`MASTER_ASSETS.TYPE`, 448): GRAPHIC 146, ENVIRONMENT 91,
OBJECT 91, CHARACTER 50, TEXT_SYSTEM 21+7+3, AUDIO 13+1, TEXT 11, plus
minor compounds. There is **no** `MEDICAL_SYMBOL`, `CAFFEINE_SYMBOL`,
`CTA_ELEMENT` or `BACKGROUND` type anywhere in the corpus.

TRANSPARENT_BG: YES 252, NO 121 (+10 "NO (full-frame)"), N/A 47.

### Two precedent questions settled by direct lookup

**Red strike-through.** Real, 12 rows. Ten are in
`Could you power your computer by typing?` (`G07 red strike`, ACTION "Draw red
strike for line N", DIRECTION "left to right along fixed baseline/stroke"),
durations **0.125–0.208s, i.e. 3–5 frames**. Two more are earthquake-video
title strikes at 0.5s and 2.0s. So a red strike that draws left-to-right is
directly precedented — but at a handful of frames, not across a spoken phrase.

**Warning / caution triangle.** Directly precedented, contrary to the first
pass's "no medical or caution precedent" claim:
- `if_all_humans_died` G03 "warning markers and MAYDAY callout"; state F06.1
  "Multiple black warning triangles appear over wall map".
- `weird_and_worrying_questions` G08 "Reactor building ... with a
  radiation-triangle icon"; G10 plaque with "small radiation-triangle and bomb
  icons".
- `could_you_survive_nanosecond_sun` O13 "Travel advice warning placard";
  states F08.1/F08.3/F08.5 "red parenthetical warning near hand".

The corpus draws its warning triangles in **black**; Test A's muted red is the
guardrail-restrained variant and is a deliberate, stated departure.

**Arrows.** 34 motions touch an arrow. The overwhelming pattern is *appear /
pop / fade in*, not draw-along-path: "Reveal the stationary squirrel with its
upward-arrow caption" (0.042s, one-frame change), "**Reveal the six red curved
arrow strokes toward the book pages**" (0.292s, 7 frames), "Show the first
energy label and curved arrow" (0.042s, one-frame change), "Portal
label/arrow reveal" (0.250s), "Label and measurement arrow fade in" (0.400s).
The one directly analogous case — *curved* arrows — is a **group reveal in 7
frames**, not a path-following draw.
