import cv2,sys,numpy as np,json
F=sys.argv[1];cap=cv2.VideoCapture(F)
pick={"S001.1_char_trophy":60,"S001.12_split":1018,"S002.0_google_dark":1824,"S009.10_poker":5121,"S016.0_beta_card":6061,"S018.0_nobu":7254,"S020.0_peiwei":7585,"S010.0_black":5571,"S021.4_endcard":8189,"S009.4_flames":4568}
out={}
for k,i in pick.items():
    cap.set(cv2.CAP_PROP_POS_FRAMES,i);ok,f=cap.read()
    s=cv2.resize(f,(160,90),interpolation=cv2.INTER_AREA).reshape(-1,3).astype(np.float32)
    crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
    _,lab,cen=cv2.kmeans(s,6,None,crit,3,cv2.KMEANS_PP_CENTERS)
    cnt=np.bincount(lab.flatten(),minlength=6)/len(lab)
    o=np.argsort(-cnt)
    out[k]=[("#%02x%02x%02x"%(int(cen[j][2]),int(cen[j][1]),int(cen[j][0])),round(float(cnt[j]),3)) for j in o]
json.dump(out,open('tables/palette.json','w'),indent=1)
for k,v in out.items(): print(k,v[:4])
