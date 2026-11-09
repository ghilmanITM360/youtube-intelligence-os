import csv,random,json,collections
D='integrated_v1/'
rd=lambda f:list(csv.DictReader(open(D+f)))
cands=rd('candidates_integrated.csv');disp=rd('disputes_integrated.csv')
un=rd('unowned_intervals.csv');mg=rd('merge_measured_signal.csv')
items=[]  # (priority,kind,id,note)
for c in cands:
    if c['verdict'] in('UNVERIFIED','NOT_A_CHANGE'):items.append((1,'candidate',c['id'],c['verdict']))
items.append((1,'state','S0279','split_check'))
for c in cands:
    if c['verdict']=='RECLASSIFIED':items.append((2,'candidate',c['id'],'RECLASSIFIED'))
for d in disp:items.append((3,'dispute',d['id'],d['verdict']))
for i,u in enumerate(un):items.append((4,'unowned',f"U{u['start']}-{u['end']}",u['status']))
for m in mg:items.append((5,'merge',m['state'],'prev='+m['prev']))
random.seed(20261101)
conf=[c for c in cands if c['verdict']=='CONFIRMED']
strata=collections.defaultdict(list)
for c in conf:strata[(c['machine_kind'],c['confidence'])].append(c['id'])
for k in sorted(strata):
    ids=sorted(strata[k]);n=max(1,round(len(ids)*0.25))
    for x in random.sample(ids,n):items.append((6,'candidate',x,'CONFIRMED_SAMPLE_25pct:%s/%s'%k))
items.sort(key=lambda t:t[0]);per=80;waves=[]
with open('v2_scripts/second_pass_plan.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['reviewer_shard','wave','priority','kind','id','note'])
    for i,t in enumerate(items):
        s=i//per+1;w.writerow([f'R{s:02d}',(s-1)//3+1,*t])
n=len(items);print(n,'items',(n+per-1)//per,'shards',collections.Counter(t[0] for t in items))
