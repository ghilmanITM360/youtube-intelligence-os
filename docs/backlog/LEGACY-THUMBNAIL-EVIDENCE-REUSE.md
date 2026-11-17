# Deferred legacy thumbnail evidence reuse

Date: 2026-10-12. Priority: **P4 / DEFERRED**. Tracking: [Issue #23](https://github.com/ghilmanITM360/youtube-intelligence-os/issues/23).

**DOCUMENTATION ONLY — IMPLEMENTATION DEFERRED**

## Purpose and existing inventory

Plan future reuse of preserved historical research without starting reconciliation, visual auditing, migration or promotion. All 2,243 original changed files were preserved unchanged: 2,242 untracked and one tracked modification; zero deleted.

| Evidence classification | Files |
|---|---:|
| Unique structurally validated artifacts | 16 |
| Unique unvalidated artifacts | 22 |
| Images and archive | 2,204 (2,203 images and one ZIP) |
| Configuration requiring publication review | 1 |
| Total | 2,243 |

The verified private backup is named `yios-local-preservation-2026-10-12`. Exact machine paths and complete manifests remain private. A local backup is not remote preservation. Structural validation does not certify fresh visual judgments.

## Relationship to PR #22

[PR #22](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/22) preserves selected historical B002 records and the dated local reconciliation audit; it does not authorize reuse. The audit and JSON companion are under `docs/audits/LOCAL-REPOSITORY-RECONCILIATION-2026-10-12.*` in that PR. This plan has no code or data dependency on merging #22. Future execution depends on the preserved inventory, current audits and owner disposition of that PR. Historical and current coverage counts must stay separate.

## Proposed future phases

1. Crosswalk legacy B002 and current channel audits by exact Video_ID, Thumbnail_ID, source hashes and provenance keys.
2. Review 22 unvalidated artifacts and research helpers; identify reusable code without rerunning collection.
3. Classify historical images and visual families, recording facts, observations, interpretations and hypotheses separately.
4. Identify new intelligence evidence, exact duplicates, superseded records and unresolved conflicts with explicit rationale.
5. Validate and integrate only reviewed, deduplicated research-safe analytical outputs through atomic reviewable changes.

## Source-data safety and validation gates

Keep originals and private backup unchanged. Never infer duplication from names alone or count same-source copies as independent evidence. Preserve original/successor IDs, SHA-256 hashes, source locators and validation status. Unknown provenance remains unresolved and preserved. Do not overwrite current audits or canonical counts.

Raw images and archives remain outside ordinary Git unless a reviewed storage policy authorizes otherwise. Exclude private configuration, unvalidated bulk research, generated databases and unrelated research. No paid collection, raw-image migration, registry change or new visual analysis is authorized here.

Future gates: owner activation; identity/source-hash consistency; provenance and deduplication review; privacy/storage approval; relevant focused validators; staged-path and size inspection; owner review of integration PRs.

## Acceptance criteria and activation

Every candidate has a recorded disposition and evidence crosswalk; unvalidated artifacts/helpers have review decisions; new evidence is separated from duplicate/superseded observations; focused validation passes; only reviewed analytical outputs are integrated; raw/private evidence remains protected. Record canonical, pushed research, local validated and incomplete states separately.

**Implementation may begin only after a future explicit owner instruction activates Issue #23.** No implementation date is assigned. Creating or merging this planning document does not activate the work.

## Active priorities (owner direction, 2026-10-12)

- **P1 — Casually Finance:** [PR #21](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/21) is open at this check. Reported corpus: 206 public upload IDs, 16/18 selected videos structurally analyzed, two Shorts missing locally, production DNA generated; full audiovisual QA remains partial. When execution is authorized, reuse the corpus, finish evidence-supported audiovisual QA, cross-check high-impact numbers/proper nouns, resolve source/metadata/provenance gaps and review DNA/final report. Missing Shorts: `turJ6VMfUjI`, `Qof71Ef-3EU`. Do not repeat completed analysis.
- **P2 — New channel metadata through Apify:** waiting for owner channel URL/handle. Reuse existing YIOS acquisition pipeline for channel identity/metadata, accessible catalog, titles/descriptions/dates, Shorts/long-form classification, public engagement, thumbnail URLs, legitimately available captions/transcripts, provenance and missing records. Before any run verify identity, inspect live actor schema, check existing datasets, estimate count/price/budget and obtain explicit paid-run approval. No run is authorized now.
- **P3 — Additional audiovisual channels:** waiting for 2–4 channel identities and sources. Use What If/Casually Finance methodology with separate inventories/workspaces: full-duration examination, storytelling, shots, visual states, motion, assets, editing, audio and audiovisual alignment, packaging, performance hypotheses and channel DNA. Require independent channel evidence; do not transfer creative conclusions by assumption.
- **P4 — Legacy evidence reuse:** deferred under Issue #23 until explicit owner activation.

This dated priority block records the current decision without rewriting older project-wide status snapshots. This change creates no acquisition or analysis implementation.
