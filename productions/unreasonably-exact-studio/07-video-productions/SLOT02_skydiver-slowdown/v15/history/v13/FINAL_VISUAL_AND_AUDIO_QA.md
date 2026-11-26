# V13 final visual and audio QA

**Verdict:** V13 fixes the V12 opening regression and rebuilds the air and force explanations, but it is a **review cut, not ready to publish**.

**Blockers before publishing:**
1. **All art is candidate.** Codex's art and my V12/V13 rig are unapproved.
2. **No listening review.** Nobody has listened to the mix; I cannot hear audio.
3. **SFX not licensed.** 18 library SFX placements are not licence-cleared. A rights-clear mix exists.
4. **Narration unconfirmed.** The narration is the owner's provisional 78.2 s recording.
5. **No playback in a player.** The film has not been played in a real-time player (see below).

## File checks (final files)

| File | Picture | Audio | Decode errors | Freezes (n 0.0008, ≥ 0.75 s) | Loudness |
|---|---|---|---|---|---|
| `SKYDIVER_SLOWDOWN_V13.mp4` | 1080×1920, 24 fps, 1877 frames | AAC 78.2 s | 0 | 0 | −16.4 LUFS, LRA 4.4 LU, true peak −1.1 dBFS |
| `SKYDIVER_SLOWDOWN_V13_captions.mp4` | 1080×1920, 1877 frames | AAC 78.2 s | 0 | — | — |
| `SKYDIVER_SLOWDOWN_V13.srt` | 48 cues, 0 overlaps | | | | |

**Physics self-check:** pass. The model is byte-identical to V12.

**Earlier versions untouched:** the V9–V12 MP4 modification times are unchanged (11:19, 12:41, 13:50, 14:49).

## Real-time playback: not done

- **Chrome was not reachable.** The Claude in Chrome extension reported "not connected".
- **The in-app browser can't open local files.** It cannot open `file://` paths or local servers.
- **Nothing was uploaded to get around this,** because the brief says not to.

What was done instead:
- **Real-time-rate decode.** `ffmpeg -re` decoded the caption version in 78 s for 78.2 s of film, with no errors. This shows the file plays at real time; it is not a human viewing.
- **Consecutive frames** at three critical moments (`qa/consecutive_frames_critical.png`):
  - 2.9 s: the approach and the cut behind the faller
  - 18.0 s: the camera locking on and the air reversing
  - 43.4 s: the forces becoming equal
- **Proof strips** of 16 frames per proof (`MOTION_DESIGN_PROOFS/*_strip.png`).
- **Storyboard panels:** 75 frames at full size.

**Owner action:** watch `SKYDIVER_SLOWDOWN_V13_captions.mp4` in Chrome or QuickTime.

## Review checklist (brief §20): judged from frames, strips and panels

| Item | Status |
|---|---|
| Opening subject placement | **Fixed.** Aircraft upper-middle, figure below, readable at 360×640 (`qa/phone_size_check.png`). V12 vs V13 at 0:00, 0:01 and 0:03 in `qa/before_after/`. |
| Aircraft framing | Stays in frame; leaves at the top on purpose at about 2.4 s as the camera follows the figure |
| Cloud scale | Mid-scale clouds below the subjects; no full-frame wipe |
| Environmental depth | Four parallax layers with depth-weighted zoom, plus a haze band |
| Character continuity | Side rig (V12) throughout the science scenes. The rear pose now has bare hands (Codex V13), matching the side pose. The three-quarter pose is no longer used. |
| Arm and head motion | Unchanged from V12. The small elbow notch during the 0.3 s lift remains; head limited to ±1°. The Codex V13 folds and neck were tested and rejected (`CODEX_V13_INTEGRATION_MANIFEST.csv`). |
| Relative airflow direction | Down through still air, then up past you once the camera holds you (E1) |
| Force comparison | One scale; bars side by side; the excess is the model value |
| Upward net force | Violet, appears only after drag passes weight (43.6 s) |
| Continued downward movement | "balanced: still falling", "still moving down", a trail that is always lower, a falling needle |
| Instrument readability | Same wrist dial as V12 (B3, N1, O1) |
| Caption sync | Whisper and VAD aligned, 0 overlaps (`CAPTION_SYNC_QA.md`) |
| Audio continuity | Wind follows the fall, not the graphics (`SOUND_DESIGN_QA.md`). Not listened to. |
| Mobile readability | Labels 8.5–12 units (about 26–36 px at 1080 wide). "schematic" and "dots are schematic, not molecules" are small (8.5). |
| Pacing | Narration timing unchanged (78.2 s). One new visual event about every 1–2 s in the science section. |
| Muted review | See `SCIENTIFIC_MOTION_QA.md` |

## Defects fixed during V13 review

**Opening:**
- a sky band above the painting
- a black strip below the fields during the tilt
- the figure sitting on a painted cloud (the painting was shifted so the figure sits against sky)

**Labels:**
- a missing "→" glyph in the font
- the bar labels "weight" and "drag" overlapping
- the "net force: up" label clipped at the right edge during the push-in
- the "balanced: still falling" chip cut off by the push-in
- the recap "still moving down" chip enlarged by the push-in

**Airflow:** stray long trail lines on dots that wrapped around the screen.

## Known remaining issues

- **Elbow notch.** About 4 px at 1080 wide, visible for about 0.3 s during the two arm lifts.
- **Two-frame dissolves** (lift and glance) briefly show doubled outlines.
- **Opening-to-rear style change.** The painted opening cuts to the map-style terrain at 3.3 s.
- **Busy airflow shot.** E1's dot field fills the sky.
- **Recap gap is small.** The recap bars show only a 1.5% excess at model 148 s, which needs the ×2.6 push to read.
