# Opening selection (narration 0 to 9.7 s, three rendered candidates)

Clips (540x960, 30 fps, with V2 narration and captions):

- `OPEN_A_ground_cinematic_audio_preview.mp4`
- `OPEN_B_closeup_to_wide_audio_preview.mp4`
- `OPEN_C_earth_to_moon_audio_preview.mp4`

Each clip has a filmstrip (`filmstrip_*.png`, 12 frames plus a frame-difference curve). Code: `animation/proofs/opening.py`. Automated checks: `PROOF_REPORT.md`, 22 of 22 PASS.

**How the clips were reviewed.** Claude looked at the filmstrips, the cue frames and frame stills at 0.0, 1.5, 3.1, 4.5, 6.4 and 8.5 s. The clips were not watched in real time, and nobody listened to the audio. The scores below are Claude's internal judgement, not a viewer test.

## Shared story beats

All three treatments follow the same beats:

1. "Imagine pointing a powerful laser at the moon." The camera aims at the Moon.
2. "Not to light it up." A floodlight cone washes over the Moon, a red NO mark appears, and the cone collapses. This shows the wrong idea.
3. "To ask it a question." Brackets lock onto the Moon.
4. "You fire a pulse." One dot leaves the telescope and reaches the Moon 1.28 s later, in real time. It arrives as the narrator says "reflector".

No continuous beam is ever drawn.

## Scores (1 to 5)

| Criterion | A: ground cinematic | B: close-up to wide | C: Earth to Moon |
|---|---|---|---|
| Subject readable immediately | 5: dome and Moon visible from frame 0 | 3: frame 0 is a soft close-up of a dark tube in a dark slit | 4: Earth and Moon readable, but the observatory is only a tiny pin |
| Curiosity | 4: the shutter splits open in the first second | 4: the reveal pull-back has energy | 3: a familiar space view |
| Narration sync | 5: lands on "moon."; pulse arrives on "reflector" | 5: same | 5: same |
| Scientific clarity | 5: the same telescope is seen sending | 4 | 4: the station is iconic, not real |
| Composition | 4: a lot of empty sky in the middle section | 3: soft upscale at 2.4x zoom | 3: the icon is out of scale on Earth |
| Visual impact | 4 | 4 | 3 |
| Natural motion | 4: mechanical drive with no overshoot; camera eased | 4 | 4 |
| Continuity with B05 onward | 5: the Moon match-pushes into G05; B22 reuses the same framing | 4 | 3 |
| **Total** | **36** | **31** | **29** |

## Decision: A (Claude's choice, pending the owner's G2 review)

A is the only treatment that shows where the experiment happens (the observatory), what is aimed (the telescope) and where it is aimed (the Moon) in the very first frame. B's close-up is too dark and soft to read at phone size in the first second. C loses the observatory.

Two things were borrowed from the others:

- From B: the shutter opening in the first second is the hook action.
- From C: the later science sequences continue the Earth–Moon schematic.

The selected clip is **P03** (`renders/proofs/P03/`).

## Defects still open on A

- **Mid-section stillness.** Between 3.5 and 7.0 s, only the overlays and a slow drift move. Proposed fix: add a slow sidereal-style star drift and dome rotation.
- **Small pulse at phone size.** The pulse dot is small; it was enlarged to 1.35x, but this still needs a phone viewing.
- **Seam during the opening.** The closed and open building layers show a faint seam while the shutter opens (about 0.8 s).
