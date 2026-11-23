"""Objective ref-vs-recon metrics for 10nEByVLya0. Usage: compare_metrics.py RECON.mp4 OUT.json"""
import json,os,subprocess,sys,numpy as np
REF=os.path.expanduser('~/workprojects/videos in mp3/CasuallyFinance/The IPO Boom Is the Danger Sign [10nEByVLya0].mp4')
def load(p,n=1660):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf','scale=270:480','-pix_fmt','gray','-f','rawvideo','-'],capture_output=True).stdout
    a=np.frombuffer(r,np.uint8);return a[:len(a)//(270*480)*270*480].reshape(-1,480,270).astype(np.int16)[:n]
A,B=load(REF),load(sys.argv[1]);n=min(len(A),len(B))
A,B=A[:n],B[:n]
C=slice(160,330);K=slice(330,350)           # content band rows, caption band rows (480-row scale)
def ink(a):return (a<200)
def events(x,thr):
    d=(np.abs(np.diff(x,axis=0))>16).mean(axis=(1,2));return set(np.where(d>thr)[0]+1)
def f1(a,b,tol=2):
    a,b=sorted(a),sorted(b)
    tp=sum(any(abs(x-y)<=tol for y in b) for x in a);tr=sum(any(abs(x-y)<=tol for x in a) for y in b)
    p=tp/max(len(a),1);r=tr/max(len(b),1);return round(2*p*r/max(p+r,1e-9),3),len(a),len(b)
def bbox(m):
    ys,xs=np.where(m);return None if len(ys)==0 else (xs.min(),ys.min(),xs.max(),ys.max())
def iou(a,b):
    if a is None and b is None:return 1.
    if a is None or b is None:return 0.
    ix=max(0,min(a[2],b[2])-max(a[0],b[0]));iy=max(0,min(a[3],b[3])-max(a[1],b[1]));i=ix*iy
    u=(a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-i;return i/u if u else 0.
ia=[ink(A[i,C])for i in range(n)];ib=[ink(B[i,C])for i in range(n)]
pres=np.mean([(m.sum()>30)==(k.sum()>30) for m,k in zip(ia,ib)])
ious=[iou(bbox(m),bbox(k)) for m,k in zip(ia,ib)]
C2=slice(160,318)   # supplementary: content rows only (y<1272), excludes caption ascenders that bleed into the band
ious2=[iou(bbox(ink(A[i,C2])),bbox(ink(B[i,C2]))) for i in range(n)]
cap_a=A[:,K];cap_b=B[:,K]
res=dict(frames=n,content_presence_agreement=round(float(pres),3),content_bbox_iou_median=round(float(np.median(ious)),3),content_bbox_iou_median_nocaption_rows=round(float(np.median(ious2)),3),content_bbox_iou_mean_nocaption_rows=round(float(np.mean(ious2)),3),content_bbox_iou_mean=round(float(np.mean(ious)),3),
 content_change_event_F1_tol2=f1(events(A[:,C],.004),events(B[:,C],.004)),caption_change_event_F1_tol2=f1(events(cap_a,.01),events(cap_b,.01)),
 caption_ink_agreement=round(float(np.mean([(ink(cap_a[i]).sum()>20)==(ink(cap_b[i]).sum()>20) for i in range(n)])),3),
 ink_density_ratio_median=round(float(np.median([(m.mean()+1e-6)/(k.mean()+1e-6) for m,k in zip(ib,ia)])),3))
json.dump(res,open(sys.argv[2],'w'),indent=1);print(json.dumps(res,indent=1))
