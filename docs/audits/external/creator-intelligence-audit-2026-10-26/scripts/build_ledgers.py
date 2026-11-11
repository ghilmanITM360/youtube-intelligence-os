"""Build discovery inventory + SHA manifest from ledger/source_sha256_raw.tsv. Usage: python3 -I build_ledgers.py <audit_root>"""
import csv, sys
ROOT = sys.argv[1]
REF = 'd987510b966eaabba6cc2990290b52d2ecf3fe8e'
BASE = 'data/raw/global-youtube-knowledge/'
words = {r[2]: r[1].strip() for r in csv.reader(open(f'{ROOT}/ledger/text_map.tsv'), delimiter='\t')}
ids = {r[2]: r[0] for r in csv.reader(open(f'{ROOT}/ledger/text_map.tsv'), delimiter='\t')}
NAMED = ['Packaging (Thumbnail_Title) - SOP(1).pdf', 'YouTube_Intelligence_Brain_v1_Verified_Creator_OS.md',
 'Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf', 'new YT algorithms updates.pdf',
 'Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf', 'Script Analyzer.pdf',
 '🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf', 'YouTube algorithm guide.docx (2).pdf', 'Hook (1).pdf',
 'Viral Checklist.pdf', 'Intro Analyzer Prompts.docx (1).pdf', 'The Magic of ‘BUT’ and ‘THEREFORE’ in Storytelling.docx (1).pdf',
 'YouTube Title Analyzer — Natural Language Prompts (2).pdf', '📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf', 'Hook guide.pdf']
rows = []
for sha, size, pages, path in csv.reader(open(f'{ROOT}/ledger/source_sha256_raw.tsv'), delimiter='\t'):
    name = path.split('/', 1)[1]
    sid = ids.get(name, {'DS-000018': 'S19', 'DS-000031': 'S18'}.get(path.split('/')[0]))
    named = NAMED.index(name) + 1 if name in NAMED else ''
    note = ''
    if name in ('Hook (1).pdf', 'Hook guide.pdf'):
        note = 'Text byte-identical to the other Hook PDF; distinct PDF hash; ONE source, not independent'
    cov = 'FULL_TEXT_READ'
    if path.startswith('DS-000018'):
        cov = 'MANIFEST_63_TABS_INDEXED; T39 FULL; TARGETED_CLAIM_EXTRACTION_OTHER_62'
    rows.append([sid, named, name, 'FOUND_EXACT' if named else 'FOUND_ADDITIONAL', BASE + path, REF, 'all 79 local refs carry identical blob', sha, size, pages or 'n/a (not PDF)', words.get(name, ''), cov, note])
absent = [
 ('YIOS_Original_Frameworks_Source_Extraction_2026-10-26.md', 'owner extraction pack named in brief'),
 ('Legendary YouTube Thumbnail Analyzer (DOCX)', 'referenced in S15 pp22-24'),
 ('10 Intro Templates by Jon Youshaei', 'referenced in S15 pp25-26'),
 ('The MrBeast Playbook by Jon Youshaei', 'referenced in S15 pp26-28; S14 synthesises it'),
 ('The Casey Neistat Playbook by Jon Youshaei', 'referenced in S15 pp28-31; S14 synthesises it'),
 ('RenaeGem — The Cinematic–Algorithmic Mastermind', 'referenced in S15 p32'),
 ('"prompts" Fusion Framework PDF', 'referenced in S15 pp14-23 (content overlaps S06/S08)'),
 ('YouTube algorithm guide.docx (1)', 'earlier version cited in S15 p33; repo has (2) only'),
 ('Ultimate Google VEO 3 Prompt Guide (original PDF)', 'S10 is an LLM summary of it'),
 ('~9 image boards/slides (2026 Algorithm 9 Updates, Trust Score Cheat Sheet, etc.)', 'reacted to in S15 pp34-45'),
]
for n, why in absent:
    rows.append(['', '', n, 'NOT_FOUND', 'searched repo HEAD + all 79 refs + ~ depth 4', REF, '', '', '', '', '', 'NONE', why])
rows += [
 ['', '', 'Unlock_The_Secrets_of_YouTube_Growth_–_Own_53_Secret_ChatGPT_Prompts.pdf', 'DISCOVERED_OUTSIDE_SCOPE_NOT_READ', '~/Downloads', '', '', '', '', '', '', 'NONE', 'outside approved roots; owner may authorise'],
 ['', '', 'YIOS_Complete_YouTube_Algorithm_Intelligence_Guide_2026-10-26.pdf', 'DISCOVERED_OUTSIDE_SCOPE_NOT_READ', '~/Downloads', '', '', '', '', '', '', 'NONE', 'appears to be a generated report (secondary)'],
 ['', '', 'Raw YouTube Studio ZIPs (DS-000032, 69 ZIPs)', 'INACCESSIBLE', 'Machine A ~/Downloads + yios-private-backups', '', '', '', '', '', '', 'DERIVED_ONLY', 'derived measurements read from docs/research/decode-your-heart-2026-09-27'],
 ['', '', 'knowledge/youtube/* (30 files, 2026-10-15 consolidation)', 'FOUND_SECONDARY', 'knowledge/youtube/', REF, '', '', '', '', '', 'INDEX_READ', 'secondary synthesis; used for discovery only'],
]
H = ['source_id', 'brief_target_no', 'name', 'status', 'path_or_locator', 'git_ref', 'branch_versions', 'sha256', 'bytes', 'pdf_pages', 'extracted_words', 'coverage', 'note']
w = csv.writer(open(f'{ROOT}/ledger/SOURCE_DISCOVERY_INVENTORY.csv', 'w', newline=''))
w.writerow(H); w.writerows(rows)
named_found = sum(1 for r in rows if r[1])
assert named_found == 15, named_found
print(len(rows), 'rows;', named_found, 'named targets found')
