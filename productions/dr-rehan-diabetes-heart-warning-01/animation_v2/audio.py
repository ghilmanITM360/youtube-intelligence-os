"""Original music bed + SFX (synthesised here from sine waves/noise, no samples) and preview mix.

  python3 audio.py  -> audio/music_bed.wav, audio/sfx.wav, audio/mix_preview.wav, audio/AUDIO_MIX.json
The voice is ~/Downloads/1015.mp3, decoded read-only; it is never edited, trimmed, pitched or re-timed.
"""
import hashlib, json, os, subprocess, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audio")
SR, DUR = 48000, 45.5
MP3 = os.path.expanduser("~/Downloads/1015.mp3")
SFX = [  # (time s, kind, reason) — aligned to visual events in v2.py
    (0.25, "low", "hook: warning glow"), (3.35, "chime", "headline: warning signs"), (5.9, "pop", "doctor enters"),
    (10.35, "tick", "symptom 1"), (10.9, "tick", "symptom 2"), (11.45, "tick", "symptom 3"), (12.0, "tick", "symptom 4"),
    (16.65, "pop", "exertion arrow"), (18.85, "chime", "get it checked"),
    (21.95, "pop", "group 1"), (23.75, "pop", "group 2"), (26.45, "pop", "group 3"),
    (33.75, "low", "heart diagram"), (34.6, "tick", "artery marker"), (36.15, "chime", "sudden symptoms"),
    (38.9, "pop", "emergency phone"), (39.6, "chime", "takeaway"),
]


def tone(f, d, amp, att=0.005, rel=None):
    t = np.arange(int(SR * d)) / SR
    env = np.minimum(1, t / att) * np.exp(-t / (rel or d / 4))
    return amp * env * np.sin(2 * np.pi * f * t)


def sfx(kind):
    if kind == "pop":
        t = np.arange(int(SR * 0.12)) / SR
        return 0.35 * np.exp(-t / 0.03) * np.sin(2 * np.pi * (520 - 1800 * t) * t)
    if kind == "tick":
        return tone(1320, 0.08, 0.18, rel=0.015)
    if kind == "chime":
        return tone(784, 0.9, 0.16, rel=0.25) + tone(1175, 0.9, 0.10, rel=0.2)
    if kind == "low":
        return tone(110, 1.2, 0.30, att=0.08, rel=0.4) + tone(220, 1.2, 0.08, att=0.08, rel=0.3)


def music():
    n = int(SR * DUR)
    t = np.arange(n) / SR
    chords = [(220.0, 261.6, 329.6), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7), (164.8, 207.7, 246.9)]  # Am F G E
    seg = 2.8
    out = np.zeros(n)
    for i in range(int(DUR / seg) + 1):
        a, b = int(i * seg * SR), min(n, int((i + 1) * seg * SR + 0.6 * SR))
        if a >= n:
            break
        tt = t[a:b] - t[a]
        env = np.minimum(1, tt / 0.6) * np.minimum(1, np.maximum(0, (b - a) / SR - tt) / 0.6)
        for f in chords[i % 4]:
            out[a:b] += env * (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt)) / 3
        # soft plucked note on each chord change
        out[a:b] += 0.5 * tone(chords[i % 4][2] * 2, (b - a) / SR, 0.5, rel=0.5)[: b - a]
    out /= np.max(np.abs(out))
    return out


def wav(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def db(x):
    return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    sha = hashlib.sha256(open(MP3, "rb").read()).hexdigest()
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", MP3, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    voice = np.frombuffer(raw, dtype="<f4").astype(float)
    n = int(SR * DUR)
    voice = np.pad(voice, (0, max(0, n - len(voice))))[:n]
    m = music()
    # music level: about -20 dB under speech RMS while speaking; lifted slightly in the speech-free tail
    speech_rms = db(voice[: int(SR * 38.6)])
    gain = 10 ** ((speech_rms - 20 - db(m)) / 20)
    tail = np.ones(n); tail[int(SR * 38.6):] = 1.6
    m = m * gain * tail
    fx = np.zeros(n)
    for ts, kind, _ in SFX:
        s = sfx(kind) * 10 ** ((speech_rms - 14 - db(sfx(kind))) / 20)
        a = int(ts * SR); fx[a:a + len(s)] += s[: n - a]
    mix = voice + m + fx
    peak = np.max(np.abs(mix))
    if peak > 0.89:  # whole-mix gain only (voice timing/pitch untouched)
        mix *= 0.89 / peak
    wav(os.path.join(OUT, "music_bed.wav"), m)
    wav(os.path.join(OUT, "sfx.wav"), fx)
    wav(os.path.join(OUT, "mix_preview.wav"), mix)
    json.dump(dict(voice=dict(file="1015.mp3 (owner-supplied, not committed)", sha256=sha, sha_matches_record=
                              sha == "8f9e39ab409959d4e06f99052860cf4391d56a7ab6caa85f560217d35cc3daf5",
                              treatment="decoded read-only, full length, no trim/pitch/speed/word change"),
                   music=dict(source="original, synthesised by audio.py (sine chords Am-F-G-E, 2.8 s per chord)",
                              rights="created in this project; no third-party samples or library tracks",
                              level_db_below_speech=20),
                   sfx=[dict(t=t, kind=k, why=r) for t, k, r in SFX],
                   measured=dict(speech_rms_db=round(speech_rms, 1), music_rms_db=round(db(m[: int(SR * 38.6)]), 1),
                                 mix_peak=round(float(np.max(np.abs(mix))), 3), whole_mix_gain=round(min(1, 0.89 / peak), 3)),
                   trim_proposal="Speech ends ~38.6 s. Proposed publish trim: end at ~42.0 s (3.4 s takeaway hold) — "
                                 "NOT applied; needs owner approval."),
              open(os.path.join(OUT, "AUDIO_MIX.json"), "w"), indent=1)
    print("speech", round(speech_rms, 1), "dB; peak", round(peak, 3))
