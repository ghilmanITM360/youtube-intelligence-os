# Design System Plan

Small and native-first: CSS custom properties for tokens, semantic HTML, a minimal component set. No component library is required for M1; adopt one only if a measured need appears (see PROPOSED_TECHNICAL_ARCHITECTURE.md).

## 1. Tokens

| Group | Tokens |
|---|---|
| Color: surfaces | `--surface`, `--surface-raised`, `--surface-sunken`, `--border` (light and dark sets, under `prefers-color-scheme` and `[data-theme]`) |
| Color: ink | `--ink-primary`, `--ink-secondary`, `--ink-muted` (text never uses series colors) |
| Color: accent | one brand accent for links/focus/selection |
| Color: data | categorical theme (fixed order, max 8), one sequential ramp, one diverging pair + neutral midpoint. **Validate with the dataviz validator** in light and dark before shipping |
| Color: status (reserved) | good / warning / serious / critical: always with icon + label |
| Evidence layers | not colors: a **badge shape + label** set (From source ■, Measured ◆, Observation ●, AI reading ◇ dashed outline, Idea to test △, Suspect ⚠). Color is a secondary cue only |
| Type | system UI sans for UI; tabular numerals for figures; scale 12/14/16/20/24/32/48 (hero) |
| Space | 4-px base: 4, 8, 12, 16, 24, 32, 48 |
| Radius | 4 (controls, bar ends), 8 (cards) |
| Motion | 150-200 ms ease-out for disclosure; respect `prefers-reduced-motion` |
| Focus | 2-px accent outline + 2-px offset, always visible |

## 2. Components

| Component | Notes |
|---|---|
| App shell | nav rail / bottom bar, breadcrumbs, search box |
| Stat tile, KPI row, hero figure | value + delta + optional sparkline; as-of caption |
| Meter, meter list | progress against a whole (workstreams) |
| Chart card | title, as-of, chart/table toggle, legend (≥ 2 series), export |
| Charts | strip/dot plot, column, line, ranked bar, heatmap, small multiples, dumbbell, timeline: one shared library wrapper |
| Data table | sortable, sticky header, virtualized, column chooser, row → detail |
| Filter chips row | dimension chips + date range (native `<input type="date">`) |
| Evidence badge | layer shape + label + tooltip definition |
| Status chip | fixed vocabulary, icon + label |
| Provenance drawer | source, run, method, layer, date, dataset link |
| Insight card | claim, evidence badge, confidence, counter-evidence (collapsed), falsification condition |
| Empty state | reason + what would fill it |
| Error state | what failed, which source, retry |
| Skeleton loaders | per card |
| Compare tray | up to 4 items |
| Dialog / confirm | only for M3 mutating actions; states the tier and the exact effect |
| Toast | non-blocking confirmations |
| Thumbnail grid + lightbox | lazy-loaded, alt text = video title |
| Transcript reader | search-in-text, source label, timestamp anchors |

## 3. Accessibility checklist (WCAG 2.2 AA)

Text contrast 4.5:1 (3:1 large/UI); non-text contrast 3:1 for chart marks and focus; no information by color alone (1.4.1); every chart has a table and an `aria-label` summary; keyboard access to chart marks (roving tabindex) with tooltips on focus; target size ≥ 24 px (2.5.8); focus not obscured by the sticky tray (2.4.11); reflow at 320 px (1.4.10); `forced-colors` support (texture fill for series); reduced motion.

## 4. Governance

Tokens in one CSS file; components documented on one "kitchen sink" page rendered from real read-model data (doubles as the visual regression fixture).
