# DS-000011 and DS-000018: deep knowledge corpus audit

Audit timestamp: 2026-09-24 11:32 UTC (16:32 Asia/Karachi). Branch: `chore/full-local-data-sync-and-senior-health-acquisition`. Starting HEAD: `c740f89212dd7a1c59c273fce07e2613f24a68c4`. Starting worktree: one unrelated untracked `.codex/environments/` directory; no tracked changes. This audit changed no source, catalog, registry, or production code. Evidence labels used below: **VERIFIED_FROM_REPOSITORY** (directly inspected bytes or rows), **VERIFIED_FROM_PRIMARY_WEB_SOURCE** (linked current platform documentation), **DERIVED** (repeatable calculation), **INFERRED** (reasoned interpretation), **UNVERIFIED**, **CONFLICTING**, **STALE**. A label on a source claim does not certify its causal explanation.

## 1. Executive Summary

**DS-000011 is a mixed creative and creator education library, not an official YouTube training set.** Seventeen physical documents contain sixteen textually unique works: hook and script templates, title/thumbnail/SEO checklists, AI image/video prompting, a senior-health creator operating prompt, and two long, mixed-source algorithm compilations. Almost all original authors, publication dates, and original URLs are missing. One hook PDF is repeated under a second filename. Its strongest use is as a *dated, source-labeled creative checklist and hypothesis library*, not platform truth. [VERIFIED_FROM_REPOSITORY: `data/manifests/DS-000011.md`; `document_records`; J files below.]

**DS-000018 is one user-supplied Google Doc snapshot with 63 tabs, not 63 official updates.** Tabs hold third-party video titles, descriptions/chapters, and transcripts or scripts (245,914 manifest words); two pairs reproduce substantially the same videos, leaving **61 unique substantive video-source texts**. Stored source dates and authors are poorly captured. Its 33-row claim artifact selects passages from only seven tabs, and the later validation artifact disposes all 33 claims: 10 supported, 12 partially supported, 1 contradicted, 8 lacking primary support, 2 not currently verifiable. These are *disposition counts*, not 33 proven algorithm changes. [VERIFIED_FROM_REPOSITORY: `data/manifests/DS-000018.md`; E archive and `source-manifest.json`; `data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md` final synthesis.]

No original first-party YouTube Analytics exports, private viewer data, ranking weights, or platform experiment datasets live in either corpus. Two DS-000018 tabs preserve platform-attributed interview speech, but the archived transcript alone does not independently establish speaker identity or verbatim accuracy. Current official guidance supports personalized, surface-specific discovery, appeal/engagement/satisfaction, contextual Search relevance, and cross-format discovery; it does not support universal CTR/retention thresholds, a compulsory separate Shorts channel, a deterministic 48-hour gate, or a secret trust score. [VERIFIED_FROM_REPOSITORY: J, E; VERIFIED_FROM_PRIMARY_WEB_SOURCE: section 17.]

## 2. Dataset Identity

| Field | DS-000011 | DS-000018 |
|---|---|---|
| Official catalog name | All Training Data of YouTube — Global Knowledge Corpus | 2026 Algorithm Update — Multi-Tab Creator Research Corpus |
| Semantic class | A, global YouTube knowledge | A, global YouTube knowledge |
| Registered | 2026-08-27 12:11:47Z; `RUN-000012`, `BATCH-000001` | 2026-09-02; `RUN-000021` |
| Source type and owner | User-supplied external folder, `/Users/ghilmanislam360/Downloads/all training data of youtube`; original compiler/owner UNKNOWN | User-supplied multi-tab Google Doc; document owner/compiler UNKNOWN |
| Purpose established by content | Creative training/reference, prompt templates, creator advice, algorithm commentary | Creator video research and claim monitoring, with some platform-attributed interviews |
| Raw path | `data/raw/global-youtube-knowledge/DS-000011/` | `data/raw/global-youtube-knowledge/DS-000018/2026 Algorithm Update - Google Docs tab snapshot.zip` |
| Manifest | `data/manifests/DS-000011.md` | `data/manifests/DS-000018.md` |
| Catalog status | `INGESTED`: 17 physical `source_files`, 17 `document_records` | `STRUCTURED_REGISTERED`: 1 physical `source_files` archive plus 64 member rows |
| Derived knowledge | 17 rules in `data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json`; rules cover 15 of 17 document IDs and some IDs repeat | 33 claims in `data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md`; final validation in `.../youtube-algorithm-primary-validation-2026-09-04.md`; same 33 rules in strategy registry |
| Channel package | NONE | NONE |
| First-party Analytics | NONE | NONE |

Identity and counts come from both manifests and read-only queries against `data/catalog/youtube_inventory.db`; raw files were rehashed against `source_files` and every DS-000018 archive member against its registered hash. Catalog `PRAGMA integrity_check=ok`, zero foreign-key violations. [VERIFIED_FROM_REPOSITORY.]

## 3. Exact File Inventory

**Physical files only** (archive members are counted separately to avoid double counting):

| Dataset | Format | Files | Bytes | Purpose |
|---|---:|---:|---:|---|
| DS-000011 | PDF | 14 | 5,944,506 | Guides, frameworks, checklists, compilations |
| DS-000011 | DOCX | 2 | 1,037,217 | AI image/video prompting guides |
| DS-000011 | Markdown | 1 | 20,885 | Senior-health creator operating prompt |
| DS-000011 | **Total** | **17** | **7,002,608** | 16 textually unique works |
| DS-000018 | ZIP | 1 | 566,739 | Immutable Google Doc tab snapshot |
| DS-000018 | **Logical contents** | **63 Markdown + 1 JSON** | **1,686,004 uncompressed** | 63 video-research tabs plus provenance manifest; not extra physical files |

Both datasets occupy only `data/raw/global-youtube-knowledge/DS-000011/` or `DS-000018/` as raw physical directories. No raw spreadsheet, TXT, HTML, media, or standalone screenshot is present. `.docx.pdf` suffixes on several DS-000011 files are real PDFs by signature. PDF inspection gave 328 pages total (including duplicate 58-page Hook PDF), 270 unique-text pages. `document_records` describes Renae as eight pages and the SEO checklist as eight pages, while current `pdfinfo` shows **12 and 13 pages** respectively; catalog characterization is stale for those page counts. Physical file hashes and sizes nevertheless match the catalog. [DERIVED from raw files, `pdfinfo`, catalog.]

Repository-wide text references: 27 files mention `DS-000011`, 23 mention `DS-000018` in the current checked tree (some overlap). Principal direct references are both manifests, `data/manifests/batches/BATCH-000001.md` and `..._FILES.csv`, `data/intelligence/global/youtube-algorithm-{source-intelligence-2026-09-02,primary-validation-2026-09-04}.md`, `data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json`, `scripts/report_channel_strategy_intelligence.py`, `docs/Phases.md`, `docs/DATA_INVENTORY.md`, and project audit/status documents under `docs/`. Channel-intelligence and test references are downstream uses, not additional raw copies. Neither ID has a channel-data package. [VERIFIED_FROM_REPOSITORY: `rg -l` repository census; cited paths.]

Full text-reference inventory at starting HEAD (the audit report itself is excluded). `rg -l` searched tracked and nonignored text; binary references are represented separately by catalog rows and E member hashes. These are *mentions*, not all independent artifacts:

```text
DS-000011 (27):
data/extracted/channel-data/DS-000022/DS-000022_PACKAGE_VALIDATION_REPORT.md
data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md
data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md
data/intelligence/system/intelligence-freshness-registry.json
data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json
data/manifests/DS-000011.md
data/manifests/DS-000018.md
data/manifests/batches/BATCH-000001.md
data/manifests/batches/BATCH-000001_FILES.csv
docs/DATA_INVENTORY.md
docs/PROJECT_STATUS_REPORT_2026-09-13.md
docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md
docs/YOUTUBE_INTELLIGENCE_OS_FULL_AUDIT_2026-08-31.md
docs/audits/CHANNEL-DATA-DEEP-AUDIT.md
docs/audits/COMPLETE-DATA-VERIFICATION-AND-INVENTORY-2026-09-23.md
docs/audits/DATA_HOLDINGS_AUDIT_2026-09-14.md
docs/audits/FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md
docs/audits/LOCAL_FILE_INVENTORY_2026-09-22.csv
docs/audits/PROJECT-DEEP-TECHNICAL-REPORT.md
docs/audits/REPOSITORY-HEALTH-AUDIT-2026-09-20.md
docs/audits/REPOSITORY_AUDIT_2026-09-14.md
docs/audits/REPOSITORY_AUDIT_HANDOFF_2026-09-14.md
docs/audits/YOUTUBE_CHANNEL_REGISTRY_COMPLETION_AUDIT_2026-09-15.md
scripts/generate_batch_manifests.py
scripts/plan_intelligence_refresh.py
scripts/report_channel_strategy_intelligence.py
tests/test_channel_strategy_intelligence.py

DS-000018 (23):
data/intelligence/channels/CH-000003/topic-opportunity-intelligence-pilot-2026-09-09.md
data/intelligence/channels/CH-000004/packaging-intelligence-pilot-2026-09-09.md
data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md
data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md
data/intelligence/system/intelligence-freshness-registry.json
data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json
data/manifests/DS-000018.md
docs/DATA_INVENTORY.md
docs/Phases.md
docs/YOUTUBE_CHANNEL_REGISTRY.md
docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md
docs/audits/CHANNEL-DATA-DEEP-AUDIT.md
docs/audits/COMPLETE-DATA-VERIFICATION-AND-INVENTORY-2026-09-23.md
docs/audits/DATA_HOLDINGS_AUDIT_2026-09-14.md
docs/audits/FINAL_CHANNEL_COVERAGE_AND_DS000026_PROPOSAL_2026-09-15.md
docs/audits/LOCAL_FILE_INVENTORY_2026-09-22.csv
docs/audits/REPOSITORY-HEALTH-AUDIT-2026-09-20.md
docs/audits/REPOSITORY_AUDIT_2026-09-14.md
docs/audits/YOUTUBE_CHANNEL_REGISTRY_COMPLETION_AUDIT_2026-09-15.md
docs/audits/YOUTUBE_CHANNEL_REGISTRY_TRACKER_HANDOFF_2026-09-14.md
scripts/plan_intelligence_refresh.py
scripts/report_channel_strategy_intelligence.py
tests/test_channel_strategy_intelligence.py
```

## 4. Storage Architecture

`J` below means `data/raw/global-youtube-knowledge/DS-000011/`. `E` means `data/raw/global-youtube-knowledge/DS-000018/2026 Algorithm Update - Google Docs tab snapshot.zip`. `E::tabs/tab-NN-video-NN.md` is a ZIP member, not an extracted file. T01–T62 follow that naming rule; T63 is `E::tabs/tab-63-tab-63.md`. `E::source-manifest.json` maps each T source to an exact Google Docs tab locator and a SHA-256. The DS-000018 source Doc is [the user-supplied multi-tab document](https://docs.google.com/document/d/14F1A38ngCbsn2ABWD-gRmUaLL_8utow31VLGHFEANJU/edit?usp=sharing); the raw ZIP is a snapshot, not Google's native original bytes. [VERIFIED_FROM_REPOSITORY: E manifest.]

Each physical source is an immutable `RAW_SOURCE`; catalog `source_files`, `document_records`, manifests and derived intelligence point back to it. The DS-000011 registry compresses selected works into 17 rules; the DS-000018 registry repeats the 33 separately validated claims. These layers do not make the original source authoritative. `scripts/run_youtube_intelligence.py` and `scripts/report_channel_strategy_intelligence.py` produce channel-relative plans/diagnoses; the latter contains the global training registry. No production RAG or vector DB exists. [VERIFIED_FROM_REPOSITORY: `docs/Database.md`, `data/catalog/README.md`, both manifests, strategy script.]

## 5. Source Inventory: every substantive unique source

Authority classes: **PRIMARY_PLATFORM_EVIDENCE** requires verifiable original platform statement/document; **PRIMARY_CREATOR_EVIDENCE** means a creator's direct experience or own disclosed data, not proof of YouTube internals; **REPUTABLE_SECONDARY** requires attributable and inspectable reporting; **EXPERIENTIAL** is personal advice without reproducible data; **DERIVED_ANALYSIS** is synthesized/AI-authored interpretation; **UNVERIFIED** has insufficient attribution or inaccessible evidence. No creator is ranked by quality. Here `D` = DERIVED_ANALYSIS, `X` = EXPERIENTIAL, `U` = UNVERIFIED, `P?` = platform-attributed transcript awaiting original-video verification. `DATE_UNKNOWN` means publication date is unestablished even when title says 2026. `T` means time-sensitive claims; `E` means mostly evergreen creative technique. Original publisher/URL for J works: UNKNOWN; original YouTube URLs for E tabs: only where retained inside tab, never inferred from title. [VERIFIED_FROM_REPOSITORY: J content, E manifest and tabs.]

| # | Dataset | Source / stored position | Type | Date | Topics | Authority | Freshness | File |
|---:|---|---|---|---|---|---|---|---|
| 1 | 011 | DOC-000001 Engine personalities; model-as-filmmaker metaphors | AI framework | UNKNOWN | script, AI | D | E | `J/Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf` |
| 2 | 011 | DOC-000002 Hook psychology, three-beat formula, template vault | AI compilation | UNKNOWN | hook, retention | D | E | `J/Hook (1).pdf` |
| 3 | 011 | DOC-000004 Intro Analyzer; seven model-role prompts | Prompt set | UNKNOWN | hook, script | D | E | `J/Intro Analyzer Prompts.docx (1).pdf` |
| 4 | 011 | DOC-000005 Packaging SOP; one visual idea, short title; asserts 10%+ CTR goal | Checklist | UNKNOWN | title, thumbnail | U | T | `J/Packaging (Thumbnail_Title) - SOP(1).pdf` |
| 5 | 011 | DOC-000006 Renae v2.5; 16 storytelling commandments | AI framework | UNKNOWN | story, AI | D | E | `J/Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf` |
| 6 | 011 | DOC-000007 Script Analyzer; seven model-role prompts | Prompt set | UNKNOWN | script, hook | D | E | `J/Script Analyzer.pdf` |
| 7 | 011 | DOC-000008 Nano-Banana image-prompt guide | AI guide | UNKNOWN | images, visual | D | T | `J/The Ultimate Nano-Banana Prompt Guide.docx` |
| 8 | 011 | DOC-000009 VEO 3 video-prompt guide; stacked AI analyses | AI guide | UNKNOWN | video AI, editing | D | T | `J/Ultimate Google VEO 3 Prompt Guide for VIRAL Videos.docx` |
| 9 | 011 | DOC-000010 Viral Checklist; attributed to Codie Sanchez, no original URL | Creator checklist | UNKNOWN | hook, title | X | E | `J/Viral Checklist.pdf` |
| 10 | 011 | DOC-000011 Title Analyzer; formulas plus model prompts | Mixed prompt set | UNKNOWN | title, satisfaction | D | T | `J/YouTube Title Analyzer — Natural Language Prompts (2).pdf` |
| 11 | 011 | DOC-000012 Algorithm/monetization mega-guide; @NotNotAbu2 sections interleaved with AI chat analyses | Mixed compilation | UNKNOWN | discovery, SEO, revenue | D | T | `J/YouTube algorithm guide.docx (2).pdf` |
| 12 | 011 | DOC-000013 YouTube Intelligence Brain v1; senior-health operating prompt and explicit truth hierarchy | AI operating prompt | UNKNOWN | end-to-end strategy | D | T | `J/YouTube_Intelligence_Brain_v1_Verified_Creator_OS.md` |
| 13 | 011 | DOC-000014 Algorithm updates; Tom Brady angles plus AI whiteboard critique | Mixed compilation | UNKNOWN | titles, discovery | D | T | `J/new YT algorithms updates.pdf` |
| 14 | 011 | DOC-000015 BUT/THEREFORE causal-story prompt; technique attributed to Trey Parker/Matt Stone | AI framework | UNKNOWN | story, script | D | E | `J/The Magic of ‘BUT’ and ‘THEREFORE’ in Storytelling.docx (1).pdf` |
| 15 | 011 | DOC-000016 SEO checklist, including tags and keyword steps | Checklist | UNKNOWN | Search, metadata | U | T | `J/🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf` |
| 16 | 011 | DOC-000017 Seven-engine story prompts and 16 commandments | AI prompt set | UNKNOWN | story, script | D | E | `J/📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf` |
| 17 | 018 | T01 Eight small-channel mistakes; separate-format, AEO, deletion claims | Creator transcript | UNKNOWN | formats, AEO | U | T | `E::tabs/tab-01-video-01.md` |
| 18 | 018 | T02 Bad habits; breaks, intros, late breakouts | Creator transcript | UNKNOWN | growth, hooks | X | T | `E::tabs/tab-02-video-02.md` |
| 19 | 018 | T03 Kashif Majeed named in title; warns about automation/demonetization | Creator transcript, Hindi | UNKNOWN | AI, monetization | X | T | `E::tabs/tab-03-video-03.md` |
| 20 | 018 | T04 Hindi explanation of new-channel growth and SEO | Creator transcript, Hindi | UNKNOWN | discovery, SEO | U | T | `E::tabs/tab-04-video-04.md` |
| 21 | 018 | T05 Audience matchmaker, outliers, viewer journey, Search; includes tool promotion | Creator transcript | UNKNOWN | audience, topics | X | T | `E::tabs/tab-05-video-05.md` |
| 22 | 018 | T06 Beginner-to-expert algorithm guide; personalized distribution and satisfaction | Creator transcript | UNKNOWN | recommendations | U | T | `E::tabs/tab-06-video-06.md` |
| 23 | 018 | T07 Hindi new-channel plan and binge-loop strategy | Creator transcript, Hindi | UNKNOWN | planning, series | X | T | `E::tabs/tab-07-video-07.md` |
| 24 | 018 | T08 Cross-platform matching/engagement model, early sample-fit theory | Creator transcript | UNKNOWN | recommendations | U | T | `E::tabs/tab-08-video-08.md` |
| 25 | 018 | T09 Hindi claim that subscriber/views/watch time no longer matter; test-cycle model | Creator transcript, Hindi | UNKNOWN | ranking signals | U | T | `E::tabs/tab-09-video-09.md` |
| 26 | 018 | T10 Shorts upload/settings walkthrough, music and collaboration | Creator transcript, Hindi | UNKNOWN | Shorts workflow | X | T | `E::tabs/tab-10-video-10.md` |
| 27 | 018 | T11 Shorts hashtags/music tactics and viral claims | Creator transcript, Hindi | UNKNOWN | Shorts, tags | U | T | `E::tabs/tab-11-video-11.md` |
| 28 | 018 | T13 Distinct Shorts-upload follow-up; audience-active time and credibility | Creator transcript, Hindi | UNKNOWN | Shorts, timing | X | T | `E::tabs/tab-13-video-13.md` |
| 29 | 018 | T14 2026 upload-settings walkthrough; says tag SEO unimportant | Creator transcript | UNKNOWN | metadata, publishing | X | T | `E::tabs/tab-14-video-14.md` |
| 30 | 018 | T15 1,000-subscriber strategy, TV context and early metrics claims | Creator transcript | UNKNOWN | growth, TV | X | T | `E::tabs/tab-15-video-15.md` |
| 31 | 018 | T16 commentary on platform competition and creator adaptation | Creator transcript | UNKNOWN | industry, growth | X | T | `E::tabs/tab-16-video-16.md` |
| 32 | 018 | T17 algorithm myths, posting time and audience value | Creator transcript | UNKNOWN | timing, audience | X | T | `E::tabs/tab-17-video-17.md` |
| 33 | 018 | T18 AI-platform discovery, policy and Shorts change claims | Creator transcript | UNKNOWN | AI, Search, policy | U | T | `E::tabs/tab-18-video-18.md` |
| 34 | 018 | T19 self-reported 70k-subscriber turnaround; wrong-audience diagnosis | Creator transcript | UNKNOWN | discovery, analytics | X | T | `E::tabs/tab-19-video-19.md` |
| 35 | 018 | T20 48-hour view cliff, warm/cold audience, longer-tail counterexample | Creator transcript | UNKNOWN | discovery, analytics | X | T | `E::tabs/tab-20-video-20.md` |
| 36 | 018 | T21 nine SEO settings, tags/file-name and old-video optimization | Creator transcript, Hindi | UNKNOWN | Search, metadata | U | T | `E::tabs/tab-21-video-21.md` |
| 37 | 018 | T22 five purported growth signals, CTR/retention and audience expansion | Creator transcript | UNKNOWN | analytics | U | T | `E::tabs/tab-22-video-22.md` |
| 38 | 018 | T23 Hindi algorithm explanation; clicks/history/engagement plus IP/device claims | Creator transcript, Hindi | UNKNOWN | personalization | U | T | `E::tabs/tab-23-video-23.md` |
| 39 | 018 | T24 “two-minute hack”: channel keywords/default tags said to direct recommendations | Creator transcript | UNKNOWN | tags, metadata | U | T | `E::tabs/tab-24-video-24.md` |
| 40 | 018 | T25 Shorts monetization case, “warm-up” trust claim and reused-content tactics | Creator transcript | UNKNOWN | Shorts, revenue | U | T | `E::tabs/tab-25-video-25.md` |
| 41 | 018 | T26 Shorts course, claimed 2m subscribers/1b views, faceless workflow | Creator transcript | UNKNOWN | Shorts, monetization | X | T | `E::tabs/tab-26-video-26.md` |
| 42 | 018 | T27 lengthy beginner guide: clarity, content, community, cash, consistency | Creator transcript | UNKNOWN | channel planning | X | T | `E::tabs/tab-27-video-27.md` |
| 43 | 018 | T28 subscribers/past channel history downplayed; value and authenticity | Creator transcript | UNKNOWN | growth | X | T | `E::tabs/tab-28-video-28.md` |
| 44 | 018 | T29 launch and year-one plan, packaging and output expectations | Creator transcript | UNKNOWN | strategy, packaging | X | T | `E::tabs/tab-29-video-29.md` |
| 45 | 018 | T30 purported August-2026 Shorts settings/analytics update; product promotion | Creator transcript | UNKNOWN | Shorts, analytics | U | T | `E::tabs/tab-30-video-30.md` |
| 46 | 018 | T31 post-upload prohibitions and immediate community-post promotion | Creator transcript | UNKNOWN | publishing | X | T | `E::tabs/tab-31-video-31.md` |
| 47 | 018 | T32 small-channel “big update,” audience research with Gemini and mixed formats | Creator transcript | UNKNOWN | AI, formats | U | T | `E::tabs/tab-32-video-32.md` |
| 48 | 018 | T33 “best time” claim built on active-audience chart | Creator transcript | UNKNOWN | timing | U | T | `E::tabs/tab-33-video-33.md` |
| 49 | 018 | T34 small-channel rule claims, view counts and search-topic tools | Creator transcript | UNKNOWN | discovery, Search | U | T | `E::tabs/tab-34-video-34.md` |
| 50 | 018 | T35 self-reported four-million-title analysis; title-frame multipliers, raw rows absent | Creator transcript | UNKNOWN | titles | U | T | `E::tabs/tab-35-video-35.md` |
| 51 | 018 | T36 four “algorithm eras,” semantic-era interpretation and satisfaction | Creator transcript | UNKNOWN | discovery, AI | U | T | `E::tabs/tab-36-video-36.md` |
| 52 | 018 | T37 ordinary creators, practice and monetization; many linked references | Creator transcript | UNKNOWN | growth, income | X | T | `E::tabs/tab-37-video-37.md` |
| 53 | 018 | T39 platform-attributed Todd Beaupré/Creator Insider interview on individualized recommendations | Interview transcript | UNKNOWN | Home, Suggested, audience | P? | T | `E::tabs/tab-39-video-39.md` |
| 54 | 018 | T40 thumbnail examples and native testing advice | Creator transcript | UNKNOWN | thumbnails | X | T | `E::tabs/tab-40-video-40.md` |
| 55 | 018 | T41 “microphase,” clipping/retargeting and session-chain claims | Creator transcript | UNKNOWN | discovery, formats | U | T | `E::tabs/tab-41-video-41.md` |
| 56 | 018 | T42 seven-niche selection and monetization advice | Creator transcript | UNKNOWN | niche, revenue | X | T | `E::tabs/tab-42-video-42.md` |
| 57 | 018 | T43 faceless-channel policy, synthetic disclosure and AEO/off-platform authority | Creator transcript | UNKNOWN | AI, policy, Search | U | T | `E::tabs/tab-43-video-43.md` |
| 58 | 018 | T44 Shorts “trust score,” “30k jail,” honeymoon mechanism | Creator transcript | UNKNOWN | Shorts | U | T | `E::tabs/tab-44-video-44.md` |
| 59 | 018 | T45 “SEO no longer matters,” personality/library/series case | Creator transcript | UNKNOWN | Search, growth | U | T | `E::tabs/tab-45-video-45.md` |
| 60 | 018 | T46 established-audience story-angle strategy | Creator transcript | UNKNOWN | topics, storytelling | X | T | `E::tabs/tab-46-video-46.md` |
| 61 | 018 | T47 entity/AI explanation and advertising-suitability commentary | Creator transcript | UNKNOWN | AI, policy | U | T | `E::tabs/tab-47-video-47.md` |
| 62 | 018 | T48 platform-attributed employee discussion of repetition, Subscriptions, Shorts thumbnails | Interview transcript | UNKNOWN | discovery, formats, policy | P? | T | `E::tabs/tab-48-video-48.md` |
| 63 | 018 | T49 Paddy Galloway strategy interview, private client TV/duration data and “2027” framing | Interview transcript | UNKNOWN | TV, shows, duration | X | T | `E::tabs/tab-49-video-49.md` |
| 64 | 018 | T50 “Shorts jail” and commentary originality advice | Creator transcript | UNKNOWN | Shorts, policy | U | T | `E::tabs/tab-50-video-50.md` |
| 65 | 018 | T51 semantic IDs / large-recommender-model mechanism inferred from Hindi transcript | Creator transcript, Hindi | UNKNOWN | AI, recommendations | U | T | `E::tabs/tab-51-video-51.md` |
| 66 | 018 | T52 beginner practice and publishing before perfect strategy | Creator transcript | UNKNOWN | workflow | X | E | `E::tabs/tab-52-video-52.md` |
| 67 | 018 | T53 33 growth myths, ideation and monetization planning | Creator transcript | UNKNOWN | strategy, revenue | X | T | `E::tabs/tab-53-video-53.md` |
| 68 | 018 | T54 thumbnail critique patterns; “81% better” unmeasured headline | Creator transcript | UNKNOWN | thumbnails | X | E | `E::tabs/tab-54-video-54.md` |
| 69 | 018 | T55 low-view channel-growth signs and qualitative audience response | Creator transcript | UNKNOWN | analytics, community | X | T | `E::tabs/tab-55-video-55.md` |
| 70 | 018 | T56 self-reported three-billion-view creative structure (hook/problem/story/payoff) | Creator transcript | UNKNOWN | hook, story | X | E | `E::tabs/tab-56-video-56.md` |
| 71 | 018 | T57 90-day consistency experiment, distinguishes schedule from performance | Creator transcript | UNKNOWN | cadence, analytics | X | T | `E::tabs/tab-57-video-57.md` |
| 72 | 018 | T58 “trick” headline but argues against magic settings and for audience value | Creator transcript | UNKNOWN | growth, audience | X | E | `E::tabs/tab-58-video-58.md` |
| 73 | 018 | T59 20-video personal progress/practice case | Creator transcript | UNKNOWN | workflow, growth | X | E | `E::tabs/tab-59-video-59.md` |
| 74 | 018 | T60 personalization/community/TV strategic shift interpretation | Creator transcript | UNKNOWN | discovery, community | X | T | `E::tabs/tab-60-video-60.md` |
| 75 | 018 | T61 AI Studio-assisted channel diagnosis claims “wrong audience” | Creator transcript | UNKNOWN | analytics, audience | X | T | `E::tabs/tab-61-video-61.md` |
| 76 | 018 | T62 Hindi 48-hour drop diagnosis and external promotion ideas | Creator transcript, Hindi | UNKNOWN | discovery, promotion | X | T | `E::tabs/tab-62-video-62.md` |
| 77 | 018 | T63 small-channel “dead zone,” process and experiment ideas | Creator transcript | UNKNOWN | growth, workflow | X | E | `E::tabs/tab-63-tab-63.md` |

Excluded **as duplicate source texts**, not lost: DOC-000003 `J/Hook guide.pdf` duplicates DOC-000002 *textually* (different PDF byte hashes); T12 duplicates T10 almost entirely (six-word-shingle containment 0.999); T38 duplicates T26's transcript (six-word-shingle containment 1.000). Both extra tabs remain stored and hash-registered. T13 shares a title with T12 but its script starts differently and is a separate source. [DERIVED from all PDF text and all 63 tab texts.]

## 6. Provenance

DS-000011: registered from the named local Downloads folder on 2026-08-27. All 17 current raw files have valid catalog SHA-256 and sizes. The corpus gives no original URL in any extracted text (17/17), and `document_records.authorship` is `UNKNOWN` for 15/17; Codie Sanchez is an in-text credit in DOC-000010, @NotNotAbu2 appears in portions of DOC-000012. Neither is proof that those people authored the *compiled* file. Publication/update dates for 17/17 compiled works are UNKNOWN. DOC-000015 contains a self-declared 2025-10-20 tag, not independently verified publication date. [VERIFIED_FROM_REPOSITORY: J, catalog `document_records`.]

DS-000018: source Doc URL and exact tab locators retained by E manifest; snapshot accessed 2026-09-02, eight tabs spot-compared on 2026-09-04 per dataset manifest. All 64 member hashes and archive hash match catalog today. All 63 manifest entries lack author/publisher and publication-date fields; 36/63 stored tab texts have no `http` URL at all, while 27 have at least one URL that may be a chapter or *another* video, not necessarily an original-source identifier. `source-manifest.json` records no author or source-video publication dates. Fourteen tabs contain some Devanagari text, including mixed English/Hindi. Transcript production/translation method UNKNOWN. [VERIFIED_FROM_REPOSITORY: E, manifest, catalog.]

Embedded YouTube URL index, where one video ID appears within the tab (source ownership still unverified):

| Tab | Stored video link | Tab | Stored video link | Tab | Stored video link |
|---|---|---|---|---|---|
| T01 | [nFT1xNDprIk](https://www.youtube.com/watch?v=nFT1xNDprIk) | T02 | [UCrC5B3Soyc](https://www.youtube.com/watch?v=UCrC5B3Soyc) | T05 | [ZAQJHdJZ-EQ](https://www.youtube.com/watch?v=ZAQJHdJZ-EQ) |
| T06 | [SIp7MeYbz8U](https://www.youtube.com/watch?v=SIp7MeYbz8U) | T08 | [8cQidXgtGmU](https://www.youtube.com/watch?v=8cQidXgtGmU) | T17 | [IX5vBKlBfjA](https://www.youtube.com/watch?v=IX5vBKlBfjA) |
| T20 | [x5i6KdBSPOA](https://www.youtube.com/watch?v=x5i6KdBSPOA) | T21 | [2J7_e6hOlnM](https://www.youtube.com/watch?v=2J7_e6hOlnM) | T25 | [-8BmzwwZhUk](https://www.youtube.com/watch?v=-8BmzwwZhUk) |
| T26/T38 | [X5u50PrADM8](https://www.youtube.com/watch?v=X5u50PrADM8) | T29 | [AV4r2Qixb1Y](https://www.youtube.com/watch?v=AV4r2Qixb1Y) | T32 | [Z9j8p1135KM](https://www.youtube.com/watch?v=Z9j8p1135KM) |
| T36 | [018eRp_D6Is](https://www.youtube.com/watch?v=018eRp_D6Is) | T39 | [rHLjxrbXmmY](https://www.youtube.com/watch?v=rHLjxrbXmmY) | T40 | [45rN0lhiBlk](https://www.youtube.com/watch?v=45rN0lhiBlk) |
| T41 | [uXer6ZeeweM](https://www.youtube.com/watch?v=uXer6ZeeweM) | T43 | [G9LfE3k-IEI](https://www.youtube.com/watch?v=G9LfE3k-IEI) | T44 | [N-q-XLQymnU](https://www.youtube.com/watch?v=N-q-XLQymnU) |
| T45 | [3MtsASdntAc](https://www.youtube.com/watch?v=3MtsASdntAc) | T46 | [VLfzk9NlZyI](https://www.youtube.com/watch?v=VLfzk9NlZyI) | T48 | [zjNfThCXXJw](https://www.youtube.com/watch?v=zjNfThCXXJw) |
| T49 | [WyiGFFTnIS4](https://www.youtube.com/watch?v=WyiGFFTnIS4) | T51 | [xVnsVms_U-s](https://www.youtube.com/watch?v=xVnsVms_U-s) | T55 | [DnMYPL927i8](https://www.youtube.com/watch?v=DnMYPL927i8) |

T27 and T37 each contain about 20 different YouTube video IDs in later link lists; no single original-video URL is assigned here. T10/T12 and T26/T38 repeat source text. The 36 linkless tabs remain source-located through the Google Doc tab URL in `E::source-manifest.json`; no original video URL is invented. [VERIFIED_FROM_REPOSITORY: E tabs.]

## 7. Source Authority Classification

No J item is an original YouTube Help page or direct platform research dataset. AI-chat language is explicit in DOC-000002, 006, 008, 009, 014, 015 and detectable in related prompt sets; publication provenance remains weak. DOC-000010 is attributed creator advice; DOC-000012 has credited human guide segments plus uncredited AI interpretations. E chiefly consists of creator video transcriptions. T39 and T48 are platform-attributed interview content within a *compiled user Doc*; they are worth checking against the linked original recording and current YouTube Help, but their transcript is not a preserved official document. T49 and T35 report private analyses without underlying records. Thus official-source share of directly preserved canonical raw works is **0/16 for J and 0/61 for E**; **2 E interview transcripts contain platform-attributed speakers**. The separately linked official validation pages in the intelligence layer are primary *external references*, not raw corpus members. [VERIFIED_FROM_REPOSITORY: source table, final validation.]

Origin taxonomy applied to the source table: J DOC-000001/002/004/006/007/008/009/011/013/014/015/017 are `AI_DERIVED` or mixed `AI_DERIVED`/`COMMENTARY`; DOC-000012 is mixed `CREATOR_EXPERIENCE`/`AI_DERIVED`; DOC-000010 is attributed `CREATOR_EXPERIENCE`; DOC-000005/016 have `UNKNOWN` original authors. E rows marked X are `CREATOR_EXPERIENCE`; rows marked U are `COMMENTARY` or `UNKNOWN` mechanism assertions. T39/T48 contain `OFFICIAL_YOUTUBE`-attributed speech but remain `COMMENTARY` as compiled documents pending direct original verification. No raw member qualifies as `OFFICIAL_GOOGLE`, `FIRST_PARTY_CREATOR_ANALYTICS`, or inspectable `INDUSTRY_RESEARCH` data; some creator claims merely refer to those categories. [VERIFIED_FROM_REPOSITORY; INFERRED classification boundary.]

## 8. Date / Freshness Analysis

The only reliable collection dates are 2026-08-27 (J registration) and 2026-09-02 (E snapshot). Source publication range: **UNKNOWN** for both. E titles discuss 2026; T30 says August 2026; T49 is titled “2027” while discussing 2026/2027 and beyond. Title year is not publication date or proof of a platform launch. J contains at least one 2025 internal date tag; its creative techniques can remain useful, but SEO, AI tool capabilities, disclosure policies, and algorithm mechanisms need current verification. Treat E claim dates as `DATE_UNKNOWN` unless independently matched to the original video. This audit's official comparison was checked 2026-09-24; freshness can lapse later. [VERIFIED_FROM_REPOSITORY: manifests, J DOC-000015, E T30/T49; VERIFIED_FROM_PRIMARY_WEB_SOURCE: section 17.]

| Temporal claim class | Corpus example | Audit treatment |
|---|---|---|
| Actual dated platform update | E T43 references altered/synthetic-content labeling; independent [May 27, 2026 YouTube announcement](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/) exists | Verify only label change; do not infer a ranking rewrite |
| 2026 creator observation | E T57's 90-day consistency test; E T55's “summer 2026” audience signs | Primary creator experience at most; publication/sample details incomplete |
| 2026 creator interpretation | E T36/T51 semantic-era framing; E T49 TV/show view | Hypothesis; check independent primary evidence |
| Older evergreen guidance reused in 2026 | E T17 audience value and posting-time myth; J DOC-000013 promise alignment | Keep principle if current documentation and channel evidence fit |
| Prediction/speculation | E T49 “2027” framing; E T43 AI-citation mechanism | Never call a completed platform change |
| Undated claim | Most J works and all E publication dates | `DATE_UNKNOWN`; no automatic freshness credit |

Temporal classes used below: `EVERGREEN` for creative principles that do not depend on a current product mechanism; `CURRENT_2026` only for a claim independently supported by currently available primary guidance; `HISTORICAL_BUT_USEFUL` for old strategy or platform context; `LIKELY_STALE` for superseded features/claims; `DATE_UNKNOWN` when source publication is unestablished. These categories describe *use conditions*, not deletion instructions.

## 9. DS-000011 Purpose

The name “All Training Data of YouTube” is a user folder label. The actual files are not platform training data, model weights, a complete official education library, or evidence of a system trained on all YouTube videos. They are a mixed internal/creator playbook: creative prompts (DOC-000001/004/006/007/013/017), production prompting (008/009), hook/title/SEO checklists (002/005/010/011/016), and large algorithm-commentary compilations (012/014). DOC-000013 explicitly addresses an AI assistant as a creator “brain” and specifies an output contract, which supports *prompt/reference material* as one intended use. [VERIFIED_FROM_REPOSITORY: J files, document inventory.]

## 10. DS-000011 Internal Structure

Flat raw directory, no inner taxonomy. Logical groups: **creative design** (DOC-000001/002/004/005/006/007/010/011/015/017), **AI visual/video prompting** (008/009), **SEO/discovery commentary** (012/014/016), and **integrating operating prompt** (013). DOC-000013 and DOC-000006 repeat ideas from the specialist works; DOC-000014 shares Tom Brady title-angle material with DOC-000011; DOC-000012 embeds many separate guides and AI response fragments. The 117-page mega-guide, 45-page updates PDF and two 58-page Hook PDFs account for most text and risk overweighting repeated advice in naive retrieval. `document_records.content_read=1` on all 17, yet the old row for DOC-000012 says only 35 of 117 pages were read; that flag is not proof of old full-depth review. This audit extracted text from all 117 pages and inspected page-level structure and key claims. [VERIFIED_FROM_REPOSITORY: J, `document_records`.]

## 11. DS-000011 Knowledge Map

J teaches a **creative workflow** more strongly than an algorithm model: define audience/problem; choose a differentiated, truthful angle; design title and thumbnail together; show value early; connect script beats causally; use useful visual proof; publish accurate metadata; inspect channel-relative results. It also contains unverified “algorithm” explanations and some numerical/causal recipes. DOC-000013 itself says official guidance and channel Analytics outrank uploaded playbooks; treat that hierarchy as a useful internal governance principle, not a source of platform facts. DOC-000005's 10%+ CTR goal, DOC-000012's small-batch/metadata/volume claims, and DOC-000014's captions/semantic assertions require independent validation. [VERIFIED_FROM_REPOSITORY: J DOC-000005/012/013/014.]

## 12. DS-000011 Major Findings

| Knowledge / claim | Source | Evidence class | Context | Practical use | Limitation |
|---|---|---|---|---|---|
| Compare topic demand with specific audience question before drafting | DOC-000013, DOC-000012 | DERIVED_ANALYSIS | Creator planning | Topic hypothesis and outlier review | No causal performance proof |
| Make title and thumbnail one honest promise | DOC-000005, 011, 013 | DERIVED_ANALYSIS | Browse/package | Packaging checklist | No universal design or CTR threshold |
| Context, interruption, then meaningful payoff can structure hook | DOC-000002/003 | DERIVED_ANALYSIS | Script draft | Generate variants; compare actual retention later | Duplicate text; fixed seconds unsupported |
| BUT/THEREFORE creates causal progression | DOC-000015, 006, 013 | DERIVED_ANALYSIS | Story/script | Review narrative logic | No proven ranking or retention lift |
| Treat model “personas” as lenses, not independent expert votes | DOC-000001, 004, 007, 017 | DERIVED_ANALYSIS | AI prompting | Structured critique | Model-role names and quality unvalidated |
| Search intent should influence title/description; tags require restraint | DOC-000016, 013 | DERIVED_ANALYSIS | Search-led publishing | Metadata checklist after official check | Checklists conflict on tag importance |
| Use visual proof, pacing and production plan | DOC-000013, 008, 009 | DERIVED_ANALYSIS | Production | Storyboard/prompt aid | AI image/video tool specifics age quickly |
| Do not elevate click or one viral video above satisfaction/replication | DOC-000013, 010, 012 | DERIVED_ANALYSIS | Analytics | Question generation | Private CTR/retention absent from corpus |

## 13. DS-000018 Purpose

“Algorithm Update” is the Doc title and many creator-video headlines, not a single named official 2026 release. “Multi-Tab” means 63 Google Docs tabs, each preserving a video-oriented text export. Coverage spans algorithm explanations, Shorts tactics, search/SEO, small-channel growth, packaging, TV, AI, monetization and production. Some passages describe product changes; many are 2026 creator observations, interpretations of older evergreen principles, sales-backed tactics, predictions, or undated assertions. No release-note chronology was stored. [VERIFIED_FROM_REPOSITORY: E manifest, T01–T63.]

## 14. DS-000018 Internal Structure

One ZIP: 63 Markdown tab members (1,645,996 bytes) plus one 40,008-byte JSON provenance manifest; total 1,686,004 uncompressed bytes. `zip.testzip()` passed; zero duplicate member *names*, zero nested archives, zero unsafe traversal paths, zero empty members. All 63 tabs are marked title + description/chapters + transcript/script in manifest; format and transcript detail vary. No tab is silently omitted from source table. T10/T12 and T26/T38 are repeated source texts in separately hashed exports; the remaining tabs are distinct at six-word-shingle threshold used here. [DERIVED from E ZIP and full text.]

## 15. DS-000018 Source-by-Source Analysis

Master source table above records each unique tab's creator/source *as far as stored attribution allows*, topic, claim or position, evidence type and date. The most important distinction within this corpus:

- T39: source labels Todd Beaupré and Creator Insider; interview discusses personalized candidate selection, subscriber behavior, Suggested and satisfaction. Specific internal cohorts remain unverified. [E::T39; ALG26-CLM-001–008.]
- T48: source labels a YouTube employee; interview discusses repetitive content, subscription shelf, thumbnails and viewer journeys. Policy claims and ranking effects must be separated. [E::T48; ALG26-CLM-009–011/016/017.]
- T49: Paddy Galloway interview advances TV/show strategy and self-reported client/duration statistics; underlying data absent. Its “2027” title is forward framing, not proof of 2027 events. [E::T49; ALG26-CLM-014/015, INT-003–005.]
- T36 and T51: creator semantic-era/model descriptions; an externally published recommender paper can support only bounded model concepts, not the complete current production internals asserted. [E::T36/T51; ALG26-CLM-012/013, INT-001/002.]
- T01 and T43: strong separate-channel, AEO, off-platform authority and deletion advice; several mechanisms unsupported, and T01's universal separate-channel advice conflicts with primary guidance. [E::T01/T43; ALG26-CLM-018, REC-007–010.]
- T35 and T56: self-reported multi-million item/view experience can seed creative hypotheses, but original analyses, sample frames and denominators were not preserved. [E::T35/T56.]
- T03/04/07/09/10/11/13/21/23/51/62 include Hindi or Hindi-English narration. Translation-sensitive causal claims require original-video review by a competent reader. [E manifest and named tabs.]

For all other tabs, source table's one-line position is the source-specific synopsis; it is intentionally *not* treated as independent proof when several creators repeat an idea. All 63 tab texts were read programmatically for title, text, chapters, URL, language, duplicate and topic/claim scans; unique sources were inspected at opening, midpoint, ending and at claim-bearing passages. Publication dates and most creator identities cannot be established from stored metadata; reported as UNKNOWN, not guessed. [VERIFIED_FROM_REPOSITORY.]

## 16. DS-000018 Algorithm Claims

The existing structured artifact has **18 `SOURCE_CLAIM`, 5 `SOURCE_INTERPRETATION`, 10 `SOURCE_RECOMMENDATION`** rows. Claim IDs and source locators below resolve through section 5 and `data/intelligence/global/youtube-algorithm-source-intelligence-2026-09-02.md`; `date=UNKNOWN` for all source publications. “Original status” means it was a source assertion, not an established platform fact. “Final disposition” is the 2026-09-08 validation register, not a new 2026-09-24 retest of every reference. `SUPPORTED` means only its *bounded conclusion* was supported; the full source wording can remain broader. [VERIFIED_FROM_REPOSITORY: both intelligence artifacts.]

| Claim ID | Claim, source, surface | Original status | Final disposition / decisive boundary |
|---|---|---|---|
| ALG26-CLM-001 | Personalized candidate ranking, T39, Home/Suggested | SOURCE_CLAIM | SUPPORTED; inputs differ by surface |
| ALG26-CLM-002 | Different subscriber/new-viewer response cohorts, T39, Home | SOURCE_CLAIM | PARTIALLY_SUPPORTED; exact training cohorts undisclosed |
| ALG26-CLM-003 | Evergreen later discovery, T39, recommendations | SOURCE_CLAIM | PARTIALLY_SUPPORTED; no majority-lifetime-view statistic |
| ALG26-CLM-004 | Long-term satisfaction, no single metric, T39, recommendations | SOURCE_CLAIM | SUPPORTED; no fixed metric weights |
| ALG26-CLM-005 | Audience-aligned channels can mix formats, T39, cross-format | SOURCE_CLAIM | PARTIALLY_SUPPORTED; full internal partitions undisclosed |
| ALG26-CLM-006 | Suggested may cross topics via viewer context, T39, Up Next | SOURCE_CLAIM | PARTIALLY_SUPPORTED; exact matcher undisclosed |
| ALG26-CLM-007 | New-channel cold-start audience assignment, T39, discovery | SOURCE_CLAIM | PARTIALLY_SUPPORTED; specific first-upload mechanism unproven |
| ALG26-CLM-008 | Subscribers need not watch each upload, T39, Home/subscriptions | SOURCE_CLAIM | SUPPORTED; no numeric subscriber gate |
| ALG26-CLM-009 | Repetitive mass production versus varied format, T48, policy | SOURCE_CLAIM | SUPPORTED for policy; ranking penalty not established |
| ALG26-CLM-010 | Recommended Subscriptions shelf, T48, Subscriptions | SOURCE_CLAIM | PARTIALLY_SUPPORTED; exact shelf/universal rollout unproven |
| ALG26-CLM-011 | Watch history input, T48, chiefly Home | SOURCE_CLAIM | SUPPORTED; no universal weight |
| ALG26-CLM-012 | Semantic IDs/audio/frames/metadata/pacing, T51, recommender | SOURCE_CLAIM | PARTIALLY_SUPPORTED by research; complete current deployment not shown |
| ALG26-CLM-013 | Private mood-cluster linkage, T51, recommender | SOURCE_CLAIM | NOT_CURRENTLY_VERIFIABLE |
| ALG26-CLM-014 | Client TV share 23–24% to >50%, T49, device mix | SOURCE_CLAIM | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE; private client data absent |
| ALG26-CLM-015 | 100b-view sample and 51% long-form duration rise, T49 | SOURCE_CLAIM | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE; sample absent |
| ALG26-CLM-016 | Larger Home thumbnail experiment lifted viewing, T48, Home | SOURCE_CLAIM | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE; experiment result absent |
| ALG26-CLM-017 | Shorts thumbnail effects by placement, T48, Shorts/Search/Browse | SOURCE_CLAIM | PARTIALLY_SUPPORTED; current effect by every shelf unproven |
| ALG26-CLM-018 | Shorts and long-form must use separate channels, T01, cross-format | SOURCE_CLAIM | CONTRADICTED as universal instruction |
| ALG26-INT-001 | Four eras culminating in “semantic era,” T36 | INTERNAL_DERIVATION | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE as official chronology |
| ALG26-INT-002 | Specificity/topic authority outweigh subscribers, T36 | INTERNAL_DERIVATION | PARTIALLY_SUPPORTED audience relevance; hidden weight unproven |
| ALG26-INT-003 | TV friction favors longer shows, T49 | INTERNAL_DERIVATION | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE as causal rule |
| ALG26-INT-004 | Personality gains platform premium as spectacle gets easier, T49 | INTERNAL_DERIVATION | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE as platform mechanism |
| ALG26-INT-005 | Long-form recommender more sophisticated than Shorts, T49 | INTERNAL_DERIVATION | NOT_CURRENTLY_VERIFIABLE |
| ALG26-REC-001 | Compare retention, engagement and feedback, T39 | SOURCE_RECOMMENDATION | SUPPORTED as diagnostic guidance; no targets |
| ALG26-REC-002 | Do not disable subscriber delivery as algorithm trick, T39 | SOURCE_RECOMMENDATION | SUPPORTED conditional guidance |
| ALG26-REC-003 | Choose channel architecture by audience/goal fit, T39 | SOURCE_RECOMMENDATION | SUPPORTED conditional guidance |
| ALG26-REC-004 | Clear audience promise and differentiated value, T48 | SOURCE_RECOMMENDATION | SUPPORTED as creator strategy, not hidden novelty score |
| ALG26-REC-005 | Launch with several linked videos, T48 | SOURCE_RECOMMENDATION | PARTIALLY_SUPPORTED library value; fixed batch size unproven |
| ALG26-REC-006 | Build series for return paths, T49 | SOURCE_RECOMMENDATION | SUPPORTED as creator guidance; no automatic show boost |
| ALG26-REC-007 | Early-answer/name/date formula wins AI citations, T43 | SOURCE_RECOMMENDATION | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE |
| ALG26-REC-008 | Off-platform profiles increase YouTube trust, T43 | SOURCE_RECOMMENDATION | NOT_SUPPORTED_BY_PRIMARY_EVIDENCE |
| ALG26-REC-009 | Research content gaps/net-new information, T01 | SOURCE_RECOMMENDATION | PARTIALLY_SUPPORTED research method; AI citation boost unproven |
| ALG26-REC-010 | Unlist rather than delete to preserve all learning, T01 | SOURCE_RECOMMENDATION | PARTIALLY_SUPPORTED caution; total data erasure/preservation unproven |

The `SOURCE_RECOMMENDATION` and `SOURCE_INTERPRETATION` source types are preserved above. `INTERNAL_DERIVATION` in this table describes what a *speaker infers*, not our own observed fact. The exact original labels are `SOURCE_INTERPRETATION` and `SOURCE_RECOMMENDATION` in the 2026-09-02 artifact. [VERIFIED_FROM_REPOSITORY.]

## 17. Current Official YouTube Verification

Current primary-source baseline checked on 2026-09-24:

| Official source | What it supports | What it does not disclose |
|---|---|---|
| [Recommendation system](https://support.google.com/youtube/answer/16533387?hl=en-GB) and [recommendation surfaces](https://support.google.com/youtube/answer/16089387?hl=en) | Viewer personalization, history/affinity, satisfaction; Home, Up Next, Shorts and some channel-page shelves have different contexts | Exact ranking formula, weights, private cohorts |
| [Performance signals](https://support.google.com/youtube/answer/16559650?hl=en) | Appeal, engagement, satisfaction; opening promise/value | Fixed CTR, retention or hook-second threshold |
| [Different surfaces and formats](https://support.google.com/youtube/answer/16559651?hl=en) | Topic interest, competition, seasonality; cross-format connections; no inherent channel penalty from format experiments; no universal ideal length | Guaranteed Shorts-to-long conversion; universal TV duration advantage |
| [Search ranking](https://support.google.com/youtube/answer/16090438?hl=en) and [performance FAQ](https://support.google.com/youtube/answer/141805?hl=en) | Query relevance from title, description, tags and video content; engagement and quality; publish time does not determine long-run performance; no required daily cadence | “SEO is dead,” filename/tag magic, 48-hour gate |
| [External factors](https://support.google.com/youtube/answer/16558238?hl=en) | Topic audience size, competition, seasonality and viewer preference changes | Universal topic scoring formula |
| [A/B testing titles and thumbnails](https://support.google.com/youtube/answer/16391400?hl=en) | Concurrent tests for eligible long-form videos, winner by watch time; Shorts excluded | Guaranteed winner or CTR-only optimization |
| [Shorts discovery](https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en-GB) | Shorts performance does not inherently harm long-form recommendations; no minimum cadence | “Shorts jail”/account trust-score mechanism |
| [AI labeling change, May 2026](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/) | An actual dated 2026 policy/product announcement about altered/synthetic-content labeling | General recommendation rewrite or faceless-channel trust score |

These references test specific corpus claims; they are not a generic platform tutorial. The May 2026 labeling announcement is an *actual dated update*; T43's broader “faceless channels are automatically farms” inference does not follow. We did not identify a single official platform release corresponding to the corpus title “2026 Algorithm Update”; absence in these targeted sources is **not proof no platform change occurred**. [VERIFIED_FROM_PRIMARY_WEB_SOURCE; INFERRED boundary.]

## 18. Claim Verification Matrix

| Claim | Internal source | Official support | Conflict? | Confidence and note |
|---|---|---|---|---|
| Viewer-specific Home/Up Next ranking | E T39, CLM-001/004/011 | [Recommendation Help](https://support.google.com/youtube/answer/16089387?hl=en) | No | **CONFIRMED_BY_PRIMARY_SOURCE** for broad mechanism, not weights |
| Subscriber totals do not guarantee every upload's reach | E T39, CLM-008 | [Performance FAQ](https://support.google.com/youtube/answer/141805?hl=en) | No | **CONSISTENT_WITH_PRIMARY_SOURCE**; cohort architecture unknown |
| Cross-format channel must split | E T01, CLM-018 | [Cross-format guidance](https://support.google.com/youtube/answer/16559651?hl=en) | Yes | **CONTRADICTED_BY_PRIMARY_SOURCE** as universal rule |
| More metadata/tags guarantee push | E T21/T24, J DOC-000016 | [Search Help](https://support.google.com/youtube/answer/16090438?hl=en) | Yes to guarantee | **PLAUSIBLE_BUT_UNVERIFIED** for query relevance; no push rule |
| SEO no longer matters | E T45; J DOC-000014 | [Search Help](https://support.google.com/youtube/answer/16090438?hl=en) | Yes | **CONTRADICTED_BY_PRIMARY_SOURCE** as blanket Search claim |
| “Best” publishing hour changes long-run rank | E T33 | [Performance FAQ](https://support.google.com/youtube/answer/141805?hl=en) | Yes | **CONTRADICTED_BY_PRIMARY_SOURCE** as long-term universal claim |
| 48-hour fixed gate / view jail | E T19/T20/T44/T50/T62 | [Performance FAQ](https://support.google.com/youtube/answer/141805?hl=en) | Not directly | **INSUFFICIENT_EVIDENCE** for deterministic gate; later discovery documented |
| Exact TV share and duration gains | E T49, CLM-014/015 | [Device-context guidance](https://support.google.com/youtube/answer/16559651?hl=en) | No direct test | **CREATOR_OBSERVATION_ONLY**; raw client data missing |
| Semantic ID full mechanism | E T36/T51, CLM-012/013 | Historical recommender paper linked by old validation | No direct current confirmation | **PLAUSIBLE_BUT_UNVERIFIED** for production details |
| Synthetic label update | E T43 | [Official May 2026 blog](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/) | No for label itself | **CONFIRMED_BY_PRIMARY_SOURCE** for label change only; no ranking trust claim |
| Thumbnail/title tests consider watch time | J DOC-000013, E T40 | [Official A/B Help](https://support.google.com/youtube/answer/16391400?hl=en) | No | **CONFIRMED_BY_PRIMARY_SOURCE** for eligible long-form tests |

The 33-row final source-specific dispositions remain section 16; this matrix groups high-impact claims and adds current targeted primary-source checks. `STALE` applies to claims about specific product features only after an identified newer official change, not merely because an undated creator video is old. [VERIFIED_FROM_REPOSITORY and VERIFIED_FROM_PRIMARY_WEB_SOURCE.]

## 19. Algorithm Myths / Overclaims

The strongest overclaim pattern is a plausible observation joined to a fabricated universal mechanism. Examples: “Shorts and long-form must split” (T01), “trust score/30k jail” (T44), “best posting hour to go viral” (T33), “channel keywords and default tags direct recommendations” (T24), “SEO no longer matters” (T45), “no longer relies on title or tags” (T51), “10x easier” (T47), and “10%+ CTR goal” (J DOC-000005). The stored text gives no public experiment design or ranking formula to justify these absolutes. Current Help distinguishes surfaces, audience response and individual videos. [VERIFIED_FROM_REPOSITORY: named J/E sources; VERIFIED_FROM_PRIMARY_WEB_SOURCE: section 17.]

Self-reported scale is also not proof: T35's four-million-title multipliers, T49's 100-billion-view duration figure, T56's three-billion-view claim, and T20's multi-million-video anecdote lack inspectable underlying samples. They may motivate replication with own data; do not import their effect sizes. [VERIFIED_FROM_REPOSITORY: E T20/T35/T49/T56.]

## 20. Topic Taxonomy

Hierarchy derived from source texts, not imposed as a claim of equal depth:

- **Discovery and audience:** recommendations; Home/Browse; Suggested/Up Next; Search; Shorts; live; channel pages; subscriptions; viewer personalization; audience matching; new/returning viewers; topic interest, competition, seasonality; session/continuation behavior.
- **Concept and packaging:** topic/niche/sub-niche research; titles; thumbnails; CTR and impressions; description, tags, hashtags, SEO; playlists; A/B testing.
- **Viewing experience:** hook; script; storytelling; watch time, average view duration and retention; satisfaction; engagement (likes/comments/shares); video length; pacing, editing, B-roll, CTA.
- **Publishing and business:** upload frequency/time; channel growth; community; monetization; creator workflow; AI/automation; analytics; content strategy and experiments.

Direct mention is not depth. Live and channel-page discussion is incidental; there is no live-stream performance corpus or channel-page experiment dataset. J is deepest on creative workflow, E on creator interpretations of discovery/strategy. [DERIVED from J and E full-text census.]

## 21. Topic Coverage Matrix

Counts below mean **unique substantive source texts containing direct lexical topic cues**, not independent confirmations, verified claims, or a calibrated depth score. Denominators: J 16 and E 61 after duplicate collapse. Coverage label is a separate qualitative assessment of stored depth. E main sources use T IDs; J use DOC IDs. “Evidence count” is J/E, respectively. [DERIVED from full extracted texts; conservative cue scan and source review.]

| Topic | DS-000011 coverage | DS-000018 coverage | Evidence count J/E | Main sources |
|---|---|---|---:|---|
| Algorithm/recommendations/personalization | MODERATE | STRONG | 13/49 | J DOC-000012/013/014; E T36/39/48/51 |
| Search and SEO | MODERATE | STRONG | 7/31 | J DOC-000013/016; E T21/24/45 |
| Home/Browse | LIGHT | MODERATE | 3/22 | J DOC-000012/013; E T39/48 |
| Suggested/Up Next | LIGHT | MODERATE | 3/9 | J DOC-000012/013; E T39 |
| Shorts | LIGHT | STRONG | 5/27 | J DOC-000012/014; E T10/25/26/38/44/48 |
| Live discovery | LIGHT | LIGHT | 1/8 | J DOC-000013; E T39/48 |
| Channel pages | NONE | LIGHT | 0/2 | E T39/48; mentions only |
| Subscriptions/subscriber behavior | LIGHT | STRONG | 2/40 | J DOC-000012/013; E T28/39/48 |
| Topic/audience/niche/competition/seasonality | STRONG | STRONG | 11/48 broad cues; 4/13 exact external-factor cues | J DOC-000012/013; E T05/36/39/42/49 |
| New and returning viewers | LIGHT | MODERATE | 3/12 | J DOC-000013; E T39/49/55 |
| Title/thumbnail/CTR/impressions | STRONG | STRONG | 14/61 | J DOC-000005/011/013; E T35/40/54 |
| Watch time/AVD/retention/satisfaction | STRONG | STRONG | 12/31 | J DOC-000002/013; E T20/39/48/57 |
| Engagement/likes/comments/shares | MODERATE | STRONG | 12/31 | J DOC-000010/013; E T08/39/55 |
| Hook/script/storytelling/CTA | STRONG | STRONG | 15/61 | J DOC-000002/007/015/017; E T02/53/56 |
| Editing/B-roll/visual production | STRONG | MODERATE | 13/18 cue subset | J DOC-000008/009/013; E T40/56 |
| Video length | LIGHT | LIGHT | 3/8 | J DOC-000013; E T15/49 |
| Upload frequency/time | MODERATE | STRONG | 8/26 | J DOC-000012/013; E T17/33/57 |
| Description/tags/hashtags | MODERATE | STRONG | 9/30 | J DOC-000016; E T14/21/24 |
| Playlists | LIGHT | LIGHT | 3/9 | J DOC-000012/013; E T41/45 |
| Community | MODERATE | MODERATE | 6/18 | J DOC-000013; E T27/55/60 |
| Analytics/experiments/A-B tests | MODERATE | STRONG | 6/38 broad cues; 4/18 exact test cues | J DOC-000013; E T19/39/40/61 |
| Monetization | LIGHT | MODERATE | 4/25 | J DOC-000012; E T03/25/42/53 |
| External/AEO/AI automation | MODERATE | MODERATE | 3/7 exact AEO/external cues | J DOC-000008/009/014; E T01/18/43/51 |

At finer granularity, evidence is sparse for exact private impressions/CTR, retention *curves*, viewer-level behavior, live ranking, channel-page mechanics, geographic and multilingual discovery, and causal effects of TV viewing. Mentions of Studio/Analytics are **not stored first-party Analytics data**. [VERIFIED_FROM_REPOSITORY: J/E, `docs/Phases.md`.]

## 22. Dataset Comparison

| Dimension | DS-000011 | DS-000018 |
|---|---|---|
| Purpose | Creative/creator reference and AI prompt library | Multi-video creator research and algorithm-claim watchlist |
| Scope | 17 files, 16 unique works; mixed prompt/checklist/compilation | 63 tabs, 61 unique video-source texts |
| Date range | Publication UNKNOWN; one 2025 self-tag; registered 2026-08-27 | Publication UNKNOWN; discussions mention 2026 and future 2027; captured 2026-09-02 |
| Source types | 14 PDFs, 2 DOCX, 1 MD; mostly compiled/AI-derived | Google Doc ZIP of video titles/descriptions/transcripts |
| Official sources | 0 original official works | 0 original official works; 2 platform-attributed interview transcripts |
| Creator sources | Several attributed fragments; many unattributed | Predominantly creator commentary/experience |
| Algorithm focus | Mixed, sometimes loose or contradictory | High, but “2026 update” is not single official release |
| Strategy focus | Audience/packaging/script planning | Small-channel, formats, TV, search, growth hypotheses |
| Production focus | Strong on hooks, scripts, AI visuals/video | Medium on packaging, Shorts and workflow |
| Freshness | Most publications undated | Snapshot fresh as of 2026-09-02; original video dates undated |
| Duplicate rate | 1/17 physical docs is a second text copy: 5.9% | 2/63 tabs repeated: 3.2% |
| Reuse potential | Creative checklists/prompt grounding with labels | Claim monitoring, hypotheses and official-source comparison |
| Main limitation | Mixed AI synthesis, no source URLs/dates/measurements | Transcript provenance and creator claims weaker than headline suggests |

## 23. Duplicate / Overlap Analysis

**Within J:** DOC-000002 and DOC-000003 have identical `pdftotext` output, 64,517 characters each in prior catalog note; current full-text SHA-256 comparison also matches. PDF *byte* hashes differ (`4129…` vs `4bbe…`), so the strategy-script comment describing them as “byte-identical” is inaccurate. Count one source, preserve both raw files. DOC-000011 and DOC-000014 repeat the Tom Brady title-angle passage. DOC-000006/013/017 restate the 16 commandments or seven-engine framework; DOC-000015 supplies the BUT/THEREFORE theme repeated in them. [DERIVED from J, catalog `document_records`, `scripts/report_channel_strategy_intelligence.py` lines 80–85.]

**Within E:** T10/T12 share 99.9% of the shorter text's six-word shingles; T26/T38 share 100%. They have different member hashes because wrappers/formatting differ. T13 is a separate follow-up despite a repeated title. All 63 member SHA-256 values are distinct and all archive names distinct; hash-only dedup would miss the content duplicates. [DERIVED from E full text.]

**Across J/E:** no exact archive-member or source-file hash match, and no cross-dataset document/tab pair passed a 2.5% six-word-shingle containment screen. They overlap semantically in audience matching, hooks, metadata, titles, satisfaction, Shorts, but this is *concept overlap*, not independent validation. Existing registry records an external supplied ZIP with 15 byte-identical J members and an XLSX variant of E; those are described in `data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json` source inventory and are **not** extra corpus sources. The XLSX variant lacks E T47 and has its own duplicate rows. [DERIVED from J/E texts; VERIFIED_FROM_REPOSITORY: strategy registry.]

## 24. Contradictions

| Topic | Position A | Source | Position B | Source | Resolution |
|---|---|---|---|---|---|
| Shorts plus long-form | Must separate channels | E T01, CLM-018 | Mix may work by audience fit | E T39/32, CLM-005 | Universal separation contradicted by [official format guidance](https://support.google.com/youtube/answer/16559651?hl=en); channel-specific test remains |
| SEO relevance | SEO “doesn't matter anymore” | E T45; J DOC-000014 overbroad phrasing | Query relevance includes title/description/content | E T21; J DOC-000013/016 | Surface-specific: [Search Help](https://support.google.com/youtube/answer/16090438?hl=en) supports Search relevance; no universal metadata growth recipe |
| Tags | Tags/settings push or “train” algorithm | E T21/24; J DOC-000016 | Tags minor relative to content, title, description | J DOC-000013; E T14 | Metadata may help query matching; hidden push/trust mechanism unsupported |
| Timing/cadence | Optimal time/frequency drives virality | E T33; J DOC-000012 volume passages | No fixed schedule; sustainable quality | E T17/57; J DOC-000013 | [FAQ](https://support.google.com/youtube/answer/141805?hl=en): early viewership versus long-run performance; no daily requirement |
| 48-hour performance | First two days decide fate | E T19/62 and J DOC-000012 small-batch claims | Later breakouts occur | E T02/20; J DOC-000013 | Different observation periods; deterministic gate unverified; later discovery supported |
| CTR priority | 10%+ CTR target / click first | J DOC-000005; E T31 | Satisfaction and promise delivery matter too | J DOC-000013; E T39 | [Official performance model](https://support.google.com/youtube/answer/16559650?hl=en) uses multiple signals; no universal threshold |
| Video length | TV/long videos rewarded | E T49, CLM-015/INT-003 | Length depends on viewer/purpose | J DOC-000013; E T39 | [Official guidance](https://support.google.com/youtube/answer/16559651?hl=en) rejects universal ideal length; private T49 sample unavailable |
| AI/faceless production | Off-platform identity yields YouTube trust score | E T43; J DOC-000009 promotional “viral” | Originality/policy and viewer response are separate | E T48; J DOC-000013 | Mechanism unresolved and unsupported; policy compliance is not rank guarantee |

These are **conflicting stored positions**, not proof both are equally credible. Topic, surface, channel stage and date can explain some disagreements; others remain unverified. [VERIFIED_FROM_REPOSITORY and VERIFIED_FROM_PRIMARY_WEB_SOURCE as linked.]

## 25. Freshness / Staleness

- **EVERGREEN:** J hook structure, promise-match, causal storytelling, audience-specific clarity (DOC-000002/005/013/015/017); E T52/56/58 creative practices. Still hypotheses for performance lift.
- **CURRENT_2026 (bounded):** personalized discovery, surface differences, appeal/engagement/satisfaction, cross-format possibility and native A/B watch-time criterion, only where today's official pages independently support them (E CLM-001/004/005; J DOC-000013). [Section 17 links.]
- **HISTORICAL_BUT_USEFUL:** older creator examples, past upload tests, J AI model prompt formats and E prior audience/TV observations; useful for idea generation or historical comparison, not current ranking claims.
- **LIKELY_STALE / overspecific:** product-setting recipes, tool capabilities/prices, “new” algorithm launch framing without dates, fixed 48-hour gates, model weights, SEO-dead blanket claims (J DOC-000012/014/016, E T24/30/33/44/45/51). “Likely stale” is a review queue, not proof a specific feature was removed.
- **DATE_UNKNOWN:** all 16 unique J works and 61 unique E tab sources lack verified publication dates. Snapshot dates do not convert them to published-in-2026 works. [VERIFIED_FROM_REPOSITORY.]

## 26. Data Quality

| Check | DS-000011 | DS-000018 |
|---|---:|---:|
| Physical files present / verified hash | 17/17 | 1/1 |
| Archive members present / verified hash | not applicable | 64/64 |
| Empty physical/member files | 0 | 0 |
| ZIP CRC errors / duplicate member names / nested archives / unsafe member paths | not applicable | 0 / 0 / 0 / 0 |
| Substantive text duplicates | 1 extra of 17 | 2 extra of 63 |
| Original source URL absent from raw text | 17/17 | 36/63 tabs lack any HTTP URL; some remaining URLs are secondary links |
| Structured author/publisher metadata missing | 15/17 `document_records.authorship=UNKNOWN`; two are *credited fragments* | 63/63 manifest tab entries |
| Structured publication date missing | 17/17 | 63/63 manifest tab entries |
| Unverified underlying datasets for numerical study claims | Not enumerated exhaustively; large algorithm guides lack measurement data | T35, T49 and other self-reports lack raw samples |
| Orphan manifest/raw mismatch | 0 identified | 0 identified |
| Broken original-source links | UNKNOWN; no original URLs in extracted text | UNKNOWN; not every embedded web link was live-checked |
| Catalog integrity / FK | `ok` / 0 | same shared catalog |

This is a **source-metadata quality** problem more than a damaged-file problem. Both datasets are readable; character extraction includes Hindi/English text. Embedded DOCX files have container XML, and all 14 PDFs yielded text; no OCR-only blank document was found. The old `document_records` page counts for DOC-000006 and DOC-000016 differ from current PDF inspection, and the strategy script's “byte-identical” Hook comment should be corrected in a separately authorized code change. Neither discrepancy changes raw bytes or dataset totals. [VERIFIED_FROM_REPOSITORY: hashes, ZIP CRC, `pdfinfo`, catalog, strategy script.]

## 27. Coverage Gaps

No stored first-party channel export of CTR, impressions, AVD, retention curves, watch-time source splits, returning-viewer cohorts or device breakdown exists in J or E. E T49's private client data and T35's four-million-title sample are *assertions*, not attached data. No viewer-level logs, known ranking weights or YouTube internal experiment records exist. Live discovery, channel-page behavior, TV behavior by niche, multilingual discovery, geographic effects, and current Shorts mechanics get mentions but insufficient systematic evidence. J's creative frameworks contain little observed before/after testing. E claim extraction covers seven of 63 tabs; other tabs have not been normalized at claim level. First-party Analytics ingestion in this repository is ready but has no real export, per `AGENTS.md` and `docs/Phases.md`. [VERIFIED_FROM_REPOSITORY: J, E, manifests, source intelligence, project status.]

## 28. What DS-000011 Can Be Used For

**Directly supported:** source-grounded creator education; checklists for topic framing, packaging, hooks, scripts, visual plans and publishing; AI prompt context with citations; a truth-hierarchy reference; research taxonomy; targeted comparison against channel evidence. **Requires validation:** any asserted algorithm mechanism, quantitative CTR/hook rule, cross-niche strategy effect, current AI tool behavior, medical/health claims, or SEO rank impact. **Not safe:** treating its “training” label as official/complete knowledge, copying its prompt as production policy without source/date checks, or claiming its formulas cause views. [VERIFIED_FROM_REPOSITORY: J DOC-000002/005/012/013/016/017; INFERRED use boundary.]

## 29. What DS-000018 Can Be Used For

**Directly supported:** creator-claim monitoring; 2026 creator-sentiment/source comparison; retrieval of the *33 already dispositioned* claim IDs with their exact tab/timestamp; hypothesis generation for audience, formats, Search and packaging; tracking differences from evergreen J advice. **Requires validation:** every unnormalized tab claim, dates/creator identity, transcript fidelity, private analyses, current product settings and channel-specific outcomes. **Not safe:** claiming a corpus title denotes an official release, treating repeated creator videos as independent corroboration, or turning a partially supported claim into a full algorithm rule. [VERIFIED_FROM_REPOSITORY: E, claim and validation artifacts.]

## 30. What They Must NOT Be Used For

Do not reverse-engineer a secret ranking formula, predict virality with certainty, guarantee views, invent CTR/retention/AVD thresholds, assert private YouTube internals or trust scores, use public competitor metrics as first-party Analytics, hard-code creator folklore, convert interviews into official documentation without verifying original speakers, extrapolate self-reported samples, assume 2026 title means publication/update date, or treat historic advice as current automatically. These prohibitions follow concrete missing data and official-source boundaries above, not a general objection to creator experience. [VERIFIED_FROM_REPOSITORY: J DOC-000005/012/014; E T01/35/43/44/49/51; VERIFIED_FROM_PRIMARY_WEB_SOURCE: section 17.]

## 31. Integration With Channel Evidence

**Channel evidence** is dated, channel-specific: canonical titles, descriptions, public view/like/comment snapshots, transcripts, thumbnail references and any future first-party Analytics. Example: `data/intelligence/channels/CH-000003/topic-opportunity-intelligence-pilot-2026-09-09.md` traces 32 videos in `DS-000006` and finds repeated mobility/gait outliers, while stating CTR, impressions, retention and audience overlap are unavailable. **Global knowledge** J/E supplies lenses and hypotheses only. Global advice should be retrieved alongside channel evidence, explicitly checked for audience/format/surface fit, then tested channel-relatively. A source repeated in both corpora is not extra independent proof. [VERIFIED_FROM_REPOSITORY: named CH-000003 report, J/E and manifests.]

The practical join is: question; retrieve relevant J/E source or claim; inspect authority, date, duplicate group and final validation; retrieve same-channel/peer evidence at a comparable observation time; formulate hypothesis; check it against disconfirming items; recommend a reversible experiment and state unavailable metrics. First-party Analytics, when supplied, should measure outcome rather than be inferred from public views. [INFERRED architecture from `docs/Database.md`, `scripts/run_youtube_intelligence.py`, CH-000003 pilot.]

## 32. YouTube Intelligence OS Integration Map

| Knowledge type | Dataset and source | Existing intelligence module | Safe use |
|---|---|---|---|
| Audience demand, differentiated angle | J DOC-000013; E T05/T48, REC-004/009 | Topic Opportunity Intelligence | Generate topic hypothesis, compare within channel; verify demand externally |
| Promise, title/thumbnail clarity | J DOC-000005/011; E T35/T40/T54 | Packaging Intelligence | Candidate review and eligible A/B plan; do not import universal effect sizes |
| Opening promise and causal beats | J DOC-000002/007/015/017; E T56 | Hook and Script Intelligence | Draft/review hook and story alternatives; retention remains unavailable without Analytics |
| Visual proof / AI creative prompts | J DOC-000008/009/013 | Editing/Visual Intelligence and content blueprint | Production ideation only; actual editing style needs moving-image evidence |
| Audience overlap and format choice | E CLM-005/018, REC-003; J DOC-000013 | Channel Strategy Intelligence | Compare channel-specific format response; no automatic split |
| Recommendation surfaces and limitations | E CLM-001/004/006/011 plus current official pages | Global algorithm/discovery knowledge | Explain bounded platform context with external primary citation |
| Series/returning-viewer hypothesis | E T49, REC-006; J DOC-000012/013 | Channel Strategy/blueprint | Design continuation path, then measure it |
| Claim conflicts and uncertainty | J/E and section 24 | Global knowledge / experiment design | Retrieve both positions, source and resolution |

Existing `youtube-strategy-training-knowledge-2026-09-11.json` has 50 registry rows (17 J, 33 E), but is **not a complete knowledge index**: J DOC-000012 and DOC-000014 have no direct source locator among the 17 J rules, and E claims came from T01/T36/T39/T43/T48/T49/T51 only. A future reader must be able to reach all raw unique sources. The repository's V1 modules and phase limits stand; this audit proposes no production change. [VERIFIED_FROM_REPOSITORY: registry JSON, `scripts/report_channel_strategy_intelligence.py`, `docs/Phases.md`.]

## 33. Content-Team Use Cases

| Role | Query | Safe output | Limit |
|---|---|---|---|
| Researcher | J DOC-000013; E T05/T39/T48; channel topic families | Dated topic questions, evidence map | Public views are not demand denominator |
| Strategist | E CLM-005/018 and REC-003; channel/peer format results | Conditional channel-format test | Audience overlap unknown without Analytics |
| Scriptwriter | J DOC-000002/007/015/017; E T56 | Hook/story variants tied to promise | No guaranteed retention |
| Thumbnail designer | J DOC-000005/011; E T40/T54; actual thumbnail assets | Three distinct truthful concepts | Corpus supplies no universally winning layout |
| Editor | J DOC-000009/013; actual video/frames | Storyboard and visual-proof plan | Prompt guides cannot establish observed editing style |
| Channel manager | E T17/T33/T57 and official cadence guidance | Sustainable schedule/test calendar | No “best hour” growth promise |
| Analyst | E CLM-001/004/008; first-party exports when available | Surface-aware diagnostic, uncertainty | Source transcripts lack private metrics |
| AI agent | Claim ID, member locator, date, authority, official link | Cited answer plus testable hypothesis | Never silently upgrade source claim |

## 34. AI / RAG Readiness

**NEEDS NORMALIZATION, not ready for unattended production RAG.** J is chunkable by document/heading/page but its two long compilations mix human text and AI response inside one file; section and sub-source boundaries must be retained. E is chunkable by tab, chapter and timestamp; `source-manifest.json` gives strong tab locators/hashes, but not publisher, publication date, reliable original-video ID for 36 tabs, or speaker attribution. Exact and near duplicates (J Hook pair; E T10/T12 and T26/T38) should be one retrieval cluster, with all raw references preserved. E's 33 claims are already granular but cover only seven tabs; the other 56 tabs need claim extraction before broad agent grounding. Citation availability is **good for archived member and timestamp**, **weak for original creator identity/date**. The existing catalog stores files and provenance, not embeddings; per `AGENTS.md`, no RAG/vector system should be built automatically. [VERIFIED_FROM_REPOSITORY: J/E, manifests, catalog, strategy registry.]

Minimum future retrieval contract: return `(dataset_id, source_id, raw_path/member, content_hash, passage/page/timestamp, original URL if present, capture date, publication date or UNKNOWN, assertion type, evidence class, validation status/date, duplicate group, limitations)`. Rank first by *question fit and authority*, deduplicate before counting support, show contradictions, and leave missing dates visible. A prompt can use this without a vector DB; ordinary indexed text search plus source metadata is enough for present scale. [INFERRED design; not implemented.]

## 35. Claim-Level Knowledge Model

Proposed only, no schema change:

```text
claim_id, dataset_id, source_id, raw_path, archive_member, content_sha256,
passage_locator, assertion_text, assertion_type, topic, discovery_surface,
original_publisher, original_url, published_at, captured_at,
evidence_class, primary_verification_source, verification_status,
verified_at, freshness, limitations, duplicate_group, conflict_group
```

One document can contain an official-attributed quote, a creator experiment, a sales pitch and an AI inference. Claim-level records stop those parts inheriting a single false authority grade. Preserve original words in raw evidence; store paraphrased assertion and its type in derived layer. Source-level duplicate groups prevent two exports from masquerading as corroboration. [INFERRED from J DOC-000012/014, E T39/48/49, existing 33-claim artifact.]

Decision semantics must stay separate from storage: `PLATFORM_DOCUMENTED_FACT` for a bounded independently checked Help/Blog proposition (E CLM-001's personalized recommendation core); `CONTEXTUAL_PRINCIPLE` for honest promise and audience fit (J DOC-000013); `HEURISTIC` for the three-beat hook (J DOC-000002); `HYPOTHESIS` for TV-favored long shows or an off-platform trust benefit (E T49/T43); and `EXPERIMENT_IDEA` for trying a linked series or concurrent title variants (E REC-006, J DOC-000005). None is a hard global ranking rule. [DERIVED from cited raw sources and section 17.]

## 36. High-Value Reusable Knowledge

Themes, prioritized by authority, breadth, decision impact and testability rather than creator leaderboard:

1. **Viewer- and surface-specific discovery.** E T39/T48 claim excerpts plus [current official guidance](https://support.google.com/youtube/answer/16089387?hl=en) help prevent one “algorithm score” from swallowing Search, Home, Up Next and Shorts. Channel traffic-source data could test local impact. [VERIFIED_FROM_PRIMARY_WEB_SOURCE; E CLM-001/004/011.]
2. **Audience fit, honest promise and satisfaction.** J DOC-000005/013, E T05/T48 and [official performance model](https://support.google.com/youtube/answer/16559650?hl=en) align on useful questions for topic, packaging and intro review. Actual CTR/retention must come from first-party Analytics. [VERIFIED_FROM_REPOSITORY; VERIFIED_FROM_PRIMARY_WEB_SOURCE.]
3. **Causal storytelling and visual proof.** J DOC-000002/015/017 and E T56 offer reusable writing lenses. They are creative hypotheses, assessable against transcript/visual evidence; no automatic rank boost is asserted. [VERIFIED_FROM_REPOSITORY.]
4. **Channel-relative experiments.** E T39/T49, J DOC-000013 and the CH-000003 pilot support measuring against a channel's own historical family and observation date; current official A/B testing supports concurrent packaging experiments where eligible. [VERIFIED_FROM_REPOSITORY; VERIFIED_FROM_PRIMARY_WEB_SOURCE.]
5. **Myth detection.** J DOC-000012/014 and E T01/T24/T33/T44/T45 expose overconfident recipes; section 17 lets an analyst test them before recommendations. [VERIFIED_FROM_REPOSITORY.]

## 37. Knowledge-to-Decision Examples

These are **examples of a defensible decision process**, not new recommendations for a live channel. `CH-000003` public evidence is from `data/intelligence/channels/CH-000003/topic-opportunity-intelligence-pilot-2026-09-09.md`: 32 long-form videos, two robust mobility/gait outliers, one exceptional medication-safety outlier amid a weak 16-video family median; private Analytics unavailable. This dated evidence is preferable to fabricated CTR or retention. [VERIFIED_FROM_REPOSITORY.]

| Question | Channel evidence | J knowledge | E knowledge | Official baseline and conclusion | Confidence |
|---|---|---|---|---|---|
| Topic: another mobility/fall-prevention video? | CH-000003: `VID-000162`, `VID-000163` robust mobility/gait outliers; `VID-000185` above median | DOC-000013: audience/problem and distinct angle | T05/T48: audience fit/differentiation, REC-004 | [External factors](https://support.google.com/youtube/answer/16558238?hl=en) require topic demand/competition context. Develop a *new* mobility question, then validate demand and medical accuracy. | MODERATE channel-relative, no causal proof |
| Title: number-led medication warning? | CH-000003 `VID-000187` huge outlier, but 16-item medication family median weak | DOC-000005/010/011: clarity/specificity | T35: unreplicated multipliers; T40: test variants | [A/B Help](https://support.google.com/youtube/answer/16391400?hl=en) supports eligible test. Draft distinct truthful titles; do not copy T35 multiplier. | LOW until own test |
| Thumbnail: high-contrast doctor plus body-part cue? | CH-000003 thumbnail references may be present; public views alone cannot attribute visual effect | DOC-000005/013: one visual promise | T40/T54: examples/critique, no causal proof | Use [native long-form A/B](https://support.google.com/youtube/answer/16391400?hl=en) if eligible; compare watch time, not a universal 10% CTR. | LOW until test |
| Hook: show gait demonstration early? | CH-000003 has transcripts, not retention curve | DOC-000002/007: context/value; DOC-000015: causal beat | T56: hook/problem/story/payoff | [Performance Help](https://support.google.com/youtube/answer/16559650?hl=en) supports early value. Script two openings; retention outcome remains UNKNOWN. | LOW |
| Length: make next video longer for TV? | CH-000003 public duration 491–1,402 sec; no device mix/AVD | DOC-000013: length follows value | T49: private TV/duration claims unverified | [Official length guidance](https://support.google.com/youtube/answer/16559651?hl=en) rejects ideal length. Set length by material, inspect first-party device and retention data later. | HIGH for rejecting universal rule; LOW for optimal length |
| Upload frequency: post daily? | CH-000003 median upload gap about 1.04 days, but no causal comparison | DOC-000012 has volume tactics; DOC-000013 stresses testability | T17/T33/T57 disagree | [FAQ](https://support.google.com/youtube/answer/141805?hl=en) finds no daily/weekly requirement. Keep sustainable plan; test only if operational need. | HIGH for no required cadence |
| Shorts vs long-form on same channel? | CH-000003 has 0 Shorts; no format-overlap evidence | DOC-000013: audience promise first | T01 says split; T39 says audience fit | [Official cross-format guidance](https://support.google.com/youtube/answer/16559651?hl=en) rejects automatic penalty. No split decision from this channel's data; small experiment if goal warrants. | HIGH for rejecting mandatory split |
| Retention: does intro cause drop? | Public corpus lacks retention curve | DOC-000002/013: promise and proof checklist | T39 REC-001 recommends retention review | [Performance Help](https://support.google.com/youtube/answer/16559650?hl=en) supports evaluating engagement; first-party curve needed before diagnosing drop. | INSUFFICIENT_EVIDENCE |
| Search: target “balance after 70”? | CH-000003 transcripts/titles show age and balance themes; no search traffic | DOC-000016: keyword/intent checklist | T21/T45 conflict on SEO | [Search Help](https://support.google.com/youtube/answer/16090438?hl=en) supports query relevance. Check actual query demand and channel Search traffic; do not stuff tags. | MODERATE concept, LOW channel outcome |
| Browse/Home: stronger emotional title? | CH-000003 public outliers known, Home impressions/CTR unknown | DOC-000005/013: truthful promise and visual clarity | T39 personalized Home; T48 differentiation | [Home guidance](https://support.google.com/youtube/answer/141805?hl=en) is viewer-specific. Build a clear, truthful candidate; cannot claim Home lift until Analytics/test. | LOW |

## 38. Corpus vs Official YouTube Model

**WHAT THE CORPUS SAYS:** J and E repeatedly describe a viewer-matching system influenced by audience fit, click appeal, watch behavior and satisfaction. They also mix in an asserted small-batch test sequence, semantic era, trust scores, 48-hour cliffs, formulaic metadata/CTR thresholds, TV-long-video advantages and AEO citation tactics. Those additions come from specific creator sources or AI synthesis, not a unified platform publication. [VERIFIED_FROM_REPOSITORY: J DOC-000005/012/013/014; E T01/24/33/36/39/43/44/49/51.]

**WHAT CURRENT OFFICIAL YOUTUBE SOURCES SUPPORT:** Recommendations personalize by viewer/surface and use multiple behavior/feedback signals; performance can be understood as appeal, engagement and satisfaction; Search assesses query relevance, engagement and quality; topic interest, competition and seasonality matter; Shorts/long-form can coexist; no universal ideal length, daily cadence or long-run “best time” is specified. [VERIFIED_FROM_PRIMARY_WEB_SOURCE: [recommendations](https://support.google.com/youtube/answer/16089387?hl=en), [performance](https://support.google.com/youtube/answer/16559650?hl=en), [Search](https://support.google.com/youtube/answer/16090438?hl=en), [formats/length](https://support.google.com/youtube/answer/16559651?hl=en), [external factors](https://support.google.com/youtube/answer/16558238?hl=en), [FAQ](https://support.google.com/youtube/answer/141805?hl=en).]

**Agreement:** viewer relevance, differentiated value, promise delivery, feedback and format/context differences. **Difference:** corpus absolutes on separate channels, tags/SEO, timing, thresholds and private internals exceed or conflict with official descriptions. **Unknown:** exact production model, weights, mood clusters, private experiment effects, source authors/dates for most tabs, and channel-specific effects without Analytics. [DERIVED from sections 16–18, 24.]

## 39. Practical Operating Workflow

1. State channel, audience, format, target surface and decision question.
2. Retrieve deduplicated J/E passages with source IDs; show author/date `UNKNOWN` when unknown.
3. Check E claim IDs against the **final** 33-row validation, then current official page for time-sensitive claims.
4. Retrieve channel-relative titles, transcripts, public snapshots, real thumbnail/forensic evidence and any first-party Analytics. Keep observed versus inferred values separate.
5. Form one bounded hypothesis; search for a counterexample within same channel or peer group.
6. Output recommendation only at evidence strength supported, with sources, limitations and a reversible experiment.
7. Measure later using first-party Analytics when available; preserve the result as a new dated observation, not a rewrite of old evidence.

This fits `scripts/run_youtube_intelligence.py`'s evidence-traceable plans and `scripts/report_channel_strategy_intelligence.py`'s cross-channel diagnostics; no RAG or new production module is necessary for this audit. [INFERRED from project architecture and evidence paths.]

## 40. Recommended Next Improvements

Recommendations only; none implemented here.

1. **Normalize the remaining E tabs at claim level.** Preserve source passage, assertion type, surface, original-video link/creator/date when verifiable, and a duplicate group. Prioritize T21/T24/T30/T33/T35/T44/T45/T47 because they contain consequential mechanism or numeric assertions absent from the existing 33 claims. [INFERRED from section 5 and current claim coverage.]
2. **Repair metadata, not raw evidence.** In a separate authorized change, correct stale J PDF page counts and the Hook “byte-identical” comment; add publication/publisher/source-video fields only after direct verification. Preserve existing hashes and original files. [VERIFIED_FROM_REPOSITORY: section 26.]
3. **Use first-party channel Analytics.** The catalog's ingestion path is ready, but no real export exists. CTR by traffic source, retention curves, device split, returning viewers and format overlap would test high-impact hypotheses that public views cannot. [VERIFIED_FROM_REPOSITORY: `AGENTS.md`, `docs/Phases.md`, CH-000003 report.]
4. **Keep a small current-official reference register.** Date-check official pages and record when a claim's bounded validation changes. Avoid promoting a whole creator video merely because one sentence agrees with Help. [INFERRED from sections 17–18.]
5. **Evaluate retrieval without infrastructure first.** Text search over source IDs, tabs, pages and claim rows with dedup/authority filtering can test real use cases before considering production RAG. [INFERRED from section 34, `AGENTS.md`.]

## 41. Final Mental Model

**J is the creative workshop. E is the creator-research clipping file. Official YouTube pages are the platform reference. Channel evidence is the local test.** Combine them by asking a decision question, retrieving a *specific* passage, checking its source/date/authority, comparing channel data, and designing an experiment. Do not replace channel evidence with a global rule or turn a creator's explanation of the algorithm into fact. [DERIVED from all sections.]

### Required knowledge matrix

This is the fast retrieval view. “Current verification” applies only to the stated bounded proposition; section 16 retains all 33 E dispositions. Each source resolves through section 5 to its raw path/member. [VERIFIED_FROM_REPOSITORY; primary links in section 17.]

| Knowledge / claim | Dataset | Topic | Source | Evidence class | Current verification | Practical use | Limitation |
|---|---|---|---|---|---|---|---|
| Individual viewer matching, surface-dependent | 018 | Recommendations | T39, CLM-001 | P? source; primary web independently | CONFIRMED_BY_PRIMARY_SOURCE, bounded | Surface-aware explanation | Weights unknown |
| Satisfaction uses multiple signals | 018 | Analytics | T39, CLM-004 | P? source; primary web independently | CONFIRMED_BY_PRIMARY_SOURCE | Avoid single-score model | No weights |
| Watch history matters chiefly on Home | 018 | Home | T48, CLM-011 | P? source; primary web independently | CONFIRMED_BY_PRIMARY_SOURCE | Interpret Home context | Other surfaces differ |
| Suggested can use viewer history | 018 | Up Next | T39, CLM-006 | P? source | CONSISTENT_WITH_PRIMARY_SOURCE | Related-video hypothesis | Exact matcher unknown |
| Formats can coexist by audience fit | 018 | Shorts/long-form | T39, CLM-005/REC-003 | P? source; primary web independently | CONSISTENT_WITH_PRIMARY_SOURCE | Format experiment | Conversion not guaranteed |
| Formats must use separate channels | 018 | Shorts/long-form | T01, CLM-018 | UNVERIFIED | CONTRADICTED_BY_PRIMARY_SOURCE | Myth check | No universal rule |
| Later discovery is possible | 018 | Evergreen | T39, CLM-003 | P? source | CONSISTENT_WITH_PRIMARY_SOURCE | Avoid 48-hour cutoff | Majority-of-views claim absent |
| Repetitive mass production can violate policy | 018 | AI/monetization | T48, CLM-009 | P? source; official policy independently | CONFIRMED_BY_PRIMARY_SOURCE for policy | Policy review | Not rank penalty |
| Semantic ID full production mechanism | 018 | AI recommendations | T51, CLM-012/013 | UNVERIFIED | PLAUSIBLE_BUT_UNVERIFIED | Research question | Mood clusters/deployment unknown |
| TV share and long-form duration statistics | 018 | TV/length | T49, CLM-014/015 | EXPERIENTIAL | CREATOR_OBSERVATION_ONLY | Request underlying dataset | Private sample missing |
| Early answer guarantees AI citation | 018 | AEO | T43, REC-007 | UNVERIFIED | INSUFFICIENT_EVIDENCE | Test as content clarity only | No YouTube citation formula |
| Off-platform profiles confer trust score | 018 | Off-platform | T43, REC-008 | UNVERIFIED | INSUFFICIENT_EVIDENCE | Brand hypothesis | Platform mechanism absent |
| Channel keyword/tags push recommendations | 018 | Metadata | T24 | UNVERIFIED | INSUFFICIENT_EVIDENCE | Search myth review | Query relevance ≠ push |
| “SEO is dead” | 018 | Search | T45 | UNVERIFIED | CONTRADICTED_BY_PRIMARY_SOURCE | Myth review | Search still uses relevance |
| Best upload hour guarantees virality | 018 | Timing | T33 | UNVERIFIED | CONTRADICTED_BY_PRIMARY_SOURCE as universal | Scheduling discussion | Early viewing may vary |
| Hook context/interruption/payoff | 011 | Hook | DOC-000002/003 | DERIVED_ANALYSIS | NOT A PLATFORM FACT | Draft/review alternatives | Duplicate pair; effect unmeasured |
| BUT/THEREFORE causal story | 011 | Script | DOC-000015/006/013 | DERIVED_ANALYSIS | NOT A PLATFORM FACT | Improve story coherence | No ranking guarantee |
| One truthful title/thumbnail promise | 011 | Packaging | DOC-000005/013 | DERIVED_ANALYSIS | CONSISTENT_WITH_PRIMARY_SOURCE | Packaging checklist | Design effect channel-specific |
| 10%+ CTR goal | 011 | CTR | DOC-000005 | UNVERIFIED | INSUFFICIENT_EVIDENCE | Do not adopt as target | Traffic-source mix varies |
| Title formulas, Tom Brady angles | 011 | Titles | DOC-000011/014 | DERIVED_ANALYSIS | NOT A PLATFORM FACT | Generate distinct concepts | Repeated material; no tests |
| Senior-health truth hierarchy | 011 | Governance | DOC-000013 | DERIVED_ANALYSIS | NOT A PLATFORM FACT | Keep source labels | Model prompt, not official standard |
| SEO checklist | 011 | Search | DOC-000016 | UNVERIFIED | PARTIAL official concept support | Publishing review | Tags/keyword recipes overclaim |
| AI image/video prompt guides | 011 | Production | DOC-000008/009 | DERIVED_ANALYSIS | PRODUCT CURRENTNESS UNKNOWN | Creative draft/reference | Tool behavior may change |
| Claim-level validation rather than document authority | 011+018 | Evidence | DOC-000013; CLM register | DERIVED_ANALYSIS | METHOD SUPPORTED BY PROVENANCE NEED | Agent grounding | Not a substitute for source check |

### Required use-case matrix

`YES` means corpus has directly usable *source-labeled material* for that task, not that it proves an outcome. `PARTIAL` means validation or channel data is essential. `NO` means no safe direct basis. [DERIVED from sections 5, 16–18, 27.]

| Use case | DS-000011 | DS-000018 | Combined | Notes |
|---|---|---|---|---|
| Topic research | YES | YES | YES | J workflow plus E differentiated-topic claims; check actual demand |
| Title research | YES | YES | YES | J formulas, E cases; test channel-relative |
| Thumbnail research | YES | YES | YES | Source concepts only; real assets/testing needed |
| Hook research | YES | PARTIAL | YES | J deeper; retention data absent |
| Script research | YES | PARTIAL | YES | J frameworks; E creator examples |
| Editing research | PARTIAL | PARTIAL | PARTIAL | No moving-image evidence for source claims |
| Algorithm understanding | PARTIAL | PARTIAL | PARTIAL | Official source required for platform facts |
| Search strategy | PARTIAL | PARTIAL | PARTIAL | Search-specific official check and traffic data |
| Browse/Home strategy | PARTIAL | PARTIAL | PARTIAL | Surface-specific Analytics absent |
| Shorts strategy | PARTIAL | YES | PARTIAL | E broad but many unsupported tactics; format test needed |
| Audience strategy | YES | YES | YES | Define audience; validate overlap locally |
| Analytics interpretation | PARTIAL | PARTIAL | PARTIAL | No first-party metric exports in corpora |
| Experiment design | YES | YES | YES | Hypothesis sources; outcomes still to measure |
| Content blueprint | YES | YES | YES | Use labeled advice with channel evidence |
| AI prompt grounding | YES | PARTIAL | YES | Cite exact passage and validation |
| RAG | PARTIAL | PARTIAL | PARTIAL | Needs normalization, dedup and date/authority metadata |
| Myth verification | YES | YES | YES | Official pages supply decisive check |

### Final terminal summary

```text
DS-000011 + DS-000018 DEEP AUDIT COMPLETE

DS-000011
Files: 17 physical, 7,002,608 bytes
Substantive unique sources: 16
Date range: publication UNKNOWN; captured/registered 2026-08-27; one 2025 self-tag
Main source types: 14 PDF, 2 DOCX, 1 Markdown; guides, prompts, mixed compilations
Main topics: hooks, scripts, titles/thumbnails, SEO, AI visual prompts, creator strategy
Official-source coverage: 0 directly preserved official works
Duplicate/overlap rate: 1/17 physical files repeats another file's text (5.9%); semantic overlap unquantified
Primary practical role: labeled creative and workflow reference

DS-000018
Files: 1 ZIP, 566,739 bytes; 63 tab Markdown members + 1 JSON manifest
Substantive unique sources: 61 video-source texts
Date range: publication UNKNOWN; snapshot 2026-09-02; content mentions 2026/forward-looking 2027
Main source types: creator video descriptions and transcripts; 2 platform-attributed interviews
Main topics: discovery, audience, Shorts, Search, small-channel strategy, packaging, TV, AI
Official-source coverage: 0 directly preserved official works; 2 platform-attributed transcripts
Claims extracted: 33 selected passages (18 claims, 5 interpretations, 10 recommendations)
Officially verified: 10 SUPPORTED bounded dispositions in 2026-09-08 register
Consistent but not explicitly verified: 12 PARTIALLY_SUPPORTED dispositions
Unverified: 8 NOT_SUPPORTED_BY_PRIMARY_EVIDENCE; 2 NOT_CURRENTLY_VERIFIABLE
Contradicted/stale: 1 CONTRADICTED; publication dates mostly UNKNOWN, so exact stale count UNKNOWN
Primary practical role: creator-claim watchlist and hypothesis source

COMBINED
Unique knowledge units: UNKNOWN until full claim-level normalization; 50 existing registry rows are selected rules, not a complete semantic census
Major topic groups: discovery/audience, concept/packaging, viewing experience, publishing/business, AI workflow
Duplicate knowledge: 1 J duplicate text file, 2 E duplicate/near-duplicate tabs; other paraphrase overlap unquantified
Contradictions: 8 evidence-backed topic pairs documented
Stale knowledge: exact count UNKNOWN; time-sensitive mechanisms flagged for review
Current knowledge: only bounded claims independently supported by current official pages
Major gaps: source authors/dates, first-party Analytics, causal experiments, private ranking mechanics

USABILITY
Topic research: YES
Packaging research: YES
Hook/script research: YES
Algorithm/discovery research: PARTIAL
Strategy: YES, conditional on channel evidence
Content planning: YES, with provenance
AI grounding: PARTIAL until claim-level normalization
RAG readiness: NEEDS NORMALIZATION

CORE DISTINCTION
DS-000011: creative workshop and prompt/checklist library, not official platform training data.
DS-000018: creator-video research snapshot and claim watchlist, not an official 2026 algorithm release.

BEST WAY TO USE THEM TOGETHER:
Retrieve specific deduplicated passage; verify source/date/claim; compare dated channel evidence; make hypothesis; run measurable experiment.

BIGGEST RISK IF MISUSED:
Creator or AI interpretation silently becomes a universal YouTube ranking fact.

FINAL MENTAL MODEL:
J supplies creative lenses; E supplies creator claims; official sources bound platform facts; channel evidence tests local decisions.

SOURCE DATA MODIFIED:
NO
```
