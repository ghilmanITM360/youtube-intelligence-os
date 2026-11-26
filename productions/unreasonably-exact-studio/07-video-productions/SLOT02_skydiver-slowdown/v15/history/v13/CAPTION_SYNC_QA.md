# V13 caption sync QA

**Result:** the V12 SRT had 29 cues and 1 overlap. The V13 SRT has 48 cues and 0 overlaps. Every cue is timed from Whisper word timings, snapped to voiced audio.

## The V12 fault

The V12 SRT came from phrase *estimates*, and each phrase was extended by +0.25 s.
- **Overlap:** cue 4 (12.520–14.650) overlapped cue 5 (14.400–16.660) by **0.25 s**. That was the only overlap I found in the file.
- **Over-long cues:** cue 16 was **131 characters** on screen for **7.63 s**, which is far beyond comfortable reading on a phone. The burned-in captions showed only half of such phrases at a time.

## V13 workflow (`tools/align_captions.py`)

1. **Transcribe with word timings.** whisper.cpp (`whisper-cli`), model `ggml-small.en.bin` (official ggerganov/whisper.cpp weights), options `-ml 1 -sow --dtw small.en`. This gives word-level timings in `qa/asr/narration_words.json`.
2. **Snap to speech.** Whisper word *ends* absorb the silence that follows them. For example, it put "Wait," at 10.00–11.73 s, but the word is spoken at about 11.15 s. So each cue start and end is snapped to voiced audio:
   - The narration is analysed in 10 ms frames; "voiced" means within 30 dB of loud speech.
   - Speech runs are separated by silences of at least 150 ms.
   - The cue start is the start of the last speech run that begins inside the first word's span.
3. **Segment.** Cues break at spoken punctuation, then anything over 40 characters is split near its middle. The split never comes right after a function word or a number, so "10 kilometers" stays together. One-word fragments merge forward when the pause between them is under 0.6 s ("No, but the air is doing something").
4. **Display window.**
   - Start: 0.05 s before speech.
   - End: 0.25 s after speech.
   - Minimum 0.9 s on screen.
   - Clipped so a cue never runs into the next one, which the script checks with an assertion.
5. **Wording.** The cue text is the spoken words. The one ASR error, "breaks?", is corrected to the script's "brakes?" (a homophone). The narration audio was not edited.

Per-cue table: `qa/asr/caption_alignment.csv` (start, end, speech start/end, characters, characters per second).

## Checks

| Check | Result |
|---|---|
| Chronological, no overlaps | Yes. Asserted in the script; independent re-parse of the SRT finds 0 overlaps. |
| Length | At most 39 characters; two lines of at most 24 characters each on screen |
| Duration | Longest cue 2.56 s (V12: 7.63 s) |
| Reading speed | Median about 15 characters/s. Above 20 characters/s: "That's the strange part." (26.4), "It means the air is pushing back harder" (20.1), "But remember," (20.3), "Change the posture or the conditions," (19.2). They follow fast narration; splitting them further would cut the phrases in the wrong places. |
| Begins and ends with speech | Starts 0.05 s before the detected onset. Snapping found real pauses: "Wait, what?" now starts at 11.10 s (Whisper alone said 10.0) and "Eventually," at 38.69 s (Whisper alone said 38.0). |
| Mobile placement | Lower band, about y 545–600 of 640, with a white box. Checked on frames 0.5, 30.0, 44.5 and 49.0 s (`qa/caption_check.png`). It does not cover the subject, the density boxes, the bars or the trail. The bar labels at about y 545 sit just above the caption box. |
| Caption version | `SKYDIVER_SLOWDOWN_V13_captions.mp4`: alpha overlay (`qa/caption_overlay.mov`) composited over the clean film. Same cue data as the SRT. |

## Limits

- **Not a manual alignment.** Whisper DTW timings plus an energy threshold are good to about ±0.05–0.1 s on clear speech. Nobody has scrubbed each cue by ear.
- **Not checked in real time for every cue.** In Chrome I checked sample moments (see `FINAL_VISUAL_AND_AUDIO_QA.md`), not all 48 cues.
