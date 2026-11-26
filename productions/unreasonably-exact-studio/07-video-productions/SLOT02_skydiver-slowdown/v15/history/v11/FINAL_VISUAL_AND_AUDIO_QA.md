# V11 final visual and audio QA

**Verdict:** V11 fixes the owner-flagged defects that code and composition can fix. It is still a **review cut, not publication-ready.**

**Blockers:**
1. All V11 character, wrist and landscape art is Codex **candidate** art. It is not approved, and my repairs to it also need approval.
2. There is **no limb animation.** The poses are whole drawings because no layered, registered V11 rig exists.
3. **No human has listened to the mix.**
4. Library SFX licences are not cleared. 13 library cue placements; the rights-clear mix is provided.
5. The narration choice is unconfirmed by the owner. The 78.2 s recording is used as the review-cut narration only.

## Evidence (what was actually done)

- **Owner screenshots:** all 9 viewed and mapped to V10 shots (`V10_SCREENSHOT_DEFECT_AUDIT.md`).
- **Codex V11 package:** every image was viewed (`qa/codex_v11_sheet.png`). The handoff, ARTWORK_QA, manifest, pivot map and before/after were read.
- **Renders:** four full renders. Fixes went in between each, prompted by the stills, the motion strips and the contact sheet.
  - Render 1 crashed: a single-mark column divided by zero. It was fixed, and the self-check now draws every 8th frame.
  - Render 2 showed freezes at 50.75 s and 67.96 s. A slow push was added on both cards.
  - Render 3 showed a black strip in the opening frame. It was fixed.
- **Final file check, `SKYDIVER_SLOWDOWN_V11.mp4`:**
  - 1080×1920 at 24 fps, 1877 frames; AAC audio 78.2 s
  - full decode with no errors
  - freezedetect (noise 0.0008, ≥0.75 s): **0 hits**
  - EBU R128: −16.4 LUFS, LRA 4.4 LU, peak −1.1 dBFS
- **Contact sheet** every 1.5 s (`qa/V11_contact_1p5s.png`), viewed.
- **Motion strips, viewed:** `qa/motion/wrist.png`, `air.png`, `cross.png`, `end_wrist.png`, `recap.png`. Problems found in them and fixed:
  - the speed arrow overlapped the hands
  - the "moving down" arrow sat on the boots
  - flow lines were drawn over the body
  - the arm faded out as a translucent ghost
- **Storyboard:** 90 panels at 1080×1920. A phone-size (360×640) check of 10 rebuilt-sequence panels is in `qa/phone_size_check.png`.
- **Before/after:** owner screenshot next to V11 frames for each flagged time, in `qa/before_after/`.
- **Not done this round:** browser playback of V11. V10 was played in the browser; V11 was checked by full decode only.

## The 17 passes

| # | Pass | Finding | Status |
|---|---|---|---|
| 1 | Character anatomy | Whole-pose drawings: continuous shoulders, elbows and knees. Boot caps repaired. | Fixed (candidate art) |
| 2 | Joint seams | No joints exist to open. No discs anywhere in the film. | Fixed |
| 3 | Pack attachment | Harness straps drawn over the pack in all views; no floating gap | Fixed |
| 4 | Character movement | Calm roll, bob and breathing; camera push-ins; gaze by head replacement. **No arm or hand activity.** | Partial |
| 5 | Instrument design | Graduated SLOW→FAST band, 9 ticks, "↓ DOWN SPEED", tapered needle. No longer a 4-mark clock. | Fixed (face in code; art candidate) |
| 6 | Wrist attachment | The device is shown on a wrist in every appearance. Strap and hand in frame. | Fixed |
| 7 | Instrument perspective/scale | Real third-person and first-person art; no squashed fake side view. The device keeps its size on the wrist; only the camera zooms. No three-quarter or side face view of the dial. | Mostly fixed |
| 8 | Needle continuity | Zero at the reset, rising, max at STATE 2 (43.6 s), falling after 47.7 s, > 0 once falling. Asserted in `--check`. | Fixed |
| 9 | Camera direction | Push-ins motivated by the glance. POV tilt from wrist to ground. Circular reveal from the tip ring into the zoom card. | Done |
| 10 | Falling-motion readability | Terrain parallax, relative-air specks, wisps, flow lines, marching dashes on DOWN arrows | Done |
| 11 | Terrain | Checkerboard removed: irregular jittered fields in the Codex landscape palette, merged fields, forest clumps, winding roads, crop rows close up. Codex landscape image in A1. | Fixed. At low altitude (O1/P1) the fields are large and plain. |
| 12 | Airflow | Frame stated first ("you: moving down"), then streamline-shaped lines around the body with upward chevrons, only near the body, drawn behind it | Fixed (schematic, labelled) |
| 13 | Physics | Model rerun; progression A–G shown; no V8 exaggeration; ×30 zoom labelled | Done |
| 14 | Scientific comprehension | One idea per beat. K1/Q2 split into steps. Speed and net force use distinct glyphs. Two-phase equal-time diagram. | Done. The two columns use different scales (stated). |
| 15 | Typography | Captions 15 units (45 px). Labels 9.5–13 units. Footnotes raised to 9.5 units; 7.5-unit text removed. **The wrist-inset caption is 8.5 units.** | Mostly |
| 16 | Audio | V10 design kept and retimed. Wind drops under every card (measured: −32 dB in the K1 body shot vs −40 dB on the zoom card, −31 dB in POV). New soft reveal cues at 42.0 s and 67.22 s. Instrument tick at 10.18 s and 55.40 s. | **Measured only, not listened** |
| 17 | Overall storytelling | The muted contact-sheet read follows the narration (see `SCIENTIFIC_VISUAL_QA.md`) | Improved |

## Acceptance criteria (brief §18)

| Criterion | V11 |
|---|---|
| Joints look like mechanical discs | **No** |
| Boots or limbs disconnected | **No** (boot caps painted out) |
| Pack floats above the torso | **No** |
| Three-quarter looks like a different person | Mostly no: same costume after recolour. Gloves differ; slight smile. |
| Instrument looks like an unmarked clock | **No** |
| Instrument floats independently of the wrist | **No** |
| Long empty strap fills the screen | **No** |
| Camera distorts body or equipment | No distortion found in the strips |
| Science excessively crowded | No: K1/Q2 split into steps |
| Terrain looks like a procedural checkerboard | **No** (still procedural, but irregular) |
| Speed vs net force indistinguishable | No: dashed blue DOWN vs violet double shaft UP |

These are my judgements from viewing the frames and strips. **The owner's own review is the acceptance test.**

## Audio statement

**No listening review was performed. I cannot hear audio.** Levels and cue placement come from measurement and timeline placement only. A person must listen on headphones for wind continuity, aircraft ambience, instrument ticks, transitions, reveal cues, narration clarity and balance.

`audio/V11_mix_rights_clear.wav` contains only the VO plus the generated wind and aircraft, and excludes every library cue.
