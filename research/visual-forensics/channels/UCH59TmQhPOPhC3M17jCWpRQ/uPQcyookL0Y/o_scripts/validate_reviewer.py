# Validate one bounded reviewer's outputs: coverage, hashes, witness locators, in-segment frame times.
import csv,sys,hashlib,re,json
from pathlib import Path
rv,batch,i0,i1=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]);d=Path(f'agents/{rv}');FPS=30000/1001
rows=lambda f:list(csv.DictReader(open(f)))
states={r['state_v4'] for r in rows('tables/states_v6_draft.csv')[i0:i1]}
rep={r['native_png'] for r in rows(f'tables/k_rep_frames_{batch}.csv')};strips={r['strip_png'] for r in rows(f'tables/o_motion_peaks_{batch}.csv')}
asr={int(r['seg_index']) for r in rows(f'tables/o_asr_excerpt_{batch}.csv')}
err=[];reads=rows(d/'evidence_reads.csv');paths={r['path'] for r in reads}
for m in sorted((rep|strips)-paths):err.append('NOT_READ '+m)
for r in reads:
    if not Path(r['path']).exists():err.append('MISSING '+r['path']);continue
    if hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()!=r['sha256']:err.append('HASH '+r['path'])
    if not r['witness'].strip():err.append('NOWITNESS '+r['path'])
art=rows(d/f'art_audit_{batch}.csv')
if {r['state'] for r in art}!=states or len(art)!=len(states):err.append(f'ART_COVERAGE {sorted({r["state"] for r in art}^states)} n={len(art)}')
for r in art:
    for loc in filter(None,(x.strip() for x in r['frames_viewed'].split(';'))):
        nums=re.findall(r'\d{3,6}',loc) if '/' not in loc else []
        if nums:  # bare frame numbers: resolve against this state's read paths
            bad=[n for n in nums if not any(r['state'] in q and (f'_f{n}.' in q or f'peak{n}.' in q) for q in paths)]
            if bad:err.append(f'ART_UNREAD_FRAME {r["state"]} {bad}')
            continue
        if loc not in paths:err.append(f'ART_UNREAD_LOCATOR {r["state"]} {loc}')
mo=rows(d/f'motion_events_{batch}.csv')
if {r['strip_path'] for r in mo}!=strips:err.append('MOTION_STRIP_COVERAGE')
na=rows(d/f'narration_relation_{batch}.csv')
segs={int(r['seg_index']) for r in na if r['seg_index'].strip().isdigit()}  # non-numeric rows = reviewer gap rows, kept
if segs!=asr:err.append(f'NARR_COVERAGE {sorted(segs^asr)}')
for r in na:
    a,b=float(r['asr_start_s']),float(r['asr_end_s'])
    for loc in re.findall(r'frames/[^ ;()]+?\.png',r['visual_frames_judged']):  # tolerate prose around paths; raw kept
        if loc not in paths:err.append(f'NARR_UNREAD {r["seg_index"]} {loc}');continue
        fs=[int(x) for x in re.findall(r'_f(\d+)',loc)] if 'motion_strips' not in loc else [int(re.search(r'peak(\d+)',loc).group(1))]
        f=fs[-1]
        if not (a-0.2<=f/FPS<b+0.2):err.append(f'NARR_TIME {r["seg_index"]} f{f}={f/FPS:.2f}s not in [{a},{b})')
pr=d/f'state_prompts_{batch}.csv'
if pr.exists() and {r['state'] for r in rows(pr)}!=states:err.append('PROMPT_COVERAGE')
out={'reviewer':rv,'batch':batch,'reads':len(reads),'expected_images':len(rep|strips),'art_rows':len(art),'motion_rows':len(mo),'narr_rows':len(na),'prompt_rows':len(rows(pr)) if pr.exists() else 0,'errors':err}
Path(f'tables/o_validation_{rv}_{batch}.json').write_text(json.dumps(out,indent=1));print(json.dumps(out,indent=1))
