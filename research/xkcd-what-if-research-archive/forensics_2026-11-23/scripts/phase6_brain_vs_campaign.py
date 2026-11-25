"""Brain (14 videos, MASTER_SHOTS.jsonl) vs campaign (shot_ledger.csv) on the SAME video IDs. Read-only."""
import csv, json, statistics as st, collections
P='/Users/ghilmanislam360/Documents/youtube-intelligence-os/'
J=[json.loads(l) for l in open(P+'data/raw/forensic-analysis/preserved-worktree-evidence-2026-10-21/evidence/what-if-forensic/data/staging/what-if-forensic/v1.0.0/MASTER_SHOTS.jsonl')]
B=collections.defaultdict(list)
for r in J:
    f=r['source_fields']
    try: B[r['canonical_youtube_video_id']].append(float(f['DURATION_SEC']))
    except Exception: pass
allb=[d for v in B.values() for d in v]
print('Brain shots rows',len(J),'with duration',len(allb),'videos',len(B),'median',round(st.median(allb),2),'min/max',min(allb),max(allb))
T={r['video_id']:r for r in csv.DictReader(open('06_ALIGNED_TIMING_TABLE.csv'))}
out=[]
for v,d in sorted(B.items()):
    c=T.get(v)
    out.append(dict(video_id=v,brain_shots=len(d),brain_median_shot_s=round(st.median(d),2),brain_total_s=round(sum(d),1),
        campaign_shots=c['shots'] if c else '',campaign_median_shot_s=c['median_shot_s'] if c else '',campaign_duration_s=c['duration_s'] if c else '',in_campaign_ledgers='YES' if c else 'NO'))
with open('06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
for o in out: print(o)
sh=[o for o in out if o['in_campaign_ledgers']=='YES']
print('shared with campaign ledgers',len(sh))
if sh:
    ratios=[o['brain_shots']/int(o['campaign_shots']) for o in sh]
    print('brain/campaign shot-count ratio median',round(st.median(ratios),2),'min',round(min(ratios),2),'max',round(max(ratios),2))
