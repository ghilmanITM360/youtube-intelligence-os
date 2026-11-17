# YIOS Research Export — folder decision audit

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

Target root `/Users/ghilmankhan/Documents/YIOS-Research-Export-2026-10-21`; repository `/Users/ghilmankhan/workprojects/youtube-intelligence-os`. Current branch `codex/what-if-archive-main-integration`, HEAD `badec432bbf5610748123b3f0e0bcb9cdb25fa10`; live main `08e719264e31ecd82de24f8eeb8f065c08359fe5`. Authenticated GitHub metadata confirms private repository; 40 live branch heads observed read-only. Fresh API main/Finance commit evidence retained.

Local architecture sources read: `README.md`, `AGENTS.md`, `docs/YIOS_MASTER_PLAN.md`, `docs/YOUTUBE_CHANNEL_REGISTRY.md`, `docs/PROVENANCE.md`, `data/catalog/README.md`; SQLite opened mode=ro&immutable=1. Some dated docs show old counts (71 /2,005); current directly counted SQLite is75 /2,303, and older doc counts are not silently substituted. Selected inventory current rows10channels/667videos is separate.

- `COMPLETE_SOURCE_FILE_INVENTORY.csv`: all5,373 target files, original sizes/flags/access/prior SHA evidence/primary decision.
- `REPOSITORY_CONTENT_CROSSWALK.csv`: physical file/wrapper decisions; no invented original-byte match.
- `EMBEDDED_SOURCE_IDENTITY_CROSSWALK.csv`: all9,011 source versions; exact SHA/ref/commit/blob/local evidence. Local hash reuse is prior hash + current stable size/mtime where not fresh six-file read, explicitly weaker than fresh reading.
- `EXPORT_IDENTITY_REGISTRY_COMPARISON.csv`: complete identified-key list and exact first source lineage.
- `UNIQUE_USEFUL_DATA.csv`: 453 unresolved source versions plus six known local publication gaps; **not 459 proven unique missing assets**.
- `DUPLICATES_AND_SEMANTIC_OVERLAPS.csv`: 8,558 exact source counterparts; no wrapper deletion inference.
- `evidence/findings_census.json`: all record kinds and1,157 schemas; `embedded_source_index.json` all source metadata.
- `evidence/selected_embedded_document_excerpts.json`: exact JSONL lines and truncation. Historical deep-knowledge audit line2; What If contract line134634; six script documents SOURCE_REGISTER starts at line562983; five Markdown documents are at lines563035–563039; twelve-channel resume line1071440 and reconciliation line1071442. Source excerpts preserve historical assertions; no live financial/scientific claim verification is implied.
- `VALIDATION.json`, `SHA256SUMS`, `CONTINUATION_HANDOFF.md`: final scope, preservation comparisons, blockers and integrity seal.

Agla folder automatically start nahi hoga. Is folder par integration/deletion ya cloud reads ka agla scope owner alag decide karega.

Additional evidence: `evidence/published_identity_byte_proof.json` independently checks all1,239/871 registry-absent identity strings in97 exact-published source blobs (3,798,344bytes read); all found. This proves identity occurrence, not complete row equivalence or a completed audit. Embedded source-hash matches identify a recorded original version; they do not validate every transformed export record against that original.

Object-store incident detail: `evidence/object_store_observation.json` records87 pack-related files with creation/mtime during the audit interval. Automatic Git network descendants were directly observed; per-pack actor attribution and pre-audit object-store baseline are unavailable. Zero Git object writes cannot be certified. No objects were removed to conceal or reverse the incident.

Final acceptance: 46 checks passed, 1 failed. Status PARTIAL_CONTENT_ACCESS_BLOCKED_WITH_GIT_SAFETY_INCIDENT. Target metadata changed paths=0; all details retained in VALIDATION.json. Latest usage22% five-hour/59%weekly, disk14,957,174,784bytes free, memory37%free; paid0/reset2available, none redeemed. Automation PAUSED. These resource values are observation-time, not a future transfer gate.
