# V12 rig and attachment QA

**Status:** candidate art, V12-built rig. Codex's V12 package is a rest partition only. Its own QA says the shoulder and elbow motion tests fail and the pivots are `null`. V12 does not animate that partition freely. It builds a **constrained rig**: only the moves that were tested below.

Build: `tools/build_rig.py` writes `assets/v12rig/` and `qa/rig/`.

## What the rig does

| Channel | Method | Range used | Source pixels |
|---|---|---|---|
| Rest | Codex partition reassembled (body + upper arm + forearm + hand + head) | — | Codex `character/side/*`. Max channel difference vs the V11 master is 8/255 (anti-aliasing at cut edges). |
| Head nod | Codex head rotated about the neck (1352,452), over a fixed neck/collar underlay (head pixels below y=330) | ±1° | Codex `side_head.png` |
| Blink | Eyelid drawn in code over the eye (1472,291): skin-tone lid plus a curved ink line, 0.11 s | rest head only | code |
| Glance | Head replaced by the glance head cut from `sources/glance_generation.png` with Codex's mask (dilated 9 px, feathered 2 px). 2–4 frame cross-fade. | 0/1 | Codex generated pose, registered (legs alpha IoU 0.985 vs master) |
| Arm lift | Forearm + hand rotate 0→22° about the **underside of the elbow** (1335,668) over 7 frames. The upper arm is drawn on top, so the top of the forearm tucks under the sleeve. Two small swept-sleeve patches (r 30 / 26 px) close the top notch and the bottom slit. Then a 2-frame dissolve into `raised_generation.png`, which holds. | 0→1, eased in about 0.42 s, no overshoot | Codex partition + Codex raised pose (registered, legs IoU 0.985) |

**Pivots were chosen by visual test, not certified.** The 22° end angle is the best fit to the raised drawing; at that pivot the alpha IoU is 0.54. `assets/v12rig/RIG.json` records each pivot as "chosen by visual test in V12, not certified by Codex".

## Tests run (images in `qa/rig/`)

| Test | Result |
|---|---|
| **Rest** (`lift_sequence.png` frame 0) | Matches the master. |
| **Elbow at 22°** (`elbow_zoom_22deg.png`, 2×) | Fold stays closed, no disc. **A small pale notch remains at the top of the elbow, about 8 px on the 1920 canvas**, and there is slight stray ink at the bottom point. On screen the body is 300–330 units wide, so this is about 4 px at 1080 width, and it is visible only during the roughly 0.3 s rotation. The hold frame is the clean generated pose. |
| **First pivot tried, elbow centre (1330,620)** | **Failed:** a gap opened under the elbow. The sweep fill was jaggy. Rejected. |
| **Head ±4°** | **Failed:** a light seam at the collar and a notch behind the helmet. Range cut to ±1°. At ±1.5° a faint collar seam is still visible at 2× zoom. |
| **Glance cross-fade** | Clean head. During the 2–4 fade frames there is a brief double helmet outline, which reads as a quick head turn in motion (`qa/motion/lift.png`, `react.png`). |
| **Lift dissolve** | The 2 dissolve frames show a double forearm and hand, which reads as a smear in motion. 4 frames was too ghosty, so it was cut to 2. |
| **Pack attachment** | The pack is part of the body layer and never moves relative to the harness. |
| **Identity** | Side, three-quarter and back are the same costume, recoloured in V11. **The three-quarter and back poses still have grey gloves.** Codex's bare-hand candidates are not used because their hand/cuff seams are unverified. |
| **Wrist** | The device is the same composite V11 wrist art in every close-up. Codex V12 wrist layers are not used because of hard internal cuts. The needle and scale are drawn in code (`tools/instrument11.py`). |

## Where it is used

- **B2 (8.3 s):** lift + glance as "somehow you're slowing down" begins. The push-in goes toward the wrist, then cuts to the dial close-up.
- **C1 (11.2 s):** "Wait, what?": the head snaps up from the wrist, two blinks, the arm returns.
- **M1 (54.4 s):** lift + glance again, flash-cut into first person.
- **Elsewhere:** nod ±1° and blinks about every 2–8 s (B1, D1, model scenes).

## Still needed from Codex (exact components)

1. **A painted near-elbow fold at 10°, 15° and 22°.** These are replacement sleeve drawings on the 1920×819 canvas that close the top notch without code patches.
2. **A neck/collar overlap drawn under the head**, so the head can turn ±4° without a seam.
3. **Clean bare hands for three-quarter and back**, with verified cuff seams, so the gloves match.
4. **A clean layered wrist without hard internal cuts**, only if the strap or housing needs to move.

**Ready-to-send brief with reference images:** [codex_request/CODEX_V13_ART_BRIEF.md](codex_request/CODEX_V13_ART_BRIEF.md) (zipped as `CODEX_V13_ART_REQUEST.zip`).
