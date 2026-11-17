"""Align the owner's narration MP3 against FINAL_SCRIPT.md (read-only on the MP3).

Produces AUDIO_ALIGNMENT.json: probe facts, level/clipping QA, measured pause map,
phrase segments (acoustic, silencedetect), script-vs-ASR comparison and ASR-derived
word anchors clamped to the measured phrases. Word anchors are PROVISIONAL: whisper DTW
token times are estimates (typically within ~0.1 s), not phonetic forced alignment.

Re-run unchanged for a corrected MP3:
  python3 build/align_audio.py <mp3> <FINAL_SCRIPT.md> <out.json> <work_dir> [gate.json]
Requires ffmpeg/ffprobe and whisper-cli with ggml-small.en.bin (path below).
"""
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

FPS = 30
MODEL = Path.home() / ".cache/hyperframes/whisper/models/ggml-small.en.bin"
SILENCE_DB, SILENCE_MIN_S = -45, 0.12


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True)


def frame(t):
    return round(t * FPS)


def norm(word):
    w = word.lower().replace("\u2019", "'").strip("\"\u201c\u201d.,:;?!")
    return {"12": "twelve", "0%": "zeropercent", "zero-percent": "zeropercent",
            "promotion's": "promotions"}.get(w, w)


def script_words(script_md):
    text = Path(script_md).read_text()
    body = text.split("## Complete narration", 1)[1].split("## Direction", 1)[0]
    sentences = []
    for para in [p.strip() for p in body.split("\n\n") if p.strip()]:
        # Split paragraphs into sentences at . ? ! followed by space/end (keeps quotes).
        sentences += [s for s in re.split(r"(?<=[.?!])\s+|(?<=[.?!][\u201d\"])\s+", para) if s]
    words = []
    for si, s in enumerate(sentences):
        for w in s.split():
            words.append({"display": w, "norm": norm(w), "sentence_index": si})
    return sentences, words


def silences(wav):
    err = subprocess.run(["ffmpeg", "-v", "info", "-i", wav, "-af",
                          f"silencedetect=noise={SILENCE_DB}dB:d={SILENCE_MIN_S}",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    return list(zip(starts, ends))


def main(mp3, script_md, out_json, work, gate_json=None):
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    data = Path(mp3).read_bytes()
    probe = json.loads(run(["ffprobe", "-v", "error", "-show_format", "-show_streams",
                            "-of", "json", mp3]).stdout)
    st, fmt = probe["streams"][0], probe["format"]
    wav16, wav24 = work / "vo_16k.wav", work / "vo_native.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-ar", "16000", "-ac", "1", str(wav16)])
    run(["ffmpeg", "-v", "error", "-y", "-i", mp3, str(wav24)])
    decoded = json.loads(run(["ffprobe", "-v", "error", "-show_entries",
                              "stream=duration_ts,sample_rate,duration", "-of", "json",
                              str(wav24)]).stdout)["streams"][0]
    duration = float(decoded["duration"])

    levels = subprocess.run(["ffmpeg", "-v", "info", "-i", mp3, "-af",
                             "astats=metadata=0,ebur128=peak=true", "-f", "null", "-"],
                            capture_output=True, text=True).stderr
    grab = lambda pat: float(re.findall(pat, levels)[-1])  # noqa: E731
    qa = {
        "sample_peak_dbfs": grab(r"Peak level dB: (-?[0-9.]+)"),
        "rms_dbfs": grab(r"RMS level dB: (-?[0-9.]+)"),
        "max_abs_sample": max(abs(grab(r"Max level: (-?[0-9.]+)")),
                              abs(grab(r"Min level: (-?[0-9.]+)"))),
        "flat_factor": grab(r"Flat factor: (-?[0-9.]+)"),
        "integrated_lufs": grab(r"I:\s+(-?[0-9.]+) LUFS"),
        "loudness_range_lu": grab(r"LRA:\s+(-?[0-9.]+) LU"),
        "true_peak_dbfs": grab(r"Peak:\s+(-?[0-9.]+) dBFS"),
    }
    qa["clipping_detected"] = qa["max_abs_sample"] >= 0.999 or qa["flat_factor"] > 0

    sil = silences(str(wav24))
    lead = sil[0][1] if sil and sil[0][0] == 0 else 0.0
    tail = duration - sil[-1][0] if sil and abs(sil[-1][1] - duration) < 0.02 else 0.0
    bounds = [0.0] + [t for s in sil for t in s] + [duration]
    phrases = []
    for a, b in zip(bounds[::2], bounds[1::2]):
        if b - a > 0.05:  # speech between consecutive silences
            phrases.append({"start_s": round(a, 3), "end_s": round(b, 3)})
    pauses = [{"start_s": round(a, 3), "end_s": round(b, 3), "duration_s": round(b - a, 3)}
              for a, b in sil if a > 0 and abs(b - duration) > 0.02]

    v = subprocess.run(["whisper-cli", "--version"], capture_output=True, text=True)
    version = v.stdout + v.stderr
    # -nfa is required: whisper.cpp silently skips DTW token times with flash attention.
    run(["whisper-cli", "-m", str(MODEL), "-f", str(wav16), "-l", "en", "-nfa",
         "--dtw", "small.en", "-ojf", "-of", str(work / "asr_dtw"), "-np"])
    asr = []  # words rebuilt from tokens; end = DTW time of the word's last spoken token
    for seg in json.loads((work / "asr_dtw.json").read_text())["transcription"]:
        for t in seg["tokens"]:
            txt = t["text"]
            if txt.startswith("[_") or not txt.strip():
                continue
            if re.fullmatch(r"[.,?!:;]+", txt.strip()):
                continue  # punctuation tokens carry no spoken timing
            if txt.startswith(" ") or not asr:
                asr.append({"text": txt.strip(), "dtw_end_s": t["t_dtw"] / 100, "p": t["p"]})
            else:
                asr[-1]["text"] += txt
                asr[-1]["dtw_end_s"] = t["t_dtw"] / 100
                asr[-1]["p"] = min(asr[-1]["p"], t["p"])
    if any(a["dtw_end_s"] < 0 for a in asr):
        sys.exit("DTW timestamps missing; check whisper-cli -nfa --dtw support")

    sentences, words = script_words(script_md)
    ops = difflib.SequenceMatcher(a=[w["norm"] for w in words],
                                  b=[norm(a["text"]) for a in asr], autojunk=False).get_opcodes()
    differences = []
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            for i, j in zip(range(i1, i2), range(j1, j2)):
                words[i]["asr_text"] = asr[j]["text"]
                words[i]["asr_probability"] = round(asr[j]["p"], 3)
                words[i]["dtw_end_s"] = asr[j]["dtw_end_s"]
        if tag != "equal":
            differences.append({"type": tag,
                                "script": " ".join(w["display"] for w in words[i1:i2]),
                                "asr": " ".join(a["text"] for a in asr[j1:j2]),
                                "script_word_indices": list(range(i1, i2))})

    # Phrase assignment: the narration pauses at punctuation, so punctuation chunks map 1:1
    # onto measured phrases when the counts agree; otherwise fall back to DTW proximity.
    chunk, chunks = 0, []
    for w in words:
        chunks.append(chunk)
        if re.search(r"[.,?!:][”\"]?$", w["display"]):
            chunk += 1
    if chunk == len(phrases):
        method = "PUNCTUATION_CHUNKS_MATCH_MEASURED_PAUSES_1_TO_1"
        for w, c in zip(words, chunks):
            w["phrase_index"] = c
    else:
        method = "FALLBACK_DTW_PROXIMITY_REVIEW_REQUIRED"
        for w in words:
            t = w.get("dtw_end_s", 0)
            w["phrase_index"] = min(range(len(phrases)), key=lambda k: max(
                phrases[k]["start_s"] - t, t - phrases[k]["end_s"], 0))
    for k, p in enumerate(phrases):
        members = [w for w in words if w["phrase_index"] == k]
        p["text"] = " ".join(w["display"] for w in members)
        t = p["start_s"]
        for n, w in enumerate(members):
            w["start_s"] = round(t, 3)
            last = n == len(members) - 1
            remaining = len(members) - n - 1  # keep >=40 ms for each later word
            end = p["end_s"] if last else min(max(w.get("dtw_end_s", t), t + 0.04),
                                               p["end_s"] - 0.04 * remaining)
            w["end_s"] = round(end, 3)
            t = end
        p["start_frame"], p["end_frame"] = frame(p["start_s"]), frame(p["end_s"])
    for i, w in enumerate(words):
        w["index"] = i
        w["start_frame"], w["end_frame"] = frame(w["start_s"]), frame(w["end_s"])
        w["timing_status"] = "PROVISIONAL_ASR_DTW_CLAMPED_TO_MEASURED_PHRASE"

    sentence_rows = []
    for si, s in enumerate(sentences):
        ws = [w for w in words if w["sentence_index"] == si]
        sentence_rows.append({"index": si, "text": s, "start_s": ws[0]["start_s"],
                              "end_s": ws[-1]["end_s"], "start_frame": ws[0]["start_frame"],
                              "end_frame": ws[-1]["end_frame"],
                              "timing_status": "MEASURED_PHRASE_EDGES"})

    out = {
        "schema": "finance-short-01/audio-alignment/v1",
        "fps": FPS,
        "frame_convention": "frame = round(seconds * 30); end_frame is exclusive",
        "source_audio": {
            "original_path": str(Path(mp3).resolve()),
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "codec": st["codec_long_name"], "sample_rate_hz": int(st["sample_rate"]),
            "channels": st["channels"], "bit_rate_bps": int(fmt["bit_rate"]),
            "container_duration_s": float(fmt["duration"]),
            "decoded_samples": int(decoded["duration_ts"]), "decoded_duration_s": duration,
            "total_frames_at_30fps": frame(duration),
            "modified": False,
        },
        "level_qa": qa,
        "silence_qa": {"threshold_db": SILENCE_DB, "min_silence_s": SILENCE_MIN_S,
                       "leading_silence_s": round(lead, 3), "trailing_silence_s": round(tail, 3),
                       "speech_start_s": phrases[0]["start_s"], "speech_end_s": phrases[-1]["end_s"],
                       "internal_pauses": pauses},
        "asr": {"engine": version.strip().splitlines()[0] if version.strip() else "whisper.cpp",
                "model": MODEL.name, "prompt": None, "decoding": "unprompted; -nfa --dtw small.en",
                "transcript": " ".join(a["text"] for a in asr)},
        "script_comparison": {
            "script_words": len(words),
            "asr_words": len(asr),
            "differences": differences,
            "normalizations_treated_as_equal": ["12 = twelve", "0% = zero-percent",
                                                "promotions = promotion's (apostrophe inaudible)",
                                                "punctuation ignored"],
        },
        "phrase_assignment_method": method,
        "sentences": sentence_rows,
        "phrases": phrases,
        "words": words,
    }
    if gate_json:  # manually verified pronunciation evidence, kept separate from ASR output
        out["pronunciation_gate"] = json.loads(Path(gate_json).read_text())
    Path(out_json).write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"duration={duration}s phrases={len(phrases)} words={len(words)} "
          f"differences={[(d['script'], d['asr']) for d in differences]}")


if __name__ == "__main__":
    main(*sys.argv[1:6])
