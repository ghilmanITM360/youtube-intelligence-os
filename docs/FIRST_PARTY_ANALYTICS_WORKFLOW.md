# First-Party YouTube Analytics Workflow

This workflow imports aggregate YouTube Studio or Advanced Mode exports from local CSV, TSV, or XLSX files. It does not call the YouTube API, crawl YouTube, or accept viewer-level personal data.

## Import

1. Export an aggregate report from YouTube Studio.
2. Identify the canonical owned channel ID. Ownership must be asserted explicitly; ambiguous ownership stops the import.
3. Run:

```bash
.venv/bin/python -B scripts/ingest_youtube_analytics.py \
  --source /absolute/path/to/report.csv \
  --channel CH-000000 \
  --ownership FIRST_PARTY \
  --observation-start 2026-08-01 \
  --observation-end 2026-08-31 \
  --date-range-kind CUSTOM_RANGE \
  --export-date 2026-09-11
```

The importer copies source bytes into the immutable raw inbox and writes a normalized, versioned private artifact plus a concise validation report. Both private trees are gitignored. Exact reimports return `EXACT_DUPLICATE`; existing snapshots are never overwritten.

Unknown columns remain in each normalized row as `UNMAPPED_SOURCE_FIELDS`. Unknown localized headers are not guessed. Rows that cannot be matched safely to a canonical video are reported as `AMBIGUOUS` or `UNMATCHED` and their video metrics are rejected.

## Diagnose

Run the diagnosis only after reviewing the import validation report:

```bash
.venv/bin/python -B scripts/report_first_party_channel_diagnosis.py \
  --analytics /absolute/path/to/private-normalized.json \
  --competitor CH-000000
```

The report combines own public context, first-party metrics, selected competitors' public-only context, training heuristics, and official platform guardrails. CTR is compared only inside equal channel, format, and date-range cohorts. Retention findings are associations, not causal rules. No unified engagement score is produced.

## Refresh

Preview downstream impact:

```bash
.venv/bin/python -B scripts/refresh_youtube_intelligence.py \
  --channel CH-000000 \
  --simulate-change NEW_FIRST_PARTY_ANALYTICS \
  --dry-run
```

After review, run the same command without `--dry-run`. Refresh reads registered private normalized artifacts, preserves prior diagnosis versions, and does not modify raw evidence or the canonical catalog.

## Date discipline

Use `LIFETIME`, `FIRST_24H`, `FIRST_7D`, `FIRST_28D`, `CUSTOM_RANGE`, `ROLLING_28D`, `OTHER`, or `UNKNOWN`. Do not compare unequal or overlapping windows as if they were equivalent. One compatible snapshot yields `LONGITUDINAL_FIRST_PARTY_TREND=NOT_AVAILABLE`.
