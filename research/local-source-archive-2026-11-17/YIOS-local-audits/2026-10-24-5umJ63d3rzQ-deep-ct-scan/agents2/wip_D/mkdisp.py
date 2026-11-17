import cv2,numpy as np,os
ids=[143,144,145,146,163,164,277,278,279,280]+[147,152,157,162]+list(range(165,277,5))+[276]
ids=sorted(set(ids))
R='../../disputes/'
os.makedirs('dmont',exist_ok=True)
ims=[(i,cv2.imread(f'{R}SD{i:03d}.jpg')) for i in ids]
print(ims[0][1].shape,len(ims))
per=4;k=0
for a in range(0,len(ims),per):
    rows=[]
    for i,im in ims[a:a+per]:
        im=im.copy(); cv2.putText(im,f'SD{i}',(5,18),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2); rows.append(im)
    w=max(r.shape[1] for r in rows)
    rows=[cv2.copyMakeBorder(r,0,4,0,w-r.shape[1],cv2.BORDER_CONSTANT,value=(0,0,255)) for r in rows]
    cv2.imwrite(f'dmont/d{k:02d}.jpg',np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,85]);k+=1
open('dmont/index.txt','w').write(str(ids))
print(k,ids)
