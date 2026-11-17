"""Build blind opening packet (shuffled ids, first 60 words, no channel/title/views) + key; and score filled labels.
Usage: build -> python3 blind_opening_packet_2026-11-13.py build
       score -> python3 blind_opening_packet_2026-11-13.py score <labels.csv>  (cols: bid,label in STAKE|PERSONA|OTHER)"""
import csv,random,sys,math,collections
A='_analysis/'; L=A+'openings_labeled_2026-11-13.csv'
rows=list(csv.DictReader(open(L)))
if sys.argv[1]=='build':
    random.seed(20261113); random.shuffle(rows)
    with open(A+'blind_openings_PACKET_2026-11-13.csv','w',newline='') as f,open(A+'blind_openings_KEY_do_not_open_2026-11-13.csv','w',newline='') as k:
        w=csv.writer(f);kw=csv.writer(k);w.writerow(['bid','opening_60w','label']);kw.writerow(['bid','video_id','channel','views','rel','rule_lab'])
        for i,r in enumerate(rows):
            b=f'B{i:03d}';w.writerow([b,' '.join(r['opening_150w'].split()[:60]),''])
            kw.writerow([b,r['video_id'],r['channel'],r['views'],r['rel'],r['lab']])
    print('built',len(rows))
else:
    key={r['bid']:r for r in csv.DictReader(open(A+'blind_openings_KEY_do_not_open_2026-11-13.csv'))}
    lab={r['bid']:r['label'].strip().upper() for r in csv.DictReader(open(sys.argv[2]))}
    assert set(lab)==set(key) and set(lab.values())<={'STAKE','PERSONA','OTHER'},'bad labels'
    agree=sum(lab[b]==key[b]['rule_lab'] for b in key);print('agreement with rule label',agree,'/',len(key))
    by=collections.defaultdict(list)
    for b,r in key.items(): by[r['channel']].append((lab[b]=='STAKE',math.log(max(float(r['rel']),1e-6))))
    def stat(by):
        s=[x for v in by.values() for x in v if x[0]];n=[x for v in by.values() for x in v if not x[0]]
        return sum(x[1] for x in s)/len(s)-sum(x[1] for x in n)/len(n)
    obs=stat(by);random.seed(1);ge=0;N=5000
    for _ in range(N):
        sh={}
        for c,v in by.items():
            fl=[x[0] for x in v];random.shuffle(fl);sh[c]=[(f,y[1]) for f,y in zip(fl,v)]
        ge+=stat(sh)>=obs
    print('pooled STAKE-nonSTAKE mean log rel diff %.2f  p=%.4f'%(obs,(ge+1)/(N+1)))
