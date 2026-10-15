"""Derive a gently re-paced voice WORKING COPY from the unchanged source audio.

Plan ops (source seconds, splice points must sit in measured silences):
  ("keep", a, b)            copy unchanged
  ("tempo", a, b, rate)     ffmpeg atempo (WSOLA, pitch-preserving); rate < 1 slows
  ("pause", dur)            insert digital silence (inside an existing pause)
Every join gets a 6 ms fade-out/fade-in; the file start gets an 8 ms fade-in.
Returns the piecewise-linear source->derived time map used to retime words, captions and keyframes.
"""
import hashlib, json, os, subprocess, wave
import numpy as np

SR = 48000
FADE = int(0.006 * SR)


def decode(src):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype="<f4").astype(np.float32).reshape(-1, 2)


def atempo(x, rate):
    p = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                        "-af", f"atempo={rate}", "-f", "f32le", "-"], input=x.tobytes(), capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype="<f4").reshape(-1, 2)


def fades(x):
    x = x.copy()
    r = np.linspace(0, 1, min(FADE, len(x)))[:, None]
    x[:len(r)] *= r
    x[len(x) - len(r):] *= r[::-1]
    return x


def derive(src, plan, out_wav):
    x = decode(src)
    parts, tmap, dst = [], [], 0.0
    for op in plan:
        if op[0] == "pause":
            seg = np.zeros((int(op[1] * SR), 2), np.float32)
            tmap.append(dict(op="pause", src=[None, None], dst=[round(dst, 5), round(dst + len(seg) / SR, 5)]))
        else:
            a, b = op[1], op[2]
            seg = x[int(a * SR):int(b * SR)]
            if op[0] == "tempo":
                seg = atempo(seg, op[3])
            tmap.append(dict(op=op[0], rate=op[3] if op[0] == "tempo" else 1.0, src=[a, b],
                             dst=[round(dst, 5), round(dst + len(seg) / SR, 5)]))
        parts.append(fades(seg))
        dst += len(seg) / SR
    y = np.concatenate(parts)
    y[:int(0.008 * SR)] *= np.linspace(0, 1, int(0.008 * SR))[:, None]
    with wave.open(out_wav, "w") as wv:
        wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
        wv.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes())
    return dict(source=os.path.basename(src), source_sha256=sha(src), derived=os.path.basename(out_wav),
                derived_sha256=sha(out_wav), derived_seconds=round(len(y) / SR, 5), source_seconds=round(len(x) / SR, 5),
                method="ffmpeg atempo (WSOLA time-scale modification, pitch-preserving) on listed spans only; "
                       "6 ms micro-fades at every splice; 8 ms fade-in at file start; inserted pauses are digital silence",
                ffmpeg=subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True).stdout.split("\n")[0],
                plan=[list(p) for p in plan], time_map=tmap)


def remap(tmap, t):
    """Source seconds -> derived seconds (linear inside each span)."""
    for m in tmap:
        a, b = m["src"]
        if a is not None and a - 1e-9 <= t <= b + 1e-9:
            return m["dst"][0] + (t - a) * (m["dst"][1] - m["dst"][0]) / (b - a)
    last = [m for m in tmap if m["src"][0] is not None][-1]
    return last["dst"][1] + (t - last["src"][1])


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


if __name__ == "__main__":  # self-check of the time map
    tm = [dict(op="tempo", rate=0.9, src=[0, 0.9], dst=[0, 1.0]), dict(op="pause", src=[None, None], dst=[1.0, 1.2]),
          dict(op="keep", rate=1, src=[0.9, 2.0], dst=[1.2, 2.3])]
    assert abs(remap(tm, 0.45) - 0.5) < 1e-9 and abs(remap(tm, 0.9) - 1.0) < 1e-9 and abs(remap(tm, 1.5) - 1.8) < 1e-9
    assert abs(remap(tm, 2.5) - 2.8) < 1e-9
    print("ok")
