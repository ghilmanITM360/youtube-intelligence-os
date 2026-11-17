import json, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
W,H,N=1920,1080,120
BG,INK=(252,252,252),(5,5,5)
FONT="/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf"
F1=ImageFont.truetype(FONT,110); F2=ImageFont.truetype(FONT,80)
T1,T2="Winter came early","Villages emptied by spring"
M1_START,M1_FRAMES=10,5            # reveal frames 10..14
M3_START=40; SCALES=[0.15,0.6,1.15,1.07,1.02,1.0]  # f40..f45, peak f42
SWAPS=[20,85]                      # closed->open at 20, open->closed at 85 (65-frame hold)
L1_POS=(700,330); L2_C=(1180,640)

def text_img(t,f):
    b=f.getbbox(t); im=Image.new("L",(b[2]+20,b[3]+20),0)
    ImageDraw.Draw(im).text((0,0),t,font=f,fill=255); return im
I1,I2=text_img(T1,F1),text_img(T2,F2)
def paste_ink(canvas,mask,xy):
    canvas.paste(Image.new("RGB",mask.size,INK),xy,mask)

CX,CY=320,560  # character head centre
MOUTH=(CX-45,CY+55,CX+45,CY+115)
def character(d,opened):
    d.ellipse((CX-150,CY-170,CX+150,CY+130),outline=INK,width=8)       # head
    d.line((CX,CY+130,CX,CY+330),fill=INK,width=8)                      # body
    d.line((CX,CY+200,CX-100,CY+290),fill=INK,width=8)
    d.line((CX,CY+200,CX+100,CY+290),fill=INK,width=8)
    d.line((CX,CY+330,CX-80,CY+430),fill=INK,width=8)
    d.line((CX,CY+330,CX+80,CY+430),fill=INK,width=8)
    for ex in (-55,55): d.ellipse((CX+ex-12,CY-50,CX+ex+12,CY-26),fill=INK)
    if opened: d.ellipse(MOUTH,fill=INK)
    else: d.line((CX-45,CY+85,CX+45,CY+85),fill=INK,width=8)

def frame(i):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    character(d,SWAPS[0]<=i<SWAPS[1])
    if i>=M1_START:
        k=min(i-M1_START+1,M1_FRAMES)/M1_FRAMES
        w=int(I1.width*k); paste_ink(im,I1.crop((0,0,w,I1.height)),L1_POS)
    if i>=M3_START:
        s=SCALES[min(i-M3_START,len(SCALES)-1)]
        m=I2.resize((max(1,int(I2.width*s)),max(1,int(I2.height*s))),Image.LANCZOS)
        paste_ink(im,m,(L2_C[0]-m.width//2,L2_C[1]-m.height//2))
    return np.asarray(im)

p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}",
 "-r","30000/1001","-i","-","-c:v","libx264","-pix_fmt","yuv420p","-crf","14","-r","30000/1001","rt01.mp4"],stdin=subprocess.PIPE)
for i in range(N): p.stdin.write(frame(i).tobytes())
p.stdin.close(); p.wait()

def nb(x0,y0,x1,y1,pad=12): return [round(max(0,x0-pad)/W,4),round(max(0,y0-pad)/H,4),round(min(W,x1+pad)/W,4),round(min(H,y1+pad)/H,4)]
big=SCALES[2]; w2,h2=I2.width*big,I2.height*big
json.dump({"fps":"30000/1001","frames":N,
 "M1_start":M1_START,"M1_end":M1_START+M1_FRAMES-1,
 "M3_start":M3_START,"M3_peak":M3_START+2,"M3_settle_end":M3_START+len(SCALES)-1,
 "M5_swaps":SWAPS,
 "boxes":{"line1":nb(L1_POS[0],L1_POS[1],L1_POS[0]+I1.width,L1_POS[1]+I1.height),
  "line2":nb(L2_C[0]-w2/2,L2_C[1]-h2/2,L2_C[0]+w2/2,L2_C[1]+h2/2),
  "mouth":nb(*MOUTH,pad=6),
  "character":nb(CX-150,CY-170,CX+150,CY+430)}},open("timeline.json","w"),indent=1)
