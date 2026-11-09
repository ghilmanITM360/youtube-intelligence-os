"""Stage A3: signal-level soundtrack analysis (NOT auditory listening): loudness envelope, pauses, speech-vs-nonspeech onsets, bed-level estimate,
transient/SFX candidates and spectrogram strips for visual inspection. Outputs audio_auto.json + spectrogram PNGs in the work dir.
Usage: python3 -B stage_audio_features.py <VIDEO_ID> <WORK_ROOT>
"""
import json, sys, wave
from pathlib import Path
import numpy as np

SR = 22050; NFFT = 1024; HOP = 512


def load(p):
    with wave.open(str(p)) as w:
        assert w.getframerate() == SR and w.getnchannels() == 1
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0


def stft_mag(x):
    win = np.hanning(NFFT).astype(np.float32); n = 1 + (len(x) - NFFT) // HOP
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return np.abs(np.fft.rfft(x[idx] * win, axis=1)).astype(np.float32)


def main(vid, work_root):
    work = Path(work_root) / vid
    x = load(work / "audio22k.wav"); S = stft_mag(x); n = len(S); hz = np.fft.rfftfreq(NFFT, 1 / SR); dt = HOP / SR
    P = S ** 2 + 1e-12
    rms_db = 10 * np.log10(P.sum(1) / NFFT ** 2 * 2 + 1e-12)
    band = lambda lo, hi: 10 * np.log10(P[:, (hz >= lo) & (hz < hi)].sum(1) / NFFT ** 2 * 2 + 1e-12)
    low, mid, high = band(20, 200), band(200, 3000), band(3000, 10000)
    cent = (S * hz).sum(1) / (S.sum(1) + 1e-9)
    flat = np.exp(np.log(S[:, (hz > 100) & (hz < 8000)] + 1e-9).mean(1)) / (S[:, (hz > 100) & (hz < 8000)].mean(1) + 1e-9)
    flux = np.maximum(np.log1p(S[:, 1:]) - np.log1p(np.roll(S, 1, axis=0)[:, 1:]), 0).sum(1); flux[0] = 0
    words = []
    wj = work / "whisper.json"
    if wj.exists():
        for s in json.load(open(wj))["segments"]:
            words += [(w["start"], w["end"]) for w in s["words"]]
    speech = np.zeros(n, dtype=bool)
    for a, b in words: speech[int(max(a - 0.04, 0) / dt): int(b / dt) + 2] = True
    t = np.arange(n) * dt
    # pauses = gaps between words >= 0.35 s (and non-speech lead/tail)
    pauses = []
    prev = 0.0
    for a, b in words + [(len(x) / SR, len(x) / SR)]:
        if a - prev >= 0.35:
            sl = slice(int((prev + 0.05) / dt), max(int((a - 0.05) / dt), int((prev + 0.05) / dt) + 1))
            pauses.append(dict(start=round(prev, 3), end=round(a, 3), dur=round(a - prev, 3), rms_db_mean=round(float(rms_db[sl].mean()), 1), flatness=round(float(flat[sl].mean()), 3), low_db=round(float(low[sl].mean()), 1)))
        prev = max(prev, b)
    # bed estimate per second: 10th percentile loudness
    sec = int(len(x) / SR)
    bed = [round(float(np.percentile(rms_db[int(s / dt): int((s + 1) / dt)], 10)), 1) for s in range(sec)]
    spk = [round(float(np.percentile(rms_db[int(s / dt): int((s + 1) / dt)], 90)), 1) for s in range(sec)]
    # onsets
    thr_med = np.median(flux); mad = np.median(np.abs(flux - thr_med)) + 1e-6
    z = (flux - thr_med) / mad
    cand = [i for i in range(2, n - 2) if z[i] > 12 and flux[i] >= flux[i - 1] and flux[i] >= flux[i + 1]]
    events, last = [], -1
    for i in cand:
        ts = i * dt
        if ts - last < 0.18: continue
        last = ts
        s0, s1 = i, min(i + int(0.15 / dt), n - 1)
        under = bool(speech[max(i - 2, 0): i + 8].any())
        events.append(dict(t=round(ts, 3), z=round(float(z[i]), 1), under_speech=under, low_db=round(float(low[s0:s1].max()), 1), mid_db=round(float(mid[s0:s1].max()), 1), high_db=round(float(high[s0:s1].max()), 1),
                           high_minus_mid=round(float(high[s0:s1].max() - mid[s0:s1].max()), 1), centroid=round(float(cent[s0:s1].mean()), 0), flatness=round(float(flat[s0:s1].mean()), 3), rms_db=round(float(rms_db[s0:s1].max()), 1)))
    json.dump(dict(video_id=vid, sr=SR, hop_sec=dt, duration=round(len(x) / SR, 3), n_words=len(words), pauses=pauses, bed_p10_db_per_sec=bed, speech_p90_db_per_sec=spk, onsets=events,
                   global_stats=dict(rms_db_median=round(float(np.median(rms_db)), 1), rms_db_p10=round(float(np.percentile(rms_db, 10)), 1), rms_db_p90=round(float(np.percentile(rms_db, 90)), 1), flux_median=float(thr_med), flux_mad=float(mad))),
              open(work / "audio_auto.json", "w"))
    # spectrogram strips: 120 s per strip, 1920 px wide
    from PIL import Image, ImageDraw
    db = 20 * np.log10(S[:, : int(8000 / (SR / NFFT))] + 1e-6); db = np.clip((db - db.max() + 80) / 80, 0, 1)
    img_full = (db.T[::-1] * 255).astype(np.uint8)  # freq up
    strip_sec, W = 120, 1920; per_img = 5; spd = 1.0 / dt
    strips = []
    for k in range(int(np.ceil(len(x) / SR / strip_sec))):
        a, b = int(k * strip_sec * spd), int(min((k + 1) * strip_sec * spd, n))
        seg = img_full[:, a:b]
        span_px = max(1, min(W, round((b-a) * dt / strip_sec * W)))
        im = Image.new("RGB", (W, 150), "black")
        im.paste(Image.fromarray(seg).resize((span_px, 150), Image.BILINEAR).convert("RGB"), (0, 0))
        d = ImageDraw.Draw(im)
        for s in range(0, strip_sec + 1, 10):
            x0 = int(s / strip_sec * W); d.line([x0, 0, x0, 8], fill=(255, 255, 0)); d.text((x0 + 2, 8), f"{k * strip_sec + s}s", fill=(255, 255, 0))
        for e in events:
            if k * strip_sec <= e["t"] < (k + 1) * strip_sec:
                x0 = int((e["t"] - k * strip_sec) / strip_sec * W); d.line([x0, 140, x0, 150], fill=(255, 60, 60) if not e["under_speech"] else (60, 160, 255))
        # speech mask ribbon at the bottom
        for a_, b_ in words:
            if k * strip_sec <= a_ < (k + 1) * strip_sec:
                x0 = int((a_ - k * strip_sec) / strip_sec * W); x1 = int((min(b_, (k + 1) * strip_sec) - k * strip_sec) / strip_sec * W); d.line([x0, 136, x1, 136], fill=(0, 255, 0))
        strips.append(im)
    for j in range(0, len(strips), per_img):
        sheet = Image.new("RGB", (W, 150 * len(strips[j: j + per_img])))
        for q, im in enumerate(strips[j: j + per_img]): sheet.paste(im, (0, 150 * q))
        sheet.save(work / f"spectro_{j // per_img + 1:02d}.png")
    print(vid, "onsets", len(events), "non-speech onsets", sum(not e["under_speech"] for e in events), "pauses>=0.35s", len(pauses), "bed_db median", np.median(bed), "spectro", len(strips), "strips")


if __name__ == "__main__":
    main(*sys.argv[1:3])
