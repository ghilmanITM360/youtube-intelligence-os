import cv2, numpy as np, os, subprocess, csv
W,H=1920,1080
TEAL=(138,138,31); INK=(40,40,40); CREAM=(240,245,247); WHITE=(255,255,255)
F=cv2.FONT_HERSHEY_SIMPLEX
D='/Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/reconstruction/RT3/'
def txt(im,s,x,y,sc,col,th=3,c=True,font=F):
    (w,h),_=cv2.getTextSize(s,font,sc,th)
    cv2.putText(im,s,(int(x-w/2) if c else int(x),int(y)),font,sc,col,th,cv2.LINE_AA)
def typed(s,f,f0,n=8):  # write-on type over n frames
    k=int(len(s)*min(1,max(0,(f-f0+1)/n)));return s[:k]
def shadow(im,pts,col=(110,110,110),a=.6):
    o=im.copy();cv2.fillPoly(o,[np.array(pts,np.int32)],col);cv2.addWeighted(o,a,im,1-a,0,im)
def pebble(im,x,y,s=1.0,mood='n',ink=INK,fill=(225,225,220)):
    cv2.ellipse(im,(x,y),(int(60*s),int(75*s)),0,0,360,fill,-1,cv2.LINE_AA)
    cv2.ellipse(im,(x,y),(int(60*s),int(75*s)),0,0,360,ink,3,cv2.LINE_AA)
    r=max(3,int(6*s));ey=y-int(20*s)
    for dx in(-18,18):
        ex=x+int(dx*s)
        if mood=='x':
            d=int(8*s);cv2.line(im,(ex-d,ey-d),(ex+d,ey+d),ink,3);cv2.line(im,(ex-d,ey+d),(ex+d,ey-d),ink,3)
        else: cv2.circle(im,(ex,ey),r,ink,-1,cv2.LINE_AA)
    if mood=='flat':cv2.line(im,(x-int(16*s),y+int(20*s)),(x+int(16*s),y+int(20*s)),ink,3)
def hatch(im,x0,y0,x1,y1,col,step=12):
    for i in range(x0-(y1-y0),x1,step):
        a=(max(i,x0),y0+max(0,x0-i));b=(min(i+(y1-y0),x1),y0+min(y1-y0,x1-i))
        cv2.line(im,a,b,col,1,cv2.LINE_AA)
def lamp(im,x,g,ink=INK,h=380):
    cv2.rectangle(im,(x-6,g-h),(x+6,g),ink,2);hatch(im,x-6,g-h,x+6,g,ink,6)
    cv2.fillPoly(im,[np.array([(x-40,g),(x-18,g-40),(x+18,g-40),(x+40,g)])],(200,200,195));cv2.polylines(im,[np.array([(x-40,g),(x-18,g-40),(x+18,g-40),(x+40,g)])],True,ink,2)
    for i in range(3):cv2.circle(im,(x-24+i*24,g-14),3,ink,-1)
    cv2.line(im,(x,g-h),(x+60,g-h-20),ink,4);cv2.rectangle(im,(x+40,g-h-26),(x+100,g-h-6),(200,200,195),-1);cv2.rectangle(im,(x+40,g-h-26),(x+100,g-h-6),ink,2)
    cv2.circle(im,(x+70,g-h+8),12,(120,230,255),-1);cv2.circle(im,(x+70,g-h+8),12,ink,2)
    for a in range(-60,61,30):
        t=np.radians(90+a);cv2.line(im,(x+70+int(20*np.cos(t)),g-h+8+int(20*np.sin(t))),(x+70+int(40*np.cos(t)),g-h+8+int(40*np.sin(t))),TEAL,3)
def stake(im,x,g,ink=INK,h=170):
    cv2.rectangle(im,(x-14,g-h),(x+14,g),(215,215,210),-1);cv2.rectangle(im,(x-14,g-h),(x+14,g),ink,2);hatch(im,x-14,g-h,x+14,g,ink,8)
    cv2.rectangle(im,(x-22,g-h-14),(x+22,g-h),TEAL,-1);cv2.rectangle(im,(x-22,g-h-14),(x+22,g-h),ink,2)
    cv2.rectangle(im,(x-40,g-10),(x+40,g),(190,190,185),-1);cv2.rectangle(im,(x-40,g-10),(x+40,g),ink,2)
    for k in range(1,6):cv2.line(im,(x-14,g-k*28),(x-4,g-k*28),ink,2)
def sun(im,x,y,r=60):
    cv2.circle(im,(x,y),r,(110,215,250),-1,cv2.LINE_AA);cv2.circle(im,(x,y),r,INK,3,cv2.LINE_AA)
    for a in range(0,360,30):
        t=np.radians(a);cv2.line(im,(x+int((r+12)*np.cos(t)),y+int((r+12)*np.sin(t))),(x+int((r+40)*np.cos(t)),y+int((r+40)*np.sin(t))),INK,3,cv2.LINE_AA)
def car(im,x,g,ink,body):
    cv2.fillPoly(im,[np.array([(x-150,g-30),(x-150,g-80),(x-80,g-90),(x-50,g-140),(x+60,g-140),(x+100,g-90),(x+150,g-80),(x+150,g-30)])],body)
    cv2.polylines(im,[np.array([(x-150,g-30),(x-150,g-80),(x-80,g-90),(x-50,g-140),(x+60,g-140),(x+100,g-90),(x+150,g-80),(x+150,g-30)])],True,ink,3,cv2.LINE_AA)
    cv2.rectangle(im,(x-40,g-130),(x+50,g-92),(180,160,120),-1);cv2.rectangle(im,(x-40,g-130),(x+50,g-92),ink,2);cv2.line(im,(x+5,g-130),(x+5,g-92),ink,2)
    for wx in(-85,85):
        cv2.circle(im,(x+wx,g-28),32,ink,-1);cv2.circle(im,(x+wx,g-28),18,(200,200,200),-1)
        for a in range(0,360,60):t=np.radians(a);cv2.line(im,(x+wx,g-28),(x+wx+int(18*np.cos(t)),g-28+int(18*np.sin(t))),ink,2)
    cv2.circle(im,(x+140,g-65),9,(120,230,255),-1)
def anchor(im,mk,ink=INK,bg=CREAM):
    cv2.rectangle(im,(160,40),(1760,130),bg,-1);cv2.rectangle(im,(160,40),(1760,130),ink,3)
    txt(im,'SUN CLOCK',270,100,1.1,ink,3)
    for i in range(7):
        x=480+i*210;cv2.line(im,(x,70),(x,100),ink,2);txt(im,str(i*2)+'H',x,125,.55,ink,1)
    cv2.line(im,(480,85),(1740,85),ink,3)
    x=int(480+mk*1260);cv2.fillPoly(im,[np.array([(x,95),(x-14,60),(x+14,60)])],TEAL)
def mk_at(f):
    if f<640:return .1
    if f<688:return .1
    if f<880:return .75
    return .95
GY=860
def c1(f,pop_p,pop_l):
    im=np.full((H,W,3),CREAM,np.uint8);cv2.line(im,(0,GY),(W,GY),INK,3)
    if f>=456:txt(im,typed('AT NOON',f,456),960,260,2.2,INK,5)
    if pop_p:
        shadow(im,[(520,GY),(330,GY+6),(120,GY+14),(330,GY+26),(520,GY+22)])
        pebble(im,600,GY-75,1.3)
    if pop_l:
        txt(im,'SHADOW STAYS',1200,520,1.8,TEAL,5);cv2.arrowedLine(im,(1000,540),(420,GY),TEAL,4,tipLength=.04)
    return im
def c1b(f,arrow):
    im=np.full((H,W,3),CREAM,np.uint8);cv2.line(im,(0,GY),(W,GY),INK,3)
    shadow(im,[(1000,GY),(800,GY+6),(560,GY+14),(800,GY+26),(1000,GY+22)])
    if arrow:
        sun(im,1550,330);stake(im,1400,GY)
        txt(im,'THE SUN WAS HERE',1350,470,1.2,TEAL,4);cv2.arrowedLine(im,(1450,500),(1520,400),TEAL,4)
    return im
def c2(f,night):
    ink=(235,235,225) if night else INK;bg=(70,55,40) if night else CREAM
    im=np.full((H,W,3),bg,np.uint8);cv2.line(im,(0,GY),(W,GY),ink,3)
    if night:
        for sx,sy in((300,250),(700,320),(1500,260),(1750,360),(1100,230)):cv2.circle(im,(sx,sy),4,(200,240,255),-1)
    if f>=640:
        for x in(450,950,1450):
            shadow(im,[(x+14,GY),(x-90,GY+4),(x-300,GY+12),(x-90,GY+22),(x+14,GY+20)],(90,90,90) if not night else (20,15,10),.7)
            stake(im,x,GY,ink)
    if f>=688:txt(im,'6 HOURS LATER' if f<832 or True else '',960,300,2.0,TEAL if not night else (200,210,80),5)
    if f>=736 and f<832:
        pebble(im,1700,GY-45,.6,'flat',ink);txt(im,'THIS IS FINE.',1700,GY-150,.9,ink,2)
    if f>=832:
        car(im,1000,GY-5,ink,(138,138,31));shadow(im,[(1150,GY),(900,GY+10),(520,GY+22),(900,GY+40),(1150,GY+30)],(15,10,5),.7)
    return im
def c3(f):
    im=np.full((H,W,3),CREAM,np.uint8)
    ox,oy,ex,ey=260,900,1700,280
    cv2.line(im,(ox,oy),(ex+60,oy),INK,4);cv2.line(im,(ox,oy),(ox,ey-60),INK,4)
    for i in range(1,8):
        x=ox+i*190;cv2.line(im,(x,oy),(x,oy-10),INK,2);cv2.line(im,(x,oy),(x,ey-40),(215,215,210),1)
    for j in range(1,6):
        y=oy-j*110;cv2.line(im,(ox,y),(ox+10,y),INK,2);cv2.line(im,(ox,y),(ex+60,y),(215,215,210),1)
    txt(im,'STEPS',980,oy+60,1.0,INK,2);txt(im,'SHADOWS',140,ey-80,.9,INK,2,False)
    pts=[]
    if f>=928:
        n=min(1,(f-928)/149)
        for i in range(int(n*140)+1):
            u=i/140;pts.append((int(ox+u*(ex-ox)),int(oy-(u**1.8)*(oy-ey))))
        cv2.polylines(im,[np.array(pts)],False,TEAL,6,cv2.LINE_AA)
        px,py=pts[-1];pebble(im,px,py-40,.5)
        for k in range(0,len(pts),14):
            x,y=pts[k];shadow(im,[(x,y+8),(x-30,y+14),(x-30,oy),(x,oy)],(150,150,150),.35)
    if f>=1078:txt(im,'ONE PER STEP',900,420,1.8,TEAL,5)
    if f>=1126:
        for k in range(6):shadow(im,[(1560+k*28,oy),(1500+k*28,oy-40),(1540+k*28,oy-190),(1600+k*28,oy-190)],(90,90,90),.4)
        pebble(im,1620,oy-95,.8,'flat')
    if f>=1176:txt(im,typed('SO WATCH YOUR STEP.',f,1176),960,1000,1.6,INK,4)
    return im
def lecture(f):
    im=np.full((H,W,3),CREAM,np.uint8)
    cv2.rectangle(im,(160,30),(1760,260),(235,235,230),-1);cv2.rectangle(im,(160,30),(1760,260),INK,4)
    txt(im,'WHAT IF YOUR SHADOW STAYED',960,110,1.8,INK,4);txt(im,'WHERE YOU LEFT IT?',960,190,1.8,INK,4)
    txt(im,'-A. READER',1650,245,.9,INK,2,False) if False else txt(im,'—A. READER'.replace('—','-'),1560,246,.8,INK,2)
    cv2.rectangle(im,(480,330),(1840,1000),INK,4);GL=900
    cv2.line(im,(480,GL),(1840,GL),INK,2)
    if f<156:pebble(im,250,800,1.3)
    if f>=48:lamp(im,1650,GL)
    if f>=96:
        shadow(im,[(1000,GL),(820,GL+4),(640,GL+12),(820,GL+22),(1000,GL+18)]);txt(im,'SHADOW',830,GL+70,.9,INK,2)
    if 156<=f<286:pebble(im,1250,GL-60,1.0)
    if f>=216:txt(im,'IT STAYED.',1150,500,2.2,TEAL,6)
    if f>=286:pebble(im,880,GL-40,1.0,'x');[cv2.line(im,(880+dx,GL-130),(880+dx*2,GL-170),TEAL,3) for dx in(-30,0,30)]
    return im
def card(f):
    im=np.full((H,W,3),TEAL,np.uint8)
    cv2.ellipse(im,(960,420),(150,190),0,0,360,(235,235,230),-1,cv2.LINE_AA)
    for dx in(-45,45):cv2.circle(im,(960+dx,380),12,INK,-1)
    txt(im,'?',960,500,3.2,TEAL,10)
    txt(im,'PEBBLE PONDERS',960,800,3.0,WHITE,8);return im
def endcard():
    im=np.full((H,W,3),TEAL,np.uint8);txt(im,'THANKS FOR PONDERING',960,300,3.0,WHITE,8)
    for i,x in enumerate((560,860,1160)):
        cv2.rectangle(im,(x,480),(x+200,860),(235,235,230),-1);cv2.rectangle(im,(x,480),(x+200,860),INK,4);cv2.rectangle(im,(x+20,520),(x+180,600),TEAL,-1)
        txt(im,'BOOK '+str(i+1),x+100,760,.9,INK,2)
    return im
def render(f):
    if f<360:return lecture(f)
    if f<408:return card(f)
    if f>=1200:return endcard()
    if f<640:
        mk=mk_at(f)
        if f<584:im=c1(f,f>=496,f>=544)
        elif f<592:
            t=(f-583)/8;a=c1(f,True,True);b=c1b(f,False)
            off=int(t*W);im=np.hstack([a,b])[:,off:off+W].copy();im=cv2.blur(im,(41,1))
        else:im=c1b(f,True)
        anchor(im,mk);return im
    if f<880:
        im=c2(f,False)
        if 784<=f<790:
            a=(f-783)/7;im=cv2.addWeighted(im,1-a,c2(f,True),a,0)
        elif f>=790:im=c2(f,True)
        night=f>=790;anchor(im,mk_at(f),(235,235,225) if night else INK,(70,55,40) if night else CREAM);return im
    im=c3(f);anchor(im,mk_at(f));return im
os.makedirs(D+'frames_tmp',exist_ok=True)
for f in range(1440):cv2.imwrite(D+'frames_tmp/f%04d.png'%f,render(f))
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','24','-i',D+'frames_tmp/f%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-r','24',D+'RT3_animatic.mp4'],check=True)
ev=[(0,47,'static','lecture frame: question card with attribution -A. READER + narrator + empty board'),
(48,95,'pop-on 1f','lamp post object pops on board'),
(96,155,'pop-on 1f','cold open: shadow blob + label SHADOW pops'),
(156,215,'state swap 1f','narrator moves onto board; shadow remains'),
(216,285,'pop-on 1f','gag text IT STAYED.'),
(286,359,'state swap 1f','narrator trips over shadow (x eyes)'),
(360,407,'hard cut','series card PEBBLE PONDERS (48f)'),
(408,455,'hard cut','canvas1 with persistent anchor SUN CLOCK'),
(456,495,'write-on type 8f','heading AT NOON'),
(496,543,'pop-on 1f','pebble and its shadow'),
(544,583,'pop-on 1f','label SHADOW STAYS + arrow'),
(584,591,'slide/pan with blur 8f','pan to far field, anchor fixed'),
(592,639,'pop-on 1f','sun and stake with label THE SUN WAS HERE'),
(640,687,'hard cut','canvas2: three stakes with parallel stuck shadows, anchor persists'),
(688,735,'pop-on 1f','label 6 HOURS LATER, anchor marker moves'),
(736,783,'deadpan aside pop 1f','small flat-mouth pebble: THIS IS FINE.'),
(784,831,'cross-dissolve 6f','day to night, shadows persist'),
(832,879,'pop-on 1f','car object and its stuck shadow at night'),
(880,927,'hard cut','canvas3 with axes SHADOWS vs STEPS, anchor persists'),
(928,1077,'continuous drawn growth 150f','curve grows with pebble riding the tip'),
(1078,1125,'pop-on 1f','label ONE PER STEP'),
(1126,1175,'state swap 1f','pile of shadows and flat-faced pebble'),
(1176,1199,'write-on type 8f','SO WATCH YOUR STEP.'),
(1200,1439,'full-frame end card hold 240f','THANKS FOR PONDERING + three book placeholders')]
with open(D+'RT1_intended_timeline.csv','w',newline='') as fh:
    w=csv.writer(fh);w.writerow(['start_frame','end_frame','device','description']);w.writerows(ev)
import shutil;shutil.rmtree(D+'frames_tmp')
print(len(ev))
