# Platform Selection Report

## Recommendation: **Option A, a responsive web application that runs locally** (served on `localhost` from the owner's Mac), designed desktop-first, with a phone layout for checking progress and reading plans.

Not native mobile. Not both.

## Evaluation

| Factor | Evidence from the audit | Web (A) | Mobile (B) | Both (C) |
|---|---|---|---|---|
| Users | 1 owner + reviewers + agents; work happens on two Macs | ✔ fits | ✘ wrong primary device | over-serves |
| Workflows | research reading, comparing, provenance drill-down, export to agents | ✔ wide screens, multi-panel | ✘ cramped | — |
| Data complexity | 7 stores, 10,553 videos, 45,774 files, 75×8 coverage grid, forensic timelines | ✔ tables, heatmaps, split view | partial: needs redesign into lists | double design cost |
| Chart interaction | brushing, cross-filter, hover, timelines | ✔ pointer + keyboard | touch only, limited | — |
| Offline / privacy | first-party analytics must stay local; heavy media is local only (~15 GB) | ✔ localhost reads local files directly | ✘ media not on phone; sync would breach the local-only rule | sync problem |
| Device capabilities needed | none (no camera, GPS, push) | ✔ | no advantage | — |
| Performance | local SQLite read model, sub-second | ✔ | needs a server + network anyway | — |
| Accessibility | WCAG 2.2 AA achievable with semantic HTML | ✔ mature tooling (axe, Playwright) | platform-specific work | 2× |
| Maintenance | one owner, AI agents write code; Python-first repo | ✔ one codebase | Swift/Kotlin or RN toolchain, app-store overhead | highest |
| Scalability | future multi-channel growth | ✔ add screens | — | — |

## Device plan

| Device | Role | Design |
|---|---|---|
| Desktop/laptop (primary) | full exploration, compare, review | nav rail + list/detail split |
| Tablet | reading plans, browsing | collapsible rail, sheets |
| Phone (same web app, LAN or later a private tunnel) | glance at progress, read a plan, search | bottom bar; dense views redesigned (strip plot → sparkline + top-5 list; tables → cards; heatmap → per-channel row) |

Remote phone access is **not** in scope until there is an auth decision. Exposing the local server beyond the machine needs authentication and an owner privacy decision first.

## Revisit triggers

Revisit native mobile only if (a) a team of non-owner users needs on-the-go access, or (b) on-device capture (recording, photos) becomes part of the workflow.
