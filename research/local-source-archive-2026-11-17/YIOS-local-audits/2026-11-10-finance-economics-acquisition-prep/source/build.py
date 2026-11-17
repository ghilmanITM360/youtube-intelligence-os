"""Finance+Economics re-scope: tranche lists, reuse gap-fill, proposed Actor inputs. No Apify calls."""
import csv, json, math, re
A='/Users/ghilmankhan/YIOS-local-audits/2026-11-10-stageA-channel-classification/'
S='/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/622c153f-af35-4a64-8794-cbc9a7c5edf5/scratchpad/finecon/'
PRICE=0.004  # live 2026-11-10, FREE tier 'result' event, live/actor.json
inc={x['canonical_channel_id']:x for x in csv.DictReader(open(A+'Incoming_Review.csv')) if x['primary_niche'] in ('FINANCE','ECONOMICS')}
q={x['canonical_channel_id']:x for x in csv.DictReader(open(A+'Apify_Queue.csv'))}
tabs={json.loads(l)['channel_id']:json.loads(l) for l in open(S+'tabs.jsonl')}
reuse={x['canonical_channel_id']:x for x in csv.DictReader(open(S+'REUSE_VERIFICATION.csv'))}
assert len(inc)==31 and set(tabs)==set(inc) and set(reuse)<=set(inc)
n_of=lambda s: int(re.sub(r'\D','',s) or 0)
rows=[]
for cid,x in inc.items():
    t=tabs[cid]['tabs']; sh='Shorts' in t; lv='Live' in t
    n=n_of(x['reported_videos_obs'])
    if cid in reuse:
        r=reuse[cid]; d=max(0,n-int(r['pkg_reported_videos']))
        member=cid=='UCiBGqUxeTe4AYQyRseSZaKw'   # PR #38: members-only rows interleave in the feed and are billed
        lim=d+5+(d if member else 0)
        tranche='G (gap-fill, newest-first delta)'; pkg=r['package']+f" snapshot {r['snapshot_utc']}"
        scope=f"uploads after package snapshot; live {n} vs package {r['pkg_reported_videos']} reported (+{d}); overlap rows confirm continuity"
        est_rows=lim
    else:
        lim=math.ceil(n*1.10)+5; d=''
        tranche='T1 (B1 subset)' if q[cid]['proposed_batch']=='B1' else 'T2 (follow-up)'
        pkg='none'; scope='full public metadata snapshot (all public uploads)'; est_rows=lim
    rows.append(dict(niche=x['primary_niche'],tranche=tranche,channel=x['live_title'],canonical_channel_id=cid,
        start_url=f'https://www.youtube.com/channel/{cid}',sub_niche=x['sub_niche'],subscribers_obs=x['subscribers_obs'],
        reported_videos_obs_2026_11_09=n,tabs_observed=';'.join(t),existing_package=pkg,
        maxResults_regular=lim,maxResultsShorts=lim if sh else 0,maxResultStreams=lim if lv else 0,
        est_billable_rows_max=est_rows,est_cost_usd=round(est_rows*PRICE,3),scope=scope,
        captions='NONE',ai_addons='off',media_download='none',approval_status='NOT_APPROVED'))
order={'T1 (B1 subset)':0,'T2 (follow-up)':1,'G (gap-fill, newest-first delta)':2}
rows.sort(key=lambda r:(order[r['tranche']],-r['reported_videos_obs_2026_11_09']))
F=list(rows[0])
for niche in ('FINANCE','ECONOMICS'):
    w=csv.DictWriter(open(S+f'out/{niche.title()}_List.csv','w',newline=''),fieldnames=F); w.writeheader(); w.writerows(r for r in rows if r['niche']==niche)
w=csv.DictWriter(open(S+'out/All_31_Targets.csv','w',newline=''),fieldnames=F); w.writeheader(); w.writerows(rows)
tot={}
for r in rows: tot.setdefault(r['tranche'],[0,0,0.0]); t=tot[r['tranche']]; t[0]+=1; t[1]+=r['est_billable_rows_max']; t[2]+=r['est_cost_usd']
# sanitized proposed Actor inputs (no token), one run per tranche; pilot first
def inp(rs, newest=False):
    i={"startUrls":[{"url":r['start_url']} for r in rs],"maxResults":max(r['maxResults_regular'] for r in rs),
       "maxResultsShorts":max(r['maxResultsShorts'] for r in rs),"maxResultStreams":max(r['maxResultStreams'] for r in rs),
       "transcriptionAndSubtitle":"NONE","aiVideoDescription":False,"aiVideoSummary":False}
    if newest: i["sortVideosBy"]="NEWEST"
    return i
by=lambda k:[r for r in rows if r['tranche']==k]
pilot=[r for r in rows if r['channel']=='Built On You']
plan={"note":"maxResults* are PER CHANNEL in streamers/youtube-scraper; channels with lower limits are split into their own run (see per_channel_runs) so no channel exceeds its approved limit.",
 "pilot":{"input":{**inp(pilot),"maxResults":3,"maxResultsShorts":0,"maxResultStreams":0},"maxTotalChargeUsd":0.05},
 "per_channel_runs":[{"tranche":r['tranche'],"channel":r['channel'],"input":inp([r],newest=r['tranche'].startswith('G'))} for r in rows]}
json.dump(plan,open(S+'out/PROPOSED_ACTOR_INPUTS_SANITIZED.json','w'),indent=1)
json.dump({k:{"channels":v[0],"max_billable_rows":v[1],"est_usd":round(v[2],3)} for k,v in tot.items()},open(S+'out/TRANCHE_TOTALS.json','w'),indent=1)
assert sum(v[0] for v in tot.values())==31
for k,v in tot.items(): print(k,v[0],v[1],round(v[2],3))
