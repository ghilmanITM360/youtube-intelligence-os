"""End-card check for the 24 long videos with campaign ledgers: frames at (duration-2 s) and (duration-12 s), tiled.
Also card-length upper bound for the 20 measured long videos = duration - start of last shot."""
import csv, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from ledger_lib import media
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = R + '/review_sample'
vs = open('/tmp/x24.txt').read().split()
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
ins=[];fc=[];rows=[]
for k,v in enumerate(vs):
    p=media(v); d=dur(p); rows.append((k+1,v,round(d,2)))
    for j,off in enumerate((2,12)):
        f=f'{O}/cells/e{k:02d}_{j}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{max(d-off,0):.2f}','-i',p,'-frames:v','1','-vf','scale=256:144',f],check=True)
        ins+=['-i',f]
n=len(ins)//2
fc=''.join(f'[{i}:v]' for i in range(n))+f'xstack=inputs={n}:layout='+'|'.join(f'{(i%8)*256}_{(i//8)*144}' for i in range(n))+'[o]'
subprocess.run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[o]',O+'/endcards_long_other24.jpg'],check=True)
csv.writer(open(O+'/endcards_other24_order.csv','w',newline='')).writerows([('position','video_id','duration_s')]+rows)
# card length upper bound for the 20 measured long videos
L=R+'/ledgers_measured'; idx={r['video_id']:r for r in csv.DictReader(open(L+'/INDEX.csv'))}
last={}
for r in csv.DictReader(open(L+'/ALL_SHOT_LEDGER.csv')): last[r['video_id']]=r
out=[(v,idx[v]['duration_s'],last[v]['start_pts_seconds'],round(float(idx[v]['duration_s'])-float(last[v]['start_pts_seconds']),2)) for v in idx if idx[v]['format']=='LONG' and v in last]
csv.writer(open(O+'/endcard_lengths_20long.csv','w',newline='')).writerows([('video_id','duration_s','last_shot_start_s','last_shot_length_s')]+out)
import statistics; print('last-shot length median',statistics.median(x[3] for x in out),'min',min(x[3] for x in out),'max',max(x[3] for x in out))
print(len(rows),'videos; layout 8 wide: each video = 2 tiles (dur-2 s, dur-12 s)')
