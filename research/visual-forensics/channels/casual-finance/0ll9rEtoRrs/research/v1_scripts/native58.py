import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
C=list(csv.DictReader(open('integrated_v4/reviewed_candidates_v4.csv')))
R=[c for c in C if c['smp_status'] in('REVIEWED_CONFIRMED_TYPE_WRONG','REVIEWED_NO_VISIBLE_CHANGE')]
print(len(R))
want=set()
for c in R:want|={int(c['pre_frame']),int(c['stable_frame'])}
fr={};cap=cv2.VideoCapture(src);i=0
while i<=max(want):
    ok,im=cap.read()
    if not ok:break
    if i in want:fr[i]=im
    i+=1
rows=[]
for c in R:
    a,b=fr[int(c['pre_frame'])],fr[int(c['stable_frame'])]
    d=np.abs(a.astype(np.int16)-b.astype(np.int16)).max(axis=2)
    m12=d>12;m24=d>24
    frac12=float(m12.mean());frac24=float(m24.mean())
    mm=m12 if m12.sum()>0 else None
    if mm is not None and m24.sum()>0:mm=m24
    ctx=np.hstack([cv2.resize(a,(640,360)),cv2.resize(b,(640,360))])
    if mm is not None and mm.sum()>=4:
        ys,xs=np.where(mm);y0,y1,x0,x1=max(ys.min()-20,0),min(ys.max()+20,719),max(xs.min()-20,0),min(xs.max()+20,1279)
        if x1-x0<200:cx=(x0+x1)//2;x0=max(cx-100,0);x1=min(x0+200,1279)
        if y1-y0<120:cy=(y0+y1)//2;y0=max(cy-60,0);y1=min(y0+120,719)
        ca,cb=a[y0:y1,x0:x1],b[y0:y1,x0:x1]
        sc=min(640/ca.shape[1],360/ca.shape[0],4.0)
        ca=cv2.resize(ca,None,fx=sc,fy=sc,interpolation=cv2.INTER_CUBIC);cb=cv2.resize(cb,None,fx=sc,fy=sc,interpolation=cv2.INTER_CUBIC)
        h=max(ca.shape[0],360);pad=lambda x:cv2.copyMakeBorder(x,0,h-x.shape[0],0,640-x.shape[1],cv2.BORDER_CONSTANT,value=(40,40,40))
        crop=np.hstack([pad(ca),pad(cb)]);bbox=f'{x0},{y0},{x1},{y1}'
        for k in(0,1):cv2.rectangle(ctx,(int(x0/2)+k*640,int(y0/2)),(int(x1/2)+k*640,int(y1/2)),(0,0,255),2)
    else:
        crop=np.full((360,1280,3),40,np.uint8);cv2.putText(crop,'NO PIXEL CHANGE ABOVE THRESHOLD 12',(300,190),0,0.9,(255,255,255),2);bbox=''
    cv2.putText(ctx,f"{c['id']} BEFORE f{c['pre_frame']}",(6,22),0,0.6,(0,0,255),2);cv2.putText(ctx,f"AFTER f{c['stable_frame']}",(646,22),0,0.6,(0,0,255),2)
    cv2.imwrite(f"phaseA/native58/{c['id']}.jpg",np.vstack([ctx,crop]),[cv2.IMWRITE_JPEG_QUALITY,88])
    rows.append(dict(id=c['id'],claimed=c['final_type'],first_pass_type=c['type'],prior_review=c['smp_status'],prior_suggested=c['smp_suggested_type'],pre=c['pre_frame'],stable=c['stable_frame'],changed_frac_gt12=round(frac12,5),changed_frac_gt24=round(frac24,5),change_bbox=bbox))
w=csv.DictWriter(open('phaseA/native58_metrics.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
for n,part in((1,rows[:29]),(2,rows[29:])):
    w=csv.DictWriter(open(f'phaseA/native58_input_{n}.csv','w'),fieldnames=rows[0].keys());w.writeheader();w.writerows(part)
print(sum(1 for r in rows if not r['change_bbox']),'with no pixel change')
