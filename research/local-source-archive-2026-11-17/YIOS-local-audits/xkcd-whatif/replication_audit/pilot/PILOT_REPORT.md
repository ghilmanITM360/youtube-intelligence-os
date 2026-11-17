# Pilot 12 s — "What if you drop a bowling ball on a trampoline?" (original, 2026-11-14)
## Files
- `PILOT_12S_SILENT.mp4` (video only) · `PILOT_12S_NARRATED.mp4` · `PILOT_TIMELINE.csv` · `PILOT_12S_SILENT_physics.json` · `render_pilot.py` · `keyframes_v2.png` · rejected v1: `PILOT_12S_SILENT_v1_rejected.mp4` + `keyframes_v1_rejected.png`.
## Storyboard (setup → action → visible consequence)
1. **Setup 0–3.5 s** — question text pops f3; trampoline f12; "Moss" (original character: round head, teal beanie with pom-pom, single-stroke body) f18 holds a bowling ball at arm's length over the mat; ball f24; dashed START tick at ball-bottom height f54. Hold.
2. **Action 3.5–5.2 s** — Moss opens hand (pose swap P2, 8 f), ball falls (1.1 s), then rests the mat: it dips 61 units, ball rides down and up (contact 4.6–5.2 s). Moss: chin-hand watch pose.
3. **Consequence 5.2–12 s** — ball leaves the mat, peaks 74 units high (red tick 1, f142), lands, dips less (40), peaks 31 (tick 2), then 13, 6; label "LESS EACH TIME" f222; shrug pose f250; ball settles on a slightly sagging mat.
Poses: P1 hold, P2 release, P3 watch, P4 shrug. Props: bowling ball (rigid, never squashes; 3 finger holes), trampoline (mat deforms, posts static), START/apex ticks.
## Physics
Model: free fall (g stylised so the 174-unit fall takes 1.1 s) → spring contact (half-sine, T 0.6 s, depth ∝ impact speed, d = vT/π) → leaves at e·v, e = 0.65; apex heights 74/31/13/6 = e²ⁿ·H. Mechanism checked against: general bounce physics — coefficient of restitution < 1, energy lost in deformation/vibration ([Modeling the bounce of a gas-filled ball, arXiv:2202.03034](https://arxiv.org/pdf/2202.03034)). Trampoline-specific claim (mat stores elastic energy, hysteresis/damping returns less) is standard mechanics but **I found no trampoline-specific primary source this pass** → INFERRED. Numbers (e = 0.65, 61-unit dip) are illustrative, not measured; contact time is not scaled to a real bowling ball. Real heavy ball on a real mat would sag much deeper relative to ball size; shown dip is a stylisation.
## Narration (local test voice)
Text: "Drop a bowling ball on a trampoline. The mat stretches, soaks up the energy, and gives back a little less each bounce." Voice: **macOS `say`, Samantha — local test voice, not an approved production voice**, three chunks delayed to 0.6 / 3.9 / 8.0 s and mixed to 12 s.
Machine timing check (whisper-cli large-v3-turbo-q5_0 on the mix, word offsets approximate): "stretches" 4.56–5.0 s vs first contact 4.6 s ✓; "less each bounce" 9.12–10.04 s vs apex 3 at 9.06 s and label at 9.25 s ✓; transcript round-trip exact. **Final audio was NOT listened to by anyone.**
## Machine checks (ffprobe / ffmpeg decode)
| | SILENT | NARRATED |
|---|---|---|
| duration | 12.000 s | 12.000 s |
| video | h264 1920x1080 24/1, 288 frames | same (stream copy), 288 frames |
| audio | none (by design) | AAC 48 kHz stereo, −16.9 LUFS, peak −5.3 dBFS |
| decode errors | 0 | 0 |
SHA-256 silent `637346982046…a891e4`, narrated `82d500ec533c…20e7`. Frames re-viewed by me: v1 12-frame sheet, v2 frame at 11.7 s; v2 12-frame sheet exists but only frame 11.7 s was re-checked individually. Opening/interaction/payoff were inspected in v1 sheet.
## Problem found → fix
v1: apex ticks 3–6 overlapped into one red smear, no numbers, so "less each time" was not countable. Diagnosed with toaster COP diagram + last-light rust scene (quantity label on the changed object). v2: drop ticks <5 units, number ticks 1–4 (staggered), label moved earlier (9.25 s) and enlarged question text. v2 only partially re-inspected (see above).
## Human review — NOT COLLECTED
No viewer was available. Ask a viewer to watch the silent file once and answer: (1) what moved or changed? (2) what caused it? (3) what did the red lines mean? Save their answers as `HUMAN_REVIEW_SILENT.md`. Machine checks above do not substitute.
## Known weaknesses (honest)
Flat-looking static first 3.5 s; character has no personality beyond a hat; no sound design beyond voice; trampoline is a bare table-like frame (no springs/legs depth); ball x is close to the left post; pop timing/linear grammar copied from the references, not tuned by a human.
## Verdict (Roman Urdu)
Pilot **60-second test ke liye abhi poori tarah ready nahi, lekin "conditional haan"** hai. Machine checks sab pass hain (12 s, 1920x1080, 24 fps, 0 decode error, awaaz cue se match). Magar teen cheezein baqi hain: (1) kisi insaan ne silent version dekh kar nahi bataya ke kya hua aur kyun, (2) awaaz ab tak kisi ne suni nahi aur ye sirf local test voice hai, (3) physics ka trampoline-specific hissa sirf general bounce physics se verified hai. In teeno ke baad hi 60 s test shuru karein; 60 s mein 4–5 beats chahiye, jabke ye pilot sirf ek beat hai.
