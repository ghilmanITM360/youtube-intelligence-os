import csv,json,sqlite3,hashlib,zipfile,sys
W='/Users/ghilmankhan/workprojects/yios-finance-machine-a'
B=W+'/research/finance-economics-intelligence/'
vid=sys.argv[1]; out=sys.argv[2]
m={r['Video_ID']:r for r in csv.DictReader(open(B+'VIDEO_MASTER.csv'))}
r=m[vid]; print(json.dumps(r,indent=0))
t={x['Video_ID']:x for x in csv.DictReader(open(B+'TRANSCRIPT_COVERAGE.csv'))}[vid]; print(json.dumps(t))
th={x['Video_ID']:x for x in csv.DictReader(open(B+'THUMBNAIL_COVERAGE.csv'))}[vid]; print(json.dumps(th))
for p in r['Peer_Video_IDs'].split('|'):
    q=m[p]; print(p,q['Views'],q['Age_days'],q['Format'],q['Metric_snapshot_date'],q['Performance_tier'],q['Title'])
con=sqlite3.connect(f'file:{W}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
text=con.execute('select transcript_text from transcripts where youtube_video_id=?',(vid,)).fetchone()[0]
print('chars',len(text),'bytes',len(text.encode()),'words',len(text.split()),'sha',hashlib.sha256(text.encode()).hexdigest())
print(dict(zip(['likes','comments','published'],con.execute('select likes,comments,published_at from videos where youtube_video_id=?',(vid,)).fetchone())))
a,_,mem=t['Evidence_locator'].partition('::')
ab=open(W+'/'+a,'rb').read(); zb=zipfile.ZipFile(W+'/'+a).read(mem)
print('archive',hashlib.sha256(ab).hexdigest(),'member',hashlib.sha256(zb).hexdigest(),len(zb),len(zb.splitlines()))
print('contained', ' '.join(text.split()) in ' '.join(zb.decode('utf-8','replace').split()))
open(out,'w').write(text)
