# Narration alignment (verified in Slot 02 V15 and Slot 07)

1. Receive the human recording. Store it read-only, with its SHA-256, in `narration/raw/`.
2. Transcribe the words with whisper.cpp. Slot 02 used:
   `whisper-cli -m ggml-small.en.bin -f clean16k.wav -ml 1 -sow -ojf -of clean_words --dtw small.en -l en -np`
3. Snap the word edges to voice activity. Build phrases and the beat map: see `05-animation-engine/slot02_v15_reference/align_v14.py` and `09-production-templates/storyboard/BEAT_MAP_TEMPLATE.csv`.
4. Write `narration/WORD_TIMESTAMPS.json` with the keys `meta`, `words`, `phrases`, `sentences`, `pauses`, which the Slot 07 `narration.py` reads.
5. If the take changes, never reuse old times. Warp through the matching word edges (Slot 07 `NAR.v1(t)`), or re-design on the new times.
