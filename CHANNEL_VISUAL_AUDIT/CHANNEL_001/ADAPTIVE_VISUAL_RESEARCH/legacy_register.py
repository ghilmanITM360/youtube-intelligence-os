import csv
import hashlib
from pathlib import Path

h = Path.home()
out = Path(__file__).parent
archive = h/'YIOS-Archive/discovery/YIOS-machine-a-discovery-20261028T2158PKT'
legacy = h/'YIOS-local-audits'
a = h/'workprojects/yios-finance-machine-a/research/visual-forensics/channels/casual-finance'
shorts = h/'workprojects/yio-cf-editing-forensics-local-evidence'
sources = [
    (h/'YIOS-audit-20261105T1657Z/raw/db/registry_rebuild_vs_lfs_codex_casually-finance-knowledge-navigation.json','','Repository registry QA','Navigation provenance only'),
    (archive/'CASUALLY_FINANCE_RESEARCH_COMPARISON.md','','Cross-machine historical reconciliation','Historical claims require source receipts'),
    (legacy/'CASUAL_FINANCE_15_TO_20_HANDOFF_PROMPT.md','','Historical cohort','Preserved selection rationale'),
    (legacy/'CASUALLY_FINANCE_35_VIDEO_TARGET_20261104/visual_complete_ledger.json','','19-source historical ledger','Different scope and gate from current matrix'),
    (h/'workprojects/yios-recovery-status/NEW-PC-RECOVERY-STATUS-2026-10-12.md','','Historical status','CF 16/18 structural entry, separate from other channels'),
]
for p in sorted(legacy.glob('*-deep-ct-scan')):
    ident = p.name[11:-13]
    for name in ('SOURCE_IDENTITY_AND_MANIFEST.json','source_manifest.json','VISUAL_STATES.csv','visual_states.csv','quality_gate.json'):
        path = p/name
        if path.is_file() and (p.name.startswith('2026-11-08-') or ident in ('Uumnx2Fo6cE','o3FQcd91MIs')):
            sources.append((path,ident,'Legacy source receipt or visual evidence','File-level receipt, validate exact per-source gate before promotion'))
for vid in ('Uumnx2Fo6cE','o3FQcd91MIs'):
    for name in ('PORTABLE_MANIFEST.json','EXTERNAL_EVIDENCE_MANIFEST.json'):
        sources.append((a/vid/name,vid,'Machine A portable pointer','Read-only, candidate duplicate, no cross-Mac byte claim'))
for folder in sorted(shorts.iterdir()):
    if folder.is_dir() and len(folder.name)==11 and (folder/'whisper.json').is_file():
        sources.append((folder/'whisper.json',folder.name,'Historical Shorts ASR receipt','ASR provenance only, historical Shorts contract not independently re-certified'))
with (out/'LEGACY_RESEARCH_INTEGRATION_REGISTER.csv').open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['original_path','artifact','sha256','channel','video_id','scope','coverage_limit','already_canonical','integration_destination'])
    for p,vid,scope,limit in sources:
        if p.is_file():
            w.writerow([p,p.name,hashlib.sha256(p.read_bytes()).hexdigest(),'Casually Finance',vid,scope,limit,'check before integration','channel index or source-specific appendix'])
