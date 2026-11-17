# V3 full review — `Dr_Rehan_Heart_Warning_V3_UPLOAD_CANDIDATE.mp4`
Status: **upload candidate, pending owner and clinical approval.** This is production QA, not clinician approval.

## Format
- 43.000 s, 1080×1920, 30 fps, H.264 yuv420p, AAC, 3.56 MB.
- The full file decodes with no errors (`ffmpeg -f null`).

## Automated checks on the encoded MP4
- **All 1290 frames:**
  - The minimum luminance std is 17.2, so there are no black or blank frames.
  - The bottom 120 px is pure white (mean 255) on every frame, which confirms the debug band is gone.
- **Frame-difference scan:** the largest jumps are all at the 9 planned scene cuts (5.7, 8.5, 13.2, 19.4, 28.5, 33.8, 36.2, 38.6 s) and at the S5 group swaps. No unplanned position jumps were found.
- **Text audit:** I grepped every text layer and caption in `v3.py` and `KEYFRAME_TIMELINE_V3.json` for preview / provisional / publication / approval / placeholder / likeness / owner / debug / TBD / test / `?]`. **None are rendered.** The only remaining hits are code comments and the audio filename.
- **Assets:** all layers resolved at render, and none are missing.

## Visual review
I reviewed the stills at 0.5, 7.6, 11.5, 12.3, 17, 22.5, 27.9, 32, 35, 35.5, 38, 40, 42.5 and 42.9 s, plus `V3_CONTACT_SHEET.png` (9 scenes, taken from the encoded MP4).
- **Typography:** no clipped or overlapping captions after the fixes, and captions sit at a single height.
- **Characters:** consistent identities and sizes per scene. Hands are attached in every reviewed pose.
- **Medical content:**
  - No character is diagnosed.
  - The heart is labelled as ACS with a plain-language explanation.
  - Emergency wording separates new, sudden or at-rest symptoms (call emergency services) from symptoms that only come with exertion (see a doctor promptly).
- **Not done:** no frame-by-frame human watch of the moving video, and no viewing on a real phone with the Shorts UI overlaid. No artistic sign-off is claimed.

## Known limits left as-is
- S5 shows "Type 2 diabetes" for about 1.45 s. This follows the speech pace.
- The ACS scene holds for about 2.4 s.
- The caption region is empty from 33.9 to 34.9 s, where the wording is unconfirmed.
