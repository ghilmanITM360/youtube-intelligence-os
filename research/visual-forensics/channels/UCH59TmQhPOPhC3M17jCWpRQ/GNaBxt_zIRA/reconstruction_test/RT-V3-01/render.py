import json, subprocess, numpy as np
from PIL import Image, ImageDraw
W,H,N=1920,1080,180
CX,CY,IW,IH=900,450,400,344
def hexc(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
def base():
    im=Image.new("RGB",(W,H),hexc("#c9a46a"))
    ImageDraw.Draw(im).rectangle([300,80,1499,819],fill=hexc("#3b4f3a"))  # box [300,80,1500,820)
    return im
def inset(d,hpx,col):
    if hpx<=0: return
    d.rectangle([CX-IW//2,CY-hpx//2,CX+IW//2-1,CY-hpx//2+hpx-1],fill=col)
    if hpx>100: d.ellipse([CX-90,CY-hpx*0.3,CX+90,CY+hpx*0.3],fill=(240,240,250))
OLD,NEW=(200,60,60),(60,110,200)
# frame -> (inset colour, height px)
def height(f):
    if f<30: return OLD,IH
    if f==30: return OLD,35       # collapse to line
    if f==31: return None,0       # gap
    scale={32:.77,33:1.055,34:1.05}.get(f,1.0) if f>=32 else 1
    return NEW,round(IH*scale)
p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r","30000/1001","-i","-",
 "-c:v","libx264","-crf","12","-pix_fmt","yuv420p","-r","30000/1001","rt.mp4"],stdin=subprocess.PIPE)
for f in range(N):
    im=base(); d=ImageDraw.Draw(im)
    c,h=height(f)
    if c: inset(d,h,c)
    if f>=100: d.polygon([(1280,780),(1380,600),(1180,600)],fill=(250,220,40))  # triangle, box [1180,600,1380,780]
    p.stdin.write(np.asarray(im).tobytes())
p.stdin.close(); p.wait()
json.dump({"POP_old_collapse_start":30,"POP_gap_frame":31,"POP_new_onset":32,"POP_peak_frames":[33,34],"POP_settle":35,
 "PIN_appear":100,"boxes":{"panel":[695,262,1105,638],"element":[1180,600,1380,780]}},open("timeline.json","w"),indent=1)
