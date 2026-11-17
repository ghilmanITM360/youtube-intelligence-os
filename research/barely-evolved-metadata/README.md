# BarelyEvolved public metadata snapshot

This directory contains a reproducible, point-in-time public metadata capture for YouTube channel `UCH59TmQhPOPhC3M17jCWpRQ` (`@BarelyEvolved`). The deduplicated master reconciles four accessible public videos to the channel-reported total at `2026-10-20T12:04:12.774Z`.

## Rebuild

From the repository root, with the workspace-provided `@oai/artifact-tool` available:

```bash
node research/barely-evolved-metadata/build_dataset.mjs
```

The builder reads only the immutable captures under `source/raw/`, regenerates normalized JSONL/CSV, validation and provenance records, and exports the seven-sheet workbook. It also recalculates formulas, scans for spreadsheet errors, and renders every sheet to `/tmp/yios-barely-evolved-previews` for visual inspection.

## Boundaries

- The source is the public `streamers/youtube-scraper` actor, build `0.0.318`; transcript, AI-summary, and video-download add-ons were disabled.
- The pilot and full run cost `$0.004` and `$0.024` respectively. No paid overage was used.
- Public metrics are snapshot observations, not private analytics or historical time series.
- Three of four video IDs have independently proven local media files in the private local-channel library; `4X3xd3MDZro` is not locally present.
- Title/description topic review classifies all four records outside Finance/Economics with HIGH confidence. This does not change the immutable 966 baseline or the separate 197-video Finance expansion.
- Raw video bytes, thumbnails, and transcripts are not included in this branch.
- Native Microsoft Excel recalculation is untested; workbook formulas were recalculated and checked with the repository's artifact-tool workflow.
