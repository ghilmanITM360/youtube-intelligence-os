# Complete Data Visualization Strategy

Method: the dataviz procedure (form first, color by job, validate the palette, thin marks, hover by default, table view, then look at the render). Forms were chosen from each dataset's *job*. Several datasets are best shown as **not a chart** (stat tile, meter list, table).

## 1. Layering

**Overview** (Home KPI row, niche cards) → **Categories** (niche, channel lists) → **Exploration** (channel tabs, compare, workstreams) → **Records** (video, plan, provenance).

## 2. Dataset-by-dataset matrix

| # | Dataset | Visualization | Job → why | Fields | Source / transform | Default | Advanced | Filters / sort | Drill-down | Related | Responsive | Empty / error | A11y | Perf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | Corpus totals | **KPI row** (stat tiles) | headline numbers → not a chart | channels, videos, transcripts (deduped) | read model counts | 4 tiles | delta vs last build | — | tile → filtered list | sources count | 2×2 | "read model not built" | numbers are text | precomputed |
| V2 | Workstream progress | **Meter list** | ratio per named row | done, total, blocker | workstream index | one row each | history line on page | — | row → workstream page | pinned branch | full width | "no workstreams" | text figure beside every bar | static |
| V3 | Niche activity | sparkline per niche card | trend, glanceable | uploads per month | group by niche, month | 24 months | — | — | card → niche | — | same | flat line + note | aria summary | precomputed |
| V4 | Channels | **table** + optional ranked bar | many classes → table | name, subs, videos, median views, outliers, depth | read model | sorted by median views | column chooser | niche, tier, status | row → channel | compare tray | card list | "no channels match" | native table | virtualize > 200 |
| V5 | Channel views per video | **strip/dot plot**, log y, median line, outliers emphasized (1 accent, rest gray) | distribution + emphasis | published_at, views, type | latest snapshot per video | last 24 months, long-form | Shorts toggle, linear scale | type, date brush | dot → video | median, P90 lines | sparkline + top-5 list on phone | "no metrics: <reason>" | table toggle, keyboard dots | ≤ 6k points, canvas above 2k |
| V6 | Uploads over time | **column** per month | magnitude over time | published_at | count by month | 24 months | weekly | type | bar → videos in month | — | fewer ticks | — | table | trivial |
| V7 | Outliers | **ranked horizontal bars**, multiple of channel median | rank parts | views, channel median | ratio | top 10 | top 50 | niche, date | bar → video | thumbnail beside label | list | "no outliers (n too small)" | labels are text | trivial |
| V8 | Coverage matrix (75 × 8 / 825 layers) | **heatmap** with status scale + icon per cell | grid of states | channel, capability, status, reason | registry | sorted by completeness | gap reasons | niche, status | cell → artifact/gap | — | one channel per row, scroll | — | icon + label, table | 600-825 cells: SVG ok |
| V9 | Strategy actions | **grouped labeled lists** | categorical identity, few items | action, item, evidence count | strategy JSON | grouped by action | heuristics | — | item → videos | confidence | same | NOT_AVAILABLE card | icons + text | — |
| V10 | Benchmark (2-4 channels) | **small multiples**, shared y per metric; **dumbbell** for period change | compare series without dual axis | metric per channel | benchmark JSON / read model | 3 metrics | more metrics | period | panel → channel | sample-size note | stacked panels | "only 1 channel in niche" | fixed entity colors, legend + direct labels | trivial |
| V11 | Content plan coherence | **11-cell status strip** | states in sequence | dimension, status | plan JSON | strip + labels | per-dimension text | — | cell → section | — | wraps 2 rows | — | text labels | — |
| V12 | Plan stages | document + stepper (no chart) | reading | plan JSON | — | all stages collapsed except opportunity | evidence lists | — | evidence → video | counter-evidence | single column | NOT_AVAILABLE stage | headings | — |
| V13 | Finance audit progress | meter + **line** over time (accepted cumulative) | trend | accepted_at | audit files / git dates | meter | line | channel | → queue | reanalysis meter | meter only | — | table | precomputed |
| V14 | Audit / review queue | **table** with status chips | records | id, video, status, date | audit index | pending first | validator output | status, channel | → record | rules | card list | "queue empty" | chips = icon+label | paginate |
| V15 | Forensic timeline | **timeline** (horizontal lanes: shots, text cards, events) over duration | events over time | t_start, t_end, type, label | ledger | all lanes | event detail | lane toggle | event → frame | seal status | vertical list on phone | "no forensic evidence for this video" | event list alternative | lazy-load frames |
| V16 | Thumbnails | **image grid** sorted by outlier multiple | visual comparison | thumbnail, title, multiple | thumbnail evidence + media library | 24 | lightbox | channel, topic | → video | title pattern chips | 2 columns | URL-only → placeholder + note | alt = title | lazy, srcset |
| V17 | Transcript search | result list + snippet highlight | text retrieval | snippet, video, source | FTS5 | top 20 | all | channel, niche, source | → transcript at offset | — | same | "no matches" | text | FTS server-side |
| V18 | Reference rules | grouped list by rule class + conflicts | categorical | rule, class, conflicts | reference DB | grouped | section text | class | → rule page | assessed videos | same | — | badges with text | — |
| V19 | Evidence files | faceted **table**, disposition facet as thin segmented bar | records + part-to-whole beside figures | disposition, path, hash | inventory | INGEST + SUPPORTING only | all dispositions | disposition, dataset | → file record | duplicates | card list | — | table | paginate 45k |
| V20 | Seals / evidence map | status **table** | records | video, PASS/FAIL, location | consolidation CSVs | FAIL first | hashes | status | → video | — | list | — | icons + text | small |
| V21 | Freshness | status table, stale first | records | artifact, status, basis | freshness registry | stale first | dependency path | status | → artifact | — | list | "all current" | text | small |
| V22 | Acquisition cost | stat tiles + run table | headline + records | usd, runs | Apify tables | total + last run | per run | date | → run | — | tiles | "no runs" | text | small |
| V23 | Cross-store sources | **source chips** ("Seen in: Registry · Finance DB · SH core") | identity, few items | store list per entity | read model crosswalk | chips | per-field origin | — | chip → provenance | — | wraps | — | text | — |
| V24 | First-party KPIs (when present) | KPI row + one-axis **line** per metric, competitor median as gray context | trend + emphasis | date, metric | first-party diagnosis | 90 days | compare periods | date range | point → day | — | one metric per card | "no export imported" | table | local |
| V25 | Template-network / independence (SH Report 2) | **cluster list** (no force graph) with member counts | grouping; graph adds little at this size | cluster, members | report tables | collapsed clusters | members | — | → channels | independent units count | same | — | text | — |

Network/relationship graphs were considered and **rejected** for v1: the relationships here are shallow (≤ 3 hops) and well served by context links and source chips. A force-directed graph would add motion without answering a question faster.

## 3. Interaction plan

- Cross-filter: strip-plot brush → video table; heatmap cell → filtered channel list.
- Chart-to-detail: every mark navigates (Enter/click) to its entity.
- Date range: one control per page, in the filter row; comparisons use dumbbells, not overlaid dual series.
- Grouping: niche → channel → video aggregation is precomputed in the read model.
- Contextual explanation: ⓘ on chart titles explains the metric (e.g. "multiple of channel median, long-form only").
- Export: CSV of the chart's data (permitted data only; first-party never in shared exports).

## 4. Color plan

Categorical fixed order for channels in Compare (≤ 4 at once, so all-pairs safety holds); one sequential ramp for counts/heatmaps; status palette reserved for coverage and seals (always icon + label); emphasis (accent + gray) for outliers. Validate with `scripts/validate_palette.js` (dataviz skill) in light and dark mode before implementation.

## 5. Performance budget

Read model precomputes aggregates; charts render ≤ 6k points as SVG (switch to canvas above 2k marks); thumbnails lazy-load; first contentful paint < 1 s from local disk.
