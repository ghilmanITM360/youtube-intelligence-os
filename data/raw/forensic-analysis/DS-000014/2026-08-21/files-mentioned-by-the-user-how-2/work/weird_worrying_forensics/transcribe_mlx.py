from __future__ import annotations

import json
from pathlib import Path

import mlx_whisper
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly


root = Path(__file__).resolve().parent
sample_rate, source = wavfile.read(root / "audio.wav")
source_dtype = source.dtype
audio = source.astype(np.float32)
if np.issubdtype(source_dtype, np.integer):
    audio /= max(abs(np.iinfo(source_dtype).min), np.iinfo(source_dtype).max)
if audio.ndim == 2:
    audio = audio.mean(axis=1)
if sample_rate != 16_000:
    divisor = np.gcd(sample_rate, 16_000)
    audio = resample_poly(audio, 16_000 // divisor, sample_rate // divisor).astype(np.float32)

result = mlx_whisper.transcribe(
    audio,
    path_or_hf_repo="mlx-community/whisper-small-mlx",
    language="en",
    task="transcribe",
    word_timestamps=True,
    verbose=True,
    temperature=0.0,
    initial_prompt="Weird and worrying questions from Shelby, Jeff, Tomasz, AJ and Karl; cold teeth and hot coffee, mirrors reflecting sunlight, building a new star, a volcano eruption, antimatter in the Chernobyl reactor.",
)
(root / "transcript.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
with (root / "transcript.txt").open("w") as handle:
    for segment in result["segments"]:
        handle.write(f"{float(segment['start']):06.3f}-{float(segment['end']):06.3f}\t{segment['text'].strip()}\n")
print("TRANSCRIPT:")
print(result["text"].strip())
print(f"segments={len(result['segments'])}")
