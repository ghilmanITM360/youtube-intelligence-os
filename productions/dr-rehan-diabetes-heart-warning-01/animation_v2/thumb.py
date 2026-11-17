"""Shorts thumbnails (1080x1920) from existing V2/V3 assets.  python3 thumb.py"""
import os
from PIL import Image, ImageDraw
from v3 import img, text_img, INK, RED, font

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "thumbnail")
W, H = 1080, 1920
SAFE_R = 900  # keep text/focal point clear of the right-side Shorts buttons and bottom 420 px of title UI


def put(c, im, x, y, s=1.0, anchor=(0.5, 1.0)):
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    c.paste(im, (int(x - anchor[0] * im.width), int(y - anchor[1] * im.height)), im)


def a():
    c = Image.new("RGB", (W, H), "white")
    put(c, img("patient_chest_worried"), 470, 1800, 1.35)
    for i, ic in enumerate(("icon_breath", "icon_tired", "icon_sweat", "icon_radiate")):
        put(c, img(ic), 830, 960 + 190 * i, 0.85, (0.5, 0.5))
    put(c, text_img([("DIABETES?", RED)], size=200), 470, 120, 1.0, (0.5, 0.0))
    put(c, text_img([("DON'T MISS THESE\n", INK), ("HEART SIGNS", INK)], size=110), 470, 350, 1.0, (0.5, 0.0))
    return c


def b():
    c = Image.new("RGB", (W, H), "white")
    put(c, img("heart_base"), 700, 1430, 0.95)
    put(c, img("heart_coronary"), 700, 1430, 0.95)
    put(c, img("heart_marker"), 700, 1430, 0.95)
    put(c, img("patient_chest_worried"), 300, 1800, 1.05)
    put(c, text_img([("HEART ATTACK\n", INK), ("WARNING SIGNS", RED)], size=128), 540, 120, 1.0, (0.5, 0.0))
    put(c, text_img([("with diabetes", INK)], size=90, heavy=False), 540, 430, 1.0, (0.5, 0.0))
    return c


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    ims = {"A": a(), "B": b()}
    for k, im in ims.items():
        assert im.size == (W, H)
        im.save(os.path.join(OUT, "Dr_Rehan_Heart_Warning_THUMBNAIL_%s.png" % k))
    # comparison: native (scaled to fit) + mobile grid size (~180 px wide)
    sh = Image.new("RGB", (1700, 1060), (238, 236, 232)); d = ImageDraw.Draw(sh)
    for i, (k, im) in enumerate(ims.items()):
        x = 40 + i * 840
        sh.paste(im.resize((540, 960), Image.LANCZOS), (x, 60))
        sh.paste(im.resize((180, 320), Image.LANCZOS), (x + 580, 60))
        sh.paste(im.resize((120, 213), Image.LANCZOS), (x + 580, 420))
        d.text((x, 14), "Candidate %s  (540 px | 180 px | 120 px)" % k, font=font(34, heavy=False, cond=False), fill=INK)
    sh.save(os.path.join(OUT, "THUMBNAIL_COMPARISON.png"))
    ims["A"].save(os.path.join(OUT, "Dr_Rehan_Heart_Warning_THUMBNAIL_FINAL.png"))  # selected: see V3_THUMBNAIL_QA.md
