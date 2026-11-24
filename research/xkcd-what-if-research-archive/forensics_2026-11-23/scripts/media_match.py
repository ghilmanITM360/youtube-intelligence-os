import csv,os,re,glob,subprocess,json,collections
R='/Users/ghilmanislam360/Documents/youtube-intelligence-os/'
cen={r['video_id']:r for r in csv.DictReader(open(R+'research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv'))}
D='/Users/ghilmanislam360/Documents/YIOS-Media-Library/xkcd Channel/'
fs=sorted(os.listdir(D)); print('entries',len(fs))
ext=collections.Counter(os.path.splitext(f)[1] for f in fs);print(ext)
byid=collections.defaultdict(list);unm=[]
for f in fs:
    m=re.search(r'\[([A-Za-z0-9_-]{11})\]',f)
    if m: byid[m.group(1)].append(f)
    else: unm.append(f)
vid=[i for i in byid if i in cen]; print('files w/ id',sum(len(v) for v in byid.values()),'distinct ids',len(byid),'in census',len(vid),'not in census',[i for i in byid if i not in cen],'no-id files',unm[:10])
mp4=[i for i in vid if any(f.endswith('.mp4') for f in byid[i])]
print('census ids with mp4 on this machine',len(mp4),'of',len(cen))
for k in ('LONG_FORM','SHORT'):
    have=[i for i in mp4 if cen[i]['format_class']==k]; allk=[i for i in cen if cen[i]['format_class']==k]
    print(k,len(have),'of',len(allk))
print('missing media:',[(i,cen[i]['format_class'],cen[i]['title'][:40]) for i in cen if i not in mp4])
print('dups (id with >1 file):',{i:v for i,v in byid.items() if len(v)>1})
tot=sum(os.path.getsize(D+f) for f in fs);print('total GB',tot/1e9)
