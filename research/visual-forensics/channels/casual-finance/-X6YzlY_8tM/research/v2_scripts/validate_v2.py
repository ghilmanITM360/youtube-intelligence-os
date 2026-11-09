import csv,json,os,sys,collections
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
def run(P='integrated_v2/'):
    rd=lambda n:list(csv.DictReader(open(P+n)));e=[]
    seg=rd('frame_partition_v2.csv');N=21410;pos=0
    for s in seg:
        a,b=int(s['start']),int(s['end'])
        if a!=pos:e.append(f'tiling break at {pos} vs {a}')
        if s['kind']=='UNACCOUNTED':e.append(f'unaccounted {a}-{b}')
        pos=b+1
    if pos!=N:e.append(f'covers {pos} not {N}')
    st={s['id'] for s in csv.DictReader(open('integrated_v1/states_integrated.csv'))}
    own={s['owner'] for s in seg}
    if not st<=own:e.append('state missing from partition')
    comp=rd('composition_groups_v2.csv');mem=[m for c in comp for m in c['members'].split(';')]
    if sorted(mem)!=sorted(st):e.append('composition membership != states')
    mr=rd('merge_rulings_v2.csv')
    if any(m['final_ruling_v2']=='UNRULED' for m in mr):e.append('unruled merge')
    gaps=rd('gaps_v2.csv')
    if any(g['status']=='NOT_SECOND_PASSED' for g in gaps):e.append('unreviewed gap')
    cand=rd('candidates_v2.csv');ids=[c['id'] for c in cand]
    if len(ids)!=len(set(ids)):e.append('dup candidate')
    led={r['id'] for r in rd('second_pass_ledger.csv')}
    if len(led)!=821:e.append('ledger != 821')
    for c in cand:
        if c['final_status']=='SECOND_PASSED' and c['id'] not in led:e.append('ref '+c['id'])
    return e
if __name__=='__main__':
    e=run();print('POSITIVE',e or 'PASS')
    import shutil,tempfile
    t=tempfile.mkdtemp()+'/';shutil.copytree('integrated_v2',t,dirs_exist_ok=True)
    def neg(name,fn):
        shutil.copytree('integrated_v2',t,dirs_exist_ok=True);fn();r=run(t);print('NEG',name,'DETECTED' if r else 'MISSED')
    def dropseg():
        L=list(csv.DictReader(open(t+'frame_partition_v2.csv')));L.pop(5);csv.DictWriter(open(t+'frame_partition_v2.csv','w',newline=''),L[0].keys()).writerows([dict(zip(L[0],L[0]))]+L)
    neg('drop_partition_row',dropseg)
    def dupc():
        L=list(csv.DictReader(open(t+'candidates_v2.csv')));L.append(L[0]);w=csv.DictWriter(open(t+'candidates_v2.csv','w',newline=''),L[0].keys());w.writeheader();w.writerows(L)
    neg('dup_candidate',dupc)
    def unr():
        L=list(csv.DictReader(open(t+'merge_rulings_v2.csv')));L[0]['final_ruling_v2']='UNRULED';w=csv.DictWriter(open(t+'merge_rulings_v2.csv','w',newline=''),L[0].keys());w.writeheader();w.writerows(L)
    neg('unruled_merge',unr)
    def dropmem():
        L=list(csv.DictReader(open(t+'composition_groups_v2.csv')));L.pop(3);w=csv.DictWriter(open(t+'composition_groups_v2.csv','w',newline=''),L[0].keys());w.writeheader();w.writerows(L)
    neg('drop_composition',dropmem)
    sys.exit(bool(e))
