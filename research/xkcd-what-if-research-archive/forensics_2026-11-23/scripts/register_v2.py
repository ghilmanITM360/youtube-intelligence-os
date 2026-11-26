"""Phase 3: add the directive's per-file provenance attributes to 02_WHAT_IF_RELATED_FILE_REGISTER.csv (original saved as ..._v1_2026-11-23.csv).
Every added column is RULE_DERIVED from the path, category and SHA-256 recorded in the register; nothing is read from file contents (except 'match'). UNKNOWN where no rule applies.
Run: python3 -I scripts/register_v2.py"""
import csv, os, re, shutil, collections
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = A + '/02_WHAT_IF_RELATED_FILE_REGISTER.csv'; v1 = A + '/02_WHAT_IF_RELATED_FILE_REGISTER_v1_2026-11-23.csv'
if not os.path.exists(v1): shutil.copy(f, v1)
rows = list(csv.DictReader(open(v1)))
ids = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
sha = collections.Counter(r['sha256'] for r in rows if r['sha256'])
IDRE = re.compile(r'(?<![A-Za-z0-9_-])([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])')
def vid(p):
    for m in re.finditer(r'\[([A-Za-z0-9_-]{11})\]', p):
        if m.group(1) in ids: return m.group(1)
    for seg in re.split(r'[/._ ]', p):
        if seg in ids: return seg
    m = re.search(r'xkcd-([A-Za-z0-9_-]{11})', p)
    if m and m.group(1) in ids: return m.group(1)
    return 'UNKNOWN'
out = []
for r in rows:
    p = r['path']; cat = r['category']; pl = p.lower()
    comp = 'WhatIfCompetitors' in p or 'WHATIF_COMPETITOR' in p or 'Fossil' in p or 'Minute Zero' in p or 'Tracer' in p
    xk = ('xkcd' in pl or 'what-if' in pl or 'whatif' in pl or 'what_if' in pl) and not comp
    r['video_id_or_source'] = vid(p)
    r['project_channel'] = 'COMPETITOR (Fossil/Minute Zero/Tracer Project)' if comp else 'xkcd What If? (UC6IxnFzHofFJ5X2PycSMsww)' if xk else 'UNKNOWN_OR_MIXED'
    r['content_type'] = cat
    if cat == 'video' and 'YIOS-Media-Library' in p: oc = 'ORIGINAL_MEDIA_COPY (acquired source file; original upload not re-verified at source)'
    elif 'original-files' in pl or 'preservation' in pl: oc = 'PRESERVED_COPY'
    elif any(k in pl for k in ('frames_1fps', '/dense', '/sheets', 'contact', 'keyframe')): oc = 'DERIVED_FROM_MEDIA (frames/sheets)'
    elif any(k in pl for k in ('transcript', 'audits', 'asr')): oc = 'DERIVED (transcript/audit)'
    elif cat in ('doc', 'table', 'json', 'text', '.py', '.sh', '.jsonl'): oc = 'DERIVED_OR_AUTHORED_ANALYSIS (not confirmed original)'
    else: oc = 'UNKNOWN'
    r['original_copy_derived'] = oc
    n = sha.get(r['sha256'], 0) if r['sha256'] else 0
    r['duplicate_bytes_in_register'] = 'UNKNOWN (no sha256)' if not r['sha256'] else f'YES ({n} paths share this sha256)' if n > 1 else 'NO (unique within this register)'
    r['existing_provenance'] = 'SHA256_RECORDED' if r['sha256'] else 'NONE_RECORDED'
    r['existing_qa'] = 'IS_A_QA_OR_VALIDATION_RECORD' if re.search(r'quality_gate|VALIDATION|validation_report|QA', p) else 'UNKNOWN (file-level QA not recorded)'
    r['reuse_restrictions'] = ('THIRD_PARTY_COPYRIGHT: reference/analysis only, never a production asset' if (cat in ('video', 'image', 'audio') and (xk or comp)) else
                               'NONE_KNOWN for own analysis files; quoted source text is third-party' if cat in ('doc', 'table', 'json', 'text', '.py', '.sh', '.jsonl') else 'UNKNOWN')
    low = any(k in pl for k in ('/scratch/', '/agents/', '/repro/'))
    r['usable_for_study'] = 'LOW (scratch/agent/repro working file)' if low else 'YES (source media or frames)' if cat in ('video', 'audio', 'image') and (xk or comp) else 'YES_AS_CONTEXT' if xk or comp else 'UNKNOWN_RELEVANCE'
    r['field_basis'] = 'RULE_DERIVED from path/category/sha256 (not file-by-file inspected)'
    out.append(r)
w = csv.DictWriter(open(f, 'w', newline=''), fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
C = collections.Counter
print(len(out), C(r['original_copy_derived'].split(' ')[0] for r in out), C(r['usable_for_study'].split(' ')[0] for r in out), C(r['video_id_or_source'] != 'UNKNOWN' for r in out), C(r['project_channel'][:12] for r in out))
