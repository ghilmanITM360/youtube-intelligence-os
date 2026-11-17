import cv2, numpy as np, subprocess, math, csv
W,H,N=1080,1920,1440
TEAL=(138,138,31); BG=(240,244,246); F=cv2.FONT_HERSHEY_SIMPLEX
EV=[]  # (frame,end,device,desc)
def ev(a,b,d,s): EV.append((a,b,d,s))
def prog(f,s,n=8): return min(1.0,(f-s+1)/n)
def text(img,s,x,y,sc,col,th,f,st):
    if f<st: return
    k=max(1,math.ceil(prog(f,st)*len(s))); cv2.putText(img,s[:k],(x,y),F,sc,col,th,cv2.LINE_AA)
def stroke(img,pts,col,th,f,st):
    if f<st: return
    p=prog(f,st); segs=[(pts[i],pts[i+1]) for i in range(len(pts)-1)]
    L=[math.dist(a,b) for a,b in segs]; tot=sum(L)*p
    for (a,b),l in zip(segs,L):
        if tot<=0: break
        t=min(1,tot/l); e=(int(a[0]+(b[0]-a[0])*t),int(a[1]+(b[1]-a[1])*t))
        cv2.line(img,a,e,col,th,cv2.LINE_AA); tot-=l
def pebble(img,cx,cy,ax,ay,ink,pose=0):
    cv2.ellipse(img,(cx,cy),(ax,ay),0,0,360,(168,170,175),-1,cv2.LINE_AA)
    cv2.ellipse(img,(cx,cy),(ax,ay),0,0,360,ink,4,cv2.LINE_AA)
    ex=int(ax*.35); ey=cy-int(ay*.2)
    r=int(ax*.07) if pose==0 else int(ax*.14)
    for s in(-1,1): cv2.circle(img,(cx+s*ex,ey),r,ink,-1,cv2.LINE_AA)
    if pose: cv2.ellipse(img,(cx,cy+int(ay*.3)),(int(ax*.15),int(ax*.12)),0,0,360,ink,3,cv2.LINE_AA)
def sun(img,c,ink):
    cv2.circle(img,c,48,(80,200,245),-1,cv2.LINE_AA); cv2.circle(img,c,48,ink,4,cv2.LINE_AA)
    for i in range(12):
        a=i*math.pi/6; cv2.line(img,(int(c[0]+62*math.cos(a)),int(c[1]+62*math.sin(a))),(int(c[0]+82*math.cos(a)),int(c[1]+82*math.sin(a))),ink,4,cv2.LINE_AA)
def render(f):
    im=np.full((H,W,3),BG,np.uint8); night=f>=1206
    ink=(235,235,235) if night else (40,40,40)
    # banner (anchor)
    cv2.rectangle(im,(60,130),(1020,240),TEAL,-1)
    cv2.putText(im,"SUN CLOCK",(90,208),F,1.8,(255,255,255),4,cv2.LINE_AA)
    t="NOON" if f<372 else "3 PM" if f<932 else "6 PM" if f<1206 else "MIDNIGHT"
    cv2.putText(im,t,(720 if len(t)<8 else 640,208),F,1.5,(255,255,255),4,cv2.LINE_AA)
    # top panel
    cv2.rectangle(im,(60,260),(1020,900),(60,45,35) if night else (252,248,240),-1)
    cv2.line(im,(60,785),(1020,785),ink,4)
    if 30<=f<1206: sun(im,(240,380) if f<372 else (640,420) if f<932 else (880,400),ink)
    if 126<=f: cv2.ellipse(im,(480,780),(130,12),0,0,360,(110,110,110),-1,cv2.LINE_AA)
    if 986<=f: cv2.ellipse(im,(700,780),(70,10),0,0,360,(110,110,110),-1,cv2.LINE_AA)
    if 78<=f: pebble(im,330 if f<372 else 900,700,70,85,ink)
    if 590<=f:
        cv2.rectangle(im,(180,600),(204,785),(60,100,140),-1)
        for y in(640,700,750): cv2.line(im,(184,y),(200,y+8),ink,2)
        for dx,dy,r in((0,520,70),(-45,570,55),(45,570,55),(0,600,50),(-60,520,40),(60,520,40)):
            cv2.circle(im,(192+dx,dy),r,(90,170,90),-1,cv2.LINE_AA)
        cv2.circle(im,(192,545),95,ink,3,cv2.LINE_AA)
        for dx,dy in((-30,510),(25,540),(-5,580),(40,500)): cv2.circle(im,(192+dx,dy),5,ink,-1)
    text(im,"YOUR SHADOW",430,640,1.6,ink,3,f,174)
    stroke(im,[(560,660),(560,752),(545,732),(560,752),(575,732)],TEAL,5,f,222)
    stroke(im,[(380+i*25,785 if i%2 else 765) for i in range(9)],TEAL,4,f,644)
    text(im,"LEFT BEHIND",80,850,1.5,TEAL,4,f,426)
    text(im,"SHADOW PILEUP",520,850,1.5,TEAL,4,f,1040)
    if 1262<=f:
        cv2.circle(im,(880,400),45,(190,235,245),-1,cv2.LINE_AA); cv2.circle(im,(862,388),8,(150,190,200),-1); cv2.circle(im,(895,415),6,(150,190,200),-1)
        for p in((700,330),(780,300),(600,430),(960,310)): cv2.drawMarker(im,p,(235,235,235),cv2.MARKER_STAR,22,2)
    text(im,"GOOD NIGHT",330,330,1.6,TEAL,4,f,1372)
    # bottom panel
    cv2.rectangle(im,(60,1000),(1020,1700),(252,248,240),-1)
    sa=bottomA(f); sb=bottomB(f)
    reg=(slice(1004,1696),slice(64,1016))
    if 700<=f<=707:
        t=(f-699)/8; sh=int(t*952)
        a=bottomA(699)[reg]; b=bottomB(708)[reg]; c=np.zeros_like(a)
        c[:,:952-sh]=a[:,sh:]; c[:,952-sh:]=b[:,:sh]; c=cv2.blur(c,(41,1)); im[reg]=c
    else: im[reg]=(sa if f<700 else sb)[reg]
    cv2.rectangle(im,(60,260),(1020,900),ink if night else (40,40,40),3)
    cv2.rectangle(im,(60,1000),(1020,1700),(40,40,40),3)
    return im
def panel():
    im=np.full((H,W,3),(252,248,240),np.uint8); return im
def bottomA(f):
    im=panel(); ink=(40,40,40); cv2.line(im,(64,1600),(1016,1600),ink,4)
    if f>=270: pebble(im,300,1450,130,150,ink,1 if f>=534 else 0)
    text(im,"IT STAYS PUT",500,1150,1.6,ink,3,f,318)
    if f>=480:
        cv2.rectangle(im,(540,1250),(960,1380),(255,255,255),-1); cv2.rectangle(im,(540,1250),(960,1380),ink,3)
        cv2.fillPoly(im,[np.array([(560,1380),(500,1440),(600,1380)])],(255,255,255)); cv2.line(im,(560,1380),(500,1440),ink,3); cv2.line(im,(500,1440),(600,1380),ink,3)
        cv2.putText(im,"WAIT, WHAT?",(570,1338),F,1.3,ink,3,cv2.LINE_AA)
    return im
def bottomB(f):
    im=panel(); ink=(40,40,40); cv2.line(im,(64,1600),(1016,1600),ink,4)
    if f>=770:
        pts=[(int(540-380*math.cos(a*math.pi/60)),int(1550-380*math.sin(a*math.pi/60))) for a in range(61)]
        cv2.polylines(im,[np.array(pts)],False,ink,5,cv2.LINE_AA)
    if f>=824:
        for a in(30,90,150): cv2.circle(im,(int(540-380*math.cos(a*math.pi/180)),int(1550-380*math.sin(a*math.pi/180))),24,TEAL,-1,cv2.LINE_AA)
    text(im,"SUNRISE",90,1660,1.2,ink,3,f,878)
    text(im,"SHADOW FOREST",270,1390,1.6,ink,3,f,1094)
    if f>=1150:
        for x in range(300,801,100): cv2.ellipse(im,(x,1572),(40,9),0,0,360,(110,110,110),-1,cv2.LINE_AA)
    stroke(im,[(270,1415),(680,1415)],TEAL,6,f,1316)
    return im
E=[(30,'pop','top: sun pops on'),(78,'pop','top: pebble narrator pops on'),(126,'pop','top: shadow pops on ground'),
(174,'write','top: YOUR SHADOW label write-on 8f'),(222,'stroke','top: teal arrow stroke 8f'),
(270,'pop','bottom: large pebble narrator pops on'),(318,'write','bottom: IT STAYS PUT write-on 8f'),
(372,'swap','top: pebble jumps away, sun moves, banner NOON->3 PM'),(426,'write','top: LEFT BEHIND write-on 8f'),
(480,'pop','bottom: WAIT, WHAT? speech bubble pops on'),(534,'swap','bottom: pebble pose swap to wide eyes'),
(590,'pop','top: detailed tree pops on'),(644,'stroke','top: teal hatch stroke over stuck shadow 8f'),
(700,'slide','bottom panel slides to sun-path scene with blur 8f'),(770,'pop','bottom: sun-path arc pops on'),
(824,'pop','bottom: three teal sun markers pop'),(878,'write','bottom: SUNRISE write-on 8f'),
(932,'swap','top: sun moves low right, banner 3 PM->6 PM'),(986,'pop','top: second stuck shadow pops'),
(1040,'write','top: SHADOW PILEUP write-on 8f'),(1094,'write','bottom: SHADOW FOREST write-on 8f'),
(1150,'pop','bottom: row of small shadows pops on'),(1206,'swap','top: night swap, sun off, banner MIDNIGHT'),
(1262,'pop','top: moon and stars pop on'),(1316,'stroke','bottom: teal underline stroke 8f'),(1372,'write','top: GOOD NIGHT write-on 8f')]
d={'pop':0,'swap':0,'write':7,'stroke':7,'slide':7}
if __name__=='__main__':
    with open('RT1_intended_timeline.csv','w',newline='') as fh:
        w=csv.writer(fh); w.writerow(['start_frame','end_frame','device','description'])
        for s,k,t in E: w.writerow([s,s+d[k],k,t])
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','24','-i','-','-frames:v',str(N),'-c:v','libx264','-pix_fmt','yuv420p','-r','24','-crf','14','RT4_animatic.mp4'],stdin=subprocess.PIPE)
    for f in range(N): p.stdin.write(render(f).tobytes())
    p.stdin.close(); p.wait()
    for f in (0,200,500,720,1000,1439): cv2.imwrite(f'chk_{f}.png',render(f))
