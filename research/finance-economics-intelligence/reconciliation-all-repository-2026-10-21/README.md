# Repository-wide Finance/Economics universe — 2026-10-21

This versioned derived layer reconciles every enumerated Finance/Economics video
corpus already committed in the repository or an existing committed research
branch. It does not change the frozen 966, the 197-video expansion, or the
63-video MonkeyExplains expansion.

## Result

- Prior population: **1,226** unique Video IDs (966 + 197 + 63).
- Newly synchronized: **386** unique Video IDs: 180 from the six-channel
  `LANDSCAPE_VIDEOS.csv` snapshot and 206 from Casually Finance
  `VIDEO_PERFORMANCE.csv` at immutable commit
  `fb1e56d03e5ad53086c74247cd2972b262d09b78`.
- Exact overlap among all five layers: **0** for the new sources; combined
  population: **1,612** unique Video IDs.
- After the consecutive `NICK_154` audit, deep-complete is **430** original
  videos. All 386 additions are `METADATA_ONLY_NOT_DEEP_AUDITED`; total
  remaining workload is **1,182**.
- The 10 MEDIUM-confidence MonkeyExplains inclusions were reread from their
  actual titles and descriptions. Their inclusion remains reasonable, but no
  transcript is registered, so confidence was not silently upgraded.

## Files

- `FINANCE_UNIVERSE.csv`: authoritative combined per-Video-ID index with
  identity, URL, provenance, evidence availability, decision, audit state and
  blocker.
- `NEW_ELIGIBLE_ADDITIONS.csv`: the 386 additions beyond 1,226.
- `CHANNEL_DIRECTORY.csv`: 42 identified Finance/Economics channels: 27 with
  included video datasets, five with fully classified but excluded datasets,
  and ten `IDENTITY_ONLY_NEEDS_DATA` channels.
- `MONKEY_MEDIUM_CONFIDENCE_REVIEW.csv`: bounded evidence review of the 10
  uncertain inclusions.
- `VALIDATION.json` and `FILE_CHECKSUMS_SHA256.json`: counts, source pins and
  reproducibility hashes.

Rebuild with `python3 build_repository_finance_universe.py` from the parent
directory. The builder reads immutable source ledgers and uses `git show` for
the pinned Casually Finance branch artifact. It performs no network access.

The six landscape datasets are first-page snapshots, not complete channel
catalogues. Identity-only channels require a supplied repository dataset before
any video can be counted. No absent record is inferred.
