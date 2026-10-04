"""Channel coverage table (all registry channels) and master package table (one row per canonical video).

Joins by exact Video_ID / Thumbnail_ID only. Public metrics only: no private Studio data is read here.
Performance fields reuse build_video_metrics.py's age-matched model; they describe lifetime public views, NOT packaging quality.
Outputs: channel-coverage.csv, master-packages.csv (+ .json), re-run after each audit wave.
"""
import csv, glob, json, re, sqlite3, statistics
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REG = sqlite3.connect(ROOT / 'data/catalog/youtube_channel_registry.db')
OWN = {'UCQIzqH7QZ9viBYpOFqgSXMg'}  # Decode Your Heart - Dr. Rehan (own channel)
NAME_NICHE = [(r'invest|financ|money|wealth|millionaire|dividend|career|expensive|retired|capital|ledger|net ?worth', 'FINANCE_(NAME_INFERENCE_ONLY)'),
              (r'parent', 'PARENTING_(NAME_INFERENCE_ONLY)'), (r'brick body|bro pump|fasted', 'FITNESS_HEALTH_(NAME_INFERENCE_ONLY)'),
              (r'doc|health|senior', 'HEALTH_(NAME_INFERENCE_ONLY)'), (r'explain|history|stories|wheels|chat', 'EXPLAINER_OR_OTHER_(NAME_INFERENCE_ONLY)')]
CLASS_RANK = {'REGISTERED_LOCAL_THUMBNAIL': 0, 'CURRENT_PUBLIC_THUMBNAIL': 1, 'SCREENSHOT_EMBEDDED_THUMBNAIL': 2}


def audited():
    a = {}
    for f in sorted(glob.glob(str(HERE / 'audit-batch-B002-*.json'))) + [str(HERE / 'individual-audit-batch-001.json')]:
        for r in json.load(open(f)): a[r['Thumbnail_ID']] = (r.get('batch_id', 'B001'), r.get('score_100'))
    return a


def package_audits():
    pa = {}
    for f in sorted(glob.glob(str(HERE / 'package-audit-PK-*.json'))):
        for r in json.load(open(f)): pa[r['Package_ID']] = r
    return pa


def band(p, n):
    if p == '': return 'INSUFFICIENT_COHORT'
    p = float(p)
    if n >= 20 and p >= 0.9: return 'TOP_10_PERCENT'
    if p >= 0.75: return 'TOP_25_PERCENT'
    if n >= 20 and p <= 0.1: return 'BOTTOM_10_PERCENT'
    if p <= 0.25: return 'BOTTOM_25_PERCENT'
    return 'MIDDLE_50_PERCENT'


def main():
    chan = {c: dict(name=n, handle=h, sg=sg, tg=tg, st=st) for c, n, h, sg, tg, st in REG.execute('select canonical_channel_id,channel_name,current_handle,source_group,target_group,status from channels')}
    tf = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-forensics.csv').open())}
    vm = {r['Video_ID']: r for r in csv.DictReader((HERE / 'video-metrics.csv').open())}
    uni = defaultdict(list)
    for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()):
        if r['Video_ID'] and r['Thumbnail_ID'] and r['Evidence_Class'] in CLASS_RANK: uni[r['Video_ID']].append(r)
    aud = audited()
    pa = package_audits()
    ta = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-analyst-audit.csv').open())} if (HERE / 'title-analyst-audit.csv').exists() else {}
    niche = {}
    for r in tf.values(): niche.setdefault(r['Channel_ID'], Counter())[r['Niche']] += 1
    niche = {c: k.most_common(1)[0][0] for c, k in niche.items()}
    # age-adjusted outlier stats from the same 12-nearest-age peers used by the performance class
    by = defaultdict(list)
    for v, r in vm.items(): by[(r['Channel_ID'], r['Format'])].append(r)
    outl, rz, rawpct = {}, {}, {}
    for k, g in by.items():
        ok = [r for r in g if r['Public_Views'] != '' and r['Video_Age_Days'] != '']
        views = np.array([float(r['Public_Views']) for r in ok]) if ok else np.array([])
        for r in ok:
            rawpct[r['Video_ID']] = round(float((views < float(r['Public_Views'])).mean() + 0.5 * (views == float(r['Public_Views'])).mean()), 3)
            if len(ok) < 8: continue
            peers = sorted((p for p in ok if p is not r), key=lambda p: abs(float(p['Video_Age_Days']) - float(r['Video_Age_Days'])))[:12]
            pv = np.array([float(p['Public_Views']) for p in peers])
            med = float(np.median(pv))
            if med > 0: outl[r['Video_ID']] = round(float(r['Public_Views']) / med, 2)
            mad = float(np.median(np.abs(np.log10(pv + 1) - np.median(np.log10(pv + 1))))) * 1.4826
            if mad > 0: rz[r['Video_ID']] = round((np.log10(float(r['Public_Views']) + 1) - float(np.median(np.log10(pv + 1)))) / mad, 2)
    rows = []
    for vid, t in tf.items():
        m = vm[vid]
        cands = sorted(uni.get(vid, []), key=lambda r: CLASS_RANK[r['Evidence_Class']])
        p = cands[0] if cands else {}
        extra = [f"{c['Thumbnail_ID']}:{c['Evidence_Class']}:{c['Creative_Temporal_Alignment']}" for c in cands[1:]]
        tid = p.get('Thumbnail_ID', '')
        a = aud.get(tid)
        n = int(m['Cohort_Size'] or 0)
        lim = []
        if p.get('Creative_Temporal_Alignment') == 'CURRENT_PUBLIC_ONLY': lim.append('THUMBNAIL_IS_CURRENT_PUBLIC_NOT_PROVEN_AT_VIEW_TIME')
        if m['Metric_Date_Source'].endswith('UPPER_BOUND'): lim.append('METRIC_DATE_IS_UPPER_BOUND')
        if m['Performance_Class'] == 'INSUFFICIENT_COHORT': lim.append('NO_AGE_MATCHED_COHORT')
        if not tid: lim.append('NO_ACCESSIBLE_IMAGE')
        rows.append(dict(
            Package_ID=f'PKG-{vid}', Channel_ID=t['Channel_ID'], Channel_Name=t['Channel_Name'], Niche=t['Niche'], Sub_Niche='UNSPECIFIED', Video_ID=vid, YouTube_Video_ID=vid, Format=t['Format'],
            Title_Current=t['Exact_Title'], Title_Observed_At=m['Metric_Observation_Date'], Title_Observation_Basis='CURRENT_REGISTRY_TITLE_AT_METRIC_OBSERVATION_DATE_OR_EARLIER', Published_At=t['Published_At'],
            Thumbnail_ID=tid, Creative_Version_ID=p.get('Creative_Version_ID', ''), Thumbnail_Source=p.get('Source_Type', ''), Thumbnail_Evidence_Class=p.get('Evidence_Class', ''), Thumbnail_Observed_At=p.get('Source_Observation_Date', ''),
            Creative_Temporal_Alignment=p.get('Creative_Temporal_Alignment', 'UNKNOWN'), Additional_Creatives='|'.join(extra), Visual_Family_ID=p.get('Visual_Family_ID', ''),
            Views=m['Public_Views'], Metric_Observed_At=m['Metric_Observation_Date'], Metric_Date_Confidence='EXACT' if m['Metric_Date_Source'].startswith('INVENTORY') else 'UPPER_BOUND', Age_Days=m['Video_Age_Days'],
            Relative_Performance_Class=m['Performance_Class'], Perf_Percentile_Age_Matched=m['Perf_Percentile_Age_Matched'], Cohort_Size=n, Performance_Band=band(m['Perf_Percentile_Age_Matched'], n),
            Within_Channel_Percentile_Raw_Views=rawpct.get(vid, ''), Outlier_Multiple_Age_Adjusted=outl.get(vid, ''), Robust_Z_Age_Adjusted=rz.get(vid, ''), Evidence_Tier='D_AGE_ADJUSTED_PUBLIC' if m['Performance_Class'] != 'INSUFFICIENT_COHORT' else 'E_RAW_PUBLIC_VIEWS',
            Title_Audit_Status=('PROGRAMMATIC_AND_ANALYST_DONE_QA_SAMPLED' if ta[vid].get('qa_status') == 'QA_SAMPLED' else 'PROGRAMMATIC_AND_ANALYST_DONE_NOT_QA_SAMPLED') if vid in ta else 'PROGRAMMATIC_DONE_ANALYST_PENDING', ANALYST_TITLE_DIAGNOSTIC_SCORE=ta.get(vid, {}).get('ANALYST_TITLE_DIAGNOSTIC_SCORE', ''), Title_Orientation=ta.get(vid, {}).get('orientation', ''), Title_Overpromise_Risk=ta.get(vid, {}).get('overpromise_risk', ''), Title_Medical_Flag=ta.get(vid, {}).get('medical_title_flag', ''), Thumbnail_Audit_Status=('AUDITED_' + a[0]) if a else ('PENDING' if tid else 'NO_IMAGE'), Thumbnail_Diagnostic_Score=a[1] if a else '',
            Packaging_Audit_Status=(('AUDITED_' + pa[f'PKG-{vid}']['batch_id']) if f'PKG-{vid}' in pa else 'NOT_STARTED') if tid else 'NOT_POSSIBLE_NO_IMAGE',
            EXPERT_PACKAGING_DIAGNOSTIC_SCORE=pa.get(f'PKG-{vid}', {}).get('score_100', ''), Package_Primary_Relationship=pa.get(f'PKG-{vid}', {}).get('primary_relationship', ''), Evidence_Limitations='|'.join(lim)))
    with (HERE / 'master-packages.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(rows[0])); w.writeheader(); w.writerows(rows)
    (HERE / 'master-packages.json').write_text(json.dumps(rows, ensure_ascii=False))
    # channel coverage
    cv = []
    for cid, c in sorted(chan.items(), key=lambda kv: kv[1]['name'].lower()):
        g = [r for r in rows if r['Channel_ID'] == cid]
        nv, nt, nth = len(g), sum(1 for r in g if r['Title_Current']), sum(1 for r in g if r['Thumbnail_ID'])
        both = sum(1 for r in g if r['Title_Current'] and r['Thumbnail_ID'])
        ta = sum(1 for r in g if r['Thumbnail_Audit_Status'].startswith('AUDITED'))
        pm = sum(1 for r in g if r['Relative_Performance_Class'] in ('HIGH', 'MIDDLE', 'LOW'))
        pv = sum(1 for r in g if r['Views'] != '')
        hist = sum(1 for r in g if r['Creative_Temporal_Alignment'] in ('HISTORICAL_SNAPSHOT_VERIFIED', 'SAME_PERIOD_VERIFIED'))
        if nv == 0: st, gap = 'IDENTITY_ONLY', 'No video-level data extracted for this channel (identity verified only)'
        elif both == nv and nv >= 1: st, gap = 'FULL_PACKAGING_DATA', 'Visual audits pending' if ta < nv else ''
        elif nth == 0: st, gap = 'TITLE_ONLY', 'No accessible thumbnail image'
        elif nt == 0: st, gap = 'THUMBNAIL_ONLY', 'No titles'
        else: st, gap = 'PARTIAL_PACKAGING_DATA', f'{nv - both} videos lack a thumbnail image'
        if st == 'FULL_PACKAGING_DATA' and ta < nv: gap = f'{nv - ta} thumbnail audits pending; package analysis not started'
        nn = niche.get(cid)
        if not nn:
            nn = 'UNKNOWN_IDENTITY_ONLY'
            for pat, lab in NAME_NICHE:
                if re.search(pat, c['name'], re.I): nn = lab; break
        cv.append(dict(Channel_ID=cid, Channel_Name=c['name'], Handle=c['handle'] or '', Own_Competitor_Reference='OWN' if cid in OWN else 'COMPETITOR_OR_REFERENCE_UNSPECIFIED', Registry_Target_Group=c['tg'], Niche=nn, Sub_Niche='UNSPECIFIED',
                       Canonical_Videos=nv, Videos_With_Title=nt, Videos_With_Thumbnail=nth, Videos_With_Title_And_Thumbnail=both, Thumbnail_Audits_Complete=ta, Packaging_Audits_Complete=sum(1 for r in g if r['Packaging_Audit_Status'].startswith('AUDITED')),
                       Public_Performance_Data=f'{pv}/{nv} videos with views; {pm} age-matched classified' if nv else 'NONE', First_Party_Data='PRIVATE_STUDIO_NOT_JOINED' if cid in OWN else 'NONE',
                       Temporal_Thumbnail_Evidence=f'{hist} videos with snapshot/screenshot-period creative' if nv else 'NONE', Coverage_Status=st, Main_Gap=gap))
    with (HERE / 'channel-coverage.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, list(cv[0])); w.writeheader(); w.writerows(cv)
    print(len(rows), Counter(r['Thumbnail_Audit_Status'][:9] for r in rows), Counter(r['Performance_Band'] for r in rows))
    print(len(cv), Counter(c['Coverage_Status'] for c in cv))


if __name__ == '__main__':
    main()
