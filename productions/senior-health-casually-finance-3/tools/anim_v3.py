"""V3 motion correction on top of the V2 engine (anim_v2.py keeps rendering V2 unchanged; outputs go to animation/v3).
- Run characters: legs and both arms are redrawn every frame by rig.RunRig (two-leg gait, contralateral arms); the
  invisible root carries the gait's vertical oscillation; torso/head/face stay the original SVG parts.
- marks(): small ground marks that travel at exactly the stance-foot speed, so a planted foot never slides against
  the visible ground (tracking-shot reading when the character runs in place).
- swimmer(): rig.SwimRig arms/legs + water effects parented to the swimmer root.
- Red opening headline bar (same component in all three videos) replaces the first scene headline while it shows."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anim_v2 import Video, FPS, W, H, HEAD_Y, INK, CORAL, TEAL, ARIAL, ease, font
from PIL import Image, ImageDraw
import rig as R

RED, BLACK = (206, 32, 41), "/System/Library/Fonts/Supplemental/Arial Black.ttf"
BAR_X, BAR_PAD = 60, 26


def paste(canvas, im, x, y):
    """alpha_composite that tolerates negative / off-canvas offsets."""
    x0, y0 = max(0, -x), max(0, -y)
    if x0 >= im.width or y0 >= im.height or x >= W or y >= H:
        return
    canvas.alpha_composite(im.crop((x0, y0, min(im.width, W - x), min(im.height, H - y))), (x + x0, y + y0))


def fade(im, o):
    if o < 0.999:
        im = im.copy()
        im.putalpha(im.getchannel("A").point(lambda v: int(v * o)))
    return im


class Video3(Video):
    TAG, SUB = "V3", "v3"

    def __init__(self, *a, bar=None, **kw):
        super().__init__(*a, **kw)
        self.rigs, self.bar = {}, bar          # bar: dict(lines=[...], until=seconds)

    # ---------- building ----------
    def character(self, sc, asset, x, y, s, run=None, **kw):
        if not run:
            return super().character(sc, asset, x, y, s, **kw)
        per, rg = run[0], (run[2] if len(run) > 2 else R.RunRig())
        name = f"rig{len(self.rigs)}"
        self.rigs[name] = rg
        body = self.layer(sc, asset, x, y, s, name=f"{sc['id']}--{asset}--root", o=0.0, **kw)
        body["loop"] = ("rig", name, per)
        body["kids"] = []
        for lay in self.reg[asset]["layers"]:
            part = lay["id"].split("--", 1)[1]
            K = self.layer(sc, asset, 0, 0, s, part=part, at=body["at"], until=body["until"], parent=body,
                           speed=kw.get("speed"), z=body["z"], name=f"{sc['id']}--{asset}--{part}")
            if part in rg.parts:
                K["rig"] = (name, part)
            body["kids"].append(K)
        return body

    def swimmer(self, sc, asset, x, y, s, per, rg, z=5, **kw):
        name = f"rig{len(self.rigs)}"
        self.rigs[name] = rg
        root = self.layer(sc, asset, x, y, s, o=0.0, name="swimmer--root", **kw)
        root["loop"] = ("rig", name, per)
        order = ["rear-arm", "rear-leg", "body", "front-leg", "head", "front-arm"]   # far arm behind the body
        root["kids"] = []
        for part in order:
            K = self.layer(sc, asset, 0, 0, s, part=part, parent=root, until=root["until"], z=z,
                           name=f"swimmer--{part}")
            if part in rg.parts:
                K["rig"] = (name, part)
            root["kids"].append(K)
        fx = self.layer(sc, asset, 0, 0, s, part="fx", parent=root, until=root["until"], z=9, name="swimmer--water-fx")
        fx["rig"] = (name, "fx")
        root["kids"].append(fx)
        return root

    def marks(self, root, gy, z=1, gap=150):
        self.layers.append(dict(name=root["name"].replace("--root", "--ground-marks"), asset=None, part=None, x=0, y=gy,
                                s=1.0, at=root["at"], until=root["until"], enter="cut", exit="cut", moves=[], loop=None,
                                pivot=(0, 0), z=z, o=1.0, parent=None, speed=None, enter_dur=8, scene=root["scene"],
                                marks=dict(root=root["name"], gap=gap)))

    # ---------- evaluation ----------
    def phase(self, root, t):
        return self.ltime(root, t) / root["loop"][2]

    def state(self, L, t):
        lp = L.get("loop")
        if not (lp and lp[0] == "rig"):
            return super().state(L, t)
        x, y, s, r, o, wp, wd = super().state(dict(L, loop=None), t)
        rg = self.rigs[lp[1]]
        return x, y - rg.bounce(self.phase(L, t) % 1.0) * s, s, r, o, wp, wd

    def draw_layer(self, canvas, L, t, cam):
        if L.get("marks"):
            return self.draw_marks(canvas, L, t, cam)
        if not L.get("rig"):
            return super().draw_layer(canvas, L, t, cam)
        x, y, s, r, o, _, _ = self.state(L, t)
        if o <= 0.01:
            return
        k, cx, cy = cam
        x, y, s = cx + (x - cx) * k, cy + (y - cy) * k, s * k
        name, part = L["rig"]
        rg = self.rigs[name]
        im = R.image(rg, part, round(self.phase(L["parent"], t) % 1.0, 4), round(s, 3))
        paste(canvas, fade(im, o), round(x - rg.M * s), round(y - rg.M * s))

    def draw_marks(self, canvas, L, t, cam):
        root = next(R_ for R_ in self.layers if R_["name"] == L["marks"]["root"])
        rx, _, rs, _, ro, _, _ = Video.state(self, dict(root, loop=None, o=1.0), t)
        rg = self.rigs[root["loop"][1]]
        gap = L["marks"]["gap"]
        off = (rx - rg.ground_shift(self.phase(root, t)) * rs) % gap      # world x of the ground under the feet
        k, cx, cy = cam
        d = ImageDraw.Draw(canvas)
        for i in range(-1, int(W / k / gap) + 3):
            for dx, dy, ln in ((0, 22, 30), (70, 44, 18)):
                x0 = off + i * gap + dx
                X0, Y = cx + (x0 - cx) * k, cy + (L["y"] + dy - cy) * k
                d.line([(X0, Y), (X0 + ln * k, Y)], fill=(176, 170, 156), width=max(2, round(5 * k)))

    # ---------- headline bar ----------
    def bar_image(self):
        """White text layer of the red opening bar (block colour added in draw_bar)."""
        lines = self.bar["lines"]
        size = 92
        while size > 56:
            f = font(BLACK, size)
            if max(ImageDraw.Draw(Image.new("L", (1, 1))).textlength(l, font=f) for l in lines) <= W - 2 * BAR_X - 2 * BAR_PAD - 20:
                break
            size -= 2
        lh = round(size * 1.12)
        txt = Image.new("RGBA", (W - 2 * BAR_X, 2 * BAR_PAD + lh * len(lines)))
        d = ImageDraw.Draw(txt)
        for i, l in enumerate(lines):
            d.text((txt.width / 2, BAR_PAD + lh * i + lh / 2), l, font=f, fill=(255, 255, 255), anchor="mm")
        return txt

    def draw_bar(self, canvas, t):
        if not hasattr(self, "_bar"):
            self._bar = self.bar_image()
        txt = self._bar
        ui = ease(t / (6 / FPS))                                      # short entrance: settle down 14 px + fade in
        uo = ease((self.bar["until"] - t) / (8 / FPS))                # smooth exit: fade + lift
        im = Image.new("RGBA", txt.size, RED + (255,))
        im.alpha_composite(txt)
        paste(canvas, fade(im, min(ui * 0.45 + 0.55, uo)), BAR_X, HEAD_Y + 10 - round(14 * (1 - ui)) - round(18 * (1 - uo)))

    def frame(self, n):
        t = n / FPS
        sc = next((s for s in self.scenes if s["start"] <= t < s["end"]), self.scenes[-1])
        canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        cam = self.camera(t)
        for L in sorted(self.layers, key=lambda L: L["z"]):
            if L["at"] <= t < L["until"] and not L.get("kids"):
                self.draw_layer(canvas, L, t, cam)
        if self.bar and t < self.bar["until"]:
            self.draw_bar(canvas, t)
        elif self.bar and sc is self.scenes[0]:                       # first headline fades in after the bar
            tmp = Image.new("RGBA", (W, H))
            self.draw_headline(tmp, sc, t)
            canvas.alpha_composite(fade(tmp, ease((t - self.bar["until"]) / (6 / FPS))))
        else:
            self.draw_headline(canvas, sc, t)
        self.draw_caption(canvas, t)
        return canvas.convert("RGB")

    def timeline(self):
        super().timeline()
        import json
        p = os.path.join(self.anim, f"KEYFRAME_TIMELINE_{self.TAG}.json")
        doc = json.load(open(p))
        byname = {L["name"]: L for L in self.layers}
        for tr in doc["tracks"]:
            L = byname.get(tr["layer"], {})
            if L.get("rig"):
                rg = self.rigs[L["rig"][0]]
                tr["procedural_rig"] = dict(rig=type(rg).__name__, part=L["rig"][1], source="tools/rig.py",
                                            params={k: v for k, v in vars(rg).items() if isinstance(v, (int, float))})
            if L.get("marks"):
                tr["ground_marks"] = L["marks"]
        doc["opening_bar"] = self.bar and dict(self.bar, colour=list(RED), font="Arial Black", in_frame=0,
                                                out_frame_exclusive=round(self.bar["until"] * FPS))
        doc["rigs"] = {k: type(v).__name__ for k, v in self.rigs.items()}
        json.dump(doc, open(p, "w"), indent=1)
