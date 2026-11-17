import json,sys,re,collections
p=sys.argv[1]; uses={}; res={}
for line in open(p):
    try: d=json.loads(line)
    except: continue
    m=d.get('message') or {}
    c=m.get('content')
    if not isinstance(c,list): continue
    for b in c:
        if not isinstance(b,dict): continue
        if b.get('type')=='tool_use' and b.get('name')=='Read':
            fp=(b.get('input') or {}).get('file_path','')
            if re.search(r'\.(png|jpe?g|webp|gif)$',fp,re.I): uses[b['id']]=(fp,d.get('timestamp'))
        if b.get('type')=='tool_result' and b.get('tool_use_id') in uses or (b.get('type')=='tool_result'):
            cc=b.get('content'); kinds=[]; txt=''
            if isinstance(cc,list):
                for x in cc:
                    kinds.append(x.get('type'));
                    if x.get('type')=='text': txt+=x.get('text','')[:120]
            elif isinstance(cc,str): kinds=['str']; txt=cc[:120]
            res[b.get('tool_use_id')]=(kinds,txt)
n=collections.Counter()
for k,(fp,ts) in uses.items():
    kinds,txt=res.get(k,(['MISSING'],''))
    ok='image' in kinds; n[ok]+=1
    print(ts, 'IMAGE' if ok else 'NOIMG', fp.split('primitive-education/')[-1], '' if ok else repr(txt))
print('TOTAL',dict(n))
