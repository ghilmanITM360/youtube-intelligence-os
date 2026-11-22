"""Focused integrity and reproduction checks for this research deliverable."""
import csv
import hashlib
import json
import math
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent.parent
BASE='7e2f6d3a3d5e4294d5f8bc4737dd0c784610c1f1'
REQUIRED=['README.md','EXECUTIVE_FINDINGS.md','VIDEO_PERFORMANCE.csv','TITLE_THUMBNAIL_PLAYBOOK.md','TOPIC_TREND_ANALYSIS.md','SCRIPT_STORYTELLING_ANALYSIS.md','VISUAL_MOTION_PRODUCTION_DNA.md','ASSET_FACTORY_AND_CODEX_FEASIBILITY.md','ORIGINAL_CHANNEL_PRODUCTION_SOP.md','IMPROVEMENT_OPPORTUNITIES.md','EVIDENCE_AND_LIMITATIONS.md','DEMO/README.md','DEMO/index.html']

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    for name in REQUIRED:assert (ROOT/name).is_file(),name
    sources=json.loads((ROOT/'SOURCE_HASHES.json').read_text())
    for name,expected in sources.items():
        assert digest(REPO/name)==expected, f'Source changed: {name}'
        blob=subprocess.check_output(['git','show',BASE+':'+name],cwd=REPO)
        assert hashlib.sha256(blob).hexdigest()==expected, f'Source differs from frozen base: {name}'
    rows=list(csv.DictReader((ROOT/'VIDEO_PERFORMANCE.csv').open()));by={r['Video_ID']:r for r in rows}
    assert len(rows)==len(by)==206
    raw=list(csv.DictReader((REPO/'data/extracted/forensic-analysis/casually-finance/2026-10-12/01_CHANNEL_METADATA/all-videos-metadata.csv').open()))
    for r in raw:
        d=by[r['video_id']]
        assert d['Title']==r['title'] and d['Public_Views']==r['views'] and d['Snapshot_Date']==r['collected_at']
    for r in rows:
        age=(datetime.fromisoformat(r['Snapshot_Date'].replace('Z','+00:00'))-datetime.fromisoformat(r['Publish_Date'])).total_seconds()/86400
        assert abs(float(r['Age_Days'])-age)<.00001
        assert abs(float(r['Views_Per_Day'])-int(r['Public_Views'])/age)<.001
        if age<7:assert r['Tier']=='INSUFFICIENT_DATA' and not r['Peer_IDs']
        else:
            peers=[by[v] for v in r['Peer_IDs'].split(';')]
            assert len(peers)==int(r['Peer_Count'])>=5
            assert all(p['Format']==r['Format'] and p['Video_ID']!=r['Video_ID'] and float(p['Age_Days'])>=7 for p in peers)
            if r['Peer_Mode']=='AGE_CALIPER':assert all(.5<=float(p['Age_Days'])/age<=2.00001 for p in peers)
            assert float(r['Ratio_Bootstrap_Low'])<=float(r['Ratio_Bootstrap_High'])
        thumb=r['Thumbnail_Reference']
        if thumb!='THUMBNAIL_VISUAL_UNAVAILABLE':assert (REPO/thumb).read_bytes()[:3]==b'\xff\xd8\xff'
    generated=['VIDEO_PERFORMANCE.csv','ANALYTICS_SUMMARY.json','SOURCE_HASHES.json']
    before={n:digest(ROOT/n) for n in generated}
    subprocess.run([sys.executable,str(ROOT/'build_analytics.py')],cwd=REPO,check=True,capture_output=True)
    assert before=={n:digest(ROOT/n) for n in generated},'Non-deterministic analytics'
    for p in ROOT.rglob('*.md'):
        if p.name in ['AGENTS.md','CLAUDE.md']:continue
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if target.startswith(('http:','https:','mailto:','#')):continue
            assert (p.parent/target.split('#')[0]).exists(),(p,target)
    changes=subprocess.check_output(['git','diff','--name-only',BASE],cwd=REPO,text=True).splitlines()
    assert all(n.startswith('research/casually-finance-success-playbook/') for n in changes)
    manifest=json.loads((ROOT/'DEMO/asset-manifest.json').read_text())
    assert manifest['authored_rigs']==1 and manifest['derived_pose_expression_variants']==9
    assert len({digest(ROOT/'DEMO/assets'/n) for n in manifest['files'] if n.startswith('mira_')})==9
    check=json.loads((ROOT/'DEMO/CHECK_RESULTS.json').read_text());assert check['ok']
    assert all(check[k]['errorCount']==0 for k in ['lint','runtime','layout','contrast'])
    result={'status':'FOCUSED_VALIDATION_PASSED','source_base':BASE,'upload_rows':len(rows),'source_hashes_unchanged':len(sources),'metadata_preserved':True,'peer_pools_valid':True,'deterministic_analytics':True,'evidence_links_resolve':True,'diff_scoped_to_research_folder':True,'demo_original_rigs':1,'demo_derived_states':9,'demo_check_errors':0,'continuous_competitor_review':'NOT_CLAIMED'}
    (ROOT/'VALIDATION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
