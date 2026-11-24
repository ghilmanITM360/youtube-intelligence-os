"""Discover + classify What If research files. Read-only on sources. Writes candidates.csv in scratchpad.
usage: python3 -I classify.py"""
import os, csv, hashlib, subprocess, re, sys, json
SP = os.path.dirname(os.path.abspath(__file__))
H = '/Users/ghilmanislam360/'
D = H + 'Documents/'
REPO = D + 'youtube-intelligence-os'
ARCH = 'research/xkcd-what-if-research-archive/'
# (source root, dest subdir, label)
ROOTS = [
 (D+'YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics', 'forensics_2026-11-23/', 'main_forensics_audit'),
 (D+'YIOS-local-audits/2026-11-23-codex-independent-xkcd-review', 'codex_independent_review_2026-11-23/', 'codex_independent_review'),
 (D+'YIOS-local-audits/2026-11-23-codex-what-if-readiness-review', 'codex_readiness_review_2026-11-23/', 'codex_readiness_review'),
 (D+'YIOS-local-audits/2026-11-17-xkcd-83-script-intelligence', 'earlier_audits_2026-11-17/xkcd-83-script-intelligence/', 'earlier_83_script_audit'),
 (D+'YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU', 'earlier_audits_2026-11-17/xkcd-8fADp43wJwU_ct_scan/', 'earlier_single_video_ct_scan'),
 (D+'yios-worktree-preservation-2026-10-21/evidence/what-if-forensic', 'earlier_preserved_evidence_2026-10-21/what-if-forensic/', 'preserved_what_if_forensic_evidence'),
]
SINGLES = [
 (H+'Downloads/Pasted text(20261123-055514).txt', 'inputs/MASTER_DIRECTIVE_pasted_text_20261123-055514.txt', 'original_master_directive'),
 (H+'Downloads/WHAT_IF_INDEPENDENT_AUDIT.md', 'inputs/WHAT_IF_INDEPENDENT_AUDIT.md', 'external_audit_input'),
 (D+'YIOS-Visual-Forensics-Discovery-2026-10-28/WHAT_IF_VISUAL_RESEARCH_STATUS.md', 'earlier_audits_2026-10-28/WHAT_IF_VISUAL_RESEARCH_STATUS.md', 'earlier_status_note'),
]
IMG = {'.jpg','.jpeg','.png','.webp','.gif','.svg','.bmp','.tif','.tiff','.heic'}
VID = {'.mp4','.mov','.mkv','.webm','.avi','.m4v'}
AUD = {'.wav','.mp3','.m4a','.flac','.aac','.ogg'}
CACHE_PARTS = ('__pycache__', '.venv', 'site-packages', 'node_modules', '.DS_Store')
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''): h.update(c)
    return h.hexdigest()
def gitblob(p):
    h = hashlib.sha1(); n = os.path.getsize(p); h.update(b'blob %d\0' % n)
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''): h.update(c)
    return h.hexdigest()
def classify(path, rel):
    ext = os.path.splitext(path)[1].lower()
    if any(x in path.split(os.sep) or x in path for x in CACHE_PARTS) and '.venv' in path or '__pycache__' in path or path.endswith('.DS_Store'):
        return 'EXCLUDE', 'cache_or_venv_or_system', ext
    if ext in IMG: return 'EXCLUDE', 'image', ext
    if ext in VID: return 'EXCLUDE', 'video', ext
    if ext in AUD: return 'EXCLUDE', 'audio', ext
    if ext == '.pyc': return 'EXCLUDE', 'cache_or_venv_or_system', ext
    if os.path.basename(path) == 'pip_demucs.log': return 'EXCLUDE', 'dependency_install_log', ext
    if ext == '.log': return 'EXCLUDE', 'repo_gitignore_rule_*.log', ext
    return 'INCLUDE', '', ext
rows = []
def walk(root, dest, label):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.venv-demucs', '__pycache__', 'node_modules')] if True else dn
        for f in fn:
            p = os.path.join(dp, f); rel = os.path.relpath(p, root)
            rows.append((p, dest + rel, label))
    # venv dirs that were pruned: record as one excluded row-group
for r in ROOTS:
    if os.path.isdir(r[0]): walk(*r)
for s in SINGLES:
    if os.path.exists(s[0]): rows.append(s)
# pruned venv summary
venv = D + 'YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU/.venv-demucs'
venv_count = sum(len(fs) for _, _, fs in os.walk(venv)) if os.path.isdir(venv) else 0
# repo blob index on origin/main
out = subprocess.run(['git', '-C', REPO, 'ls-tree', '-r', 'origin/main'], capture_output=True, text=True, check=True).stdout
blobidx = {}
for line in out.splitlines():
    meta, path = line.split('\t', 1); mode, typ, h = meta.split()
    blobidx.setdefault(h, []).append(path)
SEC = re.compile(r'AIza[0-9A-Za-z_\-]{35}|sk-[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|(?i:bearer\s+[A-Za-z0-9._\-]{20,})|(?i:(api[_-]?key|secret|passwd|password|token)\s*["\']?\s*[:=]\s*["\'][^"\'\s]{8,})|[A-Za-z0-9._%+-]+@(gmail|yahoo|outlook|hotmail)\.com')
TEXT = {'.md','.txt','.csv','.json','.py','.log','.xml','.srt','.jsonl','.sh','.tsv'}
w = csv.writer(open(SP + '/candidates.csv', 'w', newline=''))
w.writerow(['source_path','repo_path','label','decision','reason','ext','size','sha256','git_blob_sha1','in_origin_main_as','secret_hits'])
n = 0
for p, dest, label in rows:
    rel = dest
    dec, why, ext = classify(p, rel)
    size = os.path.getsize(p)
    s = sha(p)
    gb = gitblob(p) if dec == 'INCLUDE' else ''
    inrepo = ';'.join(blobidx.get(gb, [])) if gb else ''
    hits = ''
    if dec == 'INCLUDE' and ext in TEXT:
        try:
            txt = open(p, 'r', errors='ignore').read()
            m = SEC.findall(txt); hits = str(len(m)) if m else ''
        except Exception as e: hits = 'ERR'
    w.writerow([p, ARCH + dest if dec == 'INCLUDE' else '', label, dec, why, ext, size, s, gb, inrepo, hits]); n += 1
json.dump({'venv_pruned_files': venv_count, 'rows': n}, open(SP + '/classify_meta.json', 'w'))
print(n, 'rows; venv pruned', venv_count)
