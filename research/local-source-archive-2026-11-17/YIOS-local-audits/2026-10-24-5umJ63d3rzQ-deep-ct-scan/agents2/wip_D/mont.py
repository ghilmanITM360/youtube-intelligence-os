import sys,cv2,numpy as np
ids=sys.argv[2:]; out=sys.argv[1]
R='/Users/ghilmankhan/YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan/evidence/'
rows=[]
for i in ids:
    im=cv2.imread(R+i+'.jpg'); h=im.shape[0]
    rows.append(im[:min(560,h)])
w=max(r.shape[1] for r in rows)
rows=[cv2.copyMakeBorder(r,0,6,0,w-r.shape[1],cv2.BORDER_CONSTANT,value=(0,0,255)) for r in rows]
cv2.imwrite(out,np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,88])
