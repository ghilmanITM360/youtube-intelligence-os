# Funded Master-Channel Extraction Plan

**Goal:** Extract, package, validate, commit, push, and remote-verify the maximum number of complete remaining channel catalogs while keeping normal extraction spend at or below $2.50 and leaving at least $0.30 of the authenticated $2.80 balance unused.

**Source of truth:** Repository evidence, canonical YouTube channel IDs, authenticated Apify Console, and immutable `streamers/youtube-scraper` outputs.

## Budget decision

- Authenticated plan: Free, no discount.
- Authenticated usage: $2.20 of $5.00; available balance $2.80.
- Authenticated Actor event price: $4.00 per 1,000 videos written to the dataset.
- Conservative estimate: public uploads plus two channel/about records per channel, because DS-000021 actual billing matched all 238 dataset results.
- Thirteen smallest catalogs: 600 uploads, 626 expected results, $2.504. Rejected because it exceeds the $2.50 normal-extraction cap.
- Approved allocation: twelve smallest catalogs, 518 uploads, 542 expected results, $2.168. Expected unused balance: $0.632.

## Deterministic batches

1. `DS-000023`: Maximus, The Life Outline, Bro Pump, Crayon Capital, Zoozle. Expected 110 videos, 120 results, $0.480.
2. `DS-000024`: Hypothetically, Brimm., Lost Legacy, ago. Expected 178 videos, 186 results, $0.744.
3. `DS-000025`: Stickly, Mack, Explain In Paint. Expected 230 videos, 236 results, $0.944.

## Per-batch procedure

1. Re-read authenticated current balance.
2. Confirm expected complete-catalog count, estimated cost, cumulative cost, and reserve.
3. Save exact Actor input before launch.
4. Run `streamers/youtube-scraper` without paid add-ons.
5. Save run metadata, dataset ID, exact input, full run log, and untouched dataset JSON.
6. Reconcile canonical channel IDs and every public video ID. Preserve about/non-video records.
7. If transcripts are missing, perform targeted recovery only for affected URLs, preserve evidence, then use verified placeholders only when unavailable.
8. Generate combined JSON/CSV/XLSX, five-sheet channel workbooks, transcript ZIPs, summaries, overlap report, manifests, source ledger, and checksums.
9. Validate IDs, ZIPs, workbooks, formulas, hyperlinks, hashes, descriptions, duplicates, credentials, and repository tests.
10. Commit dataset, push `main`, and verify local/upstream/remote SHAs before next batch.

## Stop rules

- Do not start a batch unless its complete expected catalog fits while preserving at least $0.30.
- Stop if actual cost/count drift makes the next complete batch unsafe.
- Do not buy credits, upgrade plans, or enable paid transcript/AI/date add-ons.
- Do not modify DS-000020, DS-000021, or DS-000022.
