import json,sys,time,collections
from pathlib import Path
r=json.load(open(Path(sys.argv[0]).parent/'stream_compare.json'))
for n,lim,excl in [('PrimitiveEducation',60,('videos/',)),('xkcd',40,('videos/','census/')),('CF-V003-5umJ',45,('agents','tables/')),('CF-V005-X6Yz',8,('agents',)),('CF-V006-xtqb',45,('agents','session_20261103')),('CF-V006-EP0002',20,()),('CF-V006-progress',25,()),('CF-35target',14,()),('7ch-readiness',25,())]:
    a=sorted(r[n]['absent'],key=lambda x:-x[2]); print(f'\n== {n} absent {len(a)}')
    for p,s,m in [x for x in a if not x[0].startswith(excl)][:lim]: print(time.strftime('%m-%dT%H:%M',time.gmtime(m)),s,p)
    c=collections.Counter('/'.join(x[0].split('/')[:2]) for x in a if x[0].startswith(excl)); print(' grouped',c.most_common(6))
