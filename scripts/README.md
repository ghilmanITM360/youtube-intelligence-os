# Scripts

This directory contains small, transparent inventory, ingestion, registration, verification, and read-only reporting utilities justified by real datasets.

`apify_youtube_ingest.py` is the Phase 1D bounded adapter for `streamers/youtube-scraper`. `plan` computes the result/cost ceiling without a network call. `run` reads `APIFY_TOKEN` from the environment, invokes one exact channel target, validates and deduplicates results, reconciles identity, and transactionally registers append-only snapshots/provenance. `reconcile-cost` records a finalized charged-event ledger without running another Actor.
