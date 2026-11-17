import csv
m={int(r['frame']):float(r['mean_abs_diff_320']) for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))}
S=list(csv.DictReader(open('tables/states_v4_draft.csv')))
out=[]
for r in S[1:]:
    s=int(r['start']);w={n:m.get(n,0) for n in range(s-10,s+11)}
    pk=max(w,key=w.get);pv=w[pk]
    # contiguous run of frames >=max(1.0,0.1*peak) containing peak
    th=max(1.0,0.1*pv);a=pk
    while a-1 in w and w[a-1]>=th:a-=1
    b=pk
    while b+1 in w and w[b+1]>=th:b+=1
    kind='HARD_CUT' if a==b else ('TRANSITION_%df'%(b-a+1) if pv>=th else 'NONE')
    out.append([r['state_v4'],s,pk,round(pv,2),a,b,kind,s-a,'OK' if a==s else ('START_OFF_%+d'%(s-a))])
with open('tables/k_boundary_convention_check.csv','w',newline='') as o:
    w=csv.writer(o);w.writerow('state_v4,start,peak_frame,peak_mad320,run_first,run_last,kind,start_minus_runfirst,verdict'.split(','));w.writerows(out)
import collections
print(collections.Counter(x[6].split('_')[0] for x in out),collections.Counter(x[8] for x in out))
for x in out:
    if x[8]!='OK' or x[6].startswith('TRANS'):print(x)
