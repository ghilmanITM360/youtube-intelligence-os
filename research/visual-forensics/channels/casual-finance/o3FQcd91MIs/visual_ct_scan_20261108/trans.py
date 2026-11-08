import cv2,sys,numpy as np
F=sys.argv[1]; cap=cv2.VideoCapture(F)
def get(i):
    cap.set(cv2.CAP_PROP_POS_FRAMES,i); ok,f=cap.read(); return f
# (label, first frame idx, count)
sets=[("S001.0>1 zoom/pop",39,5),("S001.1>2 arrow+toddler",172,4),("S001.11>12 zigzag split",998,4),("S001.15>16 text swap",1352,4),
("S005.1>2 chart return",2682,4),("S009.3>4 X+flames",4547,4),("S009.14>S010 black",5551,4),("S017.6>S018 3-frame",7230,6),
("S002.0 google entry",1821,4),("S021.3>4 end card",8166,4),("S021.4 end>black",8335,3),("S001.5 FartCoin",396,4)]
def sheet(group,name):
    rows=[]
    for lab,a,n in group:
        tiles=[]
        for k in range(n):
            f=cv2.resize(get(a+k),(320,180),interpolation=cv2.INTER_AREA)
            cv2.putText(f,f"f{a+k} t{(a+k+1)/30:.3f}",(5,18),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
            tiles.append(f)
        while len(tiles)<6: tiles.append(np.full((180,320,3),128,np.uint8))
        cv2.putText(tiles[0],lab,(5,170),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
        rows.append(np.hstack(tiles))
    cv2.imwrite(name,np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,78])
sheet(sets[:6],'frames/trans_sheet_1.jpg');sheet(sets[6:],'frames/trans_sheet_2.jpg')
