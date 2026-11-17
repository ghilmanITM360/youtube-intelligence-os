import pathlib,json,csv,collections,hashlib,os,datetime,subprocess
O=pathlib.Path(__file__).parent;E=O/'evidence';R=pathlib.Path('/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21');P=pathlib.Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os')
meta=json.loads((E/'initial_metadata.json').read_text());sources=json.loads((E/'embedded_source_index.json').read_text());sc=list(csv.DictReader((O/'EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv').open()));sm={r['source_id']:r for r in sc};census=json.loads((E/'findings_census.json').read_text());cmp=json.loads((E/'git_tree_comparison.json').read_text());dups=json.loads((E/'record_value_duplicates.json').read_text());docs=json.loads((E/'selected_embedded_document_excerpts.json').read_text());six=json.loads((E/'six_local_research_hashes.json').read_text())
prior=list(csv.DictReader(open('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/ALL_YIOS_LOCAL_ASSETS_INVENTORY.csv')));prior={r['relative_path']:r for r in prior if r['root_directory']==str(R)};sourcehash=collections.defaultdict(list)
for s in sources:sourcehash[s['source_sha256']].append(s['source_id'])
def csvout(name,rows,fields=None):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def write(n,s):(O/n).write_text(s)
inv=[];cw=[]
for r in meta:
 rel=r['relative_path'];old=prior.get(rel,{});group=rel.split('/')[0] if '/' in rel else 'ROOT_CONTROL';sha=census['sha256'] if rel=='ALL_RESEARCH_FINDINGS.jsonl' else old.get('machine_a_sha256','');association=sourcehash.get(pathlib.Path(rel).name.split('.')[0],[]) if group=='sources' else []
 purpose='Historical compressed original-source preservation container; exact payload unavailable' if group=='sources' else 'Historical remote-recovered Git object candidate; filename is not byte verification' if group=='remote_recovered' else 'Combined cross-ref export; preserves records and source lineage' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else 'Historical export control/report/index/tool; purpose inferred from name unless embedded evidence exists'
 status='FULL_STREAM_SCHEMA_CENSUS_SEMANTIC_SAMPLE' if not r['dataless'] else 'CONTENT_NOT_ACCESSIBLE'
 row=dict(relative_path=rel,absolute_path=str(R/rel),type=pathlib.Path(rel).suffix or 'extensionless',size=r['size'],allocated_bytes=r['blocks']*512,residency='ICLOUD_DATALESS' if r['dataless'] else 'RESIDENT',resident_bytes='UNKNOWN_PARTIAL_ALLOCATION' if r['dataless'] else str(r['size']),classification='PRESERVATION_CONTAINER' if group in ('sources','remote_recovered') else 'DERIVED_EXPORT_OR_CONTROL',content_access=status,sha256_evidence=sha,hash_authority='FRESH_COMPLETE_READ' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else 'PRIOR_AUDIT_ONLY_NOT_REVALIDATED_CURRENT_BYTES' if sha else 'NONE',mtime_ns=r['mtime_ns'],flags=r['flags'],purpose=purpose,references='evidence/embedded_source_index.json' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else ';'.join(association),sensitivity='PRIVATE_MIXED_RESEARCH_POTENTIAL_PERSONAL_ANALYTICS_RIGHTS_NO_PUBLICATION_REVIEW',primary_recommendation='KEEP_LOCAL_UNTIL_RECOVERY_PROVEN' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else 'NEEDS_FURTHER_VERIFICATION',cleanup='DO_NOT_DELETE' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else 'UNKNOWN_PRESERVE')
 inv.append(row);cw.append(dict(relative_path=rel,source_sha256_evidence=sha,local_yios='UNKNOWN',git_history='UNKNOWN',published_github='UNKNOWN',comparison='UNKNOWN',related_source_versions=len(association),related_source_identities=';'.join(association),relation_authority='FILENAME_ASSOCIATION_ONLY_NOT_CONTAINER_INTEGRITY' if association else 'FULL_RECORD_SOURCE_COMPARISON_IN_EMBEDDED_SOURCE_IDENTITY_CROSSWALK' if rel=='ALL_RESEARCH_FINDINGS.jsonl' else 'CONTENT_NOT_ACCESSIBLE',recommendation=row['primary_recommendation'],reason=purpose,cleanup=row['cleanup']))
csvout('COMPLETE_SOURCE_FILE_INVENTORY.csv',inv);csvout('REPOSITORY_CONTENT_CROSSWALK.csv',cw)
# Unknown is not evidence of unique content.
u=[]
for s in sc:
 if s['comparison']=='UNKNOWN' or 'casually-finance-script-intelligence/' in s['source_path']:
  u.append(dict(source_path=s['source_path'],source_id=s['source_id'],source_sha256=s['source_sha256'],export_records=s['export_records'],classification='ALREADY_LOCAL_UNTRACKED_PUBLICATION_GAP' if 'casually-finance-script-intelligence/' in s['source_path'] else 'UNIQUENESS_UNPROVEN',usefulness='Dated script/title/transcript/topic research; source-specific review before reuse' if 'casually-finance-script-intelligence/' in s['source_path'] else 'Potential historical source/recovery value; semantic classification incomplete',local_yios=s['local_yios'],published_github=s['published_github'],priority='P1' if 'casually-finance-script-intelligence/' in s['source_path'] else 'VERIFY_FIRST',recommendation='MERGE_UNIQUE_KNOWLEDGE_AFTER_APPROVAL' if 'casually-finance-script-intelligence/' in s['source_path'] else 'NEEDS_FURTHER_VERIFICATION',evidence='EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv#source_id='+s['source_id']))
csvout('UNIQUE_USEFUL_DATA.csv',u)
duprows=[dict(source_path=s['source_path'],source_id=s['source_id'],source_sha256=s['source_sha256'],match=s['comparison'],local_counterpart=s['local_counterpart'],git_blob=s['git_blob'],remote_ref=s['remote_ref'],remote_commit=s['remote_commit'],coverage='EXACT_UNCOMPRESSED_SOURCE_VERSION_NOT_COMPRESSED_WRAPPER',cleanup='UNKNOWN_PRESERVE',reason='An original-source exact match does not establish wrapper, record lineage, or independent backup redundancy') for s in sc if s['comparison']=='EXACT MATCH'];csvout('DUPLICATES_AND_SEMANTIC_OVERLAPS.csv',duprows)
write('CONTENT_ACCESS_AND_ICLOUD_LIMITATIONS.md',f'''# Content access and iCloud limitations

Observed UTC {datetime.datetime.now(datetime.timezone.utc).isoformat()} / 27 October 2026 Asia/Karachi.

Complete bounded metadata census: {len(meta):,} regular files, {sum(r['size'] for r in meta):,} logical bytes, {sum(r['blocks']*512 for r in meta):,} allocated bytes (allocation is not cloud recoverability). 5,372 UF_DATALESS files; one resident JSONL of 2,741,894,860 bytes. No symlink following; zero symlink files observed. No target hydration requested. Actual resident byte extent of dataless files cannot be established from blocks alone.

All 1,089,195 JSONL records parsed, full stream SHA-256 {census['sha256']}; zero parse errors. 1,157 kind/schema combinations. Full syntax/schema census is not complete semantic reading. Nineteen record-kind previews plus sixteen selected embedded document excerpts were inspected; two excerpts are truncated as recorded in evidence. Top-level reports, CSVs, index, manifest, Python and logs are CONTENT_NOT_ACCESSIBLE at their current original paths. They were not executed or silently reconstructed.

Sources are 9,011 exported source/version identities across 8,811 paths; these are neither physical target-file counts nor verified originals. source_sha256 is an embedded historical assertion until matched independently. Compressed filenames are association clues only. Binary_reference records do not restore original binary bytes even when reference_only is false.

Identity extraction checks explicit ID fields in top-level dictionaries and immediate list records, not every nested object, transcript text or URL. IDs are syntactically filtered, not independently verified public existence. SOURCE_INDEX / ALL_VIDEOS / ALL_CHANNELS actual contents remain inaccessible, so this is not an exhaustive canonical export CSV comparison.

Prior hash evidence: {sum(bool(r.get('machine_a_sha256')) for r in prior.values())} files in the prior audit. Those hashes are not fresh confirmation of unavailable cloud bytes. Content availability and cloud versions are unknown; no account-wide iCloud sync or upload-backlog guarantee.

Do not delete, hydrate in bulk, change sync settings or infer loss. Owner may later authorize a small named-file read of the primary controls and compression samples with a download limit, timeout and new append-only receipts. No such follow-up has been started.
''')
write('RECOMMENDED_YIOS_INTEGRATIONS.md','''# Proposed integrations — owner decisions only

No integration is executed or approved by this report. Existing schemas and modules govern; no new database is proposed.

## P0 — establish readable controls and original recovery

Source root `/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21/`. Prioritize `YOUTUBE_RESEARCH_MASTER_REPORT.md`, `SUMMARY.json`, `SOURCE_INDEX.json`, `SHA256_MANIFEST.json`, `LFS_DATABASE_RECOVERY.json`, `MISSING_DATA_AND_CONFLICTS.md`, extraction/recovery Python and logs, then named compressed-original samples. Current status CONTENT_NOT_ACCESSIBLE. Preserve exact files externally; no repo destination should be approved until readable bytes, redaction, dependency and recovery checks pass.

## P1 — six already-local unpublished script-intelligence documents

Original export records live in `ALL_RESEARCH_FINDINGS.jsonl` at lines 563034–563039 (exact document locators in embedded source index and selected excerpts). Existing exact current local bytes live under `/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/casually-finance-script-intelligence/`:

- `SOURCE_REGISTER.csv`: dated claim/source ledger; preserve source IDs, dates, URLs and distinctions between facts/calculations/interpretations.
- `SCRIPT_DNA.md`: observed hook/pacing/narration patterns; keep 16-transcript / six-Short denominator and negative cases.
- `TOPIC_RESEARCH.md`: historical editorial direction and ranked hypotheses; not today's financial advice or creator's unpublished plan.
- `TITLE_DNA.md`: 206-title historical snapshot, associations, overlapping heuristics and counterexamples; not causal virality rules.
- `TRANSCRIPT_COVERAGE.md`: historical 16/206 coverage, ASR and duplication limitations; cannot overwrite current coverage.
- `FINAL_SHORT_SCRIPT.md`: approval draft with stale dated financial assertions; do not publish or execute automatically.

Proposed destination is the same existing directory and exact same names, subject to source-writer and owner review. Do not add a second copy from this export. Keep exact archival text; any revised claims belong in a separately versioned reviewed revision. New normalized observations must use existing per-channel intelligence/provenance conventions, exact canonical channel/video IDs, source SHA, record line, observation date, evidence layer and review status. Add no new canonical Finance authority. Machine B Finance owner must decide any Finance merge/publication; protected Machine A research ownership remains in force.

Git tracking may suit reviewed text and sanitized ledger in the existing private repository, with rights/credential/analytics review first. Original audio/video and binary preservation stay outside ordinary Git. Required checks: fresh source hash and writer window, exact existing-file diff, UTF-8/CSV validation, source register referential integrity, explicit historical dates, rights/privacy review and conflict check against latest published Finance release. Current six-file SHA evidence is in evidence/six_local_research_hashes.json (77,142 bytes).

## P2 — registry integration is a separate data review

`EXPORT_IDENTITY_REGISTRY_COMPARISON.csv` lists 1,239 syntactically valid video identities and 871 channel identities absent from current registry. Every one's first observed source version is already exact-published in Git. These are not newly discovered missing repository assets. Examples: discovery/search hits, Finance expansion registers and Casually Finance metadata. Current registry has 75 channels and 2,303 videos; selected inventory has 10 channels and 667 videos. Never pool them or treat registry membership as completed audit status.

If owner later requests registration, use existing channel registry builder/input ledgers (`scripts/build_youtube_channel_registry.py`, `data/catalog/channel_registry/`) and supplied-source registration workflow. Map canonical channel ID, YouTube video ID, source dataset/run, publication/observation date, exact source locator and independent layer coverage. Deduplicate video ID while retaining distinct dated metric snapshots; unresolved identity and transcript gaps stay explicit. Register only source-authorized records after owner and Machine B review, not all 1,239/871 automatically.

## P3 — existing research should be referenced, not recopied

8,335 exported source versions match a live published branch's exact blob hash; 8,558 have an exact local/Git counterpart under the stated checks. See per-version crosswalk for full ref, commit, blob and SHA. This proves version availability in published Git history at those branch tips, not integration into main, original media recovery, LFS payload retrieval or current research truth. Reuse existing Finance/What If/global knowledge modules and reviewed source indexes; retain historical export lineage externally.

Forensic observations must follow `docs/WHAT_IF_INTEGRATION_WORKFLOW.md` and `docs/PROVENANCE.md`, retain timestamp/frame/table source references, and never become independent video samples or causal success claims. No new automation implementation is authorized.
''')
write('EXTERNAL_PRESERVATION_RECOMMENDATIONS.md','''# External preservation recommendations

Keep this entire target intact pending original-byte recovery proof. It is a cross-ref historical research/recovery snapshot, not a clean new competitor dataset.

- 5,130 `sources/*.source.gz`: potential original byte containers; all currently dataless. Names and embedded source hashes do not validate decompression, safe paths, original length or reconstructability. Verify bounded named members and source hashes before redundancy decisions.
- 204 `remote_recovered/<object-id>`: historical object recovery cache; actual original bytes unavailable. Confirm file SHA-1 Git-object identity, remote commit reachability, LFS pointer/payload distinction and dependent reports before cleanup. Do not infer bytes from filename.
- 39 root controls/exports: preserve exact historical checkpoint, report, source index, checksum, recovery errors and method scripts/logs. Only the combined findings JSONL is currently resident/readable. Top-level ALL_* CSVs and master report cannot yet be classified from actual contents.
- 2.74 GB findings JSONL: valuable combined record/source-lineage access. It includes binary references, not all original media. An exact JSON export regeneration has not been demonstrated. Keep externally with its newly measured SHA-256 and private access; do not add the giant file to ordinary Git.
- Original transcripts, thumbnails, media, editable projects, SQLite snapshots and mixed-private records require owner-approved private storage with original path, content hash, length, source/remote ID and independent retrieval receipt. This audit made no Drive upload or new cloud destination.

No full-folder independent original-byte recovery proof is established here. Prior V7 completion and current catalog LFS recovery do not establish recoverability of every historical export wrapper or old catalog version. Reference `/Users/ghilmankhan/YIOS-v8-readiness-20261026T235710Z/LFS_REMOTE_PAYLOAD_VERIFICATION.csv` as a prior observation, not a fresh download. No new LFS bytes were requested by this folder audit.

Privacy: authenticated repository is private. Keep export and audit owner-only; do not publish mixed content, derived private analytics, personal data, token-containing operational logs or third-party transcripts without specific review. Hash identity is not redistribution permission.
''')
write('MANUAL_CLEANUP_REVIEW.md',f'''# Manual cleanup review — no deletions authorized

Current file-level safe-to-consider count: ZERO. All target originals remain DO_NOT_DELETE or UNKNOWN_PRESERVE.

{len(duprows):,} embedded source versions have exact local/Git counterparts, including {cmp['counts']['published_github']['YES']:,} exact-published versions. This does not prove the 5,130 compressed containers, 204 recovery objects or export controls are independently recoverable or redundant. Per-version identities cannot be substituted for per-file checks.

Among 1,010,717 selected tabular/SQLite/archive-row records, 514,733 repeated occurrences share exact kind + canonicalized value with another occurrence (495,984 unique values). Different provenance and snapshots may legitimately repeat values. Do not delete source rows, compressed originals or a whole export based on this aggregate. The comparison excludes other record kinds and is not a global content deduplication of all source bytes.

Eventual MANUAL_REVIEW_SAFE_TO_CONSIDER candidates could include verified duplicate wrappers or reproducible intermediate aggregates, only after: (1) current exact bytes are read/hash checked; (2) independent private restore succeeds; (3) original source and all method/version inputs exist; (4) lineage, time coverage and dependent indexes are preserved; (5) protected owner confirms no active dependency. No destructive commands are provided. Logs and recovery scripts have provenance value until full method/rebuild verification.
''')
# Owner report, Roman Urdu first, bounded conclusions explicit.
write('YIOS_RESEARCH_EXPORT_FOLDER_DECISION_REPORT.md',f'''# YIOS Research Export — folder decision audit

27 October 2026, Machine A. **Decision report tayyar hai, lekin poori content classification BLOCKED/PARTIAL hai.** 5,372 iCloud placeholders ke original bytes safely available nahi thay. Git ke automatic lazy-recovery subprocess ka safety incident bhi neeche documented hai. Yeh report integration, deletion ya upload ki approval nahi hai.

## Seedhi baat

Yeh folder purani YIOS research ko mukhtalif Git branches, tables, archives aur recovered sources se ek jagah dekhne ke liye banaye gaye historical export ki shakal rakhta hai. Is ka saboot resident `ALL_RESEARCH_FINDINGS.jsonl` ke har record mein source path, SHA-256, refs, snapshot aur record-kind fields hain. Creator scripts aur top-level master report read nahi ho sake, is liye un ka asal workflow mukammal verify nahi hua.

**5,373 files, 3,710,635,920 logical bytes (3.71 GB)** mile. `sources/` mein 5,130 compressed containers, `remote_recovered/` mein 204 objects aur root par 39 controls/exports hain. Sirf **ek target file** actually poori stream read hui: `ALL_RESEARCH_FINDINGS.jsonl`, 2,741,894,860 bytes. Baqi 5,372 files dataless hain; un ka listed size local ya independently recoverable original bytes ka proof nahi.

JSONL ke **1,089,195 records** poore parse hue, zero syntax errors. **9,011 source-version identities / 8,811 paths** hain; yeh physical files ya independent research samples ka count nahi. Full schema census ke saath 19 kind previews aur 16 selected embedded document excerpts inspect hue. Har paragraph ka complete semantic reading claim nahi hai.

## Kya useful hai aur kya pehle se hai?

- **8,335 source versions published Git branch blobs se exact hash match hain.** Inhein dobara main mein copy karna munasib default nahi. `EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv` har match ka commit/ref/blob/SHA deta hai. Published branch par hona main mein merged hona nahi.
- **8,558 source versions ka exact local ya Git counterpart** mila; 453 ka exact counterpart is bounded comparison se establish nahi hua. Yeh 453 “unique missing original files” nahi: is mein older snapshots, ignored inputs, large un-hashed candidate blobs aur unresolved recovery evidence shamil hain.
- Current local channel registry mein **75 channels / 2,303 videos** hain. Export ke explicit ID fields mein 3,542 syntactically valid video IDs aur 932 channel IDs mile. **1,239 videos aur 871 channel IDs registry mein nahi**, magar un sab ka first observed source version GitHub ki published branch mein exact present hai. Is liye unhein missing-from-GitHub kehna ghalat hoga. Exact lists `EXPORT_IDENTITY_REGISTRY_COMPARISON.csv` mein hain; nested/URL identities ka exhaustive census nahi.
- **Six script-intelligence files** pehle se main checkout ke untracked research folder mein exact maujood hain: total **77,142 bytes**, fresh hashes stable. Published equivalent is audit mein prove nahi hua. In ka research aur original script value hai; dobara export se copy ki zarurat nahi. Finance/source owner review ke baad isi existing location ko publication/preservation ke liye consider karein.

## YouTube ke kaam mein istemal

`TITLE_DNA.md` historical 206-title sample mein title features aur strong/weak examples rakhta hai. Yeh idea aur packaging hypotheses de sakta hai; title ne views cause kiye, yeh prove nahi karta. `SCRIPT_DNA.md` aur `TRANSCRIPT_COVERAGE.md` historical 16 transcripts / six Shorts ke sample ko explain karte hain. `TOPIC_RESEARCH.md` dated editorial direction aur `FINAL_SHORT_SCRIPT.md` approval draft deta hai. Draft ke October financial assertions current independently revalidate nahi kiye gaye; seedha publish na karein.

Finance master-report excerpt khud historical sampled checkpoint aur newer full-population reports ki taraf ishara karta hai. Current Finance branch `61f26b5ca9a7bd39c0aa2b63780bb33c18d29cff` ko purane export statuses se replace nahi karna. Twelve-channel metadata excerpt 445 unique historical videos aur unresolved three-upload difference batata hai; yeh acquired original transcripts ya completed deep audits ka proof nahi. What If contract source-declared observations, held identities aur production hypotheses ko alag rakhta hai. Existing provenance workflow hi istemal hona chahiye.

## Owner decision table

| File / group | What it contains | Useful? | Exists in YIOS? | Pushed to GitHub? | Recommendation | Why? |
|---|---|---|---|---|---|---|
| `ALL_RESEARCH_FINDINGS.jsonl` | Cross-ref extracted records, text, tables, binary references | YES | PARTIAL | PARTIAL | KEEP_LOCAL_UNTIL_RECOVERY_PROVEN | Thousands of exact original-source matches; this exact 2.74 GB export/rebuild not proven |
| Six `research/casually-finance-script-intelligence/*` embedded versions | Title/script/topic methods, source ledger, draft | YES | YES | UNKNOWN | MERGE_UNIQUE_KNOWLEDGE_AFTER_APPROVAL | Already exact local/untracked; do not copy twice; owner review first |
| 8,335 published embedded source versions | Existing research/source bytes in branch tips | YES | PARTIAL | YES | ALREADY_IN_REPO_EXACT | Per-source hashes/refs/commits; not all on main |
| `ALL_VIDEOS.csv`, `ALL_CHANNELS.csv` | Named export tables; actual schema/content unreadable now | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Do not substitute JSONL-derived identities for these exact CSVs |
| `YOUTUBE_RESEARCH_MASTER_REPORT.md`, `CHANNEL_URL_LIST.md`, `MISSING_DATA_AND_CONFLICTS.md` | Named historical summaries/limits; original text unavailable | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Titles and prior hashes cannot prove actual information or redundancy |
| `SOURCE_INDEX.json`, `RESEARCH_FILES_INVENTORY.csv`, `SHA256_MANIFEST.json` | Named lineage/integrity controls | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Essential to original-source recovery decisions once readable |
| `VERIFIED_PROJECT_CHECKPOINTS.json`, progress/status records, LFS recovery controls | Historical completion/recovery assertions | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Must preserve dates; a declared verification is not this audit's verification |
| `sources/` — 5,130 gzip containers | Candidate preserved original bytes | UNKNOWN | PARTIAL | PARTIAL | NEEDS_FURTHER_VERIFICATION | Embedded originals often match; compressed payloads not read or decompressed |
| `remote_recovered/` — 204 objects | Historical recovery-object candidates | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Object-like names do not validate bytes, remote reachability or LFS payload |
| Six Python tools and six logs | Possible export/recovery procedure and incident provenance | UNKNOWN | UNKNOWN | UNKNOWN | NEEDS_FURTHER_VERIFICATION | Dataless, not executed; do not call regenerable without exact inputs |

## Kya integrate karein, kya separate rakhein?

Priority 0: original controls aur compressed-source recovery ko bounded named-file verification se samjhein. Priority 1: six already-local research documents ko existing source owner ke saath review karein; koi new canonical Finance database na banayein. Priority 2: owner agar chahe to published source identities ki controlled registry mapping karein, completed audit flags invent na karein. Priority 3: existing branch research ko index/reference karein, mass copy na karein.

Large combined export, historical compressed originals, binary snapshots, mixed-private data aur recovery receipts external private preservation mein rahen. Small sanitized research documents/portable provenance indexes existing repo conventions mein suitable ho sakte hain. Detailed exact source/destination, schema, deduplication, privacy and test conditions `RECOMMENDED_YIOS_INTEGRATIONS.md` mein hain. Har proposal future owner approval hai, executed change nahi.

## Kya redundant ya delete ho sakta hai?

Tabular comparison ke 1,010,717 records mein 514,733 repeated value occurrences mile; provenance alag ho sakti hai. Yeh disk cleanup list nahi. **Abhi zero target files deletion ke liye safe-to-consider certified hain.** Original compressed bytes, cloud recoverability, dependencies aur exact rebuild proof ke baghair sab ko preserve karein. Main report, manifests, scripts/logs aur unknown sources bina additional verification delete na karein. `MANUAL_CLEANUP_REVIEW.md` proof conditions deta hai; koi destructive command nahi.

## Trust aur blockers

Poora target metadata inventory complete hai. Actual target payload reading **1/5,373 files** hai; 5,372 CONTENT_NOT_ACCESSIBLE. 9,011 embedded source versions ki bounded exact comparison complete hai; 8,350 candidate Git blobs /765,719,373 bytes hashed, max25 MB each and total768 MB cap. Remaining candidate blobs un-hashed hain. Arbitrary all-history deleted versions ka exhaustive scan nahi.

Git's partial-clone configuration `remote.origin.promisor=true` thi. Initial `git ls-tree` missing-tree read ne automatic network-recovery descendants start kiye; audit-owned process aur attributable orphan descendants rok diye gaye. No explicit fetch command was requested, lekin **implicit fetching/object-store writes ko rule out nahi kar sakte**. Yeh user ke no-fetch boundary ke mutabiq safety incident hai. Baad ke reads lazy-fetch disabled thay. No object deletion/reversion attempted. See `evidence/GIT_LAZY_FETCH_SAFETY_INCIDENT.json`. Final tracked/status/stash/worktree/ref comparisons `VALIDATION.json` mein exact hain; object store ke liye initial complete snapshot nahi tha. Is liye blanket “Git unchanged/no downloads” certificate nahi.

No source content overwrite, integration, Drive upload, commit/push, ownership change, script execution from target or iCloud bulk hydration was performed. Audit scripts ran only from this external output directory. V7/V8 automation remains paused subject to final receipt. Source mtime/size/flags checks and all report checksums are recorded. Head/branch/worktree preservation does not prove object database immutability.

## Technical evidence and locators

Target root `{R}`; repository `{P}`. Current branch `codex/what-if-archive-main-integration`, HEAD `badec432bbf5610748123b3f0e0bcb9cdb25fa10`; live main `08e719264e31ecd82de24f8eeb8f065c08359fe5`. Authenticated GitHub metadata confirms private repository; 40 live branch heads observed read-only. Fresh API main/Finance commit evidence retained.

Local architecture sources read: `README.md`, `AGENTS.md`, `docs/YIOS_MASTER_PLAN.md`, `docs/YOUTUBE_CHANNEL_REGISTRY.md`, `docs/PROVENANCE.md`, `data/catalog/README.md`; SQLite opened mode=ro&immutable=1. Some dated docs show old counts (71 /2,005); current directly counted SQLite is75 /2,303, and older doc counts are not silently substituted. Selected inventory current rows10channels/667videos is separate.

- `COMPLETE_SOURCE_FILE_INVENTORY.csv`: all5,373 target files, original sizes/flags/access/prior SHA evidence/primary decision.
- `REPOSITORY_CONTENT_CROSSWALK.csv`: physical file/wrapper decisions; no invented original-byte match.
- `EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv`: all9,011 source versions; exact SHA/ref/commit/blob/local evidence. Local hash reuse is prior hash + current stable size/mtime where not fresh six-file read, explicitly weaker than fresh reading.
- `EXPORT_IDENTITY_REGISTRY_COMPARISON.csv`: complete identified-key list and exact first source lineage.
- `UNIQUE_USEFUL_DATA.csv`: 453 unresolved source versions plus six known local publication gaps; **not 459 proven unique missing assets**.
- `DUPLICATES_AND_SEMANTIC_OVERLAPS.csv`: 8,558 exact source counterparts; no wrapper deletion inference.
- `evidence/findings_census.json`: all record kinds and1,157 schemas; `embedded_source_index.json` all source metadata.
- `evidence/selected_embedded_document_excerpts.json`: exact JSONL lines and truncation. Historical deep-knowledge audit line2; What If contract line134634; six script documents lines563034–563039; twelve-channel resume line1071440 and reconciliation line1071442. Source excerpts preserve historical assertions; no live financial/scientific claim verification is implied.
- `VALIDATION.json`, `SHA256SUMS`, `CONTINUATION_HANDOFF.md`: final scope, preservation comparisons, blockers and integrity seal.

Agla folder automatically start nahi hoga. Is folder par integration/deletion ya cloud reads ka agla scope owner alag decide karega.
''')
print('reports',len(inv),len(cw),len(u),len(duprows))
