import numpy as np, cv2, json, subprocess
W,H=1920,1080; BOX=(300,80,1500,820); PX=(560,1240); PY=(200,700)
BOARD=(0x3b,0x4f,0x3a); WALL=(0xc9,0xa4,0x6a)  # RGB
SQ0,CAM0,CAMN=30,100,16  # collapse start, first moving frame, moving frames
def board(swapped, ph=1.0):
    b=np.zeros((H,W,3),np.uint8); b[:]=BOARD
    # static decor (scene content, own shapes)
    cv2.circle(b,(420,200),60,(230,200,60),-1)
    cv2.rectangle(b,(1300,600),(1420,760),(200,80,80),-1)
    cv2.fillPoly(b,[np.array([(1300,300),(1420,300),(1360,200)])],(90,160,220))
    cv2.circle(b,(420,720),50,(240,240,240),-1)
    cy=(PY[0]+PY[1])/2; h=(PY[1]-PY[0])*ph; y0,y1=int(round(cy-h/2)),int(round(cy+h/2))
    p=np.zeros((PY[1]-PY[0],PX[1]-PX[0],3),np.uint8)
    if not swapped:
        p[:]=(240,230,200); cv2.circle(p,(340,250),150,(220,60,60),-1)
    else:
        p[:]=(40,60,150); cv2.fillPoly(p,[np.array([(100,420),(340,60),(580,420)])],(250,210,50))
    p=cv2.resize(p,(PX[1]-PX[0],y1-y0),interpolation=cv2.INTER_AREA) if ph<1 else p
    b[y0:y1,PX[0]:PX[1]]=p
    return b
# sq phase heights: f30,31 collapse; 32,33 band; 34,35 expand; 36+ full
BAND=0.22
def ph(f):
    k=f-SQ0
    return {0:1-(1-BAND)/3,1:1-2*(1-BAND)/3,2:BAND,3:BAND,4:1-2*(1-BAND)/3,5:1-(1-BAND)/3}.get(k,1.0)
def swapped(f): return f>=SQ0+2
def ease(t): return t*t*(3-2*t)
def frame(f):
    img=np.zeros((H,W,3),np.uint8); img[:]=WALL
    b=board(swapped(f), ph(f))
    k=min(max(f-(CAM0-1),0),CAMN)
    s=1+0.25*ease(k/CAMN)
    if s>1:
        c=((BOX[0]+BOX[2])/2,(BOX[1]+BOX[3])/2)
        M=cv2.getRotationMatrix2D(c,0,s); b=cv2.warpAffine(b,M,(W,H),flags=cv2.INTER_LINEAR,borderValue=BOARD)
    x0,y0,x1,y1=BOX; img[y0:y1,x0:x1]=b[y0:y1,x0:x1]
    return img
ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s","1920x1080","-r","30000/1001","-i","-",
 "-c:v","libx264","-crf","12","-pix_fmt","yuv420p","-r","30000/1001","rt.mp4"],stdin=subprocess.PIPE)
for f in range(180): ff.stdin.write(frame(f).tobytes())
ff.stdin.close(); ff.wait()
json.dump({"SQ_collapse_start":30,"SQ_band_frames":[32,33],"SQ_settled":36,"CAM_start":100,"CAM_end":115,
 "boxes":{"panel":[PX[0],PY[0],PX[1],PY[1]],"scene":list(BOX)}},open("timeline.json","w"))
