"""Builds the HyperFrames project in hf/ from the EDL below + word timings.
Run: python3 build.py   (then: cd hf && npx hyperframes check)
Every time on screen comes from a spoken word (VO: vo_transcript.json, doctor: whisper json)."""
import json, re, html, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
HF = os.path.join(HERE, "hf")
VO = json.load(open(os.path.join(WORK, "03_narration_audio/vo_transcript.json")))
DRW = [w for s in json.load(open(os.path.join(WORK, "00_intake/doctor_transcript_whisper.json"))) for w in s["words"]]
VO_DUR = {"H01": 25.835, "I01": 20.689, "J01": 15.726, "J02": 29.081, "B01": 6.740, "B02": 23.327, "U01": 38.296, "O01": 30.903}
J02_CUT = (17.95, 19.85)  # "Doctor check" removed (edl.md, VO trims)
T1 = (58.24, 59.33)       # doctor false start "fall out" (edl.md T1, set on the waveform)

C = dict(navy="#14213D", deep="#0B1430", off="#F4F1EC", paper="#FAF6EE", red="#D64545", grey="#8A8A8A", hi="#F5D547", graphite="#3A3A3A")

def norm(t): return re.sub(r"[^a-z0-9]", "", t.lower())

def vo_words(k):
    out = []
    for w in VO[k]["words"]:
        s, e = w["s"], w["e"]
        if k == "J02":
            if J02_CUT[0] <= s < 19.5 and norm(w["w"]) in ("doctor", "check"): continue
            if s >= J02_CUT[0]:  # large-v3 runs early here; speech resumes at 20.17 (silencedetect)
                sh = J02_CUT[1] - J02_CUT[0]; s, e = max(s, 20.17) - sh, max(e, 20.4) - sh
        out.append({"w": w["w"].strip(), "s": s, "e": e})
    return out

def find(words, phrase, occ=0):
    p = [norm(x) for x in phrase.split()]
    n = [norm(w["w"]) for w in words]
    hits = [i for i in range(len(n)) if n[i:i + len(p)] == p]
    if len(hits) <= occ: raise SystemExit(f"anchor not found: {phrase!r} #{occ}")
    return words[hits[occ]]["s"]

# ---------- EDL ----------
SEQ = ["H01", "I01", ("DR1", 0.0, 40.20), "J01", ("DR2", 40.20, 59.64), "J02", ("DR3", 59.64, 99.16), "B01",
       ("DR4", 99.16, 116.32), "B02", ("DR5", 116.32, 156.20), "U01", ("DR6", 156.20, 190.30), "O01",
       ("DR7", 190.30, 205.20), ("END", 4.5)]
LEAD = 0.9  # every scene transitions in this long; a narrator scene before its voice starts (over the doctor's last words)
GAP_VO_DR, GAP_DR_VO, GAP_VO_VO = 0.35, 0.35, 0.45

items, t, prev = [], 0.0, None
for s in SEQ:
    if isinstance(s, str):
        a = t + (GAP_DR_VO if prev == "dr" else GAP_VO_VO if prev == "vo" else LEAD)
        items.append(dict(kind="vo", id=s, audio=a, start=a - LEAD, end=a + VO_DUR[s]))
        t, prev = a + VO_DUR[s], "vo"
    elif s[0] == "END":
        items.append(dict(kind="end", id="END", start=t + 0.2, end=t + 0.2 + s[1])); t += 0.2 + s[1]
    else:
        a = t + GAP_VO_DR
        cut = (T1[1] - T1[0]) if s[1] < T1[0] < s[2] else 0
        d = s[2] - s[1] - cut
        items.append(dict(kind="dr", id=s[0], src_in=s[1], src_out=s[2], start=a, end=a + d))
        t, prev = a + d, "dr"
for i, it in enumerate(items):  # each scene ends where the next one has finished wiping in
    it["slot_end"] = items[i + 1]["start"] + LEAD + 0.05 if i + 1 < len(items) else it["end"]
    if i + 1 < len(items): it["exit_t"] = items[i + 1]["start"] - it["start"]
TOTAL = round(items[-1]["end"], 2)

def dr_local(src_t, it):
    """doctor source time -> scene-local time (accounts for the T1 cut)."""
    if it["src_in"] < T1[0] < it["src_out"] and src_t >= T1[1]: return src_t - it["src_in"] - (T1[1] - T1[0])
    return src_t - it["src_in"]

def D(phrase, it, occ=0):
    words = [w for w in DRW if it["src_in"] <= w["s"] < it["src_out"]]
    return round(dr_local(find(words, phrase, occ), it), 3)

# ---------- text helpers ----------
def words_html(text, cls="w"):
    return " ".join(f'<span class="{cls}">{html.escape(x)}</span>' if not x.startswith("<") else x for x in text.split(" "))

def letters_html(text):
    return "".join(f'<span class="l">{html.escape(ch) if ch != " " else "&nbsp;"}</span>' for ch in text)

ENTER = {
    "blur": lambda s, t: f'tl.fromTo("{s} .w",{{opacity:0,filter:"blur(8px)"}},{{opacity:1,filter:"blur(0px)",duration:0.16,stagger:0.067,ease:"power4.out"}},{t});',
    "ink": lambda s, t: f'tl.fromTo("{s} .w",{{opacity:0.12}},{{opacity:1,duration:0.22,stagger:0.085,ease:"power2.out"}},{t});',
    "rise": lambda s, t: f'tl.fromTo("{s} .in",{{yPercent:110,rotationX:-55,transformPerspective:900,transformOrigin:"50% 100%"}},{{yPercent:0,rotationX:0,duration:0.8,ease:"power4.out"}},{t});',
    "mask": lambda s, t: f'tl.fromTo("{s} .in",{{clipPath:"inset(0% 100% 0% 0%)"}},{{clipPath:"inset(0% 0% 0% 0%)",duration:0.7,ease:"expo.out"}},{t});',
    "letters": lambda s, t: f'tl.fromTo("{s} .l",{{opacity:0,filter:"blur(4px)"}},{{opacity:1,filter:"blur(0px)",duration:0.2,stagger:0.035,ease:"power3.out"}},{t});',
    "pop": lambda s, t: f'tl.fromTo("{s} .in",{{scale:0.6,opacity:0}},{{scale:1,opacity:1,duration:0.5,ease:"back.out(1.6)"}},{t});',
}

def beat_markup(bid, b):
    txt, kind = b["text"], b.get("enter", "blur")
    inner = letters_html(txt) if kind == "letters" else words_html(txt)
    inner = f'<span class="in">{inner}</span>'
    return f'<div id="{bid}" class="beat {b.get("cls", "")}" style="{b.get("style", "")}">{inner}</div>'

def gate(sel, t): return f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:1,duration:0.01}},{t});'

# ---------- transitions (shared by every scene) ----------
def mask_in(sel, a, b, d=LEAD):
    """soft feathered mask sweep: a/b are the gradient at start/end; removed once done"""
    return (f'tl.fromTo("{sel}",{{maskImage:"{a}",webkitMaskImage:"{a}"}},{{maskImage:"{b}",webkitMaskImage:"{b}",duration:{d},ease:"power2.inOut"}},0);'
            f'tl.set("{sel}",{{maskImage:"none",webkitMaskImage:"none"}},{d + 0.01:.2f});')

SWEEP = ("linear-gradient(100deg, rgba(0,0,0,1) -30%, rgba(0,0,0,0) 0%)", "linear-gradient(100deg, rgba(0,0,0,1) 100%, rgba(0,0,0,0) 130%)")
IRIS = ("radial-gradient(circle at 45% 45%, rgba(0,0,0,1) -25%, rgba(0,0,0,0) 0%)", "radial-gradient(circle at 45% 45%, rgba(0,0,0,1) 100%, rgba(0,0,0,0) 125%)")

def vo_in(sid):
    """narrator scene arrives: feathered sweep + a light streak riding its edge + the type settles out of a zoom-blur"""
    return (mask_in(f"#{sid}-all", *SWEEP) +
            f'\ntl.fromTo("#{sid}-streak",{{x:-460,opacity:0}},{{x:2040,duration:{LEAD},ease:"power2.inOut"}},0);'
            f'tl.to("#{sid}-streak",{{opacity:1,duration:0.15}},0);tl.to("#{sid}-streak",{{opacity:0,duration:0.2}},{LEAD - 0.2:.2f});'
            f'\ntl.fromTo("#{sid}-stage",{{scale:1.08,filter:"blur(10px)"}},{{scale:1,filter:"blur(0px)",duration:1.1,ease:"power3.out"}},0);')

def exit_js(sel, t0):
    """outgoing scene pushes forward and softens while the next one sweeps over it"""
    return f'tl.to("{sel}",{{scale:1.06,filter:"blur(8px)",duration:{LEAD + 0.05},ease:"power2.in"}},{t0:.3f});'

def ambient_js(sid, dur):
    """slow background life: blobs drift, the bed pushes in, the grain moves every frame"""
    return (f'tl.fromTo("#{sid}-bg",{{scale:1}},{{scale:1.06,duration:{dur:.2f},ease:"none"}},0);'
            f'tl.fromTo("#{sid}-o1",{{x:-120,y:-40}},{{x:160,y:60,duration:{dur:.2f},ease:"sine.inOut"}},0);'
            f'tl.fromTo("#{sid}-o2",{{x:140,y:50}},{{x:-120,y:-60,duration:{dur:.2f},ease:"sine.inOut"}},0);'
            f'tl.fromTo("#{sid}-all .grain",{{x:0,y:0}},{{x:-90,y:60,duration:{dur:.2f},ease:"steps({max(1, int(dur * 12))})"}},0);')

def beats_js(sid, beats, scene_end):
    js = []
    for i, b in enumerate(beats):
        sel = f"#{sid}-b{i}"
        js.append(gate(sel, b["at"]) + ENTER[b.get("enter", "blur")](sel, b["at"]))
        out = b.get("out")
        if out is None:
            nxt = [x["at"] for x in beats[i + 1:] if not x.get("stack")]
            out = nxt[0] - 0.08 if nxt else None
        if out is not None and out < scene_end - 0.1:
            js.append(f'tl.to("{sel}",{{opacity:0,filter:"blur(8px)",duration:0.2,ease:"power3.in"}},{max(out - 0.2, b["at"] + 0.3):.3f});')
    return "\n".join(js)

STYLE_CSS = f"""
#root{{position:absolute;inset:0;overflow:hidden;font-family:Inter,sans-serif}}
.bg{{position:absolute;inset:0}}
.mc .bg{{background:radial-gradient(120% 90% at 75% 20%,#1E3A7A 0%,{C['deep']} 55%,#060B1C 100%)}}
.cc .bg{{background:{C['off']}}}
.nb .bg{{background:{C['paper']} repeating-linear-gradient(0deg,transparent 0 63px,rgba(120,150,190,.18) 63px 64px)}}
.mc{{color:#EEF2FF}} .cc{{color:{C['navy']}}} .nb{{color:{C['graphite']}}}
.grain{{position:absolute;inset:-10%;opacity:.07;mix-blend-mode:overlay}}
.beat{{position:absolute;left:0;right:0;text-align:center;line-height:1.08;letter-spacing:-0.01em}}
.beat .in{{display:inline-block}}
.hero{{font-size:200px;font-weight:900;letter-spacing:-0.04em}}
.big{{font-size:120px;font-weight:900;letter-spacing:-0.03em}}
.mid{{font-size:78px;font-weight:700}}
.sm{{font-size:40px;font-weight:400;letter-spacing:.02em}}
.tag{{font-size:28px;font-weight:700;letter-spacing:.32em;text-transform:uppercase}}
.serif{{font-family:'Playfair Display',serif;font-style:italic;font-weight:400}}
.hand{{font-family:Hand,cursive}}
.red{{color:{C['red']}}} .grey{{color:{C['grey']}}}
.hl .in{{background:linear-gradient(transparent 55%,{C['hi']} 55% 92%,transparent 92%);padding:0 .1em}}
.wipe{{position:absolute;inset:0}}
.orb{{position:absolute;width:900px;height:900px;border-radius:50%;filter:blur(120px);opacity:.55}}
.mc .orb{{background:#2B4FA8}} .cc .orb{{background:#E2D9CA}} .nb .orb{{background:#F1E6CF;opacity:.4}}
.streak{{position:absolute;left:0;top:0;width:340px;height:1080px;opacity:0;filter:blur(8px);
background:linear-gradient(90deg,transparent,rgba(214,69,69,.35) 30%,rgba(255,236,220,.85) 50%,rgba(214,69,69,.35) 70%,transparent)}}
.plate{{position:absolute;overflow:hidden;opacity:0}} .pcam{{position:absolute;inset:-3%}}
.pcam img{{position:absolute;inset:0;width:100%;height:100%}} .ghost{{opacity:0;mix-blend-mode:screen}}
.scrim{{position:absolute;inset:0}} .leak{{position:absolute;inset:0;mix-blend-mode:screen;opacity:0;pointer-events:none}}
.leak video{{width:1920px;height:1080px;object-fit:cover}}
.onph{{color:#fff !important;text-shadow:0 2px 28px rgba(0,0,0,.55)}} .onph.hl .in{{background:none;color:{C['hi']}}}
.bignum{{position:absolute;left:0;right:0;top:330px;height:360px;opacity:0;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:340px;
color:#CFE0FF;text-shadow:0 0 60px rgba(120,160,255,.55)}} .bignum .r{{position:absolute;left:0;right:0;text-align:center;line-height:360px;opacity:0}}
.lcd{{position:absolute;left:1330px;top:250px;width:330px;padding:22px 30px;border-radius:22px;background:rgba(10,18,40,.72);border:2px solid rgba(157,183,255,.35);
font-family:'JetBrains Mono',monospace;color:#CFE0FF;opacity:0}} .lcd .k{{font-size:22px;letter-spacing:.3em;color:#9DB7FF}}
.lcd .n{{position:absolute;left:30px;top:58px;font-size:96px;font-weight:700;opacity:0}} .lcd .box{{height:120px}}
.streak.mc{{background:linear-gradient(90deg,transparent,rgba(80,130,255,.4) 30%,rgba(220,232,255,.9) 50%,rgba(80,130,255,.4) 70%,transparent)}}
"""

FONT_FACE = "@font-face{font-family:Hand;src:url('assets/fonts/hand.ttf')}"
GRAIN = ('<svg class="grain" width="100%" height="100%"><filter id="{id}"><feTurbulence type="fractalNoise" baseFrequency=".9" '
         'numOctaves="2" seed="7"/></filter><rect width="100%" height="100%" filter="url(#{id})"/></svg>')

def ecg_path(w=1920, y=540, amp=1.0, dip=False):
    seg = f"L {{x}} {y} l 30 0 l 14 {-40*amp} l 16 {120*amp} l 18 {-190*amp} l 16 {130*amp} l 14 {-20*amp} l 40 0"
    d, x = f"M -40 {y} ", 0
    while x < w + 40:
        d += seg.format(x=x) + " "; x += 380
    return d

def comp(sid, style, body, js, dur):
    return f"""<template>
<style>{FONT_FACE}{STYLE_CSS.replace('#root', '#root')}</style>
<div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080">
<div id="{sid}-all" class="wipe {style}"><div id="{sid}-bg" class="bg"></div>
<div id="{sid}-o1" class="orb" style="left:-200px;top:-300px"></div><div id="{sid}-o2" class="orb" style="right:-250px;bottom:-350px"></div>
{GRAIN.format(id=sid + '-n')}
<div id="{sid}-stage" class="wipe" data-layout-allow-overlap>
{body}
</div>
</div>
<div id="{sid}-streak" class="streak {style}" data-layout-ignore></div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
tl.set({{}}, {{}}, {dur:.3f});
window.__timelines["{sid}"] = tl;
</script>
</template>"""

# ---------- story plates (v3 stills, prep_plates.py) ----------
# enter masks: the plate is revealed by a keyframed clip-path, never a plain cut
MASKS = {
    "slit": ("inset(50% 0% 50% 0%)", "inset(0% 0% 0% 0%)", 1.3, "power3.inOut"),      # eyes opening
    "iris": ("circle(0% at {o})", "circle(150% at {o})", 1.0, "power2.in"),
    "up": ("inset(100% 0% 0% 0%)", "inset(0% 0% 0% 0%)", 0.9, "expo.out"),
    "draw": ("inset(0% 0% 100% 0%)", "inset(0% 0% 0% 0%)", 1.1, "power1.inOut"),      # pencil goes top to bottom
    "fromC_L": ("inset(0% 0% 0% 100%)", "inset(0% 0% 0% 0%)", 0.8, "expo.out"),       # opens from the centre line outwards
    "fromC_R": ("inset(0% 100% 0% 0%)", "inset(0% 0% 0% 0%)", 0.8, "expo.out"),
}
SCRIM = {"dark": "linear-gradient(180deg,rgba(6,11,28,.62),rgba(6,11,28,.28) 45%,rgba(6,11,28,.7))",
         "night": "rgba(6,11,28,.72)", "paper": "rgba(250,246,238,.5)", "light": "rgba(244,241,236,.78)",
         "low": "linear-gradient(90deg,rgba(6,11,28,.72),rgba(6,11,28,.2) 60%)",
         "warm": "linear-gradient(180deg,rgba(40,20,5,.6),rgba(40,20,5,.15) 55%,rgba(40,20,5,.05))",
         "right": "linear-gradient(270deg,rgba(6,11,28,.8),rgba(6,11,28,.45) 45%,rgba(6,11,28,.1) 75%)"}

def handheld(sel, t0, t1, amp=6):
    """deterministic handheld drift (after the Cinecom 'Real Handheld Movement' preset): small x/y steps, sine eased"""
    js, t, k = [], t0, 0
    while t < t1 - 0.2:
        d = min(1.1, t1 - t)
        x, y = amp * math.sin(k * 2.3 + 1), amp * 0.7 * math.cos(k * 1.7 + 2)
        js.append(f'tl.to("{sel}",{{x:{x:.1f},y:{y:.1f},duration:{d:.2f},ease:"sine.inOut"}},{t:.3f});')
        t += d; k += 1
    return "".join(js)

def plates(sid, ps):
    """ps: dicts with src, t0, t1 and optional box(l,t,w,h), enter, o (mask/zoom origin), z0/z1 (scale), x0/x1, scrim, fit, hold, css"""
    mk, js = [], []
    for i, p in enumerate(ps):
        pid = f"{sid}-p{i}"; l, tp, w, h = p.get("box", (0, 0, 1920, 1080)); o = p.get("o", "50% 50%")
        scrim = f'<div class="scrim" style="background:{SCRIM[p["scrim"]]}"></div>' if p.get("scrim") else ""
        ghost = f'<img id="{pid}-g" class="ghost" src="assets/plates/{p["src"]}" style="object-fit:{p.get("fit", "cover")}"/>' if p.get("ghost") else ""
        mk.append(f'<div id="{pid}" class="plate" style="left:{l}px;top:{tp}px;width:{w}px;height:{h}px;{p.get("css", "")}"><div id="{pid}-c" class="pcam">'
                  f'<img id="{pid}-i" src="assets/plates/{p["src"]}" style="object-fit:{p.get("fit", "cover")};object-position:{p.get("pos", "50% 50%")};transform-origin:{o}"/>{ghost}</div>{scrim}</div>')
        t0, t1, en = p["t0"], p["t1"], p.get("enter", "fade")
        if en == "fade":
            js.append(f'tl.fromTo("#{pid}",{{opacity:0}},{{opacity:1,duration:{p.get("fd", 0.6)},ease:"power2.out"}},{t0:.3f});')
        else:
            a, b, d, e = MASKS[en]; a, b = a.format(o=o), b.format(o=o)
            js.append(gate(f"#{pid}", t0) + f'tl.fromTo("#{pid}",{{clipPath:"{a}"}},{{clipPath:"{b}",duration:{d},ease:"{e}"}},{t0:.3f});')
        js.append(f'tl.fromTo("#{pid}-i",{{scale:{p.get("z0", 1.04)},x:{p.get("x0", 0)},y:{p.get("y0", 0)}}},'
                  f'{{scale:{p.get("z1", 1.12)},x:{p.get("x1", 0)},y:{p.get("y1", 0)},duration:{t1 - t0 + 0.6:.2f},ease:"{p.get("ease", "sine.inOut")}"}},{t0:.3f});')
        if p.get("hh", True): js.append(handheld(f"#{pid}-c", t0, t1 + 0.4, p.get("hh_amp", 5)))
        if not p.get("hold"): js.append(f'tl.to("#{pid}",{{opacity:0,duration:0.35,ease:"power2.in"}},{t1 - 0.35:.3f});')
    return "\n".join(mk), "\n".join(js)

def leak(lid, src, t0, d, peak=0.85):
    """VIP film-burn / light-leak clip, screen-blended: one rise, peak and recovery"""
    m = (f'<div id="{lid}" class="leak"><video id="{lid}-v" class="clip" src="assets/fx/{src}.mp4" data-start="{t0:.3f}" '
         f'data-duration="{d:.3f}" muted playsinline></video></div>')
    j = (f'tl.fromTo("#{lid}",{{opacity:0}},{{opacity:{peak},duration:{d * 0.3:.2f},ease:"power2.out"}},{t0:.3f});'
         f'tl.to("#{lid}",{{opacity:0,duration:{d * 0.45:.2f},ease:"power2.in"}},{t0 + d * 0.55:.3f});')
    return m, j

# ---------- narrator scenes ----------
def vo_scene(it):
    k, sid = it["id"], it["id"].lower()
    W = vo_words(k)
    A = lambda p, o=0: round(LEAD + find(W, p, o), 3)
    dur = it["slot_end"] - it["start"]
    extra_html, extra_js, style = "", "", "cc"
    ps, ps_extra = [], ""
    # wipe-in: the whole scene is revealed left->right behind a red ECG stroke
    wipe = vo_in(sid)
    if k == "H01":
        style = "mc"
        beats = [
            dict(at=A("72") - 0.3, text="You're", cls="mid", style="top:250px", out=A("72") + 1.1),
            dict(at=A("finally"), text="Your blood pressure is finally coming down.", enter="ink", cls="mid", style="top:150px;left:120px;right:640px;text-align:left"),
            dict(at=A("good"), text="Good news?", enter="blur", cls="big serif", style="top:420px;left:120px;right:640px;text-align:left", stack=True),
            dict(at=A("but now"), text="BUT", enter="pop", cls="hero red", style="top:380px"),
            dict(at=A("every"), text="every time you stand up…", enter="ink", cls="mid", style="top:300px;left:80px;right:50%;text-align:left", out=A("should") - 0.2),
            dict(at=A("the room"), text="the room spins.", enter="blur", cls="big serif", style="top:500px;left:80px;right:50%;text-align:left", stack=True, out=A("should") - 0.2),
            dict(at=A("lower"), text="Even LOWER?", enter="rise", cls="big", style="top:250px", out=A("after") - 0.1),
            dict(at=A("second"), text="Or a second look?", enter="blur", cls="big serif", style="top:420px", stack=True, out=A("after") + 0.8),
            dict(at=A("after"), text="After 65", enter="mask", cls="tag", style="top:250px", out=A("matters") - 0.3),
            dict(at=A("matters"), text="Protect the heart", enter="rise", cls="mid", style="top:420px;left:0;right:50%", stack=True),
            dict(at=A("dangerous"), text="Avoid dangerous drops", enter="rise", cls="mid red", style="top:420px;left:50%;right:0", stack=True),
        ]
        down, stand, rm, spins, but = A("coming"), A("stand"), A("the room"), A("spins"), A("but now")
        # the story: her hand (ring, watch) -> her dawn bedroom, the monitor reading falls -> BUT -> she stands and the room
        # spins -> the dark hallway, where a fall happens -> after 65: her garden vs that hallway
        t72 = A("72")
        ps = [dict(src="dawn_room.jpg", t0=0.0, t1=t72 + 0.5, enter="slit", o="64% 40%", z0=1.5, z1=1.3, scrim="night", css="filter:blur(10px)"),
              dict(src="dawn_hand.jpg", t0=t72 + 0.35, t1=A("blood") - 0.1, enter="iris", o="50% 50%", z0=1.25, z1=1.08, x0=-60, x1=0, scrim="right"),
              dict(src="dawn_room.jpg", t0=A("blood") - 0.4, t1=but - 0.02, enter="iris", o="64% 40%", z0=1.0, z1=1.42, scrim="dark"),
              dict(src="dawn_window.jpg", t0=A("every") - 0.15, t1=A("should") - 0.2, box=(960, 0, 960, 1080), enter="up", o="50% 35%",
                   z0=1.12, z1=1.02, y0=90, y1=0, ease="power3.out", ghost=True),
              dict(src="night_hall.jpg", t0=A("should") - 0.2, t1=A("after") - 0.05, enter="iris", o="32% 76%", z0=1.0, z1=1.35, scrim="dark", ease="power1.in"),
              dict(src="garden.jpg", t0=A("matters") - 0.25, t1=dur, box=(0, 0, 960, 1080), enter="fromC_L", o="40% 60%", z0=1.08, z1=1.16, scrim="dark", hold=True),
              dict(src="night_hall.jpg", t0=A("dangerous") - 0.45, t1=dur, box=(960, 0, 960, 1080), enter="fromC_R", o="32% 76%", z0=1.3, z1=1.36, scrim="dark", hold=True)]
        # home-monitor readout (code-drawn, illustrative numbers) ticks DOWN while the line falls
        nums, f0, f1 = ["158", "151", "144", "137", "129"], A("finally") - 0.1, A("down") + 0.5
        step = (f1 - f0) / len(nums)
        lcd = '<div id="h01-lcd" class="lcd"><div class="k">SYS</div><div class="box">' + "".join(
            f'<div id="h01-n{i}" class="n" data-layout-ignore>{n}</div>' for i, n in enumerate(nums)) + '</div></div>'
        lcd_js = gate("#h01-lcd", f0 - 0.4) + f'tl.fromTo("#h01-lcd",{{y:30}},{{y:0,duration:0.6,ease:"expo.out"}},{f0 - 0.4:.3f});'
        for i in range(len(nums)):
            lcd_js += gate(f"#h01-n{i}", f0 + i * step) + (f'tl.set("#h01-n{i - 1}",{{opacity:0}},{f0 + i * step:.3f});' if i else "")
        lcd_js += f'tl.to("#h01-lcd",{{opacity:0,duration:0.2}},{but - 0.25:.3f});'
        roll = ["158", "151", "143", "136", "128", "119", "111", "102", "94", "87", "80", "72"]
        big = '<div id="h01-big" class="bignum">' + "".join(f'<div id="h01-r{i}" class="r" data-layout-ignore>{n}</div>' for i, n in enumerate(roll)) + '</div>'
        rs = (t72 - 0.15) / len(roll)
        big_js = gate("#h01-big", 0.05) + "".join(gate(f"#h01-r{i}", 0.05 + i * rs) + (f'tl.set("#h01-r{i - 1}",{{opacity:0}},{0.05 + i * rs:.3f});' if i else "") for i in range(len(roll)))
        big_js += (f'tl.fromTo("#h01-big",{{scale:1.6,filter:"blur(6px)"}},{{scale:1,filter:"blur(0px)",duration:{t72:.2f},ease:"power2.out"}},0.05);'
                   f'tl.fromTo("#h01-big",{{color:"#CFE0FF"}},{{color:"#FFFFFF",duration:0.1}},{t72 - 0.1:.3f});'
                   f'tl.fromTo("#h01-flash",{{opacity:0}},{{opacity:0.85,duration:0.05}},{t72 - 0.1:.3f});tl.to("#h01-flash",{{opacity:0,duration:0.35,ease:"power2.out"}},{t72 - 0.05:.3f});'
                   f'tl.to("#h01-big",{{scale:1.12,duration:0.12,ease:"power2.out"}},{t72 - 0.1:.3f});tl.to("#h01-big",{{scale:0.42,x:470,y:40,duration:0.5,ease:"expo.inOut"}},{t72 + 0.25:.3f});'
                   f'tl.to("#h01-big",{{opacity:0,filter:"blur(8px)",duration:0.25}},{A("blood") - 0.3:.3f});')
        extra_html_pre = big + '<div id="h01-flash" class="scrim" style="background:#fff;opacity:0"></div>'
        lk, lkj = leak("h01-leak", "leak_red", but - 0.05, 1.4, 0.55)
        ps_extra = ('<div id="h01-spot" class="scrim" style="opacity:0;background:radial-gradient(circle at 32% 76%,'
                    'rgba(0,0,0,0) 0 170px,rgba(4,8,20,.7) 300px)"></div>')
        extra_html = (f'<svg id="h01-line" width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore>'
                      f'<path id="h01-bp" d="M -20 640 C 300 600, 600 690, 900 720 S 1500 760, 1940 790" fill="none" stroke="{C["red"]}" stroke-width="5" stroke-linecap="round"/>'
                      f'<path id="h01-dip" d="M -20 640 C 300 600, 600 690, 900 720 S 1100 735, 1200 990" fill="none" stroke="{C["red"]}" stroke-width="5" stroke-linecap="round" opacity="0"/></svg>'
                      + lcd + lk + extra_html_pre)
        extra_js = "\n".join([
            f'tl.fromTo("#h01-bp",{{strokeDasharray:2400,strokeDashoffset:2400}},{{strokeDashoffset:0,duration:2.2,ease:"power2.inOut"}},{down - 0.4:.3f});',
            f'tl.to("#h01-bp",{{opacity:0,duration:0.15}},{but - 0.1:.3f});',
            f'tl.fromTo("#h01-dip",{{opacity:0,strokeDasharray:1700,strokeDashoffset:1700}},{{opacity:1,strokeDashoffset:0,duration:0.6,ease:"power3.in"}},{stand:.3f});',
            f'tl.to("#h01-dip",{{opacity:0,duration:0.3}},{A("should") - 0.3:.3f});',
            # the room spins: the plate tilts and smears, a ghost copy slides off it (double vision), then it settles
            f'tl.fromTo("#h01-p3-c",{{rotation:0,scale:1,filter:"blur(0px)"}},{{rotation:10,scale:1.2,filter:"blur(6px)",duration:0.9,ease:"power2.inOut",immediateRender:false}},{rm - 0.1:.3f});',
            f'tl.to("#h01-p3-c",{{rotation:0,scale:1,filter:"blur(0px)",duration:0.8,ease:"power2.out"}},{spins + 0.8:.3f});',
            f'tl.fromTo("#h01-p3-g",{{opacity:0,x:0}},{{opacity:0.6,x:70,duration:0.5,ease:"sine.inOut",immediateRender:false}},{rm - 0.1:.3f});',
            f'tl.to("#h01-p3-g",{{x:-30,duration:0.6,ease:"sine.inOut"}},{rm + 0.5:.3f});',
            f'tl.to("#h01-p3-g",{{opacity:0,x:0,duration:0.6}},{spins + 0.8:.3f});',
            f'tl.fromTo("#h01-stage",{{rotation:0}},{{rotation:1.6,duration:1.0,ease:"power2.inOut",immediateRender:false}},{spins - 0.2:.3f});',
            f'tl.to("#h01-stage",{{rotation:0,duration:0.6,ease:"power2.out"}},{spins + 1.1:.3f});',
            # "a second look": the hallway darkens round the curled rug
            f'tl.fromTo("#h01-spot",{{opacity:0}},{{opacity:1,duration:0.9,ease:"power2.inOut"}},{A("second") - 0.3:.3f});',
            f'tl.to("#h01-spot",{{opacity:0,duration:0.3}},{A("after") - 0.35:.3f});',
            lcd_js, lkj, big_js,
            # drama: snap punch-ins on the hits, a hard camera shake while the room spins
            f'tl.fromTo("#h01-stage",{{scale:1.22}},{{scale:1,duration:0.45,ease:"expo.out",immediateRender:false}},{but:.3f});',
            f'tl.fromTo("#h01-stage",{{scale:1.12}},{{scale:1,duration:0.5,ease:"expo.out",immediateRender:false}},{A("lower"):.3f});',
            "".join(f'tl.to("#h01-stage",{{x:{18 * math.sin(i * 2.1):.1f},y:{12 * math.cos(i * 1.7):.1f},duration:0.07,ease:"none"}},{rm + 0.1 + i * 0.07:.3f});' for i in range(12)),
            f'tl.to("#h01-stage",{{x:0,y:0,duration:0.2,ease:"power2.out"}},{rm + 0.1 + 12 * 0.07:.3f});',
            f'tl.fromTo("#h01-vig",{{opacity:0}},{{opacity:1,duration:0.15}},{rm:.3f});tl.to("#h01-vig",{{opacity:0,duration:0.9,ease:"power2.out"}},{spins + 0.5:.3f});'])
        extra_html += '<div id="h01-vig" class="scrim" style="opacity:0;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,0) 45%,rgba(140,20,20,.55) 100%)"></div>'
        wipe = 'tl.fromTo("#h01-stage",{scale:1.06},{scale:1,duration:1.6,ease:"power3.out"},0);'
    elif k == "I01":
        beats = [
            dict(at=A("rehan"), text="Dr. Rehan Omer", enter="letters", cls="big", style="top:330px;left:600px;right:60px;text-align:left"),
            dict(at=A("consultant"), text="Consultant Interventional Cardiologist & Diabetologist", enter="mask", cls="sm", style="top:500px;left:600px;right:60px;text-align:left", stack=True),
            dict(at=A("that means"), text="He opens blocked heart arteries", enter="ink", cls="mid", style="top:300px;left:600px;right:60px;text-align:left"),
            dict(at=A("without"), text="without open surgery", enter="blur", cls="mid serif red", style="top:400px;left:600px;right:60px;text-align:left", stack=True),
            dict(at=A("diabetes"), text="+ treats diabetes", enter="rise", cls="mid", style="top:520px;left:600px;right:60px;text-align:left", stack=True),
            dict(at=A("right"), text="The right target isn't the same for everyone.", enter="ink", cls="mid", style="top:170px;left:80px;right:900px;text-align:left"),
        ]
        r = A("right")
        card = "border-radius:18px;box-shadow:0 30px 80px rgba(20,33,61,.35)"
        ps = [dict(src="consult.jpg", t0=0.0, t1=dur, scrim="light", o="40% 60%", z0=1.0, z1=1.1, fd=0.3, hold=True),
              dict(src="coat_door.jpg", t0=0.3, t1=A("that means") - 0.05, box=(130, 150, 400, 760), enter="up", o="50% 45%", css=card, hh_amp=3),
              dict(src="cuff.jpg", t0=A("that means") - 0.1, t1=r - 0.1, box=(130, 150, 400, 760), enter="iris", o="62% 50%", pos="80% 50%", css=card, hh_amp=3)]
        extra_html = f'<div id="i01-still" style="position:absolute;left:960px;top:0;width:960px;height:1080px;overflow:hidden"><img id="i01-img" src="assets/dr_still.jpg" style="position:absolute;left:-480px;top:0;width:1920px;height:1080px"/></div>'
        extra_js = f'''tl.fromTo("#i01-still",{{clipPath:"circle(0% at 50% 45%)"}},{{clipPath:"circle(80% at 50% 45%)",duration:0.8,ease:"expo.out"}},{r - 0.1});
tl.fromTo("#i01-img",{{scale:1}},{{scale:1.05,duration:{dur - r:.2f},ease:"none"}},{r - 0.1});'''
    elif k == "J01":
        style = "nb"
        beats = [
            dict(at=A("in plain"), text="In plain words", enter="mask", cls="tag", style="top:150px"),
            dict(at=A("cholesterol"), text="#1 High cholesterol", enter="ink", cls="mid hand grey", style="top:300px", stack=True),
            dict(at=A("high", 1), text="#2 High blood pressure", enter="ink", cls="mid hand", style="top:420px", stack=True),
            dict(at=A("blocked"), text="→ blocked heart arteries", enter="blur", cls="sm hand", style="top:560px", stack=True, out=A("but after") - 0.1),
            dict(at=A("but after"), text="But after 65…", enter="rise", cls="big hand", style="top:340px"),
            dict(at=A("catch"), text="there's a catch.", enter="blur", cls="mid hand hl", style="top:520px", stack=True),
        ]
        s = A("strongest")
        ps = [dict(src="kitchen.jpg", t0=0.0, t1=A("cholesterol") - 0.15, scrim="paper", o="45% 75%", z0=1.0, z1=1.6, ease="power2.in", fd=0.3)]
        extra_html = f'<svg width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore><ellipse id="j01-ring" cx="960" cy="468" rx="560" ry="80" fill="none" stroke="{C["red"]}" stroke-width="5" transform="rotate(-2 960 468)"/></svg>'
        extra_js = f'''tl.fromTo("#j01-ring",{{strokeDasharray:2400,strokeDashoffset:2400}},{{strokeDashoffset:0,duration:0.7,ease:"power2.inOut"}},{s});
tl.to("#j01-ring",{{opacity:0,duration:0.2}},{A("but after") - 0.3});'''
    elif k == "J02":
        style = "nb"
        beats = [
            dict(at=A("quick"), text="Quick fix on one word", enter="mask", cls="tag", style="top:150px"),
            dict(at=A("called"), text="Orthostatic HYPOtension", enter="ink", cls="big hand", style="top:300px"),
            dict(at=A("hypo") - 0.1, text="HYPER = high", enter="blur", cls="mid hand grey", style="top:300px", stack=True),
            dict(at=A("means"), text="HYPO = low ✓", enter="rise", cls="mid hand hl", style="top:450px", stack=True),
            dict(at=A("you get"), text="stand up", enter="pop", cls="mid hand", style="top:150px;left:0;right:66%"),
            dict(at=A("falls"), text="→ BP falls", enter="pop", cls="mid hand red", style="top:150px;left:33%;right:33%", stack=True),
            dict(at=A("dizzy"), text="→ dizzy, faint", enter="pop", cls="mid hand", style="top:150px;left:66%;right:0", stack=True),
            dict(at=A("that's"), text="Check BP sitting AND standing", enter="ink", cls="mid hand", style="top:170px"),
            dict(at=A("should"), text="Should older people be treated at all?", enter="blur", cls="mid serif", style="top:420px"),
        ]
        h = A("means")
        sk = dict(fit="contain", enter="draw", hh=False, z0=1.0, z1=1.02, t1=A("that's") - 0.1)
        ps = [dict(sk, src="sk_sit.png", t0=A("you get") - 0.2, box=(172, 270, 296, 640)),
              dict(sk, src="sk_rise.png", t0=A("falls") - 0.3, box=(840, 270, 240, 640)),
              dict(sk, src="sk_dizzy.png", t0=A("dizzy") - 0.3, box=(1474, 270, 252, 640)),
              dict(src="cuff.jpg", t0=A("that's") - 0.1, t1=A("should") - 0.1, box=(560, 320, 800, 450), enter="iris", o="62% 50%",
                   css="border-radius:18px;box-shadow:0 30px 80px rgba(58,58,58,.3);transform:rotate(-2deg)", hh_amp=3)]
        extra_html = f'<svg width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore><path id="j02-strike" d="M 700 350 L 1220 345" stroke="{C["red"]}" stroke-width="7" stroke-linecap="round"/></svg>'
        extra_js = f'''tl.fromTo("#j02-strike",{{strokeDasharray:560,strokeDashoffset:560,opacity:1}},{{strokeDashoffset:0,duration:0.35,ease:"power2.out"}},{h - 0.3});
tl.to("#j02-strike",{{opacity:0,duration:0.2}},{A("you get") - 0.3});'''
        # the HYPOtension line hides when the HYPER/HYPO rows arrive
        beats[1]["out"] = A("hypo") - 0.15
    elif k == "B01":
        beats = [
            dict(at=A("so what"), text="What counts as HIGH?", enter="ink", cls="big", style="top:250px"),
            dict(at=A("that line"), text="The line has moved.", enter="blur", cls="mid serif", style="top:640px", stack=True),
        ]
        m = A("moved")
        extra_html = f'''<svg width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore>
<line id="b01-axis" x1="360" y1="520" x2="1560" y2="520" stroke="{C['navy']}" stroke-width="4"/>
<text x="560" y="590" font-size="40" font-family="Inter" fill="{C['grey']}" text-anchor="middle">140</text>
<text x="1360" y="590" font-size="40" font-family="Inter" fill="{C['grey']}" text-anchor="middle">150</text>
<g id="b01-mark"><circle cx="1360" cy="520" r="18" fill="{C['red']}"/></g></svg>'''
        extra_js = f'''tl.fromTo("#b01-axis",{{strokeDasharray:1200,strokeDashoffset:1200}},{{strokeDashoffset:0,duration:0.8,ease:"power2.inOut"}},{A("high") - 0.2});
tl.fromTo("#b01-mark",{{x:0}},{{x:-800,duration:1.4,ease:"power2.inOut"}},{m - 0.4});'''
    elif k == "B02":
        style = "mc"
        beats = [
            dict(at=A("here's"), text="Here's the challenge.", enter="mask", cls="tag", style="top:140px"),
            dict(at=A("untreated"), text="Untreated → heart at risk", enter="ink", cls="mid", style="top:230px"),
            dict(at=A("carelessly"), text="Lowered carelessly → falls", enter="ink", cls="mid red", style="top:230px"),
            dict(at=A("so how"), text="Protect the heart without new danger?", enter="blur", cls="mid serif", style="top:230px"),
            dict(at=A("by choosing"), text="Medicine that fits the PERSON.", enter="rise", cls="mid", style="top:230px"),
        ]
        ps = [dict(src="night_hall.jpg", t0=0.0, t1=A("by choosing") + 0.8, scrim="night", o="32% 76%", z0=1.0, z1=1.15, fd=0.3),
              dict(src="warm_room.jpg", t0=A("by choosing") - 0.2, t1=dur, scrim="dark", o="64% 40%", z0=1.05, z1=1.12, fd=1.4, hold=True)]
        extra_html = f'''<svg width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore>
<line x1="960" y1="520" x2="960" y2="900" stroke="#9DB7FF" stroke-width="6"/><path d="M 880 900 L 1040 900" stroke="#9DB7FF" stroke-width="6"/>
<g id="b02-beam" style="transform-origin:960px 520px"><line x1="560" y1="520" x2="1360" y2="520" stroke="#EEF2FF" stroke-width="6"/>
<g id="b02-l"><path d="M 470 660 Q 560 720 650 660 Z" fill="none" stroke="#EEF2FF" stroke-width="4"/><line x1="560" y1="520" x2="470" y2="660" stroke="#EEF2FF" stroke-width="2"/><line x1="560" y1="520" x2="650" y2="660" stroke="#EEF2FF" stroke-width="2"/>
<path d="M 560 650 c -30 -30 -60 0 -30 30 l 30 28 l 30 -28 c 30 -30 0 -60 -30 -30 z" fill="{C['red']}"/></g>
<g id="b02-r"><path d="M 1270 660 Q 1360 720 1450 660 Z" fill="none" stroke="#EEF2FF" stroke-width="4"/><line x1="1360" y1="520" x2="1270" y2="660" stroke="#EEF2FF" stroke-width="2"/><line x1="1360" y1="520" x2="1450" y2="660" stroke="#EEF2FF" stroke-width="2"/>
<text x="1360" y="652" font-size="40" font-family="Inter" font-weight="700" fill="#9DB7FF" text-anchor="middle">falls</text></g></g></svg>'''
        extra_js = f'''tl.fromTo("#b02-beam",{{rotation:0}},{{rotation:-9,duration:0.9,ease:"power2.inOut"}},{A("heart") - 0.2});
tl.to("#b02-beam",{{rotation:9,duration:1.1,ease:"power2.inOut"}},{A("falls") - 0.3});
tl.to("#b02-beam",{{rotation:0,duration:1.4,ease:"elastic.out(1,0.75)"}},{A("fit")});
tl.fromTo("#b02-l",{{rotation:0}},{{rotation:9,duration:0.9,ease:"power2.inOut",svgOrigin:"560 520"}},{A("heart") - 0.2});
tl.to("#b02-l",{{rotation:-9,duration:1.1,ease:"power2.inOut",svgOrigin:"560 520"}},{A("falls") - 0.3});
tl.to("#b02-l",{{rotation:0,duration:1.4,ease:"elastic.out(1,0.75)",svgOrigin:"560 520"}},{A("fit")});
tl.fromTo("#b02-r",{{rotation:0}},{{rotation:9,duration:0.9,ease:"power2.inOut",svgOrigin:"1360 520"}},{A("heart") - 0.2});
tl.to("#b02-r",{{rotation:-9,duration:1.1,ease:"power2.inOut",svgOrigin:"1360 520"}},{A("falls") - 0.3});
tl.to("#b02-r",{{rotation:0,duration:1.4,ease:"elastic.out(1,0.75)",svgOrigin:"1360 520"}},{A("fit")});'''
    elif k == "U01":
        style = "nb"
        beats = [
            dict(at=A("one point"), text="One point, in more detail", enter="mask", cls="tag", style="top:150px"),
            dict(at=A("diuretics"), text="Diuretics (water tablets)", enter="ink", cls="big hand", style="top:300px"),
            dict(at=A("aren't"), text="not automatically off-limits", enter="blur", cls="mid hand hl", style="top:480px", stack=True),
            dict(at=A("in fact"), text="HYVET trial · age 80+", enter="ink", cls="mid hand", style="top:300px"),
            dict(at=A("150"), text="aimed for 150/80", enter="pop", cls="big hand red", style="top:430px", stack=True),
            dict(at=A("today"), text="Today: no single target", enter="rise", cls="big hand", style="top:200px"),
            dict(at=A("dizziness"), text="dizziness · frailty · kidneys · other conditions", enter="ink", cls="sm hand", style="top:420px", stack=True),
            dict(at=A("even"), text="Some prostate medicines → BP drop on standing", enter="ink", cls="mid hand", style="top:600px", stack=True),
        ]
    elif k == "O01":
        style = "nb"
        beats = [
            dict(at=A("so what"), text="Your BP after 65?", enter="ink", cls="big hand onph", style="top:200px"),
            dict(at=A("there's no"), text="No ONE number.", enter="rise", cls="big hand", style="top:300px"),
            dict(at=A("the real"), text="Is it controlled", enter="ink", cls="mid hand", style="top:300px"),
            dict(at=A("safely"), text="SAFELY?", enter="pop", cls="hero hand hl", style="top:400px", stack=True),
            dict(at=A("if you"), text="Dizzy when you stand", enter="ink", cls="mid hand", style="top:240px;text-align:left;left:520px"),
            dict(at=A("keep"), text="Keep falling", enter="ink", cls="mid hand", style="top:360px;text-align:left;left:520px", stack=True),
            dict(at=A("unwell"), text="Unwell after medicine", enter="ink", cls="mid hand", style="top:480px;text-align:left;left:520px", stack=True),
            dict(at=A("talk"), text="→ talk to your doctor", enter="rise", cls="mid hand red", style="top:640px;text-align:left;left:520px", stack=True),
            dict(at=A("the goal"), text="Not just lower.", enter="blur", cls="big hand onph", style="top:300px;left:80px;right:760px;text-align:left"),
            dict(at=A("better"), text="Better PROTECTION.", enter="rise", cls="big hand onph hl", style="top:450px;left:80px;right:760px;text-align:left", stack=True),
            dict(at=A("never"), text="Never change your BP medicine on your own.", enter="ink", cls="mid", style="top:380px"),
            dict(at=A("own") + 0.4, text="For education only. Talk to your own doctor before changing any medicine.", enter="blur", cls="sm grey", style="top:620px", stack=True),
        ]
    if k == "O01":
        g, nv = A("the goal"), A("and never")
        ps = [dict(src="dawn_room.jpg", t0=0.0, t1=2.0, scrim="dark", o="64% 40%", z0=1.0, z1=1.12, fd=0.3),
              dict(src="warm_room.jpg", t0=0.6, t1=A("there's no") - 0.1, scrim="warm", o="64% 40%", z0=1.03, z1=1.42, fd=1.4),
              dict(src="sk_dizzy.png", t0=A("if you") - 0.2, t1=g - 0.3, box=(170, 230, 280, 606), fit="contain", enter="draw", hh=False, z0=1.0, z1=1.02),
              dict(src="garden.jpg", t0=g - 0.25, t1=nv - 0.1, enter="iris", o="22% 38%", z0=1.0, z1=1.12, scrim="low"),
              dict(src="lily_run.jpg", t0=A("better") - 0.3, t1=nv - 0.1, box=(1240, 110, 520, 800), enter="up", o="50% 60%",
                   css="border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.35)", hh_amp=3)]
        lk, lkj = leak("o01-leak", "leak_warm", A("better") - 0.4, 2.6, 0.7)
        extra_html += lk; extra_js += "\n" + lkj
    beats = sorted(beats, key=lambda b: b["at"])
    for b in beats: b["at"] = round(b["at"], 3)
    ph, pj = plates(sid, ps)
    body = ph + ps_extra + "\n".join(beat_markup(f"{sid}-b{i}", b) for i, b in enumerate(beats)) + extra_html
    js = wipe + "\n" + pj + "\n" + ambient_js(sid, dur) + "\n" + beats_js(sid, beats, dur) + "\n" + extra_js + "\n" + (exit_js(f"#{sid}-stage", it["exit_t"]) if "exit_t" in it else "")
    return comp(sid, style, body, js, dur), style

# ---------- doctor scenes ----------
FACE_ORIGIN = "45% 45%"  # his face sits at ~x860,y480 in 1920x1080

def pop_left(pid, t0, t1, title, sub="", enter="mask"):
    """keyword pop on the empty grey wall to his left (x 90..640), never over the face"""
    sub_html = f'<div class="pop-sub">{html.escape(sub)}</div>' if sub else ""
    m = f'<div id="{pid}" class="pop"><div class="in"><div class="pop-t">{html.escape(title)}</div>{sub_html}</div></div>'
    js = gate(f"#{pid}", t0) + ENTER[enter](f"#{pid}", t0) + f'\ntl.to("#{pid}",{{opacity:0,filter:"blur(8px)",duration:0.2,ease:"power3.in"}},{t1 - 0.2:.3f});'
    return m, js, t0

DR_CSS = f"""
#root{{position:absolute;inset:0;overflow:hidden;font-family:Inter,sans-serif;background:{C['off']}}}
.cam{{position:absolute;inset:0;transform-origin:{FACE_ORIGIN}}}
.cam video{{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}}
.pop{{position:absolute;left:90px;top:300px;width:560px;color:{C['navy']}}}
.pop .in{{display:block;border-left:6px solid {C['red']};padding:14px 0 14px 28px;background:rgba(244,241,236,.86)}}
.pop-t{{font-size:54px;font-weight:900;line-height:1.05;letter-spacing:-0.02em}}
.pop-sub{{font-size:30px;font-weight:400;margin-top:10px;color:#3c4660}}
.card{{position:absolute;left:0;top:0;width:900px;height:1080px;background:{C['off']};color:{C['navy']};padding:150px 90px}}
.row{{font-size:44px;font-weight:700;margin:0 0 34px;line-height:1.15}}
.row small{{display:block;font-size:30px;font-weight:400;color:{C['grey']};margin-top:6px}}
.lt{{position:absolute;left:90px;bottom:200px;color:{C['navy']}}}
.lt .in{{display:block;background:rgba(244,241,236,.92);padding:22px 34px;border-left:8px solid {C['red']}}}
.lt-n{{font-size:56px;font-weight:900;letter-spacing:-0.02em}} .lt-r{{font-size:28px;margin-top:6px}}
.lt-tag{{font-size:20px;letter-spacing:.3em;color:{C['red']};font-weight:700;margin-bottom:10px}}
"""

def dr_scene(it):
    sid, d0 = it["id"].lower(), it["end"] - it["start"]
    dur = it["slot_end"] - it["start"]
    split_cut = it["src_in"] < T1[0] < it["src_out"]
    if split_cut:
        a = T1[0] - it["src_in"]
        vids = (f'<video id="{sid}-v1" class="clip" src="assets/doctor.mp4" data-start="0" data-duration="{a:.3f}" data-media-start="{it["src_in"]:.3f}" data-has-audio="true" playsinline></video>'
                f'<video id="{sid}-v2" class="clip" src="assets/doctor.mp4" data-start="{a:.3f}" data-duration="{d0 - a:.3f}" data-media-start="{T1[1]:.3f}" data-has-audio="true" playsinline></video>')
    else:
        vids = f'<video id="{sid}-v" class="clip" src="assets/doctor.mp4" data-start="0" data-duration="{d0:.3f}" data-media-start="{it["src_in"]:.3f}" data-has-audio="true" playsinline></video>'
    over, js = [], []
    cam = []  # (t, scale, how) -- how: cut | push(dur)
    P = lambda *a, **k: over.append(pop_left(*a, **k))
    if sid == "dr1":
        lt = f'<div id="dr1-lt" class="lt"><div class="in"><div class="lt-tag">DECODE YOUR HEART</div><div class="lt-n">{letters_html("Dr. Rehan Omer")}</div><div class="lt-r">Consultant Interventional Cardiologist &amp; Diabetologist</div></div></div>'
        over.append((lt, gate("#dr1-lt", 0.4) + ENTER["letters"]("#dr1-lt", 0.6) + '\ntl.fromTo("#dr1-lt .in",{clipPath:"inset(0% 100% 0% 0%)"},{clipPath:"inset(0% 0% 0% 0%)",duration:0.7,ease:"expo.out"},0.4);\ntl.to("#dr1-lt",{opacity:0,filter:"blur(8px)",duration:0.25,ease:"power3.in"},5.6);', 0))
        h = D("hypoepidemias", it); P("dr1-p1", h, h + 3.4, "Hyperlipidemia", "= high cholesterol")
        ih = D("inter heart", it, 1); P("dr1-p2", ih, ih + 4.0, "INTERHEART", "a large worldwide heart-attack study", enter="ink")
        tr = D("always be treated", it); P("dr1-p3", tr, tr + 3.2, "High BP →", "should always be treated", enter="rise")
        cam = [(0, 1.0, "push", 7.5), (D("strongest", it), 1.1, "cut"), (D("coronary", it), 1.0, "cut"), (D("coronary", it) + 0.01, 1.05, "push", 15),
               (D("showed", it), 1.1, "cut"), (D("causation", it), 1.0, "cut"), (D("hypertension per", it), 1.12, "cut"), (D("properly", it), 1.0, "push", 3.8)]
    elif sid == "dr2":
        fall = D("fall down", it, 0)
        card = f'''<div id="dr2-card" class="card"><div class="in">
<div class="row" id="dr2-r1">Older people fall more easily</div>
<div class="row" id="dr2-r2">Orthostatic <span style="color:{C['red']}">HYPO</span>tension<small>BP drops when you stand up</small></div>
<svg width="720" height="330" style="display:block"><path id="dr2-line" d="M 0 80 L 300 80 C 360 80, 380 260, 460 270 L 720 270" fill="none" stroke="{C['red']}" stroke-width="6"/>
<circle cx="150" cy="40" r="22" fill="none" stroke="{C['navy']}" stroke-width="5"/><line x1="150" y1="62" x2="150" y2="150" stroke="{C['navy']}" stroke-width="5"/></svg></div></div>'''
        o = D("orthostatic", it); s2 = D("stand up", it)
        cjs = f'''tl.fromTo("#dr2-cam",{{x:0}},{{x:470,duration:0.7,ease:"power2.inOut"}},{D("elderly", it):.3f});
tl.fromTo("#dr2-card",{{xPercent:-100,rotationY:-35,transformPerspective:1400,transformOrigin:"100% 50%"}},{{xPercent:0,rotationY:0,duration:0.9,ease:"power3.inOut"}},{D("elderly", it):.3f});
tl.fromTo("#dr2-r1",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.5,ease:"power4.out"}},{D("prone", it):.3f});
tl.fromTo("#dr2-r2",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.5,ease:"power4.out"}},{o:.3f});
tl.fromTo("#dr2-line",{{strokeDasharray:900,strokeDashoffset:900}},{{strokeDashoffset:0,duration:1.6,ease:"power2.inOut"}},{s2:.3f});
tl.to("#dr2-cam",{{x:0,duration:0.6,ease:"power2.inOut"}},{fall + 0.6:.3f});
tl.to("#dr2-card",{{xPercent:-100,duration:0.6,ease:"power2.inOut"}},{fall + 0.6:.3f});'''
        over.append((card, cjs, 0))
        cam = [(0, 1.0, "cut"), (T1[0] - it["src_in"], 1.08, "cut")]
    elif sid == "dr3":
        a = D("initially", it); P("dr3-p1", a, a + 4.2, "OLD BELIEF", "treating BP in older people did more harm", enter="ink")
        b = D("but with", it); P("dr3-p2", b + 0.3, b + 4.6, "A major trial", "showed treatment helps", enter="mask")
        c = D("systolic", it); P("dr3-p3", c, c + 6.0, "Top number < 150", "systolic blood pressure", enter="rise")
        cam = [(0, 1.0, "push", 8), (b, 1.1, "cut"), (D("it came", it), 1.0, "cut"), (D("it came", it) + 0.01, 1.05, "push", 10), (c, 1.12, "cut"), (c + 6, 1.0, "cut")]
    elif sid == "dr4":
        a = D("140", it); P("dr4-p1", a, a + 5.0, "140/90 or more", "+ other conditions → treat", enter="rise")
        cam = [(0, 1.0, "push", 8), (a, 1.1, "cut"), (a + 5, 1.0, "cut")]
    elif sid == "dr5":
        rows = [("dr5-r0", D("diuretics", it), "Avoid sudden drops in BP", ""),
                ("dr5-r1", D("prostatic", it), "Prostate enlargement", "→ alpha blockers"),
                ("dr5-r2", D("coronary", it), "Coronary artery disease", "→ beta blockers"),
                ("dr5-r3", D("ckd", it), "Kidney disease / diabetes", "→ ACE inhibitors / ARBs")]
        card = '<div id="dr5-card" class="card"><div class="row" style="font-size:28px;letter-spacing:.3em;color:#D64545">MEDICINE FITS THE PERSON</div>' + "".join(
            f'<div class="row" id="{r}">{html.escape(a)}<small>{html.escape(b)}</small></div>' for r, _, a, b in rows) + "</div>"
        st = D("the choice", it)
        cjs = f'''tl.fromTo("#dr5-cam",{{x:0}},{{x:470,duration:0.7,ease:"power2.inOut"}},{st:.3f});
tl.fromTo("#dr5-card",{{xPercent:-100,rotationY:-35,transformPerspective:1400,transformOrigin:"100% 50%"}},{{xPercent:0,rotationY:0,duration:0.9,ease:"power3.inOut"}},{st:.3f});''' + "".join(
            f'\ntl.fromTo("#{r}",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.55,ease:"expo.out"}},{t0:.3f});' for r, t0, _, _ in rows)
        over.append((card, cjs, 0))
        cam = [(0, 1.0, "push", 6)]
    elif sid == "dr6":
        a = D("to cut", it)
        ticks = [("dr6-t0", D("proper antihypertensive", it), "✓ Treat it"), ("dr6-t1", D("dosage", it), "✓ Adjust the dose"),
                 ("dr6-t2", D("comorbidities", it), "✓ Look at other illnesses"), ("dr6-t3", D("geriatric", it), "✓ See a trained specialist")]
        m = '<div id="dr6-list" class="pop" style="top:220px;opacity:0"><div class="in"><div class="pop-sub" style="letter-spacing:.3em;color:#D64545;font-weight:700">BOTTOM LINE</div>' + "".join(
            f'<div class="pop-t" id="{i}" style="font-size:46px;margin-top:18px">{html.escape(x)}</div>' for i, _, x in ticks) + "</div></div>"
        j = gate("#dr6-list", a) + f'tl.fromTo("#dr6-list .in",{{clipPath:"inset(0% 100% 0% 0%)"}},{{clipPath:"inset(0% 0% 0% 0%)",duration:0.7,ease:"expo.out"}},{a:.3f});' + "".join(
            f'\ntl.fromTo("#{i}",{{opacity:0,filter:"blur(6px)"}},{{opacity:1,filter:"blur(0px)",duration:0.2,ease:"power4.out"}},{t0:.3f});' for i, t0, _ in ticks)
        over.append((m, j, a))
        cam = [(0, 1.0, "push", 10), (a, 1.08, "cut"), (D("geriatric", it) + 2, 1.0, "cut")]
    elif sid == "dr7":
        s = D("subscribed", it)
        m = f'<div id="dr7-sub" class="pop" style="top:auto;bottom:220px;width:auto"><div class="in" style="border:none;background:{C["red"]};color:#fff;border-radius:60px;padding:22px 48px;font-size:44px;font-weight:900">Subscribe</div></div>'
        over.append((m, gate("#dr7-sub", s) + ENTER["pop"]("#dr7-sub", s) + f'\ntl.to("#dr7-sub",{{opacity:0,duration:0.25}},{d0 - 2:.3f});', s))
        cam = [(0, 1.0, "push", 14)]
    # camera keyframes
    cj = []
    for c in cam:
        if c[2] == "cut": cj.append(f'tl.set("#{sid}-cam",{{scale:{c[1]}}},{c[0]:.3f});')
        else: cj.append(f'tl.fromTo("#{sid}-cam",{{scale:{c[1]}}},{{scale:{c[1] + 0.05:.2f},duration:{c[3]},ease:"none"{",immediateRender:false" if c[0] > 0 else ""}}},{c[0]:.3f});')
    # iris reveal of the doctor on entry
    entry = mask_in(f"#{sid}-wrap", *IRIS) + f'\ntl.fromTo("#{sid}-wrap",{{scale:1.12,filter:"blur(8px)"}},{{scale:1,filter:"blur(0px)",duration:1.0,ease:"power3.out"}},0);'
    body = f'<div id="{sid}-wrap" class="cam" data-layout-allow-overlap><div id="{sid}-cam" class="cam">{vids}</div>' + "\n".join(o[0] for o in over) + "</div>"
    js = entry + "\n" + "\n".join(cj) + "\n" + "\n".join(o[1] for o in over) + "\n" + (exit_js(f"#{sid}-wrap", it["exit_t"]) if "exit_t" in it else "")
    return f"""<template>
<style>{DR_CSS}</style>
<div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-layout-allow-overlap>
{body}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
tl.set({{}}, {{}}, {dur:.3f});
window.__timelines["{sid}"] = tl;
</script>
</template>"""

def end_scene(it):
    dur = it["end"] - it["start"]
    body = f'''<svg width="1920" height="1080" style="position:absolute;inset:0" data-layout-ignore><path id="end-ecg" d="{ecg_path(y=800, amp=0.6)}" fill="none" stroke="{C['red']}" stroke-width="4"/></svg>
<div id="end-b0" class="beat big" style="top:380px">{words_html("Decode Your Heart")}</div>
<div id="end-b1" class="beat mid serif" style="top:540px">{words_html("with Dr. Rehan")}</div>'''
    js = vo_in("end") + f'''\ntl.fromTo("#end-ecg",{{strokeDasharray:6000,strokeDashoffset:6000}},{{strokeDashoffset:0,duration:2.4,ease:"power2.inOut"}},0.1);
{ENTER['blur']('#end-b0', 0.6)}
{gate('#end-b0', 0.6)}{gate('#end-b1', 1.2)}{ENTER['ink']('#end-b1', 1.2)}'''
    return comp("end", "cc", body, js, dur)

# ---------- captions ----------
def caption_words():
    out = []
    for it in items:
        if it["kind"] == "vo":
            out += [dict(w=w["w"], s=it["audio"] + w["s"], e=it["audio"] + w["e"], sc=it["id"]) for w in vo_words(it["id"])]
        elif it["kind"] == "dr":
            for w in DRW:
                if not (it["src_in"] <= w["s"] < it["src_out"]) or w["e"] - w["s"] <= 0.01 or w["p"] < 0.3: continue
                if it["src_in"] < T1[0] < it["src_out"] and T1[0] <= w["s"] < T1[1]: continue
                l = dr_local(w["s"], it); out.append(dict(w=w["w"].strip(), s=it["start"] + l, e=it["start"] + l + (w["e"] - w["s"]), sc=it["id"]))
    fix = {"hypoepidemias": "hyperlipidemia,", "inter": "INTERHEART", "our": "beta"}
    res = []
    for i, w in enumerate(out):
        n = norm(w["w"])
        if n == "heart" and res and res[-1]["w"] == "INTERHEART": continue
        if n == "flexible" or n == "cardia": w = dict(w, w="…")
        if n in fix and (n != "our" or (i + 1 < len(out) and norm(out[i + 1]["w"]) == "blockers")): w = dict(w, w=fix[n])
        res.append(w)
    return res

def caption_groups(ws, maxw=5):
    groups, cur = [], []
    for w in ws:
        if cur and (len(cur) >= maxw or w["s"] - cur[-1]["e"] > 0.25 or cur[-1]["w"][-1:] in ".?!," or w["sc"] != cur[-1]["sc"]):
            groups.append(cur); cur = []
        cur.append(w)
    if cur: groups.append(cur)
    return groups

def captions_comp():
    gs = caption_groups(caption_words())
    mk, js = [], []
    for i, g in enumerate(gs):
        s, e = g[0]["s"] - 0.05, g[-1]["e"] + 0.15
        if i + 1 < len(gs): e = min(e, gs[i + 1][0]["s"] - 0.07)
        txt = " ".join(html.escape(w["w"]) for w in g)
        mk.append(f'<div id="cap-{i}" class="cap"><span>{txt}</span></div>')
        js.append(f'tl.fromTo("#cap-{i}",{{opacity:0}},{{opacity:1,duration:0.08}},{s:.3f});tl.set("#cap-{i}",{{opacity:0,visibility:"hidden"}},{e:.3f});')
    return f"""<template>
<style>#root{{position:absolute;inset:0;pointer-events:none}}
.cap{{position:absolute;left:0;right:0;bottom:84px;text-align:center;opacity:0;font-family:Inter,sans-serif}}
.cap span{{display:inline-block;background:rgba(20,33,61,.78);color:#fff;font-size:42px;font-weight:700;padding:10px 26px;border-radius:12px;letter-spacing:-0.005em}}</style>
<div id="root" data-composition-id="captions" data-width="1920" data-height="1080" data-layout-allow-caption-zone>
{chr(10).join(mk)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
tl.set({{}}, {{}}, {TOTAL:.3f});
window.__timelines["captions"] = tl;
</script>
</template>"""

# ---------- sound ----------
def sound():
    a, n = [], 0
    def add(src, t, vol, dur=None, media=0.0, fi=0, fo=0, tr=20):
        nonlocal n; n += 1
        extra = (f' data-duration="{dur:.3f}"' if dur else "") + (f' data-media-start="{media:.3f}"' if media else "") + \
                (f' data-fade-in="{fi}"' if fi else "") + (f' data-fade-out="{fo}"' if fo else "")
        a.append(f'<audio id="snd{n}" class="clip" src="{src}" data-start="{max(t, 0):.3f}" data-volume="{vol}" data-track-index="{tr}"{extra}></audio>')
    whooshes = ["assets/sfx/whoosh1.wav", "assets/sfx/whoosh3.mp3", "assets/sfx/whoosh2.wav"]
    for i, it in enumerate(items):
        if it["kind"] == "vo":
            a.append(f'<audio id="vo-{it["id"].lower()}" class="clip" src="assets/vo/{it["id"]}.wav" data-start="{it["audio"]:.3f}" data-duration="{VO_DUR[it["id"]]:.3f}" data-volume="1" data-track-index="{10 + i % 2}"></audio>')
            if i:  # whoosh2 is a long riser peaking at 8.35 s: start late so the peak lands mid-wipe
                w = whooshes[i % 3]
                add(w, it["start"] + 0.05, 0.35, dur=1.0 if "2" in w else 1.6, media=7.75 if "2" in w else 0.0, fo=0.4, tr=20 + i % 2)
        elif it["kind"] in ("dr", "end"): add("assets/sfx/whoosh1.wav", it["start"] + 0.05, 0.2, dur=1.4, fo=0.5, tr=22 + i % 2)
    h = items[0]; hw = vo_words("H01")
    add("assets/sfx/boom.wav", h["audio"] + find(hw, "but now"), 0.5, dur=3, fo=1, tr=25)
    for p_, v_ in (("72", 0.5), ("blood", 0.25), ("every", 0.3), ("should", 0.3), ("matters", 0.25), ("dangerous", 0.25)):
        add("assets/sfx/punch.wav" if p_ == "72" else "assets/sfx/whoosh3.mp3", h["audio"] + find(hw, p_) - 0.15, v_, dur=1.2, fo=0.4, tr=29)
    add("assets/sfx/boom.wav", h["audio"] + find(hw, "the room"), 0.35, dur=2.5, fo=1, tr=24)
    for i_ in range(11): add("assets/sfx/click2.mp3", 0.05 + i_ * (h["audio"] + find(hw, "72") - 0.15) / 12, 0.18, dur=0.15, tr=40 + i_ % 2)
    add("assets/sfx/punch.wav", h["audio"] + find(hw, "but now") - 0.05, 0.45, dur=1.3, fo=0.4, tr=27)  # VIP punch hole
    add("assets/sfx/glitch.wav", h["audio"] + find(hw, "the room") - 0.1, 0.18, dur=1.2, fi=0.2, fo=0.6, tr=28)  # VIP glitch, low: the room tilting
    add("assets/sfx/riser.wav", items[1]["start"] - 5.0, 0.3, dur=5.6, fi=1.5, fo=0.3, tr=26)
    # music bed (user's track, licence to confirm): drops out 1.5 s before O01's last line, back for the subscribe + end card
    o = next(x for x in items if x["id"] == "O01")
    cut = o["audio"] + find(vo_words("O01"), "and never") - 1.5
    t, m = items[1]["start"], 0.0
    while t < cut - 1:
        d = min(150.0 - m, cut - t)
        add("assets/music/bed.mp3", t, 0.12, dur=d, media=m, fi=2 if m == 0 else 0, fo=1.2 if t + d >= cut - 0.01 else 0, tr=30 + (t > 200))
        t += d; m = 0.0
    back = o["end"] + 0.5
    add("assets/music/bed.mp3", back, 0.12, dur=TOTAL - back, media=60.0, fi=1.5, fo=2.5, tr=32)
    return "\n".join(a)

# ---------- write ----------
os.makedirs(os.path.join(HF, "compositions"), exist_ok=True)
hosts = []
for z, it in enumerate(items, start=1):
    sid = it["id"].lower()
    if it["kind"] == "vo": src, _ = vo_scene(it)
    elif it["kind"] == "dr": src = dr_scene(it)
    else: src = end_scene(it)
    open(os.path.join(HF, "compositions", f"{sid}.html"), "w").write(src)
    dur = it["slot_end"] - it["start"]
    hosts.append(f'<div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{it["start"]:.3f}" '
                 f'data-duration="{dur:.3f}" data-track-index="{1 + z % 2}" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index:{z}"></div>')
open(os.path.join(HF, "compositions", "captions.html"), "w").write(captions_comp())
hosts.append(f'<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" '
             f'data-track-index="5" data-track-kind="captions" data-width="1920" data-height="1080" style="z-index:100"></div>')

index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #060B1C; }}
#root {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; }}
#ground {{ position: absolute; inset: 0; background: #060B1C; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080" data-fps="30">
<div id="ground"></div>
{chr(10).join(hosts)}
{sound()}
</div>
<script>
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = gsap.timeline({{ paused: true }});
</script>
</body>
</html>
"""
open(os.path.join(HF, "index.html"), "w").write(index)
json.dump([{k: (round(v, 3) if isinstance(v, float) else v) for k, v in it.items()} for it in items], open(os.path.join(HERE, "timeline.json"), "w"), indent=1)
for it in items:
    m, s = divmod(it["start"], 60)
    print(f'{it["id"]:4} {int(m)}:{s:05.2f}  dur {it["end"] - it["start"]:6.2f}')
print("TOTAL", TOTAL, f"= {int(TOTAL // 60)}:{TOTAL % 60:05.2f}")
