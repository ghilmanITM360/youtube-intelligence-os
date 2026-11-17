# Structure and authority map

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
