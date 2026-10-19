#!/usr/bin/env python3
"""Pass B: deterministic automated temporal + audio analysis of ONE source video.

Usage: python3 -I forensic_features.py <video_id> <repo_research_dir> <local_evidence_root> [--asr]

Reads the canonical file path/SHA256 from SOURCE_MEDIA_INVENTORY.csv, verifies the hash, decodes every
native frame once (streaming, reduced to a 180-px short side), and writes:
  <local_evidence_root>/<vid>/gray.npy        (N,H,W) uint8   - regenerable, kept outside Git
  <local_evidence_root>/<vid>/audio16k.wav, spectro.png, whisper.json (with --asr)
  <research_dir>/videos/<vid>/auto/frame_metrics.csv, audio_metrics.csv, AUTO_SUMMARY.json
Event segmentation lives in segment_events.py so thresholds can be tuned without re-decoding.
"""
import csv
import hashlib
import json
import os
import subprocess
import sys
import wave

import numpy as np

SHORT_SIDE = 180


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height,r_frame_rate,nb_frames", "-of", "json", path], capture_output=True, text=True)
    s = json.loads(r.stdout)["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return int(s["width"]), int(s["height"]), float(num) / float(den)


def decode_gray(path, w, h):
    """Stream every native frame as (h,w) uint8 gray, area-averaged. Returns (N,h,w) and mean RGB (N,3)."""
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-an", "-fps_mode", "passthrough", "-vf", "scale=%d:%d:flags=area" % (w, h),
           "-pix_fmt", "rgb24", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    fs = w * h * 3
    gray, rgbm = [], []
    while True:
        b = p.stdout.read(fs)
        if len(b) < fs:
            break
        a = np.frombuffer(b, np.uint8).reshape(h, w, 3)
        rgbm.append(a.reshape(-1, 3).mean(0))
        gray.append((a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114).astype(np.uint8))
    p.wait()
    return np.stack(gray), np.array(rgbm)


def frame_metrics(gray, fps):
    n, h, w = gray.shape
    g = gray.astype(np.int16)
    d = np.zeros(n, np.float32)
    ch = np.zeros(n, np.float32)
    cells = np.zeros((n, 8, 4), np.float32) if h >= w else np.zeros((n, 4, 8), np.float32)
    cr, cc = cells.shape[1], cells.shape[2]
    for i in range(1, n):
        diff = np.abs(g[i] - g[i - 1])
        d[i] = diff.mean()
        m = diff > 16
        ch[i] = m.mean()
        cells[i] = m[: h // cr * cr, : w // cc * cc].reshape(cr, h // cr, cc, w // cc).mean((1, 3))
    ink = (gray < 235).mean((1, 2)).astype(np.float32)
    dark = (gray < 60).mean((1, 2)).astype(np.float32)
    return d, ch, ink, dark, cells


def audio(path, out_dir):
    wav = os.path.join(out_dir, "audio16k.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", wav], check=True)
    with wave.open(wav) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768.0
    return wav, x


def audio_metrics(x, sr=16000, hop=0.05):
    n = int(sr * hop)
    k = len(x) // n
    seg = x[: k * n].reshape(k, n)
    rms = np.sqrt((seg ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(rms + 1e-9)
    spec = np.abs(np.fft.rfft(seg * np.hanning(n), axis=1))
    f = np.fft.rfftfreq(n, 1 / sr)
    def band(lo, hi):
        m = (f >= lo) & (f < hi)
        return 20 * np.log10(spec[:, m].mean(1) + 1e-9)
    lo, mid, hi = band(20, 300), band(300, 3400), band(3400, 8000)
    flux = np.r_[0, np.maximum(0, np.diff(np.log(spec + 1e-6), axis=0)).mean(1)]
    return db, lo, mid, hi, flux, hop


def spectrogram_png(x, path, sr=16000):
    from PIL import Image
    n, hop = 512, 256
    win = np.hanning(n)
    frames = (len(x) - n) // hop
    S = np.stack([np.abs(np.fft.rfft(x[i * hop: i * hop + n] * win)) for i in range(frames)]).T
    S = 20 * np.log10(S + 1e-6)
    S = np.clip((S - (S.max() - 80)) / 80, 0, 1)[::-1]
    S = S[:, : (S.shape[1] // 4) * 4].reshape(S.shape[0], -1, 4).mean(2)
    img = (np.stack([S, S ** 2, 1 - S], -1) * 255).astype(np.uint8)
    Image.fromarray(img).resize((min(img.shape[1], 2400), 320)).save(path)


def main(vid, rdir, ev_root, asr=False):
    inv = [r for r in csv.DictReader(open(os.path.join(rdir, "SOURCE_MEDIA_INVENTORY.csv")))
           if r["Video_ID"] == vid and r["Canonical_For_Analysis"] == "True"][0]
    src = os.path.join("/Users/ghilmankhan/Downloads/CasuallyFinance", inv["Relative_Path"])
    assert sha256(src) == inv["SHA256"], "source hash mismatch"
    ev = os.path.join(ev_root, vid)
    out = os.path.join(rdir, "videos", vid, "auto")
    os.makedirs(ev, exist_ok=True)
    os.makedirs(out, exist_ok=True)
    W, H, fps = probe(src)
    if H >= W:
        tw, th = SHORT_SIDE, int(round(SHORT_SIDE * H / W))
    else:
        th, tw = SHORT_SIDE, int(round(SHORT_SIDE * W / H))
    gray, rgbm = decode_gray(src, tw, th)
    np.save(os.path.join(ev, "gray.npy"), gray)
    d, ch, ink, dark, cells = frame_metrics(gray, fps)
    with open(os.path.join(out, "frame_metrics.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["frame", "t_sec", "mean_abs_diff", "changed_frac", "ink_frac", "dark_frac", "mean_r", "mean_g", "mean_b"])
        for i in range(len(gray)):
            w.writerow([i, round(i / fps, 4), round(float(d[i]), 4), round(float(ch[i]), 5), round(float(ink[i]), 4),
                        round(float(dark[i]), 4)] + [round(float(v), 1) for v in rgbm[i]])
    np.savez_compressed(os.path.join(ev, "cells.npz"), cells=cells)
    wav, x = audio(src, ev)
    db, lo, mid, hi, flux, hop = audio_metrics(x)
    with open(os.path.join(out, "audio_metrics.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t_sec", "rms_db", "low_db", "voice_db", "high_db", "flux"])
        for i in range(len(db)):
            w.writerow([round(i * hop, 3), round(float(db[i]), 1), round(float(lo[i]), 1), round(float(mid[i]), 1),
                        round(float(hi[i]), 1), round(float(flux[i]), 3)])
    spectrogram_png(x, os.path.join(ev, "spectro.png"))
    if asr:
        import whisper
        m = whisper.load_model("small.en", device="cpu")
        res = m.transcribe(wav, word_timestamps=True, condition_on_previous_text=False, fp16=False, language="en")
        json.dump(res, open(os.path.join(ev, "whisper.json"), "w"))
        words = [dict(w, segment=s["id"]) for s in res["segments"] for w in s["words"]]
        with open(os.path.join(out, "asr_words.csv"), "w", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(["word_index", "start_sec", "end_sec", "word", "probability", "segment"])
            for i, w_ in enumerate(words):
                wr.writerow([i, round(w_["start"], 3), round(w_["end"], 3), w_["word"].strip(), round(w_["probability"], 3), w_["segment"]])
    summ = {"video_id": vid, "source_sha256": inv["SHA256"], "source": inv["Relative_Path"], "fps": fps, "frames_decoded": int(len(gray)),
            "frames_ffprobe": int(inv["Video_Frames_Counted"]), "analysis_size": [tw, th], "source_size": [W, H],
            "duration_s": float(inv["Duration_S"]), "audio_samples": int(len(x)), "audio_s": round(len(x) / 16000, 3),
            "asr": "whisper small.en (cpu, word timestamps)" if asr else "not run"}
    json.dump(summ, open(os.path.join(out, "AUTO_SUMMARY.json"), "w"), indent=1)
    print(json.dumps(summ))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], "--asr" in sys.argv)
