import numpy as np, cv2, subprocess, json
rng=np.random.default_rng(7)
W,H,SH=1920,1080,137.5
PAD=300; SW=W+2*PAD
P=[0,0.0247,0.0601,0.1089,0.1714,0.2489,0.3377,0.4409,0.5518,0.6545,0.7455,0.8225,0.8834,0.9291,0.967,0.989,1.0]
def prog(f): return 0.0 if f<=19 else P[min(f-19,16)]
s=np.zeros((H,SW,3),np.uint8)
for y in range(H):  # sky gradient
    t=y/H; s[y]=(int(235-60*t),int(200-30*t),int(150+20*t))
def poly(pts,col):
    pts=np.array(pts,np.int32); cv2.fillPoly(s,[pts],col,cv2.LINE_AA); cv2.polylines(s,[pts],True,(30,30,40),3,cv2.LINE_AA)
for _ in range(25):  # clouds
    cx,cy=int(rng.integers(0,SW)),int(rng.integers(40,350))
    for _ in range(5):
        ex,ey=cx+int(rng.integers(-70,70)),cy+int(rng.integers(-20,20)); r=int(rng.integers(25,60))
        cv2.circle(s,(ex,ey),r,(250,250,255),-1,cv2.LINE_AA); cv2.circle(s,(ex,ey),r,(150,150,180),2,cv2.LINE_AA)
for L,(base,amp,col) in enumerate([(520,120,(150,120,110)),(680,100,(90,160,110)),(820,90,(60,140,70)),(960,70,(40,110,50))]):
    xs=np.arange(0,SW+40,40); ph=rng.uniform(0,6.28,3)
    ys=base+amp*(np.sin(xs/300+ph[0])*.5+np.sin(xs/137+ph[1])*.3+np.sin(xs/71+ph[2])*.2)
    poly([(0,H)]+list(zip(xs,ys.astype(int)))+[(SW+40,H)],col)
    for _ in range(18):  # trees & rocks on layer
        x=int(rng.integers(0,SW)); y=int(np.interp(x,xs,ys))+int(rng.integers(10,60)); sc=0.6+0.3*L
        if rng.random()<.6:
            cv2.rectangle(s,(x-5,y),(x+5,y+int(40*sc)),(60,40,30),-1)
            for k in range(3): poly([(x-int((45-k*10)*sc),y-int(k*35*sc)+10),(x+int((45-k*10)*sc),y-int(k*35*sc)+10),(x,y-int((k*35+50)*sc))],(30+k*20,100+k*25,50+k*10))
        else:
            r=int(rng.integers(15,40)); poly([(x-r,y+r//2),(x-r//2,y-r),(x+r//2,y-r*.8),(x+r,y+r//2)],tuple(int(c) for c in rng.integers(100,170,3)))
for _ in range(2500):  # fine grain texture
    x,y=int(rng.integers(0,SW)),int(rng.integers(0,H)); cv2.circle(s,(x,y),int(rng.integers(1,4)),tuple(int(c) for c in rng.integers(0,255,3)),-1,cv2.LINE_AA)
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30000/1001','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-r','30000/1001','rt.mp4'],stdin=subprocess.PIPE)
for f in range(60):
    # content moves right: camera window starts at right and slides left; start offset PAD+SH/2 -> PAD-SH/2
    tx=-PAD+SH*prog(f)-SH/2
    fr=cv2.warpAffine(s,np.float32([[1,0,tx],[0,1,0]]),(W,H),flags=cv2.INTER_LINEAR)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
json.dump({"PAN_start":20,"PAN_end":35,"total_shift_px":SH,"method":"Static seeded procedural 2520px-wide scene warped per frame with cv2.warpAffine bilinear using the measured cumulative progress table times 137.5 px, content moving +x."},open('timeline.json','w'),indent=1)
