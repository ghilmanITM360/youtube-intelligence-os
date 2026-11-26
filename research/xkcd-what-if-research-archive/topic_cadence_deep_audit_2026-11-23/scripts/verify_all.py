import csv,openpyxl,datetime as dt,random,json,collections,os
os.chdir(os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-23-what-if-topic-cadence-deep-audit'))
R=[]
def chk(n,ok,d): R.append((n,'PASS' if ok else 'FAIL',d)); print(('PASS' if ok else 'FAIL'),n,d)
o=list(csv.DictReader(open('ORIGINAL_CALENDAR_AUDIT.csv')))
c=collections.Counter(x['slot_class'] for x in o)
chk('original slots',c['LONG']==10 and c['SHORT']==13 and c['REST']==5 and c['EVAL']==2,dict(c))
s=list(csv.DictReader(open('PROPOSED_60_DAY_ORDER.csv'))); cs=collections.Counter(x['type'] for x in s)
chk('schedule 60 rows',len(s)==60,dict(cs))
wb=openpyxl.load_workbook('PROPOSED_60_DAY_ORDER.xlsx'); ws=wb['New recommended']
chk('xlsx==csv schedule',[[str(c.value or '') for c in r] for r in ws.iter_rows(min_row=2)]==[[x[k] for k in s[0]] for x in s],'cell-by-cell')
cand=list(csv.DictReader(open('TOPIC_RESEARCH_CANDIDATES.csv')))
chk('every decision has evidence id',all(x['evidence_ids'] for x in cand),len(cand))
chk('scored totals reproduce',all(x['total_0_100']=='UNSCORED' or abs(float(x['total_0_100'])-sum(w*int(v)/3 for w,v in zip([20,15,20,15,10,10,10],x['score_O_P_S_F_V_E_C'].split())))<=0.5 for x in cand),'weights 20/15/20/15/10/10/10')
orig_ids={x['bank_id'] for x in o if x['slot_class'] in('LONG','SHORT') and x['bank_id']!='Chosen Day 14'}; cid={x['candidate_id'] for x in cand}
chk('every original bank id traced to a candidate decision',orig_ids<=cid,sorted(orig_ids-cid))
inv=list(csv.DictReader(open('UPLOAD_INVENTORY.csv')))
chk('inventory unique keys',len({(x['channel_id'],x['video_id']) for x in inv})==len(inv),len(inv))
chk('inventory all rows have exact timestamp',all(x['published_at'] for x in inv),'')
# recompute 25 random cadence cells from inventory
T=dt.datetime.fromisoformat('2026-11-23T21:33:37.559614+05:00'); cad=list(csv.DictReader(open('CHANNEL_UPLOAD_CADENCE.csv')));random.seed(1); bad=0
for x in random.sample([y for y in cad if y['format'] in('Long','Short')],25):
    lo=T-dt.timedelta(days=int(x['window_days']))
    n=sum(1 for i in inv if i['channel_id']==x['channel_id'] and i['format']==x['format'] and lo<dt.datetime.fromisoformat(i['published_utc'])<=T)
    bad+= n!=int(x['count_observed'])
chk('25 random cadence cells recomputed',bad==0,f'mismatches={bad}')
ev=list(csv.DictReader(open('TOPIC_RESEARCH_EVIDENCE.csv'))); chk('evidence rows = raw search rows',len(ev)==sum(1 for _ in open('raw/search_raw.jsonl')),len(ev))
chk('unknown not zero: views are numeric (observed) or UNAVAILABLE, never blank/0 placeholders',all((e['views'].isdigit() and e['metadata_status'].startswith('OBSERVED')) or e['views'].startswith('UNAVAILABLE') for e in ev),sum(1 for e in ev if e['views'].startswith('UNAVAILABLE')))
json.dump(R,open('raw/verify_results.json','w'))
