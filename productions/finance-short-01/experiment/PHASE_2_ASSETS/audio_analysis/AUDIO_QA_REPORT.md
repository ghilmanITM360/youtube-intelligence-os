# Audio QA report: owner MP3

Checked 2026-10-13. The MP3 was copied byte-for-byte and never edited. All processing ran on decoded scratch copies.

## Source

| Field | Value |
|---|---|
| File | `source_audio/TTSOL-en-AU-WilliamMultilingual-20261013-154730.mp3` (read-only copy of `~/Downloads/…`) |
| SHA256 | `f4a9e22d313601c431873f3e7ea38a20a31ee43ff5b4c11ce8d1a668897d7b33` (original and copy match) |
| Size | 316,368 bytes |
| Codec | MPEG-1 Layer III, 48 kbps CBR, mono, 24,000 Hz |
| Duration | **52.728 s** container = 1,265,472 decoded samples = 52.728 s; 1,582 frames at 30 fps |

## Technical QA: PASS

- **Clipping:** none. Sample peak −2.82 dBFS, true peak −2.8 dBFS, max |sample| 0.7225, flat factor 0.
- **Loudness:** −20.6 LUFS integrated, LRA 1.5 LU, RMS −21.0 dBFS. This is quiet for Shorts. Level it in the final mix (for example toward −14 LUFS); don't alter this source file.
- **Silence and completeness:** 0.207 s lead-in, 0.370 s tail after the last word ("too", ending 52.358 s). There are 20 internal pauses of 0.33–0.90 s. Nothing is truncated: all 140 script words are present in order.
- **Phrase structure:** the 21 speech phrases match the script's 21 punctuation breaks 1:1, so phrase edges are acoustic measurements (silencedetect −45 dB, ≥0.12 s).

## Script match: PASS except one word

An unprompted whisper.cpp (small.en) transcript matches `FINAL_SCRIPT.md` word for word, apart from normalizations ("12" = twelve, "0%" = zero-percent, apostrophe in "promotion's", punctuation) and **one substitution**:

| Script | Heard | Time |
|---|---|---|
| introductory **APR** | introductory **April** | **38.63–39.03 s** (frames 1159–1171), inside sentence 36.845–39.647 s |

## Pronunciation gate: FAIL (material)

"APR" must be spoken as the letters A-P-R. The MP3 says the month "April". The evidence is in `pronunciation_gate.json`, `APR_segment_spectrogram_annotated.png` and `apr_acoustics.py`:

1. Five independent decodes return "April": full file, isolated sentence with beam/greedy/temperature 0.4, and tail only. A decoder prompt that explicitly primed "APR / A.P.R." still produced "April".
2. Acoustics: after the "A" glide and the /p/ closure come ~0.17 s of r-coloured, dark-l material (F3 ≈ 1.6–1.7 kHz, F2 ≈ 0.95–1.08 kHz). There is no /iː/ ("pee", which this voice produces at F2 ≈ 2 kHz) and no open "ar" vowel. That is "-pril", not "P-R".

Limitation: no human listening pass was possible. The verdict rests on ASR agreement plus acoustic segmentation, and both point the same way.

**Required:** a corrected MP3 from the owner, with the TTS input written as `A-P-R` or `A.P.R.` (or the tool's spell-out/SSML option). After that, re-run:

```
python3 build/align_audio.py <corrected.mp3> ../FINAL_SCRIPT.md AUDIO_ALIGNMENT.json <scratch_dir> audio_analysis/pronunciation_gate.json
```

Until then, every timestamp in `AUDIO_ALIGNMENT.json`, `SCENE_ASSET_MAP.csv` and `CLAUDE_HANDOFF.md` is **provisional**. A regenerated TTS file can shift every timing slightly, not only the APR sentence.

## Timing confidence

| Layer | Method | Status |
|---|---|---|
| Phrase and sentence edges | Measured silence boundaries | Measured on this MP3, ±~20 ms |
| Word anchors | whisper DTW token end times clamped into measured phrases | `PROVISIONAL_ASR_DTW_CLAMPED_TO_MEASURED_PHRASE`; typically within ~0.1 s, sometimes worse (APR is ~0.1 s early). Not verified word-level sync |
| APR word span | Manual acoustic segmentation | 38.63–39.03 s |
