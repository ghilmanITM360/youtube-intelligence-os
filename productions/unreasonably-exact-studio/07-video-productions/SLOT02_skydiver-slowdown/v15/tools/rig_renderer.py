"""Render registered vector parts along editable keyframe tracks. Run from any cwd."""
import argparse, ctypes.util, io, json, math, subprocess
from functools import lru_cache
from pathlib import Path
mac_cairo=Path('/opt/homebrew/lib/libcairo.2.dylib')
if mac_cairo.exists() and ctypes.util.find_library('cairo') is None:
    find_library=ctypes.util.find_library
    ctypes.util.find_library=lambda name: str(mac_cairo) if name=='cairo' else find_library(name)
import cairocffi as C
import cairosvg
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
WIDTH,HEIGHT=720,1280
@lru_cache(None)
def drawing(file, canvas_w=None):
    """Return (surface, x, y, k): surface holds the alpha-cropped art at k px per canvas unit.
    PNG layers (Codex) keep their native delivery resolution (4x for 640x400 canvases): k = png_width/canvas_w,
    so the 4x export is applied exactly once. SVGs are rasterised at 2x as before."""
    if str(file).lower().endswith('.png'):
        im = Image.open(ROOT/file).convert('RGBA')
        k = im.width / canvas_w if canvas_w else 1.0
    else:
        im = Image.open(io.BytesIO(cairosvg.svg2png(url=str(ROOT/file), scale=2))).convert('RGBA'); k = 2.0
    bb = im.getchannel('A').getbbox()   # alpha bounds: generated PNGs may hold RGB under zero alpha
    x, y, r, b = bb
    crop = io.BytesIO(); im.crop(bb).save(crop, 'PNG'); crop.seek(0)
    return C.ImageSurface.create_from_png(crop), x/k, y/k, k
def draw(ctx, file, opacity=1, canvas_w=None):
    surf, x, y, k = drawing(file, canvas_w)
    ctx.save(); ctx.translate(x, y); ctx.scale(1/k, 1/k); ctx.set_source_surface(surf)
    ctx.get_source().set_filter(C.FILTER_GOOD); ctx.paint_with_alpha(opacity); ctx.restore()
def sprite(ctx,file,x,y,sx,sy=None):
    ctx.save();ctx.translate(x,y);ctx.scale(sx,sx if sy is None else sy)
    draw(ctx,'assets/'+file+'.svg');ctx.restore()
@lru_cache(None)
def rig(view):return json.loads((ROOT/f'rigs/{view}/rig.json').read_text())
def value(keys,u):
    if u<=keys[0][0]:return keys[0][1]
    for (t0,a),(t1,b) in zip(keys,keys[1:]):
        if u<=t1:
            q=(u-t0)/(t1-t0);return a+(b-a)*q*q*(3-2*q)
    return keys[-1][1]
def actor(ctx,view,channels,cx,cy,scale):
    model=rig(view); parts={part['id']:part for part in model['parts']}
    def apply(name):
        p=parts[name]
        if p['parent']:apply(p['parent'])
        ctx.translate(channels.get(name+'_x',0),channels.get(name+'_y',0))
        px,py=p['pivot'];angle=max(p['limits'][0],min(p['limits'][1],channels.get(name,0)))
        ctx.translate(px,py);ctx.rotate(math.radians(angle));ctx.translate(-px,-py)
    ctx.save();ctx.translate(cx,cy);ctx.scale(scale,scale);ctx.translate(-model['canvas'][0]/2,-model['canvas'][1]/2)
    cw = model['canvas'][0]
    for name,p in parts.items():
        blink = int(channels.get('blink', 0) >= 0.5)
        if name=='lids': opacity=blink          # lids REPLACE eyes during a blink
        elif name=='eyes': opacity=1-blink
        else: opacity=channels.get(name+'_alpha', p.get('opacity', 1) if name!='lids' else 1)
        f = channels.get(name+'_file', p['file'])   # replacement drawing (e.g. mouth_open)
        if opacity:
            ctx.save();apply(name);draw(ctx,f,opacity,cw)
            hook=channels.get('_attach',{}).get(name)   # attached equipment drawn in the part's own FK frame
            if hook: hook(ctx)
            ctx.restore()
    ctx.restore()
def travel(comp,u):
    a,b=comp['travel']['initial'],comp['travel']['final']
    return comp['seconds']*(a*u+.5*(b-a)*u*u),a+(b-a)*u
def hud(ctx,x,y,s,speed):
    actor(ctx,'instrument',{'pointer':-72+144*speed/200},x,y,s)
def world(ctx,layout,distance):
    ctx.set_source_rgb(.975,.974,.952);ctx.paint()
    if layout=='ground':
        s=.69+.00029*distance
        sprite(ctx,'environment/river_plain',180-455*s,327-517*s,s)
        return
    if layout in ('portrait','instrument'):return
    # Camera tracks much of the fall. Spacing and speed share a single integrated distance.
    for i,(x,y,sz) in enumerate([(-19,119,.58),(234,376,.67),(-43,625,.80),(262,784,.72),(35,1000,.42)]):
        yy=((y-distance*.40+100)%1120)-100
        sprite(ctx,'environment/cloud_far',x,yy,sz)
    for x,y,sz in [(-124,364,.80),(283,650,1.17),(-102,920,.94),(296,1180,.97)]:
        yy=((y-distance*.99+130)%1370)-130
        sprite(ctx,'environment/cloud_close',x,yy,sz)
    # Near shelf enters and leaves the tracked frame considerably faster than the distant bank.
    if layout in ('fast','slow'):
        for x,y,sz in [(-244,744,1.52),(230,1430,1.68)]:
            yy=((y-distance*1.42+210)%1990)-210
            sprite(ctx,'environment/cloud_close',x,yy,sz)
    factor=.081 if layout=='slow' else .025
    sprite(ctx,'environment/far_ridge',0,536-distance*factor,.505)
    near_y = 578 - distance * factor * 1.20
    # Continue the foreground fill beyond its illustrated strip.
    ctx.set_source_rgb(210 / 255, 216 / 255, 204 / 255)
    ctx.rectangle(0, near_y + 210 * .52, 360, 640)
    ctx.fill()
    sprite(ctx,'environment/near_ridge',-4,near_y,.52)
def stage(comp,u,solid):
    # Solid pass contains only compositable foreground art. Background remains independent.
    d,speed=travel(comp,u); view=comp['view']; layout=comp['layout']
    f=comp['framing']; ch={k:value(v,u) for k,v in comp['channels'].items()}
    ctx=C.Context(solid);ctx.scale(WIDTH/360,HEIGHT/640)
    if view=='instrument':hud(ctx,180,296,1.23,speed)
    elif view=='pov':actor(ctx,view,ch,180,535,1.17)
    else:
        actor(ctx,view,ch,f['x'],f['y']+f['drift_per_unit']*d,f['scale'])
        if layout=='slow':hud(ctx,278,135,.44,speed)
        if layout=='glance':hud(ctx,262,376,.52,speed)
    frame=C.ImageSurface(C.FORMAT_ARGB32,WIDTH,HEIGHT)
    bg=C.Context(frame);bg.scale(WIDTH/360,HEIGHT/640);world(bg,layout,d);bg.identity_matrix()
    bg.set_source_surface(solid);bg.paint()
    return frame
def pipe(options):
    return subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y',*options],stdin=subprocess.PIPE)
def render(id,poster=False):
    comp=json.loads((ROOT/f'motion_clips/compositions/{id}.json').read_text())
    fps=comp['fps']; n=round(comp['seconds']*fps)
    if poster:
        f=stage(comp,.53,C.ImageSurface(C.FORMAT_ARGB32,WIDTH,HEIGHT))
        f.write_to_png(str(ROOT/f'previews/{id}.png'));return
    video=pipe(['-f','rawvideo','-pix_fmt','bgra','-s',f'{WIDTH}x{HEIGHT}','-r',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',str(ROOT/f'motion_clips/{id}.mp4')])
    alpha=pipe(['-f','image2pipe','-framerate',str(fps),'-vcodec','png','-i','-','-c:v','qtrle','-pix_fmt','argb',str(ROOT/f'motion_clips/alpha/{id}.mov')])
    try:
        for i in range(n):
            fg=C.ImageSurface(C.FORMAT_ARGB32,WIDTH,HEIGHT)
            frame=stage(comp,i/(n-1),fg);frame.flush()
            video.stdin.write(frame.get_data());fg.write_to_png(alpha.stdin)
    finally:
        video.stdin.close();alpha.stdin.close()
        rc=[p.wait() for p in [video,alpha]]
        if any(rc):raise SystemExit(f'{id}: encoder failure {rc}')
    print(id,n,flush=True)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('ids',nargs='+');parser.add_argument('--poster',action='store_true');args=parser.parse_args()
    for id in args.ids:render(id,args.poster)
