# MonkeyExplains1999 Finance expansion — 2026-10-21

This is a derived, versioned classification layer over the committed public
metadata in PR #38 (`f176aa2861cd93913b977e6159a4e00f4eabeacc`). It does not
merge PR #38, repeat acquisition, or import restricted records.

## Reconciled population

- Full-channel public source collection: 76 unique videos (61 regular and 15
  Shorts), preserved in `FULL_CHANNEL_SOURCE.csv`.
- Restricted source references excluded from the public collection: 45.
- Individually classified as Finance/Economics eligible from actual title and
  description: 63.
- Excluded as unrelated to Finance/Economics: 13. They remain registered in the
  full-channel source and the 76-row crosswalk.
- Exact duplicates against the frozen 966 or existing 197 additions: 0.
- New unique Finance additions: 63.
- Combined unique research population: 966 + 197 + 63 = 1,226.

All 63 additions are `METADATA_ONLY_NOT_DEEP_AUDITED`. Metadata eligibility is
not a transcript review, factual audit, visual review, or performance analysis.
The prior 966 and 197 collections remain unchanged.

## Files

- `FULL_CHANNEL_SOURCE.csv`: all 76 public PR #38 records.
- `FINANCE_INCLUSION_CROSSWALK.csv`: one title/description decision per public
  Video ID, including the 13 exclusions.
- `FINANCE_EXPANSION_MASTER.csv`: the 63 eligible unique additions.
- `DUPLICATE_OVERLAP_WITH_PRIOR_POPULATION.csv`: header-only because overlap is
  zero.
- `CHANNEL_CLASSIFICATION_SUMMARY.csv`: channel and disposition totals.
- `SOURCE_PROVENANCE.json`, `EXPANSION_VALIDATION.json`, and
  `FILE_CHECKSUMS_SHA256.json`: authority, reconciliation, and file integrity.

Rebuild derived files with `python3 build_monkey_expansion.py` from the parent
directory. `--import-source` is only for rematerializing the tracked public CSV
from the immutable PR #38 commit. It uses `git show`; it does not access YouTube
or a paid service.
