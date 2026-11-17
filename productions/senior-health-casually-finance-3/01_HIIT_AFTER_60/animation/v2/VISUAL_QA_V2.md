# HIIT V2: visual, motion and output QA

**Output.** `HIIT_After_60_V2_REVIEW.mp4`, 1080×1920, 30 fps, 31.133 s, H.264 + AAC. Mobile copy: `_MOBILE_540x960.mp4`.

**Status.** REVIEW ONLY, publication-blocked: clinical approval and human listening are outstanding.

## Machine checks (`RENDER_QA_V2.json`)
**Decode and sync.**
- Full ffmpeg decode: no errors.
- Audio/video stream duration delta: 0.000 s.
- Peak −0.9 dBFS, mean −16.9 dB.
- No blank frames.

**Large inter-frame changes.** Each one is intentional:
- 14.0 s: clinic cut
- 17.1–17.2 s: eased push-in
- 21.9–22.1 s: widen + callback bars
- 24.8 s: park cut (inside the planned-cut window)

These were inspected at 10 fps in temporal windows: no pops, and objects stay connected.

**Captions.** 20 cues; minimum 0.86 s, median 1.64 s; none under 0.8 s. The block's bottom edge is 1492 px.

**Assets.**
- 12 existing assets, 97 tracks (character parts, parents, text).
- New artwork files: 0. Text labels are rendered type, not artwork.
- All referenced rasters were present (the render would fail otherwise).

**Contact sheets.**
- `CONTACT_SHEET_V2.png`: one frame per second, 0–31.08 s.
- `CORRECTED_FRAMES_V1_V2.png`: V1/V2 pairs.

## Visual review (frames, 10 fps windows 0–4.5, 13.6–14.4, 16.7–17.7, 21.6–22.6 s)
**Hook.** The idea is clear at frame 0: question, intensity contrast and a runner. Everything is built by 1.5 s, the rating lands on "7", and the hook clears before the next headline.

**Run cycle.**
- Shoulders, arms and legs stay connected across adjacent frames.
- The front foot meets the path.
- The camera only moves between ideas.

**Mobile 540×960.**
- Headline ≈50 px and captions ≈33 px: readable.
- The two supporting labels ("example: hard + easy intervals", "speaker's rating") are ≈17–18 px. They are secondary and must be confirmed on a phone.
- No important graphic sits under the right-hand action rail or the bottom title band.

**Not achievable here.** Real-time playback judgement of motion feel. The owner should watch it on a phone.

## Casually Finance techniques applied
These are generic observed techniques, from research in `reference_local/research/MOTION_DNA.md` and `CASUALLY_FINANCE_VISUAL_SPEC.md`. No competitor pixels or characters are used, and no claim is made about their private workflow.

| Technique | Observed reference | Applied here |
|---|---|---|
| Progressive build, not a finished dashboard | -X6YzlY_8tM 169–189 s (successive bars) | Interval bars grow one by one with the words |
| Retain the host while the chart is exposed | roe3SgezmmU M0001 0.042–0.667 s | Runner stays on stage while the bars build in the hook |
| Camera reframing on static drawings | -X6YzlY_8tM 29–31 s (pointing host) | Push-in on Nora and Sam during the risk explanation |
| Continuity inside a scene while adding emphasis | roe3SgezmmU M0091 | Heart and Sam persist; concern marker added; bars callback |
| Character reaction serves the argument | rSa2aziEsAI M0010 20.333–21.1 s | Sam stops and worries on "However"; staggered pose changes in the clinic |
| Cut, then local enlargement | JsK53moCyZA M0046 30.4–32.867 s | Clinic/park cuts, then object pops |
| White stage, flat selective colour, reused cast/props | VISUAL_DNA | Same Sam/Nora/heart/bars reused across beats |

## Remaining human requirements
1. **Listening, end to end:** "mobility" vs "morbidity" (19.4 s), "caught" vs "got" (11.1 s), "avoided in" (21.9 s), and the naturalness of the 0.90 and 0.93 stretched spans (0–1.43 s, 3.21–7.94 s).
2. **Clinical review:**
   - H4: absolute "expert cardiologist" supervision.
   - H5/H6: blanket avoidance of HIIT with cardiovascular disease, which contrasts with supervised cardiac-rehab interval programmes; see `../../MEDICAL_SOURCES.json`.
   - The 7/10 rating is opinion.
3. **Phone review:** check the small supporting labels.
4. **Rights:** owner decision on the synthesised music/SFX and the supplied voice.
