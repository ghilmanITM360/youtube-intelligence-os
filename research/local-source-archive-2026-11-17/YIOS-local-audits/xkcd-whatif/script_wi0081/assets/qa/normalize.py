"""Deterministic size/anchor step for tool output (owner-approved SIZE POLICY, extended).
Usage: python3 normalize.py NATIVE.png OUT.png [char|plain W H]
char : uniform scale so the mint head fill is as tall as the master's (338 px), then
       translate so the head centre is x=768 and the head fill top is y=150 on a 1536x1536
       RGBA canvas. Never stretches, never repaints. plain: uniform fit, centred."""
import sys, numpy as np
from PIL import Image
MINT_H, MINT_TOP, AXIS = 338, 150, 768   # measured on ALIEN_MASTER_001
def mint_bbox(im):
    a = np.array(im.convert('RGBA')).astype(int)
    m = (abs(a[...,0]-227)<14)&(abs(a[...,1]-252)<10)&(abs(a[...,2]-222)<14)&(a[...,3]>200)
    ys, xs = np.where(m); return xs.min(), ys.min(), xs.max(), ys.max()
def char(im, size=1536, height=None, axis=AXIS):
    x0,y0,x1,y1 = mint_bbox(im); s = MINT_H/(y1-y0)
    r = im.convert('RGBA').resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    out = Image.new('RGBA', (size,height or size), (0,0,0,0))
    out.alpha_composite(r, (round(axis-(x0+x1)/2*s), round(MINT_TOP-y0*s)))  # negative offsets crop, fine
    return out
def plain(im, w, h):
    s = min(w/im.width, h/im.height); r = im.resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    out = Image.new(im.mode, (w,h), (0,0,0,0) if im.mode=='RGBA' else (255,255,255))
    out.paste(r, ((w-r.width)//2, (h-r.height)//2)); return out
if __name__ == '__main__':
    src, dst, mode = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv)>3 else 'char')
    im = Image.open(src)
    if im.mode == 'RGBA':
        im = im.copy()
        alpha = im.getchannel('A').point(lambda value: 255 if value >= 253 else value)
        im.putalpha(alpha)
    (char(im, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])) if mode=='char' and len(sys.argv)>=7 else char(im) if mode=='char' else plain(im, int(sys.argv[4]), int(sys.argv[5]))).save(dst)
