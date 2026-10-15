# Finance and Economics Phase 2 readiness

**Ready for bounded, reuse-first competitive research. Complete source recovery remains partial. No new competitive audit was conducted in this phase.**

Read [central preflight](../../knowledge/youtube/RESEARCH_PREFLIGHT.md) first. [Existing inventory](EXISTING_DATA_INVENTORY.csv) has 39 rows: 13 canonical finance channels, 5 adjacent channels, 18 identity-only leads (including the canonical identity for Casual Finance), and 3 separate research overlays/report entries. The 13 finance channels contain **966 distinct saved videos and 955 non-placeholder transcripts**, recomputed read-only from the current registry. These are not current live YouTube totals. The repository registry overall contains 75 identities, 2,303 video records and 2,291 non-placeholder transcripts. [Computed counts](../../knowledge/youtube/REGISTRY_COUNTS.json).

Canonical finance: Crayon Capital, Lucas Grant, Brimm., Carl Invests, Nick Invests, Primate Economics, Bob Invests, Sonny Finance, Money Life POV, Dark Ledger, Shaami Finance, Matty Invests and Mr. Finance. Selection reuses the existing finance inventory's niche assessments; ambiguous and adjacent channels retain those labels. Identity-only niches remain unverified.

## Reuse before acquisition

- **Casual Finance / @CasuallyFinance:** immutable branch catalog contains 206 unique video IDs (recounted from CSV), with the public snapshot dated 2026-10-11. Existing forensic work covers 16 available selected videos; missing selected Shorts and partial audio/motion QA remain limitations. The success playbook and Office exports reuse that corpus. They are not another 206 observations.
- **Casual Economics:** PR #25's current report, dated 2026-10-14, documents 11 original videos, 11 auto-caption tracks in branch-only DS-000036, and 11 structural packages. Full AV sign-off is explicitly 0/11. Older October 12 inventory statements that acquisition/analysis is pending are superseded within that research branch, not in the canonical main registry. Use its latest report and QA register, not its older inventory summary.
- **Thumbnails:** 38 local Finance image files, including resized review variants, are hash-indexed in [LOCAL_THUMBNAIL_INDEX.csv](LOCAL_THUMBNAIL_INDEX.csv). Do not interpret these as 38 videos or historical upload-time thumbnails. Canonical thumbnail URL fields and local images have separate availability states.
- **Other sources:** [FINANCE_SOURCE_MAP.csv](FINANCE_SOURCE_MAP.csv) locates canonical packages, manifests, extracted classifications, historical benchmarks, local reports, branch Word/Excel artifacts and cloud candidates. It is a source pointer map, not another observation table.

## Readiness meanings

`METADATA_READY` / `TITLES_READY`: structured saved records exist. `THUMBNAILS_LOCAL`: named local image bytes exist. `THUMBNAIL_URL_ONLY`: URL evidence exists but does not establish a local or historical image. Both can occur where coverage is mixed. `TRANSCRIPTS_READY`: non-placeholder text covers the stated dataset denominator. `TRANSCRIPTS_PARTIAL`: incomplete text or selected-subset coverage. `VISUAL_RESEARCH_READY`: research can be reused with its QA limits. `RESEARCH_ONLY`: unpromoted research scope. `SOURCE_MISSING`: no acquired content in that identity-only scope; other overlays may exist.

Registry thumbnail counts are registry fields only. In particular, absent registry URLs do not establish that an older workbook lacks URL columns. Source workbooks and raw metadata remain available for targeted extraction if Phase 2 needs them.

## Phase 2 instruction

On `research/finance-economics-intelligence`, read the knowledge preflight and this inventory; reuse the immutable Casually Finance and Casual Economics reports and canonical 13-channel datasets. Agree the comparison cohort/question, evaluate saved-data freshness, fill only decision-critical gaps, then conduct a source-cited competitive audit separating observed performance, interpretations and hypotheses. Preserve canonical sources and existing PRs. Do not start acquisition, API integration, paid scraping or production without task authorization.
