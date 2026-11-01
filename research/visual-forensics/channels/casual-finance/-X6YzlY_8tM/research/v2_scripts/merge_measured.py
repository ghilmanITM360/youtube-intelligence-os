import csv,json,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
M={int(r['frame']):r for r in csv.DictReader(open('FULL_FRAME_MEASUREMENTS.csv'))}
st=list(csv.DictReader(open('integrated_v1/states_integrated.csv')))
out=[];import collections;c=collections.Counter()
for k,s in enumerate(st):
    if 'MERGE_WITH_PREV' not in json.dumps(s): continue
    a=int(s['start']);p=st[k-1]
    fr=float(M[a]['changed_frac_thr10_320']);big=int(M[a]['px_diff_ge150'])
    gap=a-int(p['end'])-1
    # MEASURED signal at boundary frame vs previous frame; thresholds are a heuristic, not a ruling
    lab='MERGE_SUPPORTED_BY_LOW_BOUNDARY_CHANGE' if fr<0.30 else ('KEEP_SEPARATE_CANDIDATE_HARD_CUT' if fr>0.60 else 'UNCERTAIN_MID_CHANGE')
    c[lab]+=1;out.append(dict(state=s['id'],prev=p['id'],boundary_frame=a,gap_frames_between=gap,changed_frac_at_boundary=fr,px_ge150=big,measured_label=lab,reviewer_flag='MERGE_WITH_PREV',final_ruling='PENDING_SECOND_REVIEW'))
with open('integrated_v1/merge_measured_signal.csv','w',newline='') as f:
    w=csv.DictWriter(f,list(out[0]));w.writeheader();w.writerows(out)
print(dict(c))
