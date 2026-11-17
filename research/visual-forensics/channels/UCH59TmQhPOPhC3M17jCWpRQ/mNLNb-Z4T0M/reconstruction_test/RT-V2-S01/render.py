import numpy as np, cv2, json, subprocess
W,H,N=1920,1080,208
rng=np.random.RandomState(7)
INK=(24,24,24)
def bgr(h): return (int(h[5:7],16),int(h[3:5],16),int(h[1:3],16))
SKY,GRASS,WATER,WATER2=bgr('#d0f8f8'),bgr('#789838'),bgr('#68c8d8'),bgr('#68b8d8')
def jit(pts,a=2.5,closed=True,sub=14):
    out=[];P=list(pts)+([pts[0]] if closed else [])
    for p,q in zip(P[:-1],P[1:]):
        n=max(1,int(np.hypot(q[0]-p[0],q[1]-p[1])//sub))
        for i in range(n):
            t=i/n; out.append((p[0]+(q[0]-p[0])*t+rng.uniform(-a,a),p[1]+(q[1]-p[1])*t+rng.uniform(-a,a)))
    return out
def outline(img,pts,closed=True,a=2.5,th=(4,7)):
    p=jit(pts,a,closed)
    if closed: p.append(p[0])
    for u,v in zip(p[:-1],p[1:]):
        cv2.line(img,(int(u[0]),int(u[1])),(int(v[0]),int(v[1])),INK,int(rng.randint(th[0],th[1]+1)),cv2.LINE_AA)
def shape(img,pts,fill,closed=True,a=2.5,th=(4,7)):
    j=jit(pts,a,closed); cv2.fillPoly(img,[np.array(j,np.int32)],fill,cv2.LINE_AA)
    outline(img,pts,closed,a,th)
def curve(xs,ys,n=60):
    return np.interp(np.linspace(0,len(xs)-1,n),range(len(xs)),xs),np.interp(np.linspace(0,len(xs)-1,n),range(len(xs)),ys)
def smooth(c,k=0):
    return c
HOR=210
def background():
    img=np.full((H,W,3),SKY,np.uint8)
    img[HOR-60:]=GRASS
    # hills
    xs=np.arange(0,W+1,20)
    for cx,w,top in((250,700,70),(1660,640,95)):
        pts=[(x,HOR-60+ (1-((x-cx)/w*2)**2)*(-0) ) for x in xs]
        hill=[(x,HOR-top*max(0,1-((x-cx)/w)**2)+20) for x in xs if abs(x-cx)<w]
        hill=[(hill[0][0],HOR+30)]+hill+[(hill[-1][0],HOR+30)]
        shape(img,hill,(70,150,110),True,3)
    # ground band between hills: horizon line
    cv2.rectangle(img,(0,HOR+30),(W,H),GRASS,-1)
    # river polygon winding
    ys=np.linspace(HOR+30,H,30)
    cxs=960+120*np.sin(ys/130)*(ys-HOR)/870+ (ys-HOR)*0.0
    half=70+(ys-HOR)*1.08
    L=[(c-h,y) for c,h,y in zip(cxs,half,ys)]
    R=[(c+h,y) for c,h,y in zip(cxs,half,ys)]
    poly=np.array(L+R[::-1],np.int32)
    cv2.fillPoly(img,[poly],WATER,cv2.LINE_AA)
    m=np.zeros((H,W),np.uint8); cv2.fillPoly(m,[poly],1)
    # two-tone water bands
    for y in range(HOR+60,H,90):
        img[y:y+35][m[y:y+35]>0]=WATER2
    for side in (L,R[::-1][::-1]):
        outline(img,[(min(max(x,0),W),y) for x,y in side],False,3,(4,7))
    # banks hatch texture
    for _ in range(260):
        x=rng.randint(0,W);y=rng.randint(HOR+40,H-5)
        if m[y,x]==0: cv2.line(img,(x,y),(x+rng.randint(-6,6),y-14),(60,110,50),2,cv2.LINE_AA)
    # ripple marks in water (static)
    for _ in range(40):
        x=rng.randint(0,W);y=rng.randint(HOR+80,H-5)
        if m[y,x]: cv2.ellipse(img,(x,y),(18,5),0,200,340,(190,230,235),3,cv2.LINE_AA)
    # village on horizon
    for i,(x,w,h) in enumerate([(1120,34,18),(1165,28,16),(1205,38,20),(1250,30,15),(1290,34,18)]):
        y=HOR+22
        shape(img,[(x,y),(x+w,y),(x+w,y-h*0.6),(x,y-h*0.6)],(210,230,240),True,1,(2,3))
        shape(img,[(x-4,y-h*0.6),(x+w/2,y-h),(x+w+4,y-h*0.6)],(60,70,170),True,1,(2,3))
    # trees
    def tree(x,y,s):
        shape(img,[(x-12*s,y),(x+12*s,y),(x+8*s,y-90*s),(x-8*s,y-90*s)],(50,90,130),True,2)
        for dx,dy,r in((0,-130,52),(-38,-100,38),(40,-104,40)):
            c=[(x+dx*s+r*s*np.cos(t),y+dy*s+r*s*np.sin(t)) for t in np.linspace(0,6.28,14,endpoint=False)]
            shape(img,c,(60,120,60),True,5)
    tree(190,640,1.5); tree(1730,520,1.2); tree(110,870,1.9)
    return img,m
bg,wm=background()
# shimmer
srng=np.random.RandomState(3)
shim=[(int(srng.randint(700,1250)),int(srng.randint(560,760)))for _ in range(8)]
def shimmer(img,f):
    if f>40: return
    for i,(x,y) in enumerate(shim):
        if (f//4+i)%3==0 and wm[y,x]: cv2.line(img,(x,y),(x+14,y),(230,250,250),3,cv2.LINE_AA)
def text_sprite(word,scale=2.6):
    (tw,th),_=cv2.getTextSize(word,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,scale,5)
    return tw,th
def make_group(word,item):
    S=np.zeros((300,560,4),np.uint8)
    col=np.zeros((300,560,3),np.uint8); al=np.zeros((300,560),np.uint8)
    tw,th=text_sprite(word)
    org=(20,110)
    cv2.putText(al,word,org,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2.6,255,14,cv2.LINE_AA)  # outline mask
    ol=al.copy()
    wh=np.zeros_like(al); cv2.putText(wh,word,org,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2.6,255,6,cv2.LINE_AA)
    col[ol>0]=INK; col[wh>0]=(255,255,255)
    a=np.maximum(ol,wh)
    # dotted arrow from under word to item
    ax,ay=60,150; ix,iy=300,250
    for t in np.linspace(0,1,9)[:-1]:
        x=ax+(ix-ax)*t+ 30*np.sin(t*3); y=ay+(iy-ay)*t
        cv2.circle(col,(int(x),int(y)),5,(255,255,255),-1,cv2.LINE_AA); cv2.circle(a,(int(x),int(y)),6,255,-1)
    pts=[(ix-26,iy-42),(ix,iy-42),(ix-12,iy-18)]
    cv2.fillPoly(col,[np.array([(ix-30,iy-40),(ix-4,iy-48),(ix-8,iy-22)],np.int32)],(255,255,255)); cv2.fillPoly(a,[np.array([(ix-30,iy-40),(ix-4,iy-48),(ix-8,iy-22)],np.int32)],255)
    # item at (ix,iy)+offset
    ic=np.zeros_like(col); ia=np.zeros_like(a)
    cx,cy=ix+10,iy+10
    if item=='dot':
        for dx,dy in((0,0),(14,-6),(-10,8),(8,12)):
            cv2.circle(ic,(cx+dx,cy+dy),5,INK,-1,cv2.LINE_AA); cv2.circle(ia,(cx+dx,cy+dy),6,255,-1)
    elif item=='mud':
        e=[(cx+34*np.cos(t)*(1+.2*np.sin(3*t)),cy+20*np.sin(t)) for t in np.linspace(0,6.28,12,endpoint=False)]
        p=np.array(e,np.int32); cv2.fillPoly(ic,[p],(40,70,110),cv2.LINE_AA); cv2.polylines(ic,[p],True,INK,5,cv2.LINE_AA); cv2.fillPoly(ia,[p],255); cv2.polylines(ia,[p],True,255,5)
    else:
        body=np.array([(cx-44,cy),(cx-20,cy-20),(cx+20,cy-18),(cx+44,cy-4),(cx+60,cy-22),(cx+60,cy+22),(cx+44,cy+4),(cx+20,cy+18),(cx-20,cy+20)],np.int32)
        cv2.fillPoly(ic,[body],(150,150,150),cv2.LINE_AA); cv2.polylines(ic,[body],True,INK,5,cv2.LINE_AA); cv2.fillPoly(ia,[body],255); cv2.polylines(ia,[body],True,255,5)
        cv2.line(ic,(cx-32,cy-6),(cx-24,cy+2),INK,3); cv2.line(ic,(cx-32,cy+2),(cx-24,cy-6),INK,3)
    m=ia>0; col[m]=ic[m]; a[m]=255
    return np.dstack([col,a]),(ix+10,iy+10)
GROUPS=[('bugs','dot',55,(800,490),1.0,(960,345)),('mud','mud',85,(740,690),1.35,(930,295)),('rotten fish','fish',115,(640,890),1.7,(900,250))]
# fix: third label wider
def make_person():
    S=np.zeros((420,420,3),np.uint8); A=np.zeros((420,420),np.uint8)
    img=np.zeros((420,420,3),np.uint8)
    def sh(pts,fill,cl=True): 
        j=jit(pts,2,cl,10); cv2.fillPoly(img,[np.array(j,np.int32)],fill,cv2.LINE_AA); outline(img,pts,cl,2)
    sh([(60,420),(70,300),(140,260),(280,260),(350,300),(360,420)],(60,60,170))  # shirt
    sh([(175,240),(245,240),(240,280),(180,280)],(150,190,235))
    c=[(210+88*np.cos(t),150+100*np.sin(t)) for t in np.linspace(0,6.28,16,endpoint=False)]
    sh(c,(150,190,235))
    sh([(120,130),(140,70),(210,50),(285,75),(300,135),(250,95),(160,100)],(30,50,80))
    for ex in(175,245):
        cv2.ellipse(img,(ex,155),(20,12),0,10,170,INK,5,cv2.LINE_AA)
    cv2.ellipse(img,(210,215),(26,14),0,200,340,INK,5,cv2.LINE_AA)
    cv2.circle(img,(280,178),5,(235,200,120),-1,cv2.LINE_AA)
    mask=np.zeros((420,420),np.uint8)
    mask[(img.sum(2)>0)]=255
    return np.dstack([img,mask])
PERSON=make_person()
def ease(t): t=min(max(t,0),1); return t*t*(3-2*t)
def overlay(frame,spr,cx,cy,s):
    h,w=spr.shape[:2]; nw,nh=max(2,int(w*s)),max(2,int(h*s))
    r=cv2.resize(spr,(nw,nh),interpolation=cv2.INTER_AREA)
    x0,y0=int(cx),int(cy); x0-=0; 
    xs,ys=x0,y0
    X0,Y0=max(xs,0),max(ys,0);X1,Y1=min(xs+nw,W),min(ys+nh,H)
    if X1<=X0 or Y1<=Y0: return
    p=r[Y0-ys:Y1-ys,X0-xs:X1-xs]; a=p[...,3:4].astype(np.float32)/255
    frame[Y0:Y1,X0:X1]=(frame[Y0:Y1,X0:X1]*(1-a)+p[...,:3]*a).astype(np.uint8)
gs=[(make_group(w,i),w,ap,pos,sc,tg) for w,i,ap,pos,sc,tg in GROUPS]
pr=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30000/1001','-i','-','-frames:v',str(N),'-c:v','libx264','-pix_fmt','yuv420p','-crf','14','-r','30000/1001','rt.mp4'],stdin=subprocess.PIPE)
for f in range(N):
    fr=bg.copy(); shimmer(fr,f)
    for (spr,anc),w,ap,pos,sc,tg in gs:
        if f<ap: continue
        d0=max(70,ap); t=ease((f-d0)/(195-d0)) if f>=d0 else 0
        pop=min(1,0.4+0.6*(f-ap)/5)
        s=sc*(1-0.7*t)*pop
        # anchor (item) position moves pos->tg
        ax=pos[0]+(tg[0]-pos[0])*t; ay=pos[1]+(tg[1]-pos[1])*t
        overlay(fr,spr,ax-anc[0]*s,ay-anc[1]*s,s)
    if f>=140:
        t=(f-140)/67; e=ease(t)
        s=1.5-1.2*e; cy=1180-(1180-330)*e; cx=1060+25*np.sin(t*5)*(1-e*.5)
        overlay(fr,PERSON,cx-210*s,cy-420*s,s)
    pr.stdin.write(fr.tobytes())
pr.stdin.close(); pr.wait()
json.dump({'frames':N,'cut':0,'shimmer':[0,40],'labels':[{'word':w,'appear':ap,'drift_start':max(70,ap),'drift_end':195} for w,i,ap,pos,sc,tg in GROUPS],'character':{'enter':140,'end':207},'camera_motion':False},open('timeline.json','w'),indent=1)
m=(wm>0).mean();print('water frac',m)
cv2.imwrite('/tmp/_bg.png',bg)
