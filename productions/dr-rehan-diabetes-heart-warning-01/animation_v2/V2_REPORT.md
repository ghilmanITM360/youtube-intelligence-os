# V2 visual redesign — report, calibration, QA, handoff

Status: **V2 PREVIEW — NOT FOR PUBLICATION.** Audio wording, presenter credit and clinical review are still pending. V1 (`../animation/`, `../assets/`, `../exports/`) is untouched and kept as comparison evidence.

## Why V1 failed
- Cream backgrounds and boxed UI cards (a title panel plus a body panel) in every state. This reads as a generic medical-infographic template.
- Characters took up roughly 25–35% of frame height and were boxed in by panels. Faces were too small to act at phone scale.
- The three groups were nearly identical repeated cards. The heart and artery sat on empty cream with no narrative link.
- Several states were held for only 1.3–1.8 s with paragraph text. There were no captions and no sound.

## Style recipe (from existing research, not re-analysed)
Sources: `CHANNEL_PRODUCTION_DNA.md` §1–5 and `ORIGINAL_PRODUCTION_BLUEPRINT.md` §0–3 (git ref `fce81670`), plus private review of the Switzerland `3tVMjRRXQIg` sheet covering ~131–171 s. Reference frames stayed in the session scratchpad and are **not committed**.

1. **Background.** Predominantly pure white. Each scene has one concept object, with red reserved for emphasis. Simple flat environment plates (stairs, sofa/window) are used only where the setting tells the story.
2. **Characters.** One base body: oversized egg head (~40% of figure height), dot eyes with highlight, tiny mouth, mitten hands, stick legs and an outline with slight wobble. Identity comes from accessories (moustache plus green jumper; glasses plus white coat; bald top plus cane; grey bun; bob plus BP cuff).
   - Distinct from the reference: the head is egg-shaped rather than round, the outline is warm near-black, the palette is ours, and there is no copied host.
3. **Typography.** Heavy condensed black headlines with one red keyword. Labels are short. Verbatim captions sit in a separate zone.
4. **Composition.** Plate, then 1–3 characters, then one concept prop, then a headline. The presenter peeks in from the edge, as the reference host does.
5. **Motion.** One meaningful change per spoken phrase: pop, slide, pose switch, staggered icon build, headline wipe, gentle camera push, and callback reuse of earlier plates and icons.

## Calibration gate (three hero moments)
Files: `calibration/C1_hook.png`, `C2_doctor_patient.png` and `C3_three_groups.png`. Each was compared privately, side by side, with the reference sheet.

| # | First pass defect | Fix before bulk render |
|---|---|---|
| C1 hook | Headline and "easy to MISS" overlapped the patient's head; the figure sat too high | Stage moved down 190 px; patient scale 1.12→1.0; speech bubble moved left of the head |
| C2 doctor + patient | Preview band text overflowed | Band font 30→24 px |
| C3 groups | Group labels sat on top of heads; the S3 presenter overlapped captions; S4 arrow crossed a face | Labels pinned to the headline zone; presenter peek placed inside the stage; arrow moved to the top of the stairs |

After the fixes, the remaining differences from the reference are deliberate:
- No photographs or archival inserts, because no usable licensed medical source images are available.
- Fewer environment plates (2).
- No black year or number cards.

No claim of artistic equivalence is made.

## Scenes and assets
- 9 scenes, 80 animated layers and 28 caption lines. See `KEYFRAME_TIMELINE_V2.json` and `NARRATION_VISUAL_MAP.csv`.
- 37 original assets, all used (`ASSET_REGISTER_V2.csv`). 30 have an SVG source and PNG export; 7 are PNG-only badge or glow layers.
- Assets are drawn by code: `art.py` (characters, props, plates) and `v2.py` (badges, tag, divider).
- Character variants:
  - Patient: 6 (chest/smile on stairs, chest/pain, chest/worried, meter, neutral, phone)
  - Presenter: 4
  - Older man, older woman, woman with BP cuff and pills: 1 each
- Props: heart base, coronary overlay and marker (separate layers); 8 icons; speech bubble; glow; stairs, sofa and window plates.
- V1 artwork is not used in V2. None of it passed the white-canvas comparison.

## Narration coverage
- Every spoken phrase from 0.0 to 38.1 s has an on-screen change. See `NARRATION_VISUAL_MAP.csv` for scene times and phrases.
- 38.6–45.5 s is room tone. It is used for a takeaway with no speech, and no narration was invented. Captions stop where the speech stops.

## Medical text QA
Captions are verbatim ASR. Uncertain words are shown in amber brackets: `[angina?]`, `[subsets?]`, `[coronary syndrome?]` and `[sudden?]`. The speaker said "acute chronic syndrome" in the transcript, and ASR heard "acute coronation in their home". Nothing has been verified by listening.

Explanatory labels are paraphrases, not quotes:
- Less obvious warning signs (breathless, unusually tired, cold sweat, jaw/arm/back discomfort; AHA warning-sign list)
- Chest discomfort with exertion / angina-like symptoms
- 3 groups: Type 2 diabetes, Older men & women, Other health conditions (e.g. high blood pressure, high cholesterol)
- Acute coronary syndrome (ACS): blood supply to the heart muscle suddenly reduced (simplified)
- Takeaway that separates urgent from routine care:
  - "New, sudden or at-rest symptoms? Call emergency services now."
  - "Symptoms only with exertion? See your doctor promptly."
  - This follows the AHA/ACC 2021 chest-pain guideline and the 2025 ACS patient messages.

No character is labelled with a diagnosis. There is no ECG, heartbeat or plaque-growth animation. The heart is marked "simplified". **Clinician approval is still required.**

## Audio
- Voice: `1015.mp3`, sha256 `8f9e39ab…daf5` (verified). Decoded read-only at full length, with no trim, pitch, speed or word change.
- The whole mix was scaled once by ×0.89 to avoid clipping. Encoded max volume is -1.0 dB and mean volume is -18.5 dB.
- Music: original, synthesised in `audio.py` (soft Am–F–G–E chords) at about 20 dB under speech, lifted in the tail. No library tracks are used. It was created in this project, but no rights opinion is claimed.
- SFX: 17 soft synthesised pops, ticks, chimes and low tones placed at visual events (`audio/AUDIO_MIX.json`). There are no heartbeat alarms or whooshes.
- Trailing room tone is kept. **Trim proposal, not applied:** end the publish cut at ~42.0 s. This needs owner approval.

## Encoded-video QA (`Dr_Rehan_Heart_Warning_V2_PREVIEW.mp4`)
- 45.50 s, 1080×1920, 30 fps, H.264 + AAC 192k, 3.97 MB.
- Black/blank check: sampled at 2 fps, the lowest content std is 18.9 and nothing is blank.
- Missing assets: none. Every layer resolved at render.
- `CONTACT_SHEET_V2.png` is taken from the encoded MP4 at 75% of each scene.

Review was frame-sampled: 12 calibration and QA stills plus the contact sheet. Known weak points:
- S5 (21.95–23.4 s) holds the Type 2 diabetes group for only 1.45 s. The speech sets this pace.
- S10 (ACS) holds the heart for about 2.4 s before the next scene.
- Nobody has watched the full video with sound. This is still required.
- Mobile: the headline is 96–120 px, labels 40–78 px and captions 62 px at 1080 width. That is readable at about 360×640 in the reviewed stills, but it has not been checked with platform UI over the video.

## Before publication
1. The owner listens and confirms the four uncertain phrases.
2. Approve Dr. Rehan's name/credit and the use of an illustrated presenter.
3. Clinician review of labels, simplified anatomy and the emergency wording/locale.
4. Approve or reject the ~42 s trim.
5. Rights decision on the synthesised music.
6. Full playback review on a phone.

## Rebuild
```
cd animation_v2 && python3 art.py && python3 audio.py && python3 v2.py timeline && python3 v2.py render && python3 v2.py sheet
```
This needs Pillow, numpy, ffmpeg and `~/Downloads/1015.mp3`. `qa/` and `audio/*.wav` are regenerated and not committed.
