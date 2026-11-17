#!/usr/bin/env python3
"""Original 12 s pilot: bowling ball on a trampoline. PIL frames (2x supersample) piped to ffmpeg. Same grammar as proof renderer:
canvas #F8F8F8, ink stroke 8px@1080p, 1-frame pop-ons, locked camera, hard poses. usage: render_pilot.py out.mp4 [keyframes.png]"""
import sys,math,json,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1]; FPS=24; N=288; W,H=1920,1080; SS=2
U=W*SS/1000.0           # design units -> px (1000 x 562.5)
INK,RED,BG,TEAL,BALL='#1E1E1E','#D7263D','#F8F8F8','#2A7F8E','#4A4F5C'
SW=int(8*SS)
FONT='/System/Library/Fonts/Supplemental/ChalkboardSE.ttc'
fnt=lambda s:ImageFont.truetype(FONT,int(s*U))
Q='Q: What if you drop a bowling ball on a trampoline?'
GROUND=500; MAT=380; XL,XR=410,810; BX=490; R=36; CX=360
# ---- physics (stylised time, real structure: free fall -> spring contact -> restitution e)
H0=MAT-(204); TF=1.1; g=2*H0/TF**2; v0=g*TF; E=0.65; T=0.6; T_REL=3.5
sched=[]; t=T_REL+TF; v=v0
while v>30 and t<12:
    sched.append(dict(t_in=t,v_in=v,d=v*T/math.pi)); t+=T; v*=E; t+=2*v/g
def ball_state(t):
    """returns (ball bottom y, mat depression D, phase)"""
    if t<T_REL: return 204,0,'hold'
    if t<sched[0]['t_in']: dt=t-T_REL; return 204+0.5*g*dt*dt,0,'fall'
    prev_leave=None
    for i,c in enumerate(sched):
        if c['t_in']<=t<c['t_in']+T:
            D=c['d']*math.sin(math.pi*(t-c['t_in'])/T); return MAT+D,D,'contact'
        leave=c['t_in']+T; vout=c['v_in']*E; nxt=sched[i+1]['t_in'] if i+1<len(sched) else 1e9
        if leave<=t<nxt:
            dt=t-leave; y=MAT-(vout*dt-0.5*g*dt*dt)
            rip=c['d']*0.18*math.exp(-dt/0.18)*math.cos(2*math.pi*2.5*dt)
            return min(y,MAT+0)+0,rip,'air'
    c=sched[-1]; dt=t-(c['t_in']+T); sag=8   # settle on mat
    return MAT+sag,sag*(1+0.4*math.exp(-dt/0.2)*math.cos(2*math.pi*3*dt)),'rest'
apex=[(c['t_in']+T+c['v_in']*E/g, (c['v_in']*E)**2/(2*g)) for c in sched if (c['v_in']*E)**2/(2*g)>=5]  # v2: ticks <5 units merged into one line, dropped
ev={'question':3,'tramp':12,'char':18,'ball':24,'start_tick':54,'label_final':222}
rel_f=int(T_REL*FPS); 
def pose(f,t):
    if f<rel_f: return 'P1_HOLD'
    if f<rel_f+8: return 'P2_RELEASE'
    if f<int(10.4*FPS): return 'P3_WATCH'
    return 'P4_SHRUG'
def P(x,y): return (x*U,y*U)
def line(d,pts,col=INK,w=SW):
    pp=[P(*p) for p in pts]; d.line(pp,fill=col,width=w,joint='curve')
    for q in (pp[0],pp[-1]): d.ellipse([q[0]-w/2,q[1]-w/2,q[0]+w/2,q[1]+w/2],fill=col)
def circ(d,x,y,r,fill=None,out=INK,w=SW):
    d.ellipse([*P(x-r,y-r),*P(x+r,y+r)],fill=fill,outline=out,width=w)
def char(d,p):
    hx,hy=CX,234; neck=270; hip=390
    circ(d,hx,hy,36,fill=BG)
    d.pieslice([*P(hx-40,hy-44),*P(hx+40,hy+8)],180,360,fill=TEAL,outline=INK,width=SW//2)  # beanie
    circ(d,hx+6,hy-46,9,fill=TEAL,w=SW//2)                                                    # pom-pom
    line(d,[(hx,neck),(CX,hip)]); line(d,[(CX,hip),(CX-30,GROUND)]); line(d,[(CX,hip),(CX+30,GROUND)])
    line(d,[(CX-30,GROUND),(CX-48,GROUND)]); line(d,[(CX+30,GROUND),(CX+48,GROUND)])
    sh=(CX,285)
    if p=='P1_HOLD': line(d,[sh,(425,240),(490,212)]); line(d,[sh,(325,330),(335,372)])
    elif p=='P2_RELEASE': line(d,[sh,(425,300),(455,345)]); line(d,[sh,(325,330),(335,372)])
    elif p=='P3_WATCH': line(d,[sh,(405,320),(372,262)]); line(d,[sh,(325,330),(335,372)])
    else: line(d,[sh,(310,335),(285,298)]); line(d,[sh,(410,335),(435,298)])
def tramp(d,D):
    for x in (XL,XR): line(d,[(x,MAT),(x,GROUND)]); line(d,[(x-14,GROUND),(x+14,GROUND)]); d.rectangle([*P(x-10,MAT-8),*P(x+10,MAT+4)],fill=INK)
    pts=[]
    for x in np.linspace(XL,XR,60):
        s=(x-XL)/(BX-XL) if x<=BX else (XR-x)/(XR-BX)
        pts.append((x,MAT+D*math.sin(math.pi/2*s)))
    line(d,pts)
def ball(d,y_bottom):
    cy=y_bottom-R; circ(d,BX,cy,R,fill=BALL)
    for dx,dy in ((-10,-14),(6,-18),(-2,-4)): d.ellipse([*P(BX+dx-4,cy+dy-4),*P(BX+dx+4,cy+dy+4)],fill=INK)
def frame(f):
    t=f/FPS; im=Image.new('RGB',(W*SS,H*SS),BG); d=ImageDraw.Draw(im)
    line(d,[(0,GROUND),(1000,GROUND)])
    if f>=ev['question']: d.text(P(30,22),Q,font=fnt(30),fill=INK)
    yb,D,ph=ball_state(t)
    if f>=ev['tramp']: tramp(d,D)
    if f>=ev['char']: char(d,pose(f,t))
    if f>=ev['ball']: ball(d,yb)
    if f>=ev['start_tick']:
        for x in range(835,876,16): line(d,[(x,204),(x+8,204)],INK,SW//2)
        d.text(P(884,188),'START',font=fnt(20),fill=INK)
    if ph=='fall' and (f//3)%2==0: line(d,[(BX-14,yb-R*2-22),(BX-14,yb-R*2-8)],INK,SW//2); line(d,[(BX+14,yb-R*2-22),(BX+14,yb-R*2-8)],INK,SW//2)
    for i,(ta,h) in enumerate(apex):
        if f>=int(round(ta*FPS)): line(d,[(835,MAT-h),(875,MAT-h)],RED); d.text(P(884+14*max(0,i-1),MAT-h-13),str(i+1),font=fnt(20),fill=RED)
    if f>=ev['label_final']: d.text(P(560,100),'LESS EACH TIME',font=fnt(44),fill=INK)
    return im.resize((W,H),Image.LANCZOS)
if __name__=='__main__':
    ff=subprocess.Popen(['ffmpeg','-nostdin','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-r',str(FPS),'-movflags','+faststart','-an',OUT],stdin=subprocess.PIPE)
    keys=[0,12,20,30,60,90,100,110,115,125,144,170,200,230,260,287]; ks=[]
    for f in range(N):
        im=frame(f); ff.stdin.write(im.tobytes())
        if f in keys: ks.append(im.resize((640,360)))
    ff.stdin.close(); ff.wait()
    if len(sys.argv)>2:
        sh=Image.new('RGB',(640*4,360*4),'white')
        for i,k in enumerate(ks): sh.paste(k,((i%4)*640,(i//4)*360))
        sh.save(sys.argv[2])
    json.dump(dict(fps=FPS,frames=N,release_s=T_REL,contacts=sched,apex_s_height=apex,g=g,e=E,contact_T=T),open(OUT.rsplit('.',1)[0]+'_physics.json','w'),indent=1)
    print('apex',[(round(a,2),round(h)) for a,h in apex]); print('contacts',[(round(c['t_in'],2),round(c['d'])) for c in sched])
