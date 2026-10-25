# Audio Map

**Evidence:** `05_audio/audio_extract.mp3`, `05_audio/silence_raw.log` (ffmpeg `silencedetect=noise=-30dB:d=0.3`), `volumedetect` (mean -19.2 dB, max -0.8 dB).

## Limitation (read first)
No local speech-to-text engine was available in this environment (checked `whisper`, `whisper-cli`, `whisper.cpp`, `openai-whisper`). Per the evidence-priority rule, an unverifiable transcript must not be fabricated. **Narration wording is UNKNOWN.** Only structural/timing evidence below is OBSERVED.

## NARRATION
- Presence: LIKELY (a single continuous audio bed runs 0–83.4s at consistent -19 dB mean loudness, typical of a voice+music mix rather than music alone, given the video is a spoken "what if" question format).
- Wording: UNKNOWN.

## MUSIC
- Presence: LIKELY (continuous bed, no other silence gaps besides the one at 4.13–4.47s over 83s runtime).
- Track identity: UNKNOWN — do not guess a title/artist.

## SFX
- One audio event: a near-silence dip (-30dB threshold, 0.345s) at 4.13–4.47s, exactly coincident with the S01→S02 whip-zoom-blur cut (TIMELINE F01.1→F02.0, motion A02). LIKELY a transition whoosh/duck or a narration breath/pause; cannot confirm which without transcription.
- No other silence gaps ≥0.3s were detected anywhere else in the 83s runtime — i.e., no other hard audio cut points exist to anchor additional SFX to.

## AMBIENCE
None detected/applicable (flat hand-drawn content, no diegetic ambience implied).

## SILENCE
Only the 4.13–4.47s dip noted above.

## Sync table
| Timestamp | Audio type | Description | Visual event it syncs with | Confidence |
|---|---|---|---|---|
| 4.13–4.47s | SFX or VO pause | ~0.35s near-silence dip | S01→S02 whip-zoom-blur cut (F01.1→F02.0) | OBSERVED (silence) / LIKELY (causal link to the cut) |
