import csv,os,sys
rd=lambda f:list(csv.DictReader(open(f)))
C={c['id']:c for c in rd('integrated_v1/candidates_integrated.csv')}
D={d['id']:d for d in rd('integrated_v1/disputes_integrated.csv')}
S={s['id']:s for s in rd('integrated_v1/states_integrated.csv')}
SD={d['id']:d for d in rd('tables/disputes_scenedetect.csv')}
H=['id','kind','note','start','end','first_verdict','first_type','first_desc','first_conf','machine_cls','evidence']
plan=rd('v2_scripts/second_pass_plan.csv')
for r in sys.argv[1:]:
    rows=[]
    for p in plan:
        if p['reviewer_shard']!=r:continue
        i,k,n=p['id'],p['kind'],p['note']
        if k=='candidate':
            c=C[i];rows.append([i,k,n,c['start'],c['end'],c['verdict'],c['type'],c['desc'],c['confidence'],c['machine_cls'],c['evidence']])
        elif k=='dispute':
            d=D[i];f=SD[i]['cut_frame'];ev='disputes/%s.jpg'%i
            rows.append([i,k,n,f,f,d['verdict'],'SCENEDETECT_CUT',d['desc'],d['confidence'],'matches:'+d['matches_candidate'],ev])
        elif k=='unowned':
            a,b=i[1:].split('-');rows.append([i,k,n,a,b,'UNOWNED','',"unowned interval; no first-pass description",'','',''])
        elif k=='merge':
            s=S[i];rows.append([i,k,n,s['start'],s['end'],'MERGE_WITH_PREV','', s['story_function'],s['confidence'],'',s['rep_image']])
    os.makedirs('agents/second_pass/'+r,exist_ok=True)
    csv.writer(open('agents/second_pass/%s/items.csv'%r,'w',newline='')).writerows([H]+rows)
    print(r,len(rows))
