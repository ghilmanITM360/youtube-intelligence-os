"""Generate extras, README, tools and final manifests into the staging tree. usage: python3 -I finalize.py"""
import os, csv, json, hashlib, shutil, subprocess, collections, datetime, re
SP = os.path.dirname(os.path.abspath(__file__))
ARCH = 'research/xkcd-what-if-research-archive/'
R = SP + '/stage/' + ARCH
REPO = '/Users/ghilmanislam360/Documents/youtube-intelligence-os'
D = '/Users/ghilmanislam360/Documents/'
H = '/Users/ghilmanislam360/'
def git(*a): return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True, check=True).stdout
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''): h.update(c)
    return h.hexdigest()
BASE = git('rev-parse', 'origin/main').strip()
summ = json.load(open(SP + '/stage_summary.json')); man = json.load(open(SP + '/manifest_entries.json'))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
# 1) repo existing What If paths (inventory only, not copied)
pat = re.compile(r'what-if|whatif|xkcd|UC6IxnFzHofFJ5X2PycSMsww|unreasonably-exact', re.I)
lines = git('ls-tree', '-r', '-l', 'origin/main').splitlines()
ex = []
for l in lines:
    meta, path = l.split('\t', 1); mode, typ, h, size = meta.split()
    if pat.search(path): ex.append((path, h, size))
with open(R + 'REPO_EXISTING_WHATIF_PATHS_ON_ORIGIN_MAIN.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['path_on_origin_main', 'git_blob_sha1', 'size_bytes', 'base_commit']); [w.writerow([*e, BASE]) for e in sorted(ex)]
bl = git('diff', '--name-only', 'origin/main...origin/research/what-if-channel-strategy-2026-11-18').split('\n')
bl = [b for b in bl if b and re.search(r'unreasonably-exact|what-if|WHATIF', b, re.I)]
bsha = git('rev-parse', 'origin/research/what-if-channel-strategy-2026-11-18').strip()
with open(R + 'REPO_WHATIF_FILES_ONLY_ON_OTHER_BRANCH.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['path', 'branch', 'branch_head', 'note'])
    for b in sorted(bl): w.writerow([b, 'origin/research/what-if-channel-strategy-2026-11-18', bsha, 'owned by another session; NOT copied or modified here'])
# 2) external locations and decisions
ext = [
 (D+'YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/', 'INCLUDED non-image files', 'primary research folder; images, pycache excluded'),
 (D+'YIOS-local-audits/2026-11-23-codex-independent-xkcd-review/', 'INCLUDED', 'Codex independent review (4 files)'),
 (D+'YIOS-local-audits/2026-11-23-codex-what-if-readiness-review/', 'INCLUDED', 'Codex production readiness review (1 file)'),
 (H+'Downloads/Pasted text(20261123-055514).txt', 'INCLUDED (renamed)', 'original master directive; sha256 e38230526627e27b49c0f09c44dcac2cdba63fbcfe773c0f7370607d72668dc7 matches the hash recorded earlier'),
 (H+'Downloads/WHAT_IF_INDEPENDENT_AUDIT.md', 'INCLUDED', 'external audit input; sha256 40e72a1c...'),
 (D+'YIOS-local-audits/2026-11-17-xkcd-83-script-intelligence/', 'INCLUDED', 'earlier 83-script audit incl. 83 transcript .txt (third-party narration text; same videos already tracked in research/what-if-scripts)'),
 (D+'YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU/', 'INCLUDED non-image, non-audio, non-venv', '.venv-demucs (15,520 files), 339 jpg, 4 wav, pip install log excluded'),
 (D+'yios-worktree-preservation-2026-10-21/evidence/what-if-forensic/', 'INCLUDED', '9 jsonl/json preserved forensic evidence (earlier Oct 2026 run)'),
 (D+'YIOS-Visual-Forensics-Discovery-2026-10-28/WHAT_IF_VISUAL_RESEARCH_STATUS.md', 'NOT COPIED: identical bytes already on origin/main', 'mapped in DEDUP_MAP.csv'),
 (D+'YIOS-Visual-Forensics-Discovery-2026-10-28/ (other 21 files)', 'NOT INCLUDED: unrelated or multi-channel', 'general visual-forensics discovery across channels, not What If specific'),
 (D+'YIOS-Media-Library/xkcd Channel/', 'EXCLUDED: 88 mp4 video (about 531 MB)', 'media; hashes of the 88 are in forensics_2026-11-23/14_HASH_VERIFY_88.csv'),
 (H+'Downloads/Randall-Munroe-What-If__-Serious-Scientific-Answers-to-Absurd-Hypothetical-Questions-Houghton-Mifflin-Harcourt-2014.pdf', 'EXCLUDED: copyrighted book PDF', 'third-party book; also non-research media'),
 (H+'Downloads/What_If_15_Original_PDF_Parts/', 'EXCLUDED: copyrighted book PDF parts', 'third-party book excerpts'),
 (H+'Downloads/What If Everyone on Earth Jumped at Once.mp4', 'EXCLUDED: video', 'media'),
 (H+'Downloads/Adrian-2026-11-04-*.mp3', 'EXCLUDED: audio', 'narration test audio from another task'),
 (D+'Codex/2026-08-28/now-ingest-only-the-completed-xkcd/', 'NOTHING TO INCLUDE', 'directory exists but contains 0 files'),
 (D+'youtube-intelligence-os/.claude/worktrees/yios-canonical/', 'NOT INCLUDED', 'other worktree on feat/yios-canonical-data; not What If research, not touched'),
 (D+'youtube-intelligence-os/research/what-if-scripts, research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww, research/production-experiments/what-if-derived, data/manifests/what-if-forensic-source-v1.json and others', 'ALREADY IN REPO (origin/main)', 'inventory in REPO_EXISTING_WHATIF_PATHS_ON_ORIGIN_MAIN.csv; not copied'),
 ('origin/research/what-if-channel-strategy-2026-11-18 (13 commits ahead of main)', 'ALREADY ON ITS OWN BRANCH', 'strategy, Unreasonably Exact productions and calendar; listed in REPO_WHATIF_FILES_ONLY_ON_OTHER_BRANCH.csv; owned by another session'),
 ('Machine A (/Users/ghilmankhan/workprojects/youtube-intelligence-os)', 'UNAVAILABLE', 'not reachable from Machine B; contents unknown'),
 ('xkcd What If article text and book art', 'UNAVAILABLE', 'article correspondence 0 verified; no book-art comparison was done'),
]
with open(R + 'EXTERNAL_LOCATIONS_AND_DECISIONS.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['location', 'decision', 'reason_or_note']); [w.writerow(e) for e in ext]
# 3) verify tool
open(R + 'verify_manifest.py', 'w').write('''"""Verify this archive against MANIFEST.csv (sha256 + size) and check that no unlisted file exists.
usage (from repo root, any checkout of the branch):  python3 -I research/xkcd-what-if-research-archive/verify_manifest.py"""
import csv, hashlib, os, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(os.path.dirname(here))
rows = [r for r in csv.DictReader(open(here + '/MANIFEST.csv')) if r['status'] in ('INCLUDED', 'GENERATED')]
bad = 0; listed = set()
for r in rows:
    p = os.path.join(root, r['repo_path']); listed.add(os.path.normpath(p))
    if not os.path.isfile(p): print('MISSING', r['repo_path']); bad += 1; continue
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    if h != r['sha256'] or os.path.getsize(p) != int(r['size_bytes']): print('MISMATCH', r['repo_path']); bad += 1
skip = {os.path.normpath(here + '/MANIFEST.csv'), os.path.normpath(here + '/MANIFEST.json')}
extra = [os.path.join(dp, f) for dp, _, fs in os.walk(here) for f in fs if os.path.normpath(os.path.join(dp, f)) not in listed | skip]
for e in extra: print('UNLISTED', e); bad += 1
print(len(rows), 'files checked;', 'OK' if not bad else str(bad) + ' problems'); sys.exit(1 if bad else 0)
''')
os.makedirs(R + 'archive_tools', exist_ok=True)
for n in ('classify.py', 'build_stage.py', 'finalize.py'): shutil.copyfile(SP + '/' + n, R + 'archive_tools/' + n)
# 4) numbers for README, read from the sources themselves
A = D + 'YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/'
def n(p): return sum(1 for _ in csv.DictReader(open(A + p)))
N = dict(shots=n('ledgers_measured/ALL_SHOT_LEDGER.csv'), reviewed=n('review_sample/REVIEWED_SAMPLE.csv'), tranA=n('phase15_scene_coding/A_ten_SCENE_CODING.csv'),
         inv=n('03_CHANNEL_MASTER_INVENTORY.csv'), listen=n('09_LISTENING_REVIEW_PACK.csv'), prio=n('09_LISTENING_PRIORITY_ITEMS.csv'), add=n('14_LISTENING_PACK_ADDITIONS.csv'),
         rules=n('knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv'), sci=n('07_SCIENCE_CLAIM_CHECKS.csv'), epi=n('07e_EPISODE_CLAIM_CHECKS.csv'), style=n('06_STYLE_MEASUREMENTS_125.csv'))
heard = sum(1 for r in csv.DictReader(open(A + '09_LISTENING_REVIEW_PACK.csv')) if (r.get('heard_by') or '').strip())
N['heard_rows'] = heard
cat = '\n'.join(f'| {k} | {v} |' for k, v in sorted(summ['by_category'].items()))
grp = '\n'.join(f'| {k} | {v} |' for k, v in sorted(summ['by_source_group'].items()))
exc = '\n'.join(f'| {k} | {v} | {summ["excluded_bytes_by_reason"][k]/1048576:.1f} MB |' for k, v in sorted(summ['excluded_by_reason'].items()))
readme = f'''# xkcd What If? research archive (non-image backup)

Created {NOW}. Base commit: `{BASE}` (origin/main at creation). This branch holds a **backup copy of the text, data, code and report files** of the xkcd What If? research done on Machine B on 2026-11-23, plus earlier What If audit files. **Images, video and audio are not stored** (their paths, sizes and SHA-256 are in `EXCLUDED_FILES.csv`).

## Status (read this before using anything here)
**Research IN PROGRESS. DRAFT. NOT complete and NOT independently validated.** The folder name `...complete-forensics` repeats the directive's title; it is not a completion claim.

| Review kind | Status |
|---|---|
| Machine measurement (ffprobe, detectors, ASR) | done for 88 of 92 listed videos (4 media files unavailable) |
| Same-model self-review (Claude, one coder) | most coding: 156 boundary reviews, 125 + 160 style frames, 10 claims + 51 episode rows, tranche A scene coding |
| Partial independent review (Codex, a different tool) | two documents: `codex_independent_review_2026-11-23/` (findings F01 to F14, reproduced SC02, SC03, SC05, E09g only) and `codex_readiness_review_2026-11-23/` (production readiness, checks of operative text); neither listened to audio or has expert standing |
| Human listening | **0** (`heard_by` is empty in all {N["listen"]} rows of `09_LISTENING_REVIEW_PACK.csv`, {N["heard_rows"]} rows filled) |
| Expert or domain reviewer | **0** |
| Original MP4 playback by a reviewer | none recorded |

Do not read any count below as verified scenes, retention evidence or channel-wide rates.

## Counts and where they come from (source file, as of 2026-11-23)
| Quantity | Value | Source |
|---|---|---|
| Inventory rows (videos listed) | {N["inv"]} (88 media files present, 4 missing) | `forensics_2026-11-23/03_CHANNEL_MASTER_INVENTORY.csv` |
| Audit-layer detector shots (44 videos) | {N["shots"]} detector shots, **not** verified scenes | `forensics_2026-11-23/ledgers_measured/ALL_SHOT_LEDGER.csv` |
| Audit-layer detector events | 2,160, machine detections, not interpreted | `forensics_2026-11-23/ledgers_measured/ALL_EVENT_LEDGER.csv` |
| Campaign-layer shots (44 other videos) | 718 shots, 2,708 events (ledgers live in the repo under `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/`, not copied) | `forensics_2026-11-23/13_FINAL_REPORT.md` |
| Boundary review sample | {N["reviewed"]} shots, same-model, stratified and clustered; descriptive only | `forensics_2026-11-23/review_sample/REVIEWED_SAMPLE.csv`, `14_SAMPLE_DESIGN_ANALYSIS.json` |
| Literal scene coding (Phase 6.4, owner decision) | {N["tranA"]} of 1,437 ledger shots coded (tranche A), 1,177 not coded (B 594, C 583); 3 stills per shot, same-model | `forensics_2026-11-23/phase15_scene_coding/PROGRESS.md`, `A_ten_SCENE_CODING.csv` |
| Style frames | {N["style"]} purpose-selected frames (+160 episode frames) | `forensics_2026-11-23/06_STYLE_MEASUREMENTS_125.csv` |
| Science rows | {N["sci"]} rows in `07_SCIENCE_CLAIM_CHECKS.csv` (SC01 to SC10 plus SC03B rework); {N["epi"]} episode rows | `forensics_2026-11-23/07_*` |
| Rule ledger | {N["rules"]} rules (K01 to K23), draft, operative text revised 2026-11-23 | `forensics_2026-11-23/knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv` |
| Listening items | {N["prio"]} priority + {N["add"]} additions, none listened | `09_LISTENING_PRIORITY_ITEMS.csv`, `14_LISTENING_PACK_ADDITIONS.csv` |

The 563 (unreviewed shots of the 719) and 1,177 (uncoded shots of 1,437) remainders belong to different schemes and must not be added. A detector shot is not a verified scene.

## Latest corrections and where they live
- Reconciliation of the Codex review and the external audit: `forensics_2026-11-23/14_RECONCILIATION_CODEX_AND_EXTERNAL_AUDIT_2026-11-23.md` and the final report v4 `forensics_2026-11-23/13_FINAL_REPORT.md`.
- Operative rule text revised (old text kept in column `rule_text_prior_v3`): `knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv`; pre-edit copies of every edited file: `versions_before_reconcile_2026-11-23/`.
- Science: SC02 now QUALIFIED, SC03 OPEN, E09g wording discrepancy (about 1,900 to 2,250 times, not 2x) recorded in `07_SCIENCE_CLAIM_CHECKS.csv`, `07e_EPISODE_CLAIM_CHECKS.csv`.
- Nothing in this archive was rewritten to hide history: older versions are kept (`*_v1_*`, `*_v2prelight_*`, `versions_before_reconcile_2026-11-23/`).

## Known stale or contradictory wording (left as is; NOT rewritten here)
Reported by the Codex readiness review and confirmed by text search on the source files at creation time:
| Where | Stale statement | Latest position |
|---|---|---|
| `forensics_2026-11-23/12_CODEX_CLAUDE_WORKFLOW.md` line 24; `forensics_2026-11-23/knowledge_base_draft/WHAT_IF_SCRIPT_TO_VIDEO_PLAYBOOK.md` line 5 (and the older `*_v2prelight_*` copies) | "narration from 0 s" | rule K06 and hypothesis H2: audio energy near 0 s is measured, speech onset is UNVERIFIED (the Whisper 0.00 s is an artefact); no listening |
| `forensics_2026-11-23/knowledge_base_draft/WHAT_IF_SCIENTIFIC_ANIMATION_GRAMMAR.md` line 5 | "Observed changes are mostly pop-ons, scene swaps and write-ons (K16)" | K16: camera-like moves occur, frequency unmeasured |
| `forensics_2026-11-23/07_SCIENCE_CLAIM_CHECKS.md`, `07e_TEN_EPISODE_PHYSICS_STUDIES.md` | earlier category counts and an earlier 2023-benchmark E09g paragraph precede the corrected text | read the reconcile columns in the CSVs and the addenda |

Read the latest qualified statement, not the first numeric summary.

## Layout
`forensics_2026-11-23/` primary research folder (paths relative to the original folder are preserved) | `codex_independent_review_2026-11-23/` | `codex_readiness_review_2026-11-23/` | `inputs/` original master directive and external audit | `earlier_audits_2026-11-17/` (83-script audit with transcripts; single-video CT scan, text only) | `earlier_preserved_evidence_2026-10-21/` | `archive_tools/` scripts that built this archive | `MANIFEST.csv`, `MANIFEST.json`, `EXCLUDED_FILES.csv`, `DEDUP_MAP.csv`, `EXTERNAL_LOCATIONS_AND_DECISIONS.csv`, `REPO_EXISTING_WHATIF_PATHS_ON_ORIGIN_MAIN.csv`, `REPO_WHATIF_FILES_ONLY_ON_OTHER_BRANCH.csv`, `verify_manifest.py`.

## Included
{summ["included_files"]} source files ({summ["included_bytes"]/1048576:.1f} MB) copied byte for byte, plus generated archive files (listed in MANIFEST with status GENERATED).
| Category | Files |
|---|---|
{cat}

| Source group | Files |
|---|---|
{grp}

## Excluded (full list with SHA-256 in `EXCLUDED_FILES.csv`)
| Reason | Files | Size |
|---|---|---|
{exc}
Also not listed file by file: {summ["venv_pruned_files"]:,} files of a Python virtual environment (`.venv-demucs`), and one `.pyc`. Frame images are described by the CSV and JSON metadata that are included (`phase15_scene_coding/*.csv`, `07*_SAMPLE_FRAMES.csv`, ledgers). The 88 source MP4s, the book PDF and its parts, and other unrelated Downloads items are excluded (`EXTERNAL_LOCATIONS_AND_DECISIONS.csv`). Eight `*.log` files are excluded because the repository `.gitignore` ignores `*.log` (line 31); they are build logs only.

## Deduplication
Two files are byte-identical to files already on origin/main and were not copied (mapping in `DEDUP_MAP.csv`). {len([1 for k, v in collections.Counter(m["sha256"] for m in man if m["status"] == "INCLUDED").items() if v > 1])} groups of internal exact duplicates are kept on purpose (version and provenance copies) and listed there.

## Unavailable or not done
Listening, expert review, Machine A data, source-article correspondence, book-art comparison, scene coding of tranches B and C, 2,160 event interpretations, any original video or asset.

## Rights and privacy notes
The GitHub repository is **public**. The archive includes transcripts and ASR text of third-party (xkcd) videos as research data; the same transcripts are already tracked on origin/main under `research/what-if-scripts/`. No secrets were found by a pattern scan of included text (API keys, tokens, private keys, passwords, e-mail addresses). Local paths contain the Machine B user name, as many existing repo documents do. No xkcd art, book pages or audio are stored.

## Verify
`python3 -I research/xkcd-what-if-research-archive/verify_manifest.py` recomputes SHA-256 and size for every file listed in `MANIFEST.csv` and reports unlisted files.
'''
open(R + 'README.md', 'w').write(readme)
# 5) final manifests: sourced rows + generated rows
gen = []
for dp, _, fs in os.walk(R):
    for f in fs:
        p = os.path.join(dp, f); rel = os.path.relpath(p, SP + '/stage')
        if rel in (ARCH + 'MANIFEST.csv', ARCH + 'MANIFEST.json'): continue
        if any(m['repo_path'] == rel for m in man): continue
        gen.append(dict(repo_path=rel, source_path='GENERATED ' + NOW + ' by archive_tools', size_bytes=os.path.getsize(p), sha256=sha(p),
                        git_blob_sha1='', category='archive_generated', source_group='archive_generated', status='GENERATED', existing_repo_path_on_origin_main=''))
allrows = man + gen
cols = ['repo_path', 'source_path', 'size_bytes', 'sha256', 'git_blob_sha1', 'category', 'source_group', 'status', 'existing_repo_path_on_origin_main']
with open(R + 'MANIFEST.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=cols); wr.writeheader(); wr.writerows(sorted(allrows, key=lambda m: (m['repo_path'] or m['source_path'])))
json.dump(dict(archive=ARCH, created_utc=NOW, base_commit=BASE, branch='research/xkcd-what-if-research-archive', status='DRAFT / self-reviewed / partial Codex review only; listening 0; expert 0; not complete',
               summary=summ, counts_from_sources=N, note='MANIFEST.csv and MANIFEST.json cannot list their own hashes; every other file is listed.', files=allrows),
          open(R + 'MANIFEST.json', 'w'), indent=1)
print('generated files:', len(gen), 'manifest rows:', len(allrows)); print(json.dumps(N))
