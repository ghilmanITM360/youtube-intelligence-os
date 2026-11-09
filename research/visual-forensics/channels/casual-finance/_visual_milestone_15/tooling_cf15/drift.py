import cv2, sys, numpy as np
src=sys.argv[1]; pairs=[tuple(map(int,p.split(':'))) for p in sys.argv[2:]]
need=sorted({x for p in pairs for x in p}); fr={}
cap=cv2.VideoCapture(src); i=0
while True:
    ok,f=cap.read()
    if not ok or i>max(need): break
    if i in need: fr[i]=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    i+=1
orb=cv2.ORB_create(3000)
for a,b in pairs:
    A,B=fr[a],fr[b]; ka,da=orb.detectAndCompute(A,None); kb,db=orb.detectAndCompute(B,None)
    m=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True).match(da,db)
    pa=np.float32([ka[x.queryIdx].pt for x in m]); pb=np.float32([kb[x.trainIdx].pt for x in m])
    M,inl=cv2.estimateAffinePartial2D(pa,pb,method=cv2.RANSAC,ransacReprojThreshold=1.5)
    s=np.hypot(M[0,0],M[1,0]); print(a,b,'matches',len(m),'inliers',int(inl.sum()),'scale %.5f'%s,'tx %.2f ty %.2f'%(M[0,2],M[1,2]))
