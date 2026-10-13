"""Reproduce the saved-snapshot playbook analysis; never fetch or alter source evidence."""
import csv
import hashlib
import json
import math
import random
import re
import statistics as st
from collections import Counter
from datetime import datetime
from pathlib import Path

SOURCE = Path('data/extracted/forensic-analysis/casually-finance/2026-10-12')
OUT = Path('research/casually-finance-success-playbook')
TOPICS = {
 'roe3SgezmmU':'Markets','Uumnx2Fo6cE':'Real estate','xtqbRt94TTw':'Corporate finance',
 'DgbHW0IqHrI':'Debt','0ll9rEtoRrs':'Interest rates','OC1yu0L7jT4':'Macroeconomics',
 'CxclJzssUoc':'Corporate finance','HXlcMbxzz0U':'Corporate finance','kW48sP3rb2o':'Interest rates',
 'JZDpLZG2r6Y':'Markets','2J2Fb1bBufA':'Corporate finance','-RMZszjZSNE':'Macroeconomics',
 'YEhsWyY_WKQ':'Corporate finance','-X6YzlY_8tM':'Corporate finance','WCS1bK3KB3U':'Markets',
 'gG239LrksH4':'Macroeconomics','yViMyIVOHkQ':'Macroeconomics','Xkk9GnnJHBg':'Macroeconomics',
 'dPoDyl9Ys38':'Crypto','5umJ63d3rzQ':'Interest rates','KTnp2OlQJHA':'Personal finance',
 'RXFBHYxyqdk':'Markets','965yZYhY_f4':'Personal finance','Im-N3K9Pnf0':'Macroeconomics',
 'eePIUX0Sd6c':'Markets','IcxhABuHITM':'Debt','7K991LgY3tc':'Debt','hbsYaLaN_F8':'Crypto',
 '7uu6qaCGZsY':'Corporate finance','DKyJABtbF2o':'Historical financial stories',
 'kwMHrTFCWUE':'Personal finance','dlBhLhn8lL0':'Crypto','o3FQcd91MIs':'Personal finance'}
FEATURES = {
 'CURIOSITY_GAP':r'why|secret|hidden|nobody|quietly|something|not why|worse than|off about',
 'CONTRADICTION':r'but|except|not for|scam|safest.*breaking|boring.*bursts|bad.*up|save.*break|dumbest.*win',
 'HIDDEN_MECHANISM':r'hidden|secret|quietly|nobody|behind|not why|plain sight',
 'FEAR_CONSEQUENCE':r'crisis|crash|break|debt|trap|fail|scam|impact|drowning|bubble|worse|stop|monster',
 'EXPLANATORY_QUESTION':r'^why\b|^how\b|\?|^wtf\b',
 'NUMERIC_SPECIFICITY':r'\d',
 'NAMED_INSTITUTION':r'fed\b|federal reserve|bank of japan|spacex|nasdaq|microstrategy|redfin|wall street|goldman|blackrock',
 'TIMELINESS':r'\b202[4-6]\b|new |just |about to|already|last month|today',
 'PERSONAL_STAKES':r'\byou\b|your |mortgage|house|home|retire|401|investor|saving|money',
 'EMOTIONAL_FRAMING':r'wtf|scam|dumbest|smartest|garbage|trap|worse|monster|impact|crisis',
 'ELLIPSIS':r'\.\.\.|…',
 'PARENTHESIS':r'[()]',
 'COLON':r':',
}

def deduplicate(rows):
    found = {}
    for row in rows:
        vid = row['video_id']
        if vid in found and found[vid] != row:
            raise ValueError(f'Conflicting duplicate: {vid}')
        found[vid] = row
    return list(found.values())

def tier(ratio):
    for threshold, label in [(4,'BREAKOUT'),(2,'TOP_PERFORMER'),(1.25,'ABOVE_BASELINE'),(.8,'TYPICAL'),(.5,'BELOW_BASELINE')]:
        if ratio >= threshold:
            return label
    return 'UNDERPERFORMER'

def peers_for(row, rows):
    eligible = [x for x in rows if x['video_id'] != row['video_id'] and x['format_class'] == row['format_class'] and x['age'] >= 7]
    eligible.sort(key=lambda x:(abs(math.log(x['age']/row['age'])),x['video_id']))
    close = [x for x in eligible if .5 <= x['age']/row['age'] <= 2]
    if len(close) >= 5:
        return close[:12], 'AGE_CALIPER'
    return eligible[:8], 'WIDE_AGE_FALLBACK'

def topic(row):
    if row['video_id'] in TOPICS:
        return TOPICS[row['video_id']], 'ANALYST_LONG_FORM_ASSIGNMENT'
    t = row['title'].lower()
    rules = [ ('Real estate',r'hous|home|mortgage|rent|real estate'),
      ('Crypto',r'bitcoin|crypto|microstrategy|dogecoin'),
      ('Corporate finance',r'ipo|spacex|private credit|company|companies|corporate|ai |\bai\b|nvidia|openai'),
      ('Interest rates',r'bond|yield|interest|rate|inflation|\bfed\b'),
      ('Debt',r'debt|deficit|treasury|borrowing'),
      ('Policy',r'government|congress|tariff|tax|bailout'),
      ('Historical financial stories',r'1973|1929|2008|history'),
      ('Markets',r'stock|market|gold|trading|wall street'),
      ('Personal finance',r'invest|money|retire|401|saving|wealth|rich'),
      ('Macroeconomics',r'econom|japan|recession|dollar|oil')]
    for label, rule in rules:
        if re.search(rule,t): return label,'TITLE_KEYWORD_HEURISTIC'
    return 'Other observed categories','TITLE_KEYWORD_HEURISTIC_UNRESOLVED'

def read(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig')))

def image_present(path):
    return path.is_file() and path.read_bytes()[:3] == b'\xff\xd8\xff'

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    sourcefile = SOURCE/'01_CHANNEL_METADATA/all-videos-metadata.csv'
    raw = read(sourcefile)
    rows = deduplicate(raw)
    assert len(rows) == 206, 'Coverage changed: review before rerunning'
    qa = {r['video_id']:r for r in read(SOURCE/'07_VALIDATION/VIDEO_QA_COMPLETION_MATRIX.csv')}
    for r in rows:
        r['age']=(datetime.fromisoformat(r['collected_at'].replace('Z','+00:00'))-datetime.fromisoformat(r['published_at'])).total_seconds()/86400
        assert r['age']>0
        r['vpd']=int(r['views'])/r['age']
    output=[]
    for r in rows:
        thumb=SOURCE/f"02_VIDEO_FORENSICS/{r['video_id']}/evidence/thumbnail_maxresdefault.jpg"
        family,assignment=topic(r)
        base={ 'Video_ID':r['video_id'],'URL':r['watch_url'],'Title':r['title'],'Publish_Date':r['published_at'],
          'Public_Views':r['views'],'Snapshot_Date':r['collected_at'],'Snapshot_ID':r['snapshot'],
          'Duration_Sec':r['duration_sec'],'Format':r['format_class'],'Age_Days':round(r['age'],5),
          'Views_Per_Day':round(r['vpd'],3),'Topic_Family':family,'Topic_Assignment':assignment,
          'Original_Topic_Label':r['topic_derived_heuristic'],
          'Content_Format': 'SELECTED_EXPLAINER_ASR_VISUAL' if r['video_id'] in qa and qa[r['video_id']]['structural_qa']=='COMPLETE_VERIFIED' else 'UNVERIFIED_METADATA_ONLY',
          'Thumbnail_Reference':str(thumb) if image_present(thumb) else 'THUMBNAIL_VISUAL_UNAVAILABLE',
          'Thumbnail_URLs_Metadata_Only':r['thumbnail_urls'],
          'Research_Coverage':qa[r['video_id']]['structural_qa'] if r['video_id'] in qa else 'METADATA_ONLY',
          'Title_Chars':len(r['title']),'Title_Words':len(re.findall(r"\b[\w’']+\b",r['title'])),
          'Title_Features':';'.join(name for name,pattern in FEATURES.items() if re.search(pattern,r['title'],re.I)),
          'Peer_Mode':'LAUNCH_WINDOW','Peer_Count':0,'Peer_IDs':'','Peer_Min_Age_Days':'','Peer_Max_Age_Days':'',
          'Peer_Median_Views_Per_Day':'','Performance_Ratio':'','Tier':'INSUFFICIENT_DATA',
          'Baseline_Bootstrap_P05':'','Baseline_Bootstrap_P95':'','Ratio_Bootstrap_Low':'','Ratio_Bootstrap_High':'',
          'Bootstrap_Tier_Agreement':'','Raw_Views_Format_Percentile':'','VPD_Format_Percentile':'',
          'Confidence':'INSUFFICIENT_LAUNCH_LT_7_DAYS'}
        group=[x for x in rows if x['format_class']==r['format_class'] and x['age']>=7]
        if r['age']>=7 and len(group)>=6:
            peers,mode=peers_for(r,rows)
            baseline=st.median(x['vpd'] for x in peers)
            ratio=(r['vpd']+1)/(baseline+1)
            rng=random.Random(r['video_id'])
            samples=sorted(st.median(rng.choices([x['vpd'] for x in peers],k=len(peers))) for _ in range(1000))
            low,high=samples[49],samples[949]
            agreement=sum(tier((r['vpd']+1)/(v+1))==tier(ratio) for v in samples)/len(samples)
            base.update(Peer_Mode=mode,Peer_Count=len(peers),Peer_IDs=';'.join(x['video_id'] for x in peers),
              Peer_Min_Age_Days=round(min(x['age'] for x in peers),3),Peer_Max_Age_Days=round(max(x['age'] for x in peers),3),
              Peer_Median_Views_Per_Day=round(baseline,3),Performance_Ratio=round(ratio,4),Tier=tier(ratio),
              Baseline_Bootstrap_P05=round(low,3),Baseline_Bootstrap_P95=round(high,3),
              Ratio_Bootstrap_Low=round((r['vpd']+1)/(high+1),4),Ratio_Bootstrap_High=round((r['vpd']+1)/(low+1),4),
              Bootstrap_Tier_Agreement=agreement,
              Raw_Views_Format_Percentile=round(sum(int(x['views'])<=int(r['views']) for x in group)/len(group),4),
              VPD_Format_Percentile=round(sum(x['vpd']<=r['vpd'] for x in group)/len(group),4),
              Confidence='MODERATE_DESCRIPTIVE' if mode=='AGE_CALIPER' and agreement>=.8 else 'LOW_BASELINE_SENSITIVE')
        output.append(base)
    with (OUT/'VIDEO_PERFORMANCE.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(output[0]));writer.writeheader();writer.writerows(output)
    summaries={}
    for kind in ['LONG_FORM','SHORT']:
        group=[x for x in output if x['Format']==kind]
        aged=[x for x in group if x['Tier']!='INSUFFICIENT_DATA']
        features={}
        for feature in FEATURES:
            yes=[x for x in aged if feature in x['Title_Features'].split(';')]
            no=[x for x in aged if x not in yes]
            features[feature]={'n':len(yes),'median_ratio':st.median(x['Performance_Ratio'] for x in yes) if yes else None,
               'without_n':len(no),'without_median_ratio':st.median(x['Performance_Ratio'] for x in no) if no else None,
               'tiers':dict(Counter(x['Tier'] for x in yes)),
               'examples':[{k:x[k] for k in ['Video_ID','Title','Publish_Date','Tier','Performance_Ratio']} for x in sorted(yes,key=lambda x:x['Performance_Ratio'],reverse=True)[:2]+sorted(yes,key=lambda x:x['Performance_Ratio'])[:2]]}
        topics={t:{'n':len(g),'median_ratio':st.median(x['Performance_Ratio'] for x in g), 'tiers':dict(Counter(x['Tier'] for x in g))} for t in sorted({x['Topic_Family'] for x in aged}) if (g:=[x for x in aged if x['Topic_Family']==t])}
        summaries[kind]={'n':len(group),'aged_n':len(aged),'median_views':st.median(int(x['Public_Views']) for x in group),
          'aged_median_vpd':st.median(x['Views_Per_Day'] for x in aged),'tiers':dict(Counter(x['Tier'] for x in group)),
          'features':features,'topics':topics,'top_by_ratio':sorted(aged,key=lambda x:x['Performance_Ratio'],reverse=True)[:5],
          'bottom_by_ratio':sorted(aged,key=lambda x:x['Performance_Ratio'])[:5]}
    (OUT/'ANALYTICS_SUMMARY.json').write_text(json.dumps(summaries,indent=2)+'\n')
    sources=[sourcefile,SOURCE/'01_CHANNEL_METADATA/metadata-coverage.json',SOURCE/'01_CHANNEL_METADATA/channel-metadata.json']
    sources+=list((SOURCE/'03_MASTER_DATA').glob('MASTER_*.csv'))
    sources+=list((SOURCE/'04_PRODUCTION_DNA').glob('*.md'))+list((SOURCE/'05_PATTERNS_AND_BLUEPRINTS').glob('*.md'))
    sources+=[SOURCE/'07_VALIDATION'/n for n in ['VIDEO_QA_COMPLETION_MATRIX.csv','MOTION_QA_DISPOSITION.csv','FINANCE_CLAIM_VERIFICATION.csv','MOBILE_THUMBNAIL_QA.md','NEW_MAC_TARGETED_VISUAL_QA_2026-10-12.json']]
    sources+=list((SOURCE/'02_VIDEO_FORENSICS').glob('*/evidence/thumbnail_maxresdefault.jpg'))
    manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    (OUT/'SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'unique_uploads':len(output),'by_format':{k:{s:v[s] for s in ['n','aged_n','tiers']} for k,v in summaries.items()},'thumbnail_images':sum(x['Thumbnail_Reference']!='THUMBNAIL_VISUAL_UNAVAILABLE' for x in output),'source_hashes':len(manifest)},indent=2))

if __name__ == '__main__':
    main()
