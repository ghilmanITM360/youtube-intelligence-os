"""V2 keyframe compositor for the three senior-health review videos (V1 engine tools/anim.py stays untouched).

Changes from V1 (see each package's animation/v2/CORRECTION_LOG_V1_V2.md):
  - layers live on one global timeline (a layer may span scene/headline changes -> no pose/position pops)
  - parent-child layers (props stay attached to a moving character), text layers, run-cycle loops with
    speed keys, wipe_up/grow entrances, eased exits, global camera keys that hold during reading
  - verified caption text (word corrections by index) shown as phrase-level two-line cues with minimum duration,
    placed above the Shorts UI zone; no review strip, claim IDs or amber QA marks in frames (QA files only)
  - optional derived voice (tools/voice_stretch.py) with a source->derived time map applied to every word time

  python3 <video>/animation/project_v2.py render | test A B | still t1 t2 ...
"""
import csv, functools, hashlib, io, json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voice_stretch import remap  # noqa: E402

FPS, W, H, RASTER = 30, 1080, 1920, 3
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARP = os.environ.get("SHARP", "/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp")
INK, CORAL, TEAL, AMBER, GREY = (41, 42, 45), (200, 104, 85), (50, 124, 121), (196, 128, 20), (150, 150, 150)
CHALK = "/System/Library/Fonts/Supplemental/ChalkboardSE.ttc"
ARIALB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
UNI = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # fallback for glyphs Arial Bold lacks (subscript 2)
CAP_Y, CAP_SIZE, CAP_LINE = 1330, 66, 80   # caption block top; bottom stays <= ~1500 (above Shorts title/UI zone)
HEAD_Y = 150


@functools.lru_cache(None)
def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def ease(u, kind="out"):
    u = min(1.0, max(0.0, u))
    if kind == "out":
        return 1 - (1 - u) ** 3
    if kind == "inout":
        return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2
    if kind == "back":  # small settle, used sparingly for badge entrances
        c = 1.4
        return 1 + (c + 1) * (u - 1) ** 3 + c * (u - 1) ** 2
    return u


class Video:
    def __init__(self, pkg, out_name, music_chords, music_seg=2.4, voice=None, word_fix=None, cue_breaks=()):
        self.pkg = os.path.join(ROOT, pkg)
        self.name, self.out_name = pkg, out_name
        self.anim = os.path.join(self.pkg, "animation/v2")
        self.raster_dir = os.path.join(self.pkg, "animation/raster")  # shared derived cache; V1 files never rewritten
        self.reg = {a["asset_id"]: a for a in json.load(open(os.path.join(self.pkg, "assets/ASSET_REGISTER.json")))}
        self.src_audio = os.path.join(self.pkg, "source_audio/original_audio.m4a")
        self.voice = os.path.join(self.pkg, voice) if voice else None
        self.pacing = json.load(open(os.path.join(self.anim, "VOICE_PACING.json"))) if voice else None
        tm = (lambda t: remap(self.pacing["time_map"], t)) if voice else (lambda t: t)
        self.T = tm  # source seconds -> output seconds
        raw = [(float(r["start"]), float(r["end"]), r["word"].strip()) for r in
               csv.DictReader(open(os.path.join(self.pkg, "script/WORDS_SMALL_EN.csv")))]
        self.asr_words = raw
        fix = word_fix or {}
        self.words, self.breaks = [], set()  # breaks: output word positions that end a caption cue (phrase edits)
        for i, (s, e, t) in enumerate(raw):
            t = fix.get(i, t)
            if t:  # "" removes an ASR token; "a b" keeps one timing span for a corrected multi-word token
                self.words.append((tm(s), tm(e), t))
                if i in cue_breaks:
                    self.breaks.add(len(self.words) - 1)
        self.corrections = [dict(index=i, asr=raw[i][2], shown=v, src_start=raw[i][0]) for i, v in sorted(fix.items())]
        ff = json.load(open(os.path.join(self.pkg, "source_audio/FFPROBE.json")))
        self.duration = self.pacing["derived_seconds"] if voice else float(ff["format"]["duration"])
        self.frames = round(self.duration * FPS)
        self.music_chords, self.music_seg = music_chords, music_seg
        self.scenes, self.layers, self.sfx, self.cam_keys = [], [], [], [(0, 1.0, 540, 900)]

    # ---------- timing ----------
    def w(self, word, after=0.0, end=False):
        """Output-time start (or end) of the first shown word matching `word` at/after `after` (output seconds)."""
        key = word.lower().strip(".,?!")
        for s, e, t in self.words:
            if s >= after - 1e-6 and t.lower().strip(".,?!") == key:
                return e if end else s
        raise KeyError(f"{word!r} after {after}")

    def aw(self, word, after=0.0, end=False):
        """Like w() but over the raw ASR tokens (mapped to output time); for tokens merged/hidden in captions."""
        key = word.lower().strip(".,?!")
        for s, e, t in self.asr_words:
            if self.T(s) >= after - 1e-6 and t.lower().strip(".,?!") == key:
                return self.T(e) if end else self.T(s)
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
        if isinstance(asset, tuple):  # ("text", text, size, colour, font, align)
            _, text, size, col, fp, _al = asset
            f = font(fp, size * RASTER, 2 if fp == CHALK else 0)
            lines = text.split("\n")
            d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
            wd = max(d0.textlength(l, font=f) for l in lines)
            lh = int(size * RASTER * 1.18)
            im = Image.new("RGBA", (int(wd) + 12 * RASTER, lh * len(lines) + 12 * RASTER))
            d = ImageDraw.Draw(im)
            for i, l in enumerate(lines):
                d.text((im.width / 2, 6 * RASTER + lh * i + lh / 2), l, font=f, fill=col, anchor="mm",
                       stroke_width=3 * RASTER, stroke_fill=(255, 255, 255))
            return im
        im = Image.open(self.raster(asset, part)).convert("RGBA")
        a = self.reg[asset]
        if im.size != (a["width"] * RASTER, a["height"] * RASTER):
            im = im.resize((a["width"] * RASTER, a["height"] * RASTER), Image.LANCZOS)
        return im

    def part_center(self, asset, part, side="center"):
        x0, y0, x1, y1 = self.img(asset, part).getchannel("A").getbbox()
        return {"center": ((x0 + x1) / 2, (y0 + y1) / 2), "bottom": ((x0 + x1) / 2, y1)}[side][0] / RASTER, \
            {"center": ((x0 + x1) / 2, (y0 + y1) / 2), "bottom": ((x0 + x1) / 2, y1)}[side][1] / RASTER

    # ---------- building ----------
    def scene(self, sid, start, end, headline, label=""):
        sc = dict(id=sid, start=start, end=end, headline=headline, label=label)
        self.scenes.append(sc)
        return sc

    def cam(self, t, k, cx=540, cy=900, dur=0.6):
        """Camera key: hold the previous framing, then ease over `dur` seconds to arrive at (k,cx,cy) at time t."""
        self.cam_keys.append((t, k, cx, cy, dur))

    def layer(self, sc, asset, x, y, s, at=None, until=None, enter="cut", exit="cut", part=None, z=0, moves=(),
              loop=None, pivot=None, sfx=None, name=None, o=1.0, parent=None, speed=None, enter_dur=8):
        """x,y = asset-canvas top-left in world px at scale s (parent: x,y relative to parent's x,y).
        enter: cut|rise|pop|fade|slide_l|slide_r|wipe|wipe_up|grow ; exit: cut|fade|sink (8 frames before until).
        moves: [(t0,t1,dict(x,y,s,r,o), ease?)] ; loop: ('bob',amp,period) | ('hop',amp,period) |
        ('swing',deg,period[,phase]) | ('spin',deg_per_s) | ('pulse',amp,[times]) ; speed: [(t,factor)] for loop time."""
        at = sc["start"] if at is None else at
        until = sc["end"] if until is None else until
        if isinstance(asset, tuple):
            im = self.img(asset)
            pv = (im.width / RASTER / 2, im.height / RASTER / 2)
        else:
            pv = self.reg[asset]["anchors"]["pivot"]
        nm = name or (f"{sc['id']}--{asset}" + (f"--{part}" if part else "") if not isinstance(asset, tuple)
                      else f"{sc['id']}--text--{asset[1][:18]}")
        L = dict(name=nm, asset=asset, part=part, x=x, y=y, s=s, at=at, until=until, enter=enter, exit=exit,
                 moves=list(moves), loop=loop, pivot=pivot or pv, z=z, o=o, parent=parent, speed=speed,
                 enter_dur=enter_dur, scene=sc["id"])
        self.layers.append(L)
        if sfx:
            self.sfx.append((at, sfx, L["name"]))
        return L

    def text(self, sc, text, cx, cy, size=46, col=INK, fp=CHALK, **kw):
        """Text layer centred at (cx,cy) world px (not camera-exempt: it is part of the illustrated stage)."""
        key = ("text", text, size, col, fp, "c")
        im = self.img(key)
        return self.layer(sc, key, cx - im.width / RASTER / 2, cy - im.height / RASTER / 2, 1.0, **kw)

    def group(self, sc, asset, x, y, s, part_opts=None, **kw):
        out, snd = [], kw.pop("sfx", None)
        if snd:
            self.sfx.append((kw.get("at", sc["start"]), snd, f"{sc['id']}--{asset}"))
        for lay in self.reg[asset]["layers"]:
            part = lay["id"].split("--", 1)[1]
            opts = dict(kw, **(part_opts or {}).get(part, {}))
            if opts.pop("skip", False):
                continue
            px, py = x + opts.pop("dx", 0), y + opts.pop("dy", 0)  # per-part offset (e.g. move a window)
            out.append(self.layer(sc, asset, px, py, s, part=part, **opts))
        return out

    def character(self, sc, asset, x, y, s, run=None, **kw):
        """Character as part layers sharing one parent transform. run=(period, arm_deg) adds a run cycle:
        arms swing about the shoulders in opposite phase, body hops twice per stride, legs rock about the hips."""
        body = self.layer(sc, asset, x, y, s, name=f"{sc['id']}--{asset}--root", o=0.0, **kw)  # invisible parent
        kids = []
        sh = self.reg[asset]["anchors"].get("shoulders") or [[143, 244], [258, 244]]
        for lay in self.reg[asset]["layers"]:
            part = lay["id"].split("--", 1)[1]
            loop, pivot = None, None
            if run:
                per, deg = run
                if part == "rear-arm":
                    loop, pivot = ("swing", deg, per, 0.5), sh[0]
                elif part == "front-arm":
                    loop, pivot = ("swing", deg, per, 0.0), sh[1]
                elif part == "legs":
                    loop, pivot = ("swing", 3.5, per, 0.25), (200, 380)
            kids.append(self.layer(sc, asset, 0, 0, s, part=part, at=body["at"], until=body["until"], parent=body,
                                   loop=loop, pivot=pivot, speed=kw.get("speed"), z=body["z"],
                                   name=f"{sc['id']}--{asset}--{part}"))
        if run:
            body["loop"] = ("hop", 9, run[0] / 2)
        body["kids"] = kids
        return body

    # ---------- evaluation ----------
    def ltime(self, L, t):
        """Loop-local time with piecewise-constant speed factors (phase stays continuous when speed changes)."""
        if not L["speed"]:
            return t - L["at"]
        keys = [(L["at"], 1.0)] + [k for k in L["speed"] if k[0] > L["at"]]
        tau = 0.0
        for i, (k0, f) in enumerate(keys):
            k1 = keys[i + 1][0] if i + 1 < len(keys) else 1e9
            if t <= k0:
                break
            tau += (min(t, k1) - k0) * f
        return tau

    def state(self, L, t):
        x, y, s, r, o = L["x"], L["y"], L["s"], 0.0, L["o"]
        for mv in L["moves"]:
            t0, t1, tgt = mv[:3]
            if t >= t0:
                u = ease((t - t0) / max(1e-6, t1 - t0), mv[3] if len(mv) > 3 else "inout")
                x += (tgt.get("x", x) - x) * u; y += (tgt.get("y", y) - y) * u
                s += (tgt.get("s", s) - s) * u; r += (tgt.get("r", r) - r) * u; o += (tgt.get("o", o) - o) * u
        d = L["enter_dur"] / FPS
        u = ease((t - L["at"]) / d)
        wipe, wdir = 1.0, "x"
        e = L["enter"]
        if e == "rise":
            y += 30 * (1 - u); o *= u
        elif e == "pop":
            s *= 0.85 + 0.15 * ease((t - L["at"]) / d, "back"); o *= min(1, u * 1.6)
        elif e == "fade":
            o *= u
        elif e == "slide_l":
            x -= 80 * (1 - u); o *= u
        elif e == "slide_r":
            x += 80 * (1 - u); o *= u
        elif e == "wipe":
            wipe = ease((t - L["at"]) / (14 / FPS))
        elif e in ("wipe_up", "grow"):
            wipe, wdir = u, "up"
        ex = L["exit"]
        if ex != "cut":
            ue = ease((L["until"] - t) / (8 / FPS))
            o *= ue
            if ex == "sink":
                y += 30 * (1 - ue)
        lp = L["loop"]
        if lp:
            k, lt = lp[0], self.ltime(L, t)
            if k == "bob":
                y += lp[1] * math.sin(2 * math.pi * lt / lp[2])
            elif k == "hop":
                y -= lp[1] * abs(math.sin(math.pi * lt / lp[2]))
            elif k == "swing":
                ph = lp[3] if len(lp) > 3 else 0.0
                r += lp[1] * math.sin(2 * math.pi * (lt / lp[2] + ph))
            elif k == "spin":
                r -= lp[1] * lt
            elif k == "pulse":
                for tp in lp[2]:
                    if 0 <= t - tp < 0.5:
                        s *= 1 + lp[1] * math.sin(math.pi * (t - tp) / 0.5)
        if L["parent"] is not None:
            P = L["parent"]
            px, py, ps, pr, po, _, _ = self.state(P, t)
            k = ps / P.get("ref_s", P["s"])  # ref_s: parent scale at which child offsets were authored
            x, y, s = px + x * k, py + y * k, s * k
            o *= (po / P["o"]) if P["o"] > 0 else self.parent_vis(P, t)
            r += pr
        return x, y, s, r, o, wipe, wdir

    def parent_vis(self, P, t):
        """Visibility factor of an invisible parent root from its entrance/exit (so children fade together)."""
        L = dict(P, o=1.0, loop=None, parent=None, moves=[m for m in P["moves"] if "o" in m[2]])
        return self.state(L, t)[4]

    @functools.lru_cache(maxsize=1024)
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
        x, y, s, r, o, wipe, wdir = self.state(L, t)
        if o <= 0.01:
            return
        k, cx, cy = cam
        x, y, s = cx + (x - cx) * k, cy + (y - cy) * k, s * k
        im, ox, oy = self.transformed(L["asset"], L["part"], round(s, 3), round(r, 1), L["pivot"][0], L["pivot"][1])
        if o < 0.999 or wipe < 0.999:
            im = im.copy()
            if o < 0.999:
                im.putalpha(im.getchannel("A").point(lambda v: int(v * o)))
            if wipe < 0.999:
                m = Image.new("L", im.size, 0)
                if wdir == "up":  # reveal from the bottom of the drawn content upward (bars grow from baseline)
                    bb = im.getchannel("A").getbbox() or (0, 0, im.width, im.height)
                    top = bb[3] - (bb[3] - bb[1]) * wipe
                    ImageDraw.Draw(m).rectangle([0, int(top), im.width, im.height], fill=255)
                else:
                    ImageDraw.Draw(m).rectangle([0, 0, int(im.width * wipe), im.height], fill=255)
                im.putalpha(Image.composite(im.getchannel("A"), m, m))
        canvas.alpha_composite(im, (round(x + ox), round(y + oy)))

    def camera(self, t):
        keys = sorted(self.cam_keys)
        prev = keys[0]
        for i, kk in enumerate(keys[1:], 1):
            if t < kk[0]:
                p0 = keys[i - 1]
                dur = kk[4] if len(kk) > 4 else 0.6
                u = ease((t - (kk[0] - dur)) / dur, "inout") if t > kk[0] - dur else 0.0
                return tuple(p0[j] + (kk[j] - p0[j]) * u for j in (1, 2, 3))
            prev = kk
        return prev[1], prev[2], prev[3]

    # ---------- text ----------
    def draw_headline(self, canvas, sc, t):
        parts = sc["headline"]
        first = sc is self.scenes[0]
        u = 1.0 if first else ease((t - sc["start"]) / (6 / FPS))
        size = 100
        d = ImageDraw.Draw(canvas)
        f = font(CHALK, size, 2)
        total = sum(d.textlength(p, font=f) for p, _ in parts)
        while total > 960 and size > 64:
            size -= 4; f = font(CHALK, size, 2); total = sum(d.textlength(p, font=f) for p, _ in parts)
        layer = Image.new("RGBA", (W, 220))
        ld = ImageDraw.Draw(layer)
        xx = (W - total) / 2
        for p, col in parts:
            ld.text((xx, 80), p, font=f, fill=col, anchor="lm", stroke_width=4, stroke_fill=(255, 255, 255))
            xx += ld.textlength(p, font=f)
        if sc["label"]:
            ld.text((W / 2, 175), sc["label"], font=font(CHALK, 50, 1), fill=TEAL, anchor="mm")
        if u < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v: int(v * u)))
        canvas.alpha_composite(layer, (0, HEAD_Y + round(16 * (1 - u))))

    def caption_chunks(self):
        if hasattr(self, "_chunks"):
            return self._chunks
        ws = self.words
        chunks, cur = [], []
        for i, (s, e, t) in enumerate(ws):
            cur.append((s, e, t))
            text = " ".join(x[2] for x in cur)
            nxt = ws[i + 1] if i + 1 < len(ws) else None
            hard = nxt is None or t[-1] in ".?!" or nxt[0] - e > 0.45 or i in self.breaks
            soft = t[-1] in ",;" and len(text) >= 14
            full = nxt is not None and len(text) + 1 + len(nxt[2]) > 44
            if hard or soft or full:
                if full and not hard and not soft and t.lower().strip(",") in (
                        "a", "the", "of", "an", "to", "your", "that", "in", "for", "and", "or", "who", "is"):
                    if len(cur) > 1:  # move the dangling function word to the next cue
                        chunks.append(cur[:-1]); cur = [cur[-1]]; continue
                chunks.append(cur); cur = []
        # merge cues that would flash (< 0.8 s of speech) into a neighbour when the result still fits two lines
        merged = []
        for c in chunks:
            if merged and (c[-1][1] - c[0][0] < 0.8 or merged[-1][-1][1] - merged[-1][0][0] < 0.8) and \
                    len(" ".join(x[2] for x in merged[-1] + c)) <= 44 and c[0][0] - merged[-1][-1][1] < 0.45:
                merged[-1] = merged[-1] + c
            else:
                merged.append(c)
        out = []
        for i, c in enumerate(merged):
            s0, e0 = c[0][0], c[-1][1] + 0.45
            if i + 1 < len(merged):
                nx = merged[i + 1][0][0]
                e0 = nx if nx - c[-1][1] < 0.9 else min(e0, nx)
            e0 = max(e0, min(s0 + 1.0, merged[i + 1][0][0] if i + 1 < len(merged) else self.duration))
            out.append(dict(start=s0, end=min(e0, self.duration), words=c, text=" ".join(x[2] for x in c)))
        self._chunks = out
        return out

    @staticmethod
    def split_lines(words, d, f):
        text = " ".join(w[2] for w in words)
        if d.textlength(text, font=f) <= 900 and len(text) <= 22:
            return [list(range(len(words)))]
        best = None
        for k in range(1, len(words)):
            a = d.textlength(" ".join(w[2] for w in words[:k]), font=f)
            b = d.textlength(" ".join(w[2] for w in words[k:]), font=f)
            pen = abs(a - b) + (0 if words[k - 1][2][-1] in ",." else 60) + \
                (150 if words[k - 1][2].lower() in ("a", "the", "of", "an", "to", "and", "or") else 0)
            if max(a, b) <= 940 and (best is None or pen < best[0]):
                best = (pen, k)
        k = best[1] if best else len(words) // 2
        return [list(range(k)), list(range(k, len(words)))]

    @staticmethod
    def segments(word):
        return [p for p in word.replace("₂", "\0₂\0").split("\0") if p]

    def word_len(self, d, word, f):
        return sum(d.textlength(p, font=font(UNI, CAP_SIZE) if p == "₂" else f) for p in self.segments(word))

    def draw_caption(self, canvas, t):
        d = ImageDraw.Draw(canvas)
        for c in self.caption_chunks():
            if c["start"] <= t < c["end"]:
                f = font(ARIALB, CAP_SIZE)
                lines = self.split_lines(c["words"], d, f)
                cur = max((i for i, w in enumerate(c["words"]) if w[0] <= t), default=-1)
                for li, idx in enumerate(lines):
                    y = CAP_Y + CAP_LINE * li + (CAP_LINE / 2 if len(lines) == 1 else 0) + CAP_LINE / 2
                    sp = d.textlength(" ", font=f)
                    lw = sum(self.word_len(d, c["words"][i][2], f) for i in idx) + sp * (len(idx) - 1)
                    xx = (W - lw) / 2
                    for i in idx:
                        s, e, wd = c["words"][i]
                        col = CORAL if i == cur and t < e + 0.25 else INK
                        for seg in self.segments(wd):  # draw "₂" with the fallback font, same size and stroke
                            fs = font(UNI, CAP_SIZE) if seg == "₂" else f
                            d.text((xx, y), seg, font=fs, fill=col, anchor="lm", stroke_width=9, stroke_fill=(255, 255, 255))
                            xx += d.textlength(seg, font=fs)
                        xx += sp
                return

    # ---------- frame ----------
    def frame(self, n):
        t = n / FPS
        sc = next((s for s in self.scenes if s["start"] <= t < s["end"]), self.scenes[-1])
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        cam = self.camera(t)
        for L in sorted(self.layers, key=lambda L: L["z"]):
            if L["at"] <= t < L["until"] and not L.get("kids"):
                self.draw_layer(canvas, L, t, cam)
        self.draw_headline(canvas, sc, t)
        self.draw_caption(canvas, t)
        return canvas.convert("RGB")

    # ---------- audio ----------
    def audio(self):
        SR = 48000
        src = self.voice or self.src_audio
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        voice = np.frombuffer(raw, dtype="<f4").astype(float).reshape(-1, 2)
        n = int(SR * self.frames / FPS)
        voice = np.pad(voice, ((0, max(0, n - len(voice))), (0, 0)))[:n]
        if not self.voice:  # clean start/end on the unchanged source (8 ms in, 30 ms out); content untouched
            voice[:384] *= np.linspace(0, 1, 384)[:, None]
        voice[-1440:] *= np.linspace(1, 0, 1440)[:, None]
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
        m *= 10 ** ((speech - 24 - db(m)) / 20)
        m *= np.minimum(1, t / 0.4) * np.minimum(1, (n / SR - t) / 0.8)
        fx = np.zeros(n)
        for ts, kind, _ in self.sfx:
            s = sfx_wave(kind, SR)
            s *= 10 ** ((speech - 19 - db(s)) / 20)
            a = int(ts * SR)
            fx[a:a + len(s)] += s[: max(0, n - a)]
        mix = voice + (m + fx)[:, None]
        gain = min(1.0, 0.89 / np.max(np.abs(mix)))
        mix *= gain
        path = os.path.join(self.anim, "build_mix.wav")
        with wave.open(path, "w") as wv:
            wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR)
            wv.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
        vrep = dict(source_file="source_audio/original_audio.m4a", source_sha256=sha(self.src_audio))
        if self.voice:
            vrep.update(derived_file=os.path.relpath(self.voice, self.pkg), derived_sha256=sha(self.voice),
                        pacing="animation/v2/VOICE_PACING.json",
                        treatment=f"derived paced voice (see VOICE_PACING.json) + 30 ms end fade; whole-mix gain x{gain:.3f}")
        else:
            vrep.update(treatment=f"decoded unchanged; 8 ms start fade-in, 30 ms end fade-out; whole-mix gain x{gain:.3f}; "
                                  "no trim, speed, pitch or word change")
        self.audio_report = dict(
            voice=vrep,
            music=dict(source="synthesised in tools/anim_v2.py from sine chords (no samples, no library track)",
                       chords_hz=self.music_chords, seconds_per_chord=seg, level_db_below_speech=24,
                       rights="created in this project from code; rights opinion not given; no claim this removes all rights questions"),
            sfx=[dict(t=round(a, 2), kind=k, event=e) for a, k, e in self.sfx], sfx_level_db_below_speech=19,
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
        for L in self.layers:
            keys = [dict(frame=round(L["at"] * FPS), x=L["x"], y=L["y"], scale=L["s"], entry=L["enter"])]
            keys += [dict(frame_in=round(m[0] * FPS), frame_out=round(m[1] * FPS), ease=m[3] if len(m) > 3 else "inout",
                          **m[2]) for m in L["moves"]]
            asset = L["asset"] if not isinstance(L["asset"], tuple) else "text:" + L["asset"][1]
            tracks.append(dict(scene=L["scene"], layer=L["name"], asset=asset, part=L["part"], z=L["z"],
                               parent=L["parent"]["name"] if L["parent"] else None,
                               in_frame=round(L["at"] * FPS), out_frame_exclusive=round(L["until"] * FPS),
                               exit=L["exit"], pivot=L["pivot"], keys=keys, loop=L["loop"], speed=L["speed"]))
        doc = dict(fps=FPS, width=W, height=H, frames=self.frames, duration_seconds=self.duration,
                   transform="child world = parent xy + child xy * parent scale ratio; camera: world=cam_center+(xy-cam_center)*k",
                   camera_keys=[dict(t=k[0], frame=round(k[0] * FPS), scale=k[1], center=[k[2], k[3]]) for k in sorted(self.cam_keys)],
                   scenes=[dict(id=s["id"], in_frame=round(s["start"] * FPS), out_frame_exclusive=round(s["end"] * FPS),
                                headline="".join(p for p, _ in s["headline"]), label=s["label"]) for s in self.scenes],
                   tracks=tracks, sfx=[dict(t=a, kind=k, event=e) for a, k, e in self.sfx])
        json.dump(doc, open(os.path.join(self.anim, "KEYFRAME_TIMELINE_V2.json"), "w"), indent=1)
        return doc

    def srt(self):
        def ts(x):
            ms = round(x * 1000)
            return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"
        lines = [f"{i}\n{ts(c['start'])} --> {ts(c['end'])}\n{c['text']}\n" for i, c in enumerate(self.caption_chunks(), 1)]
        open(os.path.join(self.anim, "CAPTIONS_V2.srt"), "w").write("\n".join(lines))

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
        cues = self.caption_chunks()
        durs = [c["end"] - c["start"] for c in cues]
        streams = probe["streams"]
        vdur = float(next(s for s in streams if s["codec_name"] == "h264")["duration"])
        adur = float(next(s for s in streams if s["codec_name"] == "aac")["duration"])
        rep = dict(file=os.path.basename(mp4), probe=probe, decode_errors=dec.strip() or "none",
                   av_duration_delta_s=round(abs(vdur - adur), 3),
                   max_volume=[l.split(":")[-1].strip() for l in vol.splitlines() if "max_volume" in l],
                   mean_volume=[l.split(":")[-1].strip() for l in vol.splitlines() if "mean_volume" in l],
                   min_frame_std_10fps=round(float(stds.min()), 1), blank_frames=int((stds < 8).sum()),
                   large_jumps_s=big, headline_changes_s=cuts,
                   unplanned_large_jumps_s=[b for b in big if not any(abs(b - c) <= 0.15 for c in cuts)],
                   scenes=len(self.scenes), layer_tracks=len(self.layers),
                   unique_assets=len({L["asset"] for L in self.layers if not isinstance(L["asset"], tuple)}),
                   caption_cues=len(cues), caption_min_s=round(min(durs), 2), caption_median_s=round(float(np.median(durs)), 2),
                   cues_under_0_8s=[c["text"] for c in cues if c["end"] - c["start"] < 0.8],
                   caption_block_bottom_px=CAP_Y + 2 * CAP_LINE, word_corrections=self.corrections,
                   review_marks_in_frames=False, sfx=len(self.sfx), audio=self.audio_report)
        json.dump(rep, open(os.path.join(self.anim, "RENDER_QA_V2.json"), "w"), indent=1)
        return rep

    def contact_sheet(self, mp4, step=1.0):
        """Complete sheet: one frame per `step` seconds over the whole video, plus the last frame."""
        times = list(np.arange(0.0, self.duration - 0.05, step)) + [self.duration - 0.05]
        tw, th, cols = 216, 384, 8
        raw = []
        for tt in times:
            png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{tt:.3f}", "-i", mp4, "-frames:v", "1", "-vf",
                                  f"scale={tw}:{th}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
            raw.append((tt, Image.open(io.BytesIO(png)).convert("RGB")))
        rows = math.ceil(len(raw) / cols)
        sheet = Image.new("RGB", (cols * (tw + 8) + 8, rows * (th + 34) + 8), (228, 228, 224))
        d = ImageDraw.Draw(sheet)
        for i, (tt, im) in enumerate(raw):
            x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 34)
            sheet.paste(im, (x, y))
            d.text((x, y + th + 4), f"{tt:.2f}s", font=font(ARIAL, 20), fill=INK)
        sheet.save(os.path.join(self.anim, "CONTACT_SHEET_V2.png"))

    def main(self, argv):
        mode = argv[1] if len(argv) > 1 else "render"
        os.makedirs(os.path.join(self.anim, "qa"), exist_ok=True)
        if mode == "test":
            a, b = float(argv[2]), float(argv[3])
            print(self.render(round(a * FPS), round(b * FPS), os.path.join(self.anim, "qa/test_window.mp4")))
        elif mode == "still":
            for s in argv[2:]:
                self.frame(round(float(s) * FPS)).save(os.path.join(self.anim, f"qa/still_{float(s):05.2f}.png"))
        elif mode == "srt":
            self.srt(); print(open(os.path.join(self.anim, "CAPTIONS_V2.srt")).read())
        else:
            mp4 = self.render()
            mob = mp4.replace(".mp4", "_MOBILE_540x960.mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp4, "-vf", "scale=540:960:flags=lanczos",
                            "-c:v", "libx264", "-crf", "22", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                            "-movflags", "+faststart", mob], check=True)
            self.timeline(); self.srt(); self.contact_sheet(mp4)
            rep = self.qa(mp4)
            json.dump(self.audio_report, open(os.path.join(self.anim, "AUDIO_PROVENANCE_V2.json"), "w"), indent=1)
            os.remove(os.path.join(self.anim, "build_mix.wav"))
            print(json.dumps({k: rep[k] for k in ("decode_errors", "av_duration_delta_s", "max_volume", "mean_volume",
                                                  "blank_frames", "unplanned_large_jumps_s", "caption_min_s",
                                                  "cues_under_0_8s", "layer_tracks", "unique_assets", "scenes")}, indent=1))


def sfx_wave(kind, SR):
    t = np.arange(int(SR * {"pop": 0.12, "tick": 0.08, "chime": 0.9, "soft": 0.5, "whoosh": 0.35}[kind])) / SR
    if kind == "pop":
        return np.exp(-t / 0.03) * np.sin(2 * np.pi * (520 - 1800 * t) * t)
    if kind == "tick":
        return np.exp(-t / 0.015) * np.sin(2 * np.pi * 1320 * t)
    if kind == "chime":
        return np.exp(-t / 0.25) * (np.sin(2 * np.pi * 784 * t) + 0.6 * np.sin(2 * np.pi * 1175 * t))
    if kind == "whoosh":  # filtered-noise sweep, seeded so renders are reproducible
        n = np.random.default_rng(7).standard_normal(len(t))
        n = np.convolve(n, np.ones(24) / 24, "same")
        return np.sin(np.pi * t / t[-1]) ** 2 * n
    return np.minimum(1, t / 0.05) * np.exp(-t / 0.15) * np.sin(2 * np.pi * 330 * t)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
