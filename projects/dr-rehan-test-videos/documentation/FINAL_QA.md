# FINAL QA: Calf_Pain_PAD_FINAL_v2.mp4

This report was run on 2026-10-13. Every number below comes from the delivered `Calf_Pain_PAD_FINAL_v2.mp4`, not a draft. V1 and its QA are kept in `V1_ARCHIVE/`.

## Video: PASS
| Check | Result |
|---|---|
| Format | H.264 High · **1080×1920 · 30 fps** CFR · yuv420p, BT.709 TV range · **1818 frames = 60.600 s** · 29,991,732 bytes |
| Full decode (`ffmpeg -f null`) | 0 errors |
| `blackdetect` (d ≥ 0.1 s) | 0 black segments |
| `freezedetect` (n = 0.003, d ≥ 1.5 s) | 0 static holds |
| Assets and fonts | Kalam and Nunito are bundled and awaited with `delayRender`. No fallback glyphs or missing assets were seen in the 40-frame `CONTACT_SHEET_v2.png` |
| Ending | The last word "investigate" ends at ≈60.42 s and the video runs to 60.600 s, so nothing is cut |

## Audio: PASS (no human listening)
| Check | Result |
|---|---|
| Stream | AAC-LC, 48 kHz, stereo, 192 kb/s, 60.600 s |
| Narration identity and sync | Source MP3 SHA-256 is unchanged (`b419bad2…`). Envelope cross-correlation against the source MP3 is **0.9995**, best lag **0 ms**. The voice has no EQ, compression, pitch, speed or word edits |
| Narration dominance | Music alone measures −31.7 LUFS, 20 LU under the narration, and is ducked a further ≤5 dB under speech. SFX peak between −21 and −26 dBFS |
| Intelligibility under music | faster-whisper `small.en` on the final mix vs on the narration-only track: **193/193 words, WER 0.5 %** |
| Loudness and clipping | Mix is **−13.6 LUFS integrated**, **true peak −1.5 dBFS**, so no clipping. One static −1.88 dB gain is applied to the whole mix, because the source MP3 already peaks at +0.06 dBFS |
| Starts and stops | Music has a 1.2 s fade-in and a cosine fade-out ending on the last frame. There are no hard starts or stops (checked in the waveform and code, not by ear) |
| **Human listening** | **UNVERIFIED.** The agent cannot play audio. Every audio result above is measured, not heard |

## Captions: PASS
- 41 cues, contiguous from 0.000 to 60.580 s, parsed by ffmpeg.
- 2–7 words per cue (≤42 characters), shown on one or two balanced lines.
- No two cues are on screen at once: one cue is visible at a time, with a 0.12 s fade-in.
- On-screen captions and `Calf_Pain_PAD.srt` are generated from the same source: `tools/make_srt.py`, using real-audio word times.
- Safe zones:
  - Low band: y ≈1300–1420, x 95–915. This keeps captions above the Shorts description area and left of the action buttons.
  - Top band: used only from 25.5 to 35.9 s, where the doctor and board fill the lower frame.
- Readability was checked on rendered frames at **1080×1920**, **270×480** (6 dense scenes) and **216×384** (all of 0–3 s and the last 5 s). Captions stay legible at 216×384.
- None of the checked frames shows a caption over a face, the calf, the anatomy or a gesture.

## Animation: PASS (minor notes below)
- **Characters:** one rig with two looks. Proportions were upgraded the same way in every shot (thicker limbs, real calves, scaled hands and shoes, wider shoulders, flared coat).
- **Doctor name:** shown as Dr. Rehan Omar on the badge and in every visible credit.
- **Walk:** the IK ground-locked walk keeps stance feet planted. A 10 fps strip of the 3× calf close-up shows the stance shoes moving with the pavement seams; planted shoes stay flat.
- **Finale:** the magnifier is IK-aimed, so the **lens sits on the patient's calf** (frames 59.6 s and 60.55 s). The disclaimer is in its own pill, clear of legs, captions and titles.
- **Transitions:** eight narrative match transitions plus two continuous merged shots. No scene is static for 1.5 s or more (freezedetect).
- **First 3 s, muted (216×384 frames at 0, 0.5, 1, 1.5, 2, 2.5 and 3 s):** these show a walking figure, a wince, the calf clutch with push-in, then "WALKING → PAIN" and the seated "REST → RELIEF" in green. At 3 s, "WHY DO DOCTORS NOTICE THIS?" appears as the doctor arrives.
- **Last 5 s:** the patient limps in, the doctor raises a finger, then kneels with the lens on the calf. "ALWAYS, ALWAYS / INVESTIGATE" and the disclaimer pill appear, and the patient nods.

## Medical: PASS
- Checked against the AHA "Top Things to Know: 2024 Lower Extremity PAD Guideline", read in V1. That guideline links PAD to MI, stroke and death, and treats claudication and CLTI as separate subsets.
- **Mechanism:** at rest, a normal and a narrowed artery both supply the muscle. During activity, only the narrowed one falls short. The plaque sits inside the wall and the lumen never fully closes.
- **Walking vs rest:** the walking-pain panel notes "eases with rest", while rest pain is drawn as a separate, more serious pattern. Its wording is "may signal severe blood-flow loss" and "persistent pain at rest → seek prompt medical assessment". It is never shown as a diagnosis or as the inevitable next step.
- **Risk:** shown as direction only: heart attack ↑, stroke ↑, "elevated cardiovascular risk". No statistics.
- **Disclaimer:** "Not every cramp is PAD. A clinician can tell." is shown from 57.6 s.

## UNRESOLVED (flagged, not silently changed)
| Time | Issue | Handling |
|---|---|---|
| **4.74–5.58 s** | **Name mismatch.** The recorded voice says "Dr. Rahim" (ASR heard "Rahin"); the correct name is **Dr. Rehan Omar**. | The badge and all graphics show Dr. Rehan Omar. The caption stays verbatim, "Let's see what Dr. Rahim says.", so the video never claims the voice says otherwise. **Fix:** have the original speaker re-record "Let's see what Dr. Rehan Omar says". Then replace 4.30–5.60 s in `public/narration.mp3`, change chunk 4 in `tools/make_srt.py`, and run `npm run final`. |
| **41.5 s** | **Unclear medical term.** The script says "critical demischemia"; ASR heard "critical nimischemia". | The caption reads **`critical [limb] ischemia,`**, with the brackets marking an inferred word. The on-screen labels avoid the term. **Needs a human listen.** |
| 15.2 / 26.9 / 28.6 / 42.6 s | Script ≠ ASR: "low on" vs "in", "the most" vs "the mode most", "that is" vs "There is", "which is" vs "It is" | The captions follow the supplied script, as in V1. No correction was made without listening. |

## Minor remaining notes (non-blocking)
- **Lip-sync:** driven by loudness, not phonemes.
- **Walk endings:** blending from walk to stand can shift a foot a few pixels at the moment of stopping.
- **Finale:** the "INVESTIGATE" title sits a few pixels above the patient's hair tuft in the last 0.8 s.
- **S8 pointing:** the board panels are beyond arm's reach, so the doctor points toward them rather than touching them.
- **Deletable intermediates** (not deleted; needs your approval): `project/out/` (renders, drafts, QA frames) and `.asr-venv/` (ASR environment, ~214 MB). `npm run final` rebuilds everything.
