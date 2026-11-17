import cv2, numpy as np, os, subprocess, shutil
D="/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT2"
FR=D+"/frames_tmp"; os.makedirs(FR,exist_ok=True)
W,H=1920,1080
BG=(247,247,247); INK=(50,45,40); TEAL=(138,138,31)  # BGR of #1F8A8A
F=cv2.FONT_HERSHEY_DUPLEX
def txt(im,s,x,y,sc,col=INK,th=3,clip=None):
    if clip is not None:
        (w,h),_=cv2.getTextSize(s,F,sc,th); tmp=im.copy()
        cv2.putText(tmp,s,(x,y),F,sc,col,th,cv2.LINE_AA)
        im[:, :int(x+w*clip)]=tmp[:, :int(x+w*clip)]
    else: cv2.putText(im,s,(x,y),F,sc,col,th,cv2.LINE_AA)
def pebble(im,cx,cy,r=60,col=(235,225,215),look=1):
    cv2.ellipse(im,(cx,cy),(r,int(r*0.85)),0,0,360,col,-1,cv2.LINE_AA)
    cv2.ellipse(im,(cx,cy),(r,int(r*0.85)),0,0,360,INK,3,cv2.LINE_AA)
    for dx in(-r//3,r//3): cv2.circle(im,(cx+dx+look*4,cy-r//6),6,INK,-1,cv2.LINE_AA)
def building(im,x,y,w,h,col=(225,222,218)):
    cv2.rectangle(im,(x,y),(x+w,y+h),col,-1); cv2.rectangle(im,(x,y),(x+w,y+h),INK,3)
    for yy in range(y+20,y+h-20,36):
        for xx in range(x+16,x+w-30,32):
            cv2.rectangle(im,(xx,yy),(xx+16,yy+20),(240,235,215),-1); cv2.rectangle(im,(xx,yy),(xx+16,yy+20),INK,1)
    for k in range(0,w,14): cv2.line(im,(x+k,y+h),(x+k+10,y+h-10),INK,1)  # base hatching
    cv2.line(im,(x+w//2,y),(x+w//2,y-30),INK,2); cv2.circle(im,(x+w//2,y-34),5,INK,-1)
def car(im,x,y,w,h,stuck=True):
    cv2.rectangle(im,(x,y-120),(x+w,y+h+40),(215,215,210),-1)  # shaft
    cv2.rectangle(im,(x,y-120),(x+w,y+h+40),INK,3)
    for k in range(y-120,y+h+40,18): cv2.line(im,(x,k),(x+8,k+8),INK,1)
    for dx in(w//2-20,w//2,w//2+20): cv2.line(im,(x+dx,y-120),(x+dx,y),INK,2)  # cables
    cv2.rectangle(im,(x+14,y),(x+w-14,y+h),(190,200,205),-1); cv2.rectangle(im,(x+14,y),(x+w-14,y+h),INK,3)
    mid=x+w//2; cv2.rectangle(im,(x+30,y+14),(mid-4,y+h-14),(215,225,230),-1)
    cv2.rectangle(im,(mid+4,y+14),(x+w-30,y+h-14),(215,225,230),-1)
    cv2.rectangle(im,(x+30,y+14),(x+w-30,y+h-14),INK,2); cv2.line(im,(mid,y+14),(mid,y+h-14),INK,2)
    for i in range(3):
        for j in range(2): cv2.circle(im,(x+w-22,y+30+i*16+j*0),4,INK,1)
    cv2.rectangle(im,(x+w//2-30,y+2),(x+w//2+30,y+12),TEAL,-1)  # display
    for k in range(6): cv2.line(im,(x+34,y+h-14-k*3),(mid-8,y+h-14-k*3),(150,160,165),1)
def banner(im,t,dark=False):
    c=(60,50,40) if dark else (255,255,255)
    cv2.rectangle(im,(0,0),(W,90),TEAL,-1)
    txt(im,"ELEVATORS STOPPED: ALL",40,62,1.6,(255,255,255),3)
    txt(im,"T+"+t,W-330,62,1.6,(255,255,255),3)
def stairs(im,x,y,n=14,sw=60,sh=34):
    for i in range(n):
        cv2.rectangle(im,(x+i*sw,y-i*sh),(x+(i+1)*sw,y-i*sh+sh*3),(205,205,200),-1)
        cv2.rectangle(im,(x+i*sw,y-i*sh),(x+(i+1)*sw,y-i*sh+sh*3),INK,2)
        for k in range(0,sh*3,12): cv2.line(im,(x+i*sw,y-i*sh+k),(x+i*sw+12,y-i*sh+k+12),INK,1)

def s_question(f):
    im=np.full((H,W,3),BG,np.uint8)
    cv2.rectangle(im,(260,330),(1660,750),TEAL,6)
    c=min(1,f/8)
    txt(im,"WHAT IF EVERY ELEVATOR",350,500,2.6,INK,4,clip=c)
    txt(im,"IN A CITY STOPPED AT ONCE?",350,640,2.6,TEAL,4,clip=c)
    return im
def s_city(f):  # f local 0..101
    im=np.full((H,W,3),BG,np.uint8)
    cv2.line(im,(0,950),(W,950),INK,4)
    for i,(x,h) in enumerate([(80,520),(330,720),(600,420),(860,640),(1130,780),(1400,500),(1650,600)]):
        building(im,x,950-h,200 if i%2 else 230,h)
    if f>=48: # inset cutaway of stuck car + narrator
        cv2.rectangle(im,(1000,160),(1860,880),BG,-1); cv2.rectangle(im,(1000,160),(1860,880),TEAL,6)
        car(im,1180,420,200,250); pebble(im,1285,560,38,look=0)
        txt(im,"CAR STUCK",1480,520,1.5,TEAL,3)
    banner(im,"00:00"); return im
def s_stairs(f,label=False):
    im=np.full((H,W,3),(239,240,227),np.uint8)
    stairs(im,200,880,22,70,34); 
    for i,(sx,sy) in enumerate([(300,860),(520,790),(760,700),(1000,620),(1240,520)]):
        pebble(im,sx,sy-80,26,look=1)
    cv2.rectangle(im,(1500,220),(1800,900),(215,215,210),-1); cv2.rectangle(im,(1500,220),(1800,900),INK,3)
    for k in range(220,900,20): cv2.line(im,(1500,k),(1510,k+10),INK,1)
    car(im,1560,520,180,210)
    if label:
        txt(im,"FLOOR 40",1000,400,1.8,TEAL,3); cv2.arrowedLine(im,(1180,420),(1400,490),TEAL,4,tipLength=0.15)
    banner(im,"00:30"); return im
def s_tower(aside):
    im=np.full((H,W,3),BG,np.uint8)
    building(im,760,160,400,820,(228,226,222))
    for yy in range(200,940,60): cv2.line(im,(760,yy),(1160,yy),INK,1)
    car(im,940,500,70,100)
    pebble(im,1500,780,70,look=-1)
    if aside:
        cv2.rectangle(im,(1220,500),(1860,660),(255,255,255),-1); cv2.rectangle(im,(1220,500),(1860,660),INK,3)
        txt(im,"WELL. THAT'S",1250,570,1.4,INK,3); txt(im,"A LOT OF STAIRS.",1250,630,1.4,TEAL,3)
    banner(im,"01:00"); return im
def s_night(lights,write):
    im=np.full((H,W,3),(43,35,20),np.uint8)
    for i,(x,h) in enumerate([(100,500),(380,720),(660,420),(940,640),(1220,780),(1500,540)]):
        cv2.rectangle(im,(x,950-h),(x+220,950),(70,58,40),-1); cv2.rectangle(im,(x,950-h),(x+220,950),(200,200,190),2)
        for yy in range(950-h+20,930,40):
            for xx in range(x+16,x+200,36):
                on=lights and ((xx+yy)//36)%3!=0
                cv2.rectangle(im,(xx,yy),(xx+18,yy+22),(150,230,240) if on else (55,48,32),-1)
    if write is not None:
        txt(im,"STAIRS: 1   ELEVATORS: 0",360,1040,2.2,(255,255,255),4,clip=write)
    banner(im,"24:00" if not lights else "12:00",True); return im

def frame(f):
    if f<48: return s_question(f)
    if f<150: return s_city(f-48)
    if f<252: return s_stairs(f,label=f>=204)
    if f<260: # slide w/ blur
        a=s_stairs(251,True); b=s_tower(False); k=(f-251)/9.0
        off=int(W*k); im=np.hstack([a,b])[:,off:off+W].copy()
        im=cv2.blur(im,(41,1)); banner(im,"00:30" if k<.5 else "01:00"); return im
    if f<360: return s_tower(f>=306)
    if f<490: return s_night(f<420,None)
    return s_night(False,min(1,(f-490)/8))
# banner redraw on slide is fine (rest of slide blurred only)

for f in range(576): cv2.imwrite(f"{FR}/f{f:04d}.png",frame(f))
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","24","-i",FR+"/f%04d.png","-c:v","libx264","-pix_fmt","yuv420p","-r","24",D+"/RT2_animatic.mp4"],check=True)
shutil.rmtree(FR)
rows=[(0,47,"write-on","QUESTION CARD: WHAT IF EVERY ELEVATOR IN A CITY STOPPED AT ONCE? (write-on f0-8)"),
(48,95,"hard cut + anchor pop","Cut to city canvas; persistent teal counter banner ELEVATORS STOPPED / T+ pops"),
(96,149,"pop","Cutaway inset of stuck elevator car (detailed shaft, cables, panels) + narrator + label CAR STUCK"),
(150,203,"hard cut","New tinted canvas: stairwell with climbing pebbles, elevator shaft; banner T+00:30"),
(204,251,"pop","Label FLOOR 40 + arrow pops"),
(252,305,"slide/pan with blur 8f","Slide to tower canvas (f252-259), banner T+01:00"),
(306,359,"deadpan narrator aside","Speech bubble WELL. THAT'S A LOT OF STAIRS."),
(360,419,"hard cut","Night city dark canvas, lit windows, banner T+12:00"),
(420,489,"state swap (1f)","Window lights switch off, banner T+24:00"),
(490,575,"write-on","Payoff text STAIRS: 1 ELEVATORS: 0 (write-on f490-498), hold to end")]
with open(D+"/RT1_intended_timeline.csv","w") as o:
    o.write("start_frame,end_frame,device,description\n")
    for r in rows: o.write(f'{r[0]},{r[1]},{r[2]},"{r[3]}"\n')
