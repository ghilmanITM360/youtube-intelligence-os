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
