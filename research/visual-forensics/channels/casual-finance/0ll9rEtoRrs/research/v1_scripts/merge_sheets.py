import csv,json,cv2,numpy as np
src=json.load(open('source_manifest.json'))['source_path']
S=sorted(csv.DictReader(open('integrated_v2/reviewed_states_v2.csv')),key=lambda s:int(s['start']))
M={r['id']:r for r in csv.DictReader(open('phaseA/merge_metrics.csv'))}
pairs=[(S[i-1],S[i]) for i in range(1,len(S)) if S[i]['flag_merge']=='True']
want={}
for p,s in pairs:
    for f in (int(p['end']),int(s['start'])): want[f]=None
fr=sorted(want);cap=cv2.VideoCapture(src);i=0;k=0
while k<len(fr):
    ok,im=cap.read()
    if not ok:break
    if i==fr[k]:
        want[i]=cv2.resize(im,(560,315));k+=1
    i+=1
tiles=[]
for p,s in pairs:
    a=want[int(p['end'])].copy();b=want[int(s['start'])].copy()
    cv2.putText(a,f"{p['id']} END f{p['end']}",(6,22),0,0.6,(0,0,255),2)
    cv2.putText(b,f"{s['id']} START f{s['start']} d={M[s['id']]['boundary_diff']} gap={M[s['id']]['gap_frames']}",(6,22),0,0.6,(0,0,255),2)
    tiles.append(np.hstack([a,b]))
n=0
for j in range(0,len(tiles),6):
    cv2.imwrite(f'phaseA/merge_sheets/m{j//6+1:02d}.jpg',np.vstack(tiles[j:j+6]),[cv2.IMWRITE_JPEG_QUALITY,80]);n+=1
open('phaseA/merge_sheet_index.csv','w').write('sheet,ids\n'+''.join(f"m{j//6+1:02d},{' '.join(s['id'] for p,s in pairs[j:j+6])}\n" for j in range(0,len(pairs),6)))
print(n)
