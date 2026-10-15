"""Read-only validation of this bounded research checkpoint."""
import csv
import hashlib
import json
import sqlite3
import subprocess
from collections import Counter
from pathlib import Path
from statistics import median

from build_baseline import compare

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]


def rows(name):
    with (BASE/name).open(newline='') as stream:
        return list(csv.DictReader(stream))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    videos=rows('VIDEO_MASTER.csv');ids={r['Video_ID'] for r in videos}
    channels=rows('CANONICAL_CHANNELS.csv')
    assert len(videos)==len(ids)==966 and len(channels)==13
    assert len(rows('CHANNEL_UNIVERSE.csv'))==21
    assert all(v['Title'] for v in videos)
    for name in ['TITLE_FEATURES.csv','THUMBNAIL_COVERAGE.csv','TRANSCRIPT_COVERAGE.csv']:
        r=rows(name);assert len(r)==966 and {x['Video_ID'] for x in r}==ids,name
    texts=rows('TRANSCRIPT_COVERAGE.csv');valid=[r for r in texts if r['Status']=='TEXT_AVAILABLE']
    assert len(valid)==955 and len({r['Text_SHA256'] for r in valid})==955
    db=ROOT/'data/catalog/youtube_channel_registry.db'
    assert sha(db)==json.loads((BASE/'BASELINE_VALIDATION.json').read_text())['db_sha256_before']
    con=sqlite3.connect(f'file:{db}?mode=ro',uri=True)
    for r in valid:
        text=con.execute('SELECT transcript_text FROM transcripts WHERE youtube_video_id=? AND dataset_id=?',(r['Video_ID'],r['Dataset'])).fetchone()[0]
        assert hashlib.sha256(text.encode()).hexdigest()==r['Text_SHA256'],r['Video_ID']
    typed=[dict(v,Age_days=float(v['Age_days']) if v['Age_days'] else '',Views=int(v['Views']) if v['Views'] else None) for v in videos]
    for v in typed:
        result=compare(v,typed)
        for key,value in zip(['Performance_tier','Peer_count','Lifetime_rate_ratio','Peer_Video_IDs','Tier_basis'],result):
            assert str(v[key])==str(value),(v['Video_ID'],key)
    sensitivity=rows('PERFORMANCE_SENSITIVITY.csv');by={v['Video_ID']:v for v in typed}
    assert len(sensitivity)==176
    for r in sensitivity:
        v=by[r['Video_ID']];peers=[by[x] for x in v['Peer_Video_IDs'].split('|')][:5]
        ratio=v['Views']/v['Age_days']/median(p['Views']/p['Age_days'] for p in peers)
        tier='STRONG' if ratio>=2 else 'WEAK' if ratio<.5 else 'TYPICAL'
        assert round(ratio,5)==float(r['Five_peer_ratio']) and tier==r['Five_peer_tier']
        assert r['Agrees']==str(tier==v['Performance_tier'])
    sample=rows('REVIEW_SAMPLE.csv');semantic=rows('SEMANTIC_REVIEWS.csv');visual=rows('THUMBNAIL_REVIEWS.csv')
    assert len(sample)==len(semantic)==30
    assert {v['Channel'] for v in sample}=={v['Channel'] for v in videos}
    assert {v['Video_ID'] for v in sample}=={v['Video_ID'] for v in semantic}
    assert sum(r['Review_scope']=='FULL_STORED_TEXT' for r in semantic)==9
    assert len(visual)==27
    assets={}
    for name in ['THUMBNAIL_FETCH_REGISTER.csv','THUMBNAIL_FALLBACK_REGISTER.csv']:
        for r in rows(name):
            if r['Path']:
                assert r['Video_ID'] in r['URL']
                assert sha(ROOT/r['Path'])==r['SHA256']
                assets[r['Video_ID']]=r
    assert set(assets)=={r['Video_ID'] for r in visual}
    assert sum(r['Mobile_review']=='REVIEWED_320_WIDE' for r in rows('THUMBNAIL_COVERAGE.csv'))==27
    landscape=rows('LANDSCAPE_VIDEOS.csv');assert len(landscape)==180
    all_sets=[ids,{r['Video_ID'] for r in landscape}]
    for r in rows('REUSED_SOURCE_REGISTER.csv'):
        content=subprocess.check_output(['git','show',r['Version']],cwd=ROOT)
        assert hashlib.sha256(content).hexdigest()==r['SHA256']
        key='Video_ID' if r['Locator'].endswith('/VIDEO_PERFORMANCE.csv') else 'video_id' if r['Locator'].endswith('/PERFORMANCE_COMPARISON.csv') else None
        if key:all_sets.append({v[key] for v in csv.DictReader(content.decode().splitlines())})
    assert sum(map(len,all_sets))==len(set.union(*all_sets))==1363
    score_fields=['Demand_editorial','Evidence_strength','Novelty','Competition_headroom','Audience_usefulness','Research_feasibility','Production_affordability','Repeatability']
    backlog=rows('TOPIC_IDEA_BACKLOG.csv');assert len(backlog)==12
    for r in backlog:
        assert all(1<=int(r[k])<=5 for k in score_fields)
        assert sum(int(r[k]) for k in score_fields)==int(r['Total_out_of_40'])
        assert set(r['Evidence_Video_IDs'].split(';'))<=set.union(*all_sets)
    assert len(rows('SOURCE_GAP_DISPOSITIONS.csv'))==26
    assert not subprocess.check_output(['git','diff','03a6cd0','--','data/raw','data/catalog','data/manifests'],cwd=ROOT)
    result=dict(status='PASS_BOUNDED_CHECKPOINT_NOT_PHASE_COMPLETION',phase_complete=False,
        canonical_channels=13,canonical_unique_videos=966,canonical_titles=966,valid_transcript_texts=955,
        exact_transcript_text_duplicates=0,automated_script_features=len(rows('SCRIPT_FEATURES.csv')),
        full_text_reads=9,excerpt_or_full_reviews=30,mobile_thumbnail_reviews=27,attempted_thumbnail_videos=30,
        sampled_thumbnail_unavailable=3,canonical_without_new_mobile_review=939,
        canonical_without_semantic_review=936,formats=dict(Counter(v['Format'] for v in videos)),
        tiers=dict(Counter(v['Performance_tier'] for v in videos)),sensitivity_agreements=sum(r['Agrees']=='True' for r in sensitivity),
        sensitivity_denominator=176,landscape_channels=6,landscape_video_cards=180,
        reused_overlay_video_records=217,disjoint_referenced_video_ids=1363,original_path_gaps_dispositioned=26,
        raw_catalog_manifest_git_diff='EMPTY',canonical_db_sha256=sha(db),
        private_metrics='UNKNOWN',context_usage='UNKNOWN',
        exact_head_ci='CHECK_PR_36_AFTER_FINAL_PUSH; NOT_CERTIFIED_BY_THIS_LOCAL_VALIDATOR')
    (BASE/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
