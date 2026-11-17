# Screen-by-Screen Specifications

Common to every screen: breadcrumbs, global search, as-of date for the data shown, loading skeletons (no spinners over 300 ms without a skeleton), an error state with a retry and the failing source named, and empty states that state the reason. Role: single local owner (no RBAC in v1). The *Access* row lists the action tier when it is not read-only. Milestone: **M1** read-only core, **M2** visualization depth, **M3** workflows.

---

### S1 Home (M1)
- **Purpose**: orient: what YIOS knows, what moved, what is blocked. **Users**: P1.
- **Data**: deduped totals (channels, videos, transcripts), workstream progress, latest insights (top outliers last 90 days), stale artifacts, local-only-evidence warning.
- **Source**: read model `entity_*`, freshness registry, workstream index (START_HERE data).
- **Layout**: KPI row (4 stat tiles) → workstream meter list → "Insights" cards (3-6) → "Needs attention" list.
- **Interactions**: every tile and meter is a link; insight card → video/channel.
- **Mobile**: tiles 2×2, meter list full width, cards as a vertical list. **Desktop**: 12-column grid.
- **Acceptance**: loads under 1 s from the local read model; every figure links to a filtered list that reproduces it.

### S2 Niches (M1)
- **Purpose**: pick a domain. **Data**: per niche: channels, videos, independent channel-units (template networks collapsed), coverage %, last refresh.
- **Layout**: 3-5 large cards; each card has a sparkline of uploads per month (all channels in the niche).
- **Acceptance**: niche totals equal the sum of their deduped channels.

### S3 Channels list (M1)
- **Purpose**: find and rank channels. **Data**: name, thumbnail/avatar URL, subscribers (as of), videos, median long-form views, outlier count, data-depth badge, coverage status.
- **Components**: data table (sortable, sticky header), filter chips (niche, tier, status, has transcripts), compare checkbox.
- **Mobile**: card list with the 3 key figures. **Acceptance**: sorting and filtering are URL state; 159+ rows render without lag (virtualized above 200).

### S4 Channel page (M1, tabs M1-M2)
- **Header**: name, handle, niche, subscribers, video count, data-depth badge, "Seen in N sources", as-of.
- **Tabs**: Overview · Videos · Intelligence · Strategy · Plans · Coverage.
  - *Overview*: stat tiles; uploads-over-time column chart; views-per-video strip plot (log) with median line; top 5 outliers.
  - *Videos*: strip plot + table (cross-filtered by brush); type and date filters.
  - *Intelligence*: insight cards per layer (topic, packaging, hook/script, editing) with evidence badge, confidence, counter-evidence and falsification condition; `NOT_AVAILABLE` cards say why.
  - *Strategy*: action groups (CONTINUE … STOP) as labeled lists; benchmark small multiples vs peer.
  - *Plans*: plan cards → S7.
  - *Coverage*: one-row layer heatmap + gaps list.
- **Acceptance**: no tab shows a figure without a source; health channels show the medical-validation flag on Intelligence and Plans.

### S5 Video page (M1, forensics M2)
- **Data**: thumbnail, title, publish date, duration, type, views/likes/comments snapshots (as of each), multiple of channel median, transcript (with source label), hook (first ~30 s), classifications (topic = AI reading, format = verified), finance audit link, forensic ledger, sources panel.
- **Layout**: two columns (media + facts | transcript/hook); tabs Overview · Transcript · Forensics · Sources.
- **Forensics tab**: horizontal timeline over the duration (shots, text cards, events) with a scrubber; frames load only if the local media library (#41) resolves them, otherwise "Media is local only on Mac A".
- **Acceptance**: a placeholder transcript is never shown as real; seal status is visible when a ledger exists.

### S6 Compare (M2)
- **Purpose**: 2-4 channels or videos side by side. **Charts**: small multiples sharing one y-scale per metric; dumbbell for period-over-period; aligned stat tiles.
- **Guard**: shows sample size and the "2 channels per niche" calibration warning when the strategy engine is the source.
- **Acceptance**: never a dual-axis chart; entity colors stay fixed when one is removed.

### S7 Plan document (M1)
- **Data**: plan JSON: opportunity (angle, confidence, evidence, counter-evidence, falsification), packaging (title hypotheses, thumbnail concepts), hook, script blueprint, editing (or NOT_AVAILABLE), coherence (11 dims), unavailable metrics, framework block (if present), slop-gate result (if a script exists).
- **Layout**: document-style reading column, stage stepper on the left, a coherence strip at the top (11 cells, status scale + icon).
- **Actions**: export MD/PDF (M1); "copy agent prompt" (M3).
- **Acceptance**: a plan without a `reference_framework` block is labeled "not framework-guided" (AGENTS.md).

### S8 Plans index (M1)
- Table of all plans: channel, opportunity, confidence, framework-guided yes/no, slop verdict, date.

### S9 Workstreams (M1) and Workstream page (M2)
- **Index**: meter list (Finance 558/1,612; reanalysis 26/558; CF 19/20; xkcd 29/91; Senior Health reports 6). Each row shows its next blocker.
- **Page**: progress over time (line), queue table with status chips, blockers list, pinned evidence branch/commit (as a link to GitHub).
- **M3**: review queue: "Mark reviewed" writes a HUMAN_INTERPRETATION record with reviewer and date (CANONICAL_MUTATION tier, explicit confirm).

### S10 Knowledge (M2)
- Rules grouped by rule class (creative heuristic, owner preference, platform claim, empirical hypothesis, tool-specific, superseded), each with its class badge and conflicts; section reader with FTS search; "videos assessed against this rule" list.
- **Acceptance**: no rule is styled or worded as a platform fact.

### S11 Evidence Library (M2)
- Datasets table (class, status, validator result) → dataset page → files (faceted by disposition; TOOLING/NOISE hidden by default) → file record (hash, path, duplicates).
- Seal verification table (PASS/FAIL), evidence map (local-only flags).

### S12 System (M2)
- Freshness table (stale first), coverage matrix heatmap (75 × 8 capabilities), acquisition costs (stat tiles + run table), read-model build info (source hashes, build time).
- **M3**: "Dry-run refresh" (SAFE_DERIVED tier, confirm).

### S13 Search results (M1)
- Grouped: Channels · Videos · Transcript matches (highlighted snippet + timestamp if available) · Rules. Keyboard: `/` focuses, arrows move, Enter opens.

### S14 My Channel (M3, only when first-party data exists)
- KPI row + one-axis line charts; competitor median as context lines in gray. Local only; a banner states that this data never leaves the machine.

---

## Wireframes (low fidelity)

**S1 Home, desktop**
```text
┌────┬──────────────────────────────────────────────────────────────────┐
│ ⌂  │ Home                                   [ / Search everything   ] │
│ ⌕  ├──────────────┬──────────────┬──────────────┬────────────────────┤
│ ⇄  │ 10,553 videos│ 300+ channels│ 8,000+ trans.│ 6 plans            │
│ ▤  │ as of 17 Nov │ 4 niches     │ 2 sources    │ 1 framework-guided │
│ ◎  ├──────────────┴──────────────┴──────────────┴────────────────────┤
│    │ Workstreams                                                      │
│    │ Finance audit     ███████░░░░░░░░  558 / 1,612  next: NICK_279   │
│    │ Casual Finance    ██████████████░  19 / 20      next: 1 video    │
│    │ xkcd What If      █████░░░░░░░░░░  29 / 91      blocked: media   │
│    ├──────────────────────────────────────┬──────────────────────────┤
│    │ Insights (last 90 days)              │ Needs attention          │
│    │ [thumb] 38× median · Metabolic …  ◇  │ ⚠ 4 seals fail verify    │
│    │ [thumb] 12× median · Dr. Okoro …  ■  │ ⚠ 843 MB local-only      │
│    │ [thumb]  9× median · Matty …      ■  │ ⓘ 3 artifacts stale      │
└────┴──────────────────────────────────────┴──────────────────────────┘
```
Figures in this wireframe are placeholders for layout only. Real numbers come from the read model.

**S4 Channel page, Videos tab, desktop**
```text
Home / Senior Health / Dr. Okoro
┌──────────────────────────────────────────────────────────────────────┐
│ Dr. Okoro  @handle · Senior Health · 66 videos · Seen in 3 sources   │
│ [Overview] [Videos] [Intelligence] [Strategy] [Plans] [Coverage]     │
├──────────────────────────────────────────────────────────────────────┤
│ [Long-form ▾] [Last 24 mo ▾] [Evidence: all ▾]            [⊞ table]  │
│ views (log)   ●                                                      │
│      ·  ·  ·· ● ·· ·  · ···  ·  ··· ·  ── median ──  · · ·           │
│   ═══════[ brushed range ]═══════                                    │
├──────────────────────────────────────────────────────────────────────┤
│ Title                         Published  Views   × median  Evidence  │
│ …                             2026-05-02 1.2M    38×       ■ source  │
└──────────────────────────────────────────────────────────────────────┘
```

**S5 Video page, phone**
```text
┌───────────────────────┐
│ ‹ Dr. Okoro           │
│ [ thumbnail 16:9    ] │
│ Title …               │
│ 1.2M views · 38× med. │
│ as of 11 Nov ■ source │
│ [Overview|Transcript| │
│  Forensics|Sources]   │
│ Hook (first 30 s)     │
│ "…"  Machine transcr. │
│ Seen in: Registry ·   │
│ SH core               │
├───────────────────────┤
│ ⌂   ⌕   ▤   ☰         │
└───────────────────────┘
```
