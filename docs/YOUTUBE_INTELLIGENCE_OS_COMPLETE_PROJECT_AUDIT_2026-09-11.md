# YouTube Intelligence OS — Complete Project Audit (2026-09-11)

Canonical human/AI handoff document. Grounded in live repository state at commit
`5629687` (verified `origin/main`, local main, and live remote main all identical
at the time of writing). This document explains the whole system so a future
UI-development task can proceed without re-deriving architecture from scratch.

---

## 1. What Is This Project?

**One-paragraph summary:** YouTube Intelligence OS is a local-first, evidence-preserving
system that ingests raw YouTube channel/video/transcript/thumbnail/analytics evidence,
classifies it, and derives layered, provenance-traceable intelligence (topic, packaging,
hook, script, editing, channel strategy, competitor benchmark, new-channel blueprint) that
a creator or strategist can use to decide what to continue, fix, reduce, or test — without
ever letting an AI guess silently become a claimed fact.

**Nontechnical explanation:** Imagine you run (or want to run) a YouTube channel and you
have a pile of evidence about your own and competitors' videos — titles, thumbnails,
transcripts, view counts, retention curves, your own private Studio analytics. This system
organizes that pile, keeps a clear paper trail for every claim it makes, and produces a
structured diagnosis: which topics/formats are repeatable winners vs. one-off flukes, why
specific videos are succeeding or failing, how you compare to named competitors, and what a
brand-new channel in a niche should do differently. It never invents data it wasn't given,
and it is explicit whenever it doesn't have enough evidence to answer a question.

**Technical explanation:** A SQLite catalog (`data/catalog/youtube_inventory.db`, 27 tables,
schema migrations 1–10) stores canonical entities (datasets, channels, videos, transcripts,
classifications, visual/forensic evidence, first-party analytics inputs) with full
provenance. A set of read-only Python report scripts derive JSON/Markdown "intelligence"
artifacts on top of that catalog, each one declaring its evidence layer, source hashes, and
generation method. A deterministic incremental-refresh planner tracks a dependency graph
between artifacts (via `data/intelligence/system/intelligence-freshness-registry.json`) so
that only artifacts genuinely affected by new evidence are ever regenerated — nothing is
silently stale, and nothing is regenerated needlessly. No network calls happen except two
narrowly-scoped, opt-in acquisition adapters (a bounded Apify YouTube scraper and a
registered-thumbnail downloader); everything else is pure local computation over already-
ingested evidence.

**Who it's for:** a solo or small-team creator/strategist who wants a disciplined,
falsifiable content strategy tool — not a general analytics dashboard, and not a
push-button "generate my next video" tool.

**What it deliberately does NOT do:**
- No live YouTube API integration, no scraping beyond one bounded pilot adapter.
- No UI, no RAG, no agents, no vector database (explicitly deferred to Phases 10–12,
  not started).
- No universal "this will go viral" scoring — every diagnosis is scoped to a channel,
  a niche, and an evidence layer.
- No fabricated competitor private metrics (CTR, retention, watch time) — competitors
  only ever get public-evidence treatment.
- No promotion of an AI interpretation into a claimed fact.

---

## 2. Core Objective

The system implements this pipeline:

```
LARGE YOUTUBE DATA (raw exports, transcripts, thumbnails, analytics)
  → FILTER / NORMALIZE (classification, provenance-tagged extraction)
  → IDENTIFY SUCCESS / FAILURE (relative, cohort-based — never a fixed view threshold)
  → FIND REPEATABLE VS ONE-OFF PATTERNS (family-level aggregation across ≥3 items)
  → COMPARE COMPETITORS (benchmark within same-niche peer groups only)
  → DIAGNOSE A TARGET CHANNEL (channel strategy: what's working/failing and why)
  → DETERMINE WHAT TO CONTINUE / FIX / REDUCE / TEST (action taxonomy, evidence-backed)
  → BUILD A BETTER NEW-CHANNEL STRATEGY (blueprint: proven patterns + gaps + falsification criteria)
  → RECALIBRATE WHEN NEW EVIDENCE ARRIVES (incremental refresh, affected-layers-only)
```

This differs from a topic generator, title generator, thumbnail generator, or analytics
dashboard because:
- Every conclusion carries its evidence layer (fact vs. measured metric vs. AI
  interpretation vs. hypothesis) rather than presenting everything as equally certain.
- Conclusions are channel/format/date-range-relative, never a universal rule
  ("videos over X views are good") — cross-niche calibration explicitly found **0** of 7
  tested heuristics reached `ROBUST_CROSS_NICHE_PATTERN` status, and reports that honestly
  rather than forcing a rule.
- Nothing is generated speculatively — a report script only produces output for a channel
  when the underlying evidence (transcript, forensic video, first-party export) actually
  exists; otherwise the field is `NOT_AVAILABLE`, never fabricated.
- Recalibration is structural: new evidence invalidates only the specific downstream
  artifacts that depend on it, tracked by a dependency graph, not a blanket "regenerate
  everything."

---

## 3. Data Foundation

- **Raw evidence** (`data/raw/`): original supplied bytes — CSV/XLSX exports, video files,
  screenshots, documents. Immutable once ingested; gitignored (privacy + repo-size policy).
- **Catalog/database** (`data/catalog/youtube_inventory.db`): canonical structured facts
  derived from raw evidence, with full provenance back to source files/hashes. Gitignored;
  only manifests/provenance records are committed to git.
- **Datasets**: 19 canonical datasets (`DS-000001`…`DS-000019`), each with a semantic class
  (see §8) and a manifest describing scope and disposition.
- **Channels**: 5 canonical channels registered from those datasets.
- **Canonical content items**: 303 videos.
- **Transcripts**: 303 transcript records (302 `AVAILABLE`, 1 `UNAVAILABLE`).
- **Thumbnail references/snapshots**: 115 `thumbnail_evidence` rows; 5,172 `visual_assets`
  rows (acquired image snapshots + derived observations combined); 244 `visual_observations`.
- **Forensic evidence**: registered actual video-frame/keyframe evidence exists for exactly
  one channel (`CH-000004`) — this is why editing/visual intelligence is real for that
  channel only.
- **Training knowledge / platform knowledge**: two special datasets, `DS-000011` (a
  17-document creative/creator corpus — algorithm guides, hook/packaging/script analyzers,
  prompt guides) and `DS-000018` (a 63-tab, ~245,914-word 2026-algorithm-update research
  corpus, 33/33 primary-source dispositions completed). See §8.
- **First-party analytics exports**: capability is `READY`; no real owned-channel export has
  been ingested yet. Normalized private snapshots would live under gitignored
  `data/intelligence/first-party/` (does not currently exist on disk).
- **Derived intelligence**: versioned JSON/Markdown artifacts under `data/intelligence/`,
  committed to git (except the private first-party subtree).

**RAW → EXTRACTED → NORMALIZED → INTELLIGENCE** maps onto: `data/raw/` (untouched source) →
`data/extracted/` (deterministic pulls) → `data/normalized/` (structured, provenance-tagged
entities, largely realized as the SQLite catalog) → `data/intelligence/` (derived,
versioned, human/AI-readable conclusions). Source data at each layer is never edited in
place; every regeneration produces a new dated artifact.

---

## 4. Evidence Model

The canonical evidence taxonomy (defined in `docs/Database.md`) has 10 states:

| State | Meaning |
|---|---|
| `RAW_SOURCE` | Original supplied bytes/file. Immutable. |
| `EXTRACTED_FACT` | Deterministically pulled from raw source (a CSV cell, a video's frame rate). |
| `MEASURED_FACT` | Computed via a defined, repeatable measurement (shot-length stats, hashes). |
| `OBSERVATION` | A human/tool-noted fact not present as a raw field (e.g. "this screenshot shows a vidIQ overlay"). |
| `AI_INTERPRETATION` | An AI-generated reading/summary/judgment, always traceable to its source(s). |
| `HUMAN_INTERPRETATION` | A person's judgment, recorded as theirs — not a fact. |
| `HYPOTHESIS` | An unvalidated idea. Explicitly not a recommendation. |
| `RECOMMENDATION` | A validated, actionable suggestion — still distinct from fact. |
| `SUSPECT` | Looks like fact but isn't independently verified; must be surfaced as such. |
| `SUPERSEDED` | A replaced record, kept for the audit trail, never deleted. |

**Why this matters:** it lets every downstream consumer (a person, or eventually a UI) tell
at a glance whether a statement is "the source file said X," "we computed X," "the AI
thinks X," or "this is an untested idea." Mixing these categories is exactly how strategy
tools become unreliable.

**How the system prevents AI interpretation from silently becoming platform fact:** every
classification and intelligence row carries an explicit `evidence_layer` (or equivalent
field) and provenance chain back to a raw source hash. Concretely, in the live database,
`content_classifications.classification_dimension = CONTENT_FORMAT` rows are always
`VERIFIED` (a deterministic, low-ambiguity judgment), while `CONTENT_TOPIC` rows are always
`PROPOSED` (an AI-assisted judgment that has not been promoted to `VERIFIED`) — the system
encodes the fact/AI-interpretation boundary directly into a required status field rather
than relying on convention. A related but narrower semantic-class axis (A–H, in
`docs/DATA_CLASSIFICATION.md`) separately tags *what kind* of knowledge a dataset holds
(global platform knowledge, competitor evidence, forensic video, channel-specific
intelligence, etc.), orthogonal to the fact/interpretation axis.

One caveat worth flagging for the UI team: the DB currently implements a narrower
operational subset of the 10-state model (mainly `EXTRACTED_FACT`, `MEASURED_FACT`,
`OBSERVATION`, `VERIFIED`/`PROPOSED` status) — `SUSPECT`, `HUMAN_INTERPRETATION`,
`HYPOTHESIS`, `RECOMMENDATION`, and `SUPERSEDED` exist as documented concepts and appear as
prose labels in some Markdown artifacts, but are not yet normalized DB columns/enums
everywhere. This is a documented, not hidden, gap (see §23 System Gaps).

---

## 5. Database Architecture

**Schema version:** 10 migrations applied (`schema_meta` table, latest 2026-09-10: "Register
supplied thumbnail references and transcript timing quality without fabricating an
acquisition run"). **Table count:** 27.

Grouped logically:

- **Dataset / file provenance:** `datasets`, `source_locations`, `source_files`,
  `discovered_files`, `file_relationships`, `ingestion_runs`, `ingestion_errors`,
  `dataset_relationships`.
- **Channels / content:** `channels`, `channel_dataset_links`, `channel_snapshots`,
  `videos`, `video_snapshots`.
- **Transcripts:** `transcripts`.
- **Classification:** `content_classifications`, `entity_classifications`.
- **Forensic / visual evidence:** `thumbnail_evidence`, `visual_assets`,
  `visual_observations`.
- **Source runs / ingestion (multimodal + Apify):** `source_batches`, `batch_roots`,
  `apify_source_runs`, `apify_result_records`, `apify_run_cost_observations`,
  `document_records`.
- **Intelligence support:** `field_provenance` (per-field provenance chain), `schema_meta`.
- **First-party analytics:** no persistent DB schema exists for first-party analytics —
  by design, normalized snapshots are private, versioned JSON files under
  `data/intelligence/first-party/` rather than SQLite rows, so ingesting real analytics
  never touches the canonical catalog.

Relationships in human terms: a `dataset` is the unit of provenance for everything ingested
from one source; a `channel` and its `videos` are linked back to the dataset(s) that
established them; every `transcript`, `thumbnail_evidence`, `visual_asset`, and
`content_classification` row references its owning `video`, its `dataset`, and the specific
`source_file`/`ingestion_run` that produced it — so any claim in the system can be traced
back to an exact file and byte range.

---

## 6. Datasets

19 canonical datasets. Representative entries (full detail in
`data/manifests/DS-0000XX.md`):

| Dataset | Purpose | Channel | Content Type | Status |
|---|---|---|---|---|
| DS-000001 | Structured YouTube Studio-style export (Phase 1B) | CH-000001, CH-000002 | Channel/video/transcript entities | Registered |
| DS-000002–DS-000016 | Recursive multi-source multimodal ingestion (Phase 1C), 45,774 files, 100% dispositioned | mixed / supporting | documents, images, OCR/semantic sources | Registered |
| DS-000011 | Global YouTube creator/algorithm knowledge corpus (17 docs) | — (platform knowledge) | PDFs, prompt guides | Ingested, fully characterized |
| DS-000017 | xkcd's What If? channel evidence | CH-000004 | videos + forensic evidence | Registered |
| DS-000018 | 2026 Algorithm Update research corpus (63-tab doc export) | — (platform knowledge) | creator-research claims | Structured-registered, 33/33 dispositioned |
| DS-000019 | Dr. Elias Senior Health channel evidence | CH-000005 | videos, transcripts | Registered |

(Datasets DS-000002–DS-000016 are supporting multimodal/document sources rather than
channel-defining sources; see `data/manifests/` for the full per-dataset breakdown — this
audit intentionally does not restate all 19 in full prose per the task's own instruction to
stay concise.)

---

## 7. Channels

| Channel ID | Name | Niche | Item Count | Available Evidence | Intelligence Coverage |
|---|---|---|---|---|---|
| CH-000001 | Matty Invests | Finance | 94 | 93 transcripts | Topic, Packaging, Hook/Script, Channel Strategy, Benchmark, Blueprint, Unified Plan |
| CH-000002 | Mr. Finance | Finance | 65 | 65 transcripts | Topic, Packaging, Hook/Script, Channel Strategy, Benchmark, Blueprint, Unified Plan |
| CH-000003 | Dr. Aliza Wright \| Advice | Health | 32 | 32 transcripts | Topic, Packaging, Hook/Script, Channel Strategy, Benchmark, Blueprint, Unified Plan |
| CH-000004 | xkcd's What If? | Science | 83 | 83 transcripts + forensic video evidence | Topic, Packaging, Hook/Script, **Editing**, Unified Plan (no peer-group benchmark/blueprint — only channel in its niche) |
| CH-000005 | Dr. Elias Senior Health | Health | 29 | 29 transcripts | Topic, Packaging, Hook/Script, Channel Strategy, Benchmark, Blueprint, Unified Plan |

CH-000004 exists in the corpus specifically to exercise the editing/visual intelligence
layer against real forensic evidence (frame-level analysis), which no other channel
currently has. The two finance channels and two health channels exist specifically to
validate the channel-strategy/benchmark engine bidirectionally within a niche (each channel
diagnosed against the other as competitor).

---

## 8. Platform / Training Knowledge

- **YouTube platform facts:** authoritative claims about how the platform behaves
  (algorithm mechanics, discovery signals). Sourced primarily from `DS-000018` where a claim
  has been validated as an official/primary-source-backed statement.
- **Creator heuristics:** informal "what creators believe works" claims — mostly from
  `DS-000011` and the unvalidated portions of `DS-000018`. Treated as testable hypotheses,
  not facts, until the corpus evidence agrees or disagrees with them.
- **Training frameworks:** the analyzer/checklist documents in `DS-000011` (hook, packaging,
  script analyzers) that inform *how* the system's intelligence scripts structure their
  archetypes — not data to be cited as fact, but methodology.
- **Corpus evidence:** the actual channel/video/transcript/analytics data in the SQLite
  catalog — the only source that can validate or falsify a channel-specific empirical claim.

**DS-000011** (Global Knowledge Corpus, 17 documents — algorithm guides, hook/packaging/
script analyzer PDFs, a viral checklist, VEO3/Nano-Banana prompt guides, a "YouTube
Intelligence Brain v1" markdown) and **DS-000018** (63-tab Google Doc export, ~245,914
words, 33/33 primary-source dispositions completed, described in its own manifest as
containing "unverified creator and source-attributed claims about YouTube discovery,
audience behavior, and creator strategy") are consumed by
`scripts/report_channel_strategy_intelligence.py`'s `build_training_registry()` function as
a provenance-tagged registry — the system re-uses these documents' vetted claims, it does
not re-derive or re-validate them from scratch each run.

**Precedence rule:** official primary evidence (validated `DS-000018` claims) wins for
platform-behavior questions; corpus evidence (the actual channel's own data) wins for
channel-specific empirical strategy questions; training heuristics (`DS-000011` and
unvalidated `DS-000018` claims) remain testable/falsifiable rather than authoritative until
the corpus evidence confirms them for a specific channel.

---

## 9. Classification Engine

`scripts/classify_content_pilot.py` registers two classification dimensions per video:

- **CONTENT_TOPIC** — subject-matter classification (from a controlled vocabulary,
  including e.g. `SCIENCE_HYPOTHETICALS`, `STEM_EXPLANATIONS` for CH-000004). Always
  recorded with status `PROPOSED` — an AI-assisted judgment not yet promoted to fact.
- **CONTENT_FORMAT** — structural/format classification. Always recorded with status
  `VERIFIED` — a lower-ambiguity, deterministic-enough judgment.

Each classification row carries `evidence_layer`, `source_locator`, and
`classification_method` for full provenance and reproducibility.

Live counts: 604 classification rows total (302 `CONTENT_FORMAT`/`VERIFIED` + 302
`CONTENT_TOPIC`/`PROPOSED`), covering 302 of 303 videos. The one remaining video has zero
classification rows — it is **evidence-blocked, not guessed**: the system leaves it
unclassified rather than fabricate a topic/format for a video it lacks sufficient evidence
to classify confidently. This is a deliberate design choice, not an oversight.

---

## 10. Topic Intelligence

`scripts/report_topic_opportunity.py` (generic, works across all 5 channels) builds, per
channel:
- **Topic families** — groupings of videos by classified topic.
- **Performance normalization** — relative (views/day or best-available public proxy,
  never raw view count) so that older and newer videos, and different channels, can be
  compared fairly.
- **Outlier detection** — flags individual videos whose performance is far from their
  family's norm, distinguishing them from the family's typical behavior.
- **Repeatability** — a family needs multiple (3+) supporting items before it's called a
  "strong"/repeatable pattern; a single high performer is flagged as a possible one-off,
  not evidence of a repeatable family.
- **Strong vs. weak families** — families are explicitly labeled by their evidence strength,
  not just their average performance.
- **Internal candidates / opportunities** — under-explored topic families with some
  supporting signal, flagged as testable candidates rather than guaranteed winners.
- **Web/external validation:** not currently wired in for this layer (no live web search is
  part of this system) — any "external validation" happening elsewhere in the system comes
  from the pre-ingested `DS-000011`/`DS-000018` corpora, not live web calls.

**Limitations:** entirely bounded by what's in the corpus — a channel with fewer videos
(e.g. CH-000005 at 29) has proportionally weaker repeatability evidence than one with more
(CH-000001 at 94).

---

## 11. Packaging Intelligence

`scripts/report_packaging_intelligence.py` (generic) covers:
- **Titles** — extracted verbatim, classified into title archetypes.
- **Thumbnail acquisition** — `scripts/acquire_registered_thumbnails.py` downloads *only*
  already-registered thumbnail URLs (the one network-calling report-adjacent script besides
  the Apify adapter), producing an immutable snapshot — it does not re-derive URLs or guess
  at missing ones.
- **Visual evidence / thumbnail archetypes** — derived from the acquired snapshot images
  where available.
- **Title-thumbnail pair relationships** — package-level hypotheses about how title and
  thumbnail work together.
- **Package hypotheses** are explicitly labeled `HYPOTHESIS`, not fact.
- **Temporal uncertainty:** a thumbnail acquired *today* is a snapshot of the *current*
  thumbnail — YouTube creators frequently change thumbnails after publication. The system
  is explicit that **current thumbnails do not prove historical causation** for a video's
  original performance; any packaging-performance association is flagged as an association
  observed with present-day evidence, not a proven causal claim about what drove the
  original view count.

---

## 12. Hook Intelligence

`scripts/report_hook_script_intelligence.py` (one unmodified generic reporter across all 5
channels — confirmed, no channel-specific branches) covers:
- **Opening windows** — the measured first N seconds of a transcript (timing derived from
  transcript timing-quality metadata, e.g. `EXACT_TIMESTAMPED` vs. `POSITIONAL_ONLY`).
- **Timing quality** — explicitly tracked per transcript; a hook conclusion drawn from
  low-quality timing is flagged as weaker evidence than one from exact timestamps.
- **Measured hook features** — objective properties of the opening (e.g. question posed,
  claim stated, structure).
- **AI-interpreted hook archetypes** — pattern labels applied to the measured features,
  explicitly tagged as `AI_INTERPRETATION`.
- **Package → hook promise match** — whether the packaging (title/thumbnail) promise is
  paid off by the actual hook content.
- **Performance association** — `OBSERVED_FIRST_PARTY_ASSOCIATION` or the equivalent
  public-evidence association, never a hard causal rule.
- **Why competitor retention is not fabricated:** retention/AVD data is private first-party
  Studio data. Competitors never get one, so the system never invents a competitor
  retention curve — competitor hook analysis is limited to what's observable publicly
  (transcript timing, structure), and the report is explicit when that's all it has.

---

## 13. Script Intelligence

Also produced by `report_hook_script_intelligence.py` (script intelligence and hook
intelligence share the same reporter and evidence chain):
- **Script phases** — segmentation of the transcript into structural phases (intro, body,
  payoff, outro or similar).
- **Script archetypes** — AI-interpreted structural patterns across phases.
- **Payoff structure** — whether/how the video's opening promise is resolved.
- **Pacing proxies** — measured proxies for pacing (word rate, phase-length ratios) drawn
  from transcript timing, not fabricated.
- **Counter-evidence** — the system explicitly looks for and records evidence that
  contradicts a proposed archetype, rather than only collecting confirming evidence.
- **Content blueprints:** script-level patterns feed into the higher-level new-channel
  blueprint (§18), not a separate blueprint of their own.
- Measured data (pacing proxies, phase timing) is kept distinct from AI interpretation
  (archetype labels) throughout — the same fact/interpretation separation as everywhere
  else in the system.

---

## 14. Editing / Visual Intelligence

`scripts/report_editing_visual_intelligence.py` (generic script, conditionally available
output):
- **Actual forensic evidence requirement:** this layer only produces real analysis when
  frame-level forensic video evidence has been registered for a channel. Today that's
  **CH-000004 only**.
- **Keyframes / visual states / visual pacing:** derived from registered forensic evidence
  (frame extraction, `image_pipeline.py`'s perceptual-hash/metadata helper feeding
  `visual_assets`/`visual_observations`).
- **Script→visual alignment:** whether visual changes align with script phase transitions,
  where evidence exists.
- **Editing archetypes / blueprints:** pattern labels applied only where forensic evidence
  supports them.
- **Why thumbnail ≠ editing evidence, and transcript ≠ editing evidence:** a thumbnail is a
  single static image chosen for the video's listing page, not a sample of in-video editing;
  a transcript captures words, not cuts, pacing, or visual treatment. Neither substitutes
  for actual frame-level evidence, so the system does not infer editing intelligence from
  either.
- **Graceful `NOT_AVAILABLE`:** for the 4 channels without forensic evidence, the editing
  layer reports `NOT_AVAILABLE` rather than guessing from transcript/thumbnail proxies — a
  dedicated cross-channel `editing-intelligence-availability` artifact documents this
  explicitly for all 5 channels.

---

## 15. Success / Failure Intelligence

The model is strictly **relative**, never a fixed universal threshold:
- **Video-level states:** a video's performance is assessed against its own topic family's
  median/typical performance within the same channel and comparable date range — never
  against a hardcoded view count.
- **Family-level states:** a topic/format family is judged as a repeatable winner only with
  ≥3 supporting videos showing consistent above-median performance; a single viral video is
  explicitly labeled as a possible one-off, not proof of a repeatable pattern.
- **Why one viral video ≠ a repeatable winner:** a single outlier could be luck, an external
  event, algorithmic promotion unrelated to content quality, or any number of one-time
  factors — the system requires repeated evidence before calling a pattern reliable.
- **Why universal view thresholds are avoided:** absolute view counts are not comparable
  across channels of different sizes/ages, or across different niches — a "good" video for a
  29-video channel and a 94-video channel look nothing alike in raw numbers.

---

## 16. Channel Strategy Intelligence

`scripts/report_channel_strategy_intelligence.py` (one unmodified generic engine, validated
bidirectionally on 2 independent niches: health CH-000005↔CH-000003, finance
CH-000001↔CH-000002) composes the lower layers (topic, packaging, hook/script, editing
where available) plus the training/platform knowledge registry (§8) into:
- **What works / what fails**, at both the video and family level.
- **Repeatable winners** (≥3-item families with consistent above-median performance) vs.
  **one-off successes** (single outliers) vs. **weak experiments** (insufficient evidence
  either way).
- **Root-cause layers:** a diagnosis is attributed to the specific layer most likely
  responsible (topic demand, packaging response, hook/intro drop, mid-video retention,
  traffic-source dependence, audience mismatch, format mismatch, loyalty weakness) rather
  than a single opaque "this video did badly" verdict.
- **Action taxonomy:** `CONTINUE`, `DOUBLE_DOWN`, `FIX`, `REDUCE`, `STOP`, `TEST`, `WATCH` —
  defined and assigned in code (`ACTION_TYPES` set + `generate_actions()`), each action
  attached to specific evidence. `DOUBLE_DOWN` requires a repeatable, above-median pattern;
  `FIX`/`REDUCE` apply to below-median recurring patterns; `WATCH` applies to mixed or
  single-outlier-dependent signals.
- **Evidence / counter-evidence / falsification:** every diagnosis records the evidence
  supporting it and explicitly looks for counter-evidence; heuristics that later evidence
  contradicts are downgraded, not silently discarded.

---

## 17. Competitor Benchmark

Peer groups are **within-niche only**, currently:
- **Health:** CH-000005 vs. CH-000003.
- **Finance:** CH-000001 vs. CH-000002.

CH-000004 (science) has no peer in the corpus, so it has no benchmark/blueprint artifact —
correctly reported as unavailable rather than benchmarked against an unrelated niche.

The **cross-niche calibration** artifact
(`data/intelligence/system/cross-niche-strategy-calibration-2026-09-11.json`) tested 7
calibrated heuristics across the two available niches and found: **0**
`ROBUST_CROSS_NICHE_PATTERN`, 1 `NICHE_SPECIFIC_PATTERN`, 1 `CHANNEL_SPECIFIC_PATTERN`, 3
`CONFLICTING_PATTERN`, 2 `INSUFFICIENT_EVIDENCE`. This is reported honestly as an evidence-
coverage limitation (only 2 channels per niche, 2 niches total) rather than forced into
false universal rules — with more channels/niches, this same unmodified engine would likely
surface genuinely robust cross-niche patterns; the current near-zero robust-pattern count is
a data-depth artifact, not a methodology failure.

---

## 18. New-Channel Blueprint

The blueprint subcommand of `report_channel_strategy_intelligence.py` composes benchmark
output for a niche into a blueprint covering: target audience, positioning, niche
boundaries, content pillars, proven patterns (backed by repeatable-winner evidence),
patterns explicitly flagged as *not* to blindly copy (one-off or channel-specific,
non-transferable), underexploited gaps, title/hook/script principles, experiment
categories, and falsification criteria (what evidence would prove a blueprint assumption
wrong).

**Blueprint ≠ competitor clone:** the blueprint is built from the *pattern-level* evidence
across peer channels (what topic/packaging/hook approaches repeatedly work in the niche),
not a copy of any single competitor's specific videos — and it explicitly separates
"proven, transferable" patterns from "channel-specific, do not copy" ones.

Two blueprints exist today: finance and senior-health (matching the two benchmarked niches).

---

## 19. Unified Orchestrator

`scripts/run_youtube_intelligence.py` composes, per channel and per opportunity:

```
CHANNEL → OPPORTUNITY → PACKAGE → HOOK → SCRIPT → EDITING (where available)
```

into one evidence-traceable content plan (JSON + Markdown, under
`data/intelligence/plans/`). **Graceful degradation:** each layer is optional in the final
plan — a channel without forensic evidence simply omits the editing section (marked
`NOT_AVAILABLE`) rather than failing to produce a plan at all. Missing one layer does not
kill the workflow because the orchestrator treats each layer as an independent, optionally-
present input rather than a hard dependency chain that must all succeed.

Plans exist today for all 5 channels' primary candidate opportunity.

---

## 20. Incremental Refresh System

- **Dependency graph:** encoded in `scripts/plan_intelligence_refresh.py` — maps each change
  type (e.g. `NEW_TRANSCRIPT`, `NEW_THUMBNAIL_REFERENCE`, `NEW_FORENSIC_EVIDENCE`,
  `NEW_FIRST_PARTY_ANALYTICS`) to the set of artifact types it can invalidate.
- **Freshness registry:** `data/intelligence/system/intelligence-freshness-registry.json` —
  32 artifacts, each with `ARTIFACT_ID`, `ARTIFACT_SHA256`, `ARTIFACT_TYPE`, `CHANNEL_IDS`,
  `CURRENT_STATUS`, and `SOURCE_DEPENDENCIES` (upstream code + artifact hashes).
- **Stale detection:** keyed on canonical IDs, DB content hashes, and generator/code
  hashes — file modification times are explicitly ignored, so touching a file without
  changing its meaning never triggers a false-positive refresh.
- **Dry-run:** the planner never writes files or DB rows; it only computes what *would* be
  affected.
- **Affected-only refresh:** `scripts/refresh_youtube_intelligence.py` regenerates only the
  artifacts the planner identifies as stale, writing a new successor artifact (never
  overwriting history) only when the regenerated content is semantically different from the
  prior version.
- **Historical intelligence preservation:** every refresh creates a new dated artifact and
  logs a run report under `system/refresh-runs/`; nothing is deleted or silently replaced.
- **Confidence upgrade/downgrade, action/blueprint versioning:** new evidence can strengthen
  (upgrade) or weaken (downgrade) a prior conclusion's confidence; each new version is a
  distinct artifact so the history of how a conclusion evolved is preserved.

**Examples of what different new evidence invalidates:**
- *New transcript* → topic/packaging/hook/script layers for that channel, and anything
  downstream (channel strategy, benchmark, blueprint, unified plan) that consumed them.
- *New thumbnail* → packaging intelligence for that channel and downstream layers.
- *New forensic evidence* → editing/visual intelligence for that channel (and its
  `EDITING_AVAILABILITY` status), plus downstream layers.
- *New channel* → that channel's own layers, plus benchmark/cross-niche-calibration
  artifacts if it joins an existing niche peer group.
- *New metric snapshot* (public or first-party) → success/failure and channel-strategy
  layers, and — for first-party specifically — `FIRST_PARTY_DIAGNOSIS`, explicitly
  **excluding** `CROSS_NICHE_CALIBRATION`/`TRAINING_CALIBRATION` (private data never
  contaminates cross-niche public-pattern calibration).

Verified live: running the planner with no simulated change returns
`NO_REFRESH_REQUIRED` against all 32 registered artifacts (0 stale, 0 partially-stale, 0
blocked, 0 unknown) — the registry is fully current as of this audit.

---

## 21. First-Party Analytics

**Capability:** ready; **real data ingested: no.**

- **Formats:** CSV, TSV, XLSX (YouTube Studio / Advanced Mode exports).
- **Metrics supported when present in an export:** views, impressions, impressions-CTR,
  watch-time hours, average view duration, average percentage viewed, unique viewers,
  subscribers gained/lost, likes/comments/shares, new/casual/regular/returning viewers,
  retention percentage, intro-30s percentage. Missing metrics are simply absent from output
  — never synthesized.
- **Traffic sources / audience segments:** normalized dimensions (traffic source, search
  term, geography, subscription status, format, elapsed video time, audience segment),
  preserved as reported, never invented.
- **OWN vs. COMPETITOR:** first-party metrics are exclusively for channels marked
  `CHANNEL_OWNERSHIP_CONTEXT=FIRST_PARTY`. Competitors only ever receive public-evidence
  treatment — private metrics are structurally prevented from being projected onto
  competitor rows (`COMPETITOR_PRIVATE_METRICS = NOT_AVAILABLE` unless canonical competitor
  evidence explicitly contains them).
- **Snapshot versioning:** identity is a composite of channel, source file hash, sheet,
  report type, observation window, date-range kind, and filters. Overwrite policy is
  `NEVER`; an exact re-import is recognized as `EXACT_DUPLICATE`; a conflicting re-import
  under the same identity is rejected as an error.
- **Storage:** raw copies under gitignored `data/raw/inbox/first-party-analytics/`;
  normalized private snapshots under gitignored `data/intelligence/first-party/`. Neither
  directory currently exists on disk — confirming no real ingestion has occurred.
- **Current truth:** the pipeline (import → diagnose → refresh-trigger) is fully built and
  tested against synthetic fixtures only; it is waiting on a real Studio export from an
  actual owned channel before it produces a production diagnosis.

---

## 22. What the System Can Answer Today

Given sufficient evidence for the channel/niche in question, this system can currently
support answering questions like:
- Why is this channel succeeding or struggling, broken down by topic, packaging, hook, and
  (where forensic evidence exists) editing?
- Which topic families are backed by repeatable (3+ item) evidence vs. resting on a single
  outlier?
- Which specific viral result looks like a one-off rather than a repeatable pattern?
- What does one named competitor in the same niche do differently in packaging, topic
  choice, or hook structure — using only public evidence?
- What should this channel continue, double down on, fix, reduce, or test — with the
  specific evidence behind each recommendation?
- If building a new channel in the health or finance niche, what positioning, content
  pillars, and title/hook/script principles are supported by the two benchmarked
  competitors in that niche, and which patterns should *not* be blindly copied?
- Which title/hook/script patterns are evidence-supported vs. still hypotheses?
- Which prior conclusions weakened or strengthened after new evidence (transcript,
  thumbnail, forensic evidence, or first-party analytics) was ingested — visible via the
  refresh-run history.
- What changed in the system's understanding after a new channel joined an existing niche
  peer group (via cross-niche/benchmark recalibration).

This audit deliberately does not fabricate example outputs for these questions — the actual
per-channel artifacts under `data/intelligence/channels/` and `data/intelligence/cross-
channel/` contain the real, current answers.

---

## 23. What the System Cannot Know

**Data/evidence limitations (would resolve with more evidence, not more code):**
- No competitor private analytics (CTR, retention, watch time) exist or ever will by
  design — competitors are structurally public-evidence-only.
- Forensic video evidence exists for only 1 of 5 channels, so editing/visual intelligence
  is genuinely unavailable for the other 4 until such evidence is registered.
- Only 2 channels per niche (health, finance) and no peer at all for the science channel —
  benchmark/blueprint confidence is limited by this small peer-group size.
- No first-party analytics have been ingested yet, so own-channel diagnostic enrichment has
  zero production evidence behind it (fixture-tested only).
- Longitudinal (multi-snapshot) trend analysis, for both public metrics and first-party
  analytics, requires ≥2 compatible observation windows — currently unavailable everywhere
  since only single snapshots exist.

**Genuine system capability gaps (would require new engineering, not new data):**
- No documented, runnable, end-to-end CLI chain exists (in any doc) linking new-channel
  registration → classification → topic/packaging/hook/script/editing →
  channel-strategy → blueprint → refresh into one sequence; the pieces are all
  independently documented and runnable, but the full chain is only described narratively
  (Phases.md, v1-status doc), not as a single worked command sequence. This is a
  documentation/operator-ergonomics gap, not a missing capability.
- The 10-state evidence taxonomy from `docs/Database.md` is only partially realized as
  normalized DB columns/enums (see §4) — some evidence states exist only as prose labels in
  Markdown artifacts today.
- No service/API/query layer exists yet in front of SQLite + JSON artifacts (see §32) — this
  is the primary blocker for UI development, not a data problem.

---

## 24. Current Data Depth

| Niche | Channels | Notes |
|---|---|---|
| Finance | 2 (CH-000001, CH-000002) | Benchmarked bidirectionally; blueprint exists |
| Health | 2 (CH-000003, CH-000005) | Benchmarked bidirectionally; blueprint exists |
| Science | 1 (CH-000004) | No peer; forensic-evidence pilot channel; no benchmark/blueprint |

More channels per niche directly improve:
- **Benchmark confidence** — a 2-channel peer group can only show "channel A differs from
  channel B," not "this is a niche-wide pattern"; 4–6 channels per niche would let the
  existing benchmark engine distinguish niche-wide patterns from single-competitor quirks.
- **Cross-niche calibration** — the 0-robust-pattern result in §17 is a direct consequence
  of having only 2 niches with 2 channels each; more niches and more channels per niche
  would let the same unmodified calibration engine actually surface robust patterns where
  they exist.
- **Success/failure reliability** — larger topic families (more videos per family) sharpen
  the repeatable-vs-one-off distinction described in §15.

None of this requires new backend architecture — the topic/packaging/hook/channel-strategy/
benchmark engines are already generic and channel-count-agnostic; they simply need more
registered channels to run against.

---

## 25. Repository Map

```
data/raw/           Original supplied bytes (gitignored). Entry point: data/raw/inbox/.
data/catalog/       SQLite canonical database (gitignored). youtube_inventory.db is canonical.
data/manifests/     Per-dataset/batch manifest records (committed — provenance, not raw data).
data/intelligence/  Derived, versioned JSON/Markdown intelligence artifacts (committed,
                    except gitignored data/intelligence/first-party/ private analytics).
scripts/            All ingestion, classification, reporting, orchestration, and refresh
                    Python scripts (~35), plus scripts/README.md and source_adapters/.
tests/              20 test files + tests/fixtures/ (includes synthetic first-party-
                    analytics fixtures — never real data).
docs/               Architecture, Database, DATA_CLASSIFICATION, DATA_ENTRY_WORKFLOW,
                    Phases, DECISIONS, Security, STATUS_QUERIES, FIRST_PARTY_ANALYTICS_
                    WORKFLOW, and historical audit docs.
schemas/            Versioned SQL migrations (001_initial.sql … current), inventory/.
config/             Placeholder only (README), reserved for justified future config.
channels/           Placeholder only (README), reserved for future per-channel workspaces.
logs/               Placeholder only (README), not yet populated.
```

No `api/`, `server/`, or UI/frontend directory exists anywhere in the repository — confirms
that UI/service-layer work genuinely has not started, consistent with Phases 10–12 being
explicitly deferred.

---

## 26. Important Script Map

| Script | Role | Input | Output | Safe to run directly? | Mutating/Read-only |
|---|---|---|---|---|---|
| `register_supplied_channel.py` | Register a channel workbook + transcripts | XLSX + transcript dir | channel/video/transcript DB rows | Yes, with real args | Mutating (DB) |
| `register_batch.py` | Bulk multi-root discovery + registration | Source roots | discovered_files/datasets rows | Yes | Mutating (DB) |
| `register_structured_source.py` | Phase 1B structured registration | Dataset-shaped source | structured entity rows | Yes | Mutating (DB) |
| `inventory_catalog.py` | Core inventory infra (init/ingest/verify) | `--source`, `--dataset-id` | catalog rows, manifests | Yes | Mutating (DB) |
| `classify_content_pilot.py` | Register topic/format classifications | item list / batch manifest | `content_classifications` rows | Yes | Mutating (DB) |
| `report_topic_opportunity.py` | Topic Opportunity Intelligence | `--channel` | JSON/MD artifact | Yes | Read-only |
| `report_packaging_intelligence.py` | Packaging Intelligence | `--channel`, upstream artifacts | JSON artifact | Yes | Read-only |
| `acquire_registered_thumbnails.py` | Download registered thumbnail URLs | `--channel` | images + manifest | Yes (network, HTTPS-only) | Read-only DB / writes files |
| `report_hook_script_intelligence.py` | Hook + Script Intelligence | `--channel`, upstream artifacts | JSON/MD artifact | Yes | Read-only |
| `report_editing_visual_intelligence.py` | Editing/Visual Intelligence | `--channel`, upstream artifacts | JSON/MD/availability artifact | Yes | Read-only |
| `report_channel_strategy_intelligence.py` | Diagnosis / benchmark / blueprint | `diagnose`/`benchmark`/`blueprint` subcommands | JSON/MD artifacts | Yes | Read-only |
| `run_youtube_intelligence.py` | Unified orchestrator | `--channel`, `--opportunity` | Content plan JSON/MD | Yes | Read-only |
| `plan_intelligence_refresh.py` | Read-only refresh planner | `--channel`, `--simulate-change`, `--write-registry` | Plan JSON / freshness registry | Yes | Read-only (unless `--write-registry`, still deterministic) |
| `refresh_youtube_intelligence.py` | Executes affected-only refresh | `--channel`, `--simulate-change`, `--dry-run` | Successor artifacts + run report | Yes | Writes intelligence artifacts only, never catalog DB |
| `ingest_youtube_analytics.py` | First-party analytics import | `--source`, `--channel`, `--ownership` | Private normalized JSON + validation report | Yes | Reads DB read-only; writes files only |
| `report_first_party_channel_diagnosis.py` | Own-channel diagnosis | `--analytics`, `--competitor` | Diagnosis JSON | Yes | Read-only |
| `apify_youtube_ingest.py` | Bounded Apify acquisition pilot | `--channel-url`, `--cost-cap`, `APIFY_TOKEN` | Catalog rows + cost manifest | Only with explicit authorization/token/cost cap | Mutating (DB) + network |
| `generate_batch_manifests.py` | Regenerate manifests from DB | `batch_id` | Manifest/coverage files | Yes | Read-only DB / writes files |
| `report_dataset_matrix.py` / `report_channel_coverage.py` / `report_corpus_status.py` | Status reporting | `--db-path`, `--json` | Markdown/JSON reports | Yes | Read-only |

---

## 27. Artifact Map

- **Channel intelligence** (`data/intelligence/channels/CH-0000XX/`): per-channel topic,
  packaging, hook/script, (editing where available), and channel-strategy-diagnosis
  artifacts.
- **Cross-channel intelligence** (`data/intelligence/cross-channel/`): packaging/topic
  comparisons, niche benchmarks, editing-intelligence-availability summary.
- **System intelligence** (`data/intelligence/system/`): v1 status/capabilities, freshness
  registry, cross-niche calibration, training-knowledge registry, first-party analytics
  contract/capability-status, refresh-run logs.
- **Blueprints** (`data/intelligence/blueprints/`): niche-level new-channel blueprints
  (finance, senior-health).
- **Refresh reports** (`data/intelligence/system/refresh-runs/`): one report per executed
  refresh run, permanent audit trail.
- **Capability registry:** `INTEL-0031` in the freshness registry — a system-wide artifact
  tracking which capabilities are live per channel.
- **Training registry:** `INTEL-0032` — the `DS-000011`/`DS-000018`-derived provenance-
  tagged knowledge registry.
- **First-party capability artifacts:** the import contract and capability-status JSON
  files under `data/intelligence/system/` (versioned, public — these describe the
  *capability*, not any private data).

---

## 28. Full End-to-End Workflows

**A. New competitor channel:** register via `register_supplied_channel.py` (or the
multimodal `register_batch.py` path for less-structured sources) → classify with
`classify_content_pilot.py` → run `report_topic_opportunity.py`,
`report_packaging_intelligence.py`, `report_hook_script_intelligence.py` for the new
channel → if it joins an existing niche, re-run `report_channel_strategy_intelligence.py
benchmark` for that niche → optionally re-run `blueprint` → run
`plan_intelligence_refresh.py` to confirm registry state, then `--write-registry`.

**B. New data for an existing channel:** ingest new raw evidence → 
`plan_intelligence_refresh.py --channel <ID>` to preview affected layers → 
`refresh_youtube_intelligence.py --channel <ID> --simulate-change NEW_TRANSCRIPT --dry-run`
→ same command without `--dry-run` → review the report under
`data/intelligence/system/refresh-runs/`.

**C. New thumbnails:** register the thumbnail reference → 
`acquire_registered_thumbnails.py --channel <ID>` → `plan_intelligence_refresh.py
--simulate-change NEW_THUMBNAIL_REFERENCE` (or `NEW_THUMBNAIL_BINARY`) → 
`refresh_youtube_intelligence.py` with the same change type.

**D. New forensic video evidence:** register the forensic evidence (frame extraction via
`image_pipeline.py` + loader scripts into `visual_assets`/`visual_observations`) → 
`plan_intelligence_refresh.py --simulate-change NEW_FORENSIC_EVIDENCE` → 
`refresh_youtube_intelligence.py` with the same change type — this is what would make
editing intelligence available for a channel beyond CH-000004.

**E. New public metric snapshot:** register the snapshot → `plan_intelligence_refresh.py
--simulate-change NEW_PUBLIC_METRIC_SNAPSHOT` → `refresh_youtube_intelligence.py`.

**F. New first-party analytics export:**
```
.venv/bin/python -B scripts/ingest_youtube_analytics.py \
  --source /absolute/path/to/report.csv --channel <ID> --ownership FIRST_PARTY \
  --observation-start <date> --observation-end <date> --date-range-kind <KIND> \
  --export-date <date>
.venv/bin/python -B scripts/report_first_party_channel_diagnosis.py \
  --analytics <path to normalized JSON> --competitor <peer channel ID>
.venv/bin/python -B scripts/refresh_youtube_intelligence.py \
  --channel <ID> --simulate-change NEW_FIRST_PARTY_ANALYTICS --dry-run
```

**G. Create a channel strategy diagnosis:**
`.venv/bin/python -B scripts/report_channel_strategy_intelligence.py diagnose --target <ID>
--benchmarks <peer benchmark artifact path(s)>`

**H. Build a new-channel blueprint:**
`.venv/bin/python -B scripts/report_channel_strategy_intelligence.py blueprint --niche
<niche> --benchmarks <benchmark artifact path(s)>`

**I. Run incremental refresh (general form):**
`.venv/bin/python -B scripts/plan_intelligence_refresh.py [--channel <ID>]` (dry-run
preview) → `.venv/bin/python -B scripts/refresh_youtube_intelligence.py [--channel <ID>]
--simulate-change <TYPE> --dry-run` → same without `--dry-run` → 
`.venv/bin/python -B scripts/plan_intelligence_refresh.py --write-registry` once satisfied.

None of these command forms are invented — each is either drawn directly from
`docs/DATA_ENTRY_WORKFLOW.md`, `docs/FIRST_PARTY_ANALYTICS_WORKFLOW.md`, or the scripts'
own `--help` output.

---

## 29. Current Project Health (live, verified 2026-09-11)

- **Git state:** clean except 3 pre-existing, unrelated untracked items
  (`.codex/environments/`, two older standalone audit docs dated 2026-08-31/2026-09-01) —
  none touched by this task.
- **Main HEAD:** `5629687`. **Origin/main:** `5629687`. **Live remote main:** `5629687`. All
  three match — main is fully up to date and was not modified by this task.
- **Test count:** 285 passed, 0 failed, 0 skipped, 1 pre-existing unrelated warning
  (duplicate-zip-entry warning in `test_register_structured_source.py`, not a Step-24/audit
  artifact).
- **DB integrity:** `ok`. **FK violations:** 0.
- **Freshness status:** `NO_REFRESH_REQUIRED` (fresh dry-run against all 32 registered
  artifacts).
- **Stale artifact count:** 0 (32 `CURRENT`, 0 stale/partial/blocked/unknown).
- **Current capability status:** Foundation/provenance complete; classification working;
  platform knowledge validated; training knowledge structured/calibrated; topic, packaging,
  hook, script intelligence generalized-working across all 5 channels; editing/visual
  intelligence working where forensic evidence exists (CH-000004 only); channel strategy,
  benchmark, and blueprint generalized-working for the 2 benchmarked niches; unified
  orchestration working; incremental refresh working; first-party analytics ingestion
  ready; own-channel diagnostic enrichment ready for real data, none ingested yet.

---

## 30. Backend Maturity Assessment

| Dimension | Assessment |
|---|---|
| Architecture maturity | **MATURE** — consistent provenance model, evidence-layer discipline, deterministic dependency-graph refresh; validated across 2 independent niches with one unmodified engine. |
| Data foundation | **WORKING** — 19 datasets, 5 channels, 303 items, 302/303 classified; solid but narrow (2 channels/niche, 1 forensic-evidence channel). |
| Intelligence coverage | **WORKING** — topic/packaging/hook/script generalized to all channels; editing intentionally partial (evidence-gated, not a defect). |
| Strategy capability | **WORKING** — channel strategy/benchmark/blueprint validated bidirectionally on 2 niches; cross-niche calibration correctly reports low confidence given current evidence depth. |
| Refresh / maintenance | **MATURE** — dependency graph, freshness registry, dry-run planning, and versioned successor artifacts are all live and verified with 0 stale artifacts. |
| First-party readiness | **WORKING** (capability) / **NOT_READY** (production evidence) — pipeline fully built and tested on synthetic fixtures; zero real ingested exports. |
| Testing | **MATURE** — 285 tests, 0 failures, includes determinism and privacy-guard tests. |
| Documentation | **PARTIAL** — most subsystems individually well-documented (Database, DATA_ENTRY_WORKFLOW, FIRST_PARTY_ANALYTICS_WORKFLOW, Phases), but no single doc chains the full new-channel-to-blueprint CLI workflow end to end (see §23). |
| UI readiness | **NOT_READY** — no service/API/query layer exists; see §32. |

---

## 31. Technical Debt / Risks

- **P1 — No service/API/query layer in front of SQLite + JSON artifacts.** A future UI has
  no stable, typed interface to consume; it would otherwise need to open SQLite directly or
  parse Markdown/JSON files ad hoc. This is the single biggest blocker to UI work and should
  be the first UI-adjacent engineering task.
- **P1 — Undocumented end-to-end CLI workflow chain** (§23, §28): the full new-channel →
  blueprint pipeline is only described narratively, not as one worked command sequence.
  Low effort to fix (a doc, not code), but worth doing before onboarding new operators or a
  UI "run pipeline" feature.
- **P2 — Partial realization of the 10-state evidence taxonomy in the DB** (§4, §23): some
  evidence states exist only as prose labels in Markdown, not normalized DB enums. Not
  blocking current capabilities, but would need resolution before a UI tries to render
  evidence-state badges generically from the DB alone.
- **P2 — Small peer-group sample size** (2 channels/niche, 2 niches, 1 unpaired channel):
  limits benchmark/cross-niche confidence. Resolved by ingesting more channels, not by new
  engineering — flagged as a data-depth risk, not an architecture risk.
- **P3 — Large, single-purpose report scripts** (e.g.
  `report_channel_strategy_intelligence.py` spans diagnose/benchmark/blueprint/training-
  registry in one file). Manageable at current scale; a service layer built on top of these
  scripts should wrap them rather than refactor them prematurely.
- **P3 — Local-SQLite-only assumption.** Fine for current single-operator, local-first
  scope; would need revisiting only if multi-user concurrent write access became a
  requirement (not currently planned).
- **No P0 found.** Nothing discovered during this audit constitutes a severe, silently-
  wrong, or currently-breaking defect.

---

## 32. UI Readiness Audit

**Is the backend ready for a UI?** Not directly — but it is ready for a *thin read-service
layer* to be built on top of it, after which UI work becomes straightforward.

- **Can the UI consume SQLite directly?** Not recommended. The catalog DB is gitignored,
  machine-local, and its schema/query patterns are an internal implementation detail (raw
  SQL joins across 27 tables) — coupling a UI directly to it would break the moment the
  schema evolves (10 migrations already, more expected).
- **Can the UI consume the JSON artifacts directly?** Partially. Channel/cross-
  channel/system intelligence artifacts are already structured JSON with fairly consistent
  shapes — a UI *could* read these as static files for a read-only dashboard, but there's no
  index/manifest of "what artifacts currently exist and are current" other than the
  freshness registry, and no HTTP-servable boundary (they're local files).
- **Can the UI consume Markdown artifacts?** Only for human-readable display (e.g. rendering
  a diagnosis report as-is) — not for structured data binding.
- **Can the UI shell out to CLI scripts?** For read-only reports, yes in principle (they're
  deterministic and side-effect-free), but this is fragile as a long-term UI data path
  (process-spawn latency, no typed response contract, no auth/permission boundary).

**Recommendation:** build a small, read-mostly service/query layer (even a lightweight local
HTTP API or a typed Python query module) that: (1) wraps `report_common.connect()`-style
read-only SQLite access, (2) reads the freshness registry to know which JSON artifacts are
current, (3) exposes a stable, versioned JSON contract per §33 below, and (4) explicitly
gates any mutating action (ingestion, refresh execution) behind clear confirmation, never
exposing raw SQL or file-system paths to the UI layer. This adapter should be built as its
own thin layer, not by modifying the existing report scripts, so all 285 tests and the
freshness registry stay untouched.

---

## 33. UI Data Contract (Proposed Read Model)

| UI Concept | Current Backend Source | Readiness | Missing Adapter |
|---|---|---|---|
| System Overview | `system/v1-status`, `system/v1-capabilities`, freshness registry | High | Small aggregator to merge these into one overview payload |
| Channels (list) | `channels` table + `channel-strategy-diagnosis`/topic/packaging artifacts | High | Query wrapper over SQLite + artifact index |
| Channel Profile | `channels`/`videos` tables + all per-channel artifacts | High | Same as above, per-channel join |
| Videos | `videos`, `transcripts`, `content_classifications`, `thumbnail_evidence` | High | Query wrapper (no existing script lists raw video rows as JSON) |
| Topic Intelligence | `channels/CH-*/topic-opportunity-intelligence-*.json` | High | None — already structured JSON |
| Packaging Intelligence | `channels/CH-*/packaging-intelligence-*.json` | High | None |
| Hook Intelligence | `channels/CH-*/hook-script-intelligence-*.json` | High | None |
| Script Intelligence | Same artifact as Hook Intelligence | High | None |
| Editing Intelligence | Per-channel editing artifact (CH-000004) + `editing-intelligence-availability` | High (with explicit `NOT_AVAILABLE` for 4/5 channels) | None |
| Success / Failure | Embedded within topic/channel-strategy artifacts, not a standalone artifact | Medium | Small extraction/reshape adapter if a standalone view is wanted |
| Strategy Diagnosis | `channels/CH-*/channel-strategy-diagnosis-*.json` | High | None |
| Competitor Benchmark | `cross-channel/*-benchmark-*.json` | High (only for the 2 benchmarked niches) | None |
| New-Channel Blueprint | `blueprints/*-blueprint-*.json` | High (finance, senior-health only) | None |
| Unified Content Plan | `plans/CH-*/...` | High | None |
| Evidence / Provenance | `field_provenance` table, `evidence_layer`/`classification_status` columns | Medium | Query wrapper; no existing script surfaces raw provenance as JSON |
| Refresh Status | Freshness registry + `plan_intelligence_refresh.py` output + `system/refresh-runs/` | High | None — already machine-readable |
| First-Party Analytics Import | `first-party-analytics-import-contract.json`, `-capability-status-*.json` | High (capability); no real data | None for capability display; real ingestion needs a UI-triggered CLI wrapper with explicit confirmation |
| System Health | Test suite, DB integrity pragmas, freshness registry | Medium | Small health-check aggregator script (none currently packages these into one JSON) |

---

## 34. Proposed Future UI Information Architecture

(Logical modules only — no visual design.)

- **Overview** — system health, capability status, channel count, last refresh state.
- **Channels** — list view sourced from the Channels read model.
- **Channel Detail** — profile + all per-channel intelligence tabs (topic, packaging, hook,
  script, editing, strategy diagnosis).
- **Videos** — per-channel video list with classification/evidence badges.
- **Intelligence** — cross-cutting views into topic/packaging/hook/script/editing artifacts,
  filterable by channel.
- **Strategy Diagnosis** — the action-taxonomy (`CONTINUE`/`DOUBLE_DOWN`/`FIX`/`REDUCE`/
  `STOP`/`TEST`/`WATCH`) view per channel, with evidence drill-down.
- **Competitor Compare** — the two currently-benchmarked niche pairs, with an honest "no
  peer available" state for CH-000004.
- **Blueprints** — the two existing niche blueprints, with an honest "not yet available"
  state for unbenchmarked niches.
- **Content Plans** — the unified orchestrator's per-channel plans.
- **Evidence Explorer** — a provenance drill-down view (fact vs. AI interpretation vs.
  hypothesis), directly serving the evidence-model transparency this system is built around.
- **Import Data** — first-party analytics import flow (CSV/TSV/XLSX upload), gated as a
  `CANONICAL_MUTATION`-adjacent action requiring explicit confirmation.
- **Refresh Center** — dry-run preview + confirmed-refresh execution, backed directly by the
  existing planner/refresh scripts.
- **System Health** — test/DB/freshness status, sourced from the System Health read model.
- **Settings** — out of scope for now; no backend concept currently corresponds to
  user-facing settings.

---

## 35. UI Action Safety

| Action | Classification |
|---|---|
| View channel diagnosis / any intelligence artifact | READ_ONLY |
| View system health / freshness status | READ_ONLY |
| Run refresh planner dry-run (`plan_intelligence_refresh.py`) | SAFE_DERIVED_ACTION |
| Run refresh with `--dry-run` (`refresh_youtube_intelligence.py`) | SAFE_DERIVED_ACTION |
| Execute refresh without `--dry-run` (writes new artifact version) | SAFE_DERIVED_ACTION (deterministic, reversible via history — but should still require explicit user confirmation in the UI) |
| Regenerate freshness registry (`--write-registry`) | SAFE_DERIVED_ACTION |
| Ingest new first-party analytics export | CANONICAL_MUTATION (writes new immutable evidence + private artifacts) |
| Register a new channel/dataset/classification | CANONICAL_MUTATION |
| Acquire registered thumbnails (network call) | CANONICAL_MUTATION (writes files) + EXTERNAL_ACTION (network) |
| Run the Apify acquisition adapter | CANONICAL_MUTATION + EXTERNAL_ACTION (network, cost-capped) |
| Publish a video / any live YouTube action | EXTERNAL_ACTION — currently entirely unsupported by this backend |

This classification should directly inform UI permission tiers: READ_ONLY and
SAFE_DERIVED_ACTION are safe for any authenticated user of a future UI; CANONICAL_MUTATION
and EXTERNAL_ACTION should require an explicit, separate confirmation step and ideally a
distinct permission level, mirroring how this audit itself was required to ask before any
push/branch-creation step.
