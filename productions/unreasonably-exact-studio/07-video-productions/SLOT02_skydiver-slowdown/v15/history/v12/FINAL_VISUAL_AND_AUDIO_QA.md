# V12 final visual and audio QA

**Verdict:** V12 is a substantive motion-design re-edit of V11. It is still a **review cut, not ready to publish.**

**Blockers:**
1. All character, wrist and environment art is Codex **candidate** art, and V12's rig built from it is unapproved.
2. **No human has listened to the mix.**
3. Library SFX licences are not cleared. There are 15 library cue placements; a rights-clear mix is provided.
4. The owner has not confirmed the narration. The 78.2 s recording is the provisional review narration.

## Evidence

**Renders:** 3 full renders (49 s each) and 2 rounds of stills. Fixes made between rounds:
- the opening figure was invisible
- the ×30 lens slid off-screen during the push-in
- the trail labels overlapped the trail
- the reaction shot cut off the face
- freezedetect hit at 21.9 s on the "starts at rest" hold, so a slow creep was added

**Final file checks:**

| File | Picture | Audio | Decode | Freezes (n 0.0008, ≥ 0.75 s) | Loudness |
|---|---|---|---|---|---|
| `SKYDIVER_SLOWDOWN_V12.mp4` | 1080×1920, 24 fps, 1877 frames | AAC 78.2 s | no errors | 0 | −16.4 LUFS integrated, LRA 4.3 LU, peak −1.0 dBFS |
| `SKYDIVER_SLOWDOWN_V12_captions.mp4` | same frame count | AAC 78.2 s | no errors | — | — |

**Viewed:**
- Motion strips (16 frames each) in `qa/motion/`: open, lift, react, lens, trail, slow.
- Proof strips in `MOTION_DESIGN_PROOFS/`.
- Contact sheets `qa/stills_sheet_*.png`.
- Phone-size check `qa/phone_size_check.png`.
- V11-vs-V12 sheets against all 8 owner screenshots: `qa/before_after/`, overview `qa/V11_vs_V12_overview.png`.

**Not done:** real-time playback in a player. The film was checked by full decode, frame strips and stills only.

## Acceptance criteria (brief §22): my judgement from frames and strips

| V12 must not pass if… | Status |
|---|---|
| **Unnecessary text dominates** | Passes. 39 V11 items audited. Brand, banners, inset captions and footers removed; burned captions moved to an optional export plus SRT. |
| **Science looks like static slides** | Passes. No full-frame white cards. The lens, trail and graph build in place, and each held frame keeps a slow push. |
| **The character just bobs** | Mostly passes. Purposeful arm lift, glance, blink and snap-back in B2/C1/M1. Elsewhere the motion is still calm whole-body motion plus nods. |
| **Arm moves expose holes or discs** | Passes with a caveat: a small pale notch at the elbow top during the 0.3 s rotation (`RIG_AND_ATTACHMENT_QA.md`). No discs, no torso hole. |
| **Assets do not combine** | Mostly passes. The 2-frame dissolves (lift, glance) show brief doubled outlines, which read as a smear in motion. |
| **Unmotivated camera** | Passes. Every move is listed with its reason in `MOTION_DESIGN_RESEARCH.md`. |
| **Parallax lacks depth** | Passes. A world camera over a metre-scale mesh, depth-sorted clouds and a near-cloud wipe (`PARALLAX_LAYER_MAP.md`). |
| **Airflow is decorative** | Passes. Stated in the body frame ("air, relative to you"), with drawn-on paths, travelling markers and occlusion. Marked schematic. |
| **Arrows misrepresent the model** | Passes. Common scale, model-driven, and the lens is disclosed as ×30. |
| **Comparison uses misleading scales** | Passes. One trail, one interval, one scale (the V11 4 s / 15 s columns are gone). |
| **Speedometer interrupts unrelated scenes** | Passes. The floating inset is removed; the dial appears only on the wrist, in B3, N1 and O1. |
| **Meaning depends entirely on narration** | Mostly passes. The muted read is in `SCIENTIFIC_VISUAL_QA.md`. J1 and I1 lean on narration. |

## Known issues

- **Small labels:** 8–9.5 units, about 24–28 px at 1080 wide: "schematic", ruler labels, "a mark every 10 s · one scale", the "×30" badge. Readable on the phone-size sheet, but small.
- **R1 pull-back:** the figure becomes very small, by design (the "model" frame).
- **Gloves differ:** grey gloves in the three-quarter and back poses, bare hands in the side pose.
- **Low-altitude terrain** (O1, P1) is still large, plain fields.
- **A1 scale:** the figure and aircraft are drawn at an enlarged, illustrative scale. They are not to scale with the terrain.

## Audio

- V11 design kept and retimed to V12 (`tools/mix_v12.py`, `SOUND_DESIGN_CUE_SHEET.csv`):
  - wind dips only while the lens is open, under the trail and under the graph
  - new sleeve-rustle cues on both arm lifts
  - tick on each cut to the dial
  - gust under "did the air grow brakes?"
- Stems are in `audio/stems/`. `audio/V12_mix_rights_clear.wav` contains only the VO plus the generated wind and aircraft, with no library cues.
- **No listening review was performed. I cannot hear audio.** Loudness and decode checks are measurements, not listening. A person must listen on headphones for wind continuity, cue taste and level, narration clarity and the new rustles.
