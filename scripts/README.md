# Scripts

This directory contains small, transparent inventory, ingestion, registration, verification, and read-only reporting utilities justified by real datasets.

`apify_youtube_ingest.py` is the Phase 1D bounded adapter for `streamers/youtube-scraper`. `plan` computes the result/cost ceiling without a network call. `run` reads `APIFY_TOKEN` from the environment, invokes one exact channel target, validates and deduplicates results, reconciles identity, and transactionally registers append-only snapshots/provenance. `reconcile-cost` records a finalized charged-event ledger without running another Actor.

`classify_content_pilot.py` preserves the five-item Phase 2 pilot and runs controlled manifest batches with `--manifest`, `--batch-size`, and `--dry-run`. Its controlled formats are `SHORT_FORM` / `LONG_FORM`, derived from duration (`SHORT_FORM` is at most 180 seconds). Topic rows are proposed, non-reproducible `AI_INTERPRETATION`; format rows are verified, reproducible `MEASURED_FACT`.

## Controlled content-topic vocabulary

| Label | Definition | Include | Exclude / boundary |
| --- | --- | --- | --- |
| `BUSINESS_ECONOMICS` | Economics and operating models of businesses or industries. | Revenue, costs, capital needs, risk, unit economics, and ownership of a business. | Household money management belongs in `PERSONAL_FINANCE`; retirement-centered decisions belong in `RETIREMENT_PLANNING`. |
| `CARDIOVASCULAR_HEALTH` | Health of the heart and circulatory system. | Blood pressure, heart disease, circulation, cardiovascular risk, and cardiovascular medication. | General older-adult function belongs in `HEALTHY_AGING`; blood-sugar or insulin-centered material belongs in `METABOLIC_HEALTH`. |
| `HEALTHY_AGING` | Health, function, independence, and longevity in older adults. | Age-related mobility, strength, balance, cognition, and broadly framed senior health. | Use a specific health label when cardiovascular or metabolic health is the primary subject; retirement finance belongs in `RETIREMENT_PLANNING`. |
| `METABOLIC_HEALTH` | Regulation of blood sugar, insulin, and related metabolic conditions. | Diabetes, prediabetes, glycemic response, insulin resistance, and nutrition primarily discussed through metabolic effects. | Cardiovascular-first material belongs in `CARDIOVASCULAR_HEALTH`; general older-adult function belongs in `HEALTHY_AGING`. |
| `PERSONAL_FINANCE` | Money management for individuals or households outside a retirement-first frame. | Budgeting, saving, debt, consumer spending, and general personal investing. | Retirement-centered planning belongs in `RETIREMENT_PLANNING`; business or industry operating economics belongs in `BUSINESS_ECONOMICS`. |
| `RETIREMENT_PLANNING` | Financial and lifestyle preparation for or management of retirement. | Retirement portfolios, withdrawals, Social Security, retirement spending, and retirement lifestyle decisions. | General household finance without a retirement focus belongs in `PERSONAL_FINANCE`; senior health belongs in the applicable health topic. |
| `SCIENCE_HYPOTHETICALS` | Scientific reasoning applied to an explicit counterfactual, feasibility, or scale scenario. | “What if” questions and imagined conditions whose consequences are worked out scientifically. | Direct explanations of real phenomena or concepts belong in `STEM_EXPLANATIONS`. |
| `STEM_EXPLANATIONS` | Direct explanations of real scientific, technical, engineering, or mathematical phenomena and concepts. | Factual “how” or “why” explanations, demonstrations, and concept-focused problem solving. | Explicit counterfactual or imagined scenarios belong in `SCIENCE_HYPOTHETICALS`; clinical guidance belongs in the applicable health topic. |
