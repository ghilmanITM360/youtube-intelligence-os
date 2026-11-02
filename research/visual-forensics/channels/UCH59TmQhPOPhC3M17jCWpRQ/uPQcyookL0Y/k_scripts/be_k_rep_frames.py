import cv2,numpy as np,csv,sys,os,json
SRC="/Users/ghilmankhan/Downloads/videos in mp3/BarelyEvolved-MP4/The Worst Time in History to Be Born as a Human [uPQcyookL0Y].mp4"
batch,i0,i1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
extra=json.loads(sys.argv[4]) if len(sys.argv)>4 else {}
S=list(csv.DictReader(open('tables/states_v5_draft.csv')))[i0:i1]
os.makedirs(f'frames/native_rep/{batch}',exist_ok=True)
cap=cv2.VideoCapture(SRC);rows=[]
for r in S:
    a,b=int(r['start']),int(r['end']);n=b-a+1
    fr=sorted(set([min(b,a+4)] if n<30 and n<8 else ([min(b,a+4),(a+b)//2] if n<120 else [min(b,a+4),a+n//3,a+2*n//3,b-3]))|set(extra.get(r['state_v4'],[])))
    if n>=8 and n<30:fr=sorted(set([min(b,a+4),b-2]))
    for f in fr:
        cap.set(cv2.CAP_PROP_POS_FRAMES,f);ok,im=cap.read();p=f'frames/native_rep/{batch}/{r["state_v4"]}_f{f}.png';cv2.imwrite(p,im)
        px=im[::4,::4].reshape(-1,3).astype(np.float32)
        _,lab,c=cv2.kmeans(px,5,None,(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0),1,cv2.KMEANS_PP_CENTERS)
        cnt=np.bincount(lab.ravel(),minlength=5);o=np.argsort(-cnt)
        pal=';'.join('#%02x%02x%02x:%.1f%%'%(int(c[k][2]),int(c[k][1]),int(c[k][0]),100*cnt[k]/cnt.sum()) for k in o)
        rows.append([r['state_v4'],f,p,pal])
with open(f'tables/k_rep_frames_{batch}.csv','w',newline='') as o:
    w=csv.writer(o);w.writerow(['state_v5','frame','native_png','kmeans5_palette_native_every4px_BGR2RGB_hex:share']);w.writerows(rows)
print(len(rows),'frames')
