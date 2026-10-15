"""V3 upload-candidate compositor (V2 art/animation, internal annotations removed, end trimmed).
V2 keyframe compositor: white canvas, layered original assets, audio-timed.

  python3 v2.py timeline            -> KEYFRAME_TIMELINE_V3.json
  python3 v2.py frames t1 t2 ...    -> qa/frame_<t>.png  (calibration / QA stills)
  python3 v2.py render [lowres]     -> preview MP4 (muxes original MP3 + music/SFX bed)
  python3 v2.py sheet               -> V3_CONTACT_SHEET.png from the encoded MP4
Times are seconds on the ORIGINAL 1015.mp3 clock (word times: ../animation/AUDIO_ALIGNMENT.json).
"""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
W, H, FPS = 1080, 1920, 30
DUR = 45.5
END = 43.0  # export cut: speech ends 38.6 s (ASR); 4.4 s takeaway hold, 1.0 s audio fade. Source MP3 untouched.
STAGE_DY = 190  # world layers sit lower: headline zone 140-560, stage 560-1640, captions 1690
MP3 = os.path.expanduser("~/Downloads/1015.mp3")
MP3_SHA = "8f9e39ab409959d4e06f99052860cf4391d56a7ab6caa85f560217d35cc3daf5"
OUTMP4 = os.path.join(HERE, "Dr_Rehan_Heart_Warning_V3_UPLOAD_CANDIDATE.mp4")
INK = (38, 34, 31)
RED = (214, 64, 52)
GREY = (120, 120, 126)
FONT = "/System/Library/Fonts/Avenir Next Condensed.ttc"
FONT2 = "/System/Library/Fonts/Avenir Next.ttc"


def font(size, heavy=True, cond=True):
    return ImageFont.truetype(FONT if cond else FONT2, size, index=8 if heavy else 2)


_cache = {}


def img(name):
    if name not in _cache:
        _cache[name] = Image.open(os.path.join(A, name + ".png")).convert("RGBA")
    return _cache[name]


def text_img(spans, size=96, heavy=True, cond=True, maxw=980, align="center", lh=1.08):
    """spans: list of (text, colour). '\n' inside text breaks lines. Returns RGBA."""
    f = font(size, heavy, cond)
    lines, cur = [], []
    for t, col in spans:
        parts = t.split("\n")
        for i, p in enumerate(parts):
            if i:
                lines.append(cur); cur = []
            if p:
                cur.append((p, col))
    lines.append(cur)
    lw = [sum(f.getlength(t) for t, _ in ln) for ln in lines]
    hgt = int(size * lh)
    im = Image.new("RGBA", (int(max(lw + [10])) + 8, hgt * len(lines) + int(size * 0.3)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, ln in enumerate(lines):
        x = (im.width - lw[i]) / 2 if align == "center" else 4
        for t, col in ln:
            d.text((x, i * hgt), t, font=f, fill=col)
            x += f.getlength(t)
    return im


def ease(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)


def back(u):  # gentle overshoot for pops (max ~4%)
    u = max(0.0, min(1.0, u))
    c = 1.2
    return 1 + (c + 1) * (u - 1) ** 3 + c * (u - 1) ** 2


class L:
    """One animatable layer. keys: list of (t, dict(x,y,s,o,r)); x,y = anchor position on canvas."""

    def __init__(self, src, x, y, s=1.0, t0=0.0, t1=DUR, anchor=(0.5, 1.0), world=True, z=0, wipe=None):
        self.src, self.t0, self.t1, self.anchor, self.world, self.z, self.wipe = src, t0, t1, anchor, world, z, wipe
        self.keys = [(t0, dict(x=x, y=y, s=s, o=1.0, r=0.0))]
        self.swaps = [(t0, src)]
        self.kind = []

    def to(self, t, dur=0.35, fn=ease, **kv):
        base = dict(self.keys[-1][1])
        self.keys.append((t, base, None))
        nb = dict(base)
        nb["x"] += kv.pop("dx", 0); nb["y"] += kv.pop("dy", 0)
        nb.update(kv)
        self.keys.append((t + dur, nb, fn))
        return self

    def pop(self, dur=0.3):
        k = self.keys[0][1]
        self.kind.append("POP_IN")
        self.keys = [(self.t0, dict(k, s=k["s"] * 0.82, o=0.0)), (self.t0 + dur, k, back)] + self.keys[1:]
        return self

    def slide(self, dx=0, dy=0, dur=0.4):
        k = self.keys[0][1]
        self.kind.append("SLIDE_IN")
        self.keys = [(self.t0, dict(k, x=k["x"] + dx, y=k["y"] + dy)), (self.t0 + dur, k, ease)] + self.keys[1:]
        return self

    def fade(self, dur=0.25):
        k = self.keys[0][1]
        self.kind.append("FADE_IN")
        self.keys = [(self.t0, dict(k, o=0.0)), (self.t0 + dur, k, ease)] + self.keys[1:]
        return self

    def out(self, t, dur=0.25, **kv):
        self.kind.append("EXIT")
        kv.setdefault("o", 0.0)
        self.to(t - dur, dur, **kv)
        self.t1 = t
        return self

    def swap(self, t, src):
        self.kind.append("POSE_SWITCH")
        self.swaps.append((t, src))
        return self

    def state(self, t):
        ks = self.keys
        cur = dict(ks[0][1])
        for i in range(1, len(ks)):
            tk, v = ks[i][0], ks[i][1]
            fn = ks[i][2] if len(ks[i]) > 2 else None
            if t >= tk:
                cur = dict(v)
            elif fn is not None:
                tp = ks[i - 1][0]
                u = fn((t - tp) / max(1e-6, tk - tp))
                prev = ks[i - 1][1]
                cur = {k: prev[k] + (v[k] - prev[k]) * u for k in v}
                break
            else:
                break
        src = [s for ts, s in self.swaps if t >= ts][-1]
        return cur, src

    def spec(self):
        return dict(src=self.swaps, t0=self.t0, t1=self.t1, anchor=self.anchor, world=self.world, z=self.z,
                    wipe=self.wipe, ops=self.kind,
                    keys=[dict(t=round(k[0], 3), **{a: round(b, 3) for a, b in k[1].items()}) for k in self.keys])


TEXT = {}


def T(key, spans, **kw):
    TEXT[key] = (spans, kw)
    return key


def get(src):
    if isinstance(src, Image.Image):
        return src
    if src in TEXT:
        if ("_t", src) not in _cache:
            spans, kw = TEXT[src]
            _cache[("_t", src)] = text_img(spans, **kw)
        return _cache[("_t", src)]
    return img(src)


# ------------------------------------------------------------------ SCENES
# Each scene: (id, t_start, t_end, narration span, camera keys, layers)
SCENES = []


def scene(sid, a, b, said, cam=(1.0, 1.0)):
    s = dict(id=sid, t0=a, t1=b, said=said, cam=cam, layers=[])
    SCENES.append(s)
    return s["layers"]


def build():
    SCENES.clear()
    # S1 HOOK 0.0-5.65  "People with diabetes may be more likely to miss the warning signs of heart attack."
    ls = scene("S1_HOOK", 0.0, 5.65, "People with diabetes ... warning signs of heart attack.", cam=(1.0, 1.07))
    ls.append(L("plate_stairs", 540, 1420, 1.0, 0.0, anchor=(0.5, 1.0), z=0))
    ls.append(L("glow_red", 545, 1060, 0.95, 0.25, z=1, anchor=(0.5, 0.5)).fade(0.5)
              .to(1.3, 0.6, s=1.08).to(2.0, 0.7, s=0.95).to(3.0, 0.4, s=1.12, o=1.0))
    ls.append(L("patient_chest_smile", 560, 1365, 1.0, 0.0, z=2).pop(0.35))
    ls.append(L(T("bub", [("“Just tired…”", INK)], size=58, heavy=False), 215, 690, 1.0, 0.95, anchor=(0.5, 0.5), z=4).pop())
    ls.append(L("bubble", 215, 720, 1.0, 0.9, anchor=(0.5, 0.5), z=3).pop())
    ls.append(L(T("tag_dm", [("DIABETES", (255, 255, 255))], size=54), 820, 905, 1.0, 0.6, anchor=(0.5, 0.5), z=5).pop())
    ls.append(L("tagbox_blue", 820, 905, 1.0, 0.6, anchor=(0.5, 0.5), z=4).pop())
    ls.append(L(T("h1a", [("Heart attack\n", INK), ("warning signs?", RED)], size=112), 540, 170, 1.0, 3.35,
                anchor=(0.5, 0.0), world=False, wipe=0.45, z=9))
    ls.append(L(T("h1b", [("easy to ", INK), ("MISS", RED)], size=84), 540, 430, 1.0, 2.85,
                anchor=(0.5, 0.0), world=False, z=9).pop(0.25))
    # S2 DOCTOR INTRO 5.65-8.45 "Let's listen what Dr. Rehan says."
    ls = scene("S2_DOCTOR", 5.65, 8.45, "Let's listen what Dr. Rehan says.")
    ls.append(L("patient_neutral", 320, 1380, 0.98, 5.65, z=2).slide(dx=-120, dur=0.35))
    ls.append(L("doctor_smile", 760, 1400, 1.12, 5.85, z=3).slide(dx=520, dur=0.45).swap(7.4, "doctor_explain"))
    ls.append(L(T("dr", [("Dr. Rehan", INK)], size=120), 540, 220, 1.0, 6.85, anchor=(0.5, 0.0), world=False, wipe=0.4))
    # S3 ATYPICAL 8.45-13.15 "So in patients who have these atypical symptoms which are not particularly significantly"
    ls = scene("S3_ATYPICAL", 8.45, 13.15, "So in patients who have these atypical symptoms which are not particularly significantly", cam=(1.0, 1.03))
    ls.append(L("patient_chest_worried", 590, 1350, 0.88, 8.45, z=2).fade(0.2))
    ls.append(L("doctor_point", 150, 1420, 0.8, 8.45, z=6).slide(dx=-420, dur=0.35))
    ls.append(L(T("h3", [("Less obvious\n", INK), ("warning signs", RED)], size=104), 540, 170, 1.0, 9.75,
                anchor=(0.5, 0.0), world=False, wipe=0.4))
    for i, (ic, lab, x, y) in enumerate([("icon_breath", "Breathless", 330, 520), ("icon_tired", "Unusually tired", 880, 560),
                                          ("icon_sweat", "Cold sweat", 880, 860), ("icon_radiate", "Jaw / arm / back\ndiscomfort", 880, 1130)]):
        t = 10.35 + 0.55 * i
        ls.append(L(ic, x, y + 190, 0.95, t, anchor=(0.5, 0.5), world=False, z=4).pop())
        ls.append(L(T("lab3%d" % i, [(lab, INK)], size=50, heavy=False), x, y + 285, 1.0, t + 0.1, anchor=(0.5, 0.0), world=False, z=4).fade(0.2))
    # S4 ANGINA ON EXERTION 13.15-19.4
    ls = scene("S4_EXERTION", 13.15, 19.4, "in angina but in angina-like symptoms which appear on exertion they should always be evaluated", cam=(1.0, 1.06))
    ls.append(L("plate_stairs", 540, 1420, 1.0, 13.15, z=0))
    ls.append(L("glow_red", 545, 1060, 0.95, 15.85, z=1, anchor=(0.5, 0.5)).fade(0.4).to(16.8, 0.5, s=1.1))
    ls.append(L("patient_chest_pain", 560, 1365, 1.0, 13.15, z=2))
    ls.append(L(T("h4", [("Chest discomfort\n", INK), ("with exertion", RED)], size=104), 540, 170, 1.0, 14.35,
                anchor=(0.5, 0.0), world=False, wipe=0.45))
    ls.append(L(T("h4s", [("angina-like symptoms", GREY)], size=54, heavy=False), 540, 420, 1.0, 15.55,
                anchor=(0.5, 0.0), world=False).fade(0.3))
    ls.append(L("icon_exert", 860, 560, 1.25, 16.65, anchor=(0.5, 0.5), z=4).pop())
    ls.append(L("doctor_clip", 150, 1420, 0.8, 17.85, z=6).slide(dx=-420, dur=0.35))
    ls.append(L("icon_check", 880, 820, 1.0, 18.85, anchor=(0.5, 0.5), z=7).pop())
    ls.append(L(T("lab4", [("Get it checked", (63, 163, 91))], size=58), 880, 925, 1.0, 18.95, anchor=(0.5, 0.0), z=7).fade(0.2))
    # S5-S8 THREE GROUPS 19.4-28.5
    a0 = 19.4
    ls = scene("S5_GROUPS", a0, 28.45, "in certain subsets of patients which are number one type 2 diabetes, number 2 elderly males and elderly females and number 3 ... comorbid conditions.")
    ls.append(L(T("h5", [("3 groups ", RED), ("to watch", INK)], size=112), 540, 170, 1.0, 19.65, anchor=(0.5, 0.0), world=False, wipe=0.4))
    for i, x in enumerate((330, 540, 750)):
        ls.append(L("badge%d_off" % (i + 1), x, 430, 1.0, 20.25 + 0.3 * i, anchor=(0.5, 0.0), world=False).pop())
    for i, (x, t) in enumerate(((330, 21.95), (540, 23.4), (750, 26.35))):
        ls.append(L("badge%d_on" % (i + 1), x, 430, 1.0, t, anchor=(0.5, 0.0), world=False, z=8).pop(0.25))
    ls.append(L("patient_meter", 540, 1440, 0.95, 21.95, z=2).slide(dx=700, dur=0.4).out(23.65, dx=-760))
    ls.append(L(T("g1", [("Type 2 diabetes", INK)], size=78), 540, 590, 1.0, 22.15, anchor=(0.5, 0.0), world=False, z=5).fade(0.2).out(23.4))
    ls.append(L("oldman", 540, 1440, 0.95, 23.75, z=2).pop().to(25.05, 0.4, x=310, s=0.9).out(26.55, dx=-700))
    ls.append(L("oldwoman", 780, 1440, 0.9, 25.1, z=2).slide(dx=500, dur=0.4).out(26.55, dx=700))
    ls.append(L(T("g2", [("Older men ", INK), ("& women", INK)], size=78), 540, 590, 1.0, 23.8, anchor=(0.5, 0.0), world=False, z=5).fade(0.2).out(26.35))
    ls.append(L("woman_pills", 540, 1440, 0.95, 26.45, z=2).slide(dx=700, dur=0.4))
    ls.append(L(T("g3", [("Other health conditions", INK)], size=78), 540, 590, 1.0, 26.6, anchor=(0.5, 0.0), world=False, z=5).fade(0.2))
    ls.append(L(T("g3s", [("e.g. high blood pressure, high cholesterol", GREY)], size=48, heavy=False), 540, 690, 1.0, 27.4,
                anchor=(0.5, 0.0), world=False, z=5).fade(0.25))
    # S9 LINEUP 28.45-33.75 "So these three groups of people should always be evaluated for"
    ls = scene("S9_LINEUP", 28.45, 33.75, "So these three groups of people should always be evaluated for")
    ls.append(L(T("h9", [("These 3 groups:\n", INK), ("get checked", RED)], size=104), 540, 170, 1.0, 28.5,
                anchor=(0.5, 0.0), world=False, wipe=0.4).swap(31.6, T("h9b", [("Should always be\n", INK), ("evaluated", RED)], size=104)))
    for (src, x, t, sc) in (("patient_meter", 190, 29.1, 0.62), ("oldman", 430, 29.9, 0.6), ("oldwoman", 640, 30.0, 0.56),
                            ("woman_pills", 880, 30.6, 0.62)):
        ls.append(L(src, x, 1060, sc, t, z=2).pop())
    for i, (x, t) in enumerate(((190, 29.15), (535, 29.95), (880, 30.65))):
        ls.append(L("badge%d_on" % (i + 1), x, 590, 0.8, t, anchor=(0.5, 0.0), world=False, z=3).pop())
        ls.append(L("icon_check", x, 1480, 0.6, 31.65 + 0.2 * i, anchor=(0.5, 0.5), world=False, z=5).pop())
    # S10 ACS 33.75-36.15 "acute [coronary syndrome?]"
    ls = scene("S10_ACS", 33.75, 36.15, "(no caption: wording unconfirmed)", cam=(1.0, 1.05))
    ls.append(L("heart_base", 540, 1330, 1.0, 33.75, z=1).pop(0.35))
    ls.append(L("heart_coronary", 540, 1330, 1.0, 34.1, z=2).fade(0.35))
    ls.append(L("heart_marker", 540, 1330, 1.0, 34.6, z=3).pop())
    ls.append(L(T("h10", [("Acute coronary\nsyndrome ", RED), ("(ACS)", INK)], size=104), 540, 170, 1.0, 33.8,
                anchor=(0.5, 0.0), world=False, wipe=0.4))
    ls.append(L(T("h10s", [("Blood supply to the heart muscle\nis suddenly reduced", GREY)], size=52, heavy=False, cond=False),
                540, 440, 1.0, 34.7, anchor=(0.5, 0.0), world=False).fade(0.3))
    # S11 SUDDEN 36.15-38.6 "if they have sudden onset symptoms which I have just mentioned."
    ls = scene("S11_SUDDEN", 36.15, 38.6, "if they have sudden onset symptoms which I have just mentioned.")
    ls.append(L("plate_window", 800, 900, 0.8, 36.15, z=0))
    ls.append(L("plate_sofa", 540, 1440, 1.0, 36.15, z=0))
    ls.append(L("patient_chest_worried", 470, 1370, 1.05, 36.15, z=2))
    ls.append(L("glow_red", 455, 1060, 0.8, 36.2, z=1, anchor=(0.5, 0.5)).fade(0.3))
    ls.append(L("icon_sudden", 780, 760, 1.0, 36.15, anchor=(0.5, 0.5), z=4).pop())
    ls.append(L(T("h11", [("Sudden", RED), (" or new\nsymptoms", INK)], size=110), 540, 170, 1.0, 36.2,
                anchor=(0.5, 0.0), world=False, wipe=0.4))
    for i, ic in enumerate(("icon_breath", "icon_tired", "icon_sweat", "icon_radiate")):  # callback
        ls.append(L(ic, 200 + 226 * i, 520, 0.6, 37.25 + 0.15 * i, anchor=(0.5, 0.5), world=False, z=5).pop(0.25))
    # S12 TAKEAWAY 38.6-45.5 (no narration; room tone continues)
    ls = scene("S12_TAKEAWAY", 38.6, END, "(no speech — recorded room tone)")
    ls.append(L("patient_phone", 300, 1250, 0.85, 38.6, z=2))  # no fade: avoids near-blank frame at cut
    ls.append(L("icon_phone", 780, 1000, 1.1, 38.9, anchor=(0.5, 0.5), z=4).pop())
    ls.append(L(T("h12", [("New, sudden or\nat-rest symptoms?", INK)], size=96), 540, 160, 1.0, 38.65,
                anchor=(0.5, 0.0), world=False, wipe=0.45))
    ls.append(L(T("h12b", [("Call emergency\nservices now", RED)], size=96), 540, 390, 1.0, 39.6,
                anchor=(0.5, 0.0), world=False, wipe=0.45))
    ls.append(L("divider", 540, 1480, 1.0, 40.4, anchor=(0.5, 0.0), world=False).fade(0.3))
    ls.append(L(T("h12c", [("Symptoms only with exertion?\n", INK), ("See your doctor promptly.", (63, 163, 91))],
                  size=62, heavy=True), 540, 1500, 1.0, 40.6, anchor=(0.5, 0.0), world=False, wipe=0.5))
    for s in SCENES:
        for l in s["layers"]:
            l.t1 = min(l.t1, s["t1"])


def make_ui_assets():
    """Simple text-free UI shapes generated once (tag box, badges, divider)."""
    from art import Canvas
    c = Canvas(300, 90, 41); c.poly([(6, 8), (294, 8), (294, 82), (6, 82)], fill="#3D84C6"); c.save("tagbox_blue")
    c = Canvas(600, 12, 42); c.line([(10, 6), (590, 6)], color="#D8D3CB", w=5); c.save("divider")
    for n in (1, 2, 3):
        for on in (0, 1):
            im = Image.new("RGBA", (130, 130), (0, 0, 0, 0))
            d = ImageDraw.Draw(im)
            d.ellipse((5, 5, 125, 125), fill=RED if on else (235, 232, 226), outline=INK, width=7)
            f = font(84)
            d.text((65, 66), str(n), font=f, fill=(255, 255, 255) if on else (160, 156, 150), anchor="mm")
            im.save(os.path.join(A, "badge%d_%s.png" % (n, "on" if on else "off")))


# ------------------------------------------------------------------ CAPTIONS (verbatim ASR, uncertainty kept)
UNCERTAIN = {"China": "angina", "subsurface": "subsets", "coronation": "[coronary", "in their home": "syndrome?]",
             "certain onset": "sudden onset"}


def captions():
    al = json.load(open(os.path.join(HERE, "..", "animation", "AUDIO_ALIGNMENT.json")))
    words = [(w["word"].strip(), w["start"], w["end"]) for w in al["words"]]
    # verbatim text with marked uncertain spans
    out, i = [], 0
    toks = []
    while i < len(words):
        w, a, b = words[i]
        nxt = words[i + 1][0] if i + 1 < len(words) else ""
        if w == "in" and nxt == "their" and i + 2 < len(words) and words[i + 2][0] == "home":
            i += 3; continue  # uncertain ACS wording: no verbatim caption; on-screen label explains ACS
        if w == "certain" and nxt.startswith("onset"):
            toks.append(("sudden", a, b, True)); i += 1; continue  # owner script word
        if w == "in" and nxt == "China":  # owner script: "significantly angina but angina-like"
            i += 1; continue
        if w == "China" and nxt.startswith("like"):
            toks.append(("angina-like", a, words[i + 1][2], False)); i += 2; continue
        if w == "acute" and nxt == "coronation":
            i += 2; continue
        rep = {"China": "angina", "subsurface": "subsets"}.get(w)  # owner script words (ASR misheard)
        toks.append((rep or w, a, b, bool(rep))); i += 1
    # group into short lines (<= 4 words, break on punctuation or pause)
    cur = []
    for t in toks:
        if cur and t[1] - cur[-1][2] > 0.5:  # never bridge a pause/uncaptioned span
            out.append(cur); cur = []
        cur.append(t)
        end = t[0] not in ("Dr.", "type") and (t[0][-1] in ".,?" or len(cur) >= 4)
        if end:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    caps = []
    for g in out:
        caps.append(dict(t0=g[0][1], t1=g[-1][2] + 0.15, words=[(w, u) for w, _, _, u in g]))
    for a, b in zip(caps, caps[1:]):
        a["t1"] = min(a["t1"], b["t0"])
    return caps


def cap_img(c):
    spans = []
    for i, (w, u) in enumerate(c["words"]):
        spans.append(((" " if i else "") + w, INK))
    return text_img(spans, size=62, heavy=True, cond=False)


# ------------------------------------------------------------------ RENDER
def frame(t, caps, lowres=False):
    canvas = Image.new("RGB", (W, H), "white")
    sc = [s for s in SCENES if s["t0"] <= t < s["t1"]] or [SCENES[-1]]
    s = sc[0]
    u = (t - s["t0"]) / (s["t1"] - s["t0"])
    cam = s["cam"][0] + (s["cam"][1] - s["cam"][0]) * ease(u)
    cx, cy = W / 2, 1000
    for l in sorted(s["layers"], key=lambda l: l.z):
        if not (l.t0 <= t < l.t1):
            continue
        st, src = l.state(t)
        if st["o"] <= 0.01:
            continue
        im = get(src)
        sc_ = st["s"] * (cam if l.world else 1.0)
        x, y = st["x"], st["y"]
        if l.world:
            y += STAGE_DY
            x, y = cx + (x - cx) * cam, cy + (y - cy) * cam
        w, h = max(1, int(im.width * sc_)), max(1, int(im.height * sc_))
        im2 = im.resize((w, h), Image.BILINEAR) if (w, h) != im.size else im
        if l.wipe:
            p = ease((t - l.t0) / l.wipe)
            if p < 1:
                cw = max(1, int(w * p))
                im2 = im2.crop((0, 0, cw, h)) if cw < w else im2
        if st["o"] < 1:
            a = im2.getchannel("A").point(lambda v, o=st["o"]: int(v * o))
            im2 = im2.copy(); im2.putalpha(a)
        px, py = int(x - l.anchor[0] * w), int(y - l.anchor[1] * h)
        canvas.paste(im2, (px, py), im2)
    d = ImageDraw.Draw(canvas)
    for c in caps:
        if c["t0"] <= t < c["t1"]:
            ci = get_cap(c)
            canvas.paste(ci, (int(W / 2 - ci.width / 2), 1690), ci)
    return canvas


_capcache = {}


def get_cap(c):
    k = (c["t0"],)
    if k not in _capcache:
        _capcache[k] = cap_img(c)
    return _capcache[k]


def timeline_json(caps):
    return dict(fps=FPS, size=[W, H], duration_s=END, frames=int(END * FPS), audio_clock="1015.mp3 original, untrimmed",
                coordinate_contract="x,y = anchor point on 1080x1920 canvas; anchor = fraction of layer size; s uniform scale; "
                                    "world layers scale with scene camera about (540,1000)",
                scenes=[dict(id=s["id"], t0=s["t0"], t1=s["t1"], narration_span=s["said"], camera_scale=list(s["cam"]),
                             layers=[l.spec() for l in s["layers"]]) for s in SCENES],
                captions=[dict(t0=round(c["t0"], 3), t1=round(c["t1"], 3), text=" ".join(w for w, _ in c["words"]),
                               uncertain=[w for w, u in c["words"] if u]) for c in caps])


def main():
    if not os.path.exists(os.path.join(A, "badge1_on.png")):
        make_ui_assets()
    build()
    caps = captions()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "timeline"
    if cmd == "timeline":
        json.dump(timeline_json(caps), open(os.path.join(HERE, "KEYFRAME_TIMELINE_V3.json"), "w"), indent=1)
        print("scenes", len(SCENES), "layers", sum(len(s["layers"]) for s in SCENES), "captions", len(caps))
    elif cmd == "frames":
        os.makedirs(os.path.join(HERE, "qa"), exist_ok=True)
        for a in sys.argv[2:]:
            frame(float(a), caps).save(os.path.join(HERE, "qa", "frame_%06.2f.png" % float(a)))
    elif cmd == "render":
        low = "lowres" in sys.argv
        out = OUTMP4 if not low else os.path.join(HERE, "qa", "lowres.mp4")
        os.makedirs(os.path.join(HERE, "qa"), exist_ok=True)
        size = "540x960" if low else "%dx%d" % (W, H)
        mix = os.path.join(HERE, "audio", "mix_preview.wav")
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H),
                              "-r", str(FPS), "-i", "-", "-i", mix, "-af", "afade=t=out:st=%.2f:d=1.0" % (END - 1.0), "-t", str(END), "-vf", "scale=" + size, "-c:v", "libx264", "-crf", "20",
                              "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
                              "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        n = int(END * FPS)
        for f in range(n):
            p.stdin.write(frame(f / FPS, caps).tobytes())
        p.stdin.close(); p.wait()
        print("wrote", out)
    elif cmd == "sheet":
        tmp = os.path.join(HERE, "qa", "sheet"); os.makedirs(tmp, exist_ok=True)
        ts = [round(s["t0"] + 0.75 * (s["t1"] - s["t0"]), 2) for s in SCENES]
        tiles = []
        for t in ts:
            fp = os.path.join(tmp, "%.2f.png" % t)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", OUTMP4, "-frames:v", "1", fp], check=True)
            tiles.append((t, Image.open(fp).resize((270, 480))))
        cols = 6
        sheet = Image.new("RGB", (270 * cols, 520 * math.ceil(len(tiles) / cols)), "white")
        d = ImageDraw.Draw(sheet)
        for i, ((t, im), s) in enumerate(zip(tiles, SCENES)):
            x, y = (i % cols) * 270, (i // cols) * 520
            sheet.paste(im, (x, y))
            d.text((x + 6, y + 486), "%s %.2fs" % (s["id"], t), font=font(24, heavy=False, cond=False), fill=INK)
        sheet.save(os.path.join(HERE, "V3_CONTACT_SHEET.png"))


if __name__ == "__main__":
    main()
