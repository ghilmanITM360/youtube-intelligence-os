import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
C=list(csv.DictReader(open('integrated_v3/reviewed_candidates_v3.csv')))
rows=[c for c in C if c['smp_status']=='FIRST_PASS_ONLY']
rows.sort(key=lambda c:int(c['stable_frame']))
print(len(rows))
want={}
for r in rows:want[int(r['pre_frame'])]=None;want[int(r['stable_frame'])]=None
ks=sorted(want);cap=cv2.VideoCapture(src);n=0;k=0
while k<len(ks):
    ok,im=cap.read()
    if not ok:break
    if n==ks[k]:want[n]=cv2.resize(im,(560,315));k+=1
    n+=1
tiles=[]
for r in rows:
    a=want[int(r['pre_frame'])].copy();b=want[int(r['stable_frame'])].copy()
    cv2.putText(a,f"{r['id']} BEFORE f{r['pre_frame']}",(6,22),0,0.6,(0,0,255),2);cv2.putText(b,f"AFTER f{r['stable_frame']} claimed={r['final_type_v3']}",(6,22),0,0.6,(0,0,255),2)
    tiles.append(np.hstack([a,b]))
for j in range(0,len(tiles),6):cv2.imwrite(f'phaseA/cand_sheets_r/r{j//6+1:02d}.jpg',np.vstack(tiles[j:j+6]),[cv2.IMWRITE_JPEG_QUALITY,80])
print(len(tiles)//6+(len(tiles)%6>0))
csv.writer(open('phaseA/cand_rest_ids.csv','w')).writerows([('id',)]+[(r['id'],) for r in rows])
