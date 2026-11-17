"""Rebuild matched descriptive summaries and sensitivity from saved research rows."""
from collections import defaultdict
from statistics import median

from build_baseline import BASE, compare, read_csv, write_csv


def main():
    raw = read_csv(BASE / 'VIDEO_MASTER.csv')
    videos = [dict(r, Views=int(r['Views']) if r['Views'] else None,
                   Age_days=float(r['Age_days']) if r['Age_days'] else '') for r in raw]
    by = {v['Video_ID']: v for v in videos}
    ranked = [v for v in videos if v['Performance_tier'] != 'INSUFFICIENT_DATA']
    sensitivity = []
    for v in ranked:
        peers = [by[x] for x in v['Peer_Video_IDs'].split('|')][:5]
        ratio = v['Views'] / v['Age_days'] / median(p['Views'] / p['Age_days'] for p in peers)
        tier = 'STRONG' if ratio >= 2 else 'WEAK' if ratio < .5 else 'TYPICAL'
        sensitivity.append(dict(Video_ID=v['Video_ID'],Primary_tier=v['Performance_tier'],
            Five_peer_ratio=round(ratio,5),Five_peer_tier=tier,Agrees=tier==v['Performance_tier']))
    write_csv('PERFORMANCE_SENSITIVITY.csv', sensitivity)
    date_sensitivity = []
    for delta in (-1,1):
        # Move the common snapshot for an entire cohort, keeping publication dates fixed.
        shifted = [dict(v,Age_days=v['Age_days']+delta if v['Age_days']!='' else '') for v in videos]
        for v in shifted:
            if v['Dataset'] != 'DS-000022':
                continue
            primary = by[v['Video_ID']]['Performance_tier']
            tier, count, ratio, peers, basis = compare(v,shifted)
            date_sensitivity.append(dict(Video_ID=v['Video_ID'],Snapshot_shift_days=delta,
                Primary_tier=primary,Shifted_tier=tier,Agrees=tier==primary,Peer_count=count,
                Ratio=ratio,Peer_Video_IDs=peers,Tier_basis=basis))
    write_csv('DATE_SENSITIVITY.csv',date_sensitivity)
    features = {r['Video_ID']: r for r in read_csv(BASE/'SCRIPT_FEATURES.csv')}
    titles = {r['Video_ID']: r for r in read_csv(BASE/'TITLE_FEATURES.csv')}
    groups = defaultdict(list)
    for v in ranked:
        groups[(v['Channel'],v['Format'],v['Performance_tier'])].append(v['Video_ID'])
    result=[]
    for (channel,fmt,tier), ids in sorted(groups.items()):
        ids=sorted(ids)
        row=dict(Channel=channel,Format=fmt,Tier=tier,N=len(ids),Video_IDs='|'.join(ids))
        for key in ['Word_count','Sentence_word_mean_proxy','Causal_marker_count','Example_marker_count','Transition_marker_count','CTA_marker_count']:
            values=[float(features[i][key]) for i in ids if i in features]
            row[key+'_median']=median(values) if values else ''
        for key in ['Question_opener','Numbers','Negative_tokens','Curiosity_tokens']:
            row[key+'_fraction_present']=sum(float(titles[i][key])>0 for i in ids)/len(ids)
        result.append(row)
    write_csv('FEATURE_COMPARISONS.csv',result)
    # Preserve selection identities; refresh derived values, not the sample design.
    sample_ids=[r['Video_ID'] for r in read_csv(BASE/'REVIEW_SAMPLE.csv')]
    raw_by={v['Video_ID']:v for v in raw}
    write_csv('REVIEW_SAMPLE.csv',[raw_by[i] for i in sample_ids])
    semantic=read_csv(BASE/'TITLE_SEMANTIC_REVIEWS.csv')
    for r in semantic:
        r['Performance_tier']=raw_by[r['Video_ID']]['Performance_tier']
    write_csv('TITLE_SEMANTIC_REVIEWS.csv',semantic)
    print({'ranked':len(ranked),'five_peer_agreements':sum(r['Agrees'] for r in sensitivity),
           'date_scenarios':len(date_sensitivity),'date_agreements':sum(r['Agrees'] for r in date_sensitivity)})


if __name__ == '__main__':
    main()
