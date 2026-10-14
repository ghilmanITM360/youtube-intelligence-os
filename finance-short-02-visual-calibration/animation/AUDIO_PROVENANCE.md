# Audio provenance — Finance Short 02 narration

## Source file

| Field | Value |
|---|---|
| File | `cartesia_2026-10-14T09_09_17Z_Skylar_sonic-3.6-2026-08-27.wav` |
| Supplied by | Owner, 2026-10-14, at `/Users/ghilmankhan/Downloads/` on Laptop B |
| Project copy | `animation/audio/` (byte-identical, read-only `chmod 444`; the Downloads original was not modified) |
| SHA256 | `3eff2e57cd6f86e9a879d907d4cd46478dcc04d1660050b78ce4f72a5ee50328` (original and copy match) |
| Size / format | 4,381,820 bytes, WAV PCM s16le, 44.1 kHz, mono |
| Duration | **49.68 s** (2,190,888 samples) |
| Origin | The filename indicates Cartesia TTS, voice "Skylar", model `sonic-3.6-2026-08-27`, generated 2026-10-14 09:09:17 UTC. This is read from the filename only and was not independently verified. |
| Rights | The owner supplied this audio for this production. It is committed to the owner's **private** repository for recoverability. No other rights claim is made, and Cartesia's terms were not reviewed in this session. |

## Technical QA (measured)

- Sample peak −0.37 dBFS, **0 clipped samples** (max +31407 / min −29135). Mean volume −13.5 dB.
- Speech runs 0.00–49.28 s; the 0.40 s tail is room tone. There is no leading silence longer than 0.18 s.
- 11 inter-phrase pauses of 0.20–0.45 s (ffmpeg `silencedetect` −40 dB / 0.18 s). They line up with the approved phrase breaks.
- No dropouts were detected, and no pause falls inside a phrase.

## Script correspondence

The approved narration is the project's `editable_sources/original/APPROVED_NARRATION.txt` (147 words, SHA256 `a43916ce…`). It was compared with a local openai-whisper `base` transcription that has word timestamps.

- **Result: `MATCH_AFTER_NUMBER_NORMALIZATION`**. The ASR token sequence (134 tokens) equals the approved text after normalization (134 tokens). There are no substantive wording differences, no missing or extra words, and no reordering.
- Normalization-only differences: ASR prints "$3 trillion", "$7.5 billion", "$234 billion", "2021" and "$107 billion" where the script spells out "three trillion dollars", "seven and a half billion dollars", "two hundred and thirty-four billion dollars", "twenty twenty-one" and "one hundred and seven billion dollars". ASR also drops the hyphen in "quarter-point" and changes punctuation.
- **Inferred, not heard:** ASR cannot confirm how the numbers were spoken (e.g. "seven and a half" vs "seven point five") or that each "dollars" was spoken. Uninterrupted speech follows "$234 billion" (33.88–34.76 s) and "$107 billion" (43.32–44.46 s), with no pause. That is consistent with the approved "dollars", but it is waveform evidence only.
- **No human listening.** Claude did not listen to this file. All statements above come from ASR and waveform measurement.

## Use in the video

- The WAV is the **timing authority**. Video length = audio length (1491 frames at 30 fps = 49.70 s; the AAC stream is 49.68 s).
- Narration is **unchanged**: no cut, trim, speed, pitch, EQ or gain change. It is encoded once to AAC-LC 192 kb/s, resampled 44.1 → 48 kHz, mono.
- The decoded MP4 audio has exactly the WAV's sample count at 48 kHz (2,384,640). Its zero-lag SNR against the WAV is 47.3 dB, so there is no truncation or offset. Peak after encoding is −0.45 dBFS sample / −0.4 dBTP true peak, with no clipping.
- **No music and no sound effects.** No third-party audio is in the file.

Reproduce the alignment from the project directory with `python3 animation/tools/align_audio.py`, which needs openai-whisper and its `base` model. It writes `AUDIO_ALIGNMENT.json`.
