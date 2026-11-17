# Data-to-Experience Mapping

For each meaningful dataset: why it exists, who needs it, the question it answers, how users reach it, the clearest display, what goes beside it, interactions, and what stays hidden until asked. Screen names refer to `04-product-and-ux/SCREEN_BY_SCREEN_SPECIFICATIONS.md`.

**Users** (see USER_RESEARCH.md): **O** = owner/operator (non-technical decision maker), **R** = researcher/reviewer (owner in review mode, or a human semantic reviewer), **A** = AI agent (consumes the same read API, not the UI).

| Dataset | Why it exists | Who | Question answered | Discovery | Clearest display | Shown beside it | Interactions | Hidden until requested |
|---|---|---|---|---|---|---|---|---|
| Channels (registry 75 + branch stores, deduped) | the unit of competition | O, R | "Who are we watching, in which niche, how big are they?" | Home → Niches → Channels; global search | card grid / sortable table with subscriber count, video count, median views, coverage badge | niche, data-depth badge, as-of date | sort, filter by niche/tier/status, compare (select 2-4) | raw IDs, alias list, identity evidence JSON |
| Channel data layers + coverage (825 + 600 cells) | honest record of what we have | O, R | "How much do we actually know about this channel?" | Channel page header; Coverage screen | **coverage heatmap** (channels × layers, status scale + icon) | limitation reason on hover | click a cell → the gap reason / artifact | evidence_path strings |
| Availability gaps (216) | explain absences | R | "Why is this missing?" | inline empty states | empty-state message with the reason | link to the dataset that would fill it | — | — |
| Videos + snapshots (10,553 unique) | the unit of performance | O, R | "Which videos worked, relative to their own channel?" | Channel → Videos tab; search | **dot/strip plot of views by publish date** (log scale), outliers emphasized; table toggle | channel median line, video type | hover tooltip; click → Video page; filter type/date; brush a date range | raw_json, description text |
| Outliers / breakouts (Senior Health reports, packaging) | where the signal is | O | "What broke out and why might it have?" | Home insight cards; Channel → Outliers | ranked bar (multiple of channel median) | thumbnail, title, topic, evidence layer badge | click → Video; "compare with siblings" | statistical method details |
| Transcripts + FTS | what was said | R, O | "Who has talked about X, and how did they open?" | global search (full text) | search results with highlighted snippet | source label (captions / ASR uncertified / placeholder) | open full transcript, jump to hook (first 30 s) | full text by default; word timings |
| Thumbnails / visual assets | packaging evidence | O | "What do winning thumbnails look like?" | Video page; Packaging view | image grid, sorted by outlier multiple | title, views multiple | lightbox; filter by channel/topic | EXIF, perceptual hash |
| Field provenance (12,335) | trust | R | "Where did this number come from?" | ⓘ on any value | provenance drawer: source file, run, method, layer, date | dataset link | open the source file record | hashes |
| Datasets + ledgers (26/33) | provenance at batch level | R | "What batches exist and are they clean?" | Evidence Library | table with status, class, file counts | validator status | drill to files | per-file hash lists |
| Discovered files (45,774) | inventory | R | "Is this file ingested, duplicate, or noise?" | Evidence Library → Files | faceted table (disposition facet) | duplicate-of link | filter, search path | TOOLING/NOISE rows hidden by default (77% of rows) |
| Intelligence artifacts (topic, packaging, hook/script, editing, strategy) | the analysis | O | "What should this channel make next, and why?" | Channel → Intelligence tab | **insight cards** with evidence-layer badges, confidence, counter-evidence | the evidence list | expand card → evidence; open plan | full JSON |
| Strategy labels (CONTINUE/DOUBLE_DOWN/FIX/REDUCE/STOP/TEST/WATCH) | direction | O | "Keep doing what? Stop what?" | Channel → Strategy | grouped list by action, with icon + label | evidence count, confidence | click → supporting videos | heuristics |
| Benchmarks / blueprints | competitive position | O | "How does channel A compare with B?" | Compare screen | **small multiples** of the same metric per channel; dumbbell for before/after | sample size warning | swap channels | calibration JSON |
| Content plans | the action | O | "What exactly do I make, and how sure are we?" | Plans screen; Channel → Plans | **plan document** view: opportunity → package → hook → script → editing, with a coherence strip (11 dims) | NOT_AVAILABLE metrics listed explicitly; medical-validation flag | expand each stage; export MD/PDF | linkage internals |
| Reference rules + sections (33 / 1,260) | the playbook | O, R | "What does the training corpus say about X, and how reliable is it?" | Knowledge screen; search | rules list grouped by rule class; section reader | rule class badge (never "platform fact"), conflicts | search, open source section | constituent video list |
| Finance audits (558/1,612) + reanalysis | deep evidence | R | "Which videos are reviewed, which pending?" | Workstreams → Finance | **progress meter** + queue table | status chips (ACCEPTED, SEMANTIC_REVIEW_PENDING) | filter by status/channel; open audit | validator output |
| Visual forensic ledgers + seals | editing DNA | R, O | "How is this video edited, beat by beat?" | Video page → Forensics tab (when present) | **timeline** of events/shots over video duration | seal status badge, ASR status | scrub, click event → frame (local media) | raw event JSON |
| Evidence map (457 rows) + seal verification (28) | integrity | R | "Is this evidence verified and where does it live?" | Workstreams; Video page badge | status table with PASS/FAIL icons | local-only flag | filter FAIL | hashes |
| Workstream progress (CF 19/20, xkcd 29/91, finance 558/1,612) | where are we | O | "How far along is each project?" | Home | **meter list** (one row per workstream) | next blocker | click → workstream page | — |
| Apify runs + costs | spend | O | "What have we spent on data?" | Settings → Acquisition | stat tiles + run table | cost cap | — | input JSON |
| Slop-gate reports | delivery QA | O | "Is this script safe to deliver?" | Production screen | verdict badge (PASS/FAIL) + findings list + C1-C5 checklist | the disclaimer that PASS ≠ undetectable | open report | rule internals |
| Freshness registry | system health | R | "Is anything stale?" | System screen | status table, stale first | dependency path | dry-run refresh (later milestone) | dependency graph JSON |
| First-party analytics | own-channel truth | O | "How is MY channel doing?" | My Channel (when data exists) | KPI row + line charts (one axis each) | competitor median as context | date range | stays local; never synced |
| Branches / repo state | maintenance | R | "What is unmerged?" | out of scope for the Explorer (use git/GitHub) | — | — | — | — |

## Rules this mapping enforces

1. Every value rendered carries its **evidence layer** visually (badge or style) and an **as-of date**.
2. `NOT_AVAILABLE` renders as an explanatory empty state, never as zero and never as a blank.
3. Counts across stores are **deduped**, and any multi-store aggregate says how many independent sources it rests on.
4. CTR, retention and causation are never shown or implied for competitor data (AGENTS.md reference-framework rules).
5. Medical-content flags (`medical_validation_required`) are always visible on health plans.
