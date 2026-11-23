#!/usr/bin/env python3
"""sheet.py <mp4> <out.jpg> <cols> <t1> <t2> ... : labelled contact sheet of native frames."""
import sys, subprocess, io
from PIL import Image, ImageDraw
mp4, out, cols = sys.argv[1], sys.argv[2], int(sys.argv[3]); ts = [float(x) for x in sys.argv[4:]]
W = 620; ims = []
for t in ts:
    b = subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',mp4,'-frames:v','1','-vf',f'scale={W}:-1','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
    im = Image.open(io.BytesIO(b)).convert('RGB'); d = ImageDraw.Draw(im); d.rectangle([0,0,110,20],fill=(0,0,0)); d.text((4,4),f't={t:.3f}',fill=(255,255,0)); ims.append(im)
h = ims[0].height; rows = (len(ims)+cols-1)//cols
S = Image.new('RGB',(cols*W,rows*h),'white')
for i,im in enumerate(ims): S.paste(im,((i%cols)*W,(i//cols)*h))
S.save(out, quality=85)
