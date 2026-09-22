from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

import mlx_whisper


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("wav")
    parser.add_argument("output_json")
    parser.add_argument("--model", default="mlx-community/whisper-small-mlx")
    args = parser.parse_args()

    sample_rate, audio = wavfile.read(args.wav)
    if audio.ndim == 2:
        audio = audio.astype(np.float32).mean(axis=1)
    else:
        audio = audio.astype(np.float32)
    if np.issubdtype(audio.dtype, np.integer):
        audio /= np.iinfo(audio.dtype).max
    else:
        peak = max(float(np.max(np.abs(audio))), 1.0)
        audio /= peak
    if sample_rate != 16_000:
        gcd = np.gcd(sample_rate, 16_000)
        audio = resample_poly(audio, 16_000 // gcd, sample_rate // gcd).astype(np.float32)

    result = mlx_whisper.transcribe(
        audio,
        path_or_hf_repo=args.model,
        language="en",
        task="transcribe",
        word_timestamps=True,
        verbose=True,
        temperature=0.0,
        initial_prompt="How long could you drive toward the sunset? Earth, sunset, North Pole, Longyearbyen, Arctic Circle, PyEphem.",
    )
    Path(args.output_json).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print("TRANSCRIPT:")
    print(result["text"].strip())
    print(f"segments={len(result['segments'])}")


if __name__ == "__main__":
    main()
