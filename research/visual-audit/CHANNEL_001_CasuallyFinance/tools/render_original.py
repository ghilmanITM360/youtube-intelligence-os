"""Tiny original-asset renderer (PIL + ffmpeg). Motion rules come from 11_MOTION_WINDOWS: pop-in/pose/text-swap = 1 frame, rise/slide = linear or ease-out over 12-16 frames, zoom = 1.0 -> 1.2 over ~15 frames. All art drawn here; nothing copied from the source channel."""
import sys,subprocess,math
from PIL import Image,ImageDraw,ImageFont
W,H,FPS=1920,1080,24
INK=(30,30,40);BG=(250,250,247);TEAL=(52,170,170);ORG=(240,140,40);GOLD=(235,185,40);RED=(215,50,50);GRN=(60,160,90)
F=lambda s:ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',s)
def figure(d,x,y,pose,s=1.0):
    # original figure "Mo": rounded-square teal head, orange beanie, line body
    hw=int(70*s)
    d.rounded_rectangle([x-hw,y-hw*2,x+hw,y],radius=int(28*s),fill=TEAL,outline=INK,width=int(7*s))
    d.pieslice([x-hw,y-hw*2-int(40*s),x+hw,y-int(20*s)+0],180,360,fill=ORG,outline=INK,width=int(6*s))
    ey=y-int(hw*1.1)
    for dx in(-28,28):d.ellipse([x+dx*s-7*s,ey-7*s,x+dx*s+7*s,ey+7*s],fill=INK)
    if pose=='worried':
        d.line([x-45*s,ey-26*s,x-15*s,ey-18*s],fill=INK,width=int(6*s));d.line([x+45*s,ey-26*s,x+15*s,ey-18*s],fill=INK,width=int(6*s))
        d.arc([x-20*s,y-40*s,x+20*s,y-12*s],200,340,fill=INK,width=int(6*s))
    else:d.arc([x-30*s,y-55*s,x+30*s,y-15*s],20,160,fill=INK,width=int(6*s))
    bt=y+int(150*s);w=int(7*s)
    d.line([x,y,x,bt],fill=INK,width=w)
    d.line([x,y+40*s,x-70*s,y+110*s],fill=INK,width=w)
    if pose=='point':d.line([x,y+40*s,x+170*s,y-30*s],fill=INK,width=w)
    else:d.line([x,y+40*s,x+70*s,y+110*s],fill=INK,width=w)
    d.line([x,bt,x-50*s,bt+120*s],fill=INK,width=w);d.line([x,bt,x+50*s,bt+120*s],fill=INK,width=w)
def coin(d,x,y,r,label):
    d.ellipse([x-r,y-r,x+r,y+r],fill=GOLD,outline=INK,width=8)
    f=F(int(r*0.9));d.text((x,y),label,font=f,fill=INK,anchor='mm')
def text(d,x,y,t,size,col=INK):d.text((x,y),t,font=F(size),fill=col,anchor='mm')
def ease(k,t):return t if k=='linear' else 1-(1-t)**2
def prog(f,start,n,k='linear'):
    return 0 if f<start else (1 if f>=start+n else ease(k,(f-start)/n))
def bars(d,x0,y0,vals,col,scale=1.0):
    for i,v in enumerate(vals):
        h=v*scale;d.rectangle([x0+i*150,y0-h,x0+i*150+110,y0],fill=col,outline=INK,width=6)
    d.line([x0-20,y0,x0+len(vals)*150,y0],fill=INK,width=7)
def scene_frame(sc,f,d):
    if sc=='intro':
        figure(d,520,430,'neutral')
        if f>=12:text(d,1250,300,'Why does coffee',92)
        if f>=12:text(d,1250,410,'cost more now?',92)
    elif sc=='chart':
        n=[0,12,34]
        bars(d,420,820,[200,260,330],GRN,1) if f>=n[0] else 0
        if f>=n[1]:bars(d,1050,820,[180,230,300,380],ORG)
        if f>=n[2]:figure(d,260,520,'neutral',0.8)
        p=prog(f,40,10);
        if p>0:d.line([700,300,700+int(500*p),300-int(180*p)],fill=RED,width=14)
    elif sc=='coin':
        figure(d,520,430,'point')
        p=prog(f,30,15,'ease_out');r=int(170-70*p)
        coin(d,1300,520,r,'$1' if f<24 else '$0.8')
        if f>=24:text(d,1300,820,'same coin, less coffee',60)
    elif sc=='zoom':
        bars(d,420,820,[200,260,330,420,520],ORG)
        figure(d,300,430,'worried' if f>=18 else 'neutral',0.9)
        text(d,1200,230,'prices up, wages flat',80)
    elif sc=='end':
        text(d,960,500,'inflation = a shrinking coin',90)
SC=[('intro',72),('chart',77),('coin',67),('zoom',84),('end',36)]
def render(out,vertical=False):
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','14',out],stdin=subprocess.PIPE)
    for sc,n in SC:
        for f in range(n):
            im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im);scene_frame(sc,f,d)
            if sc=='zoom':
                s=1+0.2*prog(f,20,15,'ease_out')
                cw,ch=int(W/s),int(H/s);im=im.crop(((W-cw)//2,(H-ch)//2,(W-cw)//2+cw,(H-ch)//2+ch)).resize((W,H),Image.LANCZOS)
            p.stdin.write(im.tobytes())
    p.stdin.close();p.wait()
if __name__=='__main__':render(sys.argv[1])
