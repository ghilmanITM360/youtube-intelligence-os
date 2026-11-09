"""Stage A: audio extraction + local Whisper (free, base model already cached) word-timed transcript. Resumable (skips if whisper.json exists).
Usage: python3 -B stage_audio.py <VIDEO_ID> <WORK_ROOT> <OUT_DIR>
ASR is machine output: every word carries Whisper's probability; nothing is hand-corrected here.
"""
import csv, json, subprocess, sys, time
from pathlib import Path


def main(vid, work_root, out):
    out = Path(out); work = Path(work_root) / vid; work.mkdir(parents=True, exist_ok=True)
    row = next(r for r in csv.DictReader(open(out / "00_MANIFEST/SELECTED_18.csv")) if r["video_id"] == vid)
    src = row["local_path"]
    w16, w22 = work / "audio16k.wav", work / "audio22k.wav"
    if not w16.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", str(w16)], check=True)
    if not w22.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "22050", str(w22)], check=True)
    wj = work / "whisper.json"
    if wj.exists():
        print("whisper cached", wj); return
    import whisper
    t0 = time.time()
    model = whisper.load_model("base", device="cpu")
    res = model.transcribe(str(w16), language="en", word_timestamps=True, condition_on_previous_text=False, temperature=0.0, fp16=False, verbose=False)
    json.dump({"video_id": vid, "asr_model": "openai-whisper base (local, free)", "language": res.get("language"), "elapsed_sec": round(time.time() - t0, 1),
               "segments": [{"id": s["id"], "start": s["start"], "end": s["end"], "text": s["text"], "avg_logprob": s["avg_logprob"], "no_speech_prob": s["no_speech_prob"],
                             "compression_ratio": s["compression_ratio"],
                             "words": [{"word": w["word"], "start": w["start"], "end": w["end"], "probability": w["probability"]} for w in s.get("words", [])]} for s in res["segments"]]},
              open(wj, "w"))
    print("done", vid, round(time.time() - t0, 1), "s")


if __name__ == "__main__":
    main(*sys.argv[1:4])
