import cv2,csv,json,numpy as np,sys
F=sys.argv[1]
ev=list(csv.DictReader(open('visual_event_ledger.csv')))
st=list(csv.DictReader(open('visual_states.csv')))
micro={'S007.1':3855,'S009.2':4417,'S009.8':4916}
rng=[]
for i,s in enumerate(st):
    a=0 if i==0 else int(ev[i-1]['end_frame'])
    b=8337 if i==len(st)-1 else int(ev[i]['start_frame'])-1
    rng.append((s['visual_state_id'],a,b))
need=set()
for sid,a,b in rng:
    need|={a,(a+b)//2,b}
    if sid in micro: need|={micro[sid]-1,micro[sid]}
c=cv2.VideoCapture(F);fr={};i=0
while i<=max(need):
    ok,f=c.read()
    if not ok:break
    if i in need: fr[i]=f
    i+=1
def hexc(c): return "#%02x%02x%02x"%(int(c[2]),int(c[1]),int(c[0]))
def lum(c):
    v=[x/255 for x in (c[2],c[1],c[0])];v=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in v];return .2126*v[0]+.7152*v[1]+.0722*v[2]
def analyze(f):
    small=cv2.resize(f,(640,360),interpolation=cv2.INTER_AREA)
    bgc=np.median(small.reshape(-1,3),axis=0)
    fg=(np.abs(small.astype(int)-bgc).max(axis=2)>40).astype(np.uint8)
    d=cv2.dilate(fg,np.ones((15,15),np.uint8))
    n,lab,stats,cent=cv2.connectedComponentsWithStats(d,connectivity=8)
    blobs=[]
    for k in range(1,n):
        x,y,w,h,area=stats[k]
        if area>=300: blobs.append((int(area),[round(x/640,3),round(y/360,3),round((x+w)/640,3),round((y+h)/360,3)]))
    blobs.sort(key=lambda t:-t[0]);blobs=[b for _,b in blobs[:7]]
    px=small.reshape(-1,3).astype(np.float32)
    crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,15,1.0)
    _,lb,cen=cv2.kmeans(px[::4],6,None,crit,2,cv2.KMEANS_PP_CENTERS)
    cnt=np.bincount(lb.flatten(),minlength=6)/len(lb);o=np.argsort(-cnt)
    pal=[(hexc(cen[j]),round(float(cnt[j]),3)) for j in o if cnt[j]>=0.004][:5]
    darkest=min(cen,key=lambda x:lum(x));cr=(max(lum(bgc),lum(darkest))+.05)/(min(lum(bgc),lum(darkest))+.05)
    ys,xs=np.nonzero(fg)
    cx=round(float(xs.mean()/640),3) if len(xs) else None;cy=round(float(ys.mean()/360),3) if len(xs) else None
    return dict(bg=hexc(bgc),fg_fraction=round(float(fg.mean()),4),centroid=[cx,cy],blobs=blobs,palette=pal,max_contrast_vs_bg=round(float(cr),1))
out={}
for sid,a,b in rng:
    m=(a+b)//2
    o=analyze(fr[m]);o.update(start_frame=a,end_frame=b,n_frames=b-a+1,start_pts=round((a+1)/30,4),end_pts=round((b+1)/30,4),dur_s=round((b-a+1)/30,4),mid_frame=m)
    if sid in micro: o['micro_event_frame']=micro[sid];o['before_micro']=analyze(fr[micro[sid]-1]);o['after_micro']=analyze(fr[micro[sid]])
    out[sid]=o
json.dump(out,open('v2/state_objective.json','w'),indent=0)
print(len(out),sum(v['n_frames'] for v in out.values()))
