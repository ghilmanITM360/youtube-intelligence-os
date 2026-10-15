"""Shared keyframe compositor for the three senior-health review previews.

Each video keeps its editable project in <video>/animation/project.py (scene/layer/keyframe data only).
This module rasterises the package's own SVG assets once (3x, via Sharp), composites frames with Pillow,
mixes the UNCHANGED source audio with a quiet locally synthesised bed + SFX, and encodes with ffmpeg.

  python3 <video>/animation/project.py test     -> bounded window render (qa/test_window.mp4)
  python3 <video>/animation/project.py render   -> full review MP4 + mobile MP4 + SRT + timeline + QA + contact sheet
"""
import csv, functools, hashlib, json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FPS, W, H, RASTER = 30, 1080, 1920, 3
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARP = os.environ.get("SHARP", "/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp")
INK, CORAL, TEAL, AMBER, GREY = (41, 42, 45), (200, 104, 85), (50, 124, 121), (196, 128, 20), (150, 150, 150)
CHALK = "/System/Library/Fonts/Supplemental/ChalkboardSE.ttc"
ARIALB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
REVIEW_MARKS = True  # review strip + claim flags; switch off only after owner + clinical sign-off


@functools.lru_cache(None)
def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def ease(u, kind="out"):
    u = min(1.0, max(0.0, u))
    if kind == "out":
        return 1 - (1 - u) ** 3
    if kind == "inout":
        return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2
    return u


class Video:
    def __init__(self, pkg, out_name, music_chords, music_seg=2.4):
        self.pkg = os.path.join(ROOT, pkg)
        self.name = pkg
        self.out_name = out_name
        self.anim = os.path.join(self.pkg, "animation")
        self.raster_dir = os.path.join(self.anim, "raster")
        self.reg = {a["asset_id"]: a for a in json.load(open(os.path.join(self.pkg, "assets/ASSET_REGISTER.json")))}
        self.words = [(float(r["start"]), float(r["end"]), r["word"].strip()) for r in
                      csv.DictReader(open(os.path.join(self.pkg, "script/WORDS_SMALL_EN.csv")))]
        ff = json.load(open(os.path.join(self.pkg, "source_audio/FFPROBE.json")))
        self.duration = float(ff["format"]["duration"])
        self.frames = round(self.duration * FPS)
        self.claims = list(csv.DictReader(open(os.path.join(self.pkg, "qa/MEDICAL_CLAIMS.csv"))))
        self.music_chords, self.music_seg = music_chords, music_seg
        self.scenes, self.sfx, self.caption_overrides, self.amber_spans = [], [], {}, []

    # ---------- timing helpers ----------
    def w(self, word, after=0.0, end=False):
        """Start (or end) time of the first ASR word matching `word` at/after `after`."""
        key = word.lower().strip(".,")
        for s, e, t in self.words:
            if s >= after - 1e-6 and t.lower().strip(".,?!") == key:
                return e if end else s
        raise KeyError(f"{word!r} after {after}")

    # ---------- assets ----------
    def raster(self, asset, part=None):
        name = f"{asset}--{part}" if part else asset
        out = os.path.join(self.raster_dir, name + ".png")
        if not os.path.exists(out):
            src = os.path.join(self.pkg, "assets/svg", ("parts/" + name) if part else name) + ".svg"
            os.makedirs(self.raster_dir, exist_ok=True)
            js = (f"require({json.dumps(SHARP)})({json.dumps(src)},{{density:{72 * RASTER}}}).png()"
                  f".toFile({json.dumps(out)}).catch(e=>{{console.error(e);process.exit(1)}})")
            subprocess.run(["node", "-e", js], check=True)
        return out

    @functools.lru_cache(None)
    def img(self, asset, part=None):
        im = Image.open(self.raster(asset, part)).convert("RGBA")
        a = self.reg[asset]
        if im.size != (a["width"] * RASTER, a["height"] * RASTER):
            im = im.resize((a["width"] * RASTER, a["height"] * RASTER), Image.LANCZOS)
        return im

    def part_center(self, asset, part, side="center"):
        """Pivot helper in asset-canvas units from the part's alpha bbox."""
        x0, y0, x1, y1 = self.img(asset, part).getchannel("A").getbbox()
        cx, cy = {"center": ((x0 + x1) / 2, (y0 + y1) / 2), "right": (x1 - (y1 - y0) / 2, (y0 + y1) / 2),
                  "left": (x0 + (y1 - y0) / 2, (y0 + y1) / 2)}[side]
        return cx / RASTER, cy / RASTER

    # ---------- scene building ----------
    def scene(self, sid, start, end, headline, label="", cam=(1.0, 1.035), cam_center=(540, 900)):
        sc = dict(id=sid, start=start, end=end, headline=headline, label=label, cam=cam,
                  cam_center=cam_center, layers=[])
        self.scenes.append(sc)
        return sc

    def layer(self, sc, asset, x, y, s, at=None, until=None, enter="cut", part=None, z=None, moves=(),
              loop=None, pivot=None, sfx=None, name=None, o=1.0):
        """x,y = asset-canvas top-left in world px at scale s. enter: cut|rise|pop|fade|wipe|slide_l|slide_r.
        moves: [(t0, t1, dict(x=,y=,s=,r=,o=))] absolute targets, eased. loop: ('bob',amp,period) |
        ('swing',deg,period) | ('spin',deg_per_s) | ('pulse',amp,[times])."""
        at = sc["start"] if at is None else at
        until = sc["end"] if until is None else until
        a = self.reg[asset]
        L = dict(name=name or f"{sc['id']}--{asset}" + (f"--{part}" if part else ""), asset=asset, part=part,
                 x=x, y=y, s=s, at=at, until=until, enter=enter, moves=list(moves), loop=loop,
                 pivot=pivot or a["anchors"]["pivot"], z=len(sc["layers"]) if z is None else z, o=o)
        sc["layers"].append(L)
        if sfx:
            self.sfx.append((at, sfx, L["name"]))
        return L

    def group(self, sc, asset, x, y, s, part_opts=None, **kw):
        """One layer per exported part (shared canvas registration); part_opts overrides per part."""
        out, snd = [], kw.pop("sfx", None)
        if snd:
            self.sfx.append((kw.get("at", sc["start"]), snd, f"{sc['id']}--{asset}"))
        for i, lay in enumerate(self.reg[asset]["layers"]):
            part = lay["id"].split("--", 1)[1]
            opts = dict(kw, **(part_opts or {}).get(part, {}))
            out.append(self.layer(sc, asset, x, y, s, part=part, **opts))
        return out

    # ---------- evaluation ----------
    def state(self, L, t):
        x, y, s, r, o = L["x"], L["y"], L["s"], 0.0, L["o"]
        for t0, t1, tgt in L["moves"]:
            if t >= t0:
                u = ease((t - t0) / max(1e-6, t1 - t0), "inout")
                x += (tgt.get("x", x) - x) * u; y += (tgt.get("y", y) - y) * u
                s += (tgt.get("s", s) - s) * u; r += (tgt.get("r", r) - r) * u; o += (tgt.get("o", o) - o) * u
        d = 8 / FPS
        u = ease((t - L["at"]) / d)
        wipe = 1.0
        if L["enter"] == "rise":
            y += 30 * (1 - u); o *= u
        elif L["enter"] == "pop":
            s *= 0.82 + 0.18 * u; o *= min(1, u * 1.6)
        elif L["enter"] == "fade":
            o *= u
        elif L["enter"] == "slide_l":
            x -= 60 * (1 - u); o *= u
        elif L["enter"] == "slide_r":
            x += 60 * (1 - u); o *= u
        elif L["enter"] == "wipe":
            wipe = ease((t - L["at"]) / (14 / FPS))
        lp = L["loop"]
        if lp:
            k = lp[0]
            if k == "bob":
                y += lp[1] * math.sin(2 * math.pi * (t - L["at"]) / lp[2])
            elif k == "swing":
                r += lp[1] * math.sin(2 * math.pi * (t - L["at"]) / lp[2])
            elif k == "spin":
                r -= lp[1] * (t - L["at"])
            elif k == "pulse":
                for tp in lp[2]:
                    if 0 <= t - tp < 0.5:
                        s *= 1 + lp[1] * math.sin(math.pi * (t - tp) / 0.5)
        return x, y, s, r, o, wipe

    @functools.lru_cache(maxsize=512)
    def transformed(self, asset, part, s, r, px, py):
        im = self.img(asset, part)
        k = s / RASTER
        im = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
        if abs(r) < 0.05:
            return im, 0, 0
        pad = int(max(im.size) * 0.6)
        big = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad))
        big.paste(im, (pad, pad))
        big = big.rotate(r, resample=Image.BICUBIC, center=(pad + px * s, pad + py * s))
        return big, -pad, -pad

    def draw_layer(self, canvas, L, t, cam):
        x, y, s, r, o, wipe = self.state(L, t)
        if o <= 0.01:
            return
        k, (cx, cy) = cam
        x, y, s = cx + (x - cx) * k, cy + (y - cy) * k, s * k
        im, ox, oy = self.transformed(L["asset"], L["part"], round(s, 3), round(r, 1), L["pivot"][0], L["pivot"][1])
        if o < 0.999 or wipe < 0.999:
            im = im.copy()
            if o < 0.999:
                im.putalpha(im.getchannel("A").point(lambda v: int(v * o)))
            if wipe < 0.999:
                m = Image.new("L", im.size, 0)
                ImageDraw.Draw(m).rectangle([0, 0, int(im.width * wipe), im.height], fill=255)
                im.putalpha(Image.composite(im.getchannel("A"), m, m))
        canvas.alpha_composite(im, (round(x + ox), round(y + oy)))

    # ---------- text ----------
    def draw_headline(self, d, canvas, sc, t):
        parts = sc["headline"]  # list of (text, colour)
        u = 1.0 if sc is self.scenes[0] else ease((t - sc["start"]) / (5 / FPS))  # hook headline readable at frame 0
        size = 104
        f = font(CHALK, size, 2)
        total = sum(d.textlength(p, font=f) for p, _ in parts)
        while total > 980 and size > 64:
            size -= 4; f = font(CHALK, size, 2); total = sum(d.textlength(p, font=f) for p, _ in parts)
        layer = Image.new("RGBA", (W, 200))
        ld = ImageDraw.Draw(layer)
        xx = (W - total) / 2
        for p, col in parts:
            ld.text((xx, 100), p, font=f, fill=col, anchor="lm"); xx += ld.textlength(p, font=f)
        if sc["label"]:
            fl = font(CHALK, 48, 1)
            ld.text((W / 2, 185), sc["label"], font=fl, fill=TEAL, anchor="mb")
        if u < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v: int(v * u)))
        canvas.alpha_composite(layer, (0, 170 + round(20 * (1 - u))))

    def caption_chunks(self):
        if hasattr(self, "_chunks"):
            return self._chunks
        ws = []
        for s, e, t in self.words:
            t = self.caption_overrides.get(round(s, 2), t)
            if t:
                ws.append((s, e, t))
        chunks, cur = [], []
        for i, (s, e, t) in enumerate(ws):
            cur.append((s, e, t))
            text = " ".join(x[2] for x in cur)
            nxt = ws[i + 1] if i + 1 < len(ws) else None
            brk = (nxt is None or t[-1] in ".,?!" or nxt[0] - e > 0.25 or len(text) >= 16
                   or len(text) + 1 + len(nxt[2]) > 24)
            if brk and not (nxt and t.lower() in ("a", "the", "of", "an", "to", "your", "that") and len(text) < 24):
                chunks.append(cur); cur = []
        out = []
        for i, c in enumerate(chunks):
            s0 = c[0][0]
            e0 = c[-1][1] + 0.35
            if i + 1 < len(chunks):
                e0 = min(e0, chunks[i + 1][0][0]) if chunks[i + 1][0][0] - c[-1][1] < 0.6 else e0
            out.append(dict(start=s0, end=min(e0, self.duration), words=c))
        self._chunks = out
        return out

    def amber(self, s):
        return any(a <= s + 1e-6 < b for a, b in self.amber_spans)

    def draw_caption(self, d, t):
        for c in self.caption_chunks():
            if c["start"] <= t < c["end"]:
                f = font(ARIALB, 74)
                text = " ".join(w[2] for w in c["words"])
                total = d.textlength(text, font=f)
                xx, y = (W - total) / 2, 1530
                cur = max((i for i, w in enumerate(c["words"]) if w[0] <= t), default=-1)
                for i, (s, e, wd) in enumerate(c["words"]):
                    col = AMBER if self.amber(s) else (CORAL if i == cur and t < e + 0.3 else INK)
                    d.text((xx, y), wd, font=f, fill=col, anchor="lm", stroke_width=9, stroke_fill=(255, 255, 255))
                    if self.amber(s):
                        lw = d.textlength(wd, font=f)
                        d.line([(xx, y + 46), (xx + lw, y + 46)], fill=AMBER, width=5)
                    xx += d.textlength(wd + " ", font=f)
                return

    def review_flags(self):
        out = []
        for c in self.claims:
            if c["status"] in ("CLINICIAN_REVIEW", "ASR_AND_CLINICIAN_REVIEW"):
                out.append((float(c["start_seconds"]), float(c["end_seconds"]), c["claim_id"], c["status"]))
        return out

    def draw_review(self, d, t):
        if not REVIEW_MARKS:
            return
        flag = next((f for f in self.review_flags() if f[0] <= t < f[1]), None)
        if flag:
            d.rectangle([0, 0, W, 64], fill=(252, 233, 196))
            msg = f"! {flag[2]} {flag[0]:.1f}-{flag[1]:.1f}s  " + (
                "ASR + clinical wording unverified" if flag[3].startswith("ASR") else "clinical review required")
            d.text((W / 2, 34), msg.upper(), font=font(ARIALB, 28), fill=(140, 80, 0), anchor="mm")
        else:
            d.rectangle([0, 0, W, 64], fill=(244, 244, 242))
            d.text((W / 2, 34), "REVIEW PREVIEW · NOT FOR PUBLICATION", font=font(ARIAL, 26), fill=GREY, anchor="mm")

    # ---------- frame ----------
    def frame(self, n):
        t = n / FPS
        sc = next((s for s in self.scenes if s["start"] <= t < s["end"]), self.scenes[-1])
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        u = ease((t - sc["start"]) / max(0.1, sc["end"] - sc["start"]), "inout")
        cam = (sc["cam"][0] + (sc["cam"][1] - sc["cam"][0]) * u, sc["cam_center"])
        for L in sorted(sc["layers"], key=lambda L: L["z"]):
            if L["at"] <= t < L["until"]:
                self.draw_layer(canvas, L, t, cam)
        d = ImageDraw.Draw(canvas)
        self.draw_headline(d, canvas, sc, t)
        self.draw_caption(d, t)
        self.draw_review(d, t)
        return canvas.convert("RGB")

    # ---------- audio ----------
    def audio(self):
        SR = 48000
        src = os.path.join(self.pkg, "source_audio/original_audio.m4a")
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        voice = np.frombuffer(raw, dtype="<f4").astype(float).reshape(-1, 2)
        n = int(SR * self.frames / FPS)
        voice = np.pad(voice, ((0, max(0, n - len(voice))), (0, 0)))[:n]
        mono = voice.mean(1)
        db = lambda x: 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)
        speech = db(mono[np.abs(mono) > 0.01])
        t = np.arange(n) / SR
        m = np.zeros(n)
        seg = self.music_seg
        for i in range(int(n / SR / seg) + 1):
            a, b = int(i * seg * SR), min(n, int(((i + 1) * seg + 0.5) * SR))
            if a >= n:
                break
            tt = t[a:b] - t[a]
            env = np.minimum(1, tt / 0.5) * np.minimum(1, np.maximum(0, (b - a) / SR - tt) / 0.5)
            ch = self.music_chords[i % len(self.music_chords)]
            for f in ch:
                m[a:b] += env * (np.sin(2 * np.pi * f * tt) + 0.2 * np.sin(4 * np.pi * f * tt)) / 3
            m[a:b] += 0.4 * np.exp(-tt / 0.35) * np.sin(2 * np.pi * ch[-1] * 2 * tt)
        m /= np.max(np.abs(m))
        m *= 10 ** ((speech - 22 - db(m)) / 20)
        fade = np.minimum(1, t / 0.4) * np.minimum(1, (n / SR - t) / 0.8)
        m *= fade
        fx = np.zeros(n)
        for ts, kind, _ in self.sfx:
            s = sfx_wave(kind, SR)
            s *= 10 ** ((speech - 16 - db(s)) / 20)
            a = int(ts * SR)
            fx[a:a + len(s)] += s[: max(0, n - a)]
        mix = voice + (m + fx)[:, None]
        peak = np.max(np.abs(mix))
        gain = min(1.0, 0.89 / peak)  # whole-mix gain only: voice wording/speed/pitch untouched
        mix *= gain
        path = os.path.join(self.anim, "build_mix.wav")
        with wave.open(path, "w") as wv:
            wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
            wv.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
        self.audio_report = dict(
            voice=dict(file="source_audio/original_audio.m4a", sha256=sha(src),
                       treatment=f"decoded unchanged; one whole-mix gain x{gain:.3f} to keep peak <= -1 dBFS; "
                                 "no trim, speed, pitch or word change"),
            source_music_check="source gaps measure ~-56 dB mean, noise floor ~-69 dB: no audible music bed in source "
                               "(measurement, not listening certification)",
            music=dict(source="synthesised in tools/anim.py from sine chords (no samples, no library track)",
                       chords_hz=self.music_chords, seconds_per_chord=seg, level_db_below_speech=22,
                       rights="created in this project; no third-party material; rights opinion not given"),
            sfx=[dict(t=round(a, 2), kind=k, event=e) for a, k, e in self.sfx],
            measured=dict(speech_rms_db=round(speech, 1), mix_peak=round(float(np.max(np.abs(mix))), 3)))
        return path

    # ---------- outputs ----------
    def render(self, f0=0, f1=None, out=None):
        f1 = self.frames if f1 is None else f1
        wav_path = self.audio()
        out = out or os.path.join(self.anim, self.out_name)
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
               "-r", str(FPS), "-i", "-", "-ss", f"{f0 / FPS:.4f}", "-t", f"{(f1 - f0) / FPS:.4f}", "-i", wav_path,
               "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for n in range(f0, f1):
            p.stdin.write(self.frame(n).tobytes())
        p.stdin.close()
        assert p.wait() == 0
        return out

    def timeline(self):
        tracks = []
        for sc in self.scenes:
            for L in sc["layers"]:
                keys = [dict(frame=round(L["at"] * FPS), x=L["x"], y=L["y"], scale=L["s"], entry=L["enter"])]
                keys += [dict(frame_in=round(a * FPS), frame_out=round(b * FPS), **tg) for a, b, tg in L["moves"]]
                tracks.append(dict(scene=sc["id"], layer=L["name"], asset=L["asset"], part=L["part"], z=L["z"],
                                   in_frame=round(L["at"] * FPS), out_frame_exclusive=round(L["until"] * FPS),
                                   pivot=L["pivot"], keys=keys, loop=L["loop"]))
        doc = dict(fps=FPS, width=W, height=H, frames=self.frames, duration_seconds=self.duration,
                   transform="world=cam_center+(xy-cam_center)*cam; rotate about pivot*scale; scale uniform",
                   scenes=[dict(id=s["id"], in_frame=round(s["start"] * FPS), out_frame_exclusive=round(s["end"] * FPS),
                                headline="".join(p for p, _ in s["headline"]), label=s["label"], camera=s["cam"])
                           for s in self.scenes],
                   tracks=tracks, sfx=[dict(t=a, kind=k, event=e) for a, k, e in self.sfx])
        json.dump(doc, open(os.path.join(self.anim, "KEYFRAME_TIMELINE.json"), "w"), indent=1)
        return doc

    def srt(self):
        def ts(x):
            ms = round(x * 1000)
            return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"
        lines = []
        for i, c in enumerate(self.caption_chunks(), 1):
            text = " ".join(w[2] for w in c["words"])
            lines.append(f"{i}\n{ts(c['start'])} --> {ts(c['end'])}\n{text}\n")
        open(os.path.join(self.anim, "CAPTIONS_REVIEW.srt"), "w").write("\n".join(lines))

    def qa(self, mp4):
        probe = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                           "stream=codec_name,width,height,r_frame_rate,pix_fmt,duration,nb_frames:format=duration,size",
                                           "-of", "json", mp4], capture_output=True, text=True).stdout)
        dec = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-f", "null", "-"], capture_output=True, text=True).stderr
        vol = subprocess.run(["ffmpeg", "-nostats", "-i", mp4, "-af", "volumedetect", "-f", "null", "-"],
                             capture_output=True, text=True).stderr
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", mp4, "-vf", "fps=10,scale=270:480", "-f", "rawvideo",
                              "-pix_fmt", "gray", "-"], capture_output=True).stdout
        fr = np.frombuffer(raw, np.uint8).reshape(-1, 480, 270).astype(float)
        stds = fr.std(axis=(1, 2))
        diffs = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
        cuts = [round(s["start"], 2) for s in self.scenes[1:]]
        big = [round((i + 1) / 10, 1) for i, v in enumerate(diffs) if v > 6]
        unplanned = [b for b in big if not any(abs(b - c) <= 0.15 for c in cuts)]
        rep = dict(file=os.path.basename(mp4), probe=probe, decode_errors=dec.strip() or "none",
                   max_volume=[l.split(":")[-1].strip() for l in vol.splitlines() if "max_volume" in l],
                   mean_volume=[l.split(":")[-1].strip() for l in vol.splitlines() if "mean_volume" in l],
                   min_frame_std_10fps=round(float(stds.min()), 1), blank_frames=int((stds < 8).sum()),
                   large_jumps_s=big, planned_cuts_s=cuts, unplanned_large_jumps_s=unplanned,
                   scenes=len(self.scenes), layer_tracks=sum(len(s["layers"]) for s in self.scenes),
                   unique_assets=len({L["asset"] for s in self.scenes for L in s["layers"]}),
                   caption_chunks=len(self.caption_chunks()), sfx=len(self.sfx), audio=self.audio_report)
        os.makedirs(os.path.join(self.anim, "qa"), exist_ok=True)
        json.dump(rep, open(os.path.join(self.anim, "qa/RENDER_QA.json"), "w"), indent=1)
        return rep

    def contact_sheet(self, mp4):
        times = [0.5, 1.5, 2.5] + [s["start"] + 0.8 * (s["end"] - s["start"]) for s in self.scenes]
        thumbs = []
        for tt in times:
            png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{tt:.2f}", "-i", mp4, "-frames:v", "1", "-vf",
                                  "scale=270:480", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
            import io
            thumbs.append((tt, Image.open(io.BytesIO(png)).convert("RGB")))
        cols = 6
        rows = math.ceil(len(thumbs) / cols)
        sheet = Image.new("RGB", (cols * 280 + 10, rows * 520 + 10), (228, 228, 224))
        d = ImageDraw.Draw(sheet)
        for i, (tt, im) in enumerate(thumbs):
            x, y = 10 + (i % cols) * 280, 10 + (i // cols) * 520
            sheet.paste(im, (x, y))
            d.text((x, y + 485), f"{tt:.2f}s", font=font(ARIAL, 22), fill=INK)
        sheet.save(os.path.join(self.anim, "CONTACT_SHEET.png"))

    def main(self, argv):
        mode = argv[1] if len(argv) > 1 else "render"
        if mode == "test":  # bounded window: hook + first transition (+ optional extra window)
            a, b = (float(argv[2]), float(argv[3])) if len(argv) > 3 else (0, 5)
            os.makedirs(os.path.join(self.anim, "qa"), exist_ok=True)
            out = self.render(round(a * FPS), round(b * FPS), os.path.join(self.anim, "qa/test_window.mp4"))
            print(out)
        elif mode == "still":  # PNG stills at given seconds
            os.makedirs(os.path.join(self.anim, "qa"), exist_ok=True)
            for s in argv[2:]:
                self.frame(round(float(s) * FPS)).save(os.path.join(self.anim, f"qa/still_{float(s):05.2f}.png"))
        else:
            mp4 = self.render()
            mob = mp4.replace(".mp4", "_MOBILE_540x960.mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp4, "-vf", "scale=540:960:flags=lanczos",
                            "-c:v", "libx264", "-crf", "22", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                            "-movflags", "+faststart", mob], check=True)
            self.timeline(); self.srt(); self.contact_sheet(mp4)
            rep = self.qa(mp4)
            json.dump(self.audio_report, open(os.path.join(self.anim, "AUDIO_PROVENANCE.json"), "w"), indent=1)
            os.remove(os.path.join(self.anim, "build_mix.wav"))
            print(json.dumps({k: rep[k] for k in ("decode_errors", "max_volume", "mean_volume", "min_frame_std_10fps",
                                                  "blank_frames", "unplanned_large_jumps_s", "layer_tracks",
                                                  "unique_assets", "scenes")}, indent=1))


def sfx_wave(kind, SR):
    t = np.arange(int(SR * {"pop": 0.12, "tick": 0.08, "chime": 0.9, "soft": 0.5}[kind])) / SR
    if kind == "pop":
        return np.exp(-t / 0.03) * np.sin(2 * np.pi * (520 - 1800 * t) * t)
    if kind == "tick":
        return np.exp(-t / 0.015) * np.sin(2 * np.pi * 1320 * t)
    if kind == "chime":
        return np.exp(-t / 0.25) * (np.sin(2 * np.pi * 784 * t) + 0.6 * np.sin(2 * np.pi * 1175 * t))
    return np.minimum(1, t / 0.05) * np.exp(-t / 0.15) * np.sin(2 * np.pi * 330 * t)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
