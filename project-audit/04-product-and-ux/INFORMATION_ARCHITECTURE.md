# Information Architecture

Organizing idea: **Discover → Understand → Explore → Compare → Inspect → Act**, mapped to five top-level areas plus global search. Niches and workstreams are the doors; channels and videos are the rooms; evidence is the foundation every value links down to.

## 1. Sitemap

```mermaid
flowchart TB
  HOME[Home: what we know, progress, insights]
  HOME --> NICHE[Niches: Finance, Senior Health, Science/What If, Other]
  NICHE --> CHL[Channels list]
  CHL --> CH[Channel page]
  CH --> CHO[Overview]
  CH --> CHV[Videos + outliers]
  CH --> CHI[Intelligence: topic, packaging, hook/script, editing]
  CH --> CHS[Strategy + benchmark]
  CH --> CHP[Plans]
  CH --> CHE[Coverage + evidence]
  CHV --> VID[Video page]
  VID --> VIO[Overview + packaging]
  VID --> VIT[Transcript + hook]
  VID --> VIF[Forensics timeline, when present]
  VID --> VIS[Sources + provenance]
  HOME --> CMP[Compare: 2-4 channels or videos]
  HOME --> PLANS[Plans: all content plans]
  PLANS --> PLAN[Plan document]
  HOME --> WS[Workstreams: Finance audit, Casual Finance, xkcd, Senior Health, Production]
  WS --> WSD[Workstream page: progress, queue, blockers]
  WSD --> REV[Review queue, later milestone]
  HOME --> KN[Knowledge: reference rules and sections]
  HOME --> EV[Evidence Library: datasets, files, ledgers, seals]
  HOME --> SYS[System: freshness, coverage matrix, acquisition costs]
  SEARCH[[Global search: channels, videos, transcripts, rules]] -.-> CH & VID & KN
```

## 2. Primary navigation

| Area | Purpose (stage) | Contains |
|---|---|---|
| **Home** | Discover | KPI row, workstream meter list, latest insights, stale-data warnings |
| **Explore** (Niches → Channels → Videos) | Understand, Explore | the entity hierarchy |
| **Compare** | Compare | side-by-side channels/videos, benchmarks |
| **Plans** | Act | content plans, production readiness (slop gate) |
| **Workstreams** | Understand, Act | research progress, queues, blockers |
| Secondary: **Knowledge**, **Evidence**, **System** | Inspect | playbook, provenance, health |

## 3. Hierarchy and parent-child relationships

`Niche ⊃ Channel ⊃ Video ⊃ {Transcript, Thumbnail, Forensic ledger, Snapshot}`. Cross-links: `Video ↔ Finance audit ↔ Reference rule`, `Plan → evidence (videos, rules)`, `Any value → Provenance record → Dataset → File`.

## 4. Navigation mechanics

| Mechanism | Rule |
|---|---|
| Breadcrumbs | on every entity page: Home / Senior Health / Dr. Okoro / Video title |
| Global search | one box, grouped results (Channels, Videos, Transcript matches, Rules); `/` shortcut |
| Filters | one row above content; chips; state in URL (shareable, back-button safe) |
| Context links | "Seen in 3 sources", "Used in plan CH-000005-CAND-001", "Supports rule R-12" |
| Quick actions | Compare (add to tray), Copy link, Export (MD/CSV/PDF), "Ask agent about this" (later; copies a prompt with IDs) |
| Deep links | every screen state is a URL: needed because the owner shares links with agents |

## 5. Naming (information scent)

Use plain labels; show internal IDs only in a secondary line or the provenance drawer.

| Internal | UI label |
|---|---|
| `NOT_AVAILABLE` | "Not available: <reason>" |
| `SEMANTIC_REVIEW_PENDING` | "Awaiting human review" |
| `ASR_UNCERTIFIED` | "Machine transcript (unverified)" |
| `AI_INTERPRETATION` | "AI reading" |
| `EXTRACTED_FACT` / `MEASURED_FACT` | "From source" / "Measured" |
| `HYPOTHESIS` | "Idea to test" |
| DS-000032 | "Decode Your Heart acquisition (DS-000032)" |

## 6. User flows

```mermaid
flowchart LR
  A[Home] -->|niche card| B[Senior Health channels]
  B -->|sort by outlier count| C[Channel page]
  C -->|Videos tab, outliers| D[Video page]
  D -->|Sources panel| E[Provenance drawer]
  D -->|add to compare| F[Compare]
  C -->|Plans tab| G[Plan document]
  G -->|evidence item| D
  G -->|export| H[MD/PDF]
```

```mermaid
flowchart LR
  A[Home] -->|Finance audit meter| B[Workstream: Finance]
  B -->|filter Awaiting review| C[Queue]
  C --> D[Audit record + evidence]
  D -->|later milestone| E[Mark reviewed: recorded as HUMAN_INTERPRETATION with reviewer + date]
```

Every dataset in DATA_TO_UI_MAPPING.md has a home in this sitemap. Branch/repo maintenance is deliberately **not** in the Explorer (GitHub and git already serve it).
