# V3 audio mix QA

Date 2026-10-14, Laptop B. `tools/sound.py` writes the mix and its measurements to `V3_AUDIO_MIX.json`. Checks on the encoded file come from `tools/qa.py video` and are recorded in `V3_VIDEO_QA.json`.

**Verdict:** technically clean and the narration is intact. **No one has listened to the mix.** Claude cannot hear audio, so everything below is signal measurement, not listening. The owner should check on a phone speaker and on headphones that:
- the bed is audible but not distracting;
- the effects are noticeable but not cartoonish.

## Mix structure

| Layer | Treatment |
|---|---|
| Narration | The owner's WAV, decoded and resampled 44.1 → 48 kHz. No edit, trim, EQ, compression, speed or pitch change. The only processing is the uniform **−1.35 dB master gain** shared by the whole mix, which creates true-peak headroom. The source file is untouched (read-only, same SHA256) |
| Music bed | Original. Set **20 dB below the speech RMS** (−13.2 dBFS) before ducking. **Ducked 4 dB** while the voice is present (60 ms attack, 450 ms release), so it sits about 24 dB under the voice during speech and rises gently in pauses. 0.25 s fade-in; 1.4 s fade-out across the end hold. High-passed at 70 Hz and low-passed at 9 kHz |
| Effects | 10 original one-shots, 0.14–1.6 s long, placed on the first frame of the visual they reinforce. The times are read from `KEYFRAME_TIMELINE.json` |
| Master | One gain to reach −1.5 dBTP, measured by 4× oversampling. No limiter, so the voice is not dynamically altered |

## Measured

| Check | Result |
|---|---|
| Narration present and in sync, encoded final | Best-fit lag **0 samples**, gain −1.35 dB (exactly the master), narration-to-rest **23.1 dB** |
| Narration words | Same WAV as V2, all 134 ASR tokens; no audio removed. The end hold adds silence only after the last word (49.28 s) |
| Truncation | The MP4 holds 2,448,000 samples at 48 kHz = 51.00 s, the full video length. The WAV content ends at 49.68 s |
| Speech-to-background, voiced frames | Median **22.6 dB**, 5th percentile 5.0 dB (quiet word tails) |
| Same, 1–4 kHz intelligibility band | Median **25.9 dB**, 5th percentile 5.6 dB |
| Bed level in narration pauses | −23.1 dB relative to speech |
| Clipping | Mix sample peak −1.50 dBFS. **Encoded final true peak −1.5 dBTP** (ffmpeg ebur128); limit is −1 dBTP |
| Loudness, integrated (EBU R128) | V3 mix −15.0 LUFS (LRA 3.8 LU). Narration-only −13.7 LUFS. Not normalized, as the brief requires |
| AAC encode fidelity | Decoded final vs `FS02_V3_MIX.wav`: 47.1 dB SNR |

## Effects (10)

Levels are before the −1.35 dB master gain. "Voice" is the narration's RMS over the same window.

| t (s) | Visual | Sound | Peak dBFS | RMS dBFS | Voice RMS |
|---:|---|---|---:|---:|---:|
| 0.83 | Rate arrow rises (S01_01) | Soft rising tone with air | −24 | −32.0 | −12.3 |
| 3.31 | Interest bill enters (S01_03) | Two paper flicks | −22 | −37.7 | −19.2 |
| 6.59 | FOMC ¼-point highlight box (S02_01) | Marker stroke | −22 | −35.6 | −13.5 |
| 12.65 | Interest flow Fed → banks (S02_06) | Soft swoosh | −21 | −36.4 | −12.1 |
| 16.31 | ABOUT $7.5B lands (S03_04) | Restrained pop | −21 | −32.2 | −13.9 |
| 27.25 | Ledger opens (S05_02) | Three page rustles | −20 | −37.4 | −9.6 |
| 31.93 | H.4.1 −233,587 highlight (S05_05) | Marker stroke | −22 | −34.9 | −14.4 |
| 38.07 | Treasury payments pause (S06_03) | Soft knock, ~220 Hz so phone speakers reproduce it | −19 | −29.2 | −12.6 |
| 41.73 | $107.4B lands (S06_05) | Restrained pop, lower pitch than the first | −21 | −31.5 | −9.6 |
| 48.60 | BOTH CAN BE TRUE (S07_04) | Mallet dyad in the bed's key + felt thump | −21 | −37.8 | −19.6 |

Every effect is 15–28 dB below the voice in its window. There are no cash-register sounds, no repeated whooshes, and no sound on caption words.

## Research basis and limits

- The Casually Finance DNA has **no direct observations of music or SFX** (`SHORTS_DNA.md`: "No music absence … is established"). The sound design is therefore an editorial choice for this production; nothing here claims it matches the reference creator.
- The audibility thresholds were chosen without listening. Phone speakers may make the bed and the marker/page effects inaudible; headphones may make the pops more noticeable. Retune them in `tools/sound.py`: `BED_REL` and `DUCK`, and the `norm(...)` peak in each effect.
- `Finance_Short_02_FINAL_v3_NARRATION_ONLY.mp4` has the same V3 picture with the untouched narration (−0.4 dBTP), for comparison or as the fallback.
