"""Medical packaging safety register. Packaging judgements only (title + thumbnail wording); NO transcript/content evidence has been read, so CONTRADICTED_BY_CONTENT is never assigned.
Outputs medical-packaging-safety.csv/json: one row per package-audited health package, with title-only flag, thumbnail-only label, package label, escalation pattern and the content-verification queue
(queued = package makes a diagnosis/cure/reversal/fear claim, or a MISLEADING_RISK / UNRESOLVED label, or title and thumbnail risk labels disagree by >= 2 levels). Title-only counts cover all 2,303 videos."""
import csv, json
from collections import Counter
from pathlib import Path
from build_package_inputs import thumb_rows

HERE = Path(__file__).resolve().parent
rd = lambda f: list(csv.DictReader((HERE / f).open()))
LEVEL = {'NOT_HEALTH': -1, 'MEDICAL_PACKAGING_SAFE': 0, 'NEEDS_CONTEXT': 1, 'UNRESOLVED': 1, 'MISLEADING_RISK': 2}
ta = {r['Video_ID']: r for r in rd('title-analyst-audit.csv')}
tf = {r['Video_ID']: r for r in rd('title-forensics.csv')}
tr = thumb_rows()
mp = {r['Package_ID']: r for r in rd('master-packages.csv')}
out = []
for p in rd('package-forensics.csv'):
    if p['medical_package_label'] == 'NOT_HEALTH' and ta[p['Video_ID']]['medical_title_flag'] == 'NOT_HEALTH': continue
    th = tr[mp[p['Package_ID']]['Thumbnail_ID']][1]
    t_lab, th_lab, pk_lab = ta[p['Video_ID']]['medical_title_flag'], th.get('medical_label', 'NOT_HEALTH'), p['medical_package_label']
    gap = LEVEL[th_lab] - LEVEL[t_lab] if t_lab != 'NOT_HEALTH' and th_lab != 'NOT_HEALTH' else 0
    pattern = p['medical_escalation'] if p['medical_escalation'] != 'NONE' else ('THUMBNAIL_MORE_EXTREME_THAN_TITLE' if gap >= 1 else 'TITLE_MORE_EXTREME_THAN_THUMBNAIL' if gap <= -1 else 'NONE')
    claims = tf[p['Video_ID']]['Health_Claim_Type']
    queue = p['content_verification_queue'] == 'Y' or pk_lab in ('MISLEADING_RISK', 'UNRESOLVED') or abs(gap) >= 2
    out.append(dict(Package_ID=p['Package_ID'], Channel_Name=p['Channel_Name'], Video_ID=p['Video_ID'], Title=p['Title'], Title_Medical_Flag=t_lab, Thumbnail_Medical_Label=th_lab, Package_Medical_Label=pk_lab,
                    Escalation_Pattern=pattern, Title_Claim_Types_Rule_Based=claims, Misleading_Risk=p['misleading_risk'], Credible=p['credible'], Content_Verification_Queue='YES' if queue else 'NO',
                    Verification_Question=('Does the content support: ' + p['package_promise'][:150]) if queue else '', CONTRADICTED_BY_CONTENT='NOT_ASSESSED_CONTENT_NOT_READ'))
with (HERE / 'medical-packaging-safety.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, list(out[0])); w.writeheader(); w.writerows(out)
summ = dict(method='packaging judgement only; content not read', title_only_all_videos=dict(Counter(r['medical_title_flag'] for r in ta.values())),
            health_packages_audited=len(out), package_label=dict(Counter(r['Package_Medical_Label'] for r in out)), thumbnail_label=dict(Counter(r['Thumbnail_Medical_Label'] for r in out)), escalation_patterns=dict(Counter(r['Escalation_Pattern'] for r in out)),
            content_verification_queue=sum(r['Content_Verification_Queue'] == 'YES' for r in out), contradicted_by_content=0)
(HERE / 'medical-packaging-safety.json').write_text(json.dumps(dict(summary=summ, rows=out), ensure_ascii=False, indent=1))
print(json.dumps(summ, indent=1))
