# Word-level timing from the narration MP3 (faster-whisper small.en, cached locally).
import json, sys
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe(sys.argv[1], word_timestamps=True, beam_size=5, language="en")
words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for s in segs for w in s.words]
json.dump(words, open(sys.argv[2], "w"), indent=0)
print(" ".join(f'{x["w"]}@{x["s"]:.2f}' for x in words))
