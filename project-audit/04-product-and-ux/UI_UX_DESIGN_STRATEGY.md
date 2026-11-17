# UI/UX Design Strategy

## 1. Design stance

YIOS's product is **trustworthy knowledge**. The interface should feel like a calm research desk, not a marketing dashboard: few colors, generous whitespace, strong typography, and evidence visible on demand. Visual delight comes from clarity (well-made charts, thumbnails, timelines), not decoration.

## 2. Principles (ranked)

1. **Show certainty, not just values.** Every insight carries an evidence badge and an as-of date. Distinguishing fact from AI reading is the product's core value proposition; flattening them defeats it.
2. **Absence is information.** Designed empty states explain what is missing and why.
3. **Overview first, detail on demand** (Shneiderman's mantra; NN/g progressive disclosure). Four layers: Home → category → entity page → record/provenance.
4. **Plain language.** Internal IDs and status codes are secondary text.
5. **Every screen is a link.** URL state for filters, tabs and selection, so the owner can hand a view to an agent.
6. **Read-only first.** No action that mutates evidence in the first milestones. Later actions get explicit confirmation tiers (READ_ONLY → SAFE_DERIVED → CANONICAL_MUTATION → EXTERNAL, from the 2026-09-11 handoff).
7. **Never imply capabilities that do not exist**: no "publish to YouTube", no CTR/retention for competitors, no "AI-generated script" buttons.
8. **Accessible by default**: WCAG 2.2 AA, keyboard complete, every chart has a table view.

## 3. Layout model

| Breakpoint | Layout |
|---|---|
| ≥ 1200 px (desktop, primary) | left navigation rail + content + optional right detail panel (list/detail split) |
| 768-1199 px (tablet) | collapsible rail; detail panel becomes an overlay sheet |
| < 768 px (phone) | bottom bar with 4 items (Home, Explore, Plans, Search); entity pages become stacked sections; charts switch to compact forms (sparklines, ranked lists); tables become card lists |

## 4. Interaction patterns

| Pattern | Use |
|---|---|
| Filter chips row | niche, date range, video type, evidence layer, status |
| Compare tray | select up to 4 channels/videos from anywhere; persistent bottom tray |
| Provenance drawer | ⓘ beside any value opens source, method, layer, date |
| Hover/focus tooltip | every chart mark; also reachable via keyboard |
| Brush to filter | time-series and strip plots filter the table below (cross-filter) |
| Toggle chart ↔ table | on every chart card |
| Export | MD/CSV per view; PDF for plans (keeps the owner's existing report habit) |
| Status chips | fixed vocabulary, icon + label + tooltip definition |

## 5. Tone and copy

Short, declarative and specific: "12 of 75 channels have transcripts with placeholders", not "Some data may be incomplete". Bilingual readiness (English UI; copy kept in one strings file) because the owner works in English and Urdu.

## 6. What success looks like (acceptance for the whole UX)

- A first-time user answers "which Senior Health videos broke out last year and why might they have?" in ≤ 4 clicks without help.
- Every number on screen can reach its source in ≤ 2 clicks.
- No screen shows a value without an evidence state.
- Lighthouse accessibility ≥ 95; axe-core 0 serious violations; full keyboard path through primary flows.
