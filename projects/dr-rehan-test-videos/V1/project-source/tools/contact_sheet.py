# Labelled contact sheet from frames extracted out of the FINAL mp4 (out/frames/f_<sec>.png).
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont

files = sorted(glob.glob(os.path.join(sys.argv[1], "f_*.png")), key=lambda p: float(os.path.basename(p)[2:-4]))
cols, tw, th, pad, lab = 8, 216, 384, 6, 30
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + lab + pad) + pad + 50), "white")
d = ImageDraw.Draw(sheet)
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
d.text((pad, 12), "Calf_Pain_PAD_FINAL.mp4 - frames sampled from the rendered file (time in s)", fill="black", font=font)
for i, f in enumerate(files):
    r, c = divmod(i, cols)
    x, y = pad + c * (tw + pad), 50 + pad + r * (th + lab + pad)
    sheet.paste(Image.open(f).convert("RGB").resize((tw, th), Image.LANCZOS), (x, y + lab))
    d.rectangle([x, y + lab, x + tw - 1, y + lab + th - 1], outline="#888")
    d.text((x + 4, y + 3), os.path.basename(f)[2:-4] + " s", fill="#C0262D", font=font)
sheet.save(sys.argv[2])
print(sheet.size)
