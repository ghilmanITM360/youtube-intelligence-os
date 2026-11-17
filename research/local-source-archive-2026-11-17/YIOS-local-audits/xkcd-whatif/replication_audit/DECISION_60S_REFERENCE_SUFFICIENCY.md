# Decision: reference sufficiency and 60 s test (2026-11-14)

Labels: OBSERVED / INFERRED / UNKNOWN. Machine checks and human checks are kept separate.

## Verdicts (Roman Urdu)

1. **60-second test banana shuru karein?** Haan. Silent 60 s storyboard aur render shuru kar sakte hain. Reference data kaafi hai; koi naya video chahiye nahi.
2. **Full video ke liye approve?** Nahi. Ye approve nahi hoga jab tak insaan awaaz na sune, silent version dekh kar jawab na de, aur trampoline ka number kisi source se na mile.

## 1. Pilot v2, start to finish (OBSERVED from 12 frames, 0.5–11.7 s, `pilot/review_v2/SHEET_v2_12frames.png`)

Machine-extracted frames viewed by me. This is not the human silent review.
- 0.5 s: question line, empty trampoline. 3.4 s: Moss holds ball (release). 4.0 s: ball falls, two motion ticks. 4.6 s: first contact, mat dips. 5.0 s: deepest dip, ball in the mat. 5.4 s: ball rises, mat flat. 6.6 s: apex, red tick "1". 7.0 s: second contact. 8.2 s: tick "2". 9.4 s: ticks 1–3 plus "LESS EACH TIME". 10.4 s and 11.7 s: tick 4, shrug pose, rest.
- v1 problem (overlapping ticks 3–6, colliding labels): **fixed in labels**: ticks capped at 4, numbered, labels staggered. **Remaining**: ticks 3 and 4 are only about 7 px apart at 1080p. They are separate lines but tight at small size. Needs human eyes at 9.3–11.9 s.
- Weakness (OBSERVED): the first 3.4 s has only the empty trampoline and the question. The mat reads as a thin line on two posts. It dips and shows contact clearly.

## 2. Z_xJ40QXu7Q frames, now viewed (14 frames, `av_review/zx_frames/SHEET_Zx_14frames.png`)

| Time | Narration (ASR, machine) | Visible change | Consequence drawn |
|---|---|---|---|
| 22 s | (card, after 20 s question intro) | red title card | none |
| 34.5 s | "same thing happens with buildings" | hard cut to tall tower | scale |
| 53.5 s | "One is wind" | wind lines drawn around the tower | wind problem |
| 61.5 s | "elevators" | shaft, catapult joke | elevator limit |
| 100, 125, 150 s | "100 floors … stacked" | same diagram; counter FLOORS 100 → 1,000,000 → 100,000,000 vs GOAL 1,000,000,000 | escalation shown as a changing number |
| 153, 160, 168 s | "centrifugal forces" | swing ride, Earth with Fg/Fc arrows, GRAVITY WINS / CENTRIFUGAL WINS bar | cause as arrows and a ruler |
| 185, 201, 210, 222 s | "tear itself up by the roots … orbit near the moon … leave our galaxy" | switch to dark field; tower pulls the Moon; "~220 km/s" label; satellite flies off toward a galaxy | payoff on dark background with a speed label |

Findings: (a) the red title card is at about 20–22 s here, after the question narration, not at 2 s. The earlier "2.0 s opening card" measurement is NOT universal; Z_xJ40QXu7Q is a counterexample (OBSERVED). (b) Escalation is a **counter that changes on one diagram**: the same device as our red ticks. (c) Payoff switches to a dark field with one quantity label. Audio still NOT_LISTENED; timecodes are in `av_review/AUDIO_HUMAN_PASS_TIMECODES.csv`.

## 3. Do we need more reference videos? Answer: zero

| Question | Already answered by | Effect on 60 s |
|---|---|---|
| How does escalation look on screen? | Z_xJ40QXu7Q 100/125/150 s; 8fADp43wJwU last-light scene | use one changing counter across the 60 s, not new scenes |
| How does payoff look? | Z_xJ40QXu7Q 185–222 s | final 10 s on dark field with one quantity |
| Vertical recompose? | FkUNHhVbQ1Q vs 2p305nzcVQE | out of scope for the 60 s test |
| Pacing of a "typical" long? | Z_xJ40QXu7Q: 24 shots in 235 s (avg about 9.8 s per shot) | plan 5–7 beats in 60 s |
| Where hearing matters | needs a listener, not a video | human pass |
Proposing a sixth video would not close any gap above. Open gaps are listening, viewer comprehension and a trampoline source. Not video-dependent.

## 4. Trampoline physics check (web search, two searches this session)

- **Supported qualitatively (primary-ish):** a trampoline bed is elastic with damping (Park et al., PMC10747761 models elasticity and damping); a jumper has to add energy to keep height, so each unforced bounce is lower (PDH Online course model, ½ k y² with energy loss). General bounce theory: height after n bounces = e^(2n) h0 (arXiv 2202.03034, ball paper, not trampoline).
- **Not found:** any measured restitution or per-bounce height decay for a trampoline bed; no paper quantified bed hysteresis. A forum thread named air displacement as a loss, unconfirmed.
- **Illustrative in our pilot:** e = 0.65 (heights 74/31/13/6), dip depths 61/40/26/17/11/7, T = 0.6 s, mat shape. These are not measured. A bowling-ball impact would also likely be much heavier than a person for the mat. UNKNOWN: whether a real mat bottoms out.
- **Controlled observation:** not done. Cheapest close: record a ball (not bowling) on a real trampoline at 60 fps, measure heights. Needs a human with the object.

## 5. What is machine-checked vs human-pending

| Item | Status |
|---|---|
| Pilot decode, duration, 1920×1080, 24 fps, 288 frames, streams | PASS, machine (earlier pass, `pilot/PILOT_REPORT.md`) |
| Whisper timing of narration vs action | PASS, machine |
| Loudness −16.9 LUFS, peak −5.3 dBFS | machine |
| Frames of v2 seen by me | done (this session) |
| Silent comprehension by a viewer | **PENDING HUMAN** |
| Narrated audio listened to by a human | **PENDING HUMAN** |
| Five reference videos listened to | **PENDING HUMAN** |

## 6. Exact remaining checks before the 60 s test

1. Human watches `pilot/PILOT_12S_SILENT.mp4` with no sound and answers the questions in `pilot/PILOT_REPORT.md` (what is dropped, what happens, why each bounce shrinks). Eyes at **9.3–11.9 s** (ticks 3–4 legibility) and **0–3.4 s** (empty opening).
2. Human listens to `pilot/PILOT_12S_NARRATED.mp4`: **0.6 s** ("Drop a bowling ball"), **4.5–5.0 s** ("stretches"), **9.1–10.0 s** ("less each bounce"). Does the voice sound acceptable; is the sync natural?
3. Human listens to the reference windows in `av_review/AUDIO_HUMAN_PASS_TIMECODES.csv` (20 windows).
4. Approve or replace the macOS Samantha voice.
5. Close trampoline: either a source with measured bounce decay, or the 60 fps trampoline test; else label the 60 s numbers "illustrative".
6. Book: one page-image check of any figure we cite (OCR unproofread).
