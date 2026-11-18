# Tag xkcd What If census videos into micro-niches; outlier = views / median views of the 6 nearest same-format videos by publish date.
import json,sys,statistics as st,datetime as dt
from collections import defaultdict,Counter
# usage: python3 niches.py <census.csv> <out_dir>
import csv
CSV,S=sys.argv[1],sys.argv[2]; snap=dt.datetime(2026,11,4,tzinfo=dt.timezone.utc); rows=[]
for x in csv.DictReader(open(CSV)):
  p=dt.datetime.fromisoformat(x['publish_datetime']); age=(snap-p).days
  v=int(x['views_player']) if x['views_player'].isdigit() else None
  rows.append([x['format_class'],x['video_id'],x['publish_datetime'][:10],age,int(x['duration_s'] or 0),v,round(v/age) if v and age else None,x['title']])
N={ # video_id -> niche (assigned by reading titles + transcripts; see report for rules)
'gp5G1QG6cXc':'Planet-scale Earth changes','19gun1mffWs':'Planet-scale Earth changes','ERieN5pee7A':'Planet-scale Earth changes','WH4g1ptJ-70':'Planet-scale Earth changes','zJNmUWZXj2M':'Planet-scale Earth changes','XvvXDEtMfhw':'Planet-scale Earth changes','U4cONnQxgvo':'Planet-scale Earth changes','GgEGcxJRDik':'Planet-scale Earth changes','-1-ldW4kpLM':'Planet-scale Earth changes','5k8ciEx__5w':'Planet-scale Earth changes','e3uk7jU3RHo':'Planet-scale Earth changes','wBLVmEZV2Oc':'Planet-scale Earth changes','FKXVs4UteSc':'Planet-scale Earth changes','p2M8Y0z9Rl0':'Planet-scale Earth changes','Ny9m2l6h478':'Planet-scale Earth changes',
'Jpy55EgMQgY':'Oceans & water','aMshLs0YCTQ':'Oceans & water','FkUNHhVbQ1Q':'Oceans & water','2p305nzcVQE':'Oceans & water','4ZVtHknKuvg':'Oceans & water','0EytSWiKrFg':'Oceans & water','FYoHYq8VRt0':'Oceans & water','alkJ7xScBiw':'Oceans & water','pfbzrrcQZjs':'Oceans & water','QZIEjvSlOMQ':'Oceans & water',
'UXA-Af-JeCE':'Sun & stellar extremes','m1aMh7z8Y7I':'Sun & stellar extremes','X7sbn9LMZOg':'Sun & stellar extremes','n_KUCunjMwQ':'Sun & stellar extremes','qu8nx1qUwEU':'Sun & stellar extremes','sFTRRdHqZIQ':'Space & orbit','EsUBRd1O2dU':'Space & orbit','2LSyizrk8-0':'Space & orbit','TgA0lXEW7dw':'Space & orbit','i6e4NnFnQi0':'Space & orbit',
'JqFSGkFPipM':'Moon','jgafb8G7i4o':'Moon','aIIBBj6KR-Y':'Moon','mtTbwHzhUiM':'Moon','UQgw50GQu1A':'Moon','n2XRulD_IVs':'Moon','DiWFXv9N0Vs':'Moon','mEUqVgGf4e0':'Moon',
'TFhrRrRdUbA':'Exotic matter & particles','3EI08o-IGYk':'Exotic matter & particles','Uj10jGq2O8o':'Exotic matter & particles','EFRUL7vKdU8':'Exotic matter & particles','vBfR2Zb0dkc':'Exotic matter & particles','BnGqPxnQh9A':'Exotic matter & particles',
's3oLIDaElaE':'Human survival limits','35KZm1yiyIE':'Human survival limits','oTzW-mTQd5w':'Human survival limits','NxVdO7M2YdM':'Human survival limits','r7B0MzvwDcA':'Human survival limits','XwJAbyn5uGY':'Human survival limits','eSPcp-tfGbA':'Human survival limits','PUtI3xoaHx0':'Human survival limits','jjzYUOd5HAA':'Human survival limits','oBWqlxDd8sU':'Human survival limits',
'8fADp43wJwU':'Light & optics','kNry0bf7eC0':'Light & optics','BO8rOs05v48':'Light & optics','oLoxdLfB6Gs':'Light & optics','TIDHee_Q5Gk':'Light & optics','zgBTwtg7H8E':'Light & optics','xA9aqKGBeOs':'Light & optics','fs28lEq9smw':'Light & optics','_efsqO-4OoQ':'Light & optics',
'IdlQsjq5vKo':'Absurd engineering','WYf9-xfm6t8':'Absurd engineering','DDNMLh1I_jY':'Absurd engineering','Z_xJ40QXu7Q':'Absurd engineering','J-E8rjWR9rM':'Absurd engineering','oMtAHGv-DU4':'Absurd engineering','0L44GEJ5pLE':'Absurd engineering','X97DDWvxaqQ':'Absurd engineering','RgBYohJ7mIk':'Absurd engineering','WQTNLuhfkwk':'Absurd engineering','JcXpCyPc2Xw':'Absurd engineering','rgUfcFAPicY':'Absurd engineering','9VG0yqq_PHM':'Absurd engineering',
'lLlwvmu1ZeA':'Units, money & society','saj7b5C6TCM':'Units, money & society','jVy3qd70AqU':'Units, money & society','YL2VNtus4xk':'Units, money & society','pMMo3XvoKD4':'Units, money & society','d5TD3r1nLqM':'Units, money & society','U8F7UNK9jco':'Units, money & society','rGZ6TsXvi8E':'Units, money & society',
'SLd4hnmeW_g':'Weird & worrying compilations','alBQCm0QpJg':'Weird & worrying compilations',
}
missing=[r[1] for r in rows if r[1] not in N]; assert not missing, missing
for fmt in ['LONG_FORM','SHORT']:
  F=sorted([r for r in rows if r[0]==fmt and r[5]],key=lambda r:r[2])
  for i,r in enumerate(F):
    nb=sorted(F[:i]+F[i+1:],key=lambda q:abs((dt.date.fromisoformat(q[2])-dt.date.fromisoformat(r[2])).days))[:6]
    r.append(round(r[5]/st.median(q[5] for q in nb),2))
out=[]
for r in rows:
  out.append(dict(format=r[0],video_id=r[1],published=r[2],age_days=r[3],duration_s=r[4],views=r[5],views_per_day=r[6],title=r[7],outlier=r[8] if len(r)>8 else None,niche=N[r[1]]))
json.dump(out,open(S+'/xkcd_census_scored_2026-11-04.json','w'),indent=1)
print('niche summary (views at 2026-11-04 census; outlier = vs 6 nearest same-format neighbours)')
by=defaultdict(list)
for o in out:
  if o['views']: by[(o['niche'],o['format'])].append(o)
for k in sorted(by,key=lambda k:(k[1],-st.median(x['outlier'] for x in by[k]))):
  v=by[k]; print(f"{k[1][:5]} {k[0]:30} n={len(v):2} median_views={int(st.median(x['views'] for x in v)):>9,} median_outlier={st.median(x['outlier'] for x in v):.2f} hits>=1.5x={sum(x['outlier']>=1.5 for x in v)}")
for fmt,n in [('LONG_FORM',12),('SHORT',8)]:
  print('\nTOP',fmt,'by lifetime views'); 
  for o in sorted([o for o in out if o['format']==fmt and o['views']],key=lambda o:-o['views'])[:n]: print(f"  {o['views']:>10,} age={o['age_days']:4} out={o['outlier']:.2f} {o['video_id']} [{o['niche']}] {o['title']}")
  print('TOP',fmt,'by outlier score');
  for o in sorted([o for o in out if o['format']==fmt and o['views']],key=lambda o:-o['outlier'])[:n]: print(f"  {o['outlier']:.2f} {o['views']:>10,} age={o['age_days']:4} {o['video_id']} [{o['niche']}] {o['title']}")
# cadence
d=sorted(dt.date.fromisoformat(o['published']) for o in out)
gaps=[(b-a).days for a,b in zip(d,d[1:])]
print('\ncadence: uploads',len(d),'span',d[0],d[-1],'gap counter',Counter(gaps).most_common(6),'weekday',Counter(x.strftime('%a') for x in d))
for y in ['2023','2024','2025','2026']: print(y,Counter(o['format'] for o in out if o['published'].startswith(y)))
