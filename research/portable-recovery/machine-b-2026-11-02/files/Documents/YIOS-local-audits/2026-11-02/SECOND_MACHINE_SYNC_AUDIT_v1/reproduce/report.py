from audit import *
from datetime import timedelta

def size(n):return f'{n:,} bytes ({n/1024**2:.2f} MiB; {n/1024**3:.3f} GiB)'
def table(headers,rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |',*['| '+' | '.join(str(v).replace('|',' / ').replace('\n',' ') for v in r)+' |' for r in rows]])
def main():
 c=read('finance/canonical-summary.json');a=read('finance/machine-a-published-summary.json');sync=read('synchronization.json');clean=read('cleanup_summary.json');wts=read('worktree_clone_inventory.json');matrix=read('branch_matrix.json');pop=read('population_counts.json');val=read('validation_results.json');visual=read('visual_packages.json');port=read('portability_summary.json');media=read('media_integrity_summary.json');stash=read('stash_summary.json');books=read('workbook_reconciliation.json');storage=read('git_storage_observation.json');lf=list(csv.DictReader((OUT/'lfs_presence.csv').open()));counts=read('finance/evidence_counts.json');locations=read('location_totals_after.json')
 audit_at=now();local=datetime.now(timezone(timedelta(hours=5))).isoformat()
 write('audit_metadata.json',{'package_version':1,'package':'SECOND_MACHINE_SYNC_AUDIT_v1','owner_date':'2026-11-02','generated_at_utc':audit_at,'generated_at_asia_karachi':local,'repository':'ghilmanITM360/youtube-intelligence-os','root':str(ROOT),'output':str(OUT),'scope':'Repository synchronization, safe exact-file cleanup and branch/data/evidence audit; no new research, writer transfer, PR mutation, push or scheduler edit.','status':'AUDIT_COMPLETED_WITH_EXPLICIT_DATA_AND_PORTABILITY_ISSUES','freshness':'Authenticated initial fetch and final independent live branch read; exact times and SHAs in remote/ and after/.','interpretation_policy':'Measured counts and fresh checks distinguished from published declarations, historical owner reports and unresolved external state.'})
 wt_table=table(['Path / branch','Full HEAD','Upstream / delta','State'],[[f"{r['path']} / {r['branch']}",r['head_after'],f"{r['upstream']} / {r['ahead']} ahead {r['behind']} behind",'CLEAN'] for r in wts])
 write('README.md',f'''# YIOS second-machine synchronization and complete project audit — v1

Owner date: 2026-11-02 (Asia/Karachi). Generated {local}. Machine `Users-MacBook-Pro.local`, macOS26.2/25C56, user `ghilmanislam360`. Repository authenticated as `ghilmanITM360`; private repository identity verified. All output is outside the research checkout at `{OUT}`.

**Result:** all24 local branches and all3 existing linked checkouts already matched their own fetched upstreams. There were no staged, unstaged or nonignored untracked changes. No fast-forward would change a ref; no checked-out branch was moved. `main` is `{git('rev-parse','origin/main')}`. The primary checkout is Finance, not `main`.

**Critical distinction:** canonical Finance/OPEN-DRAFT PR36 remains `{c['sha']}` with461/1,612 accepted limited-evidence audits. Separate published Machine A branch `{a['sha']}` has554/1,612, is44 commits beyond canonical and contains93 additional completed IDs. Its work is recovered in local Git objects, not merged into canonical/default. No push, PR36 change, ownership transfer or research integration occurred.

**Cleanup:** exactly3 proven disposable paths; gross {size(clean['gross_logical_bytes_removed'])}; compressed verified recovery {size(clean['recovery_compressed_bytes'])}; net logical savings {size(clean['net_logical_bytes_reclaimed_before_other_audit_outputs'])}. No raw evidence deleted. Finder metadata caused an invalid-ref Git integrity failure; removing that exact metadata file fixed it. Separate background object-layout changes were observed and verified; their space delta is not credited to cleanup.

**Research:** canonical461 accepted /16 partial /17 blocked /1,118 pending; separate Machine A554 /16 /17 /1,025. These are alternative versions of the same1,612 videos. Full-evidence completion is0, and visual/full-AV signoff is separate.

**Validation:** both canonical Finance validators,38Finance tests,2formatting tests, channel registry and final Git integrity pass. Full repository tests:459pass,1skip,1fail. Two provenance rows point to stale `.gitattributes` hashes. Workbooks agree with their JSONL at461/554 and have0error-type cells; the universe CSV is stale at430. Hosted CI did not start because of billing. This is not an all-project-valid certification.

**Media:**456/456 registered private media files hash-match here (454videos +2audio,4.06GiB). All five published CT001–005 source MP4 hashes match local files. Most CT frame/audio/private reviewer evidence is absent. CT006 has an older published PR21 package and hash-verified source inside `Downloads/CasuallyFinance.zip`; the separately reported new CheckpointB workspace is not found in the fetched CT namespace.

## Read the package

- [Roman Urdu owner report](OWNER_REPORT_ROMAN_URDU.md)
- [Before/after synchronization](SYNC_REPORT.md)
- [Every branch](BRANCH_AUDIT.md), [complete CSV](branch_matrix.csv), [JSON](branch_matrix.json)
- [Every worktree/clone](WORKTREE_CLONE_AUDIT.md), [CSV](worktree_clone_inventory.csv)
- [Data inventory](DATA_INVENTORY.md), [typed populations](population_counts.csv), [all files](files.csv), [after location totals](location_totals_after.csv)
- [Structure and authorities](STRUCTURE_AUTHORITY_MAP.md)
- [Cleanup and recovery](CLEANUP_RECOVERY.md), [exact ledger](cleanup_ledger.csv), [local path classifications](local_path_classifications.csv), [stash contents](stash_contents.csv)
- [Fresh validation and limits](VALIDATION_REPORT.md), [raw results](validation_results.json)
- [Portability/missing evidence](PORTABILITY_MISSING_EVIDENCE.md), [exact transfer entries](machine_a_transfer_requirements.csv), [LFS presence](lfs_presence.csv)
- [Ten practical workflows](DATA_USE_GUIDE.md)
- [Prioritized unresolved issues](UNRESOLVED_ISSUES.md)

`branches/trees/` contains a complete file/blob index for every fetched branch tip; `branches/diffs/`, `branches/commits/`, `branches/cherry/` and `branches/exclusive/` show changes, history and reuse. `structured_datasets.csv` indexes1,436unique CSV/JSONL blob versions across branches. `json_schema_record_counts.csv` indexes declared arrays; `published_validation_declarations.json` preserves historical declarations without presenting them as fresh validation. `branch_data_areas.csv` gives every branch's category counts and Git blob bytes.

## Evidence and recovery limits

The filesystem census is bounded to likely project locations, registered worktrees and discovered YIOS/media/handoff paths. Other volumes and arbitrary unrelated personal directories were not searched. Before/after snapshots have observation times; this is not an atomic disk image. Git object sizes do not include absent LFS payloads. File counts/projections are not independent video counts. APFS extent sharing is unknown. The recovery checkpoint covers the performed exact-file cleanup; large originals and the complete stash remain in place, not duplicated as a full off-device backup. Machine A's present local filesystem/processes and private cloud stores are not observable here.
''')
 write('SYNC_REPORT.md',f'''# Before and after synchronization

Initial authenticated remote observation: `{sync['initial_fetch_status']['observed_at']}`. Final independent GitHub branch read: `{sync['final_live_observed_at']}`. No remote heads moved between those observations. Exact46 remote SHAs are in `remote/freshness.json` and `after/github-branches.json`.

`gh api user` and repository metadata verified login/repository. `git fetch origin --no-prune --tags --no-recurse-submodules --no-auto-gc` succeeded without changing checked-out files. No branch/tag pruning. Default branch independently reported by GitHub: `main`; local/origin/default SHA `{git('rev-parse','origin/main')}`. No tags were enumerated. Repository is not shallow, has no configured sparse/partial clone or submodules observed, and uses one Git common directory.

{wt_table}

All24 local branch/upstream comparisons were0/0 before and after. No local branch commits were absent from every remote. There are46 fetched remote branches,24 local branches,7additional Codex recovery/checkpoint refs and1stash ref. All reference identities before/after are unchanged, including stash `{stash['sha']}`. No active merge/rebase/cherry-pick/revert/bisect/sequencer/index lock was found. `uv.lock` is a dependency lockfile, not writer ownership.

No safe update was skipped: every eligible ref was already at its verified upstream. There was no reason to switch the Finance checkout to default or to recreate a worktree. Active/shared research ownership was left untouched. Canonical Finance and the Claude worktree are the same commit but different assigned local branches; the coordination worktree preserves an implementation role.

Finance comparison: canonical vs Machine A `{read('finance/branch-comparison.json')['canonical_vs_machine_a_counts']}` (canonical-only / Machine-A-only commits). Canonical is an ancestor, but automatic fast-forwarding to a different research branch would change the publication/writer role and is outside this synchronization. The Machine A branch is latest on its own published research branch. It is not contained in canonical Finance or default.

The30remote branches not contained in default include research, production, docs, divergent historical work and isolated test-state histories. Sixteen remote tips are contained, including default itself; the other15are consolidation candidates only after role/evidence review. Divergent histories: packaging repair50/36, thumbnail research71/36, repository remediation4/119 and UI handoff1/143. The three isolated `yios-test/` branches have unrelated roots; no merge-base is reported for them. Patch-equivalence results are explicitly retained in the matrix/cherry appendices.

## Observed Git storage change

{storage['old_loose_paths_no_longer_present']:,} old loose-object paths disappeared during the audit. Every corresponding object ID still resolves from Git; all refs and stash are unchanged; final `git fsck --full --no-dangling` passes. Loose objects were already mostly packable in the initial count. Background maintenance/packing is an inference; the initiator was not established and no maintenance command was run by this audit. Before/after common-directory sizes are in `git_storage_observation.json`; this unrelated space change is not counted as cleanup savings.

No pushes, merges, rebases, force updates, PR edits, branch/worktree removals, stash clears or scheduled-task changes occurred.
''')
 write('WORKTREE_CLONE_AUDIT.md',f'''# Existing clones and worktrees

Bounded discovery found one independent YIOS repository and its two linked worktrees. The main root already existed; no clone/worktree was created. Search roots and depth limits are in `discovery.json`. No claim is made about unrelated folders or external volumes.

{wt_table}

Shared common directory: `{ROOT}/.git`. It is counted once, not once per worktree. No hardlinked inode duplicates were detected by the census; APFS clone extent sharing is unknown. Logical file duplication is not a measurement of reclaimable physical space.

{table(['Role','Logical bytes before / files','Keep/reuse assessment'],[[r['role'],f"{r['disk_before']['bytes']:,} / {r['disk_before']['files']:,}",r['needed_assessment']] for r in wts])}

The primary and Claude Finance checkouts are exact Git-HEAD duplicates, but have different local runtime/evidence and writer assignments. The primary has1,493ignored paths at checkpoint, the coordination worktree108, and Claude11. Ignored files are individually classified in `local_path_classifications.csv`. There are no nonignored untracked files or local-only branch commits. The large local stash and external media/preservation archives remain separate dependencies.

The primary is needed for current source/catalog/runtime/evidence access. Coordination is needed to retain the tested separate tooling implementation until real receiving-Mac acceptance. The Claude worktree is a possible future consolidation candidate after its owning session releases it and ignored paths are reviewed; it was not removed. A clean Git tree or published commit does not prove a worktree is disposable.

Local process inspection and the supported Codex chat snapshot identified this audit as the active YIOS task. Other YIOS chats seen were `notLoaded`; that is not a writer release. Claude Desktop/Codex service processes are present. No separate research/ffmpeg/validator writer process or live Git mutation lock was established at preflight. Machine A and other client activity remain unknown. Existing Finance ownership records conflict across branch roles: canonical retains Machine B sole-writer history, Machine A continuation declares separate owner-directed execution without verified Machine B release. No authority was silently transferred.

Source paths in this checkout resolve to registered DS workbooks/ZIPs and real LFS registry bytes. Media is under `Documents/YIOS-Media-Library`; all456registered bytes were verified. CT001–005 source videos exist here, but the complete Machine A frames/audio/reviewer working sets mostly do not. The `.env`, two empty legacy DBs, ignored raw acquisition files, external preservation directories and stash were retained. Full worktree/clone rows and dependencies are in CSV/JSON companions.
''')
 # Typed data summary deliberately avoids adding overlapping populations.
 primary=list(csv.DictReader((OUT/'primary_data_inventory.csv').open()))
 write('DATA_INVENTORY.md',f'''# Measured data inventory

The pre-cleanup filesystem census contains24,144file entries across34bounded scopes, logical {size(18064260968)}. It includes shared Git only once, excludes this new audit package, and excludes the nested Claude worktree from the parent count. This is a logical/allocated-block census, not deduplicated APFS physical extents. After cleanup and background Git packing, `location_totals_after.csv` provides measured updated scope totals. All originals were retained except the three exact disposable paths in the cleanup ledger.

## Primary checkout files before cleanup

{table(['Category','Files','Actual logical bytes','Unique hashes / hashed files'],[[r['category'],r['file_count'],r['actual_logical_bytes'],str(r['unique_content_hashes_bounded'])+' / '+str(r['hashed_files_bounded'])] for r in primary])}

Hash census excludes runtime/cache/dependency files and secrets, and is bounded at64MiB per file; separately registered large source and media hashes were checked beyond that bound. Across the census there are5,266identical-content groups within that bound, including repeated checkouts, source/extracted copies, projections and external preservation. A byte match does not make two observations independent. `identical_content_groups.csv` contains exact paths/hashes. Two inspection sidecars in the table have since been removed with verified recovery copies.

## Logical populations and acceptance

{table(['Population','Videos / files','Accepted or structural','Partial / blocked / pending'],[['Canonical Finance',1612,'461 limited;0 full','16 /17 /1,118'],['Separate published Machine A Finance',1612,'554 limited;0 full','16 /17 /1,025'],['Canonical registry','2,303 videos;75 channel identities','Metadata/source registry, not audit acceptance','2,291 real transcripts;12 placeholders;33 datasets'],['CT001–005','5 source videos','2 visual-only;0 full AV','3 partial;all human-AV signoff blocked'],['Older PR21 Casually Finance','18 selected','16 structural source packages','2 selected sources absent;overlap with later CT cases'],['Casual Economics sampled corpus',11,'11 structural;0 deep/AV','Optional listening/independent claim QA remains'],['Private local media','456 files','456 hash matches','389 high-confidence IDs;67 unresolved mappings'],['12-channel public metadata',445,'12 channels,metadata only','No deep-audit acceptance inferred'],['MonkeyExplains1999',76,'121raw minus45members-only','Finance uses63selected expansion records'],['BarelyEvolved',4,'Metadata snapshot','3local media files separately registered']])}

Finance disposition priority is explicit and mutually exclusive: all six dimensions complete → accepted; otherwise any missing-source block → blocked; otherwise authored complete/IN_PROGRESS → partial; remaining → pending. Baseline performance classification alone does not count as authored partial research. Original966and expansion646are disjoint by the registered universe, while branch versions and multiple projections are not added. Existing partial `TFtBWn9CWOU` is retained. Canonical Nick Invests has363registered originals and194fully completed limited-evidence records; supplementary 2026-10-23 reports are older snapshots.

## Catalogs and packages

`youtube_channel_registry.db` is actual SQLite, frozen SHA256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`, not an LFS pointer. It contains75channels,2,303videos/transcript rows,2,291real transcript FTS entries,33datasets and40standard packages. The existing registry validator passes. Its disposable rebuild has319artifact rows while the frozen DB has318; the validator's documented domain checks accept the snapshot. Do not rebuild/replace the frozen source merely to equalize that index count.

`youtube_inventory.db` is a different selected inventory:26datasets,10channels,667videos,668transcript references,6,953source-file rows,45,774discovered-file rows,5,172visual assets and604classifications. Historical discovered-file rows do not prove those45,774files are physically on this Mac. Two ignored legacy DB files are empty-schema SQLite; retained as unknown consumers. All four current DBs pass SQLite integrity; no foreign-key violations found. Schemas/counts are in `sqlite_inventory.json`.

66tracked workbook files have60unique content hashes (source/extracted copies are not independent datasets). `current_workbooks.csv` records every sheet's nonempty row structure. Finance has exactly one current combined workbook per branch version,1,612uniquevideo rows,42channel rows and966detail rows. All embedded JSON fields and six status columns compare equal to their branch's canonical JSONL. Cached dashboard counts agree at461/554;0Excel error-type cells. Native Excel recalculation was not tested. The `FINANCE_UNIVERSE.csv` identity/layer index still reports430complete in both versions: stale status projection, not an additional authority for current acceptance.

`structured_datasets.csv` indexes1,436unique CSV/JSONL blob versions across46branch tips, with record counts, explicit ID-key counts, duplicate-ID rows, status declarations, columns and all locations. Records with repeated IDs can be expected events/shots/search hits; duplicate-ID rows are not automatically duplicate videos. `json_schema_record_counts.csv` counts arrays without treating arbitrary JSON keys as records. One historical `channel_about.jsonl` blob has39non-JSONL lines; the raw source is preserved and no normalization claim is made.

## Claims, receipts, reviewer/state and production data

{table(['Finance version','Structured claims / videos','Source receipt entries','Calculation receipt entries','Exact stored-ASR witnesses'],[[x['scope'],str(x['counts']['structured_claim_rows'])+' / '+str(x['counts']['structured_claim_audit_videos']),x['counts']['primary_source_receipts'],x['counts']['calculation_receipts'],x['structured_claim_witness_checks'].get('MATCH',0)] for x in counts])}

Source receipt entries often repeat the same source across audits; they are not unique primary documents or a fresh verification of entailment. Older267video claim audits are narrative text, not structured claim rows. Canonical397and separate-branch1,820structured witnesses with exact ranges all match stored transcript bytes; other structured claims do not carry these exact range fields. Source confidence was only explicitly added in later Machine A batches; absent labels remain LEGACY_UNLABELLED, not upgraded to direct evidence. Receipts include direct inspection, snippets, recall and explicit source-unavailable limits. `finance/claims.csv`, `primary_source_receipts.csv`, `calculation_receipts.csv`, `transcript_read_receipts.csv` preserve those distinctions.

State/scene/event/composition/reviewer data exists in older PR21, Casual Economics, the38-Short editing corpus and later CT001–005 branches. CT001 has76parent states, CT002507states, CT003409states/254compositions/922motion rows, CT004530states/367compositions, and CT005has its current integrated_v2/second-pass ledgers. These counts use different versions/contracts and must not be summed as independent videos. Raw reviewer outputs are claims subject to integration, not automatic acceptance. Full branch file/category/row inventories are in `branch_data_areas.csv`, `branches/trees/`, `structured_datasets.csv` and `visual_packages.json`.

Production candidates exist on Dr Rehan test/heart-warning, Finance Short01/02 and three Senior Health production branches, with scripts/storyboards/assets/audio timing/QA/manifests and some rendered candidates. They are separate from research acceptance; several are explicitly QA_BLOCKED or owner-review candidates. LFS presence is independently listed:20locally present object versions (one current materialized source plus19stored older versions),6missing payload versions. No private media was downloaded or regenerated.

External YIOS recovery/preservation folders, handoffs, algorithm/creator audits, visual discovery material, transcript ZIPs, MP4s and archives are inventoried with actual paths and byte counts. ZIP central-directory members are counted separately from loose files in `zip_archives.csv`; archive copies are not added as new videos. Stash untracked content2,267files/843,095,575bytes is preserved in Git and mostly duplicated in external preservation, not copied into this audit as large media.
''')
 write('STRUCTURE_AUTHORITY_MAP.md','''# Structure and authority map

## Hierarchy and responsibilities

| Path/area | Role and authority |
| --- | --- |
| AGENTS.md, docs/Phases.md, docs/Decisions.md | Owner scope, phase and architecture rules; V1 complete does not mean every research population complete. No automatic V2. |
| data/raw/ | Immutable supplied/acquired source bytes. Never edit for a validator or projection discrepancy. |
| data/manifests/DS-*.md and *_FILES.csv | Durable dataset provenance, fingerprints, processing decisions, overlap and limitations. Shared mutable configuration hashes can become stale and require explicit correction. |
| data/extracted/channel-data/DS-*/packages/ | Standardized workbook/transcript ZIP packages derived/copied from registered source; byte-equivalent copies are not independent sources. |
| data/catalog/youtube_inventory.db | Selected inventory/discovery/normalization/provenance index; references do not prove current filesystem presence. |
| data/catalog/youtube_channel_registry.db | Broader channel/video/transcript source registry; frozen LFS-backed real SQLite used by Finance. Distinct population from selected inventory. |
| data/intelligence/channels/CH-*/ and data/intelligence/system/ | Versioned intelligence/interpretations, capability contracts and calibration; evidence coverage explicit. Editing/visual canonical V1 capability attaches only to registered forensic channels. |
| research/finance-economics-intelligence/audit-baseline/ | Immutable966-ID baseline and26source fingerprints. Canonical per-video audit JSON/receipts and VIDEO_AUDIT_966.jsonl are current research authorities within their branch. |
| Finance component CSVs, completion matrix, combined workbook | Derived projections. Seven component CSVs reconcile under the canonical validator. Extra JSONL fields are not silently promoted into CSV headers. Workbook embedded JSON/statuses reconcile; static universe status is stale. |
| Finance reconciliation-all-repository-2026-10-21/ | Disjoint1,612-video identity/layer index and42-channel directory. Identity provenance useful; audit_status still430and is not current completion authority. |
| research/visual-forensics/channels/casual-finance/<video>/ | Per-video CT contracts/manifests/gates, versions, ledgers/reviewer responses and reconstruction guidance. Visual-only and full-AV acceptance are separate. |
| data/extracted/forensic-analysis/<channel>/<date>/ | Older published forensic packages with SOURCE/QA/STATES/SHOTS/MOTIONS and source declared observations. Overlap with newer CT cases. |
| research/casually-finance-editing-forensics/ | Older38-Short measured/analyst editing corpus; later CT cases coexist outside its old queue. |
| knowledge/youtube/ | Repository-backed synthesis and source/recovery indexes; interpretation/navigation rather than replacement evidence. Scope guards and private archive limits persist. |
| productions/, finance-short-02-visual-calibration/, projects/ | Branch-specific production candidates, assets, editable projects and QA. Rendering is not owner acceptance. |
| scripts/, tests/, schemas/, config/ | Existing tooling/contracts and validation. New audit collector scripts are external, not production infrastructure. |
| docs/audits/, reports/, handoffs | Dated reports; useful provenance but not live counts when a newer authoritative ledger exists. |
| Documents/YIOS-Media-Library | Private local original media; current456file hashes checked against separate published media manifest. Not shared Git storage. |

## Keys and schemas

`DS-0000xx` is a dataset identity; canonical inventory `CH-00000x` is a project identity, and YouTube `UC...` channel IDs are external platform identities. Do not equate those forms without the documented crosswalk. `Video_ID`/`video_id`/`youtube_video_id` is the11-character YouTube key. Format and metric snapshots remain per-source/per-date. `batch_id` (for example NICK_185) identifies an audit unit, not another video. Claim/source IDs are local to their batch; join on batch + video + claim/source ID, retaining branch/SHA for versioning. `source_row_id`, state/shot/event IDs and `composition_group` keys are local to a video/version/table.

Finance JSONL has one original video per row: Channel_ID,Video_ID,batch_id,identity,performance,private_metrics,script,statuses,thumbnail,title,topic,virality,event. Each of six `*_REVIEW` statuses stays separate. A fully populated baseline performance tier does not mean the title/script/thumbnail was reviewed. Canonical transcript source entries carry Text_SHA256; modern read receipts carry exact ranges, first/last witnesses, archive/member hashes and image identity. Claims preserve creator assertion, analyst assessment, source IDs and evidence-kind/confidence. `PRIVATE_*`/unavailable fields are not synthesized.

The media registry has source folder/relative path/type/byte count/SHA256, conservative video-ID confidence/evidence and original/durable locations. Unknown67mappings stay unresolved. Git object SHA1identifies versioned bytes; SHA256source/media fingerprints identify exact original payload. A Git LFS pointer identifies an OID/size, not available media bytes; local object/materialized hash checks are independent.

## Source → processing → validation → publication

1. Registered user/acquired source bytes and immutable manifests establish identity/provenance and deduplication.
2. Normalization/packages and catalog/registry projections retain IDs, source locators, hashes and explicit gaps.
3. Research reads exact stored transcript/actual thumbnail and records analyst interpretation, claims, sources/calculations, frozen public performance and uncertainty.
4. Structural validators check identities, hashes, required fields, contiguous read receipts, image association and projection reconciliation. They do not prove reasoning, source entailment, human listening or causal effects.
5. A normal validated atomic research commit and verified publication checkpoint establish availability on its branch. Separate branch publication does not imply default/canonical containment or owner acceptance.
6. Production adapts patterns into original scripts/visuals with separate asset/source/QA gates; missing evidence remains blocked, not invented.

Versioned historical packets/manifests and later correction layers are retained (for example Machine A NICK_260 corrections). A correction must identify the original version, what changed and why; no raw evidence is overwritten. Static report/workbook/source projections may describe earlier checkpoints. The current branch/SHA and acceptance ledger always qualify a count.

## Conflicting/stale authorities found

- Canonical Finance/PR36 and separate Machine A Finance have different published checkpoints and writer declarations. Both are retained; the latter is not automatically the canonical writer/ledger.
- FINANCE_UNIVERSE.csv has430accepted statuses versus461/554in current JSONL/workbooks. Use it for identity/layers/provenance, not live acceptance.
- Old Finance handoffs and earlier sections of appended RESUME_HERE can name already completed videos. Latest Machine A checkpoint points to NICK_279; first master-order untouched row is a different concept and is not a queue instruction.
- Older Casually Finance RESUME_HERE says long-form not started, while later CT003–005 packages exist and remain partial. Current per-video QUALITY_GATE supersedes that old pilot queue. CT003 gate still says candidate not pushed even though its files are now in a verified remote commit; publication is established by authenticated Git, acceptance by the gate.
- Senior Health's old COMPLETE headline is explicitly corrected to IN_PROGRESS elsewhere; do not erase the correction by quoting the old headline alone.
- Two dataset ledgers fingerprint mutable .gitattributes at627bytes; actual current configuration differs. This is a provenance-projection issue, not demonstrated raw-source corruption.
- Selected inventory and broader registry count different populations. Historical discovery rows and file/manifest references do not establish present bytes.
- Coordination implementation, private Drive/media recovery, old CI and runtime paths are distinct capabilities; a published smoke-test declaration is not actual second-Mac acceptance.
''')
 write('CLEANUP_RECOVERY.md',f'''# Cleanup and recovery ledger

The before checkpoint was made and verified before any exact-file cleanup. It records all HEADs/upstreams/refs/reflogs/worktrees, staged/unstaged binary-capable patches, ignored/nonignored untracked path lists, unfinished-operation checks, stash identities/contents and local writer/resource snapshots. There were no tracked or nonignored untracked changes to discard. No local branch commit was endangered, so a redundant large Git bundle was not created.

{table(['Exact path','Classification/action','Original bytes','Recovery'],[[r['path'],r['classification']+' / '+r['action'],r['original_bytes'],r['recovery']] for r in read('cleanup_ledger.json')])}

The two workbook `.inspect.ndjson` files are tool inspection exports, explicitly ignored. Their first records identify workbook inspection data; no tracked script/doc dependency and no open-file user was found. The retired966workbook's export is superseded; the current workbook remains intact and was independently checked. The Finder file under `.git/refs` is invalid Git-ref metadata; initial fsck's only errors were badRefName/badRefContent on that path. It is not a branch or research artifact. Exact gzip copies were created, decompressed and SHA256verified before removal, and checked again afterward. Final Git integrity passes.

Gross logical removal {size(clean['gross_logical_bytes_removed'])}. Compressed recovery {size(clean['recovery_compressed_bytes'])}. Net logical savings before other audit reports {size(clean['net_logical_bytes_reclaimed_before_other_audit_outputs'])}. APFS physical free-space changes cannot be attributed on an active volume. Other audit output consumes space and independent Git packing changed object layout; neither is disguised as additional owner cleanup savings.

## Preserved material

All raw evidence, private configuration, registered frozen sources, stashes, local/remote branches,7Codex recovery refs, worktrees, original media, external archives, old catalogs and unknown research were retained. No blanket reset/clean/removal, stash pop/clear, auto-commit or research publication occurred. `local_path_classifications.csv` lists every ignored/untracked checkpoint path with reason/action; runtime support is retained, ignored raw evidence is preserved, unknown consumers are not declared unused.

Stash `{stash['sha']}` contains a14-insertion/11-deletion tracked thumbnail completion-ledger edit and2,267untracked files totaling843,095,575bytes. The untracked tree has577exact remote-tip blob matches and2,265bounded local/external hash matches; an additional394,924,525byteArchive.zip matches its external original. The910,451bytefinance-short-experiment-01.zip has no exact local/remote container match established and remains preserved. Archive compression/container differences need not mean new research, so it is not counted as an independent dataset. Full item paths/blob IDs/SHA256/matching locations are in `stash_contents.csv`.

A newly generated full binary stash export would duplicate over1GBof retained evidence. It was replaced by a compact tracked-only patch, complete untracked object/hash inventory, unchanged stash ref and exact original Git object locators. The tracked patch passes `git apply --cached --check` against a disposable index at stash parent. No source/stash object was removed. The before recovery manifest was regenerated and verified after this audit-artifact compaction; the removed newly generated export is not counted as owner cleanup. Large evidence originals remain in place.

## Recovery instructions

Check `RECOVERY_MANIFEST.json` and `RECOVERY_VERIFIED.json`. Each removed path has its original SHA256and gzip path in `cleanup_ledger.csv`. Decompress into a new staging filename, verify SHA256against the ledger, then inspect. Do not overwrite a differing original; the Finder Git-ref metadata should remain outside `.git/refs` because reinserting it reproduces the known integrity error.

For the retained stash, inspect without popping:

```sh
git show ac51465b33be2d25d1a18749b1301cda778e33e5^3:finance-short-experiment-01.zip > /private/tmp/yios-preserved-finance-short-experiment-01.zip
git diff ac51465b33be2d25d1a18749b1301cda778e33e5^1 ac51465b33be2d25d1a18749b1301cda778e33e5 -- docs/research/thumbnail-forensics-2026-10-02/completion-ledger.csv
```

Use a fresh staging path if the example destination already exists. This checkpoint is sufficient to reverse the performed cleanup and identify/preserve unchanged local work; it is not an off-device full repository disaster backup.
''')
 write('VALIDATION_REPORT.md',f'''# Validation actually executed

Repository/source identity: canonical Finance `{c['sha']}`, frozen registry SHA256 `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`. Runtime `.venv/bin/python`3.12.14. Commands/working directories, UTCtimes, durations, stdout/stderr and exit codes are retained in `validation/*.json`/`.log`.

{table(['Check','Result','Exit / seconds'],[[r['name'],r['result'],str(r['code'])+' / '+str(r['elapsed_seconds'])] for r in val])}

Initial Git fsck failed solely on `.git/refs/.DS_Store`; after exact verified cleanup it passed. A final additional fsck after newly observed Git object-layout change also passes. All3,138formerly loose object IDs still resolve, allrefs/stash match, and every checkout remains clean at its original SHA. LFS object hashes are independently listed in `lfs_presence.csv`; Git fsck alone does not certify LFS bytes.

## Commands and scope

- `git diff --check`; `git fsck --full --no-dangling`.
- `.venv/bin/python scripts/scan_tracked_secrets.py`:0findings. Additional all-branch-tip bounded text scan:0findings; no secret values printed. Patterns/bounds are documented; this is not an exhaustive historical/binary secret audit. Private `.env` was not opened.
- `.venv/bin/python -m scripts.validate_dataset_ledgers`:DS20/21/22/23/24/25/27clean; DS28-F020andDS30-F019fail SIZE/SHA on shared`.gitattributes`. Expected627bytes/hash1970079d…; exact current hash/size and introducing history are in `validation/provenance_mismatches.json`. Raw evidence was not altered.
- `.venv/bin/python -m scripts.validate_youtube_channel_registry`:PASS,0domain errors,0duplicate channel/video IDs,0null-transcript-without-reason,0first-party ingested; disposable rebuild idempotence PASS. Original frozen source DB retained.
- Existing Finance `validate_audit_966.py` and`validate_research.py`:PASS,966identities,26frozen-source hashes, thumbnail hashes, canonical transcript hashes, statuses/CSV identity and analysis projections. Their two generated JSONreports were redirected externally with a narrowly scoped Path.write_text shim; validators themselves were unmodified. The exact shim and argv are in reproduce/ and validation/.
- `.venv/bin/python -m pytest -q -p no:cacheprovider research/finance-economics-intelligence`:38PASS.
- `node --test test_workbook_formatting.mjs` in Finance directory:2PASS.
- `.venv/bin/python -m pytest -q -p no:cacheprovider tests`:459PASS,1SKIP,1FAIL,5warnings. Failure is `LedgerChecksumTests::test_all_csv_ledger_datasets_are_clean`, the same two historical config fingerprint issues. It is not hidden as a green suite.
- Coordination worktree's existing `test_yios_coordination.py` and`test_yios_checkpoints.py`:17PASS with real disposable Git fixtures. This does not migrate a protected writer or prove Machine A receiving-client acceptance.
- Independent read-only workbook reconciliation on both exact published Finance heads:1,612unique rows/42channels/966details, all embedded JSON and statuses agree, ZIPintegrity PASS,17formulas,0error-type cells. Cached deep counts461/554. Native Excel recalculation NOT_TESTED.
- SQLite read-only integrity/foreign-key inspection for4local DBs:PASS.456/456media hashes and26/26frozen source hashes match.351published CT003/004portable member hashes match; CT001/002manifests primarily enumerate external files rather than a member list.
- Exact-range financial claim witnesses:397canonical and1,820Machine-A-version matches,0mismatches among entries with those fields. No new source entailment/financial fact-check or calculation evaluation was performed.

## Hosted CI and historical assertions

Latest canonical head run41053016403/check124053485843isFAILURE with0steps. Fresh authenticated annotation says job did not start due failed payments/spending limit. Classification:CI_BLOCKED_BILLING, not a successful CI run and not proof code tests executed. Existing runs were not retriggered. See `latest-ci-jobs.json`/`latest-ci-annotations.json`.

Machine A's554checkpoint declares48pytest +2Node checks and existing validators; those historical run counts were not rerun as a full Machine A environment. Fresh local checks independently establish its published row counts, IDs, workbook/JSONL equality and common frozen source availability. Each other branch's published validation declarations are indexed, not presented as fresh reruns.

## Unavailable/not-run checks

Full CT visual/audio evidence-based validators are blocked by absent external frames/audio and missing numpy/Whisper/PySceneDetect in the project runtime; raw evidence was not regenerated. No new listening, source decode, reviewer wave, external-source fact-check, Apify/YouTube API, private Drive restore, V2, source ingestion or research pipeline was started. Native Excel, current Machine A filesystem/processes, historical full Git secret content and remote LFS availability for absent versions remain unverified. One passing validator cannot certify these layers.
''')
 write('PORTABILITY_MISSING_EVIDENCE.md',f'''# Portability and missing evidence

## Available now

All fetched Git branch histories and tip trees are local. Canonical/coordination/Claude checkouts are already current on their own upstreams. All26Finance frozen sources match, including real LFS SQLite and canonical workbook/ZIP inputs. Registered media456/456matches under`Documents/YIOS-Media-Library` (not a Git-hosted media mirror). Git reports no shallow/partial/sparse configuration or submodules. No shared media/cloud store is configured by the inspected visual manifests.

{table(['CT video','Git package branch','Exact source SHA256','Source bytes here','Machine A evidence workspace'],[[v['video_id'],v['ref'],v['source_sha256'],'YES,hash match',v['workspace_machine_a'] or 'UNKNOWN_FROM_MANIFEST'] for v in visual])}

CT001and002are accepted only as visual-only; human listening and full-AVsignoff remain blocked. CT003checkpoint11,004P,005Jare partial. Their source MP4s do not substitute for reviewer-native crops, original responses or accepted evidence associations.

`machine_a_transfer_requirements.csv`/JSONcontains5,092path/hash/version entries from published external manifests and checksum scopes. Twelve have a matching local hash; most missing sizes are explicitlyUNKNOWNbecause checksum-only manifests do not supply bytes. Historical checkpoint scopes can include multiple versions of the same path; do not blindly overwrite differing evidence. CT001manifest lists41external files/12,973,432bytes; CT002lists968/103,733,801bytes. CT003reports695evidence frames/99,463,181bytes,701frames/21,205,956bytes and280disputes/18,189,245bytes in its source manifest; newer scoped checksum manifests retain the precise entries. CT004raw-image categories and checkpoint scopes are listed in its manifest but do not provide a complete byte total. CT005external workspace root/individual file sizes are not established by its manifest. Those unknowns must be obtained from the source machine, not guessed.

Transfer only evidence needed for the intended verification/continuation: exact missing frames/contact sheets/native crops/audio/arrays/reviewer original responses and source receipts. Reports/ledgers already in Git should be read from their exact branch. Source MP4s for001–005need no transfer. Verify the source manifests, stage absent files, compare hash, and preserve any collisions/different versions. No evidence was redownloaded, decoded or regenerated during this audit.

## Machine A Finance comparison

Historical hint SHA`9c6f42fb33e493314cced538d5c5fa599a29e6c5`matches the authenticated separate Finance branch.554accepted is independently reproducible from its966original rows plus646expansion.93additional completed IDs and44commits are published beyond canonical. Current handoff next isNICK_279`pTyMmSZ2EVs`, title“You Can't Afford a House. Good.” That next row is untouched; the canonical branch'sNICK_186is already completed on Machine A branch. First master-order untouched row`aP0pn6J8tz4`is a different selection concept, not a replacement for the checkpoint queue.

No core Finance Git transfer is required to read the554checkpoint: bytes are already in local Git, and common frozen sources match. Actual Machine A active/unpublished work is unknown. Published receipts can refer to primary data read remotely or local downloaded source files whose full bytes were not committed; a receipt/hash alone does not make those source bytes available here. `finance/primary_source_receipts.csv` preserves access scopes, explicit file paths, presence and source confidence; legacy unlabeled entries are not upgraded. For future independent financial-claim verification, obtain missing cited raw source captures/hash witnesses where the packet requires them, rather than inventing recovered primary evidence.

## Video006 xtqbRt94TTw: two distinct research states

Older published PR21 package is recoverable at`data/extracted/forensic-analysis/casually-finance/2026-10-12/02_VIDEO_FORENSICS/xtqbRt94TTw/`on`origin/codex/casually-finance-forensic-research`. SOURCE.json/QA.jsondescribe489states,133reviewed shots, PASS_STRUCTURAL and audio signal analysis without listening. This is not the newer reported CTCheckpointB.

Its older exact1080psource is present inside`/Users/ghilmanislam360/Downloads/CasuallyFinance.zip`, member`CasuallyFinance/To Save the Economy... WeΓÇÖre About to Break It - Casual Finance (1080p, h264).mp4`,49,993,573bytes, SHA256`030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66`. It was streamed and hash-verified without extraction. Available original Machine A path is`/Users/ghilmankhan/Downloads/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4`. Compare this fingerprint with the newer CTsource manifest before treating the encode as identical.

The newer Video006CTCheckpointBfolder is not located in any of46fetched branch-tip CTnamespaces. There are many older metadata/forensic references, so saying“no data for this video”would be false. The owner's historical report says first-pass shards1and3structurally passed and8were pending; that is not a fresh inspection. Required transfer/recovery from Machine A: its entire unpublished CT006workspace with source_manifest/checksum files, reviewer input shards and original OUTresponses, state/candidate/dispute/measurement ledgers, frames/crops/contact sheets, audio/ASR and continuation/writer record. Exact current workspace path/hash/size and completion state remainUNKNOWNuntil its local manifest is provided. This Mac cannot inspect those files/processes or certify the report.

## LFS and environment

26distinct LFSOIDversions were encountered across branch tips:1current materialized hash match,19older locally stored objects and6absent payload versions. Existing object hashes were checked separately. Six missing versions include two historical registry snapshots plus Dr Rehan test V1/V2MP4s and music/SFXWAVs. Their exactOID/size/branch/path are in`lfs_presence.csv`; remote backing-store availability remainsUNKNOWNuntil a needed targeted LFSfetch. A pointer is not available media. Do not replace the current frozen DB with an old snapshot.

Use project`.venv/bin/python`3.12.14. openpyxl/Pillow/pytestare available; ffmpeg/ffprobe/node/uv/git-lfsbinaries exist. numpy/Whisper/PySceneDetectare absent from this runtime. System`python3`isHomebrew3.14.7(outsideproject<3.14)and XML/plist import failed on a missing libexpatsymbol. Do not rely on that interpreter for workbook/XML tooling. No dependencies were installed or repaired. Artifact-tool/other bundled dependencies for a future workbook rebuild must be located with the supported workspace-dependency loader; no rebuild was needed here.

384unique bounded branch-tip text blobs contain machine-specific`/Users/...`prefixes. The full path-reference index preserves affected paths/branch versions. Some are historical citations, while hardcoded validator/script paths can block execution. `/private/tmp/...`source paths are transient and may be permanently gone. No private Drive restore, credential service, paid acquisition or Machine A scheduler was tested. Current local crontab is absent; no matching local Codex automation or LaunchAgent was found. Historical Machine A scheduler`yios-visual-forensics-machine-a`and`~/YIOS-local-audits/vf_lock.sh`are references, not inspected local scheduled tasks. No schedules changed.
''')
 write('DATA_USE_GUIDE.md',f'''# Ten practical data-use workflows

These are existing files, Git/SQLite operations and repository tools, not a new retrieval service. Start in`{ROOT}`and use`.venv/bin/python`, not the broken systemPython. Commands below read existing evidence; production-authoring examples are instructions for a later authorized task and were not executed during this audit. Always retain branch/SHAwith a result.

## 1. Find all research for a channel

Real input:Nick Invests,YouTube channel`UCXzNNA2ngRpRiWvyA7eGd6w`. Query the actual registry and inspect the channel package:

```sh
.venv/bin/python - <<'PY'
import sqlite3
c=sqlite3.connect('file:data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
rows=c.execute('SELECT youtube_video_id,title FROM videos WHERE canonical_channel_id=?',('UCXzNNA2ngRpRiWvyA7eGd6w',)).fetchall()
print(len(rows)); print(rows[:3])
PY
```

Expected363registered video rows. Read`research/finance-economics-intelligence/channel-intelligence/nick-invests/2026-10-23/README.md`,then filter`VIDEO_AUDIT_966.jsonl`byChannel_ID. Canonical has194completed Nick originals; the supplementary report is an older dated synthesis and is not current completion authority. For Casually Finance use the separate navigation branch's`research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md`with`git show origin/codex/casually-finance-knowledge-navigation:exact/path`; its pinned corpus/CTlinks distinguish overlaps and private dependencies.

## 2. Retrieve a complete available package for one video

Real input`XJ4ls6r2MCE`(NICK_185). Retrieve its row and named packet/receipts:

```sh
.venv/bin/python - <<'PY'
import json
from pathlib import Path
b=Path('research/finance-economics-intelligence')
r=next(json.loads(l) for l in (b/'VIDEO_AUDIT_966.jsonl').read_text().splitlines() if json.loads(l)['Video_ID']=='XJ4ls6r2MCE')
print(r['batch_id'],r['statuses']);print(r['script']['source']);print(r['thumbnail'])
for name in ['NICK_185.json','NICK_185_READ_RECEIPTS.json','NICK_185_VALIDATION.json']: print(b/'audit-batches'/name)
PY
```

Read those threeJSONfiles,then the exact`thumbnail.image_path`and canonical transcript source. Nick's archive is`data/extracted/channel-data/DS-000022/packages/nick-invests/NickInvests_Transcripts_363_Videos.zip`;`TRANSCRIPT_COVERAGE.csv`and receipts map members/Text_SHA256. Actual transcript text is queryable from registry`transcripts`byyoutube_video_idwithis_placeholder=0. A complete limited-evidence text/thumbnail package does not include verified source audio/MP4/listening/private analytics. Use JSONL/receipts for full structured content; Excel is a checked projection.

For the newer separate branch,read without switching:

```sh
git show origin/codex/finance-machine-a-owner-directed:research/finance-economics-intelligence/audit-batches/NICK_278.json
git show origin/codex/finance-machine-a-owner-directed:research/finance-economics-intelligence/audit-batches/NICK_278_READ_RECEIPTS.json
```

## 3. Compare strong, typical and weak videos

Real same-channel examples in`VIDEO_MASTER.csv`:CrayonCapital`1GowFTjbUnk`NVIDIA(9.76573×STRONG),`9r-45QPLl-Y`Petrodollar(1.27641×TYPICAL),`AKrjI9m6fpk`Epstein(0.37936×WEAK),frozen2026-09-13snapshot.

```sh
.venv/bin/python - <<'PY'
import csv
with open('research/finance-economics-intelligence/VIDEO_MASTER.csv') as f:
 for r in csv.DictReader(f):
  if r['Video_ID'] in ['1GowFTjbUnk','9r-45QPLl-Y','AKrjI9m6fpk']: print({{k:r[k] for k in ['Video_ID','Title','Performance_tier','Lifetime_rate_ratio','Peer_Video_IDs','Metric_snapshot_date']}})
PY
```

Then compare their authored JSONLsections and`PERFORMANCE_SENSITIVITY.csv`; expected explicit peer IDs and frozen metric basis. Tiers describe lifetime public rate against a cohort; they are not causal explanations, current views, private retention or guaranteed success.

## 4. Compare title, thumbnail, topic and script patterns

Use the same three IDs in`TITLE_ANALYSIS_966.csv`,`THUMBNAIL_ANALYSIS_966.csv`,`TOPIC_ANALYSIS_966.csv`,`SCRIPT_ANALYSIS_966.csv`,plus`TITLE_FORMULA_LIBRARY.md`,`SCRIPT_FORMULA_LIBRARY.md`,`VIRALITY_PATTERNS_AND_COUNTEREXAMPLES.md`. Filter CSVrows byVideo_IDwithPythoncsvas above; retrieve actual image paths from JSONLand compare at native/mobile sizes only when the image exists. Output: side-by-side evidence/analyst interpretations and counterexamples. The shared“ExplainedLikeYou're5”grammar spans different performance tiers; it does not prove title formula caused views. Unreviewed rows/statuses and stale synthesis dates remain explicit.

## 5. Retrieve financial claims with sources

Real inputNICK_185. Its packet`reviews[0].script.claim_audit`contains16claim groups. Its read receipt has2primary-source receipts and2calculations. For the tax/bandwidth examples read exactassessment,source_idsand matchingreceipt.source_id,includingaccess_scope/limitations/publication_applicability. A verified source can contradict the creator's numeric claim; a direct-source label alone is not a VERIFIEDclaim verdict. Latest Machine A NICK_265+adds confidence labels that distinguish direct primary inspection, snippets, recall and unavailable sources.

Audit convenience indexes:`finance/claims.csv`,`finance/primary_source_receipts.csv`,`finance/calculation_receipts.csv`. They point back to exactexistingpacket paths/refsand preserve uncertainty. These are audit retrieval tables, not a new production interface. Expected output: creator assertion +stored-ASRwitness +analyst assessment +source/locator/date/limitation +calculationreceipt. Older narrative claim audits are not fully machine-queryable; absence of saved primary bytes prevents independent offline source entailment verification. No new financial fact-check was run here.

## 6. Retrieve channel visual grammar and editing DNA

Casually Finance older corpus:

```sh
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/VISUAL_DNA.md
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/MOTION_DNA.md
git show origin/codex/casually-finance-forensic-research:data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/EDITING_DNA.md
```

Join each statement toper-videoSOURCE.json/QA.json/STATES.csv/SHOTS.csv/MOTIONS.csvandconfidence. Later CT00176-state report is`research/visual-forensics/channels/casual-finance/o3FQcd91MIs/research/v2/visual_ct_scan_report_v2.md`; CT002has`STATE_BY_STATE_VISUAL_FORENSICS.md`. CT003–005are on the editing branch and partial. Output: descriptive channel grammar +timed/source-row evidence. Do not treat16older structural packages,38Shorts and5CTcases as independent/disjoint samples; audio and much native evidence remain unavailable.

## 7. Build an original storyboard and asset plan from published research

Read existing`docs/intelligence/CASUALLY_FINANCE_STORYBOARD_TEST.md`on`origin/codex/casually-finance-knowledge-navigation`and sourceDNAabove. It is a real navigation/storyboard example, not new forensic evidence. Assemble a later original storyboard with columns:sourcevideo/version/row/time →observedfact →analystinterpretation/uncertainty →originalscene/narration/asset/motion →requiredverification. Consult existing production branches for editable scene/asset/QApatterns,not accepted research counts.

Expected output: an original storyboard and asset plan grounded in general patterns, independently sourced financial claims and original art/voice/timing. Reusing source footage/artwork/dialogue/distinctive sequences is not a substitute for original production. The V1orchestrator exists at`scripts/run_youtube_intelligence.py`; if used later it requires a real existingchannel+opportunityIDand an externaloutputdir. No inventedRAG/API/unifiedchannelinterface is claimed and no content plan was generated today.

## 8. Identify what is missing before production

For a concrete CTvideo read its`QUALITY_GATE`/`PORTABLE_MANIFEST`/`EXTERNAL_EVIDENCE_MANIFEST`,then matchsourceSHAinthisaudit`media_integrity.csv`andmissingentriesin`machine_a_transfer_requirements.csv`. For a Finance video inspectall6statuses,source_receipts/limitations,thumbnailpath/hashandprivate_metrics. Readproduction`PRODUCTION_STATUS.json`/qaVALIDATIONonitsownbranch. Output: source/claim/image/audio/asset/rights/QAavailability checklist for that package. Existing visual-only/partial status cannot become fullAVacceptance because the sourceMP4exists. Do not rerun measurement or acquire media solely because a reference path is stale.

## 9. Resume the correct next research task

No task was resumed during this audit. Read live branch-specific`FINANCE_WRITER_OWNERSHIP.md`,`FINANCE_PROGRESS_CHECKPOINT.json`,`RESUME_HERE.md`andverifyremotehead/owningwriterbeforeanywrite. Canonical branch saysNICK_186`XP-26tqGFXc`; MachineAbranchalreadycompleted it and currentlysaysNICK_279`pTyMmSZ2EVs`. Reconcile branch/writer handback before selectingaqueue; do not restartalreadyacceptedwork. The old CTShorts pilot queue and old CT003checkpoint6guidanceare stale; currentgatesare003checkpoint11,004P,005J. NewCT006Brequiresitsactualunpublishedworkspace/currentwriterrecord; the olderPR21packagecannotresumeitsnewreviewers.

Coordination tooling exists only on its separate checked-out branch:read`docs/YIOS_TWO_MAC_WORKFLOW.md`there. Its nonproductiontestclaimsareRELEASED; theydo notreleaseprotectedlegacywriters. Do not claimactualtwoMacacceptancefromthe17localtests.

## 10. Transfer or reconstruct the environment here

Existing checkout/runtime are usable:Python3.12.14,openpyxl/Pillow/pytest,node,ffmpeg/ffprobe,git-lfs. No clone/worktree is needed. Verifyfrozenhashes and use`lfs_presence.csv`beforedecidingaLFSfetch. A later neededexactpathcanbefetchedwithoutallmediausingexistingGitLFS`git lfs fetch origin <branch> --include=<exact-path>`;thiswasnotrunforthe6unneededmissingversions. MaterializeonlytheintendedabsentfileandverifyOID/hash,neverreplaceadifferingfrozenDB.

Keepprivate`YIOS_MEDIA_ROOT=/Users/ghilmanislam360/Documents/YIOS-Media-Library`intheconsumerenvironment;readthemediabranchregistry,notstale`data/local-channel-media`paths. Preserveprivate`.env`; donotcopysecretsintoGit/audit. ObtainonlymissingCTevidencefromMachineA'smanifestroots,stage/verifyhashesandkeepcollisions. Installnumpy/Whisper/PySceneDetectonlyifafutureauthorizedforensicoperationneeds them;useanexplicitcompatibleenvironment. SystemPython3.14hasanXMLruntimefailureandisoutsideprojectcontract. Futuredocument/workbookbundledruntimeusemustlocatesupportedworkspacedependenciesratherthanhardcodeanotherMac'scachepath.

Expectedoutput:existingGit+registeredsource/mediaavailabilityandafuturetask-specificdependencyplan. Noautomaticrebuild,redownload,reviewerwave,scheduledresearchorV2infrastructureisrequiredbythisaudit.
''')
 issues=[
 (1,'Finance publication/writer split','554accepted exists on separate Machine A branch; canonical/PR36 remains461,44commitsbehindthatbranchbut0behinditsownupstream.','Owner/writer-coordinated validation and explicit reconciliation/handback; preserve both branches, no duplicate audits.'),
 (2,'Missing current CT006 workspace','New CheckpointBonlyhistoricallyreported; olderPR21package/sourceareavailablebutnotthesamenewcheckpoint.','ObtainexactMachineAworkspace/source/checksummanifest/reviewerresponsesandcurrentwriterrecord;donotregenerateexpensiveevidence.'),
 (3,'Stale Finance universe status projection','FINANCE_UNIVERSE.csv430completeversusJSONL/workbook461/554.','TreatJSONL+validatedpacketsascompletionauthority;futureowner-scopedprojectionrepairwithprovenance,notrawedits.'),
 (4,'Two failing provenance rows','DS28-F020andDS30-F019fingerprintmutable.gitattributes;fullsuite1fail.','Documenthistoricalconfigurationfingerprint/correctionsemanticsbeforeupdatingledger;rawsourcebytesremainunchanged.'),
 (5,'CT evidence/semantic/audio limits','Sources001–005present;mostprivateframes/audio/workingcropsabsent;allfullAVblocked.','Transferonlyrequiredhash-matchedevidence;separatestructuralchecksfromnativevisualandhumanlisteningacceptance.'),
 (6,'Missing LFS versions','6payloadversionsabsentlocally,twohistoricalDBsandfourDrRehanproductionmediafiles.','Targetedfetchonlyifneeded;remoteLFSavailabilityunverified;preservefrozencurrentDB.'),
 (7,'Runtime portability','Project3.12works;system3.14XMLbroken;numpy/Whisper/PySceneDetectabsent.','Useexistingproject.venv;futuretask-specificenvironmentrepair/dependenciesonly.'),
 (8,'CI billing blocker','Latestcanonicaljobfailurewith0stepsandbillingannotation.','Billing/spendingconfigurationowneraction;do notmisclassifyasexecutedcodefailureorblindlyrerun.'),
 (9,'Historical/status/path drift','384boundedtextblobversionscontain/Userspaths;oldFinance/CT/SeniorHealthheadlinesandqueuescanbestale.','Useexactbranch/gate/ledgerandhashresolver;retainhistoryandannotatestaleauthoritieswhenowner-scoped.'),
 (10,'Preserved local archives/stash','2,267stashuntrackeditemsandtrackedledgereditpreserved;oneZIPcontainerhasnoexactothercopymatchestablished.','Keepuntilsemantic/archive-memberandwriterreview;noautocommit/pop/clear orworktreedeletion.'),
 (11,'Coverage vs infrastructure','0realfirstpartyanalyticsexports;metadata/research/visual/productionacceptanceareseparate.','Useexistingboundedworkflows;donotstartV2/API/RAG/agents/automationfromthisaudit.')]
 csvout('prioritized_unresolved_issues.csv',[{'priority':r[0],'issue':r[1],'evidence':r[2],'next_step':r[3]} for r in issues])
 write('UNRESOLVED_ISSUES.md','# Prioritized unresolved issues\n\n'+table(['Priority','Issue','Evidence / limitation','Next step'],issues)+'\n\nThese are findings and follow-up recommendations. No research continuation, financial fact-check, branch integration, PR change, acquisition, environment install or scheduled task was launched.\n')
 write('OWNER_REPORT_ROMAN_URDU.md',f'''# YIOS audit — owner report, Roman Urdu — 2 November 2026

1. **Machine pehle kitni behind/ahead thi?** Apne configured upstream ke muqable mein tamam24localbranches aur3checkouts0ahead/0behindthe. PrimarycheckoutFinancebranchpartha,mainparnahin. MachineAki alagpublishedbranchcanonicalFinance se44commitsaur93acceptedvideosaagehai;isfarqkoown-upstreamstalenessnahinkahna.

2. **Ab kya verified current hai?** AuthenticatedfetchaurfinalGitHubreadneconfirmkiya:Finance/Claude`223f44981ee174988574e86d5e23ae83ee60ee5d`,coordination`205fc7ebadcbde6b5104e9cb2be53de8951511a8`,defaultmain`08e719264e31ecd82de24f8eeb8f065c08359fe5`. Koifast-forwardchangezaroorinahinthi. MachineAbranch`9c6f42fb33e493314cced538d5c5fa599a29e6c5`bhiGitmeinrecoverhochakihai. PR36OPEN/DRAFThai;usmeinkochangenahin.

3. **Cleanup/space?** Sirf3verifieddisposablefileshatin:GitrefskaFinder.DS_Storeaur2workbookinspectionlogs.44,031,783bytesgrossremovehuay,3,883,529bytescompressedrecoveryrakhi;net40,148,254bytes(38.29MiB)logicalspacebachi. Rawevidence/actualworkbooknahinhata. Gitintegrityerrorfixhua. AlagbackgroundGitpackingkaobservedspacedeltaiscleanupmeincreditnahinkiya.

4. **Unique/activeworkpreserve?** Koiuncommittedtrackedya nonignoreduntrackedworknahinmila. Ekstashmeintrackedcompletion-ledgereditkeilawa2,267items/843MBhain;stash,externaloriginals,7Codexrecoveryrefs,private.env,ignoredrawfilesaurtamamworktreespreservehain. Ek910KBFinanceexperimentZIPkiexactdoosricopyestablishnahinhui—usaybhipreserv kiya. InactivitykoMachineAwriterrelease nahinsamjha.

5. **Kisbranchmein kya/kitna?**46remotebranches+24localrefskicompletematrixhai. CanonicalFinance461/1,612accepted;alagMachineAFinance554/1,612. PR21CasuallyFinance16/18structuralpackages;CasualEconomics11sampledstructuralpackages;olderediting38Shorts;CT001–005mein2visual-onlyacceptedaur3partial.12-channelmetadata445videos,Monkey76public,BarelyEvolved4. Productioncandidatesalagbranchesparhain. Yeh overlappingpopulationshain,inhe jor karnewvideocountnahinbanana.

6. **Worktreesnecessary/redundant?** Sirf1independentGitcommonstoreaur2linkedworktrees. Primarysources/runtimeke liyeimportant;coordinationkaalagtoolingrolehai;ClaudeworktreeFinancekeexactHEADparlogicalduplicatehai,magrwriterassignment/ignoreddependenciesclearnahinhain,isliyehatayanahin. PhysicalAPFSsharingunknownhai;logicalduplicationkoautomaticallyreclaimablespacenahinkaha.

7. **Researchkitnicomplete/partial/blocked/pending?** Canonical:461acceptedlimited,16partial,17source-blocked,1,118pending. MachineAbranch:554,16,17,1,025. Donoekhi1,612populationkeversionshain. Full-evidenceFinancecompletion0;fullAVsignoffbhi0. LatestMachineAqueueNICK_279`pTyMmSZ2EVs`hai;staleNICK_186restartnahinkarna.

8. **DatayahanvsMachineA?**456/456registeredmediafileshash-match(454video+2audio,4.06GiB),26/26frozenFinanceinputsverified. CT001–005keexactMP4syahanhain. CT006kapurana49,993,573byteMP4existingZIPmeinverifiedhai;uskanayaCheckpointBworkspace,recentreviewersaurunpublished evidenceyahanestablishnahinhua.5,092manifest/checksum transferentriesmein12localhashmatches;baqikepaths/hashesaurunknownsizesexactCSVmein hain.6LFSversionsabsent;currentfrozenDBreal/verifiedhai.

9. **Aajdatausekaise?** NickInvests ke363videoregistryrowsquerykarsaktehain;videoIDseJSONLpacket,readreceipt,actualthumbnailaurstoredtranscriptnikkalsaktehain. Samechannelstrong/typical/weakcomparisons,claim/source-receiptjoins,DNA/stateledgersauroriginalstoryboardreferenceworkingcapabilitieshain.10realworkflowcommandsDATA_USE_GUIDE.mdmein hain. Koinewresearchstartnahinhui.

10. **Sabseimportantissues/nextsteps?** PehleFinancebranch/writerreconciliationaurMachineAkaactualCT006handoffrecoverkarein. UniverseCSV430parstalehai,JSONL/workbooks461/554paragreehain. DS28/30keshared.gitattributesfingerprints2ledgerfailuresdetehain;rawcorruptionprove nahinhui.38Finance+2Node tests pass,fullsuite459pass/1skip/1fail;Git/registry/frozen/mediahashcheckspass. HostedCIbillingkiwajahse0stepsparblockedhai. SystemPython3.14XMLbrokenhai—working3.12.venvusekarein. Missingnativevisual/audioevidenceaursemanticverificationko passdeclare nahinkiya.

Measuredfacts:authenticatedGitSHAs,actualfilesystembytes/hashes,recomputedledger/workbookcountsaurisMacparrunhuaytests. Publishedhistoricalevidence:olderbranchstatus/reviewer/validatorreceipts. Historicalownerhint:newVideo006Bwithshards1/3passed,8pending. Unknown:MachineAkeabkeprocesses/localunpublishedfiles,currentCT006workspacepath/hash/size,privatecloudrestoreaurabsentremoteLFSpayloadavailability. Koi push,merge,PR36edit,scheduledtaskchange,newvideoaudit/reviewerwaveyaV2worknahinhua.

FullEnglishdetail,completeCSV/JSONinventoriesaurrecovery`{OUT}`mein hain.
''')
 # Preserve executable audit provenance outside the checkout.
 for p in Path('/private/tmp/yios-sync-audit-v1').glob('*.py'):
  dest=OUT/'reproduce'/p.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 # Append local-only names and exact upstream mapping to the remote narrative.
 p=OUT/'BRANCH_AUDIT.md'
 p.write_text(p.read_text()+'\n## Complete local branch mapping\n\n'+table(['Local branch','Full SHA','Upstream','Ahead/behind','Checked-out path'],[[r['name'],r['sha'],r['upstream'],str(r['ahead_upstream'])+'/'+str(r['behind_upstream']),r['worktree'] or 'Not checked out'] for r in matrix if r['kind']=='local'])+'\n\nLocal Claude branch has no same-named remote but points exactly at published Finance upstream. No unpublished local branch commit exists. Historical declarations for every local/remote ref are embedded in branch_matrix.json/CSV; all branch trees/diffs/commits are retained.\n')
 print('Reports written',audit_at)

if __name__=='__main__':main()
