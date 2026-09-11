# Data Entry Workflow

The current Phase 1 workflow is intentionally simple:

1. User provides dataset.
2. Preserve original.
3. Inspect dataset.
4. Inventory files.
5. Calculate basic file statistics.
6. Detect exact duplicates.
7. Determine semantic role.
8. Record findings.
9. Ask for clarification only when genuinely necessary.
10. Do not perform premature full-system processing.

## Handling rules

All newly supplied material enters through `data/raw/inbox/`. Raw source files are evidence and must never be modified, rewritten, compressed, renamed destructively, or replaced by AI-generated interpretations.

Classify a file using both its physical format and its semantic role. A ZIP archive, Markdown document, image, or spreadsheet may serve many different evidentiary purposes; extension alone never determines intelligence value. If the semantic role is uncertain, retain the material as Unknown / Uncategorized until evidence or user clarification resolves it.

Derived outputs must move forward through the layers without changing the source:

```text
RAW
↓
EXTRACTED
↓
NORMALIZED
↓
INTELLIGENCE
```

Later phases may expand this workflow only through explicit architectural decisions.

## Incremental intelligence refresh

After canonical ingestion and classification:

1. Preview stale downstream layers: `.venv/bin/python -B scripts/plan_intelligence_refresh.py --channel CH-000005`.
2. For a reviewed change category, preview execution: `.venv/bin/python -B scripts/refresh_youtube_intelligence.py --channel CH-000005 --simulate-change NEW_TRANSCRIPT --dry-run`.
3. Run the same command without `--dry-run`.
4. Review the versioned report in `data/intelligence/system/refresh-runs/` and any successor artifacts.
5. Run tests and SQLite integrity checks, then commit only scoped changes.

Freshness uses canonical IDs, DB values, source hashes, generator hashes, and upstream artifact hashes. File modification times are ignored. Refresh never acquires evidence, calls network services, classifies content, mutates the catalog, or overwrites historical intelligence. First-party Analytics ingestion is a separate explicit file import described in `docs/FIRST_PARTY_ANALYTICS_WORKFLOW.md`. Rebuild the baseline registry explicitly with `scripts/plan_intelligence_refresh.py --write-registry` only after verified current artifacts are accepted.
