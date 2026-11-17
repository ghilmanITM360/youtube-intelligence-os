import csv,json,sys,os,collections
V={"CONFIRMED","RECLASSIFIED","NOT_A_CHANGE","CODEC_ARTIFACT","UNVERIFIED","SPLIT","NO_SPLIT"}
K=["id","independent_verdict","state_boundary","correction","confidence","frames_viewed","viewing","remaining_uncertainty","desc"]
def check(r,out=None,items=None):
    items=items or f'agents/second_pass/{r}/items.csv';out=out or f'agents/second_pass/{r}/OUT_{r}.json'
    ids=[x['id'] for x in csv.DictReader(open(items))];j=json.load(open(out));e=[]
    if j.get('shard')!=r:e.append('shard')
    got=[x.get('id') for x in j['items']]
    if got!=ids:e.append('ids/order')
    for x in j['items']:
        for k in K:
            if k not in x:e.append(f"{x.get('id')} missing {k}")
        if x.get('independent_verdict') not in V:e.append(f"{x.get('id')} verdict")
    return e,collections.Counter(x['independent_verdict'] for x in j['items'])
if __name__=='__main__':
    bad=0
    for r in (sys.argv[1:] or ('R04','R05','R06')):
        e,c=check(r);print(r,'ERR' if e else 'OK',e[:5],dict(c));bad+=bool(e)
    # negative test: truncated output must fail
    j=json.load(open('agents/second_pass/R05/OUT_R05.json'));j['items']=j['items'][:-1];json.dump(j,open('/tmp/_neg.json','w'))
    e,_=check('R05','/tmp/_neg.json');print('negative test fails as expected:',bool(e));os.remove('/tmp/_neg.json')
    sys.exit(bad)
