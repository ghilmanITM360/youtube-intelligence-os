# V9 final visual and audio QA (actual observations)

**Verdict: V9 is a review cut, not a publishable final.** Three blockers remain:
1. The character and equipment art is still procedural (Codex P0 assets are pending).
2. The library SFX licences are not cleared.
3. No human has listened to the mix, and the narration version needs owner confirmation.

## Evidence base

- Full-film contact sheet every 1.5 s (`qa/V9_contact_1p5s.jpg`) viewed after each render iteration (3 full renders).
- 68 full-size storyboard panels.
- 1 s, 2 fps and 4 fps sequence strips (`qa/seq_*.jpg`).
- Real-time browser playback of the final MP4 at `review.html`. The video played unmuted, and the audio decoder was confirmed active (`webkitAudioDecodedByteCount` > 0, time advancing). Screenshots were taken during live playback at ~5 s, ~9 s and ~15 s.
- `ffmpeg` full decode with no errors, `freezedetect`, and EBU R128 measurement.
- `tools/v9.py --check`.

## Pass 1 — Physics

Every beat is checked against `tools/model.py` (see PHYSICS_VISUAL_CORRECTION_LEDGER.md).

- **Found and fixed:**
  - Drag originally crossed weight at 40.2 s, before the words "stronger than your weight". It was retimed to cross at 43.6 s, with drag > weight from about 44.0 s.
  - The density comparison was nearly invisible, because the honest change is only about 8% at that point. A third equal sample, "near ground", was added to show the real ~3× gradient.
- **Holds (verified by `--check`):**
  - Velocity is never upward.
  - Altitude never rises.
  - The needle only falls after 47.7 s.
  - No ground contact is shown; the minimum altitude is 445 m.
  - Drag exceeds weight by at most 3.5%, drawn to the same scale.
  - The net force is drawn as drag − weight, at 10× in a labelled inset.

## Pass 2 — Character

- **Flutter:** flutter is layered and non-looping on all limbs. The glance acting reads at phone size, and the reaction close-up has eye, brow, blink and head beats. In the model section the body posture is unchanged and the flutter calms with speed.
- **Placeholder art (open):** the art is the inherited procedural SVG. It is clean but geometric, which is the owner's stated objection, and it is not solved.
- **Pivots:** no joint gaps were observed in the sampled frames. An extreme-pose test was not repeated for V9.

## Pass 3 — Environment

- **Fixed during review:**
  - The first terrain pass read as a checkerboard.
  - The original 23 km haze hid the Earth in the establishing shot; it is now 40 km.
  - The lower frame was empty at low altitude.
  - The horizon sat too high, leaving too little sky.
- **Now:**
  - The horizon sits in the lower third for tracking shots, with broad sky above.
  - The cloud deck appears below the camera at 10 km and above the horizon at low altitude.
  - Field size grows correctly as altitude drops (A2 → P1 → R1).
  - Earth's curvature is not exaggerated.
- **Weakness:** the straight-down POV (O1) still reads as a coarse pastel mosaic.

## Pass 4 — Camera

- **Motivated moves:**
  - Establishing push-in, motivated by finding "you".
  - Wrist insert, motivated by the glance.
  - Pull-back, motivated by the model caveat.
- **Fixed:** the pull-back originally began 60 m from the figure, so a giant pack filled the frame; it now begins at tracking scale. The final shot was a 1.8 s static hold; a drift was added.
- **Remaining static stretch:** 21.9–22.7 s only. It is intentional: the "starting from rest" beat, with no world motion.

## Pass 5 — Instrument

- One instrument design appears in exactly two placements: a fixed card through the model section, and the wrist insert.
- The needle sits at 0 at the declared reset and never reverses after 47.7 s. There are no numerals.
- The hook insert is tagged "later in the fall".
- **Weakness:** the wrist and sleeve are a procedural placeholder (CH-05).

## Pass 6 — Airflow

- Streamlines bend around the body and move upward, consistent with still air and a falling body.
- They are labelled "relative airflow · schematic". Speed specks are kept short and faint.
- **Fixed:** the first pass looked like rain; it was reduced.

## Pass 7 — Typography

- Headlines were removed.
- Phrase captions are 15 units (45 px), sit in the lower third and have backing boxes.
- Object labels are 8.5–11 units, attached to what they label.
- **Fixed:** two label collisions, and the `→`/`−` glyphs that rendered as boxes.
- **Risk:** 7.5–8 unit footnotes (about 22–24 px) are small on a phone.

## Pass 8 — Audio (measured, NOT heard)

**Mix measurements:**

| Measure | Value |
|---|---|
| Final integrated loudness | −16.4 LUFS |
| LRA | 4.3 LU |
| Peak | −1.0 dBFS |
| VO stem | −18.1 LUFS, unaltered in timing and gain (the +2 dB final gain is uniform across the mix) |
| WIND_AMB stem | −30.7 LUFS (~12.6 dB under VO), ducked about −7 dB inside phrases |
| Library cues | 10, all with confirmed placement |

**Cue placement:**
- 3 transition whooshes (1.55 s, 19.35 s reverse, 70.3 s), not one per cut.
- The V8 omission (zero SFX) is corrected.
- The wind is near-silent at model rest.

The assistant cannot listen. Audition was done by spectrogram and level measurement only. **A human listening pass is required.**

## Pass 9 — Muted playback

From the contact sheet without audio, the sequence reads:
1. Plane → you.
2. Pack closed.
3. Gravity.
4. Glance at a falling dial.
5. Model starts at rest.
6. Drag grows.
7. Same-air comparison.
8. Drag passes the weight tick.
9. Net force up while velocity points down.
10. The speed curve never reaches zero.
11. Model caveat.

Captions carry the questions. The weakest muted beat is J1's first second, which is an empty panel while it fades in.

## Pass 10 — Complete viewing

The full contact sheet was reviewed three times, and real-time browser playback was sampled. There was no continuous human watch.

## Open items

- **Codex P0 assets:** CH-01, CH-03, CH-05, AC-01.
- **SFX licences:** a rights-clear mix (`audio/V9_mix_rights_clear.wav`: VO plus generated wind and aircraft) exists for publication if the library is not cleared.
- **Narration confirmation:** the 78.2 s recording vs the shorter Slot 02 text.
- **Manual word alignment:** phrase times are ±0.3 s.
