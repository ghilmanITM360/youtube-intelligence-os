# HIIT After 60 — V3 motion QA (review version)

Output: `HIIT_After_60_V3_REVIEW.mp4` (+ `_MOBILE_540x960.mp4`), built by `../project_v3.py` with `tools/anim_v3.py` and `tools/rig.py`.
V2 files and `project_v2.py` are unchanged.

## Defect (V2) and root cause
- The runner appeared to move only one leg. `sam-run-warm` has a single `legs` SVG part, so both legs were one rigid image rocking ±3.5° about the pelvis.
- The arms were rigid images swinging ±20°. No joint ever bent, so no believable gait was possible with more keyframes or more speed.

## V3 fix (underlying joint motion)
The legs and both arms are now redrawn every frame by `rig.RunRig`. They use the same stroke widths and colours as the SVG parts (outline 43/36 px #292A2D; trousers #45535C; sleeves #327C79; shoe and hand shapes taken from the SVG). The torso, head and face stay the original rasters.

**Gait, per leg (the two legs half a cycle apart):**
- Heel-first contact.
- Stance for 40% of the cycle: the contact point moves back linearly at ground speed, the foot rolls heel → sole → toe, and it plantarflexes 28° at toe-off.
- Flight phase each step.
- Swing: heel recovery behind, knee flexion up to 112°, then the leg swings through.
- Knee from two-bone IK: thigh 103 px, shin 88 px. The knee always bends forward.

**Body:** vertical oscillation of 6 px (asset), lowest at mid-stance and highest in flight. Smooth cosine, no cusp.

**Arms:** contralateral (each arm is forward while the opposite leg is forward). The swing runs from −18° to +34° and is biased forward. The elbow is bent 76–104°, more on the forward swing. The forward bias stops the near forearm folding across the belly on the back-swing, which was seen in the first loop test and fixed.

**Cadence and ground:**
- Cycle is 0.6 s (≈200 steps/min, interval effort). It slows to 0.55× before Sam stops at "However", so the existing V2 timing is kept.
- Ground marks under the path move at exactly the stance-foot speed (`ground_shift`). When Sam jogs in place, the planted foot therefore does not slide against the visible ground; it reads as a tracking shot.

**Biomechanics references:**
- Hamner, Seth & Delp 2010, J Biomech (PMC2973845): stance 0–40% of the gait cycle, toe-off at 40%, cycle ≈0.68 s.
- Seethapathi & Srinivasan 2019, eLife (PMC6424559): each running step has a stance and a flight phase.
- These set the duty factor and phase structure. The joint-angle magnitudes are an animator's choice, not measured values.

## Red opening headline bar
- **Text:** "HIIT AFTER 60" / "TOO INTENSE?" on two lines. The em dash became the line break so the text stays at 92 px Arial Black on mobile.
- **Look:** solid red (206,32,41), white text, x 60–1020 px, top at y 160 px (below the Shorts top UI). It does not cover the face, the captions (y ≥ 1330) or the interval bars (y ≥ 386).
- **Timing:** frames 0–105 (0–3.52 s, the end of the opening sentence and rating). It enters with a 6-frame fade and a 14 px settle, and exits with an 8-frame fade and lift. It never reappears.
- The first scene headline is hidden while the bar shows. The bar is an editorial hook, not a medical claim: the speaker discusses whether HIIT suits people over 60 and flags heart-disease caution.

## Checks run
**Rig self-check** (`python3 tools/rig.py`, `qa/RIG_CHECK_V3.json`, 240 samples per cycle):

| Check | Result |
|---|---|
| Stance ground-contact error | 0.000 px |
| Stance slip vs ground | 0.000 px |
| Thigh and shin length error | 0.000 px |
| Loop closure (pose at p=0 vs p=1) | 0.000 px |
| Max knee/ankle step per 1/240 cycle | 2.03 px |
| Knee flexion range | 40–112° (both legs) |

**Encoded-video temporal review** (decoded from the MP4 with `tools/motion_qa_v3.py`, not from stills of the timeline):
- `GAIT_PHASES_V3.png` / `qa/hiit_S1_PHASES.png`: 8 evenly spaced phases of one cycle (t=0.600–1.125 s), plus the frames either side of both foot contacts, both toe-offs and the loop boundary.
- `qa/hiit_S1_SEQUENCE.png`: every frame of two cycles (36 consecutive frames).
- `qa/hiit_S7_PHASES.png` / `_SEQUENCE.png`: the travelling run in S07, every frame of two cycles.
- **Observed:**
  - Both legs change pose every phase and alternate stance and swing.
  - There is a flight frame between contacts.
  - Contact frames −1/0/+1 land without a pop.
  - The loop-boundary frames are continuous.
  - Arms alternate with the opposite leg.
  - No detached limbs and no stretching (the lengths are constant by construction and checked).

**Before/after:** `MOTION_V2_V3.png` shows V2 (top) and V3 (bottom) at the same 8 timestamps.

**Render QA** (`RENDER_QA_V3.json`):

| Check | Result |
|---|---|
| Duration | 31.133 s, 1080×1920, 30 fps |
| Decode errors | none |
| A/V delta | 0.000 s |
| Peak | −0.9 dBFS |
| Blank frames | 0 |
| `CAPTIONS_V3.srt` | byte-identical to `CAPTIONS_V2.srt` |
| Narration | the documented V2 paced voice (`voice_v2_paced.wav`); source audio untouched |

- The only new large-frame-change flag is 0.1 s, the bar entrance. The other flags (14.0, 17.1–17.2, 21.9–22.1 s) are the planned clinic cut and camera moves, the same as V2.
- `CONTACT_SHEET_V3.png` covers the whole video at 1 s steps.

## Limits / still open
- "Watching" here means frame-by-frame inspection of consecutive decoded frames. No human has viewed it at playback speed yet; the owner should watch the MP4.
- The park path is a gentle wave while the contact line is straight (G=1285), the same as V2. Feet can sit a few px above or below the drawn wave at some x positions.
- The far (image-left) arm is hidden behind the torso during its forward swing, as the 3/4-front torso art implies.
- The pose change from running to standing at "However" (S03) is a cut on the word, as in V2. There is no transition animation.
- Human listening, clinical review (H4/H5/H6) and owner approval remain open from V2.
