import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel


def srt_time(seconds: float) -> str:
    millis = round(seconds * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


if len(sys.argv) != 4:
    raise SystemExit("Usage: transcribe_video.py VIDEO OUTPUT_DIR MODEL_DIR")

video = Path(sys.argv[1])
output_dir = Path(sys.argv[2])
model_dir = Path(sys.argv[3])
output_dir.mkdir(parents=True, exist_ok=True)
model_dir.mkdir(parents=True, exist_ok=True)

model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8",
    download_root=str(model_dir),
)
segments_iter, info = model.transcribe(
    str(video),
    language="en",
    beam_size=5,
    best_of=5,
    vad_filter=True,
    vad_parameters={"min_silence_duration_ms": 350},
    word_timestamps=True,
    condition_on_previous_text=True,
)

segments = []
for segment in segments_iter:
    words = []
    for word in segment.words or []:
        words.append(
            {
                "start": word.start,
                "end": word.end,
                "word": word.word,
                "probability": word.probability,
            }
        )
    item = {
        "id": segment.id,
        "start": segment.start,
        "end": segment.end,
        "text": segment.text.strip(),
        "avg_logprob": segment.avg_logprob,
        "no_speech_prob": segment.no_speech_prob,
        "words": words,
    }
    segments.append(item)
    print(f"[{segment.start:8.2f}–{segment.end:8.2f}] {segment.text.strip()}", flush=True)

payload = {
    "language": info.language,
    "language_probability": info.language_probability,
    "duration": info.duration,
    "duration_after_vad": info.duration_after_vad,
    "segments": segments,
}
(output_dir / "transcript.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
(output_dir / "transcript.txt").write_text(
    "\n".join(
        f"[{srt_time(item['start']).replace(',', '.')} – {srt_time(item['end']).replace(',', '.')}] {item['text']}"
        for item in segments
    )
    + "\n",
    encoding="utf-8",
)
(output_dir / "transcript.srt").write_text(
    "\n\n".join(
        f"{index}\n{srt_time(item['start'])} --> {srt_time(item['end'])}\n{item['text']}"
        for index, item in enumerate(segments, 1)
    )
    + "\n",
    encoding="utf-8",
)

print(f"Wrote {len(segments)} segments to {output_dir}")
