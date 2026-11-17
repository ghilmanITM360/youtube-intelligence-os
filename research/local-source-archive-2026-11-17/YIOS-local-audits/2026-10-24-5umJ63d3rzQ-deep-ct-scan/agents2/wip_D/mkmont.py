import glob,csv,os,cv2,numpy as np
n={}
for s in (7,8):
    for r in csv.DictReader(open(f'../../agents/shard_{s}/candidates.csv')): n[r['id']]=int(r['n'])
ids=open('cand_order.txt').read().split()
done=set(l.split('|')[0] for f in glob.glob('notes_0*.txt') for l in open(f))
rem=[i for i in ids if i not in done]
R='../../evidence/'
for f in glob.glob('mont/*'): os.remove(f)
groups=[];cur=[]
for i in rem:
    if n[i]>=6:
        if cur: groups.append(cur);cur=[]
        groups.append([i])
    else:
        cur.append(i)
        if len(cur)==3: groups.append(cur);cur=[]
if cur: groups.append(cur)
for k,g in enumerate(groups):
    rows=[]
    for i in g:
        im=cv2.imread(R+i+'.jpg'); rows.append(im if (len(g)==1) else im[:560])
    w=max(r.shape[1] for r in rows)
    rows=[cv2.copyMakeBorder(r,0,6,0,w-r.shape[1],cv2.BORDER_CONSTANT,value=(0,0,255)) for r in rows]
    cv2.imwrite(f'mont/m{k:03d}.jpg',np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,85])
open('mont/index.txt','w').write('\n'.join(f'm{k:03d}: '+' '.join(g) for k,g in enumerate(groups)))
print(len(rem),len(groups))
